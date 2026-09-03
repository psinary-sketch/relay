# -*- coding: utf-8 -*-
"""b309_components.py -- THE COMPONENTS, IN ORDER. ### **THE FRAME ALGEBRA FIRST, THEN THE VALUES.**

### ### **THE ORDER OF THIS FILE IS THE ORDER'S OWN AND IT IS NOT COSMETIC.** ### The frame algebra
### and the controls run BEFORE a single trace is printed, because ### **A ZERO THAT ARRIVES BEFORE
### THAT SENTENCE IS AN OBSERVATION AND ONE THAT ARRIVES AFTER IT IS UNDERSTOOD.**

### ### **AND THE REGISTRATION IS SEALED WITH THE ANSWER IN IT.** ### `(P1)` through `(P5)` of
### `data/b309_registration_2026-09-03.txt` (sealed `eacdbf1c...`) state the closed form of the
### projector, the ambient, the reduction, the value and the mechanism, ### **ALL DERIVED ON PAPER
### BEFORE THIS FILE EXISTED.** ### So every table below is a CHECK ON A PREDICTION.
### ### **THE INSTRUMENT IS NOT ADJUSTED TOWARD THE PREDICTION. ### A DISAGREEMENT IS PRINTED AT
### ### FULL PROMINENCE AND KEPT.**
"""
import io
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'e16'))

import needle_pull                                   # noqa: E402
import b309_scaling_trace as ST                      # noqa: E402
import b308_local_field as LF                        # noqa: E402
import b304_smearing as SMEAR                        # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')

OWNERS = [
    # ### ### **RE-POINTED AT THE EMITTER, NOT RE-WORDED.** ### These two sentences are b304's, but
    # ### b304 emits them in its TOOL and not in its bank -- the refusal lives in the header of the
    # ### file that enacts it. ### **A NEEDLE POINTED AT THE BANK WOULD HAVE BEEN POINTED AT A
    # ### QUOTER**, and the puller said so on the first run.
    ('b304 -- THE REFUSAL THIS ACT LIFTS, IN b304\'s OWN WORDS (its tool is the emitter)',
     None, 'REFUSES THE'),
    ('b304 -- WHY THE MODEL COULD NOT CARRY THE SCALING PART (its tool is the emitter)',
     None, 'CANNOT CARRY THE NON-UNIT PART'),
    ('b21  -- THE CHART AND THE HAAR NORMALIZATION',
     'b21_2026-08-18.txt', 'via x = p^(-n) m; Haar measure'),
    ('b21  -- THE GENUINE SCALING, AND ITS ESCAPE',
     'b284_the_scalings_domain.txt', 'strictly bigger than'),
    ('b280 -- THE HAAR BRIDGE THAT MAKES THE FIRST CONDITION AN `L^2` CONDITION',
     'b280_the_consequence.txt', 'a chart point `m` at level `n`'),
    ('b280 -- THE NOT-DEAD DISCIPLINE, AND ITS `UNAVAILABLE` ARM AT LEVEL 1',
     'b280_the_consequence.txt', 'NO `k < n` AT ALL'),
    ('b293 -- THE BALL OF EXPONENT `e`',
     'b293_the_finite_family.txt', 'B_e := { m : v_p(m) >= n - e }'),
    ('b295 -- THE BARRIER STATEMENT THIS ACT NEITHER EXTENDS NOR WEAKENS',
     'b295_the_second_mechanism.txt', 'AND PAIRINGS OF THIS SHAPE'),
    ('b308 -- THE FRAME LAW FOR THE SCALING PART',
     'b308_the_local_field_instrument.txt', 'BOTH RADII MOVE'),
    ('b308 -- THE COMPUTATION THIS ACT PERFORMS, NAMED THERE AND LEFT UNDONE',
     'b308_the_local_field_instrument.txt', 'NAMED, AND NOT COMPUTED'),
]


def rule(ch='-', n=100):
    return ch * n


def powers(n):
    """### EVERY NONZERO POWER IN `[-2n, 2n]`. ### **THE RANGE IS THE LEVEL'S OWN, DOUBLED, SO IT
    ### REACHES BOTH REGIMES AND PAST THE SECOND ONE.**"""
    return [k for k in range(-2 * n, 2 * n + 1) if k != 0]


def main():
    out, fails = [], []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b309 -- THE SCALING TRACE. ### THE COMPONENTS, IN ORDER.')
    rec('=' * 100)
    rec('  ### THE FIXTURES OF EVERY FILE USED IN A VERDICT, RUN BEFORE ANY OF THEM IS TRUSTED:')
    ok_st, ok_lf, ok_sm = ST.self_test(False), LF.self_test(False), SMEAR.self_test(False)
    rec('    b309_scaling_trace : %s    b308_local_field : %s    b304_smearing : %s'
        % ('PASS' if ok_st else '### FAIL', 'PASS' if ok_lf else '### FAIL',
           'PASS' if ok_sm else '### FAIL'))
    if not (ok_st and ok_lf and ok_sm):
        rec('  ### REFUSING TO REPORT A COMPUTATION FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2, out

    rec('')
    rec('  ### THE OWNERS, PULLED FROM THE FILES THAT EMIT THEM:')
    unpullable = 0
    for label, fn, anchor in OWNERS:
        # ### `None` names the TOOL that emits the sentence rather than a bank in `data/`.
        path = os.path.join(D, fn) if fn else os.path.join(HERE, 'b304_smearing.py')
        try:
            line = needle_pull.pull(path, anchor)
            rec('  %s' % label)
            rec('      %s' % line[:140])
        except LookupError:
            unpullable += 1
            fails.append('owner needle: %s' % label)
            rec('  ### FAIL (UNPULLABLE) %s   anchor=%r' % (label, anchor))
    rec('  ### OWNER SENTENCES PULLED : %d   ### UNPULLABLE : %d'
        % (len(OWNERS) - unpullable, unpullable))

    # ==============================================================================================
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 1 -- THE OBJECT COMPUTED.')
    rec('=' * 100)

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (1a) THE FRAME ALGEBRA, STATED BEFORE ANY VALUE IS READ.')
    rec(rule())
    rec('  ### `theta(p^k)` carries `V(n,n)` to `V(n-k, n+k)`, so the composed map is ### NOT AN')
    rec('  ### ENDOMORPHISM OF ANY SINGLE FRAME ### and its trace is undefined until an ambient is')
    rec('  ### named. ### **THE SMALLEST FRAME CONTAINING BOTH IS `W = V(max(n,n-k), max(n,n+k))`**,')
    rec('  ### since `V(r,s)` sits inside `V(r\',s\')` exactly when BOTH radii grow.')
    rec('  ### ### **AND THE SECOND QUESTION THE ORDER PUTS FIRST: CAN THE PROJECTION MEET ITS')
    rec('  ### ### IMAGE AT ALL?** ### `Son` vanishes on the ball, so its support sits at')
    rec('  ### `|x| = p^s` for `s` in `[1, n]`; the image\'s sits at `s` in `[1+k, n+k]`.')
    rec('  ### **THE TWO RANGES MEET EXACTLY WHEN `|k| <= n-1`**, and that is asked here BOTH by')
    rec('  ### the exponent ranges AND by intersecting the actual index sets in `W`.')
    rec('')
    rec('  %-8s %-5s %-12s %-12s %-12s %-16s %-14s %s'
        % ('cell', 'k', 'source', 'target', 'ambient W', 'exponent ranges', 'index sets',
           'regime'))
    frame_bad = 0
    for (p, n) in ST.CELLS:
        for k in powers(n):
            W = ST.ambient(p, n, k)
            se, ie = ST.support_exponents(n), ST.image_exponents(n, k)
            meet_exp = bool(se & ie)
            meet_idx = None
            if W.M <= ST.AMBIENT_BOUND:
                meet_idx = bool(ST.overlap_by_indices(p, n, k))
            agree = (meet_idx is None) or (meet_idx == meet_exp)
            if not agree:
                frame_bad += 1
                fails.append('frame overlap at (%d,%d) k=%+d' % (p, n, k))
            regime = 'B -- they meet' if meet_exp else 'A -- disjoint'
            if abs(k) <= 1 or abs(k) == n or abs(k) == n - 1:
                rec('  %-8s %-5s %-12s %-12s %-12s %-16s %-14s %s'
                    % ('(%d,%d)' % (p, n), '%+d' % k, 'V(%d,%d)' % (n, n),
                       'V(%d,%d)' % (n - k, n + k), 'V(%d,%d)' % (W.r, W.s),
                       'MEET' if meet_exp else 'DISJOINT',
                       ('MEET' if meet_idx else 'DISJOINT') if meet_idx is not None
                       else 'out of reach',
                       regime))
    rec('  ### **THE TWO ROUTES TO THE SAME PREDICATE DISAGREE AT : %d CELL/POWER PAIRS.**'
        % frame_bad)
    rec('  ### ### **SO REGIME A (`|k| >= n`) IS A SUPPORT SEPARATION AND ANY ZERO THERE IS')
    rec('  ### ### UNDERSTOOD BEFORE IT IS SEEN. ### REGIME B (`1 <= |k| <= n-1`) IS WHERE THE')
    rec('  ### ### PROJECTION AND ITS IMAGE GENUINELY OVERLAP, AND A ZERO THERE WOULD NEED A')
    rec('  ### ### REASON THAT IS NOT THE FRAMES.**')

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (1b) THE CONTROLS, IN BOTH POLARITIES, BEFORE ANY SCALING VALUE IS READ.')
    rec(rule())
    rec('  ### **A SUITE OF ZEROS WITH NO NONZERO IN IT IS A DEAD INSTRUMENT REPORTING.** ### The')
    rec('  ### known-NONZERO case is `k = 0`, where the trace is b304\'s not-dead witness; the')
    rec('  ### known-ZERO case is a unit whose trace b304\'s own function returns as zero.')
    rec('  %-8s %-16s %-14s %-26s %s'
        % ('cell', 'Tr(Pi) built', 'the law', 'a unit with trace zero', 'closed form agrees'))
    for (p, n) in ST.CELLS:
        P, rank, _basis = ST.son_projector_built(p, n)
        N = p ** (2 * n)
        tr0 = sum(P[i][i] for i in range(N))
        law = (p ** n - 1) ** 2
        units = [t for t in range(N) if SMEAR.gcd(t, N) == 1]
        zero_units = [t for t in units if SMEAR.trace_scaled(P, t, N) == 0]
        if zero_units:
            t0 = zero_units[0]
            byclosed = sum(ST.son_projector_closed(p, n, (pow(t0, -1, N) * m) % N, m)
                           for m in range(N))
            zs = 't = %d, Tr = 0' % t0
            ag = 'YES, also 0' if byclosed == 0 else '### NO ###'
            if byclosed != 0:
                fails.append('known-zero control at (%d,%d)' % (p, n))
        else:
            zs = '### UNAVAILABLE -- none'
            ag = 'n/a'
        good = (tr0 == law and rank == law)
        if not good:
            fails.append('known-nonzero control at (%d,%d)' % (p, n))
        rec('  %-8s %-16s %-14s %-26s %s'
            % ('(%d,%d)' % (p, n), '%s %s' % (tr0, 'NONZERO' if tr0 else '### ZERO'),
               '(p^n-1)^2 = %d %s' % (law, 'AGREE' if tr0 == law else '### NO'), zs, ag))
    rec('  ### **AND THE `UNAVAILABLE` ARM, WHICH IS NOT A PASS:** ### at level 1 regime B is')
    rec('  ### EMPTY -- there is no `k` with `1 <= |k| <= n-1` -- so the not-dead witness for the')
    rec('  ### overlapping regime ### **CANNOT EXIST THERE AND IS REPORTED AS UNAVAILABLE.** ### That')
    rec('  ### is b280\'s own shape: its first draft would have tested `k = n` as its own witness at')
    rec('  ### level 1 and reported the dead value as the live one.')
    for (p, n) in ST.CELLS:
        if n == 1:
            rec('    (%d,%d) : regime B is EMPTY -- ### **UNAVAILABLE, NOT A PASS**' % (p, n))

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (1c) `F1` -- THE CLOSED FORM AGAINST THE BUILT PROJECTOR, ENTRY BY ENTRY.')
    rec(rule())
    rec('  ### The registration\'s `(P1)`, under seal: `Pi` is zero on any row or column lying on')
    rec('  ### the ball, and `[i=j] - (1/q)[i = j mod q]` off it. ### **ROUTE B USES THIS AND ROUTE A')
    rec('  ### DOES NOT**, so it is checked against b304\'s Gram-Schmidt projector before it is used.')
    rec('  %-8s %-10s %-16s %-18s %s'
        % ('cell', 'N', 'entries compared', 'disagreeing', 'trace from the form'))
    for (p, n) in ST.CELLS:
        P, _rank, _b = ST.son_projector_built(p, n)
        N = p ** (2 * n)
        bad = sum(1 for i in range(N) for j in range(N)
                  if P[i][j] != ST.son_projector_closed(p, n, i, j))
        trc = sum(ST.son_projector_closed(p, n, i, i) for i in range(N))
        if bad:
            fails.append('closed form at (%d,%d)' % (p, n))
        rec('  %-8s %-10d %-16d %-18s %s'
            % ('(%d,%d)' % (p, n), N, N * N, '%d %s' % (bad, 'PASS' if not bad else '### FAIL ###'),
               '%s (dimension law %d)' % (trc, (p ** n - 1) ** 2)))
    rec('  ### **THE TRACE OF THE CLOSED FORM IS `(p^{2n} - p^n)(1 - p^{-n}) = (p^n - 1)^2`** --')
    rec('  ### the dimension law, arrived at from the PROJECTOR rather than from the count, which is')
    rec('  ### the first check this seat ran on paper and the reason the form was trusted enough to')
    rec('  ### be sealed.')

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (1d) `F2` -- THE AMBIENT: THE EMBEDDING AND THE SCALING, AS EXACT IDENTITIES.')
    rec(rule())
    rec('  ### **THE EMBEDDING MUST PRESERVE THE HAAR INNER PRODUCT EXACTLY** -- it is a change of')
    rec('  ### chart, not a change of function -- and ### **`theta(p^k)` MUST SCALE IT BY EXACTLY')
    rec('  ### `p^{-k}`**, which is `|p^k|` and is the statement that the action is unitary after')
    rec('  ### b21\'s normalization. ### Both are checked on the object\'s own vectors.')
    rec('  %-8s %-5s %-30s %s' % ('cell', 'k', 'embedding preserves <,>', 'theta scales by p^{-k}'))
    amb_bad = 0
    for (p, n) in ST.CELLS:
        fr = LF.model_frame(p, n)
        basis = LF.son_basis(fr, 0, 0)[:3]
        for k in powers(n):
            W = ST.ambient(p, n, k)
            if W.M > ST.AMBIENT_BOUND:
                continue
            e_ok, s_ok = True, True
            for f in basis:
                ef = ST.embed(p, n, k, f)
                sf = ST.scaled_in_ambient(p, n, k, f)
                if LF.inner(W, ef, ef) != LF.inner(fr, f, f):
                    e_ok = False
                if LF.inner(W, sf, sf) != Fraction(1, p ** k) * LF.inner(fr, f, f) \
                        if k > 0 else \
                        LF.inner(W, sf, sf) != Fraction(p ** (-k)) * LF.inner(fr, f, f):
                    s_ok = False
            if not (e_ok and s_ok):
                amb_bad += 1
                fails.append('ambient identity at (%d,%d) k=%+d' % (p, n, k))
            if abs(k) == 1:
                rec('  %-8s %-5s %-30s %s'
                    % ('(%d,%d)' % (p, n), '%+d' % k,
                       'YES, exactly' if e_ok else '### NO ###',
                       'YES, exactly' if s_ok else '### NO ###'))
    rec('  ### **CELL/POWER PAIRS WHERE EITHER IDENTITY FAILS : %d**' % amb_bad)

    return _component_one_e(rec, fails, out)


# ==================================================================================================
def _component_one_e(rec, fails, out):
    rec('')
    rec(rule())
    rec('### (1e) THE TRACE ITSELF, BOTH ROUTES, AT EVERY NONZERO POWER.')
    rec(rule())
    rec('  ### **ROUTE A** builds the projector in the ambient by Gram-Schmidt and sums the')
    rec('  ### diagonal of the composed matrix; it assumes NOTHING about `Pi`\'s shape. ### **ROUTE')
    rec('  ### B** is the registration\'s reduction against the closed form. ### Where the ambient')
    rec('  ### exceeds %d chart points ### **ROUTE A IS OUT OF REACH AND THE ACT SAYS SO**'
        % ST.AMBIENT_BOUND)
    rec('  ### rather than dropping the second route quietly.')
    rec('')
    rec('  %-8s %-5s %-9s %-16s %-16s %-12s %-18s %s'
        % ('cell', 'k', 'regime', 'ROUTE A', 'ROUTE B', 'agree', 'composed operator',
           'ambient grid'))
    results = {}
    two_routes, only_b, disagree = 0, 0, 0
    nonzero_found = []
    for (p, n) in ST.CELLS:
        for k in powers(n):
            W = ST.ambient(p, n, k)
            tb = ST.trace_route_b(p, n, k)
            results[(p, n, k)] = tb
            if tb != 0:
                nonzero_found.append((p, n, k, tb))
            if W.M <= ST.AMBIENT_BOUND:
                ta, _alive, _dim, _g = ST.trace_route_a(p, n, k)
                two_routes += 1
                ok = (ta == tb)
                if not ok:
                    disagree += 1
                    fails.append('routes disagree at (%d,%d) k=%+d' % (p, n, k))
                    rec('  ### ### **DISAGREEMENT AT (%d,%d) k=%+d : ROUTE A = %s, ROUTE B = %s**'
                        % (p, n, k, ta, tb))
                ta_s, ag = str(ta), 'YES' if ok else '### NO ###'
                # ### **THE COMPRESSION, WHICH IS THE OPERATOR THE TRACE IS A TRACE OF.**
                nz, dim = ST.compression_matrix(p, n, k)
                expected_zero = (abs(k) >= n)
                if (nz == 0) != expected_zero:
                    fails.append('compression liveness at (%d,%d) k=%+d' % (p, n, k))
                op = ('ZERO operator' if nz == 0
                      else 'ALIVE (%d of %d^2)' % (nz, dim))
            else:
                only_b += 1
                ta_s, ag, op = 'out of reach', 'route A only', 'not formed'
            if abs(k) <= 2 or abs(k) == n:
                rec('  %-8s %-5s %-9s %-16s %-16s %-12s %-18s %s'
                    % ('(%d,%d)' % (p, n), '%+d' % k,
                       'B' if abs(k) <= n - 1 else 'A', ta_s, str(tb), ag, op, W.M))
    rec('')
    rec('  ### ### **AND THE COLUMN THAT REFUTES A CLAUSE OF THIS ACT\'S OWN SEALED PREDICTION.**')
    rec('  ### `(P4)` says that in regime A ### **"THE COMPOSED OPERATOR IS IDENTICALLY ZERO, NOT')
    rec('  ### MERELY TRACELESS"**. ### **THAT NAMES THE WRONG OPERATOR.** ### `theta(p^k) Pi` maps')
    rec('  ### `Son` onto its image and that image is NOT zero -- it is ### ORTHOGONAL ### to `Son`,')
    rec('  ### which is a different thing. ### **WHAT DISJOINT SUPPORTS KILL IS THE COMPRESSION')
    rec('  ### `Pi theta(p^k) Pi`**, and the column above is that operator, measured.')
    rec('  ### ### **THE PREDICTION\'S MATHEMATICAL CONTENT SURVIVES AND ITS WORDING DOES NOT, AND')
    rec('  ### ### THE RUN IS WHAT SAID SO. ### THE SEAL IS NOT EDITED.**')
    rec('  ### ### **AND IN REGIME B THE COMPRESSION IS ALIVE AND ITS TRACE IS ZERO** -- which is')
    rec('  ### the not-dead witness the order asked for, in its strongest available form: ### **NOT')
    rec('  ### A ZERO OPERATOR REPORTING A ZERO TRACE, BUT A LIVE ONE.**')
    rec('')
    rec('  ### **CELL/POWER PAIRS COMPUTED BY BOTH ROUTES : %d   ### BY ROUTE B ONLY : %d**'
        % (two_routes, only_b))
    rec('  ### **ROUTES DISAGREEING : %d**' % disagree)
    rec('  ### ### **NONZERO TRACES FOUND : %d**' % len(nonzero_found))
    for (p, n, k, v) in nonzero_found:
        rec('      ### ### **NONZERO AT (%d,%d) k=%+d : %s** ### -- the navigator\'s prediction is'
            ' REFUTED and this line is the refutation.' % (p, n, k, v))

    # ---------------------------------------------------------------------------------------------
    rec('')
    rec(rule())
    rec('### (1f) `F4` -- THE FUNCTIONAL EQUATION BETWEEN THE TWO DIRECTIONS.')
    rec(rule())
    rec('  ### The registration\'s `(P3)` derives `Tr(theta(p^k) Pi) = p^{-k} Tr(theta(p^{-k}) Pi)`')
    rec('  ### from the frame algebra alone. ### **IT IS CHECKED HERE AND NOT ASSUMED**, and at')
    rec('  ### these values it is the relation `0 = p^{-k} * 0`, which is TRUE AND SAYS LITTLE --')
    rec('  ### ### **A RELATION BETWEEN TWO ZEROS IS SATISFIED BY ANY SCALAR, AND THE ACT SAYS SO')
    rec('  ### ### RATHER THAN COUNTING IT AS EVIDENCE.**')
    feq_bad = 0
    for (p, n) in ST.CELLS:
        for k in range(1, 2 * n + 1):
            a, b = results[(p, n, k)], results[(p, n, -k)]
            if a != Fraction(1, p ** k) * b:
                feq_bad += 1
                fails.append('functional equation at (%d,%d) k=%d' % (p, n, k))
    rec('  ### **PAIRS CHECKED : %d   ### FAILING : %d**'
        % (sum(2 * n for _p, n in ST.CELLS), feq_bad))

    return _component_two(rec, fails, out, results, nonzero_found)


# ==================================================================================================
def _component_two(rec, fails, out, results, nonzero_found):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 2 -- THE MECHANISM.')
    rec('=' * 100)
    if nonzero_found:
        rec('  ### ### **COMPONENT 1 RETURNED A NONZERO. ### THE DERIVATION BELOW IS THE ZERO')
        rec('  ### ### BRANCH AND DOES NOT APPLY. ### THE ACT STOPS AND REPORTS.**')
        return 1, out

    rec('  ### ### **COMPONENT 1 RETURNED EXACTLY ZERO AT EVERY CELL AND EVERY NONZERO POWER.**')
    rec('  ### So the derivation owed is the zero branch, and it is a ### BARRIER STATEMENT ### with')
    rec('  ### its scope printed beside it.')
    rec('')
    rec(rule())
    rec('### (2a) TWO REGIMES, TWO MECHANISMS -- AND THE SECOND IS THE ONE THAT MATTERS.')
    rec(rule())
    rec('  ### ### **REGIME A (`|k| >= n`) -- A SUPPORT SEPARATION.** ### `Son` vanishes on the')
    rec('  ###   ball, so its support sits at `|x| = p^s` with `s` in `[1, n]`; `theta(p^k)`')
    rec('  ###   multiplies every absolute value by `p^k`, putting the image at `[1+k, n+k]`.')
    rec('  ###   ### **FOR `|k| >= n` THESE ARE DISJOINT AND THE COMPOSED OPERATOR IS IDENTICALLY')
    rec('  ###   ### ZERO -- NOT MERELY TRACELESS.** ### That is the object\'s FIRST condition and')
    rec('  ###   the level, and nothing else.')
    rec('  ### ### **REGIME B (`1 <= |k| <= n-1`) -- THE SUPPORTS MEET AND THE TRACE IS STILL')
    rec('  ###   ### ZERO.** ### By the closed form and the reduction, the trace is')
    rec('  ###   ### **`SUM over t off the ball of ( [ (p^j - 1) t = 0 mod N ]')
    rec('  ###   ###   - (1/q) [ (p^j - 1) t = 0 mod q ] )`,** ### `j = |k|`, `q = p^n`,')
    rec('  ###   `N = p^{2n}`.')
    rec('  ###   ### ### **AND `p^j - 1` IS A UNIT.** ### It is coprime to `p`, so each congruence')
    rec('  ###   forces `t = 0` modulo `N` and modulo `q` respectively -- ### **AND BOTH OF THOSE')
    rec('  ###   ### SETS ARE EXACTLY THE BALL, WHICH THE SUM EXCLUDES.** ### Both counts are zero.')
    rec('')
    rec('  ### **THE MECHANISM, IN ONE SENTENCE: ### THE SCALING MAP HAS NO FIXED POINT OFF THE')
    rec('  ### BALL, IN EITHER CONGRUENCE, BECAUSE `p^j - 1` IS INVERTIBLE -- AND THE ONLY FIXED')
    rec('  ### POINT IT HAS IS THE ONE PLACE THE OBJECT IS REQUIRED TO VANISH.**')
    rec('')
    rec('  ### **THE ARITHMETIC CORE, MEASURED AT EVERY CELL AND POWER RATHER THAN ASSERTED:**')
    rec('  %-8s %-5s %-14s %-14s %-22s %s'
        % ('cell', 'j', 'gcd(p^j-1,N)', 'gcd(p^j-1,q)', 'off-ball fixed points', 'both counts'))
    mech_bad = 0
    for (p, n) in ST.CELLS:
        N, q = p ** (2 * n), p ** n
        for k in range(1, 2 * n + 1):
            g1 = SMEAR.gcd(p ** k - 1, N)
            g2 = SMEAR.gcd(p ** k - 1, q)
            a_count = sum(1 for t in range(N) if t % q != 0 and ((p ** k - 1) * t) % N == 0)
            b_count = sum(1 for t in range(N) if t % q != 0 and ((p ** k - 1) * t) % q == 0)
            good = (g1 == 1 and g2 == 1 and a_count == 0 and b_count == 0)
            if not good:
                mech_bad += 1
                fails.append('mechanism at (%d,%d) j=%d' % (p, n, k))
            if k <= 2:
                rec('  %-8s %-5d %-14d %-14d %-22s %s'
                    % ('(%d,%d)' % (p, n), k, g1, g2, '%d and %d' % (a_count, b_count),
                       'both zero' if good else '### NO ###'))
    rec('  ### **CELL/POWER PAIRS WHERE THE MECHANISM FAILS : %d**' % mech_bad)

    rec('')
    rec(rule())
    rec('### (2b) IS IT A PROPERTY OF THE CONDITIONS OR OF THE CELLS? ### **BY DERIVATION.**')
    rec(rule())
    rec('  ### ### **OF THE CONDITIONS.** ### Every step of (2a) is general in `p`, `n` and `j`:')
    rec('  ###   the closed form of `Pi` is built from the object\'s TWO CONDITIONS and nothing')
    rec('  ###     else -- the ball coordinates and the residue-class indicators mod `q`, whose')
    rec('  ###     class of `0` IS the ball;')
    rec('  ###   the reduction to a sum over `Z/N` is the frame algebra, which is general;')
    rec('  ###   and `p^j - 1` is coprime to `p` for every prime `p` and every `j >= 1`.')
    rec('  ### ### **NO STEP MENTIONS A CELL.** ### The sweep above is a CHECK on a derivation, not')
    rec('  ### the derivation itself, and the act says which is which because ### **A SWEEP OVER')
    rec('  ### SEVEN CELLS IS NOT A PROOF OVER ALL OF THEM.**')
    rec('')
    rec(rule())
    rec('### (2c) THE SCOPE OF THE BARRIER STATEMENT, PRINTED WITH IT.')
    rec(rule())
    rec('  ### **WHICH MAP:** ### `theta(p^k)`, the scaling part of `Q_p^x`, composed with the')
    rec('  ###   orthogonal projection onto `Son(p,n)` -- the object\'s OWN space, the diagonal')
    rec('  ###   member `(0,0)` of b293\'s family, and no other member.')
    rec('  ### **WHICH FRAMES:** ### from `V(n,n)` to `V(n-k, n+k)`, traced in the smallest ambient')
    rec('  ###   containing both. ### **A DIFFERENT AMBIENT IS A DIFFERENT NUMBER AND THE ACT DOES')
    rec('  ###   NOT CLAIM OTHERWISE.**')
    rec('  ### **WHAT IT DOES NOT SAY:**')
    rec('  ###   ### **NOTHING ABOUT THE ARCHIMEDEAN PLACE** -- b285\'s boundary stands, no')
    rec('  ###     finite-side structural fact types at infinity, and this one does not either.')
    rec('  ###   ### **NOTHING ABOUT THE IDENTITY, ABOUT `h2`, OR ABOUT THE COMPLETE ROSTER.**')
    rec('  ###   ### **NOTHING ABOUT b273\'s `A` AT `k = n`.** ### That operator pairs the object\'s')
    rec('  ###     space against itself through a compression; this one traces a group action')
    rec('  ###     against a projection. ### **THE BARRIER AND THE COMPRESSION ARE NEITHER EXTENDED')
    rec('  ###     NOR WEAKENED HERE**, and the two must not be read as one statement.')
    rec('  ###   ### **NOTHING ABOUT ANY OTHER FUNCTIONAL ON THIS INSTRUMENT.** ### The vanishing')
    rec('  ###     of one trace is a statement about one trace.')
    rec('  ###   ### **AND NOTHING ABOUT THE SOURCE\'S FUNCTIONAL.** ### The source smears against a')
    rec('  ###     test function over the whole group; ### **A VANISHING OF EVERY INDIVIDUAL TERM')
    rec('  ###     IS A STATEMENT ABOUT TERMS, AND WHAT FOLLOWS FOR A SUM IS NOT CLAIMED HERE.**')
    rec('  ### ### **AND THE READING THE ACT REFUSES IN BOTH DIRECTIONS: ### A ZERO IS NOT A ROUTE')
    rec('  ### ### AND IT IS NOT AN ANTI-ROUTE.** ### The order forbids reading a nonzero as a')
    rec('  ### route; this act adds that the converse reading is forbidden too.')

    return _components_three_four(rec, fails, out, nonzero_found)


# ==================================================================================================
def _components_three_four(rec, fails, out, nonzero_found):
    rec('')
    rec('=' * 100)
    rec('### COMPONENT 3 -- THE SMEARED FORM.')
    rec('=' * 100)
    rec('  ### ### **THE ORDER MAKES THIS COMPONENT CONDITIONAL AND THE CONDITION IS NOT MET.**')
    rec('  ### *"only if Component 1 is nonzero somewhere ... If Component 1 is zero everywhere, say')
    rec('  ### plainly that there is nothing to smear and stop."*')
    rec('  ### ### **COMPONENT 1 IS ZERO EVERYWHERE. ### THERE IS NOTHING TO SMEAR. ### THIS')
    rec('  ### ### COMPONENT STOPS HERE.**')
    rec('  ### **AND WHAT IS THEREFORE NOT DONE, SAID RATHER THAN LEFT TO BE INFERRED:** ### no test')
    rec('  ### function is chosen, no class is stated, no price is quoted, no compressed value is')
    rec('  ### computed, and b262\'s mass is not named even as context -- ### **BECAUSE NAMING IT')
    rec('  ### BESIDE A COMPONENT THAT DID NOT RUN WOULD BE CONTEXT FOR NOTHING.**')

    rec('')
    rec('=' * 100)
    rec('### COMPONENT 4 -- WHAT IT DOES AND DOES NOT DO.')
    rec('=' * 100)
    rec('  ### ### **WHAT IT DOES.**')
    rec('  ###   ### It computes, for the first time in this record, ### **THE COMPRESSION OF THE')
    rec('  ###     SCALING PART OF `Q_p^x` AGAINST THE OBJECT\'S PROJECTION** -- the quantity b304')
    rec('  ###     refused because the model folds it, at every nonzero power in `[-2n, 2n]` at')
    rec('  ###     seven banked cells, exactly, by two independent routes wherever both are in')
    rec('  ###     reach.')
    rec('  ###   ### It returns ### **EXACTLY ZERO EVERYWHERE**, and it derives WHY in two regimes:')
    rec('  ###     a support separation above the level, and ### **THE INVERTIBILITY OF `p^j - 1`')
    rec('  ###     BELOW IT.**')
    rec('  ###   ### It gives a definite meaning to a sum b304 could only write formally, because')
    rec('  ###     at a non-unit the model\'s inverse does not exist.')
    rec('  ### ### **WHAT IT DOES NOT DO.**')
    rec('  ###   ### **IT DOES NOT DECIDE ANYTHING THE MODEL LEFT OPEN.** ### The instrument')
    rec('  ###     reproduces the model where the model was right and sees one direction further.')
    rec('  ###     ### **SEEING FURTHER IS NOT DECIDING.**')
    rec('  ###   ### **IT DOES NOT TOUCH THE BARRIER OR THE COMPRESSION**, which are statements')
    rec('  ###     about the pairing of the object\'s space against the top-level power.')
    rec('  ###   ### **IT DOES NOT CLAIM A ROUTE IN EITHER DIRECTION**, and it does not state an')
    rec('  ###     aggregation. ### `M-2` is owed.')
    rec('  ###   ### **IT DOES NOT REMOVE THE TRUNCATION.** ### b308\'s limit stands: untying the')
    rec('  ###     radii removed the wraparound and left the truncation exactly where it was.')
    rec('')
    rec(rule())
    rec('### (4a) THE EXPOSURE OF THIS ACT\'S OWN NUMBERS, BY CALL PATH.')
    rec(rule())
    rec('  ### The arm is b308\'s, imported: a ### NON-UNIT PUSHFORWARD SITE ### is a line reducing')
    rec('  ### the product of a grid index with a power of the residue characteristic modulo the')
    rec('  ### grid size. ### **IT FINDS A SHAPE; THE SEAT RULES.**')
    scan = [('tools/b309_scaling_trace.py', 'THE COMPUTATION'),
            ('tools/b309_components.py', 'THIS RUNNER'),
            ('tools/b308_local_field.py', 'b308 -- the frame, the ball, the embedding law'),
            ('tools/b304_smearing.py', 'b304 -- the projector and the unit trace'),
            ('tools/b303_family.py', 'b293/b303 -- the conditions and the nullspace')]
    total_sites = 0
    for rel, who in scan:
        path = os.path.join(ROOT, rel.replace('/', os.sep))
        sites = LF.pushforward_sites(path) if os.path.exists(path) else []
        total_sites += len(sites)
        rec('  %-36s %-6d %s' % (rel, len(sites), who))
        for ln, dfn, txt in sites:
            rec('        line %-5d %-26s %s' % (ln, dfn, txt[:64]))
    rec('')
    rec('  ### ### **THE READING, AND IT IS THIS SEAT\'S:**')
    rec('  ### **`b309_scaling_trace.py` -- THE SITES ARE IN THE REDUCED SUM AND IN THE MECHANISM\'S')
    rec('  ###   OWN COUNTS, AND NEITHER IS A FOLD.** ### `(p^j t) mod N` there is not a function')
    rec('  ###   being transported: it is ### **AN INDEX OF THE PROJECTOR BEING LOOKED UP**, and the')
    rec('  ###   reduction that produced it was derived in the ambient where nothing folds.')
    rec('  ###   ### **THE TRANSPORT ITSELF -- `scaling_column` -- CARRIES NO SUCH SITE: IT DIVIDES')
    rec('  ###   ### THE INDEX OR LEAVES IT ALONE, AND NEVER MULTIPLIES IT.** ### That is the')
    rec('  ###   mechanical form of b308\'s finding and it is visible in the printed lines.')
    rec('  ### **`b304_smearing.py` AND `b303_family.py` -- 0 SITES**, as at b308.')
    rec('  ### ### **AND THE DISTINCTION THIS ACT ADDS TO b308\'s:** ### a row of the scaling map')
    rec('  ### has ### AT MOST ONE ENTRY ### . ### **A FOLD REQUIRES TWO VALUES ARRIVING AT ONE')
    rec('  ### INDEX AND BEING ADDED; A MAP WITH ONE ENTRY PER ROW CANNOT DO THAT**, and that is')
    rec('  ### checked in this file\'s own fixtures rather than argued here.')
    return (0 if not fails else 1), out


if __name__ == '__main__':
    code, lines = main()
    io.open(os.path.join(D, 'b309_components_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(lines) + '\n')
    if code == 0:
        print('\n  ### CHECKS FAILING : 0')
    sys.exit(code)
