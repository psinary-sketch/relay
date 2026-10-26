# -*- coding: utf-8 -*-
"""act_close.py -- THE CLOSE'S SHARED FUNCTIONS, standing clauses v4 rows (62)-(68) ((R323)(4)), a shared tool from b713.

### Each function answers one repair of (R323)(4), and every tool that reads the object imports it from here and keeps no form of its own:
###   (i)   w_patterns, w_allows  -- ONE LIST OF WRITES: the write list read from the act's face, its (W) table, every backticked path;
###   (ii)  step_commits          -- EVERY COMMIT OF A STEP: a step bank row's commits (its `commits` list, or its one `commit`);
###   (iii) defect_owners         -- ONE COUNTER: the defects bank's letters counted by owner, once;
###   (iv)  lock_refuses          -- THE LOCK AS A MEMBRANE: the pre-lock steps' banks refuse a rewrite once the act's lock is written;
###   (vi)  close_steps, close_refuses -- THE CLOSE IN ONE ORDER: v4 row (68) read as numbered steps, each with its evidence, and a step
###         refused while a lower step's evidence is absent.
### ((v), the capture for every push, is tools/push_gated.sh's own; the head line's remote read is tools/b713_closing.py's.) Every function is
### pure in its arguments or reads only the paths it is given; nothing here writes. Written by the Write tool at b713.
### b714, standing clauses v5 rows (74)-(79) ((R324)(6)), each by the Edit tool, the diff banked in data/b714_tool_repairs.txt:
###   (i)   author_words, author_words_section, bank_hashes, hand_edits -- THE AUTHOR'S WORD AFTER THE SEAL: the word read from its own bank,
###         data/<act>_author_words.txt, verbatim; a tool-written bank's hashes recorded at its write and a hand edit read against them;
###   (ii)  act_figures, constant_scan -- THE ACT'S FIGURES FROM ONE SOURCE: the act, the next act, the chain's row count and the root
###         check's range read at run time from the step banks and data/act_roots.txt, and a figure left as a constant in a tool found;
###   (iii) close_steps at v5 row (79), with each step's evidence qualifier ("reading ready True"), evidence_ok, close_refuses on it, and
###         declared_failures -- EVERY STEP OF THE CLOSE IN THE ORDER: the seal refused while [2] reads READY False or [7]'s combined
###         pre-run bank is absent, and the face's declared-failure list read from the arms' own results;
###   ((iv) the hook is tools/b714_hook.py; (v) the one lettering is tools/act_letters.py.)
"""
import fnmatch
import hashlib
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
V4 = os.path.join(D, 'standing_clauses_v4.txt')
V5 = os.path.join(D, 'standing_clauses_v5.txt')


# ================================================================================ (i) ONE LIST OF WRITES
W_HEAD = re.compile(r'^### \(W\) THE WRITE LIST')
Z_HEAD = re.compile(r'^### \(Z\) THE NOTHINGS')
W_PATH = re.compile(r'`((?:relay|PLACE-papers|SIDE-[\w-]+)/[^`\s]+)`')


def w_patterns(face_text):
    """every backticked repository path of the face's (W) table, from its head to the (Z) head: ['relay/data/b712_*', ...]."""
    out, on = [], False
    for l in (face_text or '').replace(chr(13), '').split(NL):
        if W_HEAD.match(l):
            on = True
            continue
        if on and Z_HEAD.match(l):
            break
        if on:
            for p in W_PATH.findall(l):
                if p not in out:
                    out.append(p)
    return out


def w_allows(path, patterns, repo='relay'):
    """True where `<repo>/<path>` matches a (W) pattern (a glob, `*` within the name)."""
    q = '%s/%s' % (repo, path.replace('\\', '/'))
    return any(fnmatch.fnmatchcase(q, p) for p in patterns)


# ================================================================================ (ii) EVERY COMMIT OF A STEP
def step_commits(rows, phase=None, repo=None):
    """every commit a step bank's rows carry -- each row's `commits` list where it has one, else its `commit` -- for the rows of the phase and
    the repository named (all where None), in the bank's order, each once."""
    out = []
    for r in rows or []:
        if (phase is not None and r.get('phase') != phase) or (repo is not None and r.get('repo') != repo):
            continue
        for c in (r.get('commits') or [r.get('commit') or '']):
            if c and c not in out:
                out.append(c)
    return out


# ================================================================================ (iii) ONE COUNTER
OWNER = re.compile(r"^\(([a-z]'?)\) THE ([A-Z][A-Z_ -]*?)(?:’S|'S|’|')")


def defect_owners(letter_rows):
    """the defects' letters counted by owner, once: {'TOTAL': n, 'SEAT': n, 'NAVIGATOR': n, 'OTHER': n, 'by': [(letter, owner)]}. A row is
    `(x) THE <OWNER>'S ...` (the bank's own indent read through); SEAT and NAVIGATOR are the owners those words name, every other owner (a
    tool's, the carried form's) OTHER."""
    by = []
    for s in letter_rows or []:
        m = OWNER.match(s.lstrip())
        if m:
            o = m.group(2).strip()
            by.append((m.group(1), 'SEAT' if o == 'SEAT' else 'NAVIGATOR' if o == 'NAVIGATOR' else 'OTHER'))
    return dict(TOTAL=len(by), SEAT=sum(1 for _x, o in by if o == 'SEAT'), NAVIGATOR=sum(1 for _x, o in by if o == 'NAVIGATOR'),
                OTHER=sum(1 for _x, o in by if o == 'OTHER'), by=by)


# ================================================================================ (vi) THE CLOSE IN ONE ORDER
# ### b714 (iii): a step's words do not cross into the next step's (`(?:(?!; \[\d+\] ).)*?`, a step opening "; [n] " -- v5's [8] names "[2]
# ### or [7]" in its own words), and an evidence path may carry a qualifier -- v5's [2] "(data/<act>_root_banks_dry.json reading ready
# ### True)"; the carried pattern read v5's [2] through [3]'s evidence.
STEP = re.compile(r'\[(\d+)\] ((?:(?!; \[\d+\] ).)*?) \((data/<act>_[^)\s]+|the commands bank)((?: reading [^()]*)?)\)')
ROW_V5 = 'THE CLOSE IN ONE ORDER AT v5, THE STEPS NUMBERED'
ROW_V4 = 'THE CLOSE IN ONE ORDER, THE STEPS NUMBERED'


def _close_row(text=None):
    """the close's row and its name: v5 row (79) where the text carries it, else v4 row (68) (a replay over v4's text)."""
    t = text if text is not None else open(V5, encoding='utf-8').read()
    L = t.replace(chr(13), '').split(NL)
    for needle, name in ((ROW_V5, 'v5 row (79)'), (ROW_V4, 'v4 row (68)')):
        row = next((l for l in L if l.strip().startswith(needle)), '')
        if row:
            return row, name
    return '', 'no close row'


def close_steps(v4_text=None):
    """the close's row (v5 row (79); v4 row (68) where only that is given) as [(n, words, evidence)], the evidence a path with <act> or
    'the commands bank'. The argument keeps its b713 name; it takes either version's text."""
    row, _name = _close_row(v4_text)
    return [(int(n), w, e) for n, w, e, _q in STEP.findall(row)]


def step_qualifiers(text=None):
    """{n: qualifier} for the steps whose evidence carries one: {2: 'reading ready True'} at v5."""
    row, _name = _close_row(text)
    return dict((int(n), q.strip()) for n, _w, _e, q in STEP.findall(row) if q.strip())


def _evidence(e, act, dd):
    return None if not e.startswith('data/') else os.path.join(dd, os.path.basename(e.replace('<act>', act)))


def evidence_ok(path, qualifier='', present=None):
    """a step's evidence stands: the bank present and, where the row qualifies it, reading as the row says -- `reading ready True` a JSON
    bank whose `ready` is True. `present(path)` replaces the presence test for a replay."""
    if not (present or os.path.exists)(path):
        return False
    if qualifier == 'reading ready True':
        try:
            return json.load(open(path, encoding='utf-8')).get('ready') is True
        except Exception:
            return False
    return True


def close_refuses(act, n, dd=None, v4_text=None, present=None):
    """the refusal's text where a step lower than n lacks its evidence or its evidence does not read as its row qualifies it, '' where step n
    may run. `present(path)` decides a bank's presence (default: the file exists) so a replay can read the banks as they stood at a time."""
    dd = dd or D
    row, name = _close_row(v4_text)
    steps = close_steps(v4_text)
    quals = step_qualifiers(v4_text)
    if not steps or n not in [s[0] for s in steps]:
        return '### THE CLOSE`S ORDER (%s) CARRIES NO STEP [%d] -- REFUSED' % (name, n)
    miss = [(k, w, e) for k, w, e in steps if k < n and _evidence(e, act, dd) and not evidence_ok(_evidence(e, act, dd), quals.get(k, ''), present)]
    if miss:
        k, w, e = miss[0]
        return ('### THE CLOSE IN ONE ORDER (standing clauses %s): STEP [%d] REFUSED -- STEP [%d] (%s) IS UNFINISHED, ITS EVIDENCE %s%s '
                '%s%s -- NOTHING RUN' % (name, n, k, w[:60], e.replace('<act>', act), (' ' + quals[k]) if quals.get(k) else '',
                                         'NOT AS ITS ROW READS' if quals.get(k) and (present or os.path.exists)(_evidence(e, act, dd)) else 'ABSENT',
                                         (' (and %d more lower steps)' % (len(miss) - 1)) if len(miss) > 1 else ''))
    return ''


# ================================================================================ (iii) THE FACE'S DECLARED FAILURES, FROM THE ARMS' RESULTS
FAILING = re.compile(r'LIVE FAILING : \d+ \[([^\]]*)\]')


def declared_failures(prerun_text, waiting=()):
    """the face's declared-failure list read from the combined pre-run bank (data/<act>_arms_prerun.txt): every arm its foot names failing,
    less those the caller names as waiting on a step after the seal (their evidence a later step's bank), in the bank's order."""
    m = FAILING.search(prerun_text or '')
    if not m:
        return None
    names = re.findall(r"'([A-Z0-9-]+)'", m.group(1))
    return [x for x in names if x not in set(waiting)]


# ================================================================================ (iv) THE LOCK AS A MEMBRANE
def pre_lock_banks(act, v4_text=None):
    """the banks of the steps before the lock in v4 row (68) (the lock's own step excluded), by basename, each with its .txt/.json sibling."""
    steps = close_steps(v4_text)
    lock_n = next((k for k, w, e in steps if e.endswith('_lockgate.json')), None)
    out = []
    for k, w, e in steps:
        if lock_n is not None and k < lock_n and e.startswith('data/'):
            b = os.path.basename(e.replace('<act>', act))
            stem = re.sub(r'\.(txt|json)$', '', b)
            out += [b, stem + '.txt', stem + '.json']
    return sorted(set(out))


def lock_refuses(act, name, dd=None, v4_text=None):
    """the refusal's text where the act's lock is written (data/<act>_lockgate.json) and the bank is one a step before the lock wrote and
    stands written; '' otherwise. As the root's membrane refuses after the root (row (53)), so the lock's after the lock."""
    dd = dd or D
    base = os.path.basename(name)
    if not os.path.exists(os.path.join(dd, '%s_lockgate.json' % act)):
        return ''
    if base in pre_lock_banks(act, v4_text) and os.path.exists(os.path.join(dd, base)):
        return ('### THE LOCK AS A MEMBRANE (standing clauses v4 row (65)): %s`S LOCK IS WRITTEN (data/%s_lockgate.json) AND %s IS A BANK '
                'WRITTEN BEFORE IT -- NOTHING WRITTEN' % (act, act, base))
    return ''


# ================================================================================ (i) THE AUTHOR'S WORD AFTER THE SEAL (b714, v5 row (74))
AUTHOR_WORDS_HEAD = "### THE AUTHOR'S WORD AFTER THE SEAL"


def author_words(act, dd=None):
    """the author's word received after the seal, verbatim from data/<act>_author_words.txt (its bytes, CR removed), or None where the act
    has no such bank."""
    p = os.path.join(dd or D, '%s_author_words.txt' % act)
    if not os.path.exists(p):
        return None
    return open(p, encoding='utf-8').read().replace(chr(13), '')


def author_words_section(act, dd=None):
    """the section the closing, record and trail tools print: its head, then the bank's lines verbatim each under four spaces, or NONE."""
    t = author_words(act, dd)
    if t is None:
        return [AUTHOR_WORDS_HEAD + ' (data/%s_author_words.txt): NONE RECEIVED' % act]
    body = t.rstrip(NL).split(NL)
    return [AUTHOR_WORDS_HEAD + ' (data/%s_author_words.txt, %d lines, sha256 %s), verbatim:' % (
        act, len(body), hashlib.sha256(t.encode('utf-8')).hexdigest()[:16])] + ['    ' + l for l in body]


def bank_hashes(paths):
    """{path: sha256 of its bytes} for the banks a tool has just written -- the record a hand edit is read against."""
    out = {}
    for p in paths:
        with open(p, 'rb') as fh:
            out[p] = hashlib.sha256(fh.read()).hexdigest()
    return out


def hand_edits(hashes):
    """the banks whose bytes no longer hash as their tool wrote them: [(path, written, now)], `now` None where the bank is gone."""
    out = []
    for p, h in sorted((hashes or {}).items()):
        if not os.path.exists(p):
            out.append((p, h, None))
            continue
        with open(p, 'rb') as fh:
            now = hashlib.sha256(fh.read()).hexdigest()
        if now != h:
            out.append((p, h, now))
    return out


# ================================================================================ (ii) THE ACT'S FIGURES FROM ONE SOURCE (b714, v5 row (75))
CHAIN_ROW = re.compile(r'^b(\d+) [0-9a-f]{64} [0-9a-f]{64}(?: .*)?$')   # ### act root previous [note] (b625's row carries a note)
STEPS_BANK = re.compile(r'^b(\d+)_steps\.json$')


def chain_rows(roots_text):
    """the act-root chain's rows of data/act_roots.txt in order, [(act number, line)] -- a `corrigendum` line is not a chain row."""
    return [(int(m.group(1)), i) for i, l in enumerate((roots_text or '').replace(chr(13), '').split(NL), 1)
            for m in [CHAIN_ROW.match(l.strip())] if m]


def act_figures(dd=None, roots_text=None, act=None):
    """the act's figures read at run time: the act (the highest bNNN with a step bank data/bNNN_steps.json, or `act` given), the next act,
    the chain's rows before the act (its own row the next), and the root check's range -- the chain's first act through the act itself
    where its row stands, else through the last row. Returns a dict; nothing is carried as a constant."""
    dd = dd or D
    if act is None:
        nums = [int(m.group(1)) for f in os.listdir(dd) for m in [STEPS_BANK.match(f)] if m]
        if not nums:
            raise ValueError('no step bank under %s' % dd)
        n = max(nums)
    else:
        n = int(str(act).lstrip('b'))
    if roots_text is None:
        roots_text = open(os.path.join(dd, 'act_roots.txt'), encoding='utf-8').read()
    rows = chain_rows(roots_text)
    acts = [a for a, _i in rows]
    before = [a for a in acts if a < n]
    own = n in acts
    last = n if own else (acts[-1] if acts else n)
    return dict(act='b%d' % n, next_act='b%d' % (n + 1), chain_rows=len(acts), rows_before=len(before),
                own_row=len(before) + 1, own_row_stands=own,
                range_first=acts[0] if acts else n, range_last=last, range=list(range(acts[0] if acts else n, last + 1)))


SCAN_FORMS = ('act', 'next', 'needle', 'range')


def constant_scan(text, act_n, forms=SCAN_FORMS):
    """the lines of a tool's text (comments aside) carrying a figure of the act <act_n> as a constant -- the forms a carried figure took at
    b713: a quoted 'bNNN' for the act ('act') or the next ('next'), a `**Next:** bNNN` needle of any act ('needle'), range(624, NNN) to
    any literal end ('range'). The suite is scanned in all four (its act read from the step bank); a tool whose name is its act's (its
    `ACT = 'bNNN'` line its identity) in 'needle' and 'range'. [(line, the form)]."""
    out = []
    pats = [('act', r"['\"]b%d['\"]" % act_n, 'the act quoted'), ('next', r"['\"]b%d['\"]" % (act_n + 1), 'the next act quoted'),
            ('needle', r"\*\*Next:\*\* b\d+", 'the Next needle'),
            ('range', r"range\(\s*624\s*,\s*\d+\s*\)", 'the root range')]   # ### any literal: b713's carried figures were stale ones
    for i, l in enumerate((text or '').replace(chr(13), '').split(NL), 1):
        if l.lstrip().startswith('#'):
            continue
        for k, p, what in pats:
            if k in forms and re.search(p, l):
                out.append((i, what))
    return out
