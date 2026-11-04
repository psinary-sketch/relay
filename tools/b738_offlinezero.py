# -*- coding: utf-8 -*-
"""tools/b738_offlinezero.py -- (R348)(3): W-ORD-ZQ-OFFLINE-ZERO BUILT ON R4, BOX A, TO SP1. Carried from tools/b735_ef.py's routes. No lean process
runs on this host; every build is the runner's (SIDE-explicit-formula build-module.yml, dispatched at main, the ref zq-b730's commit).

  planmd5               the plan bank's md5 against its blob at 3dab6492, printed before any Lean file (step zero printed it first)
  clone                 a fresh clone of zq-b730 at CLONE, a clone row with its snapshots before and after ((R347)(2)(iv)'s rule)
  commit <sha> <group>  a commit row, the clone's snapshots beside it
  push <sha>            a push row, the free read taken now, the remote's tip read back
  dispatch <sha> <n> <group> <target>   gh workflow run, the row carrying the free read before it; the run id read back into the row
  read <n> <run> <artifact dir>   a read row, verdict from the artifact's files
  errors <artifact dir> error blocks from the run's build.log
  lines                 the measured lines of each group's module against the plan's estimate, printed
  bank <artifact dir>   data/b738_offlinezero.txt through standing.figbank: controls first, the dispatches, the lines, the axioms, the grade at the end
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b738_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import figbank as FB             # noqa: E402
import scratchfsck as SF         # noqa: E402

NL = '\n'
REPO = 'psinary-sketch/SIDE-explicit-formula'
URL = 'https://github.com/%s.git' % REPO
CLONE = 'D:/zq-b738'      # ### outside the Temp tree, where b735-b737's three pack losses fell (b737 defect (h)); the cause not established
ROWS = os.path.join(D, 'b738_dispatch_rows.json')
PLAN = 'data/b737_offlinezero_plan.txt'
PLAN_MD5 = '3d61f519917a3ee20ac4d7c5fab197ef'
PLAN_AT = '3dab6492'
BANK = os.path.join(D, 'b738_offlinezero.txt')
NOTES = 'data/b738_offlinezero_notes.txt'
ZQ = 'SIDEExplicitFormula/Schema/ZQ/OffZero/'
# ### the groups in the ruling's order, each its own module and its own dispatch; the plan's estimate (data/b737_offlinezero_plan.txt :78-:99)
GROUPS = (('S1', 'Box', (40, 80), ('boxA', 'boxA_isBounded', 'closure_boxA', 'mem_closure_boxA')),
          ('S2', 'Diff', (20, 40), ('ne_one_of_mem_closure_boxA', 'zqFn_diffContOnCl_boxA')),
          ('S3', 'MinModulus', (40, 80), ('min_modulus_zero',)),
          ('S4', 'Carrier', (30, 60), ('carrier_of_box',)),
          ('e', 'Main', (5, 15), ('zq_offline_of_box', 'zq_li_not_nonneg_of_box')))
NS = 'SIDEExplicitFormula.Schema.ZQ.OffZero.'
SP1 = NS + 'zq_offline_of_box'
SP1_LINES = (135, 275)
# ### (R348)(3)(b): S5a-S5b past SP1, each its own module and dispatch; the plan's estimates :87, :89, SP2 at :135
GROUPS2 = (('S5a', 'Split', (150, 300), ('f_modif_eq', 'lamM_eq', 'thA_conv', 'thB_eq', 'thB_conv', 'zq_lambda0_split')),
           ('S5b', 'Tail', (150, 300), ('tail_qR', 'thetaU_anti', 'thetaU_half', 'thetaU_half_le', 'tail_le', 'zq_theta_tail', 'zq_thetaC_tail')))
SP2 = (NS + 'zq_lambda0_split', NS + 'zq_thetaC_tail')   # ### zq_Λ₀_split's ASCII name: the print step refuses a non-ASCII target
SP2_LINES = (300, 600)
S5CD = (900, 2500)       # ### S5c-S5d's estimate, data/b737_offlinezero_plan.txt :91, :93, :136
STANDARD = ('propext', 'Classical.choice', 'Quot.sound')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def _now():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def cmd_planmd5():
    b = open(os.path.join(RELAY, PLAN), 'rb').read()
    h = hashlib.md5(b).hexdigest()
    blob = subprocess.run(['git', '-C', RELAY, 'show', '%s:%s' % (PLAN_AT, PLAN)], capture_output=True).stdout
    print('the plan bank %s md5 %s ; wanted %s ; equal %s ; equal its blob at %s %s ; %d lines' % (PLAN, h, PLAN_MD5, h == PLAN_MD5, PLAN_AT, hashlib.md5(blob).hexdigest() == h, b.count(b'\n')))
    if h != PLAN_MD5:
        sys.exit('### THE PLAN BANK MOVED')


def cmd_clone():
    if os.path.exists(CLONE):
        sys.exit('### %s STANDS -- NOT CLONED' % CLONE)
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT CLONED' % read[0])
    before = SF.snapshot(os.path.dirname(CLONE) or 'D:/')
    r = subprocess.run(['git', 'clone', '--branch', K.ZQ_BRANCH, '--single-branch', URL, CLONE], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    after = SF.snapshot(CLONE)
    tip = git(CLONE, 'rev-parse', 'HEAD').strip()
    rows = _rows()
    rows.append(DR.row('clone', read, kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, clone=CLONE, exit=r.returncode, tip=tip, tip_entering=tip == K.ZQ_ENTERING,
                       snap_before=before, snap_after=after, at=read[1]))
    DR.write(ROWS, rows)
    print('  before: ' + SF.line(before))
    print('  after:  ' + SF.line(after))
    print('  tip %s ; the entering b25fd82c: %s' % (tip[:8], tip == K.ZQ_ENTERING))


def cmd_commit(sha, item):
    rows = _rows()
    full = git(CLONE, 'rev-parse', sha).strip()
    snap = SF.snapshot(CLONE)
    rows.append(DR.row('commit', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, item=item, sha=full, parent=git(CLONE, 'rev-parse', full + '^').strip(),
                       files=[x for x in git(CLONE, 'show', '--format=', '--name-only', full).split(NL) if x], snap=snap))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('item', 'sha', 'parent', 'files', 'free_mb')}, SF.line(snap))


def cmd_push(sha):
    rows = _rows()
    rem = subprocess.run(['git', '-C', CLONE, 'ls-remote', 'origin', 'refs/heads/' + K.ZQ_BRANCH], capture_output=True, text=True).stdout.split()
    full = git(CLONE, 'rev-parse', sha).strip()
    rows.append(DR.row('push', DR.free(), kernel='SIDE-explicit-formula', branch=K.ZQ_BRANCH, sha=full, remote=rem[0] if rem else None, remote_equal=bool(rem) and rem[0] == full, at=_now()))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_dispatch(sha, n, item, target):
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT DISPATCHED' % read[0])
    if int(n) > K.MAX_DISPATCHES:
        sys.exit('### DISPATCH %s PAST THE ACT`S %d -- NOT DISPATCHED' % (n, K.MAX_DISPATCHES))
    if any(r['kind'] == 'dispatch' and r['n'] == int(n) for r in _rows()):
        sys.exit('### DISPATCH %s ROWED ALREADY -- NOT DISPATCHED' % n)
    r = subprocess.run(['gh', 'workflow', 'run', 'build-module.yml', '--repo', REPO, '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + target], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel='SIDE-explicit-formula', item=item, n=int(n), sha=sha, target=target, at=read[1], error=(r.stderr or '')[:300]))
    else:
        rid = m.group(1) if m else ''
        if not rid:
            time.sleep(8)
            rid = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', REPO, '--workflow', 'build-module.yml', '--limit', '1', '--json', 'databaseId'], capture_output=True, text=True).stdout)[0]['databaseId']
        rows.append(DR.row('dispatch', read, kernel='SIDE-explicit-formula', item=item, n=int(n), workflow='build-module.yml', at_ref='main', sha=sha, target=target, run=int(rid), at=read[1]))
    DR.write(ROWS, rows)
    print(rows[-1])


def _art(art, name):
    p = os.path.join(art, name)
    return io.open(p, encoding='utf-8', errors='replace').read() if os.path.exists(p) else ''


def cmd_read(n, run, art):
    v = json.loads(subprocess.run(['gh', 'run', 'view', str(run), '--repo', REPO, '--json', 'status,conclusion,updatedAt'], capture_output=True, text=True, encoding='utf-8').stdout)
    ex = _art(art, 'build_exit.txt').strip()
    log = _art(art, 'build.log')
    ref = _art(art, 'ref.txt').strip().split()
    errs = [l for l in log.split(NL) if l.startswith('error: ') or (': error:' in l and 'OffZero' in l)]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    ax = [l for l in _art(art, 'axioms.txt').split(NL) if l.strip()]
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', _art(art, 'mem.log'))]
    rows = _rows()
    rows.append(DR.row('read', DR.free(), kernel='SIDE-explicit-formula', n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'], built_ref=ref[0] if ref else None,
                       toolchain=ref[-1] if ref else None, build_exit=ex, verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs[:40], sorry_warnings=len(warn_sorry),
                       axioms_lines=[l for l in ax if 'OffZero' in l or "'" + NS in l or 'error' in l][-30:], sorryAx=any('sorryAx' in l for l in ax),
                       runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact=art))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('n', 'run', 'conclusion', 'build_exit', 'verdict', 'sorry_warnings', 'sorryAx', 'runner_low_mb', 'free_mb')}, 'errors', len(errs))
    for l in rows[-1]['axioms_lines']:
        print('   ', l)


def cmd_errors(art):
    log = _art(art, 'build.log').split(NL)
    out, keep = [], 0
    for l in log:
        if re.search(r'^(error|warning: .*sorry)', l) or ': error' in l:
            keep = 16
        if keep:
            out.append(l)
            keep -= 1
    print(NL.join(out[:300]))
    print('### LOG LINES %d ; ERROR HEADS %d' % (len(log), len([l for l in log if l.startswith('error') or ': error' in l])))


def _lines(mod):
    p = os.path.join(CLONE, ZQ + mod + '.lean')
    return len(io.open(p, encoding='utf-8').read().rstrip(NL).split(NL)) if os.path.exists(p) else None


def lines_table(groups=GROUPS, est=SP1_LINES, label='SP1', at=':134'):
    out, tot = [], 0
    for g, mod, (lo, hi), _names in groups:
        n = _lines(mod)
        tot += n or 0
        out.append('  %-3s %-28s measured %s ; the estimate %d-%d ; %s' % (g, ZQ + mod + '.lean', n, lo, hi,
                                                                          'NOT WRITTEN' if n is None else 'within' if lo <= n <= hi else 'BELOW' if n < lo else 'ABOVE'))
    out.append('  %s IN ALL: measured %d ; the estimate %d-%d (data/b737_offlinezero_plan.txt %s) ; the ratio %.3f-%.3f' % (label, tot, est[0], est[1], at, tot / est[1], tot / est[0]))
    return out, tot


def cmd_lines():
    print(NL.join(lines_table()[0]))
    print(NL.join(lines_table(GROUPS2, SP2_LINES, 'S5a-S5b', ':87, :89')[0]))


def _ax_any(reads, name):
    """the axioms line of `name` from the latest KERNEL read whose artifact prints it: (list or None, run)."""
    for n in sorted(reads, reverse=True):
        r = reads[n]
        if r.get('build_exit') == '0' and r.get('artifact'):
            a = _ax_of(_art(r['artifact'], 'axioms.txt'), name)
            if a is not None:
                return a, r['run']
    return None, None


def _ax_of(axtext, name):
    """the axioms line of `name` in an axioms.txt: the standard three, a list, or None where not printed."""
    m = re.search(r"'%s' depends on axioms: \[([^\]]*)\]" % re.escape(name), axtext)
    if m:
        return tuple(x.strip() for x in m.group(1).split(','))
    if re.search(r"'%s' does not depend on any axioms" % re.escape(name), axtext):
        return ()
    return None


def cmd_bank(art):
    rows = _rows()
    disp = [r for r in rows if r['kind'] == 'dispatch']
    reads = dict((r['n'], r) for r in rows if r['kind'] == 'read')
    axt = _art(art, 'axioms.txt')
    ctl_std = _ax_of("'x' depends on axioms: [propext, Classical.choice, Quot.sound]", 'x') == STANDARD
    ctl_none = _ax_of("'y' does not depend on any axioms", 'y') == ()
    ctl_miss = _ax_of('', 'z') is None
    ctl_fig = FB.reading('## THE CONTROLS\n  a\n\n0.123') ['ok'] and not FB.reading('0.123\n## THE CONTROLS\n  a')['ok']
    free = DR.free()
    tab, tot = lines_table()
    sp1, sp1_run = _ax_any(reads, SP1)
    cor = _ax_any(reads, NS + 'zq_li_not_nonneg_of_box')[0]
    last = reads.get(max(reads)) if reads else None
    sp1_read = [r for r in reads.values() if r['run'] == sp1_run]
    reached = bool(sp1_read) and not sp1_read[0]['sorryAx'] and sp1_read[0]['sorry_warnings'] == 0 and set(sp1) <= set(STANDARD)
    L = ['b738 -- W-ORD-ZQ-OFFLINE-ZERO ON R4, BOX A, TO SP1 ((R348)(3)(a)) AND PAST IT TO SP2 ((R348)(3)(b)), BUILT ON zq-b730 FROM b25fd82c BY THE RUNNER (%s)' % _now(), '',
         '## THE CONTROLS',
         '  the axioms reader on a constructed standard line: %s ; on a constructed axiom-free line: %s ; on an absent name, None: %s' % (ctl_std, ctl_none, ctl_miss),
         '  the figure-bank reader: the controls first passes, the controls after refused: %s' % ctl_fig,
         '  the plan bank`s md5 equal to step zero`s %s: %s' % (PLAN_MD5, hashlib.md5(open(os.path.join(RELAY, PLAN), 'rb').read()).hexdigest() == PLAN_MD5),
         '  free memory at this bank: %d MB at %s, the hold %d' % (free[0], free[1], DR.HOLD),
         '  the dispatch rows refused by standing.dispatchrows: %s' % (DR.check(rows) or 'NONE'), '',
         '## THE DISPATCHES: %d OF AT MOST %d, EACH READ BY ITS RUN ID, EACH ROW CARRYING free_mb' % (len(disp), K.MAX_DISPATCHES)]
    for r in disp:
        rd = reads.get(r['n'], {})
        L.append('  %d | group %-3s | %s | sha %s | run %s | free %d MB | %s, exit %s, %d errors, sorry warnings %s, sorryAx %s, runner low %s MB, read at free %s MB' % (
            r['n'], r['item'], r['target'].split('.')[-1], r['sha'][:8], r['run'], r['free_mb'], rd.get('verdict', 'UNREAD'), rd.get('build_exit'), len(rd.get('errors') or []),
            rd.get('sorry_warnings'), rd.get('sorryAx'), rd.get('runner_low_mb'), rd.get('free_mb')))
    L += ['', '## THE LINES, MEASURED AGAINST THE PLAN`S ESTIMATES (I-10`s form)'] + tab + ['',
          '## THE AXIOMS OF S1-S4 AND (e), EACH FROM THE LATEST KERNEL READ WHOSE ARTIFACT PRINTS IT (the last read run %s; SP1 from run %s)' % (
              last['run'] if last else None, sp1_run)]
    for g, mod, _e, names in GROUPS:
        for nm in names:
            a, run = _ax_any(reads, NS + nm)
            L.append('  %-3s %-34s %s (run %s)' % (g, nm, 'NOT PRINTED' if a is None else (', '.join(a) or 'none'), run))
    L += ['',
          '## THE STATEMENT AT SP1 (SIDEExplicitFormula/Schema/ZQ/OffZero/Main.lean)',
          '  zq_offline_of_box (c : ℂ) (hc : c ∈ boxA) (m : ℝ) (hcm : ‖zqFn c‖ < m) (hfr : ∀ z ∈ frontier boxA, m ≤ ‖zqFn z‖) : ∃ ρ ∈ zqZeroConfig.carrier, ρ.re ≠ 1 / 2',
          '  THE OPEN HYPOTHESES, NAMED: hcm and hfr, the numerics of S5-S6 (zqFn certified at a point of box A below m, and at least m on its frontier); hc the point`s place,',
          '  which the ruling`s form leaves out (data/b738_offlinezero_notes.txt (1)). No sentence here says a zero is located in Lean or that Li nonnegativity fails as a theorem:',
          '  zq_li_not_nonneg_of_box carries the same two hypotheses.', '']
    tab2, tot2 = lines_table(GROUPS2, SP2_LINES, 'S5a-S5b', ':87, :89')
    L += ['## S5a-S5b PAST SP1 ((R348)(3)(b)): THE LINES, MEASURED AGAINST THE PLAN`S ESTIMATES (I-10`s form)'] + tab2 + ['',
          '## THE AXIOMS OF S5a-S5b, EACH FROM THE LATEST KERNEL READ WHOSE ARTIFACT PRINTS IT']
    sp2_ok = True
    for g, mod, _e, names in GROUPS2:
        for nm in names:
            a, run = _ax_any(reads, NS + nm)
            L.append('  %-3s %-34s %s (run %s)' % (g, nm, 'NOT PRINTED' if a is None else (', '.join(a) or 'none'), run))
    sp2ax = [_ax_any(reads, x)[0] for x in SP2]
    for x, a in zip(SP2, sp2ax):
        if a is None or not set(a) <= set(STANDARD):
            sp2_ok = False
    built = [r for r in reads.values() if r.get('build_exit') == '0']
    sp2 = reached and sp2_ok and all(_lines(m) for _g, m, _e, _n in GROUPS2) and not any(r.get('sorryAx') or r.get('sorry_warnings') for r in built)
    r_lo, r_hi = tot2 / SP2_LINES[1], tot2 / SP2_LINES[0]
    L += ['',
          '## THE STATEMENTS AT SP2 (SIDEExplicitFormula/Schema/ZQ/OffZero/Split.lean, Tail.lean)',
          '  zq_Λ₀_split (s : ℂ) : zqPair.Λ₀ s = lamM s + lamM (1 - s), lamM w = ∫ t in Ioi 1, (t : ℂ) ^ (w - 1) * (thetaC t - 1) (lamM_eq)',
          '  zq_thetaC_tail {t : ℝ} (ht : 1 ≤ t) : ‖(thetaC t - 1) - ((thetaTr (cc * t) - 1 : ℝ) : ℂ)‖ < 1e-14, thetaTr the box |m|, |n| ≤ 14',
          '  (data/b738_offlinezero_notes.txt (5): the box holds every Q ≤ 112; the plan`s Q(v) ≤ N form is not the one built). No integral is evaluated,',
          '  no value of zqFn is computed, no zero is located in Lean, and Li nonnegativity is not refuted as a theorem.', '',
          '## THE REMAINDER OF S5 PRICED AGAIN FROM S5a-S5b ((R348)(3)(b))',
          '  S5a-S5b`s ratio, measured over the estimate: %d / %d-%d = %.3f-%.3f' % (tot2, SP2_LINES[0], SP2_LINES[1], r_lo, r_hi),
          '  S5c-S5d at %d-%d (the plan :136): by that ratio %d-%d lines ; by the midpoint ratio %.3f, %d-%d' % (
              S5CD[0], S5CD[1], round(S5CD[0] * r_lo), round(S5CD[1] * r_hi), tot2 / 450, round(S5CD[0] * tot2 / 450), round(S5CD[1] * tot2 / 450)),
          '  S5c and S5d NOT BEGUN ((R348)(3)(c)); the incomplete gamma, complex Stirling and certified elementary values stay ABSENT at the pin (the plan :120-:123)', '',
          '### ### **SP1 %s ; SP2 %s ; DISPATCHES %d OF %d ; LINES SP1 %d AGAINST %d-%d, S5a-S5b %d AGAINST %d-%d ; zq_offline_of_box AXIOMS %s ; THE CONTRAPOSITIVE AXIOMS %s ; THE ORDER OPEN AT %s.**' % (
              'REACHED' if reached else 'NOT REACHED', 'REACHED' if sp2 else 'NOT REACHED', len(disp), K.MAX_DISPATCHES, tot, SP1_LINES[0], SP1_LINES[1],
              tot2, SP2_LINES[0], SP2_LINES[1],
              'NOT PRINTED' if sp1 is None else ', '.join(sp1) or 'none', 'NOT PRINTED' if cor is None else ', '.join(cor) or 'none',
              'SP2' if sp2 else 'SP1' if reached else 'S1')]
    r = FB.write(BANK, NL.join(L))
    print(NL.join(L))
    print('written data/b738_offlinezero.txt ; figbank: %s' % r['why'])


if __name__ == '__main__':
    a = sys.argv[1:]
    fn = {'planmd5': cmd_planmd5, 'clone': cmd_clone, 'commit': cmd_commit, 'push': cmd_push, 'dispatch': cmd_dispatch, 'read': cmd_read,
          'errors': cmd_errors, 'lines': cmd_lines, 'bank': cmd_bank}.get(a[0] if a else '')
    if not fn:
        sys.exit(__doc__)
    fn(*a[1:])
