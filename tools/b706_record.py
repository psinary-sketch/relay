# -*- coding: utf-8 -*-
"""b706_record.py -- THE ACT'S RECORD TOOL, b706 under (R316).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b706 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and b705's routes (the print-list dispatch, the artifact reader, the join grade) are reached through
### tools/b705_record.py (sealed at b705 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### THE CARRY-TIME REPAIRS OF THIS TOOL (data/b706_tool_repairs.txt): (a) prev_capture cut at this act's anchor -- b705 ran in THIS session, so
### b698's window "to the session's end" would read b706's own commands as b705's; (b) ROOT_EXCLUDE extended at carry time with every untracked
### write a b706_*.py tool declares in its head (`### UNTRACKED WRITE: data/b706_<name>`), data/b706_rules.txt row (1), printed by `rootexclude`.
### Written by the Write tool at b706 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b706_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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

import b706_worklist as K          # noqa: E402
import b705_worklist as K705       # noqa: E402  ### b705's data, for the controls on b705's banks
import b705_record as P5           # noqa: E402  ### b705's tool, imported unedited (its import binds b698's R, b703's P3 and b704's P4 to b705: rebound below)
R, P3, P4 = P5.R, P5.P3, P5.P4     # ### b698's routes, b703's and b704's repaired readers, through b705's module

ACT, PREV = 'b706', 'b705'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b705 ran and closed in THIS session (44411d52), so its window is b703's form -- from its anchor (R315)'s line
# ### to this act's anchor (R316)'s line; its post-push stretch from its post-push combine to (R316)'s line (prev_capture below, the cut)
PREV_SESSION_PATH = SESSION
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = SUBAGENTS
FACE = os.path.join(D, 'b706_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b706_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b705_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('correspondence_gen.py',)

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b706_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b706_<name>`.
EXCLUDE_KINDS = (r'defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                 r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                 r'commands|mirror.*|close_sentence|read_calls')
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b706_(\S+)\s*$', re.M)


def declared_untracked():
    """every b706_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b706_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b706_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b706_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P5._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 and b705


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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='8454a2bb' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S, b704'S AND b705'S REPAIRED READERS, THROUGH b705'S MODULE
_deps = P3._deps                   # ### the primed names read (b703 (f))
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line
_read_verdict, CAP = P4._read_verdict, P4.CAP   # ### b704's repaired verdict (offset, limit VALUES, the cap of two hundred)
_print_modules = P5._print_modules              # ### b705's print-list reader (every name mapped to its module by git grep bounded to the tree)


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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R316)(9); b705's form, one kernel branch)
def branches(*a):
    """`branches before`: data/b706_branches_before.json -- b698's route, carried (every branch (R316)(9) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b706_branches.txt (.json) --
    each branch's fate read now against the tips banked before."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b706_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R316)(9): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b706_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R316)(9) names one kernel branch, SIDE-faces-join push-b705-join.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[6:]))


# ================================================================================ THE READ BANK (b704's repaired route; the word's time the anchor's, from b705)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b706_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
    for n, f in sorted(vars(mod).items(), key=lambda kv: inspect.getsourcelines(kv[1])[1] if inspect.isfunction(kv[1]) and kv[1].__module__ == mod.__name__ else 0):
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            print('  %-28s :%d' % (n, inspect.getsourcelines(f)[1]))


def verdicts(*a):
    """prints each named bank's verdict line (its last `### ### **...**` line), for the suite's predicates to quote; writes nothing."""
    for n_ in a:
        m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', rdn(n_))
        print('  %s | %s' % (n_, ' '.join(m[-1].split()) if m else '### NO VERDICT LINE'))


# ================================================================================ THE DISPATCH, THE RUNNER (b698's routes; b705's print-list check; b703's runner reader)
runstatus, runner = R.runstatus, R.runner
STD3 = P3.STD3


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: b698's dispatch (one dispatch per tree state, the run id read), with b705's check
    (data/b705_rules.txt row (1)): every name of print_targets.txt at the ref mapped to its module by git grep bounded to the kernel's tree; a
    target not covering every module is REFUSED, nothing dispatched; the row banked carries `whole` True with the modules the list needs."""
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


# ================================================================================ THE LATE ROUTES (b705's, carried with b706's names; the previous window cut)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor. Rebound here: b705's
    import rebound b698's to its own, which reads from (R315)'s line."""
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
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after


def prev_capture():
    """G-EDIT-ROUTE's window over the previous act, b703's form for a previous act in THIS session, with this act's cut (the carry-time repair (a)):
    b705's capture AFTER ITS POST-PUSH SUITE -- every command of this session from the call that combined b705's post-push parts into
    data/b705_checks_postpush.txt to the first user line carrying (R316)'s anchor. b698's route reads to the session's end, which in one session
    would take this act's own commands as the previous act's."""
    rows = ER.capture(SESSION, K.PREV_ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    cut = _anchor_ts(K.ANCHOR)
    cut_e = _iso_epoch(cut) if cut else None
    if not cut_e:
        sys.exit('### THIS ACT`S ANCHOR %r IS NOT TIMED IN THE SESSION -- THE PREVIOUS WINDOW HAS NO END -- NOTHING READ' % K.ANCHOR)
    out = [dict(r, src='%s %s' % (PREV, r['src'])) for r in rows if first[0] <= r['ts'] and (_iso_epoch(r['ts']) or 0) < cut_e]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


R.prev_capture = prev_capture
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b705's route with b706's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (cut at
    this act's anchor), the local lean reading (N1), the dispatches (three ordered: the join, the two entry-tag branches), the detached runs,
    sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests. data/b706_commands.txt (.json)."""
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
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES, THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, this session %s, from its post-push combine to (R316)`s line): '
              '%d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (three ordered this act, N1: the join kernel, the two entry-tag branches) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R316)(9) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    print('  kernels read: %d (SIDE-faces-join among them; no kernel written after this read)' % len(ks))


def _standing():
    import b705_worklist as K705
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B705_FACE.split('/')))) - set(K705.ACT_ARMS)) | set(K.STANDING_ADDED))


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


# ================================================================================ COMPONENT 1: THE SORT, (R316)(2)
TEN = (('G-WORKFLOW-FILES', 'j', 'declared', 'the held join: the run`s gate NOT DERIVES by (R315)(5)`s own clause, Lake resolving Mathlib`s packages from lv-conservation`s manifest',
        'NO REPAIR: the arm correct; the join`s manifest repaired and dispatched once under (R316)(4)'),
       ('G-RUNNER-READ', 'j', 'declared', 'the held join, the gate NOT DERIVES', 'NO REPAIR: the arm correct; (R316)(4)'),
       ('G-RUNNER-GATE', 'j', 'declared', 'the held join, the gate NOT DERIVES', 'NO REPAIR: the arm correct; (R316)(4)'),
       ('G-READ-RULE-STANDING', 'e', 'declared', 'two whole reads of files of two hundred lines or more at the opening', 'NO REPAIR: the arm correct; from b705 every call counts'),
       ('G-WRITELIST-KINDS', '', 'after', 'the navigator`s: a rules file (data/b706_rules.txt) ordered mid-act after the (W) list was sealed -- an event in b705`s bank, unlettered',
        'REPAIRED at carry time under (R316)(2): a (W) list that admits data/b<next act>_rules.txt by form, the arm requiring the form (tools/b706_checks.py wl_ok; data/b706_tool_repairs.txt row (1))'),
       ('G-ANSWERS-CHECKED', 'n', 'after', 'the checker reading the PDF`s sha256 prefix as a commit', 'REPAIRED at carry time under (R316)(2): tools/b706_citation.py answer tells a root prefix or a file hash from a commit by its bank`s row (data/b706_tool_repairs.txt row (2))'),
       ('G-ENTRY-TITLE-FORM', 'o', 'after', 'the needle`s lower-case "the" against the entry`s "The"', 'REPAIRED at carry time under (R316)(2): tools/b706_checks.py entry_title_ok compares after case-folding the article alone (data/b706_tool_repairs.txt row (3))'),
       ('G-TRAIL-LINES-EQUAL-DEFECTS', 'o', 'after', '(o) lettered after the trail landed', 'NO REPAIR: the sequence rule of (R315)(2) binding and read by the gate -- no defect lettered after the trail`s dry run without that dry run re-read'),
       ('G-TRAIL-DEFECTS-EQUAL', 'o', 'after', '(o) lettered after the trail landed', 'NO REPAIR: the sequence rule binding'),
       ('G-TRAIL-RESOLVED-EQUAL', 'o', 'after', '(o) lettered after the trail landed', 'NO REPAIR: the sequence rule binding'))


def _drow(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def armsort(*a):
    """data/b706_arm_sort.txt: (R316)(2), the ten arms failing at b705's close (data/b705_checks_postpush.txt's LIVE FAILING list) -- the four
    declared on the face and the six found after the seal -- each with its cause by letter and line in data/b705_defects.txt (the write-list
    event by its line) and its disposition in the ruling's words; rows are arms."""
    ck = rdn('b705_checks_postpush.txt')
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip()]
    df = rdn('b705_defects.txt').split(NL)
    face = rd(os.path.join(ROOT, *K.B705_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ev = next((i + 1 for i, l in enumerate(df) if l.strip().startswith('G-WRITELIST-KINDS fails after the seal')), 0)
    rows = []
    for name, letter, where, cause, disp in TEN:
        if letter:
            s, e, t = _drow(df, letter)
            e = max(e - 1, s)
        else:
            s, e, t = ev, ev + 3, ' '.join(x.strip() for x in df[ev - 1:ev + 3]) if ev else ''
        rows.append((name, name in fails, 'declared on the face' if name in declared else 'found after the seal', letter or 'event', s, e, cause, disp, t[:140]))
    L = ['%s -- COMPONENT 1, (R316)(2): THE TEN ARMS FAILING AT b705`S CLOSE, THE SIX AFTER THE SEAL SORTED BY CAUSE, EACH WITH ITS DISPOSITION (%s)' % (ACT, utc()), '',
         '### rows are arms: the arm | failing at b705`s close (relay data/b705_checks_postpush.txt, LIVE FAILING %d) | declared on the face or found after the seal' % len(fails),
         '### (relay data/b705_registration_2026-10-22.txt) | its cause by letter and line in relay data/b705_defects.txt (the write-list event by its line) |',
         '### the disposition in (R316)(2)`s words. The sequence rule, (R315)(2), binding and read by the gate: no defect is lettered after the trail`s dry run',
         '### without that dry run re-read.', '']
    for name, f, where, letter, s, e, cause, disp, t in rows:
        L += ['  %-28s | failing %s | %s | (%s) data/b705_defects.txt :%d-:%d -- %s | %s' % (name, f, where, letter, s, e, cause, disp),
              '      the row: %s' % t]
    rep = [r for r in rows if r[7].startswith('REPAIRED')]
    L += ['', '### ### **ARMS %d ; FAILING AT b705`S CLOSE %d OF %d ; DECLARED ON THE FACE %d ; FOUND AFTER THE SEAL %d ; REPAIRED AT CARRY TIME %d ; NO REPAIR %d.**' % (
        len(rows), sum(1 for r in rows if r[1]), len(rows), sum(1 for r in rows if r[2] == 'declared on the face'), sum(1 for r in rows if r[2] == 'found after the seal'),
        len(rep), len(rows) - len(rep))]
    if 'dry' not in a:
        put_txt('%s_arm_sort.txt' % ACT, L)
        put_json('%s_arm_sort.json' % ACT, dict(at=utc(), rows=[dict(arm=r[0], failing=r[1], where=r[2], letter=r[3], lines=[r[4], r[5]], cause=r[6], disposition=r[7]) for r in rows],
                                                failing=fails, declared=declared))
    print(NL.join(L[7:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R316)(1)
WH = ('*Appended 2026-10-22 by b706 to b705’s entry (:9990), under `(R316)`(1) -- b705 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b705_closing.txt):*')
WB = (' “b705 closed: relay 9f5871da, PLACE-papers c4c4273; suite 128 of 138; root 8454a2bb2428eba3…; 5 prompts answered; 15 defects” '
      '(data/b705_closing.txt :1); the closing commit f9a60e40 pushed alone after the line was written and read back equal at the remote '
      '(data/b705_closing_push_out.txt :5). The count’s contour read at step zero, b685–b687’s rectangle and b696’s tail strip each enclosing '
      'every zero of Λ_Q, the Q0 figures standing (data/b705_contour.txt); the detection law held over the five pairs b675’s route reaches, '
      'each within [0.67, 1.5], the twelve higher pairs beyond its modulus rule and entered with the bound (data/b705_detection.txt); the '
      'notched Weil window at 0.79799715717868013876 + 29.55176109862911459913 i nonnegative at widths 32 to 128 and negative at 192, the '
      'hypothesis HELD from width 192 (data/b705_window.txt); the I-6 ranking with the support radius at its head, the sign-onset registration '
      '(iii) committed alone before any number, the Connes–Consani range read by page (data/b705_i6_ranking.txt, data/b705_registrations.txt); '
      'E0’s RESTRICTIONS given four heads on the author’s word, the three inclusions DERIVES, every other header unchanged (data/b705_e0_met.txt); '
      'the join SIDE-faces-join created at 732c1b49 and HELD at its one run, Lake resolving Mathlib’s transitive packages from '
      'lv-conservation’s manifest so the cache was not served, FacesJoin.lean not reached, the cause banked from the run’s artifact as defect '
      '(j) (data/b705_join_grade.txt); W-ORD-ENTRY-TAG-PRINTS entered (OPEN_TRAILS :15590). b704’s five post-seal items answered by the '
      'generated corrigendum at FINDINGS :9976 (corrigenda row (25)); b704’s weight at :9974. The entry at FINDINGS :9990, the trail at '
      'OPEN_TRAILS :15592; the root 8454a2bb over 89 banks chained from 97bd2133 (data/b705_act_root.json); suite 131 of 138 pre-push and '
      '128 of 138 post-push, four failures declared on the face (G-READ-RULE-STANDING on (e); G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE '
      'on the held join) and six found after the seal (G-WRITELIST-KINDS on data/b706_rules.txt, G-ANSWERS-CHECKED, G-ENTRY-TITLE-FORM and the '
      'three trail-equality arms; data/b705_checks.txt, data/b705_checks_postpush.txt); N1–N4 and S1–S3 HELD, N5 HELD at the record and REFUTED '
      'at the close on data/b706_rules.txt (data/b705_scores_close.json); the sealed tools’ hashes equal at the close, 13 of 13; the citation '
      'check 138 cites, 136 OK, 2 misses the navigator’s; fifteen defects (a)–(o), (g), (h), (i) and (k) the navigator’s (data/b705_defects.txt); '
      '“5 prompts answered” the answers bank’s 4 rows and the root’s prompt, put in two calls under (m); the three excluded files moved to the '
      'session scratchpad with sha256 equal before and after; the mirror mirror-refresh-2026-10-22-b705.zip CLEAN on all three clauses with '
      'the root line (data/b705_mirror.txt). The six post-seal items entered by this act’s corrigendum. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B705_ENTRY,
         check=[('FINDINGS.md', K.B705_ENTRY, '## The faces joined by closure'), ('OPEN_TRAILS.md', K.B705_TRAIL, '### b705')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE CARRY-TIME REPAIRS, (R316)(2), AND THEIR CONTROLS
REPAIR_ROWS = [
    ('(1) tools/b706_checks.py `wl_ok`, G-WRITELIST-KINDS -- ANSWERS (R316)(2): b705`s arm read C3.wl_ok (tools/b703_checks.py :1320-:1321) over the '
     'face`s (W) list, which named relay/data/b705_* and no file of a later act; data/b706_rules.txt, written on the author`s word after the seal, '
     'failed it (b705`s event, the navigator`s). The repair is in the (W) list`s form -- it admits the next act`s rules file by form, '
     '`relay/data/b707_rules.txt` -- and the arm now requires that form on the face beside the written files` cover. The control: '
     'data/b706_repair_controls.txt.', 'b703_checks.py', 'b706_checks.py', 'wl_ok', ()),
    ('(2) tools/b706_citation.py `answer`, G-ANSWERS-CHECKED -- ANSWERS (R316)(2): b682`s route (tools/b682_citation.py :234-:236, carried by '
     'tools/b705_citation.py :431-:444) read every bare token of seven to twelve hex characters as a commit, so the root prompt`s second answer '
     'naming the fetched source`s sha256 "b8e0b54a..." printed a MISS -- b705`s (n). The repaired route reads every sha256 a bank`s row names '
     '(the root list, the hashes banks, any bank line carrying "sha256"), checks a token those rows name against its row, prints it OK and '
     'masks it from the commit reading; the predicate answers_checked_ok is b705`s, unchanged. The control: data/b706_repair_controls.txt.',
     'b705_citation.py', 'b706_citation.py', 'answer', ('_sha_rows',)),
    ('(3) tools/b706_checks.py `entry_title_ok`, G-ENTRY-TITLE-FORM -- ANSWERS (R316)(2): b705`s predicate (tools/b705_checks.py :684-:689) '
     'required `the faces joined by closure at SIDE-faces-join` in a title that opens "## The faces joined by closure ..." -- b705`s (o), found '
     'after the seal. The repaired predicate compares after case-folding the article alone (`_fold_article`: the heading`s first word The, A or An '
     'lowered, nothing else), its needles this act`s objects. The control: data/b706_repair_controls.txt.', 'b705_checks.py', 'b706_checks.py',
     'entry_title_ok', ('_fold_article',)),
    ('(4) tools/b706_record.py `prev_capture` -- ANSWERS the carry: b698`s route (tools/b698_record.py :1053-:1064) reads the previous act`s '
     'window from its post-push combine to the session`s end; b705 ran in THIS session, so that window would take this act`s own commands as '
     'b705`s (b703`s form named the cut at the next ruling`s line but did not make it). The repaired route cuts the window at the first user '
     'line carrying (R316)`s anchor. The control: data/b706_repair_controls.txt.', 'b698_record.py', 'b706_record.py', 'prev_capture', ()),
    ('(5) tools/b706_record.py `_root_exclude`, `declared_untracked` -- ANSWERS data/b706_rules.txt row (1) (b705`s (l), (m)): the root route`s '
     'exclusion list carried from the previous act`s tool and extended at carry time with every untracked write a b706_*.py tool declares in its '
     'head (`### UNTRACKED WRITE: data/b706_<name>`), read from the tools` own declarations at import; the `rootexclude` route prints them; '
     'the `rootdry` route runs the root route dry on the pre-root tree before the seal and banks its READY. The control: '
     'data/b706_repair_controls.txt.', 'b705_record.py', 'b706_record.py', '_root_exclude', ('declared_untracked',)),
]


def repairs(*a):
    """data/b706_tool_repairs.txt: the carry-time repairs, each with the order or carry it answers, its diff written by this route (difflib, the
    plain unified_diff of whole lines; the old text from the sealed tool named)."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS, (R316)(2) (%s)' % (ACT, utc()), '',
         '### rows are repairs with what they answer: the tool and its part ; what it answers ; the form. Each diff beneath its row, written by',
         '### this route (difflib over the function`s source: the sealed tool`s against this act`s; a new function printed whole). The controls',
         '### that distinguish each repaired reading from the old one: data/b706_repair_controls.txt. No sealed tool is edited;',
         '### tools/correspondence_gen.py`s parser is extended at Component 3 under (R316)(6), its diff in data/b706_generator_reach.txt.', '']
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
    L += ['### ### **REPAIRS %d ; SHARED TOOLS EDITED 0 AT THE CARRY (correspondence_gen.py AT COMPONENT 3 BY RULING) ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


def _answer_text(needle, anchor):
    """b682's selection of an answer text (tools/b682_citation.py :210-:223), pure: the latest user text carrying `needle` after `anchor`."""
    import b677_citation as C
    best, seen = None, False
    for t in C._user_texts():
        if anchor in t:
            seen = True
        u = t.replace('’', "'")
        if seen and needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u or 'user has answered' in u):
            best = t
    if best is None:
        return ''
    k = best.find(needle)
    b0, e0 = best.rfind('BEGIN', 0, k), best.find('END', k)
    return best[b0:e0 + 3] if (b0 >= 0 and e0 > k) else best


def repairctl(*a):
    """data/b706_repair_controls.txt: each repaired reading and the old one run on b705's banks or b705's own answer (the keys each reads), then
    on mutated copies, so that the repaired reading is distinguished from the old on real state."""
    import b703_checks as C3
    import b705_checks as C5
    import b706_checks as C6
    import b706_citation as CIT
    import b682_citation as P82
    L = ['%s -- COMPONENT 1, (R316)(2): THE REPAIRED READINGS AGAINST THE OLD ON b705`S BANKS AND ANSWERS (%s)' % (ACT, utc()), '',
         '### rows are cases: the arm or tool | the source (b705`s banks or answer, or a mutated copy) | the old reading | the repaired | wanted.',
         '### Each repaired reading is DISTINGUISHED where one row reads them apart.', '']
    cases = []
    # ### (1) G-WRITELIST-KINDS on b705`s face and written files
    face5 = rd(os.path.join(ROOT, *K.B705_FACE.split('/')))
    globs5 = C3.wl_globs(face5)
    written5 = sorted(set('relay/' + x for x in g(ROOT, 'diff', '--name-only', K705.PRE_RELAY, K.PRE_RELAY).split(NL) if x.strip())
                      | set('PLACE-papers/' + x for x in g(PP, 'diff', '--name-only', K705.PRE_PP, K.PRE_PP).split(NL) if x.strip()))
    with6 = written5 + ['relay/data/b706_rules.txt']
    S = dict(globs=globs5, written=with6, next_rules='relay/data/b706_rules.txt')
    cases.append(('G-WRITELIST-KINDS', 'b705`s face`s (W) globs (%d) and its written files (%d) with data/b706_rules.txt among them' % (len(globs5), len(with6)),
                  C3.wl_ok(S), C6.wl_ok(S), (False, False)))
    S2 = dict(globs=globs5 + ['relay/data/b706_rules.txt'], written=with6, next_rules='relay/data/b706_rules.txt')
    cases.append(('G-WRITELIST-KINDS', 'the same with the (W) list in the repaired form (the next act`s rules file admitted by form)', C3.wl_ok(S2), C6.wl_ok(S2), (True, True)))
    S3 = dict(globs=globs5, written=[w for w in written5 if any(fnmatch.fnmatch(w, p) for p in globs5)], next_rules='relay/data/b706_rules.txt')
    cases.append(('G-WRITELIST-KINDS', 'b705`s face`s globs over its covered files alone (no rules file written): the form absent', C3.wl_ok(S3), C6.wl_ok(S3), (True, False)))
    # ### (2) the answer checker on b705`s root answer, second call
    txt = _answer_text('Root, second call', K.PREV_ANCHOR)
    old_tokens = sorted(set(h for h in re.findall(r'\b([0-9a-f]{7,12})\b', txt) if re.search(r'[a-f]', h) and re.search(r'\d', h)))
    shas = CIT._sha_rows()
    masked = txt
    named = []
    for m in CIT._HEX8.finditer(txt):
        if m.group(1) in shas:
            named.append((m.group(1), shas[m.group(1)]))
            masked = masked.replace(m.group(1), 'SHA-' + m.group(1)[:4] + '-' + m.group(1)[4:])
    new_tokens = sorted(set(h for h in re.findall(r'\b([0-9a-f]{7,12})\b', masked) if re.search(r'[a-f]', h) and re.search(r'\d', h)))
    old_ok = all(any(P82.commit_in(r_, h) for r_ in P82.REPOS + (K.EF_DIR, K.KERNEL_DIR)) for h in old_tokens)
    new_ok = all(any(P82.commit_in(r_, h) for r_ in P82.REPOS + (K.EF_DIR, K.KERNEL_DIR)) for h in new_tokens) and all(
        os.path.exists(os.path.join(ROOT, *b_.split('/'))) for _h, (b_, _l) in named)
    L += ['### the answer carrying `Root, second call` (%d characters): hex tokens b682`s reading takes as commits %s ; named by a bank`s row as a sha256 %s ; '
          'left for the commit reading after the mask %s' % (len(txt), old_tokens, ['%s by %s :%d' % (h, b_, l_) for h, (b_, l_) in named], new_tokens), '']
    cases.append(('G-ANSWERS-CHECKED', 'b705`s root answer (the second call): every hex token a commit at HEAD (old) ; every token a commit or a bank-named sha256 (repaired)',
                  old_ok, new_ok, (False, True)))
    planted = txt + ' deadbee1'
    pt = sorted(set(h for h in re.findall(r'\b([0-9a-f]{7,12})\b', planted) if re.search(r'[a-f]', h) and re.search(r'\d', h)))
    pm = planted
    for m in CIT._HEX8.finditer(planted):
        if m.group(1) in shas:
            pm = pm.replace(m.group(1), 'SHA-' + m.group(1)[:4] + '-' + m.group(1)[4:])
    pnt = sorted(set(h for h in re.findall(r'\b([0-9a-f]{7,12})\b', pm) if re.search(r'[a-f]', h) and re.search(r'\d', h)))
    cases.append(('G-ANSWERS-CHECKED', 'a mutated copy, a token no bank names (deadbee1) planted', all(P82.commit_in(ROOT, h) for h in pt), all(P82.commit_in(ROOT, h) for h in pnt), (False, False)))
    # ### (3) G-ENTRY-TITLE-FORM`s needle clause on b705`s title
    t5 = C5.K.__dict__ and '## The faces joined by closure at SIDE-faces-join held; the count’s contour encloses every zero of Λ_Q'
    nd5 = 'the faces joined by closure at SIDE-faces-join'
    cases.append(('G-ENTRY-TITLE-FORM', 'b705`s title and its needle: the needle clause of tools/b705_checks.py entry_title_ok (old) ; after _fold_article (repaired)',
                  nd5 in t5, nd5 in C6._fold_article(t5), (False, True)))
    tm = t5.replace('joined', 'split')
    cases.append(('G-ENTRY-TITLE-FORM', 'a mutated copy, the title`s "joined" set to "split"', nd5 in tm, nd5 in C6._fold_article(tm), (False, False)))
    # ### (4) prev_capture: b698`s window against the cut
    rows_all = ER.capture(SESSION, K.PREV_ANCHOR, SUBAGENTS)
    first = [r['ts'] for r in rows_all if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    cut = _anchor_ts(K.ANCHOR)
    cut_e = _iso_epoch(cut) if cut else None
    old_rows = [r for r in rows_all if first and first[0] <= r['ts']]
    new_rows = prev_capture()
    after_old = [r for r in old_rows if cut_e and (_iso_epoch(r['ts']) or 0) >= cut_e]
    after_new = [r for r in new_rows if cut_e and (_iso_epoch(r['ts']) or 0) >= cut_e]
    L += ['### the previous window: b698`s route from b705`s post-push combine to the session`s end %d commands, of which after (R316)`s line %d ; the cut route %d commands, '
          'after the line %d ; the anchor at %s' % (len(old_rows), len(after_old), len(new_rows), len(after_new), cut), '']
    cases.append(('prev_capture', 'this session from b705`s post-push combine: no command of the window after (R316)`s line', not after_old and bool(old_rows), not after_new and bool(new_rows), (False, True)))
    # ### (5) ROOT_EXCLUDE extended by declaration
    pat0 = R.ROOT_EXCLUDE
    import b706_record as SELF
    keep = SELF.declared_untracked
    try:
        SELF.declared_untracked = lambda: []
        p_none = SELF._root_exclude()
        SELF.declared_untracked = lambda: [('b706_x.py', 'x_units.jsonl')]
        p_decl = SELF._root_exclude()
    finally:
        SELF.declared_untracked = keep
    pat5 = P5.R.ROOT_EXCLUDE if hasattr(P5, 'R') else pat0
    old_m = bool(re.compile(pat5.pattern.replace('b705_', 'b706_')).match('b706_x_units.jsonl'))
    cases.append(('ROOT_EXCLUDE', 'no tool declares an untracked write: b706_x_units.jsonl excluded by name (old: b705`s pattern with the act renamed)', old_m, bool(p_none.match('b706_x_units.jsonl')), (False, False)))
    cases.append(('ROOT_EXCLUDE', 'a tool declares data/b706_x_units.jsonl untracked: the file excluded by name', old_m, bool(p_decl.match('b706_x_units.jsonl')), (False, True)))
    cases.append(('ROOT_EXCLUDE', 'the declaration present: a bank of a committed kind (b706_partners.txt) still named', not pat5.match('b705_partners.txt'), not p_decl.match('b706_partners.txt'), (True, True)))
    ok = True
    for name, src, o, nw, want in cases:
        asw = (bool(o), bool(nw)) == want
        ok = ok and asw
        L.append('  %-20s | %s | old %-5s | repaired %-5s | wanted old %s, repaired %s | %s' % (name, src, bool(o), bool(nw), want[0], want[1], 'AS WANTED' if asw else '### NOT AS WANTED'))
    dist = [n_ for n_, _s, o, nw, _w in cases if bool(o) != bool(nw)]
    L += ['', '### ### **CASES %d ; AS WANTED %s ; EACH REPAIRED READING DISTINGUISHED FROM THE OLD ON A ROW: %s.**' % (len(cases), ok, sorted(set(dist)))]
    put_txt('%s_repair_controls.txt' % ACT, L)
    print(NL.join(L[5:]))


def rootdry(*a):
    """data/b706_rules.txt row (1): the root route run DRY on the pre-root tree before the seal -- the banks the route names (ROOT_EXCLUDE
    extended), each read for CR LF, its status and its blob at HEAD; READY where every named bank is clean and equal at HEAD and none is CR LF
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b706_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b706_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


import fnmatch   # noqa: E402


# ================================================================================ COMPONENT 2: THE PARTNER COPIES, (R316)(3)
def _pairs():
    """the 17 partner pairs of data/b672_roster_read.json: [(doc, roster path, partner, highest_versioned)] where the two paths differ."""
    j = jl('b672_roster_read.json')
    return [(t['doc'], t['path'], t['partner'], t.get('highest_versioned')) for t in (j.get('tables') or [])
            if t.get('partner') and t.get('path') and t['partner'] != t['path']]


def pairs(*a):
    """prints, per pair, the two paths with their existence and line counts, which is the versioned copy, and every REGISTRY.md line naming
    either file by its basename (line number and text); writes nothing."""
    reg = rd(os.path.join(PP, 'REGISTRY.md')).split(NL)
    for doc, p, q, hv in _pairs():
        ver = hv if hv in (p, q) else None
        unv = q if ver == p else p
        print('=== %s | roster path %s | partner %s | versioned %s | unversioned %s' % (doc, p, q, ver, unv))
        for x in (p, q):
            fp = os.path.join(PP, *x.split('/'))
            print('    %-70s exists %s ; lines %s' % (x, os.path.exists(fp), len(rd(fp).split(NL)) if os.path.exists(fp) else '-'))
        for i, l in enumerate(reg, 1):
            if os.path.basename(p) in l or os.path.basename(q) in l or (os.path.basename(unv).replace('.md', '') + '`') in l:
                print('    REGISTRY :%d %s' % (i, l[:220]))


GEN_SUBJECT = re.compile(r'correspondence_gen|regenerated by|Correspondence cells written|Correspondence tables regenerated|by the generator', re.I)


def _blame(path, n):
    """the commit and subject of a PLACE-papers line, by git blame -L (porcelain)."""
    out = g(PP, 'blame', '-L', '%d,%d' % (n, n), '--porcelain', '--', path)
    sha = (out.split(NL)[0].split() or [''])[0]
    subj = g(PP, 'log', '-1', '--format=%s', sha).strip() if sha else ''
    return sha[:7], subj


def partners_read(*a):
    """(R316)(3), the first step per pair: the two Correspondence tables found by the roster's anchor in each copy (tools/correspondence_gen.py
    find_table), diffed line by line (difflib, autojunk off); every differing line with both sides' last commits by git blame and its cause
    read as b700's reading 4 read it (A REGENERATED CELL where either side's commit is a generator write; A HAND EDIT otherwise); the hand-edited
    lines printed WHOLE side by side for the seat's reading of their kind. data/b706_partners_read.txt (.json). Nothing written to a paper."""
    import difflib
    import correspondence_gen as CG
    j = jl('b672_roster_read.json')
    L = ['%s -- COMPONENT 2, (R316)(3): THE 17 PAIRS` CORRESPONDENCE TABLES DIFFED, EVERY DIFFERING LINE WITH ITS CAUSE, THE HAND-EDITED LINES SIDE BY SIDE (%s)' % (ACT, utc()), '',
         '### rows are differing lines per pair: the roster side :line | the partner side :line | the cause (b700`s reading: A REGENERATED CELL where a side`s last',
         '### commit is a generator write, else A HAND EDIT) | the two commits. Beneath each pair, every HAND EDIT line printed whole on both sides, for the kind',
         '### (R316)(3) enters: the versioned side carries it ; the unversioned side carries it ; both differ, raised. PLACE-papers HEAD %s.' % g(PP, 'rev-parse', '--short', 'HEAD').strip(), '']
    rows, hand_all = [], []
    for t in (j.get('tables') or []):
        p, q = t.get('path'), t.get('partner')
        if not q or q == p:
            continue
        hv = t.get('highest_versioned')
        ver = hv if hv in (p, q) else None
        x = rd(os.path.join(PP, *p.split('/'))).replace(chr(13), '').split(NL)
        y = rd(os.path.join(PP, *q.split('/'))).replace(chr(13), '').split(NL)
        rx, ry = CG.find_table(x, t), CG.find_table(y, t)
        if not isinstance(rx, tuple) or not isinstance(ry, tuple):
            L += ['=== %s : %s against %s -- TABLE NOT FOUND: %s / %s' % (t['doc'], p, q, rx if not isinstance(rx, tuple) else 'found', ry if not isinstance(ry, tuple) else 'found'), '']
            rows.append(dict(doc=t['doc'], path=p, partner=q, versioned=ver, found=False, differing=None, hand=[]))
            continue
        tx, ty = x[rx[0]:rx[1]], y[ry[0]:ry[1]]
        ops = [o for o in difflib.SequenceMatcher(None, tx, ty, autojunk=False).get_opcodes() if o[0] != 'equal']
        diff, hand = [], []
        for tag, i1, i2, j1, j2 in ops:
            for k in range(max(i2 - i1, j2 - j1)):
                a_ = (rx[0] + i1 + k + 1) if i1 + k < i2 else None
                b_ = (ry[0] + j1 + k + 1) if j1 + k < j2 else None
                ca = _blame(p, a_) if a_ else ('', '(the line on one side alone)')
                cb = _blame(q, b_) if b_ else ('', '(the line on one side alone)')
                cause = 'A REGENERATED CELL' if (GEN_SUBJECT.search(ca[1]) or GEN_SUBJECT.search(cb[1])) else 'A HAND EDIT'
                diff.append(dict(a=a_, b=b_, cause=cause, ca=ca, cb=cb))
                if cause == 'A HAND EDIT':
                    hand.append(dict(doc=t['doc'], a=a_, b=b_, roster_line=x[a_ - 1] if a_ else None, partner_line=y[b_ - 1] if b_ else None,
                                     roster_commit=ca, partner_commit=cb, roster_is_versioned=(ver == p)))
        L += ['=== %s : %s against %s -- the versioned copy %s ; the tables :%d-:%d and :%d-:%d ; DIFFERING %d ; HAND EDITS %d' % (
            t['doc'], p, q, 'the roster`s path' if ver == p else ('the partner' if ver == q else 'UNREAD'), rx[0] + 1, rx[1], ry[0] + 1, ry[1], len(diff), len(hand))]
        L += ['  :%-5s | :%-5s | %-20s | %s %s | %s %s' % (d['a'] or '-', d['b'] or '-', d['cause'], d['ca'][0], d['ca'][1][:70], d['cb'][0], d['cb'][1][:70]) for d in diff]
        for h in hand:
            L += ['  THE HAND EDIT, WHOLE:', '    the roster side %s :%s (%s): %s' % ('(VERSIONED)' if h['roster_is_versioned'] else '(unversioned)', h['a'] or '-', h['roster_commit'][0], h['roster_line']),
                  '    the partner    %s :%s (%s): %s' % ('(unversioned)' if h['roster_is_versioned'] else '(VERSIONED)', h['b'] or '-', h['partner_commit'][0], h['partner_line'])]
        L.append('')
        rows.append(dict(doc=t['doc'], path=p, partner=q, versioned=ver, found=True, differing=len(diff), hand=hand, spans=[list(rx), list(ry)]))
        hand_all += hand
    L += ['### ### **PAIRS %d ; TABLES FOUND %d ; DIFFERING LINES %d ; HAND EDITS %d (%s) ; REGENERATED CELLS %d.**' % (
        len(rows), sum(1 for r in rows if r['found']), sum(r['differing'] or 0 for r in rows), len(hand_all),
        ', '.join('%s %d' % (r['doc'], len(r['hand'])) for r in rows if r['hand']) or 'none', sum(r['differing'] or 0 for r in rows) - len(hand_all))]
    put_txt('%s_partners_read.txt' % ACT, L)
    put_json('%s_partners_read.json' % ACT, dict(at=utc(), rows=rows))
    print(NL.join([l for l in L if l.startswith('===') or l.startswith('    the ') or l.startswith('  THE HAND')] + L[-1:]))


def _pair_rows():
    """[(table record, versioned path, unversioned path)] for the 17 pairs, the versioned copy the roster's highest_versioned."""
    out = []
    for t in (jl('b672_roster_read.json').get('tables') or []):
        p, q = t.get('path'), t.get('partner')
        if not q or q == p:
            continue
        hv = t.get('highest_versioned')
        ver = hv if hv in (p, q) else None
        out.append((t, ver, (q if ver == p else p) if ver else None))
    return out


def _table_lines(path, t):
    import correspondence_gen as CG
    x = rd(os.path.join(PP, *path.split('/'))).replace(chr(13), '').split(NL)
    r = CG.find_table(x, t)
    return x, (r if isinstance(r, tuple) else None)


def partners_regen(*a):
    """(R316)(3), the second and third steps for every pair in one call: the generator's sources read once (one ls-remote per tabled kernel,
    the print banks, the grades), each VERSIONED copy's table regenerated by tools/correspondence_gen.py's own regen_bytes (the generator run
    once over the regenerated-cell lines into the versioned copy; its bytes written as the generator writes them, nothing else of the file
    touched); then the pair's two tables diffed: every remaining differing line printed whole -- a line equal on both sides to a hand-edited
    pair of data/b706_partners_read.txt is RESOLVED BY ITS KIND (the author's word: the versioned side carries it, counted apart from the zero
    diff), any other line REMAINING; the pair reads RENAME when no line remains, HELD otherwise. data/b706_partners.txt (.json). `dry` writes no
    paper and no bank."""
    import difflib
    import correspondence_gen as CG
    dry = 'dry' in a
    roster = jl('b672_roster_read.json')
    pr = jl('b706_partners_read.json')
    hand = {}
    for r in pr.get('rows') or []:
        for h in r.get('hand') or []:
            vline = h['roster_line'] if h['roster_is_versioned'] else h['partner_line']
            uline = h['partner_line'] if h['roster_is_versioned'] else h['roster_line']
            hand.setdefault(r['doc'], []).append((vline, uline, h))
    ks = CG.kernels_of(roster)
    tags, tlog = CG.read_tags(ks, remote=True)
    banks, blog = CG.read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=CG.read_grades(), present=CG.present)
    L = ['%s -- COMPONENT 2, (R316)(3): THE GENERATOR RUN ONCE INTO EACH VERSIONED COPY, THE PAIRS DIFFED, THE HAND-EDITED LINES RESOLVED BY THEIR KIND (%s)' % (ACT, utc()), '',
         '### rows are pairs in the roster`s order: the versioned copy (written by the generator`s regen_bytes) | the unversioned copy (not written) | the cells the',
         '### generator changed | the lines differing between the two tables after the run | of them RESOLVED BY KIND (the versioned side carries it: the author`s',
         '### word at the hand-edits prompt, data/b706_author_answers.txt) | REMAINING | the reading (RENAME where no line remains, else HELD). The sources: one',
         '### ls-remote per tabled kernel (%d kernels), the print banks at the tags, the grades -- the generator`s own readers.' % len(ks), '',
         '### THE TAGS READ: ' + ' ; '.join('%s %s %s' % (k, tg, (c or '')[:7]) for k, _rd, tg, c, _loc in tlog), '']
    rows = []
    for t, ver, unv in _pair_rows():
        doc = t['doc']
        if not ver:
            rows.append(dict(doc=doc, versioned=None, unversioned=None, reading='HELD: NO VERSIONED COPY'))
            L += ['=== %s -- HELD: no versioned copy in the roster' % doc, '']
            continue
        vp = os.path.join(PP, *ver.split('/'))
        vb = open(vp, 'rb').read()
        nb, res = CG.regen_bytes(vb, t, ctx, doc)
        changed = res['counts']['CELLS CHANGED']
        written = nb != vb
        if written and not dry:
            open(vp + '.tmp', 'wb').write(nb)
            os.replace(vp + '.tmp', vp)
        x, rx = _table_lines(ver, t) if not dry else (nb.decode('utf-8').replace(chr(13), '').split(NL), None)
        if dry:
            r_ = CG.find_table(x, t)
            rx = r_ if isinstance(r_, tuple) else None
        y, ry = _table_lines(unv, t)
        if rx is None or ry is None:
            # ### the author`s word at the first prompt: E_DIFFICULTY_THEOREM, its table in the versioned copy alone (the roster`s path) and not
            # ### in the unversioned one by the roster`s anchor, carries no differing line and proceeds with the rest (the second pass 0)
            one_sided_ok = (rx is not None and ry is None and changed == 0)
            rows.append(dict(doc=doc, versioned=ver, unversioned=unv, status=res.get('status'), cells_changed=changed, written=written, second_pass=0 if changed == 0 else None,
                             differing=0, resolved=0, apart=0, newer_unversioned=0,
                             reading='RENAME (THE TABLE IN THE VERSIONED COPY ALONE BY THE ANCHOR, NO DIFF TAKEN; the author`s word)' if one_sided_ok
                             else ('RENAME (TABLE IN NEITHER COPY BY THE ANCHOR)' if rx is None and ry is None else 'HELD: THE TABLE FOUND IN THE UNVERSIONED COPY ALONE, OR CELLS CHANGED')))
            L += ['=== %s : %s (versioned) | %s (unversioned) | the generator: %s, cells changed %d, written %s | the table by the anchor: versioned %s, unversioned %s | %s' % (
                doc, ver, unv, res.get('status'), changed, written, 'found' if rx else 'NOT FOUND', 'found' if ry else 'NOT FOUND', rows[-1]['reading']), '']
            continue
        tx, ty = x[rx[0]:rx[1]], y[ry[0]:ry[1]]
        # ### THE MEASURE THAT DECIDES THE RENAME (the author`s word at the zero-diff prompt, data/b706_author_answers.txt): the generator`s
        # ### second pass changes 0 cells in the surviving copy, and the retired copy carries nothing newer -- each remaining line`s two sides by
        # ### git blame (a line the generator has just written, uncommitted, is the newest)
        nb2, res2 = CG.regen_bytes(nb if not dry else nb, t, ctx, doc)
        second = res2['counts']['CELLS CHANGED']
        ops = [o for o in difflib.SequenceMatcher(None, tx, ty, autojunk=False).get_opcodes() if o[0] != 'equal']
        diff = []
        for tag, i1, i2, j1, j2 in ops:
            for k in range(max(i2 - i1, j2 - j1)):
                la = tx[i1 + k] if i1 + k < i2 else None
                lb = ty[j1 + k] if j1 + k < j2 else None
                va = (rx[0] + i1 + k + 1) if la is not None else None
                ub = (ry[0] + j1 + k + 1) if lb is not None else None
                if any(la == v_ and lb == u_ for v_, u_, _h in hand.get(doc, [])):
                    kind, cv, cu = 'RESOLVED BY KIND (the hand edit: the versioned side carries it)', ('', ''), ('', '')
                else:
                    cv = _blame(ver, va) if (va and not dry) else ('', '')
                    cu = _blame(unv, ub) if ub else ('', '')
                    dv = g(PP, 'log', '-1', '--format=%ct', cv[0]).strip() if cv[0] and not cv[0].startswith('0000000') else ''
                    du = g(PP, 'log', '-1', '--format=%ct', cu[0]).strip() if cu[0] and not cu[0].startswith('0000000') else ''
                    v_uncommitted = (not cv[0]) or cv[0].startswith('0000000')
                    newer_u = bool(du) and (not v_uncommitted) and bool(dv) and int(du) > int(dv)
                    kind = '### THE UNVERSIONED SIDE NEWER -- HELD' if newer_u else 'THE VERSIONED SIDE CARRIES IT (counted apart)'
                diff.append(dict(v=va, u=ub, kind=kind, vline=la, uline=lb, v_commit=cv, u_commit=cu))
        resolved = sum(1 for d in diff if d['kind'].startswith('RESOLVED'))
        apart = sum(1 for d in diff if d['kind'].startswith('THE VERSIONED'))
        newer = [d for d in diff if d['kind'].startswith('###')]
        reading = 'RENAME' if (second == 0 and not newer) else 'HELD: %s' % ('; '.join(([('THE SECOND PASS CHANGES %d CELLS' % second)] if second else []) + (['%d LINE(S) NEWER ON THE UNVERSIONED SIDE' % len(newer)] if newer else [])))
        rows.append(dict(doc=doc, versioned=ver, unversioned=unv, status=res.get('status'), cells_changed=changed, written=written, second_pass=second, differing=len(diff),
                         resolved=resolved, apart=apart, newer_unversioned=len(newer), reading=reading, spans=[list(rx), list(ry)], diff=diff))
        L += ['=== %s : %s (versioned) | %s (unversioned) | the generator: %s, cells changed %d, written %s, THE SECOND PASS CHANGES %d | differing after %d | '
              'the hand edits resolved by kind %d | the versioned side carries it, counted apart %d | newer on the unversioned side %d | %s' % (
                  doc, ver, unv, res.get('status'), changed, written, second, len(diff), resolved, apart, len(newer), reading)]
        for d in diff:
            L += ['  %-64s versioned :%-5s (%s %s) | unversioned :%s (%s %s)' % (d['kind'], d['v'] or '-', d['v_commit'][0] or '-', (d['v_commit'][1] or '')[:50],
                                                                                 d['u'] or '-', d['u_commit'][0] or '-', (d['u_commit'][1] or '')[:50]),
                  '      V: %s' % (d['vline'] if d['vline'] is not None else '(no line)'), '      U: %s' % (d['uline'] if d['uline'] is not None else '(no line)')]
        L.append('')
    ren = [r for r in rows if r['reading'].startswith('RENAME')]
    L += ['### ### **PAIRS %d ; THE GENERATOR WROTE %d VERSIONED COPIES (%d CELLS CHANGED) ; THE SECOND PASS CHANGES %d ; DIFFERING LINES AFTER THE RUN %d, THE HAND EDITS '
          'RESOLVED BY KIND %d, THE VERSIONED SIDE CARRIES IT (COUNTED APART) %d, NEWER ON THE UNVERSIONED SIDE %d ; RENAME %d ; HELD %d%s.**' % (
              len(rows), sum(1 for r in rows if r.get('written')), sum(r.get('cells_changed') or 0 for r in rows), sum(r.get('second_pass') or 0 for r in rows),
              sum(r.get('differing') or 0 for r in rows), sum(r.get('resolved') or 0 for r in rows), sum(r.get('apart') or 0 for r in rows),
              sum(r.get('newer_unversioned') or 0 for r in rows), len(ren), len(rows) - len(ren),
              (' (%s)' % ', '.join(r['doc'] for r in rows if r not in ren)) if len(rows) - len(ren) else '')]
    if not dry:
        put_txt('%s_partners.txt' % ACT, L)
        put_json('%s_partners.json' % ACT, dict(at=utc(), rows=rows, tags=dict((k, list(v)) for k, v in tags.items() if v)))
    else:
        L[0] = L[0].replace('THE GENERATOR RUN ONCE', 'A DRY RUN, NO PAPER WRITTEN: THE GENERATOR`S BYTES COMPUTED')
        put_txt('%s_partners_dry.txt' % ACT, L)
        put_json('%s_partners_dry.json' % ACT, dict(at=utc(), dry=True, rows=rows, tags=dict((k, list(v)) for k, v in tags.items() if v)))
    if 'show' in a:
        print(NL.join(L))
        return
    print(NL.join([l for l in L if l.startswith('===')] + L[-1:]))


def registry_rows(*a):
    """prints, per pair, REGISTRY.md's table rows naming the paper: the main row (`| id | title | \\`unversioned\\` | version |`) and the edition
    rows naming the versioned file; the version the versioned name carries beside, for the seat's Edit; writes nothing."""
    reg = rd(os.path.join(PP, 'REGISTRY.md')).split(NL)
    for t, ver, unv in _pair_rows():
        m = re.search(r'_v(\d+(?:_\d+)*)\.md$', ver or '')
        vtag = 'v' + m.group(1).replace('_', '.') if m else '?'
        print('=== %s | versioned %s -> the tag %s | unversioned %s' % (t['doc'], ver, vtag, unv))
        for i, l in enumerate(reg, 1):
            if l.startswith('| ') and (('`%s`' % unv) in l or ('`%s`' % ver) in l or (ver or '\x00') in l):
                print('    :%d %s' % (i, l[:260]))


def readers(*a):
    """`readers before | after`: (R316)(3)'s last step -- the 102 standing reader hits of b672 (relay tools at HEAD outside the act tools naming
    an unversioned file, git grep -F per basename over the 25 pairs of data/b672_one_copy.json) re-read, and the generator's roster re-read:
    each of the 19 tables found by its anchor at the unversioned name (the file of record after the rename). data/b706_readers_<stage>.txt (.json);
    `after` prints both stages side by side."""
    import b672_record as R72
    import correspondence_gen as CG
    stage = a[0] if a else 'before'
    pairs = (jl('b672_one_copy.json').get('pairs') or [])
    hits = dict((r['unversioned'], R72._standing_hits(os.path.basename(r['unversioned']))) for r in pairs)
    found = []
    for t in (jl('b672_roster_read.json').get('tables') or []):
        p, q = t.get('path'), t.get('partner')
        hv = t.get('highest_versioned')
        unv = p if (not q or q == p) else ((q if hv == p else p) if hv in (p, q) else p)
        fp = os.path.join(PP, *unv.split('/'))
        ok = False
        if os.path.exists(fp):
            r = CG.find_table(rd(fp).replace(chr(13), '').split(NL), t)
            ok = isinstance(r, tuple)
        found.append((t['doc'], unv, os.path.exists(fp), ok))
    L = ['%s -- COMPONENT 2, (R316)(3): THE STANDING READER HITS AND THE GENERATOR`S ROSTER RE-READ, %s THE RENAMES (%s)' % (ACT, stage.upper(), utc()), '',
         '### rows are the 25 pairs of relay data/b672_one_copy.json: the unversioned file | the standing readers naming its basename (relay tools at HEAD',
         '### outside the act tools, b672`s reader, git grep -F) ; then the 19 tables of the generator`s roster (data/b672_roster_read.json), each at the',
         '### unversioned name: the file present ; the table found by its anchor. PLACE-papers HEAD %s ; relay HEAD %s.' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), g(ROOT, 'rev-parse', '--short', 'HEAD').strip()), '']
    L += ['  %-70s hits %d' % (u, len(h)) for u, h in hits.items()]
    L += ['', '### THE ROSTER AT THE UNVERSIONED NAMES:'] + ['  %-36s %-70s present %-5s table %s' % (d, u, e, 'FOUND' if ok else 'NOT FOUND') for d, u, e, ok in found]
    tot = sum(len(h) for h in hits.values())
    nf = sum(1 for _d, _u, _e, ok in found if ok)
    if stage == 'after':
        b = jl('%s_readers_before.json' % ACT)
        L += ['', '### BEFORE THE RENAMES (data/%s_readers_before.txt): HITS %s ; TABLES FOUND %s -- AFTER: HITS %d ; TABLES FOUND %d ; EQUAL %s' % (
            ACT, b.get('hits'), b.get('found'), tot, nf, (b.get('hits') == tot and b.get('found') == nf))]
    L += ['', '### ### **STANDING READER HITS %d OVER %d PAIRS (b672: 102 OVER 21) ; ROSTER TABLES %d, FOUND AT THE UNVERSIONED NAME %d.**' % (
        tot, sum(1 for h in hits.values() if h), len(found), nf)]
    put_txt('%s_readers_%s.txt' % (ACT, stage), L)
    put_json('%s_readers_%s.json' % (ACT, stage), dict(at=utc(), stage=stage, hits=tot, found=nf, per_file=dict((u, len(h)) for u, h in hits.items()),
                                                      tables=[dict(doc=d, path=u, present=e, found=ok) for d, u, e, ok in found]))
    print(NL.join(L[-3:]))


# ================================================================================ COMPONENT 3: THE JOIN'S MANIFEST, (R316)(4) (b705's routes carried, the lakefile re-ordered)
KI = K.KERNEL_DIR
JOIN_FILES = ('lean-toolchain', 'lakefile.toml', 'FacesJoin.lean', 'print_targets.txt', '.github/workflows/build-module.yml', 'README.md', '.gitignore')


def _blob_sha(repo, rev, path):
    return g(repo, 'rev-parse', '%s:%s' % (rev, path)).strip()


def joinlake(*a):
    """data/b706_join_lakefile.txt: the join kernel's lakefile as edited by the Edit tool, printed WHOLE before the commit ((R316)(4) and the
    author's word: SIDEExplicitFormula, sideLvConservation, mathlib LAST, each at its same revision), its diff against 732c1b49's by line, the
    requires' order read from the text, and Lake's hint line cited from the run's artifact bank (data/b705_art_SIDE-faces-join_join_cache_log.txt
    :21); no lake-manifest.json at the root."""
    import difflib
    now = rd(os.path.join(KI, 'lakefile.toml')).replace(chr(13), '')
    old = (_show(KI, K.JOIN_TIP_B705, 'lakefile.toml') or '').replace(chr(13), '')
    def requires(text):
        """the [[require]] blocks in order: [(name, rev)] -- the block's own lines alone, not the package's or a lib's name line."""
        out = []
        for blk in re.split(r'(?m)^\[\[require\]\]\s*$', text)[1:]:
            body = re.split(r'(?m)^\[', blk)[0]
            nm = re.search(r'(?m)^name = "([^"]+)"', body)
            rv = re.search(r'(?m)^rev = "([0-9a-f]{40})"', body)
            out.append((nm.group(1) if nm else '?', rv.group(1) if rv else ''))
        return out
    names = [n for n, _r in requires(now)]
    revs = dict(requires(now))
    old_revs = dict(requires(old))
    hint = rdn('b705_art_SIDE-faces-join_join_cache_log.txt').split(NL)
    hl = next((i + 1 for i, l in enumerate(hint) if 'Try putting `require mathlib` last' in l), 0)
    d = list(difflib.unified_diff(old.split(NL), now.split(NL), 'lakefile.toml at 732c1b49', 'lakefile.toml (this act, the working tree)', lineterm=''))
    manifest = os.path.exists(os.path.join(KI, 'lake-manifest.json'))
    L = ['%s -- COMPONENT 3, (R316)(4) AND THE AUTHOR`S WORD: THE JOIN KERNEL`S LAKEFILE RE-ORDERED, PRINTED WHOLE BEFORE THE COMMIT (%s)' % (ACT, utc()), '',
         '### the requires in order: %s ; each at its revision %s ; the same revisions as at 732c1b49 %s ; mathlib LAST %s ; a lake-manifest.json at the root %s' % (
             names, dict((k, v[:8]) for k, v in revs.items()), revs == old_revs, names[-1:] == ['mathlib'], manifest),
         '### Lake`s hint, data/b705_art_SIDE-faces-join_join_cache_log.txt :%d: %s' % (hl, hint[hl - 1].strip() if hl else '### NOT FOUND'), '',
         '### THE LAKEFILE, WHOLE:'] + ['    ' + x for x in now.rstrip(NL).split(NL)] + ['', '### THE DIFF AGAINST 732c1b49 (%d lines):' % len(d)] + ['    ' + x for x in d]
    L += ['', '### ### **REQUIRES %d IN ORDER %s ; REVISIONS UNCHANGED %s ; MATHLIB LAST %s ; NO MANIFEST ON THIS HOST %s ; THE HINT CITED AT :%d.**' % (
        len(names), ' > '.join(names), revs == old_revs, names[-1:] == ['mathlib'], not manifest, hl)]
    put_txt('%s_join_lakefile.txt' % ACT, L)
    put_json('%s_join_lakefile.json' % ACT, dict(at=utc(), order=names, revs=revs, unchanged=revs == old_revs, mathlib_last=names[-1:] == ['mathlib'], manifest=manifest, hint_line=hl))
    print(NL.join(L[2:4] + L[-1:]))


def joinfiles(*a):
    """data/b706_join_files.txt: the join kernel's files at its commit, printed whole before the push, each with its blob id; the workflow's blob
    against SIDE-explicit-formula's at v0.37 (carried verbatim at b705; this act's workflow commit on SIDE-explicit-formula's main is not
    carried into the join); the pins and the three requirements read from the lakefile; no identifier of the author in any file."""
    import b706_checks as C6
    tip = g(KI, 'rev-parse', 'HEAD').strip()
    L = ['%s -- COMPONENT 3, (R316)(4): THE JOIN KERNEL %s AT ITS COMMIT %s, ITS FILES PRINTED BEFORE THE PUSH (%s)' % (ACT, K.KERNEL, tip[:7], utc()), '',
         '### rows are files at the commit: the path | its blob id | its bytes; each printed whole beneath. The workflow as b705 carried it from',
         '### SIDE-explicit-formula`s build-module.yml at v0.37 (blob %s); the lakefile requiring SIDEExplicitFormula at v0.37 = %s, sideLvConservation' % (
             _blob_sha(K.EF_DIR, K.EF_V037, '.github/workflows/build-module.yml')[:12], K.EF_V037[:7]),
         '### at v0.10.0 = %s and Mathlib at explicit-formula`s pin LAST, by git revision; nothing of either kernel edited.' % K.LV_V0100[:7], '']
    ident = []
    for f in JOIN_FILES:
        t = _show(KI, tip, f) or ''
        hits = [w for w in C6.IDENT_WF if w in t.lower() and not (w == 'psinary' and f in ('lakefile.toml',))]
        ident += [(f, w) for w in hits]
        L += ['  %-40s blob %s ; %d bytes%s' % (f, _blob_sha(KI, tip, f)[:12], len(t.encode('utf-8')), (' ; ### IDENTIFIER NEEDLE %s' % hits) if hits else '')]
    for f in JOIN_FILES:
        t = _show(KI, tip, f) or ''
        L += ['', '=== %s' % f] + ['    ' + x for x in t.rstrip(NL).split(NL)]
    wf_eq = _blob_sha(KI, tip, '.github/workflows/build-module.yml') == _blob_sha(K.EF_DIR, K.EF_V037, '.github/workflows/build-module.yml')
    lf = _show(KI, tip, 'lakefile.toml') or ''
    names = [re.search(r'(?m)^name = "([^"]+)"', re.split(r'(?m)^\[', b)[0]).group(1) for b in re.split(r'(?m)^\[\[require\]\]\s*$', lf)[1:]
             if re.search(r'(?m)^name = "([^"]+)"', re.split(r'(?m)^\[', b)[0])]
    pins = ('rev = "%s"' % K.EF_MATHLIB in lf, 'rev = "%s"' % K.EF_V037 in lf, 'rev = "%s"' % K.LV_V0100 in lf, (_show(KI, tip, 'lean-toolchain') or '').strip() == K.EF_LEAN)
    L += ['', '### ### **FILES %d AT %s ; THE WORKFLOW`S BLOB EQUAL TO SIDE-explicit-formula`S AT v0.37 %s ; MATHLIB %s, SIDE-explicit-formula v0.37 %s, SIDE-lv-conservation v0.10.0 %s REQUIRED BY REVISION, '
          'IN THE ORDER %s ; THE TOOLCHAIN v4.34.0-rc1 %s ; IDENTIFIER NEEDLES IN THE WORKFLOW OR THE MODULE %s.**' % (
              len(JOIN_FILES), tip[:7], wf_eq, pins[0], pins[1], pins[2], ' > '.join(names), pins[3], [x for x in ident if x[0] in ('.github/workflows/build-module.yml', 'FacesJoin.lean')] or 'NONE')]
    put_txt('%s_join_files.txt' % ACT, L)
    put_json('%s_join_files.json' % ACT, dict(at=utc(), tip=tip, workflow_equal=wf_eq, pins=list(pins), order=names, blobs=dict((f, _blob_sha(KI, tip, f)) for f in JOIN_FILES)))
    print(NL.join(L[:12] + L[-1:]))


def artfile(*a):
    """`artfile <kernel> <run id> <label> <name> [<name> ...]`: a named file of the run's artifact, read only after the artifact's sha256 equals
    the banked one (data/b706_runner_rows.json, the row read by its id) and the platform's digest; banked as data/b706_art_<kernel>_<label>_<name>.txt."""
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


JOIN_GRADES = P5.JOIN_GRADES
JOIN_E0 = P5.JOIN_E0


def joingrade(*a):
    """`joingrade <label>`: data/b706_join_grade.txt (.json) -- b705's route carried (its readers P3._thm_sig, P3._self_eq imported): faces_join's
    statement verbatim from the kernel at its commit, the seat's reading of its binders (none) and the grade, the shared E0 rule's grade as the
    check, the salt-check of REGISTRY.md :544 clause by clause, the runner's print of the name; on a run that is not DERIVES, the build's error
    lines printed by line and the join HELD; Lake's hint cited by its line in b705's artifact bank where the cause recurs."""
    import e0_rule as E
    label = a[0] if a else 'join'
    E.LEXICON.update(JOIN_E0)
    rows_ = jl('%s_runner_rows.json' % ACT).get('rows') or []
    run = next((r for r in reversed(rows_) if r.get('kernel') == K.KERNEL and r.get('label') == label), None)
    ax = rdn('%s_axioms_%s_%s.txt' % (ACT, K.KERNEL, label)) if run else ''
    AX = dict(_deps(ax))
    tip = g(KI, 'rev-parse', 'HEAD').strip()
    L = ['%s -- COMPONENT 3, (R316)(4) as (R315)(5) specified the grade: THE GRADE OF faces_join, READ FROM ITS STATEMENT, WITH E0 AND THE SALT-CHECK BESIDE IT (%s)' % (ACT, utc()), '',
         '### rows are, per theorem: the statement verbatim, the binders with their class read by hand, the grade they give, the E0 rule`s check, and',
         '### the salt-check`s clauses with their readings. The statement at %s %s; the profile from run %s (gate %s); the lakefile re-ordered, mathlib last' % (
             K.KERNEL, tip[:7], run['run_id'] if run else '### NO RUN', run['gate'] if run else '-'),
         '### (data/b706_join_lakefile.txt), Lake`s hint at data/b705_art_SIDE-faces-join_join_cache_log.txt :21.', '']
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
                ('the terminal states lv-conservation`s own declaration, no restatement in the module (N3)',
                 'SIDELvConservation.RegisterPentagon.Register4_positivity' in head and 'def Register4_positivity' not in (_show(KI, tip, fpath) or ''),
                 'the right-hand side names SIDELvConservation.RegisterPentagon.Register4_positivity; the module defines no Register4_positivity')]
        ok = all(s[1] for s in salt)
        allok = allok and ok and eg == hgrade
        L += ['== %s (%s :%d-:%d):' % (name, fpath, i, j)] + ['    ' + l for l in st.split(NL)]
        L += ['  THE BINDERS, READ BY HAND (the seat`s reading, before the check): %s' % ('NONE -- a closed statement' if not hand else '')]
        L += ['    %-12s : %-34s %s' % b for b in hand]
        L += ['  THE GRADE READ FROM THE STATEMENT: %s ; THE NAMED PREMISE: %s' % (hgrade, hprem),
              '  THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (JOIN_E0; the shared file not edited):',
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
        L += ['   (R316)(4): on any failure, the error banked by line and the join held, no second dispatch.', '']
    L += ['### ### **THEOREMS %d ; %s ; THE GATE %s ; THE JOIN %s ; EVERY SALT-CHECK PASSED AND EVERY CHECK AGREEING %s.**' % (
        len(JOIN_GRADES), ' ; '.join(summ), gate or '### NO RUN', 'HELD' if held else 'DERIVES AT THE STANDARD THREE', allok)]
    put_txt('%s_join_grade.txt' % ACT, L)
    put_json('%s_join_grade.json' % ACT, dict(at=utc(), tip=tip, run=run['run_id'] if run else None, gate=gate, held=held, ok=allok and not held, rows=summ))
    print(NL.join(L[-4:]))


# ================================================================================ COMPONENT 3: THE GENERATOR'S ROSTER AFTER THE RENAMES, (R316)(3) and (6)
def roster706(*a):
    """data/b706_roster_read.json (.txt): the generator's roster after the renames -- b672's 20 tables, each at the unversioned name (the file
    of record after (R316)(3)), its anchor unchanged, no partner; each table found by its anchor at that name. The generator and the figures
    tool read this roster from b706 on (tools/correspondence_gen.py ROSTER, the edit under (R316)(6) with its cause; the sealed figures tool's
    ROSTER rebound at the suite)."""
    import correspondence_gen as CG
    j = jl('b672_roster_read.json')
    out, L = [], ['%s -- COMPONENT 3: THE GENERATOR`S ROSTER AFTER THE RENAMES OF (R316)(3) (%s)' % (ACT, utc()), '',
                  '### rows are the 20 tables of data/b672_roster_read.json, each at its unversioned name, the file of record after the rename; the anchor as b672',
                  '### read it; the table found by that anchor now. No partner: the one copy.', '']
    for t in (j.get('tables') or []):
        p, q = t.get('path'), t.get('partner')
        hv = t.get('highest_versioned')
        unv = p if (not q or q == p) else ((q if hv == p else p) if hv in (p, q) else p)
        a_ = dict((k, v) for k, v in t.items() if k not in ('partner', 'partner_found', 'partner_identical', 'partner_lines_differing', 'found_b670', 'found_record', 'same_table', 'rows', 'rows_differing'))
        a_.update(b670_path=p, path=unv, highest_versioned=unv, renamed_at_b706=(unv != p))
        x = rd(os.path.join(PP, *unv.split('/'))).replace(chr(13), '').split(NL)
        r = CG.find_table(x, t)
        a_['found'] = [r[0] + 1, r[1]] if isinstance(r, tuple) else r
        out.append(a_)
        L.append('  %-36s %-70s renamed %-5s found %s' % (t['doc'], unv, a_['renamed_at_b706'], a_['found']))
    L += ['', '### ### **TABLES %d ; RENAMED AT b706 %d ; FOUND BY THE ANCHOR %d.**' % (len(out), sum(1 for a_ in out if a_['renamed_at_b706']), sum(1 for a_ in out if isinstance(a_['found'], list)))]
    put_txt('%s_roster_read.txt' % ACT, L)
    put_json('%s_roster_read.json' % ACT, dict(at=utc(), from_roster='b672_roster_read.json', tables=out))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE WORKFLOW'S PROBE STEP, (R316)(5)
WF = '.github/workflows/build-module.yml'


def wfstep(*a):
    """data/b706_workflow_step.txt (.json): SIDE-explicit-formula's build-module.yml as edited by the Edit tool, printed WHOLE before the commit,
    its diff against main (git diff), the new step's place read from the text (after the print step, before the closure), its separate
    artifact, and the identifier needles (none)."""
    import b706_checks as C6
    EF = K.EF_DIR
    now = rd(os.path.join(EF, WF)).replace(chr(13), '')
    before = (_show(EF, 'main', WF) or '').replace(chr(13), '')
    diff = subprocess.run(['git', '-C', EF, 'diff', '--', WF], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL).split(NL)
    ls = now.split(NL)
    step = lambda s: next((i + 1 for i, l in enumerate(ls) if l.strip().lstrip('- ') == s), 0)   # noqa: E731  ### a step line reads `- name: ...`
    i_print = step('name: Axioms of the named terminals')
    i_probe = step("name: Chain probe of the ref's root ChainProbe.lean")
    i_close = step("name: Constant closure of the kernel's own declarations")
    i_up = step("name: Upload the chain probe's artifact, separate from the run's")
    sep = 'name: chain-probe-${{ github.run_id }}' in now and 'path: probe/' in now
    ident = [w for w in C6.IDENT_WF if w in now.lower()]
    L = ['%s -- COMPONENT 3, (R316)(5), W-ORD-WORKFLOW-PROBE-STEP: SIDE-explicit-formula`s build-module.yml WITH ITS PROBE STEP, PRINTED WHOLE BEFORE THE COMMIT (%s)' % (ACT, utc()), '',
         '### the step: `Chain probe of the ref`s root ChainProbe.lean` at :%d, after the print step (:%d) and before the closure (:%d), run when the ref carries' % (i_probe, i_print, i_close),
         '### ChainProbe.lean at the root; its output probe/chainprobe.txt uploaded as a SEPARATE artifact chain-probe-<run id> by the step at :%d (%s); identifier' % (i_up, sep),
         '### needles in the file: %s. The edit by the Edit tool; main before the edit %s.' % (ident or 'NONE', g(EF, 'rev-parse', '--short', 'main').strip()), '',
         '### THE WORKFLOW, WHOLE:'] + ['    ' + x for x in now.rstrip(NL).split(NL)] + ['', '### THE DIFF AGAINST main (%d lines):' % len(diff)] + ['    ' + x for x in diff]
    ok = 0 < i_print < i_probe < i_close and sep and not ident and now != before
    L += ['', '### ### **THE PROBE STEP AT :%d, AFTER THE PRINT STEP :%d AND BEFORE THE CLOSURE :%d ; A SEPARATE ARTIFACT %s ; IDENTIFIER NEEDLES %s ; DIFF LINES %d ; AS ORDERED %s.**' % (
        i_probe, i_print, i_close, sep, ident or 'NONE', len(diff), ok)]
    put_txt('%s_workflow_step.txt' % ACT, L)
    put_json('%s_workflow_step.json' % ACT, dict(at=utc(), probe_line=i_probe, print_line=i_print, closure_line=i_close, upload_line=i_up, separate=sep, ident=ident,
                                                diff_lines=len(diff), ok=ok, main_before=g(EF, 'rev-parse', 'main').strip()))
    print(NL.join(L[2:5] + L[-1:]))


# ================================================================================ COMPONENT 3: THE GENERATOR'S REACH, (R316)(6)
CITE_FORM = re.compile(r'(SIDE-[a-z0-9]+(?:-[a-z0-9]+)*)(?:\s+at the (?:ζ )?page[’\']s pin)?\s+`?(v\d+(?:\.\d+)*)`?\s*=\s*`?([0-9a-f]{7,40})`?')


def genreach(*a):
    """`genreach forms`: the citation forms of the 11 table lines of data/b704_cells_reach.txt printed before the edit (data/b706_generator_forms.txt).
    `genreach`: after the edit -- the generator's dry run over data/b706_roster_read.json printing SIDE-explicit-formula among its parsed kernels
    with its cell count; THE CONTROL: the generator as committed at HEAD (its blob loaded as a module, unedited) and as edited both run over the
    roster's tables with one set of sources, every re-emitted file compared byte for byte, the diff empty; G-CORRESPONDENCE-CURRENCY's reach:
    how many counted rows name each parsed kernel. data/b706_generator_reach.txt (.json), data/b706_generator_diff.txt."""
    import correspondence_gen as CG
    if a and a[0] == 'forms':
        cre = rdn('b704_cells_reach.txt').split(NL)
        L = ['%s -- COMPONENT 3, (R316)(6): THE CELL FORMS IN WHICH THE 11 TABLE LINES NAME SIDE-explicit-formula, PRINTED FROM data/b704_cells_reach.txt BEFORE THE EDIT (%s)' % (ACT, utc()), '',
             '### rows are the table lines (data/b704_cells_reach.txt, "the line:" rows): the paper :line | each citation-form mention (kernel, version, commit) read by the form',
             '### `(name, SIDE-explicit-formula [at the page`s pin] vX = `sha`)`, the regex CITE_FORM the generator gains.', '']
        seen = set()
        n_m = 0
        for i, l in enumerate(cre):
            if l.strip().startswith('the line:') and i > 0:
                head = cre[i - 1].strip().split(' | ')
                key = (head[0], head[1]) if len(head) > 1 else (str(i), '')
                if key in seen:
                    continue
                seen.add(key)
                ms = [(k, v, c) for k, v, c in CITE_FORM.findall(l) if k == 'SIDE-explicit-formula']
                n_m += len(ms)
                L.append('  %-36s %-60s %s' % (key[0], key[1], ms or '(no citation-form mention of SIDE-explicit-formula; the kernel named otherwise)'))
        L += ['', '### ### **TABLE LINES %d ; CITATION-FORM MENTIONS OF SIDE-explicit-formula %d.**' % (len(seen), n_m)]
        put_txt('%s_generator_forms.txt' % ACT, L)
        print(NL.join(L[5:]))
        return
    import importlib.util
    roster = jl('b706_roster_read.json')
    # ### the generator at HEAD, unedited, loaded from its blob as a module of its own (the working tree holds the edit)
    src_head = _show(ROOT, 'HEAD', 'tools/correspondence_gen.py') or ''
    spec = importlib.util.spec_from_loader('correspondence_gen_head', loader=None, origin=os.path.join(T, 'correspondence_gen.py'))
    OLD = importlib.util.module_from_spec(spec)
    OLD.__file__ = os.path.join(T, 'correspondence_gen.py')
    exec(compile(src_head, 'tools/correspondence_gen.py@HEAD', 'exec'), OLD.__dict__)
    ks_new = CG.kernels_of(roster)
    ks_old = OLD.kernels_of(roster)
    tags, tlog = CG.read_tags(ks_new, remote=False)
    banks, blog = CG.read_banks(tags)
    ctx = dict(tags=tags, banks=banks, grades=CG.read_grades(), present=CG.present)
    rows, equal_all = [], True
    for t in roster['tables']:
        p = os.path.join(PP, *t['path'].split('/'))
        b = open(p, 'rb').read()
        nb_old, r_old = OLD.regen_bytes(b, t, ctx, t['doc'])
        nb_new, r_new = CG.regen_bytes(b, t, ctx, t['doc'])
        eq = nb_old == nb_new
        equal_all = equal_all and eq
        rows.append(dict(doc=t['doc'], path=t['path'], status=r_new.get('status'), cells_old=r_old['counts']['CELLS CHANGED'], cells_new=r_new['counts']['CELLS CHANGED'], equal=eq))
    # ### the reach: per kernel the rows naming it in the kernel cell and the citation-form mentions in any cell
    reach = {}
    for t in roster['tables']:
        p = os.path.join(PP, *t['path'].split('/'))
        x = open(p, 'rb').read().decode('utf-8').replace('\r\n', '\n').split('\n')
        ft = CG.find_table(x, t)
        if isinstance(ft, str):
            continue
        cols = CG.columns(x[ft[0]])
        for l in x[ft[0] + 1:ft[1]]:
            if CG.SEP_ROW.match(l):
                continue
            sp = CG.spans(l)
            named = set()
            if cols['kernel'] is not None and len(sp) > cols['kernel']:
                named |= set(k for k, _t in CG.parse_kernel_cell(CG.cell(l, sp[cols['kernel']])) if k)
            cited = set(k for k, _v, _c in CITE_FORM.findall(l))
            for k in named:
                reach.setdefault(k, dict(kernel_cell=0, cited=0))['kernel_cell'] += 1
            for k in cited:
                reach.setdefault(k, dict(kernel_cell=0, cited=0))['cited'] += 1
    dry = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'correspondence_gen.py'), 'dry', os.path.join(D, 'b706_roster_read.json')],
                         capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT)
    dtxt = ((dry.stdout or '') + (dry.stderr or '')).replace(chr(13), '').rstrip(NL).split(NL)
    gdiff = subprocess.run(['git', '-C', ROOT, 'diff', '--', 'tools/correspondence_gen.py'], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL).split(NL)
    put_txt('%s_generator_diff.txt' % ACT, ['%s -- (R316)(6): tools/correspondence_gen.py EDITED BY THE EDIT TOOL, THE DIFF AGAINST HEAD (%d lines) (%s)' % (ACT, len(gdiff), utc()), ''] + gdiff)
    L = ['%s -- COMPONENT 3, (R316)(6), W-ORD-CORRESPONDENCE-EF-REACH: THE GENERATOR`S PARSER EXTENDED TO THE CITATION FORM, ITS DRY RUN, THE BYTE-FOR-BYTE CONTROL, THE REACH (%s)' % (ACT, utc()), '',
         '### the roster: data/b706_roster_read.json (the 20 tables at the unversioned names after (R316)(3)). The edit: tools/correspondence_gen.py CITE_FORM and',
         '### kernels_of reading every cell`s citation-form mentions, ROSTER pointed at b706`s roster (its cause the renames), the regen functions untouched',
         '### (data/b706_generator_diff.txt). The parsed kernels before the edit %d, after %d: %s.' % (len(ks_old), len(ks_new), sorted(set(ks_new) - set(ks_old)) or 'NONE ADDED'), '',
         '### THE DRY RUN AFTER THE EDIT (tools/correspondence_gen.py dry data/b706_roster_read.json, exit %d), its print:' % dry.returncode] + ['    ' + x for x in dtxt]
    L += ['', '### THE CONTROL: every roster table re-emitted by the generator at HEAD (unedited) and as edited, from one set of sources, compared byte for byte:']
    L += ['  %-36s %-66s %-28s cells old %d new %d ; EQUAL %s' % (r['doc'], r['path'], r['status'], r['cells_old'], r['cells_new'], r['equal']) for r in rows]
    L += ['', '### THE REACH (G-CORRESPONDENCE-CURRENCY): rows naming each parsed kernel in the kernel cell | citation-form mentions in any cell:']
    L += ['  %-36s kernel cell %3d | cited %3d' % (k, v['kernel_cell'], v['cited']) for k, v in sorted(reach.items())]
    L += ['', '### ### **PARSED KERNELS %d (SIDE-explicit-formula AMONG THEM %s, ITS CITATION-FORM CELLS %d) ; THE CONTROL: TABLES %d, EVERY RE-EMISSION EQUAL BYTE FOR BYTE %s ; THE DRY RUN EXIT %d.**' % (
        len(ks_new), 'SIDE-explicit-formula' in ks_new, (reach.get('SIDE-explicit-formula') or {}).get('cited', 0), len(rows), equal_all, dry.returncode)]
    put_txt('%s_generator_reach.txt' % ACT, L)
    put_json('%s_generator_reach.json' % ACT, dict(at=utc(), kernels_old=sorted(ks_old), kernels_new=sorted(ks_new), control=rows, equal=equal_all, reach=reach, dry_exit=dry.returncode))
    print(NL.join(L[2:5] + L[-1:]))


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, rootexclude=rootexclude, armsort=armsort, c1=c1,
              repairs=repairs, repairctl=repairctl, rootdry=rootdry, pairs=pairs, partners_read=partners_read, partners_regen=partners_regen,
              registry_rows=registry_rows, readers=readers, joinlake=joinlake, joinfiles=joinfiles, artfile=artfile, joingrade=joingrade, roster706=roster706, wfstep=wfstep, genreach=genreach)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b706_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
