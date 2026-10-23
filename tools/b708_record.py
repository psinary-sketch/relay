# -*- coding: utf-8 -*-
"""b708_record.py -- THE ACT'S RECORD TOOL, b708 under (R318).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b708 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and its probe, tie, quote and cut forms, b705's routes (the print-list dispatch, the artifact reader),
### b706's (the runner choosing the run's artifact by name, the prints branch, the probe-step artifact, the mentions re-read) and b707's (the
### declared untracked writes, the root route's dry run, the rowgen roster re-pointed, the previous window in b701's form) are reached through
### tools/b707_record.py (sealed at b707 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b708 in stages: stage one, step zero's routes (the tie among them); Components 1-6 by the Edit tool.
### Routes: `python tools/b708_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import hashlib
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

import b708_worklist as K          # noqa: E402
import b707_worklist as K707       # noqa: E402  ### b707's data, for the controls on b707's banks
import b707_record as P7           # noqa: E402  ### b707's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4, b705's P5 and b706's P6 to b707: rebound below)
R, P3, P4, P5, P6 = P7.R, P7.P3, P7.P4, P7.P5, P7.P6   # ### b698's routes, b703's to b706's repaired readers, through b707's module

ACT, PREV = 'b708', 'b707'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b707 ran and closed in ANOTHER session (aa198636; this act opens 0be08567 after the author's /clear) -- b701's
# ### form: from b707's post-push combine in that session to that session's end (prev_capture below)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b708_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b708_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b707_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('mirror_prevbuild.json',)   # ### (R318)(2): the mirror builder's own state file, written at every build

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b708_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b708_<name>`.
EXCLUDE_KINDS = P7.EXCLUDE_KINDS
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b708_(\S+)\s*$', re.M)


def declared_untracked():
    """every b708_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b708_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b708_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b708_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P7._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 to b707


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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='6fe154f9' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S TO b707'S REPAIRED READERS, THROUGH b707'S MODULE
_deps = P3._deps                   # ### the primed names read (b703 (f))
R._deps = _deps
DEFECT_ROW = R.DEFECT_ROW
read_defect_row = P3.read_defect_row
_defect_short = P3._defect_short   # ### the act PASSED AT THE CALL (b700's repair)
R._defect_short = _defect_short
_last_export, span_line = P3._last_export, P3.span_line
_read_verdict, CAP = P4._read_verdict, P4.CAP   # ### b704's repaired verdict (offset, limit VALUES, the cap of two hundred)
_print_modules = P5._print_modules              # ### b705's print-list reader (every name mapped to its module by git grep bounded to the tree)
_artifact_named = P6._artifact_named            # ### b706's: the run's artifact chosen by name
roster708 = P7.roster707                        # ### b707's rowgen roster re-pointed through data/b706_partners.json (the fourth path reader)


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster b707's)
answers = R.answers


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (b707's roster707); each tool's verdict lines
    banked with its exit. data/b708_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    Ro = roster708()
    paths = [os.path.join(PP, p) for _n, p, _f in Ro]
    miss = [p for p in paths if not os.path.exists(p)]
    if len(Ro) != 19 or miss:
        sys.exit('### THE ROSTER IS NOT 19 PATHS AT HEAD: %d, missing %s' % (len(Ro), miss))
    moved = [(n, f, p) for n, p, f in Ro if f]
    t0 = time.time()
    con = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'rowgen.py'), 'constellation', PP] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    dif = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'rowgen', 'diff_rowpin.py'), os.path.join(T, 'rowgen', 'namemap.json')] + paths,
                         capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=500)
    secs = int(time.time() - t0)
    co, do = (con.stdout or '') + (con.stderr or ''), (dif.stdout or '') + (dif.stderr or '')
    tail = lambda t: [l for l in t.replace(chr(13), '').split(NL) if l.strip()][-12:]   # noqa: E731
    L = ['%s -- %s: ROWGEN DIFF AND CONSTELLATION MODE (b670 rules row 3) (%s)' % (ACT, stage.upper(), utc()), '',
         '### the roster: the 19 tables of relay data/b586_corroboration.txt :34 at PLACE-papers HEAD %s, each at its file of record after b706`s renames '
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json, b707`s reader) ; the instruments: tools/rowgen/rowgen.py '
         '`constellation`, tools/rowgen/diff_rowpin.py (build-free; `rowgen.py diff` runs lean and is not run on this host) ; %d s' % (
             g(PP, 'rev-parse', '--short', 'HEAD').strip(), len(moved), secs), '']
    L += ['### re-pointed: %s -> %s' % (f, p) for _n, f, p in moved]
    L += ['', '### constellation, exit %d ; its last lines:' % con.returncode] + ['    ' + l for l in tail(co)] + [
         '', '### diff_rowpin, exit %d ; its last lines:' % dif.returncode] + ['    ' + l for l in tail(do)] + [
         '', '### ### **CONSTELLATION EXIT %d ; ROWGEN DIFF EXIT %d ; TABLES 19 ; RE-POINTED %d.**' % (con.returncode, dif.returncode, len(moved))]
    put_txt('%s_rowgen_%s.txt' % (ACT, stage), L)
    print(NL.join(L[-14:]))


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R318)(8); b707's form)
def branches(*a):
    """`branches before`: data/b708_branches_before.json -- b698's route, carried (every branch (R318)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b708_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the kept branch port-b707 read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b708_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    krepo, kb = K.KEPT_BRANCH
    kept_local = g(krepo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + kb).strip()
    kept_remote = R._remote_heads(krepo).get(kb, '')
    L = ['%s -- STEP ZERO, (R318)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b708_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R318)(8) names relay`s four and PLACE-papers` two; port-b707 of',
         '### SIDE-lv-conservation is NOT deleted, local or remote, read beside them.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['  %-22s | %-28s | kept   | local %s ; remote %s ; %s' % (os.path.basename(krepo), kb, kept_local[:12] or 'absent', kept_remote[:12] or 'absent',
                                                                'STANDS' if kept_local == kept_remote == K.PORT_COMMIT else '### NOT AS KEPT')]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s ; port-b707 STANDS %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows),
        kept_local == kept_remote == K.PORT_COMMIT)]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[], kept=dict(repo=krepo, branch=kb, local=kept_local, remote=kept_remote)))
    print(NL.join(L[7:]))


# ================================================================================ THE READ BANK (b704's repaired route; the word's time the anchor's, from b705)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b708_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6, 'b707': P7}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
    for n, f in sorted(vars(mod).items(), key=lambda kv: inspect.getsourcelines(kv[1])[1] if inspect.isfunction(kv[1]) and kv[1].__module__ == mod.__name__ else 0):
        if inspect.isfunction(f) and f.__module__ == mod.__name__:
            print('  %-28s :%d' % (n, inspect.getsourcelines(f)[1]))


def verdicts(*a):
    """prints each named bank's verdict line (its last `### ### **...**` line), for the suite's predicates to quote; writes nothing."""
    for n_ in a:
        m = re.findall(r'(?ms)^\s*### ### \*\*(.*?)\*\*\s*$', rdn(n_))
        print('  %s | %s' % (n_, ' '.join(m[-1].split()) if m else '### NO VERDICT LINE'))


# ================================================================================ THE DISPATCH, THE RUNNER (b698's routes; b705's print-list check; b706's artifact by name)
runstatus, runner = R.runstatus, R.runner
STD3 = P3.STD3
EF = K.EF_DIR
WF = K.WORKFLOW


def dispatch(*a):
    """`dispatch <kernel> <ref sha> <label> <target> [dry]`: b698's dispatch (one dispatch per tree state, the run id read), with b705's check
    (data/b705_rules.txt row (1)): every name of print_targets.txt at the ref mapped to its module by git grep bounded to the kernel's tree; a
    target not covering every module is REFUSED, nothing dispatched; the row banked carries `whole` True with the modules the list needs."""
    kernel, ref, label, target = a[0], a[1], a[2], a[3]
    mods = _print_modules708('D:/' + kernel, ref)
    need = sorted(set(m for m in mods.values() if m))
    unmapped = [n for n, m in mods.items() if not m]
    tgt = target.split()
    whole = bool(need) and not unmapped and all(m in tgt for m in need)
    print('  the print list %d names ; their modules %d %s ; unmapped %s ; the target %d modules ; whole %s' % (len(mods), len(need), need[:6], unmapped or 'NONE', len(tgt), whole))
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
    print('  the row banked with whole True ; print modules %d' % len(need))


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


# ================================================================================ THE LATE ROUTES (b707's, carried with b708's names; the previous window in its own session)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor."""
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
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (b707's carry-time repair, carried): b707's
    capture AFTER ITS POST-PUSH SUITE -- every command of session aa198636 from the call that combined b707's post-push parts into
    data/b707_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, K.PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    out = [dict(r, src='%s %s' % (PREV, r['src'])) for r in rows if first[0] <= r['ts']]
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
    """b707's route with b708's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b707's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (two ordered: the probe branch and the prints
    branch), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests.
    data/b708_commands.txt (.json)."""
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
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, its own session %s, from its post-push combine to that session`s end): '
              '%d commands from %s, its offences printed whole (%d):' % (PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (two ordered this act, N1 as the fact clause reads it: the probe branch and the prints branch of SIDE-explicit-formula) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R318)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    ks = list(dict.fromkeys(_kerns() + ['SIDE-faces-join']))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (SIDE-faces-join among them; no kernel main written this act; the two scratch branches of SIDE-explicit-formula deleted after their banks)' % len(ks))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B707_FACE.split('/')))) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


def rootdry(*a):
    """data/b706_rules.txt row (1): the root route run DRY on the pre-root tree before the seal -- the banks the route names (ROOT_EXCLUDE
    extended), each read for CR LF, its status and its blob at HEAD; READY where every named bank is clean and equal at HEAD and none is CR LF
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b708_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b708_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ STEP ZERO: THE LICENSED TABLE'S NEXT DOCUMENT, (R318)(6) (b704's tie form)
SUMMARY = re.compile(r'### ### \*\*(\w+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b708_tie.txt: (R318)(6), the licensed table's next document -- b652's order, b674's tie-break rule and data/b705_rules.txt row (2)
    printed verbatim before the document is named; the agenda's rows as b704's tie bank read them (data/b704_tie.txt, b702's cut entered there),
    b704's cut entered from its own bank (data/b704_cut.json); the documents at the top count, each table's summary line verbatim, each
    document's sha256 at PLACE-papers HEAD against its table's read; b674's rule step by step in its written order, b705's row (2) where its
    condition is not met."""
    f52 = rdn('b652_ferry.txt').split(NL)
    r74 = rdn('b674_rules.txt').split(NL)
    r05 = rdn('b705_rules.txt').split(NL)
    t04 = rdn('b704_tie.txt').split(NL)
    cut = jl('b704_cut.json')
    rows = []
    for i, l in enumerate(t04, 1):
        m = re.match(r'^\s+(\d+) \| (\w[\w ]*?)\s+\| (.*?)(?:\s+### b702`s cut: .*)?$', l)
        if m and ' (b702_tie :' in l:
            rows.append(dict(line=i, count=int(m.group(1)), kind=m.group(2).strip(), row=m.group(3)))
    for r in rows:
        if r['row'].startswith('day1/ONE_PAGE_PROOF.md') and cut.get('after') is not None:
            r['count_b704'], r['count'] = r['count'], cut['after']
    kern = [r for r in rows if r['kind'] == 'kernel']
    comp = sorted([r for r in rows if r['kind'] == 'companion'], key=lambda r: -r['count'])
    top = comp[0]['count'] if comp else None
    at_top = [r for r in comp if r['count'] == top]
    L = ['%s -- STEP ZERO, (R318)(6): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER, b674`S TIE-BREAK RULE AND b705`S ROW (2) PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :19:', '    ' + f52[18].strip(), '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:'] + [r74[k] for k in range(7, 11)] + ['',
         '### data/b705_rules.txt ROW (2), VERBATIM FROM :11-:14:'] + [r05[k] for k in range(10, 14)] + ['',
         '### THE AGENDA`S ROWS, VERBATIM FROM b704`S TIE BANK (relay data/b704_tie.txt :14-:46, b702`s cut entered there), b704`S CUT ENTERED FROM relay data/b704_cut.json',
         '### (%s %s -> %s); rows are documents: the count now | the kind | the row (its line in b704`s bank):' % (cut.get('document'), cut.get('before'), cut.get('after'))]
    L += ['  %4d | %-9s | %s (b704_tie :%d)%s' % (r['count'], r['kind'], r['row'], r['line'], ('   ### b704`s cut: %d -> %d' % (r['count_b704'], r['count'])) if 'count_b704' in r else '')
          for r in rows]
    L += ['', '### THE KERNELS BY DESCENDING COUNT: the top count %s ; kernels at 0 %d of %d -- the order passes to the companions ("then the companions")' % (
        max([r['count'] for r in kern] or [0]), sum(1 for r in kern if r['count'] == 0), len(kern)),
          '### THE COMPANIONS BY DESCENDING COUNT: %s' % '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in comp),
          '### THE TOP COUNT %s ; the documents standing at it %d' % (top, len(at_top)), '### the tables of the documents at the top count, their summary lines verbatim, and the document at HEAD against the table`s read:']
    tabs = []
    for r in at_top:
        tb = re.search(r'\[data/(b646_table_\w+\.txt)\]', r['row'])
        tl = rdn(tb.group(1)).split(NL) if tb else []
        sm = next((SUMMARY.match(x) for x in tl if SUMMARY.match(x)), None)
        dm = re.search(r'PLACE-papers (\S+) at (\w+), (\d+) lines, sha256 ([0-9a-f]{64})', NL.join(tl[:4]))
        doc = dm.group(1) if dm else '?'
        head_sha = hashlib.sha256((_show(PP, 'HEAD', doc) or '').encode('utf-8')).hexdigest() if dm else ''
        x = dict(row=r, bank=tb.group(1) if tb else None, summary=sm.group(0) if sm else '### NO SUMMARY LINE', doc=doc,
                 claims=int(sm.group(2)) if sm else 0, und=int(sm.group(5)) if sm else 0, over=int(sm.group(6)) if sm else 0,
                 unl=int(sm.group(7)) if sm else 0, read_sha=dm.group(4) if dm else '', head_sha=head_sha, read_at=dm.group(2) if dm else '')
        x['outside'] = x['over'] + x['unl'] + x['und']
        tabs.append(x)
        L += ['    relay data/%s : %s' % (x['bank'], x['summary']),
              '      the document %s: sha256 at the table`s read (%s) %s ; at PLACE-papers HEAD %s ; %s' % (
                  doc, x['read_at'], x['read_sha'][:16], head_sha[:16], 'UNMOVED' if x['read_sha'] == head_sha else '### MOVED SINCE ITS READ')]
    L += ['### b674`s rule, step by step in its written order:']
    pick = None
    if len(tabs) == 1:
        pick = tabs[0]
        L.append('    NOT REACHED: one document at the top count (b705`s row (2) not reached either: no tie to close)')
    elif tabs:
        ov = sorted(set(t['over'] for t in tabs))
        L.append('    (i) the rule`s condition, equal OVERREACHES counts: %s -- %s' % (', '.join('%s %d' % (t['doc'], t['over']) for t in tabs), 'MET' if len(ov) == 1 else 'NOT MET'))
        cand = tabs
        if len(ov) > 1:
            mo = max(t['over'] for t in tabs)
            cand = [t for t in tabs if t['over'] == mo]
            L.append('    data/b705_rules.txt row (2): b674`s measures in their written order, OVERREACHES first, the first that separates deciding: %s' % ', '.join(
                '%s %d' % (t['doc'], t['over']) for t in tabs))
        if len(cand) > 1:
            L.append('    (ii) a declared suite failure on either document: NONE (no arm of b707`s suite names either; data/b707_checks.txt)')
            mo = max(t['outside'] for t in cand)
            L.append('    (iii) the rows outside LICENSED/CITED of any kind (OVERREACHES + UNLICENSED + UNDERSTATES): %s' % ', '.join(
                '%s %d (%d + %d + %d)' % (t['doc'], t['outside'], t['over'], t['unl'], t['und']) for t in cand))
            c2 = [t for t in cand if t['outside'] == mo]
            if len(c2) > 1:
                mc = max(t['claims'] for t in c2)
                L.append('    (iv) the larger table (CLAIMS): %s' % ', '.join('%s %d' % (t['doc'], t['claims']) for t in c2))
                c2 = [t for t in c2 if t['claims'] == mc]
            cand = c2
        pick = cand[0] if len(cand) == 1 else None
        if pick is None and cand:
            L.append('    ### THE RULE ENDS IN A TIE -- RAISED, NOTHING NAMED')
    nxt = [r for r in comp if r['count'] < (top or 0)][:2]
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER, b674`S TIE-BREAK AND b705`S ROW (2): %s (A COMPANION ; THE TOP COUNT %s, %d DOCUMENT%s AT IT ; %s ; THE NEXT BY COUNT %s).**' % (
        pick['doc'] if pick else '### NONE NAMED', top, len(at_top), '' if len(at_top) == 1 else 'S', 'NO TIE' if len(tabs) == 1 else ('THE RULES READ IN THEIR WRITTEN ORDER' if pick else '### THE RULES DO NOT REACH THE TIE'),
        '; '.join('%s %d' % (r['row'].split('   ')[0].strip(), r['count']) for r in nxt))]
    if 'dry' not in a:
        put_txt('%s_tie.txt' % ACT, L)
        put_json('%s_tie.json' % ACT, dict(at=utc(), top=top, at_top=[t['doc'] for t in tabs], pick=pick['doc'] if pick else None,
                                          tables=[dict((k, v) for k, v in t.items() if k != 'row') for t in tabs]))
    print(NL.join(L))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R318)(1)-(2)
WH = ('*Appended 2026-10-23 by b708 to b707’s entry (:10106), under `(R318)`(1) -- b707 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b707_closing.txt):*')
ONSET_ROW = re.compile(r'^  (band|rho0) \| (\S+)\s+\| a (\S+) \+- (\S+) \| .*?\| lambda (\S+) \+- (\S+), (\S+) \+- (\S+) \| ([A-Z ]+?BEYOND ITS BOUND)', re.M)


def _onset_rows(text):
    out = {}
    for m in ONSET_ROW.finditer(text):
        out[(m.group(1), m.group(2))] = dict(a=m.group(3), lmin=m.group(5), reading=m.group(9).strip())
    return out


def _declared_b707():
    face = rd(os.path.join(ROOT, *K.B707_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    return sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []


def _failing_b707():
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', rdn('b707_checks_postpush.txt'))
    return [x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip()]


def _wb():
    """b707's weight line, its figures read from b707's banks where a bank names them (the declared arms from the face, the failing eight
    from the post-push bank, the eigenvalues from the onset banks, the scores from the scores banks) and otherwise quoted from the closing
    record (relay data/b707_closing.txt) by line; the onset figures' reading of (R318)(2) beside it in the navigator's words."""
    decl, fails = _declared_b707(), _failing_b707()
    post = [a for a in fails if a not in decl]
    q0, z = _onset_rows(rdn('b707_onset.txt')), _onset_rows(rdn('b707_onset_controls.txt'))
    sr, sc = jl('b707_scores.json'), jl('b707_scores_close.json')
    if len(decl) != 4 or len(fails) != 8 or len(post) != 4 or not q0.get(('band', '192')) or not z.get(('rho0', '32')):
        sys.exit('### b707`S FACE OR ITS BANKS NOT AS READ (declared %s ; failing %s) -- NOTHING COMPOSED' % (decl, fails))
    return (' “b707 closed: relay 2507e99c, PLACE-papers 95dc6f6; suite 129 of 137; root 6fe154f9820e7d9e…; 3 prompts answered; 9 defects” '
            '(data/b707_closing.txt :1); the closing commit b5898a61 pushed alone after the line was written and read back equal at the remote '
            '(data/b707_closing_push_out.txt :5). The sign-onset radius at Q0 on the family span{C, N} at two frequencies over the ladder log 2, '
            '2 log 32 ... 2 log 192 (data/b707_onset.txt): the band zero’s family positive definite to 2 log 128 (λ_min %s there) and negative at '
            'a* = 2 log 192 (λ_min %s); ρ₀’s family positive definite at log 2 (λ_min %s) and negative from a* = 2 log 32 (λ_min %s); the ζ '
            'control positive definite at every rung of both frequencies, λ_min %s at the band’s 2 log 192 and %s at ρ₀’s 2 log 32 '
            '(data/b707_onset_controls.txt); the falsifier NOT FIRED, the hypothesis HELD (the ruling’s “the falsifier HELD” the navigator’s (c) '
            'of this act). The forward-port opened on port-b707 of SIDE-lv-conservation at the shared pin: five files on the branch, one '
            'dispatch (run 39888369981), 6 of 12 modules built, the build held at C7OrderBounds.lean :277:55 with :380:8 beside it, nothing '
            'merged, the deposit untouched (data/b707_port_files.txt, data/b707_port.txt). The three readers of the renames written and controlled '
            '-- tools/mirror_roster.json re-pointed to 70 entries (four re-pointed, thirteen duplicates struck), tools/terminal_table.py’s ledger '
            'walk excluding the retired copies’ directory under archive/, tools/rule_arms.py’s family reading of a lettered half -- 22 control '
            'cases as wanted (data/b707_tool_repairs.txt, data/b707_repair_controls.txt); the mirror mirror-refresh-2026-10-22-b707.zip CLEAN on '
            'all three clauses over 70 files with the root line (data/b707_mirror.txt). The higher pairs’ route registered in '
            'data/b707_registrations.txt (committed alone at 6e8ece87), the next axis (e) representation coordinates. The entry at FINDINGS '
            ':10106, the trail at OPEN_TRAILS :15688; the root 6fe154f9 over 83 banks chained from aa8a696b (data/b707_act_root.json, '
            'data/b707_root_banks.txt), the chain b624–b707 AGREE; suite 133 of 137 pre-push and 129 of 137 post-push, four failures declared '
            'on the face (%s) and four found after the seal (%s; data/b707_checks.txt, data/b707_checks_postpush.txt); N1–N5 and S3 HELD at the '
            'lock, N5 REFUTED at the close on tools/mirror_prevbuild.json alone, S1 and S2 HELD at the close (data/b707_scores.json, '
            'data/b707_scores_close.json: N5 %s, S1 %s, S2 %s); the sealed tools’ hashes equal at the close, 11 of 11; the citation check 161 cites, '
            '156 OK, 5 missed, every one the navigator’s; nine defects (a)–(i), (c), (d), (e), (f) and (g) the navigator’s (data/b707_defects.txt; the '
            'ruling’s “four” the navigator’s (d) of this act), (i) the seat’s; “3 prompts answered” the answers bank’s 2 rows and the root’s prompt; '
            'the report’s five lines by the sealed tool and the four lines the author’s word at the root named by the unsealed tool '
            '(data/b707_report.txt, data/b707_report_root.txt). The post-seal item (i) entered by this act’s corrigendum. Nothing deposited. '
            'THE ONSET FIGURES’ READING, in the navigator’s words for the author’s strike (`(R318)`(2)): the onsets found at the coarse grid’s '
            'own points (a = 2 log N at the widths 32 and 192 b694 and b705 used), confirming b705’s signs; the rung question (whether the '
            'onset sits within one step past log 2, log 3, log 5 or log 7) not yet resolved, since no grid point lies between the coarse '
            'points where the sign turns; the ζ control’s margin small (order 1e-7) and to be printed beside its certified tail bound before '
            'it is read as a figure -- the fine grid registered for b709 in data/b708_registrations.txt.' % (
                q0[('band', '128')]['lmin'], q0[('band', '192')]['lmin'], q0[('rho0', 'log2')]['lmin'], q0[('rho0', '32')]['lmin'],
                z[('band', '192')]['lmin'], z[('rho0', '32')]['lmin'], ', '.join(decl), ', '.join(post),
                (sc.get('N5') or ['-'])[0], (sc.get('S1') or ['-'])[0], (sc.get('S2') or ['-'])[0]))


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B707_ENTRY,
         check=[('FINDINGS.md', K.B707_ENTRY, '## The sign-onset radius at the Epstein zeta'), ('OPEN_TRAILS.md', K.B707_TRAIL, '### b707')],
         dry=dry)


# ================================================================================ COMPONENT 2: THE PROBE THROUGH THE WORKFLOW'S STEP, (R318)(4)
def _lib_srcdirs(kernel_dir, rev='HEAD'):
    """the lakefile's lean_lib blocks with a srcDir, at rev: [(srcDir, name)] -- a module under a lib's srcDir is named relative to it (the
    vendored lib BulkaVendored at srcDir Vendored/Bulka: Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean is the module
    Lc.LiCriterion.ReverseDirection)."""
    txt = _show(kernel_dir, rev, 'lakefile.toml') or ''
    out = []
    name = None
    for l in txt.split(NL):
        m = re.match(r'^\s*name\s*=\s*"([^"]+)"', l)
        if m:
            name = m.group(1)
        m = re.match(r'^\s*srcDir\s*=\s*"([^"]+)"', l)
        if m:
            out.append((m.group(1).strip('/'), name))
    return out


def _print_modules708(kernel_dir, rev='HEAD'):
    """b705's _print_modules (tools/b705_record.py :732) with the carry-time repair of this act (data/b708_tool_repairs.txt row (1)): a hit under a
    lean_lib's srcDir is named relative to that srcDir, as Lake names it; every other hit as b705 named it (the path with / for . and no .lean)."""
    names = [l.strip() for l in (_show(kernel_dir, rev, 'print_targets.txt') or '').split(NL) if l.strip()]
    dirs = _lib_srcdirs(kernel_dir, rev)
    out = {}
    for n in names:
        short = n.split('.')[-1]
        hit = g(kernel_dir, 'grep', '-n', '-E', '-e', r'^(@\[[^]]*\] *)?((private|protected|noncomputable|nonrec) +)*(theorem|lemma|def|abbrev|structure|instance) +%s([ :({\[]|$)' % re.escape(short),
                rev, '--', '*.lean').strip()
        f = hit.split(':', 2)[1] if hit.count(':') >= 2 else ''
        if not f.endswith('.lean'):
            out[n] = None
            continue
        rel = f[:-5]
        for sd, _nm in dirs:
            if rel.startswith(sd + '/'):
                rel = rel[len(sd) + 1:]
                break
        out[n] = rel.replace('/', '.')
    return out


def _probe_parts():
    """chain_page's own selection at the b704 list's pin (b704's form): (CP, names, corr_names, watch)."""
    import chain_page as CP
    CP.VARIANT = None
    CP.PIN_TAG, CP.PIN = CP.node_pin(os.path.join(ROOT, *K.NODES_B704.split('/')))
    nodes, _drops, _corr, marks = CP.read_nodes(os.path.join(ROOT, *K.NODES_B704.split('/')))
    names = [x['name'] for x in nodes]
    corr = CP.corr_select(CP.record_rows(), names, marks, None)
    return CP, names, corr, list(K.PROBE_WATCH)


def probe(*a):
    """`probe [dry]`: the probe text by tools/chain_page.py's probe_text at the b704 list's pin (v0.37), its cells the list's names, the two
    candidate nodes of (R314)(3) and the Correspondence names (b704's selection, data/b704_probe.json) -- written as the root ChainProbe.lean of
    the probe branch's working tree ((R318)(4): the workflow's probe step at main's build-module.yml :101 imports each module of the target
    above it and runs it), which must be checked out at probe-b708 cut from main (badaccc) with no tracked change. The lake target the union
    of the print list's modules (data/b705_rules.txt row (1): print_targets.txt whole, each name mapped to its module by git grep bounded to the
    tree) and the probe's own module imports. data/b708_probe.txt (.json): the text's sha256 against b704's, its cells, the target."""
    CP, names, corr, watch = _probe_parts()
    br = g(EF, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    base = g(EF, 'rev-parse', 'HEAD').strip()
    dirty = g(EF, 'status', '--porcelain', '--untracked-files=no').strip()
    cells = names + [c for c in K.CANDIDATES if c not in names] + corr
    text = CP.probe_text(cells, names + [c for c in K.CANDIDATES if c not in names], watch)
    pmods = [l.split()[1] for l in CP.probe_imports().split(NL) if l.startswith('import ')]
    plist = _print_modules708(EF, 'main')
    need = sorted(set(m for m in plist.values() if m))
    unmapped = [n for n, m in plist.items() if not m]
    target_mods = sorted(set(pmods) | set(need))
    target = ' '.join(target_mods)
    sha = hashlib.sha256(text.encode('utf-8')).hexdigest()
    b704 = jl('b704_probe.json')
    same = sha == b704.get('sha256')
    ok = br == K.PROBE_BRANCH and base == K.EF_MAIN and not dirty and CP.PIN == K.EF_V037 and not unmapped
    L = ['%s -- (R318)(4): THE PROBE THROUGH THE WORKFLOW`S STEP -- ITS TEXT BY THE GENERATOR, ITS TARGET (%s)' % (ACT, utc()), '',
         '### the generator: relay tools/chain_page.py probe_text at the list relay %s (pin %s = %s); the kernel checkout %s at %s (main, one commit past' % (
             K.NODES_B704, CP.PIN_TAG, (CP.PIN or '')[:7], br, base[:7]),
         '### v0.37 = %s by the workflow file alone, the navigator`s (e)), tracked changes %s. The text is written as the probe branch`s root ChainProbe.lean;' % (K.EF_V037[:7], dirty or 'NONE'),
         '### the workflow`s probe step (build-module.yml :101-:115 at main) prepends one import per target module and runs it, its output the separate',
         '### artifact chain-probe-<run id> (:140-:146). The target: data/b705_rules.txt row (1), print_targets.txt whole (%d names, their modules %d, unmapped %s),' % (len(plist), len(need), unmapped or 'NONE'),
         '### joined with the probe`s own module imports (%d; b704`s target); the union %d modules.' % (len(pmods), len(target_mods)),
         '  cells %d (the list`s names %d ; the candidates %d ; the Correspondence names %d) ; the node set %d ; the watch %s' % (
             len(cells), len(names), len([c for c in K.CANDIDATES if c not in names]), len(corr), len(names) + len([c for c in K.CANDIDATES if c not in names]), watch),
         '  the text: %d bytes ; %d lines ; sha256 %s ; b704`s text sha256 %s ; EQUAL %s' % (len(text.encode('utf-8')), text.count(NL), sha, (b704.get('sha256') or '-')[:16], same),
         '  the lake target (%d modules): %s' % (len(target_mods), target),
         '', '### ### **THE PROBE TEXT %s ; sha256 %s ; EQUAL TO b704`S %s ; CELLS %d ; TARGET MODULES %d (THE PRINT LIST`S %d, THE PROBE`S %d) ; THE CHECKOUT AT %s %s.**' % (
             'WRITTEN' if ok and 'dry' not in a else ('NOT WRITTEN (dry)' if ok else '### NOT WRITTEN, THE CHECKOUT NOT AS ORDERED'), sha[:16], same, len(cells),
             len(target_mods), len(need), len(pmods), K.PROBE_BRANCH, 'FROM main AT badaccc' if ok else '### NOT AS ORDERED')]
    if ok and 'dry' not in a:
        import io as _io
        _io.open(os.path.join(EF, K.PROBE_FILE), 'w', encoding='utf-8', newline=NL).write(text)
        put_txt('%s_probe.txt' % ACT, L)
        put_json('%s_probe.json' % ACT, dict(at=utc(), sha256=sha, equal_b704=same, cells=cells, nodes=names, candidates=list(K.CANDIDATES), corr=corr, target=target,
                                            print_modules=need, probe_modules=pmods, pin=CP.PIN, branch=br, base=base))
    print(NL.join(L[-4:]))


def probediff(*a):
    """data/b708_probe_diff.txt: the probe branch's commit against main and against v0.37, by path (git diff --name-status, --stat) -- one
    path against main, the root file ChainProbe.lean added; against v0.37 that file and the workflow."""
    tip = g(EF, 'rev-parse', K.PROBE_BRANCH).strip()
    nsm = [l for l in g(EF, 'diff', '--name-status', 'main', tip).split(NL) if l.strip()]
    stm = [l for l in g(EF, 'diff', '--stat', 'main', tip).split(NL) if l.strip()]
    ns37 = [l for l in g(EF, 'diff', '--name-status', 'v0.37', tip).split(NL) if l.strip()]
    L = ['%s -- (R318)(4): THE PROBE BRANCH`S DIFF AGAINST main AND AGAINST v0.37 (%s)' % (ACT, utc()), '',
         '### %s = %s against main = %s (badaccc) and against v0.37 = %s; rows are paths changed (git diff --name-status), then the stat.' % (
             K.PROBE_BRANCH, tip[:7], K.EF_MAIN[:7], K.EF_V037[:7]), '', '### against main:']
    L += ['  ' + l for l in nsm] + [''] + ['  ' + l for l in stm] + ['', '### against v0.37:'] + ['  ' + l for l in ns37]
    ok = nsm == ['A\t' + K.PROBE_FILE] and sorted(ns37) == sorted(['A\t' + K.PROBE_FILE, 'M\t' + K.WORKFLOW])
    L += ['', '### ### **PATHS CHANGED AGAINST main %d ; THE ONE PATH THE ROOT FILE ChainProbe.lean %s ; AGAINST v0.37 %d (THE PROBE FILE AND THE WORKFLOW) ; THE MODULES` TREE v0.37`S %s.**' % (
        len(nsm), nsm == ['A\t' + K.PROBE_FILE], len(ns37), ok)]
    if 'dry' not in a:
        put_txt('%s_probe_diff.txt' % ACT, L)
    print(NL.join(L[-1:]))


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b706's runner706 carried with b708's names -- the run's artifact chosen BY NAME
    (build-module-<run id>; a run of the workflow uploads a second artifact, chain-probe-<run id>), its sha256 against the platform's digest
    before any reading, the build's exit and error lines, the memory log, the print step read, the gate."""
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
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
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


R.runner = runner


def _probe_artifact(run_id):
    """the run's SEPARATE chain-probe artifact (chain-probe-<run id>) read by name, its sha256 against the platform's digest before any
    reading: (artifact row, sha256, {file: text})."""
    import io as _io
    import zipfile
    repo = 'psinary-sketch/' + K.KERNEL
    art, arts = _artifact_named(repo, run_id, 'chain-probe-')
    if not art:
        return None, None, {}, [x.get('name') for x in arts]
    rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
    sha = hashlib.sha256(rz.stdout).hexdigest()
    digest = (art.get('digest') or '').replace('sha256:', '')
    if not digest or digest != sha:
        sys.exit('### THE PROBE ARTIFACT`S SHA256 %s IS NOT THE PLATFORM`S DIGEST %s -- NOTHING READ' % (sha[:16], (digest or '-')[:16]))
    T_ = {}
    with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
        for n in z.namelist():
            T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    return art, sha, T_, [x.get('name') for x in arts]


def probeview(*a):
    """`probeview <run id>`: the probe run read by its id -- the SEPARATE chain-probe artifact by name, its sha256 against the platform's
    digest before any reading; probe/chainprobe.txt banked whole as data/b708_probe_out_zeta.txt and parsed by chain_page's parser, every cell
    of the probe named or missing; the step's log read (RUN or NOT RUN with its reason); where the step did not run, its error banked for
    W-ORD-WORKFLOW-PROBE-STEP's re-opening. data/b708_probe_run.txt (.json)."""
    import chain_page as CP
    run_id = int(a[0])
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event')
    run = json.loads(out or b'{}')
    art, sha, T_, names_ = _probe_artifact(run_id)
    pj = jl('%s_probe.json' % ACT)
    text = T_.get('chainprobe.txt', '')
    log = ' '.join(T_.get('chainprobe_log.txt', '').split())
    cells, perr = CP.parse(text)
    want = pj.get('cells') or []
    missing = [n for n in want if n not in cells or cells[n].get('missing')]
    ran = log.startswith('RUN:')
    L = ['%s -- (R318)(4): THE PROBE THROUGH THE WORKFLOW`S STEP ON THE HOSTED RUNNER, READ BY ITS RUN ID (%s)' % (ACT, utc()), '',
         '### the probe: relay data/b708_probe.txt (the generator`s text sha256 %s, %d cells) as the root ChainProbe.lean of %s at %s, the modules` tree v0.37`s' % (
             (pj.get('sha256') or '')[:16], len(want), K.PROBE_BRANCH, g(EF, 'rev-parse', K.PROBE_BRANCH).strip()[:7]),
         '### (relay data/b708_probe_diff.txt); the step build-module.yml :101 at main, its output the separate artifact chain-probe-<run id> (:140).',
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'), run.get('updatedAt')),
         '### the artifacts listed %d: %s ; the probe`s chosen by name (chain-probe-)' % (len(names_), names_),
         '### the probe artifact: id %s ; %s ; %s bytes ; sha256 %s ; AGREE WITH THE PLATFORM`S DIGEST (read after the agreement)' % (
             (art or {}).get('id'), (art or {}).get('name'), (art or {}).get('size_in_bytes'), sha) if art else '### the probe artifact: NONE LISTED',
         '### the step`s log (probe/chainprobe_log.txt): %s' % (log or '### ABSENT'),
         '### the step`s output (probe/chainprobe.txt): %d bytes ; error lines %d ; cells parsed %d ; cells wanted %d ; missing %d' % (
             len(text), len(perr), len(cells), len(want), len(missing))] + ['    ' + l for l in perr[:20]] + ['### the missing cells: %s' % (missing or 'NONE')]
    ok = run.get('conclusion') == 'success' and bool(art) and ran and not perr and not missing
    L += ['', '### ### **RUN %s (probe) ; CONCLUSION %s ; THE PROBE ARTIFACT %s ; THE STEP %s ; ERROR LINES %d ; PROBE CELLS %d OF %d ; MISSING %d ; THE PROBE %s.**' % (
        run_id, run.get('conclusion'), 'AGREE' if art else '### NONE', 'RAN' if ran else '### NOT RUN', len(perr), len(want) - len(missing), len(want), len(missing),
        'READ' if ok else '### NOT READ WHOLE -- THE ORDER RE-OPENS')]
    put_txt('%s_probe_run.txt' % ACT, L)
    put_json('%s_probe_run.json' % ACT, dict(at=utc(), run_id=run_id, conclusion=run.get('conclusion'), artifact=dict(id=(art or {}).get('id'), name=(art or {}).get('name'), sha256=sha),
                                            step_ran=ran, log=log, errors=perr, missing=missing, cells=len(cells), wanted=len(want), ok=bool(ok)))
    if art:
        put_txt('%s_probe_out_zeta.txt' % ACT, text.rstrip(NL).split(NL))
    print(NL.join(L[:9] + L[-2:]))


def probecompare(*a):
    """data/b708_probe_compare.txt (.json): (R318)(4), the probe diffed against b704's probe bank -- every cell of data/b708_probe_out_zeta.txt
    against the same cell of data/b704_probe_out_zeta.txt (run 39721668586 at v0.37, through the closure step), by chain_page's parser: the
    statement (the sig), the kind, the module and line, the axioms, the consumed nodes; every differing sig printed with its cause read from the
    two cells. The page is regenerated where a sig moved and not otherwise."""
    import chain_page as CP
    now, _e1 = CP.parse(rdn('%s_probe_out_zeta.txt' % ACT))
    old, _e2 = CP.parse(rdn('b704_probe_out_zeta.txt'))
    want = jl('%s_probe.json' % ACT).get('cells') or []
    rows, moved = [], []
    for n in want:
        a_, b_ = old.get(n) or {}, now.get(n) or {}
        if a_.get('missing') or b_.get('missing') or not a_ or not b_:
            rows.append((n, 'MISSING', 'b704 %s ; b708 %s' % ('missing' if a_.get('missing') or not a_ else 'present', 'missing' if b_.get('missing') or not b_ else 'present')))
            moved.append(n)
            continue
        diffs = []
        for k_ in ('statement', 'kind', 'module', 'line', 'axioms', 'consumes'):
            if a_.get(k_) != b_.get(k_):
                diffs.append(k_)
        if diffs:
            cause = ('the sig' if 'statement' in diffs else '') + (' the place %s:%s -> %s:%s' % (a_.get('module'), a_.get('line'), b_.get('module'), b_.get('line')) if ('module' in diffs or 'line' in diffs) else '') \
                + (' the axioms %s -> %s' % (a_.get('axioms'), b_.get('axioms')) if 'axioms' in diffs else '') + (' the consumed nodes' if 'consumes' in diffs else '') + (' the kind' if 'kind' in diffs else '')
            rows.append((n, 'DIFFERS ' + ','.join(diffs), cause.strip()))
            if 'statement' in diffs:
                moved.append(n)
        else:
            rows.append((n, 'EQUAL', ''))
    sig_moved = [n for n in moved]
    L = ['%s -- (R318)(4): THE PROBE DIFFED AGAINST b704`S PROBE BANK, CELL BY CELL (%s)' % (ACT, utc()), '',
         '### this act`s probe (relay data/b708_probe_out_zeta.txt, the workflow`s probe step at %s, the tree v0.37`s) against b704`s (relay data/b704_probe_out_zeta.txt,' % K.PROBE_BRANCH,
         '### run 39721668586 through the closure step at v0.37), by chain_page`s parser; rows are cells: name | EQUAL, DIFFERS <fields> or MISSING | the cause.',
         '### A sig moved is a cell whose #print statement differs (or is missing on one side); the page is regenerated where one moved and not otherwise.', '']
    L += ['  %-70s %-28s %s' % r for r in rows if r[1] != 'EQUAL']
    L += ['  (every other cell EQUAL: %d)' % sum(1 for r in rows if r[1] == 'EQUAL')]
    L += ['', '### ### **CELLS COMPARED %d ; EQUAL %d ; DIFFERING %d ; SIGS MOVED %d %s ; THE PAGE %s.**' % (
        len(rows), sum(1 for r in rows if r[1] == 'EQUAL'), sum(1 for r in rows if r[1] != 'EQUAL'), len(sig_moved), sig_moved[:10] or '',
        'REGENERATED (a sig moved)' if sig_moved else 'NOT REGENERATED (no sig moved)')]
    put_txt('%s_probe_compare.txt' % ACT, L)
    put_json('%s_probe_compare.json' % ACT, dict(at=utc(), compared=len(rows), equal=sum(1 for r in rows if r[1] == 'EQUAL'), moved=sig_moved,
                                                differing=[dict(name=r[0], how=r[1], cause=r[2]) for r in rows if r[1] != 'EQUAL']))
    print(NL.join(L[-2:]))


# ================================================================================ COMPONENT 2: THE ENTRY-TAG PRINT AT v0.17, (R318)(5) (b706's form)
def tagstate(*a):
    """`tagstate <tag>`: the tag's tree read through the tool (no blob through the shell): its files, lean-toolchain, the lakefile's name and
    require lines, the mentioned theorem's module by git grep bounded to the tree; writes nothing."""
    tag = a[0]
    tree = (g(EF, 'ls-tree', '-r', '--name-only', tag) or '').split()
    lt = (_show(EF, tag, 'lean-toolchain') or '').strip()
    lf_name = next((f for f in ('lakefile.toml', 'lakefile.lean') if f in tree), None)
    lf = (_show(EF, tag, lf_name) or '') if lf_name else ''
    req = [l.strip() for l in lf.split(NL) if 'require' in l or 'mathlib' in l.lower() or 'lean_lib' in l or 'name' in l][:12]
    thm = K.TAG_THEOREMS.get(tag, '')
    short = thm.split('.')[-1]
    hit = g(EF, 'grep', '-n', '-E', '-e', r'^(theorem|lemma) +%s\b' % re.escape(short), tag, '--', '*.lean').strip()
    print('  tag %s ; peel %s ; files %d ; lean-toolchain %r ; lakefile %s' % (tag, g(EF, 'rev-list', '-n', '1', tag).strip()[:12], len(tree), lt, lf_name))
    print('  the lakefile`s require and lib lines: %s' % req)
    print('  print_targets.txt in the tree %s ; the workflow in the tree %s ; lake-manifest.json %s' % ('print_targets.txt' in tree, WF in tree, 'lake-manifest.json' in tree))
    print('  the theorem %s: %s' % (thm, hit[:160] or '### NOT FOUND'))


def printprobe(*a):
    """`printprobe <tag>`: the scratch branch prints-b708-<tag>, checked out at the tag with no tracked change, given (R316)(7)'s three files
    by this route (b706's form) -- the workflow as SIDE-explicit-formula's main carries it (its blob's bytes, verbatim), print_targets.txt
    naming the mentioned theorem alone, and a root ChainProbe.lean in tools/chain_page.py's probe form (PROBE_HEAD, one #chain_cell for the
    theorem, the import of its module alone) for the workflow's probe step; the files banked with their sha256 in
    data/b708_print_files_<branch>.json (.txt) before the commit. Nothing else of the tag's tree is touched."""
    import io as _io
    import chain_page as CP
    tag = a[0]
    br = 'prints-b708-%s' % tag
    thm, mod = K.TAG_THEOREMS[tag], K.TAG_MODULES[tag]
    head = g(EF, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    base = g(EF, 'rev-parse', 'HEAD').strip()
    peel = g(EF, 'rev-list', '-n', '1', tag).strip()
    dirty = g(EF, 'status', '--porcelain', '--untracked-files=no').strip()
    if head != br or base != peel or dirty:
        sys.exit('### THE CHECKOUT IS NOT %s AT %s WITH NO TRACKED CHANGE (head %s at %s, dirty %r) -- NOTHING WRITTEN' % (br, tag, head, base[:7], dirty))
    wf_text = _show(EF, 'main', WF) or ''
    pt_text = thm + NL
    probe_ = CP.PROBE_HEAD.replace('@@IMPORTS@@', 'import %s' % mod) + NL + '#chain_cell %s [%s] []' % (thm, thm) + NL
    files = {WF: wf_text, 'print_targets.txt': pt_text, 'ChainProbe.lean': probe_}
    os.makedirs(os.path.join(EF, '.github', 'workflows'), exist_ok=True)
    for f, t in files.items():
        _io.open(os.path.join(EF, *f.split('/')), 'w', encoding='utf-8', newline=NL).write(t)
    files['lakefile.toml'] = _show(EF, tag, 'lakefile.toml') or ''
    files['lean-toolchain'] = _show(EF, tag, 'lean-toolchain') or ''
    shas = dict((f, hashlib.sha256(t.encode('utf-8')).hexdigest()) for f, t in files.items())
    wf_main_sha = hashlib.sha256((_show(EF, 'main', WF) or '').encode('utf-8')).hexdigest()
    L = ['%s -- COMPONENT 2, (R318)(5) IN (R316)(7)`S FORM: THE SCRATCH BRANCH %s AT %s = %s, ITS THREE FILES WRITTEN BY THIS ROUTE AND BANKED BEFORE THE COMMIT (%s)' % (ACT, br, tag, peel[:7], utc()), '',
         '### rows are files: the path | sha256 | bytes. The workflow is main`s blob verbatim; the print list the mentioned theorem alone; the probe',
         '### chain_page.py`s PROBE_HEAD with the import of %s and one #chain_cell; the lakefile and toolchain the tag`s own, unedited.' % mod, '']
    L += ['  %-40s sha256 %s ; %d bytes' % (f, shas[f], len(t.encode('utf-8'))) for f, t in files.items()]
    for f in (WF, 'print_targets.txt', 'ChainProbe.lean'):
        L += ['', '=== %s' % f] + ['    ' + x for x in files[f].rstrip(NL).split(NL)]
    L += ['', '### ### **BRANCH %s AT %s ; FILES WRITTEN 3 ; THE WORKFLOW EQUAL TO main`S BLOB %s ; THE TARGET MODULE %s ; THE THEOREM %s.**' % (
        br, peel[:7], shas[WF] == wf_main_sha, mod, thm)]
    put_txt('%s_print_files_%s.txt' % (ACT, br), L)
    put_json('%s_print_files_%s.json' % (ACT, br), dict(at=utc(), branch=br, tag=tag, peel=peel, theorem=thm, module=mod, blobs=files, sha256=shas))
    print(NL.join(L[:8] + L[-1:]))


def printsbank(*a):
    """`printsbank <tag> <run id>`: the run's SEPARATE chain-probe artifact (chain-probe-<run id>) read by name, its sha256 against the platform's
    digest before any reading; probe/chainprobe.txt banked as data/b708_prints_<tag>.txt (the probe's own print, parsed by tools/chain_page.py's
    parser as the banked chain probes are) with data/b708_prints_<tag>.json (the run, the artifact, the parsed cell)."""
    import chain_page as CP
    tag, run_id = a[0], int(a[1])
    art, sha, T_, names_ = _probe_artifact(run_id)
    if not art:
        sys.exit('### NO chain-probe ARTIFACT ON RUN %d (listed %s) -- NOTHING READ' % (run_id, names_))
    text = T_.get('chainprobe.txt', '')
    log = T_.get('chainprobe_log.txt', '')
    cells, errors = CP.parse(text)
    thm = K.TAG_THEOREMS[tag]
    c = cells.get(thm) or {}
    L = ['%s -- THE ENTRY-TAG PRINT AT %s (SIDE-explicit-formula %s), RUN %d, THE PROBE STEP`S OUTPUT READ AFTER THE PROBE ARTIFACT`S SHA256 %s AGREED WITH THE PLATFORM`S (%s)' % (
        ACT, tag, g(EF, 'rev-list', '-n', '1', tag).strip()[:7], run_id, sha[:16], utc()), '### the probe`s log: %s' % ' '.join(log.split()),
         '### the artifact %s (id %s, %s bytes) ; files %s ; the probe`s errors %d ; the cell %s: %s' % (
             art.get('name'), art.get('id'), art.get('size_in_bytes'), sorted(T_), len(errors), thm, ('statement ' + c.get('statement', '')) if c.get('statement') else ('### ' + ('MISSING' if c.get('missing') else 'NOT PARSED'))),
         ''] + text.rstrip(NL).split(NL)
    put_txt('%s_prints_%s.txt' % (ACT, tag), L)
    put_json('%s_prints_%s.json' % (ACT, tag), dict(at=utc(), tag=tag, run_id=run_id, artifact=dict(id=art.get('id'), name=art.get('name'), sha256=sha), files=sorted(T_),
                                                   log=log, errors=errors, cell=c, theorem=thm))
    print(NL.join(L[:3]))


def cellsreach(*a):
    """data/b708_cells_reread.txt (.json): (R318)(5)'s last step -- the two unbanked mentions of data/b706_cells_reread.txt re-read: the first
    against the new print bank (data/b708_prints_v0.17.txt): the statement at v0.17 beside the statement at v0.37 (data/b704_probe_out_zeta.txt),
    "equal" or "differs"; the second (FACES_LEDGER :20) naming no kernel and no tag, re-read as it stands, unbanked by its own line (b707's (e),
    this act's (f)); the nine b706 read equal carried."""
    import chain_page as CP
    cells37, _e = CP.parse(rdn('b704_probe_out_zeta.txt'))
    banks = dict((tg, CP.parse(rdn('%s_prints_%s.txt' % (ACT, tg)))[0]) for tg in K.TAG_THEOREMS if os.path.exists(os.path.join(D, '%s_prints_%s.txt' % (ACT, tg))))
    prev = jl('b706_cells_reread.json').get('rows') or []
    rows = []
    for r in prev:
        if r.get('verdict') == 'equal':
            rows.append(dict(r, verdict='equal (b706, carried)', bank=r.get('bank')))
            continue
        m = next((x for x in K.MENTIONS_UNBANKED if x[1] == r.get('path') and x[2] == r.get('line')), None)
        tg = m[3] if m else None
        full = K.TAG_THEOREMS.get(tg) if tg else None
        st37 = (cells37.get(full) or {}).get('statement') if full else None
        st_t = ((banks.get(tg) or {}).get(full) or {}).get('statement') if (tg in banks and full) else None
        if tg in banks and full:
            v = 'equal' if (st_t and st37 and ' '.join(st_t.split()) == ' '.join(st37.split())) else ('differs' if (st_t and st37) else 'unbanked (the bank holds no cell for the name)')
        else:
            v = 'unbanked (no kernel and no tag named by the line; read as it stands)'
        rows.append(dict(doc=r['doc'], path=r['path'], line=r['line'], full=full or r.get('full') or '(none named)', tag=tg or '(no tag)', st37=st37, st_t=st_t, verdict=v,
                         bank=('data/%s_prints_%s.txt' % (ACT, tg)) if tg in banks else None))
    L = ['%s -- COMPONENT 2, (R318)(5): THE TWO UNBANKED MENTIONS OF data/b706_cells_reread.txt RE-READ AGAINST THE ENTRY-TAG PRINT AT v0.17 (%s)' % (ACT, utc()), '',
         '### rows are mentions (paper :line | theorem | tag): the statement at the tag from data/b708_prints_<tag>.txt (the probe step`s print, run on the scratch',
         '### branch at the tag) against the statement at v0.37 (data/b704_probe_out_zeta.txt, run 39721668586); "equal" or "differs"; a mention with no tag',
         '### beside the kernel stays unbanked (FACES_LEDGER :20, the F1 row, names no kernel: b707`s (e), this act`s (f)); the nine b706 read equal carried.', '']
    for r in rows:
        L += ['  %s | %s :%d | %s | tag %s | %s' % (r['doc'], r['path'], r['line'], r['full'], r['tag'], r['verdict'])]
        if not r['verdict'].startswith('equal (b706'):
            L += ['      at v0.37: %s' % (r['st37'] or '-'), '      at %s (%s): %s' % (r['tag'], r['bank'] or 'no bank', r['st_t'] or '-')]
    L += ['', '### ### **MENTIONS 11 ; EQUAL %d (9 CARRIED FROM b706, %d RE-READ THIS ACT) ; DIFFERS %d ; UNBANKED %d (no kernel and no tag named %d).**' % (
        sum(1 for r in rows if r['verdict'].startswith('equal')), sum(1 for r in rows if r['verdict'] == 'equal'), sum(1 for r in rows if r['verdict'] == 'differs'),
        sum(1 for r in rows if r['verdict'].startswith('unbanked')), sum(1 for r in rows if 'no kernel and no tag' in r['verdict']))]
    put_txt('%s_cells_reread.txt' % ACT, L)
    put_json('%s_cells_reread.json' % ACT, dict(at=utc(), rows=rows))
    print(NL.join([l for l in L if l.startswith('  ') and ' | tag ' in l] + L[-1:]))


def scratch(*a):
    """data/b708_scratch_branches.txt (.json): the two scratch branches of (R318)(4)-(5), each cut, committed once, pushed alone in branch mode,
    dispatched once and deleted by name locally and at the remote after its bank was committed; read now against the remote (one ls-remote),
    main and the tags untouched."""
    rh = R._remote_heads(EF)
    rows = []
    for br, base, tip, bank in ((K.PROBE_BRANCH, K.EF_MAIN, '75bd018b784d3f9d27a829af65b54d33fd8e2796', 'data/b708_probe.txt'),
                                (K.PRINTS_BRANCH, K.EF_V017, '2627fa68a67dde0487bb0beab5f2ca8aca2549d9', 'data/b708_print_files_prints-b708-v0.17.txt')):
        rows.append(dict(branch=br, base=base, tip=tip, local=bool(g(EF, 'branch', '--list', br).strip()), remote=br in rh, bank=bank,
                         tip_in_log=bool(g(EF, 'cat-file', '-t', tip).strip() == 'commit')))
    main_ = g(EF, 'rev-parse', 'main').strip()
    tags_past = [t for t in g(EF, 'tag', '--contains', K.EF_V037).split(NL) if t.strip() and t.strip() != 'v0.37']
    L = ['%s -- COMPONENT 2, (R318)(4)-(5): THE SCRATCH BRANCHES OF SIDE-explicit-formula, DELETED BY NAME AFTER THEIR BANKS WERE COMMITTED (%s)' % (ACT, utc()), '',
         '### rows are branches: the branch | its base | its one commit | present locally | present at the remote (one ls-remote) | the bank committed before the delete.',
         '### Each deleted in the house form: -D locally (a scratch branch, unmerged), then `push origin --delete` at the remote, one branch per command, each its own message.']
    L += ['  %-20s | base %s | tip %s | local %s | remote %s | %s' % (r['branch'], r['base'][:7], r['tip'][:7], r['local'], r['remote'], r['bank']) for r in rows]
    L += ['', '### ### **SCRATCH BRANCHES %d ; DELETED LOCALLY %d ; DELETED AT THE REMOTE %d ; main %s UNMOVED %s ; TAGS PAST v0.37 %s.**' % (
        len(rows), sum(1 for r in rows if not r['local']), sum(1 for r in rows if not r['remote']), main_[:7], main_ == K.EF_MAIN, tags_past or 'NONE')]
    put_txt('%s_scratch_branches.txt' % ACT, L)
    put_json('%s_scratch_branches.json' % ACT, dict(at=utc(), rows=rows, main=main_, tags_past=tags_past))
    print(NL.join(L[4:]))


# ================================================================================ COMPONENT 3: THE RE-CUT OF day1/Spectral_Inertness.md ((R318)(6); b704's form)
CUT_DOC = K.CUT_DOC
CUT_TABLE = K.CUT_TABLE
# ### the lines the cut changes, each with one case-exact needle and one wider case-insensitive needle (the two shapes of b702's search)
QUOTE_LINES = [
    (9, 'The theorem and its consequences are machine-checked in Lean 4 against Mathlib', 'the theorem and its consequences are machine-checked'),
    (57, 'The product formula and its spectral inertness are formally verified in Lean 4 against Mathlib', 'three files build a chain from prime powers to rationals'),
    (59, '(prime powers): p^{v_p(n)} · |n|_p = 1. 6 theorems.', 'p^{v_p(n)} · |n|_p = 1. 6 theorems'),
    (60, '(integers): |n| · ∏_{p|n} |n|_p = 1. 8 theorems.', '|n| · ∏_{p|n} |n|_p = 1. 8 theorems'),
    (61, '(rationals and spectral inertness): ∏_v |x|_v = 1 for x ∈ ℚ×, together with ∀ s : ℂ, 1^s = 1. 8 theorems.', 'together with ∀ s : ℂ, 1^s = 1. 8 theorems'),
    (63, 'Total: 22 theorems. Zero `sorry` (unproved assertions). Zero custom axioms.', 'merged into the mathlib standard library (prs \\#36881 and \\#36865)'),
    (87, "This seal is the proof of RH's one certified premise", 'the catalogue surrounding it is machine-checked'),
    (107, '| Zeros confined to critical line | Yes | **No** |', 'zeros confined to critical line | yes'),
    (112, 'The outcome difference is the confinement of zeros.', 'the outcome difference is the confinement of zeros'),
    (116, 'we make it explicit and formally verify it', 'with all 34 confirmed'),
    (161, 'This paper develops one component of a proof of Theorem (RH)', 'develops one component of a proof of theorem (rh)'),
    (172, 'it is what lets a finite catalogue of mechanisms be sufficient', 'lets a finite catalogue of mechanisms be sufficient'),
    (174, 'it verifies that the interface predicates are independent of the spectral parameter', 'verifies that the interface predicates are independent of the spectral parameter'),
    (200, 'A second inertness-shaped machine fact now stands beside Conservation of Spectra', 'inertness-shaped machine fact now stands beside conservation of spectra'),
    (209, 'the register sentence (`h2` the single open premise) unchanged', 'the register sentence (`h2` the single open premise) unchanged'),
]
CUT_HELD = (178, 181)   # ### the Correspondence table's cells (:176-:181): no cell by hand, the paper off the roster (b704's form, data/b704_cut.txt :32-:39)


def quote(*a):
    """data/b708_quote.txt (.json): data/b690_rules.txt row (2) at a paper cut, BEFORE the cut's commit -- each line the cut changes read at
    PLACE-papers HEAD, its two needles checked to stand in it, each searched with git grep -n -F across PLACE-papers' tracked tree at HEAD (the
    exact shape and the case-insensitive shape); every hit outside the cut lines themselves a quoting line, entered as a residue in the cut bank.
    The b670 form a paper cut takes (a `document`, no kernel, no merge), as b703's repaired arm reads it."""
    doc = (_show(PP, 'HEAD', CUT_DOC) or '').replace(chr(13), '').split(NL)
    rows, bad = [], []
    for ln, nd, wd in QUOTE_LINES:
        line = doc[ln - 1]
        if nd not in line or wd.lower() not in line.lower():
            bad.append((ln, nd in line, wd.lower() in line.lower()))
        h1 = [x for x in g(PP, 'grep', '-n', '-F', nd, 'HEAD', '--').split(NL) if x.strip()]
        h2 = [x for x in g(PP, 'grep', '-n', '-i', '-F', wd, 'HEAD', '--').split(NL) if x.strip()]
        own = lambda h: h.split(':', 2)[1] == CUT_DOC and int(h.split(':', 3)[2]) in [q[0] for q in QUOTE_LINES]   # noqa: E731
        rows.append(dict(line_no=ln, line=line, needle=nd, wide=wd, hits=[h for h in h1 if not own(h)], hits_wide=[h for h in h2 if not own(h)],
                         own=[h for h in h2 if own(h)]))
    if bad:
        sys.exit('### A NEEDLE DOES NOT STAND IN ITS OWN LINE %s -- NOTHING WRITTEN' % bad)
    quoting = sorted(set((h.split(':', 3)[1], int(h.split(':', 3)[2])) for r in rows for h in r['hits'] + r['hits_wide']))
    L = ['%s -- COMPONENT 3, (R318)(6): THE QUOTATION SEARCH BEFORE THE CUT`S COMMIT, data/b690_rules.txt row (2), OVER %s (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the lines the cut changes, read at PLACE-papers HEAD %s; each with a case-exact needle and a case-insensitive needle, both checked to' % g(PP, 'rev-parse', '--short=7', 'HEAD').strip(),
         '### stand in the line; each searched with git grep -n -F across the tracked tree at HEAD. The cut lines themselves are not counted (their own',
         '### hits printed). Rows are lines: :line | needle | hits | case-insensitive needle | hits, then every hit with its quoting line.', '']
    for r in rows:
        L.append('  :%-3d | %-62r %d hit(s) | %-50r %d hit(s) | own %d' % (r['line_no'], r['needle'], len(r['hits']), r['wide'], len(r['hits_wide']), len(r['own'])))
        L += ['      %s' % h[:220] for h in sorted(set(r['hits'] + r['hits_wide']))]
    L += ['', '### THE QUOTING LINES, DISTINCT (file :line), EACH A RESIDUE: %s' % ('; '.join('%s :%d' % q for q in quoting) or 'NONE'),
          '### ### **LINES CHANGED BY THE CUT %d ; NEEDLES %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE ; SEARCHED BEFORE THE CUT`S COMMIT.**' % (
              len(rows), 2 * len(rows), len(quoting))]
    if 'dry' not in a:
        put_txt('%s_quote.txt' % ACT, L)
        put_json('%s_quote.json' % ACT, dict(at=utc(), document=CUT_DOC, base=g(PP, 'rev-parse', 'HEAD').strip(), rows=rows, quoting=[list(q) for q in quoting]))
    print(NL.join(L[6:]) if 'dry' in a else NL.join([x for x in L if x.startswith('  :')] + L[-2:]))


TROW = re.compile(r'^  :(\d+) \| [^|]+\| [^|]+\| [^|]+\| [^|]+\| (MATCHES|OVERREACHES|UNLICENSED|UNDERSTATES) ; "(.*)" ; (.*)$')


def cutbank(*a):
    """data/b708_cut.txt (.json): (R318)(6), the re-cut of day1/Spectral_Inertness.md by the b670 method -- each non-MATCHES row of its table
    (relay data/b646_table_Spectral_Inertness.txt) with its STATED text searched whitespace-normalized in the document at the base and now, the
    row met where it no longer stands; the Correspondence cells held (no cell by hand, the paper off the roster: b704's form); the residues from
    the quotation search (data/b708_quote.json). `cutbank [<cut commit>]`: with the cut's PLACE-papers commit named, the bank's base is that
    commit's parent (`<sha>^`) and "now" its tree."""
    commit = a[0] if a and re.match(r'^[0-9a-f]{7,40}$', a[0]) else None
    base_ref = (commit + '^') if commit else 'HEAD'
    norm = lambda s: ' '.join((s or '').split())   # noqa: E731
    base = norm(_show(PP, base_ref, CUT_DOC))
    now = norm(_show(PP, commit, CUT_DOC) if commit else rd(os.path.join(PP, CUT_DOC)))
    rows = []
    for l in rdn(CUT_TABLE).split(NL):
        m = TROW.match(l)
        if not m or m.group(2) == 'MATCHES':
            continue
        ln, v, st, act = int(m.group(1)), m.group(2), m.group(3), m.group(4)
        held = ln in CUT_HELD
        rows.append(dict(line=ln, verdict=v, stated=st, action=act.split(' -- ')[0][:60], held=held, base=norm(st) in base, now=norm(st) in now))
    mt = [(int(m.group(1)), m.group(3)) for m in (TROW.match(l) for l in rdn(CUT_TABLE).split(NL)) if m and m.group(2) == 'MATCHES']
    mt_lost = [(ln, st) for ln, st in mt if norm(st) in base and norm(st) not in now]
    q = jl('%s_quote.json' % ACT)
    res = [list(x) for x in (q.get('quoting') or [])]
    dist = [r for r in rows if r['verdict'] in ('OVERREACHES', 'UNLICENSED')]
    und = [r for r in rows if r['verdict'] == 'UNDERSTATES']
    before = sum(1 for r in dist if r['base'])
    after = sum(1 for r in dist if r['now'])
    L = ['%s -- COMPONENT 3, (R318)(6): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (ACT, CUT_DOC, utc()), '',
         '### the document: %s (v2.3.1), named by b652`s order passing to the companions, alone at the top count (relay data/b708_tie.txt), b674`s rule and' % CUT_DOC,
         '### b705`s row (2) not reached. Its table: relay data/%s, pinned at 96779e5, 209 lines, sha256 3bf77f85e2a5af68 = the base`s. The' % CUT_TABLE,
         '### cut: each non-MATCHES row`s ACTION applied by the Edit tool on the rows alone, the paper`s title, opening label lines, version line and file',
         '### name untouched (W-ORD-KEYSTONE-HEADS held: the cut writes rows, not the paper`s opening); the Correspondence cells :178 and :181 held (no',
         '### Correspondence cell by hand, the paper off the 20-table roster, b704`s form at data/b704_cut.txt :32-:39).',
         '### the base %s ; now %s.' % (base_ref, commit or 'the working tree'), '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row`s STATED text searched whitespace-normalized in the document at the base and now,',
         '### the row met where it no longer stands. Rows: base line | verdict | applied or HELD | stands at the base | stands now | the STATED text:']
    for r in rows:
        L.append('  :%-3d | %-11s | %-7s | base %-5s | now %-5s | %s' % (r['line'], r['verdict'], 'HELD' if r['held'] else 'applied', r['base'], r['now'], r['stated'][:110]))
        if r['held']:
            L.append('        HELD: a cell of the paper`s Correspondence table (base :176-:181); no Correspondence cell by hand, and the paper is off the 20-table roster')
    unmet = [r for r in rows if not r['held'] and r['now']]
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b708_quote.txt, two shapes, the search run before the cut`s commit): each quoting',
          '### line, file :line -- carried by its own table or frozen as deposited; none written:']
    L += ['  %s :%d' % (f, n_) for f, n_ in res]
    L += ['', '### THE ROWS APPLIED THAT STILL STAND: %s' % (['%d %s' % (r['line'], r['stated'][:60]) for r in unmet] or 'NONE'),
          '### UNDERSTATES (not in the distance): %d at the base, %d now' % (sum(1 for r in und if r['base']), sum(1 for r in und if r['now'])),
          '### THE CONTROL, THE MATCHES ROWS: %d at the base ; standing now %d ; no longer standing %s' % (
              sum(1 for _l, st in mt if norm(st) in base), sum(1 for _l, st in mt if norm(st) in now), ['%d %s' % (ln, st[:60]) for ln, st in mt_lost] or 'NONE'),
          '### ### **THE DISTANCE BY THE b670 METHOD: BEFORE %d, AFTER %d ; ROWS APPLIED %d ; HELD %d (CORRESPONDENCE CELLS) ; QUOTING LINES %d ENTERED AS RESIDUES.**' % (
              before, after, sum(1 for r in rows if not r['held']), sum(1 for r in rows if r['held']), len(res))]
    if 'dry' not in a:
        put_txt('%s_cut.txt' % ACT, L)
        put_json('%s_cut.json' % ACT, dict(at=utc(), document=CUT_DOC, base=base_ref if commit else '', before=before, after=after,
                                          held=[r['line'] for r in rows if r['held']], residues=res, matches_lost=[list(x) for x in mt_lost],
                                          rows=[dict((k, v) for k, v in r.items()) for r in rows]))
    print(NL.join(L[-4:]))


def quotecheck(*a):
    """a print only: G-RULE-RECUT-QUOTE's reading (tools/rule_arms.py, unedited) over the quote banks, restricted to this act's -- the search
    before the cut's own PLACE-papers commit, every quoting line entered in the cut bank's residues."""
    import rule_arms as RA
    S = RA.sources(ACT, None, K.ANCHOR, K.PARTS, pre_relay=None, pre_pp=None)
    mine = [q for q in S['quotes'] if q['act'] == int(ACT[1:])]
    S2 = dict(S)
    S2['quotes'] = mine
    S2['cut_banks'] = dict((k, v) for k, v in S['cut_banks'].items() if k == int(ACT[1:]))
    for q in mine:
        print('  %s kind %s ; merge %s ; search at %s ; before the merge %s ; needled %s ; quoting %d ; unentered %d' % (
            q['bank'], q.get('kind', 'kernel'), (q['merge'] or ['-'])[0][:7], q['at'], bool(q['merge'] and q['at'] and q['at'] < q['merge'][1]),
            q['needled'], len(q['quoting']), len(q['unentered'])))
    print('  the arm over b708`s banks: %s ; over every bank: %s' % (RA.reading('G-RULE-RECUT-QUOTE', S2), RA.reading('G-RULE-RECUT-QUOTE', S)))


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks, c1=c1,
              scratch=scratch, quote=quote, cutbank=cutbank, quotecheck=quotecheck, probe=probe, probediff=probediff, runner=runner, probeview=probeview, probecompare=probecompare, tagstate=tagstate, printprobe=printprobe,
              printsbank=printsbank, cellsreach=cellsreach,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, tie=tie)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b708_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
