# -*- coding: utf-8 -*-
"""b561_record.py -- LANE TWO, ACT THREE: THE LI-WEIL BRIDGE AT THE LIMIT EXCHANGE -- THE DECAY READ, (D1)-(D4) ATTEMPTED,
HELD AT THE EARLIEST OBSTACLE; b560 ENTERED AT ITS WEIGHT; THE PUSH DISCIPLINE; THE CONSUMER READ: THE RECORD, UNDER (R171).
### `python tools/b561_record.py reads | weight | decay | item <Dk> <names> | e0 | consumer | findings | row | rowgen_diff |
### workorder | trail | components | desk`
### b560's helpers are IMPORTED (b560_record), never copied. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b560_record as Q  # noqa: E402
P = Q.P
PP, FIND, OT, CORR, EF, LV = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF, Q.LV
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
at, decl_at, statement, statement_block = Q.at, Q.decl_at, Q.statement, Q.statement_block
parse_prints, check_line, rowgen_record, STD3 = Q.parse_prints, Q.check_line, Q.rowgen_record, Q.STD3
put_txt, put_json, jl = Q.put_txt, Q.put_json, Q.jl
PRIOR_RELAY = 'd3f1b1d9'   # ### b560's table housekeeping -- relay's tip before this act
PRIOR_PP = '86676f5'       # ### b560's PLACE-papers commit
PRIOR_GS = 'f8b8a1e'       # ### SIDE-global-section before this act
V04 = '941503b836c1f3548d94b1207276f724dba3263f'
BR = 'li-weil-b561'
OLD = 'li-weil-b560'
NSL = 'SIDEExplicitFormula.LiWeil.'
BALPOS = Q.BALPOS
SCR = os.environ.get('B561_SCRATCH') or os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


# ------------------------------------------------------------------------------ READING (1): the reads
def reads():
    L = ['b561 -- READING (1): THE READS, PRINTED VERBATIM BY PATH AND LINE', '### SIDE-explicit-formula v0.4 = %s' % V04[:7], '']
    src = at(V04, 'SIDEExplicitFormula/LiWeil.lean')
    names = re.findall(r"^(?:theorem|def)\s+([A-Za-z_']+)", src, re.M)
    L.append('### LiWeil.lean @941503b -- every declaration (%d):' % len(names))
    rows = []
    for n in names:
        k = decl_at(src, n)
        st = statement(src, k, 14)
        for i, l in enumerate(st):
            L.append('    LiWeil.lean:%-4d | %s' % (k + i, l))
        rows.append(dict(rev=V04[:7], file='SIDEExplicitFormula/LiWeil.lean', name=n, line=k))
    for rel, n in (('Zeta23/WeilEF/ZeroSummability.lean', 'zero_sum_inv_sq'), ('Zeta23/WeilEF/ZeroSummability.lean', 'zero_sum_inv_sq_gen'),
                   ('SIDEExplicitFormula/PowerLimit.lean', 'weighted_summable'), ('SIDEExplicitFormula/PowerLimit.lean', 'weighted_finite_bound'),
                   ('SIDEExplicitFormula/PowerLimit.lean', 'rest_tendsto_zero'), ('SIDEExplicitFormula/PowerLimit.lean', 'dominant_summable'),
                   ('Zeta23/ExplicitFormula.lean', 'EF_lit')):
        t = at(V04, rel)
        k = decl_at(t, n)
        L.append('')
        L.append('### %s:%d @941503b -- %s' % (rel, k, n))
        for i, l in enumerate(statement(t, k, 10)):
            L.append('    %5d | %s' % (k + i, l))
        rows.append(dict(rev=V04[:7], file=rel, name=n, line=k))
    L.append('    ### the exponents: zero_sum_inv_sq sums m_ρ / (1 + ‖γ_ρ‖²) -- EXPONENT 2 in ‖γ_ρ‖; weighted_summable asks')
    L.append('    ### f ρ (1 + |⌈Im ρ⌉|)^4 <= Bf -- EXPONENT 4 in the ordinate.')
    sd = rd(os.path.join(D, 'b560_stageD.txt')).split(NL)
    L.append('')
    L.append('### relay data/b560_stageD.txt :137-:176 (the obstacle, (D1)-(D6), the converse (V1)-(V4)):')
    for i in range(136, min(176, len(sd))):
        L.append('    b560_stageD.txt:%d | %s' % (i + 1, sd[i]))
    pr = rd(os.path.join(D, 'b549_premise.txt')).split(NL)
    L.append('')
    L.append('### relay data/b549_premise.txt:12 | ' + pr[11])
    B = rd(BALPOS).split(NL)
    L.append('### BALANCE_AND_POSITIVITY.md:764 | ' + B[763][:300])
    F = rd(FIND).split(NL)
    for n in (5478, 5486, 5575, 5601):
        L.append('### FINDINGS.md:%d | %s' % (n, F[n - 1][:300]))
    for repo in (EF, ROOT):
        h = rd(os.path.join(repo, '.githooks', 'pre-push')).split(NL)
        L.append('### %s/.githooks/pre-push:1-4 (core.hooksPath = %s) | %s' % (os.path.basename(repo), g(repo, 'config', 'core.hooksPath').strip(), ' / '.join(h[:4])))
        rule = [i + 1 for i, l in enumerate(h) if 'push-*' in l and 'REFUSED' in l]
        L.append('    the main-from-push-* refusal at :%s | %s' % (rule, h[rule[0] - 1].strip()[:160] if rule else ''))
    df = rd(os.path.join(D, 'b560_defects.txt'))
    L.append('### relay data/b560_defects.txt (e) | ' + df[df.index('(e) THE TAG'):df.index('(f) ')].replace(NL, ' ')[:600])
    L.append('### the push tools in relay before this act: %s ; no standing push script' % sorted(x for x in os.listdir(T) if 'push' in x))
    put_txt('b561_reads.txt', L)
    put_json('b561_reads.json', dict(rows=rows, names=names))
    print('  written: b561_reads.txt (%d lines), %d declarations of LiWeil.lean' % (len(L), len(names)))


# ------------------------------------------------------------------------------ READING (2): b560 at its weight
W_TWOFORMS = ('*Appended 2026-09-29 by b561, under the author’s ruling `(R171)`(1), to the two-forms entry (:5478, its joint at :5486) '
              '-- THE LI FORM’S FORWARD HALF COMPILED:*')
W_BALPOS = ('*Appended 2026-09-29 by b561 beneath the block at :764, under the author’s ruling `(R171)`(1); no byte above changes -- '
            'THE LI FORM’S FORWARD HALF COMPILED:*')
W_TIER = ('*Appended 2026-09-29 by b561, under `(R171)`(1) -- THE TIER-LAW LINE:*')
W_FIELD = ('*Appended 2026-09-29 by b561 to the field entry (:5575) and its sources block (:5601), under `(R171)`(1) -- THE '
           'PROGRAMME’S LI FORM BESIDE THE FIELD:*')


def weight():
    for p, h in ((FIND, W_TWOFORMS), (BALPOS, W_BALPOS), (FIND, W_TIER), (FIND, W_FIELD)):
        guard_absent(p, h)
    k = 'SIDE-explicit-formula v0.4 = `941503b`, `LiWeil.lean`'
    out = {}
    out['twoforms'] = append_to(FIND, NL + W_TWOFORMS + ' the Li form’s forward half now stands compiled over the genuine zeros: '
                                '`rh_imp_li_nonneg : RiemannHypothesis → ∀ n, 0 ≤ LiCoeff n` (%s), `LiCoeff n` the absolutely '
                                'convergent sum Σ_ρ m_ρ Re (1 − (1 − ρ⁻¹)ⁿ) over the nontrivial zeros of Mathlib’s ζ. The form as an '
                                'equivalence is not compiled: the converse (∀ n, 0 ≤ LiCoeff n → RH) stays T1-lit, priced at relay '
                                '`data/b560_stageD.txt` (V1)-(V4). With `h2_sign_iff_rh` it composes: h2_sign → RH → every Li '
                                'coefficient nonnegative.' % k + NL)
    out['balpos'] = append_to(BALPOS, NL + W_BALPOS + ' `rh_imp_li_nonneg : RiemannHypothesis → ∀ n, 0 ≤ LiCoeff n` (%s): the '
                              'forward half of the Li form, over the zeros of Mathlib’s ζ with multiplicity, the coefficient '
                              'absolutely convergent. The Li form as an equivalence to RH is not compiled; its converse is T1-lit '
                              '(Bombieri–Lagarias 1999, Theorem 1).' % k + NL)
    out['tier'] = append_to(FIND, NL + W_TIER + ' `rh_imp_li_nonneg` is **T0** by the tier law (FINDINGS :4805): a closed statement '
                            'over Mathlib’s objects -- its one premise Mathlib’s `RiemannHypothesis`, its conclusion a sign of a sum '
                            'over the zeros of `riemannZeta` weighted by `analyticOrderAt` -- with no premise carrying the content. It '
                            'is not an RH-anchor in the proving direction: it concludes from RH. The converse is T1-lit.' + NL)
    out['field'] = append_to(FIND, NL + W_FIELD + ' beside the field’s Weil-criterion records the programme now holds the Li form’s '
                             'forward half compiled (`rh_imp_li_nonneg`, %s) and its converse T1-lit, priced (V1)-(V4); the Weil '
                             'form compiled both ways (`h2_sign_iff_rh`) as before.' % k + NL)
    out['lines'] = dict(twoforms=line_of(FIND, W_TWOFORMS), balpos=line_of(BALPOS, W_BALPOS), tier=line_of(FIND, W_TIER),
                        field=line_of(FIND, W_FIELD))
    put_json('b561_weight.json', out)
    for key, p in (('twoforms', FIND), ('balpos', BALPOS), ('tier', FIND), ('field', FIND)):
        n = out['lines'][key]
        print('  %s:%d | %s' % (os.path.basename(p), n, rd(p).split(NL)[n - 1][:220]))



# ------------------------------------------------------------------------------ READING (4): the decay read
DECAY = r'''b561 -- READING (4): THE DECAY READ, ON THE PAGE, BEFORE ANY BUILD (COMPONENT 3)
### The objects are v0.4's (LiWeil.lean): blSmooth n u = e^{u/2} P_n(u), blTest n = 1_{u<0} blSmooth n, truncMember n f =
### f · blSmooth n for a bump f = ContDiffBump c, and LiLimitExchange n's family: bumps with c + rOut <= 0 tending to 1 at every
### u < 0. Every step below is a derivation on the page; a step resting on a result not compiled in the federation says so.

### (1) THE TRANSFORM AT A ZERO. paperFT k z = ∫ k(u) e^{i z u} du (Defs.lean:60) and gammaOf ρ = (ρ - 1/2)/i, so
###     i · gammaOf ρ · u = (ρ - 1/2) u and e^{u/2} e^{(ρ-1/2)u} = e^{ρ u}. At a member f:
###         H_f(ρ) := paperFT (truncMember n f) (gammaOf ρ) = ∫ f(u) P_n(u) e^{ρ u} du,
###     and at the jump function (D1, blTransform): H(ρ) = ∫_{u<0} P_n(u) e^{ρ u} du = 1 - (1 - 1/ρ)^n = liTerm n ρ for Re ρ > 0.
###     The member and P_n are real, so the paired transform at a member is H_f(ρ) + H_f(conj ρ) = 2 Re H_f(ρ), as at the jump.

### (2) THE EXCESS, AND THE TRUNCATION PARAMETER. E_f(ρ) := H_f(ρ) - H(ρ) = ∫ (f(u) - 1_{u<0}) P_n(u) e^{ρ u} du. The bump is
###     1 on [c - rIn, c + rIn] and 0 off (c - rOut, c + rOut), with c + rOut <= 0. Its RIGHT deficit lies in [c + rIn, 0]:
###     put δ := -(c + rIn) > 0, the distance from the bump's plateau to 0. Pointwise convergence to 1 at every u < 0 forces
###     δ_m -> 0 along the family (and c_m - rIn_m -> -∞ on the left). On the right, 1_{u<0} - f ∈ [0, 1], equal to 1 on
###     [c + rOut, 0) and to 1 - st on the transition; write μ δ := ∫_{-δ}^{0} (1 - f(u)) du, μ ∈ (0, 1] (μ = 1/2 when
###     c + rOut = 0, by st(1 - t) = 1 - st(t) for Mathlib's Real.smoothTransition).

### (3) WHERE ‖ρ‖ δ IS SMALL. On [-δ, 0]: |e^{ρ u} - 1| <= ‖ρ‖ δ e^{‖ρ‖ δ} and |P_n(u) - n| <= δ 2^n (P_n(0) = C(n,1) = n;
###     the coefficients C(n, j+1)/j! sum to at most 2^n). So the right part of the excess is
###         E_right = ∫_{-δ}^{0} (f - 1) P_n e^{ρu} du = -n μ δ + r,   |r| <= δ² (2^n + 2 n ‖ρ‖)   (for ‖ρ‖ δ <= 1/2),
###     and Re E_right <= -n μ δ / 2 < 0 once ‖ρ‖ δ <= μ/8 and δ <= n μ /(4·2^n). THE SIGN IS ONE AND THE SAME FOR EVERY ZERO in
###     that range. The left part is ∫_{u <= c - rIn} (f - 1) P_n e^{ρ u}: of size e^{-β R} R^{n-1} at R = rIn - c -> ∞ for a zero
###     of real part β -- it tends to 0 for each zero, uniformly on zeros with β bounded below.
### (4) WHERE ‖ρ‖ δ IS LARGE. Integrating by parts, E_right = -n/ρ + (1/ρ) ∫ f' P_n e^{ρu} du + (terms of order 1/‖ρ‖²), and the
###     middle term is O(1/(‖ρ‖² δ)) by a second integration by parts on the smooth transition: the excess tends back to the
###     jump's own -n/ρ, whose real part n β/‖ρ‖² is what Stage B's bound already carries.
### (5) THE SUPREMUM OVER THE FAMILY AT A FIXED ZERO. For a member with δ ≍ μ/(8‖ρ‖), (3) gives |2 Re E_f(ρ)| >= n μ δ ≍ n μ²/(8 ‖ρ‖),
###     while the jump's pair is O(liConst n / ‖ρ‖²) (pairTerm_norm_le). So along any family whose δ_m passes through every scale
###     (δ_m = 1/m does), sup_m |pair_m(ρ)| >= c_n / ‖ρ‖ for every large zero: THE UNIFORM BOUND IS OF ORDER n/‖ρ‖, NOT n/‖ρ‖². A
###     bound C/‖ρ‖² at a member needs δ <= C'/‖ρ‖², a rate in the truncation parameter depending on the zero; a family gives
###     each δ_m for all zeros at once, and no δ_m -> 0 meets it at every zero.

### (6) AGAINST zero_sum_inv_sq's EXPONENT. zero_sum_inv_sq (ZeroSummability.lean:247) makes Σ m_ρ/(1 + ‖γ_ρ‖²) converge:
###     exponent 2. The uniform bound (5) has exponent 1, and Σ m_ρ/‖ρ‖ DIVERGES -- by the Riemann-von Mangoldt count
###     N(T) ≍ T log T (a literature theorem, T1-lit; the kernel carries only the upper local count
###     zetaZeroConfig_local_count, which cannot prove a divergence). weighted_summable's exponent 4 is further off still.
###     ### **SO (D3) IS NEITHER A PAIRING ESTIMATE ON EXISTING LEMMAS NOR A NEW SUMMABILITY LEMMA: A DOMINANT FOR THE PAIRED
###     ### TRUNCATED TRANSFORMS UNIFORM ALONG THE FAMILY AND SUMMABLE OVER THE ZEROS DOES NOT EXIST.** The pairing does not
###     help: the excess is REAL at leading order (-n μ δ), so pairing doubles it rather than cancelling it.

### (7) THE ZERO SIDE ALONG THE FAMILY -- A DERIVATION, NOT COMPILED. The excess has one sign on the zeros with ‖ρ‖ δ <= μ/8,
###     roughly (1/π)(μ/8δ) log(1/δ) of them (Riemann-von Mangoldt, T1-lit), so it sums to about -(n μ²/(8π)) log(1/δ). Read on
###     the other side of EF_lit instead (truncMember_EF, compiled): the right edge moves neither the pole terms (they converge)
###     nor the prime terms (they sit at |u| = log m >= log 2); it enters the Γ-integral only, where gammaBracket(r) grows like
###     log|r| (Stirling; Zeta23/GammaFacts carries Stirling bounds, whose use here is not checked), and the excess, of size
###     n δ Δ(i r δ) with Δ the transition's Laplace profile, integrates against log|r| to
###         (n/2π) log(1/δ) ∫ Re Δ(ix) dx + O(1) = (n/2π) log(1/δ) · (2π · (-1/2)) = -(n/2) log(1/δ) + O(1)
###     -- the Fourier integral picks the midpoint (-1/2) of the excess's jump at 0, whatever the profile. ### **SO ALONG EVERY
###     FAMILY IN LiLimitExchange's HYPOTHESIS THE ZERO SIDE TENDS TO -∞ FOR n >= 1: LiLimitExchange n IS EXPECTED FALSE FOR
###     n >= 1** (for n = 0, P_0 = 0 and both sides are 0). The one-sided smoothing moves the jump's midpoint into u < 0; the
###     Bombieri-Lagarias identity holds at the jump normalised to its midpoint, k_n(0) = n/2, which no member of this family
###     approaches from both sides. This is a derivation resting on Stirling's sharp asymptotic and (for the zero-count form)
###     on Riemann-von Mangoldt, neither of which this act compiles; it is not a theorem of the kernel.

### (8) THE SCORE. H12a: "the paired truncated transform decays at least like 1/‖ρ‖² uniformly in the truncation parameter ...
###     refuted if the uniform bound needs a rate in the truncation parameter the family does not give" -- ### **REFUTED BY THE
###     DERIVATION**: (5), the uniform bound is of order n/‖ρ‖; a 1/‖ρ‖² bound needs δ <= C/‖ρ‖², a rate the family does not give.
### (9) WHAT THIS DOES TO THE PRICE. (D3) as priced at b560 does not exist; (D4) by Tannery has no dominant; b560's stated
###     `LiLimitExchange` is, on this derivation, false for n >= 1, so `li_identity_of_exchange` is INTERFACES on a premise
###     that cannot be discharged in the form written. Re-priced:
###       (X1) the explicit formula on a class containing the jump normalised to its midpoint (Weil's formula for functions of
###            bounded variation with k(0) = (k(0-) + k(0+))/2) -- the leading item at OPEN_TRAILS :11424, "the explicit formula
###            on a class wider than EF_lit's" -- a lemma of substance, T1-lit in the literature (Weil 1952; Bombieri 2000);
###       (X2) or two-sided families, the transition centred at 0, for which the -(n/2) log(1/δ) term cancels at leading
###            order; the zero side still has no uniform dominant (the excess stays of order 1/‖ρ‖ per zero with signs that
###            now alternate), so the limit is taken on EF_lit's OTHER side -- the pole terms, the prime sum (D5) and the
###            Γ-integral converging -- and the zero side's limit is read through the identity, not by Tannery;
###       (X3) LiLimitExchange restated for (X2)'s family and the one-sided statement's failure recorded; a Lean proof of the
###            failure would need the Riemann-von Mangoldt lower count or Stirling's asymptotic in the kernel -- priced, not
###            attempted.
###     (D1) and (D2) stand as priced and valid on either family; they are attempted next, in the bank's order.
'''


def decay():
    num = rd(os.path.join(SCR, 'decay_num_out.txt'))
    L = DECAY.rstrip(NL).split(NL) + ['', '### THE NUMERICAL ILLUSTRATION (scratchpad decay_num.py, mpmath 30 digits; n = 1, P_1 = 1; Mathlib`s',
                                      '### Real.smoothTransition profile, right edge at 0, width δ; ρ = 1/2 + iγ) -- AN ILLUSTRATION, NOT EVIDENCE FOR A THEOREM:']
    L += ['    ' + x for x in num.rstrip(NL).split(NL)]
    L += ['### read: for ‖ρ‖δ small, 2 Re E = -2 n μ δ to four digits (one sign); the supremum over δ of ‖ρ‖ |2 Re E| is 1.742,',
          '### 1.766, 1.770 at γ = 14.1, 100, 1000 -- flat in ‖ρ‖, so the uniform bound is ≈ 1.77 n/‖ρ‖, the order (5) derives.']
    put_txt('b561_decay_read.txt', L)
    put_json('b561_decay.json', dict(h12a='REFUTED', uniform_order='n/||rho||', d3='NEITHER', exchange_expected='FALSE for n >= 1',
                                     sup_values=re.findall(r'of \|rho\| \|2 Re E\| : ([0-9.]+)', num)))
    print('  written: b561_decay_read.txt (%d lines) ; sup values %s' % (len(L), re.findall(r'of \|rho\| \|2 Re E\| : ([0-9.]+)', num)))



# ------------------------------------------------------------------------------ READING (5): the items
ITEMS = {
    'D1': ('blTransform DISCHARGED -- the transform of k_n at gammaOf ρ is the Li term for Re ρ > 0',
           ['norm_pow_mul_cexp', 'integrableOn_pow_mul_cexp', 'integral_pow_mul_cexp', 'blPoly_neg_cast', 'binomial_li',
            'blTest_integrand', 'blTransform_holds']),
    'D2': ('the member transforms tend to the jump`s at each fixed zero, Re ρ > 0 (dominated convergence in u)',
           ['integrable_blTest_integrand', 'truncMember_transform_tendsto']),
}
MOD = 'SIDEExplicitFormula/LiWeilExchange.lean'
NSX = NSL


def item():
    X = sys.argv[2]
    title, names = ITEMS[X]
    src = rd(os.path.join(EF, MOD)).replace(chr(13), '')
    att = sorted(f for f in os.listdir(SCR) if re.match(r'st%s_\d+\.txt$' % X, f))
    pr = rd(os.path.join(SCR, 'items_prints.txt'))
    P0 = parse_prints(pr)
    L = ['b561 -- READING (5): ITEM %s -- %s' % (X, title), '',
         '### the branch %s from v0.4 = %s ; the module %s (fed on stdin after LiWeil.lean, which has no olean)' % (BR, V04[:7], MOD), '',
         '### THE ELABORATION ATTEMPTS OF THIS ITEM, each with its exit and error count (the whole module as it then stood):']
    for f in att:
        t = rd(os.path.join(SCR, f)).split(NL)
        L.append('    ' + t[0])
        for x in t[1:]:
            if x.strip() and 'deprecated' not in x and 'linter' not in x:
                L.append('        | ' + x[:230])
    L.append('')
    L.append('### THE DECLARATIONS OF THIS ITEM, AS THE SOURCE STATES THEM:')
    for n in names:
        k = decl_at(src, n)
        for i, l in enumerate(statement(src, k, 12)):
            L.append('    %5d | %s' % (k + i, l))
    L.append('')
    L.append('### LEAN`S PRINTS:')
    for n in names:
        L.append('    %s : %s' % (n, P0.get(NSX + n)))
        c = check_line(pr, NSX + n)
        if c:
            L.append('        ' + c[:400])
    rows = {n: dict(axioms=P0.get(NSX + n), std3_or_fewer=P0.get(NSX + n) is not None and set(P0[NSX + n]) <= set(STD3)) for n in names}
    ok = all(r['std3_or_fewer'] for r in rows.values())
    L.append('### ### **PRINTED %d OF %d ; THE STANDARD THREE OR FEWER, NO sorryAx : %s**' % (
        sum(1 for r in rows.values() if r['axioms'] is not None), len(names), ok))
    put_txt('b561_%s.txt' % X, L)
    put_json('b561_%s.json' % X, dict(item=X, names=names, rows=rows, all_std3=ok, attempts=len(att)))
    print('  written: b561_%s.txt ; %s' % (X, L[-1]))


D34 = ['b561 -- READING (5): ITEMS D3 AND D4 -- HELD AT THE READ, BEFORE A LINE OF (D3) WAS WRITTEN', '',
       '### ### **(D3) HELD -- THE EARLIEST OBSTACLE.** relay `data/b561_decay_read.txt` (5)-(6): a dominant for the paired truncated',
       '### transforms uniform along the family does not exist; the uniform bound is of order n/‖ρ‖, and Σ m_ρ/‖ρ‖ diverges over the',
       '### zeros (Riemann-von Mangoldt, T1-lit). So (D3) is NEITHER a pairing estimate on existing lemmas NOR a new summability',
       '### lemma, and no line of it is written ((R171)(3): the read decides before the build).',
       '### ### **(D4) NOT REACHED** -- Tannery over the zeros needs (D3)`s dominant, which does not exist.',
       '### ### **AND THE STATED EXCHANGE**: `LiLimitExchange` (LiWeil.lean, v0.4) is, on the decay read`s (7), expected FALSE for n >= 1',
       '### (the zero side along a one-sided family tends to -∞ like -(n/2) log(1/δ)); a derivation, not a theorem of the kernel.',
       '### ### **RE-PRICED** (the decay read`s (9)): (X1) the explicit formula on a class containing the midpoint-normalised jump',
       '### (Weil`s formula for functions of bounded variation; the leading item at OPEN_TRAILS :11424) -- substance, T1-lit; (X2) a',
       '### two-sided family centred at 0 and the limit read on EF_lit`s other side ((D5) first, then the identity), no Tannery on',
       '### the zero side; (X3) LiLimitExchange restated for (X2)`s family, the one-sided failure recorded; (D5), (D6) as priced at',
       '### b560. (D1) and (D2), landed here, stand on either family.']


def items_held():
    put_txt('b561_D3_D4.txt', D34)
    print('  written: b561_D3_D4.txt')


# ------------------------------------------------------------------------------ READING (6): the E0 read
X_GRADES = {
    'norm_pow_mul_cexp': ('DERIVES', 'the norm of the integrand'),
    'integrableOn_pow_mul_cexp': ('DERIVES', 'x^j e^{-ρx} integrable on (0, ∞) for Re ρ > 0'),
    'integral_pow_mul_cexp': ('DERIVES', 'the Gamma integral at a complex rate for natural exponents, j!/ρ^(j+1), by integration by parts'),
    'blPoly_neg_cast': ('DERIVES', 'P_n(-x) as a complex finite sum'),
    'binomial_li': ('DERIVES', 'Σ_{j<n} C(n,j+1)(-1)^j ρ^{-(j+1)} = liTerm n ρ'),
    'blTest_integrand': ('DERIVES', 'the integrand of paperFT (blTest n) at gammaOf ρ is 1_{u<0} P_n(u) e^{ρu}'),
    'blTransform_holds': ('DERIVES', '(D1): blTransform n -- b560`s stated Prop -- holds for every n'),
    'integrable_blTest_integrand': ('DERIVES', 'the jump`s integrand integrable on ℝ for Re ρ > 0'),
    'truncMember_transform_tendsto': ('DERIVES', '(D2): the member transforms tend to the jump`s at each fixed ρ, Re ρ > 0 -- per zero, nothing uniform'),
}


def e0():
    src = rd(os.path.join(EF, MOD)).replace(chr(13), '')
    names = re.findall(r"^(?:theorem|def)\s+([A-Za-z_']+)", src, re.M)
    pr = rd(os.path.join(SCR, 'items_prints.txt'))
    P0 = parse_prints(pr)
    L = ['b561 -- READING (6): THE E0 READ -- EVERY DECLARATION OF LiWeilExchange.lean GRADED, THE SALT-CHECK, THE ROWGEN RECORD', '']
    rows = {}
    for n in names:
        gr, why = X_GRADES.get(n, ('### UNGRADED', ''))
        ax = P0.get(NSX + n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-30s %-9s %s -- %s' % (n, gr, ax, why))
    L.append('### the salt-check: no Prop is defined in the module; blTransform_holds concludes b560`s `blTransform n`, whose body is')
    L.append('### Zeta23`s paperFT of the test function at gammaOf ρ equal to liTerm n ρ (Lean`s #print below) -- nothing encoded.')
    blk = pr[pr.index('def SIDEExplicitFormula.LiWeil.blTransform'):] if 'def SIDEExplicitFormula.LiWeil.blTransform' in pr else ''
    L += ['    ' + x for x in blk.split(NL)[:6]]
    defs = re.findall(r'^def\s+(\S+)', src, re.M)
    recs, ctl = rowgen_record([NSX + n for n in ('blTransform_holds', 'integral_pow_mul_cexp', 'truncMember_transform_tendsto')], MOD,
                              g(EF, 'rev-parse', 'HEAD').strip(), pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % g(EF, 'rev-parse', '--short', 'HEAD').strip())
    for r in recs:
        L.append('    %-30s defenc %-5s %s | doc: %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], r['doc'][:100]))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    gate = all(r['std3_or_fewer'] for r in rows.values()) and all(r['grade'] == 'DERIVES' for r in rows.values()) and not defs and ctl[0]
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; EVERY GRADE DERIVES %s ; NO DEFINITION IN THE MODULE %s => MERGE %s**'
             % (all(r['std3_or_fewer'] for r in rows.values()), all(r['grade'] == 'DERIVES' for r in rows.values()), not defs, gate))
    put_txt('b561_e0.txt', L)
    put_json('b561_e0.json', dict(rows=rows, gate=gate, rowgen=recs, rowgen_control=ctl[0], names=names, defs=defs))
    print(NL.join(L[-3:]))


# ------------------------------------------------------------------------------ READING (7): the consumer read
CONSUMER_H = ('*Appended 2026-09-29 by b561, under the author’s ruling `(R171)`(4), to the LI-WEIL-BRIDGE work-order (:3548; b560’s line '
              'at :11523) -- THE CONSUMER READ:*')


def consumer():
    guard_absent(OT, CONSUMER_H)
    lv = at('HEAD', 'SIDELvConservation/RegisterPentagon.lean', LV)
    zp = at('HEAD', 'SIDELvConservation/ZeroActingPairing.lean', LV)
    def blk(t, name, cap=6):
        k = decl_at(t, name)
        return (k, statement(t, k, cap)) if k else (None, [])
    L = ['b561 -- READING (7): THE CONSUMER READ -- THE THREE STATEMENTS SIDE BY SIDE', '']
    pr = rd(os.path.join(D, 'b549_premise.txt')).split(NL)
    L.append('### (i) inequalityToPositivity, as b549 banked it (relay data/b549_premise.txt:12):')
    L.append('    ' + pr[11].strip())
    for t, n, f in ((lv, 'Register4_positivity', 'RegisterPentagon.lean'), (lv, 'Register4_channelInequality', 'RegisterPentagon.lean'),
                    (zp, 'zeroActingPairing_to_RH', 'ZeroActingPairing.lean')):
        k, st = blk(t, n, 8)
        L.append('    SIDE-lv-conservation %s:%s | %s' % (f, k, ' '.join(x.strip() for x in st)[:400]))
    sx = at('HEAD', 'SIDEExplicitFormula/LiWeil.lean')
    for n in ('rh_imp_li_nonneg', 'li_identity_of_exchange'):
        k, st = blk(sx, n, 8)
        L.append('### (%s) %s, SIDE-explicit-formula LiWeil.lean:%s:' % ('ii' if n.startswith('rh') else 'iii', n, k))
        L += ['    ' + x for x in st]
    para = ('The residue theorem’s premise `inequalityToPositivity : Register4_channelInequality lam_A lam_Z → Register4_positivity lam` '
            'maps the channel inequality (−λ_A(n) ≤ λ_Z(n) for n ≥ 1) to positivity (0 ≤ λ(n) for n ≥ 1) for sequences the theorem '
            'leaves arbitrary; it is arithmetic once λ = λ_A + λ_Z holds for the same sequences. Restated in SIDE-explicit-formula with '
            'λ := `LiCoeff`, the premise consumes the IDENTITY’S direction: it needs `LiCoeff n = λ_A(n) + λ_Z(n)` with λ_A and λ_Z '
            'the archimedean and finite-place channels, which is the Bombieri–Lagarias arithmetic formula -- `LiCoeff n` as the '
            'explicit formula’s value at the Bombieri–Lagarias family, `li_identity_of_exchange`’s conclusion once its exchange is '
            'discharged, the literature right-hand side split into its pole-and-Γ part and its prime part. It does not consume '
            '`rh_imp_li_nonneg`, which produces `Register4_positivity LiCoeff` FROM RH: the residue chain runs the other way, '
            'positivity → RH, through `liCriterion : Register4_positivity lam → RiemannHypothesis`, the converse direction (T1-lit, '
            '(V1)-(V4)). The restatement target is therefore the identity at the midpoint-normalised jump ((X1) or (X2) of relay '
            '`data/b561_decay_read.txt`), with λ_A and λ_Z named as `literatureRHS`’s parts at the family; not attempted.')
    L += ['', '### THE READ, ONE PARAGRAPH:', '    ' + para]
    put_txt('b561_consumer.txt', L)
    o = append_to(OT, NL + CONSUMER_H + ' ' + para + ' (relay `data/b561_consumer.txt`.)' + NL)
    o['line'] = line_of(OT, CONSUMER_H)
    put_json('b561_consumer.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)



# ------------------------------------------------------------------------------ the kernel state, the scores, the desk
PRE_HEADS = dict(Q.PRE_HEADS, **{'SIDE-explicit-formula': '941503b', 'SIDE-global-section': 'f8b8a1e'})
NEW_FILES = ['AxiomCheckLiWeilExchange.lean', 'SIDEExplicitFormula/LiWeilExchange.lean']
w_ = Q.w_


def mains():
    return {k: sorted(x for x in g(os.path.join(Q.DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def kstate():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    ns = [x for x in g(EF, 'diff', '--name-status', V04, 'main').split(NL) if x.strip()]
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls,
                v05=g(EF, 'rev-parse', 'v0.5^{}').strip(), v05obj=g(EF, 'rev-parse', 'v0.5').strip(),
                v05type=g(EF, 'cat-file', '-t', 'v0.5').strip(),
                br=g(EF, 'rev-parse', BR).strip(), br_parent=g(EF, 'rev-parse', BR + '^').strip(),
                held=g(EF, 'rev-parse', Q.HELD).strip(),
                old_local=g(EF, 'branch', '--list', OLD).strip(),
                status=sorted(set(x.split('\t')[0] for x in ns)), files=sorted(x.split('\t')[1] for x in ns),
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', V04, 'main']).returncode == 0)


def scores():
    dj, e0j = jl('b561_decay.json'), jl('b561_e0.json')
    d1, d2 = jl('b561_D1.json'), jl('b561_D2.json')
    k = kstate()
    push = rd(os.path.join(D, 'b561_push_test.txt'))
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if (x.startswith('b561_') or x == 'push_gated.sh') and needle in rd(os.path.join(T, x))]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(Q.P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    mm = {k2: [f for f in v if f.endswith('.lean')] for k2, v in mains().items()}
    other = {k2: v for k2, v in mm.items() if k2 != 'SIDE-explicit-formula'}
    held_ok = k['held'] == Q.HELD_TIP == k['remote'].get('refs/heads/' + Q.HELD)
    c3 = push[push.index('=== CASE 3'):push.index('=== CASE 4')] if '=== CASE 3' in push and '=== CASE 4' in push else ''
    order_ok = ('main read back at the remote' in c3 and 'peeled local' in c3
                and c3.index('main read back at the remote') < c3.index('peeled local'))
    cons = rd(os.path.join(D, 'b561_consumer.txt'))
    s = dict(
        h12a=(dj.get('h12a') == 'HOLDS'),
        h12b=False,
        h12c=False,
        n1=(dj.get('h12a') == 'HOLDS'),
        n2=(bool(d1.get('all_std3')) and bool(d2.get('all_std3')) and 'HELD -- THE EARLIEST OBSTACLE' in rd(os.path.join(D, 'b561_D3_D4.txt'))),
        n3=None,
        n4=("consumes the IDENTITY’S direction" in cons and 'It does not consume' in cons),
        n5=('CASE 1 ok' in push and 'CASE 2: DEFECT REPRODUCED' in push and 'TEST VERDICT : THE TAG PUSH DOES NOT RUN' in push),
        n6=(k['status'] == ['A'] and k['files'] == NEW_FILES and k['ff'] and all(v == [] for v in other.values()) and zen == [] and dep
            and trial['head'].startswith('f22ff35') and trial['status'] == '' and held_ok),
        s1=(dj.get('h12a') == 'REFUTED' and dj.get('uniform_order') == 'n/||rho||'),
        s2=(bool(d1.get('all_std3')) and d1.get('attempts', 99) <= 4),
        s3=order_ok,
        _detail=dict(kernel=k, mains=mm, zen=zen, dep=dep, trial=trial, held_ok=held_ok))
    return s


def desk():
    s = scores()
    d0 = s['_detail']
    k = d0['kernel']
    lines = ['=' * 104, 'b561 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
             '### (R171)(3)`S THREE.', '-' * 104,
             '  **(H12a)** ### **%s.** -- the decay read (data/b561_decay_read.txt (5), (8)): the uniform bound along the family is of order'
             ' n/‖ρ‖; a 1/‖ρ‖² bound needs δ <= C/‖ρ‖², a rate the family does not give. Illustration: sup ‖ρ‖|2 Re E| = %s.'
             % (w_(s['h12a']), jl('b561_decay.json').get('sup_values')),
             '  **(H12b)** ### **REFUTED.** -- by its own clause: the only dominant uniform along the family is of order n/‖ρ‖, which the'
             ' kernel`s count bound (zero_sum_inv_sq, exponent 2) does not make summable -- and (D3), its antecedent, does not exist.',
             '  **(H12c)** ### **REFUTED.** -- LiLimitExchange remains a hypothesis (and is expected false for n >= 1, the decay read`s (7));'
             ' li_identity_of_exchange stays INTERFACES; no sorryAx anywhere.', '',
             '### THE NAVIGATOR`S SIX.', '-' * 104,
             '  **(N1)** ### **%s.** -- H12a %s.' % (w_(s['n1']), w_(s['h12a'])),
             '  **(N2)** ### **%s.** -- (D1) %s, (D2) %s; (D3) HELD at the read; (D4) not reached.'
             % (w_(s['n2']), jl('b561_D1.json').get('all_std3'), jl('b561_D2.json').get('all_std3')),
             '  **(N3)** ### **NOT SCORABLE.** -- its antecedent (li_identity lands) is unreached.',
             '  **(N4)** ### **%s.** -- the consumer read: inequalityToPositivity consumes the identity`s direction; rh_imp_li_nonneg is'
             ' the opposite direction (data/b561_consumer.txt).' % w_(s['n4']),
             '  **(N5)** ### **%s.** -- the push test: CASE 1 (refused main push, exit 3, no tag at the remote), CASE 2 (b560`s chain, the'
             ' defect reproduced) (scratchpad push_test.sh, quoted in relay 46ced1ba).' % w_(s['n5']),
             '  **(N6)** ### **%s.** -- SIDE-explicit-formula main against 941503b: %s %s, a fast-forward %s ; .lean files changed on the'
             ' other mains %s ; detection-region-b559 at 8faf7de local and remote %s ; tools naming the platform %s ; deposit clean %s ;'
             ' trial %s.' % (w_(s['n6']), k['status'], k['files'], k['ff'], [x for x, v in d0['mains'].items() if v and x != 'SIDE-explicit-formula'] or 'NONE',
                           d0['held_ok'], d0['zen'] or 'NONE', d0['dep'], d0['trial']), '',
             '### THE SEAT`S THREE.', '-' * 104,
             '  **(S1)** ### **%s.** -- the decay read scored H12a %s, the uniform order %s.' % (w_(s['s1']), jl('b561_decay.json').get('h12a'),
                                                                                        jl('b561_decay.json').get('uniform_order')),
             '  **(S2)** ### **%s.** -- (D1) at the standard three at attempt %s.' % (w_(s['s2']), jl('b561_D1.json').get('attempts')),
             '  **(S3)** ### **%s.** -- CASE 3: main read back printed before the tag`s peeled read-back.' % w_(s['s3']), '',
             '### THE TAG.', '-' * 104,
             '  v0.5 %s object %s peeled %s (remote %s) ; main %s (remote %s) ; li-weil-b561 %s (remote %s) ; li-weil-b560 local [%s], remote [%s]'
             % (k['v05type'], k['v05obj'][:7], k['v05'][:7], k['remote'].get('refs/tags/v0.5^{}', '')[:7], k['main'][:7],
                k['remote'].get('refs/heads/main', '')[:7], k['br'][:7], k['remote'].get('refs/heads/' + BR, '')[:7], k['old_local'],
                k['remote'].get('refs/heads/' + OLD, '')), '']
    nav = [s[x] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')]
    seat = [s[x] for x in ('s1', 's2', 's3')]
    lines.append('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
                 % (nav.count(True), nav.count(False), nav.count(None), seat.count(True), seat.count(False)))
    lines.append('### ### **(R171)(3) : H12a %s ; H12b %s ; H12c %s.**' % tuple(w_(s[x]) for x in ('h12a', 'h12b', 'h12c')))
    d = rd(os.path.join(D, 'b561_defects.txt'))
    lines += ['', '### THIS ACT`S OWN DEFECTS.'] + d.rstrip().split(NL)
    put_txt('b561_desk_notes.txt', lines)
    put_json('b561_scores.json', {k2: v for k2, v in s.items() if not k2.startswith('_')})
    print(NL.join(lines[:34]))


# ------------------------------------------------------------------------------ READING (8): the entry, the row, the trail
FH = ('## The Li–Weil bridge at the limit exchange: the paired transform’s decay read, the exchange attempted, held at (D3) -- '
      'the transform identity compiled, the one-sided exchange derived false')
ROWNO = '396'
WO_LINE = ('*Appended 2026-09-29 by b561, under the author’s ruling `(R171)`(3), to the LI-WEIL-BRIDGE work-order (:3548; b560’s line '
           'at :11523) -- THE WORK-ORDER’S LINE UPDATED:*')
HEADING = ('### b561 — lane two, act three under (R171): the Li–Weil bridge at the limit exchange, held at (D3) at the decay read; the '
           'transform identity compiled (v0.5); b560 entered at its weight; the push discipline repaired; the consumer read')


def findings():
    guard_absent(FIND, FH)
    s = jl('b561_scores.json')
    k = kstate()
    wj, cj = jl('b561_weight.json'), jl('b561_consumer.json')
    t = ['', FH, '',
         '*Filed at b561 on the author’s ruling `(R171)`. Lane two, act three. Banks: relay `data/b561_decay_read.txt`, `data/b561_D1.txt`, '
         '`data/b561_D2.txt`, `data/b561_D3_D4.txt`, `data/b561_e0.txt`, `data/b561_consumer.txt`, `data/b561_v05_push.txt`; '
         'SIDE-explicit-formula v0.5 = `%s` (`SIDEExplicitFormula/LiWeilExchange.lean`). Nothing about ζ’s zeros is claimed beyond '
         'the compiled statements’ own words; a derivation on the page is labelled as one.*' % k['v05'][:7], '',
         '**What is compiled, 9 of 9 at the standard three.** (D1): `blTransform_holds` -- the transform of the Bombieri–Lagarias '
         'test function k_n(u) = 1_{u<0} e^{u/2} P_n(u) at γ_ρ is 1 − (1 − 1/ρ)ⁿ for Re ρ > 0, b560’s stated `blTransform` now '
         'proved, through `integral_pow_mul_cexp` (∫_{x>0} xʲ e^{−ρx} dx = j!/ρ^{j+1}, the Gamma integral at a complex rate for '
         'natural exponents, by integration by parts on (0, ∞)) and `binomial_li`. (D2): `truncMember_transform_tendsto` -- along '
         'any family of bumps supported left of 0 tending to 1 on u < 0, each member’s transform at γ_ρ tends to k_n’s, zero by '
         'zero; nothing uniform over the zeros.', '',
         '**The decay read, a derivation.** At a member whose plateau ends a distance δ from 0, the excess of its transform over the '
         'jump’s is −nμδ + O(δ²(2ⁿ + n‖ρ‖)) for ‖ρ‖δ small -- real, and of one sign for every such zero (μ a constant of the bump’s '
         'profile, 1/2 for Mathlib’s). So the supremum along the family at a fixed zero is of order n/‖ρ‖, and a bound C/‖ρ‖² needs '
         'δ ≤ C/‖ρ‖², a rate no family gives at every zero at once. Against `zero_sum_inv_sq`’s exponent 2, and with Σ 1/‖ρ‖ '
         'divergent over the zeros (Riemann–von Mangoldt, not compiled), no dominant uniform along the family exists: (D3) is '
         'neither a pairing estimate nor a new summability lemma, and pairing doubles the excess rather than cancelling it. A '
         'numerical illustration at n = 1 gives sup ‖ρ‖|2 Re E| = 1.742, 1.766, 1.770 at γ = 14.1, 100, 1000. Read on EF_lit’s '
         'other side, the right edge enters only the Γ-integral and contributes −(n/2)·log(1/δ): along every family in its '
         'hypothesis the zero side tends to −∞ for n ≥ 1, so `LiLimitExchange n` as b560 stated it is, on this derivation, false '
         'for n ≥ 1. The one-sided smoothing moves the jump’s midpoint into u < 0. This rests on Stirling’s sharp asymptotic and '
         'the Riemann–von Mangoldt count, neither compiled here.', '',
         '**Where it stops, and the re-price.** HELD at (D3), at the read, before a line of it was written; (D4) not reached. '
         'H12a REFUTED, H12b REFUTED by its own clause, H12c REFUTED. The exchange is re-priced at (X1) the explicit formula on a '
         'class containing the jump normalised to its midpoint (the leading item at OPEN_TRAILS :11424, substance), (X2) a '
         'two-sided family with the limit read on EF_lit’s other side, (X3) `LiLimitExchange` restated for (X2); (D1) and (D2) '
         'stand on either family.', '',
         '**b560 at its weight.** Entered at FINDINGS :%s (the two-forms entry), :%s (the tier-law line: `rh_imp_li_nonneg` is '
         'T0), :%s (the field entry) and BALANCE_AND_POSITIVITY.md :%s: the Li form’s forward half compiled, the equivalence not.'
         % (wj['lines']['twoforms'], wj['lines']['tier'], wj['lines']['field'], wj['lines']['balpos']), '',
         '**The consumer read** (OPEN_TRAILS :%s): `inequalityToPositivity` consumes the identity’s direction, `LiCoeff n` as the '
         'explicit formula’s value split into λ_A and λ_Z, not `rh_imp_li_nonneg`; the residue chain’s last step is the converse.'
         % cj.get('line'), '',
         '**The push discipline.** `relay/tools/push_gated.sh` (committed alone): main pushed from a push-* branch and read back '
         'equal before any tag push, with pipefail; its test refused a main push and showed the tag not pushed, and reproduced '
         'b560’s defect on the old chain. v0.5 went out through it.', '',
         '**The scores.** H12a %s; H12b %s; H12c %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s.'
         % tuple(w_(s.get(x)) for x in ('h12a', 'h12b', 'h12c', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6')), '',
         '**Next** (`(R171)`(5)): W-ORD-GRH-WEIL. The bridge’s remaining items -- (X1)-(X3), (D5), (D6), the converse (V1)-(V4) -- '
         'return to the trails with their prices.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH or any zero of ζ '
         'beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH)
    put_json('b561_findings.json', o)
    print('  FINDINGS.md:%(heading_line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


ROW_NAMES = ['integral_pow_mul_cexp', 'binomial_li', 'blTransform_holds', 'truncMember_transform_tendsto']


def row():
    k = kstate()
    ej = jl('b561_e0.json')
    cells = [ROWNO,
             '**THE LI–WEIL BRIDGE AT THE LIMIT EXCHANGE, HELD AT (D3)** (b561, under (R171)). SIDE-explicit-formula v0.5 = %s '
             '(LiWeilExchange.lean): the transform of the Bombieri–Lagarias test function at γ_ρ is 1 − (1 − 1/ρ)ⁿ for Re ρ > 0 '
             '(blTransform, stated at v0.4, now proved), through the Gamma integral at a complex rate for natural exponents; the '
             'member transforms tend to it zero by zero. The exchange is not proved: the decay read finds no dominant uniform along '
             'the family (order n/‖ρ‖) and derives LiLimitExchange false for n ≥ 1 as stated. Nothing here proves RH.' % k['v05'][:7],
             '`SIDE-explicit-formula/SIDEExplicitFormula/LiWeilExchange.lean` (v0.5) : ' + ', '.join('`%s%s`' % (NSL, n) for n in ROW_NAMES),
             '%d of %d declarations: [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b561_e0.txt)'
             % (sum(1 for r in ej['rows'].values() if r['std3_or_fewer']), len(ej['rows'])),
             ' ; '.join('`%s` %s' % (n, ej['rows'][n]['grade']) for n in ROW_NAMES),
             'LANDED on main by fast-forward, v0.5 pushed after main read back (tools/push_gated.sh); HELD at (D3) at the read; '
             'LiLimitExchange stays a Prop, li_identity_of_exchange INTERFACES on it; h2 where the deposit left it; nothing deposits; '
             'nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-500:], r.stderr[-300:])
    put_json('b561_rows.json', dict(cells=cells, exit=r.returncode))


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b561_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROWNO)]
    out = RG.diff(recs, NL.join(rowtxt))
    L = ['b561 -- READING (6): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROW %s' % ROWNO, '',
         '### records: %d ; row found: %s' % (len(recs), bool(rowtxt))] + ['    ' + str(x) for x in out]
    put_txt('b561_rowgen.txt', L)
    print(NL.join(L))


def workorder():
    guard_absent(OT, WO_LINE)
    k = kstate()
    t = (NL + WO_LINE + ' of the truncation route (:11294-:11302) and b560’s (D1)-(D6), at SIDE-explicit-formula v0.5 = `%s` '
         '(`LiWeilExchange.lean`): **T1 / (D1) COMPILED** (`blTransform_holds`); **(D2) COMPILED** (`truncMember_transform_tendsto`, '
         'zero by zero); **(D3) HELD AT THE READ** -- no dominant uniform along the family exists (order n/‖ρ‖, relay '
         '`data/b561_decay_read.txt`); **(D4) NOT REACHED**; `LiLimitExchange` as stated derived false for n ≥ 1 (a derivation, '
         'not compiled). Re-priced: (X1) the explicit formula on a class containing the midpoint-normalised jump (:11424’s '
         'leading item), (X2) a two-sided family with the limit read on EF_lit’s other side ((D5) first), (X3) the exchange '
         'restated for (X2); (D5), (D6) and the converse (V1)-(V4) stand as priced. The bridge’s items return to the trails with '
         'these prices; the next act is W-ORD-GRH-WEIL (`(R171)`(5)).' % k['v05'][:7] + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, WO_LINE)
    put_json('b561_workorder.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def components():
    L = ['=' * 132, 'b561 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b561_reads.txt', 'b561_decay_read.txt', 'b561_D1.txt', 'b561_D2.txt', 'b561_D3_D4.txt', 'b561_e0.txt',
              'b561_v05_push.txt', 'b561_consumer.txt', 'b561_rowgen.txt', 'b561_branches.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b561_weight.json', 'lines'), ('b561_consumer.json', 'line'), ('b561_findings.json', 'heading_line'),
                   ('b561_rows.json', 'exit'), ('b561_workorder.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    L.append('### the push tool: relay %s' % g(ROOT, 'log', '-1', '--format=%h %s', '--', 'tools/push_gated.sh').strip()[:160])
    L.append('### the push test (scratchpad push_test_out.txt):')
    L += ['  ' + x for x in rd(os.path.join(D, 'b561_push_test.txt')).rstrip().split(NL)]
    put_txt('b561_components.txt', L)
    print('  written: b561_components.txt (%d lines)' % len(L))


def trail():
    guard_absent(OT, HEADING)
    s = jl('b561_scores.json')
    f, wj, cj, wo = jl('b561_findings.json'), jl('b561_weight.json'), jl('b561_consumer.json'), jl('b561_workorder.json')
    k = kstate()
    pt = g(ROOT, 'log', '-1', '--format=%h', '--', 'tools/push_gated.sh').strip()
    t = ['', HEADING, '',
         '**(R171) ratified.** (1) b560 entered at its weight. (2) The push discipline. (3) The bridge one more act at the limit exchange, '
         'held at the earliest obstacle, the decay read before the build. (4) The consumer read. (5) W-ORD-GRH-WEIL next, whatever the '
         'outcome. Two readings of the order’s words declared on the face: no standing push script existed, so `push_gated.sh` is new; '
         'FINDINGS :5601 is the field entry’s sources block, the line appended beneath the entry (:5575) and it.', '',
         '**Entered:** FINDINGS.md:%s (the two-forms line), :%s (the tier-law line), :%s (the field-entry line), :%s (the entry); '
         'BALANCE_AND_POSITIVITY.md:%s; OPEN_TRAILS.md:%s (the consumer read), :%s (the work-order’s line); SIDE-global-section '
         'CORRESPONDENCE.md row %s; SIDE-explicit-formula v0.5 = `%s`, the branch `li-weil-b561` pushed by name.'
         % (wj['lines']['twoforms'], wj['lines']['tier'], wj['lines']['field'], f.get('heading_line'), wj['lines']['balpos'],
            cj.get('line'), wo.get('line'), ROWNO, k['v05'][:7]), '',
         '**The push discipline:** relay `%s` (`tools/push_gated.sh`, its test quoted: a refused main push exits 3 with no tag at the '
         'remote; b560’s chain reproduces the leak); v0.5 pushed through it, main read back before the tag.' % pt, '',
         '**H12a %s · H12b %s · H12c %s.** The stop: (D3), at the decay read -- the uniform bound is of order n/‖ρ‖; `LiLimitExchange` '
         'derived false for n ≥ 1 as stated; re-priced (X1)-(X3).' % tuple(w_(s.get(x)) for x in ('h12a', 'h12b', 'h12c')), '',
         '**The kernel:** `LiWeilExchange.lean` (v0.5) and its axiom-check file, new files only; 9 declarations at the standard three, no '
         '`sorryAx`; `blTransform_holds` and `truncMember_transform_tendsto` DERIVES.', '',
         '**Next:** W-ORD-GRH-WEIL (`(R171)`(5)); the bridge’s remaining items return to the trails with their prices.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**One fast-forward onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** Nothing deposits; nothing at '
         'Zenodo written; no existing `.lean` file edited; no Zeta23 file edited; no monograph byte changed; no keystone body edited (one '
         'line appended beneath BALPOS :764); ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit left it; '
         'the four lists stay OPEN; nothing here is a statement about RH or any zero beyond the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b561_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        sys.exit('usage: b561_record.py <component>')
    fn()
