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


# ================================================================================ COMPONENT 2: THE JOIN KERNEL, (R315)(5)
KI = K.KERNEL_DIR
JOIN_FILES = ('lean-toolchain', 'lakefile.toml', 'FacesJoin.lean', 'print_targets.txt', '.github/workflows/build-module.yml', 'README.md', '.gitignore')


def _blob_sha(repo, rev, path):
    return g(repo, 'rev-parse', '%s:%s' % (rev, path)).strip()


def joinfiles(*a):
    """data/b705_join_files.txt: the join kernel's files at its commit, printed whole before the push ((R315)(5): "its lakefile and workflow printed
    before the push"), each with its blob id; the workflow's blob against SIDE-explicit-formula's at main (carried verbatim); the two pins and
    the two requirements read from the lakefile; no identifier of the author in any file (the needles of tools/b705_checks.py IDENT_WF)."""
    import b705_checks as C5
    tip = g(KI, 'rev-parse', 'HEAD').strip()
    L = ['%s -- COMPONENT 2, (R315)(5): THE JOIN KERNEL %s AT ITS COMMIT %s, ITS FILES PRINTED BEFORE THE PUSH (%s)' % (ACT, K.KERNEL, tip[:7], utc()), '',
         '### rows are files at the commit: the path | its blob id | its bytes; each printed whole beneath. The workflow carried verbatim from',
         '### SIDE-explicit-formula`s .github/workflows/build-module.yml at main (blob %s); the lakefile requiring Mathlib at explicit-formula`s pin,' % _blob_sha(K.EF_DIR, 'main', '.github/workflows/build-module.yml')[:12],
         '### SIDE-explicit-formula at v0.37 = %s and SIDE-lv-conservation at v0.10.0 = %s by git revision; nothing of either kernel edited.' % (K.EF_V037[:7], K.LV_V0100[:7]), '']
    ident = []
    for f in JOIN_FILES:
        t = _show(KI, tip, f) or ''
        hits = [w for w in C5.IDENT_WF if w in t.lower() and not (w == 'psinary' and f in ('lakefile.toml',))]
        ident += [(f, w) for w in hits]
        L += ['  %-40s blob %s ; %d bytes%s' % (f, _blob_sha(KI, tip, f)[:12], len(t.encode('utf-8')), (' ; ### IDENTIFIER NEEDLE %s' % hits) if hits else '')]
    for f in JOIN_FILES:
        t = _show(KI, tip, f) or ''
        L += ['', '=== %s' % f] + ['    ' + x for x in t.rstrip(NL).split(NL)]
    wf_eq = _blob_sha(KI, tip, '.github/workflows/build-module.yml') == _blob_sha(K.EF_DIR, 'main', '.github/workflows/build-module.yml')
    lf = _show(KI, tip, 'lakefile.toml') or ''
    pins = ('rev = "%s"' % K.EF_MATHLIB in lf, 'rev = "%s"' % K.EF_V037 in lf, 'rev = "%s"' % K.LV_V0100 in lf, (_show(KI, tip, 'lean-toolchain') or '').strip() == K.EF_LEAN)
    L += ['', '### ### **FILES %d AT %s ; THE WORKFLOW`S BLOB EQUAL TO SIDE-explicit-formula`S AT MAIN %s ; MATHLIB %s, SIDE-explicit-formula v0.37 %s, SIDE-lv-conservation v0.10.0 %s REQUIRED BY REVISION ; '
          'THE TOOLCHAIN v4.34.0-rc1 %s ; IDENTIFIER NEEDLES IN THE WORKFLOW OR THE MODULE %s.**' % (
              len(JOIN_FILES), tip[:7], wf_eq, pins[0], pins[1], pins[2], pins[3], [x for x in ident if x[0] in ('.github/workflows/build-module.yml', 'FacesJoin.lean')] or 'NONE')]
    put_txt('%s_join_files.txt' % ACT, L)
    put_json('%s_join_files.json' % ACT, dict(at=utc(), tip=tip, workflow_equal=wf_eq, pins=list(pins), blobs=dict((f, _blob_sha(KI, tip, f)) for f in JOIN_FILES)))
    print(NL.join(L[:12] + L[-1:]))


def _print_modules(kernel_dir, rev='HEAD'):
    """each name of the kernel's print_targets.txt mapped to the module declaring it, by git grep bounded to the kernel's tree at rev: the
    declaration line `theorem|def|structure|abbrev <short>` in a .lean file -> the module (the path with / for . and no .lean)."""
    names = [l.strip() for l in (_show(kernel_dir, rev, 'print_targets.txt') or '').split(NL) if l.strip()]
    out = {}
    for n in names:
        short = n.split('.')[-1]
        hit = g(kernel_dir, 'grep', '-n', '-E', '-e', r'^(@\[[^]]*\] *)?((private|protected|noncomputable|nonrec) +)*(theorem|lemma|def|abbrev|structure|instance) +%s([ :({\[]|$)' % re.escape(short),
                rev, '--', '*.lean').strip()
        f = hit.split(':', 2)[1] if hit.count(':') >= 2 else ''
        out[n] = f[:-5].replace('/', '.') if f.endswith('.lean') else None
    return out


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: b698's dispatch (one dispatch per tree state, the run id read), with (R315)(4) applied --
    data/b705_rules.txt row (1): the target is the print list whole. Before the dispatch every name of print_targets.txt is mapped to its module
    by git grep bounded to the kernel's tree; a target not covering every module is REFUSED, nothing dispatched; the row banked carries `whole`
    True with the modules the list needs."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    mods = _print_modules('D:/' + kernel, ref)
    need = sorted(set(m for m in mods.values() if m))
    unmapped = [n for n, m in mods.items() if not m]
    tgt = target.split()
    whole = bool(need) and not unmapped and all(m in tgt for m in need)
    print('  the print list %d names ; their modules %s ; unmapped %s ; the target %s ; whole %s' % (len(mods), need, unmapped or 'NONE', tgt, whole))
    if not whole:
        sys.exit('### THE TARGET DOES NOT COVER THE PRINT LIST`S MODULES (data/b705_rules.txt row (1)) -- NOT DISPATCHED')
    R.dispatch(*a)
    if 'dry' in a[4:]:
        return
    j = jl('%s_dispatches.json' % ACT)
    rows = j.get('rows') or []
    if rows:
        rows[-1].update(whole=True, print_names=len(mods), print_modules=need)
        put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  the row banked with whole True ; modules %s' % need)


E0_PIN = 'SIDE-explicit-formula v0.36 = dfadc8c (H2SignWide.lean blob 0ff5c255, equal at v0.37 = 38e2734 and in the working tree)'
E0_NEW = {'acDeriv': ('prop', E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :28'),
          "classK'": ('prop', E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :33'),
          'classKsum': ('prop', E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :43')}
E0_RESTRICT = [dict(head='classK', where='SIDE-explicit-formula v0.36 = dfadc8c, SIDEExplicitFormula/H2Sign.lean :24',
                    reads='even, C^2, compactly supported, an autocorrelation h * h~ of such h -- a condition on k alone', restricts=('k',)),
               dict(head='classKsum', where=E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :43',
                    reads='even, C^2, compactly supported, a finite sum of autocorrelations of C^2 compactly supported h_i -- a condition on k alone',
                    restricts=('k',)),
               dict(head="classK'", where=E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :33',
                    reads='even, acDeriv, compactly supported, a finite sum of autocorrelations of acDeriv compactly supported h_i -- a condition on k alone',
                    restricts=('k',)),
               dict(head='acDeriv', where=E0_PIN + ', SIDEExplicitFormula/H2SignWide.lean :28',
                    reads='C^1 with the derivative an indefinite integral of an integrable g -- a condition on f alone', restricts=('f',))]


def _e0_heads():
    """the headers of data/b703_widening_grade.txt (rows '== name (file :a-:b):' then the statement verbatim to '  THE BINDERS')."""
    import io as _io
    import re as _re
    L = _io.open(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'b703_widening_grade.txt'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    out, i = [], 0
    while i < len(L):
        if L[i].startswith('== '):
            name, j, stmt = L[i][3:].split(' (')[0], i + 1, []
            while j < len(L) and not L[j].startswith('  THE BINDERS'):
                stmt.append(L[j].strip())
                j += 1
            s = ' '.join(stmt).split(':=')[0]
            out.append((name, _re.sub(r'^theorem\s+\S+\s*', '', s).strip()))
            i = j
        else:
            i += 1
    return out


def _e0_all(E, heads):
    rows = []
    for name, head in heads:
        try:
            g, why, _r = E.grade(head, 'theorem')
        except Exception as e:
            g, why = 'BUG', str(e)[:100]
        rows.append(dict(name=name, grade=g, why=why))
    return rows


def _e0_sha():
    import hashlib as _h
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'e0_rule.py')
    return _h.sha256(open(p, 'rb').read()).hexdigest()


def _wjson(name, obj):
    raw = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', name)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(raw)
    os.replace(p + '.tmp', p)


def e0met(*a):
    """`e0met before | variants | after`: (R315)(9)'s control. `before`: every header of data/b703_widening_grade.txt graded by the shared
    tools/e0_rule.py as it stands, banked with the file's sha256. `variants`: the same headers graded under in-memory variants of the rule
    (MET + the three names; RESTRICTIONS + the four heads; LEXICON + the three), the file unedited, the table banked -- the evidence for
    the prompt where the ruling's mechanism and the rule's own words part. `after`: the headers re-graded after the Edit, the before/after
    diff per name and the file's diff banked as data/b705_e0_met.txt."""
    import e0_rule as E
    stage = a[0]
    heads = _e0_heads()
    if stage == 'before':
        rows = _e0_all(E, heads)
        _wjson('%s_e0_met_before.json' % ACT, dict(at=utc(), e0_rule_sha256=_e0_sha(), rows=rows))
        for r in rows:
            print('  %-28s %-20s %s' % (r['name'], r['grade'], r['why'][:90]))
        print('### BEFORE: %d headers ; tools/e0_rule.py sha256 %s' % (len(rows), _e0_sha()[:16]))
        return
    if stage == 'variants':
        base = _e0_all(E, heads)
        met0, res0, lex0 = E.MET, list(E.RESTRICTIONS), dict(E.LEXICON)
        V = {}
        try:
            E.MET = met0 + tuple(E0_NEW)
            V['MET+3'] = _e0_all(E, heads)
            E.MET = met0
            E.RESTRICTIONS = res0 + E0_RESTRICT
            V['RESTRICTIONS+4'] = _e0_all(E, heads)
            E.RESTRICTIONS = res0
            E.LEXICON.update(E0_NEW)
            V['LEXICON+3'] = _e0_all(E, heads)
            E.LEXICON.clear()
            E.LEXICON.update(lex0)
            E.MET = met0 + tuple(E0_NEW)
            E.RESTRICTIONS = res0 + E0_RESTRICT
            E.LEXICON.update(E0_NEW)
            V['ALL THREE'] = _e0_all(E, heads)
        finally:
            E.MET, E.RESTRICTIONS = met0, res0
            E.LEXICON.clear()
            E.LEXICON.update(lex0)
        names = list(V)
        L = ['%s -- (R315)(9): E0`S READING OF data/b703_widening_grade.txt`S HEADERS UNDER IN-MEMORY VARIANTS OF THE RULE, THE FILE UNEDITED (%s)' % (ACT, utc()), '',
             '### rows are headers: name | the rule as it stands (sha256 %s) | ' % _e0_sha()[:16] + ' | '.join(names),
             '### MET+3: MET extended with %s ; RESTRICTIONS+4: named restrictions %s on their variable ; LEXICON+3: the three as Props with their lines.' % (
                 sorted(E0_NEW), [r['head'] for r in E0_RESTRICT]), '']
        for k, r in enumerate(base):
            L.append('  %-28s | %-20s | ' % (r['name'], r['grade']) + ' | '.join('%-20s' % V[n][k]['grade'] for n in names))
        L += ['', '### the rule`s own words on a MET name (tools/e0_rule.py FORMS, `met`): "a named predicate on quantified variables that MET holds',
              '### -- the forward guard (OPEN_TRAILS :13221), a premise until the author rules the name a restriction" -> outcome `premise` -> INTERFACES.']
        put_txt('%s_e0_met_variants.txt' % ACT, L)
        print(NL.join(L[2:]))
        return
    if stage == 'after':
        before = jl('%s_e0_met_before.json' % ACT)
        rows = _e0_all(E, heads)
        B = dict((r['name'], r) for r in before['rows'])
        changed = [(r['name'], B[r['name']]['grade'], r['grade']) for r in rows if B.get(r['name'], {}).get('grade') != r['grade']]
        out = subprocess.run(['git', 'diff', '--', 'tools/e0_rule.py'], cwd=ROOT, capture_output=True).stdout
        diff = (out or b'').decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL).split(NL)
        L = ['%s -- (R315)(9), W-ORD-E0-MET-CLASSK: tools/e0_rule.py EXTENDED BY THE EDIT TOOL, E0`S READING OF data/b703_widening_grade.txt`S HEADERS BEFORE AND AFTER (%s)' % (ACT, utc()), '',
             '### rows are headers: name | before (tools/e0_rule.py sha256 %s, %s) | after (sha256 %s) | changed' % (before['e0_rule_sha256'][:16], before['at'], _e0_sha()[:16]), '']
        for r in rows:
            L.append('  %-28s | %-20s | %-20s | %s' % (r['name'], B.get(r['name'], {}).get('grade'), r['grade'], 'CHANGED' if B.get(r['name'], {}).get('grade') != r['grade'] else 'unchanged'))
        L += ['', '### CHANGED %d: %s' % (len(changed), changed or 'NONE'), '', '### THE FILE`S DIFF (git diff -- tools/e0_rule.py, %d lines):' % len(diff)] + ['    ' + l for l in diff]
        L += ['', '### ### **HEADERS %d ; CHANGED BY THE EXTENSION %d %s ; EVERY OTHER NAME UNCHANGED %s.**' % (
            len(rows), len(changed), [c[0] for c in changed], all(B.get(r['name'], {}).get('grade') == r['grade'] for r in rows if r['name'] not in [c[0] for c in changed]))]
        put_txt('%s_e0_met.txt' % ACT, L)
        _wjson('%s_e0_met.json' % ACT, dict(at=utc(), before=before, after=dict(e0_rule_sha256=_e0_sha(), rows=rows), changed=changed, diff=diff))
        print(NL.join(L[2:4 + len(rows) + 2] + L[-1:]))
        return
    sys.exit('usage: e0met before | variants | after')


def artfile(*a):
    """`artfile <kernel> <run id> <label> <name> [<name> ...]`: a named file of the run's artifact, read only after the artifact's sha256 equals
    the banked one (data/b705_runner_rows.json, the row read by its id) and the platform's digest; banked as data/b705_art_<kernel>_<label>_<name>.txt."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, label, names = a[0], int(a[1]), a[2], list(a[3:])
    repo = 'psinary-sketch/' + kernel
    row = next((r for r in (jl('%s_runner_rows.json' % ACT).get('rows') or []) if r.get('kernel') == kernel and r.get('run_id') == run_id), None)
    if not row or not row.get('artifact_sha256'):
        sys.exit('### THE RUN IS NOT BANKED WITH AN ARTIFACT SHA256 -- NOTHING READ')
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    art = (json.loads(out or b'{}').get('artifacts') or [{}])[0]
    rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
    sha = hashlib.sha256(rz.stdout).hexdigest()
    if sha != row['artifact_sha256'] or sha != (art.get('digest') or '').replace('sha256:', ''):
        sys.exit('### THE ARTIFACT`S SHA256 %s IS NOT THE BANKED %s -- NOTHING READ' % (sha[:16], row['artifact_sha256'][:16]))
    with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
        have = z.namelist()
        for n in names:
            t = z.read(n).decode('utf-8', 'replace').replace(chr(13), '') if n in have else '### NOT IN THE ARTIFACT (%s)' % have
            L = ['%s -- THE RUN %d (%s, %s) ARTIFACT`S %s, READ AFTER THE ARTIFACT`S SHA256 %s AGREED WITH THE BANKED AND THE PLATFORM`S (%s)' % (ACT, run_id, kernel, label, n, sha[:16], utc()), ''] + t.rstrip(NL).split(NL)
            put_txt('%s_art_%s_%s_%s.txt' % (ACT, kernel, label, n.replace('/', '_').replace('.', '_')), L)
            print(NL.join(L))


JOIN_GRADES = {'faces_join': ('FacesJoin.lean', '', [], 'DERIVES',
                              'NONE (no binder; an equivalence of two closed propositions, each kernel`s own, through Mathlib`s RiemannHypothesis)')}
JOIN_E0 = {'h2_sign': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2Sign.lean :29'),
           'Register4_positivity': ('prop', 'SIDE-lv-conservation SIDELvConservation/RegisterPentagon.lean :152 at v0.10.0'),
           'LiCoeff': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/LiWeil.lean :243'),
           'RiemannHypothesis': ('prop', 'Mathlib RiemannHypothesis')}


def joingrade(*a):
    """`joingrade <label>`: data/b705_join_grade.txt (.json) -- faces_join's statement verbatim from the kernel at its commit, the seat's reading of
    its binders by hand (none) and the grade it gives, the shared E0 rule's grade as the check (its lexicon extended here, the shared file not
    edited at this step), the salt-check of REGISTRY.md :544 clause by clause, the runner's print of the name (b703's grade route, its readers
    _thm_sig and _self_eq imported); on a run that is not DERIVES, the build's error lines printed by line and the join HELD."""
    import e0_rule as E
    label = a[0] if a else 'join'
    E.LEXICON.update(JOIN_E0)
    rows_ = jl('%s_runner_rows.json' % ACT).get('rows') or []
    run = next((r for r in reversed(rows_) if r.get('kernel') == K.KERNEL and r.get('label') == label), None)
    ax = rdn('%s_axioms_%s_%s.txt' % (ACT, K.KERNEL, label)) if run else ''
    AX = dict(_deps(ax))
    tip = g(KI, 'rev-parse', 'HEAD').strip()
    L = ['%s -- COMPONENT 2, (R315)(5): THE GRADE OF faces_join, READ FROM ITS STATEMENT, WITH E0 AND THE SALT-CHECK BESIDE IT (%s)' % (ACT, utc()), '',
         '### rows are, per theorem: the statement verbatim, the binders with their class read by hand, the grade they give, the E0 rule`s check, and',
         '### the salt-check`s clauses with their readings. The statement at %s %s; the profile from run %s (gate %s).' % (
             K.KERNEL, tip[:7], run['run_id'] if run else '### NO RUN', run['gate'] if run else '-'), '']
    allok, summ = True, []
    for name, (fpath, ns, hand, hgrade, hprem) in JOIN_GRADES.items():
        i, j, head, st = P3._thm_sig(_show(KI, tip, fpath), name)
        eg, why, read = E.grade(' ' + head + ' ', 'theorem')
        prof = AX.get(ns + name)
        concl = E.conclusion(E.statement_only(' ' + head + ' ')) or head
        salt = [('no True-typed conclusion, no uniformly-True predicate', not re.search(r'\bTrue\b', concl), 'the conclusion %r' % concl.strip()[:120]),
                ('no X = X', not P3._self_eq(concl), 'no equation of a term with itself in the conclusion (its two whole sides compared)'),
                ('no hypothesis that is the claim', all(concl.strip() not in (t or '') for _n, t in read) if read else True, 'hypotheses %s' % ([n for n, _t in read] or 'none')),
                ('no fabricated witness', '∃' not in concl, 'the conclusion constructs nothing' if '∃' not in concl else 'an existential in the conclusion'),
                ('hypotheses named', all(n for n, _t in read) if read else True, ', '.join('%s : %s' % x for x in read) or 'no binder'),
                ('#print axioms profiled after the first three', prof is not None and set(prof) <= set(STD3), 'run %s: %s' % (run['run_id'] if run else '### NO RUN', prof)),
                ('the terminal states lv-conservation`s own declaration, no restatement in the module (N2)',
                 'SIDELvConservation.RegisterPentagon.Register4_positivity' in head and 'def Register4_positivity' not in (_show(KI, tip, fpath) or ''),
                 'the right-hand side names SIDELvConservation.RegisterPentagon.Register4_positivity; the module defines no Register4_positivity')]
        ok = all(s[1] for s in salt)
        allok = allok and ok and eg == hgrade
        L += ['== %s (%s :%d-:%d):' % (name, fpath, i, j)] + ['    ' + l for l in st.split(NL)]
        L += ['  THE BINDERS, READ BY HAND (the seat`s reading, before the check): %s' % ('NONE -- a closed statement' if not hand else '')]
        L += ['    %-12s : %-34s %s' % b for b in hand]
        L += ['  THE GRADE READ FROM THE STATEMENT: %s ; THE NAMED PREMISE: %s' % (hgrade, hprem),
              '  THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (JOIN_E0; the shared file not edited at this step):',
              '    E0 GRADE %s ; its reason: %s ; the hypotheses it read: %s' % (eg, why, read),
              '    THE HAND READING AND THE CHECK %s' % ('AGREE' if eg == hgrade else '### DIFFER (%s against %s)' % (hgrade, eg)),
              '  THE SALT-CHECK (REGISTRY.md :544), clause by clause:']
        L += ['    %-85s %s -- %s' % (c, 'PASS' if ok_ else '### FAIL', how) for c, ok_, how in salt]
        L += ['  PROFILE %s ; SALT-CHECK %s' % (prof, 'PASS' if ok else '### FAIL'), '']
        summ.append('%s GRADE %s (E0 %s) SALT %s PROFILE %s' % (name, hgrade, eg, 'PASS' if ok else 'FAIL', 'STD3' if prof is not None and set(prof) <= set(STD3) else prof))
    gate = (run or {}).get('gate')
    held = gate != 'DERIVES'
    if held:
        L += ['== THE JOIN HELD: the run`s gate %s ; the build`s error lines, by line (relay data/%s_buildlog_%s_%s.txt):' % (gate, ACT, K.KERNEL, label)]
        L += ['    ' + x for x in ((run or {}).get('errors') or ['### NO RUN READ'])[:60]]
        L += ['   the author`s word at the join-name prompt: a composition that does not close against lv`s declaration is banked by line and the join holds, that mismatch the finding.', '']
    L += ['### ### **THEOREMS %d ; %s ; THE GATE %s ; THE JOIN %s ; EVERY SALT-CHECK PASSED AND EVERY CHECK AGREEING %s.**' % (
        len(JOIN_GRADES), ' ; '.join(summ), gate or '### NO RUN', 'HELD' if held else 'DERIVES AT THE STANDARD THREE', allok)]
    put_txt('%s_join_grade.txt' % ACT, L)
    put_json('%s_join_grade.json' % ACT, dict(at=utc(), tip=tip, run=run['run_id'] if run else None, gate=gate, held=held, ok=allok and not held, rows=summ))
    print(NL.join(L[-4:]))


# ================================================================================ COMPONENT 5 AND 6: THE SCORES, THE RECORD, THE TRAIL, THE DRY RUN (b704's form, b705's content)
EF = K.EF_DIR
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
N5_RELAY_DATA = R.N5_RELAY_DATA
_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
num_word = P3.num_word
_trail_defects, _trail_resolved = P3._trail_defects, P3._trail_resolved


def _jgz(name):
    import gzip
    try:
        return json.loads(gzip.decompress(open(os.path.join(D, name), 'rb').read()).decode('utf-8'))
    except Exception:
        return {}


def _bank_utc(text):
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', NL.join((text or '').split(NL)[:2]))
    return _iso_epoch(m.group(1)) if m else None


def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _n1():
    """N1: no lean process on this host; one runner dispatch, the join kernel's, read by its run id with its artifact's sha256 verified."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    rr = [r for r in (jl('%s_runner_rows.json' % ACT).get('rows') or []) if r.get('kernel') == K.KERNEL]
    art = rdn('%s_art_%s_join_cache_log.txt' % (ACT, K.KERNEL))
    sha = (rr[0].get('artifact_sha256') or '') if rr else ''
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == 1 and len(dj) == 1 and dj[0].get('ref') == K.JOIN_TIP \
        and dj[0].get('run_id') == K.JOIN_RUN and len(rr) == 1 and rr[0].get('run_id') == K.JOIN_RUN and bool(re.match(r'^[0-9a-f]{64}$', sha)) \
        and ('AGREED WITH THE BANKED AND THE PLATFORM`S' in art) and dj[0].get('whole') is True
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches in the capture: %s (relay data/b705_commands.json); the '
        'dispatches bank (relay data/b705_dispatches.json): %s -- the join kernel`s one commit, its run, whole by data/b705_rules.txt row (1), the run '
        'read by its id, its artifact`s sha256 %s (relay data/b705_runner_rows.json), the artifact`s cache log read after it agreed; the join held, so '
        'no second dispatch' % (cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread',
                                ['%s run %s whole %s' % ((d.get('ref') or '')[:7], d.get('run_id'), d.get('whole')) for d in dj], sha[:16] or 'UNREAD'))


def _n2():
    """N2: the join's terminal states lv-conservation's own Register4_positivity, no restatement; its grade DERIVES at the standard three, or the
    act holds the join with the error banked."""
    jg = jl('%s_join_grade.json' % ACT)
    t = rdn('%s_join_grade.txt' % ACT)
    mod = _show(KI, K.JOIN_TIP, 'FacesJoin.lean') or ''
    errs = [l for l in rdn('%s_buildlog_%s_join.txt' % (ACT, K.KERNEL)).split(NL) if l.startswith('error:')]
    states = 'SIDELvConservation.RegisterPentagon.Register4_positivity SIDEExplicitFormula.LiWeil.LiCoeff' in mod and 'def Register4_positivity' not in mod
    n2 = re.search(r'no restatement in the module \(N2\) PASS', t) is not None
    tag = g(KI, 'tag', '--list', K.JOIN_TAG).strip()
    held = jg.get('held') is True and jg.get('gate') == 'NOT DERIVES' and '== THE JOIN HELD' in t and len(errs) >= 1 and tag == ''
    derives = jg.get('held') is False and jg.get('gate') == 'DERIVES' and tag != ''
    ok = states and n2 and (held or derives)
    return ('HELD' if ok else 'REFUTED'), (
        'faces_join states lv-conservation`s own declaration against h2_sign: %s, the N2 salt clause %s (relay data/b705_join_grade.txt); the run`s '
        'gate %s, the join %s, the build`s error lines banked %d (relay data/b705_buildlog_SIDE-faces-join_join.txt), its cause read from the run`s '
        'own artifact (data/b705_art_SIDE-faces-join_join_cache_log.txt: Mathlib`s dependencies resolved from lv-conservation`s manifest, the cache '
        'not served, FacesJoin.lean never reached; defect (j)); the tag %s: %s; no second dispatch' % (
            states, 'PASS' if n2 else 'FAIL', jg.get('gate'), 'HELD' if jg.get('held') else 'DERIVES', len(errs), K.JOIN_TAG, tag or 'NOT MADE'))


def _n3():
    """N3: the contour bank committed before any Q0 figure is printed; every registration computed read from data/b703_registrations.txt as
    committed at b703, unchanged; the sign-onset registration committed before any radius is computed."""
    stepz = _git_ct(ROOT, K.STEPZERO_BANKS)
    dc, wc = _bank_utc(rdn('%s_detection_controls.txt' % ACT)), _bank_utc(rdn('%s_window_controls.txt' % ACT))
    contour_in = 'data/b705_contour.txt' in _files_of(ROOT, K.STEPZERO_BANKS)
    first = bool(stepz) and dc is not None and wc is not None and stepz < dc and stepz < wc and contour_in
    log703 = g(ROOT, 'log', '--format=%h', '--', 'data/b703_registrations.txt').strip()
    st703 = g(ROOT, 'status', '--porcelain', '--', 'data/b703_registrations.txt').strip()
    eq703 = g(ROOT, 'rev-parse', 'HEAD:data/b703_registrations.txt').strip() == g(ROOT, 'rev-parse', 'b8a36309:data/b703_registrations.txt').strip()
    unchanged = log703 == 'b8a36309' and st703 == '' and eq703
    regs_files = _files_of(ROOT, K.C4_REGS)
    regs_t, rank_t, src_t = _git_ct(ROOT, K.C4_REGS), _git_ct(ROOT, K.C4_RELAY), _git_ct(ROOT, K.C4_SRC)
    regs = rdn('%s_registrations.txt' % ACT)
    alone = regs_files == ['data/b705_registrations.txt'] and bool(regs_t) and bool(rank_t) and bool(src_t) and src_t < regs_t < rank_t \
        and 'NO RADIUS COMPUTED' in regs and '(iii) THE SIGN-ONSET RADIUS AT Q0 -- COMPUTED AT b707' in regs
    ok = first and unchanged and alone
    return ('HELD' if ok else 'REFUTED'), (
        'the contour bank in the step-zero commit %s (%s) and that commit before the detection controls (%s) and the window controls (%s): %s (relay '
        'data/b705_contour.txt); data/b703_registrations.txt at its one commit %s, the tree clean %s, HEAD`s blob b703`s %s; data/b705_registrations.txt '
        'committed alone (%s, files %s) after the source`s commit %s and before the ranking`s %s: %s, no radius computed' % (
            K.STEPZERO_BANKS, contour_in, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(dc)) if dc else '-',
            R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(wc)) if wc else '-', first, log703 or 'UNREAD', st703 == '', eq703,
            K.C4_REGS, regs_files, K.C4_SRC, K.C4_RELAY, alone))


def _n4():
    """N4: the detection law's controls reproduce b675's figure at rho_0 and zeta's nonnegativity through the largest predicted n*; the window's
    sign at the band zero printed per width with its term anatomy; every falsifier read and printed HELD or REFUTED."""
    dc, dt = rdn('%s_detection_controls.txt' % ACT), rdn('%s_detection.txt' % ACT)
    wt = rdn('%s_window.txt' % ACT)
    dj, wj = _jgz('%s_detection.json.gz' % ACT), _jgz('%s_window.json.gz' % ACT)
    c1 = 'C1: n*(rho0) BY b675`S ROUTE 63676 AGAINST b675`S 63676, EQUAL True' in ' '.join(dc.split())
    c2 = 'C2 NONNEGATIVE True' in ' '.join(dt.split()) and 'NONNEG (VACUOUS by algebra' in dt
    fals_d = re.search(r'THE REGISTRATION`S HYPOTHESIS: (HELD|REFUTED|NOT SCORABLE) over the pairs computed', dt)
    widths = wj.get('widths') or []
    per_width = all(('  %-4s | P ' % w) in wt for w in widths) and wt.count('THE MOVER') >= 2 * len(widths)
    fals_w = re.search(r'THE REGISTRATION`S HYPOTHESIS \(the notched window at the band zero reads a witness\): (HELD|REFUTED|UNDECIDED)', wt)
    ok = c1 and c2 and bool(fals_d) and fals_d.group(1) in ('HELD', 'REFUTED') and dj.get('verdict') == fals_d.group(1) and bool(widths) and per_width \
        and bool(fals_w) and fals_w.group(1) in ('HELD', 'REFUTED') and wj.get('verdict') == fals_w.group(1)
    return ('HELD' if ok else 'REFUTED'), (
        'C1 at rho_0 by b675`s route equal to b675`s 63676: %s; C2 zeta nonnegative through the largest predicted n* (%s): %s, vacuous by algebra '
        '(relay data/b705_detection_controls.txt); the detection law`s falsifier read %s over %s pairs computed, %s beyond reach (relay '
        'data/b705_detection.json.gz); the window`s sign printed at %d widths with P, PR and A at Q0 and at zeta and b694`s at rho_0 beside, the mover '
        'named per width, negative at %s, its falsifier %s, the hypothesis %s (relay data/b705_window.json.gz)' % (
            c1, (dj.get('controls') or {}).get('C2', {}).get('at_largest', ['-'])[0] if isinstance((dj.get('controls') or {}).get('C2'), dict) else '-', c2,
            fals_d.group(1) if fals_d else 'UNREAD', dj.get('computed'), len(dj.get('beyond') or []), len(widths), wj.get('negative_at'),
            'NOT FIRED' if wj.get('falsifier_fired') is False else ('FIRED' if wj.get('falsifier_fired') else 'UNREAD'), fals_w.group(1) if fals_w else 'UNREAD'))


def _n5():
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    main_ok = ef_main == K.EF_V037 and not g(EF, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    join_tags = g(KI, 'tag', '--list').strip()
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b705_', x) and x not in ['tools/' + t for t in K.REPAIRED_TOOLS]]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b705_|audit_b705_)', x) or re.match(r'^data/terminal_table', x)
                                                or x in ['tools/' + t for t in K.REPAIRED_TOOLS] or (x.startswith('data/') and x[5:] in N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B704_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(EF, lock) + _amended_after(KI, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    src_tool = rd(os.path.join(T, 'b705_cc_source.py'))
    fetch_ok = "'User-Agent': 'Mozilla/5.0'" in src_tool and not any(w in src_tool.lower() for w in ('psinary', 'seale', 'hotmail', 'orcid'))
    wf = _show(KI, K.JOIN_TIP, '.github/workflows/build-module.yml') or ''
    wf_ok = bool(wf) and not any(w in wf.lower() for w in ('psinary', 'seale', 'york', 'hotmail', 'orcid', 'secrets.'))
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    ok = k_ok and main_ok and join_tags == '' and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ and arms_ok \
        and not amended and not ident and fetch_ok and wf_ok and not chained and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-explicit-formula`s '
            'main at v0.37 and no tag past it: %s; the join kernel`s tags: %s; the standing arms added beyond b704`s face, the act arms apart: %s (%s); '
            'shared tools edited beyond the one the ruling names (tools/e0_rule.py, (R315)(9)): %s; sealed tools not agreeing: %s; commits amended '
            'after the seal: %s; deletes with anything chained after: %s; one git write per message (%s): %s; PLACE-papers beyond the two ledgers: %s; '
            'papers moved or renamed: %s; relay files of a kind beyond the act`s banks and tools, e0_rule.py, the table, the root list, the corrigenda '
            'bank and b704`s push-out bank: %s; the glossary unchanged: %s; outbound requests other than git and gh %d, an identifier of the author in %s; '
            'the source tool`s one fetch with a generic agent and no identifier: %s; no identifier in the join kernel`s workflow: %s' % (
                K.DRAFT, k_ok, main_ok, join_tags or 'NONE', added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, len(ob),
                [r['line'] for r in ident] or 'NONE', fetch_ok, wf_ok))


def scores(*a):
    """`scores [dry]` writes data/b705_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b705_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


def TRAIL_HEAD():
    return ('### b705 — lane two, act one hundred and thirty-two, the research act under (R315): b704 at its weight; the eight failures sorted and three '
            'predicates repaired; the closure join built as its own kernel and held at its one run; the count’s contour read; the detection law over '
            'seventeen pairs and the notched window at the lowest band zero; the perspective ranking; E0’s lexicon extended')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    ol = [x.get('line') for x in (jl('%s_order_tagprints.json' % ACT).get('lines') or [])] + ['-']
    dj, wj = _jgz('%s_detection.json.gz' % ACT), _jgz('%s_window.json.gz' % ACT)
    jg = jl('%s_join_grade.json' % ACT)
    fj_ = jl('%s_standing_figures.json' % ACT)
    e0 = jl('%s_e0_met.json' % ACT)
    rows = dj.get('rows') or []
    ratios = ['%s %s' % (r['idx'], ((r.get('ratio') or '-').strip('[]').split(' +/-')[0][:6]) if r.get('ratio') else 'beyond reach') for r in rows]
    within = [r['idx'] for r in rows if r.get('within')]
    errs = len([l for l in rdn('%s_buildlog_%s_join.txt' % (ACT, K.KERNEL)).split(NL) if l.startswith('error:')])
    return dict(corr_line=co.get('entry_line', '-'), order=ol[0], join_gate=jg.get('gate', '-'), join_held=jg.get('held'), join_run=jg.get('run', '-'),
                join_errs=errs, det_verdict=dj.get('verdict', '-'), det_computed=dj.get('computed', '-'), det_within=within, det_beyond=dj.get('beyond') or [],
                ratios=ratios, L0=(dj.get('L0') or '-').strip('[]').split(' +/-')[0][:10], win_verdict=wj.get('verdict', '-'), win_neg=wj.get('negative_at') or [],
                win_widths=wj.get('widths') or [], figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                e0_changed=len(e0.get('changed') or []))


def _title():
    f = _figs()
    return ('## The faces joined by closure at SIDE-faces-join %s; the count’s contour encloses every zero of Λ_Q; the detection law over seventeen '
            'pairs, %s within the registered range and %s beyond the route’s reach; the Weil window at the lowest band zero %s; the perspective '
            'ranking, the support radius at its head' % (
                'held' if f['join_held'] else 'v0.1.0', num_word(len(f['det_within'])), num_word(len(f['det_beyond'])),
                ('negative from width %s' % f['win_neg'][0]) if f['win_neg'] else 'nonnegative at every width'))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) the closure join written as its own kernel SIDE-faces-join at SIDE-explicit-formula’s pin, requiring both kernels by revision, '
            'faces_join stating lv-conservation’s own Register4_positivity on the author’s word, dispatched once and HELD at NOT DERIVES -- Lake '
            'resolving Mathlib’s dependencies from lv-conservation’s manifest (the last require), the cache not served, sixteen error lines in '
            'Mathlib’s dependencies, FacesJoin.lean never reached -- the error banked by line, no tag, no second dispatch, the fix Lake names carried '
            'as W-ORD-FACES-JOIN-MANIFEST for b706’s ruling (defect (j)); (2) the join kernel’s one commit made with the org’s noreply identity on '
            'the command, not amended; (3) the contour read at step zero, both ranges enclosing every zero of Λ_Q, the Q0 figures standing and '
            'W-ORD-Q0-TAILS-WIDE not entered; (4) twelve of the seventeen pairs beyond b675’s route’s reach by its own modulus rule, entered with '
            'the bound and not estimated, the law HELD over the five computed; (5) the notched window at the band zero negative at width 192 alone, '
            'the falsifier not fired, the archimedean term the mover at narrow widths and the prime term from 64; (6) the sign-onset registration '
            'reading the ruling’s "a = 32" as the ladder’s width (support radius 2 log 32) and Q0’s prime side empty below log 4 by the form, beside '
            'the ruling’s log 2; (7) E0’s RESTRICTIONS extended on the author’s word where the ruling named MET, the variants bank the control that '
            'chose (defect (k)); (8) G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE declared failing on the held join beside G-READ-RULE-STANDING '
            'on defect (e); (9) the %s navigator %s (%s) and the seat’s %s defect%s as lettered' % (
                num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', letters, num_word(seat), '' if seat == 1 else 's'))


def _finding_text():
    """the FINDINGS entry, composed before the root: its head line the result sentence, the result before its conditions; its scores line from the
    scores bank alone (data/b686_rules.txt row (1)); the root carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The research act’s five objects read: the closure join faces_join -- Weil positivity on classK equivalent to lv-conservation’s own '
         'Register4_positivity at the Li coefficients, stated in one module of a new kernel at SIDE-explicit-formula’s pin -- is %s at its one run, '
         'Mathlib’s dependencies built from lv-conservation’s manifest and the module never reached; the count’s contour, b685–b687’s rectangle and '
         'b696’s tail strip, encloses every zero of Λ_Q, so the Q0 figures stand; the detection law’s prediction n* = L₀/r(ρ) holds within '
         '[0.67, 1.5] at the %s pairs b675’s route reaches (n*/predicted %s), the %s higher pairs beyond its modulus rule and entered with the bound; '
         'b518’s notched window at the lowest band zero 0.798 + 29.552i reads nonnegative at widths 32 to 128 and %s beyond its ball; and the I-6 '
         'ranking puts the support radius of the test window at its head, registered for b707 as the sign-onset radius before any number.' % (
             'HELD' if f['join_held'] else 'DERIVES', num_word(len(f['det_within'])), ', '.join(r.split(' ')[1] for r in f['ratios'] if 'beyond' not in r),
             num_word(len(f['det_beyond'])), ('negative at %s' % f['win_neg'][0]) if f['win_neg'] else 'nonnegative at 192'), '',
         '*Filed at b705 on the author’s ruling `(R315)` and the author’s words at its prompts; %d question%s put. Banks: relay '
         '`data/b705_arm_sort.txt`, `data/b705_tool_repairs.txt`, `data/b705_corrigendum.txt`, `data/b705_join_files.txt`, '
         '`data/b705_runner_SIDE-faces-join_join.txt`, `data/b705_join_grade.txt`, `data/b705_contour.txt`, `data/b705_detection.txt`, '
         '`data/b705_window.txt`, `data/b705_registrations.txt`, `data/b705_i6_ranking.txt`, `data/b705_e0_met.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R315)`(1)-(2)): b704 entered at its weight (FINDINGS :%s); the generated entry at FINDINGS :%s answers b704’s five '
         'post-seal items -- (r) and (s), the two predicates found wrong after the seal, and the three trail-equality arms broken by a defect lettered '
         'after the trail landed; the corrigenda bank appended at row (25); the sealed face, the trail and the root-named banks unedited.' % (c1_[0], f['corr_line']), '',
         '**The sort and the repairs** (`(R315)`(2)-(4)): the eight arms failing at b704’s close sorted by cause (relay data/b705_arm_sort.txt), three '
         'declared on the face and five found after the seal; four repaired at carry time -- G-ACTROOT-BANKED reading the root route’s own item list, '
         'G-ANSWERS-CHECKED admitting the root prompt’s checks after the seal, G-README-CURRENCY’s readme() reading the README’s currency rows alone '
         '(0 stale, the baseline reset), G-WORKFLOW-FILES reading the dispatch’s target whole (data/b705_rules.txt row (1)) -- each with its diff and '
         'its control on b704’s banks (relay data/b705_tool_repairs.txt, data/b705_repair_controls.txt, data/b705_readme_control.txt); four not '
         'repaired, the arms correct.', '',
         '**The join** (`(R315)`(5), N1–N2): SIDE-faces-join created at Lean v4.34.0-rc1 and Mathlib de5ce8a9, requiring SIDE-explicit-formula v0.37 '
         'and SIDE-lv-conservation v0.10.0 by revision, its workflow SIDE-explicit-formula’s verbatim, no identifier of the author in any file; '
         'faces_join : h2_sign ↔ SIDELvConservation.RegisterPentagon.Register4_positivity LiCoeff, lv-conservation’s own declaration on the author’s '
         'word, proved by composing the two kernels’ equivalences; one dispatch (run %s), read by its id with the artifact’s sha256 verified: BUILD '
         'EXIT 1, %d error lines, every one in Mathlib’s own dependencies compiled from source at revisions lv-conservation’s manifest pins, the cache '
         'step reading "mathlib: failed to fetch cache" -- the lakefile’s last require, lv-conservation, outranking Mathlib’s manifest (defect (j)); '
         'the gate NOT DERIVES, the join %s with the lines banked (relay data/b705_join_grade.txt), no tag, no second dispatch; the composition’s '
         'type neither closed nor mismatched; W-ORD-FACES-JOIN-MANIFEST for b706’s ruling.' % (f['join_run'], f['join_errs'], 'HELD' if f['join_held'] else 'DERIVES'), '',
         '**The contour** (`(R315)`(6), N3): read at step zero before any Q0 figure -- the b685–b687 rectangle (1 − σ₁, σ₁) = (−1.4024, 2.4024) and '
         'the b696 tail bound’s strip [−1/2, 3/2] each enclose every zero of Λ_Q, Davenport–Heilbronn’s zeros in (1, 3/2) among them (relay '
         'data/b705_contour.txt); the Q0 figures stand; W-ORD-Q0-TAILS-WIDE not entered; nothing restated.', '',
         '**The detection law** (`(R315)`(7)(i), N4; data/b703_registrations.txt (ii), unchanged): the controls first -- n*(ρ₀) by b675’s route 63676, '
         'equal to b675’s, and ζ’s coefficients nonnegative through the largest predicted n* (vacuous by algebra, the instrument’s sign); L₀ = r(ρ₀) × '
         'n*(ρ₀) = %s; over the seventeen off-line pairs %s computed, n*/predicted %s, every one within [0.67, 1.5]; %s pairs beyond the route’s '
         'reach -- b675’s rule needs every rest modulus below (1 + R)/2 and the uncertified points’ bound exceeds it from the sixth pair on -- entered '
         'with the bound, not estimated; the falsifier %s (relay data/b705_detection.txt, the binary bank beside its hashes).' % (
             f['L0'], num_word(len(f['det_within'])), ', '.join(r.split(' ', 1)[1] for r in f['ratios'] if 'beyond' not in r), num_word(len(f['det_beyond'])), f['det_verdict']), '',
         '**The window** (`(R315)`(7)(ii), N4): b518’s notched family at γ₀ = 29.5517…, b694’s ladder 32 to 192, the terms in balls with the '
         'archimedean tail as b696’s DLMF ball; the controls first -- ζ nonnegative at every width of both families, the centred window at Q0 '
         'nonnegative at every width; the notched window at Q0: P − PR + A nonnegative at 32, 48, 64, 96 and 128 and NEGATIVE at 192 (S = −8.888 ± '
         '2.8e−25), so the falsifier (nonnegative at every width) is not fired and the hypothesis %s from width %s; the term anatomy per width beside '
         'b694’s at ρ₀: from ζ to Q0 the archimedean term moves most at 32 and 48 and the prime term from 64; against ρ₀ (negative from 32) the band '
         'zero needs the widest window, the archimedean term the mover at every width (relay data/b705_window.txt).' % (f['win_verdict'], f['win_neg'][0] if f['win_neg'] else '-'), '',
         '**The ranking** (`(R315)`(8)): the small-support positivity result read at source first -- Connes–Consani, the archimedean place, '
         'arXiv:2006.13771: Weil positivity for test functions supported in (1/2, 2), the support radius log 2 exactly where ζ’s prime side is empty, '
         'their Theorem 1 and Theorem 6.11 by page (relay data/b705_source_cc_2006_13771.txt); the sign-onset radius at Q0 registered as (iii) in '
         'data/b705_registrations.txt and committed alone before any number (the ruling’s "a = 32" read as the ladder’s width, support radius '
         '2 log 32; Q0’s prime side empty below log 4, the form representing neither 2 nor 3); the seven axes scored at statement grade '
         '(relay data/b705_i6_ranking.txt): the support radius 5, representation coordinates 4, the cover 3 (a wall that narrowed, from '
         'data/b703_wsign7.txt), re-centering 2, the generic deformation 1, the subspace and the chiasmus 0 by the spec’s own rule; the top axis for '
         'b707.', '',
         '**E0’s lexicon** (`(R315)`(9)): measured first on the file unedited (relay data/b705_e0_met_variants.txt) -- the ruling’s MET list yields a '
         'premise under the rule’s own words, so MET+3 leaves two inclusions PREDICATE-UNLISTED and turns the third INTERFACES; on the author’s word '
         'the four heads classK, classKsum, classK’ and acDeriv entered in RESTRICTIONS by the Edit tool, each on its variable with its line at v0.36; '
         'the three inclusions now DERIVES, every other header of data/b703_widening_grade.txt unchanged before and after, the diff banked (relay '
         'data/b705_e0_met.txt; the ruling’s "MET" the navigator’s (k)).', '',
         '**The standing arms**: the four figures at b705 -- %s, %s, %s, %s -- against b704’s 0, 12, 131, 0, the README figure by the repaired '
         'readme() against its reset baseline 0 (relay data/b705_standing_figures.txt); G-READ-RULE-STANDING declared failing on defect (e), the two '
         'whole reads at the opening; G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE declared failing on the held join, by (R315)(5)’s own clause; '
         'no standing arm added.' % (f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins']), '',
         '**The orders** (`(R315)`(4) and the author’s words): W-ORD-ENTRY-TAG-PRINTS entered (OPEN_TRAILS :%s), trigger b706, the premise the '
         'navigator’s (i); W-ORD-P3-CONTOUR-SIGMA read and its bank written, W-ORD-README-FIGURE-SCOPE repaired at carry time, W-ORD-E0-MET-CLASSK’s '
         'remaining content done, W-ORD-LV-CLOSURE-JOIN’s join built and held -- each for b706’s ruling to close or carry; W-ORD-FACES-JOIN-MANIFEST '
         'and W-ORD-Q0-TAILS-WIDE named for it, the second not entered.' % f['order'], '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and raised before the components that cite '
         'them; %d answer check%s, each before its answer was acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-',
                                                                           checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the three computations say one thing about the band -- the off-line zeros b675’s route '
         'reaches obey the one-parameter law to within a factor 1.2, the lowest band zero is seen by the notched window only at the widest width, '
         'and the proven range of positivity ends exactly where the primes begin -- and the ranking names the parameter that joins them, the support '
         'radius. It strengthens the programme’s offering of a located clause: the clause’s two compiled faces now stand in one module that names '
         'each kernel’s own declaration, held at the build and not at the type, and the instruments that read the clause’s wall are calibrated '
         'against each other at one zero.', '',
         '**Carried to:** b706 (W-ORD-PAPER-PARTNER-COPIES’s disposition (iii) over the 17 pairs; W-ORD-WORKFLOW-PROBE-STEP; W-ORD-CORRESPONDENCE-EF-REACH; '
         'W-ORD-ENTRY-TAG-PRINTS; W-ORD-FACES-JOIN-MANIFEST; the faces row naming the join kernel); b707 (the sign-onset radius and the top-ranked axis '
         'at full grade; W-ORD-Q0-TAILS-WIDE where (R315)(6) entered it, which it did not); b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5); '
         'W-ORD-KEYSTONE-HEADS on its trigger; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R315) ratified.** (1) b704 at its weight. (2) The sort, the repairs and the corrigendum. (3) The README figure. (4) The probe target. '
             '(5) The closure join. (6) The count’s contour. (7) The computations. (8) The perspective ranking. (9) E0’s lexicon. (10) The branches. '
             '(11) The readfirst bank. (12) The draft held at v5. (13) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b704’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s (one order); this record.' % (
                 c1_[0], f['corr_line'], fj.get('entry_line'), f['order']), '',
             '**Act root:** b705 `%s` (previous `%s`, b704’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b705_author_answers.txt); the root’s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The join:** SIDE-faces-join at `%s`, faces_join stating lv-conservation’s own Register4_positivity, one dispatch (run %s), the gate %s, '
             'the join %s with %d error lines banked -- Mathlib’s dependencies from lv-conservation’s manifest, the module never reached -- no tag, no '
             'second dispatch (relay data/b705_join_grade.txt).' % (K.JOIN_TIP[:7], f['join_run'], f['join_gate'], 'HELD' if f['join_held'] else 'DERIVES', f['join_errs']), '',
             '**The contour:** both ranges enclose every zero of Λ_Q; the Q0 figures stand (relay data/b705_contour.txt).', '',
             '**The detection law:** %s pairs computed, every one within [0.67, 1.5]; %s beyond reach with the bound; the falsifier %s (relay '
             'data/b705_detection.txt).' % (num_word(len(f['det_within'])), num_word(len(f['det_beyond'])), f['det_verdict']), '',
             '**The window:** negative at %s alone, nonnegative at the five widths below; the falsifier not fired, the hypothesis %s (relay '
             'data/b705_window.txt).' % (', '.join(f['win_neg']) or 'no width', f['win_verdict']), '',
             '**The ranking:** the support radius at its head (relay data/b705_i6_ranking.txt); the sign-onset radius registered as (iii) before any '
             'number (relay data/b705_registrations.txt), for b707.', '',
             '**E0’s lexicon:** RESTRICTIONS extended with four heads on the author’s word, %d inclusions DERIVES, every other header unchanged (relay '
             'data/b705_e0_met.txt).' % f['e0_changed'], '',
             '**The kernels:** one created, SIDE-faces-join, its one commit on main pushed in main mode and dispatched once; SIDE-explicit-formula’s '
             'main unmoved at v0.37 and lv-conservation’s at its deposit; no lean or lake on this host.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b705_closing.txt).', '',
             '**The open orders:** `W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-PAPER-PARTNER-COPIES`; `W-ORD-STANDING-CLAUSES-BANK`; '
             '`W-ORD-LV-CLOSURE-JOIN` (the join built and held); `W-ORD-KEYSTONE-HEADS`; `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA` (read, '
             'its bank written); `W-ORD-E0-MET-CLASSK` (its content done); `W-ORD-WORKFLOW-PROBE-STEP`; `W-ORD-CORRESPONDENCE-EF-REACH`; '
             '`W-ORD-README-FIGURE-SCOPE` (repaired at carry time); `W-ORD-ENTRY-TAG-PRINTS`.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b704’s 0, 12, 131, 0, the README baseline reset to 0; G-READ-RULE-STANDING '
             'declared on the face as a carried failure on defect (e); G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE declared beside it on the held '
             'join (relay data/b705_standing_figures.txt, data/b705_read_calls.txt, data/b705_join_grade.txt).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b705_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R315).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b705_citation_check.txt), step zero (data/b705_ferry.txt, data/b705_readfirst.txt, data/b705_stepzero.txt, '
         'data/b705_tests_stepzero.txt, data/b705_rowgen_stepzero.txt, data/b705_branches.txt, data/b705_contour.txt, data/b705_rules.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 1 : b704`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s ; the sort and the repairs (data/b705_arm_sort.txt, '
         'data/b705_tool_repairs.txt, data/b705_repair_controls.txt, data/b705_readme_control.txt) ; W-ORD-ENTRY-TAG-PRINTS OPEN_TRAILS :%s' % (c1_[0], f['corr_line'], f['order']),
         '### COMPONENT 2 : the join (data/b705_join_files.txt, data/b705_runner_SIDE-faces-join_join.txt, data/b705_join_grade.txt), run %s, the gate %s, '
         'the join %s ; N1 %s ; N2 %s' % (f['join_run'], f['join_gate'], 'HELD' if f['join_held'] else 'DERIVES', S['N1'][0], S['N2'][0]),
         '### COMPONENT 3 : the detection law (data/b705_detection_controls.txt, data/b705_detection.txt), %s ; the window (data/b705_window_controls.txt, '
         'data/b705_window.txt), %s ; N4 %s' % (f['det_verdict'], f['win_verdict'], S['N4'][0]),
         '### COMPONENT 4 : the source (data/b705_source_cc_2006_13771.txt), the registrations (data/b705_registrations.txt), the ranking '
         '(data/b705_i6_ranking.txt), E0`s lexicon (data/b705_e0_met.txt, %d changed)' % f['e0_changed'],
         '### COMPONENT 5 : the carry-time reading (data/b705_tool_repairs.txt), the dry-run steps (data/b705_reg_gate.txt), the seal '
         '(data/b705_seal_hashes.json), the suite in six parts, the per-part seconds (data/b705_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def findings(*a):
    t, e = _finding_text()
    e = R.conv(e)
    dry = 'dry' in a
    cells_, fired = R.screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = R.conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = R.screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; the trail's Defects line AND its Resolved line read against
    the defects bank. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = R.conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = R.screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = R._face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        if which == 'TRAIL':
            m = re.search(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % ACT, text, re.M)
            got = m.group(1) if m else None
            want = '; '.join(_defect_short(ACT)) or 'none'
            eq = got == want
            print('  THE TRAIL`S DEFECTS LINE: %s' % got)
            print('  THE DEFECTS BANK`S ROWS (relay data/%s_defects.txt, by the repaired reader): %s' % (ACT, want))
            print('  ### THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK %s' % eq)
            rows, nav = _owners_now()
            gr = _trail_resolved(t)
            wr = (num_word(len(nav)), num_word(len(rows) - len(nav)))
            eqr = gr == wr
            print('  THE TRAIL`S RESOLVED LINE`S COUNTS: %s ; THE BANK`S OWNERS (navigator, seat): %s' % (gr, wr))
            print('  ### THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK %s' % eqr)
            clean = clean and eq and eqr
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


def mbank(*a):
    """b704's mbank (its span line read from the mirror bank chain) carried by copy with b705's names."""
    import hashlib as _hl
    import zipfile
    import b616_record as R6
    ZIP = R.ZIP
    z = zipfile.ZipFile(ZIP)
    names_ = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names_), R6.nd_sets())[0]
    files_ = [n for n in names_ if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT)))
    for l in L[:9]:
        print(l[:240])


def guard(*a):
    """data/b705_guard_dry.txt (.json): b704's route with b705's names -- the suite's `--guard-dry` run in its own process (it writes nothing), its
    print banked verbatim; the writes by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b705_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b705_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b705_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b705_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b705_checks.py :%d `%s`,'
         % (k, src[k - 1].strip() if k else '?'), '### the line above the per-part seconds write at :%d.' % ((k or 0) + 1), '',
         '### THE PRINT, VERBATIM (exit %d):' % r.returncode]
    L += [x for x in r.stdout.rstrip(NL).split(NL)]
    L += ['', '### THE WRITES BY MODE, READ FROM THE SUITE`S writer_plan: %s' % '; '.join('%s %s' % (m, w or 'NONE') for m, w in writes.items()), '',
          '### ### **%s**' % ('THE GUARD HELD ; THE POST-ROOT PATH WRITES NONE OF THE PER-PART SECONDS BANKS ; THE PRE-RUN WRITES THEM ALONE'
                               if ok else '### THE GUARD IS NOT AS READ -- SEE ABOVE')]
    if 'dry' not in a:
        put_txt('%s_guard_dry.txt' % ACT, L)
        put_json('%s_guard_dry.json' % ACT, dict(at=utc(), writes=writes, guard_line=k, exit=r.returncode, ok=ok))
    print(NL.join(L))


def armnames(*a):
    """the suite's arm names in its order, for the face's (G2) block -- names alone, no source printed."""
    import b705_checks as CH
    names_ = [x[0] for x in CH.ARMS]
    st = set(_standing())
    print('  ARMS %d ; standing among them %d ; the act`s %d ; beyond both %s' % (
        len(names_), len(st & set(names_)), len(set(names_) & set(K.ACT_ARMS)), sorted(set(names_) - st - set(K.ACT_ARMS)) or 'NONE'))
    print('  standing not in the suite: %s' % (sorted(st - set(names_)) or 'NONE'))
    print('  act arms not in the suite: %s' % (sorted(set(K.ACT_ARMS) - set(names_)) or 'NONE'))
    for i in range(0, len(names_), 7):
        print('### ' + ' '.join('`%s`' % n for n in names_[i:i + 7]))


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              scores=scores, components=components, findings=findings, trail=trail, drycheck=drycheck, mbank=mbank, guard=guard, armnames=armnames,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, armsort=armsort, figures=figures, figctl=figctl, c1=c1,
              orders=orders, repairs=repairs, repairctl=repairctl, joinfiles=joinfiles, joingrade=joingrade, artfile=artfile, e0met=e0met)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b705_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
