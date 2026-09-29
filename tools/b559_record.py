# -*- coding: utf-8 -*-
"""b559_record.py -- LANE TWO, ACT ONE: W-ORD-DETECTION-REGION -- THE FINITE FORM OF THE POWER-WINDOW ROUTE, STATED, BUILT
ON A BRANCH, GATED, AND MERGED OR HELD: THE RECORD, UNDER (R169).
### `python tools/b559_record.py reads | housekeeping | constants | literal | elab | axioms | e0 | price | reading | findings |
### row | components | desk | trail`
### The branch, its commit, push and read-back, the commits, pushes and branch commands of the ritual are the seat`s.
### This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, hashlib
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP = P.PP
FIND, OT = P.FIND, P.OT
CORR = P.CORR
EF = os.path.join(DD, 'SIDE-explicit-formula')
NL = chr(10)
rd, g, append_to, guard_absent, poss, outside_bt = P.rd, P.g, P.append_to, P.guard_absent, P.poss, P.outside_bt
PRIOR_RELAY = '22e5d2e4'   # ### b558`s closing -- relay`s tip before this act; the two housekeeping commits follow it
HK_REFRESH, HK_TOOL = '745d15da', '673a39e2'
PRIOR_PP = '5a911f4'       # ### b558`s PLACE-papers commit
V02 = '5c72cad24303f23d92256ebd466d3a3d32424a4b'
BRANCH = 'detection-region-b559'
NS = 'SIDEExplicitFormula.B321.'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def at(rev, rel, repo=EF):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, rel)], capture_output=True).stdout.decode('utf-8', 'replace').replace(chr(13), '')


def line_of(path, head):
    return P.line_of(path, head)


# ------------------------------------------------------------------------------ READING (1): the reads
CITES = [
    ('SIDEExplicitFormula/PowerWindow.lean', [(62, 'selfConv'), (94, 'selfConv_support'), (121, 'power (the j-fold iterated self-convolution)'),
                                               (129, 'power_support: support in [-(2^j L), 2^j L]'), (162, 'polyOp'),
                                               (274, 'base_nonzero_at'), (276, 'its witness L0 = 1 / (4 (|z| + 1))'), (328, 'offScore'),
                                               (331, 'off_finite_above'), (334, 'its height T = max 1 (B / c)'), (368, 'dominant_exists'),
                                               (377, 'the dominant by Set.exists_max_image'), (385, 'plateau_dominant'), (398, 'tieSet'),
                                               (401, 'killSet'), (427, 'real_even_interpolant'), (432, 'its witness CV'),
                                               (481, 'the ferry`s ":481" -- this line'), (483, 'rh_strip (the strip predicate: zetaZeroConfig.carrier)')]),
    ('SIDEExplicitFormula/PowerLimit.lean', [(245, 'PWSetup'), (251, 'PWSetup.hdom'), (271, 'Kp'), (274, 'cE'), (277, 'Ep'), (437, 'Xval'),
                                              (445, 'Nf'), (591, 'rT'), (658, 'fixed_poly_bound'), (667, 'its witness'), (672, 'coeffs_exist'),
                                              (683, 'its witnesses B and D'), (749, 'tie_term_neg'), (756, 'kill_term_zero'),
                                              (764, 'rest_term_small'), (800, 'Aw (the decay constant)'), (809, 'zero_weight'),
                                              (879, 'weighted_finite_bound'), (949, 'dominant_summable'), (957, 'its bound Bf'),
                                              (1025, 'rest_tendsto_zero'), (1057, 'the per-zero limit, no rate'),
                                              (1066, 'Tannery: tendsto_tsum_of_dominated_convergence'), (1082, 'zeroSide_eventually_neg'),
                                              (1092, 'the index J from Metric.tendsto_atTop'), (1159, 'zeroSideNeg (the assembly from :1159)'),
                                              (1176, 'plateau_dominant at the assembly'), (1193, 'h2_sign_imp_rh_strip'), (1248, 'the file`s end')]),
    ('SIDEExplicitFormula/DecayBound.lean', [(63, 'paperFT_decay'), (98, 'paperFT_decay_zero')]),
    ('SIDEExplicitFormula/H2Sign.lean', [(24, 'classK'), (29, 'h2_sign'), (30, 'its body'), (31, 'its sign')]),
    ('SIDEExplicitFormula/Seam.lean', [(101, 'h2_sign_iff_rh')]),
    ('SIDEExplicitFormula/B321Identity.lean', [(24, 'zeroSide')]),
    ('SIDEExplicitFormula/RestBound.lean', [(44, 'HCount'), (51, 'zeta3Sum')]),
    ('Zeta23/Defs.lean', [(121, 'gammaOf'), (124, 'reflect')]),
    ('Zeta23/RvM/LocalCount.lean', [(112, 'half_count_large'), (122, 'its witness A1'), (282, 'zeta_local_zero_count'),
                                    (285, 'K = Ncount (-4) 5'), (287, 'its witness A0'), (310, 'zetaZeroConfig_local_count')]),
    ('Zeta23/Statement.lean', [(54, 'IsNontrivialZero'), (105, 'zetaZeros: carrier')]),
    ('Zeta23/WeilEF/Main.lean', [(286, 'EF_lit_zetaZeroConfig')]),
]


def reads():
    L = ['b559 -- READING (1): THE READS, CITED BY PATH AND LINE AT SIDE-explicit-formula v0.2 = %s (made before the seal; the face`s (C))' % V02[:7], '']
    for rel, marks in CITES:
        t = at(V02, rel).split(NL)
        for n, what in marks:
            L.append('  %s:%-5d %-52s | %s' % (rel, n, what[:52], t[n - 1][:150] if n <= len(t) else '### BEYOND THE FILE'))
    L.append('')
    L.append('  toolchain and Mathlib rev of v0.2: lean-toolchain = %s ; lakefile.toml mathlib rev = %s' % (
        at(V02, 'lean-toolchain').strip(), re.search(r'rev = "([0-9a-f]+)"', at(V02, 'lakefile.toml')).group(1)))
    b551 = rd(os.path.join(D, 'b551_components.txt')).split(NL)
    L.append('  b551`s census, data/b551_components.txt:24 -- %s' % b551[23][:200])
    O = rd(OT).split(NL)
    for n, what in ((11151, 'the DETECTION-REGION entry (b547)'), (11332, 'b554`s re-price from the closed form'), (11423, 'the critical path`s row')):
        L.append('  OPEN_TRAILS.md:%d %s -- %s' % (n, what, O[n - 1][:220]))
    F = rd(FIND).split(NL)
    for n, what in ((57, 'the salt-check, instituted'), (3044, 'the E0 gate'), (5529, 'the detection-geometries entry'),
                    (5681, 'its correction (b550)'), (5754, 'its correction (b553)')):
        L.append('  FINDINGS.md:%d %s -- %s' % (n, what, F[n - 1][:220]))
    E = rd(os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')).split(NL)
    for n in (28, 37):
        L.append('  phase1.5/method/EXCLUSION_ENGINE.md:%d the salt-check`s rule text -- %s' % (n, E[n - 1][:220]))
    S = rd(os.path.join(D, 'b554_sign_pattern.txt')).split(NL)
    for n in range(78, 85):
        L.append('  data/b554_sign_pattern.txt:%d -- %s' % (n, S[n - 1]))
    put_txt('b559_reads.txt', L)
    print(NL.join(L[:6]))
    print('  written: b559_reads.txt (%d lines)' % len(L))


# ------------------------------------------------------------------------------ READING (2): the housekeeping
def housekeeping():
    R = ROOT
    L = ['b559 -- READING (2): THE HOUSEKEEPING, (R169)(1), DONE AT THE ACT`S START', '']
    for c, what in ((HK_REFRESH, '(a) b558`s refresh record committed alone'), (HK_TOOL, '(b) the instrument change committed alone')):
        files = [x for x in g(R, 'show', '--name-only', '--pretty=format:', c).split(NL) if x.strip()]
        L.append('### %s -- %s' % (what, c))
        L.append('    parent %s ; files %s' % (g(R, 'rev-parse', '--short', c + '^').strip(), files))
        L.append('    subject: %s' % g(R, 'log', '-1', '--pretty=%s', c).strip()[:300])
    L.append('')
    L.append('### (b) the message of %s, whole (the test quoted):' % HK_TOOL)
    L.extend('    ' + x for x in g(R, 'log', '-1', '--pretty=%B', HK_TOOL).rstrip().split(NL))
    L.append('')
    rr = rd(os.path.join(D, 'b559_b558_postpush_rerun.txt')).split(NL)
    L.append('### (b) the re-run on b558`s push, data/b559_b558_postpush_rerun.txt -- its reading line, the arm, and the verdict:')
    L.extend('    ' + x for x in rr if ('POST-PUSH READING' in x or 'G-PEEK-DECLARED' in x or 'ARMS RUN' in x or 'VERDICT :' in x
                                       or 'CONTROL FAILURES' in x or 'NOT RE-RUN' in x or 'content digests' in x))
    ok = any('LIVE PASSING : 63' in x for x in rr) and any('ALL ARMS PASS AND EVERY CONTROL BEHAVES' in x for x in rr)
    L.append('### ### **THE RE-RUN PRINTS 63 OF 63: %s**' % ok)
    put_txt('b559_housekeeping.txt', L)
    put_json('b559_housekeeping.json', dict(refresh=HK_REFRESH, tool=HK_TOOL, rerun_63=ok))
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (3): the constants
KINDS = ('EXPLICIT', 'EXISTENTIAL-WITH-WITNESS', 'NON-CONSTRUCTIVE')
MARKERS = ['Metric.tendsto_atTop', 'tendsto_tsum_of_dominated_convergence', 'Tendsto', 'exists_max_image', 'Classical.choose', 'choose ']
# (name, file, line, what the threshold or constant is, kind, witness, reach)
CONST = [
    ('zeroSide_eventually_neg', 'SIDEExplicitFormula/PowerLimit.lean', 1082,
     'the index j at which the zero side is negative: j = max J D (:1093, :1095)', 'NON-CONSTRUCTIVE',
     'J from `Metric.tendsto_atTop.mp (rest_tendsto_zero H Q B D hQb) _ hc0` (:1092) -- an existential out of a limit with no rate; D from coeffs_exist',
     'THE CONFIGURATION'),
    ('rest_tendsto_zero', 'SIDEExplicitFormula/PowerLimit.lean', 1025,
     'the rest over M^(2^(j+1)) tends to 0: a Tendsto, no index', 'NON-CONSTRUCTIVE',
     'per zero `tendsto_pow_atTop_nhds_zero_of_lt_one` on offScore/M < 1 (:1055-:1057), no uniform ratio; summed by `tendsto_tsum_of_dominated_convergence` (:1066) -- no rate',
     'THE CONFIGURATION'),
    ('tie_term_neg', 'SIDEExplicitFormula/PowerLimit.lean', 749,
     'the tie term`s real part, an equality at every j: -(N_rho M^(2^(j+1)))', 'EXPLICIT',
     'N_rho = Nf H rho = |K(v)^2 (1 - c^2 v)| (:445), K over the kill nodes (:271), c = cE over the tie set (:274); M the dominant score',
     'THE CONFIGURATION'),
    ('kill_term_zero', 'SIDEExplicitFormula/PowerLimit.lean', 756, 'the kill term is 0 at every j', 'EXPLICIT', 'K(v) = 0 (:369)', 'THE CONFIGURATION'),
    ('rest_term_small', 'SIDEExplicitFormula/PowerLimit.lean', 764,
     'each term bounded at every j: B^2 (1 + |w|)^(2D) offScore^(2^(j+1))', 'EXPLICIT',
     'the bound is a closed term in B, D (from coeffs_exist) and the zero`s own offScore and |w| = |gammaOf rho|', 'THE CONFIGURATION'),
    ('coeffs_exist', 'SIDEExplicitFormula/PowerLimit.lean', 672,
     'there are B, D bounding every P_j', 'EXISTENTIAL-WITH-WITNESS',
     'B = card(VF) * max CV 0 * BK * BE, D = 2 card(VF) + 2 DK + DE (:683); CV from real_even_interpolant over the tie nodes, BK, DK and BE, DE from fixed_poly_bound (:667) of Kp and Ep',
     'THE CONFIGURATION'),
    ('dominant_summable', 'SIDEExplicitFormula/PowerLimit.lean', 949,
     'the dominant is summable; its sum bounded by 3 A0 Bf zeta3Sum (weighted_finite_bound :879)', 'EXISTENTIAL-WITH-WITNESS',
     'Bf = 128 * 8^D * B^2 * (Aw H / M)^(2^(D+1)) (:957); A0 from zetaZeroConfig_local_count (:952)', 'THE CONFIGURATION'),
    ('Aw', 'SIDEExplicitFormula/PowerLimit.lean', 800,
     'the decay constant of the base: (INT |g0| + INT |g0````|) e^(L/2)', 'EXPLICIT', 'a closed term in the base window', '(gamma, delta) ALONE'),
    ('paperFT_decay', 'SIDEExplicitFormula/DecayBound.lean', 63,
     '|g^(z)| |z|^p <= (INT |g^(p)|) exp(L |Im z|)', 'EXPLICIT', 'a closed term in the window and z', '(gamma, delta) ALONE'),
    ('paperFT_decay_zero', 'SIDEExplicitFormula/DecayBound.lean', 98,
     '|g^(z)| <= (INT |g|) exp(L |Im z|)', 'EXPLICIT', 'a closed term in the window and z', '(gamma, delta) ALONE'),
    ('zetaZeroConfig_local_count', 'Zeta23/RvM/LocalCount.lean', 310,
     'N(t, t+1) <= A0 log(|t| + 3) with 1 <= A0', 'EXISTENTIAL-WITH-WITNESS',
     'A0 = max 1 (max (2 A1) K) (:287), K = Ncount (-4) 5 (:285), A1 = (1 / log(R/r)) (|log(3C)| + 2 max A 0) (:122) with r = 0.84, R = 0.95 and A, C from zeta_growth_right (ZetaGrowth.lean:159)',
     'ABSOLUTE (zeta alone)'),
    ('base_nonzero_at', 'SIDEExplicitFormula/PowerWindow.lean', 274,
     'a width below which the plateau`s transform is nonzero at z', 'EXISTENTIAL-WITH-WITNESS',
     'L0 = 1 / (4 (|z| + 1)) (:276); at the assembly z = gammaOf rho1, so the base half-support is 1 / (4 (|gammaOf rho1| + 1))',
     '(gamma, delta) ALONE'),
    ('plateau_dominant', 'SIDEExplicitFormula/PowerWindow.lean', 385,
     'the base width and a dominant off-line zero rho_s of the largest score M', 'EXISTENTIAL-WITH-WITNESS',
     'the width from base_nonzero_at at rho1 (:389); rho_s from dominant_exists (:394)', 'THE CONFIGURATION'),
    ('dominant_exists', 'SIDEExplicitFormula/PowerWindow.lean', 368,
     'an off-line zero of maximal score', 'EXISTENTIAL-WITH-WITNESS',
     'a maximiser by `Set.exists_max_image` over the finite set of off-line zeros scoring at least offScore(rho1) (:377): a zero of zeta, not a term in rho1',
     'THE CONFIGURATION'),
    ('off_finite_above', 'SIDEExplicitFormula/PowerWindow.lean', 331,
     'zeros of score at least c lie below height T', 'EXPLICIT', 'T = max 1 (B / c), B = (INT |g````|) e^(L/2) (:333-:334)', '(gamma, delta) ALONE'),
    ('real_even_interpolant', 'SIDEExplicitFormula/PowerWindow.lean', 427,
     'a coefficient bound for real interpolants on a node set', 'EXISTENTIAL-WITH-WITNESS',
     'CV = SUM_j SUM_i |(Lagrange.basis s id i).coeff j| (:432): a closed term in the nodes, the nodes being the tie set`s v', 'THE CONFIGURATION'),
]


def decl_span(text, name):
    """### the declaration`s head line and its body: from `theorem|def name` to the next top-level declaration."""
    t = text.split(NL)
    pat = re.compile(r'^(theorem|def|lemma|structure|noncomputable def) %s\b' % re.escape(name))
    i = next((k for k, l in enumerate(t) if pat.match(l)), None)
    if i is None:
        return None, '', ''
    j = next((k for k in range(i + 1, len(t)) if re.match(r'^(theorem|def|lemma|structure|open|/--|/-!|end |namespace|variable|@\[)', t[k])), len(t))
    body = NL.join(t[i:j])
    head = body.split(':=')[0].split(NL + '  |')[0]
    return i + 1, re.sub(r'\s+', ' ', head).strip(), body


def constants():
    rows, L = [], ['b559 -- READING (3): THE CONSTANTS, READ AT v0.2 = %s' % V02[:7], '',
                   '### KINDS: EXPLICIT (a closed term in the lemma`s inputs) ; EXISTENTIAL-WITH-WITNESS (an existential whose proof supplies',
                   '### the term, named) ; NON-CONSTRUCTIVE (a limit with no rate, or a choice with no bound in the lemma`s inputs). REACH:',
                   '### (gamma, delta) ALONE ; ABSOLUTE ; THE CONFIGURATION (a quantity of zeros of zeta other than the one excluded).',
                   '### MARKERS: a mechanical scan of each body at v0.2 for %s.' % ', '.join('`%s`' % m.strip() for m in MARKERS), '']
    for name, rel, line, what, kind, wit, reach in CONST:
        text = at(V02, rel)
        ln, head, body = decl_span(text, name)
        marks = [m.strip() for m in MARKERS if m in body]
        rows.append(dict(name=name, file=rel, line=line, found_line=ln, statement=head, what=what, kind=kind, witness=wit, reach=reach, markers=marks))
        L.append('### %s -- %s:%s%s' % (name, rel, ln, '' if ln == line else '  ### THE TABLE SAID :%d' % line))
        L.append('    statement : %s' % head[:600])
        L.append('    threshold : %s' % what)
        L.append('    kind      : %s' % kind)
        L.append('    witness   : %s' % wit)
        L.append('    reach     : %s' % reach)
        L.append('    markers   : %s' % (marks or 'none'))
        L.append('')
    nc = [r for r in rows if r['kind'] == 'NON-CONSTRUCTIVE']
    mark_ok = all(('Metric.tendsto_atTop' in r['markers'] or 'tendsto_tsum_of_dominated_convergence' in r['markers']) for r in nc)
    conf = [r['name'] for r in rows if r['reach'] == 'THE CONFIGURATION']
    L.append('### THE COUNTS: %s ; reach THE CONFIGURATION: %d of %d' % (
        ' ; '.join('%s %d' % (k, sum(1 for r in rows if r['kind'] == k)) for k in KINDS), len(conf), len(rows)))
    L.append('### the NON-CONSTRUCTIVE rows each carry a limit marker in their own body: %s' % mark_ok)
    L.append('')
    L.append('### ### **H9a IS REFUTED.** (R169)(4): "refuted if a threshold rests on a non-constructive step (a compactness or a limit')
    L.append('### with no rate) that yields no j0 without a new estimate." THE STEP, BY LINE: PowerLimit.lean:1092, `obtain <J, hJ> :=')
    L.append('### Metric.tendsto_atTop.mp (rest_tendsto_zero H Q B D hQb) _ hc0` -- the index is read off a limit; rest_tendsto_zero')
    L.append('### (:1025) is Tannery`s theorem (:1066) over per-zero limits (:1057) whose ratios offScore/M < 1 carry no uniform bound.')
    L.append('### AND BENEATH IT, THE REACH: the index depends on M (the dominant`s score, a maximiser over zeros of zeta, PowerWindow')
    L.append('### :377), on the tie and kill sets (Kp :271, cE :274, Nf :445), on CV over the tie nodes (PowerWindow :432), and on the')
    L.append('### largest ratio offScore/M outside those sets -- quantities of the zero configuration, not of (gamma, delta). So no')
    L.append('### j0 : R -> R -> N is written from these constants.')
    L.append('')
    L.append('### THE ESTIMATE THAT WOULD REPLACE IT, PRICED:')
    L.append('    (E1) a rate for the rest: with theta the largest offScore(x)/M over the zeros outside the tie and kill sets (a maximum')
    L.append('         over a finite set by off_finite_above, below 1), for j >= D the rest over M^(2^(j+1)) is at most')
    L.append('         theta^(2^(j+1) - 2^(D+1)) * 3 A0 Bf zeta3Sum; with fR_bound (:986) carrying the extra factor it gives an index')
    L.append('         explicit in (theta, the tie terms` N, B, D, A0, Aw, M) -- a CONFIGURATION-RELATIVE j0. One lemma, moderate.')
    L.append('    (E2) those constants bounded by (gamma, delta) alone: theta has no bound below 1 in terms of the excluded zero (two')
    L.append('         zeros of near-equal score); CV grows without bound as two tie nodes approach; N_rho tends to 0 as a tie node')
    L.append('         approaches a kill node (v = -gamma_k^2); the tie and kill sets are bounded in size by the count below height')
    L.append('         T(M) (explicit). E2 needs a lower bound on the separation of the zeros of zeta near the dominant`s score -- or a')
    L.append('         route that does not interpolate on nodes -- which no compiled lemma and no ZeroConfig field carries. Research')
    L.append('         grade; not one lemma. The closed-form route (b554, OPEN_TRAILS :11332, C1-C5) avoids the interpolation and is')
    L.append('         priced there at three of substance.')
    L.append('')
    L.append('### TWO READINGS OF (R169)(2) AGAINST THE KERNEL, PRINTED:')
    L.append('    the base window is not fixed: the route takes its half-support from the excluded zero, 1 / (4 (|gammaOf rho1| + 1))')
    L.append('    (PowerWindow :276 at :389), and PWSetup (:245-:251) carries the width L as a parameter, fixing none;')
    L.append('    the n-th window is not an n-fold power: `power g j` is the j-fold iterated SELF-convolution, the 2^j-fold power,')
    L.append('    with support in [-(2^j L), 2^j L] (PowerWindow :129-:130); kWindow at index j is weilTest of it, support in')
    L.append('    [-(2^(j+1) L), 2^(j+1) L] -- so the support at index j is 2^(j+1) * l, not j * l.')
    L.append('')
    L.append('### THE POSITIVE CONTROL OF THIS CLASSIFICATION: the same reading names witnesses where the proofs construct them --')
    L.append('    base_nonzero_at (:276), off_finite_above (:334), fixed_poly_bound (:667), coeffs_exist (:683), weighted_finite_bound')
    L.append('    and dominant_summable (:957), the local count (:287, :122) -- %d rows EXISTENTIAL-WITH-WITNESS and %d EXPLICIT; the'
             % (sum(1 for r in rows if r['kind'] == 'EXISTENTIAL-WITH-WITNESS'), sum(1 for r in rows if r['kind'] == 'EXPLICIT')))
    L.append('    NON-CONSTRUCTIVE word falls only where a limit marker stands in the body.')
    put_txt('b559_constants.txt', L)
    put_json('b559_constants.json', dict(rows=rows, h9a=False, step='SIDEExplicitFormula/PowerLimit.lean:1092',
                                         nonconstructive=[r['name'] for r in nc], markers_ok=mark_ok, configuration=conf))
    print(NL.join(L[-40:]))




# ------------------------------------------------------------------------------ READING (5): the literal probe
SCR = os.environ.get('B559_SCRATCH', '')


def literal():
    L = ['b559 -- READING (5): (R169)(3)`s h2_sign_upto TYPED AS THE RULING TYPES IT, FED ON STDIN WITH THE NEW MODULE`S HEADER IMPORT',
         '### `lake env lean --stdin` from the SIDE-explicit-formula checkout on detection-region-b559 (the narrow-import rule).',
         '### Variant (a): the ruling`s text inside the kernel`s namespace. Variant (b): the same with `open Zeta23.EF`, so that',
         '### `weilTest` resolves and what remains is the ruling`s own shape.', '']
    runs = {'a': (1, 799), 'b': (1, 22)}
    for v in ('a', 'b'):
        L.append('### variant (%s) -- the input:' % v)
        L.extend('    ' + x for x in rd(os.path.join(SCR, 'literal_%s.lean' % v)).rstrip().split(NL))
        L.append('### variant (%s) -- exit %d, %d s (the first load of the Mathlib objects took the time) -- Lean`s messages:' % ((v,) + runs[v]))
        L.extend('    ' + x for x in rd(os.path.join(SCR, 'literal_%s_out.txt' % v)).rstrip().split(NL))
        L.append('')
    L.append('### ### **THE LITERAL DOES NOT ELABORATE.** `h ∈ classK` asks for a `Membership` instance on `(ℝ → ℂ) → Prop`: `classK`')
    L.append('### is a predicate (H2Sign.lean:24), not a set. `weilTest` is `Zeta23.EF.weilTest`. And `0 ≤ weilTest h h` would compare a')
    L.append('### FUNCTION `ℝ → ℂ` with 0 pointwise -- not the sign `h2_sign` states (H2Sign.lean:29-31, `0 ≤ poleTerm k - primeSum k +')
    L.append('### archTerm k`). The module states the predicate as `h2_sign` states its sign, over `k` with `classK k` and a support bound.')
    put_txt('b559_literal.txt', L)
    put_json('b559_literal.json', dict(variants={v: dict(exit=runs[v][0], secs=runs[v][1],
                                                          errors=rd(os.path.join(SCR, 'literal_%s_out.txt' % v)).count(': error'))
                                                 for v in runs}))
    print(NL.join(L[-5:]))


# ------------------------------------------------------------------------------ the prints, read
def prints():
    t = rd(os.path.join(D, 'b559_axioms.txt'))
    out = {}
    for m in re.finditer(r"'SIDEExplicitFormula\.B321\.([^']+)' depends on axioms: \[([^\]]*)\]", t):
        out[m.group(1)] = [x.strip() for x in m.group(2).split(',') if x.strip()]
    return out


NEW = ['h2_sign_upto', 'h2_sign_upto_mono', 'h2_sign_imp_upto', 'upto_all_imp_h2_sign', 'h2_sign_iff_forall_upto', 'forall_upto_iff_rh',
       'ellOf', 'j₀', 'detection_region']
COMPILED = ['h2_sign_upto_mono', 'h2_sign_imp_upto', 'upto_all_imp_h2_sign', 'h2_sign_iff_forall_upto', 'forall_upto_iff_rh']
HELDN = ['j₀', 'detection_region']
STD3 = ['propext', 'Classical.choice', 'Quot.sound']


# ------------------------------------------------------------------------------ READING (6): the E0 read
def e0():
    pr = prints()
    ax = rd(os.path.join(D, 'b559_axioms.txt')).split(NL)
    st = NL.join(ax[ax.index(next(x for x in ax if x.startswith('SIDEExplicitFormula.B321.detection_region :'))):
                    ax.index(next(x for x in ax if x.startswith('def RiemannHypothesis')))])
    L = ['b559 -- READING (6): THE E0 READ OF THE STATED detection_region, AND THE GRADES OF THE COMPILED COMPANIONS', '',
         '### THE STATEMENT, AS LEAN PRINTS IT (data/b559_axioms.txt):']
    L.extend('    ' + x for x in st.split(NL))
    L += ['',
          '### EVERY CONSTITUENT UNFOLDED TO ITS OWNER:',
          '    the conclusion `ρ.re - 1 / 2 = 0` ........ Mathlib: `Complex.re`, subtraction and equality on `ℝ`',
          '    `riemannZeta ρ = 0`, `0 < ρ.re`, `ρ.re < 1` .. Mathlib: `riemannZeta`, `Complex.re`, the order on `ℝ` -- the kernel`s',
          '                                                  `Zeta23.IsNontrivialZero` (Statement.lean:54) unfolded',
          '    `h2_sign_upto L₀` (the hypothesis hL) ..... this module: over `classK` (H2Sign.lean:24 -- Mathlib`s `ContDiff`,',
          '                                                  `HasCompactSupport` and Zeta23`s `EF.weilTest`) and b321`s `poleTerm`, `primeSum`,',
          '                                                  `archTerm` (B321Identity.lean); it names no zero of zeta and no real part',
          '    `ellOf ρ` ................................ this module: `1 / (4 (‖Zeta23.gammaOf ρ‖ + 1))`, `gammaOf ρ = (ρ - 1/2) / I`',
          '                                                  (Defs.lean:121) -- Mathlib`s norm and division',
          '    `j₀ γ δ` ................................. this module: `sorry` -- UNOWNED; its value is `sorryAx``s',
          '',
          '### THE SALT-CHECK (EXCLUSION_ENGINE.md :28, :37; FINDINGS :57): no Prop of the module encodes the conclusion --',
          '### `h2_sign_upto`, `ellOf` and `j₀` name no real part of a zero; the conclusion stands in the theorem alone. The',
          '### statement`s FORM passes. ### Its region premise rests on `j₀`, whose body is `sorry`: until `j₀` is written the premise',
          '### has no fixed content, and the theorem`s own proof is `sorry`.',
          '### ### **THE GRADE ON THE BRANCH: T4 (a `sorry` body, the tier law`s bottom rung). NOT DERIVES. NO MERGE, NO TAG (R169)(5).**',
          '',
          '### THE COMPILED COMPANIONS, BY STATEMENT-READ (the three-grade vocabulary):']
    for n in COMPILED:
        L.append('    %-26s DERIVES -- prints %s' % (n, pr.get(n)))
    L += ['    `h2_sign_iff_forall_upto` is `h2_sign ↔ ∀ L₀, h2_sign_upto L₀`: its two sides are the kernel`s Prop and the finite form,',
          '    and the proof is the compact support of a classK window; `forall_upto_iff_rh` carries it to Mathlib`s `RiemannHypothesis`',
          '    through `h2_sign_iff_rh` (Seam.lean:101). Equivalences between open statements: neither is proved.',
          '',
          '### THE ROWGEN DIFF: NOT RUN -- it is the merge gate`s (R169)(5), and the branch is HELD.']
    grades = {n: 'DERIVES' for n in COMPILED}
    grades['detection_region'] = 'T4'
    put_txt('b559_e0.txt', L)
    put_json('b559_e0.json', dict(grade='T4', derives=False, grades=grades, prints=pr, statement=st))
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (7): the price corrected
PRICEH = ('*Appended 2026-09-29 by b559, under the author`s ruling `(R169)`(5), to the DETECTION-REGION entry at :11151 and b554`s '
          'price at :11332 -- THE PRICE CORRECTED BY THE MEASURED OBSTACLE:*')


def price():
    guard_absent(OT, PRICEH)
    s = (PRICEH + ' the explicit index j₀(γ, δ), priced at b554 as the one lemma of substance, is not one lemma by the PowerLimit '
         'route. `zeroSide_eventually_neg` takes its index from `Metric.tendsto_atTop` over a Tannery limit with no rate '
         '(SIDE-explicit-formula v0.2, `PowerLimit.lean`:1092, :1025, :1066), and the constants beneath it are quantities of the '
         'zero configuration -- the dominant score, the tie and kill sets, the interpolation bound over the tie nodes, the largest '
         'ratio off those sets -- not of (γ, δ). Priced: (E1) a rate given that ratio, one lemma of moderate weight, gives an index '
         'relative to the configuration; (E2) the configuration`s constants bounded by (γ, δ) alone needs a separation estimate for '
         'the zeros near the dominant score that no compiled lemma carries -- research grade, open. The closed-form route (:11332, '
         'C1-C5) stands beside it at three of substance. The statement is held on the branch `detection-region-b559` (8faf7de), '
         '`j₀` and `detection_region` with `sorry` bodies; the join `h2_sign ↔ ∀ L₀, h2_sign_upto L₀` compiled there at the '
         'standard three (relay `data/b559_constants.txt`, `data/b559_axioms.txt`).')
    o = append_to(OT, NL.join(['', s, '']))
    o['line'] = line_of(OT, PRICEH)
    put_json('b559_price.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


# ------------------------------------------------------------------------------ READINGS (8) and (9): the reading and the entry
FH = ('## The detection region: the finite form of the power-window route — h2_sign on windows of support at most L₀ against '
      'off-line zeros with j₀(γ, δ)·ℓ ≤ L₀ — stated and held at the named obstacle')


def bench():
    S = rd(os.path.join(D, 'b554_sign_pattern.txt')).split(NL)
    runs = [l.strip() for l in S[77:81]]
    nodes = {}
    for l in S:
        m = re.match(r'^\s+(\d+)\s+Z (\S+)\s+OFF (\S+)\s+ON (\S+)\s+pair (\S+)\s+29\.55 (\S+)', l)
        if m:
            nodes[int(m.group(1))] = dict(Z=float(m.group(2)), pair=float(m.group(5)), o2955=float(m.group(6)))
    return runs, nodes


def findings():
    guard_absent(FIND, FH)
    runs, nodes = bench()
    c = jl('b559_constants.json')
    pr = prints()
    t = [FH, '',
         '*Filed at b559 on the author`s ruling `(R169)`. Lane two, act one. Banks: relay `data/b559_constants.txt`, `data/b559_literal.txt`, '
         '`data/b559_axioms.txt`, `data/b559_e0.txt`, `data/b559_branch.txt`; the branch `detection-region-b559` of SIDE-explicit-formula at '
         '`8faf7de` (from v0.2 = `5c72cad`), pushed by name and HELD. Nothing about ζ’s zeros is claimed beyond the compiled statements’ own words.*', '',
         '**The hypotheses, scored.** H9a REFUTED: `zeroSide_eventually_neg` (PowerLimit.lean:1082) takes its index `max J D` from '
         '`Metric.tendsto_atTop` over `rest_tendsto_zero` (:1092), a Tannery limit (:1066) over per-zero limits with no rate (:1057), and '
         'the constants beneath it reach THE CONFIGURATION -- %d of the %d rows read -- the dominant score (a maximiser over zeros of ζ, '
         'PowerWindow.lean:377), the tie and kill sets (`Kp` :271, `cE` :274, `Nf` :445), the interpolation bound over the tie nodes '
         '(PowerWindow.lean:432) and the largest ratio off those sets. No `j₀ : ℝ → ℝ → ℕ` of (γ, δ) alone is written from them. '
         'H9b, H9c, H9d NOT SCORABLE: each asks of a `j₀` written from those constants, and none is.' % (len(c.get('configuration', [])), len(c.get('rows', []))), '',
         '**What the branch holds.** `DetectionRegion.lean` and `AxiomCheckDetection.lean`, new files only, no existing module edited. '
         'Compiled at the standard three: `h2_sign_upto` (the finite positivity: `h2_sign`’s sign on the `classK` windows vanishing '
         'outside [−L₀, L₀]), `h2_sign_upto_mono`, `h2_sign_imp_upto`, `upto_all_imp_h2_sign`, **`h2_sign_iff_forall_upto : h2_sign ↔ '
         '∀ L₀, h2_sign_upto L₀`** and **`forall_upto_iff_rh : (∀ L₀, h2_sign_upto L₀) ↔ RiemannHypothesis`**, and `ellOf` (the base '
         'half-support the route takes, 1/(4(‖gammaOf ρ‖ + 1)), PowerWindow.lean:276). Stated with `sorry` bodies, printing `sorryAx`: '
         '`j₀` and `detection_region`, (R169)(3)’s theorem with hypothesis `h2_sign_upto L₀` alone and conclusion `ρ.re - 1 / 2 = 0` '
         'for a zero of Mathlib’s `riemannZeta` in the open strip. The E0 read: every constituent owned, the salt-check passed by the '
         'statement’s form, the grade T4 on the branch by its `sorry`; no merge, no tag, no `sorry` on `main`.', '',
         '**Two readings of (R169)(2) against the kernel.** The base window is not fixed: the route takes its half-support from the '
         'excluded zero (PowerWindow.lean:276 at :389), and `PWSetup` (PowerLimit.lean:245-251) fixes none. The n-th window is not an '
         'n-fold power: `power g j` is the j-fold iterated self-convolution, the 2^j-fold power (PowerWindow.lean:121, :129), and the '
         'window of index j is supported in [−2^(j+1)·ℓ, 2^(j+1)·ℓ]. And the ruling’s `h2_sign_upto`, typed as written, does not '
         'elaborate (`classK` is a predicate, `weilTest h h` a function); the module states the sign as `h2_sign` does.', '',
         '**The obstacle, priced** (the line appended to OPEN_TRAILS beside :11151 and :11332): (E1) a rate given the largest ratio off '
         'the tie and kill sets -- one lemma, moderate -- gives an index relative to the configuration; (E2) the configuration’s '
         'constants bounded by (γ, δ) alone needs a separation estimate for the zeros near the dominant score that no compiled lemma '
         'carries -- research grade, open. The closed-form route (b554, C1-C5) stands beside it at three of substance.', '',
         '**The reading, `(R169)`(6), descriptive voice.** No compiled region exists at this act, so there is no compiled L₀ at '
         '(16.29, 0.453) to set against the bench. What the bench’s numbers are, as `data/b554_sign_pattern.txt` records them: one '
         'functional Q(a) = OFF + ON of the whole Q0 bank (the Epstein control, disc −23, 17 off-line orbits; not ζ), at one window family '
         'of order 7, whose sign over a ∈ [30, 60] runs %s; so 33.19 and 38.96 are the left ends of its two negative runs. b553’s correction '
         '(FINDINGS :5754) holds here: the bench banks one detection width for the functional as a whole, none per zero. The zero at '
         '(16.290216, 0.453260) is Q0’s own (FINDINGS :5533); its pair term is %.1f at a = 30 and %.1f at a = 60, while the '
         '29.551761 orbit’s term changes sign across the range (%+.1f at a = 30, %+.1f at a = 34, %+.1f at a = 38). On the compiled '
         'side READING (3) finds the route’s index a property of the configuration too -- the dominant score and its competitors. The '
         'two sides meet on one point of shape: detection, on the bench and on the compiled route alike, is read off the whole '
         'configuration, not off one zero’s (γ, δ); a per-zero region R(L₀) would need the configuration’s constants bounded by (γ, δ), '
         'which is (E2). Against the detection-geometries entry (FINDINGS :5529): it reads the Weil side’s cost as governed by the '
         'zero’s distance from the line and the local density at its height; the route’s index is governed also by the separation of '
         'the scores near the dominant, which the entry does not name; and b550’s correction (:5681) is borne out -- the route’s n is '
         '2^j, its support 2^(j+1)·ℓ with ℓ taken from the excluded zero.' % (
             '; '.join(' '.join(r.split()[:1] + r.split()[-3:]) for r in runs), nodes[30]['pair'], nodes[60]['pair'],
             nodes[30]['o2955'], nodes[34]['o2955'], nodes[38]['o2955']), '',
         '**The housekeeping, (R169)(1).** relay `data/b558_refresh.txt` committed alone (`745d15da`); `G-PEEK-DECLARED`’s post-push '
         'reading changed to content digests against the pushed tree and committed alone with its test quoted (`673a39e2`); the re-run '
         'on b558’s push prints 63 of 63 (relay `data/b559_b558_postpush_rerun.txt`).', '',
         '**Next:** W-ORD-LI-WEIL-BRIDGE (`(R169)`(7)); the order of lane two does not change on a HELD.', '',
         '*Nothing deposits; nothing at Zenodo written; no `sorry` on any `main`; nothing here is a statement about RH or any zero of ζ.*', '']
    w = append_to(FIND, NL.join([''] + t))
    w['heading_line'] = line_of(FIND, FH)
    w['reading_line'] = line_of(FIND, '**The reading, `(R169)`(6), descriptive voice.**')
    put_json('b559_findings.json', w)
    print('  FINDINGS.md : %(added)d bytes added, prefix %(prefix)s ; the entry at line %(heading_line)d ; the reading at %(reading_line)d' % w)


# ------------------------------------------------------------------------------ READING (9): the row
def row():
    pr = prints()
    cells = ['394',
             '**THE DETECTION REGION, STATED AND HELD AT THE NAMED OBSTACLE** (b559, under (R169)). SIDE-explicit-formula branch '
             'detection-region-b559 at 8faf7de (from v0.2 = 5c72cad), pushed by name, NOT MERGED: DetectionRegion.lean states the finite '
             'positivity h2_sign_upto in the kernel`s vocabulary and compiles its join, h2_sign ↔ ∀ L₀, h2_sign_upto L₀ and hence ↔ '
             'Mathlib`s RiemannHypothesis; (R169)(3)`s j₀ and detection_region are stated with sorry bodies, because PowerLimit`s index '
             'comes from a limit with no rate over constants of the zero configuration (relay data/b559_constants.txt). Nothing here proves RH.',
             '`SIDE-explicit-formula/SIDEExplicitFormula/DetectionRegion.lean` (branch detection-region-b559 only) : ' +
             ', '.join('`%s%s`' % (NS, n) for n in NEW),
             '%d of %d compiled declarations: [propext, Classical.choice, Quot.sound]; j₀ and detection_region: [propext, sorryAx, '
             'Classical.choice, Quot.sound] (relay data/b559_axioms.txt)' % (sum(1 for n in NEW if pr.get(n) == STD3), len(NEW) - len(HELDN)),
             ' ; '.join('`%s` DERIVES' % n for n in COMPILED),
             'HELD on the branch: j₀ and detection_region carry sorry and are no grade`s; no sorry on main; no tag v0.3; h2 where the '
             'deposit left it; nothing deposits; nothing at Zenodo written.']
    r = subprocess.run([sys.executable, os.path.join(T, 'corr_row.py'), CORR] + cells, capture_output=True, text=True, encoding='utf-8')
    print(r.stdout[-600:], r.stderr[-400:])
    put_json('b559_rows.json', dict(cells=cells, exit=r.returncode))


# ------------------------------------------------------------------------------ the scores, the desk
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-effects': 'ef4cff7', 'SIDE-silence-principle': '667c254', 'SIDE-compression': 'e9a5a36', 'SIDE-structural-error-correction': '6a4f482',
             'SIDE-cosmo': 'c5cba30'}


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def kstate():
    br = g(EF, 'rev-parse', BRANCH).strip()
    return dict(branch=br, parent=g(EF, 'rev-parse', BRANCH + '^').strip(),
                remote=g(EF, 'ls-remote', 'origin', 'refs/heads/' + BRANCH).split('\t')[0].strip(),
                main=g(EF, 'rev-parse', 'main').strip(),
                ancestor=subprocess.run(['git', '-C', EF, 'merge-base', '--is-ancestor', BRANCH, 'main']).returncode == 0,
                tags=[x for x in g(EF, 'tag', '-l', 'v0.3*').split(NL) if x.strip()],
                status=sorted(set(x.split('\t')[0] for x in g(EF, 'diff', '--name-status', V02, BRANCH).split(NL) if x.strip())),
                files=sorted(x.split('\t')[-1] for x in g(EF, 'diff', '--name-status', V02, BRANCH).split(NL) if x.strip()))


def scores():
    c, e, lit = jl('b559_constants.json'), jl('b559_e0.json'), jl('b559_literal.json')
    pr = prints()
    k = kstate()
    el = rd(os.path.join(D, 'b559_elab_attempt1.txt'))
    m = re.search(r'exit (\d+) -- (\d+) s -- errors (\d+)', el)
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b559_') and needle in rd(os.path.join(T, x))]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(P.TRIAL, 'rev-parse', 'HEAD').strip(), status=g(P.TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    mm = {k2: [f for f in v if f.endswith('.lean')] for k2, v in mains().items()}   # ### (N6): a statement lives in a .lean file
    merged = k['ancestor'] and bool(k['tags'])
    h9a = c.get('h9a')
    return dict(
        h9a=h9a, h9b=None, h9c=None, h9d=None,
        n1=h9a,
        n2=(pr.get('detection_region') == STD3 and e.get('derives') is True),
        n3=None, n4=None,
        n5=merged,
        n6=(k['status'] == ['A'] and all(v == [] for v in mm.values()) and zen == [] and dep
            and trial['head'].startswith('f22ff35') and trial['status'] == ''),
        s1=(lit.get('variants', {}).get('a', {}).get('exit', 0) != 0 and lit.get('variants', {}).get('a', {}).get('errors', 0) > 0),
        s2=(all('sorryAx' in pr.get(n, ['sorryAx']) for n in HELDN) and all(n in pr and 'sorryAx' not in pr[n] for n in NEW if n not in HELDN)),
        s3=(bool(m) and int(m.group(1)) == 0 and int(m.group(3)) == 0 and int(m.group(2)) < 600),
        _detail=dict(kernel=k, mains=mm, zen=zen, dep=dep, trial=trial, elab=m.group(0) if m else None))


def desk():
    s = scores()
    k = s['_detail']['kernel']
    pr = prints()
    lines = ['=' * 104, 'b559 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
             '### (R169)(4)`S FOUR.', '-' * 104,
             '  **(H9a)** ### **%s.** -- the index of zeroSide_eventually_neg from Metric.tendsto_atTop over a limit with no rate '
             '(PowerLimit.lean:1092); the non-constructive rows %s; reach THE CONFIGURATION in %d rows (data/b559_constants.txt).'
             % (w_(s['h9a']), jl('b559_constants.json').get('nonconstructive'), len(jl('b559_constants.json').get('configuration', []))),
             '  **(H9b)** ### **%s.** -- it asks of a j0 written from the constants; none is (H9a). The print of the stated detection_region: %s.'
             % (w_(s['h9b']), pr.get('detection_region')),
             '  **(H9c)** ### **%s.** -- no compiled j0, so no j0 * l to evaluate at any point.' % w_(s['h9c']),
             '  **(H9d)** ### **%s.** -- no compiled j0, so no region to find empty or nonempty.' % w_(s['h9d']), '',
             '### THE NAVIGATOR`S SIX.', '-' * 104,
             '  **(N1)** ### **%s.** -- H9a: %s.' % (w_(s['n1']), w_(s['h9a'])),
             '  **(N2)** ### **%s.** -- detection_region prints %s; the E0 grade %s.' % (w_(s['n2']), pr.get('detection_region'), jl('b559_e0.json').get('grade')),
             '  **(N3)** ### **%s.** -- no compiled L0 at (16.29, 0.453); H9c not scorable.' % w_(s['n3']),
             '  **(N4)** ### **%s.** -- H9d not scorable.' % w_(s['n4']),
             '  **(N5)** ### **%s.** -- the branch an ancestor of main: %s ; tags v0.3: %s ; main %s.' % (w_(s['n5']), k['ancestor'], k['tags'] or 'none', k['main'][:7]),
             '  **(N6)** ### **%s.** -- the branch against v0.2 by status %s (%s) ; .lean files changed on the mains %s ; tools naming the platform %s ; deposit clean %s ; trial %s.'
             % (w_(s['n6']), k['status'], k['files'], [x for x, v in s['_detail']['mains'].items() if v] or 'NONE', s['_detail']['zen'] or 'NONE',
                s['_detail']['dep'], s['_detail']['trial']), '',
             '### THE SEAT`S THREE.', '-' * 104,
             '  **(S1)** ### **%s.** -- variant (a): %s.' % (w_(s['s1']), jl('b559_literal.json').get('variants', {}).get('a')),
             '  **(S2)** ### **%s.** -- %s.' % (w_(s['s2']), '; '.join('%s %s' % (n, pr.get(n)) for n in NEW)),
             '  **(S3)** ### **%s.** -- the last elaboration: %s.' % (w_(s['s3']), s['_detail']['elab']), '']
    nav = [s[x] for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')]
    seat = [s[x] for x in ('s1', 's2', 's3')]
    lines.append('### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
                 % (nav.count(True), nav.count(False), nav.count(None), seat.count(True), seat.count(False)))
    lines.append('### ### **(R169)(4) : H9a %s ; H9b %s ; H9c %s ; H9d %s.**' % tuple(w_(s[x]) for x in ('h9a', 'h9b', 'h9c', 'h9d')))
    d = rd(os.path.join(D, 'b559_defects.txt')) if os.path.exists(os.path.join(D, 'b559_defects.txt')) else ''
    if d:
        lines += ['', '### THIS ACT`S OWN DEFECTS.'] + d.rstrip().split(NL)
    put_txt('b559_desk_notes.txt', lines)
    put_json('b559_scores.json', {k2: v for k2, v in s.items() if not k2.startswith('_')})
    print(NL.join(lines))


# ------------------------------------------------------------------------------ the components bank
def components():
    L = ['=' * 132, 'b559 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b559_reads.txt', 'b559_housekeeping.txt', 'b559_constants.txt', 'b559_literal.txt', 'b559_elab_attempt1.txt',
              'b559_axioms.txt', 'b559_branch.txt', 'b559_e0.txt'):
        L.append('### relay data/%s' % n)
        L.extend('  ' + x for x in rd(os.path.join(D, n)).rstrip().split(NL))
        L.append('')
    for n, key in (('b559_price.json', 'line'), ('b559_findings.json', 'heading_line'), ('b559_rows.json', 'exit')):
        L.append('### relay data/%s -- %s %s' % (n, key, jl(n).get(key)))
    put_txt('b559_components.txt', L)
    print('  written: b559_components.txt (%d lines)' % len(L))


# ------------------------------------------------------------------------------ READING (9): the trail record
HEADING = ('### b559 — lane two, act one under (R169): W-ORD-DETECTION-REGION stated on a branch and held at the named obstacle; '
           'the housekeeping from b558')


def trail():
    guard_absent(OT, HEADING)
    s = jl('b559_scores.json')
    f, pc = jl('b559_findings.json'), jl('b559_price.json')
    t = ['', HEADING, '',
         '**(R169) ratified.** (1) The housekeeping: b558`s refresh record committed; the post-push check made to compare content '
         'digests against the pushed tree. (2) The object: the finite form of the power-window route. (3) The statement fixed. (4) '
         'H9a-H9d fixed before any build. (5) Merge and tag on the E0 gate and the print, not on compile; otherwise the branch pushed by '
         'name and HELD. (6) The reading, whatever the outcome. (7) W-ORD-LI-WEIL-BRIDGE next.', '',
         '**Entered:** FINDINGS.md:%d (the entry; the reading at :%d); OPEN_TRAILS.md:%d (the price corrected); SIDE-global-section '
         'CORRESPONDENCE.md row 394; SIDE-explicit-formula branch `detection-region-b559` at `8faf7de` (pushed by name, HELD).'
         % (f.get('heading_line'), f.get('reading_line'), pc.get('line')), '',
         '**The housekeeping:** relay `745d15da` (the refresh record), `673a39e2` (the instrument change, its test quoted); the re-run '
         'on b558`s push 63 of 63.', '',
         '**H9a REFUTED · H9b NOT SCORABLE · H9c NOT SCORABLE · H9d NOT SCORABLE.** The step: `PowerLimit.lean`:1092; the reach: the '
         'zero configuration.', '',
         '**The branch:** `DetectionRegion.lean`, `AxiomCheckDetection.lean`, new files only; seven declarations at the standard three '
         '(`h2_sign_iff_forall_upto`, `forall_upto_iff_rh` among them), `j₀` and `detection_region` carrying `sorryAx`; E0 grade T4; '
         'no merge, no tag.', '',
         '**Next:** W-ORD-LI-WEIL-BRIDGE.', '',
         '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
         % tuple(w_(s.get(x)) for x in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
         '**A kernel lane opened on a branch only; no `sorry` on any `main`; no tag.** Nothing deposits; nothing at Zenodo written; no '
         'existing `.lean` file edited; no monograph byte changed; no keystone body edited; ERRATA untouched; the ceiling unchanged; row '
         'U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or any zero beyond '
         'the compiled statements’ own words.', '']
    o = append_to(OT, NL.join(t))
    o['line'] = line_of(OT, HEADING)
    put_json('b559_trail.json', o)
    print('  OPEN_TRAILS.md:%(line)d (%(added)d bytes appended, prefix kept %(prefix)s)' % o)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        sys.exit('usage: b559_record.py reads | housekeeping | constants | literal | e0 | price | findings | row | components | desk | trail')
    fn()
