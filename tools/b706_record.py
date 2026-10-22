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
    ('(6) tools/b706_record.py `runner706`, `_artifact_named` -- ANSWERS the carry under (R316)(5) and (7): b698`s runner (tools/b698_record.py '
     'runner, carried by tools/b705_record.py) reads the run`s FIRST LISTED artifact; a run of the workflow as edited under (R316)(5) uploads '
     'two, build-module-<run id> and chain-probe-<run id>, so the first listed may be the probe`s. runner706 chooses the run`s own artifact by '
     'name and is printed whole (the sealed tool has no function of that name); every other clause b698`s -- the sha256 against the platform`s '
     'digest before any reading, the build`s exit and error lines, the memory log, the print step, the gate. The two print runs were read through '
     'it, the join run through b698`s (one artifact). The control: data/b706_repair_controls.txt.', 'b698_record.py', 'b706_record.py', 'runner706',
     ('_artifact_named',)),
    ('(7) tools/b706_standing_figures.py `correspondence`, `partners`, `_roster` -- ANSWERS the carry under (R316)(3): b703`s readers '
     '(tools/b703_standing_figures.py :106-:156 and :186-:206, carried through tools/b705_standing_figures.py) take their roster from '
     'data/b672_roster_read.json, whose `path` is the VERSIONED copy for nine tables and whose `partner` the unversioned copy of each pair; after '
     'the renames those paths are gone (nine tables missing, seventeen partners in archive/). correspondence() is carried line for line over THIS '
     'ACT`S roster (data/b706_roster_read.json, the 20 tables at the unversioned names, each found by its anchor); partners() reads one copy per '
     'table, the figure 0 with every row ONE COPY, the order`s unit having no two copies from b706 on. No sealed module`s constant is rebound. '
     'The control: data/b706_repair_controls.txt.', 'b703_standing_figures.py', 'b706_standing_figures.py', 'correspondence', ('partners', '_roster')),
    ('(8) tools/b706_checks.py `partners_fig_ok`, G-PARTNER-COPIES -- ANSWERS the pre-run`s first standing-c run: b703`s fig_ok '
     '(tools/b703_checks.py :1127-:1130) reads a figure against the previous act`s alone, and with the partner copies resolved under (R316)(3) '
     'the figure drops from b705`s 131 to 0 (one copy per table), so the arm`s positive control -- the live figure raised by one -- still passed '
     'against 131 and the harness read the arm DEFECTIVE. The repaired predicate, printed whole, reads the partners figure against the LOWER of '
     'b705`s figure and this act`s banked reading (data/b706_standing_figures.json): the baseline reset to the reading the resolution gives, no '
     'regression from it admitted; the other three figures read b703`s predicate unchanged. The control: data/b706_repair_controls.txt.',
     'b703_checks.py', 'b706_checks.py', 'partners_fig_ok', ()),
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
    # ### (6) the run`s artifact chosen by name (runner706) against b698`s first-listed reading, on a listing in the order the platform gives it
    arts2 = [dict(name='chain-probe-39852365437', id=1), dict(name='build-module-39852365437', id=2)]
    arts1 = [dict(name='chain-probe-39852365437', id=1)]
    pick_old = lambda arts: (arts[0] if arts else None)   # noqa: E731  ### b698`s choice: the first listed (tools/b698_record.py runner)
    pick_new = lambda arts: next((x for x in arts if (x.get('name') or '').startswith('build-module-')), None)   # noqa: E731  ### _artifact_named`s clause
    listed = re.search(r"^### the artifacts listed (\d+): (\[.*\])", rd(os.path.join(D, 'b706_runner_SIDE-explicit-formula_prints_v0_1.txt')), re.M)
    L += ['### the artifacts the v0.1 print run listed, in the platform`s order: %s' % (listed.group(2) if listed else '### NOT READ'), '']
    cases.append(('runner706', 'two artifacts listed, the probe`s first: the run`s own (build-module-) chosen', (pick_old(arts2) or {}).get('name', '').startswith('build-module-'),
                  (pick_new(arts2) or {}).get('name', '').startswith('build-module-'), (False, True)))
    cases.append(('runner706', 'a mutated listing, the probe`s artifact alone: nothing chosen', (pick_old(arts1) or {}).get('name', '').startswith('build-module-'),
                  (pick_new(arts1) or {}).get('name', '').startswith('build-module-'), (False, False)))
    # ### (7) the standing figures` roster after the renames: b703`s readers over b672`s roster against b706`s over this act`s
    import b703_standing_figures as SF3
    import b706_standing_figures as SF6
    old_files = [t.get('path') for t in SF3._roster()] + [t.get('partner') for t in SF3._roster() if t.get('partner')]
    new_files = [t.get('path') for t in SF6._roster()]
    old_present = bool(old_files) and all(os.path.exists(os.path.join(PP, *p.split('/'))) for p in old_files)
    new_present = bool(new_files) and all(os.path.exists(os.path.join(PP, *p.split('/'))) for p in new_files)
    L += ['### the rosters` files present in the working tree: b672`s %d paths and partners, present %s ; b706`s %d paths, present %s' % (
        len(old_files), old_present, len(new_files), new_present), '']
    cases.append(('standing_figures', 'every file the roster names present after the renames (b672`s roster: old ; this act`s: repaired)', old_present, new_present, (False, True)))
    _po, rows_old = SF3.partners()
    _pn, rows_new = SF6.partners()
    old_read = bool(rows_old) and all(r.get('differing') is not None for r in rows_old)
    new_read = bool(rows_new) and all(r.get('differing') is not None for r in rows_new) and all((r.get('reason') or '').startswith('ONE COPY') for r in rows_new)
    L += ['### partners(): b703`s over b672`s roster %d rows, every row read %s (%d with a copy not found) ; b706`s over this act`s roster %d rows, every row ONE COPY %s' % (
        len(rows_old), old_read, sum(1 for r in rows_old if r.get('differing') is None), len(rows_new), new_read), '']
    cases.append(('standing_figures', 'partners(): every roster row read (no copy missing), each row of one copy', old_read, new_read, (False, True)))
    # ### (8) the partners figure`s baseline: b703`s fig_ok against b705`s 131 alone, the repaired predicate against the lower of 131 and this act`s 0
    fj6 = jl('%s_standing_figures.json' % ACT)
    base5 = jl('b705_standing_figures.json')
    S8 = dict(fig=dict(partners=dict(figure=(fj6.get('partners') or {}).get('figure'))), fig_prev=dict(partners=dict(figure=(base5.get('partners') or {}).get('figure'))), figj=fj6)
    S8m = dict(fig=dict(partners=dict(figure=((fj6.get('partners') or {}).get('figure') or 0) + 1)), fig_prev=S8['fig_prev'], figj=fj6)
    L += ['### the partners figure: this act`s banked reading %s, b705`s %s' % ((fj6.get('partners') or {}).get('figure'), (base5.get('partners') or {}).get('figure')), '']
    cases.append(('G-PARTNER-COPIES', 'the live figure (0) against b705`s 131 (old) ; against the lower of 131 and this act`s banked 0 (repaired)', C3.fig_ok(S8, 'partners'), C6.partners_fig_ok(S8), (True, True)))
    cases.append(('G-PARTNER-COPIES', 'a mutated copy, the live figure raised by one (the arm`s own positive control)', C3.fig_ok(S8m, 'partners'), C6.partners_fig_ok(S8m), (True, False)))
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


# ================================================================================ COMPONENT 4: THE ENTRY-TAG PRINTS, (R316)(7)
EF = K.EF_DIR
TAG_THEOREMS = {'v0.1': 'SIDEExplicitFormula.B321.ch_iff_rh', 'v0.2': 'SIDEExplicitFormula.B321.h2_sign_iff_rh'}   # ### the mentioned theorems, data/b704_cells_reach.txt :84-:94


def tagstate(*a):
    """`tagstate <tag>`: the tag's tree read through the tool (no blob through the shell): its files, lean-toolchain, the lakefile's name and
    require lines, the mentioned theorem's module by git grep bounded to the tree; writes nothing."""
    tag = a[0]
    tree = (g(EF, 'ls-tree', '-r', '--name-only', tag) or '').split()
    lt = (_show(EF, tag, 'lean-toolchain') or '').strip()
    lf_name = next((f for f in ('lakefile.toml', 'lakefile.lean') if f in tree), None)
    lf = (_show(EF, tag, lf_name) or '') if lf_name else ''
    req = [l.strip() for l in lf.split(NL) if 'require' in l or 'mathlib' in l.lower() or 'lean_lib' in l or 'name' in l][:12]
    thm = TAG_THEOREMS.get(tag, '')
    short = thm.split('.')[-1]
    hit = g(EF, 'grep', '-n', '-E', '-e', r'^(theorem|lemma) +%s\b' % re.escape(short), tag, '--', '*.lean').strip()
    print('  tag %s ; peel %s ; files %d ; lean-toolchain %r ; lakefile %s' % (tag, g(EF, 'rev-list', '-n', '1', tag).strip()[:12], len(tree), lt, lf_name))
    print('  the lakefile`s require and lib lines: %s' % req)
    print('  print_targets.txt in the tree %s ; the workflow in the tree %s ; lake-manifest.json %s' % ('print_targets.txt' in tree, WF in tree, 'lake-manifest.json' in tree))
    print('  the theorem %s: %s' % (thm, hit[:160] or '### NOT FOUND'))


TAG_MODULES = {'v0.1': 'SIDEExplicitFormula.H2Bridge', 'v0.2': 'SIDEExplicitFormula.Seam'}   # ### the mentioned theorems' modules at the tags (tagstate)


def printprobe(*a):
    """`printprobe <tag>`: the scratch branch prints-b706-<tag>, checked out at the tag with no tracked change, given (R316)(7)'s three files
    by this route -- the workflow as SIDE-explicit-formula's main carries it after (R316)(5) (its blob's bytes, verbatim), print_targets.txt
    naming the mentioned theorem alone, and a root ChainProbe.lean in tools/chain_page.py's probe form (PROBE_HEAD, one #chain_cell for the
    theorem, the import of its module alone) for the workflow's probe step; the files banked with their sha256 in
    data/b706_print_files_<branch>.json (.txt) before the commit. Nothing else of the tag's tree is touched."""
    import hashlib
    import io as _io
    import chain_page as CP
    tag = a[0]
    br = 'prints-b706-%s' % tag
    thm, mod = TAG_THEOREMS[tag], TAG_MODULES[tag]
    head = g(EF, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    base = g(EF, 'rev-parse', 'HEAD').strip()
    peel = g(EF, 'rev-list', '-n', '1', tag).strip()
    dirty = g(EF, 'status', '--porcelain', '--untracked-files=no').strip()
    if head != br or base != peel or dirty:
        sys.exit('### THE CHECKOUT IS NOT %s AT %s WITH NO TRACKED CHANGE (head %s at %s, dirty %r) -- NOTHING WRITTEN' % (br, tag, head, base[:7], dirty))
    wf_text = _show(EF, 'main', WF) or ''
    pt_text = thm + NL
    probe = CP.PROBE_HEAD.replace('@@IMPORTS@@', 'import %s' % mod) + NL + '#chain_cell %s [%s] []' % (thm, thm) + NL
    files = {WF: wf_text, 'print_targets.txt': pt_text, 'ChainProbe.lean': probe}
    os.makedirs(os.path.join(EF, '.github', 'workflows'), exist_ok=True)
    for f, t in files.items():
        _io.open(os.path.join(EF, *f.split('/')), 'w', encoding='utf-8', newline=NL).write(t)
    files['lakefile.toml'] = _show(EF, tag, 'lakefile.toml') or ''
    files['lean-toolchain'] = _show(EF, tag, 'lean-toolchain') or ''
    shas = dict((f, hashlib.sha256(t.encode('utf-8')).hexdigest()) for f, t in files.items())
    L = ['%s -- COMPONENT 4, (R316)(7): THE SCRATCH BRANCH %s AT %s = %s, ITS THREE FILES WRITTEN BY THIS ROUTE AND BANKED BEFORE THE COMMIT (%s)' % (ACT, br, tag, peel[:7], utc()), '',
         '### rows are files: the path | sha256 | bytes. The workflow is main`s blob (%s) verbatim; the print list the mentioned theorem alone; the probe' % (_blob_sha(EF, 'main', WF)[:12]),
         '### chain_page.py`s PROBE_HEAD with the import of %s and one #chain_cell; the lakefile and toolchain the tag`s own, unedited.' % mod, '']
    L += ['  %-40s sha256 %s ; %d bytes' % (f, shas[f], len(t.encode('utf-8'))) for f, t in files.items()]
    for f in (WF, 'print_targets.txt', 'ChainProbe.lean'):
        L += ['', '=== %s' % f] + ['    ' + x for x in files[f].rstrip(NL).split(NL)]
    L += ['', '### ### **BRANCH %s AT %s ; FILES WRITTEN 3 ; THE WORKFLOW EQUAL TO main`S BLOB %s ; THE TARGET MODULE %s ; THE THEOREM %s.**' % (
        br, peel[:7], hashlib.sha256(wf_text.encode('utf-8')).hexdigest() == hashlib.sha256((_show(EF, 'main', WF) or '').encode('utf-8')).hexdigest(), mod, thm)]
    put_txt('%s_print_files_%s.txt' % (ACT, br), L)
    put_json('%s_print_files_%s.json' % (ACT, br), dict(at=utc(), branch=br, tag=tag, peel=peel, theorem=thm, module=mod, blobs=files, sha256=shas))
    print(NL.join(L[:8] + L[-1:]))


def _artifact_named(repo, run_id, prefix):
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    return next((x for x in arts if (x.get('name') or '').startswith(prefix)), None), arts


def runner706(*a):
    """`runner706 <kernel> <run id> <ref> <label> <note...>`: b698's runner carried with one change (this act's repair (6), data/b706_tool_repairs.txt):
    the run's artifact chosen BY NAME (build-module-<run id>) where b698's reader takes the first listed -- a run of the workflow as edited
    under (R316)(5) uploads a second artifact (chain-probe-<run id>); everything else b698's: the artifact's sha256 against the platform's digest
    before any reading, the build's exit and error lines, the memory log, the print step read, the gate."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    art, arts = _artifact_named(repo, run_id, 'build-module-')
    art = art or {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt')),
         '### the artifacts listed %d: %s ; the run`s own chosen by name (build-module-)' % (len(arts), [x.get('name') for x in arts])]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = __import__('hashlib').sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, kernel, label), blog.rstrip(NL).split(NL))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:15] + L[-3:]))


def printsbank(*a):
    """`printsbank <tag> <run id>`: the run's SEPARATE chain-probe artifact (chain-probe-<run id>) read by name, its sha256 against the platform's
    digest before any reading; probe/chainprobe.txt banked as data/b706_prints_<tag>.txt (the probe's own print, parsed by tools/chain_page.py's
    parser as the banked chain probes are) with data/b706_prints_<tag>.json (the run, the artifact, the parsed cell)."""
    import hashlib
    import io as _io
    import zipfile
    import chain_page as CP
    tag, run_id = a[0], int(a[1])
    repo = 'psinary-sketch/SIDE-explicit-formula'
    art, arts = _artifact_named(repo, run_id, 'chain-probe-')
    if not art:
        sys.exit('### NO chain-probe ARTIFACT ON RUN %d (listed %s) -- NOTHING READ' % (run_id, [x.get('name') for x in arts]))
    rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
    sha = hashlib.sha256(rz.stdout).hexdigest()
    digest = (art.get('digest') or '').replace('sha256:', '')
    if not digest or digest != sha:
        sys.exit('### THE PROBE ARTIFACT`S SHA256 %s IS NOT THE PLATFORM`S DIGEST %s -- NOTHING READ' % (sha[:16], digest[:16]))
    with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
        names_ = z.namelist()
        text = z.read('chainprobe.txt').decode('utf-8', 'replace').replace(chr(13), '') if 'chainprobe.txt' in names_ else ''
        log = z.read('chainprobe_log.txt').decode('utf-8', 'replace').replace(chr(13), '') if 'chainprobe_log.txt' in names_ else ''
    cells, errors = CP.parse(text)
    thm = TAG_THEOREMS[tag]
    c = cells.get(thm) or {}
    L = ['%s -- THE ENTRY-TAG PRINT AT %s (SIDE-explicit-formula %s), RUN %d, THE PROBE STEP`S OUTPUT READ AFTER THE PROBE ARTIFACT`S SHA256 %s AGREED WITH THE PLATFORM`S (%s)' % (
        ACT, tag, g(EF, 'rev-list', '-n', '1', tag).strip()[:7], run_id, sha[:16], utc()), '### the probe`s log: %s' % ' '.join(log.split()),
         '### the artifact %s (id %s, %s bytes) ; files %s ; the probe`s errors %d ; the cell %s: %s' % (
             art.get('name'), art.get('id'), art.get('size_in_bytes'), names_, len(errors), thm, ('statement ' + c.get('statement', '')) if c.get('statement') else ('### ' + ('MISSING' if c.get('missing') else 'NOT PARSED'))),
         ''] + text.rstrip(NL).split(NL)
    put_txt('%s_prints_%s.txt' % (ACT, tag), L)
    put_json('%s_prints_%s.json' % (ACT, tag), dict(at=utc(), tag=tag, run_id=run_id, artifact=dict(id=art.get('id'), name=art.get('name'), sha256=sha), files=names_,
                                                   log=log, errors=errors, cell=c, theorem=thm))
    print(NL.join(L[:3]))


def cellsreach(*a):
    """data/b706_cells_reread.txt (.json): (R316)(7)'s last step -- the 11 unbanked mentions of data/b704_cells_reach.txt re-read against the new
    print banks (data/b706_prints_v0.1.txt, data/b706_prints_v0.2.txt): the statement at the named tag from the bank beside the statement at
    v0.37 (data/b704_probe_out_zeta.txt), printed "equal" or "differs"; a mention naming no tag stays unbanked (no bank holds a tag it does not
    name)."""
    import chain_page as CP
    cells37, _e = CP.parse(rdn('b704_probe_out_zeta.txt'))
    banks = dict((tg, CP.parse(rdn('b706_prints_%s.txt' % tg))[0]) for tg in TAG_THEOREMS)
    prev = jl('b704_cells_reach.json').get('rows') or []
    rows = []
    for r in prev:
        if r.get('verdict') == 'EQUAL':
            continue
        tg, full = r.get('tag'), r.get('full')
        st37 = (cells37.get(full) or {}).get('statement') if full else None
        st_t = ((banks.get(tg) or {}).get(full) or {}).get('statement') if (tg in banks and full) else None
        if tg in banks and full:
            v = 'equal' if (st_t and st37 and ' '.join(st_t.split()) == ' '.join(st37.split())) else ('differs' if (st_t and st37) else 'unbanked (the bank holds no cell for the name)')
        else:
            v = 'unbanked (no tag named beside the kernel)'
        rows.append(dict(doc=r['doc'], path=r['path'], line=r['line'], full=full or r.get('id'), tag=tg, st37=st37, st_t=st_t, verdict=v, bank=('data/b706_prints_%s.txt' % tg) if tg in banks else None))
    L = ['%s -- COMPONENT 4, (R316)(7): THE 11 UNBANKED MENTIONS OF data/b704_cells_reach.txt RE-READ AGAINST THE ENTRY-TAG PRINT BANKS (%s)' % (ACT, utc()), '',
         '### rows are mentions (paper :line | theorem | tag): the statement at the tag from data/b706_prints_<tag>.txt (the probe step`s print, run on the scratch',
         '### branch at the tag) against the statement at v0.37 (data/b704_probe_out_zeta.txt, run 39721668586); "equal" or "differs"; a mention with no tag',
         '### beside the kernel stays unbanked. The paths as b704 read them (before (R316)(3)`s renames; the lines unchanged in the renamed files).', '']
    for r in rows:
        L += ['  %s | %s :%d | %s | tag %s | %s' % (r['doc'], r['path'], r['line'], r['full'], r['tag'], r['verdict']),
              '      at v0.37: %s' % (r['st37'] or '-'), '      at %s (%s): %s' % (r['tag'], r['bank'] or 'no bank', r['st_t'] or '-')]
    L += ['', '### ### **MENTIONS RE-READ %d ; EQUAL %d ; DIFFERS %d ; UNBANKED %d (no tag named %d).**' % (
        len(rows), sum(1 for r in rows if r['verdict'] == 'equal'), sum(1 for r in rows if r['verdict'] == 'differs'),
        sum(1 for r in rows if r['verdict'].startswith('unbanked')), sum(1 for r in rows if 'no tag named' in r['verdict']))]
    put_txt('%s_cells_reread.txt' % ACT, L)
    put_json('%s_cells_reread.json' % ACT, dict(at=utc(), rows=rows))
    print(NL.join([l for l in L if l.startswith('  ') and ' | tag ' in l] + L[-1:]))


# ================================================================================ COMPONENT 5: THE STANDING FIGURES FROM THIS ACT'S ROSTER (repair (7))
def figures(*a):
    """data/b706_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py -- correspondence() and partners() over
    THIS ACT'S roster after the renames (repair (7)), readme() b705's repaired one, pins() b703's -- each against b705's figure
    (data/b705_standing_figures.json), the pins baseline b705's rows; the partners rows printed ONE COPY, the correspondence rows per paper."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b705_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b706, READ FROM THIS ACT`S ROSTER AFTER THE RENAMES OF (R316)(3), AGAINST b705`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the unversioned names --',
         '### data/b706_tool_repairs.txt row (7); readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s, imported unedited), %.0f s;' % (t1 - t0),
         '### each arm fails on a regression from the previous act`s figure (data/b705_standing_figures.json).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b706 %s ; b705 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE (the order`s unit, lines differing between two copies, has no two copies from b706 on):']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b706: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b705`S %s, %s, %s, %s ; THE ROSTER THIS ACT`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


# ================================================================================ COMPONENT 5: THE ORDERS AT OPEN_TRAILS, (R316)(3)-(7)
ORDERS = [
    (K.ORDER_PARTNER, 'W-ORD-PAPER-PARTNER-COPIES',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-PAPER-PARTNER-COPIES` (:15446), under `(R316)`(3) and the author’s words at its two prompts -- THE ORDER DISCHARGED:*',
     ' disposition (iii) taken up over the 17 pairs of relay data/b700_reading4.txt. The 8 hand-edited lines read side by side first (relay '
     'data/b706_partners_read.txt), every one of the kind “the versioned side carries it”, resolved by that kind on the author’s word and counted '
     'apart from the zero diff; the generator run once into the versioned copies (26 cells at SIMPLICITY_OF_RIEMANN_ZEROS, 13 at '
     'SILENCE_STAGES_DEALIGNMENT, measured dry before any paper was written: data/b706_partners_dry.txt); the zero diff read against the '
     'generator on the author’s word -- the second pass changing 0 cells in the surviving copy and the retired copy carrying nothing newer -- '
     'with the 107 remaining lines printed on both sides and counted apart, every one the versioned side’s, 0 newer on the unversioned side, '
     '17 renamed and 0 held (data/b706_partners.txt); E_DIFFICULTY_THEOREM’s table in its versioned copy alone, no diff taken. Per pair, in '
     'the written order: the unversioned copy retired to archive/2026-10-22-b706-partner-copies/ by git mv with its history, the versioned copy '
     'renamed by git mv to the unversioned name, REGISTRY’s row keeping the version as its tag, one commit alone (PLACE-papers 1dfd9bc..cedf7e9, '
     'seventeen). The 102 standing reader hits equal before and after, the roster’s 20 tables found at the unversioned names '
     '(data/b706_readers_after.txt). The ruling’s unscoped “diffed to zero” the navigator’s (c). The Project mirror’s roster names as renamed '
     'from this act’s export. Status DISCHARGED.'),
    (K.ORDER_LV_JOIN, 'W-ORD-LV-CLOSURE-JOIN',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-LV-CLOSURE-JOIN` (:15452; its opening step read at :15494), under `(R316)`(4) -- THE JOIN HELD AT lv-conservation’s MODULE:*',
     ' SIDE-faces-join’s manifest repaired (W-ORD-FACES-JOIN-MANIFEST, directly below) and the join dispatched once at b37a7b6 (run '
     '39850337262, read by its id, the artifact’s sha256 verified): the cache served (8,691 files), Mathlib and its packages built from the '
     'cache, lv-conservation’s fifteen files rebuilt at the shared pin and the build HELD at SIDELvConservation/GammaBounds.lean :177:8 '
     '(“Tactic `rewrite` failed: Did not find an occurrence of the pattern”) at Mathlib de5ce8a9 -- the price b703 read at the pins: a failing '
     'lv module blocks the join under the condition and is priced then as an lv forward-port at a new tag; FacesJoin.lean not reached, the gate '
     'NOT DERIVES, no tag, no second dispatch (relay data/b706_join_grade.txt, data/b706_buildlog_SIDE-faces-join_join.txt). For the next '
     'ruling: the forward-port of lv-conservation’s GammaBounds.lean at the shared pin, or the join at another pin, priced there. Status OPEN.'),
    (K.ORDER_LV_JOIN, 'W-ORD-LV-CLOSURE-JOIN',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-LV-CLOSURE-JOIN` (:15452), under `(R316)`(4) and the author’s word at the manifest prompt -- THE ORDER **`W-ORD-FACES-JOIN-MANIFEST`**, ENTERED AND DISCHARGED:*',
     ' named by b705’s trail (:15592) for this ruling: the join’s lakefile such that Lake resolves Mathlib’s transitive packages from Mathlib’s '
     'own manifest and the cache serves. At b705’s run (39799253764) the root carried no lake-manifest.json and `require mathlib` stood first, so '
     'Lake took the transitive packages from the last require’s manifest, lv-conservation’s at Lean v4.29.1 (defect (j) there). Done at b706: '
     'the lakefile re-ordered by the Edit tool -- SIDEExplicitFormula v0.37, sideLvConservation v0.10.0, then mathlib LAST at de5ce8a9, each at '
     'its same revision -- Lake’s own hint from the run’s artifact (cache.log :21) on the author’s word; no manifest written on this host; the '
     'lakefile printed before the commit (relay data/b706_join_lakefile.txt); one commit b37a7b6 on main, pushed in main mode and read back; one '
     'dispatch, the cache served and Mathlib built, so the manifest’s object is met; the join held past it at lv-conservation’s own module '
     '(above). The ruling’s order “Mathlib explicit before both” the navigator’s (b), the order that had failed; the ferry’s lake-manifest.json '
     'at 732c1b49 the navigator’s (a), the tree carrying none. Status DISCHARGED.'),
    (K.ORDER_PROBE_STEP, 'W-ORD-WORKFLOW-PROBE-STEP',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-WORKFLOW-PROBE-STEP` (:15544), under `(R316)`(5) -- THE ORDER DISCHARGED:*',
     ' build-module.yml on SIDE-explicit-formula’s main given the step “Chain probe of the ref’s root ChainProbe.lean” at :101, after the print '
     'step (:81) and before the closure (:117): where the ref carries a root ChainProbe.lean (imported by no module) it imports each module of the '
     'target above that file’s text and runs it, its output uploaded as the separate artifact chain-probe-<run id> (:140); no other step changed. '
     'Edited by the Edit tool, printed before the commit (relay data/b706_workflow_step.txt, 49 diff lines, no identifier), one commit badaccc on '
     'main under this ruling, pushed in the push tool’s main mode and read back (data/b706_ef_push_out.txt); no dispatch on main for it. The '
     'step exercised by the two entry-tag dispatches of (R316)(7) on scratch branches carrying the workflow at main, both prints read from the '
     'separate artifact. The trigger for the chain’s next probe, b708. Status DISCHARGED.'),
    (K.ORDER_EF_REACH, 'W-ORD-CORRESPONDENCE-EF-REACH',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-CORRESPONDENCE-EF-REACH` (:15546), under `(R316)`(6) -- THE ORDER DISCHARGED:*',
     ' the cell forms printed from relay data/b704_cells_reach.txt before the edit: 11 table lines, 15 citation-form mentions of '
     'SIDE-explicit-formula (data/b706_generator_forms.txt). tools/correspondence_gen.py’s parser extended by the Edit tool to the form '
     '“(`theorem`, SIDE-explicit-formula vX = `sha`)” in any cell (CITE_FORM, kernels_of, cite_mentions; the diff in data/b706_generator_diff.txt), '
     'its roster read from data/b706_roster_read.json at the unversioned names. The dry run after the edit: 17 kernels parsed, '
     'SIDE-explicit-formula among them with 13 citation-form cells; the control: every roster table re-emitted by the generator unedited and as '
     'edited from one set of sources, 20 of 20 equal byte for byte, the diff empty; G-CORRESPONDENCE-CURRENCY’s reach printed beside its figure, '
     'the 17 parsed kernels named with their kernel-cell and cited counts (data/b706_generator_reach.txt). Status DISCHARGED.'),
    (K.ORDER_TAG_PRINTS, 'W-ORD-ENTRY-TAG-PRINTS',
     '*Appended 2026-10-22 by b706 beneath `W-ORD-ENTRY-TAG-PRINTS` (:15590), under `(R316)`(7) -- THE ORDER DISCHARGED:*',
     ' for each of v0.1 = baed4df and v0.2 = 5c72cad a scratch branch cut at the tag carrying the workflow at main, a one-name print list and a '
     'root ChainProbe.lean naming the mentioned theorem -- prints-b706-v0.1 at 748f2a9 (ch_iff_rh, SIDEExplicitFormula.H2Bridge) and '
     'prints-b706-v0.2 at 34e098a (h2_sign_iff_rh, SIDEExplicitFormula.Seam), their files banked before each dispatch '
     '(data/b706_print_files_prints-b706-v0.1.txt, -v0.2.txt); one dispatch per branch (runs 39852365437, 39852975531), read by their ids with the '
     'artifacts’ sha256 verified, both DERIVES; the probe step’s print read from the separate chain-probe artifact and banked at '
     'data/b706_prints_v0.1.txt and data/b706_prints_v0.2.txt (each theorem at the standard three, its statement equal to v0.37’s); each branch '
     'deleted by name locally and at the remote after its bank was committed (relay 4e1fdef0), the tags untouched. The 11 unbanked mentions '
     're-read against the new banks: 9 equal, 0 differs, 2 unbanked (no tag named beside the kernel: SIMPLICITY_OF_RIEMANN_ZEROS :442, '
     'FACES_LEDGER :20) (data/b706_cells_reread.txt). Status DISCHARGED.'),
]


def orders(*a):
    """the six order lines appended to OPEN_TRAILS through b698's guarded landing, each beneath its order by its line (the ledger is
    append-only); data/b706_orders.json."""
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', h, NL + h + b + NL) for _ln, _nm, h, b in ORDERS], '%s_orders.json' % ACT, 'orders', entry=None,
         check=[('OPEN_TRAILS.md', ln, nm) for ln, nm, _h, _b in ORDERS], dry=dry)


# ================================================================================ COMPONENT 6: THE SCORES (b686's order), THE RECORD, THE TRAIL, THE DRY RUN, THE MIRROR
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
num_word = P3.num_word
_trail_defects, _trail_resolved = P3._trail_defects, P3._trail_resolved


def _bank_utc(text):
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', NL.join((text or '').split(NL)[:2]))
    return _iso_epoch(m.group(1)) if m else None


def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _ts_epoch(ts):
    return _iso_epoch((ts or '')[:19] + 'Z') if ts else None


def _n1():
    """N1: no lean process on this host; three runner dispatches (the join, the two entry-tag branches), each read by its run id with its
    artifact's sha256 verified."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    rr = jl('%s_runner_rows.json' % ACT).get('rows') or []
    want = {K.JOIN_RUN: K.JOIN_TIP}
    want.update(dict((K.PRINT_RUNS[t], None) for t, _b in K.PRINT_BRANCHES))
    by_run = dict((d.get('run_id'), d) for d in dj)
    rows_ok = len(dj) == 3 and sorted(by_run) == sorted(want) and all(d.get('whole') is True for d in dj) and by_run[K.JOIN_RUN].get('ref') == K.JOIN_TIP \
        and all(by_run[K.PRINT_RUNS[t]].get('ref', '').startswith(K.PRINT_TIPS[t]) for t, _b in K.PRINT_BRANCHES)
    shas = dict((r.get('run_id'), r.get('artifact_sha256') or '') for r in rr)
    read_ok = len(rr) == 3 and sorted(shas) == sorted(want) and all(re.match(r'^[0-9a-f]{64}$', s) for s in shas.values())
    pj = dict((t, jl('%s_prints_%s.json' % (ACT, t))) for t, _b in K.PRINT_BRANCHES)
    probe_ok = all(pj[t].get('run_id') == K.PRINT_RUNS[t] and re.match(r'^[0-9a-f]{64}$', (pj[t].get('artifact') or {}).get('sha256') or '') for t in pj)
    art = rdn('%s_art_%s_join_cache_log.txt' % (ACT, K.KERNEL))
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == 3 and rows_ok and read_ok and probe_ok \
        and 'AGREED WITH THE BANKED AND THE PLATFORM`S' in art
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches in the capture: %s (relay data/b706_commands.json); the '
        'dispatches bank (relay data/b706_dispatches.json): %s, each whole by data/b705_rules.txt row (1); each run read by its id with its artifact`s '
        'sha256 (relay data/b706_runner_rows.json): %s; the two chain-probe artifacts read by name with their sha256 (relay data/b706_prints_v0.1.json, '
        'v0.2): %s; the join`s cache log read after its artifact agreed' % (
            cm.get('local_lean') if cm else 'unread', len(cm.get('dispatches') or []) if cm else 'unread',
            ['%s %s run %s whole %s' % (d.get('label'), (d.get('ref') or '')[:7], d.get('run_id'), d.get('whole')) for d in dj],
            ['%s %s' % (r.get('label'), (r.get('artifact_sha256') or 'UNREAD')[:16]) for r in rr],
            ['%s %s' % (t, ((pj[t].get('artifact') or {}).get('sha256') or 'UNREAD')[:16]) for t in pj]))


def _n2():
    """N2: every renamed pair diffs to zero before its git mv (the generator's second pass 0, nothing newer on the retired side), the reader hits
    and the roster count equal after the renames; no pair renamed while its diff is not zero."""
    pj = jl('%s_partners.json' % ACT).get('rows') or []
    ren = [r for r in pj if str(r.get('reading', '')).startswith('RENAME')]
    held = [r['doc'] for r in pj if r not in ren]
    zero = all(r.get('second_pass') == 0 and r.get('newer_unversioned') == 0 for r in ren)
    first = _git_ct(PP, K.C2_PP_FIRST)
    at = _bank_utc(rdn('%s_partners.txt' % ACT))
    dry_at = _bank_utc(rdn('%s_partners_dry.txt' % ACT))
    before = bool(first) and dry_at is not None and dry_at < first
    rb, ra = rdn('%s_readers_before.txt' % ACT), rdn('%s_readers_after.txt' % ACT)
    pat = r'STANDING READER HITS (\d+) OVER (\d+) PAIRS .*?ROSTER TABLES (\d+), FOUND AT THE UNVERSIONED NAME (\d+)'
    mb, ma = re.search(pat, ' '.join(rb.split())), re.search(pat, ' '.join(ra.split()))
    hits = bool(mb) and bool(ma) and mb.group(1) == ma.group(1) and ma.group(3) == ma.group(4)
    ok = len(pj) == 17 and len(ren) == 17 and not held and zero and before and hits
    return ('HELD' if ok else 'REFUTED'), (
        'pairs %d, renamed %d, held %s (relay data/b706_partners.json); the second pass changing 0 cells and nothing newer on the retired side for every '
        'renamed pair: %s; the generator`s run measured dry at %s, before the first rename commit %s (%s): %s; the standing reader hits %s before and %s '
        'after the renames, the roster`s %s tables found %s at the unversioned names (relay data/b706_readers_before.txt, data/b706_readers_after.txt); '
        'the 107 remaining lines counted apart, every one the versioned side`s, on the author`s word; the bank`s own print at %s after the renames' % (
            len(pj), len(ren), held or 'none', zero, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(dry_at)) if dry_at else '-', K.C2_PP_FIRST,
            R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(first)) if first else '-', before, mb.group(1) if mb else '-', ma.group(1) if ma else '-',
            ma.group(3) if ma else '-', ma.group(4) if ma else '-', R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(at)) if at else '-'))


def _n3():
    """N3: the join's lakefile names Mathlib at de5ce8a9 before both requires; its grade reads DERIVES at the standard three against
    lv-conservation's own declaration, or the join holds with the error banked by line."""
    lj = jl('%s_join_lakefile.json' % ACT)
    order = lj.get('order') or []
    revs = lj.get('revs') or {}
    at_pin = revs.get('mathlib', '').startswith(K.EF_MATHLIB[:8]) if isinstance(revs.get('mathlib'), str) else (K.EF_MATHLIB in json.dumps(revs))
    before_both = bool(order) and order[0] == 'mathlib'
    last = bool(order) and order[-1] == 'mathlib' and lj.get('mathlib_last') is True
    jg = jl('%s_join_grade.json' % ACT)
    t = rdn('%s_join_grade.txt' % ACT)
    errs = [l for l in rdn('%s_buildlog_%s_join.txt' % (ACT, K.KERNEL)).split(NL) if l.startswith('error:')]
    states = 'SIDELvConservation.RegisterPentagon.Register4_positivity SIDEExplicitFormula.LiWeil.LiCoeff' in (_show(KI, K.JOIN_TIP, 'FacesJoin.lean') or '')
    tag = g(KI, 'tag', '--list', K.JOIN_TAG).strip()
    held = jg.get('held') is True and jg.get('gate') == 'NOT DERIVES' and '== THE JOIN HELD' in t and len(errs) >= 1 and tag == '' \
        and any('GammaBounds.lean:177' in l for l in errs)
    derives = jg.get('held') is False and jg.get('gate') == 'DERIVES' and tag != ''
    second = states and (held or derives)
    ok = at_pin and before_both and second
    return ('HELD' if ok else 'REFUTED'), (
        'the join`s lakefile (relay data/b706_join_lakefile.txt): the requires in the order %s, Mathlib at de5ce8a9 %s, Mathlib BEFORE both requires %s '
        '-- the expectation`s first clause is the ruling`s order (R316)(4), the order that had already failed at b705`s run; on the author`s word Lake`s '
        'own hint was taken, mathlib LAST (%s), the ruling`s order the navigator`s (b), so the first clause reads REFUTED by the author`s word; the second '
        'clause: faces_join states lv-conservation`s own declaration %s, the run`s gate %s, the join %s with %d error lines banked by line '
        '(SIDELvConservation/GammaBounds.lean :177, relay data/b706_buildlog_SIDE-faces-join_join.txt), the tag %s %s, no second dispatch: %s' % (
            ' > '.join(order) or 'UNREAD', at_pin, before_both, last, states, jg.get('gate'), 'HELD' if jg.get('held') else 'DERIVES', len(errs), K.JOIN_TAG,
            tag or 'NOT MADE', 'HELD' if second else 'REFUTED'))


def _n4():
    """N4: the generator re-emits every pre-edit cell byte for byte; the entry-tag branches are deleted after their banks are committed and the
    tags stand at baed4df and 5c72cad."""
    gj = jl('%s_generator_reach.json' % ACT)
    ctl = gj.get('control') or []
    bytes_ok = gj.get('equal') is True and bool(ctl) and all(c.get('equal') for c in ctl)
    c4 = _git_ct(ROOT, K.C4_RELAY)
    rows = R.capture()
    dels = [r for r in rows if r['tool'] in ('Bash', 'PowerShell') and any(b in r['cmd'] for _t, b in K.PRINT_BRANCHES) and ('branch -D' in r['cmd'] or '--delete' in r['cmd'])]
    dts = [_ts_epoch(r['ts']) for r in dels]
    after = bool(c4) and len(dels) == 4 and all(x and x > c4 for x in dts)
    gone = all(g(EF, 'branch', '--list', b).strip() == '' for _t, b in K.PRINT_BRANCHES)
    tags = dict((t, g(EF, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % t).strip()) for t, _b in K.PRINT_BRANCHES)
    tags_ok = tags.get('v0.1') == K.EF_V01 and tags.get('v0.2') == K.EF_V02
    ok = bytes_ok and after and gone and tags_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the generator`s control (relay data/b706_generator_reach.json): %d roster tables re-emitted unedited and as edited from one set of sources, every '
        'one equal byte for byte %s; the four branch deletes (two local, two remote) in the capture at %s, after the banks` commit %s at %s: %s; the branches '
        'gone locally %s; the tags v0.1 %s, v0.2 %s against baed4df, 5c72cad: %s' % (
            len(ctl), bytes_ok, ['%s' % (r['ts'] or '')[:19] for r in dels], K.C4_RELAY, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(c4)) if c4 else '-',
            after, gone, (tags.get('v0.1') or '-')[:7], (tags.get('v0.2') or '-')[:7], tags_ok))


def _n5():
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    ef_past = [l for l in g(EF, 'log', '--first-parent', '--format=%H', K.EF_V037 + '..main').split(NL) if l.strip()]
    ef_files = sorted(x for x in g(EF, 'diff', '--name-only', K.EF_V037, 'main').split(NL) if x.strip())
    main_ok = ef_main == K.EF_MAIN and len(ef_past) == 1 and ef_files == [K.WORKFLOW] and not g(EF, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    join_tags = g(KI, 'tag', '--list').strip()
    pj = jl('%s_partners.json' % ACT).get('rows') or []
    pair_files = set(r.get('versioned') for r in pj) | set(r.get('unversioned') for r in pj)
    archive = set(K.ARCHIVE_DIR + '/' + r.get('unversioned') for r in pj)
    allowed = set(K.PP_WRITTEN) | pair_files | archive | {K.FACES_PAGE}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in allowed]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    ren_beyond = [l for l in renames if not any(p in l for p in pair_files)]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b706_', x) and x not in ['tools/' + t for t in K.REPAIRED_TOOLS]]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b706_|audit_b706_)', x) or re.match(r'^data/terminal_table', x)
                                                or x in ['tools/' + t for t in K.REPAIRED_TOOLS] or (x.startswith('data/') and x[5:] in R.N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B705_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(EF, lock) + _amended_after(KI, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_ef = _show(EF, K.EF_MAIN, K.WORKFLOW) or ''
    wf_ki = _show(KI, K.JOIN_TIP, K.WORKFLOW) or ''
    wf_ok = bool(wf_ef) and bool(wf_ki) and not any(w in (wf_ef + wf_ki).lower() for w in ('psinary', 'seale', 'york', 'hotmail', 'orcid', 'secrets.'))
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    ok = k_ok and main_ok and join_tags == '' and not pp_beyond and not ren_beyond and not kinds_beyond and not shared_tools and not differ and arms_ok \
        and not amended and not ident and wf_ok and not chained and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-explicit-formula`s '
            'main one commit past v0.37 touching the workflow alone and no tag past it: %s; the join kernel`s tags: %s; the standing arms added beyond b705`s '
            'face, the act arms apart: %s (%s); shared tools edited beyond the one the ruling names (tools/correspondence_gen.py, (R316)(6)): %s; sealed tools '
            'not agreeing: %s; commits amended after the seal: %s; deletes with anything chained after: %s; one git write per message (%s): %s; PLACE-papers '
            'beyond the two ledgers, REGISTRY, the 17 pairs` files and their archive paths and the faces page: %s; papers moved or renamed beyond the 17 pairs` '
            'git mv: %s (renames %d); relay files of a kind beyond the act`s banks and tools, the generator, the table, the root list, the corrigenda bank and '
            'b705`s push-out bank: %s; the glossary unchanged: %s; outbound requests other than git and gh %d, an identifier of the author in %s; no identifier '
            'in the workflow at SIDE-explicit-formula`s main or the join kernel`s: %s' % (
                K.DRAFT, k_ok, main_ok, join_tags or 'NONE', added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                chained or 'NONE', gw_note, gw_ok, pp_beyond or 'NONE', ren_beyond or 'NONE', len(renames), kinds_beyond or 'NONE', gl, len(ob),
                [r['line'] for r in ident] or 'NONE', wf_ok))


def scores(*a):
    """`scores [dry]` writes data/b706_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b706_scores_close.json."""
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
    return ('### b706 — lane two, act one hundred and thirty-three, the re-cut act under (R316): b705 at its weight; the six post-seal failures '
            'sorted and three tools repaired; the seventeen partner pairs renamed in place; the join’s manifest repaired and the join held at '
            'lv-conservation’s module; the workflow’s probe step; the generator reaching the central kernel; the entry-tag prints at v0.1 and v0.2; '
            'the faces row held')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    ol = [x.get('line') for x in (jl('%s_orders.json' % ACT).get('lines') or [])]
    pj = jl('%s_partners.json' % ACT).get('rows') or []
    ren = [r['doc'] for r in pj if str(r.get('reading', '')).startswith('RENAME')]
    held = [r['doc'] for r in pj if r['doc'] not in ren]
    dj = jl('%s_partners_dry.json' % ACT).get('rows') or []
    cells = dict((r['doc'], r.get('cells_changed')) for r in dj if r.get('written'))
    jg = jl('%s_join_grade.json' % ACT)
    errs = [l for l in rdn('%s_buildlog_%s_join.txt' % (ACT, K.KERNEL)).split(NL) if l.startswith('error:')]
    ws = jl('%s_workflow_step.json' % ACT)
    gr = jl('%s_generator_reach.json' % ACT)
    reach = (gr.get('reach') or {}).get('SIDE-explicit-formula') or {}
    pr = dict((t, jl('%s_prints_%s.json' % (ACT, t))) for t, _b in K.PRINT_BRANCHES)
    cj = jl('%s_cells_reread.json' % ACT).get('rows') or []
    fj_, f5 = jl('%s_standing_figures.json' % ACT), jl('b705_standing_figures.json')
    ra = ' '.join(rdn('%s_readers_after.txt' % ACT).split())
    m = re.search(r'STANDING READER HITS (\d+) OVER (\d+) PAIRS .*?ROSTER TABLES (\d+), FOUND AT THE UNVERSIONED NAME (\d+)', ra)
    return dict(corr_line=co.get('entry_line', '-'), orders=ol, renamed=len(ren), held=held, pairs=len(pj), cells=cells,
                apart=sum(r.get('apart') or 0 for r in pj), resolved=sum(r.get('resolved') or 0 for r in pj), newer=sum(r.get('newer_unversioned') or 0 for r in pj),
                join_gate=jg.get('gate', '-'), join_held=jg.get('held'), join_run=jg.get('run', '-'), join_errs=len(errs),
                wf_ok=ws.get('ok'), wf_lines=(ws.get('print_line'), ws.get('probe_line'), ws.get('closure_line'), ws.get('upload_line')),
                gen_kernels=len(gr.get('kernels_new') or []), gen_cited=reach.get('cited', '-'), gen_equal=gr.get('equal'),
                prints=dict((t, dict(run=pr[t].get('run_id'), stmt=((pr[t].get('cell') or {}).get('statement') or '-'), axioms=((pr[t].get('cell') or {}).get('axioms') or []),
                                     module=((pr[t].get('cell') or {}).get('module') or '-'))) for t in pr),
                cells_n=len(cj), cells_eq=sum(1 for r in cj if r.get('verdict') == 'equal'), cells_df=sum(1 for r in cj if r.get('verdict') == 'differs'),
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs5=dict((k, (f5.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                hits=(m.group(1), m.group(3), m.group(4)) if m else ('-', '-', '-'))


def _title():
    f = _figs()
    return ('## %d of %d partner pairs renamed in place, %d held; SIDE-faces-join %s; the workflow’s probe step; the generator reaching '
            'SIDE-explicit-formula, %s cells; the entry-tag prints at v0.1 and v0.2, %d of %d mentions equal' % (
                f['renamed'], f['pairs'], len(f['held']), 'held at lv-conservation’s module, its manifest repaired' if f['join_held'] else 'v0.1.0, the faces joined by closure',
                f['gen_cited'], f['cells_eq'], f['cells_n']))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    f = _figs()
    return ('(1) the eight hand-edited lines of the 17 pairs each resolved by their kind, the versioned side carrying every one, and the 107 lines '
            'remaining after the generator’s run counted apart and printed with both sides, every one the versioned side’s, the zero diff read '
            'against the generator on the author’s two answers, the first prompt put on an unmeasured premise (f); (2) E_DIFFICULTY_THEOREM '
            'renamed with its Correspondence table in its versioned copy alone, no diff taken, on the author’s word; (3) the join’s lakefile '
            're-ordered mathlib LAST on Lake’s own hint and the author’s word, the ruling’s order the navigator’s (b) and the ferry’s manifest the '
            'navigator’s (a), the join then held at lv-conservation’s GammaBounds.lean :177 at the shared pin, the price b703 read, no tag, no '
            'second dispatch, N3 refuted on its first clause; (4) the two print runs read through a runner that chooses the run’s own artifact by '
            'name, the workflow as edited uploading two; (5) the print runs labelled prints_v0_1 and prints_v0_2, b698’s reader admitting no dot; '
            '(6) the standing figures read from this act’s roster, the partners figure 0 with one copy per table; (7) the partners bank re-run '
            'after the generator’s write, the 39 cells standing in the dry bank; (8) G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE declared '
            'failing on the held join; (9) the %s navigator %s (%s) and the seat’s %s defect%s as lettered' % (
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
    p1, p2 = f['prints'].get('v0.1') or {}, f['prints'].get('v0.2') or {}
    e = ['', _title(), '',
         'The re-cut act’s five objects read: the seventeen partner pairs are renamed in place -- the eight hand-edited lines each carried by the '
         'versioned side and resolved by that kind, the generator run once (%s), the second pass changing 0 and nothing newer on the retired side, '
         '%d lines counted apart, %d renamed and %d held; SIDE-faces-join’s manifest is repaired (mathlib last, Lake’s own hint) and dispatched once, '
         'the cache served and Mathlib built, the join %s at lv-conservation’s GammaBounds.lean :177 at the shared pin with FacesJoin.lean not '
         'reached; the workflow’s probe step stands on SIDE-explicit-formula’s main at badaccc; the generator parses SIDE-explicit-formula’s '
         'citation form, %s cells, every re-emission byte-equal; and the entry-tag prints at v0.1 and v0.2 both DERIVES at the standard three, '
         '%d of %d mentions equal, %d differing.' % (
             ', '.join('%d at %s' % (v, k) for k, v in f['cells'].items()) or 'no cell changed', f['apart'], f['renamed'], len(f['held']),
             'HELD' if f['join_held'] else 'DERIVES', f['gen_cited'], f['cells_eq'], f['cells_n'], f['cells_df']), '',
         '*Filed at b706 on the author’s ruling `(R316)` and the author’s words at its prompts; %d question%s put. Banks: relay '
         '`data/b706_arm_sort.txt`, `data/b706_tool_repairs.txt`, `data/b706_corrigendum.txt`, `data/b706_partners_read.txt`, `data/b706_partners.txt`, '
         '`data/b706_readers_after.txt`, `data/b706_join_lakefile.txt`, `data/b706_runner_SIDE-faces-join_join.txt`, `data/b706_join_grade.txt`, '
         '`data/b706_workflow_step.txt`, `data/b706_generator_reach.txt`, `data/b706_prints_v0.1.txt`, `data/b706_prints_v0.2.txt`, '
         '`data/b706_cells_reread.txt`, `data/b706_faces.txt`, `data/b706_standing_figures.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R316)`(1)-(2)): b705 entered at its weight (FINDINGS :%s); the generated entry at FINDINGS :%s answers b705’s six '
         'post-seal items -- the write-list event on data/b706_rules.txt, (n) and (o), the two predicates found wrong after the seal, and the three '
         'trail-equality arms broken by a defect lettered after the trail landed; the corrigenda bank appended at row (26); the sealed face, the '
         'trail and the root-named banks unedited.' % (c1_[0], f['corr_line']), '',
         '**The sort and the repairs** (`(R316)`(2)): the ten arms failing at b705’s close sorted by cause (relay data/b706_arm_sort.txt), four '
         'declared on the face and six found after the seal; three repaired at carry time -- G-WRITELIST-KINDS reading a (W) list that admits the '
         'next act’s rules file by form, G-ANSWERS-CHECKED’s checker telling a bank-named sha256 from a commit, G-ENTRY-TITLE-FORM comparing after '
         'case-folding the article -- and four more at the carry: prev_capture cut at (R316)’s anchor, ROOT_EXCLUDE extended by the tools’ own '
         'declarations with the root route run dry READY before the seal (data/b706_rules.txt row (1)), the runner’s artifact chosen by name, the '
         'standing figures read from this act’s roster; each a diff with its control (relay data/b706_tool_repairs.txt, '
         'data/b706_repair_controls.txt); seven not repaired, the arms correct.', '',
         '**The partner copies** (`(R316)`(3), N2): W-ORD-PAPER-PARTNER-COPIES’s disposition (iii) over the 17 pairs of data/b700_reading4.txt -- '
         'the 8 hand-edited lines read side by side first (relay data/b706_partners_read.txt), every one “the versioned side carries it” and '
         'resolved by that kind on the author’s word; the generator run once into the versioned copies, measured dry before any paper was written '
         '(%s; relay data/b706_partners_dry.txt); the zero diff read against the generator on the author’s word -- the second pass 0, nothing newer '
         'on the retired side -- with %d remaining lines printed on both sides and counted apart, %d newer on the unversioned side, %d renamed, %d '
         'held (relay data/b706_partners.txt); E_DIFFICULTY_THEOREM’s table in its versioned copy alone, no diff taken; per pair the unversioned '
         'copy retired to archive/2026-10-22-b706-partner-copies/ by git mv with its history and the versioned copy renamed by git mv to the '
         'unversioned name, REGISTRY’s row keeping the version as its tag, one commit alone (PLACE-papers 1dfd9bc..cedf7e9); the %s standing reader '
         'hits equal before and after, the roster’s %s tables found %s at the unversioned names (relay data/b706_readers_after.txt); the ruling’s '
         'unscoped “diffed to zero” the navigator’s (c), the first prompt’s unmeasured premise the seat’s (f).' % (
             ', '.join('%d cells at %s' % (v, k) for k, v in f['cells'].items()) or 'no cell changed', f['apart'], f['newer'], f['renamed'], len(f['held']),
             f['hits'][0], f['hits'][1], f['hits'][2]), '',
         '**The join** (`(R316)`(4), N1, N3): SIDE-faces-join’s lakefile re-ordered by the Edit tool -- SIDEExplicitFormula v0.37, '
         'sideLvConservation v0.10.0, then mathlib LAST at de5ce8a9, each at its same revision -- Lake’s own hint from b705’s run (cache.log :21) '
         'on the author’s word, no manifest written on this host, printed before the commit (relay data/b706_join_lakefile.txt), one commit '
         'b37a7b6 on main pushed in main mode and read back; one dispatch (run %s), read by its id with the artifact’s sha256 verified: the cache '
         'served, Mathlib and its packages built, lv-conservation’s fifteen files rebuilt at the shared pin and the build held at '
         'SIDELvConservation/GammaBounds.lean :177:8 (“Tactic `rewrite` failed”), %d error lines banked by line, FacesJoin.lean never reached, the '
         'gate NOT DERIVES, the join %s, no tag, no second dispatch (relay data/b706_join_grade.txt); faces_join’s statement graded DERIVES by hand '
         'and by E0, its profile unprinted; the price b703 read at the pins -- a failing lv module blocks the join and is priced as an lv '
         'forward-port -- for the next ruling; W-ORD-FACES-JOIN-MANIFEST entered and discharged, the ruling’s order “Mathlib before both” the '
         'navigator’s (b) and the ferry’s manifest at 732c1b49 the navigator’s (a).' % (f['join_run'], f['join_errs'], 'HELD' if f['join_held'] else 'DERIVES'), '',
         '**The workflow** (`(R316)`(5)): build-module.yml on SIDE-explicit-formula’s main given the chain-probe step at :%s, after the print step '
         '(:%s) and before the closure (:%s), running a root ChainProbe.lean when the ref carries one and uploading its output as the separate '
         'artifact chain-probe-<run id> (:%s); edited by the Edit tool, printed before the commit, 49 diff lines, no identifier (relay '
         'data/b706_workflow_step.txt); one commit badaccc on main, pushed in main mode and read back; no dispatch on main; the step exercised by '
         'the two entry-tag dispatches; the trigger the next probe at b708; W-ORD-WORKFLOW-PROBE-STEP discharged.' % (
             f['wf_lines'][1], f['wf_lines'][0], f['wf_lines'][2], f['wf_lines'][3]), '',
         '**The generator** (`(R316)`(6), N4): the cell forms printed from data/b704_cells_reach.txt before the edit, 11 table lines and 15 '
         'citation-form mentions (relay data/b706_generator_forms.txt); tools/correspondence_gen.py’s parser extended by the Edit tool to the form '
         '“(`theorem`, SIDE-explicit-formula vX = `sha`)” in any cell, its roster at the unversioned names (the diff in data/b706_generator_diff.txt); '
         'the dry run: %s kernels parsed, SIDE-explicit-formula among them with %s citation-form cells; the control: every roster table re-emitted '
         'unedited and as edited from one set of sources, 20 of 20 equal byte for byte (%s); the reach printed beside G-CORRESPONDENCE-CURRENCY’s '
         'figure (relay data/b706_generator_reach.txt); W-ORD-CORRESPONDENCE-EF-REACH discharged.' % (f['gen_kernels'], f['gen_cited'], f['gen_equal']), '',
         '**The entry-tag prints** (`(R316)`(7), N1, N4): scratch branches prints-b706-v0.1 (748f2a9 at baed4df) and prints-b706-v0.2 (34e098a at '
         '5c72cad), each the tag’s tree with the workflow at main, a one-name print list and a root ChainProbe.lean naming the mentioned theorem, '
         'their files banked before each dispatch; one dispatch each (runs %s, %s), read by their ids with the artifacts’ sha256 verified, both '
         'DERIVES; the probe step’s print read from the separate chain-probe artifact: %s at %s and %s at %s, each at the standard three (relay '
         'data/b706_prints_v0.1.txt, data/b706_prints_v0.2.txt); each branch deleted by name locally and at the remote after its bank was committed, '
         'the tags untouched; the 11 unbanked mentions of data/b704_cells_reach.txt re-read: %d equal, %d differs, %d unbanked (no tag named beside '
         'the kernel) (relay data/b706_cells_reread.txt); W-ORD-ENTRY-TAG-PRINTS discharged.' % (
             p1.get('run'), p2.get('run'), (p1.get('stmt') or '-').replace('theorem ', '').split(' :')[0], p1.get('module'),
             (p2.get('stmt') or '-').replace('theorem ', '').split(' :')[0], p2.get('module'), f['cells_eq'], f['cells_df'], f['cells_n'] - f['cells_eq'] - f['cells_df']), '',
         '**The faces row** (`(R316)`(8)): (4) tagged nothing, so no prompt was raised, no row changes and no page is written -- '
         'THE_CLAUSE_AND_ITS_COMPILED_FACES.md stands as b704 wrote it (PLACE-papers c9b2e55); the hold named here: the join held at '
         'lv-conservation’s module at the shared pin, SIDELvConservation/GammaBounds.lean :177 (relay data/b706_faces.txt).', '',
         '**The standing arms**: the four figures at b706 -- %s, %s, %s, %s -- against b705’s %s, %s, %s, %s, read from this act’s roster after the '
         'renames (relay data/b706_standing_figures.txt), the partners figure 0 with one copy per table; G-WORKFLOW-FILES, G-RUNNER-READ and '
         'G-RUNNER-GATE declared failing on the held join by (R316)(4)’s own clause; no standing arm added.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs5']['correspondence'], f['figs5']['readme'], f['figs5']['partners'], f['figs5']['pins']), '',
         '**The orders** (`(R316)`(3)-(7)): W-ORD-PAPER-PARTNER-COPIES, W-ORD-WORKFLOW-PROBE-STEP, W-ORD-CORRESPONDENCE-EF-REACH and '
         'W-ORD-ENTRY-TAG-PRINTS discharged; W-ORD-FACES-JOIN-MANIFEST entered and discharged; W-ORD-LV-CLOSURE-JOIN annotated with the hold at '
         'lv-conservation’s module (OPEN_TRAILS :%s-:%s).' % (f['orders'][0] if f['orders'] else '-', f['orders'][-1] if f['orders'] else '-'), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed and raised before the component that cites '
         'it; %d answer check%s, each before its answer was acted on, the join-manifest answer checked again after the checker’s repair (d).' % (
             cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the five objects say one thing about the corpus and its kernels -- every roster paper '
         'now has one copy, named as the file of record, whose Correspondence cells the generator writes and whose citation-form mentions of the '
         'central kernel it now parses; the entry tags the papers cite print the statements they cite, equal to the statements at v0.37; and the '
         'clause’s two compiled faces stand one build short of a join, the cache served, Mathlib built, lv-conservation’s own module failing at '
         'the pin the join requires. It strengthens the programme’s offering of a located clause: its citations are read by the generator, its '
         'entry tags by the runner, and the join’s remaining price is one module of one kernel, named by line.', '',
         '**Carried to:** b707 (the sign-onset radius at Q0 with its controls; the top-ranked axis at full grade; the twelve higher pairs priced '
         'beyond b675’s modulus rule, registered before any number); b708 (the re-cut act with the opening probe through the workflow’s step); '
         'b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5); the next ruling (the join held at lv-conservation’s module, the lv forward-port b703 '
         'priced); W-ORD-KEYSTONE-HEADS on its trigger; the draft held at v5.', '',
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
    p1, p2 = f['prints'].get('v0.1') or {}, f['prints'].get('v0.2') or {}
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R316) ratified.** (1) b705 at its weight. (2) The failures sorted, the repairs and the corrigendum. (3) The partner copies. (4) The '
             'join’s manifest. (5) The workflow’s probe step. (6) The generator’s reach. (7) The entry-tag prints. (8) The faces row. (9) The branches. '
             '(10) The readfirst bank. (11) The draft held at v5. (12) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b705’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s-:%s (four discharges, one order '
             'entered and discharged, one annotation); this record.' % (
                 c1_[0], f['corr_line'], fj.get('entry_line'), f['orders'][0] if f['orders'] else '-', f['orders'][-1] if f['orders'] else '-'), '',
             '**Act root:** b706 `%s` (previous `%s`, b705’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b706_author_answers.txt); the root’s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The partner copies:** %d of %d pairs renamed in place, %d held; the 8 hand edits resolved by kind, %d lines counted apart, %d newer on '
             'the retired side; the reader hits %s before and after (relay data/b706_partners.txt; PLACE-papers 1dfd9bc..cedf7e9).' % (
                 f['renamed'], f['pairs'], len(f['held']), f['apart'], f['newer'], f['hits'][0]), '',
             '**The join:** SIDE-faces-join at `%s`, its lakefile re-ordered mathlib last, one dispatch (run %s), the gate %s, the join %s with %d '
             'error lines banked -- SIDELvConservation/GammaBounds.lean :177 at the shared pin, FacesJoin.lean never reached -- no tag, no second '
             'dispatch (relay data/b706_join_grade.txt).' % (K.JOIN_TIP[:7], f['join_run'], f['join_gate'], 'HELD' if f['join_held'] else 'DERIVES', f['join_errs']), '',
             '**The workflow:** the probe step at build-module.yml :%s on SIDE-explicit-formula’s main at `%s`, its output a separate artifact (relay '
             'data/b706_workflow_step.txt).' % (f['wf_lines'][1], K.EF_MAIN[:7]), '',
             '**The generator:** %s kernels parsed, SIDE-explicit-formula among them with %s citation-form cells; every re-emission byte-equal %s '
             '(relay data/b706_generator_reach.txt).' % (f['gen_kernels'], f['gen_cited'], f['gen_equal']), '',
             '**The entry-tag prints:** runs %s and %s, both DERIVES; %s and %s at the standard three; %d of %d mentions equal, %d differs (relay '
             'data/b706_prints_v0.1.txt, data/b706_prints_v0.2.txt, data/b706_cells_reread.txt).' % (
                 p1.get('run'), p2.get('run'), (p1.get('stmt') or '-').replace('theorem ', '').split(' :')[0], (p2.get('stmt') or '-').replace('theorem ', '').split(' :')[0],
                 f['cells_eq'], f['cells_n'], f['cells_df']), '',
             '**The faces row:** the join held, no prompt, no row changed, no page written; the hold named in the entry (relay data/b706_faces.txt).', '',
             '**The kernels:** SIDE-faces-join’s main moved by its manifest commit and dispatched once; SIDE-explicit-formula’s main moved by the one '
             'workflow commit, two scratch branches cut at the entry tags and deleted after their banks, every tag unmoved; lv-conservation’s main '
             'and deposit unmoved; no lean or lake on this host.', '',
             '**The mirror:** the export made after this root in the b670 form, its roster names as renamed, its name in the closing (relay '
             'data/b706_closing.txt).', '',
             '**The open orders:** `W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-STANDING-CLAUSES-BANK`; `W-ORD-LV-CLOSURE-JOIN` '
             '(the join held at lv-conservation’s module, its manifest repaired); `W-ORD-KEYSTONE-HEADS`; `W-ORD-QUASI-RH-FIELD-WATCH`; '
             '`W-ORD-P3-CONTOUR-SIGMA` (read at b705); `W-ORD-E0-MET-CLASSK` (its content done at b705); `W-ORD-README-FIGURE-SCOPE` (repaired at '
             'b705). Discharged this act: `W-ORD-PAPER-PARTNER-COPIES`, `W-ORD-FACES-JOIN-MANIFEST`, `W-ORD-WORKFLOW-PROBE-STEP`, '
             '`W-ORD-CORRESPONDENCE-EF-REACH`, `W-ORD-ENTRY-TAG-PRINTS`.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b705’s %s, %s, %s, %s, read from this act’s roster; G-WORKFLOW-FILES, '
             'G-RUNNER-READ and G-RUNNER-GATE declared on the face as carried failures on the held join (relay data/b706_standing_figures.txt, '
             'data/b706_join_grade.txt).' % (f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                                             f['figs5']['correspondence'], f['figs5']['readme'], f['figs5']['partners'], f['figs5']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b706_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R316).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b706_citation_check.txt), step zero (data/b706_ferry.txt, data/b706_readfirst.txt, data/b706_stepzero.txt, '
         'data/b706_tests_stepzero.txt, data/b706_rowgen_stepzero.txt, data/b706_branches.txt)',
         '### COMPONENT 1 : b705`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s ; the sort and the repairs (data/b706_arm_sort.txt, '
         'data/b706_tool_repairs.txt, data/b706_repair_controls.txt) ; the root route dry (data/b706_root_banks_dry.txt)' % (c1_[0], f['corr_line']),
         '### COMPONENT 2 : the partner copies (data/b706_partners_read.txt, data/b706_partners_dry.txt, data/b706_partners.txt, data/b706_readers_after.txt), '
         '%d of %d renamed, %d held ; N2 %s' % (f['renamed'], f['pairs'], len(f['held']), S['N2'][0]),
         '### COMPONENT 3 : the join (data/b706_join_lakefile.txt, data/b706_runner_SIDE-faces-join_join.txt, data/b706_join_grade.txt), run %s, the gate %s, '
         'the join %s ; the workflow (data/b706_workflow_step.txt) ; the generator (data/b706_generator_reach.txt, %s cells) ; N1 %s ; N3 %s' % (
             f['join_run'], f['join_gate'], 'HELD' if f['join_held'] else 'DERIVES', f['gen_cited'], S['N1'][0], S['N3'][0]),
         '### COMPONENT 4 : the entry-tag prints (data/b706_prints_v0.1.txt, data/b706_prints_v0.2.txt, data/b706_cells_reread.txt), %d of %d mentions equal ; '
         'the faces row (data/b706_faces.txt), the join held ; N4 %s' % (f['cells_eq'], f['cells_n'], S['N4'][0]),
         '### COMPONENT 5 : the carry-time reading (data/b706_tool_repairs.txt), the figures (data/b706_standing_figures.txt), the orders (data/b706_orders.json), '
         'the dry-run steps (data/b706_reg_gate.txt), the seal (data/b706_seal_hashes.json), the suite in seven parts, the per-part seconds '
         '(data/b706_arm_seconds.txt) ; S3 %s' % S['S3'][0],
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
    """b705's mbank (its span line read from the mirror bank chain) carried by copy with b706's names."""
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
    pj = jl('%s_partners.json' % ACT).get('rows') or []
    renamed_in = [r['unversioned'] for r in pj if any(n.endswith(r['unversioned'].split('/')[-1]) for n in files_)]
    versioned_in = [r['versioned'] for r in pj if any(n.endswith(r['versioned'].split('/')[-1]) for n in files_)]
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE ROSTER NAMES AS RENAMED UNDER (R316)(3): of the 17 pairs, the unversioned names carried %d, the retired versioned names carried %d' % (
             len(renamed_in), len(versioned_in)),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT), renamed_in=renamed_in, versioned_in=versioned_in))
    for l in L[:10]:
        print(l[:240])


def guard(*a):
    """data/b706_guard_dry.txt (.json): b705's route with b706's names -- the suite's `--guard-dry` run in its own process (it writes nothing), its
    print banked verbatim; the writes by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b706_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b706_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b706_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b706_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b706_checks.py :%d `%s`,'
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
    import b706_checks as CH
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
              figures=figures, orders=orders,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, rootexclude=rootexclude, armsort=armsort, c1=c1,
              repairs=repairs, repairctl=repairctl, rootdry=rootdry, pairs=pairs, partners_read=partners_read, partners_regen=partners_regen,
              registry_rows=registry_rows, readers=readers, joinlake=joinlake, joinfiles=joinfiles, artfile=artfile, joingrade=joingrade, roster706=roster706, wfstep=wfstep, genreach=genreach, tagstate=tagstate, printprobe=printprobe, runner706=runner706, printsbank=printsbank, cellsreach=cellsreach)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b706_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
