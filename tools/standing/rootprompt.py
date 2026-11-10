# -*- coding: utf-8 -*-
"""standing/rootprompt.py -- v1.10.0, (R340)(2)(vii): THE ROOT'S PROMPT COMPOSED FROM THE BANKS WITH THE ACT'S OWN OBJECTS; the route carried since b714 retired (b729 event (7)).

The prompt's words are the seat's, in a bank of rows; its figures are not typed: a row is a list of parts, a part a literal string or a cite [bank, line, token], and the
composer prints the token only when the token stands on that line of that bank, and refuses the prompt where one does not. So a prompt cannot carry a figure its bank does not.

  data/<act>_rootprompt_rows.json = {"questions": [{"header": ..., "rows": [[part, ...], ...]}]}
  compose(rows, read) -> text        read(bank, line) -> the line's text, or None; a row's parts joined, the rows joined by one space; SystemExit naming every stale cite
  stale(rows, read) -> [(bank, line, token)]
  ceiling(scores, tracked_at_lock, act, modified) -> (held, of, line)   v1.14.0, (R344)(2)(ii): the ceiling computed as a dry score, never typed: every score that reads REFUTED now, and N4 when a path the suite writes
                                     stood tracked at the lock (the suite's run will read as an edit) or a tracked bank differs from the lock's; PENDING counted as it may yet hold
  rows_from(text, read) -> rows      a text as put, split into rows at its sentences, every number before a cite on the sentence, found on the cited line, turned into a cite
  entry_unbacked(text, entry) -> [sentences]   v1.17.0, (R347)(2)(v), b736 events (5): a sentence of the prompt about the entry stands only as the sealed composer's
                                     own words (a quoted span found in the composed entry) or as procedure ("as composed"); a sentence promising what the entry
                                     names, written ahead of the composer, is returned, and compose_checked refuses the prompt on it
  compose_checked(rows, read, entry) -> text   compose(), then entry_unbacked() on its text, SystemExit naming each unbacked sentence
  remote_clause / remote_unbacked / remote_read   v1.23.0, (R353)(3)(i), b742 events (3): the remote figures read from the remote by the composer's caller at prompt time
                                     ("remote at <sha>; local <n> commits past it"); a clause naming a commit as pushed that is no remote head refuses the prompt
  put / put_check / put_fault   v1.31.0, (R361)(3)(iii): every prompt (sitting items, halts, root) through check_hand before it is put, banked once as
                                     data/<act>_put_<k>.json; the hook refuses an AskUserQuestion no such bank carries
Pure in its arguments; nothing written -- except remote_read (the CLI `remote`), which reads the remote once and banks data/<act>_rootprompt_remote.json,
and put (the CLI `put`), which writes its one new bank.
"""
import re

ENTRY_WORD = re.compile(r'\bentry\b', re.I)
PROCEDURE = re.compile(r'\bas composed\b|\bthe entry and (?:the )?trail\b(?![^.]*\bnam)', re.I)
QUOTED = re.compile(r'[“"]([^”"]{8,})[”"]')

CITE = re.compile(r'\((?:relay )?(data/[\w.\-]+) :(\d+)(?:[,)\- ])')
TOKEN = re.compile(r'\d[\d,.]*\d|\d')


def ceiling(scores, tracked_at_lock, act, modified=()):
    """`modified`: the banks tracked at the lock whose blobs differ from the lock's at prompt time, less the banks the lock excludes by name."""
    import probes as PB
    v = dict((k, (x[0] if isinstance(x, (list, tuple)) else x)) for k, x in scores.items())
    lost = sorted(k for k, x in v.items() if str(x).startswith('REFUTED'))
    if (PB.outputs(act, tracked_at_lock) or modified) and 'N4' in v and 'N4' not in lost:
        lost = sorted(lost + ['N4'])
    return len(v) - len(lost), len(v), 'at most %d of %d (%s REFUTED, by the banks at prompt time)' % (len(v) - len(lost), len(v), ', '.join(lost) or 'none')


def ceiling_at_lock(scores, act, data=None, modified=()):
    """v1.26.0, (R356)(3)(ii): the ceiling with its lock read by the one reader (tools/standing/lockdate.py, the lock row's commit), not given by
    hand; returns (held, of, line, the lock commit)."""
    import lockdate as LD
    lc = LD.lock_of(act, data)
    if lc is None:
        raise SystemExit('### THE CEILING NOT COMPUTED: no lock row in data/%s_steps.json' % act)
    h, of, line = ceiling(scores, LD.tracked_at(lc, prefix='data/%s_' % act), act, modified)
    return h, of, line + ' ; the lock %s by the one reader' % lc[:8], lc


def _cites(rows):
    for row in rows:
        for part in row:
            if isinstance(part, (list, tuple)):
                yield part


def stale(rows, read):
    return [tuple(c) for c in _cites(rows) if str(c[2]) not in (read(c[0], int(c[1])) or '')]


def compose(rows, read):
    bad = stale(rows, read)
    if bad:
        raise SystemExit('### THE PROMPT NOT COMPOSED: %d FIGURE(S) NOT ON THEIR BANK LINES: %s' % (len(bad), bad))
    return ' '.join(''.join(str(p[2]) if isinstance(p, (list, tuple)) else p for p in row) for row in rows)


def _norm(s):
    return ' '.join((s or '').replace('`', '').replace('’', "'").split())


def entry_unbacked(text, entry):
    """the prompt's sentences about the entry that the composed entry does not back: each sentence naming the entry, less those whose every
    quoted span stands in the entry and those that are procedure alone (a clause carrying "as composed" and naming nothing the entry holds)."""
    ent = _norm(entry)
    out = []
    for sent in re.split(r'(?<=[.;:]) (?=\S)', text or ''):
        for cl in re.split(r'(?<=,) |; ', sent):
            if not ENTRY_WORD.search(cl):
                continue
            q = QUOTED.findall(cl)
            if q and all(_norm(x) in ent for x in q):
                continue
            if PROCEDURE.search(cl) and not re.search(r'\bnamed in the entry\b|\bthe entry (?:names|prints|carries|says|will)\b', cl, re.I):
                continue
            out.append(cl.strip())
    return out


REMOTE_WORD = re.compile(r'\b(?:pushed|remote|origin)\b', re.I)
HEX = re.compile(r'\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b')   # a letter required: a run id or a count (42068096322) is no commit


def remote_clause(name, remote, local, n):
    """v1.23.0, (R353)(3)(i): the prompt's remote figure, composed and never typed: "<name> remote at <sha8>; local <n> commits past it"."""
    if n == 0 or remote[:8] == local[:8]:
        return '%s remote at %s; local level with it' % (name, remote[:8])
    return '%s remote at %s; local %d commit%s past it' % (name, remote[:8], n, '' if n == 1 else 's')


def remote_unbacked(text, remotes):
    """v1.23.0, (R353)(3)(i), b742 events (3): every clause of the prompt naming the remote (pushed, remote, origin) and a commit that is not a
    remote head read at prompt time. `remotes`: {name: full sha read from the remote}. b742's "nothing past bce5605d pushed" is returned:
    bce5605d was a local commit, the relay's remote stood at 13498fd2."""
    heads = [str(h).lower() for h in (remotes or {}).values() if h]
    out = []
    for sent in re.split(r'(?<=[.;:]) (?=\S)', text or ''):
        for cl in re.split(r'(?<=,) |; ', sent):
            if not REMOTE_WORD.search(cl):
                continue
            for h in HEX.findall(cl.lower()):
                if not any(x.startswith(h) for x in heads):
                    out.append(cl.strip())
                    break
    return out


def compose_checked(rows, read, entry, remotes=None):
    """v1.23.0: `remotes` given (the dict remote_read banks), a clause naming a commit as pushed that is no remote head refuses the prompt;
    v1.17.0's callers, passing no remotes, are unchanged."""
    t = compose(rows, read)
    bad = entry_unbacked(t, entry)
    if bad:
        raise SystemExit('### THE PROMPT NOT COMPOSED: %d SENTENCE(S) ABOUT THE ENTRY NOT FROM THE SEALED COMPOSER: %s' % (len(bad), bad))
    if remotes is not None:
        bad = remote_unbacked(t, remotes)
        if bad:
            raise SystemExit('### THE PROMPT NOT COMPOSED: %d CLAUSE(S) NAMING A COMMIT AS ON THE REMOTE THAT NO REMOTE HEAD IS: %s' % (len(bad), bad))
    return t


def rows_from(text, read):
    rows = []
    for sent in re.split(r'(?<=[.:]) (?=[A-Z(`])', text):
        cites = [(m.group(1), int(m.group(2)), m.start()) for m in CITE.finditer(sent)]
        parts, at = [], 0
        for bank, line, end in cites:
            on = read(bank, line) or ''
            for m in TOKEN.finditer(sent, at, end):
                if m.group(0) in on:
                    parts += [sent[at:m.start()], [bank, line, m.group(0)]]
                    at = m.end()
        rows.append([p for p in parts + [sent[at:]] if p != ''])
    return rows


def check_hand(text, read, entry, remotes=None, options=None, clauses=None):
    """v1.27.0, (R357)(3)(ii), b746 events (7): a question written after the seal -- a halt's text, a conflict, any prompt beside the root's
    own -- run through compose_checked as the root's prompt is: its rows taken from its text (rows_from, every figure before a cite turned
    into a cite), composed and checked against the entry; SystemExit on any unbacked sentence or stale figure. The composed text must equal
    the text as written, or the question is refused: the check is of the words put, not of a reworded copy.
    v1.30.0, (R360)(3)(iii): `options` [(label, description)] and `clauses` {score: clause text} given (score_clauses of the ruling), every
    score an option's route would cost is named in the question or in that option, or the question is refused (costs_unnamed)."""
    t = compose_checked(rows_from(text, read), read, entry, remotes)
    if ' '.join(t.split()) != ' '.join(text.split()):
        raise SystemExit('### THE QUESTION NOT COMPOSED: THE COMPOSED TEXT DIFFERS FROM THE TEXT AS WRITTEN')
    if options is not None and clauses is not None:
        bad = costs_unnamed(text, options, clauses)
        if bad:
            raise SystemExit('### THE QUESTION NOT COMPOSED: %d COST(S) OF ITS ROUTES NOT NAMED: %s' % (
                len(bad), '; '.join('option %d (%s) costs %s on its clause "%s"' % (k, lab[:40], s, w) for k, lab, s, w in bad)))
    return t


# ================================================================================ v1.30.0, (R360)(3)(iii): A HALT QUESTION NAMES EVERY SCORE ITS ROUTES WOULD COST
# ### b749 events (5), (6): the second halt's first option (one Edit of the answers bank past row (65)) named the question count's overcount as
# ### its only cost, and N4 read REFUTED on its clause "edited by hand since" -- the seat's omission. The composer reads each option's route
# ### against the ruling's own score clauses: a route word (left) and the clause words it falls under (right); a score whose clause carries
# ### those words is a cost of the route, and must be named.
ROUTE_COSTS = (
    (r'(?i)\b(?:an?|one|the)\s+Edit\b|\bby hand\b|\blift(?:ed|s)?\s+the\s+hook\b|\bhand[- ]edit', r'(?i)\bby hand\b|\bedited after the lock\b'),
    (r'(?i)\brepair[- ]phase\b|\brepair commit\b', r'(?i)\brepair phase\b|\bedited after the lock\b'),
    (r'(?i)\bplain git\b|\bgit (?:commit|add|push)\b', r'(?i)\bone-call tool\b'),
    (r'(?i)\bdeposit|\bpublish|\bnew version\b|\bZenodo (?:call|request|write)', r'(?i)\bnothing deposits\b|\bno Zenodo call\b|\bno draft published\b'),
    (r'(?i)\bmerge\b', r'(?i)\bno branch merged\b'),
    (r'(?i)\btag (?:v\d|beyond|past)', r'(?i)\bno tag beyond\b'),
    (r'(?i)\bafter the root\b', r'(?i)\bafter the root\b'),
)
SCORE_HEAD = re.compile(r'\((N\d|S\d)\)\s')


def score_clauses(ruling):
    """{score: its clause text} from the ruling's NAVIGATOR'S EXPECTATIONS, each "(Nk) ..." to the next head."""
    t = ruling or ''
    i = t.find("THE NAVIGATOR'S EXPECTATIONS")
    t = t[i:] if i >= 0 else t
    heads = list(SCORE_HEAD.finditer(t))
    return dict((m.group(1), t[m.end():(heads[k + 1].start() if k + 1 < len(heads) else len(t))].split('FERRY END')[0].strip())
                for k, m in enumerate(heads))


def route_costs(route, clauses):
    """[(score, the clause words matched)] the route's words would cost, by ROUTE_COSTS against the clauses."""
    out = []
    for rw, cw in ROUTE_COSTS:
        if re.search(rw, route or ''):
            for s, c in sorted(clauses.items()):
                m = re.search(cw, c)
                if m and s not in [x[0] for x in out]:
                    out.append((s, m.group(0)))
    return out


def costs_unnamed(question, options, clauses):
    """[(option number, label, score, clause words)]: each cost of an option's route named neither in the question nor in that option."""
    out = []
    for k, (lab, desc) in enumerate(options, 1):
        for s, w in route_costs('%s %s' % (lab, desc), clauses):
            if not re.search(r'\b%s\b' % s, '%s %s %s' % (question, lab, desc)):
                out.append((k, lab, s, w))
    return out


def relay_reader(root='D:/relay'):
    """read(bank, line) over relay-relative paths ('data/...'), the path taken once; None for a line past the file's end. A bank that
    resolves to no file refuses, printing it (v1.27.0, (R357)(3)(vii))."""
    import os
    cache = {}

    def read(bank, line):
        p = os.path.join(root, bank)
        if p not in cache:
            if not os.path.isfile(p):
                raise SystemExit('### REFUSED: %s resolves to no file (%s)' % (bank, p))
            cache[p] = open(p, encoding='utf-8').read().replace('\r', '').split('\n')
        L = cache[p]
        return L[line - 1] if 1 <= line <= len(L) else None
    return read


# ================================================================================ v1.31.0, (R361)(3)(iii): EVERY PROMPT THROUGH THE COMPOSER
# ### b750's N3 read before the root: the sitting's third prompt carried "FINDINGS :14149, b746's entry, says ..." -- a sentence about an entry
# ### outside the composer -- because the sitting items were put by hand, the composer's check bound the root's prompt and the halts alone.
# ### Every prompt the act puts -- the sitting items, the halts and the root -- now runs through check_hand (compose_checked, every figure before
# ### a cite on its line, the costs of each option's route named) before it is put: `put` composes each question and each option's words, and
# ### banks the questions once as data/<act>_put_<k>.json (k the next free number, never rewritten); the hook refuses an AskUserQuestion whose
# ### questions no such bank carries (put_fault).
def _qnorm(q):
    opts = [(_norm(o.get('label')), _norm(o.get('description'))) for o in (q.get('options') or [])]
    return (_norm(q.get('question')), _norm(q.get('header')), tuple(opts))


def put_check(questions, read, entry, ruling, remotes=None):
    """each question checked as check_hand checks a hand question, its options' costs read against the ruling's score clauses; each option's
    words through entry_unbacked as well. Returns the composed question texts; SystemExit on the first fault, naming the question."""
    clauses = score_clauses(ruling)
    out = []
    for k, q in enumerate(questions, 1):
        opts = [(o.get('label') or '', o.get('description') or '') for o in (q.get('options') or [])]
        try:
            t = check_hand(q.get('question') or '', read, entry, remotes, opts, clauses)
        except SystemExit as e:
            raise SystemExit('### QUESTION %d (%s) REFUSED: %s' % (k, q.get('header') or '', e))
        for lab, desc in opts:
            bad = entry_unbacked('%s. %s' % (lab, desc), entry)
            if bad:
                raise SystemExit('### QUESTION %d (%s) REFUSED: AN OPTION`S WORDS ABOUT THE ENTRY NOT FROM THE SEALED COMPOSER: %s' % (k, q.get('header') or '', bad))
        out.append(t)
    return out


def put(act, questions, entry='', remotes=None, relay='D:/relay'):
    """check every question (put_check) and bank them as data/<act>_put_<k>.json; returns the bank's relay path."""
    import json
    import os
    import time
    fp = os.path.join(relay, 'data', '%s_ferry.txt' % act)
    ruling = open(fp, encoding='utf-8').read() if os.path.isfile(fp) else ''
    put_check(questions, relay_reader(relay), entry, ruling, remotes)
    k = 1
    while os.path.exists(os.path.join(relay, 'data', '%s_put_%d.json' % (act, k))):
        k += 1
    rel = 'data/%s_put_%d.json' % (act, k)
    j = dict(act=act, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), composed='check_hand over each question, entry_unbacked over each option',
             questions=questions)
    with open(os.path.join(relay, rel), 'x', encoding='utf-8', newline='\n') as fh:
        fh.write(json.dumps(j, indent=1, ensure_ascii=False) + '\n')
    return rel


def put_banks(act, relay='D:/relay'):
    import glob
    import json
    import os
    out = []
    for p in sorted(glob.glob(os.path.join(relay, 'data', '%s_put_*.json' % act))):
        try:
            out.append(json.load(open(p, encoding='utf-8')))
        except (OSError, ValueError):
            pass
    return out


def put_fault(act, questions, relay='D:/relay'):
    """None where every question of the call stands, as put (question, header and options), in one of the act's put banks; else the detail."""
    if not act:
        return None
    have = set(_qnorm(q) for b in put_banks(act, relay) for q in (b.get('questions') or []))
    miss = [q.get('header') or (q.get('question') or '')[:40] for q in (questions or []) if _qnorm(q) not in have]
    if miss:
        return ('a question put without the composer: %s -- compose and bank it first (python -X utf8 -u tools/standing/rootprompt.py put <act> <questions json> [<entry file>])'
                % ', '.join(miss))
    return None


REPOS = {'relay': 'D:/relay', 'pp': 'D:/MY-DOwnloads/PLACE-papers'}


def remote_read(repo, act):
    """v1.23.0, (R353)(3)(i): ONE remote read (git ls-remote origin refs/heads/main), the local main and the count between, banked to
    data/<act>_rootprompt_remote.json under the repo's key; returns the clause. The composer's caller passes the bank's heads as `remotes`."""
    import json
    import os
    import subprocess
    path = REPOS[repo]
    out = subprocess.run(['git', '-C', path, 'ls-remote', 'origin', 'refs/heads/main'], capture_output=True, text=True)
    if out.returncode != 0 or not out.stdout.strip():
        raise SystemExit('### THE REMOTE NOT READ (%s): exit %d %s' % (repo, out.returncode, out.stderr.strip()))
    remote = out.stdout.split()[0]
    local = subprocess.run(['git', '-C', path, 'rev-parse', 'refs/heads/main'], capture_output=True, text=True).stdout.strip()
    known = subprocess.run(['git', '-C', path, 'cat-file', '-e', remote + '^{commit}'], capture_output=True).returncode == 0
    n = int(subprocess.run(['git', '-C', path, 'rev-list', '--count', '%s..%s' % (remote, local)], capture_output=True, text=True).stdout.strip()) if known else -1
    name = 'relay' if repo == 'relay' else 'PLACE-papers'
    clause = remote_clause(name, remote, local, n) if n >= 0 else '%s remote at %s; not in the local store' % (name, remote[:8])
    bank = os.path.join('D:/relay', 'data', '%s_rootprompt_remote.json' % act)
    have = json.load(open(bank, encoding='utf-8')) if os.path.exists(bank) else {}
    have[repo] = {'remote': remote, 'local': local, 'past': n, 'clause': clause}
    text = json.dumps(have, indent=1, ensure_ascii=False) + '\n'
    with open(bank, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    return clause


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 4 and sys.argv[1] == 'remote' and sys.argv[2] in REPOS:
        print(remote_read(sys.argv[2], sys.argv[3]))
    elif len(sys.argv) == 4 and sys.argv[1] == 'hand':
        # ### v1.27.0: rootprompt.py hand <question file> <entry file>, both relay paths; prints the composed question or refuses
        import os
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        for p in sys.argv[2:4]:
            if not os.path.isfile(os.path.join('D:/relay', p)):
                raise SystemExit('### REFUSED: %s resolves to no file (%s)' % (p, os.path.join('D:/relay', p)))
        q = open(os.path.join('D:/relay', sys.argv[2]), encoding='utf-8').read().strip()
        e = open(os.path.join('D:/relay', sys.argv[3]), encoding='utf-8').read()
        print('THE QUESTION COMPOSED AND CHECKED:\n' + check_hand(q, relay_reader(), e))
    elif len(sys.argv) in (4, 5) and sys.argv[1] == 'put':
        # ### v1.31.0, (R361)(3)(iii): rootprompt.py put <act> <questions json> [<entry file, a relay path>]: every question composed, checked and banked
        import json
        import os
        if hasattr(sys.stdout, 'reconfigure'):
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        qs = json.load(open(sys.argv[3], encoding='utf-8'))
        qs = qs.get('questions') if isinstance(qs, dict) else qs
        e = ''
        if len(sys.argv) == 5:
            if not os.path.isfile(os.path.join('D:/relay', sys.argv[4])):
                raise SystemExit('### REFUSED: %s resolves to no file' % sys.argv[4])
            e = open(os.path.join('D:/relay', sys.argv[4]), encoding='utf-8').read()
        rel = put(sys.argv[2], qs, e)
        print('THE QUESTIONS COMPOSED, CHECKED AND BANKED: %s (%d question%s)' % (rel, len(qs), '' if len(qs) == 1 else 's'))
    else:
        raise SystemExit('usage: rootprompt.py remote <relay|pp> <act>   (one remote read per command)\n'
                         '       rootprompt.py hand <question file> <entry file>   (v1.27.0: a question after the seal through compose_checked)\n'
                         '       rootprompt.py put <act> <questions json> [<entry file>]   (v1.31.0: every prompt composed, checked and banked before it is put)')
