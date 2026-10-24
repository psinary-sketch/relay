# -*- coding: utf-8 -*-
"""b710_record.py -- THE ACT'S RECORD TOOL, b710 under (R320).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b710 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route and its probe, tie, quote and cut forms, b705's routes (the print-list dispatch, the artifact reader),
### b706's (the runner choosing the run's artifact by name, the prints branch, the probe-step artifact, the mentions re-read) and b709's (the
### declared untracked writes, the root route's dry run, the rowgen roster re-pointed, the previous window in b701's form) are reached through
### tools/b709_record.py (sealed at b709 and unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### Written by the Write tool at b710 in stages: stage one, step zero's routes (the tie among them); Components 1-6 by the Edit tool.
### Routes: `python tools/b710_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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

import b710_worklist as K          # noqa: E402
import b709_worklist as K707       # noqa: E402  ### b709's data, for the controls on b709's banks
import b709_record as P7           # noqa: E402  ### b709's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4, b705's P5 and b706's P6 to b709: rebound below)
R, P3, P4, P5, P6 = P7.R, P7.P3, P7.P4, P7.P5, P7.P6   # ### b698's routes, b703's to b706's repaired readers, through b709's module

ACT, PREV = 'b710', 'b709'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b709 ran and closed in ANOTHER session (0be08567; this act opens c9e4ce2d after the author's /clear) -- b701's
# ### form: from b709's post-push combine in that session to that session's end (prev_capture below; a carry-time repair of b709's same-session bound)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b710_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b710_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b709_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('mirror_prevbuild.json',)   # ### (R320)(2): the mirror builder's own state file, written at every build

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b710_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b710_<name>`.
EXCLUDE_KINDS = P7.EXCLUDE_KINDS
# ### b709's declaration line read to its first space (b709: `\s*$`, which refused a declaration followed by prose and so read the grid's and the
# ### pairs' declarations as none -- the root's first dry run named 32 untracked units files); a name ending in `*` declares every file with that
# ### prefix (the grid's segment files, the pairs' band files). A carry-time repair, banked by diff (data/b710_tool_repairs.txt).
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b710_(\S+)', re.M)


def declared_untracked():
    """every b710_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b710_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [(re.escape(n[:-1]) + r'\S*') if n.endswith('*') else re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b710_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b710_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P7._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704 to b709


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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='b3213c0b' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S TO b709'S REPAIRED READERS, THROUGH b709'S MODULE
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
roster709 = P7.roster709                        # ### b707's rowgen roster re-pointed through data/b706_partners.json (the fourth path reader), through b709's module (a carry-time repair: the substitution shifted b709's own name for it)


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster b709's)
answers = R.answers


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (b709's roster707); each tool's verdict lines
    banked with its exit. data/b710_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    Ro = roster709()
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
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json, b709`s reader) ; the instruments: tools/rowgen/rowgen.py '
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R320)(8); b709's form)
def branches(*a):
    """`branches before`: data/b710_branches_before.json -- b698's route, carried (every branch (R320)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b710_branches.txt (.json) --
    each branch's fate read now against the tips banked before; the kept branch port-b707 read beside them."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b710_branches_before.json IS NOT WRITTEN -- NOTHING READ')
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
    L = ['%s -- STEP ZERO, (R320)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b710_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R320)(7) names relay`s four and PLACE-papers` two; port-b707 of',
         '### SIDE-lv-conservation is NOT deleted, local or remote, read beside them.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['  %-22s | %-28s | kept   | local %s ; remote %s ; %s' % (os.path.basename(krepo), kb, kept_local[:12] or 'absent', kept_remote[:12] or 'absent',
                                                                'STANDS' if kept_local == kept_remote == K.PORT_TIP else '### NOT AS KEPT')]   # ### a carry-time repair: b709's tip, K.PORT_TIP
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s ; port-b707 STANDS %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows),
        kept_local == kept_remote == K.PORT_TIP)]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[], kept=dict(repo=krepo, branch=kb, local=kept_local, remote=kept_remote)))
    print(NL.join(L[7:]))


# ================================================================================ THE READ BANK (b704's repaired route; the word's time the anchor's, from b705)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b710_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6, 'b709': P7}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
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
WF = getattr(K, 'WORKFLOW', '')   # ### a carry-time repair: no dispatch this act ((R320)(7)), the worklist names no workflow


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


# ================================================================================ THE LATE ROUTES (b709's, carried with b710's names; the previous window in its own session)
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
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (b709's carry-time repair, carried): b709's
    capture AFTER ITS POST-PUSH SUITE -- every command of session 0be08567 from the call that combined b709's post-push parts into
    data/b709_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
    rows = ER.capture(PREV_SESSION_PATH, K.PREV_ANCHOR, PREV_SUBAGENTS)
    first = [r['ts'] for r in rows if '%s_checks_postpush' % PREV in r['cmd'] and '--combine' in r['cmd']]
    if not first:
        sys.exit('### THE PREVIOUS ACT`S POST-PUSH COMBINE IS NOT IN ITS SESSION`S CAPTURE -- NOTHING READ')
    anchor = '9999'   # ### b710's carry-time repair: the previous act ran in ITS OWN session (b709 bounded it at this act's anchor, b700's same-session form), so its window runs to that session's end (b701's form)
    out = [dict(r, src='%s %s' % (PREV, r['src'])) for r in rows if first[0] <= r['ts'] < anchor]
    for i, r in enumerate(out):
        r['n'] = 'p%d' % (i + 1)
    return out


R.prev_capture = prev_capture
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
# ### b709's pattern read `_record.py dispatch`; this act's one dispatch ran through the `portdispatch` route, so the pattern takes the port prefix too
# ### (a carry-time repair, banked by diff: the command bank's first write read DISPATCHES 0 against the dispatch bank's one row)
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b709's route with b710's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b709's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (two ordered: the probe branch and the prints
    branch), the detached runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests.
    data/b710_commands.txt (.json)."""
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
    L += ['', '### THE RUNNER DISPATCHES (one ordered this act, N1: the port branch of SIDE-lv-conservation at its tip, through the portdispatch route) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R320)(8) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    print('  kernels read: %d (SIDE-faces-join among them; no kernel main written this act; SIDE-lv-conservation`s port-b707 at this act`s one commit, its checkout at main for this read)' % len(ks))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B709_FACE.split('/')))) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))   # ### a carry-time repair: the previous face b709's (the upper-case name the substitution left)


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
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b710_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b710_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ STEP ZERO: THE LICENSED TABLE'S NEXT DOCUMENT, (R320)(6) (b704's tie form)
SUMMARY = re.compile(r'### ### \*\*(\w+): CLAIMS (\d+) ; SKIPPED LINES (\d+) ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+)')


def tie(*a):
    """data/b710_tie.txt: (R320)(6), the licensed table's next document -- b652's order, b674's tie-break rule and data/b705_rules.txt row (2)
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
    L = ['%s -- STEP ZERO, (R320)(6): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER, b674`S TIE-BREAK RULE AND b705`S ROW (2) PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
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
            L.append('    (ii) a declared suite failure on either document: NONE (no arm of b709`s suite names either; data/b709_checks.txt)')
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


# ================================================================================ COMPONENT 2: THE PROBE THROUGH THE WORKFLOW'S STEP, (R320)(4)
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
    """b705's _print_modules (tools/b705_record.py :732) with the carry-time repair of this act (data/b710_tool_repairs.txt row (1)): a hit under a
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


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b706's runner706 carried with b710's names -- the run's artifact chosen BY NAME
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


# ================================================================================ COMPONENT 5: THE CARRY-TIME REPAIR AND ITS CONTROLS
# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, against b709`s baselines)
def figures(*a):
    """data/b710_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited (correspondence() and partners()
    over b706's roster, data/b706_roster_read.json; readme() b705's, pins() b703's), each against b709's figure (data/b709_standing_figures.json),
    the pins baseline b709's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b709_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b710, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b709`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b709_standing_figures.json). No document is cut this act; day1/Spectral_Inertness.md (cut at b709) is off the roster;',
         '### both kernels on main at the read (SIDE-lv-conservation`s checkout restored to main from port-b707 before this read, b707`s trap).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b710 %s ; b709 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b710: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b709`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', baseline='b709_standing_figures.json',
                                                        **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


def linecheck(*a):
    """`linecheck <record-lines bank> <i> <needle>...`: the suite's landed-line reading (tools/b703_checks.py landed) reproduced piece by piece and
    printed -- the bank's row, the ledger line at its number through the suite's own reader, conv(head), startswith and each needle; print only."""
    import b710_checks as CH
    bank, i = a[0], int(a[1])
    need = list(a[2:])
    rl = jl(bank)
    x = (rl.get('lines') or [])[i]
    find = CH.read(os.path.join(CH.PP, 'FINDINGS.md'))
    ot_ = CH.read(os.path.join(CH.PP, 'OPEN_TRAILS.md'))
    S_ = dict(find=find, ot=ot_)
    o = (CH.fline if x.get('file') == 'FINDINGS.md' else CH.oline)(S_, x.get('line'))
    h = conv(x.get('head', '\x00'))
    print('  row %d: file %s line %s ; the ledger text %d lines, %d chars' % (i, x.get('file'), x.get('line'), len(find.split(NL)), len(find)))
    print('  the line at that number (%d chars): %r' % (len(o), o[:160]))
    print('  conv(head) (%d chars): %r' % (len(h), h[:160]))
    print('  startswith %s ; first differing index %s' % (o.startswith(h), next((k for k in range(min(len(o), len(h))) if o[k] != h[k]), None)))
    for n_ in need:
        print('  needle %r in the line: %s' % (n_, n_ in o))
    if os.environ.get('LINECHECK_SUITE') == '1' or 'suite' in a:
        S = CH.sources(())
        xs = (S['rl'].get('lines') or [{}])[i]
        os_ = CH.fline(S, xs.get('line')) if xs.get('file') == 'FINDINGS.md' else CH.oline(S, xs.get('line'))
        print('  THE SUITE`S SOURCES: rl row %s ; find %d chars ; the line at its number (%d chars): %r' % (xs, len(S['find']), len(os_), os_[:120]))
        print('  CH.landed(S, %d, need) %s ; CH.weight_ok(S) %s' % (i, CH.landed(S, i, [n_ for n_ in need if n_ != 'suite']), CH.weight_ok(S)))


def defs(*a):
    """`defs <tool.py>`: the tool's top-level def names with their lines (print only) -- the span finder for a read by offset and limit."""
    src = rd(os.path.join(T, a[0])).split(NL)
    for i, l in enumerate(src, 1):
        if l.startswith('def ') or l.startswith('class ') or l.startswith('# ====='):
            print('  :%d %s' % (i, l[:100]))


def ksyms(*a):
    """`ksyms <tool.py>`: the worklist attributes a carried tool names as K.<NAME>, each with its lines, and which this act's worklist lacks --
    the carry's reading of what the previous act's objects were (print only, no bank)."""
    src = rd(os.path.join(T, a[0])).split(NL)
    seen = {}
    for i, l in enumerate(src, 1):
        for m in re.finditer(r'\bK\.([A-Z_0-9]+)', l):
            seen.setdefault(m.group(1), []).append(i)
    missing = sorted(n for n in seen if not hasattr(K, n))
    for n in sorted(seen):
        print('  %-28s %s lines %s' % (n, '### MISSING' if n in missing else 'present   ', seen[n][:12]))
    print('### ### **K.<NAME> REFERENCES %d ; MISSING FROM b710_worklist %d: %s.**' % (len(seen), len(missing), missing or 'NONE'))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R320)(1)-(2)
WH = ('*Appended 2026-10-24 by b710 to b709’s entry (:10198), under `(R320)`(1) -- b709 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b709_closing.txt):*')
RH = ('*Appended 2026-10-24 by b710 beside b709’s weight line, under `(R320)`(2) -- THE READINGS OF b709’S FIGURES, IN THE NAVIGATOR’S WORDS, '
      'FOR THE AUTHOR’S STRIKE (relay data/b710_ferry.txt, (R320)(2)):*')


def _fig(text, pat, what):
    m = re.search(pat, text)
    if not m:
        sys.exit('### b709`S BANKS DO NOT CARRY %s (%s) -- NOTHING COMPOSED' % (what, pat))
    return m.groups() if m.groups() else (m.group(0),)


def _declared_b709():
    face = rd(os.path.join(ROOT, *K.B709_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    return sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []


def _failing_b709():
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', rdn('b709_checks_postpush.txt'))
    return [x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip()]


def _pairs_steps():
    """the ten computed pairs of data/b709_pairs.txt in the order of height, and the pairs whose ratio is below the next-lower pair's."""
    rows = []
    for l in rdn('b709_pairs.txt').split(NL):
        m = re.match(r'^\s+(\d+) \| \[\S+ \+ \[(\S+) i \|.*\| n\*/predicted \[(\S+) \+/- \S+\] \| WITHIN', l)
        if m:
            rows.append((int(m.group(1)), float(m.group(2)), float(m.group(3))))
    rows.sort(key=lambda x: x[1])
    return rows, [(b[0], a[0]) for a, b in zip(rows, rows[1:]) if b[2] < a[2]]


def _wb():
    """b709's weight line, its figures read from b709's banks by line: the head from the closing :1, the grid and the zeta control from the
    report (:16-:17), the pairs from their bank, the port from its bank, the root from the act-root bank and the chain, the scores from the
    scores banks, the suite from the post-push bank and the face, the defects from the defects bank by the repaired reader."""
    c = rdn('b709_closing.txt')
    head = c.split(NL)[0]
    rp, pb, pt = rdn('b709_report.txt'), rdn('b709_pairs.txt'), rdn('b709_port.txt')
    decl, fails = _declared_b709(), _failing_b709()
    post = [a for a in fails if a not in decl]
    sr, sc = jl('b709_scores.json'), jl('b709_scores_close.json')
    short = _defect_short('b709')
    if decl != ['G-READ-RULE-STANDING'] or sorted(post) != ['G-AXIS-REGISTERED', 'G-REPORT-UNSEALED'] or len(short) != 8 \
            or not head.startswith('b709 closed: relay 8b842c9a, PLACE-papers 07978f3; suite 144 of 147'):
        sys.exit('### b709`S FACE OR ITS BANKS NOT AS READ (declared %s ; post %s ; defects %d ; head %s) -- NOTHING COMPOSED' % (decl, post, len(short), head[:40]))
    a_b, lam_b = _fig(rp, r'the rung log 32381 \(32381\^1\) at a = ([0-9.]+) \+- \S+, lambda_min (\S+) \+-', 'the band onset')
    lo_b, hi_b = _fig(rp, r'the nearest entering rungs log (\d+) \(40 points below\) and log (\d+) \(8 points above\)', 'the band rungs')
    a_r, lam_r = _fig(rp, r'the midpoint between log 929 and log 937 at a = ([0-9.]+) \+- \S+, lambda_min (\S+) \+-', 'the rho_0 onset')
    zb, zr = _fig(rp, r'every point of both families \((\d+) of \d+ and (\d+) of \d+\)', 'the zeta points')
    c1n, = _fig(rdn('b709_grid.txt'), r'(C1 AS WANTED True)', 'the coarse rows')
    bands = len(re.findall(r'^  band \[.*\| COMPLETE\s*$', pb, re.M))
    on, off = _fig(pb, r'new on-line zeros (\d+) ; new off-line pairs (\d+)', 'the extension')
    comp, wi, out, br = _fig(pb, r'pairs computed (\d+), within (\d+), outside (\d+)\s+; beyond reach (\d+)', 'the falsifier')
    rows, steps = _pairs_steps()
    run, = _fig(pt, r'RUN (\d+) \(port\)', 'the port run')
    built, of = _fig(pt, r'MODULES BUILT (\d+) OF (\d+)', 'the modules')
    ar = jl('b709_act_root.json')
    banks, = _fig(rdn('b709_root_banks.txt'), r'BANKS (\d+) ; CLEAN AND EQUAL AT HEAD', 'the root banks')
    files, = _fig(rdn('b709_mirror.txt'), r'entries in the zip \d+ \(files (\d+) \+ MANIFEST\)', 'the mirror files')
    agree, of_a = _fig(c, r'### AGREE (\d+) of (\d+)', 'the sealed hashes')
    cites, ok, miss = _fig(c, r'CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', 'the citation check')
    lg, = _fig(rp, r'(EQUAL True) -- the bank stands at its committed bytes', 'the lock-gate bank')
    sv = lambda J, k: (J.get(k) or ['-'])[0]   # noqa: E731
    return (' “%s” (data/b709_closing.txt :1); the closing commit 42dd8768 pushed alone in main mode after the line was written and read back '
            'equal at the remote (data/b709_closing_push_out.txt :5). The fine grid (data/b709_grid.txt): the band zero’s onset at the rung log 32381, '
            'a = %s, λ_min %s, a rung where Λ_Q vanishes, between the entering rungs log %s and log %s; ρ₀’s onset at the midpoint between log 929 and '
            'log 937, a = %s, λ_min %s; the ζ form positive at all %d points (the band %s, ρ₀ %s) with its certified tail balls beside λ_min; the coarse '
            'endpoints reproducing b707’s 32 rows exactly (%s); the registered hypothesis and falsifier printed vacuous as worded per family '
            '(data/b709_report.txt :16-:17). The pairs (data/b709_pairs.txt): the certified list of Q0’s zeros extended from height 150 to 325 in %d '
            'closed bands (%s new on-line zeros, %s new off-line pairs); %s of 12 pairs computed and %s within [0.67, 1.5], %s outside, the ratios %.4f '
            'to %.4f, rising with height as a trend over the ten and not at every step -- in the order of height %s stand below the next-lower pair’s '
            'ratio (the fact clause on the quotation, relay data/b710_citation_check.txt); pairs 11 and 15 beyond reach at 325 (needing 405.4 and '
            '442.3), W-ORD-Q0-ZEROS-443 at OPEN_TRAILS :15764. The port at port-b707 = 92af8a34, one edit at C7OrderBounds.lean :277, one dispatch '
            '(run %s), %s of %s modules building, DirichletC7Order.lean :212:55 the next line with the same changed signature, nothing merged or '
            'tagged (data/b709_port.txt). The axis (e) representation coordinates registered for b711 (data/b709_registrations.txt, relay '
            '510dc29b). b378’s lock-gate bank overwritten by a call without its argument and restored byte-equal, shown so before the root '
            '(data/b709_report.txt :4-:7, %s; defect (h)). The entry at FINDINGS :10198, the trail at OPEN_TRAILS :15766; the root b3213c0b over %s '
            'banks chained from %s (data/b709_act_root.json, data/b709_root_banks.txt), the chain b624–b709 AGREE; the mirror '
            'mirror-refresh-2026-10-23-b709.zip CLEAN on all three clauses over %s files with the root line (data/b709_mirror.txt); suite 144 of '
            '147 pre-push and post-push, %s declared on the face and %s failing after the seal on their own needles (data/b709_checks.txt, '
            'data/b709_checks_postpush.txt; answered by this act’s corrigendum and repaired at this act’s carry under `(R320)`(3)); N1 %s and N3 %s '
            'as worded, N2 %s and N4 %s, N5 %s at the record and %s at the close, S1 %s, S2 %s, S3 %s (data/b709_scores.json, '
            'data/b709_scores_close.json); the sealed tools’ hashes equal at the close, %s of %s; the citation check %s cites, %s OK, %s missed, the '
            'seat’s; eight defects (a)–(h), every one the seat’s (data/b709_defects.txt), the two post-seal needles beneath them unlettered; '
            '“1 prompt answered” the root’s prompt alone. Nothing deposited.' % (
                head, a_b, lam_b, lo_b, hi_b, a_r, lam_r, int(zb) + int(zr), zb, zr, c1n, bands, on, off, comp, wi, out,
                min(r[2] for r in rows), max(r[2] for r in rows), ', '.join('pair %d below pair %d' % s for s in steps) or 'none',
                run, built, of, lg, banks, (ar.get('previous') or '')[:8], files, ', '.join(decl), ' and '.join(sorted(post)),
                sv(sr, 'N1'), sv(sr, 'N3'), sv(sr, 'N2'), sv(sr, 'N4'), sv(sr, 'N5'), sv(sc, 'N5'), sv(sc, 'S1'), sv(sc, 'S2'), sv(sr, 'S3'),
                agree, of_a, cites, ok, miss))


def _readings():
    """(R320)(2) verbatim from the banked ferry (data/b710_ferry.txt), the navigator's words, entered beside the weight line for the strike."""
    f = rdn('b710_ferry.txt').split(NL)
    p2 = [l for l in f if l.startswith('(2) THE READINGS OF b709’S FIGURES')]
    if len(p2) != 1:
        sys.exit('### (R320)(2) NOT FOUND ONCE IN THE BANKED FERRY -- NOTHING COMPOSED')
    body = p2[0].split(': ', 1)[1].rstrip('.')
    return (' %s (data/b710_ferry.txt :%d). Beside reading (ii), by the fact clause: the rise is a trend over the ten pairs, four of them below the '
            'next-lower pair’s ratio (data/b710_citation_check.txt), and the refined form is registered at relay data/b710_registrations.txt (i) with '
            'its constants fitted from b709’s banked pairs alone, beta = 7.997097 against the route’s own 8 (data/b710_fit.txt).' % (body, f.index(p2[0]) + 1))


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL), ('FINDINGS.md', RH, NL + RH + _readings() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B709_ENTRY,
         check=[('FINDINGS.md', K.B709_ENTRY, '## The sign-onset radius at the Epstein zeta'), ('OPEN_TRAILS.md', K.B709_TRAIL, '### b709')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE REPAIRS' CONTROLS, (R320)(3)
def _data_state():
    """every file directly under relay data/: its size and its mtime -- the lock gate's NEG control reads it before and after."""
    out = {}
    for f in os.listdir(D):
        p = os.path.join(D, f)
        if os.path.isfile(p):
            st = os.stat(p)
            out[f] = (st.st_size, st.st_mtime_ns)
    return out


def _gate_call(*args):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b378_lockgate.py')] + list(args), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', cwd=ROOT, timeout=120)
    return r.returncode, ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')


def repairctl(*a):
    """data/b710_repair_controls.txt (.json), Component 1, (R320)(3): the four repairs against their old forms. (1) G-REPORT-UNSEALED's key read
    case-insensitively (tools/b710_checks.py keys_ci) on b709's report bank (data/b709_report.txt), the bank the sealed needle failed on, and on a
    NEG copy with every `ratio` removed; (2) G-AXIS-REGISTERED's quotation read after joining wrapped lines (joined) on b709's registrations bank
    and a NEG copy with the quotation's words changed; (3) the lock gate without its argument: exit 2 and relay data/ unchanged file for file,
    an empty argument the same, the POS call with an act whose face is absent passing the argument's check and refusing at the face, nothing
    written, b378's tracked bank equal to HEAD; (4) the test that ran lean: its run at step zero (data/b710_tests_stepzero.txt), the process
    listing after its part, and its text carrying no call of the reader's lean route."""
    import types
    src_ck = rd(os.path.join(T, 'b710_checks.py'))
    ns = {}
    for fn_name in ('keys_ci', 'joined'):   # ### the repaired forms as they stand in the suite's text (the suite's act sections are rewritten at Component 5)
        exec(compile(R._fn_src(src_ck, fn_name), 'tools/b710_checks.py:' + fn_name, 'exec'), ns)
    CH = types.SimpleNamespace(keys_ci=ns['keys_ci'], joined=ns['joined'])
    rows, allok = [], True

    def case(name, got, want):
        nonlocal allok
        ok = got == want
        allok = allok and ok
        rows.append(dict(case=name, got=got, wanted=want, as_wanted=ok))

    keys = ('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')
    rep = rdn('b709_report.txt')
    case('(1) the old needle on b709`s report bank (every key in capitals, case-sensitive)', all(k in rep for k in keys), False)
    case('(1) the repaired needle (keys_ci) on b709`s report bank', CH.keys_ci(rep, keys), True)
    neg1 = re.sub('(?i)ratio', 'quotient', rep)
    case('(1) NEG: the repaired needle on a copy with every `ratio` removed, any case', CH.keys_ci(neg1, keys), False)
    q = '(e) representation coordinates (the operator / Toeplitz form) -- 4'
    reg, rk = rdn('b709_registrations.txt'), rdn('b705_i6_ranking.txt').split(NL)[57]
    case('(2) the old needle on b709`s registrations bank (the quotation as one string)', q in reg, False)
    case('(2) the repaired needle (joined) on b709`s registrations bank', q in CH.joined(reg), True)
    case('(2) the repaired needle on data/b705_i6_ranking.txt :58 (the quotation on one line)', q in CH.joined(rk), True)
    case('(2) NEG: the repaired needle on a copy with "Toeplitz" changed to "Hankel"', q in CH.joined(reg.replace('Toeplitz', 'Hankel')), False)
    other = ('(e) REPRESENTATION COORDINATES', 'THE STATEMENT-GRADE RE-EXPRESSION', 'HYPOTHESIS:', 'FALSIFIER:', 'CONTROLS, printed before any figure',
             '(C1)', '(C2)', '(C3)', 'THE PRICE (DERIVED', 'COMPUTED AT b711', 'the second row :58', 'ITS LEAST EIGENVALUE lambda_min(a, N) IS THE SIGN')
    case('(2) the arm`s other needles on b709`s registrations bank, joined', all(x in CH.joined(reg) for x in other), True)
    before = _data_state()
    lg_before = g(ROOT, 'diff', 'HEAD', '--', 'data/b378_lockgate.json')
    rc0, out0 = _gate_call()
    rc1, out1 = _gate_call('')
    rc2, out2 = _gate_call('b710')
    after = _data_state()
    changed = sorted(f for f in set(before) | set(after) if before.get(f) != after.get(f))
    lg_after = g(ROOT, 'diff', 'HEAD', '--', 'data/b378_lockgate.json')
    case('(3) NEG: the lock gate with no argument exits 2 printing its usage', (rc0, 'the act argument is required' in out0), (2, True))
    case('(3) NEG: the lock gate with an empty argument exits 2 printing its usage', (rc1, 'the act argument is required' in out1), (2, True))
    case('(3) POS: with an act (b710, its default face absent) the gate passes the argument`s check and refuses at the face, exit 2',
         (rc2, 'THE FACE DOES NOT EXIST' in out2, 'the act argument is required' in out2), (2, True, False))
    case('(3) relay data/ unchanged file for file across the three calls (size and mtime)', changed, [])
    case('(3) b378`s tracked bank data/b378_lockgate.json equal to HEAD before and after', (lg_before.strip(), lg_after.strip()), ('', ''))
    tj = jl('b710_tests_stepzero.json')
    trow = next((r for r in (tj.get('rows') or tj.get('tests') or []) if (r.get('file') or r.get('name')) == 'test_elab_reader_b634.py'), {})
    tz = rdn('b710_tests_stepzero.txt')
    tl = next((l for l in tz.split(NL) if l.strip().startswith('test_elab_reader_b634.py')), '')
    src = rd(os.path.join(T, 'test_elab_reader_b634.py'))
    case('(4) the repaired test at step zero: exit 0, 7 of 7 (data/b710_tests_stepzero.txt)', ('exit 0' in tl and '7 of 7 cases as wanted -- PASS' in tl), True)
    case('(4) its text carries no call of the reader`s lean route (`EL.call(` absent; `EL.call = _refuse` present)', ('EL.call(' not in src, 'EL.call = _refuse' in src), (True, True))
    sz = rdn('b710_stepzero.txt')
    case('(4) the process listing after its part: lean 0, lake 0, python 0 (data/b710_stepzero.txt)', 'lean 0, lake 0, python 0' in sz and '22:08:15Z' in sz, True)
    L = ['%s -- COMPONENT 1, (R320)(3): THE TWO NEEDLES, THE LOCK GATE AND THE TEST AGAINST THEIR OLD FORMS, WITH THEIR CONTROLS (%s)' % (ACT, utc()), '',
         '### rows are cases: the case | the reading got | the reading wanted | AS WANTED. The banks the old needles failed on after b709`s seal:',
         '### relay data/b709_report.txt (G-REPORT-UNSEALED) and data/b709_registrations.txt :12-:13 (G-AXIS-REGISTERED); the repaired forms',
         '### tools/b710_checks.py keys_ci and joined. The lock gate: tools/b378_lockgate.py, the argument required (its main); the test:',
         '### tools/test_elab_reader_b634.py, the banked prints data/b710_elab_reader_print.txt and data/b710_elab_reader_print_sec.txt.', '']
    L += ['  %-118s | got %-24s | wanted %-24s | %s' % (r['case'][:118], str(r['got'])[:24], str(r['wanted'])[:24], 'AS WANTED' if r['as_wanted'] else '### NOT AS WANTED') for r in rows]
    L += ['', '### the lock gate`s three calls, their first lines: none %r ; empty %r ; b710 %r' % (out0.strip().split(NL)[0][:90], out1.strip().split(NL)[0][:90],
                                                                                              [l.strip() for l in out2.split(NL) if 'THE FACE DOES NOT EXIST' in l][:1])]
    L += ['', '### ### **CASES %d ; AS WANTED %s ; THE REPAIRED NEEDLES PASS ON b709`S BANKS AND THEIR NEG COPIES FAIL ; THE LOCK GATE WITHOUT ITS ARGUMENT WRITES NOTHING ; THE TEST RUNS NO LEAN.**' % (
        len(rows), allok)]
    if 'dry' not in a:
        put_txt('%s_repair_controls.txt' % ACT, L)
        put_json('%s_repair_controls.json' % ACT, dict(at=utc(), cases=rows, as_wanted=allok, changed=changed))
    print(NL.join(L[6:]))
    if not allok:
        sys.exit(1)


def _fn_diff(old_src, new_src, name, a_name, b_name):
    import difflib
    o = (R._fn_src(old_src, name) or '').split(NL)
    n = (R._fn_src(new_src, name) or '').split(NL)
    return ['    ' + l for l in difflib.unified_diff(o, n, a_name, b_name, lineterm='', n=1)]


CARRY_ROWS = []   # ### the carry-time repairs of Component 5, appended by the Edit tool at Component 5


def toolrepairs(*a):
    """data/b710_tool_repairs.txt: the repairs of (R320)(3) with their diffs and controls -- (1) G-REPORT-UNSEALED's key case-insensitive, (2)
    G-AXIS-REGISTERED's bank joined (each the function's diff, b709's sealed form against tools/b710_checks.py's, and the helper added), (3) the
    lock gate's argument required (`git diff HEAD` of tools/b378_lockgate.py), (4) the test reading banked prints (`git diff HEAD` of
    tools/test_elab_reader_b634.py); the controls data/b710_repair_controls.txt by row. At Component 5 the carry-time repairs are added as rows."""
    old, new = rd(os.path.join(T, 'b709_checks.py')), rd(os.path.join(T, 'b710_checks.py'))
    ctl = jl('%s_repair_controls.json' % ACT).get('cases') or []
    cl = lambda p: ['      control: %s -- %s' % (c['case'], 'AS WANTED' if c['as_wanted'] else '### NOT AS WANTED') for c in ctl if c['case'].startswith(p)]   # noqa: E731
    L = ['%s -- THE REPAIRS OF (R320)(3) AND THE CARRY-TIME REPAIRS, EACH WITH ITS DIFF AND ITS CONTROL (%s)' % (ACT, utc()), '',
         '### rows are repairs: the tool and its part ; what it answers ; the diff ; the controls (data/b710_repair_controls.txt). No sealed tool of',
         '### an earlier act is edited; the two shared tools edited are the ruling`s ((R320)(3)), named in (W).', '',
         '  (1) tools/b710_checks.py report_unsealed_ok and keys_ci -- (R320)(3): G-REPORT-UNSEALED`s key read case-insensitively (b709`s arm wanted',
         '      RATIO in capitals; its report printed "the twelve ratios"; data/b709_defects.txt :117-:122).']
    L += _fn_diff(old, new, 'report_unsealed_ok', 'tools/b709_checks.py', 'tools/b710_checks.py') + ['    + (the helper keys_ci added beside it)'] + cl('(1)')
    L += ['', '  (2) tools/b710_checks.py axis_registered_ok and joined -- (R320)(3): G-AXIS-REGISTERED reading the registrations bank after joining',
          '      wrapped lines (b709`s bank wraps the quotation across :12-:13; data/b709_defects.txt :123-:129).']
    L += _fn_diff(old, new, 'axis_registered_ok', 'tools/b709_checks.py', 'tools/b710_checks.py') + ['    + (the helper joined added beside it)'] + cl('(2)')
    L += ['', '  (3) tools/b378_lockgate.py main -- (R320)(3): the act argument required, a call without it exiting before any write (b709`s (h)).']
    L += ['    ' + l for l in g(ROOT, 'diff', 'HEAD', '--', 'tools/b378_lockgate.py').rstrip(NL).split(NL)] + cl('(3)')
    L += ['', '  (4) tools/test_elab_reader_b634.py -- (R320)(3): the test reading lean`s banked prints and invoking no lean (b709`s (c), its calls at',
          '      :34 and :65); the prints data/b710_elab_reader_print.txt and data/b710_elab_reader_print_sec.txt (blobs 55277c74, ef99e5c3).']
    L += ['    ' + l for l in g(ROOT, 'diff', 'HEAD', '--', 'tools/test_elab_reader_b634.py').rstrip(NL).split(NL)] + cl('(4)')
    L += CARRY_ROWS
    ok = bool(ctl) and all(c['as_wanted'] for c in ctl)
    L += ['', '### ### **REPAIRS OF (R320)(3) 4 ; CONTROLS AS WANTED %s ; CARRY-TIME ROWS %d ; NO SEALED TOOL OF AN EARLIER ACT EDITED ; SHARED TOOLS EDITED 2 (THE RULING`S).**' % (
        ok, sum(1 for l in CARRY_ROWS if re.match(r'^  \(\d+\) ', l)))]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L[-1:]))


# ================================================================================ COMPONENT 3: THE MOVES-BY-LOCUS TABLE, ENTERED ON THE AUTHOR'S WORD ((R320)(5)(ii))
MOVES_REC = ('*Appended 2026-10-24 by b710 beneath b709’s trail (:15766), under `(R320)`(5)(ii) and the author’s word of 2026-10-24 at the '
             'table’s prompt (option 1, “enter in OPEN_TRAILS”) -- THE MOVES-BY-LOCUS TABLE AT WEIL POSITIVITY ON classK, ENTERED AS THE ORDER '
             '**`W-ORD-MOVES-BY-LOCUS`**:* the six '
             'brightening moves (phase1.5/method/THE_BRIGHTENING_MOVES.md :9-:14) and the six perspective axes (phase1.5/method/INSTRUMENTS.md '
             ':131-:138), each with the act or order that tried it at the clause by ledger line and the wall’s reading, in relay '
             'data/b710_reading5.txt section (ii) :113-:155 (rows :120-:150, counts :152-:154). The twelve rows in their reading: (1) inversion-change '
             '-- W-MINE-QUADRATIC, reappeared at Level 2 (:120-:122); (2) cover-ascent -- W-SIGN-7, narrowed to zeroActing for a single zeta '
             '(:123-:124); (3) subspace-restriction -- the finite-range partial positivity, narrowed on the subspace, the classK widening of b701-b703 '
             'reappeared (:125-:127); (4) parameter-deformation -- the Lagarias deformation, reappeared at the h = 1/2 threshold (:128-:129); (5) '
             'structure-transport -- W-SUBSTRATE, reappeared, no analogue over Q (:130-:131); (6) region-compression -- the finite-range certificate and '
             'E-15, narrowed on the compressed region (:132-:135); (a) re-centering -- the notched window, re-presented (:136-:138); (b) cover -- '
             'W-SIGN-7, narrowed (:139); (c) distinguished subspace -- the widened classes, reappeared (:140-:141); (d) deformation parameter -- the '
             'generic deformation reappeared, the support radius at Q0 moved, the one row where the wall moves and at the control object, not at zeta '
             '(:142-:145); (e) representation coordinates -- re-presented at statement grade, untried by computation, registered for b711 '
             '(:146-:148); (f) reading order -- the chiasmus and the faces join, reappeared (:149-:150). Counts: 12 rows, 11 tried at the clause, 1 '
             'untried ((e), registered for b711); 1 moved, 4 narrowed, 2 re-presented, 5 reappeared. Beside them W-UNION, the new-axis composition of '
             'region-compression, priced and held (THE_BRIGHTENING_MOVES.md :25), not run. phase1.5/method/INSTRUMENTS.md is untouched. On the '
             'author’s word, each later research act that tries a move at the clause appends its row’s new reading to this record by line, so the '
             'table stays the place a proposed move is checked before it is proposed. Status OPEN.')


def moves(*a):
    dry = 'dry' in a
    land([('OPEN_TRAILS.md', MOVES_REC, NL + MOVES_REC + NL)], '%s_moves_lines.json' % ACT, 'moves', entry=None,
         check=[('OPEN_TRAILS.md', K.B709_TRAIL, '### b709'), ('FINDINGS.md', K.B709_ENTRY, '## The sign-onset radius at the Epstein zeta')], dry=dry)


# ================================================================================ COMPONENT 4: THE REGISTRATIONS RE-READ, (R320)(6)
REG_COMMIT = '41ff1193'   # ### data/b710_registrations.txt and data/b710_rules.txt committed alone at step zero, before any other bank of the act
COMPUTE_TOOLS = ('b709_pairs.py', 'b709_grid.py', 'b707_onset.py', 'b705_detection.py', 'b675_li_bench.py', 'b667_epstein_certify.py', 'b694_witness', 'b696_witness_balls.py')


def regcheck(*a):
    """data/b710_registrations_reread.txt (.json), Component 4: the registrations bank and the rules bank re-read after Components 1-3 and compared
    byte for byte with their blobs at relay 41ff1193 and at HEAD, the commits touching each read; the registration printed unchanged; nothing
    computed for its three rows -- no bank of this act carrying an n*, a surgery eigenvalue or a coefficient (by name), no computation tool of the
    rows' routes run in the act's capture; the one derived bank (data/b710_fit.txt, the fit of (i)'s constants from b709's banked pairs) named."""
    out = dict(at=utc(), rows={})
    same = True
    L = ['%s -- COMPONENT 4, (R320)(6): THE REGISTRATIONS RE-READ AFTER COMPONENTS 1-3, UNCHANGED SINCE THEIR COMMIT; NOTHING COMPUTED FOR THEIR THREE ROWS (%s)' % (ACT, utc()), '']
    for p in ('data/%s_registrations.txt' % ACT, 'data/%s_rules.txt' % ACT):
        now = rd(os.path.join(ROOT, *p.split('/'))) or ''
        then = _show(ROOT, REG_COMMIT, p) or ''
        hb = g(ROOT, 'rev-parse', 'HEAD:' + p).strip()
        tb = g(ROOT, 'rev-parse', '%s:%s' % (REG_COMMIT, p)).strip()
        wb = g(ROOT, 'hash-object', '--', p).strip()
        log = [l for l in g(ROOT, 'log', '--format=%h', '--', p).split(NL) if l.strip()]
        eq = bool(now) and now == then and wb == tb == hb
        same = same and eq
        out['rows'][p] = dict(work_blob=wb, then_blob=tb, head_blob=hb, commits=log, unchanged=eq)
        L.append('### %s -- committed alone at relay %s ; the working file`s blob %s ; at %s %s ; at HEAD %s ; the commits touching it %s ; EQUAL BYTE FOR BYTE %s' % (
            p, REG_COMMIT, wb[:12], REG_COMMIT, tb[:12], hb[:12], log, eq))
    names = sorted(f for f in os.listdir(D) if f.startswith('%s_' % ACT) and re.search(r'nstar|pair1[15]|surgery|coeff|onset|eigen|_grid|_pairs', f))
    rows = capture()
    runs = [r['n'] for r in rows if r['tool'] in ('Bash', 'PowerShell') and any(re.search(r'python[^\n]*' + re.escape(t), r['cmd']) for t in COMPUTE_TOOLS)]
    L += ['', '### banks of this act named for an n*, a surgery, a coefficient, an onset, an eigenvalue, a grid or a pairs computation: %s' % (names or 'NONE'),
          '### commands of the act running a computation tool of the rows` routes (%s): %s' % (', '.join(COMPUTE_TOOLS), runs or 'NONE'),
          '### the one derived bank: data/b710_fit.txt (tools/b710_fit.py, the constants of (i) fitted from data/b709_pairs.txt`s printed figures; no n*, zero or coefficient computed)', '',
          '### THE REGISTRATION, PRINTED UNCHANGED:'] + ['    ' + x for x in (rd(os.path.join(D, '%s_registrations.txt' % ACT)) or '').rstrip(NL).split(NL)]
    nothing = not names and not runs
    L += ['', '### ### **THE REGISTRATIONS AND THE RULES UNCHANGED SINCE THEIR COMMIT %s (relay %s) ; NOTHING COMPUTED FOR THE THREE ROWS %s.**' % (same, REG_COMMIT, nothing)]
    out.update(unchanged=same, computed_banks=names, compute_runs=runs, nothing_computed=nothing)
    put_txt('%s_registrations_reread.txt' % ACT, L)
    put_json('%s_registrations_reread.json' % ACT, out)
    print(NL.join(L[2:4] + L[5:8] + L[-1:]))


# ### stage one (step zero): b709's Component routes over its own objects pruned (data/b710_prune_record.txt); this act's are added by the Edit tool
ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              ksyms=ksyms, defs=defs, figures=figures, runner=runner,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry, linecheck=linecheck, c1=c1, repairctl=repairctl, toolrepairs=toolrepairs, moves=moves, regcheck=regcheck)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b710_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
