# -*- coding: utf-8 -*-
"""tools/b766_controls.py -- (R376)(4): THE DISPATCHES OF THE PROOF BY THE BANKED WINDOW AND THEIR READS, carried from tools/b765_controls.py
by tools/standing/carry.py (data/b766_carry_controls.txt) and narrowed by the Write tool before its first run: b765's planted build, its
saves on main and its no-zero control of the statement's file are b765's items and are not carried ((R376)(4): no planted build is ordered
at this act; (8): no planted kind and no kind for a save on main).

THE BRANCH: every run of this act is dispatched AT push-b766-proof (`gh workflow run --ref push-b766-proof`, the commit to build given as the
input ref), the act's Lean branch cut from main at 0ba9cd61 ((R376)(4), (8)), so that the run reads that branch's workflow file (main's bytes)
and the caches of that branch and of main. The commit sent is the branch's remote tip, pushed by tools/push_gated.sh --branch.

THE ITEMS, each with the needle of its clause in the ferry bank (one line), its price row (data/b766_price.json) and its input restore:
  b          (4)(b), the prime side as a finite sum ; restore on
  c          (4)(c), the window in Lean ; restore on
  d-k        (4)(d), the K values ; restore on              d-pole   (4)(d), the pole term ; restore on
  d-arch     (4)(d), the archimedean term ; restore on      d-encl   (4)(d), the enclosures ; restore on
  d-ineq     (4)(d), the inequality ; restore on            d-closing (4)(d), the closing theorem ; restore on
  closing    (4) MAIN AND THE TAG: the closing Lean commit built once from source, restore off, after a build with the restore on at that
             commit read exit 0; after it, the repeat alone
  repeat     (4) THE DISPATCHES AND THE CAP: the one repeat of a build stopped under the hold (exit 143), at the stopped build's commit, its
             input and its branch
THE CAP ((R376)(4), (8), N1): 20 (the worklist's MAX_DISPATCHES): at most 18 with the restore on, the closing one from source and one
repeat; each price row's upper figure besides, the seat's estimate and its guard, a row the author raised read at the raised figure
(ROW_RAISES: (4)(d) K values 6, the author's word of 2026-11-22, data/b766_author_words_preseal.txt :23); one run read before the next is
sent.
THE RESTORE'S KIND ([H5], the author's word of 2026-11-22): exact (a restore line of true, a key restored), prefix (a line of false, a key
restored by the prefix) or none (no key restored), recorded beside each run with the line itself.
THE LEAN NAMES NO FREQUENCY ((R376)(4)(c)): before each dispatch the files under SIDEExplicitFormula/Window/ at the commit are read for a
decimal literal and for a barred word (frequency, ordinate, riemannZeta); counts printed, no line; the window's frequency is read nowhere.
THE VERDICT: the pair (the restore-on build at the closing commit, restored, beside the closing build from source, untouched by the cache:
both exit 0, the axioms files equal by sha256) and by it MAIN AND THE TAG: main moves and v0.45 is cut on AS WANTED; [C7] on DIFFERS.
No lean process runs on this host (N1); each run is read by its run id from its downloaded artifact, the exit file governing. The kernel's
remote is read from its own git config at each call and its account printed masked; no account name is written by this tool.

  control [--bank]                       the tool's own controls, planted and printed (data/b766_controls_control.txt with --bank)
  targets <rev>                          the whole tree's targets at rev (print_targets.txt, each line resolved to its one module by
                                         tools/b757_join.py's reader), written to data/b766_targets_<sha8>.json for --targets-json
  lean <rev>                             the Lean text check over SIDEExplicitFormula/Window/ at rev, counts printed
  dispatch <sha> <n> <item> --targets-json <file>   the holds, the caps, the series and the order, the licence (the ferry's bank), the
                                         commit the remote tip of the branch, the workflow's cache steps at the commit, the Lean text check,
                                         the targets modules of the tree; then gh workflow run at the branch; the row; the run id read back
  status <run> | download <run> | read <n> <run> | errors <run> | axioms <run> | compare <run_a> <run_b>   as b765's
  verdict                                the pair and main and the tag, printed
  bank                                   data/b766_controls.txt through standing.figbank: the controls, the dispatches and reads, the verdict
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
import b766_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import commit as CT              # noqa: E402  (KERNELS: the kernels' keys and folders, the one source)

NL = '\n'
ACT = 'b766'
ROWS = os.path.join(D, 'b766_dispatch_rows.json')
BANK = os.path.join(D, 'b766_controls.txt')
CONTROL_BANK = os.path.join(D, 'b766_controls_control.txt')
ANSWERS = 'data/b766_ferry.txt'
PRICE = os.path.join(D, 'b766_price.json')
RUNS = 'D:/b766-runs'      # ### the artifacts' folder on the data volume, outside every repository; one new empty folder a run
RUNS_ROLE = 'RUNS'         # ### the name a row gives that folder (no host folder written into a bank)
RUNS_B765 = 'D:/b765-runs'  # ### b765's artifacts, read by the positive control of the restore's kind alone
ROWS_B765 = os.path.join(D, 'b765_dispatch_rows.json')
FLOOR = 5000
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')
EF = 'SIDE-explicit-formula'
KPATH = CT.KERNELS[EF]
WORKFLOW = 'build-module.yml'
BRANCH = K.WEIL_BRANCH[0]  # ### push-b766-proof, (R376)(4)
WF = '.github/workflows/build-module.yml'
ON_CAP = 18                # ### (R376)(4), (8): at most eighteen with the restore on, the closing one from source and the repeat beside them
# ### the author's word of 2026-11-22 (data/b766_author_words_preseal.txt :23, the question data/b766_put_1.json): the row (4)(d) K values
# ### raised to 6 dispatches, its priced upper 3 spent by dispatches 3, 4 and 5; the 18 with the restore on (ON_CAP), the 20 (the
# ### worklist's MAX_DISPATCHES) and the 24-hour ceiling stand; the overrun printed beside the row's price in the report; L6 (c) not
# ### compiled within the 6 is carried by name to [P2] and the seat asks before a further raise
ROW_RAISES = {'(4)(d) K values': 6}
STOPPED = 'STOPPED UNDER THE HOLD'
ACT_NS = 'SIDEExplicitFormula.Window.'   # ### the namespace of every declaration this act writes
LEAN_DIR = 'SIDEExplicitFormula/Window/'
DECIMAL = re.compile(r'\d\.\d')
BARRED = re.compile(r'(?i)frequen|ordinate|riemannZeta')
N4B = '(b) THE PRIME SIDE AS A FINITE SUM.'
N4C = '(c) THE WINDOW IN LEAN.'
N4D = '(d) THE LATER STEPS, AS FAR AS THE CEILING ALLOWS'
N4CAP = 'THE DISPATCHES AND THE CAP.'
N4MAIN = 'MAIN AND THE TAG.'
# ### each item: the needle of its clause, its price row, the input restore it sends (None: the stopped build's), its branch (None: the stopped build's)
ITEMS = {'b': (N4B, '(4)(b)', 'on', BRANCH),
         'c': (N4C, '(4)(c) theorems', 'on', BRANCH),
         'd-k': (N4D, '(4)(d) K values', 'on', BRANCH),
         'd-pole': (N4D, '(4)(d) pole term', 'on', BRANCH),
         'd-arch': (N4D, '(4)(d) archimedean', 'on', BRANCH),
         'd-encl': (N4D, '(4)(d) enclosures', 'on', BRANCH),
         'd-ineq': (N4D, '(4)(d) inequality', 'on', BRANCH),
         'd-closing': (N4D, '(4)(d) closing', 'on', BRANCH),
         'closing': (N4MAIN, '(4) closing build', 'off', BRANCH),
         'repeat': (N4CAP, None, None, None)}
ON_ITEMS = ('b', 'c', 'd-k', 'd-pole', 'd-arch', 'd-encl', 'd-ineq', 'd-closing')
AX_DEP = re.compile(r"'([^\n]+?)' depends on axioms: \[([^\]]*)\]")
AX_NONE = re.compile(r"'([^\n]+?)' does not depend on any axioms")
CACHE_KEYS = (('input', 'restore input: '), ('key', 'key: '), ('hit', 'restore hit: '), ('matched', 'restored key: '),
              ('files_before', 'files under .lake/build before the build: '), ('completed', 'build completed under the hold: '),
              ('present_before', 'key present before the save: '), ('save', 'save step: '))


def price_rows():
    return dict((r['key'], r) for r in json.load(io.open(PRICE, encoding='utf-8'))['rows'])


def row_caps(pr=None, raises=None):
    """{price row: its upper dispatch figure} for the rows the items name, read from data/b766_price.json; a row the author raised
    (ROW_RAISES, or `raises` given) at the raised figure. raises={} reads the rows as priced."""
    pr = pr or price_rows()
    raises = ROW_RAISES if raises is None else raises
    return dict((v[1], int(raises.get(v[1], pr[v[1]]['dispatches'][1]))) for v in ITEMS.values() if v[1])


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
    """the workflow file's cache predicates, b765's (R375)(4) eight: the input restore and its step; the key read once from the toolchain and
    the manifest with the commit built; the restore by the prefix; the restored key recorded; the probe and the save at the restore on alone;
    the records. b765's four of the planted input are not read: no planted build is ordered at this act."""
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
        records='out/cache_kernel.txt' in t and 'out/build_times.txt' in t)


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


# ================================================================================ the refusals
def dispatch_refusal(item, n, sha, rows, read, dk, caps=None, ctx=None):
    """why a dispatch is refused before anything is sent, or None. Pure: the rows, the free read, the disk read, the row caps and `ctx` (lean:
    the Lean text check's refusals, a list, None where not read) given."""
    caps = caps if caps is not None else row_caps()
    ctx = ctx or {}
    if item not in ITEMS:
        return 'an item (R376)(4) does not order: %r (%s)' % (item, ' | '.join(sorted(ITEMS)))
    if read[0] < DR.HOLD:
        return 'free %d MB under the hold %d' % (read[0], DR.HOLD)
    low = sorted(v for v, mb in dk.items() if mb < FLOOR)
    if low:
        return 'the volume %s under the floor %d MB' % (', '.join(low), FLOOR)
    if not 1 <= n <= K.MAX_DISPATCHES:
        return 'dispatch %d past the act`s %d ((R376)(4), N1)' % (n, K.MAX_DISPATCHES)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    if any(r.get('n') == n for r in mine):
        return 'dispatch %d rowed already' % n
    if n != 1 + len(mine):
        return 'dispatch %d is not the next in the series (%d rowed)' % (n, len(mine))
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    last = mine[-1] if mine else None
    if last and int(last['run']) not in reads:
        return 'dispatch %d (run %s) not yet read: one run read before the next is sent' % (last['n'], last['run'])
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
        return None
    if any(r.get('item') == 'closing' for r in mine):
        return 'the closing build sent: after it, the repeat of a stopped build alone'
    row_ = ITEMS[item][1]
    of_row = [r for r in mine if r.get('item') != 'repeat' and ITEMS.get(r.get('item'), (None, None))[1] == row_]
    if len(of_row) + 1 > caps.get(row_, 0):
        return 'the price row %s`s dispatch %d past its upper figure %d ((R376) N1)' % (row_, len(of_row) + 1, caps.get(row_, 0))
    if item in ON_ITEMS:
        on = [r for r in mine if r.get('item') in ON_ITEMS]   # ### the repeat stands beside the eighteen ((R376)(4))
        if len(on) + 1 > ON_CAP:
            return 'the dispatch with the restore on %d past the eighteen of (R376)(4)' % (len(on) + 1)
    if ctx.get('lean') is None:
        return 'the Lean text check not read at %s' % str(sha)[:8]
    if ctx.get('lean'):
        return 'the Lean text check refuses %d file(s) at %s: %s' % (len(ctx['lean']), str(sha)[:8], '; '.join('%s %s' % x for x in ctx['lean'][:4]))
    if item == 'closing':
        ok_on = [r for r in reads.values() if r.get('restore_input') == 'on' and r.get('built_ref') == sha and r.get('build_exit') == '0']
        if not ok_on:
            return 'the closing build from source sent before a build with the restore on at %s read exit 0' % str(sha)[:8]
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


# ================================================================================ the verdict
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
            str(on.get('axioms_sha256'))[:16], on.get('run'), str(off.get('axioms_sha256'))[:16], off.get('run')),
            shas=(on.get('axioms_sha256'), off.get('axioms_sha256')), commit=on.get('built_ref'))
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
        return dict(state='NOT SCORABLE', where='the restore-on build at the closing commit restored no key ([H5]: its kind %s, restored key %s, '
                    'files before the build %s), so no restored build stands beside the build from source' % (
                        restore_kind(on.get('cache')), (on.get('cache') or {}).get('matched'), (on.get('cache') or {}).get('files_before')))
    return dict(state='AS WANTED', where='', sha=on.get('axioms_sha256'), commit=on.get('built_ref'), runs=(on.get('run'), off.get('run')),
                hit=(on.get('cache') or {}).get('hit'), kind=restore_kind(on.get('cache')))


def main_decision(pr):
    """(4) MAIN AND THE TAG by the pair."""
    if pr['state'] == 'AS WANTED':
        return 'MAIN MOVES TO %s BY THE GATED PUSH, v0.45 CUT THERE AFTER MAIN`S READ-BACK' % str(pr.get('commit'))[:8]
    if pr['state'] == 'DIFFERS':
        return '[C7]: MAIN NOT MOVED, NO TAG CUT, THE LEAN ON ITS BRANCH'
    if pr['state'] == 'PENDING':
        return 'PENDING'
    return 'MAIN NOT MOVED, NO TAG CUT (THE PAIR %s)' % pr['state']


def verdicts(rows):
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    cl = [r for r in disp if r.get('item') == 'closing']
    if not cl:
        pr, stopped_both = pair_verdict(None, None), False
    else:
        offs = [reads.get(int(cl[0]['run']))] + [reads.get(int(r['run'])) for r in disp if r.get('item') == 'repeat' and r.get('n', 0) > cl[0]['n']]
        offs = [x for x in offs if x]
        stopped_both = len(offs) == 2 and all(x.get('verdict') == STOPPED for x in offs)
        ons = [reads[int(r['run'])] for r in disp if r.get('n', 0) < cl[0]['n'] and int(r['run']) in reads
               and reads[int(r['run'])].get('restore_input') == 'on' and reads[int(r['run'])].get('built_ref') == cl[0]['sha']
               and reads[int(r['run'])].get('build_exit') == '0']
        pr = pair_verdict(ons[-1] if ons else None, offs[-1] if offs else None)
    kernel_reads = [reads[int(r['run'])] for r in disp if int(r['run']) in reads and reads[int(r['run'])].get('build_exit') == '0']
    return dict(pair=pr, stopped_both=stopped_both, main=main_decision(pr), last_kernel=kernel_reads[-1] if kernel_reads else None)


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
    ctx = dict(lean=bad)
    why = dispatch_refusal(item, int(n), full, rows, read, dk, ctx=ctx)
    if why:
        sys.exit('### NOT DISPATCHED: %s' % why)
    mine = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    mode, branch = ITEMS[item][2], ITEMS[item][3]
    if item == 'repeat':
        mode, branch = mine[-1].get('restore'), mine[-1].get('branch')
    target = ' '.join(tj['modules'])
    print('  the targets from %s: %d modules, read at %s' % (rest[1], len(tj['modules']), tj['rev'][:8]))
    wp = wf_predicates(git(KPATH, 'show', '%s:%s' % (full, WF)))
    if not wp or not all(wp.values()):
        sys.exit('### NOT DISPATCHED: the workflow at the commit %s lacks (4)`s cache steps: %s' % (full[:8], sorted(x for x, v in wp.items() if not v)))
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
    print('  dispatch %s, %s (restore %s) at %s on %s ; the licence %s %s :%d, committed %s ; free %d MB at %s, the hold %d ; volumes %s, the floor %d' % (
        n, item, mode, full[:8], branch, lic['bank'], lic['commit'][:8], lic['line'], lic['committed_at'], read[0], read[1], DR.HOLD, dk, FLOOR))
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
                           lean_files=len(fs), lean_refused=len(bad)))
    DR.write(ROWS, rows)
    print(dict((x, rows[-1].get(x)) for x in ('kind', 'item', 'n', 'restore', 'branch', 'sha', 'run', 'free_mb', 'at')))


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
                       names=[list(x) for x in ns], artifact='%s/ef-%s/build-module-%s' % (RUNS_ROLE, run, run)))
    DR.write(ROWS, rows)
    r = rows[-1]
    print(dict((x, r[x]) for x in ('n', 'run', 'item', 'restore_input', 'conclusion', 'workflow_at_ref', 'built_ref', 'built_equal', 'build_exit',
                                   'verdict', 'sorry_warnings', 'targets', 'axiom_lines', 'axiom_within', 'axiom_missing_n', 'sorryAx', 'axioms_file_lines',
                                   'build_min', 'run_min', 'runner_low_mb', 'free_mb')), 'errors', len(errs))
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
    out = os.path.join(D, 'b766_targets_%s.json' % full[:8])
    s = json.dumps(dict(rev=full, names=n, modules=mods, refused=bad, at=_now(),
                        reader='tools/b757_join.py targets_at, through tools/b758_presend.py, both unchanged'), indent=1) + NL
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    print('written data/%s: %d modules for %d names at %s' % (os.path.basename(out), len(mods), n, full[:8]))


def verdict_lines(rows=None):
    rows = rows if rows is not None else _rows()
    v = verdicts(rows)
    pr = v['pair']
    L = ['## THE VERDICT OF (R376)(4): THE PAIR, MAIN AND THE TAG',
         '  THE PAIR: %s%s' % (pr['state'], (' ; ' + pr['where']) if pr.get('where') else (
             ' ; at %s, sha256 %s, runs %s, the restore-on build`s restore line %s (kind %s)' % (
                 str(pr.get('commit'))[:8], str(pr.get('sha'))[:16], pr.get('runs'), pr.get('hit'), pr.get('kind')) if pr['state'] == 'AS WANTED' else '')),
         '  MAIN AND THE TAG: %s' % v['main']]
    lk = v['last_kernel']
    if lk:
        L.append('  THIS ACT`S NAMES AT THE LAST READ EXITING 0 (run %s at %s):' % (lk.get('run'), str(lk.get('built_ref'))[:8]))
        for nm, st, why in lk.get('names') or []:
            L.append('    %s %s %s' % (nm, st, why))
    else:
        L.append('  THIS ACT`S NAMES: no read exiting 0')
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
    caps, priced = row_caps(), row_caps(raises={})
    want_priced = {'(4)(b)': 2, '(4)(c) theorems': 3, '(4)(d) K values': 3, '(4)(d) pole term': 1, '(4)(d) archimedean': 2, '(4)(d) enclosures': 2,
                   '(4)(d) inequality': 2, '(4)(d) closing': 1, '(4) closing build': 2}
    want_caps = dict(want_priced, **{'(4)(d) K values': 6})
    c('each price row`s upper dispatch figure as priced (data/b766_price.json)', priced, priced == want_priced)
    c('each row`s cap with the author`s raise of 2026-11-22 (ROW_RAISES): (4)(d) K values 6, every other row at its priced figure', caps,
      caps == want_caps and ROW_RAISES == {'(4)(d) K values': 6})
    on_sum, on_priced = sum(caps[ITEMS[i][1]] for i in ON_ITEMS), sum(priced[ITEMS[i][1]] for i in ON_ITEMS)
    c('the kernel`s cap (the worklist`s MAX_DISPATCHES) against the rows` upper figures, the restore-on rows` sum against the eighteen of (4): '
      'the price rows as priced 18 and 16, held by the 20 and the eighteen; with the raise 21 and 19, the 20 and the eighteen standing and '
      'refusing in the tool', (K.MAX_DISPATCHES, sum(priced.values()), on_priced, sum(caps.values()), on_sum, ON_CAP),
      K.MAX_DISPATCHES == 20 and sum(priced.values()) == 18 and on_priced == 16 and sum(caps.values()) == 21 and on_sum == 19 and ON_CAP == 18)
    good, dk = (5000, _now()), {'C:/': 20000, 'D:/': 20000}
    A, B = 'a' * 40, 'b' * 40
    lean_ok = dict(lean=[])

    def D_(n, item, run, restore='on', sha=A):
        return dict(kind='dispatch', kernel=EF, n=n, item=item, run=run, restore=restore, sha=sha)

    def R_(run, item, restore='on', ex='0', verdict='KERNEL', sha=A):
        return dict(kind='read', kernel=EF, run=run, item=item, restore_input=restore, build_exit=ex, verdict=verdict, built_ref=sha)
    b1 = [D_(1, 'b', 11), R_(11, 'b')]
    eighteen = []
    for i in range(18):
        eighteen += [D_(i + 1, 'd-k', 100 + i), R_(100 + i, 'd-k')]
    # ### the act's own series to dispatch 5 ((4)(b), (4)(c), then three of (4)(d) K values), and one with six of K values
    series5 = b1 + [D_(2, 'c', 12), R_(12, 'c')] + [x for i in range(3) for x in (D_(3 + i, 'd-k', 13 + i), R_(13 + i, 'd-k'))]
    series8 = b1 + [D_(2, 'c', 12), R_(12, 'c')] + [x for i in range(6) for x in (D_(3 + i, 'd-k', 13 + i), R_(13 + i, 'd-k'))]
    plants = [('form', 1, A, [], good, dk, None, lean_ok),
              ('b', 1, A, [], (2000, _now()), dk, None, lean_ok),
              ('b', 1, A, [], good, {'C:/': 4000, 'D:/': 20000}, None, lean_ok),
              ('b', 21, A, [], good, dk, None, lean_ok),
              ('b', 2, A, [], good, dk, None, lean_ok),
              ('b', 1, A, [D_(1, 'b', 11)], good, dk, None, lean_ok),
              ('c', 2, A, [D_(1, 'b', 11)], good, dk, None, lean_ok),
              ('closing', 2, A, [D_(1, 'b', 11), R_(11, 'b', ex='1', verdict='BREAKS')], good, dk, None, lean_ok),
              ('closing', 2, A, [D_(1, 'b', 11, sha=B), R_(11, 'b', sha=B)], good, dk, None, lean_ok),
              ('b', 3, A, b1 + [D_(2, 'b', 12), R_(12, 'b')], good, dk, None, lean_ok),
              ('d-k', 19, A, eighteen, good, dk, dict(want_caps, **{'(4)(d) K values': 19}), lean_ok),
              ('repeat', 2, A, b1, good, dk, None, lean_ok),
              ('repeat', 3, A, [D_(1, 'b', 11), R_(11, 'b', verdict=STOPPED, ex='143'), D_(2, 'repeat', 12), R_(12, 'repeat', verdict=STOPPED, ex='143')],
               good, dk, None, lean_ok),
              ('b', 3, A, b1 + [D_(2, 'closing', 12, restore='off'), R_(12, 'closing', restore='off')], good, dk, None, lean_ok),
              ('repeat', 2, A, [D_(1, 'closing', 11, restore='off', sha=B), R_(11, 'closing', restore='off', verdict=STOPPED, ex='143', sha=B)],
               good, dk, None, lean_ok),
              ('d-closing', 2, A, [D_(1, 'd-closing', 11), R_(11, 'd-closing')], good, dk, None, lean_ok),
              ('b', 1, A, [], good, dk, None, dict(lean=[('SIDEExplicitFormula/Window/X.lean', 'a decimal literal (1)')])),
              ('b', 1, A, [], good, dk, None, {}),
              ('d-k', 9, A, series8, good, dk, None, lean_ok),
              ('d-k', 6, A, series5, good, dk, want_priced, lean_ok)]
    got = [dispatch_refusal(p[0], p[1], p[2], p[3], p[4], p[5], caps=p[6] or want_caps, ctx=p[7]) for p in plants]
    c('twenty planted dispatches refused (an item (R376)(4) does not order, under the hold, under the floor, past 20, out of series, rowed '
      'already, the last run unread, the closing before a restore-on build exiting 0, the closing at another commit than that build, (4)(b)`s '
      'third, the nineteenth with the restore on, a repeat of a build not stopped, a second repeat, an item after the closing, a repeat at '
      'another commit, (4)(d)`s closing twice, a Lean file with a decimal literal, the Lean text not read, (4)(d) K values` seventh at the '
      'raised 6, its fourth at the priced 3)', [bool(x) for x in got], all(got))
    passes = [dispatch_refusal('b', 1, A, [], good, dk, caps=want_caps, ctx=lean_ok),
              dispatch_refusal('c', 2, A, b1, good, dk, caps=want_caps, ctx=lean_ok),
              dispatch_refusal('closing', 2, A, b1, good, dk, caps=want_caps, ctx=lean_ok),
              dispatch_refusal('repeat', 3, A, b1 + [D_(2, 'closing', 12, restore='off'), R_(12, 'closing', restore='off', verdict=STOPPED, ex='143')],
                               good, dk, caps=want_caps, ctx={}),
              dispatch_refusal('repeat', 2, A, [D_(1, 'c', 11), R_(11, 'c', verdict=STOPPED, ex='143')], good, dk, caps=want_caps, ctx={}),
              dispatch_refusal('d-k', 6, A, series5, good, dk, caps=want_caps, ctx=lean_ok),
              dispatch_refusal('d-k', 6, A, series5, good, dk, ctx=lean_ok)]
    c('seven planted dispatches taken ((4)(b) first ; (4)(c) after it ; the closing after the restore-on build at its commit ; the repeat of a '
      'stopped closing build ; the repeat of a stopped step build ; the act`s dispatch 6, (4)(d) K values` fourth, at the raised 6, by the '
      'planted caps and by the tool`s own read of the price bank)', passes, passes == [None] * 7)
    lic = {}
    for nd, want_line in ((N4B, 19), (N4C, 20), (N4D, 21), (N4CAP, 22), (N4MAIN, 23)):
        try:
            x = DR.licence(ANSWERS, nd)
            lic[nd[:16]] = (x['commit'][:8], x['line'], x['line'] == want_line)
        except DR.Refused as e:
            lic[nd[:16]] = str(e)[:60]
    c('the licences at the committed ferry bank: (4)(b) at :19, (4)(c) at :20, (4)(d) at :21, the cap at :22, main and the tag at :23', lic,
      all(isinstance(v, tuple) and v[2] for v in lic.values()))
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
    t2 = DR.targets_refused('SIDEExplicitFormula.Window.PrimeFinite', module_files(KPATH, K.EF_BASE))
    t3 = DR.targets_refused('Lc.LiCriterion.ReverseDirection', module_files(KPATH, K.EF_BASE))
    c('targets at main 0ba9cd61: the statement`s module taken ; a module of this act refused there (no file yet) ; a vendored module under '
      'its srcDir taken', (t1, len(t2), t3), t1 == [] and len(t2) == 1 and t3 == [])
    pl = [axioms_print("out/Axioms.lean:1:0: error: import X failed", axioms_read("out/Axioms.lean:1:0: error: x", ['a'])),
          axioms_print("NOT RUN: the build did not complete under the hold", axioms_read('', ['a'])),
          axioms_print("'a' depends on axioms: [propext]", axioms_read("'a' depends on axioms: [propext]", ['a']))]
    c('the axioms print`s state on three planted files (an import failure, the NOT RUN line, a clean print)', [x[:24] for x in pl],
      pl[0].startswith('FAILED, NO AXIOMS LINE') and pl[1].startswith('NOT RUN') and pl[2] == 'RAN')
    heads = [(A, 'refs/heads/' + BRANCH), ('c' * 40, 'refs/heads/main'), ('e' * 40, 'refs/heads/push-b765-centre')]
    tp = (tip_refusal(A, heads, BRANCH), bool(tip_refusal('c' * 40, heads, BRANCH)), bool(tip_refusal('e' * 40, heads, BRANCH)),
          bool(tip_refusal('', heads, BRANCH)), branch_tip(heads) == A, bool(tip_refusal(B, heads, BRANCH)))
    c('the remote tip: the branch`s tip taken ; main`s, push-b765-centre`s, no commit and a commit at no head refused ; the branch`s tip read',
      tp, tp == (None, True, True, True, True, True))
    tf, tm, tb, tn = targets_of(K.EF_BASE_B763)
    bj = json.load(io.open(os.path.join(D, 'b759_targets.json'), encoding='utf-8'))
    c('THE POSITIVE CONTROL: the targets reader at a3aad4cc against b759`s targets bank (data/b759_targets.json: %d modules for %d names)' % (
        len(bj['modules']), bj['names']), (tf[:8], len(tm), tn, len(tb)), tf == bj['rev'] and tm == sorted(bj['modules']) and tn == bj['names'] and not tb)
    wn = wf_predicates(git(KPATH, 'show', '%s:%s' % (K.EF_BASE, WF)))
    wo = wf_predicates(git(KPATH, 'show', '%s:%s' % (K.RUNNER_COMMIT_B764, WF)))
    c('the workflow`s cache predicates: each true at main 0ba9cd61, the bytes push-b766-proof carries ; THE PLANTED FAULT, b764`s workflow at '
      '38a57e02: its three true and the others false', (sum(wn.values()), len(wn), sorted(k for k, v in wo.items() if v)),
      all(wn.values()) and len(wn) == 8 and sorted(k for k, v in wo.items() if v) == sorted(B764_PREDICATES))
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
    rv = [(r['read'], r['restored'], r['by_prefix'], r['saved'], r['from_source'], r['untouched'], restore_kind(r)) for r in recs]
    c('the cache`s record and the restore`s kind on five planted files (the first save, built from source ; a restore by the prefix, then saved ; '
      'an exact restore ; the restore off ; a record cut short): (read, restored, by prefix, saved, from source, untouched, kind)', rv,
      rv == [(True, False, False, True, True, False, 'none'), (True, True, True, True, False, False, 'prefix'),
             (True, True, False, False, False, False, 'exact'), (True, False, False, False, True, True, 'none'),
             (False, False, False, False, False, False, 'unread')])
    # ### THE POSITIVE CONTROL of the restore's kind on b765's real records: each read row's cache record against its artifact's file
    rk, same, seen = {}, 0, 0
    for r in (json.load(io.open(ROWS_B765, encoding='utf-8')) if os.path.exists(ROWS_B765) else []):
        if r.get('kind') != 'read':
            continue
        fp = os.path.join(_art(r['run'], RUNS_B765), 'cache_kernel.txt')
        if not os.path.exists(fp):
            continue
        seen += 1
        k_file = restore_kind(cache_record(_f(_art(r['run'], RUNS_B765), 'cache_kernel.txt')))
        same += k_file == restore_kind(r.get('cache'))
        rk[k_file] = rk.get(k_file, 0) + 1
    c('THE POSITIVE CONTROL: the restore`s kind on b765`s real records (each read row of data/b765_dispatch_rows.json against its artifact`s '
      'cache_kernel.txt): read, equal, by kind', (seen, same, sorted(rk.items())),
      seen > 0 and same == seen and rk.get('exact', 0) >= 1 and rk.get('prefix', 0) >= 1 and rk.get('none', 0) >= 1)
    base = dict(build_exit='0', axioms_print='RAN', built_ref=A, built_equal=True, axioms_sha256='f' * 64, verdict='KERNEL')
    on = dict(base, run=21, restore_input='on', cache=recs[1])
    off = dict(base, run=22, restore_input='off', cache=recs[3])
    pv = [pair_verdict(on, off)['state'], pair_verdict(on, dict(off, axioms_sha256='0' * 64))['state'],
          pair_verdict(dict(on, cache=recs[0]), off)['state'], pair_verdict(on, dict(off, build_exit='1', verdict='BREAKS'))['state'],
          pair_verdict(on, None)['state'], pair_verdict(on, dict(off, verdict=STOPPED, build_exit='143'))['state'],
          pair_verdict(None, off)['state'], pair_verdict(dict(on, cache=recs[2]), off)['state']]
    c('the pair on eight planted readings (as wanted, restored by the prefix ; the files differing ; the restore-on build restoring no key ; the '
      'closing exiting 1 ; no closing read ; the closing stopped ; no restore-on build ; as wanted, an exact key)', pv,
      pv == ['AS WANTED', 'DIFFERS', 'NOT SCORABLE', 'NOT AS WANTED', 'PENDING', 'STOPPED', 'NOT AS WANTED', 'AS WANTED'])
    md = [main_decision(dict(state='AS WANTED', commit=A))[:10], main_decision(dict(state='DIFFERS'))[:4], main_decision(dict(state='PENDING')),
          main_decision(dict(state='NOT SCORABLE'))[:14]]
    c('main and the tag on four planted pairs (as wanted ; differing, [C7] ; pending ; not scorable)', md,
      md == ['MAIN MOVES', '[C7]', 'PENDING', 'MAIN NOT MOVED'])
    series = [D_(1, 'b', 11), dict(R_(11, 'b'), cache=recs[1], axioms_print='RAN', built_equal=True, axioms_sha256='f' * 64),
              D_(2, 'closing', 12, restore='off'), dict(off, kind='read', kernel=EF, run=12, item='closing')]
    vr = verdicts(series)
    c('the verdict over a planted series ((4)(b) restored by the prefix, the closing from source at its commit)', (vr['pair']['state'], vr['main'][:10]),
      (vr['pair']['state'], vr['main'][:10]) == ('AS WANTED', 'MAIN MOVES'))
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
    rows = _rows()
    c('the rows bank', 'absent' if not os.path.exists(ROWS) else '%d rows, refused by standing.dispatchrows %s' % (len(rows), DR.check(rows) or 'NONE'),
      not os.path.exists(ROWS) or not DR.check(rows))
    fr = DR.free()
    c('the free read and the disk read now', '%d MB at %s ; %s' % (fr[0], fr[1], disk()), fr[0] >= DR.HOLD and min(disk().values()) >= FLOOR)
    return L, ok


def cmd_control(*a):
    L, ok = controls()
    out = ['%s -- tools/b766_controls.py`s OWN CONTROLS, (R376)(4) (%s)' % (ACT, _now()), '', '## THE CONTROLS'] + L + [
        '', '### ### **THE TOOL`S CONTROLS: %d OF %d AS WANTED ; %s.**' % (sum(ok), len(ok), 'ALL AS WANTED' if all(ok) else 'NOT ALL AS WANTED')]
    print(NL.join(out))
    if '--bank' in a:
        r = FB.write(CONTROL_BANK, NL.join(out))
        print('written data/%s (figbank: %s)' % (os.path.basename(CONTROL_BANK), r['why']))


def cmd_bank(*_a):
    L, ok = controls()
    rows = _rows()
    out = ['%s -- (R376)(4): THE DISPATCHES OF THE PROOF BY THE BANKED WINDOW AND THEIR READS, EACH READ BY ITS RUN ID (%s)' % (ACT, _now()), '',
           '## THE CONTROLS'] + L + ['  the tool`s controls %d of %d as wanted' % (sum(ok), len(ok)), '']
    disp = [r for r in rows if r.get('kind') == 'dispatch' and r.get('kernel') == EF]
    reads = dict((int(r['run']), r) for r in rows if r.get('kind') == 'read' and r.get('kernel') == EF)
    refused = [r for r in rows if r.get('kind') == 'dispatch_refused' and r.get('kernel') == EF]
    out.append('## %s: %d DISPATCHES OF AT MOST %d ; SENDS REFUSED BY THE HOST %d' % (EF, len(disp), K.MAX_DISPATCHES, len(refused)))
    for r in disp:
        rd = reads.get(int(r['run']), {})
        cr = rd.get('cache') or {}
        out.append('  %d | %-9s | restore %s | sha %s on %s | run %s | free %d MB | licence %s :%s | %s, exit %s, built %s, %d errors, sorry warnings %s, '
                   'targets %s, axiom lines %s, within %s, outside %s, missing %s, sorryAx %s, axioms file %s lines sha256 %s, runner low %s MB, minutes %s '
                   '(build %s)' % (
                       r['n'], r['item'], r.get('restore'), r['sha'][:8], r.get('branch'), r['run'], r['free_mb'], r['licence']['commit'][:8],
                       r['licence']['line'], rd.get('verdict', 'UNREAD'), rd.get('build_exit'), rd.get('built_equal'), len(rd.get('errors') or []),
                       rd.get('sorry_warnings'), rd.get('targets'), rd.get('axiom_lines'), rd.get('axiom_within'), len(rd.get('axiom_outside') or {}),
                       rd.get('axiom_missing_n'), rd.get('sorryAx'), rd.get('axioms_file_lines'), str(rd.get('axioms_sha256'))[:16], rd.get('runner_low_mb'),
                       rd.get('run_min'), rd.get('build_min')))
        if rd:
            out.append('      the axioms print: %s ; the cache`s record: input %s, the restore line %s, files before the build %s, completed %s, key present '
                       'before the save %s, save %s -> THE RESTORE`S KIND %s (restored %s, by the prefix %s), saved %s, from source %s, untouched %s' % (
                           rd.get('axioms_print'), cr.get('input'), cr.get('hit'), cr.get('files_before'), cr.get('completed'), cr.get('present_before'),
                           cr.get('save'), rd.get('restore_kind'), cr.get('restored'), cr.get('by_prefix'), cr.get('saved'), cr.get('from_source'),
                           cr.get('untouched')))
            for nm, st, why in rd.get('names') or []:
                out.append('      %s %s %s' % (nm, st, why))
    out.append('')
    vl, v = verdict_lines(rows)
    out += vl + ['']
    nd = len(disp)
    out.append('### ### **DISPATCHES %d OF AT MOST %d (WITH THE RESTORE ON %d OF AT MOST %d) ; THE PAIR %s ; MAIN AND THE TAG: %s ; THE TOOL`S CONTROLS '
               '%d OF %d.**' % (nd, K.MAX_DISPATCHES, sum(1 for r in disp if r.get('item') in ON_ITEMS), ON_CAP, v['pair']['state'], v['main'],
                                sum(ok), len(ok)))
    r = FB.write(BANK, NL.join(out))
    print(NL.join(out))
    print('written data/b766_controls.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'control': cmd_control, 'targets': cmd_targets, 'lean': cmd_lean, 'dispatch': cmd_dispatch, 'status': cmd_status,
          'download': cmd_download, 'read': cmd_read, 'errors': cmd_errors, 'axioms': cmd_axioms, 'compare': cmd_compare, 'verdict': cmd_verdict,
          'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
