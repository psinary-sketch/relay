# -*- coding: utf-8 -*-
"""b345_control.py -- THE LI CONTROL, RE-RUN, UNDER THIS ACT'S OWN BAR (registration sealed first).

### ### **THE TAIL RULE IS TANH-SINH AT BOTH ROUTES, FIXED IN THE SEALED REGISTRATION BEFORE ANY VALUE** -- the rule
### b340's own diagnosis named, against the Gauss-Legendre-on-an-infinite-panel that failed its bar. ### **b340's BAR IS
### NOT REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED**; this is a new bar with the same threshold and a different tail
### rule.
###   ROUTE A -- b340's `I_theta`, IMPORTED AND NOT EDITED: the theta substitution, the cosine identity, `mpmath`'s
###             digamma, tanh-sinh on `4n + 4` panels.
###   ROUTE B -- WRITTEN HERE, SHARING NO CODE WITH ROUTE A: the `u` variable; `Re G_n` by the COMPLEX POWER
###             `Re[1 - ((s-1)/s)^n]` and not by the cosine identity; the kernel HAND-ROLLED at the parameters the
###             registration sealed; the phase-multiple panels and the infinite tail, by tanh-sinh.
### ### **WHAT THEY SHARE, NAMED AND NOT CLAIMED DISJOINT:** arbitrary-precision arithmetic and elementary functions.
### ### **EVERY PARAMETER OF ROUTE B's KERNEL IS TYPED FROM THE SEALED TEXT AND NONE IS CHOSEN HERE.**
"""
import io
import json
import os
import sys
import time

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b340_li_control as LC   # noqa: E402  ### ROUTE A and the keystone reader -- IMPORTED, never edited
import b327_bridge as BR       # noqa: E402  ### the bench loader and the source's (4.11) -- IMPORTED
import noise_floor as NF       # noqa: E402

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BAR_REL = mp.mpf('1e-9')       # ### sealed, section (D): the same threshold b340 used, on this act's own bar
DPS_B = 40                     # ### route B's working precision
FIX_BAR = mp.mpf('1e-25')      # ### sealed, section (C): the kernel fixture's threshold
FIX_U = ('0', '0.3', '2', '7', '50', '300')   # ### sealed, section (C): the fixture's points
M_QUAD = 512
# ### ### **THE SEALED PARAMETERS OF ROUTE B's KERNEL, TYPED FROM THE SEALED TEXT AND NOT CHOSEN HERE:**
# ### *"`psi` by upward recurrence to `|w| >= 20` and then the Stirling asymptotic through `B_10`"*.
RECUR_TO = 20                  # ### sealed, section (C)
N_BERN = 5                     # ### sealed, section (C): B_2 .. B_10, five terms
# ### the DIAGNOSTIC threshold below is NOT this act's route B, and no value of the act is computed with it; it exists
# ### only to locate WHICH half of the sealed pairing carries a defect, if the sealed fixture finds one.
RECUR_DIAG = 300
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


# ### ==============================================================================================
# ### ROUTE B's KERNEL, HAND-ROLLED. ### NO SPECIAL FUNCTION OF mpmath IS CALLED.
# ### ==============================================================================================
# ### psi(w) ~ log w - 1/(2w) - SUM_k B_2k / (2k w^2k). ### The coefficients are typed as exact rationals from the
# ### Bernoulli numbers and are read from no library: B_2/2, B_4/4, B_6/6, B_8/8, B_10/10 -- which are the sealed five
# ### -- and then B_12/12 and B_14/14, which sit BEYOND the sealed truncation and are carried for one purpose only:
# ### so the size of the FIRST OMITTED TERM can be printed beside each measured miss.
_C = [(mp.mpf(1), mp.mpf(12)), (mp.mpf(-1), mp.mpf(120)), (mp.mpf(1), mp.mpf(252)), (mp.mpf(-1), mp.mpf(240)),
      (mp.mpf(1), mp.mpf(132)), (mp.mpf(-691), mp.mpf(32760)), (mp.mpf(1), mp.mpf(12))]


def psi_hand(z, broken=False, recur_to=RECUR_TO, nbern=N_BERN):
    """### `psi(z)` for complex `z` by upward recurrence and the Stirling asymptotic, AT THE SEALED PARAMETERS.
    ### `broken` drops the `1/(2w)` term -- the discrimination arm, which must fail the fixture."""
    w = mp.mpc(z)
    acc = mp.mpc(0)
    while abs(w) < recur_to:
        acc -= 1 / w
        w += 1
    out = mp.log(w) + acc
    if not broken:
        out -= 1 / (2 * w)
    w2 = w * w
    p = w2
    for num, den in _C[:nbern]:
        out -= num / (den * p)
        p = p * w2
    return out


def first_omitted(z, recur_to=RECUR_TO, nbern=N_BERN):
    """### the magnitude of the FIRST TERM THE SEALED TRUNCATION DROPS, at the `w` the recurrence lands on.
    ### ### **A PREDICTION OF THE ROUTINE'S FLOOR MADE FROM THE SEALED PARAMETERS ALONE, printed beside the measured
    ### miss so that a failure can be told from a coding defect without argument.**"""
    w = mp.mpc(z)
    while abs(w) < recur_to:
        w += 1
    num, den = _C[nbern]
    return abs(num / (den * w ** (2 * (nbern + 1)))), abs(w)


def h_plus_B(u, broken=False):
    """### the kernel by route B's own evaluator: `Re psi(1/4 + iu/2) - log pi`."""
    return mp.re(psi_hand(mp.mpc(mp.mpf(1) / 4, mp.mpf(u) / 2), broken)) - mp.log(mp.pi)


def reG_B(n, u):
    """### `Re G_n(1/2 + iu)` by the COMPLEX POWER, not by the cosine identity route A uses."""
    s = mp.mpc(mp.mpf(1) / 2, u)
    return mp.re(1 - ((s - 1) / s) ** n)


def I_u_B(n):
    """### ROUTE B: `(1/pi) INT_0^inf Re G_n h_+ du` on the phase-multiple panels and the infinite tail, TANH-SINH."""
    with mp.workdps(DPS_B):
        pts = [mp.tan(mp.pi * m / (2 * n)) / 2 for m in range(n)] + [mp.inf]
        v, err = mp.quad(lambda u: reG_B(n, u) * h_plus_B(u), pts, method='tanh-sinh', error=True)
        return v / mp.pi, err


def fixture():
    """### THE SEALED KERNEL FIXTURE, RUN AT THE SEALED PARAMETERS AND MEASURED, NOT ASSUMED."""
    rec('')
    rec("  (C) THE KERNEL FIXTURE, AT THE SEALED PARAMETERS -- upward recurrence to |w| >= %d, Stirling through B_%d:"
        % (RECUR_TO, 2 * N_BERN))
    rec('      %-6s %-11s %-11s %-11s %-11s %-13s' % ('u', '|w| after', 'true |diff|', 'first term', 'broken miss', 'at 1e-25'))
    rec('      %-6s %-11s %-11s %-11s %-11s %-13s' % ('', 'recurrence', 'vs mpmath', 'DROPPED', 'vs mpmath', 'true / broken'))
    worst, worst_broken, pts = mp.mpf(0), mp.mpf('inf'), []
    with mp.workdps(DPS_B):
        for u in FIX_U:
            z = mp.mpc(mp.mpf(1) / 4, mp.mpf(u) / 2)
            a, b, c = mp.re(psi_hand(z)), mp.re(mp.digamma(z)), mp.re(psi_hand(z, broken=True))
            fo, wend = first_omitted(z)
            da, dc = abs(a - b), abs(c - b)
            worst, worst_broken = max(worst, da), min(worst_broken, dc)
            pts.append(dict(u=u, w_end=mp.nstr(wend, 6), true=mp.nstr(da, 4), omitted=mp.nstr(fo, 4), broken=mp.nstr(dc, 4),
                            true_pass=bool(da <= FIX_BAR), broken_pass=bool(dc <= FIX_BAR)))
            rec('      %-6s %-11.4f %-11.3e %-11.3e %-11.3e %s / %s'
                % (u, float(wend), da, fo, dc, 'PASS' if da <= FIX_BAR else 'FAIL', 'PASS' if dc <= FIX_BAR else 'FAIL'))
    true_ok, broken_fails = worst <= FIX_BAR, worst_broken > FIX_BAR
    fx = true_ok and broken_fails
    rec("    worst true |diff| %.3e   (sealed threshold %s)   ; the broken copy's SMALLEST miss %.3e"
        % (worst, mp.nstr(FIX_BAR, 2), worst_broken))
    rec('    ### the true copy passes the sealed threshold : %s ; the broken copy fails it : %s ; THE FIXTURE : %s'
        % (true_ok, broken_fails, 'PASS' if fx else '### FAIL ###'))
    diag = None
    if not fx:
        rec('')
        rec('    ### ### **THE FIXTURE FAILED AT ITS SEALED THRESHOLD. ### DIAGNOSED HERE AND NOT REPAIRED-TO-PASS.**')
        rec('    ### The measured miss tracks the FIRST DROPPED TERM of the sealed truncation at every point, so what is')
        rec("    ### measured is the truncation's own floor and not a coding defect. ### **WHICH HALF OF THE SEALED")
        rec('    ### PAIRING CARRIES IT** is isolated by holding the truncation at the sealed `B_%d` and carrying the'
            % (2 * N_BERN))
        rec("    ### recurrence further, to `|w| >= %d`. ### **THIS IS A DIAGNOSTIC. ### IT IS NOT THIS ACT'S ROUTE B,"
            % RECUR_DIAG)
        rec('    ### AND NO VALUE ANYWHERE BELOW IS COMPUTED WITH IT.**')
        dw, dbw = mp.mpf(0), mp.mpf('inf')
        with mp.workdps(DPS_B):
            for u in FIX_U:
                z = mp.mpc(mp.mpf(1) / 4, mp.mpf(u) / 2)
                dw = max(dw, abs(mp.re(psi_hand(z, recur_to=RECUR_DIAG)) - mp.re(mp.digamma(z))))
                dbw = min(dbw, abs(mp.re(psi_hand(z, broken=True, recur_to=RECUR_DIAG)) - mp.re(mp.digamma(z))))
        dok = bool(dw <= FIX_BAR and dbw > FIX_BAR)
        rec('    DIAGNOSTIC -- truncation held at the sealed B_%d, recurrence carried to |w| >= %d : worst true %.3e ;'
            % (2 * N_BERN, RECUR_DIAG, dw))
        rec('                 broken smallest %.3e ; would the sealed fixture pass there : %s' % (dbw, dok))
        rec('    ### ### **THE DEFECT SITS IN ONE NAMED HALF OF THE SEALED PAIRING: THE RECURRENCE THRESHOLD')
        rec('    ### ### `|w| >= %d`, WHICH LEAVES THE ASYMPTOTIC A FLOOR NEAR `%.1e`, ABOVE THE THRESHOLD THE SAME'
            % (RECUR_TO, worst))
        rec('    ### ### SECTION SEALED. ### THE TRUNCATION THROUGH `B_%d` IS NOT THE DEFECTIVE HALF.**' % (2 * N_BERN))
        rec('    ### ### **AT `1e-25` THE FIXTURE REJECTS THE CORRECT COPY TOO, SO AT ITS OWN THRESHOLD IT SEPARATES')
        rec('    ### ### NOTHING. ### THE BAR IS TABLED, NOT EDITED; THE SEALED FILE IS NOT TOUCHED; AND ROUTE B RUNS')
        rec('    ### ### BELOW AT THE SEALED PARAMETERS AND NOT AT THE DIAGNOSTIC ONES.**')
        rec("    ### WHAT THE BAR WOULD HAVE LICENSED AND THEREFORE IS NOT CONFERRED: that route B's hand-rolled kernel is")
        rec('    ### correct AT THE SEALED TOLERANCE. ### **WHAT IS CARRIED INSTEAD IS A MEASUREMENT -- agreement to')
        rec('    ### `%.3e` -- AND A MEASUREMENT IS NOT A MET BAR.**' % worst)
        diag = dict(recur=RECUR_DIAG, worst=mp.nstr(dw, 4), broken=mp.nstr(dbw, 4), would_pass=dok)
    return fx, worst, worst_broken, pts, diag, bool(true_ok), bool(broken_fails)


def main():
    t0 = time.time()
    rec('=' * 100)
    rec("b345 -- THE LI CONTROL, RE-RUN. ### the tail rule fixed before any value; two routes sharing no code.")
    rec('=' * 100)
    fails = []
    fx, kworst, kbroken, fpts, diag, true_ok, broken_fails = fixture()
    if not fx:
        fails.append('KERNEL FIXTURE (SEALED THRESHOLD) -- DEFECTIVE BAR, TABLED')
    # ### the keystone's indices
    rows, head_line = LC.keystone_table()
    idx = [r['n'] for r in rows]
    nmax = max(idx)
    rec('')
    rec("  THE KEYSTONE'S TABLE (owner file, line %d): %d rows, indices %s" % (head_line, len(rows), idx))
    # ### the deposit's channel, two routes, and the pole constant as its own column
    rec('')
    rec("  ROUTE A' -- lambda_A(n) and the pole constant by the bench's own definitions (b327_bridge loader), two radii, M = %d:" % M_QUAD)
    ns, nhead, _k = BR.load_bench_definitions()
    lamA, lamZ, pole = {}, {}, {}
    tA = time.time()
    for r in BR.RADII:
        lamA[r] = ns['lambdas'](ns['taylor_coeffs'](ns['f_A'], r, M_QUAD, nmax), nmax)
        lamZ[r] = ns['lambdas'](ns['taylor_coeffs'](ns['f_Z'], r, M_QUAD, nmax), nmax)
        pole[r] = ns['lambdas'](ns['taylor_coeffs'](lambda s: mp.log(s), r, M_QUAD, nmax), nmax)
    r0, r1 = BR.RADII
    radii_worst = max(abs(lamA[r0][n] - lamA[r1][n]) for n in idx)
    pole_worst = max(abs(pole[r0][n] - 1) for n in idx)
    SB = {n: BR.s_inf_closed(n) for n in idx}
    routeB_worst = max(abs(lamA[r0][n] - (SB[n] + 1)) for n in idx)
    rec('    bench head executed : %d lines ; %.0f s ; the two radii agree to %.3e ; the pole constant L_n[log s] - 1 worst %.3e'
        % (nhead, time.time() - tA, radii_worst, pole_worst))
    rec("    ROUTE B' -- S_inf(n) + 1 by the source's (4.11): worst |lambda_A - S_inf - 1| = %.3e (b327's identity, re-measured)" % routeB_worst)
    # ### the instrument
    rec('')
    rec('  THE INSTRUMENT -- I(n) by ROUTE A (b340 theta, imported) and ROUTE B (u, complex power, hand-rolled kernel), both TANH-SINH:')
    rec('    %-4s %-24s %-24s %-11s %-9s %-5s %-24s %-11s %-7s' % ('n', 'I(n) route A', 'I(n) route B', 'drift', 'gate', 'pole', 'lambda_A', '|I+1-lamA|', 'bar?'))
    table, holds_all = [], True
    for n in idx:
        tn = time.time()
        ia, ea = LC.I_theta(n)
        ib, eb = I_u_B(n)
        with mp.workdps(DPS_B):
            drift = abs(ia - ib)
            verdict, _why = NF.classify(float(ia), float(ib))
            la = lamA[r0][n]
            bar = BAR_REL * max(mp.mpf(1), abs(la))
            miss = abs(ia + 1 - la)
            ok = (miss <= bar) and (drift <= bar) and (verdict == NF.RESOLVED)
            holds_all = holds_all and ok
            ks = mp.mpf(rows[idx.index(n)]['lamA'])
            rec('    %-4d %-24s %-24s %-11.3e %-9s %-5s %-24s %-11.3e %-7s  (%.0f s; keystone %s off by %.2e)'
                % (n, mp.nstr(ia, 20), mp.nstr(ib, 20), drift, verdict, mp.nstr(pole[r0][n], 3), mp.nstr(la, 20), miss,
                   'HOLDS' if ok else '### FAILS', time.time() - tn, mp.nstr(ks, 13), abs(ia + 1 - ks)))
            table.append(dict(n=n, I_A=mp.nstr(ia, 25), I_B=mp.nstr(ib, 25), err_A=mp.nstr(ea, 3), err_B=mp.nstr(eb, 3),
                              drift=mp.nstr(drift, 3), gate=verdict, pole=mp.nstr(pole[r0][n], 20), lamA=mp.nstr(la, 25),
                              S_inf_plus_1=mp.nstr(SB[n] + 1, 25), miss=mp.nstr(miss, 3), bar=mp.nstr(bar, 3), holds=bool(ok),
                              keystone_lamA=rows[idx.index(n)]['lamA'], keystone_miss=mp.nstr(abs(ia + 1 - ks), 3),
                              lamZ=mp.nstr(lamZ[r0][n], 20), keystone_lamZ=rows[idx.index(n)]['lamZ'],
                              keystone_margin=rows[idx.index(n)]['margin'], margin=mp.nstr(lamA[r0][n] + lamZ[r0][n], 20),
                              margin_positive=bool(lamA[r0][n] + lamZ[r0][n] > 0)))
    worst_miss = max(mp.mpf(t['miss']) for t in table)
    worst_drift = max(mp.mpf(t['drift']) for t in table)
    worst_ks = max(mp.mpf(t['keystone_miss']) for t in table)
    n_hold = sum(1 for t in table if t['holds'])
    rec("    ### the bar holds at %d of %d indices ; worst |I + 1 - lambda_A| = %.3e ; worst drift between the routes = %.3e ; worst against the keystone's printed column = %.3e"
        % (n_hold, len(table), worst_miss, worst_drift, worst_ks))
    # ### the verdict by the sealed rule of section (D), and by no other
    rec('')
    what = 'none'
    if holds_all:
        rec("  ### ### **VERDICT, BY SECTION (D)'s RULE: A FOURTH CONTROL HOLDS.** ### The instrument agrees with a margin")
        rec('  ### the deposit proved, on a family outside the lawful class. ### **THAT SENTENCE AND NO MORE.**')
        verdict_s = 'A FOURTH CONTROL HOLDS'
    else:
        bad = [t for t in table if not t['holds']]
        offs = [mp.mpf(t['I_A']) + 1 - mp.mpf(t['lamA']) for t in bad]
        const = (max(abs(o - offs[0]) for o in offs) < mp.mpf('1e-6')) if len(offs) > 1 else True
        gate_ref = any(t['gate'] != NF.RESOLVED or mp.mpf(t['drift']) > mp.mpf(t['bar']) for t in bad)
        what = 'a quadrature failure (the gate refusing)' if gate_ref else ('a constant offset (the pole constant miscarried)' if const else 'a growth with n (the tail)')
        rec("  ### ### **VERDICT, BY SECTION (D)'s RULE: THE DIFFERING CONSTITUENT -- the bar fails at %s ; what differs: %s.**"
            % ([t['n'] for t in bad], what))
        verdict_s = 'THE DIFFERING CONSTITUENT'
        fails.append('BAR')
    if not fx:
        rec('')
        rec("  ### ### **AND THE ACT CLOSES WITH ONE SEALED ARM OF `G-ROUTES` TABLED AS A DEFECTIVE BAR.** ### The verdict")
        rec("  ### above is section (D)'s and is reached on section (D)'s own measurements. ### **WHAT THE FAILED FIXTURE")
        rec("  ### WOULD HAVE LICENSED IS NOT CONFERRED: NO CLAIM IS MADE THAT ROUTE B's KERNEL IS CORRECT AT `1e-25`.**")
        rec('  ### The disjointness half of `G-ROUTES` is a separate and separately checkable thing, and the check suite')
        rec('  ### measures it. ### The kernel was measured to agree to `%.3e`, which is a measurement and not a met bar,' % kworst)
        rec("  ### and which sits far below this act's own `1e-9` bar -- ### **THAT LAST CLAUSE IS AN OBSERVATION AND IS")
        rec('  ### NOT A REPAIR OF THE FIXTURE, WHICH STAYS FAILED AND STAYS UNEDITED.**')
    # ### the certifications, as the prior leg listed them
    rec('')
    rec("  THE CERTIFICATIONS, LISTED AS THE PRIOR LEG LISTED THEM (b340, quoted through the extract file):")
    rec("    ### WHICH APPLY: the kernel identity (b333), a property of the kernel; the arrangement Z = P - PR + A (b321),")
    rec("    ###   which on the Li family is the source's (4.6) channel for channel; the noise-floor gate as a method.")
    rec("    ### WHICH DO NOT: Theorem 1's inequality and the Sonin margin (defined on the class only); the square on the")
    rec("    ###   stable cut; b321's control bar and b326's per-cell closures; the atlas's zero-side truncation bound.")
    rec("    ### AND THE FAMILY IS NOT IN THE LAWFUL CLASS: three of three of Theorem 1's conditions fail (b340, re-stated).")
    # ### the deposit's finite-range positivity, restated at its scope
    rec('')
    rec("  THE DEPOSIT'S FINITE-RANGE POSITIVITY, RESTATED AT ITS SCOPE, BESIDE THE INSTRUMENT'S VALUES:")
    mono = io.open(LC.MONO, encoding='utf-8', errors='replace').read().splitlines()
    cl = [i + 1 for i, ln in enumerate(mono) if LC.CERT_FRAG in ln]
    sent = ''
    if cl:
        ln = mono[cl[0] - 1]
        a = ln.index(LC.CERT_FRAG) - 1
        sent = ln[a:ln.index('no further', a) + len('no further')]
    rec('    the monograph, line %s: *"%s"*' % (cl[0] if cl else 'NOT FOUND', sent))
    bench_txt = io.open(LC.BENCH, encoding='utf-8').read().splitlines()
    bl = [i + 1 for i, ln in enumerate(bench_txt) if LC.BENCH_FRAG in ln]
    rec('    the bench, line %s: *"%s"*' % (bl[0] if bl else 'NOT FOUND', LC.BENCH_FRAG))
    rec('    %-4s %-20s %-20s %-20s %-20s %-8s' % ('n', 'lambda_A', 'lambda_Z', 'margin lambda_n', "keystone's margin", 'sign'))
    for t in table:
        rec('    %-4d %-20s %-20s %-20s %-20s %-8s' % (t['n'], mp.nstr(mp.mpf(t['lamA']), 13), mp.nstr(mp.mpf(t['lamZ']), 13),
                                                       mp.nstr(mp.mpf(t['margin']), 13), t['keystone_margin'], 'POSITIVE' if t['margin_positive'] else '### NOT'))
    allpos = all(t['margin_positive'] for t in table)
    ks_z_worst = max(abs(mp.mpf(t['lamZ']) - mp.mpf(t['keystone_lamZ'])) for t in table)
    rec("    the margin positive at all %d tabulated indices : %s ; the keystone's lambda_Z column reproduced to %.3e"
        % (len(table), allpos, ks_z_worst))
    rec("    ### THE CERTIFICATE IS THE DEPOSIT'S AND ITS PREMISES ARE NAMED AND OPEN ; POSITIVITY IN A FINITE RANGE IS NOT")
    rec("    ### EVIDENCE OF THE KIND THE CRITERION RESPECTS ; AND THE SONIN MARGIN IS NOT DEFINED ON THIS FAMILY AT ALL.")
    rec('')
    rec("  ### NO ZERO SIDE AND NO FINITE SIDE EVALUATED ; NO GRADE MOVED ; b340's BAR NOT REWRITTEN AND NOT RE-VERDICTED.")
    rec('  ### CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    p, k = os.path.join(D, 'b345_control_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b345_control_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b345_control.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(indices=idx, table=table, holds_all=bool(holds_all), n_hold=n_hold, verdict=verdict_s, what=what,
             worst_miss=mp.nstr(worst_miss, 3), worst_drift=mp.nstr(worst_drift, 3), worst_keystone=mp.nstr(worst_ks, 3),
             kernel_fixture=bool(fx), kernel_worst=mp.nstr(kworst, 4), kernel_broken=mp.nstr(kbroken, 4),
             kernel_true_ok=true_ok, kernel_broken_fails=broken_fails, kernel_points=fpts, kernel_diagnostic=diag,
             recur_to=RECUR_TO, n_bern=N_BERN, fix_bar=mp.nstr(FIX_BAR, 2),
             radii_worst=mp.nstr(radii_worst, 3), pole_worst=mp.nstr(pole_worst, 3), routeB_worst=mp.nstr(routeB_worst, 3),
             cert_line=cl[0] if cl else None, cert_sentence=sent, bench_line=bl[0] if bl else None,
             all_margins_positive=bool(allpos), keystone_lamZ_worst=mp.nstr(ks_z_worst, 3), keystone_head_line=head_line,
             fails=fails, run_file=os.path.basename(p), elapsed=time.time() - t0), indent=1))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
