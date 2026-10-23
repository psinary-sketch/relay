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
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py (?:port)?dispatch\b(?![^\n]*\bdry\b)', re.M)   # ### b707: the port`s route is `portdispatch`


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


# ================================================================================ COMPONENT 4: THE REGISTRATIONS RE-READ, (R317)(4), AND THE NEXT AXIS
def regcheck(*a):
    """data/b707_registrations_reread.txt (.json): data/b707_registrations.txt re-read whole after the computations of Components 2 and 3 and
    compared byte for byte with the blob committed alone at step zero (relay 6e8ece87, before any computation of this act); printed unchanged;
    the next axis named for b709 from data/b705_i6_ranking.txt`s ranking line :58 ((e) representation coordinates), beside the ruling`s
    higher-pairs route of (R317)(4) computed there."""
    now = rd(os.path.join(D, '%s_registrations.txt' % ACT)) or ''
    then = _show(ROOT, K.REG_COMMIT, 'data/%s_registrations.txt' % ACT) or ''
    head_blob = g(ROOT, 'rev-parse', 'HEAD:data/%s_registrations.txt' % ACT).strip()
    then_blob = g(ROOT, 'rev-parse', '%s:data/%s_registrations.txt' % (K.REG_COMMIT, ACT)).strip()
    work_blob = g(ROOT, 'hash-object', '--', 'data/%s_registrations.txt' % ACT).strip()
    rk = (rd(os.path.join(D, 'b705_i6_ranking.txt')) or '').replace(chr(13), '').split(NL)
    l58 = rk[57] if len(rk) >= 58 else ''
    axis_ok = l58.strip().startswith('2. (e) representation coordinates')
    same = now == then and work_blob == then_blob == head_blob
    L = ['%s -- COMPONENT 4, (R317)(4): THE REGISTRATIONS RE-READ AFTER THE COMPUTATIONS, UNCHANGED; THE NEXT AXIS NAMED (%s)' % (ACT, utc()), '',
         '### data/b707_registrations.txt committed alone at relay %s before any computation (N3); re-read now: the working file`s blob %s ; the blob at %s %s ; '
         'at HEAD %s ; EQUAL BYTE FOR BYTE %s' % (K.REG_COMMIT, work_blob[:12], K.REG_COMMIT, then_blob[:12], head_blob[:12], same),
         '### the next axis for b709, from data/b705_i6_ranking.txt :58: %r -- (e) representation coordinates, the Weil form as a Hermitian-Toeplitz / prolate '
         'operator on the Sonin complement, its least eigenvalue the sign (the ranking`s second row, 4; this act computed the first, (d`), the support radius); '
         'beside it the higher pairs` route (R317)(4) registers in this bank, computed at b709' % l58.strip(), '',
         '### THE REGISTRATIONS, PRINTED UNCHANGED:'] + ['    ' + x for x in now.rstrip(NL).split(NL)]
    L += ['', '### ### **REGISTRATIONS RE-READ: UNCHANGED SINCE %s %s ; THE NEXT AXIS (e) REPRESENTATION COORDINATES (data/b705_i6_ranking.txt :58) %s ; NO FIGURE OF THE ROUTE COMPUTED THIS ACT.**' % (
        K.REG_COMMIT, same, axis_ok)]
    put_txt('%s_registrations_reread.txt' % ACT, L)
    put_json('%s_registrations_reread.json' % ACT, dict(at=utc(), commit=K.REG_COMMIT, work_blob=work_blob, then_blob=then_blob, head_blob=head_blob, unchanged=same,
                                                        next_axis='(e) representation coordinates', ranking_line=58, ranking_text=l58.strip(), axis_ok=axis_ok))
    print(NL.join(L[2:5] + L[-1:]))


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
    (K.ORDER_LV_JOIN_HELD, 'W-ORD-LV-CLOSURE-JOIN',
     '*Appended 2026-10-22 by b707 beneath `W-ORD-LV-CLOSURE-JOIN` (:15452; the join held at :15634), under `(R317)`(5) and the author’s word at this act’s second prompt -- THE ORDER **`W-ORD-LV-FORWARD-PORT`**, ENTERED AND OPENED:*',
     ' the forward-port of SIDE-lv-conservation’s deposit v0.10.0 = 93c27ec to the shared pin (Lean v4.34.0-rc1, Mathlib de5ce8a9, '
     'SIDE-explicit-formula’s), on the branch port-b707 cut at 93c27ec and pushed alone in branch mode at 69e239d (relay '
     'data/b707_port_push_out.txt): five files -- lean-toolchain and lake-manifest.json moved to the pin, lakefile.lean :12’s rev beside them, '
     'GammaBounds.lean :177’s rw given its beta-reduced goal by a `show` (the join’s hold of :15634), and SIDE-explicit-formula’s '
     'build-module.yml at main (badaccc) carried verbatim, the tree at 93c27ec carrying no workflow -- each printed before the one commit, '
     'every diff banked, no identifier in the workflow (data/b707_port_files.txt). One dispatch at the branch (run 39888369981, read by its '
     'id, the artifact’s sha256 verified): the cache served (8,691 files), GammaBounds built, and the build HELD at '
     'SIDELvConservation/C7OrderBounds.lean :277:55 (“Application type mismatch”: `WeakFEPair.hasMellin` takes the hypothesis `k < re s` '
     'before its argument at Mathlib de5ce8a9) with :380:8 beside it (the kernel’s unknown constant '
     '`exists_norm_completedRiemannZeta₀_le_exp_half`, a Mathlib name moved) -- 6 of 12 modules built (Smoke, T1_MellinFactorization, '
     'ZeroCarrier, GammaBounds, T2_SDarkness, T3_StepNineBridge), the price restated as 6 files built of 15, 6 modules remaining '
     '(C7FiniteTypeFalse, C7OrderBounds, CouplingsAtPhi, DirichletC7Order, PartialPositivity, RegisterPentagon); the print step not run '
     '(print_targets.txt absent at 93c27ec), no grade claimed, the run’s conclusion failure by that step alone (data/b707_port.txt, '
     'data/b707_buildlog_SIDE-lv-conservation_port.txt). No merge, no tag; port-b707 kept at the remote. THE ORDER: the port continued '
     'module by module on port-b707 at one dispatch per tree state, C7OrderBounds.lean :277 and :380 first; the join of '
     'W-ORD-LV-CLOSURE-JOIN re-dispatched only at a port that builds 12 of 12. The ruling’s “nothing else edited” the navigator’s (g) '
     '(relay data/b707_defects.txt). Trigger: the next ruling that names it (b709 the research act). Status OPEN.'),
]


def orders(*a):
    """the order lines appended to OPEN_TRAILS through b698's guarded landing, each beneath its order by its line (the ledger is append-only);
    data/b707_orders.json. `orders [dry] [<n>]`: one line by its index, or every line."""
    dry = 'dry' in a
    idx = [int(x) for x in a if x.isdigit()]
    sel = [ORDERS[i] for i in idx] if idx else ORDERS
    land([('OPEN_TRAILS.md', h, NL + h + b + NL) for _ln, _nm, h, b in sel], '%s_orders%s.json' % (ACT, ('_%d' % idx[0]) if idx else ''), 'orders', entry=None,
         check=[('OPEN_TRAILS.md', ln, nm) for ln, nm, _h, _b in sel], dry=dry)


# ================================================================================ COMPONENT 3: THE PORT, (R317)(5) AND THE AUTHOR`S WORD AT THE SECOND PROMPT
LV, EF, WF = K.LV_DIR, K.EF_DIR, K.WORKFLOW
LV_MODULES = ('C7FiniteTypeFalse', 'C7OrderBounds', 'CouplingsAtPhi', 'DirichletC7Order', 'GammaBounds', 'PartialPositivity', 'RegisterPentagon', 'Smoke',
              'T1_MellinFactorization', 'T2_SDarkness', 'T3_StepNineBridge', 'ZeroCarrier')   # ### SIDELvConservation/*.lean at 93c27ec (git ls-tree -r), 12
LV_OTHER_LEAN = ('AxiomCheck.lean', 'PinnedGoal.lean', 'lakefile.lean')                     # ### the three .lean files beside the 12 modules: the ruling`s 15


def portfiles(*a):
    """data/b707_port_files.txt (.json): the five files of the port branch, printed BEFORE the one commit -- each small file whole, the module`s
    repaired lines, the diff of each tracked file against 93c27ec (git diff), the carried workflow`s blob against SIDE-explicit-formula`s main
    blob (badaccc), the identifier needles in it (none), the manifest`s packages against SIDE-explicit-formula`s with lv-conservation`s own
    name kept, the toolchain at the shared pin, lakefile.lean :12`s rev at the shared pin."""
    import b706_checks as C6   # ### the identifier needles alone (IDENT_WF); imported inside the route, as b706`s wfstep did
    base, head = K.LV_V0100, g(LV, 'rev-parse', 'HEAD').strip()
    br = g(LV, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    tc = (rd(os.path.join(LV, 'lean-toolchain')) or '').replace(chr(13), '')
    lf = (rd(os.path.join(LV, 'lakefile.lean')) or '').replace(chr(13), '').split(NL)
    man = json.loads(rd(os.path.join(LV, 'lake-manifest.json')) or '{}')
    man_ef = json.loads(rd(os.path.join(EF, 'lake-manifest.json')) or '{}')
    wf_now = (rd(os.path.join(LV, *WF.split('/'))) or '').replace(chr(13), '')
    wf_blob = g(LV, 'hash-object', '--', WF).strip()
    ef_blob = g(EF, 'rev-parse', '%s:%s' % (K.EF_MAIN, WF)).strip()
    ef_main_blob = g(EF, 'rev-parse', 'main:%s' % WF).strip()
    ident = [w for w in C6.IDENT_WF if w in wf_now.lower()]
    gb = (rd(os.path.join(LV, 'SIDELvConservation', 'GammaBounds.lean')) or '').replace(chr(13), '').split(NL)
    diffs = {}
    for f in K.PORT_FILES:
        if f == WF:
            continue
        d = subprocess.run(['git', '-C', LV, 'diff', base, '--', f], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '').rstrip(NL)
        diffs[f] = d.split(NL) if d else []
    tracked_at_base = set((g(LV, 'ls-tree', '-r', '--name-only', base) or '').split(NL)) - {''}
    tc_ok = tc.strip() == K.EF_LEAN
    lf12 = lf[11] if len(lf) >= 12 else ''
    lf_ok = K.EF_MATHLIB in lf12 and sum(1 for l in lf if K.LV_MATHLIB in l) == 0
    man_ok = (man.get('packages') == man_ef.get('packages') and man.get('name') == 'sideLvConservation' and man.get('version') == man_ef.get('version')
              and any(p.get('rev') == K.EF_MATHLIB and p.get('name') == 'mathlib' for p in man.get('packages') or []))
    gb_ok = any(l.strip() == 'show exp (-1 / 2 * t) = exp (-t / 2)' for l in gb) and sum(1 for l in gb if 'rw [show (-1 / 2 : ℝ) * t = -t / 2 by ring]' in l) == 1
    gb_at = next((i + 1 for i, l in enumerate(gb) if l.strip() == 'show exp (-1 / 2 * t) = exp (-t / 2)'), 0)
    wf_ok = bool(wf_blob) and wf_blob == ef_blob == ef_main_blob and not ident and WF not in tracked_at_base
    changed = [l for l in (g(LV, 'status', '--short') or '').split(NL) if l.strip() and not l.endswith('.lp.log')]
    ok = tc_ok and lf_ok and man_ok and gb_ok and wf_ok and head == base and br == K.PORT_BRANCH and len(changed) == 5
    L = ['%s -- COMPONENT 3, (R317)(5) AND THE AUTHOR`S WORD AT THE SECOND PROMPT: THE PORT BRANCH`S FIVE FILES, PRINTED BEFORE THE ONE COMMIT (%s)' % (ACT, utc()), '',
         '### the branch %s cut at %s (v0.10.0, the deposit), checked out, HEAD %s (unmoved before the commit); the five files: the toolchain, the manifest,' % (br, base[:8], head[:8]),
         '### lakefile.lean, SIDELvConservation/GammaBounds.lean and SIDE-explicit-formula`s %s at main (%s) carried verbatim; each tracked file`s diff' % (WF, K.EF_MAIN[:8]),
         '### against %s by git diff; the workflow (untracked at %s) printed whole and its blob compared. Nothing else is edited.' % (base[:8], base[:8]), '',
         '### (1) lean-toolchain, whole: %r -> the shared pin %s: %s' % (tc.strip(), K.EF_LEAN, tc_ok)] + ['    ' + x for x in diffs.get('lean-toolchain', [])] + [
         '', '### (2) lakefile.lean, whole (:12 the rev moved to %s, the comment lines :7-:8 left as they stand -- the author`s word names the rev alone): %s' % (K.EF_MATHLIB[:8], lf_ok)]
    L += ['    %3d  %s' % (i + 1, l) for i, l in enumerate(lf)] + ['    ' + x for x in diffs.get('lakefile.lean', [])]
    L += ['', '### (3) lake-manifest.json: the packages block SIDE-explicit-formula`s main manifest`s (%d packages, mathlib at %s, Cli at %s), the manifest version %s, '
              'the root name kept %r: %s ; the diff against %s:' % (len(man.get('packages') or []), K.EF_MATHLIB[:8], next((p.get('inputRev') for p in man.get('packages') or [] if p.get('name') == 'Cli'), '-'),
                                                                   man.get('version'), man.get('name'), man_ok, base[:8])]
    L += ['    ' + x for x in diffs.get('lake-manifest.json', [])]
    L += ['', '### (4) SIDELvConservation/GammaBounds.lean: the one line repaired -- the `rw` at :177 whose target was the beta-redex `(fun x => rexp (-1 / 2 * x)) t = rexp (-t / 2)`',
          '### (b706`s run, relay data/b706_buildlog_SIDE-faces-join_join.txt :163-:178): a `show` of the beta-reduced goal placed before it (now :%d), the rw itself unchanged: %s' % (gb_at, gb_ok),
          '### the lines :170-:181 as they stand:'] + ['    %3d  %s' % (i + 1, gb[i]) for i in range(169, min(181, len(gb)))] + ['    ' + x for x in diffs.get('SIDELvConservation/GammaBounds.lean', [])]
    L += ['', '### (5) %s: carried verbatim from SIDE-explicit-formula`s main -- the working file`s blob %s ; SIDE-explicit-formula`s blob at %s %s ; at main %s ; EQUAL %s ; '
              'identifier needles %s ; absent at %s %s' % (WF, wf_blob[:12], K.EF_MAIN[:8], ef_blob[:12], ef_main_blob[:12], wf_blob == ef_blob == ef_main_blob, ident or 'NONE', base[:8], WF not in tracked_at_base),
          '### the workflow, whole:'] + ['    ' + x for x in wf_now.rstrip(NL).split(NL)]
    L += ['', '### the working tree (git status --short, the untracked .lp.log aside): %s' % changed,
          '', '### ### **FIVE FILES ON %s AT %s: TOOLCHAIN %s ; LAKEFILE :12 %s ; MANIFEST %s ; GAMMABOUNDS %s ; WORKFLOW BLOB EQUAL %s, IDENTIFIERS %s ; AS THE WORD ORDERS %s.**' % (
              br, base[:8], tc_ok, lf_ok, man_ok, gb_ok, wf_blob == ef_blob == ef_main_blob, ident or 'NONE', ok)]
    put_txt('%s_port_files.txt' % ACT, L)
    put_json('%s_port_files.json' % ACT, dict(at=utc(), branch=br, base=base, head=head, files=list(K.PORT_FILES), toolchain_ok=tc_ok, lakefile_ok=lf_ok, manifest_ok=man_ok,
                                               gammabounds_ok=gb_ok, show_line=gb_at, workflow_blob=wf_blob, ef_blob=ef_blob, workflow_equal=wf_blob == ef_blob == ef_main_blob,
                                               ident=ident, changed=changed, ok=ok, diffs=diffs))
    print(NL.join(L[2:6] + L[-1:]))


def portdispatch(*a):
    """`portdispatch <label> <target> [dry]`: b698`s dispatch form for a branch whose own tree carries the workflow -- the workflow run AT THE
    BRANCH (`--ref port-b707`) with the ref input the branch`s tip, one dispatch per tree state (refused where data/b707_dispatches.json carries
    the tree), the branch`s tip read back at the remote by one ls-remote before the dispatch; no print-list check (print_targets.txt is absent at
    93c27ec: the print step read as not run, the author`s word), the row banked with whole False and the reason."""
    label, target = a[0], a[1]
    repo = 'psinary-sketch/' + K.KERNEL
    full = g(LV, 'rev-parse', K.PORT_BRANCH).strip()
    tree = g(LV, 'rev-parse', full + '^{tree}').strip()
    j = jl('%s_dispatches.json' % ACT) if os.path.isfile(os.path.join(D, '%s_dispatches.json' % ACT)) else {}
    rows = j.get('rows') or []
    seen = [r for r in rows if r.get('tree') == tree]
    if seen:
        sys.exit('### THE TREE %s IS ALREADY BUILT (run %s) -- NOT DISPATCHED' % (tree[:12], seen[0].get('run_id')))
    if not re.match(r'^[A-Za-z0-9_. ]+$', target):
        sys.exit('### THE TARGET %r IS OUTSIDE THE LAKE GRAMMAR -- NOT DISPATCHED' % target)
    remote = (g(LV, 'ls-remote', 'origin', 'refs/heads/' + K.PORT_BRANCH).split() or [''])[0]
    print('  kernel %s ; branch %s ; tip %s ; the remote`s tip %s ; equal %s ; tree %s ; target %s' % (K.KERNEL, K.PORT_BRANCH, full, remote, remote == full, tree, target))
    if remote != full:
        sys.exit('### THE REMOTE`S %s IS NOT THE LOCAL TIP -- NOT DISPATCHED' % K.PORT_BRANCH)
    if 'dry' in a[2:]:
        return
    t0 = utc()
    rc, out, err = R._gh('workflow', 'run', 'build-module.yml', '-R', repo, '--ref', K.PORT_BRANCH, '-f', 'ref=' + full, '-f', 'target=' + target)
    if rc != 0:
        sys.exit('### THE DISPATCH REFUSED: %s' % err[-400:])
    run_id = None
    for _i in range(12):
        time.sleep(5)
        rc, out, err = R._gh('run', 'list', '-R', repo, '--workflow', 'build-module.yml', '--event', 'workflow_dispatch', '--limit', '5', '--json', 'databaseId,createdAt,status')
        new = [r for r in json.loads(out or b'[]') if r.get('createdAt', '') >= t0]
        if new:
            run_id = sorted(new, key=lambda r: r['createdAt'])[-1]['databaseId']
            break
    rows.append(dict(kernel=K.KERNEL, label=label, ref=full, tree=tree, target=target, dispatched=t0, run_id=run_id, whole=False, branch=K.PORT_BRANCH,
                     print_list='ABSENT AT 93c27ec -- the print step read as not run, no grade claimed (the author`s word at the second prompt)'))
    put_json('%s_dispatches.json' % ACT, dict(rows=rows))
    print('  dispatched %s at --ref %s ; run id %s' % (t0, K.PORT_BRANCH, run_id))


def portrun(*a):
    """`portrun <run id> <label>`: the port run read by its id -- b706`s runner706 clauses for the run and its artifact (chosen by name,
    its sha256 against the platform`s digest before any reading), the build`s exit, the memory log, the error lines; the outcome BY FILE AND LINE:
    the modules built (`Built SIDELvConservation.X`), the module held (`Building SIDELvConservation.Y` with ✖) and its first error line, the
    modules remaining of the 12 (the ruling`s "15" the 12 modules with AxiomCheck.lean, PinnedGoal.lean and lakefile.lean beside, not built by
    the target); the print step read as not run; NO GRADE CLAIMED. data/b707_port.txt (.json), the build log banked whole."""
    import hashlib
    import io as _io
    import zipfile
    run_id, label = int(a[0]), a[1]
    repo = 'psinary-sketch/' + K.KERNEL
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    art, arts = _artifact_named(repo, run_id, 'build-module-')
    art = art or {}
    T_ = {}
    sha = digest = None
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        if digest and digest == sha:
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    agree = bool(art) and bool(digest) and digest == sha
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    mem_low = int(low[-1]) if low else None
    stopped = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    bexit = T_.get('build_exit.txt', '').strip() or None
    errors = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    built = [m.group(1) for m in re.finditer(r'^[✔⚠] \[\d+/\d+\] Built SIDELvConservation\.(\w+)', blog, re.M)]
    held = [m.group(1) for m in re.finditer(r'^✖ \[\d+/\d+\] Building SIDELvConservation\.(\w+)', blog, re.M)]
    first_err = next((l for l in blog.split(NL) if re.match(r'^error: SIDELvConservation/\w+\.lean:\d+:\d+:', l)), None)
    remaining = [m for m in LV_MODULES if m not in built]
    cache = T_.get('cache.log', '')
    axioms = T_.get('axioms.txt', '').strip()
    ref_built = ' '.join(T_.get('ref.txt', '').split())
    row = dict(kernel=K.KERNEL, label=label, ref=run.get('headSha') or '', run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=sha if agree else None,
               mem_low=mem_low, stopped=stopped, build_exit=bexit, errors=errors, axioms_sha256=None, gate='NOT DERIVES',
               note='no grade claimed: the print step read as not run (print_targets.txt absent at 93c27ec), the author`s word')
    L = ['%s -- COMPONENT 3, (R317)(5): THE PORT RUN OF SIDE-lv-conservation AT THE SHARED PIN, READ BY ITS RUN ID; THE OUTCOME BY FILE AND LINE (%s)' % (ACT, utc()), '',
         '### the dispatch: the branch %s at its tip, the workflow at the branch, target SIDELvConservation (data/b707_dispatches.json)' % K.PORT_BRANCH,
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'), run.get('updatedAt')),
         '### the artifacts listed %d: %s ; the run`s own chosen by name (build-module-)' % (len(arts), [x.get('name') for x in arts]),
         '### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
             art.get('id'), art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN', 'AGREE' if agree else '### NOTHING READ FROM IT'),
         '### the ref built (out/ref.txt): %s' % (ref_built or '### UNREAD'),
         '### the cache (out/cache.log, last lines): %s' % ' | '.join(l for l in cache.rstrip(NL).split(NL)[-3:] if l),
         '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (mem_low, K.HOLD, stopped),
         '### the build: exit %s ; error lines %d:' % (bexit, len(errors))] + ['    ' + l for l in errors[:40]]
    L += ['### THE OUTCOME BY FILE AND LINE: modules built %d of %d: %s' % (len(built), len(LV_MODULES), built),
          '### the module held: %s ; its first error line: %s' % (held or 'NONE', first_err or 'NONE'),
          '### the modules remaining (not built by this run): %d %s' % (len(remaining), remaining),
          '### the ruling`s price restated: files built %d of 15 (the 12 modules, with %s beside them, not built by the target SIDELvConservation)' % (len(built), ', '.join(LV_OTHER_LEAN)),
          '### the print step: %s' % ('NOT RUN (print_targets.txt absent at 93c27ec; out/axioms.txt: %s)' % (axioms[:80] or 'ABSENT')),
          '### the lines after the held module (the log`s context, up to 24 lines):']
    if held:
        i0 = next((i for i, l in enumerate(blog.split(NL)) if ('Building SIDELvConservation.%s' % held[0]) in l), 0)
        L += ['    ' + l[:200] for l in blog.split(NL)[i0:i0 + 24]]
    else:
        L += ['    ' + l[:200] for l in blog.rstrip(NL).split(NL)[-12:]]
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; MODULES BUILT %d OF 12 (FILES %d OF 15) ; HELD AT %s ; '
              'REMAINING %d ; THE PRINT STEP NOT RUN ; NO GRADE CLAIMED.**' % (
                  run_id, label, run.get('conclusion'), 'AGREE' if agree else '### UNREAD', bexit, len(errors), len(built), len(built), (first_err or (held[0] if held else 'NONE')), len(remaining))]
    read_runner_row(row)
    put_txt('%s_port.txt' % ACT, L)
    if agree:
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, K.KERNEL, label), blog.rstrip(NL).split(NL))
        put_txt('%s_runner_%s_%s.txt' % (ACT, K.KERNEL, label), L)
    put_json('%s_port.json' % ACT, dict(at=utc(), run_id=run_id, run=run, artifact=dict(id=art.get('id'), name=art.get('name'), sha256=sha, digest=digest, agree=agree), ref_built=ref_built,
                                        mem_low=mem_low, stopped=stopped, build_exit=bexit, errors=errors, built=built, held=held, first_error=first_err, remaining=remaining,
                                        modules=list(LV_MODULES), print_step='NOT RUN', grade_claimed=False))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (K.KERNEL, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[2:10] + L[-1:]))


# ================================================================================ COMPONENT 5: THE FOUR STANDING FIGURES (b706`s tool, unedited, over b706`s roster)
def figures(*a):
    """data/b707_standing_figures.txt (.json): the four figures by relay tools/b706_standing_figures.py, unedited -- correspondence() and partners()
    over b706's roster (data/b706_roster_read.json, the 20 tables at the unversioned names), readme() b705's, pins() b703's -- each against
    b706's figure (data/b706_standing_figures.json), the pins baseline b706's rows."""
    import b706_standing_figures as SF6
    import b616_claims as KC0
    t0 = time.time()
    base = jl('b706_standing_figures.json')
    f = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
    t1 = time.time()
    pr = (f.get('partners') or {}).get('rows') or []
    cr = (f.get('correspondence') or {}).get('papers') or []
    L = ['%s -- COMPONENT 5: THE FOUR STANDING FIGURES AT b707, READ BY b706`S TOOL OVER b706`S ROSTER, AGAINST b706`S (%s)' % (ACT, utc()), '',
         '### by relay tools/b706_standing_figures.py, unedited (correspondence() and partners() over data/b706_roster_read.json, the 20 tables at the',
         '### unversioned names; readme() tools/b705_standing_figures.py`s, pins() tools/b703_standing_figures.py`s), %.0f s; each arm fails on a' % (t1 - t0),
         '### regression from the previous act`s figure (data/b706_standing_figures.json).', '']
    for k in ('correspondence', 'readme', 'partners', 'pins'):
        prev = (base.get(k) or {}).get('figure')
        now = (f.get(k) or {}).get('figure')
        L.append('  %-15s b707 %s ; b706 %s ; %s' % (k, now, prev, 'AT OR BELOW' if isinstance(now, int) and isinstance(prev, int) and now <= prev else '### ABOVE OR UNREAD'))
    L += ['', '### THE CORRESPONDENCE ROWS PER PAPER (current | behind | changed statement | unread ; the reason where the table is not read):']
    L += ['  %-36s %-66s current %3d behind %3d changed %3d unread %3d%s' % (p['paper'], p['path'], p['current'], p['behind'], p['changed'], p['unread'],
                                                                           (' ; ' + p['reason']) if p.get('reason') else '') for p in cr]
    L += ['', '### THE PARTNERS ROWS, ONE PER ROSTER TABLE:']
    L += ['  %-36s %-66s %s' % (r['paper'], r['path'], r.get('reason') or ('differing %s against %s' % (r.get('differing'), r.get('partner')))) for r in pr]
    one = sum(1 for r in pr if (r.get('reason') or '').startswith('ONE COPY'))
    L += ['', '### ### **FIGURES AT b707: CORRESPONDENCE %s ; README %s ; PARTNERS %s (ONE COPY %d OF %d TABLES) ; PINS %s -- AGAINST b706`S %s, %s, %s, %s ; THE ROSTER b706`S, %d TABLES.**' % (
        (f.get('correspondence') or {}).get('figure'), (f.get('readme') or {}).get('figure'), (f.get('partners') or {}).get('figure'), one, len(pr),
        (f.get('pins') or {}).get('figure'), (base.get('correspondence') or {}).get('figure'), (base.get('readme') or {}).get('figure'),
        (base.get('partners') or {}).get('figure'), (base.get('pins') or {}).get('figure'), len(cr))]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), roster='b706_roster_read.json', **dict((k, f.get(k)) for k in ('correspondence', 'readme', 'partners', 'pins'))))
    print(NL.join(L[:10] + L[-1:]))


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


def _jgz(name):
    import gzip
    try:
        return json.loads(gzip.decompress(open(os.path.join(D, name), 'rb').read()).decode('utf-8'))
    except Exception:
        return {}


def _n1():
    """N1: no lean process on this host; one runner dispatch (the port branch at its tip, the workflow at the branch), read by its run id with
    its artifact's sha256 verified; the print step not run and no grade claimed."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    rr = jl('%s_runner_rows.json' % ACT).get('rows') or []
    pj = jl('%s_port.json' % ACT)
    rows_ok = len(dj) == 1 and dj[0].get('run_id') == K.PORT_RUN and dj[0].get('ref') == K.PORT_COMMIT and dj[0].get('branch') == K.PORT_BRANCH and dj[0].get('whole') is False
    read_ok = len(rr) == 1 and rr[0].get('run_id') == K.PORT_RUN and re.match(r'^[0-9a-f]{64}$', rr[0].get('artifact_sha256') or '') is not None
    art_ok = (pj.get('artifact') or {}).get('agree') is True and pj.get('print_step') == 'NOT RUN' and pj.get('grade_claimed') is False
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == 1 and rows_ok and read_ok and art_ok
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches in the capture: %s (relay data/b707_commands.json); the dispatches '
        'bank (relay data/b707_dispatches.json): %s; the run read by its id with its artifact`s sha256 (relay data/b707_runner_rows.json): %s; the artifact '
        'agreeing with the platform`s digest %s, the print step %s, grade claimed %s (relay data/b707_port.json)' % (
            cm.get('local_lean') if cm else 'unread', len(cm.get('dispatches') or []) if cm else 'unread',
            ['%s %s at --ref %s run %s whole %s' % (d.get('label'), (d.get('ref') or '')[:7], d.get('branch'), d.get('run_id'), d.get('whole')) for d in dj],
            ['%s %s' % (r.get('label'), (r.get('artifact_sha256') or 'UNREAD')[:16]) for r in rr], (pj.get('artifact') or {}).get('agree'), pj.get('print_step'),
            pj.get('grade_claimed')))


def _n2():
    """N2: the registrations bank committed alone before any computation of the act and unchanged at the close; the onset's controls banked
    before any Q0 figure (the units' stamps)."""
    files = [x for x in g(ROOT, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.REG_COMMIT).split(NL) if x.strip()]
    reg_ct = _git_ct(ROOT, K.REG_COMMIT)
    oj = _jgz('%s_onset.json.gz' % ACT)
    U = oj.get('units') or []
    z = [_iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'terms' and u.get('obj') == 'zeta']
    q = [_iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'terms' and u.get('obj') == 'q0']
    c2 = [_iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'c2']
    first = min([x for x in z + q + c2 if x] or [0])
    rj = jl('%s_registrations_reread.json' % ACT)
    now = g(ROOT, 'hash-object', '--', 'data/%s_registrations.txt' % ACT).strip()
    then = g(ROOT, 'rev-parse', '%s:data/%s_registrations.txt' % (K.REG_COMMIT, ACT)).strip()
    alone = files == ['data/%s_registrations.txt' % ACT]
    before = bool(reg_ct) and bool(first) and reg_ct < first
    ctl_first = bool(z) and bool(q) and bool(c2) and all(z) and all(q) and all(c2) and max(z) < min(q) and max(c2) < min(q)
    ok = alone and before and now == then and rj.get('unchanged') is True and ctl_first and oj.get('c1_zeta_ok') is True
    return ('HELD' if ok else 'REFUTED'), (
        'the registrations` commit %s carrying %s alone: %s; its time %s before the onset`s first unit %s: %s; the blob now %s against the commit`s %s: %s, '
        're-read unchanged %s (relay data/b707_registrations_reread.json); the onset`s zeta units (%d) and C2 units (%d) all stamped before the first Q0 unit '
        '(%d): %s; C1 positive definite at every rung %s (relay data/b707_onset.json.gz through its hashes)' % (
            K.REG_COMMIT, files, alone, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(reg_ct)) if reg_ct else '-',
            R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(first)) if first else '-', before, now[:12], then[:12], now == then, rj.get('unchanged'),
            len(z), len(c2), len(q), ctl_first, oj.get('c1_zeta_ok')))


def _n3():
    """N3: the sign-onset radius: a* exists on the ladder for the band zero's family, at or below 2 log 192 and above log 4, with the ζ form
    positive definite at every rung of both frequencies and every Q0 rung read in balls -- or the falsifier fires as banked."""
    oj = _jgz('%s_onset.json.gz' % ACT)
    on = oj.get('onset') or {}
    band, rho = on.get('band') or {}, on.get('rho0') or {}
    rows = [r for r in oj.get('rows') or [] if r.get('obj') == 'q0']
    decided = bool(rows) and all(r.get('reading') in ('NEGATIVE DIRECTION BEYOND ITS BOUND', 'POSITIVE DEFINITE BEYOND ITS BOUND') for r in rows)
    try:
        a_star = float((band.get('a_star_radius') or ['0'])[0])
    except Exception:
        a_star = 0.0
    import math
    exists = bool(band.get('a_star')) and a_star > math.log(4) and a_star <= 2 * math.log(192) + 1e-9
    ok = decided and oj.get('c1_zeta_ok') is True and ((oj.get('hypothesis') == 'HELD' and exists) or (oj.get('falsifier_fired') is True and oj.get('hypothesis') == 'REFUTED'))
    return ('HELD' if ok else 'REFUTED'), (
        'the onset bank (relay data/b707_onset.txt; the gz through its hashes): the ladder %s, every Q0 rung decided in balls %s (%d rows); the band zero`s '
        'family a* = %s (a = %s), negative at %s; rho_0`s family a* = %s, negative at %s; the falsifier %s; the hypothesis %s (a* above log 4 and at or '
        'below 2 log 192: %s); C1 zeta positive definite at every rung of both frequencies %s; C2 as wanted %s' % (
            [r.get('rung') for r in oj.get('rungs') or []], decided, len(rows), band.get('a_star'), (band.get('a_star_radius') or ['-'])[0][:12], band.get('negative_at'),
            rho.get('a_star'), rho.get('negative_at'), 'FIRED' if oj.get('falsifier_fired') else 'NOT FIRED', oj.get('hypothesis'), exists, oj.get('c1_zeta_ok'),
            (oj.get('c2') or {}).get('ok')))


def _n4():
    """N4: the three readers' repairs each distinguished from the old on a control row; the mirror's dry run against b706's export clauses 1 and
    2 CLEAN and clause 3 NOT CLEAN by exactly the four names; the table's regeneration restoring the 18 rows; the split arm passing on b706's and
    b705's banks and failing every mutated copy."""
    z = rdn('%s_repair_controls.txt' % ACT)
    m = re.search(r'CASES (\d+) ; AS WANTED (\w+) ; EACH REPAIRED READING DISTINGUISHED FROM THE OLD ON A ROW: \[([^\]]*)\]', z)
    dist = set(re.findall(r"'([^']+)'", m.group(3))) if m else set()
    ro = rdn('%s_roster_control.txt' % ACT)
    m3 = re.search(r'in roster, MISSING from archive : (\d+)', ro)
    x3 = re.search(r'in archive, NOT in roster\s+: (\d+)', ro)
    miss = re.findall(r'MISSING : (\S+)', ro)
    ts = jl('%s_table_scope.json' % ACT)
    rows = [l for l in z.split(NL) if l.startswith('  G-RULE-SUITE-PARTS ')]
    arm_ok = len(rows) == 8 and all('AS WANTED' in r for r in rows) and 'old False | repaired True' in rows[0] and 'old True  | repaired True' in rows[1]
    roster_ok = 'CLAUSE 1 : CLEAN' in ro and 'CLAUSE 2 : CLEAN' in ro and bool(m3) and m3.group(1) == '4' and bool(x3) and x3.group(1) == '0' and sorted(miss) == sorted(RETIRED_FOUR)
    table_ok = ts.get('ok') is True and len(ts.get('gone') or []) == 12 and len(ts.get('restored') or []) == 18 and len(ts.get('grade_moved') or []) == 15 and not ts.get('other')
    ok = bool(m) and m.group(2) == 'True' and {'mirror_roster', 'terminal_table', 'G-RULE-SUITE-PARTS'} <= dist and roster_ok and table_ok and arm_ok
    return ('HELD' if ok else 'REFUTED'), (
        'the controls (relay data/b707_repair_controls.txt): cases %s, as wanted %s, distinguished %s; the roster`s dry run against b706`s export (relay '
        'data/b707_roster_control.txt): clause 1 CLEAN %s, clause 2 CLEAN %s, clause 3 MISSING %s %s, EXTRA %s; the table`s regeneration against b706`s final '
        '(relay data/b707_table_scope.json): gone %d, added %d, moved %d, restored %d, grades %d, other %d, as wanted %s; the split arm`s eight control rows as '
        'wanted %s' % (m.group(1) if m else '-', m.group(2) if m else '-', sorted(dist), 'CLAUSE 1 : CLEAN' in ro, 'CLAUSE 2 : CLEAN' in ro,
                       m3.group(1) if m3 else '-', sorted(miss), x3.group(1) if x3 else '-', len(ts.get('gone') or []), len(ts.get('added') or []),
                       len(ts.get('moved') or []), len(ts.get('restored') or []), len(ts.get('grade_moved') or []), len(ts.get('other') or []), ts.get('ok'), arm_ok))


RETIRED_FOUR = ('EXHAUSTIVENESS_LICENSE.md', 'TECHNE_TOOLKIT.md', 'R_CURVE_CRITERION.md', 'E_DIFFICULTY_THEOREM.md')


def _n5():
    import b633_record as R3
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    ef_ok = ef_main == K.EF_MAIN and not g(EF, 'tag', '--contains', K.EF_V037).replace('v0.37', '').strip()
    lv_main, lv_dep = g(LV, 'rev-parse', 'main').strip(), g(LV, 'rev-parse', 'v0.10.0^{commit}').strip()
    lv_port = g(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH).strip()
    lv_parent = g(LV, 'rev-parse', '--verify', '--quiet', K.PORT_COMMIT + '^').strip()
    lv_files = sorted(x for x in g(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.PORT_COMMIT).split(NL) if x.strip())
    lv_tags_past = [t for t in g(LV, 'tag', '--contains', K.PORT_COMMIT).split(NL) if t.strip()]
    lv_ok = lv_main == K.LV_MAIN and lv_dep == K.LV_V0100 and lv_port == K.PORT_COMMIT and lv_parent == K.LV_V0100 and lv_files == sorted(K.PORT_FILES) and not lv_tags_past
    join_main, join_tags = g(K.JOIN_DIR, 'rev-parse', 'main').strip(), g(K.JOIN_DIR, 'tag', '--list').strip()
    join_ok = join_main == K.JOIN_TIP and join_tags == ''
    allowed = set(K.PP_WRITTEN)
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in allowed]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    named_tools = ['tools/' + t for t in K.REPAIRED_TOOLS] + [p for p in K.REPAIRED_DATA]
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b707_', x) and x not in named_tools]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b707_|audit_b707_)', x) or re.match(r'^data/terminal_table', x)
                                                or x in named_tools or (x.startswith('data/') and x[5:] in R.N5_RELAY_DATA))]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B706_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(LV, lock)) if lock else []
    cj = jl('%s_commands.json' % ACT)
    ob = cj.get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    wf_lv = _show(LV, K.PORT_COMMIT, K.WORKFLOW) or ''
    wf_ef = _show(EF, K.EF_MAIN, K.WORKFLOW) or ''
    wf_ok = bool(wf_lv) and wf_lv == wf_ef and not any(w in wf_lv.lower() for w in ('psinary', 'seale', 'york', 'hotmail', 'orcid', 'secrets.'))
    chained = [d['n'] for d in (cj.get('delete_shapes') or []) if d.get('chained')]
    deleted = sorted(x for d in (cj.get('delete_shapes') or []) for x in (d.get('deletes') or []))
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl == pre_gl
    ok = k_ok and ef_ok and lv_ok and join_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ and arms_ok \
        and not amended and not ident and wf_ok and not chained and K.PORT_BRANCH not in deleted and gw_ok and gl
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it: %s; SIDE-lv-conservation`s main and '
            'deposit unmoved, port-b707 at its one commit on 93c27ec with the five files, no tag past it: %s; SIDE-explicit-formula`s main at badaccc, no tag '
            'past v0.37: %s; the join kernel`s main at its manifest commit, no tag: %s; the standing arms added beyond b706`s face, the act arms apart: %s (%s); '
            'shared tools edited beyond the two the ruling names and the roster: %s; sealed tools not agreeing: %s; commits amended after the seal: %s; deletes '
            'with anything chained after: %s; port-b707 deleted: %s; one git write per message (%s): %s; PLACE-papers beyond the two ledgers: %s; papers moved or '
            'renamed: %s; relay files of a kind beyond the act`s banks and tools, the two shared tools, the roster, the table, the root list, the corrigenda '
            'bank and b706`s push-out bank: %s; the glossary unchanged: %s; outbound requests other than git and gh %d, an identifier of the author in %s; no '
            'identifier in the workflow on the port branch, its text SIDE-explicit-formula`s at main: %s' % (
                K.DRAFT, k_ok, lv_ok, ef_ok, join_ok, added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE',
                chained or 'NONE', K.PORT_BRANCH in deleted, gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, len(ob),
                [r['line'] for r in ident] or 'NONE', wf_ok))


def scores(*a):
    """`scores [dry]` writes data/b707_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b707_scores_close.json."""
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
    return ('### b707 — lane two, act one hundred and thirty-four, the research act under (R317): b706 at its weight; the renames’ readers and the '
            'split arm repaired; the sign-onset radius at Q0 on the family at two frequencies; the twelve higher pairs’ route registered; '
            'lv-conservation’s forward-port opened and held at C7OrderBounds')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    ol = [x.get('line') for x in (jl('%s_orders.json' % ACT).get('lines') or [])] + [x.get('line') for x in (jl('%s_orders_1.json' % ACT).get('lines') or [])]
    oj = _jgz('%s_onset.json.gz' % ACT)
    on = oj.get('onset') or {}
    rows = dict(((r.get('obj'), r.get('freq'), r.get('rung')), r) for r in (oj.get('rows') or []))
    pj = jl('%s_port.json' % ACT)
    ts = jl('%s_table_scope.json' % ACT)
    rc = rdn('%s_repair_controls.txt' % ACT)
    m = re.search(r'CASES (\d+) ; AS WANTED (\w+)', rc)
    rr = jl('%s_registrations_reread.json' % ACT)
    fj_, f6 = jl('%s_standing_figures.json' % ACT), jl('b706_standing_figures.json')

    def ball(r, k, n=10):
        return ((r or {}).get(k) or ['-'])[0][:n]
    band_r = rows.get(('q0', 'band', (on.get('band') or {}).get('a_star') or ''))
    rho_r = rows.get(('q0', 'rho0', (on.get('rho0') or {}).get('a_star') or ''))
    return dict(corr_line=co.get('entry_line', '-'), orders=ol,
                band=(on.get('band') or {}).get('a_star'), band_a=ball(on.get('band') or {}, 'a_star_radius', 8), band_neg=(on.get('band') or {}).get('negative_at') or [],
                rho=(on.get('rho0') or {}).get('a_star'), rho_a=ball(on.get('rho0') or {}, 'a_star_radius', 8), rho_neg=(on.get('rho0') or {}).get('negative_at') or [],
                band_snn=ball(band_r, 'S_NN', 12), band_lmin=ball(band_r, 'lmin', 10), rho_snn=ball(rho_r, 'S_NN', 12), rho_lmin=ball(rho_r, 'lmin', 10),
                falsifier=oj.get('falsifier_fired'), hyp=oj.get('hypothesis'), c1=oj.get('c1_zeta_ok'), c2=(oj.get('c2') or {}).get('ok'),
                c2_n=len((oj.get('c2') or {}).get('rows') or []), rungs=[r.get('rung') for r in oj.get('rungs') or []],
                built=pj.get('built') or [], held=pj.get('held') or [], first_err=pj.get('first_error') or '-', remaining=pj.get('remaining') or [],
                port_run=pj.get('run_id'), port_conc=(pj.get('run') or {}).get('conclusion'),
                tgone=len(ts.get('gone') or []), tmoved=len(ts.get('moved') or []), trestored=len(ts.get('restored') or []), tgrades=len(ts.get('grade_moved') or []),
                tother=len(ts.get('other') or []), tdropped=len(ts.get('dropped') or []), cases=m.group(1) if m else '-', as_wanted=m.group(2) if m else '-',
                reg_unchanged=rr.get('unchanged'), axis=rr.get('next_axis'),
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')),
                figs6=dict((k, (f6.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


def _title():
    f = _figs()
    onset = ('a = 2 log %s = %s at the band zero’s family and 2 log %s = %s at ρ₀’s' % (f['band'], f['band_a'], f['rho'], f['rho_a'])) if f['band'] and f['rho'] else \
        'the form positive at every radius computed'
    rung = 'the rung none within a step at the band zero’s family, every rung named within the first step at ρ₀’s' if f['band'] else 'the rung none within a step'
    return ('## The sign-onset radius at the Epstein zeta of x² + xy + 6y², %s, %s; the ζ form positive at every radius; SIDE-lv-conservation’s '
            'forward-port at the shared pin, %d of 15 modules building; the twelve higher pairs’ route registered' % (onset, rung, len(f['built'])))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) the roster re-pointed to 70 entries on the author’s word -- the four rows re-pointed, the thirteen duplicates struck -- the ruling’s '
            '“rewritten to the 17 unversioned names” the navigator’s (f); (2) the port of five files on the author’s word, lakefile.lean’s rev and the '
            'workflow absent at 93c27ec the navigator’s (g), the print step read as not run and no grade claimed; (3) the onset’s family named at '
            'this act as span{C, N} at two frequencies, the band zero’s and ρ₀’s, the cross term by polarisation, b696’s tail bound carried to the '
            'sum window by its own inequality; (4) a* read HELD at the ladder’s last rung at the band zero’s family, where N alone is negative and '
            'the family adds no earlier direction, and at the first prime rung at ρ₀’s, the ladder coarse there; (5) the ruling’s root count, (l)’s '
            'owner and “the tag each cites” the navigator’s (c), (d), (e), entered by the fact clause; (6) G-WORKFLOW-FILES, G-RUNNER-READ and '
            'G-RUNNER-GATE declared failing on the held port run; (7) the three shared files edited before the weight line landed within Component 1, '
            'an event; (8) the %s navigator %s (%s) and the seat’s %s defect%s as lettered' % (
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
         'The research act’s four objects read: the sign-onset radius at Q0 on the family span{C, N} -- at the band zero’s ordinate a* = 2 log %s '
         '(a = %s), negative at %s alone, the least eigenvalue %s in the L2 metric; at ρ₀’s ordinate a* = 2 log %s (a = %s), negative from the first '
         'prime rung on -- the ζ form positive definite at every rung of both frequencies, the falsifier %s, the hypothesis %s; the twelve higher '
         'pairs’ route registered and priced before any number, computed at b709; SIDE-lv-conservation’s deposit ported to the shared pin on port-b707, '
         'one dispatch, %d of 12 modules built (%d of 15 files), GammaBounds among them, the build held at %s; and b706’s three readers repaired with '
         'their controls -- the roster to 70 entries, the table’s scope restoring %d rows, the split arm reading a lettered half as a half.' % (
             f['band'], f['band_a'], f['band_neg'], f['band_lmin'], f['rho'], f['rho_a'], 'fired' if f['falsifier'] else 'not fired', f['hyp'],
             len(f['built']), len(f['built']), (f['first_err'] or '-').replace('error: ', '').split(': ')[0], f['trestored']), '',
         '*Filed at b707 on the author’s ruling `(R317)` and the author’s words at its prompt; %d question%s put. Banks: relay '
         '`data/b707_tool_repairs.txt`, `data/b707_repair_controls.txt`, `data/b707_roster_control.txt`, `data/b707_table_scope.txt`, '
         '`data/b707_corrigendum.txt`, `data/b707_onset_controls.txt`, `data/b707_onset.txt`, `data/b707_registrations.txt`, '
         '`data/b707_registrations_reread.txt`, `data/b707_port_files.txt`, `data/b707_port.txt`, `data/b707_standing_figures.txt`, `data/b707_report.txt`.*' % (
             n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R317)`(1)-(2)): b706 entered at its weight (FINDINGS :%s); the generated entry at FINDINGS :%s answers b706’s seven '
         'post-seal items -- (i) the retired copies in the table’s ledger reach, (j) the root-bank arm’s required list, (k) fifteen rename commits '
         'named by range, (l) the lettered split parts, (m) the mirror’s roster, and the three trail-equality arms broken by defects lettered after '
         'the trail landed; the corrigenda bank appended at row (27); the sealed face, the trail and the root-named banks unedited.' % (c1_[0], f['corr_line']), '',
         '**The repairs** (`(R317)`(2), N4): the three readers the renames of (R316)(3) broke, each by the Edit tool with its diff and its control -- '
         'tools/mirror_roster.json re-pointed to 70 entries on the author’s word (four rows re-pointed, thirteen duplicates struck; the control '
         'tools/mirror_verify.py run dry against b706’s export: clauses 1 and 2 CLEAN, clause 3 NOT CLEAN by exactly the four names MISSING, relay '
         'data/b707_roster_control.txt); tools/terminal_table.py’s ledger walk bounded by path, the retired copies’ directory out (the regeneration '
         'against b706’s final table: %d rows gone, %d restored, %d grades, %d other, %d retired copies dropped; relay data/b707_table_scope.txt); '
         'tools/rule_arms.py’s G-RULE-SUITE-PARTS reading a lettered half as a half of the numbered half it splits, a family whole or by consecutive '
         'halves (passing on b706’s and b705’s run banks, failing every mutated copy); and the carry’s three (the rowgen roster re-pointed, prev_capture '
         'in b701’s form for another session, ROOT_EXCLUDE from the tools’ declarations) -- %s cases, as wanted %s (relay data/b707_tool_repairs.txt, '
         'data/b707_repair_controls.txt).' % (f['tgone'], f['trestored'], f['tgrades'], f['tother'], f['tdropped'], f['cases'], f['as_wanted']), '',
         '**The onset** (`(R317)`(3), N2, N3): the family named at this act, F_a(γ₀) = span{C, N} of b694’s centred and notched windows at one '
         'frequency, the Weil form S = P − PR + A in balls at 128 bits (b696’s terms and tail ball, b705’s contour, no zero tail) read as the 2×2 '
         'matrix G with the L2 Gram beside it, the cross term by polarisation; two frequencies, the band zero’s ordinate and ρ₀’s; the ladder %s. '
         'The controls before any Q0 figure: the rung structure (Λ_Q(2) = Λ_Q(3) = 0 computed, the first Q0 term at n = 4; the ζ side’s first at n = 2), '
         'C1 the ζ form POSITIVE DEFINITE at every rung of both frequencies (%s; at a = log 2 the source’s range cited by page, its conditions on ĝ not '
         'met by this family so the row is read, not taken as proven), C2 the form’s own machinery on the registered windows (b705’s at the band zero, '
         'b696’s at ρ₀, the Combo’s transform and the bilinearity; %d cases as wanted %s). The reading at Q0: the band zero’s family positive '
         'definite at every rung but the last, a* = 2 log %s (a = %s; S_NN %s, λ_min %s), the witness direction read negative beyond its bound; '
         'ρ₀’s family negative from the first prime rung, a* = 2 log %s (a = %s; S_NN %s, λ_min %s), the ladder coarse there (b696’s finer ladder '
         'placing the onset in (2 log 24, 2 log 32]); the ruling’s rungs log 2, log 3, log 4, log 5, log 7 all below the first prime rung, none within '
         'a later step; the falsifier %s; the hypothesis %s (relay data/b707_onset.txt, data/b707_onset_controls.txt; the binary bank beside its '
         'hashes).' % (f['rungs'], f['c1'], f['c2_n'], f['c2'], f['band'], f['band_a'], f['band_snn'], f['band_lmin'], f['rho'], f['rho_a'], f['rho_snn'],
                       f['rho_lmin'], 'FIRED' if f['falsifier'] else 'NOT FIRED', f['hyp']), '',
         '**The registrations** (`(R317)`(4), N2): data/b707_registrations.txt written by the Write tool and committed alone at relay %s before any '
         'computation of this act: the twelve off-line pairs beyond b675’s modulus rule (idx 5-16), each with the certified height the rule needs '
         '(154 to 442), the price by its arithmetic (256 bits, the onset cap 1.5 n*, 192 to 687 zeros by the count law’s bound, the tail ~ 2 A0 '
         'log(T0′)/T0′, the new certification above 149.72 the main cost), one alternative named (the prime-side sum, NOT PRICEABLE by b697’s '
         'reading), the hypothesis, falsifier and controls, computed at b709; re-read after the computations and unchanged %s (relay '
         'data/b707_registrations_reread.txt); the next axis for b709 named from data/b705_i6_ranking.txt :58: %s.' % (K.REG_COMMIT, f['reg_unchanged'], f['axis']), '',
         '**The port** (`(R317)`(5), N1): port-b707 cut at SIDE-lv-conservation’s deposit v0.10.0 = 93c27ec; on the author’s word five files -- '
         'lean-toolchain and lake-manifest.json moved to the shared pin, lakefile.lean :12’s rev beside them, GammaBounds.lean :177’s rw given its '
         'beta-reduced goal by a `show` (the join’s hold), SIDE-explicit-formula’s build-module.yml at main carried verbatim (the tree at 93c27ec '
         'carrying none) -- each printed before the one commit 69e239d with its diff banked, no identifier in the workflow, pushed alone in branch '
         'mode and read back (relay data/b707_port_files.txt); one dispatch at the branch (run %s), read by its id with the artifact’s sha256 '
         'verified: the cache served (8,691 files), %d of 12 modules built (%s), the build held at %s with :380:8 beside it (the kernel’s unknown '
         'constant, a Mathlib name moved), %d remaining (%s), the price restated as %d files built of 15; the print step not run (print_targets.txt '
         'absent at 93c27ec), no grade claimed, the run’s conclusion %s by that step alone; no merge, no tag, the branch kept; '
         'W-ORD-LV-FORWARD-PORT entered beneath the join’s hold (OPEN_TRAILS :%s).' % (
             f['port_run'], len(f['built']), ', '.join(f['built']), (f['first_err'] or '-').replace('error: ', '').split(': ')[0], len(f['remaining']),
             ', '.join(f['remaining']), len(f['built']), f['port_conc'], f['orders'][-1] if f['orders'] else '-'), '',
         '**The standing arms**: the four figures at b707 -- %s, %s, %s, %s -- against b706’s %s, %s, %s, %s, read by b706’s tool over b706’s roster '
         '(relay data/b707_standing_figures.txt); G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE declared failing on the held port run by '
         '(R317)(5)’s own clause and the author’s word; no standing arm added.' % (
             f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
             f['figs6']['correspondence'], f['figs6']['readme'], f['figs6']['partners'], f['figs6']['pins']), '',
         '**The orders** (`(R317)`(2), (5)): W-ORD-ENTRY-TAG-PRINTS’s remainder entered -- SIMPLICITY_OF_RIEMANN_ZEROS :442 at SIDE-explicit-formula '
         'v0.17 = 5a1630b priced one dispatch at b708, FACES_LEDGER :20 citing no tag, none; W-ORD-LV-FORWARD-PORT entered and opened beneath '
         'W-ORD-LV-CLOSURE-JOIN’s hold (OPEN_TRAILS :%s-:%s).' % (f['orders'][0] if f['orders'] else '-', f['orders'][-1] if f['orders'] else '-'), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed -- three entered by the fact clause (the root’s '
         'bank count 114 not 100, (l)’s owner, FACES_LEDGER :20 citing no tag) and two raised in one prompt before the components that cite them '
         '(the roster’s thirteen duplicates, the workflow absent at 93c27ec with lakefile.lean’s rev), every one the navigator’s; %d answer check%s, '
         'each before its answer was acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the four objects say one thing about the Weil face at Q0 -- the sign of its form is a '
         'threshold in the support radius, and the threshold is the window’s to find: at the band zero’s frequency the family sees no negative '
         'direction until the ladder’s last rung, at ρ₀’s it sees one from the first prime rung, so the onset radius is a property of the pair '
         '(frequency, family) and not of the form alone; the twelve higher pairs now carry a priced route to the same reading; and the kernel '
         'whose module held the join builds six of twelve at the shared pin, the remaining hold named by line. It strengthens the programme’s '
         'offering of a located clause by giving its measured face a second axis with a known-good lower range, and by moving the join’s price '
         'from one module of one kernel to six.', '',
         '**Carried to:** b708 (the re-cut act: the opening probe through the workflow’s step; SIMPLICITY :442’s print at v0.17; the licensed '
         'table’s next document); b709 (the research act: the higher pairs’ route as registered; the port’s next dispatch on port-b707, '
         'C7OrderBounds.lean :277 and :380 first; the next axis (e)); b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5); the next ruling (the five '
         'renames’ readers in the test files, no test edited this act); the draft held at v5.', '',
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
             '**(R317) ratified.** (1) b706 at its weight. (2) The readers’ repairs and the corrigendum. (3) The sign-onset radius. (4) The higher pairs’ '
             'route registered. (5) The forward-port. (6) The entry by its objects. (7) The branches. (8) The read-first bank. The draft held at v5. The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b706’s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s and :%s (the tag-prints remainder, '
             'W-ORD-LV-FORWARD-PORT entered); this record.' % (c1_[0], f['corr_line'], fj.get('entry_line'), f['orders'][0] if f['orders'] else '-', f['orders'][-1] if f['orders'] else '-'), '',
             '**Act root:** b707 `%s` (previous `%s`, b706’s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b707_author_answers.txt); the root’s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The repairs:** the roster to 70 entries, the table’s scope (%d rows restored), the split arm’s family reading, the carry’s three; %s cases as '
             'wanted %s (relay data/b707_tool_repairs.txt, data/b707_repair_controls.txt).' % (f['trestored'], f['cases'], f['as_wanted']), '',
             '**The onset:** a* = 2 log %s at the band zero’s family, 2 log %s at ρ₀’s; the ζ form positive definite at every rung; the falsifier %s; the '
             'hypothesis %s (relay data/b707_onset.txt).' % (f['band'], f['rho'], 'fired' if f['falsifier'] else 'not fired', f['hyp']), '',
             '**The registrations:** committed alone at relay %s before any computation, re-read unchanged %s; the next axis %s (relay '
             'data/b707_registrations.txt, data/b707_registrations_reread.txt).' % (K.REG_COMMIT, f['reg_unchanged'], f['axis']), '',
             '**The port:** port-b707 at `%s` on 93c27ec, five files, one dispatch (run %s), %d of 12 modules built, held at %s, the print step not run, '
             'no grade claimed, no merge, no tag (relay data/b707_port.txt).' % (K.PORT_COMMIT[:7], f['port_run'], len(f['built']), (f['first_err'] or '-').replace('error: ', '').split(': ')[0]), '',
             '**The kernels:** SIDE-lv-conservation’s port branch cut, pushed and dispatched once, its main and deposit unmoved; SIDE-explicit-formula’s '
             'main and tags unmoved; the join kernel unmoved; no lean or lake on this host.', '',
             '**The mirror:** the export made after this root in the b670 form over the re-pointed roster, its name in the closing (relay '
             'data/b707_closing.txt).', '',
             '**The open orders:** `W-ORD-LV-FORWARD-PORT` (entered: port-b707 held at C7OrderBounds.lean :277); `W-ORD-ENTRY-TAG-PRINTS` (its remainder, '
             'trigger b708); `W-ORD-LV-CLOSURE-JOIN` (the join held, re-dispatched at a port building 12 of 12); `W-ORD-EXPLICIT-FORMULA-C1`; '
             '`W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-STANDING-CLAUSES-BANK`; `W-ORD-KEYSTONE-HEADS`; `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA` '
             '(read at b705); `W-ORD-E0-MET-CLASSK` (its content done at b705); `W-ORD-README-FIGURE-SCOPE` (repaired at b705). Discharged this act: none.', '',
             '**The standing arms:** the four figures %s, %s, %s, %s against b706’s %s, %s, %s, %s; G-WORKFLOW-FILES, G-RUNNER-READ and G-RUNNER-GATE '
             'declared on the face as carried failures on the held port run (relay data/b707_standing_figures.txt, data/b707_port.txt).' % (
                 f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'], f['figs']['pins'],
                 f['figs6']['correspondence'], f['figs6']['readme'], f['figs6']['partners'], f['figs6']['pins']), '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b707_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R317).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b707_citation_check.txt), step zero (data/b707_ferry.txt, data/b707_readfirst.txt, data/b707_stepzero.txt, '
         'data/b707_tests_stepzero.txt, data/b707_rowgen_stepzero.txt, data/b707_branches.txt), the registrations committed alone (data/b707_registrations.txt)',
         '### COMPONENT 1 : b706`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s ; the three readers` repairs (data/b707_tool_repairs.txt, '
         'data/b707_repair_controls.txt, data/b707_roster_control.txt, data/b707_table_scope.txt) ; the tag-prints remainder (data/b707_orders.json) ; N4 %s' % (
             c1_[0], f['corr_line'], S['N4'][0]),
         '### COMPONENT 2 : the onset (data/b707_onset_controls.txt, data/b707_onset.txt, data/b707_onset_hashes.txt), a* = %s at the band zero`s family, %s at rho_0`s, '
         'the hypothesis %s ; N2 %s ; N3 %s' % (f['band'], f['rho'], f['hyp'], S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the port (data/b707_port_files.txt, data/b707_port.txt, data/b707_port_push_out.txt), run %s, %d of 12 built, held at %s ; '
         'W-ORD-LV-FORWARD-PORT (data/b707_orders_1.json) ; N1 %s' % (f['port_run'], len(f['built']), (f['first_err'] or '-').replace('error: ', '').split(': ')[0], S['N1'][0]),
         '### COMPONENT 4 : the registrations re-read (data/b707_registrations_reread.txt), unchanged %s ; the next axis %s' % (f['reg_unchanged'], f['axis']),
         '### COMPONENT 5 : the carry (data/b707_tool_repairs.txt rows (4)-(6)), the figures (data/b707_standing_figures.txt), the root route dry (data/b707_root_banks_dry.txt), '
         'the dry-run steps (data/b707_reg_gate.txt), the seal (data/b707_seal_hashes.json), the suite in seven parts, the per-part seconds (data/b707_arm_seconds.txt) ; S3 %s' % S['S3'][0],
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
    """b706's mbank (its span line read from the mirror bank chain) carried by copy with b707's names; the roster's re-pointed four read in the
    file list."""
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
    four_in = [n for n in RETIRED_FOUR if any(x.endswith(n) for x in files_)]
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names_), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE ROSTER RE-POINTED UNDER (R317)(2): 70 entries, the four re-pointed names carried %d of 4 (%s), files %d' % (len(four_in), four_in, len(files_)),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names_]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names_), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT), four_in=four_in))
    for l in L[:10]:
        print(l[:240])


def guard(*a):
    """data/b707_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the writes
    by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read by number."""
    import b707_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b707_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b707_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b707_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b707_checks.py :%d `%s`,'
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
    import b707_checks as CH
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
              figures=figures,
              mbuild=mbuild, mroot=mroot, mverify=mverify, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final,
              names=names, defshort=defshort, rowgen=rowgen, answers=answers, defects=defects, branches=branches, dispatch=dispatch,
              runstatus=runstatus, runner=runner, runwait=runwait, reads=reads, rootexclude=rootexclude, rootdry=rootdry,
              c1=c1, repairs=repairs, tablescope=tablescope, repairctl=repairctl, orders=orders, portfiles=portfiles, portdispatch=portdispatch, portrun=portrun,
              regcheck=regcheck)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b707_record.py <%s> [args]' % '|'.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
