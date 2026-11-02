# -*- coding: utf-8 -*-
"""b733_count.py -- (R343)(3): THE count FIELD'S PLAN BANK AND ITS DISPATCH ROWS. Written at b733 by the Write tool. No lean process runs on this host; every build is the runner's.

  plan                  writes data/b733_count_plan.txt: for each of C1-C7 its Prop, its nearest compiled neighbour by path and line printed from the tree at ZQ_ENTERING,
                        its price re-read by the measured ratios through standing.pricebank.reprice_read, the build order, the stop points; C3 and C4 in full, priced apart
  push <sha>            a push row, the free read taken now
  dispatch <sha> <n> <item> <target>   gh workflow run, the row carrying the free read before it; the run id read back into the row
  read <n> <run> <artifact dir> a read row, verdict from the artifact's files
  bank                  writes data/b733_count.txt from the rows and the tip
"""
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
import b733_worklist as K        # noqa: E402
import dispatchrows as DR        # noqa: E402
import pricebank as PB           # noqa: E402

NL = '\n'
EF = 'D:/SIDE-explicit-formula'
ML = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
REPO = 'psinary-sketch/SIDE-explicit-formula'
TIP = K.ZQ_ENTERING
ROWS = os.path.join(D, 'b733_dispatch_rows.json')
PLAN = os.path.join(D, 'b733_count_plan.txt')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def show(path, at=TIP):
    return git(EF, 'show', '%s:%s' % (at, path)).replace('\r', '')


def decl(path, name, at=TIP):
    """(line, lines): the declaration's first line in the tree and its span to the next declaration; a name the file lacks raises."""
    ls = show(path, at).split(NL)
    hit = [i for i, l in enumerate(ls, 1) if re.match(r'^(?:private |noncomputable |protected )*(?:theorem|lemma|def) %s\b' % re.escape(name), l)]
    if len(hit) != 1:
        raise SystemExit('### %s: %d DECLARATIONS OF %s, NOT ONE -- NOTHING WRITTEN' % (path, len(hit), name))
    i = hit[0]
    j = i
    while j < len(ls) and not re.match(r'^(?:/--|theorem |lemma |def |end |/-!)', ls[j]):
        j += 1
    return i, j - i + 1


def mathlib_line(path, needle):
    h = [i for i, l in enumerate(git(ML, 'show', 'HEAD:' + path).replace('\r', '').split(NL), 1) if needle in l]
    if not h:
        raise SystemExit('### %s: NO LINE CARRIES %s -- NOTHING WRITTEN' % (path, needle))
    return h[0]


def rd(name):
    return io.open(os.path.join(D, name), encoding='utf-8').read()


CHI, RVM = 'SIDEExplicitFormula/Chi/LocalCount.lean', 'Zeta23/RvM/LocalCount.lean'
# ### the seven: name, the Prop as the plan fixes it, the neighbour by (path, declaration), the seat's lines, the module
LEMMAS = (
    ('C1', 'the disc: for every t, the zeros with Re >= 1/2 in (t, t+1], with multiplicity, number at most A1 log(|t| + 3) (halfQ_count)', CHI, 'half_count_large_chi', 150, 'Count'),
    ('C2', 'growth on the strip: exists M, for Re s >= -1/2, |a(s)| <= M |s + 2|^3 (aE_growth)', 'Zeta23/RvM/ZetaGrowth.lean', None, 230, 'Growth'),
    ('C3', 'the lower bound at the centre: for Re s >= 3/2, |Z_Q(s)| >= 4 - Z_Q(3/2) (zq_norm_ge)', 'SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 'zq_ne_zero_of_three_halves_le', 45, 'Growth'),
    ('C4', 'Z_Q(3/2) < 4: TAKEN AS COMPILED, zq_three_halves_tsum_lt, the sum over k of r_Q(k) / k^(3/2) < 4, no line of this act', 'SIDEExplicitFormula/Schema/ZQ/Bound.lean', 'zq_three_halves_tsum_lt', 0, 'Bound, compiled'),
    ('C5', 'the small heights: ABSORBED. a has no pole, so the disc of C1 holds at every t and no finite constant is needed; no Lean declaration, the row kept so the seven stay seven', CHI, 'count_small_chi', 0, 'none'),
    ('C6', 'the assembly: zq_count_holds : exists A0, Wide.HCount zqZeroConfig A0', CHI, 'chiZeroConfig_local_count', 30, 'Count'),
    ('C7', 'the halving: N(T1, T2) <= 2 times the sum over the window with Re >= 1/2, over WideConfig (wide_N_le_two_mul_half)', 'Zeta23/RvM/Halving.lean', 'N_le_two_mul_half', 60, 'Count'),
)
ORDER_ROWS = (
    ('A', 'C3, C4 read', 'SIDEExplicitFormula.Schema.ZQ.Growth, first section', 'totQ, zq_sub_two_le, zq_norm_le, zq_norm_ge, zq_three_halves_eq'),
    ('B', 'C2', 'SIDEExplicitFormula.Schema.ZQ.Growth, whole', 'norm_Gamma_le, norm_sin_le_exp, norm_inv_Gamma_le, Lam0_bounded, aE_apriori, aE_left_edge, aE_right, aE_growth'),
    ('C', 'C7, C1, C6', 'SIDEExplicitFormula.Schema.ZQ.Count', 'wide_N_le_two_mul_half, aE_order_eq, gQ, halfQ_count, zq_count_holds'),
)


def cmd_plan():
    assert not os.path.exists(PLAN), 'the plan stands'
    price, meas = rd('b729_count_price.txt'), rd('b731_price_measured.txt')
    rows, nb = [], {}
    for c, prop, path, name, seat, mod in LEMMAS:
        if name is None:
            ln, span = 1, len(show(path).split(NL))
        else:
            ln, span = decl(path, name)
        nb[c] = (path, ln, span, name)
    tot = sum(v[2] for v in nb.values())
    env = {}
    for by in ('continuation', 'logDeriv', 'zeros'):
        env[by] = PB.reprice_read(price, meas, 'count', by)
    L = ['b733 -- THE count FIELD`S PLAN, (R343)(3): C1-C7 ON THE RESTATED PREMISE, C3 AND C4 IN FULL, COMMITTED BEFORE ANY LEAN (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### every neighbour read from the tree at zq-b730 %s by tools/b733_count.py; the Mathlib objects at the pin de5ce8a9 by path and line; each price the seat`s, a range, no bound. No lean process on this host.' % TIP[:8], '',
         '## THE STATEMENT',
         '  Schema/Wide/Config.lean :49 HCount Z A0 := 1 <= A0 and for all t, N(t, t+1) <= A0 log(|t| + 3). The restated premise (data/b732_a0_restatement.txt :23) asks exists A0, Wide.HCount Z A0, so A0 is unnamed.',
         '  The theorem aimed at: zq_count_holds : exists A0, Wide.HCount zqZeroConfig A0, in SIDEExplicitFormula/Schema/ZQ/Count.lean, on zq-b730 alone.', '',
         '## THE ROUTE, THE LEAST ONE, AND WHAT DIFFERS FROM THE PRICE BANK`S ROWS',
         '  The bank`s rows copy the kernel`s route over zeta. Two readings, data/b733_stepzero.txt :21-:22, shorten it; neither is a theorem until it compiles.',
         '  (1) Jensen runs on aE (Schema/ZQ/Zeros.lean :98), a(s) = (1 - s) Z_Q(s) extended, entire, aE 1 = -qBase; so the disc needs no distance from a pole, C1 holds at every t, and C5 is absorbed.',
         '  (2) The left edge needs no Stirling at Re s = -1/2: the functional equation gives |Gamma(1 - s) / Gamma(s)| = 1/4 + t^2 exactly, Gamma`s recursion twice and Gamma_conj. That line fixes the strip at [-1/2, 3/2].',
         '  THE DISC: centre c0 = 3/2 + (t + 1/2) i, kappa = 13/10, r = 0.87, R = 0.95. kappa r = 1.131 >= sqrt(5/4), so the disc holds every point with 1/2 <= Re < 3/2 and t < Im <= t + 1; kappa R = 1.235, so it reads aE at Re >= 0.265 and |Im| <= |t| + 2.',
         '  ZerosBound (Zeta23/FromPNTPlus/StrongPNTPrefix.lean :481) on g(z) = aE(c0 + kappa z) u, u = (aE c0)^-1: the sum of orders in the small disc is at most log B / log(R / r).',
         '  B = (M + 1) (|t| + 7)^3 / delta, delta = (4 - totQ) / 2, from C2 above and from C3 below: |aE c0| = |1 - c0| |Z_Q(c0)| >= delta. log B <= K log(|t| + 3), the count.', '',
         '## THE SEVEN, EACH WITH ITS PROP, NEIGHBOUR AND PRICE',
         '### THE BANK`S PRICE, RE-READ BY THE THREE MEASURED RATIOS THROUGH standing.pricebank.reprice_read, NO FIGURE TYPED (800-2000 lines, 15-35 dispatches, data/b729_count_price.txt :25):']
    for by in ('continuation', 'logDeriv', 'zeros'):
        ll, lh, dl, dh = env[by]
        L.append('  by %-13s %s-%s lines, %s-%s dispatches' % (by, ll, lh, dl, dh))
    al = [x for v in env.values() for x in v[:2]]
    ad = [x for v in env.values() for x in v[2:]]
    L += ['  THE ENVELOPE %s-%s lines, %s-%s dispatches, equal to data/b731_price_measured.txt :31; the ratios disagree and that spread is no confidence interval.' % (min(al), max(al), min(ad), max(ad)),
          '### EACH LEMMA`S SHARE OF THE ENVELOPE, BY ITS NEIGHBOUR`S LINES IN THE TREE, THE SEAT`S APPORTIONING; AND THE SEAT`S OWN ESTIMATE ON THIS ROUTE BESIDE IT:', '']
    for c, prop, path, name, seat, mod in LEMMAS:
        p, ln, span, nm = nb[c]
        f = span / float(tot)
        L += ['  %s  %s' % (c, prop),
              '      neighbour  %s :%d %s, %d lines' % (p, ln, nm or '(the module)', span),
              '      price      share %.3f of the envelope: %d-%d lines, %.1f-%.1f dispatches ; the seat`s on this route: %d lines ; module %s' % (f, round(min(al) * f), round(max(al) * f), min(ad) * f, max(ad) * f, seat, mod), '']
    L += ['  THE SEAT`S SUM ON THIS ROUTE: %d lines, 3-8 dispatches, inside the envelope. C4 and C5 cost no line, and the price bank`s row for each is read down accordingly. A compile failure costs a dispatch; no module is built here first.' % sum(x[4] for x in LEMMAS), '',
          '## C3 IN FULL, PRICED APART: 45 LINES, ONE DISPATCH OF GROUP A',
          '  THE STATEMENT, with c = 3/2 fixed: for Re s >= 3/2, |Z_Q(s)| >= 4 - Z_Q(3/2), where Z_Q(3/2) is the real sum totQ. On the line Re s = c it is the ruling`s form.',
          '  THE SOURCE: b685 step (3), data/b685_count_plan.txt :26-:29, |Z_Q(s) - 2| <= Z_Q(sigma) - 2 < 2 for sigma >= 3/2, and step (6), :55-:59, the Euler-product bound replaced by |Z_Q(c + iT)| >= 2 - (Z_Q(c) - 2) = 4 - Z_Q(c) > 0, c >= 3/2 forced.',
          '  THE ROUTE, LEMMA BY LEMMA:',
          '    totQ := the sum over k of wQ k, wQ of Schema/ZQ/LogDeriv.lean :%d' % decl('SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 'wQ')[0],
          '    zq_sub_two_le : Re s >= 3/2 -> |zqFn s - 2| <= totQ - 2. The proof of zq_ne_zero_of_three_halves_le, LogDeriv.lean :%d, to its line `hn`, taken whole; the file is not edited.' % decl('SIDEExplicitFormula/Schema/ZQ/LogDeriv.lean', 'zq_ne_zero_of_three_halves_le')[0],
          '    zq_norm_le : Re s >= 3/2 -> |zqFn s| <= totQ, the triangle inequality on zq_sub_two_le.',
          '    zq_norm_ge : Re s >= 3/2 -> 4 - totQ <= |zqFn s|, the reverse triangle inequality. THIS IS C3.',
          '    zq_three_halves_eq : zqFn (3/2) = totQ, so the bound reads as the ruling writes it, 4 - Z_Q(3/2); LSeries termwise, Complex.ofReal_tsum.',
          '  THE MATHLIB OBJECTS AT THE PIN: tsum_of_norm_bounded, HasSum.sub, hasSum_ite_eq, LSeries.norm_term_eq, Real.rpow_le_rpow_of_exponent_le, as LogDeriv.lean uses them; no new object.',
          '  THE KERNEL`S ANALOGUE, the Euler product, is not used; Z_Q has none. C3 stands on r_Q >= 0 and the term at k = 1, r_Q(1) = 2, and on C4.', '',
          '## C4 IN FULL, PRICED APART: 0 LINES',
          '  READ AGAINST THE ROWS: C3 needs totQ < 4. zq_three_halves_tsum_lt, Schema/ZQ/Bound.lean :%d at 23b006df and at this tip, is that sentence: the sum over k of r_Q(k) / k^(3/2) < 4. zq_three_halves_lt, :%d, is its lattice form.' % (
              decl('SIDEExplicitFormula/Schema/ZQ/Bound.lean', 'zq_three_halves_tsum_lt')[0], decl('SIDEExplicitFormula/Schema/ZQ/Bound.lean', 'zq_three_halves_lt')[0]),
          '  TAKEN AS THAT THEOREM. No certified truncation is planned; b729`s row (data/b729_count_price.txt :33) stands answered by b731. delta = (4 - totQ) / 2 > 0 needs only the strict inequality, no rational beside it.', '',
          '## C2 IN FULL: THE ROUTE, LEMMA BY LEMMA, WITH THE MATHLIB OBJECTS BY PATH AND LINE',
          '  F(s) = aE s / (s + 2)^3 on the strip -1/2 <= Re s <= 3/2, width 2, so c = 1 < pi / 2 is allowed.',
          '  right edge : Re s >= 3/2: |aE s| = |1 - s| |Z_Q s| <= |s + 2|^3 totQ, by zq_norm_le; this also carries Re s > 3/2 directly.',
          '  left edge  : Re s = -1/2: zq_fe (Zeros.lean :%d) with w = s + 1: |Gamma(1 - s)| = |w| |s| |Gamma s|, by Gamma_add_one twice and Gamma_conj, so |Z_Q s| = lam^-2 |w| |s| |Z_Q(1 - s)| <= lam^-2 |s + 2|^2 totQ.' % decl('SIDEExplicitFormula/Schema/ZQ/Zeros.lean', 'zq_fe')[0],
          '  a priori   : for |Im s| >= 1 on the strip, aE s = q^s (Gamma s)^-1 ((1 - s) Lam0 s - 1 - (1 - s) / s). Lam0 bounded on vertical strips: it is mellin f_modif, |t^(s-1)| <= t^(a-1) + t^(b-1), both integrable by the strong pair`s convergence.',
          '               (Gamma s)^-1 = (s - 1)^-1 (Gamma (s - 1))^-1, and for Re w < 1, (Gamma w)^-1 = Gamma(1 - w) sin(pi w) / pi, with |Gamma z| <= Gamma(Re z) for Re z > 0 and |sin z| <= exp |Im z|. So |F s| <= K exp(pi |Im s|), which is O(exp(pi exp(1 * |Im s|))).',
          '  conclusion : PhragmenLindelof.vertical_strip gives |F| <= M on the strip.',
          '  OBJECTS:']
    for path, needle, what in (('Mathlib/Analysis/Complex/PhragmenLindelof.lean', 'theorem vertical_strip', 'PhragmenLindelof.vertical_strip'),
                               ('Mathlib/Analysis/SpecialFunctions/Gamma/Beta.lean', 'theorem Gamma_mul_Gamma_one_sub (z : ℂ)', 'Complex.Gamma_mul_Gamma_one_sub'),
                               ('Mathlib/Analysis/SpecialFunctions/Gamma/Beta.lean', 'theorem Gamma_ne_zero_of_re_pos', 'Complex.Gamma_ne_zero_of_re_pos'),
                               ('Mathlib/Analysis/SpecialFunctions/Gamma/Basic.lean', 'theorem Gamma_add_one (s : ℂ)', 'Complex.Gamma_add_one'),
                               ('Mathlib/Analysis/SpecialFunctions/Gamma/Basic.lean', 'theorem Gamma_conj', 'Complex.Gamma_conj'),
                               ('Mathlib/Analysis/SpecialFunctions/Gamma/Basic.lean', 'theorem Gamma_eq_integral {s : ℂ}', 'Complex.Gamma_eq_integral'),
                               ('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 'def Λ₀', 'WeakFEPair.Λ₀'),
                               ('Mathlib/NumberTheory/LSeries/AbstractFuncEq.lean', 'theorem hasMellin (s : ℂ)', 'IsStrongFEPair.hasMellin; the convergence lemma beside it is private, so the route reads HasMellin`s first half'),
                               ('Mathlib/Analysis/MellinTransform.lean', 'def mellin', 'mellin'),
                               ('Mathlib/MeasureTheory/Integral/Bochner/Basic.lean', 'theorem norm_integral_le_of_norm_le', 'norm_integral_le_of_norm_le'),
                               ('Mathlib/Analysis/Calculus/DiffContOnCl.lean', 'theorem DifferentiableOn.diffContOnCl', 'DifferentiableOn.diffContOnCl')):
        L.append('    %s :%d %s' % (path, mathlib_line(path, needle), what))
    L += ['',
          '## THE ORDER OF BUILD; EACH GROUP ONE DISPATCH READ BY ITS RUN ID, FREE MEMORY READ BEFORE IT AND CARRIED IN EVERY ROW BY standing.dispatchrows',
          '  group | lemmas | module | declarations']
    L += ['  %s | %s | %s | %s' % r for r in ORDER_ROWS]
    L += ['', '## THE STOP POINTS',
          '  after each group, its run read before the next dispatch; a failing group is repaired from its log and re-dispatched, each re-dispatch counted, at most fourteen in the act.',
          '  group A stands: C3 compiled, C4 read, whatever follows.',
          '  group B fails past repair: the count stops OPEN at C2, the sorry-free remainder printed, three of five fields, the instance`s grade unchanged.',
          '  group C fails past repair: OPEN at the lemma named by the log, C2 and C3 standing. Fourteen dispatches spent: the same, at the lemma reached.',
          '  CLOSED: zq_count_holds with its axiom print, the standard three, no sorryAx; four of five fields; explicitFormula open, the instance not DERIVES.', '',
          '### ### **THE PLAN: SEVEN ROWS, C4 TAKEN AS COMPILED, C5 ABSORBED, FIVE TO BUILD ; C3 AND C4 IN FULL ; THREE GROUPS ; AT MOST FOURTEEN DISPATCHES ; NOTHING BUILT.**']
    io.open(PLAN, 'w', encoding='utf-8', newline='\n').write(NL.join(L) + NL)
    print(NL.join(L))


def _rows():
    return json.load(io.open(ROWS, encoding='utf-8')) if os.path.exists(ROWS) else []


def cmd_push(sha):
    rows = _rows()
    rows.append(DR.row('push', DR.free(), kernel='SIDE-explicit-formula', branch='zq-b730', sha=sha, remote_equal=git(EF, 'rev-parse', 'origin/zq-b730').strip() == sha, at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_commit(sha, item):
    rows = _rows()
    full = git(EF, 'rev-parse', sha).strip()
    rows.append(DR.row('commit', DR.free(), kernel='SIDE-explicit-formula', branch='zq-b730', item=item, sha=full, parent=git(EF, 'rev-parse', full + '^').strip(),
                       files=[x for x in git(EF, 'show', '--format=', '--name-only', full).split(NL) if x]))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_dispatch(sha, n, item, target):
    read = DR.free()
    if read[0] < DR.HOLD:
        sys.exit('### FREE %d UNDER THE HOLD -- NOT DISPATCHED' % read[0])
    if int(n) > K.MAX_DISPATCHES:
        sys.exit('### DISPATCH %s PAST THE ACT`S FOURTEEN -- NOT DISPATCHED' % n)
    r = subprocess.run(['gh', 'workflow', 'run', 'build-module.yml', '--repo', REPO, '--ref', 'main', '-f', 'ref=' + sha, '-f', 'target=' + target], capture_output=True, text=True, encoding='utf-8', errors='replace')
    print(r.stdout, r.stderr)
    m = re.search(r'/runs/(\d+)', r.stdout + r.stderr)
    rows = _rows()
    if r.returncode != 0:
        rows.append(DR.row('dispatch_refused', read, kernel='SIDE-explicit-formula', item=item, n=int(n), sha=sha, target=target, at=read[1], error=(r.stderr or '')[:300]))
    else:
        rid = m.group(1) if m else ''
        if not rid:
            time.sleep(6)
            rid = json.loads(subprocess.run(['gh', 'run', 'list', '--repo', REPO, '--workflow', 'build-module.yml', '--limit', '1', '--json', 'databaseId'], capture_output=True, text=True).stdout)[0]['databaseId']
        rows.append(DR.row('dispatch', read, kernel='SIDE-explicit-formula', item=item, n=int(n), workflow='build-module.yml', at_ref='main', sha=sha, target=target, run=int(rid), at=read[1]))
    DR.write(ROWS, rows)
    print(rows[-1])


def cmd_read(n, run, art):
    v = json.loads(subprocess.run(['gh', 'run', 'view', str(run), '--repo', REPO, '--json', 'status,conclusion,updatedAt'], capture_output=True, text=True, encoding='utf-8').stdout)
    ex = io.open(art + '/build_exit.txt', encoding='utf-8').read().strip()
    log = io.open(art + '/build.log', encoding='utf-8', errors='replace').read()
    ref = io.open(art + '/ref.txt', encoding='utf-8').read().strip().split()[0]
    errs = [l for l in log.split(NL) if l.startswith('error: ') and 'SIDEExplicitFormula' in l]
    warn_sorry = [l for l in log.split(NL) if 'declaration uses' in l and 'sorry' in l]
    ax = [l for l in io.open(art + '/axioms.txt', encoding='utf-8', errors='replace').read().split(NL) if l.strip()]
    nums = [int(x) for x in re.findall(r'avail_mb=(\d+)', io.open(art + '/mem.log', encoding='utf-8', errors='replace').read())]
    rows = _rows()
    rows.append(DR.row('read', DR.free(), kernel='SIDE-explicit-formula', n=int(n), run=int(run), status=v['status'], conclusion=v['conclusion'], built_ref=ref, toolchain=io.open(art + '/ref.txt', encoding='utf-8').read().strip().split()[-1],
                       build_exit=ex, verdict='KERNEL' if ex == '0' else 'BREAKS', errors=errs, sorry_warnings=len(warn_sorry), axioms_lines=[l for l in ax if 'ZQ.' in l or 'error' in l][-30:], sorryAx=any('sorryAx' in l for l in ax), runner_low_mb=min(nums) if nums else None, at=v['updatedAt'], artifact='scratchpad run/build-module-%s' % run))
    DR.write(ROWS, rows)
    print({k_: rows[-1][k_] for k_ in ('n', 'run', 'conclusion', 'build_exit', 'verdict', 'sorry_warnings', 'sorryAx', 'runner_low_mb', 'free_mb')}, 'errors', len(errs))


if __name__ == '__main__':
    a = sys.argv[1:]
    if not a:
        sys.exit(__doc__)
    if a[0] == 'plan':
        cmd_plan()
    elif a[0] == 'commit':
        cmd_commit(a[1], a[2])
    elif a[0] == 'push':
        cmd_push(a[1])
    elif a[0] == 'dispatch':
        cmd_dispatch(a[1], a[2], a[3], a[4])
    elif a[0] == 'read':
        cmd_read(a[1], a[2], a[3])
    else:
        sys.exit(__doc__)
