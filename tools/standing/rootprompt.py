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
Pure in its arguments; nothing written -- except remote_read (the CLI `remote`), which reads the remote once and banks data/<act>_rootprompt_remote.json.
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
    else:
        raise SystemExit('usage: rootprompt.py remote <relay|pp> <act>   (one remote read per command)')


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
