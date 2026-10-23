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


# ================================================================================ COMPONENT 4: THE PORT'S NEXT LINES, HELD, (R318)(7)
def portlines(*a):
    """data/b708_port_lines.txt (.json): (R318)(7), the two failing lines of port-b707's one run read from data/b707_port.txt by line, the kind of
    each failure read from the error's own text and printed -- :277:55 an application type mismatch (a changed signature: WeakFEPair.hasMellin
    takes the hypothesis `k < re s` where the argument `w` was given), :380:8 the kernel's unknown constant (a renamed Mathlib declaration,
    exists_norm_completedRiemannZeta₀_le_exp_half moved); no edit to port-b707 this act; the dispatch at b709."""
    pt = rdn('b707_port.txt').split(NL)
    l11, l14 = pt[10] if len(pt) > 10 else '', pt[13] if len(pt) > 13 else ''
    ctx = pt[34:42] if len(pt) > 41 else []
    k1 = 'a changed signature' if 'Application type mismatch' in l11 and any('is expected to have type' in l for l in ctx) else '### NOT READ'
    k2 = 'a renamed Mathlib declaration' if 'unknown constant' in l14 else '### NOT READ'
    tip = g(K.LV_DIR, 'rev-parse', K.PORT_BRANCH).strip()
    rh = R._remote_heads(K.LV_DIR)
    L = ['%s -- COMPONENT 4, (R318)(7): THE PORT`S NEXT LINES, HELD THIS ACT -- THE TWO FAILURES` KINDS READ FROM data/b707_port.txt (%s)' % (ACT, utc()), '',
         '### rows are the next failing lines of port-b707`s one run (relay data/b707_port.txt, run 39888369981), each with its error line by the bank`s line and',
         '### the kind the ruling names (a renamed Mathlib declaration, a changed signature, a broken proof) read from the error`s own text; no edit to port-b707',
         '### this act; both the port`s next dispatch at b709 ((R318)(11); W-ORD-LV-FORWARD-PORT, OPEN_TRAILS :15686).', '',
         '  C7OrderBounds.lean :277:55 | data/b707_port.txt :11 | %s | THE KIND: %s -- `WeakFEPair.hasMellin (hurwitzEvenFEPair 0).toStrongFEPair w` given `w : ℂ` where the first explicit argument is now the hypothesis `k < re s` (data/b707_port.txt :35-:42); the call`s arguments re-ordered at Mathlib de5ce8a9' % (l11.strip(), k1),
         '  C7OrderBounds.lean :380:8  | data/b707_port.txt :14 | %s | THE KIND: %s -- `SIDELvConservation.exists_norm_completedRiemannZeta₀_le_exp_half` unknown to the kernel at the pin, the name moved; the replacement to be read at b709 from Mathlib de5ce8a9`s own declarations' % (l14.strip(), k2),
         '', '### port-b707 at %s locally, %s at the remote (one ls-remote), equal to b707`s commit %s ; no edit this act.' % (tip[:12], (rh.get(K.PORT_BRANCH) or 'absent')[:12], tip == rh.get(K.PORT_BRANCH) == K.PORT_COMMIT),
         '', '### ### **LINES 2 ; KINDS: :277:55 %s ; :380:8 %s ; port-b707 UNEDITED %s ; THE NEXT DISPATCH AT b709.**' % (k1, k2, tip == rh.get(K.PORT_BRANCH) == K.PORT_COMMIT)]
    put_txt('%s_port_lines.txt' % ACT, L)
    put_json('%s_port_lines.json' % ACT, dict(at=utc(), lines=[dict(line='277:55', bank_line=11, error=l11.strip(), kind=k1), dict(line='380:8', bank_line=14, error=l14.strip(), kind=k2)],
                                             port_tip=tip, port_remote=rh.get(K.PORT_BRANCH), unedited=tip == rh.get(K.PORT_BRANCH) == K.PORT_COMMIT))
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 5: THE CARRY-TIME REPAIR AND ITS CONTROLS
def _udiff(old, new, a, b):
    import difflib
    return list(difflib.unified_diff(old, new, a, b, lineterm='', n=2))


def _fn_lines(fn):
    import inspect
    return [l.rstrip(NL) for l in inspect.getsource(fn).split(NL)]


def repairs(*a):
    """data/b708_tool_repairs.txt (.json): the ferry's Component 5 -- every carry-time repair of this act shown as a diff: (1) the print-list
    reader `_print_modules708` against b705's `_print_modules` (tools/b705_record.py :732), a hit under a lean_lib's srcDir named relative to
    it as Lake names it (the vendored lib BulkaVendored at srcDir Vendored/Bulka: its module Lc.LiCriterion.ReverseDirection, not
    Vendored.Bulka.Lc...); the two forms carried unchanged from b707 (prev_capture for another session, ROOT_EXCLUDE from the tools'
    declarations) named as carried, not repaired. No shared file edited. The controls: data/b708_repair_controls.txt."""
    old, new = _fn_lines(P5._print_modules), _fn_lines(_print_modules708)
    d1 = _udiff(old, new, 'tools/b705_record.py _print_modules (b705, sealed)', 'tools/b708_record.py _print_modules708 (this act)')
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS, THE FERRY`S COMPONENT 5 (%s)' % (ACT, utc()), '',
         '### rows are repairs with what they answer: the tool and its part ; what it answers ; the form. Each diff beneath its row, written by this',
         '### route (the carried function`s source against this act`s). The controls that distinguish each repaired reading from the old one:',
         '### data/b708_repair_controls.txt. No sealed tool is edited; no shared tool or shared data file is edited this act.', '',
         '  (1) tools/b708_record.py `_print_modules708` -- ANSWERS the dispatch of (R318)(4) under data/b705_rules.txt row (1): b705`s reader (tools/b705_record.py :732) names each print-list hit`s module by its path with / for . and no .lean, so the vendored lib`s hit Vendored/Bulka/Lc/LiCriterion/ReverseDirection.lean read as the module Vendored.Bulka.Lc.LiCriterion.ReverseDirection, a name no Lake target takes (the lib BulkaVendored declares srcDir = "Vendored/Bulka" in lakefile.toml, so Lake names the module Lc.LiCriterion.ReverseDirection); the dispatch`s `whole` check would then demand a module the target cannot carry. The repair: the lakefile`s lean_lib blocks read for their srcDir (`_lib_srcdirs`), a hit beneath a srcDir named relative to it; every other hit as b705 named it. Found at Component 2 before the probe dispatch; the repaired reader used for the probe`s target (54 modules, the run printing 109 of 109) and the prints dispatch. The control: the old and repaired readings over the print list at main, the vendored name`s file under its srcDir, the dispatched target covering the repaired modules, and a mutated lakefile without the srcDir line; data/b708_repair_controls.txt.', ''] + ['      ' + l for l in d1] + ['',
         '  CARRIED IN FORM, NOT REPAIRED: prev_capture (b707`s repair (5): the previous act`s window in b701`s form for another session, b707 having run and closed in aa198636) and ROOT_EXCLUDE (b707`s repair (6): data/b706_rules.txt row (1), extended at import with every untracked write a b708_*.py tool declares -- none declared this act), each carried into tools/b708_record.py with the act names rebound and no change of form (data/b707_tool_repairs.txt :183-:233).', '',
         '### ### **REPAIRS 1 ; CARRIED IN FORM 2 (prev_capture, ROOT_EXCLUDE) ; SHARED FILES EDITED 0 ; NO SEALED TOOL EDITED ; THE CONTROLS IN data/b708_repair_controls.txt.**']
    put_txt('%s_tool_repairs.txt' % ACT, L)
    put_json('%s_tool_repairs.json' % ACT, dict(at=utc(), repairs=[dict(n=1, tool='b708_record.py', part='_print_modules708', old='b705_record.py _print_modules', diff=d1)],
                                               carried=['prev_capture', 'ROOT_EXCLUDE']))
    print(NL.join(L[-3:]))


def _libs(kernel_dir, rev='main', text=None):
    """the lakefile's lean_lib blocks at rev: [(name, srcDir, roots, globs)] -- Lake's defaults where a key is absent (srcDir '.', roots [name],
    globs the roots as exact names); `text` names a mutated copy of the lakefile in place of the tree's."""
    txt = text if text is not None else (_show(kernel_dir, rev, 'lakefile.toml') or '')
    out, cur = [], None
    for l in txt.split(NL):
        if re.match(r'^\s*\[\[lean_lib\]\]', l):
            cur = dict(name=None, srcDir='', roots=None, globs=None)
            out.append(cur)
            continue
        if re.match(r'^\s*\[\[', l):
            cur = None
            continue
        if cur is None:
            continue
        m = re.match(r'^\s*(name|srcDir)\s*=\s*"([^"]+)"', l)
        if m:
            cur[m.group(1)] = m.group(2).strip('/') if m.group(1) == 'srcDir' else m.group(2)
        m = re.match(r'^\s*(roots|globs)\s*=\s*\[([^\]]*)\]', l)
        if m:
            cur[m.group(1)] = re.findall(r'"([^"]+)"', m.group(2))
    libs = []
    for c in out:
        roots = c['roots'] if c['roots'] is not None else [c['name']]
        globs = c['globs'] if c['globs'] is not None else list(roots)
        libs.append((c['name'], c['srcDir'], roots, globs))
    return libs


def _is_lake_module(mod, libs, rev='main'):
    """a module name is Lake`s where some lean_lib`s roots or globs cover it (X exact; `X.+` its submodules; `X.*` both) AND its file stands under that
    lib`s srcDir in the tree at rev."""
    rel = mod.replace('.', '/') + '.lean'
    for _name, sd, roots, globs in libs:
        covered = mod in roots or any((gl.endswith('.+') and mod.startswith(gl[:-2] + '.')) or (gl.endswith('.*') and (mod == gl[:-2] or mod.startswith(gl[:-2] + '.')))
                                      or (not gl.endswith(('.+', '.*')) and mod == gl) for gl in globs)
        if covered and _show(EF, rev, (sd + '/' + rel) if sd else rel):
            return True
    return False


def _apply_srcdirs(hits, dirs):
    out = {}
    for n, rel in hits.items():
        if rel is None:
            out[n] = None
            continue
        r = rel
        for sd, _nm in dirs:
            if r.startswith(sd + '/'):
                r = r[len(sd) + 1:]
                break
        out[n] = r.replace('/', '.')
    return out


def repairctl(*a):
    """data/b708_repair_controls.txt: the repaired reading against the old on real state and on mutated copies -- rows are cases: the reader |
    the source | the old reading | the repaired | wanted; each repaired reading DISTINGUISHED where one row reads them apart."""
    t0 = time.time()
    old = P5._print_modules(EF, 'main')
    new = _print_modules708(EF, 'main')
    dirs = _lib_srcdirs(EF, 'main')
    hits = dict((n, (m.replace('.', '/') if m else None)) for n, m in old.items())   # ### the old reading IS the path with / for ., so the hits are recovered from it
    vend = [n for n, m in new.items() if m and old.get(n) != m]
    disp = (jl('%s_dispatches.json' % ACT).get('rows') or [{}])[0]
    tgt = set((disp.get('target') or '').split())
    old_mods = sorted(set(m for m in old.values() if m))
    new_mods = sorted(set(m for m in new.values() if m))
    libs = _libs(EF, 'main')
    lf_text = _show(EF, 'main', 'lakefile.toml') or ''
    mut_text = NL.join(l for l in lf_text.split(NL) if not re.match(r'^\s*srcDir\s*=', l))   # ### the mutated lakefile: no srcDir line
    mut_libs = _libs(EF, 'main', text=mut_text)
    mut_new = _apply_srcdirs(hits, [(sd, n) for n, sd, _r, _g in mut_libs if sd])
    bad_list = dict(hits, **{'SIDEExplicitFormula.Planted.no_such_name': None})
    rows = [
        ('print_modules', 'the print list at main: every name mapped to a module', all(old.values()), all(new.values()), (True, True)),
        ('print_modules', 'the vendored name %s: a Lake module (a lean_lib`s roots or globs cover it and its file stands under that lib`s srcDir in the tree at main)' % (vend[0] if vend else '-'),
         bool(vend) and _is_lake_module(old[vend[0]], libs), bool(vend) and _is_lake_module(new[vend[0]], libs), (False, True)),
        ('print_modules', 'every mapped module a Lake module (lakefile.toml at main: %s)' % ['%s srcDir %r globs %s' % (n, sd, gl) for n, sd, _r, gl in libs],
         all(_is_lake_module(m, libs) for m in old_mods), all(_is_lake_module(m, libs) for m in new_mods), (False, True)),
        ('print_modules', 'the dispatched target of the probe run (relay data/b708_dispatches.json row 1) covers the reading`s modules', set(old_mods) <= tgt, set(new_mods) <= tgt, (False, True)),
        ('print_modules', 'a mutated copy of lakefile.toml, its srcDir line removed -- the repaired reading reads as the old (every mapped module a Lake module of the real lakefile)',
         all(_is_lake_module(m, libs) for m in old_mods), all(_is_lake_module(m, libs) for m in sorted(set(x for x in mut_new.values() if x))), (False, False)),
        ('print_modules', 'a mutated copy: a name no module declares planted in the list -- every name mapped', all(bad_list.values()), all(_apply_srcdirs(bad_list, dirs).values()), (False, False)),
    ]
    L = ['%s -- COMPONENT 5: THE REPAIRED READING AGAINST THE OLD ON REAL STATE AND ON MUTATED COPIES (%s)' % (ACT, utc()), '',
         '### rows are cases: the reader | the source (the kernel`s tree at main, the dispatch bank, or a mutated copy) | the old reading | the repaired | wanted.',
         '### Each repaired reading is DISTINGUISHED where one row reads them apart.', '',
         '### the print list at main: %d names ; the old reading`s modules %d ; the repaired`s %d ; the names read apart %s ; the lakefile`s srcDirs %s ; the target %d modules ; %.0f s' % (
             len(old), len(old_mods), len(new_mods), ['%s: old %s -> repaired %s' % (n, old[n], new[n]) for n in vend], dirs, len(tgt), time.time() - t0), '']
    ok = True
    for rd_, src, o, n, (wo, wn) in rows:
        asw = (o == wo and n == wn)
        ok = ok and asw
        L.append('  %-16s | %s | old %-5s | repaired %-5s | wanted old %s, repaired %s | %s' % (rd_, src, o, n, wo, wn, 'AS WANTED' if asw else '### NOT AS WANTED'))
    dist = sorted(set(rd_ for rd_, _s, o, n, _w in rows if o != n))
    L += ['', '### ### **CASES %d ; AS WANTED %s ; EACH REPAIRED READING DISTINGUISHED FROM THE OLD ON A ROW: %s.**' % (len(rows), ok, dist)]
    put_txt('%s_repair_controls.txt' % ACT, L)
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, against b707`s baselines)
def figures(*a):
    """data/b708_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited (correspondence() and partners()
    over b706's roster, data/b706_roster_read.json; readme() b705's, pins() b703's), each against b707's figure (data/b707_standing_figures.json),
    the pins baseline b707's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b707_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b708, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b707`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b707_standing_figures.json). day1/Spectral_Inertness.md, cut this act, is off the roster.', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b708 %s ; b707 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b708: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b707`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', baseline='b707_standing_figures.json',
                                                        **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


# ================================================================================ COMPONENT 5: THE REGISTRATIONS RE-READ ((R318)(3), N3)
def regcheck(*a):
    """data/b708_registrations_reread.txt (.json): data/b708_registrations.txt and data/b708_rules.txt re-read whole after Components 1-4 and
    compared byte for byte with the blobs committed alone at step zero (relay 6045dd8c); no eigenvalue computed this act (no onset or units
    bank of b708 exists; no onset tool run, read from the command capture by the suite)."""
    out = dict(at=utc(), commit=K.REG_COMMIT)
    same = True
    L = ['%s -- COMPONENT 5, (R318)(3): THE REGISTRATIONS AND THE RULES BANK RE-READ AFTER COMPONENTS 1-4, UNCHANGED; NO EIGENVALUE COMPUTED (%s)' % (ACT, utc()), '']
    for nm in ('registrations', 'rules'):
        p = 'data/%s_%s.txt' % (ACT, nm)
        now = rd(os.path.join(ROOT, *p.split('/'))) or ''
        then = _show(ROOT, K.REG_COMMIT, p) or ''
        hb = g(ROOT, 'rev-parse', 'HEAD:' + p).strip()
        tb = g(ROOT, 'rev-parse', '%s:%s' % (K.REG_COMMIT, p)).strip()
        wb = g(ROOT, 'hash-object', '--', p).strip()
        log = [l for l in g(ROOT, 'log', '--format=%h', '--', p).split(NL) if l.strip()]
        eq = now == then and wb == tb == hb and len(log) == 1
        same = same and eq
        out[nm] = dict(work_blob=wb, then_blob=tb, head_blob=hb, commits=log, unchanged=eq)
        L.append('### %s committed alone at relay %s before any computation (N3); re-read now: the working file`s blob %s ; the blob at %s %s ; at HEAD %s ; '
                 'the commits touching it %s ; EQUAL BYTE FOR BYTE %s' % (p, K.REG_COMMIT, wb[:12], K.REG_COMMIT, tb[:12], hb[:12], log, eq))
    onset_banks = sorted(f for f in os.listdir(D) if f.startswith('b708_') and ('onset' in f or 'units' in f or 'eigen' in f))
    L += ['### banks of this act naming an onset, units or an eigenvalue: %s' % (onset_banks or 'NONE'), '',
          '### THE REGISTRATIONS, PRINTED UNCHANGED:'] + ['    ' + x for x in (rd(os.path.join(D, '%s_registrations.txt' % ACT)) or '').rstrip(NL).split(NL)]
    L += ['', '### ### **REGISTRATIONS RE-READ: UNCHANGED SINCE %s %s ; THE RULES BANK UNCHANGED %s ; NO EIGENVALUE COMPUTED THIS ACT %s ; COMPUTED AT b709.**' % (
        K.REG_COMMIT, out['registrations']['unchanged'], out['rules']['unchanged'], not onset_banks)]
    out.update(unchanged=same, onset_banks=onset_banks, no_eigenvalue=not onset_banks)
    put_txt('%s_registrations_reread.txt' % ACT, L)
    put_json('%s_registrations_reread.json' % ACT, out)
    print(NL.join(L[2:5] + L[-1:]))


# ================================================================================ COMPONENT 6: THE SCORES (b686's order), THE RECORD, THE TRAIL, THE DRY RUN, THE MIRROR
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3')
SCORE_KEYS = NK + SK
_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
num_word = P3.num_word
_trail_defects, _trail_resolved = P3._trail_defects, P3._trail_resolved
LV = K.LV_DIR
IDENT_WORDS = ('psinary', 'seale', 'york', 'hotmail', 'orcid', 'secrets.')


def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _runner_rows():
    return dict((r.get('label'), r) for r in (jl('%s_runner_rows.json' % ACT).get('rows') or []))


def _n1():
    """N1, AS WORDED: no lean process on this host; THREE runner dispatches (the probe and the two entry-tag branches), each read by its run id with
    its artifact's sha256 verified. Scored as worded against the count printed: two dispatches (FACES_LEDGER :20 cites no tag, the navigator's (f))."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    rr = _runner_rows()
    pr = jl('%s_probe_run.json' % ACT)
    pv = jl('%s_prints_v0.17.json' % ACT)
    sha_ok = lambda s: re.match(r'^[0-9a-f]{64}$', s or '') is not None   # noqa: E731
    read_ok = all(sha_ok(r.get('artifact_sha256')) and r.get('run_id') for r in rr.values()) and len(rr) == len(dj) == 2 \
        and sha_ok((pr.get('artifact') or {}).get('sha256')) and sha_ok((pv.get('artifact') or {}).get('sha256')) \
        and sorted(d.get('run_id') for d in dj) == sorted([K.PROBE_RUN, K.PRINTS_RUN])
    three = len(dj) == 3 and len(cm.get('dispatches') or []) == 3
    ok = bool(cm) and not cm.get('local_lean') and read_ok and three
    return ('HELD' if ok else 'REFUTED'), (
        'as worded, on the count: dispatches banked %d (relay data/b708_dispatches.json: %s), in the capture %d (relay data/b708_commands.json) -- the expectation`s three '
        'counts a dispatch for FACES_LEDGER :20, which names no kernel and no tag (the navigator`s (f); b707`s tag-prints remainder line: no dispatch priced), so '
        'the count is two and the expectation as worded is %s; commands of this act that run lean or lake on this host: %s; each run read by its id with its '
        'artifact`s sha256 verified (relay data/b708_runner_rows.json: %s; the probe artifact %s, the prints artifact %s): %s' % (
            len(dj), ['%s %s at %s run %s whole %s' % (d.get('label'), (d.get('ref') or '')[:7], d.get('branch'), d.get('run_id'), d.get('whole')) for d in dj],
            len(cm.get('dispatches') or []) if cm else -1, 'REFUTED' if not three else 'met', cm.get('local_lean') if cm else 'unread',
            ['%s %s' % (k_, (r.get('artifact_sha256') or 'UNREAD')[:16]) for k_, r in rr.items()], ((pr.get('artifact') or {}).get('sha256') or '-')[:16],
            ((pv.get('artifact') or {}).get('sha256') or '-')[:16], read_ok))


def _n2():
    """N2: the probe step runs on the runner and its artifact is read (or its error banked and the order re-opened); no page line changes without a
    moved sig as its cause."""
    pr = jl('%s_probe_run.json' % ACT)
    pc = jl('%s_probe_compare.json' % ACT)
    page_ch = [x for x in (g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD', '--', K.FACES_PAGE) + NL + g(PP, 'diff', '--name-only', '--', K.FACES_PAGE)).split(NL) if x.strip()]
    ran = pr.get('step_ran') is True and pr.get('ok') is True and re.match(r'^[0-9a-f]{64}$', (pr.get('artifact') or {}).get('sha256') or '') is not None \
        and pr.get('missing') == [] and pr.get('cells') == pr.get('wanted') == 568
    moved = pc.get('moved') or []
    page_ok = (not moved and not page_ch) or (bool(moved) and bool(page_ch))
    ok = ran and page_ok and pc.get('compared') == 568
    return ('HELD' if ok else 'REFUTED'), (
        'the probe step on the runner (relay data/b708_probe_run.json): run %s, the step %s, the separate chain-probe artifact sha256 %s, cells %s of %s, missing %s; '
        'the probe against b704`s bank (relay data/b708_probe_compare.json): compared %s, equal %s, sigs moved %d %s; the faces page changed since %s: %s (a page line changes '
        'only with a moved sig as its cause: %s)' % (
            pr.get('run_id'), 'RAN' if pr.get('step_ran') else 'NOT RUN', ((pr.get('artifact') or {}).get('sha256') or '-')[:16], pr.get('cells'), pr.get('wanted'),
            pr.get('missing'), pc.get('compared'), pc.get('equal'), len(moved), moved[:6] or '', K.PRE_PP, page_ch or 'NONE', page_ok))


def _n3():
    """N3: the registrations bank committed at step zero and no eigenvalue computed this act; the listings of (9) printed before any branch or file
    clause was acted on, and no clause naming a file or branch the listing does not show."""
    files = [x for x in g(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.REG_COMMIT).split(NL) if x.strip()]
    reg_ct, c1_ct = _git_ct(ROOT, K.REG_COMMIT), _git_ct(ROOT, K.C1_RELAY)
    rj = jl('%s_registrations_reread.json' % ACT)
    rows = capture()
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lst = [r['ts'] for r in sh_ if re.search(r'branch\s+--merged', r['cmd'])]
    dels = [r['ts'] for r in sh_ if delete_shape(r['cmd'])[0]]
    onset_cmds = [r['n'] for r in sh_ if re.search(r'python[^\n|&;]*(b70\d_onset\.py|witness_balls\.py|witness_terms\.py)', r['cmd'])]
    before = bool(lst) and bool(dels) and min(lst) < min(dels)
    bb = jl('%s_branches_before.json' % ACT).get('rows') or []
    bj = jl('%s_branches.json' % ACT).get('rows') or []
    listed = set((r.get('repo'), r.get('branch')) for r in bb)
    named = set((r.get('repo'), r.get('branch')) for r in bj)
    in_listing = bool(named) and named <= listed
    ok = sorted(files) == ['data/b708_registrations.txt', 'data/b708_rules.txt'] and bool(reg_ct) and bool(c1_ct) and reg_ct < c1_ct and rj.get('unchanged') is True \
        and rj.get('no_eigenvalue') is True and not onset_cmds and before and in_listing
    return ('HELD' if ok else 'REFUTED'), (
        'the registrations` commit %s carrying %s alone at step zero, its time before Component 1`s %s: %s; re-read unchanged %s, no onset, units or eigenvalue bank of this act %s '
        '(relay data/b708_registrations_reread.json); commands running an onset or witness tool: %s; the listing `git branch --merged main` first at %s, the first delete at %s, '
        'the listing first: %s; every branch deleted among the branches listed before (relay data/b708_branches_before.json, %d rows; data/b708_branches.json, %d rows): %s' % (
            K.REG_COMMIT, files, K.C1_RELAY, bool(reg_ct) and bool(c1_ct) and reg_ct < c1_ct, rj.get('unchanged'), rj.get('no_eigenvalue'), onset_cmds or 'NONE',
            min(lst) if lst else '-', min(dels) if dels else '-', before, len(bb), len(bj), in_listing))


def _n4():
    """N4: the distance after the cut at or below the distance before; the quotation search run before the merge and its hit count printed; the
    mirror verifies CLEAN on all three clauses (read at the close where the mirror is not yet built: PENDING at the record)."""
    cj, qj = jl('%s_cut.json' % ACT), jl('%s_quote.json' % ACT)
    q_at = _iso_epoch((qj.get('at') or '')[:19] + 'Z') if qj.get('at') else None
    cut_ct = _git_ct(PP, K.C3_PP) if K.C3_PP else None
    m = re.search(r'QUOTING LINES (\d+) -- EACH ENTERED AS A RESIDUE', rdn('%s_quote.txt' % ACT))
    dist_ok = isinstance(cj.get('before'), int) and isinstance(cj.get('after'), int) and cj['after'] <= cj['before']
    quote_ok = bool(q_at) and bool(cut_ct) and q_at < cut_ct and bool(m) and int(m.group(1)) == len(qj.get('quoting') or []) == len(cj.get('residues') or [])
    mj = jl('%s_mirror.json' % ACT)
    mirror = mj.get('clean') if mj else None
    if mirror is None:
        v = 'PENDING'
    else:
        v = 'HELD' if (dist_ok and quote_ok and mirror is True) else 'REFUTED'
    return v, (
        'the distance by the b670 method (relay data/b708_cut.json): before %s, after %s, at or below %s; the quotation search (relay data/b708_quote.json) at %s, the cut`s commit '
        'PLACE-papers %s at %s, the search first %s, its hit count printed %s and equal to the residues entered %s; the mirror (relay data/b708_mirror.json): %s' % (
            cj.get('before'), cj.get('after'), dist_ok, qj.get('at'), K.C3_PP, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(cut_ct)) if cut_ct else '-',
            bool(q_at) and bool(cut_ct) and q_at < cut_ct, m.group(1) if m else '-', quote_ok,
            'not yet built (read at the close)' if mirror is None else ('CLEAN ON ALL THREE CLAUSES' if mirror else '### NOT CLEAN')))


def _n5():
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    ef_ok = ef_main == K.EF_MAIN and not g(EF, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    rh = R._remote_heads(EF)
    scratch_gone = not any(g(EF, 'branch', '--list', b).strip() or b in rh for b in (K.PROBE_BRANCH, K.PRINTS_BRANCH))
    lv_main, lv_dep = g(LV, 'rev-parse', 'main').strip(), g(LV, 'rev-parse', 'v0.10.0^{commit}').strip()
    lv_port = g(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH).strip()
    lv_ok = lv_main == K.LV_MAIN and lv_dep == K.LV_V0100 and lv_port == K.PORT_COMMIT and not [t for t in g(LV, 'tag', '--contains', K.PORT_COMMIT).split(NL) if t.strip()]
    join_main, join_tags = g(K.JOIN_DIR, 'rev-parse', 'main').strip(), g(K.JOIN_DIR, 'tag', '--list').strip()
    join_ok = join_main == K.JOIN_TIP and join_tags == ''
    allowed = set(K.PP_WRITTEN)
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in allowed]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b708_', x) and x[6:] not in R.N5_RELAY_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b708_|audit_b708_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in R.N5_RELAY_DATA) or (x.startswith('tools/') and x[6:] in R.N5_RELAY_TOOLS))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B707_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(EF, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_main = _show(EF, K.EF_MAIN, K.WORKFLOW) or ''
    pf = jl('%s_print_files_%s.json' % (ACT, K.PRINTS_BRANCH))
    wf_ok = bool(wf_main) and (pf.get('sha256') or {}).get(K.WORKFLOW) == hashlib.sha256(wf_main.encode('utf-8')).hexdigest() \
        and not any(w in wf_main.lower() for w in IDENT_WORDS)
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    deleted = sorted(x for d in (cj.get('delete_shapes') or []) for x in (d.get('deletes') or []))
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    ok = k_ok and ef_ok and scratch_gone and lv_ok and join_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ and arms_ok \
        and not amended and not ident and wf_ok and not chained and K.PORT_BRANCH not in deleted and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-explicit-formula`s main at badaccc, no tag past '
            'v0.37, the two scratch branches gone locally and at the remote: %s, %s; SIDE-lv-conservation`s main and deposit unmoved, port-b707 standing at its one commit, no tag '
            'past it: %s; the join kernel`s main at its manifest commit, no tag: %s; the standing arms added beyond b707`s face, the act arms apart: %s (%s); shared tools '
            'edited: %s; sealed tools not agreeing: %s; commits amended after the seal: %s; deletes with anything chained after: %s; port-b707 deleted: %s; one git write per '
            'message (%s): %s; PLACE-papers beyond the two ledgers and the named document: %s; papers moved or renamed: %s; relay files of a kind beyond the act`s banks and '
            'tools, the table, the root list, the corrigenda bank, b707`s push-out bank and tools/mirror_prevbuild.json: %s; the glossary unchanged: %s; outbound requests '
            'other than git and gh %d, an identifier of the author in %s; the workflow on the scratch branches main`s blob with no identifier: %s' % (
                K.DRAFT, k_ok, ef_ok, scratch_gone, lv_ok, join_ok, added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                chained or 'NONE', K.PORT_BRANCH in deleted, gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, len(ob),
                [r['line'] for r in ident] or 'NONE', wf_ok))


def scores(*a):
    """`scores [dry]` writes data/b708_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited (N4's mirror clause, S1, S2) into data/b708_scores_close.json."""
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
    return ('### b708 — lane two, act one hundred and thirty-five, the re-cut act under (R318): b707 at its weight; the faces chain probed through the '
            'workflow’s step at v0.37; the entry-tag prints complete; day1/Spectral_Inertness.md re-cut; the onset’s fine grid registered')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    pj, pr, pc = jl('%s_probe.json' % ACT), jl('%s_probe_run.json' % ACT), jl('%s_probe_compare.json' % ACT)
    pf, pv, cr = jl('%s_print_files_%s.json' % (ACT, K.PRINTS_BRANCH)), jl('%s_prints_v0.17.json' % ACT), jl('%s_cells_reread.json' % ACT)
    cj, qj, tj = jl('%s_cut.json' % ACT), jl('%s_quote.json' % ACT), jl('%s_tie.json' % ACT)
    pl, rr, sb = jl('%s_port_lines.json' % ACT), jl('%s_registrations_reread.json' % ACT), jl('%s_scratch_branches.json' % ACT)
    rows = cr.get('rows') or []
    fj_, f7 = jl('%s_standing_figures.json' % ACT), jl('b707_standing_figures.json')
    rr_ = _runner_rows()
    return dict(corr_line=co.get('entry_line', '-'),
                probe_sha=(pj.get('sha256') or '-')[:8], probe_equal=pj.get('equal_b704'), probe_cells=len(pj.get('cells') or []), probe_target=len((pj.get('target') or '').split()),
                probe_print_mods=len(pj.get('print_modules') or []), probe_mods=len(pj.get('probe_modules') or []),
                probe_run=pr.get('run_id'), step_ran=pr.get('step_ran'), probe_art=((pr.get('artifact') or {}).get('sha256') or '-')[:8], probe_read=pr.get('cells'), probe_want=pr.get('wanted'),
                probe_missing=len(pr.get('missing') or []), compared=pc.get('compared'), equal=pc.get('equal'), moved=pc.get('moved') or [],
                probe_gate=(rr_.get('probe') or {}).get('gate'), prints_gate=(rr_.get('prints_v0_17') or {}).get('gate'),
                prints_run=pv.get('run_id'), prints_tip=(pf.get('peel') or '-')[:7], prints_stmt=((pv.get('cell') or {}).get('statement') or '-'),
                prints_art=((pv.get('artifact') or {}).get('sha256') or '-')[:8], wf_equal=(pf.get('sha256') or {}).get(K.WORKFLOW) == hashlib.sha256((_show(EF, K.EF_MAIN, K.WORKFLOW) or '').encode('utf-8')).hexdigest(),
                mentions=len(rows), m_equal=sum(1 for r in rows if (r.get('verdict') or '').startswith('equal')), m_reread=sum(1 for r in rows if r.get('verdict') == 'equal'),
                m_differs=sum(1 for r in rows if r.get('verdict') == 'differs'), m_unbanked=sum(1 for r in rows if (r.get('verdict') or '').startswith('unbanked')),
                cut_doc=cj.get('document'), before=cj.get('before'), after=cj.get('after'), applied=sum(1 for r in (cj.get('rows') or []) if not r.get('held')),
                held=len(cj.get('held') or []), residues=len(cj.get('residues') or []), q_lines=len(qj.get('rows') or []), q_quoting=len(qj.get('quoting') or []),
                tie_top=tj.get('top'), tie_at_top=len(tj.get('at_top') or []), matches_lost=len(cj.get('matches_lost') or []),
                port_kinds=[(x.get('line'), x.get('kind')) for x in (pl.get('lines') or [])], port_unedited=pl.get('unedited'),
                reg_unchanged=rr.get('unchanged'), no_eigen=rr.get('no_eigenvalue'),
                scratch_gone=all(not r.get('local') and not r.get('remote') for r in (sb.get('rows') or [])) and len(sb.get('rows') or []) == 2,
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs7=dict((k, (f7.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


def _title():
    f = _figs()
    return ('## The faces chain probed through the workflow’s step at v0.37, %d sigs moved; the entry-tag prints complete, %d of %d mentions equal; '
            'day1/Spectral_Inertness.md re-cut: %s rows outside LICENSED/CITED to %s; the onset’s fine grid registered' % (
                len(f['moved']), f['m_equal'], f['mentions'], f['before'], f['after']))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) the ruling’s four misses entered by the fact clause and not raised -- “the falsifier HELD” (the bank: NOT FIRED, the hypothesis HELD), '
            '“four the navigator’s” (five by the bank), “main at its current tag” (main one commit past v0.37 by the workflow file alone; the branch cut '
            'from main, the modules’ tree the tag’s), “the tag each cites … one dispatch each” with N1’s three dispatches (FACES_LEDGER :20 cites none; one '
            'print dispatch, two in all) -- N1 scored as worded against the count, REFUTED; (2) the vendored lib’s module named by its srcDir, a carry-time '
            'repair of b705’s print-list reader (relay data/b708_tool_repairs.txt row (1)), the probe’s target 54 modules and the run printing 109 of 109; '
            '(3) the fine grid’s falsifier as worded vacuous on the grid as worded, entered for the strike with the discriminating reading beside it (a rung '
            'or a midpoint), the band’s grid priced at about 70 hours for b709’s ruling; (4) the four Correspondence cells of the cut document held (no cell '
            'by hand, the paper off the roster) and the title, opening labels and version line untouched; (5) G-READ-RULE-STANDING declared failing on (a)’s '
            'two whole reads, the arm unrepaired; (6) the report tool outside the sealed list until the root’s word (relay data/b708_rules.txt row (1)); (7) '
            'the citation check run twice, its own needle corrected before any delete, an event; (8) the %s navigator %s (%s) and the seat’s %s defect%s as lettered' % (
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
    kinds = '; '.join('%s %s' % (ln, k) for ln, k in f['port_kinds'])
    e = ['', _title(), '',
         'The re-cut act’s four objects read: the faces chain probed through the workflow’s own step -- the generator’s probe text (sha256 %s…, equal to '
         'b704’s, %d cells) run on a branch cut from main with the modules’ tree v0.37’s, the step RAN, its separate artifact read by run id and sha256, '
         '%d of %d cells read, %d sigs moved against b704’s bank, the page untouched; the entry-tag prints complete -- `simplicity_iff` printed at v0.17 '
         'and equal to its statement at v0.37, %d of %d mentions equal, %d unbanked by its own line; day1/Spectral_Inertness.md re-cut by the b670 method '
         'from %s rows outside LICENSED/CITED to %s, the quotation search before the cut’s commit entering %d quoting lines as residues; and the onset’s '
         'fine grid registered before any number and committed alone, computed at b709. The port’s next lines named by kind (%s), nothing edited.' % (
             f['probe_sha'], f['probe_cells'], f['probe_read'], f['probe_want'], len(f['moved']), f['m_equal'], f['mentions'], f['m_unbanked'], f['before'], f['after'],
             f['q_quoting'], kinds), '',
         '*Filed at b708 on the author’s ruling `(R318)`; %d question%s put before the root. Banks: relay `data/b708_probe.txt`, `data/b708_probe_diff.txt`, '
         '`data/b708_probe_run.txt`, `data/b708_probe_compare.txt`, `data/b708_print_files_prints-b708-v0.17.txt`, `data/b708_prints_v0.17.txt`, '
         '`data/b708_cells_reread.txt`, `data/b708_scratch_branches.txt`, `data/b708_tie.txt`, `data/b708_quote.txt`, `data/b708_cut.txt`, '
         '`data/b708_port_lines.txt`, `data/b708_registrations.txt`, `data/b708_registrations_reread.txt`, `data/b708_tool_repairs.txt`, '
         '`data/b708_repair_controls.txt`, `data/b708_standing_figures.txt`, `data/b708_corrigendum.txt`, `data/b708_report.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R318)`(1)-(2)): b707 entered at its weight as its closing prints (FINDINGS :%s), the onset figures’ reading beside it in the '
         'navigator’s words for the author’s strike; the generated entry at FINDINGS :%s answers b707’s post-seal item (i) -- the write list omitting the '
         'mirror builder’s state file -- and the three trail-equality arms broken by a defect lettered after the trail landed; the corrigenda bank appended '
         'at row (28); this act’s write list naming tools/mirror_prevbuild.json beside the zip and its stage; the report tool outside the sealed list until '
         'the root’s word (relay data/b708_rules.txt row (1)); the sealed face, the trail and the root-named banks of b707 unedited.' % (c1_[0], f['corr_line']), '',
         '**The probe** (`(R318)`(4), N2): W-ORD-WORKFLOW-PROBE-STEP’s trigger -- the branch probe-b708 cut from SIDE-explicit-formula’s main (badaccc, one '
         'commit past v0.37 by the workflow file alone; the navigator’s (e)), given the one root file ChainProbe.lean by the generator (relay '
         'tools/chain_page.py probe_text at the list of data/b704_nodes_zeta.txt, pin v0.37; sha256 %s…, equal to b704’s text, %d cells: the list’s '
         'nodes, the two candidates, the Correspondence names), the diff against main that one path; pushed alone in branch mode, dispatched once with '
         'the target print_targets.txt whole (109 names, their %d modules, the vendored lib’s named by its srcDir) joined with the probe’s %d module '
         'imports (%d in all); run %s DERIVES (109 of 109 printed, the artifact’s sha256 agreeing), the probe step RAN and its separate artifact '
         'chain-probe-%s read by name after its sha256 (%s…) agreed with the platform’s digest, %d of %d cells parsed, %d missing; diffed cell by cell '
         'against b704’s probe bank (run 39721668586 through the closure step): %d compared, %d equal, %d sigs moved; the page not regenerated; the '
         'branch deleted by name locally and at the remote after its bank’s commit, main and the tags untouched (relay data/b708_probe.txt, '
         'data/b708_probe_diff.txt, data/b708_probe_run.txt, data/b708_probe_compare.txt, data/b708_scratch_branches.txt).' % (
             f['probe_sha'], f['probe_cells'], f['probe_print_mods'], f['probe_mods'], f['probe_target'], f['probe_run'], f['probe_run'], f['probe_art'],
             f['probe_read'], f['probe_want'], f['probe_missing'], f['compared'], f['equal'], len(f['moved'])), '',
         '**The prints** (`(R318)`(5)): W-ORD-ENTRY-TAG-PRINTS’s remainder -- of the two mentions b706 left unbanked, SIMPLICITY_OF_RIEMANN_ZEROS :442 '
         'names the Prop `simplicity` at v0.17 = %s by `simplicity_iff`: the scratch branch prints-b708-v0.17 cut at the tag in (R316)(7)’s form with '
         'three files (the workflow main’s blob verbatim: %s; a one-name print list; a root ChainProbe.lean naming the theorem), pushed alone in branch '
         'mode, dispatched once, run %s DERIVES, its chain-probe artifact read after its sha256 (%s…) agreed: the statement at v0.17 `%s`, equal to the '
         'statement at v0.37; FACES_LEDGER :20 (the F1 row) names no kernel and no tag and stays unbanked by its own line (b707’s (e), this act’s (f)); '
         'the mentions %d: %d equal (%d carried from b706, %d re-read this act), %d differs, %d unbanked; the branch deleted after its bank, the tags '
         'untouched (relay data/b708_print_files_prints-b708-v0.17.txt, data/b708_prints_v0.17.txt, data/b708_cells_reread.txt).' % (
             f['prints_tip'], f['wf_equal'], f['prints_run'], f['prints_art'], ' '.join(f['prints_stmt'].split())[:200], f['mentions'], f['m_equal'],
             f['m_equal'] - f['m_reread'], f['m_reread'], f['m_differs'], f['m_unbanked']), '',
         '**The re-cut** (`(R318)`(6), N4): the licensed table’s next document by b652’s order (the kernels all at 0, the order passing to the companions), '
         'the top count %s with %d document at it, b674’s rule and data/b705_rules.txt row (2) not reached: %s, its table relay data/b646_table_Spectral_Inertness.txt '
         '(CLAIMS 116, MATCHES 92, OVERREACHES 14, UNLICENSED 8, UNDERSTATES 2), the document unmoved since its read (relay data/b708_tie.txt). The '
         'quotation search before the cut’s commit (data/b690_rules.txt row (2)): %d lines the cut changes, each with two needles, %d quoting lines across '
         'the tracked tree entered as residues (relay data/b708_quote.txt). The cut in a companion’s form by the b670 method: %d of the 24 non-MATCHES '
         'rows applied by the Edit tool on the rows alone, %d Correspondence cells held (no cell by hand, the paper off the roster), the title, opening '
         'labels and version line untouched, W-ORD-KEYSTONE-HEADS held; every MATCHES row standing (%d lost); the distance %s to %s (relay '
         'data/b708_cut.txt; PLACE-papers %s).' % (f['tie_top'], f['tie_at_top'], f['cut_doc'], f['q_lines'], f['q_quoting'], f['applied'], f['held'],
                                                   f['matches_lost'], f['before'], f['after'], K.C3_PP), '',
         '**The port** (`(R318)`(7)): port-b707’s next lines read from relay data/b707_port.txt and printed with their kinds -- C7OrderBounds.lean :277:55 '
         'a changed signature (`WeakFEPair.hasMellin` takes the hypothesis `k < re s` where `w` was given, the arguments re-ordered at Mathlib de5ce8a9), '
         ':380:8 a renamed Mathlib declaration (`exists_norm_completedRiemannZeta₀_le_exp_half` unknown to the kernel at the pin); port-b707 at its one '
         'commit locally and at the remote, unedited %s; the next dispatch at b709 (relay data/b708_port_lines.txt).' % f['port_unedited'], '',
         '**The registrations** (`(R318)`(3), N3): data/b708_registrations.txt written by the Write tool at step zero and committed alone at relay %s with '
         'data/b708_rules.txt before any computation of this act: the fine grid per family as the refinement of data/b705_registrations.txt (iii), nothing '
         'in (iii) changed -- the interval (a₊, a₋] from the onset bank (the band zero’s 2 log 128 to 2 log 192, ρ₀’s log 2 to 2 log 32) subdivided at '
         'the rungs log p^k in it and at the midpoints (ρ₀ 197 rungs, 395 points; the band 2026 rungs, 4053 points; derived counts, no eigenvalue), '
         'the quantity, hypothesis and falsifier in the ruling’s words, the falsifier as worded vacuous on the grid as worded and entered for the strike '
         'with the discriminating reading (the onset a rung or a midpoint), the controls (the coarse endpoints reproduced, the ζ form positive at every '
         'new point with its certified tail beside λ_min), the price by b707’s stamps (ρ₀ about 6–7 hours, the band about 70), computed at b709; re-read '
         'after Components 1–4 unchanged %s, no eigenvalue computed this act %s (relay data/b708_registrations_reread.txt).' % (K.REG_COMMIT, f['reg_unchanged'], f['no_eigen']), '',
         '**The standing arms**: the four figures at b708 -- %s, %s, %s, %s -- against b707’s %s, %s, %s, %s, read by b706’s tool over b706’s roster (relay '
         'data/b708_standing_figures.txt); G-READ-RULE-STANDING declared failing on (a)’s two whole reads; no standing arm added; the carry-time repair of '
         'b705’s print-list reader with its controls (relay data/b708_tool_repairs.txt, data/b708_repair_controls.txt).' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs7']['correspondence'], f['figs7']['readme'], f['figs7']['partners'], f['figs7']['pins']), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- every one the navigator’s, entered by the fact clause '
         '(“the falsifier HELD”; “four the navigator’s”; “main at its current tag”; “the tag each cites” with N1’s three dispatches), none raised; %d answer '
         'check%s before the root.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the four objects say one thing about the chain’s face -- what the page carries is what the '
         'runner prints, and the printing now runs inside the kernel’s own workflow: the probe through the step moved no sig against the closure run of '
         'b704, the tag print at v0.17 returned the statement v0.37 carries, and the companion’s rows outside its licence fell from %s to %s with every '
         'quoting line entered; the fine grid gives the onset’s question (a rung or a midpoint) a priced route. It strengthens the programme’s offering of '
         'a located clause by making the chain’s probe a step of the kernel’s build rather than a reading taken beside it.' % (f['before'], f['after']), '',
         '**Carried to:** b709 (the research act: the fine grid as data/b708_registrations.txt registers it, ρ₀’s family first or the band at its rungs '
         'alone for the ruling to name; the higher pairs’ route as data/b707_registrations.txt registers it; the port’s next dispatch on port-b707, '
         'C7OrderBounds.lean :277 and :380 first; the next axis (e)); b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5, the readfirst flip against readings 3 '
         'and 4); the next ruling (the five renames’ readers in the test files, no test edited this act; the fine grid’s falsifier as worded; the band’s '
         'grid price); the draft held at v5.', '',
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
             '**(R318) ratified.** (1) b707 at its weight. (2) The write list, the report tool and the corrigendum. (3) The fine grid registered. (4) The probe '
             'through the workflow’s step. (5) The entry-tag prints. (6) The re-cut. (7) The port’s lines held. (8) The branches. (9) The read-first bank. '
             '(10) The draft held at v5. (11) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b707’s weight with the onset reading), :%s (the corrigendum), :%s (the entry); day1/Spectral_Inertness.md re-cut '
             '(PLACE-papers %s); this record.' % (c1_[0], f['corr_line'], fj.get('entry_line'), K.C3_PP), '',
             '**Act root:** b708 `%s` (previous `%s`, b707’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b708_author_answers.txt); the root’s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The probe:** probe-b708 from main, ChainProbe.lean equal to b704’s text (%d cells), run %s, the step RAN, %d of %d cells read, %d sigs moved '
             'against b704’s bank, the page not regenerated, the branch deleted (relay data/b708_probe_compare.txt).' % (
                 f['probe_cells'], f['probe_run'], f['probe_read'], f['probe_want'], len(f['moved'])), '',
             '**The prints:** prints-b708-v0.17 at %s, run %s, `simplicity_iff` equal at v0.17 and v0.37; the mentions %d, equal %d, differs %d, unbanked %d '
             '(FACES_LEDGER :20 by its own line); the branch deleted (relay data/b708_cells_reread.txt).' % (
                 f['prints_tip'], f['prints_run'], f['mentions'], f['m_equal'], f['m_differs'], f['m_unbanked']), '',
             '**The re-cut:** day1/Spectral_Inertness.md, the distance %s to %s by the b670 method, %d rows applied, %d held, the quotation search before the '
             'cut’s commit with %d quoting lines entered as residues (relay data/b708_cut.txt, data/b708_quote.txt).' % (
                 f['before'], f['after'], f['applied'], f['held'], f['q_quoting']), '',
             '**The port:** port-b707 unedited at `%s`; :277:55 a changed signature, :380:8 a renamed Mathlib declaration; the next dispatch at b709 (relay '
             'data/b708_port_lines.txt).' % K.PORT_COMMIT[:7], '',
             '**The registrations:** the fine grid committed alone at relay %s before any computation, re-read unchanged %s, no eigenvalue computed %s; '
             'computed at b709 (relay data/b708_registrations.txt, data/b708_registrations_reread.txt).' % (K.REG_COMMIT, f['reg_unchanged'], f['no_eigen']), '',
             '**The kernels:** SIDE-explicit-formula’s two scratch branches cut, pushed, dispatched once each and deleted after their banks (gone %s), its '
             'main and tags unmoved; SIDE-lv-conservation’s port-b707 standing, unedited, its main and deposit unmoved; the join kernel unmoved; no lean or '
             'lake on this host.' % f['scratch_gone'], '',
             '**The mirror:** the export made after this root in the b670 form over b707’s roster, its name in the closing (relay data/b708_closing.txt).', '',
             '**The open orders:** `W-ORD-WORKFLOW-PROBE-STEP` (its trigger met: the chain’s next probe ran through the step, read in the entry); '
             '`W-ORD-ENTRY-TAG-PRINTS` (its remainder read to its end: SIMPLICITY :442 equal at v0.17, FACES_LEDGER :20 unbanked by its own line); '
             '`W-ORD-LV-FORWARD-PORT` (held: :277 and :380 named by kind, the next dispatch at b709); `W-ORD-LV-CLOSURE-JOIN` (the join held); '
             '`W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-STANDING-CLAUSES-BANK` (trigger b710); `W-ORD-KEYSTONE-HEADS` (held at this '
             're-cut); `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA` (read at b705); `W-ORD-E0-MET-CLASSK` (its content done at b705); '
             '`W-ORD-README-FIGURE-SCOPE` (repaired at b705). Discharged this act: none by a landing; entered this act: none.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b707’s %s, %s, %s, %s; G-READ-RULE-STANDING declared on the face as the carried '
             'failure on (a) (relay data/b708_standing_figures.txt, data/b708_read_calls.txt).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                 f['figs7']['correspondence'], f['figs7']['readme'], f['figs7']['partners'], f['figs7']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b708_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R318).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b708_citation_check.txt), step zero (data/b708_ferry.txt, data/b708_readfirst.txt, data/b708_stepzero.txt, '
         'data/b708_tests_stepzero.txt, data/b708_rowgen_stepzero.txt, data/b708_branches.txt, data/b708_tie.txt), the registrations and the rules bank committed alone '
         '(data/b708_registrations.txt, data/b708_rules.txt) ; N3 %s' % S['N3'][0],
         '### COMPONENT 1 : b707`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s (data/b708_corrigendum.txt, the corrigenda row (28))' % (c1_[0], f['corr_line']),
         '### COMPONENT 2 : the probe (data/b708_probe.txt, data/b708_probe_diff.txt, data/b708_probe_run.txt, data/b708_probe_compare.txt), run %s, %d sigs moved ; the prints '
         '(data/b708_print_files_prints-b708-v0.17.txt, data/b708_prints_v0.17.txt, data/b708_cells_reread.txt), run %s, %d of %d equal ; the scratch branches '
         '(data/b708_scratch_branches.txt) ; N1 %s ; N2 %s' % (f['probe_run'], len(f['moved']), f['prints_run'], f['m_equal'], f['mentions'], S['N1'][0], S['N2'][0]),
         '### COMPONENT 3 : the re-cut (data/b708_quote.txt, data/b708_cut.txt), %s to %s ; N4 %s' % (f['before'], f['after'], S['N4'][0]),
         '### COMPONENT 4 : the port`s lines (data/b708_port_lines.txt), unedited %s' % f['port_unedited'],
         '### COMPONENT 5 : the carry (data/b708_tool_repairs.txt, data/b708_repair_controls.txt), the figures (data/b708_standing_figures.txt), the registrations re-read '
         '(data/b708_registrations_reread.txt), the root route dry (data/b708_root_banks_dry.txt), the dry-run steps (data/b708_reg_gate.txt), the seal '
         '(data/b708_seal_hashes.json), the suite in seven parts, the per-part seconds (data/b708_arm_seconds.txt) ; S3 %s' % S['S3'][0],
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
    """b707's mbank carried with b708's names (the span line read from the mirror bank chain)."""
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
         '### THE ROSTER b707`S (70 entries, tools/mirror_roster.json unedited this act); the builder`s state file tools/mirror_prevbuild.json written at this build, named in (W) ((R318)(2)); files %d' % len(files_),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT)))
    for l in L[:10]:
        print(l[:240])


def guard(*a):
    """data/b708_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the writes
    by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b708_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b708_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b708_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b708_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b708_checks.py :%d `%s`,'
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


def scorercheck(*a):
    """a print only: the suite's G-SCORER-READS-BANKS reading over this tool's own source, each clause named; writes nothing."""
    import b708_checks as CH
    src = rd(os.path.join(T, 'b708_record.py'))
    n = ''.join(CH.strip_prose(CH._fn_src(src, f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = CH.strip_prose(CH._fn_src(src, 'scores'))
    ft = CH.strip_prose(CH._fn_src(src, '_finding_text'))
    m = re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n)
    print('  n %d chars ; _commands.json %s ; _dispatches.json %s ; _probe %s ; _cut %s ; ledger needle %r at %s' % (
        len(n), '_commands.json' in n, '_dispatches.json' in n, '_probe' in n, '_cut' in n, m.group(0) if m else None, n[max(0, m.start() - 80):m.end() + 40] if m else '-'))
    print('  sc isfile %s ; ft scores_line %s ; ft jl %s' % ("os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc, 'scores_line(S)' in ft, "jl('%s_scores.json' % ACT)" in ft))


def armnames(*a):
    """the suite's arm names in its order, for the face's (G2) block -- names alone, no source printed."""
    import b708_checks as CH
    names_ = [x[0] for x in CH.ARMS]
    st = set(_standing())
    print('  ARMS %d ; standing among them %d ; the act`s %d ; beyond both %s' % (
        len(names_), len(st & set(names_)), len(set(names_) & set(K.ACT_ARMS)), sorted(set(names_) - st - set(K.ACT_ARMS)) or 'NONE'))
    print('  standing not in the suite: %s' % (sorted(st - set(names_)) or 'NONE'))
    print('  act arms not in the suite: %s' % (sorted(set(K.ACT_ARMS) - set(names_)) or 'NONE'))
    print('  ACT_ARMS = %r' % (sorted(set(names_) - st),))
    for i in range(0, len(names_), 7):
        print('### ' + ' '.join('`%s`' % n for n in names_[i:i + 7]))


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks, c1=c1,
              scores=scores, components=components, findings=findings, trail=trail, drycheck=drycheck, mbank=mbank, guard=guard, armnames=armnames,
              figures=figures, repairs=repairs, repairctl=repairctl, regcheck=regcheck, scorercheck=scorercheck,
              scratch=scratch, portlines=portlines, quote=quote, cutbank=cutbank, quotecheck=quotecheck, probe=probe, probediff=probediff, runner=runner, probeview=probeview, probecompare=probecompare, tagstate=tagstate, printprobe=printprobe,
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
