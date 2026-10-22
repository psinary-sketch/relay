# -*- coding: utf-8 -*-
"""b705_record.py -- THE ACT'S RECORD TOOL, b705 under (R315).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b705 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers (_deps, the primed names; _defect_short, its act at the call; the span line from the mirror bank chain) and b704's repaired read
### route are reached through tools/b704_record.py (sealed at b704 and unedited), each pure in its arguments or rebound here. Every python
### child is `python -X utf8`.
### Written by the Write tool at b705 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b705_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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

import b705_worklist as K          # noqa: E402
import b704_record as P4           # noqa: E402  ### b704's tool, imported unedited (its import binds b698's R and b703's P3 to b704: rebound below)
R, P3 = P4.R, P4.P3                # ### b698's routes and b703's repaired readers, through b704's module

ACT, PREV = 'b705', 'b704'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b704 ran and closed in ANOTHER session (fb68aaef); this act opens a new one (44411d52) -- b701's form: the
# ### previous window from b704's anchor in its own session to that session's end
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
FACE = os.path.join(D, 'b705_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b705_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b704_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('e0_rule.py',)
R.ROOT_EXCLUDE = re.compile(r'^b705_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')

_R_anchor_ts = P4._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704


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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='97bd2133' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S AND b704'S REPAIRED READERS, THROUGH b704'S MODULE
_deps = P3._deps                   # ### the primed names read (b703 (f))
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line
_read_verdict, CAP = P4._read_verdict, P4.CAP   # ### b704's repaired verdict (offset, limit VALUES, the cap of two hundred)


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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R315)(10); b704's form, no kernel branch)
def branches(*a):
    """`branches before`: data/b705_branches_before.json -- b698's route, carried (every branch (R315)(10) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b705_branches.txt (.json) --
    each branch's fate read now against the tips banked before."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b705_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R315)(10): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b705_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. No kernel branch is named by (R315)(10).']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[6:]))


# ================================================================================ THE READ BANK (b704's repaired route; from b705 the word's time is the anchor's)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b705_read_calls.txt."""
    word = _anchor_ts(K.ANCHOR)
    rows = []
    for i, o, _st, _sid in R._session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i, ts=o.get('timestamp'), path=p, offset=inp.get('offset'), limit=inp.get('limit'), lines=R._lines_now(p)))
    for r in rows:
        r['verdict'] = _read_verdict(r, word)
    bad = [r for r in rows if r['verdict'] == '### AN OFFENCE']
    pre = [r for r in rows if r['verdict'].startswith('BEFORE THE WORD')]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) AND THE AUTHOR`S WORD AT b704`S SORT (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines; otherwise an offset and a limit, the limit no greater than two hundred (the',
         '### cap, the author`s word at %s). Rows are Read calls: transcript line | time | the file`s lines read now | offset | limit | the verdict |' % (word or '### NOT READ'),
         '### path. From b705 the word`s time is the act`s anchor and every call counts (the author`s word at b704`s arm-baseline prompt).']
    L += ['  %s | %s | %s | offset %s | limit %s | %s | %s' % (r['line'], r['ts'], r['lines'], r['offset'], r['limit'], r['verdict'], r['path']) for r in rows] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; ON FILES OF 200 LINES OR MORE %d ; OFFENCES %d ; THE CAP`S PRECURSORS %d ; THE WORD AT %s.**' % (
        len(rows), sum(1 for r in rows if r['lines'] is None or r['lines'] >= CAP), len(bad), len(pre), word or '### NOT READ')]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
        put_json('%s_read_calls.json' % ACT, dict(at=utc(), word=word, cap=CAP, rows=rows))
    print(NL.join([l for l in L if '### AN OFFENCE' in l or 'PRECURSOR' in l][:40] + L[-1:]))


def names(*a):
    """the functions of an imported record module (b698's by default) with the line each opens at -- names and numbers, no source printed."""
    import importlib
    import inspect
    mod = {'b698': R, 'b703': P3, 'b704': P4}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
    for n, f in sorted(vars(mod).items(), key=lambda kv: inspect.getsourcelines(kv[1])[1] if inspect.isfunction(kv[1]) and kv[1].__module__ == mod.__name__ else 0):
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            print('  %-28s :%d' % (n, inspect.getsourcelines(f)[1]))


def verdicts(*a):
    """prints each named bank's verdict line (its last `### ### **...**` line), for the suite's predicates to quote; writes nothing."""
    for n_ in a:
        m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', rdn(n_))
        print('  %s | %s' % (n_, ' '.join(m[-1].split()) if m else '### NO VERDICT LINE'))


# ================================================================================ THE DISPATCH, THE RUNNER (b698's routes; b703's runner reader through b704)
dispatch, runstatus, runner = R.dispatch, R.runstatus, R.runner
STD3 = P3.STD3


def runwait(*a):
    """`runwait <kernel> <run id> [seconds]`: the run's status read every 30 s in the FOREGROUND until it completes or the seconds pass (at most
    560, under the 590 s guard); each read printed. No wait is backgrounded."""
    end = time.time() + min(int(a[2]) if len(a) > 2 else 540, 560)
    while True:
        rc, out, err = R._gh('run', 'view', a[1], '-R', 'psinary-sketch/' + a[0], '--json', 'status,conclusion,updatedAt')
        j = json.loads(out or b'{}')
        print('  %s  status %s ; conclusion %s ; updated %s' % (utc(), j.get('status'), j.get('conclusion') or '-', j.get('updatedAt')), flush=True)
        if j.get('status') == 'completed' or time.time() + 30 > end:
            return
        time.sleep(30)


# ================================================================================ THE LATE ROUTES (b704's, carried with b705's names)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor. Rebound here: b704's
    import rebound b698's to its own, which reads b704's session."""
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('%s/%s.jsonl' % (PROJ, sid), anc, '%s/%s/subagents' % (PROJ, sid))
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    rows.sort(key=lambda r: r['ts'])
    bg = R._bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


R.capture = capture
prev_capture = R.prev_capture
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b704's route with b705's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window, the
    local lean reading (N1), the dispatch (one, the join kernel's), the detached runs, sed, the redirects, the pipes, the one-line programs, the
    moves and deletes by shape, the outbound requests. data/b705_commands.txt (.json)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if DISPATCH_CMD.search(QUOTED.sub('""', r['cmd']))]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = R.outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCH, THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, its own session %s, from its post-push combine to that session`s end): '
              '%d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (one ordered this act, N1: the join kernel) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A PIPE OF ANY KIND, read outside quoted strings (%d):' % len(anypipe)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in anypipe] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R315)(10) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; PIPES OF ANY KIND %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(anypipe), len(pyreads), len(mv), good,
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        for r, o in hits:
            print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV, session=R.PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], any_pipes=[r['n'] for r in anypipe], py_programs=[r['n'] for r in pyreads],
                                           moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


_kerns = R._kerns                  # ### b703's list (b698's and SIDE-substrate-cluster), rebound by b703's import


def kernels(*a):
    ks = list(dict.fromkeys(_kerns())) + [K.KERNEL]
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-faces-join read after its tag; no kernel written after this read)' % len(ks))


def _standing():
    import b704_worklist as K704
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B704_FACE.split('/')))) - set(K704.ACT_ARMS)) | set(K.STANDING_ADDED))


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


# ================================================================================ COMPONENT 1: THE SORT, (R315)(2)
EIGHT = (('G-README-CURRENCY', 'n', 'the navigator`s design', 'REPAIRED under (R315)(3): tools/b705_standing_figures.py readme(), the appends and the deposited versions excluded by their text (data/b705_tool_repairs.txt row (3))'),
         ('G-ACTROOT-BANKED', 'r', 'the navigator`s predicate, requiring a read bank among the root`s items where the root route excludes read banks by design', 'REPAIRED at carry time under (R315)(2)(b): tools/b705_checks.py root_banked_ok reads the root route`s own item list (data/b705_tool_repairs.txt row (1))'),
         ('G-ANSWERS-CHECKED', 's', 'the navigator`s predicate, leaving no room for the root prompt`s answer checks after the seal', 'REPAIRED at carry time under (R315)(2)(c): tools/b705_checks.py answers_checked_ok admits the checks the root prompt requires, each printed with its time (data/b705_tool_repairs.txt row (2))'),
         ('G-WORKFLOW-FILES', 'p', 'the seat`s run: the probe dispatched at 43 modules where print_targets.txt lists 109', 'REPAIRED under (R315)(4): the probe route`s target print_targets.txt whole, data/b705_rules.txt row (1), read by the arm (data/b705_tool_repairs.txt row (4))'),
         ('G-READ-RULE-STANDING', 'i', 'four reads after the word, defects (i) and (o)', 'NO REPAIR: the arm correct; from b705 every call counts'),
         ('G-TRAIL-LINES-EQUAL-DEFECTS', 'r', '(r) lettered after the trail landed', 'NO REPAIR: the sequence rule binding -- no defect is lettered after the trail without the trail`s dry run re-read'),
         ('G-TRAIL-DEFECTS-EQUAL', 'r', '(r) lettered after the trail landed', 'NO REPAIR: the sequence rule binding'),
         ('G-TRAIL-RESOLVED-EQUAL', 'r', '(r) lettered after the trail landed', 'NO REPAIR: the sequence rule binding'))


def _drow(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def armsort(*a):
    """data/b705_arm_sort.txt: (R315)(2), the eight arms failing at b704's close (data/b704_checks.txt's LIVE FAILING list), each with its cause by
    letter and line in data/b704_defects.txt and its disposition in the ruling's words; rows are arms."""
    ck = rdn('b704_checks.txt')
    m8 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m8.group(2) if m8 else '').split(',') if x.strip()]
    df = rdn('b704_defects.txt').split(NL)
    face = rd(os.path.join(ROOT, *K.B704_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    rows = []
    for name, letter, cause, disp in EIGHT:
        s, e, t = _drow(df, letter)
        rows.append((name, name in fails, 'declared on the face' if name in declared else 'found after the seal', letter, s, max(e - 1, s), cause, disp,
                     t[:140]))
    L = ['%s -- COMPONENT 1, (R315)(2): THE EIGHT ARMS FAILING AT b704`S CLOSE, SORTED BY CAUSE, EACH WITH ITS DISPOSITION (%s)' % (ACT, utc()), '',
         '### rows are arms: the arm | failing at b704`s close (relay data/b704_checks.txt, LIVE FAILING %d) | declared on the face or found after the seal' % len(fails),
         '### (relay data/b704_registration_2026-10-21.txt) | its cause by letter and line in relay data/b704_defects.txt | the disposition in (R315)(2)`s words.',
         '### The sequence rule, (R315)(2)(f)-(h): no defect is lettered after the trail lands without the trail`s dry run re-read.', '']
    for name, f, where, letter, s, e, cause, disp, t in rows:
        L += ['  %-28s | failing %s | %s | (%s) data/b704_defects.txt :%d-:%d -- %s | %s' % (name, f, where, letter, s, e, cause, disp),
              '      the row: %s' % t]
    rep = [r for r in rows if r[7].startswith('REPAIRED')]
    L += ['', '### ### **ARMS 8 ; FAILING AT b704`S CLOSE %d OF 8 ; DECLARED ON THE FACE %d ; FOUND AFTER THE SEAL %d ; REPAIRED AT CARRY TIME %d ; NO REPAIR %d.**' % (
        sum(1 for r in rows if r[1]), sum(1 for r in rows if r[2] == 'declared on the face'), sum(1 for r in rows if r[2] == 'found after the seal'), len(rep), 8 - len(rep))]
    if 'dry' not in a:
        put_txt('%s_arm_sort.txt' % ACT, L)
        put_json('%s_arm_sort.json' % ACT, dict(at=utc(), rows=[dict(arm=r[0], failing=r[1], where=r[2], letter=r[3], lines=[r[4], r[5]], cause=r[6], disposition=r[7]) for r in rows],
                                                failing=fails, declared=declared))
    print(NL.join(L[6:]))


# ================================================================================ COMPONENT 1: THE FOUR STANDING FIGURES, THE README FIGURE REPAIRED ((R315)(3))
def figures(*a):
    """data/b705_standing_figures.txt (.json): the four figures by relay tools/b705_standing_figures.py (readme() repaired under (R315)(3), the
    other three b703's unedited through it), the README figure's baseline reset to this act's reading, the other three read against b704's
    baseline (data/b704_standing_figures.json); the excluded README rows printed with their reason."""
    import b705_standing_figures as SF5
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b704_standing_figures.json')
    f = SF5.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    rr = (f.get('readme') or {}).get('rows') or []
    L = ['%s -- COMPONENT 1, (R315)(3): THE FOUR STANDING FIGURES AT b705, THE README FIGURE BY THE REPAIRED readme() AGAINST ITS RESET BASELINE, THE OTHER THREE AGAINST b704`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b705_standing_figures.py (readme() repaired, W-ORD-README-FIGURE-SCOPE; correspondence(), partners(), pins() b703`s, imported unedited), %.0f s;' % (t1 - t0),
         '### each arm fails on a regression from the previous act`s figure; the README figure`s baseline is THIS ACT`S reading (the author`s word at b704`s README-figure prompt).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        if k == 'readme':
            L.append('  %-15s b705 %s ; b704 %s (by the unrepaired readme(), 12) ; THE BASELINE RESET TO b705`S READING %s' % (k, now, prev, now))
        else:
            L.append('  %-15s b705 %s ; b704 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE README`S ROWS BY THE REPAIRED readme(): each with its line, kernel, cited tag, highest tag and state (EXCLUDED rows carry their reason):']
    L += ['  :%-4d %-26s %-9s highest %-9s %s%s' % (r['line'], r['kernel'], r['cited'], r['highest'] or '-', r['state'], (' -- ' + r['why']) if r.get('why') else '') for r in rr]
    ex = [r for r in rr if r['state'] == 'EXCLUDED']
    L += ['', '### ### **FIGURES AT b705: CORRESPONDENCE %s ; README %s (ROWS %d, EXCLUDED %d: APPENDS %d, NOT CURRENCY LINES %d, DEPOSITED %d, STALE LINES %s) ; PARTNERS %s ; PINS %s -- AGAINST b704`S %s, %s, %s, %s ; THE README BASELINE RESET TO %s.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), len(rr), len(ex), sum(1 for r in ex if 'append' in (r.get('why') or '')),
        sum(1 for r in ex if 'not a currency' in (r.get('why') or '')),
        sum(1 for r in ex if 'deposited' in (r.get('why') or '')), sorted(set(r['line'] for r in rr if r['state'] == 'STALE')) or 'NONE',
        (f.get('partners') or {}).get('figure'), (f.get('pins') or {}).get('figure'),
        (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'), (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'),
        (f.get('readme') or {}).get('figure'))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), readme_baseline_reset=True, **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:12] + L[-1:]))


def figctl(*a):
    """data/b705_readme_control.txt: the README figure's controls, (R315)(3) -- the real README by the repaired readme() (0 stale wanted), by b703's
    unrepaired readme() beside it (b704's 12), a mutated copy with the kernel line set back to v0.35 (1 stale wanted, the arm failing against
    the baseline 0), a mutated copy with a dated append naming v0.36 added (0 wanted: excluded by its text). No README edited."""
    import b705_standing_figures as SF5
    import b703_standing_figures as SF3
    import b616_claims as KC0
    import b703_checks as C3
    text = rd(os.path.join(PP, 'README.md')).replace(chr(13), '')
    base_fig = jl('%s_standing_figures.json' % ACT).get('readme', {}).get('figure')
    n_real, rows_real = SF5.readme(KC0.remote_refs, text)
    n_old, _rows_old = SF3.readme(KC0.remote_refs)
    mut = text.replace('**v0.37** (`38e2734`)', '**v0.35** (`d4e046a`)')
    assert mut != text
    n_mut, rows_mut = SF5.readme(KC0.remote_refs, mut)
    add = text.rstrip(NL) + NL + NL + "*(Appended under the author's ruling `(R999)`(1), 2026-10-22, b999: SIDE-explicit-formula v0.36 entered at its weight, v0.36 = `dfadc8c`.)*" + NL
    n_add, _rows_add = SF5.readme(KC0.remote_refs, add)
    arm = lambda live, prev: isinstance(live, int) and isinstance(prev, int) and live <= prev   # noqa: E731  ### tools/b703_checks.py fig_ok's comparison
    cases = [('the real README by the repaired readme()', n_real, 0, 'PASS' if arm(n_real, base_fig) else 'FAIL', 'PASS'),
             ('the real README by b703`s unrepaired readme() (b704`s figure beside)', n_old, 12, '-', '-'),
             ('a mutated copy, the kernel line`s **v0.37** (`38e2734`) set back to **v0.35** (`d4e046a`)', n_mut, 1, 'PASS' if arm(n_mut, base_fig) else 'FAIL', 'FAIL'),
             ('a mutated copy with a dated ceiling append naming v0.36 added at its end', n_add, 0, 'PASS' if arm(n_add, base_fig) else 'FAIL', 'PASS')]
    L = ['%s -- COMPONENT 1, (R315)(3): THE README FIGURE`S CONTROLS, THE REPAIRED readme() AGAINST THE UNREPAIRED AND ON MUTATED COPIES (%s)' % (ACT, utc()), '',
         '### rows are cases: the copy | the stale lines read | wanted | the arm`s verdict against the reset baseline %s | wanted. The README is not edited;' % base_fig,
         '### the mutated copies are texts handed to readme(). The repaired readme(): tools/b705_standing_figures.py; the unrepaired: tools/b703_standing_figures.py :163.', '']
    L += ['  %-96s | read %2s | wanted %2s | arm %-4s | wanted %s' % (c, n, w, v, wv) for c, n, w, v, wv in cases]
    L += ['', '### the stale rows of the mutated copy: %s' % ['%s %s %s' % (r['line'], r['kernel'], r['cited']) for r in rows_mut if r['state'] == 'STALE'],
          '### the excluded rows of the real README: %d (%s)' % (sum(1 for r in rows_real if r['state'] == 'EXCLUDED'), '; '.join(sorted(set(r['why'] for r in rows_real if r['state'] == 'EXCLUDED'))))]
    ok = all((n == w) and (v == wv or v == '-') for _c, n, w, v, wv in cases)
    L += ['', '### ### **THE REAL README READS %d STALE ON THE REPAIRED FIGURE (b704`S 12 ON THE UNREPAIRED) ; THE v0.35 COPY READS %d AND THE ARM FAILS ; THE APPEND COPY READS %d ; EVERY CONTROL AS WANTED %s.**' % (
        n_real, n_mut, n_add, ok)]
    put_txt('%s_readme_control.txt' % ACT, L)
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R315)(1)
WH = ('*Appended 2026-10-22 by b705 to b704’s entry (:9938), under `(R315)`(1) -- b704 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b704_closing.txt):*')
WB = (' “b704 closed: relay 3f2abacc, PLACE-papers d668413; suite 132 of 140; root 97bd213337dd2e17…; 13 prompts answered; 19 defects” '
      '(data/b704_closing.txt :1); the closing commit f5a35af1 pushed alone after the line was written and read back equal at the remote '
      '(data/b704_closing_push_out.txt :5). The faces page at v0.37 from probe run 39721668586 on the scratch branch probe-b704, deleted after '
      'its bank with main and every tag untouched, h2_sign_sum_iff_rh and h2_sign’_imp_rh added as nodes on the author’s word, six lines changed '
      'over the act each with its cause (data/b704_faces_diff.txt); the generator writing 0 cells, SIDE-explicit-formula outside its 16 parsed '
      'kernels, the 15 prose mentions read against the probe -- 4 equal, 0 differing, 11 unbanked -- and W-ORD-CORRESPONDENCE-EF-REACH entered '
      '(data/b704_cells_reach.txt); the README’s kernel line at :164 naming v0.37 = 38e2734 and the v0.36–v0.37 append at :135, PLACE-papers '
      '05c6dd6, its blob 9a8ff6ce read back equal at the remote (data/b704_readme.txt); the glossary rows h2_sign’ and h2_sign_sum appended at '
      ':107-:108 after both theorems read DERIVES under E0 and by hand (data/b704_glossary.txt); day1/ONE_PAGE_PROOF.md re-cut on the author’s '
      'word at the tie, 22 rows outside LICENSED/CITED to 2, 80 quoting lines entered as residues (data/b704_cut.txt; PLACE-papers 02b7aad); '
      'the four standing figures 0, 12, 131, 0 against b703’s 0, 11, 131, 0, the README’s one new stale line the ordered append at :135 '
      '(data/b704_standing_figures.txt); W-ORD-FACES-PROBE-CURRENT discharged, W-ORD-WORKFLOW-PROBE-STEP, W-ORD-CORRESPONDENCE-EF-REACH and '
      'W-ORD-README-FIGURE-SCOPE entered (OPEN_TRAILS :15542-:15550). b703’s one item after its closing answered by the generated corrigendum '
      'at FINDINGS :9926 (corrigenda row (24)); b703’s weight at :9924. The entry at FINDINGS :9938, the trail at OPEN_TRAILS :15552; the root '
      '97bd2133 over 91 banks chained from 3b6de278, the chain b624–b704 AGREE (data/b704_act_root.json); suite 132 of 140 pre-push and '
      'post-push, three failures declared on the face (G-READ-RULE-STANDING on (i) and (o), G-README-CURRENCY on README :135, G-WORKFLOW-FILES '
      'on the probe’s print step, 46 of 109 names) and five found after the seal (G-ACTROOT-BANKED, G-ANSWERS-CHECKED and the three '
      'trail-equality arms, defects (r) and (s); data/b704_checks.txt, data/b704_checks_postpush.txt); N1, N2, N4, N5 and S1–S3 HELD, N3 REFUTED '
      'at README :135 on the author’s word (data/b704_scores_close.json); the sealed tools’ hashes equal at the close, 10 of 10; the citation '
      'check 99 cites, 97 OK, 2 misses the navigator’s; nineteen defects (a)–(s), (f), (g), (k), (n) and (q) the navigator’s '
      '(data/b704_defects.txt); “13 prompts answered” the answers bank’s 12 rows and the root’s prompt, put in two calls under (q); the mirror '
      'mirror-refresh-2026-10-21-b704.zip CLEAN on all three clauses with the root line (data/b704_mirror.txt). The five post-seal items '
      'entered by this act’s corrigendum. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B704_ENTRY,
         check=[('FINDINGS.md', K.B704_ENTRY, '## The faces page at v0.37'), ('OPEN_TRAILS.md', K.B704_TRAIL, '### b704')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE ORDER W-ORD-ENTRY-TAG-PRINTS, (R315)(4)
ORDER_TAGPRINTS = (
    '*Appended 2026-10-22 by b705 beneath `W-ORD-CORRESPONDENCE-EF-REACH` (:15546), under `(R315)`(4) -- THE ORDER **`W-ORD-ENTRY-TAG-PRINTS`**, ENTERED:*',
    ' the eleven unbanked prose mentions of relay data/b704_cells_reach.txt name SIDE-explicit-formula at its entry tags v0.1 = baed4df (ch_iff_rh) '
    'and v0.2 = 5c72cad (h2_sign_iff_rh), or no tag, and no print bank holds either tag: the generator (relay tools/correspondence_gen.py) and the '
    'reader (tools/b704_record.py cellsreach) read them unbanked. THE ORDER, in the ruling’s words: the print banks at the entry tags v0.1 and '
    'v0.2, priced at one dispatch per tag from the tag’s own tree with print_targets.txt as it stood at that tag. Read at b705’s step zero: '
    'neither tag’s tree carries print_targets.txt or the workflow (both entered at b658), so a dispatch from the tag’s own tree runs no print '
    'step; the form the ruling’s price takes is for b706’s ruling -- a scratch branch cut at the tag carrying the workflow and a print list of '
    'the mentioned theorems, as b704’s probe branch carried the probe, one dispatch per tag, the branch deleted after its bank. No dispatch for '
    'it at b705. Trigger: b706. Status OPEN.')


def orders(*a):
    """the order's trail line appended to OPEN_TRAILS through b698's guarded landing beneath W-ORD-CORRESPONDENCE-EF-REACH by its line (the ledger
    is append-only); data/b705_order_tagprints.json."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', ORDER_TAGPRINTS[0], NL + ORDER_TAGPRINTS[0] + ORDER_TAGPRINTS[1] + NL)], '%s_order_tagprints.json' % ACT, 'orders', entry=None,
         check=[('OPEN_TRAILS.md', K.ORDER_EF_REACH, 'W-ORD-CORRESPONDENCE-EF-REACH'), ('OPEN_TRAILS.md', K.ORDER_README, 'W-ORD-README-FIGURE-SCOPE')], dry=dry)


# ================================================================================ COMPONENT 1: THE CARRY-TIME REPAIRS, (R315)(2)-(4), AND THEIR CONTROLS
REPAIR_ROWS = [
    ('(1) tools/b705_checks.py `root_banked_ok`, G-ACTROOT-BANKED -- ANSWERS (R315)(2)(b): b704`s predicate (tools/b704_checks.py :932-:945) required '
     'data/b704_read_calls.txt among the root`s items where the root route (tools/b698_record.py :1285-:1293, rebound at tools/b704_record.py :56-:58) '
     'excludes read banks by name -- defect (r), found after the seal. The repaired predicate reads the root bank`s items against the root route`s '
     'own item list (`route_list`, tools/b705_record.py root_banks with K rebound), admits no bank the route excludes and requires the act`s named '
     'banks. The control on b704`s banks: data/b705_repair_controls.txt.', 'b704_checks.py', 'b705_checks.py', 'root_banked_ok', ('_root_banked',)),
    ('(2) tools/b705_checks.py `answers_checked_ok`, G-ANSWERS-CHECKED -- ANSWERS (R315)(2)(c): b704`s predicate (tools/b704_checks.py :596-:611) '
     'allowed no check after the cut`s commit but the README figure`s, so the root prompt`s two checks failed it -- defect (s), found after the seal. '
     'The repaired predicate admits the checks the root prompt requires after the seal (any number, each with its time read), and holds every other '
     'check before the lock. The control on b704`s banks: data/b705_repair_controls.txt.', 'b704_checks.py', 'b705_checks.py', 'answers_checked_ok', ('_answers_checked',)),
    ('(3) tools/b705_standing_figures.py `readme`, G-README-CURRENCY -- ANSWERS (R315)(3), W-ORD-README-FIGURE-SCOPE: b703`s readme() '
     '(tools/b703_standing_figures.py :163-:183) counted every tag below the kernel`s highest as stale, the dated ceiling appends and the deposit '
     'note`s deposited versions among them -- b704`s (n), the navigator`s design. The repaired readme() reads the README`s currency rows as '
     'data/b702_readme_currency.txt registers them, the appends excluded by the append mark and the deposited versions by the Citable-deposit '
     'sentences, each excluded row printed with its reason; the baseline reset to this act`s reading. The control: data/b705_readme_control.txt.',
     'b703_standing_figures.py', 'b705_standing_figures.py', 'readme', ('deposited',)),
    ('(4) tools/b705_checks.py `wf_ok` and tools/b705_record.py `dispatch`, G-WORKFLOW-FILES -- ANSWERS (R315)(4): the probe was dispatched at the '
     'chain`s 43 modules where print_targets.txt lists 109 (b704`s (p)); the rule data/b705_rules.txt row (1) names the target print_targets.txt '
     'whole. The repaired arm requires, beside b704`s clauses, the dispatch row`s `whole` read True; the dispatch route reads the kernel`s print '
     'list, maps each name to its module by git grep bounded to the kernel`s tree, and refuses a target that does not cover them, writing `whole` '
     'into the row. The control on b704`s banks: data/b705_repair_controls.txt.', 'b704_checks.py', 'b705_checks.py', 'wf_ok', ('_wf_ok',)),
    ('(5) tools/b705_record.py `capture` and `reads` -- ANSWERS the carry (b704`s (2) again, and the author`s word at b704`s arm-baseline prompt): '
     'b704`s record tool, imported here for its repaired readers, rebinds b698`s `capture` at its import to its own, which reads b704`s session '
     '(fb68aaef); b705 runs in a new session (44411d52), so the capture is rebound to b705`s own; and `reads` takes the cap`s word as the act`s '
     'anchor, so every call counts from b705 on.', 'b704_record.py', 'b705_record.py', 'reads', ('capture',)),
]


def repairs(*a):
    """data/b705_tool_repairs.txt: the carry-time repairs, each with the order or carry it answers, its diff written by this route (difflib, the
    plain unified_diff of whole lines; the old text from the sealed tool named)."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS, (R315)(2)-(4) (%s)' % (ACT, utc()), '',
         '### rows are repairs with what they answer: the tool and its part ; what it answers ; the form. Each diff beneath its row, written by',
         '### this route (difflib over the function`s source: the sealed tool`s against this act`s; a new function printed whole). The controls',
         '### that distinguish each repaired predicate from the old one on b704`s banks: data/b705_repair_controls.txt; the README figure`s:',
         '### data/b705_readme_control.txt. No sealed tool is edited; tools/e0_rule.py`s MET list is extended at Component 4 under (R315)(9),',
         '### its diff in data/b705_e0_met.txt.', '']
    n = 0
    for text, oldf, newf, main_fn, extra in REPAIR_ROWS:
        L += ['  ' + text, '']
        old = R._fn_src(rd(os.path.join(T, oldf)), main_fn).split(NL)
        new = R._fn_src(rd(os.path.join(T, newf)), main_fn).split(NL)
        d = list(difflib.unified_diff(old, new, 'tools/%s %s (sealed)' % (oldf, main_fn), 'tools/%s %s (this act)' % (newf, main_fn), lineterm=''))
        n += len(d)
        L += ['      ' + x for x in d] + ['']
        for fn in extra:
            old2 = R._fn_src(rd(os.path.join(T, oldf)), fn).split(NL) if R._fn_src(rd(os.path.join(T, oldf)), fn) else []
            new2 = R._fn_src(rd(os.path.join(T, newf)), fn).split(NL)
            d = list(difflib.unified_diff(old2, new2, ('tools/%s %s (sealed)' % (oldf, fn)) if old2 else '(none)', 'tools/%s %s (this act)' % (newf, fn), lineterm=''))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; SHARED TOOLS EDITED 0 AT THE CARRY (e0_rule.py AT COMPONENT 4 BY RULING) ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


def repairctl(*a):
    """data/b705_repair_controls.txt: each repaired predicate and the old one run on b704's banks (a minimal source dict built from the banks, the
    keys each predicate reads), then on mutated copies, so that the repaired predicate is distinguished from the old on real state."""
    import b704_checks as C4
    import b705_checks as C5
    import b703_checks as C3
    import copy as _copy
    L = ['%s -- COMPONENT 1, (R315)(2)-(4): THE REPAIRED PREDICATES AGAINST THE OLD ON b704`S BANKS (%s)' % (ACT, utc()), '',
         '### rows are cases: the predicate | the source (b704`s banks, or a mutated copy) | the old predicate (tools/b704_checks.py) | the repaired',
         '### (tools/b705_checks.py) | wanted. Each repaired predicate is DISTINGUISHED where one row reads them apart.', '']
    cases = []
    # ### (2)(b) G-ACTROOT-BANKED on b704`s root bank
    ex704 = re.compile(R.ROOT_EXCLUDE.pattern.replace('b705_', 'b704_'))
    route704 = sorted(['data/' + f for f in os.listdir(D) if f.startswith('b704_') and os.path.isfile(os.path.join(D, f)) and not ex704.match(f)
                       and not f.endswith(('.gz', '.png', '.jsonl'))] + ['data/b675_corrigenda.txt', 'data/glossary.txt'])
    S4 = dict(REC=sys.modules[__name__], arj=jl('b704_act_root.json'), arj0=jl('b703_act_root.json'), rootsf=rdn('act_roots.txt'), art=rdn('b704_act_root.txt'),
              roots_pre=C3.cr0(C3.blob(ROOT, '295e53f0:data/act_roots.txt')), roots_now=C3.cr0(C3.raw(os.path.join(D, 'act_roots.txt'))), route_list=route704)
    req704 = ('data/b704_faces_diff.txt', 'data/b704_cut.txt', 'data/b704_corrigendum.txt')
    old = C4.root_banked_ok(S4)
    new = C5._root_banked(S4, 'b704', 81, required=req704, exclude=ex704)
    items704 = sorted(it.split()[0] for it in (S4['arj'].get('items') or []))
    L += ['### the root route`s list recomputed for b704 at HEAD against its root bank`s items: items not in the list %s ; in the list not among the items %s' % (
        sorted(set(items704) - set(route704)) or 'NONE', sorted(set(route704) - set(items704)) or 'NONE'), '']
    cases.append(('G-ACTROOT-BANKED', 'b704`s banks (data/b704_act_root.json, 91 items; the route`s list recomputed, %d)' % len(route704), old, new, (False, True)))
    S4m = dict(S4, arj=_copy.deepcopy(S4['arj']))
    S4m['arj']['items'] = S4m['arj']['items'] + ['data/b704_read_calls.txt ' + '0' * 64]
    cases.append(('G-ACTROOT-BANKED', 'a mutated copy, data/b704_read_calls.txt planted among the items (a bank the route excludes)', C4.root_banked_ok(S4m),
                  C5._root_banked(S4m, 'b704', 81, required=req704, exclude=ex704), (False, False)))
    # ### (2)(c) G-ANSWERS-CHECKED on b704`s citation bank
    face4 = rd(os.path.join(ROOT, *K.B704_FACE.split('/')))
    ot = rd(OT)
    S4 = dict(citation=rdn('b704_citation_check.txt'), t=dict(c4pp=C3._ct(PP, '02b7aad')), lock_epoch=C3.utc_epoch(face4, 'locked at (UTC)'),
              order_readme=((jl('b704_order_readme.json').get('lines') or [{}])[0]), ot=ot, face=face4)
    cmds4 = []
    S4['probe_branch_ts'] = C3.iso_epoch('2026-10-22T04:15:19Z')
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', S4['citation'])
    rootc = C5.root_checks(S4)
    old = C4.answers_checked_ok(S4)
    new = C5._answers_checked(S4, 12, act=704)
    cases.append(('G-ANSWERS-CHECKED', 'b704`s banks (data/b704_citation_check.txt, %d checks; the root prompt`s after the lock, each with its time: %s)' % (
        len(stamps), '; '.join('%s at %s' % (n_, t_) for t_, n_ in rootc)), old, new, (False, True)))
    S4m = dict(S4, citation=S4['citation'].replace('-- RAISED: data/b705_tool_repairs.txt', '-- RAISED: data/b703_tool_repairs.txt'))
    assert S4m['citation'] != S4['citation']
    cases.append(('G-ANSWERS-CHECKED', 'a mutated copy, a check`s one miss naming an earlier act`s bank instead of a later act`s', C4.answers_checked_ok(S4m),
                  C5._answers_checked(S4m, 12, act=704), (False, False)))
    # ### (4) G-WORKFLOW-FILES on b704`s probe
    wf4 = C4.wf_state()
    S4 = dict(wf=wf4, dispj=jl('b704_dispatches.json'), rules=rdn('b705_rules.txt'))
    old = C4.wf_ok(S4)
    new = C5._wf_ok(S4, 'SIDE-explicit-formula')
    cases.append(('G-WORKFLOW-FILES', 'b704`s banks (the probe: targets %d, printed %d, the dispatch at %d modules)' % (len(wf4['SIDE-explicit-formula']['targets']), wf4['SIDE-explicit-formula']['printed'],
                                                                                                                         len(((jl('b704_dispatches.json').get('rows') or [{}])[0].get('target') or '').split())), old, new, (False, False)))
    S4m = _copy.deepcopy(S4)
    S4m['wf']['SIDE-explicit-formula']['printed'] = len(wf4['SIDE-explicit-formula']['targets'])
    cases.append(('G-WORKFLOW-FILES', 'a mutated copy, the print bank read as printing every listed name, the dispatch still at the chain`s 43 modules (not whole)', C4.wf_ok(S4m),
                  C5._wf_ok(S4m, 'SIDE-explicit-formula'), (True, False)))
    S4m2 = _copy.deepcopy(S4m)
    S4m2['dispj']['rows'][0]['whole'] = True
    cases.append(('G-WORKFLOW-FILES', 'a mutated copy, every name printed and the dispatch row marked whole', C4.wf_ok(S4m2), C5._wf_ok(S4m2, 'SIDE-explicit-formula'), (True, True)))
    ok = True
    for name, src, o, nw, want in cases:
        asw = (bool(o), bool(nw)) == want
        ok = ok and asw
        L.append('  %-20s | %s | old %-5s | repaired %-5s | wanted old %s, repaired %s | %s' % (name, src, o, nw, want[0], want[1], 'AS WANTED' if asw else '### NOT AS WANTED'))
    dist = [n_ for n_, _s, o, nw, _w in cases if bool(o) != bool(nw)]
    L += ['', '### ### **CASES %d ; AS WANTED %s ; EACH REPAIRED PREDICATE DISTINGUISHED FROM THE OLD ON A ROW: %s.**' % (len(cases), ok, sorted(set(dist)))]
    put_txt('%s_repair_controls.txt' % ACT, L)
    print(NL.join(L[5:]))


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, armsort=armsort, figures=figures, figctl=figctl, c1=c1,
              orders=orders, repairs=repairs, repairctl=repairctl)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b705_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
