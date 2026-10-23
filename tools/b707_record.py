# -*- coding: utf-8 -*-
"""b707_record.py -- THE ACT'S RECORD TOOL, b707 under (R317).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b707 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap). b703's repaired
### readers, b704's repaired read route, b705's routes (the print-list dispatch, the artifact reader) and b706's (the runner choosing the run's
### artifact by name, the root route's dry run, the declared untracked writes) are reached through tools/b706_record.py (sealed at b706 and
### unedited), each pure in its arguments or rebound here. Every python child is `python -X utf8`.
### THE CARRY-TIME REPAIRS OF THIS TOOL (data/b707_tool_repairs.txt): (a) prev_capture for a previous act in ANOTHER session (b701's form:
### b706 ran and closed in 44411d52; this act opens aa198636), from b706's post-push combine to that session's end; (b) ROOT_EXCLUDE carried and
### extended at carry time with every untracked write a b707_*.py tool declares in its head (`### UNTRACKED WRITE: data/b707_<name>`),
### data/b706_rules.txt row (1), printed by `rootexclude`.
### Written by the Write tool at b707 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b707_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
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

import b707_worklist as K          # noqa: E402
import b706_worklist as K706       # noqa: E402  ### b706's data, for the controls on b706's banks
import b706_record as P6           # noqa: E402  ### b706's tool, imported unedited (its import binds b698's R, b703's P3, b704's P4 and b705's P5 to b706: rebound below)
R, P3, P4, P5 = P6.R, P6.P3, P6.P4, P6.P5   # ### b698's routes, b703's, b704's and b705's repaired readers, through b706's module

ACT, PREV = 'b707', 'b706'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b706 ran and closed in ANOTHER session (44411d52; this act opens aa198636 after the author's /clear) -- b701's
# ### form: from b706's post-push combine in that session to that session's end (prev_capture below)
PREV_SESSION_PATH = '%s/%s.jsonl' % (PROJ, K.PREV_SESSION)
PREV_SUBAGENTS = '%s/%s/subagents' % (PROJ, K.PREV_SESSION)
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.PREV_SESSION, K.PREV_ANCHOR
R.PREV_SESSION_PATH = PREV_SESSION_PATH
R.PREV_SUBAGENTS = PREV_SUBAGENTS
FACE = os.path.join(D, 'b707_registration_%s.txt' % K.DATE)
FACE_REL = 'data/b707_registration_%s.txt' % K.DATE
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b706_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('terminal_table.py', 'rule_arms.py', 'mirror_roster.json')

# ### THE ROOT ROUTE'S EXCLUSION LIST (data/b706_rules.txt row (1)): the kinds b698's route excludes, carried; and every untracked write a
# ### b707_*.py tool declares in its own head, read at import. A tool declares one by a line `### UNTRACKED WRITE: data/b707_<name>`.
EXCLUDE_KINDS = (r'defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                 r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                 r'commands|mirror.*|close_sentence|read_calls')
UNTRACKED_DECL = re.compile(r'^### UNTRACKED WRITE: data/b707_(\S+)\s*$', re.M)


def declared_untracked():
    """every b707_*.py tool's declaration of an untracked write (its units file, its download), read from the tools' own heads: [(tool, name)]."""
    out = []
    for f in sorted(os.listdir(T)):
        if f.startswith('b707_') and f.endswith('.py'):
            for m in UNTRACKED_DECL.finditer(rd(os.path.join(T, f)) or ''):
                out.append((f, m.group(1)))
    return out


def _root_exclude():
    names = [re.escape(n) for _f, n in declared_untracked()]
    return re.compile(r'^b707_(' + EXCLUDE_KINDS + (('|' + '|'.join(names)) if names else '') + r')\.?(txt|json|md|jsonl|)$')


R.ROOT_EXCLUDE = _root_exclude()


def rootexclude(*a):
    """prints the declared untracked writes and the exclusion pattern they extend; writes nothing."""
    decl = declared_untracked()
    for f, n in decl:
        print('  %-28s declares data/b707_%s untracked' % (f, n))
    print('  DECLARED UNTRACKED WRITES %d ; ROOT_EXCLUDE %s' % (len(decl), R.ROOT_EXCLUDE.pattern))


_R_anchor_ts = P6._R_anchor_ts   # ### b698's original, captured by b703 before its wrapper (b701's trap), carried through b704, b705 and b706


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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='aa8a696b' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row = R.read_branch_row, R.read_runner_row
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ b703'S, b704'S, b705'S AND b706'S REPAIRED READERS, THROUGH b706'S MODULE
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


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried; rowgen's roster re-pointed)
answers = R.answers


def _renamed():
    """the 17 pairs b706 renamed in place (data/b706_partners.json): the retired versioned path -> the unversioned name, the file of record."""
    return dict((r['versioned'], r['unversioned']) for r in (jl('b706_partners.json').get('rows') or []) if r.get('versioned') and r.get('unversioned'))


def roster707():
    """b698's roster (tools/b698_record.py roster: the 19 documents of data/b586_corroboration.txt :34 with the paths its table names) with every
    path b706's renames retired re-pointed to the unversioned name -- the carry-time repair of the fourth path reader the renames broke (the
    three of (R317)(2) and this one): [(name, path, re-pointed from)]."""
    ren = _renamed()
    return [(n, ren.get(p, p), p if p in ren else None) for n, p in R.roster()]


def rowgen(*a):
    """b670 rules row 3: tools/rowgen/rowgen.py `constellation <root> <papers>` and tools/rowgen/diff_rowpin.py `<namemap.json> <papers>` (the
    build-free diff) over the 19 roster tables, each at the file of record after b706's renames (roster707); each tool's verdict lines banked
    with its exit. data/b707_rowgen_<stage>.txt."""
    stage = a[0] if a and a[0] not in ('dry',) else 'stepzero'
    Ro = roster707()
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
         '((R316)(3): %d of the bank`s paths re-pointed from the retired versioned name, data/b706_partners.json) ; the instruments: tools/rowgen/rowgen.py '
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


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R317)(7); b706's form, two kernel branches)
def branches(*a):
    """`branches before`: data/b707_branches_before.json -- b698's route, carried (every branch (R317)(7) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b707_branches.txt (.json) --
    each branch's fate read now against the tips banked before."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b707_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R317)(7): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b707_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. (R317)(7) names two kernel branches, SIDE-faces-join push-b706-join',
         '### and SIDE-explicit-formula push-b706-ef.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows))]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[]))
    print(NL.join(L[7:]))


# ================================================================================ THE READ BANK (b704's repaired route; the word's time the anchor's, from b705)
def reads(*a):
    """b704's repaired route (tools/b704_record.py :392) with the author's word at b704's arm-baseline prompt applied: from b705 the word's time
    is the act's anchor and every call counts -- every Read call of the seat since the anchor with its offset and limit VALUES, the file's line
    count read now beside it; a call of a file of two hundred lines or more with no offset, or no limit, or a limit above two hundred is an
    offence. data/b707_read_calls.txt."""
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
    mod = {'b698': R, 'b703': P3, 'b704': P4, 'b705': P5, 'b706': P6}.get(a[0] if a else 'b698') or importlib.import_module(a[0])
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


# ================================================================================ THE LATE ROUTES (b706's, carried with b707's names; the previous window in its own session)
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
    """G-EDIT-ROUTE's window over the previous act, b701's form for a previous act in ITS OWN session (the carry-time repair (a)): b706's capture
    AFTER ITS POST-PUSH SUITE -- every command of session 44411d52 from the call that combined b706's post-push parts into
    data/b706_checks_postpush.txt to that session's end, its closing's commands among them; this act runs in a session of its own."""
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
    """b706's route with b707's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window (b706's
    session from its post-push combine to its end), the local lean reading (N1), the dispatches (one ordered: the port branch), the detached
    runs, sed, the redirects, the pipes, the one-line programs, the moves and deletes by shape, the outbound requests. data/b707_commands.txt (.json)."""
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
    L += ['', '### THE RUNNER DISPATCHES (one ordered this act, N1: the port branch of SIDE-lv-conservation) (%d):' % len(disp)] + (
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
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R317)(7) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
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
    print('  kernels read: %d (SIDE-faces-join among them; no kernel written after this read but the port branch of SIDE-lv-conservation under (R317)(5))' % len(ks))


def _standing():
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B706_FACE.split('/')))) - set(K706.ACT_ARMS)) | set(K.STANDING_ADDED))


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
    (the push clause, HEAD the remote main, printed beside and not required before the record`s push). data/b707_root_banks_dry.txt (.json)."""
    banks = root_banks()
    s = root_banks_state(banks)
    crlf = [b_ for b_ in banks if os.path.exists(os.path.join(ROOT, *b_.split('/'))) and b'\r\n' in open(os.path.join(ROOT, *b_.split('/')), 'rb').read()]
    missing = [b_ for b_ in banks if not os.path.exists(os.path.join(ROOT, *b_.split('/')))]
    ready = bool(s['rows']) and s['clean'] and not crlf and not missing
    L = ['%s -- THE ROOT ROUTE`S DRY RUN ON THE PRE-ROOT TREE BEFORE THE SEAL (data/b706_rules.txt row (1)) (%s)' % (ACT, utc()), '',
         '### rows are the banks the root route names (tools/b698_record.py root_banks with ROOT_EXCLUDE rebound at tools/b707_record.py, extended by',
         '### every declared untracked write: %s): status ; carried by HEAD ; HEAD`s blob equal to the file ; CR LF.' % (
             [n for _f, n in declared_untracked()] or 'NONE DECLARED'),
         '### HEAD %s ; the remote main %s ; equal %s (the push clause, read beside: the record`s push comes after the seal)' % (s['head'], s['remote'], s['pushed']), '']
    L += ['  %-52s %-6s at HEAD %-5s equal %-5s crlf %s' % (r['bank'], r['status'], r['at_head'], r['equal'], r['bank'] in crlf) for r in s['rows']]
    L += ['', '### ### **BANKS %d ; CLEAN AND EQUAL AT HEAD %d ; CR LF %s ; MISSING %s ; HEAD THE REMOTE MAIN %s ; THE DRY RUN READY %s.**' % (
        len(s['rows']), sum(1 for r in s['rows'] if r['status'] == 'clean' and r['equal']), crlf or 'NONE', missing or 'NONE', s['pushed'], ready)]
    put_txt('%s_root_banks_dry.txt' % ACT, L)
    put_json('%s_root_banks_dry.json' % ACT, dict(at=utc(), ready=ready, crlf=crlf, missing=missing, declared=declared_untracked(), **s))
    print(L[-1])


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R317)(1)
WH = ('*Appended 2026-10-22 by b707 to b706’s entry (:10046), under `(R317)`(1) -- b706 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b706_closing.txt):*')


def _declared_b706():
    face = rd(os.path.join(ROOT, *K.B706_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    return sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []


def _failing_b706():
    m = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', rdn('b706_checks_postpush.txt'))
    return [x.strip().strip("'") for x in (m.group(2) if m else '').split(',') if x.strip()]


def _wb():
    """b706's weight line, its figures read from b706's banks where a bank names them (the declared arms from the face, the failing eleven
    from the post-push bank) and otherwise quoted from the closing record (relay data/b706_closing.txt) by line."""
    decl, fails = _declared_b706(), _failing_b706()
    post = [a for a in fails if a not in decl]
    if len(decl) != 4 or len(fails) != 11 or len(post) != 7:
        sys.exit('### b706`S FACE OR ITS POST-PUSH BANK NOT AS READ (declared %s ; failing %s) -- NOTHING COMPOSED' % (decl, fails))
    return (' “b706 closed: relay 30313a13, PLACE-papers c9e0086; suite 129 of 140; root aa8a696b1c7e9fef…; 4 prompts answered; 13 defects” '
            '(data/b706_closing.txt :1); the closing commit 37e4a12f pushed alone after the line was written and read back equal at the remote '
            '(data/b706_closing_push_out.txt :5). The seventeen partner pairs renamed in place under (R316)(3): the eight hand-edited lines read '
            'side by side first and resolved by kind on the author’s word, the generator run once, the second pass changing 0 cells, 107 lines '
            'counted apart, 17 renamed and 0 held, the 102 standing reader hits equal before and after, the roster’s 20 tables found at the '
            'unversioned names (data/b706_partners_read.txt, data/b706_partners.txt, data/b706_readers_after.txt); the join’s lakefile re-ordered '
            'with mathlib last on Lake’s own hint, one commit b37a7b6, one dispatch (run 39850337262), the cache served and Mathlib built, the '
            'join HELD at SIDELvConservation/GammaBounds.lean :177 at the shared pin, the gate NOT DERIVES, no tag (data/b706_join_lakefile.txt, '
            'data/b706_runner_SIDE-faces-join_join.txt, data/b706_join_grade.txt); the workflow’s probe step at :101 of build-module.yml on '
            'SIDE-explicit-formula’s main at badaccc, 49 diff lines, no identifier (data/b706_workflow_step.txt); the generator parsing '
            'SIDE-explicit-formula’s citation form, 17 kernels and 13 cells, 20 of 20 re-emissions byte-equal (data/b706_generator_reach.txt); '
            'the entry-tag prints at v0.1 = baed4df and v0.2 = 5c72cad from scratch branches (runs 39852365437, 39852975531), both DERIVES at '
            'the standard three, 9 of 11 mentions equal, 0 differing, 2 unbanked (data/b706_prints_v0.1.txt, data/b706_prints_v0.2.txt, '
            'data/b706_cells_reread.txt); the faces row unchanged, the hold named in the entry (data/b706_faces.txt). b705’s six post-seal '
            'items answered by the generated corrigendum at FINDINGS :10030 (corrigenda row (26)); b705’s weight at :10028. The entry at '
            'FINDINGS :10046, the trail at OPEN_TRAILS :15644; the root aa8a696b over 114 banks chained from 8454a2bb (data/b706_act_root.json, '
            'data/b706_root_banks.txt); suite 129 of 140 pre-push and post-push, four failures declared on the face (%s) and seven found after '
            'the seal (%s; data/b706_checks.txt, data/b706_checks_postpush.txt); N1, N2 and N4 HELD, N3 REFUTED by the author’s word (the '
            'ruling’s order mathlib-first, the navigator’s (b)), N5 REFUTED at the record on one message carrying two git writes (18:42:34Z), '
            'S1 REFUTED at the close on the table (12 rows added, 15 grades moved, every one citing a retired copy: (i)), S2 and S3 HELD '
            '(data/b706_scores_close.json); the sealed tools’ hashes equal at the close, 10 of 10; the citation check 130 cites, 129 OK, 1 miss '
            'the navigator’s ((a)); thirteen defects (a)–(m), (a), (b), (c), (i) and (m) the navigator’s (data/b706_defects.txt); “4 prompts '
            'answered” the answers bank’s 3 rows and the root’s prompt; the mirror mirror-refresh-2026-10-22-b706.zip CLEAN on clauses 1 and 2 '
            'and NOT CLEAN on clause 3 by its roster’s 17 retired names, with the root line ((m); data/b706_mirror.txt, '
            'data/b706_mirror_verify.txt). The seven post-seal items entered by this act’s corrigendum. Nothing deposited.' % (
                ', '.join(decl), ', '.join(post)))


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + _wb() + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B706_ENTRY,
         check=[('FINDINGS.md', K.B706_ENTRY, '## 17 of 17 partner pairs renamed in place'), ('OPEN_TRAILS.md', K.B706_TRAIL, '### b706')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE THREE READERS' REPAIRS, (R317)(2), AND THE CARRY-TIME REPAIRS, WITH THEIR CONTROLS
RETIRED_FOUR = ('EXHAUSTIVENESS_LICENSE.md', 'TECHNE_TOOLKIT.md', 'R_CURVE_CRITERION.md', 'E_DIFFICULTY_THEOREM.md')
REPAIR_ROWS = [      # ### (text, kind, old, new): kind `file` diffs the whole file at relay HEAD against the working tree; kind `fn` a function
    ('(1) tools/mirror_roster.json -- ANSWERS (R317)(2) and the author`s word at this act`s first prompt (b706`s (m)): the roster named the 17 '
     'versioned paths the renames of (R316)(3) retired, so b706`s export verified NOT CLEAN on clause 3 alone (17 MISSING, data/b706_mirror_verify.txt). '
     'The ruling`s "rewritten to the 17 unversioned names" would list 13 paths twice (they stand at :14-:27 and :46 already) and the builder`s flat '
     'naming collides on a path listed twice (tools/mirror_verify.py staged_names) -- the navigator`s (f). On the author`s word: the four rows whose '
     'papers stood here at the versioned name alone (EXHAUSTIVENESS_LICENSE, TECHNE_TOOLKIT, R_CURVE_CRITERION, E_DIFFICULTY_THEOREM) re-pointed to '
     'the unversioned names in their own slots, the thirteen duplicate rows removed, 70 entries, the history line extended; by the Edit tool; the '
     'builder unedited by (R96). The control: the dry run of tools/mirror_verify.py against b706`s export (data/b707_roster_control.txt) -- clauses 1 '
     'and 2 CLEAN, clause 3 NOT CLEAN by exactly the four names MISSING; data/b707_repair_controls.txt.', 'file', 'tools/mirror_roster.json', None),
    ('(2) tools/terminal_table.py `ledger_files`, RETIRED_DIRS -- ANSWERS (R317)(2) (b706`s (i), THE NAVIGATOR`S): the ledger walk takes every .md '
     'under PLACE-papers/archive/ as a ledger (b494`s rule: a split moves a ledger, it does not retire it), so the 17 retired copies (R316)(3) moved '
     'to archive/2026-10-22-b706-partner-copies/ entered the table at b706`s final regeneration -- 12 rows added, 18 moved, 15 grades moved, every '
     'one citing a retired copy (data/b706_table_final.txt; S1 REFUTED, G-TABLE-FINAL failing). The repair: the retired copies` directory excluded '
     'by path (RETIRED_DIRS), the split ledgers of 2026-08-24 still in reach; by the Edit tool. The control: the table regenerated and diffed '
     'against b706`s final table -- the 12 added rows gone, the 18 moved rows restored to their prior state (15 grades), no other row changed '
     '(data/b707_table_scope.txt); the walk`s own count with and without the exclusion; data/b707_repair_controls.txt.', 'file', 'tools/terminal_table.py', None),
    ('(3) tools/rule_arms.py `reading`, G-RULE-SUITE-PARTS -- ANSWERS (R317)(2) (b706`s (l)): b692`s family reading strips one trailing digit '
     '(`(?<=^standing-[a-z])[0-9]$`), so standing-b2a and standing-b2b read as families of their own and b706`s run banks fail the arm at every later '
     'act. The repair: a lettered half strips its letter and its digit to the family it halves (`[0-9][a-z]?$`), and a family is met whole or '
     'by its numbered halves 1, 2, ... consecutive and at least two, a numbered half whole or by its lettered halves a, b, ... consecutive and at '
     'least two, never both (`whole`); by the Edit tool. The control: the arm`s old and repaired readings over b706`s run banks, b705`s unsplit '
     'banks and every run bank b678-b706; mutated copies: a part outside any family planted, a half planted beside its halves, a lettered half '
     'alone, a gap in the numbering; data/b707_repair_controls.txt.',
     'file', 'tools/rule_arms.py', None),
    ('(4) tools/b707_record.py `rowgen`, `roster707`, `_renamed` -- ANSWERS the carry (a fourth path reader the renames broke, data/b707_defects.txt, '
     'the events): b698`s rowgen (tools/b698_record.py :190) reads its 19-table roster from data/b586_corroboration.txt`s table, whose paths are the '
     'retired versioned names for eight documents; at this act`s step zero it refused. The repair: each roster path re-pointed through '
     'data/b706_partners.json to the file of record, the re-pointing printed in the bank (RE-POINTED 8). The control: every roster path present at '
     'PLACE-papers HEAD, the old roster against the re-pointed; data/b707_repair_controls.txt.', 'fn', ('b698_record.py', 'rowgen'),
     ('b707_record.py', 'rowgen', ('roster707', '_renamed'))),
    ('(5) tools/b707_record.py `prev_capture` -- ANSWERS the carry: b706`s route (tools/b706_record.py prev_capture) reads the previous act`s window '
     'from this session cut at this act`s anchor, b705 having run in b706`s own session; b706 ran and closed in 44411d52 and this act opens aa198636 '
     'after the author`s /clear, so b701`s form is carried: b706`s capture from its post-push combine to that session`s end, read from that '
     'session`s own file and subagents. The control: data/b707_repair_controls.txt.', 'fn', ('b706_record.py', 'prev_capture'),
     ('b707_record.py', 'prev_capture', ())),
    ('(6) tools/b707_record.py `_root_exclude`, `declared_untracked` -- ANSWERS data/b706_rules.txt row (1): the root route`s exclusion list carried '
     'from b706`s tool and extended at carry time with every untracked write a b707_*.py tool declares in its head; the `rootexclude` route prints '
     'them; `rootdry` runs the root route dry before the seal. The control: data/b707_repair_controls.txt.', 'fn', ('b706_record.py', '_root_exclude'),
     ('b707_record.py', '_root_exclude', ('declared_untracked',))),
]


def _udiff(old, new, a, b):
    import difflib
    return list(difflib.unified_diff(old, new, a, b, lineterm='', n=2))


def repairs(*a):
    """data/b707_tool_repairs.txt: the three readers` repairs of (R317)(2) (each shared file`s diff, relay HEAD against the working tree, by the
    Edit tool) and the carry-time repairs of this act`s record tool (difflib over the function`s source, the carried tool`s against this act`s)."""
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS, (R317)(2) (%s)' % (ACT, utc()), '',
         '### rows are repairs with what they answer: the file or the tool and its part ; what it answers ; the form. Each diff beneath its row,',
         '### written by this route (rows (1)-(3): the shared file at relay HEAD %s against the working tree, edited by the Edit tool under' % g(ROOT, 'rev-parse', '--short=8', 'HEAD').strip(),
         '### (R317)(2); rows (4)-(6): the carried function`s source against this act`s, a new function printed whole). The controls that',
         '### distinguish each repaired reading from the old one: data/b707_repair_controls.txt. No sealed tool is edited.', '']
    n = 0
    for text, kind, old, new in REPAIR_ROWS:
        L += ['  ' + text, '']
        if kind == 'file':
            o = (_show(ROOT, 'HEAD', old) or '').split(NL)
            w = (rd(os.path.join(ROOT, *old.split('/'))) or '').split(NL)
            d = _udiff(o, w, '%s (relay HEAD)' % old, '%s (this act, the working tree)' % old)
            n += len(d)
            L += ['      ' + x for x in d] + ['']
            continue
        oldf, fn = old
        newf, fn2, extra = new
        o = R._fn_src(rd(os.path.join(T, oldf)), fn).split(NL)
        w = R._fn_src(rd(os.path.join(T, newf)), fn2).split(NL)
        d = _udiff(o, w, 'tools/%s %s (sealed)' % (oldf, fn), 'tools/%s %s (this act)' % (newf, fn2))
        n += len(d)
        L += ['      ' + x for x in d] + ['']
        for f2 in extra:
            o2 = R._fn_src(rd(os.path.join(T, oldf)), f2)
            o2 = o2.split(NL) if o2 else []
            w2 = R._fn_src(rd(os.path.join(T, newf)), f2).split(NL)
            d = _udiff(o2, w2, ('tools/%s %s (sealed)' % (oldf, f2)) if o2 else '(none)', 'tools/%s %s (this act)' % (newf, f2))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; SHARED FILES EDITED 3 UNDER (R317)(2) (tools/mirror_roster.json, tools/terminal_table.py, tools/rule_arms.py), EACH BY THE EDIT TOOL ; '
          'DIFF LINES %d ; NO SEALED TOOL EDITED ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


def tablescope(*a):
    """data/b707_table_scope.txt (.json): the table regenerated with the retired copies` directory out of the ledger walk and diffed against relay
    HEAD`s table (b706`s final, data/b706_table_final.txt): wanted the 12 added rows gone, the 18 moved rows restored to the state HEAD`s prior
    table holds (b705`s final; 15 of them grades), nothing added and no other row changed. The walk`s own count with and without the exclusion."""
    import terminal_table as TT
    new_files = [l for l, _p in TT.ledger_files()]
    keep = TT.RETIRED_DIRS
    try:
        TT.RETIRED_DIRS = ()
        old_files = [l for l, _p in TT.ledger_files()]
    finally:
        TT.RETIRED_DIRS = keep
    dropped = sorted(set(old_files) - set(new_files))
    b6 = jl('b706_table_final.json')
    before = R._rows_state(json.loads(_show(ROOT, 'HEAD', 'data/terminal_table.json'))['rows'])
    # ### the state each moved row held BEFORE b706`s final regeneration, read from b706`s own diff lines ("moved repo / name : (before) -> (after)")
    import ast
    prior = {}
    for l in rdn('b706_table_final.txt').split(NL):
        m = re.match(r'^    moved   (\S+) / (\S+) : (\(.*?\)) -> (\(.*?\))$', l)
        if m:
            prior[(m.group(1), m.group(2))] = ast.literal_eval(m.group(3))
    t0 = time.time()
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    secs = int(time.time() - t0)
    after = R._rows_state(json.load(open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows'])
    moved = sorted(k for k in set(before) & set(after) if before[k] != after[k])
    added, gone = sorted(set(after) - set(before)), sorted(set(before) - set(after))
    b6_added = sorted(tuple(x) for x in b6.get('added') or [])
    b6_moved = sorted(tuple(x) for x in b6.get('moved') or [])
    restored = [k for k in moved if k in prior and after[k] == prior[k]]
    grade_moved = [k for k in moved if before[k][0] != after[k][0]]
    other = [k for k in moved if k not in b6_moved]
    ok = (r.returncode == 0 and gone == b6_added and len(gone) == 12 and not added and moved == b6_moved and len(moved) == 18
          and len(restored) == 18 and len(grade_moved) == 15 and not other
          and len(dropped) == 17 and all(d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in dropped))
    L = ['%s -- COMPONENT 1, (R317)(2): THE TERMINAL TABLE`S SCOPE REPAIRED -- THE TABLE REGENERATED AND DIFFED AGAINST b706`S FINAL TABLE (%s); exit %d ; %d s' % (ACT, utc(), r.returncode, secs), '',
         '### the ledger walk (tools/terminal_table.py ledger_files): files with the retired copies` directory in reach (the old reading) %d ; without it (repaired) %d ; '
         'dropped %d, every one under PLACE-papers/%s %s' % (len(old_files), len(new_files), len(dropped), K.ARCHIVE_DIR, all(d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in dropped))]
    L += ['    dropped %s' % d for d in dropped]
    L += ['', '### the table against relay HEAD`s (b706`s final, relay data/b706_table_final.txt: added 12, moved 18, grade moved 15): rows %d ; added %d ; gone %d ; moved %d ; '
              'of the moved, restored to HEAD`s prior table (b705`s final) %d ; grades moved %d ; moved rows b706`s final did not move %d' % (
                  len(after), len(added), len(gone), len(moved), len(restored), len(grade_moved), len(other))]
    L += ['    gone    %s / %s' % k for k in gone] + ['    added   %s / %s' % k for k in added] + [
        '    moved   %s / %s : %s -> %s%s' % (k[0], k[1], before[k], after[k], '' if k in restored else ' ### NOT RESTORED') for k in moved]
    L += ['', '### ### **THE WALK DROPS %d FILES, EVERY ONE A RETIRED COPY %s ; AGAINST b706`S FINAL TABLE: GONE %d (b706`S ADDED %d), ADDED %d, MOVED %d (b706`S MOVED %d), '
              'RESTORED %d, GRADES MOVED %d, OTHER ROWS CHANGED %d ; AS WANTED %s.**' % (
                  len(dropped), all(d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in dropped), len(gone), len(b6_added), len(added), len(moved), len(b6_moved),
                  len(restored), len(grade_moved), len(other), ok)]
    put_txt('%s_table_scope.txt' % ACT, L)
    put_json('%s_table_scope.json' % ACT, dict(at=utc(), rc=r.returncode, seconds=secs, ok=ok, dropped=dropped, gone=[list(k) for k in gone], added=[list(k) for k in added],
                                               moved=[list(k) for k in moved], restored=[list(k) for k in restored], grade_moved=[list(k) for k in grade_moved],
                                               other=[list(k) for k in other], walk_old=len(old_files), walk_new=len(new_files)))
    print(NL.join(L[:3] + L[-1:]))


def _rule_arms_head():
    """tools/rule_arms.py as relay HEAD carries it (the sealed reading), loaded from the blob into a module of its own: the old reading, run and
    not retyped."""
    import types
    src = _show(ROOT, 'HEAD', 'tools/rule_arms.py') or ''
    mod = types.ModuleType('rule_arms_head')
    mod.__file__ = os.path.join(T, 'rule_arms.py')
    exec(compile(src, 'tools/rule_arms.py@HEAD', 'exec'), mod.__dict__)
    return mod


def repairctl(*a):
    """data/b707_repair_controls.txt: each repaired reading and the old one run on real state (b706`s export, b706`s and b705`s run banks, the
    roster bank, this session) and on mutated copies, so that the repaired reading is distinguished from the old on a row."""
    import zipfile
    import mirror_verify as MV
    import rule_arms as RA
    L = ['%s -- COMPONENT 1, (R317)(2): THE REPAIRED READINGS AGAINST THE OLD ON REAL STATE AND ON MUTATED COPIES (%s)' % (ACT, utc()), '',
         '### rows are cases: the reader | the source (a bank, an export, a session, or a mutated copy) | the old reading | the repaired | wanted.',
         '### Each repaired reading is DISTINGUISHED where one row reads them apart.', '']
    cases = []
    # ### (1) the roster against b706`s export: the names staged by the builder`s rule (tools/mirror_verify.py staged_names, the clause 3 reading)
    z = zipfile.ZipFile(K.MIRROR_ZIP)
    have = set(n for n in z.namelist() if n.lower() != 'manifest.md')
    old_paths = json.loads(_show(ROOT, 'HEAD', 'tools/mirror_roster.json'))['files']
    new_paths = json.loads(rd(os.path.join(T, 'mirror_roster.json')))['files']
    old_exp, new_exp = set(MV.staged_names(old_paths)), set(MV.staged_names(new_paths))
    om, oe, nm, ne = sorted(old_exp - have), sorted(have - old_exp), sorted(new_exp - have), sorted(have - new_exp)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'mirror_verify.py'), K.MIRROR_ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    dry = (r.stdout + r.stderr).replace(chr(13), '')
    put_txt('%s_roster_control.txt' % ACT, ['%s -- THE ROSTER`S CONTROL: tools/mirror_verify.py RUN DRY AGAINST b706`S EXPORT WITH THE ROSTER AS EDITED (%s); exit %d' % (ACT, utc(), r.returncode),
                                             '### the export: %s ; wanted on the author`s word: clauses 1 and 2 CLEAN, clause 3 NOT CLEAN by exactly the four re-pointed names MISSING' % K.MIRROR_ZIP, '']
                 + dry.split(NL))
    c1_, c2_ = 'CLAUSE 1 : CLEAN' in dry, 'CLAUSE 2 : CLEAN' in dry
    c3m = re.search(r'in roster, MISSING from archive : (\d+)', dry)
    c3x = re.search(r'in archive, NOT in roster\s+: (\d+)', dry)
    miss_named = re.findall(r'MISSING : (\S+)', dry)
    old_dry = rdn('b706_mirror_verify.txt')
    o3m = re.search(r'in roster, MISSING from archive : (\d+)', old_dry)
    L += ['### the export %s: files %d ; the roster at HEAD %d paths, as edited %d ; staged names expected: old %d, repaired %d ; MISSING old %d %s ; repaired %d %s ; EXTRA old %d, repaired %d' % (
        os.path.basename(K.MIRROR_ZIP), len(have), len(old_paths), len(new_paths), len(old_exp), len(new_exp), len(om), om[:17], len(nm), nm, len(oe), len(ne)),
          '### the dry run as edited (data/b707_roster_control.txt): clause 1 CLEAN %s ; clause 2 CLEAN %s ; clause 3 MISSING %s, EXTRA %s, named %s ; b706`s own run (data/b706_mirror_verify.txt): MISSING %s' % (
              c1_, c2_, c3m.group(1) if c3m else '?', c3x.group(1) if c3x else '?', miss_named, o3m.group(1) if o3m else '?'), '']
    cases.append(('mirror_roster', 'b706`s export against the roster at HEAD (old) and as edited (repaired): every roster name in the export', not om and not oe, not nm and not ne, (False, False)))
    cases.append(('mirror_roster', 'the MISSING set exactly the four re-pointed names and nothing EXTRA (the author`s stated form)', om == sorted(RETIRED_FOUR) and not oe,
                  nm == sorted(RETIRED_FOUR) and not ne, (False, True)))
    cases.append(('mirror_roster', 'the roster`s 70 entries and no path listed twice (the builder`s flat naming)', len(old_paths) == 70 and len(set(old_paths)) == len(old_paths),
                  len(new_paths) == 70 and len(set(new_paths)) == len(new_paths), (False, True)))
    cases.append(('mirror_roster', 'tools/mirror_verify.py run dry over b706`s export: clauses 1 and 2 CLEAN, clause 3 MISSING exactly 4, EXTRA 0 (old: b706`s own run, MISSING 17)',
                  bool(o3m) and o3m.group(1) == '4', c1_ and c2_ and bool(c3m) and c3m.group(1) == '4' and bool(c3x) and c3x.group(1) == '0' and sorted(miss_named) == sorted(RETIRED_FOUR), (False, True)))

    def collides(paths):
        try:
            MV.staged_names(paths)
            return False
        except ValueError:
            return True
    cases.append(('mirror_roster', 'a mutated copy of the repaired roster, FINDINGS.md listed twice: the builder`s naming collides (clause 3 HARD FAILURE)', collides(new_paths),
                  collides(new_paths + ['FINDINGS.md']), (False, True)))
    # ### (2) the table`s scope: the walk and the regeneration (data/b707_table_scope.json, written by `tablescope` before this route)
    ts = jl('%s_table_scope.json' % ACT)
    if not ts:
        sys.exit('### data/b707_table_scope.json IS NOT WRITTEN -- run `tablescope` first')
    L += ['### the table`s scope (data/b707_table_scope.txt): the walk %s files with the retired directory in reach, %s without ; gone %d ; added %d ; moved %d ; restored %d ; grades %d ; other %d ; as wanted %s' % (
        ts.get('walk_old'), ts.get('walk_new'), len(ts.get('gone') or []), len(ts.get('added') or []), len(ts.get('moved') or []), len(ts.get('restored') or []),
        len(ts.get('grade_moved') or []), len(ts.get('other') or []), ts.get('ok')), '']
    cases.append(('terminal_table', 'the ledger walk: a file under the retired copies` directory among the ledgers (old: RETIRED_DIRS emptied ; repaired: as edited)',
                  (ts.get('walk_old') or 0) > (ts.get('walk_new') or 0), False, (True, False)))
    cases.append(('terminal_table', 'the walk drops exactly the 17 retired copies and nothing else', len(ts.get('dropped') or []) == 17 and all(
        d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in ts.get('dropped') or []), len(ts.get('dropped') or []) == 17 and all(
        d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in ts.get('dropped') or []), (True, True)))
    b6 = jl('b706_table_final.json')
    cases.append(('terminal_table', 'the table against b706`s final: 12 added rows gone, 18 moved rows restored (15 grades), nothing added, no other row changed (old: b706`s final diff itself)',
                  not (b6.get('added') or []) and not (b6.get('moved') or []), bool(ts.get('ok')), (False, True)))
    # ### (3) G-RULE-SUITE-PARTS: the old reading (relay HEAD`s rule_arms.py, loaded from the blob) against the repaired, over the real run banks
    OLD = _rule_arms_head()
    S = RA.sources(ACT, None, K.ANCHOR, K.PARTS)
    runs = S['runs']

    def R_with(sel):
        return dict(S, runs=dict((k, v) for k, v in runs.items() if sel(k)))
    name = 'G-RULE-SUITE-PARTS'
    r706, r705, rall = R_with(lambda k: k[0] == 706), R_with(lambda k: k[0] == 705), S
    L += ['### G-RULE-SUITE-PARTS: run banks read %d (b678-b706) ; b706`s %s ; b705`s %s ; the governing parts %s' % (
        len(runs), dict((k[1], [p for p, _s in v]) for k, v in r706['runs'].items()), dict((k[1], [p for p, _s in v]) for k, v in r705['runs'].items()),
        ['%s from b%d: %s' % (b, a_, ps) for a_, b, ps in S.get('governing') or []]), '']
    for lab, RR, want in (('b706`s three run banks (standing-a, c, b1, b2a, b2b, b3, act) against their governing parts', r706, (False, True)),
                          ('b705`s three run banks (unsplit: standing-a, c, b1, b2, act)', r705, (True, True)),
                          ('every run bank b678-b706', rall, (False, True))):
        cases.append((name, lab, OLD.reading(name, RR)[0], RA.reading(name, RR)[0], want))
    pl = dict(r706, runs=dict((k, v + [('standing-z', 1)]) for k, v in r706['runs'].items()))
    cases.append((name, 'a mutated copy of b706`s banks, a part outside any family (standing-z) planted', OLD.reading(name, pl)[0], RA.reading(name, pl)[0], (False, False)))
    pl2 = dict(r706, runs=dict((k, v + [('standing-b2', 1)]) for k, v in r706['runs'].items()))
    cases.append((name, 'a mutated copy of b706`s banks, standing-b2 planted beside standing-b2a and standing-b2b (a half beside its own halves)', OLD.reading(name, pl2)[0], RA.reading(name, pl2)[0], (False, False)))
    pl3 = dict(r705, runs=dict((k, v + [('standing-b', 1)]) for k, v in r705['runs'].items()))
    cases.append((name, 'a mutated copy of b705`s banks, standing-b planted beside standing-b1 and standing-b2 (b692`s "never both")', OLD.reading(name, pl3)[0], RA.reading(name, pl3)[0], (False, False)))
    pl4 = dict(r706, runs=dict((k, [(p, s) for p, s in v if p != 'standing-b2b']) for k, v in r706['runs'].items()))
    cases.append((name, 'a mutated copy of b706`s banks, standing-b2b removed (a lettered half alone)', OLD.reading(name, pl4)[0], RA.reading(name, pl4)[0], (False, False)))
    pl5 = dict(r705, runs=dict((k, [(p, s) for p, s in v if p != 'standing-b2']) for k, v in r705['runs'].items()))
    cases.append((name, 'a mutated copy of b705`s banks, standing-b2 removed (standing-b1 and standing-b3 alone: a gap in the numbering)', OLD.reading(name, pl5)[0], RA.reading(name, pl5)[0], (True, False)))
    # ### (4) the rowgen roster: b698`s paths against the re-pointed
    old_ro = [(n_, p) for n_, p in R.roster()]
    new_ro = roster707()
    old_present = all(os.path.exists(os.path.join(PP, p)) for _n, p in old_ro)
    new_present = all(os.path.exists(os.path.join(PP, p)) for _n, p, _f in new_ro)
    L += ['### the rowgen roster: b698`s 19 paths, present at PLACE-papers HEAD %s (missing %d) ; re-pointed through data/b706_partners.json: %d re-pointed, present %s' % (
        old_present, sum(1 for _n, p in old_ro if not os.path.exists(os.path.join(PP, p))), sum(1 for _n, _p, f in new_ro if f), new_present), '']
    cases.append(('rowgen roster', 'every roster path present at PLACE-papers HEAD (b698`s roster: old ; re-pointed: repaired)', old_present, new_present, (False, True)))
    cases.append(('rowgen roster', 'the roster 19 tables, the same names in the same order', [n_ for n_, _p in old_ro] == [n_ for n_, _p, _f in new_ro] and len(old_ro) == 19, len(new_ro) == 19, (True, True)))
    # ### (5) prev_capture: b706`s form (this session, from the previous act`s combine) against b701`s (the previous act`s own session)
    rows_this = ER.capture(SESSION, K.PREV_ANCHOR, SUBAGENTS)
    first_this = [r_['ts'] for r_ in rows_this if '%s_checks_postpush' % PREV in r_['cmd'] and '--combine' in r_['cmd']]
    new_rows = prev_capture()
    L += ['### the previous window: b706`s form over this session %s from (R316)`s anchor: %d commands, the previous act`s combine among them %s ; b701`s form over %s: %d commands from %s, every one marked b706 %s' % (
        K.SESSION_ID[:8], len(rows_this), bool(first_this), K.PREV_SESSION[:8], len(new_rows), new_rows[0]['ts'] if new_rows else '-', all(r_['src'].startswith(PREV) for r_ in new_rows)), '']
    cases.append(('prev_capture', 'the previous act`s window read: its post-push combine found and the commands after it read', bool(first_this), bool(new_rows) and all(r_['src'].startswith(PREV) for r_ in new_rows), (False, True)))
    # ### (6) ROOT_EXCLUDE extended by declaration (b706`s cases with this act`s names)
    SELF = sys.modules[__name__]
    keep = SELF.declared_untracked
    try:
        SELF.declared_untracked = lambda: []
        p_none = SELF._root_exclude()
        SELF.declared_untracked = lambda: [('b707_x.py', 'x_units.jsonl')]
        p_decl = SELF._root_exclude()
    finally:
        SELF.declared_untracked = keep
    pat6 = P6.R.ROOT_EXCLUDE if hasattr(P6, 'R') else R.ROOT_EXCLUDE
    old_m = bool(re.compile(pat6.pattern.replace('b706_', 'b707_')).match('b707_x_units.jsonl'))
    cases.append(('ROOT_EXCLUDE', 'no tool declares an untracked write: b707_x_units.jsonl excluded by name (old: b706`s pattern with the act renamed)', old_m, bool(p_none.match('b707_x_units.jsonl')), (False, False)))
    cases.append(('ROOT_EXCLUDE', 'a tool declares data/b707_x_units.jsonl untracked: the file excluded by name', old_m, bool(p_decl.match('b707_x_units.jsonl')), (False, True)))
    cases.append(('ROOT_EXCLUDE', 'the declaration present: a bank of a committed kind (b707_onset.txt) still named', not pat6.match('b706_onset.txt'), not p_decl.match('b707_onset.txt'), (True, True)))
    ok = True
    for nm_, src, o, nw, want in cases:
        asw = (bool(o), bool(nw)) == want
        ok = ok and asw
        L.append('  %-20s | %s | old %-5s | repaired %-5s | wanted old %s, repaired %s | %s' % (nm_, src, bool(o), bool(nw), want[0], want[1], 'AS WANTED' if asw else '### NOT AS WANTED'))
    dist = [n_ for n_, _s, o, nw, _w in cases if bool(o) != bool(nw)]
    L += ['', '### ### **CASES %d ; AS WANTED %s ; EACH REPAIRED READING DISTINGUISHED FROM THE OLD ON A ROW: %s.**' % (len(cases), ok, sorted(set(dist)))]
    put_txt('%s_repair_controls.txt' % ACT, L)
    print(NL.join(L[5:]))


# ================================================================================ COMPONENT 1: THE ORDER LINES (the two unbanked mentions, (R317)(2)); Component 3 appends the port`s
ORDERS = [
    (K.ORDER_TAG_PRINTS, 'W-ORD-ENTRY-TAG-PRINTS',
     '*Appended 2026-10-22 by b707 beneath `W-ORD-ENTRY-TAG-PRINTS` (:15590; discharged at :15642), under `(R317)`(2) -- THE REMAINDER ENTERED, THE TWO UNBANKED MENTIONS:*',
     ' the two mentions b706’s re-read left unbanked (relay data/b706_cells_reread.txt: 11 re-read, 9 equal, 0 differs, 2 unbanked), each named by '
     'paper and line with what its line cites. (1) SIMPLICITY_OF_RIEMANN_ZEROS :442 (the joint-step row) names the Prop `simplicity` at '
     'SIDE-explicit-formula v0.17 = `5a1630b` by `simplicity_iff` -- a tag no print bank holds; priced at one dispatch at b708 in b706’s form (a '
     'scratch branch cut at v0.17 carrying the workflow at main, a one-name print list and a root ChainProbe.lean naming `simplicity_iff`, the '
     'branch deleted after its bank). (2) FACES_LEDGER :20 (the F1 row, the finite-instance identity) names no kernel and no tag -- b704’s reader '
     'took it as a mention by the words “explicit formula” (relay data/b704_cells_reach.txt :78); nothing to print, no dispatch priced, the row '
     'read as it stands. The ruling’s “the tag each cites” the navigator’s (e) (relay data/b707_defects.txt), the second line citing none. '
     'Trigger: b708 (the first). Status OPEN.'),
]


def orders(*a):
    """the order lines appended to OPEN_TRAILS through b698's guarded landing, each beneath its order by its line (the ledger is append-only);
    data/b707_orders.json. `orders [dry] [<n>]`: one line by its index, or every line."""
    dry = 'dry' in a
    idx = [int(x) for x in a if x.isdigit()]
    sel = [ORDERS[i] for i in idx] if idx else ORDERS
    land([('OPEN_TRAILS.md', h, NL + h + b + NL) for _ln, _nm, h, b in sel], '%s_orders%s.json' % (ACT, ('_%d' % idx[0]) if idx else ''), 'orders', entry=None,
         check=[('OPEN_TRAILS.md', ln, nm) for ln, nm, _h, _b in sel], dry=dry)


ROUTES = dict(verdicts=verdicts, commands=commands, kernels=kernels, standing=standing, armsecs=armsecs, desk=desk, gatebanks=gatebanks,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry,
              c1=c1, repairs=repairs, tablescope=tablescope, repairctl=repairctl, orders=orders)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b707_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
