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
    mods = _print_modules('D:/' + kernel, ref)
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


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, tie=tie)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b708_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
