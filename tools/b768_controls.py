# -*- coding: utf-8 -*-
"""tools/b768_controls.py -- (R378)(4): THE DISPATCHES OF THE PROOF FINISHED AND OF THE CLOSING BUILD FROM SOURCE, AND THEIR READS.
Carried from tools/b767_controls.py by tools/b768_carry.py (data/b768_carry_controls.txt, the names' substitution alone) and set for (R378)
by one scratch splice before its first run: the cites the substitution shifted onto b768's letters set back to b767's and b766's; the
trial's two kinds of b767 not carried ((R378)(4) THE DISPATCHES AND THE CAP, (9)); the seat's trial at small size a step with the restore
on, item a; the closing build by route (i), which [S2] holds (OPEN_TRAILS :19355), after a build with the restore on at that commit read
exit 0; the tag v0.46; the last hour of a step's dispatch; the checks before a dispatch of (4), b767 (n)'s among them.

THE BRANCH: every run of this act is dispatched AT push-b768-proof (`gh workflow run --ref push-b768-proof`, the commit to build given as
the input ref), the act's Lean branch cut from push-b767-proof at 89fd5b54 ((R378)(4), (9)), so that the run reads that branch's workflow
file, route (i) of data/b767_source_build.txt as main holds it at 89fd5b54, and the caches of that branch and of main. The commit sent is
the branch's remote tip, pushed by tools/push_gated.sh --branch.

THE ITEMS, each with the needle of its clause in the ferry bank (one line), its input restore and its lane:
  a          (4)(a), THE SEAT'S TRIAL AT SMALL SIZE, a step dispatch ; restore on ; lane steps
  b          (4)(b), L9c archJ_comb ; restore on ; lane steps          c   (4)(c), L11c arith_eq_comb ; restore on ; lane steps
  d          (4)(d), L11d window_arith_neg ; restore on ; lane steps   e   (4)(e), L12 controlFailureExists ; restore on ; lane steps
  closing    (4) MAIN AND THE TAG: the closing Lean commit built once from source by route (i), restore off, after a build with the restore
             on at that commit read exit 0; after it, the repeat alone ; lane source
  repeat     (4) THE DISPATCHES AND THE CAP: the one repeat of the closing build stopped under the hold (exit 143), at the stopped build's
             commit, its input and its branch ; lane source
THE CAP ((R378)(4), (9), N1): 40 (the worklist's MAX_DISPATCHES): at most 36 with the restore on (ON_CAP: the steps, the trial at small
size among them); with the restore off the closing build and one repeat of it. No cap by price row: a row past its upper figure is
printed in the report and asks no question ((R378)(3)).
THE LANES: one run read before the next is sent WITHIN a lane; the closing build's lane waits on the steps' only for the restored read at
its own commit.
THE HOUR ((R378)(3)): no dispatch of a step of (4) (a, b, c, d, e) later than 14 hours after the opening row (13:06:09Z): LAST_STEP,
2026-11-25T03:06:09Z. The closing build and its repeat are not steps.
THE CHECKS BEFORE A DISPATCH ((R378)(4), from b766's defects (g), (j), (k) and (l)), `presend <sha>`, read at each dispatch: (1) each Window
file at the commit opens, past its comments, with its imports; (2) each name the commit's Window lines newly carry (qualified, or
unqualified with an underscore, the tactics' names left out), and that no kernel file declares, found by a text search (`git grep -w -F`)
of the pinned Mathlib's source in the kernel's clone at the manifest's rev, or printed as not found; and beside the order, by b763 (i)'s
class (b767 defect (h)), each name's Mathlib declaration read against the changed file's own import closure (the kernel's import lines at
the commit, Mathlib's at the rev); (3) no declaration of a changed Window file that the kernel evaluates (by `decide`, or by `rfl` as its
proof or a tactic and not as an argument, b767 (m)) carries, in itself or in a declaration of the file it names, a list literal or a range of
more than KT_CAP 4,100 places (tools/b766_kdata.py :65):
cut in blocks before it is sent; (4) from b767 (n), each changed file's longest list literal read against the longest compiled at the
branch's base in a file without the option, or the file carrying the option kernel ed88b486 carries (`set_option maxRecDepth`). (1), (3),
(4) and a qualified name declared in Mathlib only outside the file's closure refuse; the rest prints.
THE RESTORE'S KIND ([H5]): exact, prefix or none, recorded beside each run with the line itself.
THE LEAN NAMES NO FREQUENCY: before each dispatch the files under SIDEExplicitFormula/Window/ at the commit are read for a decimal literal
and for a barred word (frequency, ordinate, riemannZeta); counts printed, no line.
THE VERDICTS: THE PAIR AT THE CLOSING COMMIT and by it MAIN AND THE TAG ((R378)(4)): AS WANTED, main moves by the gated push and v0.46 is
cut there after main's read-back; DIFFERS, [C7]; the closing build and its repeat each stopped, [C8]. trial_state() is b767's, kept for its
banks' readers; nothing of b768's reads it.
No lean process runs on this host (N1); each run is read by its run id from its downloaded artifact, the exit file governing. The kernel's
remote is read from its own git config at each call and its account printed masked; no account name is written by this tool.

  control [--bank]                       the tool's own controls, planted and printed (data/b768_controls_control.txt with --bank)
  targets <rev>                          the whole tree's targets at rev (print_targets.txt, each line resolved to its one module by
                                         tools/b757_join.py's reader), written to data/b768_targets_<sha8>.json for --targets-json
  lean <rev>                             the Lean text check over SIDEExplicitFormula/Window/ at rev, counts printed
  presend <rev>                          the checks before a dispatch at rev, printed
  dispatch <sha> <n> <item> --targets-json <file>   the holds, the cap, the lanes and the order, the hour, the licence (the ferry's
                                         bank), the commit the remote tip of the branch, the workflow's cache steps and route at the commit,
                                         the Lean text check, the checks before a dispatch, the targets modules of the tree; then gh
                                         workflow run at the branch; the row; the run id read back
  status <run> | download <run> | read <n> <run> | errors <run> | axioms <run> | compare <run_a> <run_b>   as b767's
  verdict                                the pair, main and the tag, printed
  bank                                   data/b768_controls.txt through standing.figbank: the controls, the dispatches and reads, the verdicts
"""
import calendar
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
for p_ in (T, os.path.join(T, 'standing')):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b768_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b768'
ROWS = os.path.join(D, 'b768_dispatch_rows.json')
BANK = os.path.join(D, 'b768_controls.txt')
CONTROL_BANK = os.path.join(D, 'b768_controls_control.txt')
ANSWERS = 'data/b768_ferry.txt'
RUNS = 'D:/b768-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
RUNS_ROLE = 'RUNS'         # ### the name a row gives that folder (no host folder written into a bank)
PREV_RUNS = (('D:/b765-runs', os.path.join(D, 'b765_dispatch_rows.json')),   # ### the earlier acts' artifacts, read by the positive
             ('D:/b767-runs', os.path.join(D, 'b767_dispatch_rows.json')))   # ### control of the restore's kind alone
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF = 'SIDE-explicit-formula'
KPATH = CT.KERNELS[EF]
WORKFLOW = 'build-module.yml'
BRANCH = K.WEIL_BRANCH[0]  # ### push-b768-proof, (R378)(4)
BASE_PROOF = K.WEIL_BRANCH_BASE   # ### 89fd5b54, push-b767-proof's commit and main's, the branch's base ((R378)(4), (9)): read from the worklist's WEIL_BRANCH_BASE, as b767's tool read its own after its WEIL_BRANCH[1] took the tip (data/b767_events.txt (111))
E0_TRIAL = 'e0baa6677f5c240acf5d8b802269e7e99ae6f004'   # ### b768's dispatch 1 (run 45439584241), read by the control of b768 (65) alone
TRIAL_COMMIT = 'f6f60590454d1a03847ced5067aba22ba28ebe1d'   # ### b767's trial commit, its opening Lean commit (route (i) alone): read by this tool's controls alone, b768 sending no trial ((R378)(4))
NO_ROUTE_COMMIT = '3c67b8b5'   # ### push-b766-proof's commit: the eight cache steps and no route (i), the controls' planted fault of the workflow's predicates
WF = '.github/workflows/build-module.yml'
ON_CAP = 36                # ### (R378)(4), (9): at most 36 with the restore on
OPENING = '2026-11-24T13:06:09Z'      # ### the opening row, relay f4243da1 (step 1)
LAST_STEP = '2026-11-25T03:06:09Z'    # ### (R378)(3): 14 hours after the opening row (data/b768_price.txt :48)
SECOND_ROUTE = None        # ### data/b767_source_build.txt names no second route ((ii) and (iii) not chosen); route (i) held by [S2] (OPEN_TRAILS :19355)
KT_CAP = 4100              # ### tools/b766_kdata.py :65: the places one declaration's kernel evaluation takes
MATHLIB = os.path.join(KPATH, '.lake', 'packages', 'mathlib')
STOPPED = 'STOPPED UNDER THE HOLD'
ACT_NS = 'SIDEExplicitFormula.Window.'   # ### the namespace of every declaration this act writes
LEAN_DIR = 'SIDEExplicitFormula/Window/'
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')
N4A = "THE SEAT'S TRIAL AT SMALL SIZE, a step dispatch with the restore on"   # ### data/b768_ferry.txt :21
N4B = '(b) L9c, archJ_comb'                   # ### :22
N4C = '(c) L11c, arith_eq_comb'               # ### :23
N4D = '(d) L11d, window_arith_neg'            # ### :24
N4E = '(e) L12, controlFailureExists'         # ### :25
N4CAP = 'THE DISPATCHES AND THE CAP.'         # ### :28
N4MAIN = 'MAIN AND THE TAG.'                  # ### :29
# ### each item: the needle of its clause, the input restore it sends (None: the stopped build's), its branch (None: the stopped build's);
# ### b768: b767's trial-on and trial-off not carried ((R378)(4), (9)); the seat's trial at small size a step, item a, with the restore on
ITEMS = {'a': (N4A, 'on', BRANCH),
         'b': (N4B, 'on', BRANCH), 'c': (N4C, 'on', BRANCH), 'd': (N4D, 'on', BRANCH), 'e': (N4E, 'on', BRANCH),
         'closing': (N4MAIN, 'off', BRANCH), 'repeat': (N4CAP, None, None)}
ON_ITEMS = ('a', 'b', 'c', 'd', 'e')
STEP_ITEMS = ('a', 'b', 'c', 'd', 'e')
OFF_ITEMS = ('closing',)
DEPTH_OPT = re.compile(r'set_option\s+maxRecDepth\s+\d+')   # ### b767 (n): the option kernel ed88b486 carries over each run of LogNatData.lean
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")
CACHE_KEYS = (('input', 'restore input: '), ('key', 'key: '), ('hit', 'restore hit: '), ('matched', 'restored key: '),
              ('files_before', 'files under .lake/build before the build: '), ('completed', 'build completed under the hold: '),
              ('present_before', 'key present before the save: '), ('save', 'save step: '))
QNAME = re.compile(r"(?<![A-Za-z0-9_.'])([A-Z][A-Za-z0-9_']*(?:\.[A-Za-z_][A-Za-z0-9_'!?]*)+)")
DECL_HEAD = re.compile(r"^(?:@\[[^\]\n]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
                       r"(?:theorem|lemma|def|abbrev|instance|example|structure|inductive|class|opaque|axiom)\b")
DECL_NAME = re.compile(r"\b(?:theorem|lemma|def|abbrev|instance|structure|inductive|class|opaque|axiom)\s+([^\s:(\[{⦃]+)")
DECL_KW = r"(theorem|lemma|def|abbrev|alias|instance|structure|class|inductive|opaque|irreducible_def)"
IMPORT_RE = re.compile(r'^(?:public\s+|private\s+)?(?:meta\s+)?import\s+(?:all\s+)?(.*)$')
SNAKE = re.compile(r"(?<![A-Za-z0-9_.'])([a-z][A-Za-z0-9']*_[A-Za-z0-9_']*[A-Za-z0-9'])(?![A-Za-z0-9_'])")
PROJ = frozenset(('mp', 'mpr', 'symm', 'trans', 'le', 'lt', 'ne', 'elim', 'out', 'mono', 'resolve_left', 'resolve_right', 'trans_le',
                  'trans_lt', 'not_lt', 'not_le', 'ge', 'gt', 'antisymm', 'imp', 'left', 'right', 'some', 'get', 'val', 'property', 'eq',
                  'ne_of_gt', 'ne_of_lt', 'comp', 'subst', 'trans_eq', 'congr_arg', 'congr_fun', 'pos', 'nonneg', 'one', 'two'))
TACTICS = frozenset(('norm_num', 'field_simp', 'push_cast', 'exact_mod_cast', 'simp_all', 'norm_cast', 'simp_rw', 'rw_mod_cast', 'apply_fun',
                     'by_contra', 'by_cases', 'set_option', 'simp_arith', 'native_decide', 'interval_cases', 'fin_cases', 'push_neg',
                     'apply_rules', 'conv_lhs', 'conv_rhs', 'exists_intro', 'refine_lift', 'simp_intro', 'split_ifs', 'zify_proof',
                     'maxHeartbeats', 'maxRecDepth'))
VENDORED = 'Vendored/Bulka/'      # ### lakefile.toml's srcDir for the vendored library (tools/b767_source_build.py SRC)
MATHLIB_SPEC = ['Mathlib', 'Mathlib.lean']


def lane(item):
    return 'source' if item == 'repeat' or item in OFF_ITEMS else 'steps'


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _epoch(utc):
    return calendar.timegm(time.strptime(utc, '%Y-%m-%dT%H:%M:%SZ'))


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def remote():
    """(owner/name, owner) from the kernel's own origin; the owner used only to mask prints and to call gh, never written."""
    u = git(KPATH, 'remote', 'get-url', 'origin').strip()
    m = re.search(r'github\.com[:/]([^/\s]+)/([^/\s]+?)(?:\.git)?/?$', u)
    if not m or m.group(2) != EF:
        sys.exit('### THE REMOTE OF %s NOT READ AS ITS OWN GITHUB REPOSITORY -- nothing done' % EF)
    return '%s/%s' % (m.group(1), m.group(2)), m.group(1)


def mask(text, owner):
    return text.replace(owner, '<account>') if owner else text


def disk():
    return dict((v, int(shutil.disk_usage(v).free // (1024 * 1024))) for v in ('C:/', 'D:/'))


def heads_now():
    """[(sha, ref)] from one ls-remote of the kernel's heads."""
    return [tuple(l.split('\t')) for l in subprocess.run(['git', '-C', KPATH, 'ls-remote', '--heads', 'origin'], capture_output=True, text=True,
                                                         encoding='utf-8', errors='replace').stdout.split(NL) if '\t' in l]


# ================================================================================ the cache's record, the minutes, the axioms
def cache_record(text):
    """out/cache_kernel.txt read: its eight fields, and restored (the input on, a key restored, exact or by the prefix, files under .lake/build
    before the build), by_prefix (restored, not by the exact key), saved (the build completed, the key not held before the save, the save step
    succeeded), from_source (no file under .lake/build before the build, no key restored) and untouched (the input off: nothing restored, the
    probe and the save not run); read False where a field is missing."""
    f = {}
    for l in (text or '').replace('\r', '').split(NL):
        for k, pre in CACHE_KEYS:
            if l.startswith(pre) and k not in f:
                f[k] = l[len(pre):].strip()
    f['read'] = all(k in f for k, _ in CACHE_KEYS)
    nb = int(f['files_before']) if str(f.get('files_before', '')).isdigit() else -1
    got = f.get('matched') not in (None, '', 'none')
    f['restored'] = f['read'] and f['input'] == 'on' and got and nb > 0
    f['by_prefix'] = f['restored'] and f['hit'] != 'true'
    f['saved'] = f['read'] and f['completed'] == 'true' and f['present_before'] != 'true' and f['save'] == 'success'
    f['from_source'] = f['read'] and nb == 0 and not got
    f['untouched'] = (f['read'] and f['input'] == 'off' and f['hit'] == 'none' and not got and nb == 0 and f['present_before'] == 'none'
                      and f['save'] in ('skipped', 'none'))
    return f


def restore_kind(c):
    """[H5]: exact (the restore line true, a key restored), prefix (the line false, a key restored by the prefix), none (no key restored, the
    line none, or false with no key restored); unread where the record is cut short."""
    c = c or {}
    if not c.get('read'):
        return 'unread'
    got = c.get('matched') not in (None, '', 'none')
    if got and c.get('hit') == 'true':
        return 'exact'
    if got and c.get('hit') == 'false':
        return 'prefix'
    return 'none'


def build_minutes(text):
    s = re.search(r'^build start (\S+)$', text or '', re.M)
    e = re.search(r'^build end (\S+)$', text or '', re.M)
    try:
        return round((_epoch(e.group(1)) - _epoch(s.group(1))) / 60.0, 1) if s and e else None
    except ValueError:
        return None


def run_minutes(created, updated):
    try:
        return round((_epoch(updated) - _epoch(created)) / 60.0, 1)
    except (ValueError, TypeError):
        return None


def mem_parts(mem):
    """the memory log's low before the PART TWO mark and after it (route (i)), each None where no sample stands there."""
    lows, part = {'one': None, 'two': None}, 'one'
    for l in (mem or '').replace('\r', '').split(NL):
        if l.startswith('PART TWO'):
            part = 'two'
        m = re.search(r'avail_mb=(\d+)', l)
        if m:
            v = int(m.group(1))
            lows[part] = v if lows[part] is None else min(lows[part], v)
    return lows


def axioms_compare(a, b):
    la = (a or '').replace('\r', '').rstrip('\n').split(NL) if (a or '').strip() else []
    lb = (b or '').replace('\r', '').rstrip('\n').split(NL) if (b or '').strip() else []
    same = sum(1 for x, y in zip(la, lb) if x == y)
    first = next((i + 1 for i, (x, y) in enumerate(zip(la, lb)) if x != y), None)
    if first is None and len(la) != len(lb):
        first = min(len(la), len(lb)) + 1
    return dict(lines_a=len(la), lines_b=len(lb), equal_positions=same, first_diff=first, equal=bool(la) and la == lb)


def axioms_of(text):
    out = {}
    for m in AX_DEP.finditer(text or ''):
        out[m.group(1)] = tuple(x.strip() for x in m.group(2).replace(NL, ' ').split(',') if x.strip())
    for m in AX_NONE.finditer(text or ''):
        out[m.group(1)] = ()
    return out


def axioms_read(text, targets):
    ax = axioms_of(text)
    outside = dict((n, a) for n, a in ax.items() if not set(a) <= set(STANDARD))
    missing = [t for t in targets if t not in ax]
    return dict(lines=len(ax), within=len(ax) - len(outside), outside=outside, missing=missing, sorryAx='sorryAx' in (text or ''))


def axioms_print(text, ax):
    t = (text or '').strip()
    errs = [l for l in t.split(NL) if ': error' in l or l.startswith('error')]
    if t.startswith('NOT RUN'):
        return 'NOT RUN: %s' % t.split(NL)[0][:200]
    if errs and not ax['lines']:
        return 'FAILED, NO AXIOMS LINE: %s' % errs[0][:300]
    if errs:
        return 'RAN WITH ERRORS (%d error lines, the first: %s)' % (len(errs), errs[0][:200])
    return 'RAN' if ax['lines'] else 'EMPTY'


def names_state(ax_text, build_exit, names):
    """[(name, COMPILED | NOT COMPILED, why)] for this act's names: COMPILED where the build exits 0 and the axioms file carries the name's line
    within the standard three."""
    ax = axioms_of(ax_text)
    out = []
    for n in names:
        if build_exit != '0':
            out.append((n, 'NOT COMPILED', 'the exit file %s' % build_exit))
        elif n not in ax:
            out.append((n, 'NOT COMPILED', 'no axioms line'))
        elif not set(ax[n]) <= set(STANDARD):
            out.append((n, 'NOT COMPILED', 'axioms outside the standard three: %s' % ', '.join(ax[n])))
        else:
            out.append((n, 'COMPILED', '[%s]' % ', '.join(ax[n])))
    return out


def wf_predicates(text):
    """the workflow file's cache predicates, b765's (R375)(4) eight, and route (i) of (R378)(5): with the restore off, part one the target's
    modules outside the Window folder by name, its exit kept, part two the target, not run where part one did not complete under the hold."""
    t = (text or '').replace('\r', '')
    return dict(
        input_restore=bool(re.search(r'^      restore:\n(?:        .*\n)*?        default: "off"$', t, re.M)) and '          - "off"\n          - "on"' in t,
        restore_step="if: inputs.restore == 'on'\n        uses: actions/cache/restore@v4" in t,
        key_commit='echo "key=$p$(git rev-parse HEAD)" >> "$GITHUB_OUTPUT"' in t and t.count('hashFiles(') == 1,
        restore_keys='restore-keys: ${{ steps.key.outputs.prefix }}' in t and 'echo "prefix=$p" >> "$GITHUB_OUTPUT"' in t,
        matched_recorded='steps.restore.outputs.cache-matched-key' in t and 'echo "restored key: ${MATCHED:-none}" >> out/cache_kernel.txt' in t,
        probe_gated=bool(re.search(r"if: always\(\) && inputs\.restore == 'on'(?: && inputs\.planted != 'on')? && steps\.built\.outputs\.ok == 'true'\n"
                                   r"        uses: actions/cache/restore@v4", t)) and 'lookup-only: true' in t,
        save_gated=(bool(re.search(r"if: always\(\) && inputs\.restore == 'on'(?: && inputs\.planted != 'on')? && steps\.built\.outputs\.ok == 'true' "
                                   r"&& steps\.probe\.outputs\.cache-hit != 'true'", t)) and 'uses: actions/cache/save@v4' in t),
        records='out/cache_kernel.txt' in t and 'out/build_times.txt' in t,
        route_two_parts=('if [ "$RESTORE" = "off" ]; then' in t and 'SIDEExplicitFormula.Window.*) ;;' in t
                         and 'lake build $(cat out/part_one_modules.txt) > out/build_part_one.log 2>&1' in t
                         and 'echo "$?" > out/build_part_one_exit.txt' in t and 'cp out/build_part_one_exit.txt out/build_exit.txt' in t
                         and 'lake build $TARGET > out/build.log 2>&1' in t))


B764_PREDICATES = ('input_restore', 'restore_step', 'records')   # ### true at 38a57e02; the other five from b765's workflow on


# ================================================================================ the Lean text
def lean_text_refusals(files):
    """[(path, why)] for each file of {path: text} carrying a decimal literal or a barred word; counts alone printed by the callers."""
    bad = []
    for p, t in sorted(files.items()):
        if DECIMAL.search(t or ''):
            bad.append((p, 'a decimal literal (%d)' % len(DECIMAL.findall(t))))
        if BARRED.search(t or ''):
            bad.append((p, 'a barred word (%d)' % len(BARRED.findall(t))))
    return bad


def lean_files(rev):
    names = [l for l in git(KPATH, 'ls-tree', '-r', '--name-only', rev, '--', LEAN_DIR).split(NL) if l.strip().endswith('.lean')]
    return dict((n, git(KPATH, 'show', '%s:%s' % (rev, n))) for n in names)


# ================================================================================ the checks before a dispatch ((R378)(4))
def strip_comments(text):
    t = re.sub(r'/-.*?-/', ' ', text or '', flags=re.S)
    return NL.join(l.split('--')[0] for l in t.replace('\r', '').split(NL))


def imports_first(text):
    """True where the file's first line past its comments opens with `import` (or the file is empty of code)."""
    for l in strip_comments(text).split(NL):
        if l.strip():
            return l.strip().startswith('import ')
    return True


def decls(text):
    """[(head line, body)] of the file's declarations, split at each line a declaration opens."""
    out, cur = [], None
    for l in strip_comments(text).split(NL):
        if DECL_HEAD.match(l):
            if cur:
                out.append(cur)
            cur = [l, [l]]
        elif cur:
            cur[1].append(l)
    if cur:
        out.append(cur)
    return [(h, NL.join(b)) for h, b in out]


def list_sizes(body):
    """the places of each top-level list literal in body: its commas at depth one, plus one."""
    sizes, depth, n = [], 0, 0
    for ch in body:
        if ch == '[':
            depth += 1
            if depth == 1:
                n = 1
        elif ch == ']' and depth:
            depth -= 1
            if depth == 0:
                sizes.append(n)
        elif ch == ',' and depth == 1:
            n += 1
    return sizes


def own_size(body):
    rng = [int(x) for x in re.findall(r'(?:List|Finset|Array)\.range\s+\(?(\d+)', body)]
    return max(list_sizes(body) + rng + [0])


def longest_compiled(rev):
    """b767 (n): the longest top-level list literal of the Window files at rev, in a file without the option kernel ed88b486 carries and in
    a file with it, each with its file; read at the branch's base, where each file compiled."""
    out = dict(without=0, without_file=None, with_=0, with_file=None)
    for p, t in sorted(lean_files(rev).items()):
        lg = max(list_sizes(strip_comments(t)) + [0])
        k = 'with_' if DEPTH_OPT.search(t or '') else 'without'
        if lg > out[k]:
            out[k], out[k.rstrip('_') + '_file'] = lg, p.replace(LEAN_DIR, '')
    return out


def depth_refusals(files, lc):
    """b767 (n), carried by (R378)(4): each file of {path: text} whose longest list literal passes the longest compiled without the option
    and which carries no `set_option maxRecDepth`."""
    out = []
    for p, t in sorted(files.items()):
        lg = max(list_sizes(strip_comments(t)) + [0])
        if lg > lc['without'] and not DEPTH_OPT.search(t or ''):
            out.append('%s: a list literal of %d places past the longest compiled here without the option, %d (%s), and no set_option '
                       'maxRecDepth (b767 (n))' % (p.replace(LEAN_DIR, ''), lg, lc['without'], lc['without_file']))
    return out


# ### b767 (m): `rfl` read as the kernel's evaluation only where it is the declaration's proof or a tactic (`:= rfl`, `by rfl`, `exact rfl`,
# ### `<;> rfl`, a line of its own), not where it is given as an argument (`Finset.sum_congr rfl ...`), which evaluates nothing
KEVAL = re.compile(r'\bdecide\b|:=\s*rfl\b|\bby\s+rfl\b|\bexact\s+rfl\b|<;>\s*rfl\b|^\s*rfl\s*$', re.M)


def eval_sizes(text):
    """[(head, places)] for each declaration the kernel evaluates (by `decide`, or by `rfl` as its proof or a tactic, KEVAL): the largest
    list literal or range in it, or in a declaration of the same file that it names (a table defined apart and evaluated by name, b766's
    KData form)."""
    ds = decls(text)
    sizes = {}
    for h, b in ds:
        m = DECL_NAME.search(h)
        if m:
            sizes[m.group(1)] = own_size(b)
    out = []
    for h, b in ds:
        if not KEVAL.search(b):
            continue
        m = DECL_NAME.search(h)
        me = m.group(1) if m else None
        refs = [v for k, v in sizes.items() if k != me and re.search(r"(?<![A-Za-z0-9_'])%s(?![A-Za-z0-9_'])" % re.escape(k), b)]
        out.append((h.strip()[:80], max([own_size(b)] + refs)))
    return out


def qnames(lines):
    """the qualified names of the lines past their comments, each with its trailing projections (.mp, .le, ...) cut away."""
    out = set()
    for l in lines:
        for m in QNAME.findall(strip_comments(l)):
            parts = m.split('.')
            while len(parts) > 2 and parts[-1] in PROJ:
                parts.pop()
            out.add('.'.join(parts))
    return sorted(out)


def snakes(lines):
    """the unqualified names with an underscore that the lines carry past their comments, the tactics' own names left out."""
    return sorted(set(m for l in lines for m in SNAKE.findall(strip_comments(l))) - TACTICS)


def ere(s):
    return re.sub(r'([.\[\]()*+?{}|^$\\])', r'\\\1', s)


def kmodule(path):
    return (path[len(VENDORED):] if path.startswith(VENDORED) else path)[:-5].replace('/', '.')


def mmodule(path):
    return path[:-5].replace('/', '.')


# ### b768 (data/b768_events.txt (66)): Lean reads a file's imports in its header alone; an `import` line in a doc comment's example
# ### (Mathlib/Tactic/FunProp.lean :48, `import Mathlib.Analysis.Complex.Trigonometric`) was read as an import, and the closure so read
# ### reached Mathlib.Algebra.Order.Ring.Abs from Packed.lean's six imports, which Lean's does not (run 45439584241). The header ends at
# ### the first doc comment, attribute, `public section` or command line; an import line past it is not read.
HEADER_END_ERE = (r'^(/-!|/--|@\[|public (section|noncomputable)|noncomputable |namespace |section|open |variable|universe |theorem |lemma |'
                  r'def |abbrev |instance|class |structure |inductive |example|set_option |attribute |macro|syntax |elab|end|#)')


def import_graph(repo, rev, pathspec, name_of):
    """{module: [the modules it imports]} from one git grep of the import lines and the header's end at rev (no line printed): an
    import line read only above the file's first line that ends its header (b768 (66))."""
    r = subprocess.run(['git', '-C', repo, 'grep', '-n', '-E', '-e', r'^(public |private )?(meta )?import ', '-e', HEADER_END_ERE, rev, '--']
                       + list(pathspec), capture_output=True)
    imps, ends, pre = {}, {}, rev + ':'
    for l in r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL):
        if not l.startswith(pre):
            continue
        try:
            path, ln, text = l[len(pre):].split(':', 2)
            ln = int(ln)
        except ValueError:
            continue
        if not path.endswith('.lean'):
            continue
        m = IMPORT_RE.match(text)
        if m:
            imps.setdefault(path, []).append((ln, m.group(1).split('--')[0].split()))
        else:
            ends[path] = min(ends.get(path, ln), ln)
    out = {}
    for path, xs in imps.items():
        e = ends.get(path)
        for ln, toks in xs:
            if e is None or ln < e:
                out.setdefault(name_of(path), []).extend(toks)
    return out


_MG = {}


def mathlib_graph(mrev):
    if mrev not in _MG:
        _MG[mrev] = import_graph(MATHLIB, mrev, MATHLIB_SPEC, mmodule)
    return _MG[mrev]


def file_imports(text):
    """the file's imports, read past its comments and above its header's end (b768 (66))."""
    out = []
    for l in strip_comments((text or '').replace('\r', '')).split(NL):
        m = IMPORT_RE.match(l)
        if m:
            out += m.group(1).split('--')[0].split()
        elif re.match(HEADER_END_ERE.replace('(section|noncomputable)', '(?:section|noncomputable)'), l):
            break
    return out


def mathlib_closure(tokens, kg, mg):
    """the Mathlib modules a file importing `tokens` sees: the kernel's modules reached through kg, their Mathlib imports closed through mg."""
    seen_k, todo, roots = set(), list(tokens), set()
    while todo:
        t = todo.pop()
        if t == 'Mathlib' or t.startswith('Mathlib.'):
            roots.add(t)
        elif t not in seen_k and t in kg:
            seen_k.add(t)
            todo.extend(kg[t])
    seen, todo = set(), list(roots)
    while todo:
        t = todo.pop()
        if t not in seen:
            seen.add(t)
            todo.extend(x for x in mg.get(t, ()) if x == 'Mathlib' or x.startswith('Mathlib.'))
    return seen


def kernel_closure(tokens, kg):
    """the kernel's modules a file importing `tokens` sees, through kg, a module with no import line among them (b767 (k))."""
    seen, todo = set(), list(tokens)
    while todo:
        t = todo.pop()
        if t == 'Mathlib' or t.startswith('Mathlib.') or t in seen:
            continue
        seen.add(t)
        todo.extend(kg.get(t, ()))
    return seen


def _chunks(items, n=80):
    items = sorted(items)
    return [items[i:i + n] for i in range(0, len(items), n)]


def decl_hits(repo, rev, lasts, pathspec, name_of):
    """{last: the modules whose file declares a name ending in `last`}, by batched git greps of the declaration lines (none printed)."""
    out, pre = dict((x, set()) for x in lasts), rev + ':'
    for ch in _chunks(lasts):
        a = ['git', '-C', repo, 'grep', '-E']
        for x in ch:
            a += ['-e', DECL_KW + r"[[:space:]]+([^[:space:]]*\.)?" + ere(x) + r"([^A-Za-z0-9_'!?.]|$)"]
        r = subprocess.run(a + [rev, '--'] + list(pathspec), capture_output=True)
        for l in r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL):
            if not l.startswith(pre):
                continue
            path, text = l[len(pre):].split(':', 1)
            for x in ch:
                if re.search(r"\b%s\s+(?:\S*\.)?%s(?:[^A-Za-z0-9_'!?.]|$)" % (DECL_KW, re.escape(x)), text):
                    out[x].add(name_of(path))
                    _MPATH[(repo, name_of(path))] = path
    return out


# ### b768 (data/b768_events.txt (59), (61)): a qualified name read against each declaration's full name, the namespaces open at its line
# ### read from the file's scope lines; before this, a declaration of the same last word in another namespace was read as declaring it
# ### (SkewMonoidAlgebra's sum_congr as Finset.sum_congr, made by @[to_additive] with no declaration line of its own; Stream'.Seq's
# ### cons_append as core's List.cons_append; the kernel's Schema.Family.sum_comm as Finset.sum_comm), and the trial was refused for them
_MPATH, _FULL = {}, {}
SCOPE_OPEN = re.compile(r'^\s*(?:@\[[^\]\n]*\]\s*)?(?:(?:noncomputable|public|private|meta)\s+)*(namespace|section|mutual)\b[ \t]*(\S*)')
SCOPE_END = re.compile(r'^\s*end\b')


def full_names(repo, rev, path, last):
    """the full names of the file's declarations of `last` at rev: the namespaces open at each declaration line (from the file's
    `namespace`, `section`, `mutual` and `end` lines past its comments) joined to the name as written; a name written from `_root_.` as
    written."""
    key = (repo, rev, path)
    if key not in _FULL:
        _FULL[key] = strip_comments(git(repo, 'show', '%s:%s' % (rev, path)))
    pat = re.compile(r"\b%s\s+((?:[^\s:(\[{⦃]*\.)?%s)(?:[^A-Za-z0-9_'!?.]|$)" % (DECL_KW, re.escape(last)))
    stack, out = [], set()
    for l in _FULL[key].split(NL):
        m = SCOPE_OPEN.match(l)
        if m:
            stack.append(m.group(2).split('.') if m.group(1) == 'namespace' and m.group(2) else [])
            continue
        if SCOPE_END.match(l):
            if stack:
                stack.pop()
            continue
        d = pat.search(l)
        if d:
            w = d.group(2)
            out.add(w[len('_root_.'):] if w.startswith('_root_.') else '.'.join([p for s in stack for p in s] + [w]))
    return out


OPEN_LINE = re.compile(r'^\s*open\s+(.*)$')
OPEN_STOP = ('in', 'hiding', 'renaming', 'scoped', 'private', 'public')


def file_opens(text):
    """b768 (data/b768_events.txt (65)): the namespaces an unqualified name of the file resolves in: the root (''), each namespace open in
    the file by its `namespace` lines with each of its prefixes, and each name an `open` line opens, alone and joined to those namespaces.
    Read wide: a namespace too many makes the reading find more declarations, so it can refuse less, never more."""
    ops, stack, scopes = set(['']), [], []
    for l in strip_comments(text).split(NL):
        m = SCOPE_OPEN.match(l)
        if m:
            parts = m.group(2).split('.') if m.group(1) == 'namespace' and m.group(2) else []
            scopes.append(parts)
            stack = [p for s in scopes for p in s]
            for k in range(1, len(stack) + 1):
                ops.add('.'.join(stack[:k]))
            continue
        if SCOPE_END.match(l):
            if scopes:
                scopes.pop()
            stack = [p for s in scopes for p in s]
            continue
        o = OPEN_LINE.match(l)
        if o:
            for w in re.findall(r"[A-Za-z_][A-Za-z0-9_'.]*", o.group(1).split('(')[0]):
                if w in ('in', 'hiding', 'renaming'):
                    break
                if w in OPEN_STOP:
                    continue
                ops.add(w)
                for k in range(1, len(stack) + 1):
                    ops.add('.'.join(stack[:k] + [w]))
    return ops


def ns_declaring(repo, rev, mods, n, opens=None):
    """the modules of `mods` whose file declares the qualified name n: a declaration whose full name is n or ends in `.n` (a name written
    from inside one of its namespaces). A declaration of n's last word in another namespace is not read as declaring n. An unqualified
    name with the file's `opens` read (b768 (65)): a declaration whose full name is n at the root or n in a namespace the file opens; with
    no `opens`, every module, as before."""
    if not mods:
        return set(mods)
    if '.' not in n:
        if opens is None:
            return set(mods)
        want = set(n if p == '' else p + '.' + n for p in opens)
        return set(m for m in mods if (repo, m) in _MPATH and any(f in want for f in full_names(repo, rev, _MPATH[(repo, m)], n)))
    last = n.rsplit('.', 1)[1]
    return set(m for m in mods if (repo, m) in _MPATH and any(f == n or f.endswith('.' + n) for f in full_names(repo, rev, _MPATH[(repo, m)], last)))


def text_found(mrev, lasts):
    """the `lasts` a text search of the pinned Mathlib's source finds as words ((R378)(4)'s search), by batched git greps."""
    found = set()
    for ch in _chunks(lasts):
        a = ['git', '-C', MATHLIB, 'grep', '-h', '-o', '-w', '-F']
        for x in ch:
            a += ['-e', x]
        r = subprocess.run(a + [mrev, '--'] + MATHLIB_SPEC, capture_output=True)
        found |= set(l.rsplit(':', 1)[-1] for l in r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL) if l) & set(ch)
    return found


def names_reading(added, imports, sha, mrev, kg, mg, own=None, opens=None):
    """the names a file's added lines newly carry: each found by a text search of the pinned Mathlib's source or printed as not found
    ((R378)(4)); and each Mathlib declaration read against the file's own import closure (b763 (i), b767 (h)): in it, only outside it, or no
    declaration line found (a name made by an attribute, a local, a field: printed, never refused). b767 (k): each name the kernel declares
    read against the file's own module and its kernel closure; one declared in the kernel only outside them, and by no Mathlib module
    within the closure, kept in kernel_outside. The added lines read past their comments as one text first, so a block comment over
    several lines names nothing (b767 (k)). b768 (data/b768_events.txt (61)): a qualified name, in the kernel and in Mathlib, declared
    only by a declaration whose full name is it or ends in it (ns_declaring), not by one of its last word in another namespace. b768 (65):
    with the file's `opens` (file_opens), an unqualified name declared only by a declaration at the root or in a namespace the file opens,
    so an unqualified Mathlib name so declared only outside the closure is refused by presend, as a qualified one is."""
    added = strip_comments(NL.join(added)).split(NL)
    q, s = qnames(added), snakes(added)
    names = q + [x for x in s if x not in set(n.split('.')[-1] for n in q)]
    last = dict((n, n.split('.')[-1]) for n in names)
    kd = decl_hits(KPATH, sha, sorted(set(last.values())), ['*.lean'], kmodule)
    km = dict((n, ns_declaring(KPATH, sha, kd.get(last[n]) or set(), n, opens)) for n in names)   # ### b768 (61), (65): by its namespaces
    kernel = sorted(n for n in names if km[n])
    rest = [n for n in names if n not in kernel]
    kclo = kernel_closure(imports, kg) | ({own} if own else set())
    kout = [n for n in kernel if not (km[n] & kclo)]
    rl = sorted(set(last[n] for n in rest))
    ml = sorted(set(rl) | set(last[n] for n in kout))
    fl = text_found(mrev, rl) if mrev and rl else set()
    md = decl_hits(MATHLIB, mrev, ml, MATHLIB_SPEC, mmodule) if mrev and ml else {}
    mm = dict((n, ns_declaring(MATHLIB, mrev, md.get(last[n]) or set(), n, opens)) for n in rest + kout) if md else {}
    clo = mathlib_closure(imports, kg, mg)
    out = dict(qualified=q, snake=[x for x in names if x not in q], kernel=kernel, found=sorted(n for n in rest if last[n] in fl),
               not_found=sorted(n for n in rest if last[n] not in fl), in_closure=[], outside={}, undeclared=[], closure=len(clo),
               kernel_outside={}, kclosure=len(kclo))
    for n in rest:
        mods = mm.get(n) or set()
        if not mods:
            out['undeclared'].append(n)
        elif mods & clo:
            out['in_closure'].append(n)
        else:
            out['outside'][n] = sorted(mods)[:3]
    for n in kout:
        if not ((mm.get(n) or set()) & clo):
            out['kernel_outside'][n] = sorted(km[n])[:3]
    return out


def mathlib_rev(sha):
    try:
        man = json.loads(git(KPATH, 'show', '%s:lake-manifest.json' % sha))
        return next(p['rev'] for p in man['packages'] if p['name'] == 'mathlib')
    except (ValueError, StopIteration, KeyError):
        return None


def mathlib_found(rev, last):
    r = subprocess.run(['git', '-C', MATHLIB, 'grep', '-l', '-w', '-F', '-e', last, rev, '--', 'Mathlib'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return [x.split(':', 1)[-1] for x in r.stdout.split(NL) if x.strip()]


def presend(sha):
    """(refusals, report) of the checks before a dispatch at sha, against the branch's base BASE_PROOF."""
    files = lean_files(sha)
    refusals, rep = [], dict(files=len(files))
    noimp = sorted(p for p, t in files.items() if not imports_first(t))
    rep['imports_first'] = dict(read=len(files), not_first=noimp)
    refusals += ['%s does not open with its imports' % p for p in noimp]
    changed = [p for p in git(KPATH, 'diff', '--name-only', BASE_PROOF, sha, '--', LEAN_DIR).split(NL) if p.endswith('.lean') and p in files]
    rep['changed'] = changed
    mrev = mathlib_rev(sha)
    mhead = git(MATHLIB, 'rev-parse', 'HEAD').strip()
    rep['mathlib'] = dict(rev=mrev, clone_head=mhead, equal=bool(mrev) and mrev == mhead)
    kg = import_graph(KPATH, sha, ['*.lean'], kmodule) if changed else {}
    mg = mathlib_graph(mrev) if changed and mrev else {}
    agg = dict(qualified=0, snake=0, kernel=0, found=0, not_found=[], in_closure=0, outside={}, undeclared=[], kernel_outside={})
    for p in changed:
        added = [l[1:] for l in git(KPATH, 'diff', '-U0', BASE_PROOF, sha, '--', p).split(NL) if l.startswith('+') and not l.startswith('+++')]
        r = names_reading(added, file_imports(files[p]), sha, mrev, kg, mg, own=kmodule(p), opens=file_opens(files[p]))
        for n, mods in r['kernel_outside'].items():
            agg['kernel_outside']['%s (%s)' % (n, p.replace(LEAN_DIR, ''))] = mods
            refusals.append('%s: %s declared in the kernel only outside the file`s import closure (%s), b767 (k)' % (
                p.replace(LEAN_DIR, ''), n, ', '.join(mods)))
        for k in ('qualified', 'snake', 'kernel', 'found', 'in_closure'):
            agg[k] += len(r[k])
        agg['not_found'] += r['not_found']
        agg['undeclared'] += r['undeclared']
        for n, mods in r['outside'].items():
            agg['outside']['%s (%s)' % (n, p.replace(LEAN_DIR, ''))] = mods
            # ### b768 (65): an unqualified name refused too, read at the root and the file's opens (run 45439584241: abs_mul, Packed.lean :182)
            refusals.append('%s: %s declared in Mathlib only outside the file`s import closure (%s)' % (p.replace(LEAN_DIR, ''), n, ', '.join(mods)))
    agg['not_found'] = sorted(set(agg['not_found']))[:60]
    agg['undeclared'] = sorted(set(agg['undeclared']))[:60]
    rep['names'] = agg
    big = []
    for p in changed:
        for h, s in eval_sizes(files[p]):
            if s > KT_CAP:
                big.append((p, h, s))
    rep['kt'] = dict(cap=KT_CAP, over=big, largest=max([s for p in changed for _h, s in eval_sizes(files[p])] + [0]))
    refusals += ['%s: %s evaluates %d places by decide, past KT_CAP %d' % (p, h, s, KT_CAP) for p, h, s in big]
    # ### b767 (n), carried by (R378)(4): the elaborator's depth, each changed file's longest list literal against the base's
    lc = longest_compiled(BASE_PROOF)
    dref = depth_refusals(dict((p, files[p]) for p in changed), lc)
    rep['depth'] = dict(base=lc, files=[(p.replace(LEAN_DIR, ''), max(list_sizes(strip_comments(files[p])) + [0]), bool(DEPTH_OPT.search(files[p])))
                                       for p in changed], refused=dref)
    refusals += dref
    if mrev and not rep['mathlib']['equal']:
        refusals.append('the Mathlib clone`s HEAD %s is not the manifest`s rev %s at %s' % (mhead[:8], mrev[:8], sha[:8]))
    return refusals, rep


def presend_lines(sha, refusals, rep):
    return ['### THE CHECKS BEFORE A DISPATCH AT %s ((R378)(4)): Window files %d, each opening with its imports: %s ; changed against %s: %d %s'
            % (sha[:8], rep['files'], 'ALL' if not rep['imports_first']['not_first'] else 'NOT %s' % rep['imports_first']['not_first'],
               BASE_PROOF[:8], len(rep['changed']), [p.replace(LEAN_DIR, '') for p in rep['changed']]),
            '    the Mathlib clone at %s, the manifest`s rev %s: %s ; names newly carried %d qualified and %d unqualified, declared in the kernel %d ; '
            'by the text search of the pinned Mathlib found %d, NOT FOUND %d %s' % (
                rep['mathlib']['clone_head'][:8], str(rep['mathlib']['rev'])[:8], 'EQUAL' if rep['mathlib']['equal'] else 'UNEQUAL',
                rep['names']['qualified'], rep['names']['snake'], rep['names']['kernel'], rep['names']['found'], len(rep['names']['not_found']),
                rep['names']['not_found'][:30]),
            '    against each file`s own import closure (b763 (i), b767 (h)): declared within it %d ; DECLARED ONLY OUTSIDE IT %d %s ; no declaration '
            'line found (an attribute`s name, a local, a field) %d ; THE KERNEL`S NAMES DECLARED ONLY OUTSIDE IT (b767 (k)) %d %s' % (
                rep['names']['in_closure'], len(rep['names']['outside']), sorted(rep['names']['outside'].items())[:12],
                len(rep['names']['undeclared']), len(rep['names']['kernel_outside']), sorted(rep['names']['kernel_outside'].items())[:12]),
            '    the kernel evaluations by decide in the changed files: the largest %d places against KT_CAP %d ; over it %d %s' % (
                rep['kt']['largest'], KT_CAP, len(rep['kt']['over']), rep['kt']['over'][:4]),
            '    the elaborator`s depth (b767 (n)): the longest list literal compiled at %s without the option %d (%s), with it %d (%s) ; the '
            'changed files` longest %s ; refused %d' % (BASE_PROOF[:8], rep['depth']['base']['without'], rep['depth']['base']['without_file'],
                                                   rep['depth']['base']['with_'], rep['depth']['base']['with_file'], rep['depth']['files'][:8],
                                                   len(rep['depth']['refused'])),
            '    THE CHECKS: %s' % ('CLEAR' if not refusals else 'REFUSED: %s' % '; '.join(refusals[:6]))]


# ================================================================================ the refusals
def dispatch_refusal(item, n, sha, rows, read, dk, ctx=None, now=None):
    """why a dispatch is refused before anything is sent, or None. Pure: the rows, the free read, the disk read, the time `now` and `ctx`
    (lean: the Lean text check's refusals, a list, None where not read; presend: the checks' refusals, None where not read) given."""
    ctx = ctx or {}
    now = now or _now()
    if item not in ITEMS:
        return 'an item (R378)(4) and (5) do not order: %r (%s)' % (item, ' | '.join(sorted(ITEMS)))
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    if not 1 <= n <= K.MAX_DISPATCHES:
        return 'dispatch %d past the act`s %d ((R378)(4), N1)' % (n, K.MAX_DISPATCHES)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d rowed already' % n
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in the series (%d rowed)' % (n, len(mine))
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    in_lane = [r for r in mine if lane(r.get('item')) == lane(item)]
    last = in_lane[-1] if in_lane else None
    if last and int(last['run']) not in reads:
        return 'dispatch %d (run %s) of the %s lane not yet read: one run read before the next is sent in a lane' % (last['n'], last['run'], lane(item))
    if any(r.get('item') == 'closing' for r in mine) and item != 'repeat':
        return 'the closing build sent: after it, the repeat of a stopped build alone'
    if item == 'repeat':
        if not last:
            return 'no build with the restore off to repeat'
        if last.get('item') == 'repeat':
            return 'the one repeat of the build at %s sent already' % str(last.get('sha'))[:8]
        rd = reads.get(int(last['run'])) or {}
        if rd.get('verdict') != STOPPED:
            return 'the last build with the restore off (run %s, %s) not read as stopped under the hold: %s' % (last['run'], last.get('item'), rd.get('verdict'))
        if sha != last.get('sha'):
            return 'the repeat at %s where the stopped build was at %s' % (str(sha)[:8], str(last.get('sha'))[:8])
        return None
    if item in ON_ITEMS:
        on = [r for r in mine if r.get('item') in ON_ITEMS]
        if len(on) + 1 > ON_CAP:
            return 'the dispatch with the restore on %d past the 36 of (R378)(4)' % (len(on) + 1)
    if item in STEP_ITEMS and now > LAST_STEP:
        return 'a step`s dispatch at %s, past the last hour %s ((R378)(3))' % (now, LAST_STEP)
    if item == 'closing':
        if any(r.get('item') == 'closing' for r in mine):
            return 'the closing build sent already'
        ok_on = [r for r in reads.values() if r.get('restore_input') == 'on' and r.get('built_ref') == sha and r.get('build_exit') == '0']
        if not ok_on:
            return 'the closing build from source sent before a build with the restore on at %s read exit 0' % str(sha)[:8]
    if ctx.get('lean') is None:
        return 'the Lean text check not read at %s' % str(sha)[:8]
    if ctx.get('lean'):
        return 'the Lean text check refuses %d file(s) at %s: %s' % (len(ctx['lean']), str(sha)[:8], '; '.join('%s %s' % x for x in ctx['lean'][:4]))
    if ctx.get('presend') is None:
        return 'the checks before a dispatch ((R378)(4)) not read at %s' % str(sha)[:8]
    if ctx.get('presend'):
        return 'the checks before a dispatch refuse at %s: %s' % (str(sha)[:8], '; '.join(ctx['presend'][:4]))
    return None


def tip_refusal(full, heads, branch):
    """None where `full` is the remote tip of `branch`; `heads` [(sha, ref)] from one ls-remote."""
    if not re.match(r'^[0-9a-f]{40}$', full or ''):
        return 'no commit read: %r' % (full,)
    at = [ref for sha, ref in heads if sha == full and ref == 'refs/heads/' + branch]
    return None if at else 'the commit %s is not the remote tip of %s (push it by tools/push_gated.sh --branch first)' % (full[:8], branch)


def branch_tip(heads):
    return next((sha for sha, ref in heads if ref == 'refs/heads/' + BRANCH), None)


def module_files(repo, sha):
    tree = DR.tree_files(repo, sha)
    toml = git(repo, 'show', '%s:lakefile.toml' % sha)
    sds = [s.rstrip('/') for s in re.findall(r'^srcDir\s*=\s*"([^"]+)"', toml, re.M)]
    return tree + [f[len(sd) + 1:] for sd in sds for f in tree if f.startswith(sd + '/')]


def _art(run, runs=None):
    return os.path.join(runs or RUNS, 'ef-%s' % run, 'build-module-%s' % run)


def _f(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def _targets(art):
    return [l.strip() for l in _f(art, 'print_targets.txt').replace('\r', '').split(NL) if l.strip()]


# ================================================================================ the verdicts
def _ran(r):
    return str((r or {}).get('axioms_print') or '').startswith('RAN')


def pair_verdict(on, off):
    """a pair at one commit: `on` the restore-on read there (exit 0), `off` the build from source's read (or its repeat's)."""
    if not off:
        return dict(state='PENDING', where='no build from source read')
    if off.get('verdict') == STOPPED:
        return dict(state='STOPPED', where='the build from source stopped under the hold (run %s)' % off.get('run'))
    if (on and on.get('build_exit') == '0' and off.get('build_exit') == '0' and _ran(on) and _ran(off) and on.get('built_ref') == off.get('built_ref')
            and on.get('axioms_sha256') != off.get('axioms_sha256')):
        return dict(state='DIFFERS', where='the axioms files differ by sha256: %s (run %s) and %s (run %s)' % (
            str(on.get('axioms_sha256'))[:16], on.get('run'), str(off.get('axioms_sha256'))[:16], off.get('run')),
            shas=(on.get('axioms_sha256'), off.get('axioms_sha256')), commit=on.get('built_ref'))
    where = []
    if not on:
        where.append('no build with the restore on read exit 0 at the commit')
    if off.get('build_exit') != '0':
        where.append('the build from source`s exit file %s' % off.get('build_exit'))
    if not (off.get('cache') or {}).get('untouched'):
        where.append('the build from source not one the cache left untouched (the restore off, nothing restored, nothing saved)')
    if not _ran(off):
        where.append('the build from source`s axioms print %s' % off.get('axioms_print'))
    if on:
        if not on.get('built_equal') or not off.get('built_equal') or on.get('built_ref') != off.get('built_ref'):
            where.append('the two builds not at the one dispatched commit')
        if not _ran(on):
            where.append('the restore-on build`s axioms print %s' % on.get('axioms_print'))
    if where:
        return dict(state='NOT AS WANTED', where='; '.join(where))
    if not (on.get('cache') or {}).get('restored'):
        return dict(state='NOT SCORABLE', where='the restore-on build at the commit restored no key ([H5]: its kind %s, restored key %s, '
                    'files before the build %s), so no restored build stands beside the build from source' % (
                        restore_kind(on.get('cache')), (on.get('cache') or {}).get('matched'), (on.get('cache') or {}).get('files_before')))
    return dict(state='AS WANTED', where='', sha=on.get('axioms_sha256'), commit=on.get('built_ref'), runs=(on.get('run'), off.get('run')),
                hit=(on.get('cache') or {}).get('hit'), kind=restore_kind(on.get('cache')))


def _offs(disp, reads, first):
    """the reads of a build from source and of its repeat (the repeat whose row names it), in order."""
    out = [reads.get(int(first['run']))] + [reads.get(int(r['run'])) for r in disp if r.get('item') == 'repeat' and r.get('repeats') == first['n']]
    return [x for x in out if x]


def trial_state(rows):
    """b767's (R377)(5)(c): [S2], [S3], PENDING (a run or a read owed), or the pair's own state where neither outcome's sentence holds; kept for
    b767's banks' readers, read by nothing of b768's."""
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    ton = [r for r in disp if r.get('item') == 'trial-on']
    toff = [r for r in disp if r.get('item') == 'trial-off']
    if not toff:
        return dict(state='PENDING', where='the trial`s run from source not sent', pair=None, offs=[])
    offs = _offs(disp, reads, toff[0])
    on = reads.get(int(ton[0]['run'])) if ton else None
    if offs and offs[-1].get('verdict') == STOPPED:
        if len(offs) == 2 and all(x.get('verdict') == STOPPED for x in offs):
            return dict(state='[S3]', where='the run from source and its repeat each stopped under the hold (runs %s)' % ', '.join(str(x.get('run')) for x in offs),
                        pair=None, offs=offs, why='stopped')
        return dict(state='PENDING', where='the run from source stopped under the hold (run %s): its repeat owed' % offs[-1].get('run'), pair=None, offs=offs)
    if not offs:
        return dict(state='PENDING', where='the trial`s run from source not read', pair=None, offs=offs)
    if not on:
        return dict(state='PENDING', where='the trial`s restored run not read', pair=None, offs=offs)
    pr = pair_verdict(on if on.get('build_exit') == '0' else None, offs[-1])
    if pr['state'] == 'AS WANTED':
        return dict(state='[S2]', where='', pair=pr, offs=offs)
    if pr['state'] == 'DIFFERS':
        return dict(state='[S3]', where=pr['where'], pair=pr, offs=offs, why='differs')
    return dict(state=pr['state'], where=pr['where'], pair=pr, offs=offs)


def main_decision(pr, stopped_both=False, no_closing_s3=False):
    """(4) MAIN AND THE TAG by the pair at the closing commit."""
    if no_closing_s3:
        return '[C8]: NO CLOSING BUILD WAS SENT, THE TRIAL HAVING ENDED AT [S3] ; MAIN NOT MOVED, NO TAG CUT, THE LEAN ON ITS BRANCH'
    if stopped_both:
        return '[C8]: THE CLOSING BUILD FROM SOURCE AND ITS REPEAT EACH STOPPED UNDER THE HOLD ; MAIN NOT MOVED, NO TAG CUT, THE LEAN ON ITS BRANCH'
    if pr['state'] == 'AS WANTED':
        return 'MAIN MOVES TO %s BY THE GATED PUSH, v0.46 CUT THERE AFTER MAIN`S READ-BACK' % str(pr.get('commit'))[:8]
    if pr['state'] == 'DIFFERS':
        return '[C7]: MAIN NOT MOVED, NO TAG CUT, THE LEAN ON ITS BRANCH'
    if pr['state'] == 'PENDING':
        return 'PENDING'
    return 'MAIN NOT MOVED, NO TAG CUT (THE PAIR %s)' % pr['state']


def verdicts(rows):
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    tr = dict(state='NOT AT THIS ACT', where='(R378)(4) sends no trial of the build from source: route (i) held by [S2] (OPEN_TRAILS :19355)',
              pair=None, offs=[])
    cl = [r for r in disp if r.get('item') == 'closing']
    stopped_both, no_closing_s3 = False, False
    if not cl:
        pr = pair_verdict(None, None)
    else:
        offs = _offs(disp, reads, cl[0])
        stopped_both = len(offs) == 2 and all(x.get('verdict') == STOPPED for x in offs)
        ons = [reads[int(r['run'])] for r in disp if r.get('n', 0) < cl[0]['n'] and int(r['run']) in reads
               and reads[int(r['run'])].get('restore_input') == 'on' and reads[int(r['run'])].get('built_ref') == cl[0]['sha']
               and reads[int(r['run'])].get('build_exit') == '0']
        pr = pair_verdict(ons[-1] if ons else None, offs[-1] if offs else None)
    kernel_reads = [reads[int(r['run'])] for r in disp if int(r['run']) in reads and reads[int(r['run'])].get('build_exit') == '0'
                    and reads[int(r['run'])].get('restore_input') == 'on']
    return dict(trial=tr, pair=pr, stopped_both=stopped_both, no_closing_s3=no_closing_s3,
                main=main_decision(pr, stopped_both, no_closing_s3), last_kernel=kernel_reads[-1] if kernel_reads else None)


# ================================================================================ the routes
def _tj(path_):
    p = os.path.join(RELAY, path_)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else {}


def cmd_lean(rev):
    full = git(KPATH, 'rev-parse', rev).strip()
    fs = lean_files(full)
    bad = lean_text_refusals(fs)
    print('### THE LEAN TEXT CHECK AT %s over %s: files %d, lines %d ; refused %d %s' % (
        full[:8], LEAN_DIR, len(fs), sum(len(t.split(NL)) for t in fs.values()), len(bad), ['%s %s' % x for x in bad[:6]]))
    return fs, bad


def cmd_presend(rev):
    full = git(KPATH, 'rev-parse', rev).strip()
    ref, rep = presend(full)
    print(NL.join(presend_lines(full, ref, rep)))
    return ref, rep


def cmd_dispatch(sha, n, item, *rest):
    rest = list(rest)
    if rest[:1] != ['--targets-json'] or len(rest) != 2:
        sys.exit('### usage: dispatch <sha> <n> <item> --targets-json <file> -- the targets from a bank this tool wrote, nothing typed beside it')
    read, dk, rows = DR.free(), disk(), _rows()
    slug, owner = remote()
    full = git(KPATH, 'rev-parse', sha).strip()
    tj = _tj(rest[1])
    if tj.get('rev') != full or tj.get('refused') or not tj.get('modules'):
        sys.exit('### NOT DISPATCHED: the targets file %r read rev %s against the commit %s, refused %s, modules %d' % (
            rest[1], str(tj.get('rev'))[:8], full[:8], tj.get('refused'), len(tj.get('modules') or [])))
    heads = heads_now()
    btip = branch_tip(heads)
    fs, bad = cmd_lean(full)
    pref, prep = cmd_presend(full)
    ctx = dict(lean=bad, presend=pref)
    why = dispatch_refusal(item, int(n), full, rows, read, dk, ctx=ctx)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    mode, branch, repeats = ITEMS[item][1], ITEMS[item][2], None
    if item == 'repeat':
        src = [r for r in mine if lane(r.get('item')) == 'source']
        mode, branch, repeats = src[-1].get('restore'), src[-1].get('branch'), src[-1].get('n')
    target = ' '.join(tj['modules'])
    print('  the targets from %s: %d modules, read at %s' % (rest[1], len(tj['modules']), tj['rev'][:8]))
    wp = wf_predicates(git(KPATH, 'show', '%s:%s' % (full, WF)))
    if not wp or not all(wp.values()):
        sys.exit('### NOT DISPATCHED: the workflow at the commit %s lacks (4)`s cache steps or (5)`s route: %s' % (full[:8], sorted(x for x, v in wp.items() if not v)))
    why = tip_refusal(full, heads, branch)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    nt = DR.targets_refused(target, module_files(KPATH, full))
    if nt:
        sys.exit('### NOT DISPATCHED: targets not modules of the tree at %s: %s' % (full[:8], nt))
    try:
        lic = DR.licence(ANSWERS, ITEMS[item][0], by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    print('  dispatch %s, %s (restore %s, lane %s) at %s on %s ; the licence %s %s :%d, committed %s ; free %d MB at %s, the hold %d ; volumes %s, '
          'the floor %d ; the last step hour %s' % (n, item, mode, lane(item), full[:8], branch, lic['bank'], lic['commit'][:8], lic['line'],
                                                   lic['committed_at'], read[0], read[1], DR.HOLD, dk, FLOOR, LAST_STEP))
    at0 = _now()
    cmd = ['gh', 'workflow', 'run', WORKFLOW, '--repo', slug, '--ref', branch, '-f', 'ref=' + full, '-f', 'target=' + target, '-f', 'restore=' + mode]
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip())
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel=EF, item=item, n=int(n), sha=full, target=target, at=at0, restore=mode, branch=branch,
                           at_ref=branch, error=mask(r.stderr or '', owner)[:300]))
    else:
        m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
        rid = m.group(1) if m else ''
        for _ in range(8):
            if rid:
                break
            time.sleep(5)
            lst = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', slug, '--workflow', WORKFLOW, '--event', 'workflow_dispatch', '--branch', branch,
                                             '--limit', '5', '--json', 'databaseId,createdAt'], capture_output=True, text=True, encoding='utf-8').stdout or '[]')
            new = sorted((x['createdAt'], x['databaseId']) for x in lst if x['createdAt'] >= at0)
            rid = str(new[0][1]) if new else ''
        if not rid:
            sys.exit('### DISPATCHED, NO RUN ID READ BACK in 40 s -- no row written; read `gh run list` by hand and row it before any other dispatch')
        rows.append(DR.row('dispatch', read, kernel=EF, item=item, n=int(n), workflow=WORKFLOW, at_ref=branch, branch=branch, restore=mode, sha=full,
                           target=target, run=int(rid), at=at0, licence=lic, disk_mb=dk, tree=module_files(KPATH, full), branch_tip=btip,
                           lean_files=len(fs), lean_refused=len(bad), lane=lane(item), repeats=repeats,
                           presend=dict(changed=len(prep['changed']), names=prep['names'], kt_largest=prep['kt']['largest'],
                                        mathlib_equal=prep['mathlib']['equal'])))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'item', 'n', 'restore', 'lane', 'branch', 'sha', 'run', 'repeats', 'free_mb', 'at')))


def _view(run):
    slug, owner = remote()
    v = subprocess.run(['gh', 'run', 'view', str(run), '--repo', slug, '--json', 'status,conclusion,createdAt,updatedAt,headSha,headBranch,event'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    if v.returncode != 0:
        sys.exit('### THE RUN NOT READ: %s' % mask(v.stderr, owner)[:300])
    return json.loads(v.stdout), slug, owner


def cmd_status(run):
    v, _s, _o = _view(run)
    print('  run %s: %s, %s ; created %s ; updated %s ; event %s ; the workflow at %s %s ; minutes so far %s' % (
        run, v['status'], v['conclusion'] or '-', v['createdAt'], v['updatedAt'], v['event'], v['headBranch'], v['headSha'][:8],
        run_minutes(v['createdAt'], v['updatedAt'] if v['status'] == 'completed' else _now())))


def cmd_download(run):
    v, slug, owner = _view(run)
    if v['status'] != 'completed':
        sys.exit('### THE RUN IS %s -- nothing downloaded (no waiting loop: read its status again later)' % v['status'])
    dst = os.path.join(RUNS, 'ef-%s' % run)
    if os.path.exists(dst):
        sys.exit('### %s STANDS ALREADY -- nothing downloaded (one new empty folder a run)' % dst)
    os.makedirs(dst)
    r = subprocess.run(['gh', 'run', 'download', str(run), '--repo', slug, '--dir', dst], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip() or '(gh printed nothing)')
    for base, _dirs, files in os.walk(dst):
        for f in sorted(files):
            p = os.path.join(base, f)
            print('  %s %d bytes' % (os.path.relpath(p, dst).replace('\\', '/'), os.path.getsize(p)))
    if r.returncode != 0:
        sys.exit('### gh run download exit %d' % r.returncode)


def cmd_read(n, run, *rest):
    art = _art(run)
    if not os.path.exists(os.path.join(art, 'build_exit.txt')):
        sys.exit('### NO build_exit.txt IN THE RUN`S FOLDER -- nothing written (download the run first)')
    v, _slug, _owner = _view(run)
    rows = _rows()
    d = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF and r.get('n') == int(n)]
    if not d or int(d[0]['run']) != int(run):
        sys.exit('### DISPATCH %s IS NOT RUN %s BY ITS ROW -- nothing written' % (n, run))
    if any(r.get('kind') == 'read' and r.get('kernel') == EF and int(r.get('run', 0)) == int(run) for r in rows):
        sys.exit('### RUN %s READ ALREADY -- nothing written' % run)
    ex = _f(art, 'build_exit.txt').strip()
    log = _f(art, 'build.log')
    mem = _f(art, 'mem.log')
    ref = _f(art, 'ref.txt').strip().split()
    errs = [l for l in log.split(NL) if l.startswith('error: ') or ': error' in l]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    stop = [l for l in mem.split(NL) if l.startswith('STOP ')]
    axt = _f(art, 'axioms.txt')
    targets = _targets(art)
    ax = axioms_read(axt, targets)
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', mem)]
    verdict = STOPPED if (stop or ex == '143') else 'KERNEL' if ex == '0' else 'BREAKS'
    axp = axioms_print(axt, ax)
    cr = cache_record(_f(art, 'cache_kernel.txt'))
    mine = [t for t in targets if t.startswith(ACT_NS)]
    ns = names_state(axt, ex, mine)
    p1x = _f(art, 'build_part_one_exit.txt').strip() or None
    p1n = len([l for l in _f(art, 'part_one_modules.txt').replace('\r', '').split(NL) if l.strip()])
    p1log = _f(art, 'build_part_one.log')
    p1err = [l for l in p1log.split(NL) if l.startswith('error: ') or ': error' in l]
    lows = mem_parts(mem)
    rows.append(DR.row('read', DR.free(), kernel=EF, n=int(n), run=int(run), item=d[0].get('item'), restore_input=d[0].get('restore'),
                       at_ref=d[0].get('at_ref', BRANCH), branch=d[0].get('branch'), status=v['status'], conclusion=v['conclusion'],
                       workflow_branch=v['headBranch'], workflow_sha=v['headSha'], workflow_at_ref=v['headBranch'] == d[0].get('at_ref', BRANCH),
                       built_ref=ref[0] if ref else None, built_equal=bool(ref) and ref[0] == d[0]['sha'], toolchain=ref[-1] if len(ref) > 1 else None,
                       build_exit=ex, verdict=verdict, stop=stop[:3], errors=errs[:40], sorry_warnings=len(warn_sorry), targets=len(targets),
                       axiom_lines=ax['lines'], axiom_within=ax['within'], axiom_outside=dict((a, list(b)) for a, b in ax['outside'].items()),
                       axiom_missing=ax['missing'][:60], axiom_missing_n=len(ax['missing']), sorryAx=ax['sorryAx'],
                       axioms_refused=_f(art, 'axioms_refused.txt')[:300], axioms_print=axp,
                       axioms_file_lines=len(axt.replace('\r', '').rstrip('\n').split(NL)) if axt.strip() else 0,
                       axioms_sha256=hashlib.sha256(axt.replace('\r', '').encode('utf-8')).hexdigest(),
                       cache=cr, restore_kind=restore_kind(cr), build_min=build_minutes(_f(art, 'build_times.txt')),
                       run_min=run_minutes(v['createdAt'], v['updatedAt']), runner_low_mb=min(nums) if nums else None, at=v['updatedAt'],
                       names=[list(x) for x in ns], artifact='%s/ef-%s/build-module-%s' % (RUNS_ROLE, run, run),
                       repeats=d[0].get('repeats'), part_one_exit=p1x, part_one_modules=p1n, part_one_errors=p1err[:20],
                       low_part_one=lows['one'] if p1x is not None else None, low_part_two=lows['two'] if p1x is not None else None))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('n', 'run', 'item', 'restore_input', 'conclusion', 'workflow_at_ref', 'built_ref', 'built_equal', 'build_exit',
                                   'verdict', 'sorry_warnings', 'targets', 'axiom_lines', 'axiom_within', 'axiom_missing_n', 'sorryAx', 'axioms_file_lines',
                                   'build_min', 'run_min', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
    if p1x is not None:
        print('  ROUTE (i): part one %d modules, its exit %s, its errors %d, the low %s MB ; part two the low %s MB' % (
            p1n, p1x, len(p1err), lows['one'], lows['two']))
    print('  THE AXIOMS PRINT: %s ; the file`s sha256 %s' % (axp, r['axioms_sha256'][:16]))
    print('  THE CACHE`S RECORD: %s ; THE RESTORE`S KIND ([H5]): %s, its line %s' % (
        dict((x, cr.get(x)) for x in ('read', 'input', 'hit', 'files_before', 'completed', 'present_before', 'save', 'restored', 'by_prefix', 'saved',
                                      'from_source', 'untouched')), r['restore_kind'], cr.get('hit')))
    print('  THIS ACT`S NAMES (%s*): %d' % (ACT_NS, len(ns)))
    for nm, st, why in ns:
        print('    %-70s %s %s' % (nm, st, why))
    for l in (r['axioms_refused'] or '').split(NL):
        if l.strip():
            print('  REFUSED BY THE WORKFLOW`S GRAMMAR: %s' % l.strip())
    for nm, a in sorted(ax['outside'].items()):
        print('  OUTSIDE THE STANDARD THREE: %s [%s]' % (nm, ', '.join(a)))
    for nm in ax['missing'][:40]:
        print('  NO AXIOMS LINE: %s' % nm)
    for l in (errs + p1err)[:20]:
        print('  ERR', l[:300])


def cmd_errors(run):
    log = (_f(_art(run), 'build_part_one.log') + NL + _f(_art(run), 'build.log')).split(NL)
    out, keep = [], 0
    for l in log:
        if re.search(r'^(error|warning: .*sorry)', l) or ': error' in l:
            keep = 16
        if keep:
            out.append(l)
            keep -= 1
    print(NL.join(out[:300]))
    print('### LOG LINES %d ; ERROR HEADS %d' % (len(log), len([l for l in log if l.startswith('error') or ': error' in l])))


def cmd_axioms(run):
    art = _art(run)
    targets = _targets(art)
    ax = axioms_of(_f(art, 'axioms.txt'))
    for t in targets:
        a = ax.get(t)
        print('  %-80s %s' % (t, 'NO AXIOMS LINE' if a is None else '[%s]%s' % (', '.join(a), '' if set(a) <= set(STANDARD) else '  OUTSIDE')))
    s = axioms_read(_f(art, 'axioms.txt'), targets)
    print('### TARGETS %d ; AXIOM LINES %d ; WITHIN THE STANDARD THREE %d ; OUTSIDE %d ; MISSING %d ; sorryAx %s' % (
        len(targets), s['lines'], s['within'], len(s['outside']), len(s['missing']), s['sorryAx']))


def cmd_compare(run_a, run_b):
    c = axioms_compare(_f(_art(run_a), 'axioms.txt'), _f(_art(run_b), 'axioms.txt'))
    print('  the axioms files of runs %s and %s: lines %d and %d ; positions equal %d ; the first difference at line %s ; EQUAL LINE FOR LINE %s' % (
        run_a, run_b, c['lines_a'], c['lines_b'], c['equal_positions'], c['first_diff'], c['equal']))


def targets_of(rev):
    import b758_presend as P_
    full = P_.J.g('rev-parse', rev).strip()
    t = P_.J.targets_at(full)
    bad = sorted(n for n, v in t.items() if v[0] is None)
    return full, sorted(set(v[0] for v in t.values() if v[0])), bad, len(t)


def cmd_targets(rev):
    full, mods, bad, n = targets_of(rev)
    nt = DR.targets_refused(' '.join(mods), module_files(KPATH, full))
    print('  print_targets.txt at %s: names %d ; modules %d ; resolved to no one module %d %s ; modules not of the tree %d %s' % (
        full[:8], n, len(mods), len(bad), bad[:4], len(nt or []), (nt or [])[:4]))
    if bad or nt or not mods:
        sys.exit('### THE TARGETS REFUSED -- nothing written')
    out = os.path.join(D, 'b768_targets_%s.json' % full[:8])
    s = json.dumps(dict(rev=full, names=n, modules=mods, refused=bad, at=_now(),
                        reader='tools/b757_join.py targets_at, through tools/b758_presend.py, both unchanged'), indent=1) + NL
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('written data/%s: %d modules for %d names at %s' % (os.path.basename(out), len(mods), n, full[:8]))


def verdict_lines(rows=None):
    rows = rows if rows is not None else _rows()
    v = verdicts(rows)
    tr, pr = v['trial'], v['pair']
    tp = tr.get('pair') or {}
    L = ['## THE TRIAL OF THE BUILD FROM SOURCE: %s ; %s' % (tr['state'], tr['where']),
         '## THE VERDICT OF (R378)(4): THE PAIR AT THE CLOSING COMMIT, MAIN AND THE TAG',
         '  THE PAIR: %s%s' % (pr['state'], (' ; ' + pr['where']) if pr.get('where') else (
             ' ; at %s, sha256 %s, runs %s, the restore-on build`s restore line %s (kind %s)' % (
                 str(pr.get('commit'))[:8], str(pr.get('sha'))[:16], pr.get('runs'), pr.get('hit'), pr.get('kind')) if pr['state'] == 'AS WANTED' else '')),
         '  MAIN AND THE TAG: %s' % v['main']]
    lk = v['last_kernel']
    if lk:
        L.append('  THIS ACT`S NAMES AT THE LAST RESTORED READ EXITING 0 (run %s at %s):' % (lk.get('run'), str(lk.get('built_ref'))[:8]))
        for nm, st, why in lk.get('names') or []:
            L.append('    %s %s %s' % (nm, st, why))
    else:
        L.append('  THIS ACT`S NAMES: no restored read exiting 0')
    return L, v


def cmd_verdict():
    L, _v = verdict_lines()
    print(NL.join(L))


# ================================================================================ the tool's own controls
def controls():
    L, ok = [], []

    def c(what, got, want):
        ok.append(bool(want))
        L.append('  (%d) %s: %s -> %s' % (len(ok), what, got, 'AS WANTED' if want else 'NOT AS WANTED'))

    std = axioms_of("'x' depends on axioms: [propext,\n Classical.choice, Quot.sound]").get('x')
    c('the axioms reader on a wrapped standard line', std, std == STANDARD)
    c('on an axiom-free line', axioms_of("'y' does not depend on any axioms").get('y'), axioms_of("'y' does not depend on any axioms").get('y') == ())
    s = axioms_read("'a' depends on axioms: [propext, sorryAx]\n'b' does not depend on any axioms", ['a', 'b', 'c'])
    c('a planted sorryAx line and a target with no line', 'outside %s ; missing %s ; sorryAx %s' % (sorted(s['outside']), s['missing'], s['sorryAx']),
      list(s['outside']) == ['a'] and s['missing'] == ['c'] and s['sorryAx'] and s['within'] == 1)
    c('the cap: the worklist`s MAX_DISPATCHES 40, with the restore on 36 (ON_CAP), no cap by price row ; the last step hour 14 h after the '
      'opening row', (K.MAX_DISPATCHES, ON_CAP, OPENING, LAST_STEP, (_epoch(LAST_STEP) - _epoch(OPENING)) / 3600.0),
      K.MAX_DISPATCHES == 40 and ON_CAP == 36 and _epoch(LAST_STEP) - _epoch(OPENING) == 14 * 3600)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    A, B, TC = 'a' * 40, 'b' * 40, TRIAL_COMMIT
    ok_ctx = dict(lean=[], presend=[])
    early, late = '2026-11-25T01:00:00Z', '2026-11-25T03:06:10Z'

    def D_(n, item, run, restore=None, sha=A, repeats=None):
        return dict(kind='dispatch', kernel=EF, n=n, item=item, run=run, restore=restore or ITEMS.get(item, (0, 'off'))[1] or 'off', sha=sha,
                    repeats=repeats)

    def R_(run, item, restore=None, ex='0', verdict='KERNEL', sha=A, **kw):
        return dict(kind='read', kernel=EF, run=run, item=item, restore_input=restore or ITEMS.get(item, (0, 'off'))[1] or 'off', build_exit=ex,
                    verdict=verdict, built_ref=sha, **kw)
    cache_on = cache_record('restore input: on\nkey: k-bbbb\nrestore hit: false\nrestored key: k-aaaa\nfiles under .lake/build before the build: 4120\n'
                            'build completed under the hold: true\nkey present before the save: false\nsave step: success\n')
    cache_off = cache_record('restore input: off\nkey: k-bbbb\nrestore hit: none\nrestored key: none\nfiles under .lake/build before the build: 0\n'
                             'build completed under the hold: true\nkey present before the save: none\nsave step: skipped\n')
    full_on = dict(axioms_print='RAN', built_equal=True, axioms_sha256='f' * 64, cache=cache_on)
    full_off = dict(axioms_print='RAN', built_equal=True, axioms_sha256='f' * 64, cache=cache_off)
    step_b = [D_(1, 'b', 11), R_(11, 'b', **full_on)]
    clos_ok = step_b + [D_(2, 'closing', 12), R_(12, 'closing')]
    clos_stop = step_b + [D_(2, 'closing', 12), R_(12, 'closing', ex='143', verdict=STOPPED)]
    rep_stop = clos_stop + [D_(3, 'repeat', 13, restore='off', repeats=2), R_(13, 'repeat', restore='off', ex='143', verdict=STOPPED)]
    on36 = []
    for i in range(36):
        on36 += [D_(i + 1, 'b', 100 + i), R_(100 + i, 'b')]
    on35 = on36[:70]
    plants = [('form', 1, A, [], good, dk, ok_ctx, early),
              ('b', 1, A, [], (2000, _now()), dk, ok_ctx, early),
              ('b', 1, A, [], good, {'C:/': 4000, 'D:/': 20000}, ok_ctx, early),
              ('b', 41, A, [], good, dk, ok_ctx, early),
              ('b', 2, A, [], good, dk, ok_ctx, early),
              ('b', 1, A, [D_(1, 'b', 11)], good, dk, ok_ctx, early),
              ('c', 2, A, [D_(1, 'b', 11)], good, dk, ok_ctx, early),
              ('closing', 2, A, [D_(1, 'b', 11, sha=B), R_(11, 'b', sha=B)], good, dk, ok_ctx, early),
              ('closing', 2, A, [D_(1, 'b', 11), R_(11, 'b', ex='1', verdict='BREAKS')], good, dk, ok_ctx, early),
              ('b', 37, A, on36, good, dk, ok_ctx, early),
              ('repeat', 3, A, clos_ok, good, dk, ok_ctx, early),
              ('repeat', 4, A, rep_stop, good, dk, ok_ctx, early),
              ('repeat', 2, A, [D_(1, 'b', 11), R_(11, 'b', ex='143', verdict=STOPPED)], good, dk, ok_ctx, early),
              ('c', 3, A, clos_ok, good, dk, ok_ctx, early),
              ('repeat', 3, B, clos_stop, good, dk, ok_ctx, early),
              ('b', 1, A, [], good, dk, ok_ctx, late),
              ('a', 1, A, [], good, dk, ok_ctx, late),
              ('trial-on', 1, TC, [], good, dk, ok_ctx, early),
              ('trial-off', 1, TC, [], good, dk, ok_ctx, early),
              ('b', 1, A, [], good, dk, dict(lean=[('SIDEExplicitFormula/Window/X.lean', 'a decimal literal (1)')], presend=[]), early),
              ('b', 1, A, [], good, dk, dict(presend=[]), early),
              ('b', 1, A, [], good, dk, dict(lean=[], presend=['X.lean does not open with its imports']), early),
              ('b', 1, A, [], good, dk, dict(lean=[]), early),
              ('a', 37, A, on36, good, dk, ok_ctx, early)]
    why_want = ('an item (R378)(4) and (5) do not order', 'under the hold', 'under the floor', 'past the act', 'is not the next in the series',
                'rowed already', 'not yet read', 'sent before a build with the restore on', 'sent before a build with the restore on',
                'past the 36', 'not read as stopped under the hold', 'the one repeat', 'no build with the restore off to repeat',
                'the closing build sent: after it', 'where the stopped build was at', 'past the last hour', 'past the last hour',
                'an item (R378)(4) and (5) do not order', 'an item (R378)(4) and (5) do not order', 'the Lean text check refuses',
                'the Lean text check not read', 'the checks before a dispatch refuse', 'the checks before a dispatch ((R378)(4)) not read',
                'past the 36')
    got = [dispatch_refusal(p[0], p[1], p[2], p[3], p[4], p[5], ctx=p[6], now=p[7]) for p in plants]
    own = [bool(g) and w in g for g, w in zip(got, why_want)]
    c('twenty-four planted dispatches refused, EACH FOR THE REASON PLANTED (an item not ordered, under the hold, under the floor, past 40, out '
      'of series, rowed already, the last run of its lane unread, the closing at another commit than its restore-on build, the closing before '
      'a restore-on build exiting 0, the 37th with the restore on, a repeat of a build not stopped, a second repeat, a repeat with no build '
      'from source, a step after the closing, a repeat at another commit, a step past the last hour, the trial at small size past it, b767`s '
      'trial-on and trial-off, a Lean file with a decimal literal, the Lean text not read, a check before the dispatch refusing, the checks '
      'not read, the trial at small size as the 37th with the restore on)', [('own' if o else 'OTHER: %s' % g) for o, g in zip(own, got)],
      all(own) and len(got) == 24 == len(why_want))
    passes = [dispatch_refusal('a', 1, A, [], good, dk, ctx=ok_ctx, now=early),
              dispatch_refusal('b', 3, A, [D_(1, 'a', 11), R_(11, 'a'), D_(2, 'b', 12), R_(12, 'b')], good, dk, ctx=ok_ctx, now=early),
              dispatch_refusal('closing', 2, A, step_b, good, dk, ctx=ok_ctx, now=late),
              dispatch_refusal('closing', 3, A, step_b + [D_(2, 'c', 12)], good, dk, ctx=ok_ctx, now=early),
              dispatch_refusal('repeat', 3, A, clos_stop, good, dk, ctx={}, now=late),
              dispatch_refusal('b', 1, A, [], good, dk, ctx=ok_ctx, now=LAST_STEP),
              dispatch_refusal('b', 36, A, on35, good, dk, ctx=ok_ctx, now=early),
              dispatch_refusal('e', 2, A, [D_(1, 'd', 11), R_(11, 'd')], good, dk, ctx=ok_ctx, now=early)]
    c('eight planted dispatches taken (the trial at small size first ; a step after it and another, each read ; the closing after a restored '
      'build at its commit, past the step hour ; the closing beside an unread step, another lane ; the repeat of a stopped closing build ; a '
      'step at the last hour itself ; the 36th with the restore on ; L12`s step after L11d`s)', passes, passes == [None] * 8)
    lic = {}
    for nd, want_line in ((N4A, 21), (N4B, 22), (N4C, 23), (N4D, 24), (N4E, 25), (N4CAP, 28), (N4MAIN, 29)):
        try:
            x = DR.licence(ANSWERS, nd)
            lic[nd[:16]] = (x['commit'][:8], x['line'], x['line'] == want_line)
        except DR.Refused as e:
            lic[nd[:16]] = str(e)[:60]
    c('the licences at the committed ferry bank: the trial at small size at :21, (4)(b) at :22, (4)(c) at :23, (4)(d) at :24, (4)(e) at :25, '
      'the cap at :28, main and the tag at :29', lic, len(lic) == 7 and all(isinstance(v, tuple) and v[2] for v in lic.values()))
    try:
        DR.licence(ANSWERS, '(15) A CLAUSE THE RULING DOES NOT HAVE')
        miss = False
    except DR.Refused:
        miss = True
    c('a needle the ferry does not carry refused', miss, miss)
    slug, owner = remote()
    c('the kernel`s remote read from its own config, printed masked', mask(slug, owner),
      mask(slug, owner).startswith('<account>/') and bool(owner) and owner not in mask('https://github.com/%s/x/actions/runs/1' % slug, owner))
    t1 = DR.targets_refused('SIDEExplicitFormula.ControlFailureExists', module_files(KPATH, K.EF_BASE))
    t2 = DR.targets_refused('SIDEExplicitFormula.Window.PlantedB768', module_files(KPATH, K.EF_BASE))
    t3 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', module_files(KPATH, K.EF_BASE))
    t4 = DR.targets_refused('SIDEExplicitFormula.Window.KFast', module_files(KPATH, TRIAL_COMMIT))
    c('targets at main 89fd5b54: the statement`s module taken ; a planted Window module refused there (no file on main) ; a vendored module '
      'under its srcDir taken ; at b767`s trial commit f6f60590 a Window module taken', (t1, len(t2), t3, t4), t1 == [] and len(t2) == 1 and t3 == [] and t4 == [])
    pl = [axioms_print("out/Axioms.lean:1:0: error: import X failed", axioms_read("out/Axioms.lean:1:0: error: x", ['a'])),
          axioms_print("NOT RUN: the build did not complete under the hold", axioms_read('', ['a'])),
          axioms_print("'a' depends on axioms: [propext]", axioms_read("'a' depends on axioms: [propext]", ['a']))]
    c('the axioms print`s state on three planted files (an import failure, the NOT RUN line, a clean print)', [x[:24] for x in pl],
      pl[0].startswith('FAILED, NO AXIOMS LINE') and pl[1].startswith('NOT RUN') and pl[2] == 'RAN')
    heads = [(A, 'refs/heads/' + BRANCH), ('c' * 40, 'refs/heads/main'), ('e' * 40, 'refs/heads/push-b767-proof')]
    tp = (tip_refusal(A, heads, BRANCH), bool(tip_refusal('c' * 40, heads, BRANCH)), bool(tip_refusal('e' * 40, heads, BRANCH)),
          bool(tip_refusal('', heads, BRANCH)), branch_tip(heads) == A, bool(tip_refusal(B, heads, BRANCH)))
    c('the remote tip: the branch`s tip taken ; main`s, push-b767-proof`s, no commit and a commit at no head refused ; the branch`s tip read',
      tp, tp == (None, True, True, True, True, True))
    tf, tm, tb, tn = targets_of(K.EF_BASE_B763)
    bj = json.load(io.open(os.path.join(D, 'b759_targets.json'), encoding='utf-8'))
    c('THE POSITIVE CONTROL: the targets reader at a3aad4cc against b759`s targets bank (data/b759_targets.json: %d modules for %d names)' % (
        len(bj['modules']), bj['names']), (tf[:8], len(tm), tn, len(tb)), tf == bj['rev'] and tm == sorted(bj['modules']) and tn == bj['names'] and not tb)
    wt = wf_predicates(git(KPATH, 'show', '%s:%s' % (BASE_PROOF, WF)))
    wb = wf_predicates(git(KPATH, 'show', '%s:%s' % (NO_ROUTE_COMMIT, WF)))
    wo = wf_predicates(git(KPATH, 'show', '%s:%s' % (K.RUNNER_COMMIT_B764, WF)))
    c('the workflow`s predicates: each of nine true at the branch`s base 89fd5b54, the file main holds ((R378)(5), (9)) ; THE PLANTED FAULTS, push-b766-proof`s 3c67b8b5 (the eight '
      'cache steps true, route (i) false) and b764`s 38a57e02 (its three true)', (sum(wt.values()), len(wt), sorted(k for k, v in wb.items() if not v),
                                                                                    sorted(k for k, v in wo.items() if v)),
      all(wt.values()) and len(wt) == 9 and sorted(k for k, v in wb.items() if not v) == ['route_two_parts']
      and sorted(k for k, v in wo.items() if v) == sorted(B764_PREDICATES))
    recs = [cache_record('restore input: on\nkey: kernel-build-x-aaaa\nrestore hit: false\nrestored key: none\nfiles under .lake/build before the build: 0\n'
                         'build completed under the hold: true\nkey present before the save: false\nsave step: success\n'),
            cache_on,
            cache_record('restore input: on\nkey: kernel-build-x-bbbb\nrestore hit: true\nrestored key: kernel-build-x-bbbb\n'
                         'files under .lake/build before the build: 4130\nbuild completed under the hold: true\nkey present before the save: true\n'
                         'save step: skipped\n'),
            cache_off,
            cache_record('restore input: on\nkey: kernel-build-x-aaaa\nrestore hit: true\n')]
    rv = [(r['read'], r['restored'], r['by_prefix'], r['saved'], r['from_source'], r['untouched'], restore_kind(r)) for r in recs]
    c('the cache`s record and the restore`s kind on five planted files (the first save, built from source ; a restore by the prefix, then saved ; '
      'an exact restore ; the restore off ; a record cut short): (read, restored, by prefix, saved, from source, untouched, kind)', rv,
      rv == [(True, False, False, True, True, False, 'none'), (True, True, True, True, False, False, 'prefix'),
             (True, True, False, False, False, False, 'exact'), (True, False, False, False, True, True, 'none'),
             (False, False, False, False, False, False, 'unread')])
    rk, same, seen = {}, 0, 0
    for runs_, rows_ in PREV_RUNS:
        for r in (json.load(io.open(rows_, encoding='utf-8')) if os.path.exists(rows_) else []):
            if r.get('kind') != 'read':
                continue
            fp = os.path.join(_art(r['run'], runs_), 'cache_kernel.txt')
            if not os.path.exists(fp):
                continue
            seen += 1
            k_file = restore_kind(cache_record(_f(_art(r['run'], runs_), 'cache_kernel.txt')))
            same += k_file == restore_kind(r.get('cache'))
            rk[k_file] = rk.get(k_file, 0) + 1
    c('THE POSITIVE CONTROL: the restore`s kind on b765`s and b767`s real records (each read row against its artifact`s cache_kernel.txt): '
      'read, equal, by kind', (seen, same, sorted(rk.items())),
      seen > 0 and same == seen and rk.get('exact', 0) >= 1 and rk.get('prefix', 0) >= 1 and rk.get('none', 0) >= 1)
    base = dict(build_exit='0', axioms_print='RAN', built_ref=A, built_equal=True, axioms_sha256='f' * 64, verdict='KERNEL')
    on = dict(base, run=21, restore_input='on', cache=cache_on)
    off = dict(base, run=22, restore_input='off', cache=cache_off)
    pv = [pair_verdict(on, off)['state'], pair_verdict(on, dict(off, axioms_sha256='0' * 64))['state'],
          pair_verdict(dict(on, cache=recs[0]), off)['state'], pair_verdict(on, dict(off, build_exit='1', verdict='BREAKS'))['state'],
          pair_verdict(on, None)['state'], pair_verdict(on, dict(off, verdict=STOPPED, build_exit='143'))['state'],
          pair_verdict(None, off)['state'], pair_verdict(dict(on, cache=recs[2]), off)['state']]
    c('the pair on eight planted readings (as wanted, restored by the prefix ; the files differing ; the restore-on build restoring no key ; the '
      'build from source exiting 1 ; none read ; it stopped ; no restore-on build ; as wanted, an exact key)', pv,
      pv == ['AS WANTED', 'DIFFERS', 'NOT SCORABLE', 'NOT AS WANTED', 'PENDING', 'STOPPED', 'NOT AS WANTED', 'AS WANTED'])
    md = [main_decision(dict(state='AS WANTED', commit=A))[:10], main_decision(dict(state='DIFFERS'))[:4], main_decision(dict(state='PENDING')),
          main_decision(dict(state='NOT SCORABLE'))[:14], main_decision(dict(state='STOPPED'), stopped_both=True)[:4]]
    c('main and the tag on five planted pairs (as wanted, v0.46 named ; differing, [C7] ; pending ; not scorable ; the closing and its repeat '
      'stopped, [C8])', md, md == ['MAIN MOVES', '[C7]', 'PENDING', 'MAIN NOT MOVED', '[C8]'] and 'v0.46' in main_decision(dict(state='AS WANTED', commit=A)))
    series = step_b + [D_(2, 'closing', 12), dict(R_(12, 'closing'), **full_off)]
    vr = verdicts(series)
    vs = verdicts(rep_stop)
    c('the verdicts over two planted series (a restored step and the closing from source at its commit ; the closing and its repeat each '
      'stopped), the trial read as not at this act', (vr['trial']['state'], vr['pair']['state'], vr['main'][:10], vs['main'][:4]),
      (vr['trial']['state'], vr['pair']['state'], vr['main'][:10], vs['main'][:4]) == ('NOT AT THIS ACT', 'AS WANTED', 'MAIN MOVES', '[C8]'))
    nm = 'SIDEExplicitFormula.Window.x'
    ss = [names_state("'%s' depends on axioms: [propext]" % nm, '0', [nm])[0][1], names_state("'%s' depends on axioms: [propext]" % nm, '1', [nm])[0][1],
          names_state("'other' depends on axioms: [propext]", '0', [nm])[0][1], names_state("'%s' depends on axioms: [sorryAx]" % nm, '0', [nm])[0][1]]
    c('this act`s names on four planted prints (its line in the three ; the exit 1 ; no line ; sorryAx)', ss,
      ss == ['COMPILED', 'NOT COMPILED', 'NOT COMPILED', 'NOT COMPILED'])
    lt = [lean_text_refusals({'W/A.lean': 'theorem a : (2 : ℝ) ≤ 1024 := by norm_num'}),
          lean_text_refusals({'W/B.lean': 'def c : ℝ := 1.5'}),
          lean_text_refusals({'W/C.lean': '-- the frequency of the window'}),
          lean_text_refusals({'W/D.lean': 'theorem d : Real.log 1024 = 10 * Real.log 2 := by rw [show (1024 : ℝ) = 2 ^ 10 by norm_num]'})]
    c('the Lean text check on four planted files (clean ; a decimal literal ; a barred word ; clean, with powers and logarithms)',
      [len(x) for x in lt], [len(x) for x in lt] == [0, 1, 1, 0])
    big = 'theorem t : ([%s] : List Nat).all (fun x => x < 5000) = true := by decide' % ', '.join(str(i) for i in range(KT_CAP + 1))
    fit = 'theorem t : ([%s] : List Nat).all (fun x => x < 5000) = true := by decide' % ', '.join(str(i) for i in range(KT_CAP))
    nodec = 'def tbl : List Nat := [%s]' % ', '.join(str(i) for i in range(KT_CAP + 1))
    rng = 'theorem r : (List.range 4101).all (fun x => x < 5000) = true := by decide'
    refd = nodec + '\ntheorem t : tbl.all (fun x => x < 5000) = true := by decide'
    arg = ('theorem s : ∑ j ∈ Finset.range 16385, f j = ∑ j ∈ Finset.range 16385, g j := by\n'
           '  refine Finset.sum_congr rfl (fun j _ => ?_)\n  ring')
    prf = 'theorem r2 : (List.range 4101).length = 4101 := rfl'
    tac = 'theorem r3 : (List.range 4101).length = 4101 := by\n  rfl'
    ev = [max([s for _h, s in eval_sizes(x)] + [0]) for x in (big, fit, nodec, rng, refd, arg, prf, tac)]
    imp = [imports_first('/- head -/\n-- a line\nimport Mathlib\n\ndef x := 1'), imports_first('def x := 1\nimport Mathlib'), imports_first('')]
    qn = qnames(['  exact Real.add_pow_le_pow_mul_pow_of_sq_le_sq _ hx.le (Finset.sum_congr rfl fun i _ => by simp) -- Real.ignored_in_comment',
                 '  exact (Real.sinh_nonneg_iff.mpr hx).trans le_rfl'])
    sn = snakes(['  nlinarith [mul_pos ha hb, sq_nonneg (a - b)] -- one_add_one_eq_two', '  norm_num [Real.log_le_sub_one_of_pos]'])
    c('the checks before a dispatch on planted texts (a decide over 4,101 places ; over 4,100 ; a table of 4,101 with no decide ; a range of '
      '4,101 under decide ; a decide naming the table of 4,101 defined apart ; rfl given as an argument over a range of 16,385, not '
      'evaluated (b767 (m)) ; rfl as the proof over 4,101 ; rfl as a tactic over 4,101 ; the imports first past comments ; a def before '
      'the import ; empty ; the qualified names of two lines, the comment and a local`s field left out, the projections .mpr and .trans '
      'cut ; the unqualified names, the comment`s, the tactic`s and the qualified name`s left out)', (ev, imp, qn, sn),
      ev == [KT_CAP + 1, KT_CAP, 0, KT_CAP + 1, KT_CAP + 1, 0, KT_CAP + 1, KT_CAP + 1] and imp == [True, False, True]
      and qn == ['Finset.sum_congr', 'Real.add_pow_le_pow_mul_pow_of_sq_le_sq', 'Real.sinh_nonneg_iff'] and sn == ['mul_pos', 'sq_nonneg'])
    kg0 = import_graph(KPATH, TRIAL_COMMIT, ['*.lean'], kmodule)
    mrev0 = mathlib_rev(TRIAL_COMMIT)
    mg0 = mathlib_graph(mrev0)
    line0 = ['  exact (Real.sinh_nonneg_iff.mpr hx)', '  exact SIDEExplicitFormula.Window.primeTermQ_eq_finite_sum _',
             '  exact Real.no_such_name_planted_by_b768 _']
    ra = names_reading(line0, ['Mathlib.Data.Rat.Defs'], TRIAL_COMMIT, mrev0, kg0, mg0)
    rb = names_reading(line0, ['Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp'], TRIAL_COMMIT, mrev0, kg0, mg0)
    rc = names_reading(['  exact Real.sinh_nonneg_iff.mpr hx'], ['SIDEExplicitFormula.Window.PrimeFinite'], TRIAL_COMMIT, mrev0, kg0, mg0)
    cl = ((sorted(ra['outside']), ra['in_closure'], ra['kernel'], ra['not_found'], ra['undeclared']), (sorted(rb['outside']), rb['in_closure']),
          (rc['closure'] > ra['closure'] and rc['closure'] > 1000, len(kg0), len(mg0)))
    c('THE CLOSURE READING, b763 (i)`s class (b767 (h)), at the trial commit and the pinned Mathlib on three planted files: importing '
      'Mathlib.Data.Rat.Defs alone, Real.sinh_nonneg_iff declared only outside, the kernel`s name read as the kernel`s, a planted name not '
      'found and with no declaration ; importing DerivHyp, within ; importing the kernel`s PrimeFinite, its closure read through the kernel`s '
      'imports (wider than Rat.Defs`s, above 1,000 modules) ; the graphs` sizes (kernel above 400, Mathlib above 5,000)', cl,
      cl[0] == (['Real.sinh_nonneg_iff'], [], ['SIDEExplicitFormula.Window.primeTermQ_eq_finite_sum'], ['Real.no_such_name_planted_by_b768'],
                ['Real.no_such_name_planted_by_b768']) and cl[1] == ([], ['Real.sinh_nonneg_iff']) and cl[2][0] and cl[2][1] > 400 and cl[2][2] > 5000)
    lk = ['  rw [cubicB_eq_sum]']
    ka = names_reading(lk, ['SIDEExplicitFormula.Window.KValues'], TRIAL_COMMIT, mrev0, kg0, mg0, own='SIDEExplicitFormula.Window.PlantedB767')
    kb = names_reading(lk, ['SIDEExplicitFormula.Window.KappaClosed'], TRIAL_COMMIT, mrev0, kg0, mg0, own='SIDEExplicitFormula.Window.PlantedB767')
    kc = names_reading(lk, ['SIDEExplicitFormula.Window.KBasis'], TRIAL_COMMIT, mrev0, kg0, mg0, own='SIDEExplicitFormula.Window.KappaClosed')
    kd0 = names_reading(['/-- the window by', '  cubicB_eq_sum and Arch.lean, archTermQ_windowK -/', '  exact rfl'],
                        ['SIDEExplicitFormula.Window.KValues'], TRIAL_COMMIT, mrev0, kg0, mg0, own='SIDEExplicitFormula.Window.PlantedB767')
    kcl = (sorted(ka['kernel_outside'].items()), ka['kernel'], sorted(kb['kernel_outside']), sorted(kc['kernel_outside']),
           kb['kclosure'] > ka['kclosure'], (sorted(kd0['kernel_outside']), kd0['kernel'], kd0['qualified'], kd0['snake']))
    c('THE KERNEL`S NAMES AGAINST THE FILE`S CLOSURE, b767 (k), at the trial commit on four planted files: naming cubicB_eq_sum, importing '
      'KValues alone, declared only outside (in KappaClosed) ; importing KappaClosed, within ; importing KBasis as KappaClosed itself, its '
      'own module within ; the closure through KappaClosed wider than KValues`s ; three names in a block comment over two lines, none read',
      kcl, kcl[0] == [('cubicB_eq_sum', ['SIDEExplicitFormula.Window.KappaClosed'])] and kcl[1] == ['cubicB_eq_sum'] and kcl[2] == []
      and kcl[3] == [] and kcl[4] and kcl[5] == ([], [], [], []))
    ln = ['  refine Finset.sum_congr rfl (fun i _ => ?_)', '  rw [List.cons_append, List.length_cons, Finset.sum_comm]']
    rn = names_reading(ln, ['Mathlib.Algebra.BigOperators.Intervals'], TRIAL_COMMIT, mrev0, kg0, mg0, own='SIDEExplicitFormula.Window.PlantedB768')
    lw = decl_hits(MATHLIB, mrev0, ['sum_congr', 'cons_append'], MATHLIB_SPEC, mmodule)
    kw = decl_hits(KPATH, TRIAL_COMMIT, ['sum_comm'], ['*.lean'], kmodule)
    nsr = (sorted(rn['outside']), sorted(rn['kernel_outside']), rn['kernel'], sorted(rn['undeclared']), bool(lw['sum_congr']),
           bool(lw['cons_append']), bool(kw['sum_comm']))
    c('THE NAMESPACE READING, b768 (data/b768_events.txt (61)), at the trial commit and the pinned Mathlib on one planted file importing '
      'BigOperators.Intervals: Finset.sum_congr and Finset.sum_comm (each made by @[to_additive] with no declaration line of its own) and '
      'List.cons_append and List.length_cons (core`s) read with no declaration found, none refused and none the kernel`s ; where the last '
      'word alone, the reading replaced, finds a declaration of sum_congr and of cons_append in Mathlib and of sum_comm in the kernel, each '
      'in another namespace ; the control above still reading Real.sinh_nonneg_iff declared only outside', nsr,
      nsr == ([], [], [], ['Finset.sum_comm', 'Finset.sum_congr', 'List.cons_append', 'List.length_cons'], True, True, True))
    # ### b768 (data/b768_events.txt (65)): run 45439584241 broke on Packed.lean :182, `abs_mul` unknown, its module outside the file's closure
    pk_imp = ['Mathlib.Algebra.BigOperators.Intervals', 'Mathlib.Algebra.BigOperators.Ring.Finset', 'Mathlib.Algebra.Order.BigOperators.Group.Finset',
              'Mathlib.Data.List.GetD', 'Mathlib.Tactic.Linarith', 'Mathlib.Tactic.Ring']
    pk_ops = file_opens(NL.join(['namespace SIDEExplicitFormula', 'namespace Window', 'theorem planted : True := trivial', 'end Window',
                                 'end SIDEExplicitFormula']))
    la = ['    · rw [abs_mul]', '    exact le_trans (abs_nonneg _) h']
    own26 = 'SIDEExplicitFormula.Window.PlantedB768'
    ua = names_reading(la, pk_imp, TRIAL_COMMIT, mrev0, kg0, mg0, own=own26, opens=pk_ops)
    ub = names_reading(la, pk_imp + ['Mathlib.Algebra.Order.Ring.Abs'], TRIAL_COMMIT, mrev0, kg0, mg0, own=own26, opens=pk_ops)
    uc = names_reading(la, pk_imp, TRIAL_COMMIT, mrev0, kg0, mg0, own=own26)
    ops2 = file_opens(NL.join(['namespace A.B', 'open Finset Real in', 'open Nat (succ_le)', 'end A.B', 'open List hiding foo']))
    pr26, _rp26 = presend(E0_TRIAL)
    fp = mg0.get('Mathlib.Tactic.FunProp') or []
    fimp = file_imports(NL.join(['/- a planted head -/', 'module', 'public import Mathlib.Tactic.Ring', 'import Mathlib.Data.List.GetD', '',
                                 '/-!', '# a doc', 'import Mathlib.Analysis.Complex.Trigonometric', '-/', '@[expose] public section',
                                 'import Mathlib.Data.EReal.Inv']))
    ur = (sorted(ua['outside'].items()), 'abs_nonneg' in ua['outside'], ub['in_closure'], 'abs_mul' in uc['outside'], 'abs_mul' in uc['qualified'],
          sorted(ops2), pr26, ('Mathlib.Tactic.FunProp.Core' in fp, 'Mathlib.Analysis.Complex.Trigonometric' in fp),
          'Mathlib.Algebra.Order.Ring.Abs' in mathlib_closure(pk_imp, kg0, mg0), fimp)
    c('THE UNQUALIFIED NAME READ AT THE ROOT AND THE FILE`S OPENS, b768 (65), AND THE IMPORTS READ IN THE HEADER ALONE, b768 (66), at the '
      'trial commit and the pinned Mathlib: `abs_mul` under Packed.lean`s six imports read declared only outside (in '
      'Mathlib.Algebra.Order.Ring.Abs) and so refused, `abs_nonneg` not ; with that module imported, within ; THE READING REPLACED (no '
      'opens): abs_mul not read outside, or unqualified, so not refused, as at e0baa667 ; the opens of a planted file (its namespaces with '
      'their prefixes, the names its open lines open, alone and joined) ; THE CHECKS AT e0baa667 refusing Packed.lean`s abs_mul and '
      'nothing else ; Mathlib.Tactic.FunProp`s imports read with FunProp.Core and without its doc comment`s Complex.Trigonometric ; '
      'Ring.Abs outside Packed.lean`s closure ; a planted header`s imports, the doc comment`s and the one past the header`s end not read',
      ur, ur[0] == [('abs_mul', ['Mathlib.Algebra.Order.Ring.Abs'])] and not ur[1] and ur[2] == ['abs_mul'] and not (ur[3] and ur[4])
      and ur[5] == ['', 'A', 'A.B', 'A.B.Finset', 'A.B.Nat', 'A.B.Real', 'A.Finset', 'A.Nat', 'A.Real', 'Finset', 'List', 'Nat', 'Real']
      and len(pr26) == 1 and 'Packed.lean: abs_mul declared in Mathlib only outside' in pr26[0] and ur[7] == (True, False) and not ur[8]
      and ur[9] == ['Mathlib.Tactic.Ring', 'Mathlib.Data.List.GetD'])
    mrev = mathlib_rev(TRIAL_COMMIT)
    mf = (bool(mathlib_found(mrev, 'hasSum_log_one_add_inv')), bool(mathlib_found(mrev, 'eulerMascheroniSeq')),
          bool(mathlib_found(mrev, 'no_such_name_planted_by_b768')))
    c('the Mathlib search at the manifest`s rev %s (the clone`s HEAD %s): two names of the plan found, a planted name not' % (
        str(mrev)[:8], git(MATHLIB, 'rev-parse', 'HEAD').strip()[:8]), mf, mf == (True, True, False))
    pr0, rp0 = presend(BASE_PROOF)
    nb = len(lean_files(BASE_PROOF))
    c('the checks at the branch`s base 89fd5b54 against itself: no Window file changed, each of its %d opening with its imports, nothing '
      'refused' % nb, (rp0['files'], rp0['changed'], rp0['imports_first']['not_first'], pr0), rp0['files'] == nb > 17 and not rp0['changed'] and not pr0)
    lc = longest_compiled(BASE_PROOF)
    over = 'def t : List Nat := [%s]' % ', '.join(['0'] * (lc['without'] + 1))
    fit = 'def t : List Nat := [%s]' % ', '.join(['0'] * lc['without'])
    dr = [len(depth_refusals({'W/O.lean': over}, lc)), len(depth_refusals({'W/F.lean': fit}, lc)),
          len(depth_refusals({'W/P.lean': 'set_option maxRecDepth 100000 in\n' + over}, lc))]
    c('THE ELABORATOR`S DEPTH, b767 (n), carried by (R378)(4): the longest list literal compiled at the base without the option %d (%s), '
      'with it %d (%s) ; three planted files (one place past it with no option ; at it ; past it with the option ed88b486 carries)' % (
          lc['without'], lc['without_file'], lc['with_'], lc['with_file']), dr, dr == [1, 0, 0] and lc['with_'] >= 3278 and lc['without'] >= 256)
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b768_controls.py`s OWN CONTROLS, (R378)(4) (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R378)(4): THE DISPATCHES OF THE PROOF FINISHED AND OF THE CLOSING BUILD, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '',
           '## THE CONTROLS'] + L + ['  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == EF]
    out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (EF, len(disp), K.MAX_DISPATCHES, len(refused)))
    for r in disp:
        rd = reads.get(int(r['run']), {})
        cr = rd.get('cache') or {}
        out.append('  %d | %-9s | restore %s | lane %s | sha %s on %s | run %s | at %s | free %d MB | licence %s :%s | %s, exit %s, built %s, %d errors, '
                   'sorry warnings %s, targets %s, axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, axioms file %s lines sha256 %s, runner '
                   'low %s MB, minutes %s (build %s)' % (
                       r['n'], r['item'], r.get('restore'), r.get('lane'), r['sha'][:8], r.get('branch'), r['run'], r.get('at'), r['free_mb'],
                       r['licence']['commit'][:8], r['licence']['line'], rd.get('verdict', 'UNREAD'), rd.get('build_exit'), rd.get('built_equal'),
                       len(rd.get('errors') or []), rd.get('sorry_warnings'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'),
                       len(rd.get('axiom_outside') or {}), rd.get('axiom_missing_n'), rd.get('sorryAx'), rd.get('axioms_file_lines'),
                       str(rd.get('axioms_sha256'))[:16], rd.get('runner_low_mb'), rd.get('run_min'), rd.get('build_min')))
        if rd:
            out.append('      the axioms print: %s ; the cache`s record: input %s, the restore line %s, files before the build %s, completed %s, key present '
                       'before the save %s, save %s -> THE RESTORE`S KIND %s (restored %s, by the prefix %s), saved %s, from source %s, untouched %s' % (
                           rd.get('axioms_print'), cr.get('input'), cr.get('hit'), cr.get('files_before'), cr.get('completed'), cr.get('present_before'),
                           cr.get('save'), rd.get('restore_kind'), cr.get('restored'), cr.get('by_prefix'), cr.get('saved'), cr.get('from_source'),
                           cr.get('untouched')))
            if rd.get('part_one_exit') is not None:
                out.append('      ROUTE (i): part one %s modules, its exit %s, its errors %d, the low %s MB ; part two the low %s MB' % (
                    rd.get('part_one_modules'), rd.get('part_one_exit'), len(rd.get('part_one_errors') or []), rd.get('low_part_one'), rd.get('low_part_two')))
            for nm, st, why in rd.get('names') or []:
                out.append('      %s %s %s' % (nm, st, why))
    out.append('')
    vl, v = verdict_lines(rows)
    out += vl + ['']
    nd = len(disp)
    steps = [r for r in disp if r.get('item') in STEP_ITEMS]
    out.append('  THE LAST STEP`S DISPATCH: %s (the hour %s)' % (steps[-1].get('at') if steps else 'none', LAST_STEP))
    out.append('### ### **DISPATCHES %d OF AT MOST %d (WITH THE RESTORE ON %d OF AT MOST %d) ; THE TRIAL %s ; THE PAIR %s ; MAIN AND THE TAG: %s ; THE '
               'TOOL`S CONTROLS %d OF %d.**' % (nd, K.MAX_DISPATCHES, sum(1 for r in disp if r.get('item') in ON_ITEMS), ON_CAP, v['trial']['state'],
                                                 v['pair']['state'], v['main'], sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b768_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'targets': cmd_targets, 'lean': cmd_lean, 'presend': cmd_presend, 'dispatch': cmd_dispatch, 'status': cmd_status,
          'download': cmd_download, 'read': cmd_read, 'errors': cmd_errors, 'axioms': cmd_axioms, 'compare': cmd_compare, 'verdict': cmd_verdict,
          'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
