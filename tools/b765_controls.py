# -*- coding: utf-8 -*-
"""tools/b765_controls.py -- (R375)(4), (5): THE RUNNER'S CACHE TRIED AGAIN, THE DISPATCH AND THE READ, carried from tools/b764_controls.py
(b763's form, b759's and b745's before it) by the Write tool and set for b765 before its first run.

THE WORKFLOW AT push-b765-centre (70c50d37 on): the save keyed by the toolchain, the manifest and the commit built, the restore by the prefix
of the first two (data/b764_misses.txt (4)), the restored key recorded, a run with the restore off neither restoring nor saving. Every run of
this act is dispatched AT push-b765-centre (`gh workflow run --ref push-b765-centre`, the commit to build given as the input ref), so that the
run reads the centre's workflow file and the centre's cache scope: a run reads the caches of the ref it runs at and of main alone, so a run at
push-b765-planted would restore nothing and build from source, and the planted build would test no restored build.

THE ITEMS, each with the needle of its clause in the ferry bank (one line), its price row (data/b765_price.json) and its input restore:
  statement        (5)(a), restore on, the tip of push-b765-centre; the no-zero control of (R373)(7) (tools/b763_presend.py, unchanged) passed
                   over the statement's file at the commit before it is sent; the first restore-on dispatch builds from source and saves
  planted          (4)(a) as the author's word of 2026-11-21 on the runner's cache orders it (its (i); data/b765_amendments.json row 2):
                   restore on, the centre's tip, the workflow's input planted on (e83e0deb on), which takes into the runner's checkout the
                   one module the tip of push-b765-planted changes against its parent (a commit of the centre, the module at the tip sent
                   equal to its file there); sent after a read shows a build saved to the cache at the commit sent, so that the run
                   restores the exact key and its record reads "restore hit: true", a hit by either reading; scored only where the record
                   names a key restored, exact or by the prefix (the record's restore line other than none), else printed, NOT SCORED and
                   not counted toward (a); wanted: exit not 0, the log naming the module
  mainsave         the word's (iii): under HELD alone, after main's read-back at the closing commit, one dispatch at main with the restore
                   on, among the ten; wanted: no key restored and a save; where the cap would be passed, the one carried
  lemma-statement  (5)(b), restore on, the centre's tip
  lemma-step       (5)(b), restore on, the centre's tip
  lemma-later      (5)(b), restore on, the centre's tip
  closing          (4)(b), restore off, the centre's tip, after a build with the restore on at that commit read exit 0; after it, a repeat alone
  repeat           (4)(b), the one repeat of a build stopped under the hold (exit 143), at the stopped build's commit and input
THE CAP ((R375)(4), N1): 13 (the worklist's MAX_DISPATCHES): the planted one, at most ten with the restore on (statement and lemma items),
the closing one from source and one repeat; each price row's upper figure besides; one run read before the next is sent.
THE VERDICTS: the planted build's state; the pair's (the restore-on build at the closing commit, restored, beside the closing build from source,
untouched by the cache: both exit 0, the axioms files equal by sha256); H-RUNNER-RESTORE (data/b765_registration.txt PART ONE): HELD,
REFUTED, NOT SCORABLE, OPEN, or UNFORESEEN where a reading the ruling does not name stands; the statement's state ([S1]) from the axioms line of
SIDEExplicitFormula.B321.ControlFailureExists.
No lean process runs on this host (N1); each run is read by its run id from its downloaded artifact, the exit file governing. The kernel's
remote is read from its own git config at each call and its account printed masked; no account name is written by this tool.

  control [--bank]                       the tool's own controls, planted and printed (data/b765_controls_control.txt with --bank)
  targets <rev>                          the whole tree's targets at rev (print_targets.txt, each line resolved to its one module by
                                         tools/b757_join.py's reader), written to data/b765_targets_<sha8>.json for --targets-json
  zero <rev>                             the no-zero control over the statement's file at rev, printed
  planted <rev> --targets-json <file>    the planted context at the centre's commit rev (the word's (i)): push-b765-planted's remote tip,
                                         its parent, its one changed module, its lines changed, the parent an ancestor of rev, the module's
                                         file equal at rev and at the parent, printed
  dispatch <sha> <n> <item> --targets-json <file>   the holds, the caps, the series and the order, the licence (the ferry's bank, or the
                                         author's words bank for the word's items), the commit the remote tip of the item's branch, the
                                         workflow at the centre's tip and at the commit carrying the cache steps and the planted input, the
                                         targets modules of the tree; then gh workflow run at the centre (at main for the save on main), the
                                         planted input on for the planted item alone; the row; the run id read back
  THE VERDICTS gain, by the word: a planted run NOT SCORED where its record names no key restored; the pair NOT SCORABLE where the
  restore-on build at the closing commit names none; the save on main's state. A planted run not scored leaves PART ONE UNFORESEEN, a
  reading neither the ruling nor the word names, for the author.
  status <run> | download <run> | read <n> <run> | errors <run> | axioms <run> | compare <run_a> <run_b>   as b764's
  verdict                                the planted state, the pair, H-RUNNER-RESTORE and the statement's state, printed
  bank                                   data/b765_controls.txt through standing.figbank: the controls, the dispatches and reads, the verdicts
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
import b765_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b765'
ROWS = os.path.join(D, 'b765_dispatch_rows.json')
BANK = os.path.join(D, 'b765_controls.txt')
CONTROL_BANK = os.path.join(D, 'b765_controls_control.txt')
ANSWERS = 'data/b765_ferry.txt'
PRICE = os.path.join(D, 'b765_price.json')
RUNS = 'D:/b765-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
RUNS_ROLE = 'RUNS'         # ### the name a row gives that folder (no host folder written into a bank)
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF = 'SIDE-explicit-formula'
KPATH = CT.KERNELS[EF]
WORKFLOW = 'build-module.yml'
CENTRE = 'push-b765-centre'
PLANTED = 'push-b765-planted'
WF = '.github/workflows/build-module.yml'
ON_CAP = 10                # ### (R375)(4): at most ten with the restore on, the planted one and the repeat beside them
STOPPED = 'STOPPED UNDER THE HOLD'
STATEMENT_FILE = 'SIDEExplicitFormula/ControlFailureExists.lean'
STATEMENT_NAME = 'SIDEExplicitFormula.B321.ControlFailureExists'
N4 = "(4) THE RUNNER'S CACHE, TRIED AGAIN, under W-ORD-RUNNER-CACHE (OPEN_TRAILS :19059)."
N5A = '(a) THE STATEMENT, reading [L-ii] of data/b764_price.txt :55.'
N5B = "(b) GAUSS'S INTEGRAL FOR THE ARCHIMEDEAN TERM, the lemma inside readings [L-i] and [L-iii]"
# ### the author's word of 2026-11-21 on the runner's cache, banked verbatim at data/b765_author_words_preseal.txt :18-:28 (amendment row 2)
WORDS = 'data/b765_author_words_preseal.txt'
W_I = '(i) THE PLANTED BUILD OF (4)(a) is scored on a run whose cache record, out/cache_kernel.txt, reads a restore hit'
W_III = "(iii) THE SAVE ON MAIN. Under the HELD outcome, after main's read-back, one dispatch runs on main with the restore on"
MAIN = 'main'
PLANT_COMMIT = 'e83e0deb'  # ### the centre's commit carrying the workflow's input planted
# ### each item: the needle of its clause, its price row, the input restore it sends (None: the stopped build's), its branch (None: the stopped build's)
ITEMS = {'statement': (N5A, '(5)(a)', 'on', CENTRE),
         'planted': (W_I, '(4)(a) planted', 'on', CENTRE),
         'lemma-statement': (N5B, '(5)(b) statement', 'on', CENTRE),
         'lemma-step': (N5B, '(5)(b) first step', 'on', CENTRE),
         'lemma-later': (N5B, '(5)(b) later lemmas', 'on', CENTRE),
         'closing': (N4, '(4)(b) closing', 'off', CENTRE),
         'repeat': (N4, '(4)(b) closing', None, None),
         'mainsave': (W_III, '(4) the save on main', 'on', MAIN)}
LICENCE_BANK = {'planted': WORDS, 'mainsave': WORDS}   # ### the bank carrying each item's needle; the ferry's bank for the others
EXTRA_CAPS = {'(4) the save on main': 1}               # ### a row the price table (banked before the word) does not carry: the word's one
ON_ITEMS = ('statement', 'lemma-statement', 'lemma-step', 'lemma-later', 'mainsave')
PLANTED_KEYS = (('input', 'planted input: '), ('ref', 'planted ref: '), ('tip', 'planted tip: '), ('parent', 'planted parent: '),
                ('count', 'planted files: '), ('built', 'the commit built: '))
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")
CACHE_KEYS = (('input', 'restore input: '), ('key', 'key: '), ('hit', 'restore hit: '), ('matched', 'restored key: '),
              ('files_before', 'files under .lake/build before the build: '), ('completed', 'build completed under the hold: '),
              ('present_before', 'key present before the save: '), ('save', 'save step: '))
PLANTED_MAX_LINES = 10     # ### (R375)(4)(a): one closing theorem's statement replaced; the price row reads 1-5 lean lines, a line replaced counts 2


def price_rows():
    return dict((r['key'], r) for r in json.load(io.open(PRICE, encoding='utf-8'))['rows'])


def row_caps(pr=None):
    """{price row: its upper dispatch figure} for the rows the items name, read from data/b765_price.json."""
    pr = pr or price_rows()
    return dict((v[1], EXTRA_CAPS[v[1]] if v[1] in EXTRA_CAPS else int(pr[v[1]]['dispatches'][1])) for v in ITEMS.values())


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


def planted_record(text):
    """out/planted.txt read (the workflow at e83e0deb on): the input, the ref, the tip, the parent, each file taken, the count, the commit built,
    the refusal lines; taken where the input is on, the ref push-b765-planted, one file taken and counted, and no refusal; read False where the
    input's line is missing (a run of a workflow before e83e0deb)."""
    f = dict(files=[], refused=[])
    for l in (text or '').replace('\r', '').split(NL):
        if l.startswith('planted file: '):
            f['files'].append(l[len('planted file: '):].split(' sha256 ')[0].strip())
        elif l.startswith('planted file refused'):
            f['refused'].append(l[:200])
        else:
            for k, pre in PLANTED_KEYS:
                if l.startswith(pre) and k not in f:
                    f[k] = l[len(pre):].strip()
    f['read'] = 'input' in f
    f['taken'] = bool(f['read'] and f.get('input') == 'on' and f.get('ref') == PLANTED and len(f['files']) == 1 and f.get('count') == '1'
                      and not f['refused'])
    return f


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


def wf_predicates(text):
    """the workflow file's predicates for (R375)(4): b764's third input and restore step; the key read once from the toolchain and the manifest
    with the commit built; the restore by the prefix; the restored key recorded; the probe and the save at the restore on alone; the records."""
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
        # ### the author's word of 2026-11-21, (i): the input planted, off by default; its step taking push-b765-planted's files, each equal at
        # ### the commit built to its parent's; the probe and the save not run with it on; its record
        input_planted=bool(re.search(r'^      planted:\n(?:        .*\n)*?        default: "off"$', t, re.M)),
        plant_step=("if: inputs.planted == 'on'" in t and 'PLANTED_REF: push-b765-planted' in t and 'git show "$tip:$f" > "$f"' in t
                    and 'if [ "$(git rev-parse "HEAD:$f")" != "$(git rev-parse "$base:$f")" ]; then' in t),
        plant_no_save=t.count("inputs.restore == 'on' && inputs.planted != 'on' && steps.built.outputs.ok == 'true'") == 2,
        plant_record='echo "planted input: $PLANTED" > out/planted.txt' in t and 'echo "planted files: $n" >> out/planted.txt' in t)


B764_PREDICATES = ('input_restore', 'restore_step', 'records')   # ### true at 38a57e02 as at the centre; the other five b765's alone
PLANT_PREDICATES = ('input_planted', 'plant_step', 'plant_no_save', 'plant_record')   # ### true from e83e0deb on, false at d540bc98


# ================================================================================ the planted commit
def planted_judge(names, numstat, at_parent, modules):
    """(module, None) where exactly one file changed, a .lean file standing at the parent, its module among the targets' modules, its lines
    changed (added + deleted) at most PLANTED_MAX_LINES; (None, why) otherwise. Pure: `names` the changed paths, `numstat` [(added, deleted,
    path)], `at_parent` the paths standing at the parent, `modules` the targets' modules."""
    if len(names) != 1:
        return None, '%d files changed (%s), where the planted commit changes one module alone' % (len(names), ' '.join(names[:4]))
    p = names[0]
    if not p.endswith('.lean'):
        return None, 'the one file changed is no .lean file: %s' % p
    if p not in at_parent:
        return None, 'the file %s does not stand at the parent: a module the kernel already builds is changed, none added' % p
    mod = p[:-5].replace('/', '.')
    if mod not in (modules or ()):
        return None, 'the module %s is not among the targets` modules' % mod
    n = sum(int(a) + int(d) for a, d, q in numstat if q == p and str(a).isdigit() and str(d).isdigit())
    if not 1 <= n <= PLANTED_MAX_LINES:
        return None, 'the module %s changed in %d lines, where one statement is replaced (at most %d)' % (mod, n, PLANTED_MAX_LINES)
    return mod, None


def planted_of(sha, modules):
    """the planted commit read at the kernel: (module, why, parent, lines)."""
    parent = git(KPATH, 'rev-parse', sha + '^').strip()
    names = [l for l in git(KPATH, 'diff', '--name-only', parent, sha).split(NL) if l.strip()]
    num = [tuple(l.split('\t')) for l in git(KPATH, 'diff', '--numstat', parent, sha).split(NL) if l.count('\t') == 2]
    mod, why = planted_judge(names, num, set(DR.tree_files(KPATH, parent)), modules)
    return mod, why, parent, sum(int(a) + int(d) for a, d, _q in num if a.isdigit() and d.isdigit())


def planted_ctx(full, modules, heads):
    """the word's (i) at the centre's commit `full`: push-b765-planted's remote tip from `heads`, held locally; its one changed module judged
    against `modules` (the targets at `full`); its parent an ancestor of `full`; the module's file equal at `full` and at the parent, so that
    the workflow's step takes the planted change and nothing else."""
    ptip = next((sha for sha, ref in heads if ref == 'refs/heads/' + PLANTED), None)
    if not ptip:
        return dict(planted=(None, '%s not read at the remote' % PLANTED), parent_on_centre=False, module_equal=False)
    if subprocess.run(['git', '-C', KPATH, 'cat-file', '-e', ptip + '^{commit}'], capture_output=True).returncode != 0:
        return dict(planted=(None, 'the planted tip %s not held in the kernel`s clone' % ptip[:8]), parent_on_centre=False, module_equal=False)
    mod, why, parent, nl = planted_of(ptip, modules)
    names = [l for l in git(KPATH, 'diff', '--name-only', parent, ptip).split(NL) if l.strip()]
    anc = subprocess.run(['git', '-C', KPATH, 'merge-base', '--is-ancestor', parent, full], capture_output=True).returncode == 0
    eq = (len(names) == 1 and subprocess.run(['git', '-C', KPATH, 'diff', '--quiet', parent, full, '--', names[0]],
                                             capture_output=True).returncode == 0)
    return dict(planted=(mod, why), parent_on_centre=anc, module_equal=eq, planted_tip=ptip, planted_parent=parent, planted_lines=nl,
                planted_path=names[0] if len(names) == 1 else None)


def log_names(log, module):
    """the build log's lines naming the module: an error line naming its file, or a failure mark naming the module (at most 5)."""
    if not module:
        return []
    path = module.replace('.', '/') + '.lean'
    out = []
    for l in (log or '').replace('\r', '').split(NL):
        if (('error' in l and path in l) or (module in l and ('\u2716' in l or 'error' in l.lower()))) and l not in out:
            out.append(l[:300])
    return out[:5]


# ================================================================================ the refusals
def dispatch_refusal(item, n, sha, rows, read, dk, caps=None, ctx=None):
    """why a dispatch is refused before anything is sent, or None. Pure: the rows, the free read, the disk read, the row caps and `ctx` (the
    facts read at the kernel: zero_ok, planted (module, why), parent_on_centre) given."""
    caps = caps if caps is not None else row_caps()
    ctx = ctx or {}
    if item not in ITEMS:
        return 'an item (R375) does not order: %r (%s)' % (item, ' | '.join(sorted(ITEMS)))
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    if not 1 <= n <= K.MAX_DISPATCHES:
        return 'dispatch %d past the act`s %d ((R375)(4), N1)' % (n, K.MAX_DISPATCHES)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d rowed already' % n
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in the series (%d rowed)' % (n, len(mine))
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    last = mine[-1] if mine else None
    if last and int(last['run']) not in reads:
        return 'dispatch %d (run %s) not yet read: one run read before the next is sent' % (last['n'], last['run'])
    if any(r.get('item') == 'closing' for r in mine) and item not in ('repeat', 'mainsave'):
        return 'the closing build sent: after it, the repeat of a stopped build and the save on main alone'
    if item == 'repeat':
        if any(r.get('item') == 'repeat' for r in mine):
            return 'the one repeat of (4) sent already'
        if not last:
            return 'no dispatch to repeat'
        rd = reads.get(int(last['run'])) or {}
        if rd.get('verdict') != STOPPED:
            return 'the last dispatch (run %s) not read as stopped under the hold: %s' % (last['run'], rd.get('verdict'))
        if sha != last.get('sha'):
            return 'the repeat at %s where the stopped build was at %s' % (str(sha)[:8], str(last.get('sha'))[:8])
        cl = [r for r in mine if r.get('item') in ('closing', 'repeat')]
        if len(cl) + 1 > caps.get('(4)(b) closing', 0):
            return 'the price row (4)(b) closing`s dispatch %d past its upper figure %d' % (len(cl) + 1, caps.get('(4)(b) closing', 0))
        return None
    if item in ('planted', 'closing', 'mainsave') and any(r.get('item') == item for r in mine):
        return 'the item %s dispatched already: once' % item
    row_ = ITEMS[item][1]
    of_row = [r for r in mine if r.get('item') != 'repeat' and ITEMS.get(r.get('item'), (None, None))[1] == row_]
    if len(of_row) + 1 > caps.get(row_, 0):
        return 'the price row %s`s dispatch %d past its upper figure %d ((R375) N1)' % (row_, len(of_row) + 1, caps.get(row_, 0))
    if item in ON_ITEMS:
        on = [r for r in mine if r.get('item') in ON_ITEMS]
        if len(on) + 1 > ON_CAP:
            return 'the dispatch with the restore on %d past the ten of (R375)(4)' % (len(on) + 1)
    if item == 'statement' and not ctx.get('zero_ok'):
        return 'the no-zero control of (R373)(7) did not pass over %s at %s' % (STATEMENT_FILE, str(sha)[:8])
    if item == 'planted':
        if not any(r.get('kind') == 'read' and (r.get('cache') or {}).get('saved') for r in rows):
            return 'the planted build sent before a read shows a build saved to the cache at the centre: it would build from source'
        # ### the record's own line for a key restored by the prefix reads "restore hit: false": a save at the commit sent gives the planted
        # ### run the exact key, "restore hit: true", a hit by either reading of the word's (i)
        if not any(r.get('kind') == 'read' and (r.get('cache') or {}).get('saved') and r.get('built_ref') == sha for r in rows):
            return 'no save read at the commit sent %s: the planted run would restore by the prefix, its record reading "restore hit: false"' % str(sha)[:8]
        pm = ctx.get('planted') or (None, 'the planted commit not read')
        if pm[1]:
            return 'the planted commit refused: %s' % pm[1]
        if not ctx.get('parent_on_centre'):
            return 'the planted commit`s parent is no ancestor of the commit sent on %s' % CENTRE
        if not ctx.get('module_equal'):
            return 'the planted module at the commit sent differs from its file at the planted commit`s parent: more than the planted change would be taken'
    if item == 'mainsave':
        hv = verdicts(rows)['h']
        if hv[0] != 'HELD':
            return 'the save on main where H-RUNNER-RESTORE reads %s: the author`s word of 2026-11-21 (iii) sends it under HELD alone' % hv[0]
        if not ctx.get('main_read_back'):
            return 'the save on main before main`s read-back at the closing commit'
    if item == 'closing':
        ok_on = [r for r in reads.values() if r.get('restore_input') == 'on' and r.get('item') != 'planted' and r.get('built_ref') == sha
                 and r.get('build_exit') == '0']
        if not ok_on:
            return 'the closing build from source sent before a build with the restore on at %s read exit 0' % str(sha)[:8]
    return None


def tip_refusal(full, heads, branch):
    """None where `full` is the remote tip of `branch`; `heads` [(sha, ref)] from one ls-remote."""
    if not re.match(r'^[0-9a-f]{40}$', full or ''):
        return 'no commit read: %r' % (full,)
    at = [ref for sha, ref in heads if sha == full and ref == 'refs/heads/' + branch]
    return None if at else 'the commit %s is not the remote tip of %s (push it by tools/push_gated.sh --branch first)' % (full[:8], branch)


def centre_tip(heads):
    return next((sha for sha, ref in heads if ref == 'refs/heads/' + CENTRE), None)


def module_files(repo, sha):
    tree = DR.tree_files(repo, sha)
    toml = git(repo, 'show', '%s:lakefile.toml' % sha)
    sds = [s.rstrip('/') for s in re.findall(r'^srcDir\s*=\s*"([^"]+)"', toml, re.M)]
    return tree + [f[len(sd) + 1:] for sd in sds for f in tree if f.startswith(sd + '/')]


def _art(run):
    return os.path.join(RUNS, 'ef-%s' % run, 'build-module-%s' % run)


def _f(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def _targets(art):
    return [l.strip() for l in _f(art, 'print_targets.txt').replace('\r', '').split(NL) if l.strip()]


# ================================================================================ the verdicts
def planted_state(rd):
    if not rd:
        return 'PENDING'
    if rd.get('verdict') == STOPPED:
        return 'STOPPED'
    # ### the author's word of 2026-11-21, (i): a run whose record does not show the module taken is no planted build, and one whose cache
    # ### record names no key restored is printed, not scored and not counted toward (a); each read before the exit file
    if not (rd.get('planted_rec') or {}).get('taken'):
        return 'NOT A PLANTED BUILD'
    if not (rd.get('cache') or {}).get('restored'):
        return 'NOT SCORED'
    if rd.get('build_exit') == '0':
        return 'EXIT 0'
    return 'AS WANTED' if rd.get('names_module') else 'NOT AS WANTED'


def mainsave_state(rd):
    """the word's (iii): the save on main's read; wanted exit 0, the record read with the input on, no key restored and a save."""
    if not rd:
        return 'PENDING'
    if rd.get('verdict') == STOPPED:
        return 'STOPPED'
    c = rd.get('cache') or {}
    ok = (rd.get('build_exit') == '0' and c.get('read') and c.get('input') == 'on' and c.get('hit') == 'none' and c.get('matched') == 'none'
          and c.get('saved'))
    return 'AS WANTED' if ok else 'NOT AS WANTED'


def _ran(r):
    return str((r or {}).get('axioms_print') or '').startswith('RAN')


def pair_verdict(on, off):
    """the pair at the closing commit: `on` the restore-on read there (exit 0), `off` the closing build's read (or its repeat's)."""
    if not off:
        return dict(state='PENDING', where='no closing build from source read')
    if off.get('verdict') == STOPPED:
        return dict(state='STOPPED', where='the closing build stopped under the hold (run %s)' % off.get('run'))
    if (on and on.get('build_exit') == '0' and off.get('build_exit') == '0' and _ran(on) and _ran(off) and on.get('built_ref') == off.get('built_ref')
            and on.get('axioms_sha256') != off.get('axioms_sha256')):
        return dict(state='DIFFERS', where='the axioms files differ by sha256: %s (run %s) and %s (run %s)' % (
            str(on.get('axioms_sha256'))[:16], on.get('run'), str(off.get('axioms_sha256'))[:16], off.get('run')))
    where = []
    if not on:
        where.append('no build with the restore on read exit 0 at the closing commit')
    if off.get('build_exit') != '0':
        where.append('the closing build`s exit file %s' % off.get('build_exit'))
    if not (off.get('cache') or {}).get('untouched'):
        where.append('the closing build not one the cache left untouched (the restore off, nothing restored, nothing saved)')
    if not _ran(off):
        where.append('the closing build`s axioms print %s' % off.get('axioms_print'))
    if on:
        if not on.get('built_equal') or not off.get('built_equal') or on.get('built_ref') != off.get('built_ref'):
            where.append('the two builds not at the one dispatched commit')
        if not _ran(on):
            where.append('the restore-on build`s axioms print %s' % on.get('axioms_print'))
    if where:
        return dict(state='NOT AS WANTED', where='; '.join(where))
    if not (on.get('cache') or {}).get('restored'):
        return dict(state='NOT SCORABLE', where='the restore-on build at the closing commit read no restore hit, a build from source (restored key %s, '
                    'files before the build %s): the pair NOT SCORABLE by it (the author`s word of 2026-11-21, (ii))' % (
                        (on.get('cache') or {}).get('matched'), (on.get('cache') or {}).get('files_before')))
    return dict(state='AS WANTED', where='', sha=on.get('axioms_sha256'), commit=on.get('built_ref'), runs=(on.get('run'), off.get('run')),
                hit=(on.get('cache') or {}).get('hit'))


def h_verdict(pl, pr, stopped_both):
    if pl == 'EXIT 0':
        return 'REFUTED', 'the planted build exited 0'
    if pr['state'] == 'DIFFERS':
        return 'REFUTED', 'the pair`s axioms files differ'
    if stopped_both:
        return 'NOT SCORABLE', 'the closing build from source stopped under the hold at both dispatches'
    if pr['state'] == 'NOT SCORABLE':
        return 'NOT SCORABLE', pr.get('where') or 'the pair not scorable'
    if pl == 'AS WANTED' and pr['state'] == 'AS WANTED':
        return 'HELD', ''
    if pl in ('PENDING', 'STOPPED') or pr['state'] in ('PENDING', 'STOPPED'):
        return 'OPEN', 'the planted %s ; the pair %s' % (pl, pr['state'])
    return 'UNFORESEEN', 'the planted %s ; the pair %s (%s): a reading (R375)(4) does not name' % (pl, pr['state'], pr.get('where'))


def verdicts(rows):
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    pd = [r for r in disp if r.get('item') == 'planted']
    prd = reads.get(int(pd[0]['run'])) if pd else None
    rp_pl = [r for r in disp if r.get('item') == 'repeat' and pd and r.get('n', 0) > pd[0]['n'] and r.get('sha') == pd[0]['sha']]
    if prd and prd.get('verdict') == STOPPED and rp_pl:
        prd = reads.get(int(rp_pl[0]['run'])) or prd
    pl = planted_state(prd)
    cl = [r for r in disp if r.get('item') == 'closing']
    if not cl:
        pr, stopped_both = pair_verdict(None, None), False
    else:
        offs = [reads.get(int(cl[0]['run']))] + [reads.get(int(r['run'])) for r in disp if r.get('item') == 'repeat' and r.get('n', 0) > cl[0]['n']]
        offs = [x for x in offs if x]
        stopped_both = len(offs) == 2 and all(x.get('verdict') == STOPPED for x in offs)
        ons = [reads[int(r['run'])] for r in disp if r.get('n', 0) < cl[0]['n'] and int(r['run']) in reads and r.get('item') != 'planted'
               and reads[int(r['run'])].get('restore_input') == 'on' and reads[int(r['run'])].get('built_ref') == cl[0]['sha']
               and reads[int(r['run'])].get('build_exit') == '0']
        pr = pair_verdict(ons[-1] if ons else None, offs[-1] if offs else None)
    hv = h_verdict(pl, pr, stopped_both)
    md = [r for r in disp if r.get('item') == 'mainsave']
    mrd = reads.get(int(md[0]['run'])) if md else None
    rp_m = [r for r in disp if r.get('item') == 'repeat' and md and r.get('n', 0) > md[0]['n'] and r.get('sha') == md[0]['sha']]
    if mrd and mrd.get('verdict') == STOPPED and rp_m:
        mrd = reads.get(int(rp_m[0]['run'])) or mrd
    return dict(planted=pl, planted_read=prd, pair=pr, stopped_both=stopped_both, h=hv, mainsave=mainsave_state(mrd) if md else 'NOT SENT',
                mainsave_read=mrd)


def statement_state(ax_text, build_exit):
    """([S1]'s reading) COMPILED with the axioms where the build exits 0 and the axioms file carries a line for the statement's name within the
    standard three; NOT COMPILED with why otherwise."""
    ax = axioms_of(ax_text)
    if build_exit != '0':
        return 'NOT COMPILED', 'the exit file %s' % build_exit
    if STATEMENT_NAME not in ax:
        return 'NOT COMPILED', 'no axioms line for %s' % STATEMENT_NAME
    if not set(ax[STATEMENT_NAME]) <= set(STANDARD):
        return 'NOT COMPILED', 'its axioms outside the standard three: %s' % ', '.join(ax[STATEMENT_NAME])
    return 'COMPILED', '[%s]' % ', '.join(ax[STATEMENT_NAME])


def zero_read(rev):
    import b763_presend as Z
    return Z.zero_at(rev, STATEMENT_FILE)


# ================================================================================ the routes
def _tj(path_):
    p = os.path.join(RELAY, path_)
    return json.load(io.open(p, encoding='utf-8')) if os.path.exists(p) else {}


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
    ctip = centre_tip(heads)
    ctx = {}
    if item == 'statement':
        zl, zp = zero_read(full)
        print(NL.join(zl))
        ctx['zero_ok'] = zp
    pmod = None
    if item == 'planted':
        ctx.update(planted_ctx(full, tj['modules'], heads))
        pmod = ctx['planted'][0]
        print('  the planted context at %s (the word`s (i)): %s`s remote tip %s, parent %s, an ancestor of %s: %s ; the module %s (%s) ; lines '
              'changed %s ; its file equal at %s and at the parent: %s ; %s' % (
                  full[:8], PLANTED, str(ctx.get('planted_tip'))[:8], str(ctx.get('planted_parent'))[:8], full[:8], ctx['parent_on_centre'], pmod,
                  ctx.get('planted_path'), ctx.get('planted_lines'), full[:8], ctx['module_equal'], ctx['planted'][1] or 'TAKEN'))
    if item == 'mainsave':
        mtip = next((sha for sha, ref in heads if ref == 'refs/heads/' + MAIN), None)
        pc = verdicts(rows)['pair'].get('commit')
        ctx['main_read_back'] = bool(mtip) and mtip == pc == full
        print('  main at the remote %s ; the pair`s closing commit %s ; the commit sent %s: main`s read-back %s' % (
            str(mtip)[:8], str(pc)[:8], full[:8], ctx['main_read_back']))
    why = dispatch_refusal(item, int(n), full, rows, read, dk, ctx=ctx)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    mode, branch = ITEMS[item][2], ITEMS[item][3]
    planted_on = item == 'planted'
    if item == 'repeat':
        mode, branch = mine[-1].get('restore'), mine[-1].get('branch')
        planted_on = mine[-1].get('planted_input') == 'on'
        pmod = mine[-1].get('planted_module') if planted_on else None
        for k in ('planted_tip', 'planted_parent'):
            ctx[k] = mine[-1].get(k)
    wref = MAIN if branch == MAIN else CENTRE
    target = ' '.join(tj['modules'])
    print('  the targets from %s: %d modules, read at %s' % (rest[1], len(tj['modules']), tj['rev'][:8]))
    for at_, what in ((ctip, 'the centre`s remote tip'), (full, 'the commit')):
        wp = wf_predicates(git(KPATH, 'show', '%s:%s' % (at_, WF))) if at_ else {}
        if not wp or not all(wp.values()):
            sys.exit('### NOT DISPATCHED: the workflow at %s (%s) lacks (4)`s steps: %s' % (what, str(at_)[:8], sorted(x for x, v in wp.items() if not v)))
    why = tip_refusal(full, heads, branch)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    bad = DR.targets_refused(target, module_files(KPATH, full))
    if bad:
        sys.exit('### NOT DISPATCHED: targets not modules of the tree at %s: %s' % (full[:8], bad))
    try:
        lic = DR.licence(LICENCE_BANK.get(item, ANSWERS), ITEMS[item][0], by=read[1])
    except DR.Refused as e:
        sys.exit(str(e))
    print('  dispatch %s, %s (restore %s, planted %s) at %s on %s, the workflow at %s ; the licence %s %s :%d, committed %s ; free %d MB at %s, the hold %d ; '
          'volumes %s, the floor %d' % (n, item, mode, 'on' if planted_on else 'off', full[:8], branch, wref, lic['bank'], lic['commit'][:8], lic['line'],
                                        lic['committed_at'], read[0], read[1], DR.HOLD, dk, FLOOR))
    at0 = _now()
    cmd = ['gh', 'workflow', 'run', WORKFLOW, '--repo', slug, '--ref', wref, '-f', 'ref=' + full, '-f', 'target=' + target, '-f', 'restore=' + mode]
    if planted_on:
        cmd += ['-f', 'planted=on']
    r = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(mask((r.stdout or '') + (r.stderr or ''), owner).strip())
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel=EF, item=item, n=int(n), sha=full, target=target, at=at0, restore=mode, branch=branch,
                           at_ref=wref, planted_input='on' if planted_on else 'off', error=mask(r.stderr or '', owner)[:300]))
    else:
        m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
        rid = m.group(1) if m else ''
        for _ in range(8):
            if rid:
                break
            time.sleep(5)
            lst = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', slug, '--workflow', WORKFLOW, '--event', 'workflow_dispatch', '--branch', wref,
                                             '--limit', '5', '--json', 'databaseId,createdAt'], capture_output=True, text=True, encoding='utf-8').stdout or '[]')
            new = sorted((x['createdAt'], x['databaseId']) for x in lst if x['createdAt'] >= at0)
            rid = str(new[0][1]) if new else ''
        if not rid:
            sys.exit('### DISPATCHED, NO RUN ID READ BACK in 40 s -- no row written; read `gh run list` by hand and row it before any other dispatch')
        rows.append(DR.row('dispatch', read, kernel=EF, item=item, n=int(n), workflow=WORKFLOW, at_ref=wref, branch=branch, restore=mode, sha=full,
                           target=target, run=int(rid), at=at0, licence=lic, disk_mb=dk, tree=module_files(KPATH, full), planted_module=pmod,
                           centre_tip=ctip, planted_input='on' if planted_on else 'off', planted_tip=ctx.get('planted_tip'),
                           planted_parent=ctx.get('planted_parent')))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'item', 'n', 'restore', 'planted_input', 'branch', 'at_ref', 'sha', 'run', 'free_mb', 'at')))


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
    pr_ = planted_record(_f(art, 'planted.txt'))
    if d[0].get('planted_input') == 'on' and pr_.get('tip') != d[0].get('planted_tip'):
        pr_['taken'] = False
        pr_['refused'].append('the planted tip the run took %s is not the tip its row names %s' % (str(pr_.get('tip'))[:8], str(d[0].get('planted_tip'))[:8]))
    if d[0].get('planted_input') == 'on' and pr_.get('built') != d[0]['sha']:
        pr_['taken'] = False
        pr_['refused'].append('the commit built %s is not the commit dispatched %s' % (str(pr_.get('built'))[:8], d[0]['sha'][:8]))
    names = log_names(log, d[0].get('planted_module'))
    st = statement_state(axt, ex)
    rows.append(DR.row('read', DR.free(), kernel=EF, n=int(n), run=int(run), item=d[0].get('item'), restore_input=d[0].get('restore'),
                       planted_input=d[0].get('planted_input', 'off'), planted_rec=pr_, at_ref=d[0].get('at_ref', CENTRE),
                       branch=d[0].get('branch'), status=v['status'], conclusion=v['conclusion'], workflow_branch=v['headBranch'], workflow_sha=v['headSha'],
                       workflow_at_centre=v['headBranch'] == CENTRE and v['headSha'] == d[0].get('centre_tip'),
                       workflow_at_ref=v['headBranch'] == d[0].get('at_ref', CENTRE),
                       built_ref=ref[0] if ref else None, built_equal=bool(ref) and ref[0] == d[0]['sha'], toolchain=ref[-1] if len(ref) > 1 else None,
                       build_exit=ex, verdict=verdict, stop=stop[:3], errors=errs[:40], sorry_warnings=len(warn_sorry), targets=len(targets),
                       axiom_lines=ax['lines'], axiom_within=ax['within'], axiom_outside=dict((a, list(b)) for a, b in ax['outside'].items()),
                       axiom_missing=ax['missing'][:60], axiom_missing_n=len(ax['missing']), sorryAx=ax['sorryAx'],
                       axioms_refused=_f(art, 'axioms_refused.txt')[:300], axioms_print=axp,
                       axioms_file_lines=len(axt.replace('\r', '').rstrip('\n').split(NL)) if axt.strip() else 0,
                       axioms_sha256=hashlib.sha256(axt.replace('\r', '').encode('utf-8')).hexdigest(),
                       cache=cr, build_min=build_minutes(_f(art, 'build_times.txt')), run_min=run_minutes(v['createdAt'], v['updatedAt']),
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], planted_module=d[0].get('planted_module'), names_module=names,
                       statement=list(st), artifact='%s/ef-%s/build-module-%s' % (RUNS_ROLE, run, run)))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('n', 'run', 'item', 'restore_input', 'conclusion', 'workflow_at_centre', 'built_ref', 'built_equal', 'build_exit',
                                   'verdict', 'sorry_warnings', 'targets', 'axiom_lines', 'axiom_within', 'axiom_missing_n', 'sorryAx', 'axioms_file_lines',
                                   'build_min', 'run_min', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
    print('  THE AXIOMS PRINT: %s ; the file`s sha256 %s' % (axp, r['axioms_sha256'][:16]))
    print('  THE CACHE`S RECORD: %s' % dict((x, cr.get(x)) for x in ('read', 'input', 'hit', 'matched', 'files_before', 'completed', 'present_before', 'save',
                                                                      'restored', 'by_prefix', 'saved', 'from_source', 'untouched')))
    print('  THE STATEMENT %s: %s (%s)' % (STATEMENT_NAME, st[0], st[1]))
    print('  THE PLANTED RECORD (out/planted.txt): %s' % dict((x, pr_.get(x)) for x in ('read', 'input', 'ref', 'tip', 'parent', 'files', 'count', 'built',
                                                                                     'refused', 'taken')))
    if d[0].get('item') in ('planted', 'mainsave') or d[0].get('planted_input') == 'on':
        print('  THE STATE BY THE WORD OF 2026-11-21: %s' % (planted_state(r) if d[0].get('planted_input') == 'on' else mainsave_state(r)))
    if d[0].get('planted_module'):
        print('  THE PLANTED MODULE %s NAMED BY THE LOG IN %d LINES:' % (d[0]['planted_module'], len(names)))
        for l in names:
            print('    ' + l)
    for l in (r['axioms_refused'] or '').split(NL):
        if l.strip():
            print('  REFUSED BY THE WORKFLOW`S GRAMMAR: %s' % l.strip())
    for nm, a in sorted(ax['outside'].items()):
        print('  OUTSIDE THE STANDARD THREE: %s [%s]' % (nm, ', '.join(a)))
    for nm in ax['missing'][:40]:
        print('  NO AXIOMS LINE: %s' % nm)
    for l in errs[:20]:
        print('  ERR', l[:300])


def cmd_errors(run):
    log = _f(_art(run), 'build.log').split(NL)
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
    out = os.path.join(D, 'b765_targets_%s.json' % full[:8])
    s = json.dumps(dict(rev=full, names=n, modules=mods, refused=bad, at=_now(),
                        reader='tools/b757_join.py targets_at, through tools/b758_presend.py, both unchanged'), indent=1) + NL
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('written data/%s: %d modules for %d names at %s' % (os.path.basename(out), len(mods), n, full[:8]))


def cmd_zero(rev):
    zl, zp = zero_read(rev)
    print(NL.join(zl))
    print('### THE NO-ZERO CONTROL OVER %s AT %s: %s' % (STATEMENT_FILE, rev, 'PASSED' if zp else 'REFUSED'))


def cmd_planted(rev, *rest):
    if list(rest[:1]) != ['--targets-json'] or len(rest) != 2:
        sys.exit('### usage: planted <rev> --targets-json <file>')
    full = git(KPATH, 'rev-parse', rev).strip()
    tj = _tj(rest[1])
    if tj.get('rev') != full:
        sys.exit('### the targets file read at %s, not at %s' % (str(tj.get('rev'))[:8], full[:8]))
    heads = heads_now()
    ctip = centre_tip(heads)
    c = planted_ctx(full, tj['modules'], heads)
    print('### THE PLANTED CONTEXT AT %s (%s`s remote tip %s, the commit the remote tip: %s): %s`s tip %s, parent %s, an ancestor: %s ; the module '
          '%s (%s) ; lines changed %s ; its file equal at the commit and at the parent: %s ; %s' % (
              full[:8], CENTRE, str(ctip)[:8], ctip == full, PLANTED, str(c.get('planted_tip'))[:8], str(c.get('planted_parent'))[:8],
              c['parent_on_centre'], c['planted'][0], c.get('planted_path'), c.get('planted_lines'), c['module_equal'], c['planted'][1] or 'TAKEN'))


def verdict_lines(rows=None):
    rows = rows if rows is not None else _rows()
    v = verdicts(rows)
    pr = v['pair']
    L = ['## THE VERDICTS OF (R375)(4) AND (5)(a)',
         '  THE PLANTED BUILD: %s%s' % (v['planted'], (' (run %s, the module %s, exit %s, restored %s, the log naming it in %d lines)' % (
             v['planted_read'].get('run'), v['planted_read'].get('planted_module'), v['planted_read'].get('build_exit'),
             (v['planted_read'].get('cache') or {}).get('restored'), len(v['planted_read'].get('names_module') or []))) if v['planted_read'] else ''),
         '  THE PAIR: %s%s' % (pr['state'], (' ; ' + pr['where']) if pr.get('where') else (' ; at %s, sha256 %s, runs %s, the restore-on build`s restore line %s' % (
             str(pr.get('commit'))[:8], str(pr.get('sha'))[:16], pr.get('runs'), pr.get('hit')) if pr['state'] == 'AS WANTED' else '')),
         '  H-RUNNER-RESTORE: %s%s' % (v['h'][0], (' ; ' + v['h'][1]) if v['h'][1] else ''),
         '  THE SAVE ON MAIN (the word`s (iii)): %s%s' % (v['mainsave'], (' (run %s, exit %s, hit %s, restored key %s, saved %s)' % (
             v['mainsave_read'].get('run'), v['mainsave_read'].get('build_exit'), (v['mainsave_read'].get('cache') or {}).get('hit'),
             (v['mainsave_read'].get('cache') or {}).get('matched'), (v['mainsave_read'].get('cache') or {}).get('saved'))) if v['mainsave_read'] else '')]
    if v['planted_read']:
        L.append('  THE PLANTED RECORD: taken %s, tip %s, parent %s, files %s, the commit built %s, refused %s ; the cache`s restore line %s, restored key %s' % (
            (v['planted_read'].get('planted_rec') or {}).get('taken'), str((v['planted_read'].get('planted_rec') or {}).get('tip'))[:8],
            str((v['planted_read'].get('planted_rec') or {}).get('parent'))[:8], (v['planted_read'].get('planted_rec') or {}).get('files'),
            str((v['planted_read'].get('planted_rec') or {}).get('built'))[:8], (v['planted_read'].get('planted_rec') or {}).get('refused'),
            (v['planted_read'].get('cache') or {}).get('hit'), str((v['planted_read'].get('cache') or {}).get('matched'))[:48]))
    st = [r for r in rows if r.get('kind') == 'read' and r.get('item') == 'statement']
    for r in st:
        L.append('  THE STATEMENT, run %s at %s: %s (%s)' % (r.get('run'), str(r.get('built_ref'))[:8], (r.get('statement') or ['?', '?'])[0],
                                                         (r.get('statement') or ['?', '?'])[1]))
    if not st:
        L.append('  THE STATEMENT: no read of its dispatch')
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
    caps = row_caps()
    want_caps = {'(5)(a)': 2, '(4)(a) planted': 1, '(5)(b) statement': 1, '(5)(b) first step': 2, '(5)(b) later lemmas': 5, '(4)(b) closing': 2,
                 '(4) the save on main': 1}
    c('each price row`s cap, its upper dispatch figure (data/b765_price.json), and the word`s save on main at 1 beside them', caps, caps == want_caps)
    on_sum = sum(caps[ITEMS[i][1]] for i in ON_ITEMS)
    c('the kernel`s cap (the worklist`s MAX_DISPATCHES) against the rows` upper figures, the restore-on rows` sum against the ten of (4): the '
      'price rows 13 and 10, the word`s one beside them, held by the 13 and the ten (where the cap would be passed, the save on main carried)',
      (K.MAX_DISPATCHES, sum(caps.values()), on_sum, ON_CAP), K.MAX_DISPATCHES == 13 and sum(caps.values()) == 14 and on_sum == 11 and ON_CAP == 10)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    A, B = 'a' * 40, 'b' * 40

    def D_(n, item, run, restore='on', sha=A):
        return dict(kind='dispatch', kernel=EF, n=n, item=item, run=run, restore=restore, sha=sha)

    def R_(run, item, restore='on', ex='0', verdict='KERNEL', saved=False, sha=A):
        return dict(kind='read', kernel=EF, run=run, item=item, restore_input=restore, build_exit=ex, verdict=verdict, built_ref=sha, cache=dict(saved=saved))
    okz = dict(zero_ok=True)
    okp = dict(planted=('SIDEExplicitFormula.X', None), parent_on_centre=True, module_equal=True)
    st1 = [D_(1, 'statement', 11), R_(11, 'statement', saved=True)]
    tenlater = []
    for i in range(10):
        tenlater += [D_(i + 1, 'lemma-later', 100 + i), R_(100 + i, 'lemma-later')]
    plants = [('form', 1, A, [], good, dk, None, okz),
              ('statement', 1, A, [], (2000, _now()), dk, None, okz),
              ('statement', 1, A, [], good, {'C:/': 4000, 'D:/': 20000}, None, okz),
              ('statement', 14, A, [], good, dk, None, okz),
              ('statement', 2, A, [], good, dk, None, okz),
              ('statement', 1, A, [D_(1, 'statement', 11)], good, dk, None, okz),
              ('lemma-step', 2, A, [D_(1, 'statement', 11)], good, dk, None, okz),
              ('planted', 1, B, [], good, dk, None, okp),
              ('planted', 2, A, st1, good, dk, None, dict(planted=(None, 'two files changed'), parent_on_centre=True, module_equal=True)),
              ('planted', 2, A, st1, good, dk, None, dict(planted=('SIDEExplicitFormula.X', None), parent_on_centre=False, module_equal=True)),
              ('planted', 2, A, st1, good, dk, None, dict(planted=('SIDEExplicitFormula.X', None), parent_on_centre=True, module_equal=False)),
              ('planted', 2, B, st1, good, dk, None, okp),
              ('statement', 1, A, [], good, dk, None, dict(zero_ok=False)),
              ('closing', 2, A, [D_(1, 'statement', 11), R_(11, 'statement', ex='1', verdict='BREAKS')], good, dk, None, {}),
              ('closing', 2, A, [D_(1, 'statement', 11, sha=B), R_(11, 'statement', sha=B)], good, dk, None, {}),
              ('statement', 3, A, st1 + [D_(2, 'statement', 12), R_(12, 'statement')], good, dk, None, okz),
              ('lemma-later', 11, A, tenlater, good, dk, dict(want_caps, **{'(5)(b) later lemmas': 11}), {}),
              ('repeat', 2, A, st1, good, dk, None, {}),
              ('repeat', 3, A, [D_(1, 'statement', 11), R_(11, 'statement', verdict=STOPPED, ex='143'), D_(2, 'repeat', 12),
                                R_(12, 'repeat', verdict=STOPPED, ex='143')], good, dk, None, {}),
              ('statement', 3, A, st1 + [D_(2, 'closing', 12, restore='off'), R_(12, 'closing', restore='off')], good, dk, None, okz),
              ('planted', 3, B, st1 + [D_(2, 'planted', 12, sha=B), R_(12, 'planted', ex='1', verdict='BREAKS', sha=B)], good, dk, None, okp),
              ('repeat', 2, A, [D_(1, 'closing', 11, restore='off', sha=B), R_(11, 'closing', restore='off', verdict=STOPPED, ex='143', sha=B)],
               good, dk, None, {})]
    got = [dispatch_refusal(p[0], p[1], p[2], p[3], p[4], p[5], caps=p[6] or want_caps, ctx=p[7]) for p in plants]
    c('twenty-two planted dispatches refused (an item (R375) does not order, under the hold, under the floor, past 13, out of series, rowed already, '
      'the last run unread, the planted before any save, the planted commit refused, its parent no ancestor of the commit sent, its module`s file '
      'differing at the commit sent from the parent`s, the planted at a commit with no save read there, the no-zero control not passed, '
      'the closing before a restore-on build exiting 0, the closing at another commit than that build, (5)(a)`s third, the eleventh with the '
      'restore on, a repeat of a build not stopped, a second repeat, an item after the closing, the planted twice, a repeat at another commit)',
      [bool(x) for x in got], all(got))
    passes = [dispatch_refusal('statement', 1, A, [], good, dk, caps=want_caps, ctx=okz),
              dispatch_refusal('planted', 2, A, st1, good, dk, caps=want_caps, ctx=okp),
              dispatch_refusal('closing', 3, A, st1 + [D_(2, 'planted', 12, sha=B), R_(12, 'planted', ex='1', verdict='BREAKS', sha=B)], good, dk,
                               caps=want_caps, ctx={}),
              dispatch_refusal('repeat', 4, A, st1 + [D_(2, 'planted', 12, sha=B), R_(12, 'planted', ex='1', verdict='BREAKS', sha=B),
                                                     D_(3, 'closing', 13, restore='off'), R_(13, 'closing', restore='off', verdict=STOPPED, ex='143')],
                               good, dk, caps=want_caps, ctx={}),
              dispatch_refusal('lemma-step', 2, A, st1, good, dk, caps=want_caps, ctx={})]
    c('five planted dispatches taken (the statement first ; the planted after a save`s read ; the closing after the restore-on build at its commit ; '
      'the repeat of a stopped closing build ; a lemma step after the statement)', passes, passes == [None] * 5)
    lic = {}
    for bank_, nd, want_line in ((ANSWERS, N4, 17), (ANSWERS, N5A, 20), (ANSWERS, N5B, 21), (WORDS, W_I, 23), (WORDS, W_III, 25)):
        try:
            x = DR.licence(bank_, nd)
            lic[nd[:12]] = (x['commit'][:8], x['line'], x['line'] == want_line)
        except DR.Refused as e:
            lic[nd[:12]] = str(e)[:60]
    c('the licences at the committed banks: the ferry`s (4) at :17, (5)(a) at :20, (5)(b) at :21 ; the author`s words bank`s word of 2026-11-21 on '
      'the cache, its (i) at :23 and its (iii) at :25', lic, all(isinstance(v, tuple) and v[2] for v in lic.values()))
    c('each item`s licence bank: the planted and the save on main at the author`s words bank, the others at the ferry`s',
      dict((i, LICENCE_BANK.get(i, ANSWERS)) for i in sorted(ITEMS)),
      all(LICENCE_BANK.get(i, ANSWERS) == (WORDS if i in ('planted', 'mainsave') else ANSWERS) for i in ITEMS))
    try:
        DR.licence(ANSWERS, '(15) A CLAUSE THE RULING DOES NOT HAVE')
        miss = False
    except DR.Refused:
        miss = True
    c('a needle the ferry does not carry refused', miss, miss)
    slug, owner = remote()
    c('the kernel`s remote read from its own config, printed masked', mask(slug, owner),
      mask(slug, owner).startswith('<account>/') and bool(owner) and owner not in mask('https://github.com/%s/x/actions/runs/1' % slug, owner))
    t1 = DR.targets_refused('SIDEExplicitFormula.ControlFailureExists', module_files(KPATH, 'd540bc98'))
    t2 = DR.targets_refused('SIDEExplicitFormula.ControlFailureExists', module_files(KPATH, '70c50d37'))
    t3 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', module_files(KPATH, 'd540bc98'))
    c('targets: the statement`s module taken at d540bc98 and refused at 70c50d37 (no file) ; a vendored module under its srcDir taken',
      (t1, len(t2), t3), t1 == [] and len(t2) == 1 and t3 == [])
    pl = [axioms_print("out/Axioms.lean:1:0: error: import X failed", axioms_read("out/Axioms.lean:1:0: error: x", ['a'])),
          axioms_print("NOT RUN: the build did not complete under the hold", axioms_read('', ['a'])),
          axioms_print("'a' depends on axioms: [propext]", axioms_read("'a' depends on axioms: [propext]", ['a']))]
    c('the axioms print`s state on three planted files (an import failure, the NOT RUN line, a clean print)', [x[:24] for x in pl],
      pl[0].startswith('FAILED, NO AXIOMS LINE') and pl[1].startswith('NOT RUN') and pl[2] == 'RAN')
    heads = [(A, 'refs/heads/' + CENTRE), (B, 'refs/heads/' + PLANTED), ('c' * 40, 'refs/heads/main'), ('e' * 40, 'refs/heads/push-b764-runner')]
    tp = (tip_refusal(A, heads, CENTRE), tip_refusal(B, heads, PLANTED), bool(tip_refusal(B, heads, CENTRE)), bool(tip_refusal('c' * 40, heads, CENTRE)),
          bool(tip_refusal('e' * 40, heads, CENTRE)), bool(tip_refusal('', heads, CENTRE)), centre_tip(heads) == A, tip_refusal('c' * 40, heads, MAIN),
          bool(tip_refusal(A, heads, MAIN)))
    c('the remote tip: the centre`s tip taken for the centre ; the planted tip for the planted ; the planted tip refused for the centre ; main`s, '
      'push-b764-runner`s and no commit refused for the centre ; the centre`s tip read ; main`s tip taken for main, the centre`s refused for it',
      tp, tp == (None, None, True, True, True, True, True, None, True))
    tj7 = json.load(io.open(os.path.join(D, 'b765_targets_7d86a245.json'), encoding='utf-8'))
    p_tip = git(KPATH, 'rev-parse', '7d86a245').strip()
    pcx = [planted_ctx(git(KPATH, 'rev-parse', PLANT_COMMIT).strip(), tj7['modules'], [(p_tip, 'refs/heads/' + PLANTED)]),
           planted_ctx(git(KPATH, 'rev-parse', K.RUNNER_COMMIT).strip(), tj7['modules'], [(p_tip, 'refs/heads/' + PLANTED)]),
           planted_ctx(git(KPATH, 'rev-parse', PLANT_COMMIT).strip(), tj7['modules'], [])]
    pv_ = [(x['planted'][0], x['parent_on_centre'], x['module_equal']) for x in pcx]
    c('the planted context at real commits (the planted tip 7d86a245 as push-b765-planted`s remote tip): at %s the module taken, the parent an '
      'ancestor, its file equal ; at b764`s 38a57e02 the parent no ancestor ; with no remote tip read, refused' % PLANT_COMMIT, pv_,
      pv_[0] == ('SIDEExplicitFormula.SquaresAt24', True, True) and pv_[1][1] is False and pv_[2] == (None, False, False))
    tf, tm, tb, tn = targets_of(K.EF_BASE_B763)
    bj = json.load(io.open(os.path.join(D, 'b759_targets.json'), encoding='utf-8'))
    c('THE POSITIVE CONTROL: the targets reader at a3aad4cc against b759`s targets bank (data/b759_targets.json: %d modules for %d names)' % (
        len(bj['modules']), bj['names']), (tf[:8], len(tm), tn, len(tb)), tf == bj['rev'] and tm == sorted(bj['modules']) and tn == bj['names'] and not tb)
    wn = wf_predicates(git(KPATH, 'show', '%s:%s' % (PLANT_COMMIT, WF)))
    wd = wf_predicates(git(KPATH, 'show', 'd540bc98:%s' % WF))
    wo = wf_predicates(git(KPATH, 'show', '%s:%s' % (K.RUNNER_COMMIT, WF)))
    c('the workflow`s predicates for (R375)(4) and the word`s (i): each true at the centre`s %s ; at d540bc98 the four of the planted input false '
      'and the others true ; THE PLANTED FAULT, b764`s workflow at 38a57e02: its three true and the others false' % PLANT_COMMIT,
      (sum(wn.values()), len(wn), sorted(k for k, v in wd.items() if not v), sorted(k for k, v in wo.items() if v)),
      all(wn.values()) and sorted(k for k, v in wd.items() if not v) == sorted(PLANT_PREDICATES)
      and sorted(k for k, v in wo.items() if v) == sorted(B764_PREDICATES))
    recs = [cache_record('restore input: on\nkey: kernel-build-x-aaaa\nrestore hit: false\nrestored key: none\nfiles under .lake/build before the build: 0\n'
                         'build completed under the hold: true\nkey present before the save: false\nsave step: success\n'),
            cache_record('restore input: on\nkey: kernel-build-x-bbbb\nrestore hit: false\nrestored key: kernel-build-x-aaaa\n'
                         'files under .lake/build before the build: 4120\nbuild completed under the hold: true\nkey present before the save: false\n'
                         'save step: success\n'),
            cache_record('restore input: on\nkey: kernel-build-x-bbbb\nrestore hit: true\nrestored key: kernel-build-x-bbbb\n'
                         'files under .lake/build before the build: 4130\nbuild completed under the hold: true\nkey present before the save: true\n'
                         'save step: skipped\n'),
            cache_record('restore input: off\nkey: kernel-build-x-bbbb\nrestore hit: none\nrestored key: none\nfiles under .lake/build before the build: 0\n'
                         'build completed under the hold: true\nkey present before the save: none\nsave step: skipped\n'),
            cache_record('restore input: on\nkey: kernel-build-x-aaaa\nrestore hit: true\n')]
    rv = [(r['read'], r['restored'], r['by_prefix'], r['saved'], r['from_source'], r['untouched']) for r in recs]
    c('the cache`s record on five planted files (the first save, built from source ; a restore by the prefix, then saved ; an exact restore ; the '
      'restore off ; a record cut short): (read, restored, by prefix, saved, from source, untouched)', rv,
      rv == [(True, False, False, True, True, False), (True, True, True, True, False, False), (True, True, False, False, False, False),
             (True, False, False, False, True, True), (False, False, False, False, False, False)])
    pj = [planted_judge(['SIDEExplicitFormula/X.lean'], [('1', '1', 'SIDEExplicitFormula/X.lean')], {'SIDEExplicitFormula/X.lean'}, ['SIDEExplicitFormula.X']),
          planted_judge(['SIDEExplicitFormula/X.lean', 'print_targets.txt'], [], {'SIDEExplicitFormula/X.lean'}, ['SIDEExplicitFormula.X']),
          planted_judge(['.github/workflows/build-module.yml'], [], set(), ['SIDEExplicitFormula.X']),
          planted_judge(['SIDEExplicitFormula/Y.lean'], [('3', '0', 'SIDEExplicitFormula/Y.lean')], set(), ['SIDEExplicitFormula.Y']),
          planted_judge(['SIDEExplicitFormula/X.lean'], [('8', '6', 'SIDEExplicitFormula/X.lean')], {'SIDEExplicitFormula/X.lean'}, ['SIDEExplicitFormula.X']),
          planted_judge(['SIDEExplicitFormula/Z.lean'], [('1', '1', 'SIDEExplicitFormula/Z.lean')], {'SIDEExplicitFormula/Z.lean'}, ['SIDEExplicitFormula.X'])]
    c('the planted commit`s judge on six planted changes (one statement replaced, taken ; two files ; no .lean file ; a file added ; 14 lines ; a '
      'module beside the targets)', [x[0] is not None for x in pj], [x[0] is not None for x in pj] == [True, False, False, False, False, False])
    rj = [planted_of(git(KPATH, 'rev-parse', 'd540bc98').strip(), ['SIDEExplicitFormula.ControlFailureExists']),
          planted_of(git(KPATH, 'rev-parse', '70c50d37').strip(), ['SIDEExplicitFormula.ControlFailureExists'])]
    c('the judge at two real commits of the centre, each refused as a planted commit (d540bc98: two files ; 70c50d37: the workflow alone)',
      [(x[0], (x[1] or '')[:40]) for x in rj], all(x[0] is None and x[1] for x in rj))
    logp = ('\u2716 [5/9] Building SIDEExplicitFormula.X\nerror: ./SIDEExplicitFormula/X.lean:3:2: type mismatch\nerror: build failed\n')
    ln = (len(log_names(logp, 'SIDEExplicitFormula.X')), len(log_names(logp.replace('X', 'W'), 'SIDEExplicitFormula.X')), len(log_names('', 'SIDEExplicitFormula.X')),
          len(log_names(logp, None)))
    c('the log`s lines naming the module on planted logs (its failure ; another module`s ; empty ; no module named)', ln, ln[0] >= 2 and ln[1:] == (0, 0, 0))
    base = dict(build_exit='0', axioms_print='RAN', built_ref=A, built_equal=True, axioms_sha256='f' * 64, verdict='KERNEL')
    on = dict(base, run=21, restore_input='on', cache=recs[1])
    off = dict(base, run=22, restore_input='off', cache=recs[3])
    pv = [pair_verdict(on, off)['state'], pair_verdict(on, dict(off, axioms_sha256='0' * 64))['state'],
          pair_verdict(dict(on, cache=recs[0]), off)['state'], pair_verdict(on, dict(off, build_exit='1', verdict='BREAKS'))['state'],
          pair_verdict(on, None)['state'], pair_verdict(on, dict(off, verdict=STOPPED, build_exit='143'))['state'],
          pair_verdict(None, off)['state']]
    c('the pair on seven planted readings (as wanted ; the files differing ; the restore-on build reading no restore hit, NOT SCORABLE by the '
      'word`s (ii) ; the closing exiting 1 ; no closing read ; the closing stopped ; no restore-on build)', pv,
      pv == ['AS WANTED', 'DIFFERS', 'NOT SCORABLE', 'NOT AS WANTED', 'PENDING', 'STOPPED', 'NOT AS WANTED'])
    prec = planted_record('planted input: on\nplanted ref: %s\nplanted tip: %s\nplanted parent: %s\nplanted file: SIDEExplicitFormula/X.lean sha256 %s\n'
                          'planted files: 1\nthe commit built: %s\n' % (PLANTED, B, 'd' * 40, '0' * 64, A))
    precs = [prec, planted_record('planted input: off\n'),
             planted_record('planted input: on\nplanted ref: %s\nplanted tip: %s\nplanted file refused (the file at the commit built differs from '
                            'the parent`s): SIDEExplicitFormula/X.lean\n' % (PLANTED, B)),
             planted_record(''),
             planted_record('planted input: on\nplanted ref: push-b764-runner\nplanted file: SIDEExplicitFormula/X.lean sha256 0\nplanted files: 1\n')]
    pq = [(x['read'], x['taken'], len(x['files'])) for x in precs]
    c('the planted record on five planted files (taken ; the input off ; a file refused ; no file, a run before e83e0deb ; another ref): (read, '
      'taken, files)', pq, pq == [(True, True, 1), (True, False, 0), (True, False, 0), (False, False, 0), (True, False, 1)])
    prd = dict(build_exit='1', verdict='BREAKS', cache=recs[1], names_module=['error: ./SIDEExplicitFormula/X.lean:3:2'], planted_rec=prec)
    ps = [planted_state(prd), planted_state(dict(prd, build_exit='0', verdict='KERNEL')), planted_state(dict(prd, cache=recs[0])),
          planted_state(dict(prd, names_module=[])), planted_state(dict(prd, verdict=STOPPED, build_exit='143')), planted_state(None),
          planted_state(dict(prd, planted_rec=precs[1])), planted_state(dict(prd, cache=recs[0], build_exit='0', verdict='KERNEL')),
          planted_state(dict(prd, cache=recs[2]))]
    c('the planted state on nine planted reads (as wanted, restored by the prefix ; exit 0 ; no key restored, NOT SCORED by the word`s (i) ; the log '
      'not naming it ; stopped ; unread ; the module not taken ; exit 0 with no key restored, NOT SCORED before the exit ; as wanted, an exact key)', ps,
      ps == ['AS WANTED', 'EXIT 0', 'NOT SCORED', 'NOT AS WANTED', 'STOPPED', 'PENDING', 'NOT A PLANTED BUILD', 'NOT SCORED', 'AS WANTED'])
    aw, df, pe = dict(state='AS WANTED'), dict(state='DIFFERS'), dict(state='PENDING')
    hv = [h_verdict('AS WANTED', aw, False)[0], h_verdict('EXIT 0', aw, False)[0], h_verdict('AS WANTED', df, False)[0],
          h_verdict('AS WANTED', dict(state='STOPPED'), True)[0], h_verdict('PENDING', pe, False)[0],
          h_verdict('NOT SCORED', aw, False)[0], h_verdict('AS WANTED', dict(state='NOT SCORABLE', where='x'), False)[0],
          h_verdict('NOT A PLANTED BUILD', aw, False)[0]]
    c('H-RUNNER-RESTORE on eight planted pairs (both as wanted ; the planted exiting 0 ; the files differing ; the closing stopped twice ; pending ; '
      'the planted not scored, a reading neither the ruling nor the word names ; the pair NOT SCORABLE by the word`s (ii) ; no planted build)', hv,
      hv == ['HELD', 'REFUTED', 'REFUTED', 'NOT SCORABLE', 'OPEN', 'UNFORESEEN', 'NOT SCORABLE', 'UNFORESEEN'])
    held_rows = [D_(1, 'statement', 11), dict(R_(11, 'statement', saved=True), cache=recs[0], axioms_print='RAN', built_equal=True, axioms_sha256='f' * 64),
                 D_(2, 'planted', 12, sha=B), dict(prd, kind='read', kernel=EF, run=12, item='planted', restore_input='on', built_ref=B),
                 D_(3, 'lemma-step', 13), dict(on, kind='read', kernel=EF, run=13, item='lemma-step'),
                 D_(4, 'closing', 14, restore='off'), dict(off, kind='read', kernel=EF, run=14, item='closing')]
    vr = verdicts(held_rows)
    c('the verdicts over a planted series (the statement saved, the planted failing restored, a restored lemma build, the closing from source)',
      (vr['planted'], vr['pair']['state'], vr['h'][0], vr['mainsave']), (vr['planted'], vr['pair']['state'], vr['h'][0], vr['mainsave']) == (
          'AS WANTED', 'AS WANTED', 'HELD', 'NOT SENT'))
    real1 = cache_record(_f(_art(44900549948), 'cache_kernel.txt'))
    ms = [mainsave_state(dict(build_exit='0', cache=real1)), mainsave_state(dict(build_exit='0', cache=recs[1])),
          mainsave_state(dict(build_exit='0', cache=recs[2])), mainsave_state(dict(build_exit='1', cache=real1)), mainsave_state(None),
          mainsave_state(dict(build_exit='0', cache=recs[0]))]
    c('the save on main`s state: THE POSITIVE CONTROL, the real record of dispatch 1 (run 44900549948, the centre`s first save, from source, '
      'its restore line none), then five planted reads (restored by the prefix ; an exact key, no save ; exit 1 ; unread ; a restore line '
      'false with no key)', ms, ms == ['AS WANTED', 'NOT AS WANTED', 'NOT AS WANTED', 'NOT AS WANTED', 'PENDING', 'NOT AS WANTED'])
    mr = [dispatch_refusal('mainsave', 5, A, held_rows, good, dk, caps=want_caps, ctx=dict(main_read_back=True)),
          dispatch_refusal('mainsave', 5, A, held_rows, good, dk, caps=want_caps, ctx={}),
          dispatch_refusal('mainsave', 2, A, st1, good, dk, caps=want_caps, ctx=dict(main_read_back=True)),
          dispatch_refusal('mainsave', 6, A, held_rows + [D_(5, 'mainsave', 15), dict(R_(15, 'mainsave'), cache=recs[0])], good, dk, caps=want_caps,
                           ctx=dict(main_read_back=True)),
          dispatch_refusal('lemma-step', 5, A, held_rows, good, dk, caps=want_caps, ctx={})]
    c('the save on main`s dispatch (taken under HELD after main`s read-back ; refused before it ; refused where H-RUNNER-RESTORE reads OPEN ; '
      'refused a second time ; a lemma step refused after the closing)', [x is None for x in mr], [x is None for x in mr] == [True, False, False, False, False])
    ss = [statement_state("'%s' depends on axioms: [propext]" % STATEMENT_NAME, '0')[0], statement_state("'%s' depends on axioms: [propext]" % STATEMENT_NAME, '1')[0],
          statement_state("'other' depends on axioms: [propext]", '0')[0], statement_state("'%s' depends on axioms: [sorryAx]" % STATEMENT_NAME, '0')[0]]
    c('the statement`s state on four planted prints (its line in the three ; the exit 1 ; no line ; sorryAx)', ss,
      ss == ['COMPILED', 'NOT COMPILED', 'NOT COMPILED', 'NOT COMPILED'])
    zl, zp = zero_read('d540bc98')
    c('the no-zero control of (R373)(7) over the statement`s file at d540bc98 (tools/b763_presend.py, unchanged)', zl[2].strip()[:120] if len(zl) > 2 else zl, zp)
    import b763_presend as Z
    zcl, zco = Z.zero_controls()
    c('the no-zero control`s own planted controls, replayed (tools/b763_presend.py zero_controls)', '%d of %d' % (sum(zco), len(zco)), all(zco))
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b765_controls.py`s OWN CONTROLS, (R375)(4) AND (5) AND THE AUTHOR`S WORD OF 2026-11-21 ON THE RUNNER`S CACHE (%s)' % (
        ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R375)(4) AND (5): THE RUNNER`S CACHE TRIED AGAIN, THE DISPATCHES AND THE READS, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '',
           '## THE CONTROLS'] + L + ['  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == EF]
    out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (EF, len(disp), K.MAX_DISPATCHES, len(refused)))
    for r in disp:
        rd = reads.get(int(r['run']), {})
        cr = rd.get('cache') or {}
        out.append('  %d | %-15s | restore %s | sha %s on %s, the workflow at %s | run %s | free %d MB | licence %s :%s | %s, exit %s, built %s, %d errors, '
                   'sorry warnings %s, targets %s, axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, axioms file %s lines sha256 %s, runner low %s MB, '
                   'minutes %s (build %s)' % (
                       r['n'], r['item'], r.get('restore'), r['sha'][:8], r.get('branch'), r.get('at_ref'), r['run'], r['free_mb'], r['licence']['commit'][:8],
                       r['licence']['line'], rd.get('verdict', 'UNREAD'), rd.get('build_exit'), rd.get('built_equal'), len(rd.get('errors') or []),
                       rd.get('sorry_warnings'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}),
                       rd.get('axiom_missing_n'), rd.get('sorryAx'), rd.get('axioms_file_lines'), str(rd.get('axioms_sha256'))[:16], rd.get('runner_low_mb'),
                       rd.get('run_min'), rd.get('build_min')))
        if rd:
            out.append('      the axioms print: %s ; the cache`s record: input %s, hit %s, restored key %s, files before the build %s, completed %s, key present '
                       'before the save %s, save %s -> restored %s (by the prefix %s), saved %s, from source %s, untouched %s' % (
                           rd.get('axioms_print'), cr.get('input'), cr.get('hit'), (cr.get('matched') or '')[:40], cr.get('files_before'), cr.get('completed'),
                           cr.get('present_before'), cr.get('save'), cr.get('restored'), cr.get('by_prefix'), cr.get('saved'), cr.get('from_source'),
                           cr.get('untouched')))
            if r.get('planted_module'):
                out.append('      the planted module %s, named by the log in %d lines ; the planted input %s, the record taken %s (tip %s)' % (
                    r['planted_module'], len(rd.get('names_module') or []), r.get('planted_input'), (rd.get('planted_rec') or {}).get('taken'),
                    str((rd.get('planted_rec') or {}).get('tip'))[:8]))
    out.append('')
    vl, v = verdict_lines(rows)
    out += vl + ['']
    nd = len(disp)
    out.append('### ### **DISPATCHES %d OF AT MOST %d (WITH THE RESTORE ON %d OF AT MOST %d) ; THE PLANTED %s ; THE PAIR %s ; H-RUNNER-RESTORE %s ; THE SAVE '
               'ON MAIN %s ; THE TOOL`S CONTROLS %d OF %d.**' % (nd, K.MAX_DISPATCHES, sum(1 for r in disp if r.get('item') in ON_ITEMS), ON_CAP, v['planted'],
                                                                v['pair']['state'], v['h'][0], v['mainsave'], sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b765_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'targets': cmd_targets, 'zero': cmd_zero, 'planted': cmd_planted, 'dispatch': cmd_dispatch, 'status': cmd_status,
          'download': cmd_download, 'read': cmd_read, 'errors': cmd_errors, 'axioms': cmd_axioms, 'compare': cmd_compare, 'verdict': cmd_verdict,
          'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
