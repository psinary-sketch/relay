# -*- coding: utf-8 -*-
"""b296 -- THE ASYMMETRY AND ITS SHARPNESS.

### ### **WHAT THIS RUNNER MEASURES THAT b295's DID NOT.**
### b295 derived `a >= 0 or b >= n-1` and could not say where `n-1` came from. ### This runner
### measures the threshold's source ### INDEPENDENTLY OF THE CRITERION ### , and closes the
### criterion's other half.

### ### **(A) THE OPERATOR'S READING SCALE, MEASURED WITHOUT REFERENCE TO `b` (falsifier Y3).**
### The first slot enters only through `G_f(r) = SUM_{m = r mod q} (S_quot f)(m)`, a LINEAR map
### `f -> G_f`; call its matrix `Gamma`. ### The fiber sums at modulus `p^M` are the rows of the
### 0/1 matrix `Pi_M`. ### ### **`G_f` IS DETERMINED BY THE `p^M` FIBER SUMS EXACTLY WHEN
### ### `ker(Pi_M)` IS INSIDE `ker(Gamma)`, i.e. WHEN `rank(Pi_M) = rank(Pi_M stacked on
### ### Gamma)`.** ### The runner finds the SMALLEST such `M` by exact rational elimination.
### ### **PREDICTED `M = 2n - 1`, with `M = 2n-2` FAILING** -- both polarities, or the modulus
### ### was asserted rather than measured.
### ### **AND THE THRESHOLD THEN FALLS OUT: ### the condition at exponent `b` kills fiber sums at
### ### modulus `p^{n+b}` AND EVERY COARSER ONE, so it covers everything the operator reads
### ### exactly when `n + b >= M = 2n - 1`, i.e. `b >= n - 1`.**

### ### **(B) THE ONE-SIDEDNESS, MEASURED AS TWO SPACES (Y8).**
###   ### **`BALL := { f : f vanishes on the ball }`** -- the object's FIRST condition ALONE,
###     carrying ### NO ### transform condition at all.
###   ### **`FIB  := { f : every fiber sum at modulus p^n vanishes }`** -- the object's SECOND
###     condition ALONE, carrying no function-side condition.
### ### **BOTH LIE OUTSIDE THE FAMILY'S OWN INDEX RANGE** (`-n <= a,b <= n`) and are built here
### directly, which is said rather than smuggled.

### ### **(C) SHARPNESS, BY ONE WITNESS PER CELL (Y4).**
###   `f := e_{p^{n-1}} - e_{p^{n-1}+p^{2n-2}}`  -- same `p^{n+b}` fiber (needs `b <= n-2`),
###                                                 different `p^{2n-1}` fibers
###   `g := e_{p^n} - e_{p^n+p^{2n-1}}`          -- two ball points (needs `a <= -1`)
###   ### **`h := f + g`, and `<A h, h> = <A f, g> = 2 p^{n-1} (p-1) / (p^n - 1)`**, because `f`
###   has no ball mass and `g` is ball-supported.
### ### **THE SAME `h` LIES IN EVERY MEMBER WITH `-n <= a <= -1` AND `-n <= b <= n-2`.**
### ### **AT `(2,1)` THE CONSTRUCTION COLLIDES (`p^{n-1}+p^{2n-2} = 2 = p^n`) AND THE GENERAL ARM
### ### REPORTS UNAVAILABLE, NEVER A PASS (Y9).**

### ### **EXPOSURE TO THE ESCAPED-MASS ARTIFACT (Y6): ### NONE.** ### No level-shifting map
### appears; members are defined by radii and the pairing is b273's `A` at `k = n`, within one
### level. ### **THE ARTIFACT LIVES IN `g` AND `h` OF b284, WHICH ARE NOT THE `g` AND `h` OF THIS
### FILE AND DO NOT APPEAR IN IT.**

### ### **ZERO FLOAT TOKENS.** ### Exact `Fraction` throughout; witnesses re-valued in `Q(zeta_N)`.
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                                    # noqa: E402
from b270_ambient_pairing import Field, ball_of                       # noqa: E402
from b281_compression import matrix_A, apply_A, squot_rows            # noqa: E402
from b293_finite_family import (basis_family, in_family,              # noqa: E402
                                transform_vanishes, rank_exact)
from b294_family_value import pair_at_n                               # noqa: E402
from b295_second_mechanism import form_matrix, first_nonzero, diag_witness, forced_zero  # noqa: E402,E501

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (2, 3)]


# ### ==========================================================================================
# ### (A) THE OPERATOR'S READING SCALE.
# ### ==========================================================================================
def gamma_matrix(p, n):
    """### `Gamma[r][j]` = the coefficient of `f(j)` in `G_f(r)`. ### **LINEAR, EXACT, AND BUILT
    ### FROM `S_quot`'s OWN ROWS -- no reference to `a`, `b`, or any member.**"""
    N = p ** (2 * n)
    q = p ** n
    sq = squot_rows(N, p, n)
    G = [[Fraction(0)] * N for _ in range(q)]
    for m in range(N):
        row = sq.get(m)
        if not row:
            continue
        r = m % q
        for j, c in row.items():
            G[r][j] += c
    return G


def pi_matrix(p, n, M):
    """### THE FIBER SUMS OF THE REDUCTION `Z/p^{2n} -> Z/p^M`, as 0/1 rows."""
    N = p ** (2 * n)
    mod = p ** M
    P = [[Fraction(0)] * N for _ in range(mod)]
    for j in range(N):
        P[j % mod][j] = Fraction(1)
    return P


def determined_by(p, n, M, G):
    """### **IS `G_f` DETERMINED BY THE `p^M` FIBER SUMS?** ### Yes exactly when adding
    ### `Gamma`'s rows to `Pi_M`'s does not raise the rank."""
    N = p ** (2 * n)
    P = pi_matrix(p, n, M)
    r1 = rank_exact(P, N)
    r2 = rank_exact(P + G, N)
    return r1 == r2, r1, r2


def reading_scale(p, n, rec):
    """### **THE SMALLEST `M` THAT DETERMINES `G_f`, FOUND BY SEARCH AND NOT BY ASSERTION.**"""
    N = p ** (2 * n)
    G = gamma_matrix(p, n)
    smallest = None
    table = []
    for M in range(0, 2 * n + 1):
        ok, r1, r2 = determined_by(p, n, M, G)
        table.append((M, ok, r1, r2))
        if ok and smallest is None:
            smallest = M
    rec('    (A) THE OPERATOR\'S READING SCALE -- measured with NO reference to `b`:')
    for M, ok, r1, r2 in table:
        tag = ''
        if M == 2 * n - 1:
            tag = '   <- predicted 2n-1'
        elif M == 2 * n - 2:
            tag = '   <- must FAIL (too coarse)'
        elif M == 2 * n:
            tag = '   <- pointwise; works but is not minimal'
        rec('        M = %-3d modulus p^%-3d  rank(Pi)=%-4d rank(Pi|Gamma)=%-4d  determines G_f: %-5s%s'
            % (M, M, r1, r2, ok, tag))
    rec('        ### **SMALLEST M THAT DETERMINES G_f : %s   (predicted %d)  %s**'
        % (smallest, 2 * n - 1,
           'MATCH' if smallest == 2 * n - 1 else '### NO ###'))
    coarser_fails = not table[2 * n - 2][1] if 2 * n - 2 >= 0 else None
    rec('        ### both polarities: p^{2n-1} determines it : %s   p^{2n-2} does NOT : %s'
        % (table[2 * n - 1][1],
           coarser_fails if coarser_fails is not None else 'UNAVAILABLE (2n-2 < 0)'))
    return smallest, table


# ### ==========================================================================================
# ### (B) THE ONE-SIDEDNESS.
# ### ==========================================================================================
def kernel_basis(rows, N):
    """### AN EXACT BASIS FOR THE NULL SPACE OF `rows`. ### **NO FLOAT ANYWHERE.**"""
    R = [r[:] for r in rows]
    piv_cols, rank = [], 0
    for col in range(N):
        piv = None
        for i in range(rank, len(R)):
            if R[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = Fraction(1, 1) / R[rank][col]
        R[rank] = [x * inv for x in R[rank]]
        for i in range(len(R)):
            if i != rank and R[i][col] != 0:
                fct = R[i][col]
                R[i] = [x - fct * y for x, y in zip(R[i], R[rank])]
        piv_cols.append(col)
        rank += 1
    free = [c for c in range(N) if c not in piv_cols]
    out = []
    for fc in free:
        v = [Fraction(0)] * N
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def one_sidedness(p, n, A, ballset, rec, tally):
    N = p ** (2 * n)
    q = p ** n
    # ### BALL: the object's FIRST condition alone. ### No transform condition at all.
    rows = []
    for m in ballset:
        r = [Fraction(0)] * N
        r[m] = Fraction(1)
        rows.append(r)
    ball_basis = kernel_basis(rows, N)
    Mb = form_matrix(A, ball_basis, N, ballset)
    ball_zero = first_nonzero(Mb) is None

    # ### FIB: the object's SECOND condition alone. ### No function-side condition at all.
    rows = []
    for c in range(q):
        r = [Fraction(0)] * N
        for j in range(c, N, q):
            r[j] = Fraction(1)
        rows.append(r)
    fib_basis = kernel_basis(rows, N)
    Mf = form_matrix(A, fib_basis, N, ballset)
    fib_nz = first_nonzero(Mf)

    rec('    (B) THE ONE-SIDEDNESS -- each of the object\'s conditions ALONE, no other condition:')
    rec('        { f vanishing on the ball }        dim %-4d  FORM : %s  %s'
        % (len(ball_basis), 'IDENTICALLY ZERO' if ball_zero else '### NONZERO ###',
           '(the function side alone suffices)' if ball_zero else ''))
    rec('        { f with every p^n fiber sum 0 }   dim %-4d  FORM : %s'
        % (len(fib_basis), 'IDENTICALLY ZERO' if fib_nz is None else 'NONZERO'))
    if fib_nz is None:
        rec('        ### the transform side alone ALSO suffices here -- expected only at n = 1')
    else:
        rec('        ### **THE TRANSFORM SIDE ALONE DOES NOT SUFFICE.** ### first nonzero entry '
            '(i,j) = (%d,%d), value %s' % (fib_nz[0], fib_nz[1], fib_nz[2]))
    tally['onesided'].append((p, n, ball_zero, fib_nz is None))
    return ball_zero, fib_nz is None


# ### ==========================================================================================
# ### (C) SHARPNESS -- ONE WITNESS PER CELL.
# ### ==========================================================================================
def universal_witness(p, n):
    """### **THE REGISTERED CONSTRUCTION. ### RETURNS `None` WHERE IT COLLIDES (Y9).**"""
    N = p ** (2 * n)
    x0 = p ** (n - 1) % N
    x1 = (p ** (n - 1) + p ** (2 * n - 2)) % N
    y0 = p ** n % N
    y1 = (p ** n + p ** (2 * n - 1)) % N
    if len({x0, x1, y0, y1}) < 4:
        return None, (x0, x1, y0, y1)
    h = [Fraction(0)] * N
    h[x0] += 1
    h[x1] -= 1
    h[y0] += 1
    h[y1] -= 1
    return h, (x0, x1, y0, y1)


def sharpness(p, n, A, ballset, F, rec, tally):
    N = p ** (2 * n)
    predicted = Fraction(2 * p ** (n - 1) * (p - 1), p ** n - 1)
    h, pts = universal_witness(p, n)
    degenerate = h is None
    rec('    (C) SHARPNESS -- the registered witness, and the region below BOTH thresholds:')
    if h is None:
        rec('        ### **GENERAL CONSTRUCTION UNAVAILABLE AT THIS CELL (Y9) -- IT COLLIDES:**')
        rec('        p^{n-1}=%d, p^{n-1}+p^{2n-2}=%d, p^n=%d, p^n+p^{2n-1}=%d -- not four points'
            % pts)
        h = [Fraction(0)] * N
        h[p ** n] += 1
        h[1] -= 1
        predicted = Fraction(-1)
        rec('        ### the registered fallback witness `e_%d - e_1` is used instead, '
            'predicted %s' % (p ** n, predicted))
    else:
        rec('        h = e_%d - e_%d + e_%d - e_%d' % pts)

    tally['general' if not degenerate else 'fallback'].append((p, n))
    val = Fraction(0)
    Ah = apply_A(A, h, N)
    for l in ballset:
        if Ah[l] and h[l]:
            val += Ah[l] * h[l]
    cyc = F.reduce(pair_at_n(A, h, N, F))
    cyc_ok = bool(cyc) and cyc[0] == val and all(c == 0 for c in cyc[1:])
    hit = (val == predicted)
    tally['witness'].append(hit)
    tally['cyc'].append(cyc_ok)
    rec('        <A h, h>  PREDICTED %-8s  COMPUTED %-8s   %s'
        % (predicted, val, 'MATCH' if hit else '### NO ###'))
    rec('        SAME VALUE THROUGH THE CYCLOTOMIC INSTRUMENT : %-10s  %s'
        % (str(cyc[:2] if cyc else [0]), 'AGREE' if cyc_ok else '### DISAGREE ###'))
    onball = [k for k in ballset if h[k]]
    rec('        witness mass ON the ball (the object\'s FIRST condition forbids it) : %s'
        % (onball if onball else '### NONE ###'))

    # ### THE REGION BELOW BOTH THRESHOLDS -- does the ONE witness cover all of it?
    region = [(a, b) for a in range(-n, 0) for b in range(-n, n - 1)]
    inall, bad = 0, []
    for (a, b) in region:
        ok = in_family(h, p, n, a, b) and transform_vanishes(h, p, n, b)
        if ok:
            inall += 1
        else:
            bad.append((a, b))
    rec('        the SAME h lies in every member below both thresholds : %d/%d  %s'
        % (inall, len(region), 'ALL' if inall == len(region) else '### %s ###' % bad))
    tally['region'].append((p, n, inall, len(region)))

    # ### THE NEGATIVE POLARITY: the construction must STOP at the threshold, and for the
    # ### stated reason -- `f`'s two points stop sharing a `p^{n+b}` fiber at `b = n-1`.
    b_at = n - 1
    if -n <= b_at <= n:
        stops = not in_family(h, p, n, -1, b_at)
        rec('        NEGATIVE CONTROL -- at b = n-1 = %d the same h leaves the member : %s'
            % (b_at, 'YES' if stops else '### NO ###'))
        tally['negctl'].append(stops)
    # ### AND A SECOND NEGATIVE POLARITY: a lone on-ball spike is not a member.
    spike = [Fraction(0)] * N
    spike[p ** n] = Fraction(1)
    spike_ok = not in_family(spike, p, n, -1, 0)
    tally['spikectl'].append(spike_ok)
    rec('        NEGATIVE CONTROL -- a lone on-ball spike is rejected : %s'
        % ('YES' if spike_ok else '### NO ###'))


# ### ==========================================================================================
def run_cell(p, n, rec, tally):
    N = p ** (2 * n)
    q = p ** n
    ballset = sorted(ball_of(N, p, n))
    A = matrix_A(N, p, n, n)
    F = Field(N)
    csize = (p ** n - 1) // (p - 1)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d,  q = %d,  |class| = %d ----' % (p, n, N, q, csize))

    # ### Y1 FIRST: a zero from a dead instrument is not a zero.
    g0 = [Fraction(2)] * N
    g0[0] += 2 * q
    w = F.reduce(pair_at_n(A, g0, N, F))
    banked = 4 * (N - q)
    ok1 = bool(w) and w[0] == banked and all(c == 0 for c in w[1:])
    tally['y1'].append(ok1)
    rec('    Y1 NOT-DEAD WITNESS: <A g_0, g_0> = %-8s  b271 banked 4(N-q) = %-8s  %s'
        % (w[0] if w else 0, banked, 'MATCH' if ok1 else '### NO ###'))

    smallest, _ = reading_scale(p, n, rec)
    tally['scale'].append((p, n, smallest, 2 * n - 1))
    one_sidedness(p, n, A, ballset, rec, tally)
    sharpness(p, n, A, ballset, F, rec, tally)

    # ### Y5/Y8 -- the full-form sweep, kept from b295 so the criterion is re-measured whole.
    zero_forced, live_nz, refute = 0, 0, []
    zf_fn, zf_tr = 0, 0            # ### forced by the FUNCTION side vs by the TRANSFORM side
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            basis = [v for v in basis_family(p, n, a, b) if any(x != 0 for x in v)]
            if not basis:
                tally['cannot_test'] += 1
                continue
            M = form_matrix(A, basis, N, ballset)
            fnz = first_nonzero(M)
            crit = forced_zero(a, b, n)
            if crit and fnz is not None:
                refute.append((a, b))
            elif crit:
                zero_forced += 1
                if a >= 0:
                    zf_fn += 1
                    tally['y8'].append(True)
                else:
                    zf_tr += 1
            elif fnz is None:
                tally['not_necessary'].append((p, n, a, b))
            else:
                live_nz += 1
            if crit and a >= 0 and fnz is not None:
                tally['y8'].append(False)
    rec('    (D) THE FULL-FORM SWEEP, RE-RUN: forced-zero confirmed %d, live nonzero %d, '
        'criterion refuted %s' % (zero_forced, live_nz, refute if refute else 'NONE'))
    # ### **THE DECOMPOSITION, PRINTED SO Y8's COUNT CAN BE CLOSED FROM THE PAGE.** ### `Y8`
    # ### counts only the `a >= 0` members; the forced-zero total ALSO contains the `a < 0,
    # ### b >= n-1` members, which the TRANSFORM side forces. ### **A TALLY WHOSE ARITHMETIC A
    # ### READER CANNOT CLOSE IS A TALLY THAT CANNOT BE CHECKED.**
    rec('        forced-zero decomposition : %d by the FUNCTION side (a >= 0)  +  %d by the '
        'TRANSFORM side (a < 0, b >= n-1)  =  %d' % (zf_fn, zf_tr, zero_forced))
    tally['zf_fn'] += zf_fn
    tally['zf_tr'] += zf_tr
    if refute:
        tally['refute'].extend([(p, n) + r for r in refute])

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate : %s   (exact rational elimination and exact cyclotomic re-valuation)'
        % cls)


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    tally = dict(y1=[], y8=[], scale=[], onesided=[], witness=[], cyc=[], region=[],
                 negctl=[], spikectl=[], general=[], fallback=[],
                 not_necessary=[], refute=[], cannot_test=0, zf_fn=0, zf_tr=0)

    rec('=' * 100)
    rec('b296 -- THE ASYMMETRY AND ITS SHARPNESS.')
    rec('=' * 100)
    rec('### **NO LEVEL-SHIFTING MAP APPEARS. ### NOT EXPOSED TO THE ESCAPED-MASS ARTIFACT (Y6).**')
    rec('### (A) measures the operator\'s reading scale with NO reference to `b`;')
    rec('### (B) measures each of the object\'s conditions ALONE;')
    rec('### (C) exhibits ONE witness per cell for the whole region below both thresholds.')
    rec()
    for p, n in CELLS:
        run_cell(p, n, rec, tally)
        rec()

    rec('=' * 100)
    rec('### THE CLOSING TALLY.')
    rec('=' * 100)
    rec('  Y1 not-dead witness, cells matching b271        : %d/%d'
        % (sum(1 for x in tally['y1'] if x), len(tally['y1'])))
    good = sum(1 for r in tally['scale'] if r[2] == r[3])
    rec('  Y3 THE READING SCALE -- smallest M determining')
    rec('     G_f equals the predicted 2n-1                : %d/%d  %s'
        % (good, len(tally['scale']), 'PASS' if good == len(tally['scale']) else '### FAIL ###'))
    for r in tally['scale']:
        rec('      (p,n)=(%d,%d)  measured M = %s   predicted %d' % r)
    rec('  Y8 THE BARRIER -- `a >= 0` members with the')
    rec('     WHOLE FORM identically zero                  : %d/%d  %s'
        % (sum(1 for x in tally['y8'] if x), len(tally['y8']),
           'PASS' if all(tally['y8']) else '### FAIL ###'))
    rec('  ONE-SIDEDNESS (function side alone / transform side alone):')
    for p, n, bz, fz in tally['onesided']:
        rec('      (p,n)=(%d,%d)  ball-vanishing alone: %-5s   fiber-sum alone: %-5s   %s'
            % (p, n, 'ZERO' if bz else 'NONZERO', 'ZERO' if fz else 'NONZERO',
               'both suffice (n=1)' if fz else '### ONE-SIDED ###'))
    rec('  registered witnesses landing exactly            : %d/%d'
        % (sum(1 for x in tally['witness'] if x), len(tally['witness'])))
    rec('     of which by the GENERAL construction         : %d   cells %s'
        % (len(tally['general']), ['(%d,%d)' % r for r in tally['general']]))
    rec('     of which by the REGISTERED FALLBACK (Y9)     : %d   cells %s'
        % (len(tally['fallback']), ['(%d,%d)' % r for r in tally['fallback']]))
    rec('     ### **THE GENERAL ARM REPORTED UNAVAILABLE AT THE FALLBACK CELLS, NEVER A PASS.**')
    rec('  negative control (a lone on-ball spike rejected) : %d/%d'
        % (sum(1 for x in tally['spikectl'] if x), len(tally['spikectl'])))
    rec('  forced-zero decomposition, all cells            : %d (FUNCTION side, a >= 0) + %d '
        '(TRANSFORM side, a < 0 and b >= n-1) = %d'
        % (tally['zf_fn'], tally['zf_tr'], tally['zf_fn'] + tally['zf_tr']))
    rec('     ### **Y8 COUNTS THE FUNCTION-SIDE POPULATION ONLY (%d), WHICH IS WHY IT IS NOT THE'
        % tally['zf_fn'])
    rec('     ### FORCED-ZERO TOTAL. ### THE TWO NUMBERS NOW CLOSE ON THE PAGE.**')
    rec('  witness values agreeing across two instruments  : %d/%d'
        % (sum(1 for x in tally['cyc'] if x), len(tally['cyc'])))
    rec('  ONE witness covering the whole region below both thresholds:')
    for p, n, got, want in tally['region']:
        rec('      (p,n)=(%d,%d)  %d/%d members  %s'
            % (p, n, got, want, 'ALL' if got == want else '### SHORT ###'))
    rec('  negative control (h leaves the member at b = n-1): %d/%d'
        % (sum(1 for x in tally['negctl'] if x), len(tally['negctl'])))
    rec('  Y2 empty members reporting CANNOT TEST          : %d' % tally['cannot_test'])
    rec('  ### CRITERION REFUTED AT                        : %s'
        % (tally['refute'] if tally['refute'] else 'NOWHERE -- the criterion survives'))
    rec('  members below both thresholds that came back')
    rec('     ZERO (would refute necessity)                : %d  %s'
        % (len(tally['not_necessary']),
           'NONE' if not tally['not_necessary'] else '### %s ###' % tally['not_necessary']))
    rec('=' * 100)

    with open(os.path.join(ROOT, 'data', 'b296_asymmetry_run.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')

    bad = (not all(tally['y1'])) or (not all(tally['y8'])) or bool(tally['refute']) \
        or (not all(tally['witness'])) or (not all(tally['cyc'])) \
        or bool(tally['not_necessary']) or any(r[2] != r[3] for r in tally['scale'])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
