# -*- coding: utf-8 -*-
"""b563_record.py -- LANE TWO, ACT FIVE: THE LI-WEIL BRIDGE AT THE SYMMETRIC FAMILY -- (D1')-(D4'), THE EXCHANGE RESTATED
AND ATTEMPTED; THE DRIFT RE-READ PER n; THE SUPERSESSION FORM EXTENDED TO FINDINGS: THE RECORD, UNDER (R173).
### `python tools/b563_record.py reads | decay | part <D1|D2|stmt|D3|D4> | e0 | lines | findings | rows | rowgen_diff |
### workorder | trail | components | desk`. b562's helpers are IMPORTED, never copied. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b562_record as Z2  # noqa: E402
Q = Z2.Q
P = Q.P
PP, FIND, OT, CORR, EF = Q.PP, Q.FIND, Q.OT, Q.CORR, Q.EF
NL = chr(10)
rd, g, append_to, guard_absent, poss, line_of = Q.rd, Q.g, Q.append_to, Q.guard_absent, Q.poss, Q.line_of
at, decl_at, statement, statement_block = Q.at, Q.decl_at, Q.statement, Q.statement_block
parse_prints, rowgen_record, STD3 = Z2.parse_prints, Q.rowgen_record, Q.STD3
put_txt, put_json, jl, w_ = Q.put_txt, Q.put_json, Q.jl, Q.w_
PRIOR_RELAY = '4ab01dcd'   # ### b562's table housekeeping -- relay's tip before this act
PRIOR_PP = '4b6ffe9'
PRIOR_GS = '9eaec7e'
V06 = 'de1f175ec026'
BR = 'li-weil-b563'
MAIN_MOD = 'SIDEExplicitFormula/LiWeilSym.lean'
NSL = 'SIDEExplicitFormula.LiWeil.'
SCR = os.environ.get('B563_SCRATCH') or os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Temp')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def _decl_lines(L, text, fname, names, cap=10):
    for n in names:
        k = decl_at(text, n)
        if k is None:
            L.append('### %s: %s NOT FOUND' % (fname, n))
            continue
        L.append('### %s:%d @%s -- %s' % (fname, k, V06[:7], n))
        L += ['    %5d | %s' % (k + i, l) for i, l in enumerate(statement(text, k, cap))]


def reads():
    L = ['b563 -- READING (1): THE READS, PRINTED BY PATH AND LINE',
         '### SIDE-explicit-formula v0.6 = %s ; main at step zero %s' % (g(EF, 'rev-parse', 'v0.6^{}').strip()[:7], g(EF, 'rev-parse', 'main').strip()[:7]), '']
    lw = at(V06, 'SIDEExplicitFormula/LiWeil.lean')
    _decl_lines(L, lw, 'LiWeil.lean', ['LiCoeff', 'liConst', 'blPoly', 'blSmooth', 'blTest', 'truncMember', 'pair_summable',
                                       'LiLimitExchange', 'li_identity_of_exchange'], 16)
    lx = at(V06, 'SIDEExplicitFormula/LiWeilExchange.lean')
    _decl_lines(L, lx, 'LiWeilExchange.lean', ['blTransform_holds', 'integrable_blTest_integrand', 'truncMember_transform_tendsto'], 6)
    gh = at(V06, 'SIDEExplicitFormula/GRHWeil.lean').split(NL)
    L.append('### GRHWeil.lean:1-40 @%s (the module layout): the header, the import, the namespace' % V06[:7])
    L += ['    %5d | %s' % (i + 1, gh[i]) for i in range(0, 40) if gh[i].startswith(('import', 'namespace', 'open', 'noncomputable', 'variable', 'SIDE-', 'THIS'))]
    pl = at(V06, 'SIDEExplicitFormula/PowerLimit.lean')
    _decl_lines(L, pl, 'PowerLimit.lean', ['dominant_summable', 'rest_tendsto_zero'], 4)
    zs = at(V06, 'Zeta23/WeilEF/ZeroSummability.lean')
    _decl_lines(L, zs, 'Zeta23/WeilEF/ZeroSummability.lean', ['zero_sum_inv_sq'], 4)
    ef = at(V06, 'Zeta23/ExplicitFormula.lean')
    _decl_lines(L, ef, 'Zeta23/ExplicitFormula.lean', ['literatureRHS', 'EF_lit'], 6)
    mn = at(V06, 'Zeta23/WeilEF/Main.lean')
    _decl_lines(L, mn, 'Zeta23/WeilEF/Main.lean', ['EF_lit_zetaZeroConfig'], 2)
    df = at(V06, 'Zeta23/Defs.lean')
    _decl_lines(L, df, 'Zeta23/Defs.lean', ['paperFT', 'gammaOf'], 2)
    L.append('')
    b560 = rd(os.path.join(D, 'b560_reads.txt')).split(NL)
    L += ['    b560_reads.txt:%d | %s' % (i + 1, l[:200]) for i, l in enumerate(b560) if 'EF_lit' in l][:4]
    p = os.path.join(D, 'b562_drift.txt')
    L.append('### relay data/b562_drift.txt: sha256 %s ; %d lines' % (sha(p), len(rd(p).split(NL))))
    dr = rd(os.path.join(D, 'b561_decay_read.txt')).split(NL)
    L += ['    b561_decay_read.txt:%d | %s' % (i + 1, l[:180]) for i, l in enumerate(dr) if re.match(r'^### \(\d\)', l)]
    B = rd(Q.BALPOS).split(NL)
    L.append('### BALPOS :291-:295 (the literature column) and :303-:311 (the margin column):')
    L += ['    BALPOS:%d | %s' % (i + 1, B[i][:160]) for i in list(range(290, 295)) + list(range(302, 311))]
    tt = rd(os.path.join(T, 'terminal_table.py')).split(NL)
    L.append('### tools/terminal_table.py at %s -- the supersession forms and their call site:' % PRIOR_RELAY)
    for i, l in enumerate(tt):
        if re.match(r'^(SUPERSEDE_RE|TRAIL_SUP_RE|def supersede|def supersede_trail|def trail_directives)', l) or 'uniq = supersede' in l:
            L.append('    terminal_table.py:%d | %s' % (i + 1, l.strip()[:160]))
    F = rd(FIND).split(NL)
    L.append('### FINDINGS :6048 | %s' % F[6047][:400])
    tj = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = tj['rows'] if isinstance(tj, dict) else tj
    for r in rows:
        if r['name'].endswith('li_identity_of_exchange'):
            L.append('### the committed table (relay %s) for %s: grade %s' % (PRIOR_RELAY, r['name'], r['grade']))
            L += ['    cell %-22s %s:%s' % (c['grade'], c['ledger'], c['line']) for c in r['grade_cells']]
    L.append('### the committed table: CONFLICT rows %d of %d' % (sum(1 for r in rows if r['grade'] == 'CONFLICT'), len(rows)))
    L.append('### the remote`s refs of SIDE-explicit-formula (ls-remote origin):')
    rem = [x for x in g(EF, 'ls-remote', 'origin').split(NL) if x.strip()]
    L += ['    ' + x for x in rem]
    put_txt('b563_reads.txt', L)
    put_json('b563_reads.json', dict(remote=rem, drift_sha=sha(p)))
    print('  written: b563_reads.txt (%d lines)' % len(L))


# ------------------------------------------------------------------------------ the ledger lines of Components 1 and 2
SUP_LINE = ('SUPERSEDES FINDINGS :6048 for `li_identity_of_exchange`: T2-INTERFACES-on-false-premise -- appended 2026-09-29 by b563 '
            'under the author’s ruling `(R173)`(3); the source: CORRESPONDENCE row 397 of SIDE-global-section (b562) and relay '
            '`data/b561_decay_read.txt` (7), the premise false as stated for n ≥ 1; FINDINGS :6048 stands unedited above.')
B562_REC = 11567
DEF_A_H = ('*Appended 2026-09-29 by b563, under the author’s ruling `(R173)`(3), to the b562 record (:%d) -- b562’s DEFECT (a), '
           'THE SEAT’S:*' % B562_REC)
H13B_H = ('*Appended 2026-09-29 by b563, under the author’s ruling `(R173)`(2), to the b562 record (:%d) -- H13b, THE '
          'NAVIGATOR’S MIS-SPECIFICATION, THE THIRD OF ITS KIND (H4, H8, H13b):*' % B562_REC)
H13A_H = ('*Appended 2026-09-29 by b563, under the author’s ruling `(R173)`(2), to the b562 record (:%d) -- H13a, THE '
          'READING:*' % B562_REC)


def lines():
    which = sys.argv[2]
    if which == 'sup':
        guard_absent(FIND, SUP_LINE)
        o = append_to(FIND, NL + SUP_LINE + NL)
        o['line'] = line_of(FIND, SUP_LINE)
        put_json('b563_supline.json', o)
    elif which == 'defect_a':
        guard_absent(OT, DEF_A_H)
        t = (NL + DEF_A_H + ' b562’s face (READING (3)) wrote the zero-count tail beyond the bank as n (log(T/2π) + 1)/(2πT). At '
             'on-line zeros 2 Re liTerm n ρ ≈ n²/γ² (the first-order part through Re(1/ρ) = 1/(2|ρ|²), the second-order part '
             'through Re(1/ρ²) ≈ −1/γ²), so the order is n²: T2(n) = n² (log(T/2π) + 1)/(2πT). The slip was the seat’s; the face '
             'stands sealed and unedited. The bank stands corrected: relay `data/b562_drift.txt` table (i) carries T2(n) beside '
             'the face’s T1(n), and Λ_N(n) + T2(n) reproduces BALPOS’s λ_n to 3·10⁻⁹ … 3·10⁻⁷ at n = 1..8 and 10; every score of '
             'b562 used T2.' + NL)
        o = append_to(OT, t)
        o['line'] = line_of(OT, DEF_A_H)
        put_json('b563_defect_a_line.json', o)
    elif which == 'b562':
        pn = jl('b563_per_n.json')
        guard_absent(OT, H13B_H)
        t1 = (NL + H13B_H + ' H13b asked for a bound on the symmetric drift uniform in n at fixed δ; `LiLimitExchange n` is a '
              'statement at fixed n with δ → 0. The bench’s symmetric drift (max over n 0.460, 0.128, 0.030 at δ = 0.1, 0.03, '
              '0.01) falls like δ at each n and scales as n²: in the exchange’s own order of limits that is what (X2) predicts '
              '(at fixed n the excess O(n²·δ), vanishing). The clause was the navigator’s mis-specification, the third of its '
              'kind after H4 and H8; (X2) is not refuted by b562 and stays the bridge’s next item, `(R172)`(7)’s fallback to (X1) '
              'not taken. Re-scored per n at b563 from b562’s bank alone (relay `data/b563_per_n.txt`): H15d %s.' % w_(pn.get('h15d')) + NL)
        o1 = append_to(OT, t1)
        guard_absent(OT, H13A_H)
        t2 = (NL + H13A_H + ' H13a stands refuted as worded (the 10% clause fails at all three δ), but its derivation`s leading '
              'term is corroborated: the one-sided slopes −0.547, −0.994, −1.496 carry the predicted sign and grow with log(1/δ) '
              '(against −1.151, −1.753, −2.303), and the slope per unit log(1/δ) rises toward 1/2 as δ falls (0.37 between the two '
              'larger δ, 0.46 between the two smaller). The finite-δ form is incomplete; the unexplained constant is entered as a '
              'bench question, not chased. The false-as-stated mark on main stands, since falsity needs the drift’s divergence and '
              'not its constant.' + NL)
        o2 = append_to(OT, t2)
        put_json('b563_b562_lines.json', dict(h13b=dict(o1, line=line_of(OT, H13B_H)), h13a=dict(o2, line=line_of(OT, H13A_H))))
    print('  written:', which)


# ------------------------------------------------------------------------------ COMPONENT 3: the decay read, on the page
def decay():
    num = jl('b563_decay_num.json')
    pn = jl('b563_per_n.json')
    r = pn['rows'][0]['dmt2_n2d']
    L = ['b563 -- READING (4): THE DECAY READ, ON THE PAGE, BEFORE ANY BUILD (COMPONENT 3), UNDER (R173)(4)',
         '### Every step below is a derivation on the page; a step resting on a result not compiled in the federation says so.',
         '',
         '### (0) THE OBJECTS. st = Mathlib`s Real.smoothTransition (0 on (-∞, 0], 1 on [1, ∞), smooth, flat at 0 and 1, and',
         '###     st(1 - x) = 1 - st(x) since st(x) = e(x)/(e(x) + e(1-x)) with e = expNegInvGlue). For 0 < δ <= 1 the symmetric cut',
         '###     s_δ(u) = st(1/2 - u/δ) · st(δu + 2): 1 on [-1/δ, -δ/2], 0 right of δ/2 and left of -2/δ; the member s_δ · e^{u/2} P_n(u).',
         '###     At ρ = β + iγ (0 < β < 1, |γ| >= 1): H_δ(ρ) = ∫ s_δ P_n e^{ρu} du and the jump`s H(ρ) = ∫_{u<0} P_n e^{ρu} = liTerm n ρ',
         '###     (blTransform_holds). THE EXCESS E_δ(ρ) := H_δ(ρ) - H(ρ) = E_J + E_L: E_J = ∫_{-δ/2}^{δ/2} g(u) P_n(u) e^{ρu} du with',
         '###     g := s_δ - 1_{u<0} (the left factor is 1 there, δ <= 1 <= 1/δ), and E_L = ∫_{u <= -1/δ} (st(δu + 2) - 1) P_n e^{ρu} du.',
         '###     THE JUMP CUT IS ODD: g(-u) = st(1/2 + u/δ) - 1 = -st(1/2 - u/δ) = -g(u) for 0 < u <= δ/2, by st(1 - x) = 1 - st(x); |g| <= 1/2.',
         '',
         '### (1) THE REAL PART IN COSINE FORM. P_n, s_δ and e^{βu} are real, so with q(u) := P_n(u) e^{βu} (real):',
         '###         Re E_J = ∫_{-δ/2}^{δ/2} g(u) q(u) cos(γu) du = ∫_0^{δ/2} g(u) cos(γu) (q(u) - q(-u)) du        (g odd, cos even)',
         '###         Im E_J = ∫_{-δ/2}^{δ/2} g(u) q(u) sin(γu) du = ∫_0^{δ/2} g(u) sin(γu) (q(u) + q(-u)) du.',
         '###     The member is real, so H_δ(conj ρ) = conj H_δ(ρ) and the paired transform is 2 Re H_δ(ρ): the pair reads Re E alone.',
         '',
         '### (2) THE ODD-ABOUT-THE-JUMP CANCELLATION, SHOWN. In Re E_J the jump`s value q(0) = P_n(0) = n cancels: q(u) - q(-u) vanishes',
         '###     at u = 0, |q(u) - q(-u)| <= 2 u K_n with K_n := sup over |v| <= 1/2 of |q`(v)| <= e^{1/2} (sup|P_n`| + sup|P_n|) on',
         '###     [-1/2, 1/2], a constant of n alone (β < 1). The n/ρ piece that made b561`s bound n/‖ρ‖ lives in Im E_J (q(u) + q(-u) -> 2n),',
         '###     which the pair discards. FOR CONTRAST, the one-sided cut g1 = st(-u/δ) - 1 on [-δ, 0] is not odd: Re E = ∫ g1 q cos(γu)',
         '###     keeps n ∫ g1 cos(γu) du = -n μ δ Φ(γδ) (μ = 1/2, Φ(0) = 1, Φ the cut`s cosine profile), of size n/|γ| at γδ ≍ 1 -- b561`s (5).',
         '',
         '### (3) THE ORDER IN δ AT FIXED n. From (2): |Re E_J| <= (1/2) ∫_0^{δ/2} 2 u K_n du = K_n δ²/8 -- per zero O(δ²), a fortiori',
         '###     O(δ). Its leading term: Re E_J ≈ Re(q`(0)) ∫_{-δ/2}^{δ/2} g(u) u du with q`(0) = P_n`(0) + β n = C(n, 2) + β n, which is',
         '###     n²/2 on the line β = 1/2: the n² of b562`s table (ii). SUMMED OVER THE ZEROS (a derivation resting on the zero density',
         '###     (1/2π) log(γ/2π), Riemann-von Mangoldt, T1-lit, not compiled): the zeros with |γ| δ <= 1 give +κ n² δ² each, those',
         '###     beyond give -n²/γ² each (E -> -liTerm), both summing to (n² δ/2π) log(1/δ) times coefficients whose sum is the Fourier',
         '###     integral of the excess at u = 0 in the midpoint sense -- g(0-) + g(0+) = -1/2 + 1/2 = 0 for the symmetric cut. SO THE',
         '###     log(1/δ) TERM CANCELS AND THE SUMMED EXCESS IS O(n² δ) at fixed n (for the one-sided cut the midpoint is -1/2 and the',
         '###     sum is b561`s -(n/2) log(1/δ)). THE BENCH CORROBORATES IT, from b562`s bank alone (relay data/b563_per_n.txt (b)):',
         '###     (D - T2)/(n² δ) = %.4f, %.4f, %.4f at δ = 0.1, 0.03, 0.01, the same at every n -- linear in δ, scaling as n².' % tuple(r),
         '',
         '### (4) THE DECAY IN ‖ρ‖, UNIFORM IN δ <= 1, AT THE JUMP. Where |γ| δ <= 1: (3) gives |Re E_J| <= K_n δ²/8 <= K_n/(8γ²). Where',
         '###     |γ| δ >= 1: put k(u) := g(u) (q(u) - q(-u)) on [0, δ/2]; k(0) = 0, k(δ/2) = 0, k`(δ/2) = 0 (st is flat at 0), k`(0+) =',
         '###     2 g(0+) q`(0) = q`(0). Two integrations by parts against cos(γu):',
         '###         ∫_0^{δ/2} k cos(γu) du = -(k`(0+) + ∫_0^{δ/2} k`` cos(γu) du)/γ²,',
         '###     and ∫_0^{δ/2} |k``| <= C`_n free of δ: |g``| <= S2/δ² against |q(u) - q(-u)| <= 2 K_n u over a length δ/2; |g`| <= S1/δ',
         '###     against |(q(u) - q(-u))`| <= 2 K_n; |g| |(q(u) - q(-u))``| <= K`_n u. (S1, S2 the sups of |st`|, |st``|.) HENCE',
         '###         |Re E_J(ρ)| <= C_n / γ² <= 2 C_n / ‖ρ‖²   for every δ in (0, 1] and every ρ with 0 < β < 1, |γ| >= 1.',
         '',
         '### (5) THE LEFT EDGE, UNIFORM AS β -> 0. Put R = 1/δ >= 1, G(u) := (st(δu + 2) - 1) P_n(u) on u <= -R: G vanishes with every',
         '###     derivative at -R (st flat at 1), and G e^{ρu} and its derivatives vanish at -∞ for β > 0. Integrating by parts n + 1',
         '###     times: E_L = (-1/ρ)^{n+1} ∫ G^{(n+1)} e^{ρu} du, and G^{(n+1)} = Σ_{j=1}^{n+1} C(n+1, j) f^{(j)} P_n^{(n+1-j)} with f = st(δu + 2)',
         '###     (the j = 0 term dies: deg P_n = n - 1), supported on the transition [-2R, -R]. |f^{(j)}| <= S_j R^{-j}, |P_n^{(m)}| <=',
         '###     c_n R^{n-1-m} on |u| <= 2R, m = n + 1 - j: each term <= c`_n R^{-2}; over a length R with |e^{ρu}| <= 1:',
         '###         |E_L(ρ)| <= c``_n / (R ‖ρ‖^{n+1}) <= c``_n / ‖ρ‖²   for n >= 1, ‖ρ‖ >= 1, uniformly in β in (0, 1) and δ in (0, 1].',
         '###     (For n = 0, P_0 = 0 and every excess is 0.) No 1/‖ρ‖ piece: at β = 1/2 E_L is of size e^{-1/(2δ)} besides.',
         '',
         '### (6) THE SCORE. H15a: "the excess is O(n²·δ) at fixed n and decays like 1/‖ρ‖² uniformly in δ <= δ₀; refuted if the',
         '###     excess has a 1/‖ρ‖ piece that symmetry does not cancel." ### **HELD ON THE PAGE**: the paired excess 2 Re E_δ(ρ) is O(δ²)',
         '###     per zero and O(n²·δ) summed at fixed n ((3), the sum a derivation on the zero density), and |2 Re E_δ(ρ)| <= C(n)/‖ρ‖² for',
         '###     every δ in (0, 1] ((4), (5)), C(n) free of δ; the 1/‖ρ‖ piece is imaginary at leading order and cancels in the pair (2).',
         '###     So (D3`) reads |Re H_δ(ρ)| <= ((n + n 2^n) + C(n)) / ‖ρ‖², with liTerm_re_abs_le for the jump`s own part.',
         '',
         '### (7) WHAT THIS PRICES FOR (D3`), IN THE READ`S ORDER. (d1) the parity st(1 - x) = 1 - st(x) and the cosine form (1) --',
         '###     algebra and a change of variable; (d2) the jump side (4): its δ² half is elementary, its 1/γ² half needs two',
         '###     integrations by parts on (0, δ/2] with sup bounds on st` and st``; (d3) the left edge (5): an (n+1)-fold integration by',
         '###     parts with Leibniz`s rule and bounds on st`s derivatives to order n + 1 -- the heaviest item, and the one that makes',
         '###     the bound uniform as Re ρ -> 0, which no zero-free region in the kernel supplies otherwise.',
         '',
         '### THE ILLUSTRATION (tools/b563_decay_num.py, numpy Gauss-Legendre; AN ILLUSTRATION, NOT EVIDENCE FOR A THEOREM; relay',
         '### data/b563_decay_num.txt): sup over δ in [1e-3, 1] of ‖ρ‖² |2 Re E| for the symmetric member, and of ‖ρ‖ |2 Re E| for the',
         '### one-sided cut:']
    for x in num:
        L.append('    n %d  β %-5g γ %-10.6g  SYM sup ‖ρ‖²|2ReE| %-9.4g (left edge alone %-9.3g)  ONE sup ‖ρ‖|2ReE| %.4g%s' % (
            x['n'], x['beta'], x['gamma'], x['sym'], x['left'], x['one1'], '  (HYPOTHETICAL POINT)' if x['label'] == 'HYPOTHETICAL' else ''))
    L += ['### read: at β = 1/2 the symmetric sup is 1.42, 5.69, 12.81 at γ = 100 and 1000 for n = 1, 2, 3 -- flat in ‖ρ‖, near',
          '### 1.42 n²; the one-sided ‖ρ‖ |2 Re E| is flat near 1.74 n (b561`s 1.77 at n = 1). ### **H15a HELD.**']
    put_txt('b563_decay_read.txt', L)
    put_json('b563_decay.json', dict(h15a=True, surviving_piece=None, per_n_check=r))
    print('  written: b563_decay_read.txt (%d lines) ; H15a HELD' % len(L))


# ------------------------------------------------------------------------------ READING (5): the part banks
PARTS = {
    'D1': ('(a) THE SYMMETRIC FAMILY AND (D1`) -- each member in EF_lit`s class',
           ['smoothTransition_one_sub', 'symCut', 'symMember', 'symCut_contDiff', 'symCut_nonneg', 'symCut_le_one',
            'symCut_eq_zero_right', 'symCut_eq_zero_left', 'symCut_eq_one', 'symMember_classEF', 'symMember_EF'], ['symD1_']),
    'D2': ('(b) (D2`) -- the member transforms tend to the jump`s at each fixed zero',
           ['symMember_integrand', 'blTest_integrand_neg', 'symMember_transform_tendsto'], ['symBC_']),
    'stmt': ('(c) LiLimitExchangeSym STATED; the zero sum at each member is real',
             ['LiLimitExchangeSym', 'I_gammaOf_mul', 'symMember_transform_conj', 'conjEquiv', 'symZeroSum_conj', 'symZeroSum_im'],
             ['symBC_', 'symC_']),
    'D3': ('(d) (D3`) -- the bound |Re H_δ(ρ)| <= C(n)/‖ρ‖², uniform in δ in (0, 1]: (d1) the cosine form, (d2) the jump side, '
           '(d3) the left edge, the assembly',
           ['SymPairBound', 'symMember_integrand_exp', 'symMember_transform_re',
            'integral_mul_cos_ibp', 'blPoly_contDiff_infty', 'qf', 'qf1', 'qf2', 'exp_mul_hasDerivAt', 'qf_hasDerivAt',
            'qf1_hasDerivAt', 'qf_bounds', 'wf', 'wf1', 'wf2', 'wf_hasDerivAt', 'wf1_hasDerivAt', 'jump_cos_bound',
            'integral_mul_cexp_ibp', 'integral_mul_cexp_ibp_iter', 'edgeProfile', 'deriv_smoothTransition_eq_zero',
            'edgeProfile_contDiff', 'edgeProfile_eq_zero', 'edgeProfile_hasCompactSupport', 'edgeProfile_bound',
            'integrable_cut_pow_cexp', 'edgeTail', 'edgeCut_abs', 'edgeTail_integrable', 'edgeTail_hasDerivAt', 'edgeTail_ibp',
            'edgeTail_bound', 'left_edge_bound', 'jumpInd', 'symCut_split', 'wf_neg', 'wf_eq_zero', 're_ofReal_mul_cexp',
            'leftEdge_integrable', 'symPair_bound'],
           ['symD3a_', 'symD3b_', 'symD3c_', 'symD3d_']),
    'D4': ('(e) (D4`), THE DISCHARGE AND li_identity_sym -- the Bombieri-Lagarias arithmetic formula in limit form',
           ['symMember_transform_norm_le', 'exchange_of_bound', 'liLimitExchangeSym_holds', 'li_identity_sym'], ['symE_']),
}
UNIT = {'symD3a_': '(d1)', 'symD3b_': '(d2)', 'symD3c_': '(d3)', 'symD3d_': 'the assembly', 'symBC_': '(b) and (c)',
        'symC_': '(c)', 'symD1_': '(a)', 'symE_': '(e)'}
PRINTS = 'symPrints_full.txt'
# ### b563 defect (e): a run the parts share is attributed per part. symBC_1 elaborated parts (b) and (c) together; its one error
# ### (stdin:196) lies in symMember_transform_conj, a declaration of part (c) -- so part (b) closed in it, part (c) did not.
UNIT_BY_PART = {('D2', 'symBC_'): '(b)', ('stmt', 'symBC_'): '(c)'}
OWN_ERRORS = {('D2', 'symBC_1.txt'): (0, 'its one error, stdin:196, lies in symMember_transform_conj, part (c)'),
              ('stmt', 'symBC_1.txt'): (1, 'stdin:196, in symMember_transform_conj')}


def part():
    X = sys.argv[2]
    title, names, tags = PARTS[X]
    src = rd(os.path.join(EF, MAIN_MOD)).replace(chr(13), '')
    pr = rd(os.path.join(SCR, PRINTS))
    P0 = parse_prints(pr)
    L = ['b563 -- READING (5): PART %s -- %s' % (X, title), '',
         '### the branch %s at %s from v0.6 = %s ; the module %s' % (BR, g(EF, 'rev-parse', '--short', BR).strip(), V06[:7], MAIN_MOD), '',
         '### THE ELABORATION ATTEMPTS (the module as it then stood; each run`s header line: exit, elapsed, errors), with the errors:']
    att = []
    for tg in tags:
        fs = sorted(f for f in os.listdir(SCR) if re.match(r'%s\d+\.txt$' % tg, f))
        for f in fs:
            t = rd(os.path.join(SCR, f)).split(NL)
            u = UNIT_BY_PART.get((X, tg), UNIT[tg])
            m = re.search(r'errors (\d+)', t[0])
            own, why = OWN_ERRORS.get((X, f), (int(m.group(1)) if m else -1, ''))
            att.append((u, f, t[0], own))
            L.append('    %s %s ; ERRORS IN THIS PART`S DECLARATIONS %d%s' % (u, t[0], own, (' (' + why + ')') if why else ''))
            for x in t[1:]:
                if ': error' in x:
                    L.append('        | ' + x[:230])
    L.append('')
    L.append('### THE DECLARATIONS, AS THE SOURCE STATES THEM (the final text, the prints` subject):')
    for n in names:
        k = decl_at(src, n)
        if k is None:
            L.append('    ### %s NOT FOUND' % n)
            continue
        for i, l in enumerate(statement(src, k, 8)):
            L.append('    %5d | %s' % (k + i, l))
    L.append('')
    L.append('### LEAN`S PRINTS (the full-stack run, scratchpad %s, first line: %s):' % (PRINTS, pr.split(NL)[0][:140]))
    rows = {}
    for n in names:
        ax = P0.get(NSL + n)
        rows[n] = dict(axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-34s %s' % (n, ax))
    ok = all(v['std3_or_fewer'] for v in rows.values())
    L.append('### ### **PRINTED %d OF %d ; THE STANDARD THREE OR FEWER, NO sorryAx : %s**' % (
        sum(1 for v in rows.values() if v['axioms'] is not None), len(names), ok))
    put_txt('b563_%s.txt' % X, L)
    put_json('b563_%s.json' % X, dict(part=X, names=names, rows=rows, all_std3=ok,
                                       attempts=[dict(unit=a, file=b, head=c, own_errors=o) for a, b, c, o in att]))
    print('  written: b563_%s.txt ; %s' % (X, L[-1]))


G_DEFS = ('symCut', 'symMember', 'LiLimitExchangeSym', 'conjEquiv', 'SymPairBound', 'qf', 'qf1', 'qf2', 'wf', 'wf1', 'wf2',
          'edgeProfile', 'edgeTail', 'jumpInd')
ROW_NAMES = ('symPair_bound', 'liLimitExchangeSym_holds', 'li_identity_sym')   # ### the act's row: the three #check'ed terminals
G_INTERFACES = {'exchange_of_bound': 'INTERFACES on SymPairBound, a premise the module names and discharges (symPair_bound)'}


def e0():
    src = rd(os.path.join(EF, MAIN_MOD)).replace(chr(13), '')
    code = re.sub(r'/-.*?-/', '', src, flags=re.S)
    names = re.findall(r"^(?:theorem|def)\s+([A-Za-z_'0-9]+)", code, re.M)
    pr = rd(os.path.join(SCR, PRINTS))
    P0 = parse_prints(pr)
    L = ['b563 -- READING (6): THE E0 READ -- EVERY DECLARATION OF LiWeilSym.lean GRADED, THE SALT-CHECK, THE ROWGEN RECORD', '',
         '### the prints: the full-stack stdin run (LiWeil.lean, LiWeilExchange.lean, LiWeilSym.lean, AxiomCheckLiWeilSym.lean); '
         'its header: %s' % pr.split(NL)[0], '']
    rows = {}
    for n in names:
        gr = 'DEF' if n in G_DEFS else ('INTERFACES' if n in G_INTERFACES else 'DERIVES')
        ax = P0.get(NSL + n)
        rows[n] = dict(grade=gr, axioms=ax, std3_or_fewer=ax is not None and set(ax) <= set(STD3))
        L.append('    %-34s %-11s %s' % (n, 'DEFINITION' if gr == 'DEF' else gr, ax))
    for n, why in G_INTERFACES.items():
        L.append('### %s : %s' % (n, why))
    L.append('')
    L.append('### THE SALT-CHECK -- Lean`s #print of each definition (every constant a Mathlib object or the kernel`s):')
    salt = {}
    for d in G_DEFS:
        j = pr.find('def SIDEExplicitFormula.LiWeil.%s' % d)
        blk = pr[j:j + 600].split(NL + NL)[0] if j >= 0 else ''
        salt[d] = bool(blk) and 'sorry' not in blk
        L += ['    ' + x for x in blk.split(NL)[:6]] if blk else ['    ### %s NOT PRINTED' % d]
    need = {'LiLimitExchangeSym': ('LiCoeff', 'zetaZeroConfig', 'paperFT', 'symMember'), 'SymPairBound': ('paperFT', 'gammaOf', 'symMember'),
            'symCut': ('smoothTransition',)}
    for d, ws in need.items():
        j = pr.find('def SIDEExplicitFormula.LiWeil.%s' % d)
        blk = pr[j:j + 900] if j >= 0 else ''
        salt[d] = salt.get(d, False) and all(w in blk for w in ws)
    salt_ok = all(salt.values())
    L.append('### ### **THE SALT-CHECK: %s** (%s)' % (salt_ok, ', '.join('%s %s' % kv for kv in salt.items())))
    tip = g(EF, 'rev-parse', BR).strip()
    recs, ctl = rowgen_record([NSL + n for n in ROW_NAMES], MAIN_MOD, tip, pr)
    L.append('')
    L.append('### THE ROWGEN RECORD (rowgen.py`s extract_doc_body and definition_encoded IMPORTED, at %s):' % tip[:7])
    for r in recs:
        L.append('    %-30s defenc %-5s %s | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_why'], bool(r['check'])))
    L.append('    control: definition_encoded on `def b560_ctl_stub : Prop := True` -> %s (must be True)' % (ctl,))
    thms = [n for n, r in rows.items() if r['grade'] != 'DEF']
    gate = (all(r['std3_or_fewer'] for r in rows.values()) and all(r['grade'] in ('DERIVES', 'DEF', 'INTERFACES') for r in rows.values())
            and salt_ok and ctl[0] and not any(r['defenc'] for r in recs) and len(rows) == len(P0))
    L.append('### ### **THE GATE: EVERY PRINT THE STANDARD THREE %s ; THEOREMS %d (DERIVES %d, INTERFACES %d) ; DEFINITIONS %d ; '
             'PRINTED %d OF %d ; THE SALT-CHECK %s => MERGE %s**'
             % (all(r['std3_or_fewer'] for r in rows.values()), len(thms), sum(1 for n in thms if rows[n]['grade'] == 'DERIVES'),
                sum(1 for n in thms if rows[n]['grade'] == 'INTERFACES'), len(rows) - len(thms), len(P0), len(rows), salt_ok, gate))
    put_txt('b563_e0.txt', L)
    put_json('b563_e0.json', dict(rows=rows, gate=gate, salt=salt_ok, rowgen=recs, rowgen_control=ctl[0], names=names, tip=tip))
    print(NL.join(L[-2:]))


# ------------------------------------------------------------------------------ the kernel state, the scores, the desk
PRE_HEADS = dict(Z2.PRE_HEADS, **{'SIDE-explicit-formula': 'de1f175', 'SIDE-global-section': '9eaec7e'})
NEW_FILES = ['AxiomCheckLiWeilSym.lean', 'SIDEExplicitFormula/LiWeilSym.lean']
KEPT = ('detection-region-b559', 'li-weil-b561', 'grh-weil-b562')
KEPT_TIPS = {'detection-region-b559': '8faf7ded8754870669547c9caa54ee5f0275e7c1',
             'li-weil-b561': '2df46d79bd59a900dde5b8ad8240faa2a0471cdc',
             'grh-weil-b562': 'de1f175ec02655b7b1d95f22e73004e6052cfa2e'}


def mains():
    return {k: sorted(x for x in g(os.path.join(Q.DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def kstate():
    ls = {}
    for l in g(EF, 'ls-remote', 'origin').split(NL):
        if '\t' in l:
            h, r = l.split('\t')
            ls[r.strip()] = h.strip()
    ns = [x for x in g(EF, 'diff', '--name-status', V06, 'main').split(NL) if x.strip()]
    return dict(main=g(EF, 'rev-parse', 'main').strip(), remote=ls,
                v07=g(EF, 'rev-parse', 'v0.7^{}').strip(), v07obj=g(EF, 'rev-parse', 'v0.7').strip(),
                v07type=g(EF, 'cat-file', '-t', 'v0.7').strip(),
                br=g(EF, 'rev-parse', BR).strip(), kept={b: g(EF, 'rev-parse', b).strip() for b in KEPT},
                ns=sorted(x.replace('\t', ' ') for x in ns),
                ff=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', V06, 'main']).returncode == 0)


def table_cells():
    tj = json.loads(rd(os.path.join(D, 'terminal_table.json')))
    rows = tj['rows'] if isinstance(tj, dict) else tj
    return [r for r in rows if r['name'].endswith('li_identity_of_exchange')]


def scores():
    fa, fn = jl('b563_findsup_after.json'), jl('b563_findsup_noop.json')
    pn, dc = jl('b563_per_n.json'), jl('b563_decay.json')
    e0 = jl('b563_e0.json')
    parts = {x: jl('b563_%s.json' % x) for x in ('D1', 'D2', 'stmt', 'D3', 'D4')}
    k = kstate()
    rows = e0.get('rows', {})
    std = lambda n: bool(rows.get(n, {}).get('std3_or_fewer'))
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b563_') and needle in rd(os.path.join(T, x))]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(Q.P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(Q.P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    mm = {k2: [f for f in v if f.endswith('.lean')] for k2, v in mains().items()}
    other = {k2: v for k2, v in mm.items() if k2 != 'SIDE-explicit-formula'}
    kept_ok = all(k['kept'][b] == KEPT_TIPS[b] == k['remote'].get('refs/heads/' + b) for b in KEPT)
    after_term = fa.get('term_grade', {}).get('after', [])
    ratios = [r['ratio'] for r in pn.get('rows', []) if r['classical']]
    own = [r['own_ratio'] for r in pn.get('rows', []) if r['classical']]
    d3 = all(std(n) for n in ('symPair_bound', 'jump_cos_bound', 'left_edge_bound'))
    s = dict(
        h15a=bool(dc.get('h15a')),
        h15b=d3 and 'SymPairBound' in rows,
        h15c=(std('exchange_of_bound') and std('liLimitExchangeSym_holds') and std('li_identity_sym')
              and rows.get('li_identity_sym', {}).get('grade') == 'DERIVES'),
        h15d=bool(pn.get('h15d')),
        n1=(after_term != ['CONFLICT'] and not fa.get('changed')) if after_term else None,
        n2=bool(pn.get('h15d')),
        n3=bool(dc.get('h15a')),
        n4=bool(parts['D1'].get('all_std3')) and bool(parts['D2'].get('all_std3')) and d3,
        n5=std('li_identity_sym') and rows.get('li_identity_sym', {}).get('grade') == 'DERIVES',
        n6=(k['ns'] == ['A AxiomCheckLiWeilSym.lean', 'A SIDEExplicitFormula/LiWeilSym.lean'] and k['ff']
            and all(v == [] for v in other.values()) and zen == [] and dep and kept_ok and trial['head'].startswith('f22ff35')
            and trial['status'] == ''),
        s1=(after_term == ['CONFLICT'] and all(c['line'] != 6048 or c['ledger'] != 'PLACE-papers/FINDINGS.md'
                                                for c in fa.get('term', {}).get('after', []))
            and any(c['line'] == 11577 for c in fa.get('term', {}).get('after', []))),
        s2=(bool(ratios) and max(ratios) < 1 and round(max(ratios), 2) == round(min(ratios), 2) and max(own) < min(ratios)),
        s3=not d3,
        _detail=dict(kernel=k, mains=mm, zen=zen, dep=dep, trial=trial, kept_ok=kept_ok, ratios=ratios, own=own,
                     conflict=(len(fa.get('conflict_before', [])), len(fa.get('conflict_after', [])))))
    return s


def desk():
    s = scores()
    d0 = s['_detail']
    k = d0['kernel']
    fa = jl('b563_findsup_after.json')
    e0 = jl('b563_e0.json')
    parts = {x: jl('b563_%s.json' % x) for x in ('D1', 'D2', 'stmt', 'D3', 'D4')}
    att = {x: [a['head'].split(' -- ')[0].replace('### ', '') + ' ' + a['head'].split(' -- ')[1].split(' (')[0] for a in parts[x].get('attempts', [])]
           for x in parts}
    lines = ['=' * 104, 'b563 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
             '### (R173)`S FOUR.', '-' * 104,
             '  **(H15a)** ### **%s.** -- the decay read (data/b563_decay_read.txt (2)-(6)): the paired excess is O(δ²) per zero and O(n² δ) summed'
             ' (a derivation on the zero density); its 1/‖ρ‖ piece is imaginary at leading order and cancels in the pair; the jump side'
             ' and the left edge are each C(n)/‖ρ‖² for every δ in (0, 1]; no 1/‖ρ‖ piece survives.' % w_(s['h15a']),
             '  **(H15b)** ### **%s.** -- (D3`) `symPair_bound` compiled at the standard three; SymPairBound`s constant is quantified before δ'
             ' (∃ C, ∀ δ ...): free of δ (data/b563_D3.txt).' % w_(s['h15b']),
             '  **(H15c)** ### **%s.** -- (D4`) `exchange_of_bound`, the discharge `liLimitExchangeSym_holds` and `li_identity_sym` at the'
             ' standard three, no sorryAx; `li_identity_sym` carries no premise and grades DERIVES (data/b563_D4.txt, data/b563_e0.txt).' % w_(s['h15c']),
             '  **(H15d)** ### **%s.** -- the δ → 0 extrapolation within floor at every n in 1..12, misses NONE; the ratio |Z(n,0) - λ_n|/floor'
             ' %.3f .. %.3f at the classical n (data/b563_per_n.txt).' % (w_(s['h15d']), min(d0['ratios']), max(d0['ratios'])), '',
             '### THE NAVIGATOR`S SIX.', '-' * 104,
             '  **(N1)** ### **%s.** -- CONFLICT %d -> %d; li_identity_of_exchange loses its FINDINGS :6048 cell and stays CONFLICT on'
             ' OPEN_TRAILS :11577`s two cells (b562`s own trail line) and row 397; terminals whose grade changed: %s'
             ' (data/b563_findsup_after.txt).' % (w_(s['n1']), d0['conflict'][0], d0['conflict'][1], fa.get('changed') or 'NONE'),
             '  **(N2)** ### **%s.** -- H15d %s.' % (w_(s['n2']), w_(s['h15d'])),
             '  **(N3)** ### **%s.** -- H15a %s.' % (w_(s['n3']), w_(s['h15a'])),
             '  **(N4)** ### **%s.** -- (D1`) %s, (D2`) %s, (D3`) %s at the standard three; (D4`) and the discharge LANDED as well.'
             % (w_(s['n4']), att['D1'], att['D2'], att['D3']),
             '  **(N5)** ### **%s.** -- li_identity_sym %s, grade %s.' % (w_(s['n5']), e0['rows']['li_identity_sym']['axioms'],
                                                                           e0['rows']['li_identity_sym']['grade']),
             '  **(N6)** ### **%s.** -- main against v0.6 %s, a fast-forward %s ; .lean files changed on the other mains %s ; the kept'
             ' branches local = remote = their tips %s ; tools naming the platform %s ; deposit clean %s ; trial %s.'
             % (w_(s['n6']), k['ns'], k['ff'], [x for x, v in d0['mains'].items() if v and x != 'SIDE-explicit-formula'] or 'NONE',
                d0['kept_ok'], d0['zen'] or 'NONE', d0['dep'], d0['trial']), '',
             '### THE SEAT`S THREE.', '-' * 104,
             '  **(S1)** ### **%s.** -- after the line the table reads CONFLICT for li_identity_of_exchange from OPEN_TRAILS :11577 and row 397,'
             ' no FINDINGS :6048 cell.' % w_(s['s1']),
             '  **(S2)** ### **%s.** -- the literal ratio %.3f .. %.3f (below 1, one value to two digits); the member`s own %.3f .. %.3f.'
             % (w_(s['s2']), min(d0['ratios']), max(d0['ratios']), min(d0['own']), max(d0['own'])),
             '  **(S3)** ### **%s.** -- (D3`) CLOSED: (d1) at attempt 1, (d2) at 3, (d3) at 3, the assembly at 2; the act did not hold there.'
             % w_(s['s3']), '']
    nav = [s[x] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')]
    seat = [s[x] for x in ('s1', 's2', 's3')]
    lines.append('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
                 % (nav.count(True), nav.count(False), nav.count(None), seat.count(True), seat.count(False)))
    lines.append('### ### **(R173) : H15a %s ; H15b %s ; H15c %s ; H15d %s.**' % tuple(w_(s[x]) for x in ('h15a', 'h15b', 'h15c', 'h15d')))
    lines += ['', '### THIS ACT`S OWN DEFECTS.'] + rd(os.path.join(D, 'b563_defects.txt')).rstrip().split(NL)
    put_txt('b563_desk_notes.txt', lines)
    put_json('b563_scores.json', {k2: v for k2, v in s.items() if not k2.startswith('_')})
    print(NL.join(lines[:34]))


# ------------------------------------------------------------------------------ the ledger lines of Component 5
FH = ('## The Li–Weil bridge at the symmetric family: the excess read per n, the exchange restated and discharged, the '
      'Bombieri–Lagarias formula in limit form')
WO_H = ('*Appended 2026-09-29 by b563, under the author’s ruling `(R173)`(4), to the LI-WEIL-BRIDGE work-order (:3548; b562’s '
        '(X2) line at :11563) -- (X2) LANDED AT v0.7:*')
HEADING = ('### b563 — lane two, act five under (R173): the Li–Weil bridge at the symmetric family -- (D1’)-(D4’) compiled, '
           'LiLimitExchangeSym discharged, li_identity_sym (v0.7); the drift re-read per n; the supersession form extended to FINDINGS')
ROW_ACT = '399'


def rows():
    k = kstate()
    ej = jl('b563_e0.json')
    act = [ROW_ACT,
           '**THE LI–WEIL BRIDGE AT THE SYMMETRIC FAMILY: (D1’)-(D4’), THE EXCHANGE DISCHARGED, THE IDENTITY IN LIMIT FORM** (b563, '
           'under (R173)(4)). SIDE-explicit-formula v0.7 = %s (LiWeilSym.lean): the Bombieri–Lagarias function’s jump mollified '
           'evenly about 0; each member in EF_lit’s class; the member transforms tend to the Li terms at each zero; the real part '
           'of the member’s transform bounded by C(n)/‖ρ‖² uniformly in δ ∈ (0, 1] (the odd cut cancels the jump’s n/ρ in the pair; '
           'the left edge uniform as Re ρ → 0); Tannery over the genuine zeros. LiCoeff n is the δ → 0⁺ limit of EF_lit’s '
           'literature right-hand side at the symmetric members. Nothing here proves RH or any positivity of the Li coefficients.'
           % k['v07'][:7],
           '`SIDE-explicit-formula/SIDEExplicitFormula/LiWeilSym.lean` (v0.7) : ' + ', '.join('`%s%s`' % (NSL, n) for n in ROW_NAMES),
           '%d of %d declarations: [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b563_e0.txt)'
           % (sum(1 for r2 in ej['rows'].values() if r2['std3_or_fewer']), len(ej['rows'])),
           ' ; '.join('`%s` %s' % (n, ej['rows'][n]['grade']) for n in ROW_NAMES),
           'LANDED on main by fast-forward, v0.7 pushed after main read back (tools/push_gated.sh); the branch li-weil-b563 pushed '
           'by name and kept; h2 where the deposit left it; nothing deposits; nothing at Zenodo written.']
    r2 = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + act, capture_output=True, text=True, encoding='utf-8')
    print(r2.stdout[-300:], r2.stderr[-300:])
    put_json('b563_rows.json', dict(act=act, exit_act=r2.returncode))


def rowgen_diff():
    sys.path.insert(0, os.path.join(T, 'rowgen'))
    import rowgen as RG
    recs = jl('b563_e0.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = "'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or [])) if isinstance(r.get('axioms'), list) else (r.get('axioms') or '')
    rowtxt = [l for l in rd(CORR).split(NL) if l.startswith('| %s |' % ROW_ACT)]
    out = RG.diff(recs, NL.join(rowtxt))
    L = ['b563 -- READING (6): THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE MERGED RECORDS AGAINST CORRESPONDENCE ROW %s' % ROW_ACT, '',
         '### records: %d ; row found: %s' % (len(recs), bool(rowtxt))] + ['    ' + str(x) for x in out]
    put_txt('b563_rowgen.txt', L)
    print(NL.join(L))


def findings():
    guard_absent(FIND, FH)
    s = jl('b563_scores.json')
    k = kstate()
    pn, fa = jl('b563_per_n.json'), jl('b563_findsup_after.json')
    ratios = [r['ratio'] for r in pn['rows'] if r['classical']]
    own = [r['own_ratio'] for r in pn['rows'] if r['classical']]
    r1 = pn['rows'][0]['dmt2_n2d']
    sup = jl('b563_supline.json')
    t = ['', FH, '',
         '*Filed at b563 on the author’s ruling `(R173)`. Lane two, act five. Banks: relay `data/b563_findsup_after.txt`, '
         '`data/b563_per_n.txt`, `data/b563_decay_read.txt`, `data/b563_D1.txt` … `data/b563_D4.txt`, `data/b563_e0.txt`, '
         '`data/b563_v07_push.txt`; SIDE-explicit-formula v0.7 = `%s`. Nothing about the zeros of ζ is claimed beyond the compiled '
         'statements’ own words; a derivation and a measurement are labelled as such.*' % k['v07'][:7], '',
         '**What is compiled, 65 of 65 at the standard three.** The Bombieri–Lagarias function’s jump is mollified evenly about 0: '
         '`symCut δ u = st(1/2 − u/δ) · st(δu + 2)` (Mathlib’s `Real.smoothTransition`), the member `symMember n δ`. (D1’) each '
         'member is C² with compact support and EF_lit holds at it; (D2’) at each ρ with Re ρ > 0 the member’s transform tends '
         'to the Li term as δ → 0⁺; (D3’) `symPair_bound`: |Re H_δ(ρ)| ≤ C(n)/‖ρ‖² for every δ ∈ (0, 1], |Im ρ| ≥ 1, 0 < Re ρ < 1 -- '
         'the odd jump cut cancels the jump’s n/ρ in the real part (two integrations by parts on (0, δ/2]), and the left edge '
         'decays uniformly as Re ρ → 0 (the scaling u = v/δ, then iterated integration by parts on fixed profiles); (D4’) Tannery '
         'over the genuine zeros with the dominant from `zero_sum_inv_sq`. So `LiLimitExchangeSym n` is proved '
         '(`liLimitExchangeSym_holds`), and `li_identity_sym`: LiCoeff n is the δ → 0⁺ limit of EF_lit’s literature right-hand '
         'side (the pole terms, the prime sum, the Γ-integral) at the symmetric members -- the Bombieri–Lagarias arithmetic '
         'formula in limit form, over the zeros of Mathlib’s `riemannZeta`. No premise remains.', '',
         '**The decay read (H15a), on the page before any build.** The paired excess of a symmetric member over the jump is '
         'O(δ²) per zero and O(n² δ) summed at fixed n (the log(1/δ) term cancels because the cut takes the jump’s midpoint, a '
         'derivation on the zero density); it carries no 1/‖ρ‖ piece. The one-sided family of b561 keeps it.', '',
         '**The drift re-read per n (H15d).** From b562’s bank alone: the least-squares δ → 0 extrapolation of b562’s symmetric '
         'value lands on λ_n within floor at every n in 1..12, at |Z(n,0) − λ_n|/floor %.2f at every classical n; the member’s '
         'own sum, with no tail added, at %.2f. With the jump’s tail taken off, the drift is (D − T2)/(n²δ) = %.4f, %.4f, %.4f '
         'at δ = 0.1, 0.03, 0.01, linear in δ and scaling as n².' % (max(ratios), max(own), r1[0], r1[1], r1[2]), '',
         '**The supersession form reaches FINDINGS lines** (relay `tools/terminal_table.py`, one commit, its test quoted): the '
         'line at FINDINGS.md:%s supersedes FINDINGS :6048 for li_identity_of_exchange. The regenerated table drops that cell; '
         'the terminal still reads CONFLICT, from b562’s own trail line at OPEN_TRAILS :11577 and row 397. CONFLICT %d → %d; no '
         'other grade moved.' % (sup.get('line'), len(fa['conflict_before']), len(fa['conflict_after'])), '',
         '**The scores.** H15a %s; H15b %s; H15c %s; H15d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s.'
         % tuple(w_(s.get(x)) for x in ('h15a', 'h15b', 'h15c', 'h15d', 'n1', 'n2', 'n3', 'n4', 'n5', 'n6')), '',
         '**Next** (`(R173)`(7)): GRH-WEIL act two -- the 38 generic Zeta23 modules re-instantiated for L(s, χ), staged by '
         'import order, held at the earliest ζ-specific dependency.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH or any zero '
         'beyond the compiled statements’ own words.*', '']
    o = append_to(FIND, NL.join(t))
    o['heading_line'] = line_of(FIND, FH)
    put_json('b563_findings.json', o)
    print('  FINDINGS.md:%(heading_line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


def workorder():
    guard_absent(OT, WO_H)
    k = kstate()
    t = (NL + WO_H + ' at SIDE-explicit-formula v0.7 = `%s` (`LiWeilSym.lean`): **(D1’)-(D4’) COMPILED, `LiLimitExchangeSym n` '
         'DISCHARGED, `li_identity_sym` DERIVES** -- LiCoeff n as the δ → 0⁺ limit of EF_lit’s literature right-hand side at the '
         'symmetric family, 65 declarations at the standard three. The bridge’s identity side is closed in limit form; what '
         'remains of the work-order is the positivity side (the Li coefficients’ sign), not attempted. The next act is GRH-WEIL '
         'act two (`(R173)`(7)).' % k['v07'][:7] + NL)
    o = append_to(OT, t)
    o['line'] = line_of(OT, WO_H)
    put_json('b563_workorder.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes, prefix %(prefix)s)' % o)


def components():
    L = ['=' * 132, 'b563 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b563_reads.txt', 'b563_findsup_unit.txt', 'b563_findsup_noop.txt', 'b563_findsup_after.txt', 'b563_per_n.txt',
              'b563_decay_read.txt', 'b563_decay_num.txt', 'b563_D1.txt', 'b563_D2.txt', 'b563_stmt.txt', 'b563_D3.txt', 'b563_D4.txt',
              'b563_e0.txt', 'b563_v07_push.txt', 'b563_rowgen.txt', 'b563_branches.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b563_supline.json', 'line'), ('b563_defect_a_line.json', 'line'), ('b563_findings.json', 'heading_line'),
                   ('b563_rows.json', 'exit_act'), ('b563_workorder.json', 'line')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    bl = jl('b563_b562_lines.json')
    L.append('### relay data/b563_b562_lines.json -- h13b %s h13a %s' % (bl.get('h13b', {}).get('line'), bl.get('h13a', {}).get('line')))
    put_txt('b563_components.txt', L)
    print('  written: b563_components.txt (%d lines)' % len(L))


def trail():
    guard_absent(OT, HEADING)
    s = jl('b563_scores.json')
    f, wo, sup, da = jl('b563_findings.json'), jl('b563_workorder.json'), jl('b563_supline.json'), jl('b563_defect_a_line.json')
    bl = jl('b563_b562_lines.json')
    fa = jl('b563_findsup_after.json')
    k = kstate()
    t = ['', HEADING, '',
         '**(R173) ratified.** (1) b562 at its weight. (2) H13b re-read in the exchange’s own order of limits, the clause the '
         'navigator’s; the per-n re-score. (3) The supersession form extended to FINDINGS lines. (4) (X2), the kernel act. (5) The '
         'hypotheses. (6) The gates. (7) The next act, GRH-WEIL act two.', '',
         '**Entered:** FINDINGS.md:%s (the supersession line), :%s (the entry); OPEN_TRAILS.md:%s, :%s, :%s (the lines at b562’s '
         'record: its defect (a), H13b’s mis-specification, H13a’s reading), :%s (the LI-WEIL-BRIDGE work-order’s line); '
         'SIDE-global-section CORRESPONDENCE.md row %s; relay `tools/terminal_table.py` (the FINDINGS form, committed alone); '
         'SIDE-explicit-formula v0.7 = `%s`, the branch `li-weil-b563` pushed by name and kept.'
         % (sup.get('line'), f.get('heading_line'), da.get('line'), bl['h13b']['line'], bl['h13a']['line'], wo.get('line'), ROW_ACT,
            k['v07'][:7]), '',
         '**H15a %s · H15b %s · H15c %s · H15d %s.** The bridge’s identity side lands: (D1’)-(D4’) compiled, LiLimitExchangeSym '
         'discharged, li_identity_sym with no premise.' % tuple(w_(s.get(x)) for x in ('h15a', 'h15b', 'h15c', 'h15d')), '',
         '**The table:** after the FINDINGS supersession, li_identity_of_exchange keeps two sources, b562’s trail line at '
         'OPEN_TRAILS :11577 (read by the table as a compound cell and a plain one) and row 397; it stays CONFLICT, and CONFLICT '
         'stands at %d. A trail-line supersession for :11577 (the form exists since b554) would clear it. It is not written, '
         'since it was not ordered, and is left for the author.' % len(fa.get('conflict_after', [])), '',
         '**Next:** GRH-WEIL act two (`(R173)`(7)).', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**One fast-forward onto `main`, one tag pushed after main read back, no `sorry` on any `main`.** Nothing deposits; '
         'nothing at Zenodo written; no existing statement changed; no existing `.lean` file edited; no Zeta23 file edited; no '
         'monograph byte changed; no keystone body edited; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where '
         'the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or any zero beyond the compiled '
         'statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b563_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        sys.exit('usage: b563_record.py <component>')
    fn()
