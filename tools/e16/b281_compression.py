# -*- coding: utf-8 -*-
"""b281 -- THE COMPRESSION. ### DOES b280's DIAGONAL VANISHING EXTEND TO THE OPERATOR?

### THE DOUBLE NAME, KEPT AT EVERY USE:
###   ### **THE DIAGONAL VALUE**   `T(u) = <A u, u>` -- one vector in both slots.
###   ### **THE FORM**             `B(u,w) = <A u, w>` -- two slots, and b273 decided its type:
###                                ### **NEITHER HERMITIAN NOR SYMMETRIC.**
###   ### **THE COMPRESSED OPERATOR** `P_S A P_S` -- the operator cut down to `S-bar_p`.
###   ### **REAL SPAN** vs ### **COMPLEX SPAN** -- this file computes on the REAL span of the
###     integer `Son` basis. ### The derivation it checks is field-independent, and where that
###     matters it is said, not assumed.

### `A` IS b273's OWN MATRIX, NOT A NEW OBJECT:
###   ### **`A[l,j] = SUM_{m : p^k m = l mod N} S_quot[m,j]`**, so that
###   ### `T(g) = SUM_m (S_quot g)(m) conj(g(p^k m)) = <A g, g>`.
### ### **ZERO FLOAT TOKENS: every entry is a `Fraction`.**
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                        # noqa: E402
from b270_ambient_pairing import ball_of, orbit_classes    # noqa: E402
from b279_local_space import son_basis                     # noqa: E402
from b279_son_control import as_field_vector               # noqa: E402
from b270_ambient_pairing import Field                     # noqa: E402
from b271_top_level_no_go import in_E1                     # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


def squot_rows(N, p, n):
    """### `S_quot[m,j]`: class-averaging off the ball, ZERO on the ball. ### Returned as a dict
    ### `m -> {j: coeff}` so nothing dense is ever formed."""
    ballset = set(ball_of(N, p, n))
    rows = {}
    for C in orbit_classes(N, p, ballset):
        c = Fraction(1, len(C))
        for m in C:
            rows[m] = {j: c for j in C}
    for m in ballset:
        rows[m] = {}
    return rows


def matrix_A(N, p, n, k):
    """### b273's `A`, built from its own formula. ### Row `l` collects every `m` with
    ### `p^k m = l mod N`. ### **IF NO SUCH `m` EXISTS THE ROW IS EMPTY** -- and at `k = n` that
    ### is every `l` outside the ball, which is the whole finding."""
    sq = squot_rows(N, p, n)
    pk = pow(p, k, N)
    A = {}
    for m in range(N):
        l = (pk * m) % N
        row = sq.get(m)
        if not row:
            continue
        tgt = A.setdefault(l, {})
        for j, c in row.items():
            tgt[j] = tgt.get(j, 0) + c
    return {l: {j: c for j, c in row.items() if c} for l, row in A.items()}


def apply_A(A, v, N):
    out = [0] * N
    for l, row in A.items():
        s = 0
        for j, c in row.items():
            if v[j]:
                s += c * v[j]
        out[l] = s
    return out


def form(A, u, w, N):
    """### `B(u,w) = <A u, w>`. ### On the REAL span the conjugation is the identity, and this
    ### file says so rather than letting a missing `conj` pass unremarked."""
    Au = apply_A(A, u, N)
    return sum(Au[l] * w[l] for l in range(N) if Au[l] and w[l])


def c2_control(p, n, rec):
    """### C2's ENTAILMENT, ### **DERIVED BY COMPUTATION AND NOT BY ARGUMENT.**
    ### C2 is "EXTEND THE PROJECTION TO AN ACTION" -- it replaces `S_quot` by something else.
    ### ### **BUT THE ZERO NEVER CAME FROM `S_quot`.** ### `A`'s row index is `l = p^k m`, and at
    ### `k = n` that lies in `ball_n` FOR EVERY `m`, ### **WHATEVER SITS IN THE MATRIX.** ### So
    ### the image is ball-supported for ANY replacement, and every ball-vanishing `w` kills the
    ### pairing. ### Here `S_quot` is swapped for two unrelated matrices and the vanishing is
    ### re-checked, so the claim is a measurement rather than a plausible sentence."""
    N = p ** (2 * n)
    ballset = set(ball_of(N, p, n))
    basis = son_basis(p, n)
    pk = pow(p, n, N)
    subs = [('identity', lambda m: {m: Fraction(1)}),
            ('an arbitrary rational matrix', lambda m: {(3 * m + 7) % N: Fraction(m + 1, 5),
                                                        (5 * m + 2) % N: Fraction(-2, 3)})]
    allok = True
    for name, rowfn in subs:
        A = {}
        for m in range(N):
            l = (pk * m) % N
            tgt = A.setdefault(l, {})
            for j, c in rowfn(m).items():
                tgt[j] = tgt.get(j, 0) + c
        off = [l for l in A if l not in ballset]
        nzero = sum(1 for r in A.values() for c in r.values() if c)
        bad = 0
        for u in basis:
            Au = apply_A(A, u, N)
            for w in basis:
                if sum(Au[l] * w[l] for l in range(N) if Au[l] and w[l]):
                    bad += 1
        rec('      S_quot replaced by %-30s rows off ball: %d  nonzero entries: %-5d  B|SonxSon = 0: %s'
            % (name, len(off), nzero, 'YES' if not bad else '### NO ###'))
        allok &= (not off) and nzero and (not bad)
    return allok


def run_cell(p, n, rec):
    N = p ** (2 * n)
    ballset = set(ball_of(N, p, n))
    basis = son_basis(p, n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d,  ball_n = {m : %d | m},  dim Son = %d ----'
        % (p, n, N, p ** n, len(basis)))

    A = matrix_A(N, p, n, n)                    # ### at k = n

    # ### (1) THE STRUCTURAL FACT: A's IMAGE IS BALL-SUPPORTED AT k = n.
    off_ball_rows = [l for l in A if l not in ballset]
    rec('    (1) A rows supported OUTSIDE ball_n at k=n           : %d  %s'
        % (len(off_ball_rows), 'NONE -- image is ball-supported' if not off_ball_rows
           else '### PRESENT ###'))

    # ### (2) A IS NOT THE ZERO MATRIX -- else (1) would be vacuous.
    nz = sum(1 for row in A.values() for c in row.values() if c)
    rec('    (2) A is NOT the zero matrix (nonzero entries)       : %d  %s'
        % (nz, 'ALIVE' if nz else '### DEAD -- (1) IS VACUOUS ###'))

    # ### (3) THE FULL FORM ON Son x Son AT k = n -- ### **OFF-DIAGONAL INCLUDED.**
    Au = {i: apply_A(A, u, N) for i, u in enumerate(basis)}
    bad = 0
    for i in range(len(basis)):
        for j in range(len(basis)):
            w = basis[j]
            s = sum(Au[i][l] * w[l] for l in range(N) if Au[i][l] and w[l])
            if s:
                bad += 1
    rec('    (3) B(u,w) = 0 for ALL %d x %d Son pairs at k=n      : %s'
        % (len(basis), len(basis), 'YES' if not bad else '### NO (%d nonzero) ###' % bad))

    # ### (4) THE NOT-DEAD WITNESS: the SAME A, paired against a vector that does NOT vanish on
    # ### ball_n, must be NONZERO. ### **THIS IS WHAT SHOWS THE ZERO IS `S-bar_p`'s DOING.**
    q = p ** n
    g0 = [2] * N
    g0[0] += 2 * q
    # ### THE FIRST DRAFT PAIRED `A u` (u in Son) AGAINST `g_0` AND FOUND NOTHING AT (2,1).
    # ### ### **THAT WAS NOT A DEAD INSTRUMENT -- IT WAS A SECOND ANNIHILATION**: `A u = 0` for
    # ### ### `u` in `Son`, so no second slot could ever rescue it. ### The witness must therefore
    # ### ### put a NON-`Son` vector in the FIRST slot too.
    Ag0 = apply_A(A, g0, N)
    wit = sum(Ag0[l] * g0[l] for l in range(N) if Ag0[l] and g0[l])
    banked = 4 * (N - q)
    rec("    (4) NOT-DEAD: B(g_0, g_0) = %-8s   b271 banked 4(N-q) = %-8s : %s"
        % (wit, banked, 'MATCH' if wit == banked else '### MISMATCH ###'))

    # ### (4b) THE SECOND ANNIHILATION, WHICH THE FAILED WITNESS UNCOVERED:
    # ### ### **`A u = 0` FOR EVERY `u` IN `Son`** -- and this is b276's FIBER LEMMA, since
    # ### ### `(A u)(l) = SUM_{m : p^n m = l} (S_quot u)(m) = W(l)`. ### So it carries b276's
    # ### ### SCOPE, not the index law's, and that is said where it is used.
    live = [i for i in range(len(basis)) if any(Au[i][l] for l in range(N))]
    right = len(live)
    # ### ### **THE GUARD THAT KEEPS THIS HONEST.** ### b276's lemma is about ball-vanishing
    # ### ### vectors IN AMBIENT `E_1`, NOT about all of `Son`. ### A `Son` vector with
    # ### ### `A u != 0` refutes b276 ONLY IF IT LIES IN `E_1`. ### The first draft of this
    # ### ### runner printed "FIBER LEMMA FAILS HERE" without checking, which would have put a
    # ### ### false refutation of a banked lemma into the bank.
    FF = Field(N)
    in_e1 = [i for i in live if in_E1(as_field_vector(basis[i]), p ** n, N, FF)]
    rec('    (4b) A u = 0 for every Son u (b276 fiber lemma)      : %s  (%d of %d nonzero)'
        % ('YES' if right == 0 else 'NO on all of Son', right, len(basis)))
    rec('         of those, how many lie in ambient E_1            : %d  %s'
        % (len(in_e1),
           'NONE -- ### **b276 IS UNTOUCHED** ###' if not in_e1 else '### CONTRADICTS b276 ###'))
    rec("         ### **b276 LEMMA IS ABOUT BALL-VANISHING `E_1` VECTORS, NOT ALL OF `Son`.**")
    rec('         ### A `Son` vector outside `E_1` with `A u != 0` REFINES its scope; it does')
    rec('         ### not refute it. ### **AND THE BARRIER DOES NOT REST ON THIS AT ALL.**')

    # ### (5) THE k < n CONTROL: the compression is NOT zero at every k, so the k = n result is
    # ### specific. ### **ARM B AT n = 1: NO k < n EXISTS** (W-ORD-PREDICATE-ARM).
    if n >= 2:
        Ak = matrix_A(N, p, n, 1)
        Auk = {i: apply_A(Ak, u, N) for i, u in enumerate(basis)}
        found = None
        for i in range(len(basis)):
            for j in range(len(basis)):
                w = basis[j]
                s = sum(Auk[i][l] * w[l] for l in range(N) if Auk[i][l] and w[l])
                if s:
                    found = (i, j, s)
                    break
            if found:
                break
        rec('    (5) k=1 < n: B(u,w) != 0 on Son x Son              : %s'
            % ('YES -- (%d,%d) = %s' % found if found else '### NONE ###'))
    else:
        rec('    (5) k < n control: ### **UNAVAILABLE AT LEVEL 1 -- NO k < n EXISTS.**')
        rec('        ### **NOT COUNTED AS A PASS OR A FAIL.**')

    # ### (6) b273's FORM TYPE, RE-VERIFIED HERE RATHER THAN CITED: A != A^T.
    asym = None
    for l, row in A.items():
        for j, c in row.items():
            if A.get(j, {}).get(l, 0) != c:
                asym = (l, j, c, A.get(j, {}).get(l, 0))
                break
        if asym:
            break
    rec('    (6) A != A^T (the form is not symmetric)             : %s'
        % (('YES -- A[%d,%d]=%s but its transpose entry is %s' % asym)
           if asym else 'NO -- A IS SYMMETRIC'))

    rec('    (7) C2 CONTROL -- the zero does NOT come from S_quot:')
    c2ok = c2_control(p, n, rec)

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate                                     : %s' % cls)
    # ### **`right` IS NOT GATED ON.** ### The LEFT annihilation (1)+(3) carries the verdict;
    # ### the RIGHT one is b276's lemma and is reported at whatever it does.
    ok = ((not off_ball_rows) and nz and (not bad) and (wit == banked) and wit != 0
          and (asym is not None) and not in_e1 and c2ok)
    return ok


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b281 -- THE COMPRESSION. ### THE FORM ON `Son x Son`, NOT ONLY ITS DIAGONAL.')
    rec('=' * 100)
    rec('### THE QUESTION: b280 killed the DIAGONAL `<A u, u>`. ### Does the OPERATOR die?')
    rec("### ### **THE ANSWER IS DECIDED BY A's OWN ROW STRUCTURE AND NOT BY POLARIZATION.**")
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### ALL CELLS: %s' % ('PASS' if allok else '### FAILED ###'))
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b281_compression_run.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
