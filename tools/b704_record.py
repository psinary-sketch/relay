# -*- coding: utf-8 -*-
"""b704_record.py -- THE ACT'S RECORD TOOL, b704 under (R314).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b704 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers (_deps, the primed names; _defect_short, its act at the call; the span line from the mirror bank chain) are IMPORTED from
### tools/b703_record.py (sealed at b703 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b704 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b704_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b704_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited
import b703_record as P3           # noqa: E402  ### b703's repaired readers, imported unedited (its import rebinds R to b703: rebound again below)

ACT, PREV = 'b704', 'b703'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b703 ran and closed in ANOTHER session (e5bcf1d0); this act opens a new one (fb68aaef) -- b701's form: the
# ### previous window from b703's anchor in its own session to that session's end
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
FACE = os.path.join(D, 'b704_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b704_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b703_closing_push_out.txt', 'b675_corrigenda.txt', 'glossary.txt')
R.N5_RELAY_TOOLS = ()
R.ROOT_EXCLUDE = re.compile(r'^b704_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')

_R_anchor_ts = P3._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap)


def _anchor_ts(anchor, session=None):
    """b698's _anchor_ts bound its session at definition (b699's trap 1): this one reads this act's session unless another is named."""
    return _R_anchor_ts(anchor, session or SESSION)


R._anchor_ts = _anchor_ts


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='3b6de278' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S REPAIRED READERS, IMPORTED
_deps = P3._deps                   # ### the primed names read (b703 (f)); R._deps already rebound to it by b703's import
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen = R.rowgen
answers = R.answers


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R314)(8); b703's form)
def branches(*a):
    """`branches before`: data/b704_branches_before.json -- b698's route, carried (every branch (R314)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b704_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the two kernel branches of the prompt read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b704_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    kb = []
    rh = R._remote_heads(K.KERNEL_DIR)
    for b in K.KERNEL_BRANCHES_PROMPT:
        lt = g(K.KERNEL_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b).strip()
        kb.append((b, lt[:7] or 'ABSENT', (rh.get(b) or '')[:7] or 'ABSENT'))
    L = ['%s -- STEP ZERO, (R314)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b704_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. The kernel branches widening-b701 and epstein-b703 raised as one',
         '### prompt before any kernel delete ((R314)(8)), read beneath.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### the kernel branches of the prompt at the close of step zero: %s' % ' ; '.join('%s local %s remote %s' % x for x in kb)]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, kernel_branches=kb))
    print(NL.join(L[7:]))


# ================================================================================ COMPONENT 2: THE DISPATCH, THE RUNNER (b698's routes; b703's runner)
EF = K.KERNEL_DIR
dispatch, runstatus = R.dispatch, R.runstatus
STD3 = P3.STD3


# ================================================================================ STEP ZERO: THE READ RULE'S SORT, (R314)(2)
def _read_calls(path, since=None):
    """every Read call of a session transcript: (transcript line, time, file_path, offset, limit), from `since` (an ISO time) on."""
    out = []
    for i, raw in enumerate(open(path, encoding='utf-8', errors='replace'), 1):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        ts = o.get('timestamp') or ''
        if since and ts < since:
            continue
        for c in ((o.get('message') or {}).get('content') or []) if isinstance((o.get('message') or {}).get('content'), list) else []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                out.append((i, ts, inp.get('file_path', ''), inp.get('offset'), inp.get('limit')))
    return out


def _nlines(p):
    try:
        return len(open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '').rstrip(NL).split(NL))
    except OSError:
        return None


def readsort(*a):
    """data/b704_read_sort.txt: (R314)(2) -- each read-rule breach of b703 ((k) thirteen calls, (l), (m)) with whether its path, offset and
    limit leave a trace in a bank the suite can read: the act's command bank (data/b703_commands.txt) and its read bank
    (data/b703_read_calls.txt), each by path and line; and the arm the traceable ones would take. Nothing is written but the sort's bank."""
    rb = rdn('b703_read_calls.txt').split(NL)
    cb = rdn('b703_commands.txt').split(NL)
    off = [(i + 1, l) for i, l in enumerate(rb) if '| ### AN OFFENCE |' in l and re.match(r'^  \d+ \|', l)]
    calls = dict((c[0], c) for c in _read_calls(PREV_SESSION_PATH))
    rows = []
    for n, l in off:
        tl = int(l.split('|')[0].strip())
        c = calls.get(tl)
        letter = 'l' if tl == 10815 else 'k'
        incb = [j + 1 for j, x in enumerate(cb) if c and c[2] and c[2] in x]
        rows.append((letter, tl, c[1] if c else '-', c[2] if c else l.split('|')[-1].strip(), c[3] if c else '?', c[4] if c else '?',
                     _nlines(c[2]) if c else None, 'data/b703_read_calls.txt :%d' % n,
                     ('NONE (a command naming the path at data/b703_commands.txt :%s, not this call)' % incb[0]) if incb else 'NONE'))
    closing = '2026-10-22T03:06:13'
    mem = [c for c in _read_calls(PREV_SESSION_PATH, since=closing) if (_nlines(c[2]) or 0) >= 200 and not (c[3] and c[4])]
    for c in mem:
        n_ = _nlines(c[2])
        rows.append(('m', c[0], c[1], c[2], c[3], c[4], n_, 'NONE (after the read bank`s stamp 02:25:02Z and after the closing)', 'NONE'))
    L = ['%s -- STEP ZERO, (R314)(2): THE READ RULE`S BREACHES AT b703, SORTED BY TRACE (%s)' % (ACT, utc()), '',
         '### the rule: data/b698_rules.txt row (2), whole under two hundred lines, by offset and limit otherwise, memory files included. The author`s',
         '### word of 2026-10-18 (relay data/b683_ferry.txt :5): "arms for the traceable ones, the seat sorts them". Rows are breaches: the letter |',
         '### the transcript line in b703`s session (%s) | the time | the path | offset | limit | the file`s lines now | its trace in the read bank |' % K.PREV_SESSION[:8],
         '### its trace in the command bank. A breach is TRACEABLE where a bank the suite reads carries its path at a line; the offset and limit',
         '### are carried by the read bank`s row form (a row is a call without both), not as values.', '']
    for r in rows:
        L.append('  (%s) | %s | %s | %s | offset %s | limit %s | lines %s | %s | %s | %s' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8],
                 'TRACEABLE' if not r[7].startswith('NONE') else 'NOT IN A BANK'))
    tr = [r for r in rows if not r[7].startswith('NONE')]
    nt = [r for r in rows if r[7].startswith('NONE')]
    L += ['', '### THE SORT:',
          '  TRACEABLE %d ((k) %d, (l) %d): each a row of relay data/b703_read_calls.txt, written by the record tool from the session transcript at the' % (
              len(tr), sum(1 for r in tr if r[0] == 'k'), sum(1 for r in tr if r[0] == 'l')),
          '    root; the command bank (data/b703_commands.txt) carries commands, not Read calls, so it traces none of them.',
          '  NOT IN A BANK %d ((m)): made after the closing, after every bank of b703 was written; the session transcript alone carries it.' % len(nt),
          '', '### THE ARM IT WOULD WRITE (raised before any arm is written, "write the arm" / "keep it prose"):',
          '  G-READ-RULE-STANDING -- a standing arm reading the act`s own read bank (data/b<act>_read_calls.txt, written at the root from the',
          '    session transcript): it fails on any row ### AN OFFENCE (a Read call of a file of two hundred lines or more without both an offset and',
          '    a limit) not lettered in the act`s defects bank; and it reads the previous act`s session from its closing push to that session`s end',
          '    (the window the command bank already reads for commands), so a breach after the closing, as (m), is printed and lettered by the next',
          '    act. Its NEG control: a planted offence row unlettered fails it. b703`s act arm G-READ-RULE read the bank within the act alone.', '',
          '### ### **BREACHES %d ; TRACEABLE %d ((k) %d, (l) %d) ; NOT IN A BANK %d ((m) %d) ; THE COMMAND BANK TRACES 0.**' % (
              len(rows), len(tr), sum(1 for r in tr if r[0] == 'k'), sum(1 for r in tr if r[0] == 'l'), len(nt), len(nt))]
    if 'dry' not in a:
        put_txt('%s_read_sort.txt' % ACT, L)
    print(NL.join(L[8:]))


ROUTES = dict(defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch, runstatus=runstatus,
              readsort=readsort)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b704_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
