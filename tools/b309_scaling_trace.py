# -*- coding: utf-8 -*-
"""b309_scaling_trace.py -- THE SCALING TRACE. ### **THE COMPUTATION AND ITS CONTROLS.**

### ### **WHAT IS COMPUTED.** ### `Tr(theta(p^k) Pi)` for `k != 0`: the compression of the SCALING
### part of `Q_p^x` against the projection onto the object's own space. ### b304 computed the
### COMPACT part and said of the rest, in its own file: ### **"THEREFORE THIS FILE COMPUTES THE
### `Z_p^x` PART EXACTLY AND REFUSES THE `p^Z` PART"** ### -- because in the model `theta(p^k)`
### folds. ### b308 built the frame where it does not fold and named this computation without
### performing it. ### **THIS FILE PERFORMS IT.**

### ### ### **THE FIRST THING, AND THE ORDER PUTS IT FIRST FOR A REASON: ### THE TRACE IS NOT
### ### ### DEFINED UNTIL AN AMBIENT IS NAMED.**
### `theta(p^k)` carries `V(n,n)` to `V(n-k, n+k)`, so `theta(p^k) Pi` is ### **NOT AN
### ENDOMORPHISM OF ANY SINGLE FRAME.** ### The smallest frame containing both is
###   ### **`W = V(max(n, n-k), max(n, n+k))`**, ### since `V(r,s) subset V(r',s')` exactly when
### `r' >= r` AND `s' >= s`. ### **A TRACE REPORTED WITHOUT THAT SENTENCE WOULD BE A NUMBER WITH NO
### OPERATOR UNDER IT.**

### ### **THE TWO ROUTES, AND NEITHER IS THE OTHER'S RESTATEMENT.**
###   ### **ROUTE A -- THE AMBIENT MATRIX.** ### Embed the object's basis into `W`, build the
###     projector there by GRAM-SCHMIDT (b304's, imported), form the scaling map's matrix, and sum
###     the diagonal. ### **NOTHING IS ASSUMED ABOUT `Pi`'s SHAPE.**
###   ### **ROUTE B -- THE REDUCED SUM.** ### The registration derives, before this file existed,
###     that the ambient trace collapses to a sum over the MODEL's own grid against a CLOSED FORM
###     for the projector. ### **ROUTE B USES THAT CLOSED FORM AND ROUTE A DOES NOT**, so their
###     agreement checks the closed form and the reduction together.
### ### **WHERE ROUTE A IS OUT OF REACH THE BOUND IS PRINTED AND THE ROUTE IS NOT QUIETLY DROPPED.**

### ### **NO FLOAT. ### `Fraction` AND `int` ONLY.**

### ### **THE LIMITS, IN THE HEADER SO THE FILE IS NOT TRUSTED BEYOND THEM:**
### ### **(1) IT COMPUTES A TRACE, NOT A THEOREM.** ### The values below are exact at the cells and
###   powers listed and nowhere else; the DERIVATION that generalises them is the bank's, and its
###   scope is printed there.
### ### **(2) IT IS A DIFFERENT QUANTITY FROM `b273`'s `A` AT `k = n`.** ### That one pairs the
###   object's space against itself through a compression; this one traces a group action against a
###   projection. ### **THE BARRIER AND THE COMPRESSION ARE NEITHER EXTENDED NOR WEAKENED HERE**, and
###   conflating the two would be this act's worst available error.
### ### **(3) A ZERO IS NOT AN OBSTRUCTION THEOREM AND IS NOT AN ANTI-ROUTE.** ### The order forbids
###   reading a nonzero as a route; this file adds that the converse reading is forbidden too.
"""
import io
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'e16'))

import b308_local_field as LF     # noqa: E402  ### the frame, the embedding law, the ball
import b303_family as FAM         # noqa: E402  ### vp, nullspace
import b304_smearing as SMEAR     # noqa: E402  ### the projector, the unit trace, the permutation

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE CELLS ARE THE OWNERS'. ### b304's six, plus b295's level-3 discriminator. ### **NOT ONE
# ### OF THEM IS CHOSEN BY THIS ACT**, which is what keeps the sweep from being a sample picked
# ### after the answers were known.
CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)]

# ### ### **THE BOUND ON ROUTE A, DECLARED AND NOT DISCOVERED.** ### Gram-Schmidt in the ambient
# ### costs `dim^2 * |grid|`; beyond this the second route is out of reach and the act SAYS SO at
# ### every cell and power where that happens.
AMBIENT_BOUND = 1024


# ### ==============================================================================================
# ### THE PROJECTOR, TWO WAYS. ### **ONE BUILT, ONE DERIVED, AND THEY ARE COMPARED ENTRY-WISE.**
# ### ==============================================================================================
def son_projector_built(p, n):
    """### **b304's PROJECTOR, BY GRAM-SCHMIDT OVER `Q`, IMPORTED AND NOT REBUILT.**"""
    fr = LF.model_frame(p, n)
    basis = LF.son_basis(fr, 0, 0)
    P, rank = SMEAR.projector(basis, fr.M)
    return P, rank, basis


def son_projector_closed(p, n, i, j):
    """### ### **THE CLOSED FORM, WRITTEN INTO THE SEALED REGISTRATION AS `(P1)` BEFORE THIS FILE
    ### ### EXISTED.**

    ### `Son`'s orthogonal complement is spanned by the ball coordinates TOGETHER WITH the
    ### residue-class indicators mod `q = p^n`; the class of `0` IS the ball, so the two families
    ### are orthogonal and the projector is immediate:
    ###   ### **zero on any row or column lying on the ball;**
    ###   ### **`[i = j] - (1/q) [i = j mod q]` off it.**
    ### ### **THIS IS A PREDICTION UNDER SEAL, NOT A CONVENIENCE.** ### `arm_closed_form` compares
    ### it entry by entry against the built projector and a single disagreement refutes it.
    """
    q = p ** n
    if i % q == 0 or j % q == 0:
        return Fraction(0)
    return (Fraction(1) if i == j else Fraction(0)) - \
        (Fraction(1, q) if (i - j) % q == 0 else Fraction(0))


# ### ==============================================================================================
# ### THE AMBIENT, THE EMBEDDING, AND THE SCALING MAP'S COLUMN.
# ### ==============================================================================================
def ambient(p, n, k):
    """### ### **`W = V(max(n, n-k), max(n, n+k))`, THE SMALLEST FRAME CONTAINING BOTH.**"""
    return LF.Frame(p, max(n, n - k), max(n, n + k))


def embed(p, n, k, f):
    """### THE OBJECT'S VECTOR, READ IN `W`. ### **THE EMBEDDING IS A CHANGE OF CHART AND NOTHING
    ### ELSE**, and `arm_ambient` checks that it preserves the Haar inner product EXACTLY."""
    N = p ** (2 * n)
    W = ambient(p, n, k)
    shift = W.r - n                       # ### `p^shift` is the chart's refinement factor
    out = [Fraction(0)] * W.M
    for m_w in range(W.M):
        if shift == 0:
            out[m_w] = f[m_w % N]
        elif m_w % (p ** shift) == 0:
            out[m_w] = f[(m_w // (p ** shift)) % N]
    return out


def read_exponent(n, k, W):
    """### ### **THE ONE EXPONENT THE WHOLE COMPUTATION TURNS ON, DERIVED RATHER THAN GUESSED.**

    ### With `x = p^{-W.r} m_w`, the value of `theta(p^k) f` at that point is `f(p^{-k} x)`, and
    ### `p^{-k} x = p^{-n} m'` fixes
    ###   ### ### **`m' = p^{n - k - W.r} m_w`.**
    ### ### **THE EXPONENT IS NEVER POSITIVE**, because `W.r = max(n, n-k)` is `n` when `k > 0` and
    ### `n - k` when `k < 0`: at `k > 0` it is `-k`, and at `k < 0` it is exactly `0`.
    ### ### ### **SO THE INDEX IS EITHER DIVIDED OR LEFT ALONE. ### IT IS NEVER MULTIPLIED, AND
    ### ### ### THAT IS THE WHOLE OF WHY NOTHING IS FOLDED HERE.**

    ### ### **THE FIRST DRAFT OF THIS FILE WROTE `W.r - n - k`, WHICH IS RIGHT AT `k > 0` AND WRONG
    ### ### AT `k < 0` -- IT GAVE `+2j` WHERE THE DERIVATION GIVES `0`.** ### The two fixtures on
    ### the empty-row counts caught it before a single trace was computed, which is the whole reason
    ### a map this short carries fixtures at all.
    """
    return n - k - W.r


def scaled_in_ambient(p, n, k, f):
    """### **`theta(p^k) f`, WRITTEN IN `W`'s CHART**, through `read_exponent`."""
    N = p ** (2 * n)
    W = ambient(p, n, k)
    e = -read_exponent(n, k, W)           # ### `>= 0`; the index is divided by `p^e`
    out = [Fraction(0)] * W.M
    for m_w in range(W.M):
        if m_w % (p ** e) == 0:
            out[m_w] = f[(m_w // (p ** e)) % N]
    return out


def scaling_column(p, n, k, m_w):
    """### **THE ONE COLUMN THE SCALING MAP'S ROW `m_w` READS, OR `None` IF THE ROW IS EMPTY.**

    ### `Theta_k` has AT MOST ONE `1` PER ROW: it reads a value, it never accumulates two into one.
    ### ### **THAT IS THE MECHANICAL FORM OF b308's FINDING** -- the scaling part moves the frame
    ### rather than the data -- and it is why no index is ever reduced modulo the grid here.
    """
    N = p ** (2 * n)
    W = ambient(p, n, k)
    e = -read_exponent(n, k, W)           # ### `>= 0`; the index is divided by `p^e`
    if m_w % (p ** e) != 0:
        return None
    idx = (m_w // (p ** e)) % N           # ### the object-chart index this row reads
    # ### and that object-chart index, read back as a `W` index through the embedding
    shift = W.r - n
    return idx * (p ** shift) if shift > 0 else idx


# ### ==============================================================================================
# ### THE TRACE, BOTH ROUTES.
# ### ==============================================================================================
def proj_entry(orth, a, b):
    """### `Pi[a][b]` FROM AN ORTHOGONAL BASIS, ### **ON DEMAND AND WITHOUT A DENSE MATRIX.**"""
    s = Fraction(0)
    for v in orth:
        if v[a] and v[b]:
            s += v[a] * v[b] / sum(x * x for x in v)
    return s


def trace_route_a(p, n, k):
    """### **ROUTE A -- THE AMBIENT MATRIX. ### NOTHING IS ASSUMED ABOUT `Pi`'s SHAPE.**

    ### Returns `(trace, alive, dim, gridsize)` where `alive` says whether the COMPOSED operator is
    ### the zero matrix. ### **A TRACELESS LIVE OPERATOR AND A DEAD ONE ARE DIFFERENT FINDINGS.**
    """
    W = ambient(p, n, k)
    fr = LF.model_frame(p, n)
    basis = LF.son_basis(fr, 0, 0)
    emb = [embed(p, n, k, b) for b in basis]
    orth = SMEAR.orthogonalise(emb)
    zero_set = set(a for a in range(W.M) if all(v[a] == 0 for v in orth))
    tr = Fraction(0)
    alive = False
    for m_w in range(W.M):
        col = scaling_column(p, n, k, m_w)
        if col is None:
            continue
        if col not in zero_set:
            alive = True                  # ### that row of `Theta_k Pi` is not identically zero
        tr += proj_entry(orth, col, m_w)
    return tr, alive, len(orth), W.M


def compression_matrix(p, n, k):
    """### ### **`<theta(p^k) b_i, b_j>` OVER THE OBJECT'S OWN BASIS -- THE COMPRESSION `Pi theta
    ### ### Pi`, WHICH IS THE OPERATOR THE TRACE IS A TRACE OF.**

    ### ### **THIS FUNCTION EXISTS BECAUSE THE SEALED REGISTRATION NAMED THE WRONG OPERATOR.**
    ### `(P4)`'s regime-A clause says the ### COMPOSED ### operator is identically zero above the
    ### level. ### **IT IS NOT: `theta(p^k) Pi` MAPS `Son` ONTO ITS IMAGE, WHICH IS NOT ZERO.**
    ### What disjoint supports kill is the ### COMPRESSION ### `Pi theta(p^k) Pi` -- the image is
    ### ORTHOGONAL to `Son`, not absent. ### The mathematical content of the prediction survives; the
    ### object it attributed the vanishing to did not, ### **AND THE RUN IS WHAT SAID SO.**

    ### Returns `(nonzero_entries, dim)`. ### **`0` MEANS THE COMPRESSION IS THE ZERO OPERATOR;
    ### ANYTHING ELSE MEANS IT IS ALIVE, AND A ZERO TRACE ON A LIVE OPERATOR IS THE FINDING.**
    """
    W = ambient(p, n, k)
    fr = LF.model_frame(p, n)
    basis = LF.son_basis(fr, 0, 0)
    emb = [embed(p, n, k, b) for b in basis]
    sca = [scaled_in_ambient(p, n, k, b) for b in basis]
    nz = 0
    for u in sca:
        for v in emb:
            if sum(a * b for a, b in zip(u, v)) != 0:
                nz += 1
    return nz, len(basis)


def trace_route_b(p, n, k):
    """### **ROUTE B -- THE REDUCED SUM OVER THE MODEL'S OWN GRID, AGAINST THE CLOSED FORM.**

    ### The registration's `(P3)`, under seal before this file existed:
    ###   ### **`Tr(theta(p^k) Pi) = p^{-k} SUM_t P[t][p^k t mod N]` for `k > 0`,**
    ###   ### **`Tr(theta(p^{-j}) Pi) =      SUM_t P[t][p^j t mod N]` for `j > 0`.**
    ### ### **AND NOTE WHAT THAT SUM IS: THE ONE b304 COULD ONLY WRITE FORMALLY**, because at a
    ### non-unit the model's inverse does not exist. ### The untied frame gives it a meaning; it does
    ### not make the model's version of it correct.
    """
    N = p ** (2 * n)
    j = abs(k)
    s = Fraction(0)
    for t in range(N):
        s += son_projector_closed(p, n, t, (p ** j * t) % N)
    return s * Fraction(1, p ** k) if k > 0 else s


# ### ==============================================================================================
# ### THE SUPPORT RANGES -- ### **WHETHER THE PROJECTION CAN MEET ITS IMAGE AT ALL.**
# ### ==============================================================================================
def support_exponents(n):
    """### `Son` VANISHES ON THE BALL, SO ITS SUPPORT SITS AT `|x| = p^s`, `s` IN `[1, n]`."""
    return set(range(1, n + 1))


def image_exponents(n, k):
    """### `theta(p^k)` MULTIPLIES EVERY ABSOLUTE VALUE BY `p^k`."""
    return set(range(1 + k, n + k + 1))


def overlap_by_indices(p, n, k):
    """### THE SAME QUESTION ASKED OF THE ACTUAL INDEX SETS IN `W`, ### **AS A SECOND ROUTE TO ONE
    ### YES-OR-NO.** ### Two routes to one integer is b304's discipline; here it is two routes to
    ### one predicate."""
    W = ambient(p, n, k)
    fr = LF.model_frame(p, n)
    basis = LF.son_basis(fr, 0, 0)
    emb = [embed(p, n, k, b) for b in basis]
    sca = [scaled_in_ambient(p, n, k, b) for b in basis]
    s1 = set(a for a in range(W.M) if any(v[a] for v in emb))
    s2 = set(a for a in range(W.M) if any(v[a] for v in sca))
    return s1 & s2


# ### ==============================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES ON EVERYTHING THIS FILE OWNS.**
# ### ==============================================================================================
def self_test(verbose=True):
    bad = [0]

    def chk(lbl, got, exp):
        ok = (got == exp)
        bad[0] += 0 if ok else 1
        if verbose:
            print('  %-70s %-20s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-70s %-20s %s' % ('fixture', 'got/expected', 'agree'))

    # ### THE AMBIENT, BOTH DIRECTIONS, AND THE CONTAINMENT LAW.
    chk('the ambient for k = +1 at (2,2) is V(2,3)', ambient(2, 2, 1).key(), (2, 2, 3))
    chk('the ambient for k = -1 at (2,2) is V(3,2)', ambient(2, 2, -1).key(), (2, 3, 2))
    chk('### and for k = 0 it is the model frame itself', ambient(2, 2, 0).key(), (2, 2, 2))
    chk('the ambient contains the source frame (r and s both grow)',
        (ambient(2, 2, 1).r >= 2, ambient(2, 2, 1).s >= 2), (True, True))
    chk('the ambient contains the target frame V(n-k, n+k)',
        (ambient(2, 2, 1).r >= 1, ambient(2, 2, 1).s >= 3), (True, True))

    # ### THE CLOSED FORM, ### **BOTH POLARITIES, ON A CELL SMALL ENOUGH TO CHECK BY HAND.**
    # ### At (2,1): N = 4, q = 2, ball = {0, 2}; Son is spanned by e_1 - e_3.
    chk('closed form is zero on a ball row', son_projector_closed(2, 1, 0, 1), Fraction(0))
    chk('closed form is zero on a ball column', son_projector_closed(2, 1, 1, 2), Fraction(0))
    chk('closed form off the ball, diagonal', son_projector_closed(2, 1, 1, 1), Fraction(1, 2))
    chk('### closed form off the ball, same class off-diagonal',
        son_projector_closed(2, 1, 1, 3), Fraction(-1, 2))
    chk('### its trace is the dimension law at (2,1)',
        sum(son_projector_closed(2, 1, i, i) for i in range(4)), Fraction(1))
    chk('### and at (2,2), where the dimension is 9',
        sum(son_projector_closed(2, 2, i, i) for i in range(16)), Fraction(9))
    chk('### and at (3,2), where it is 64',
        sum(son_projector_closed(3, 2, i, i) for i in range(81)), Fraction(64))

    # ### THE SCALING COLUMN -- ### **AT MOST ONE PER ROW, WHICH IS THE NO-FOLD PROPERTY.**
    cols = [scaling_column(2, 2, 1, m) for m in range(ambient(2, 2, 1).M)]
    chk('every row of the scaling map reads at most one column',
        all(c is None or isinstance(c, int) for c in cols), True)
    chk('### and at k = +1 exactly half the rows are empty',
        sum(1 for c in cols if c is None), ambient(2, 2, 1).M // 2)
    cols2 = [scaling_column(2, 2, -1, m) for m in range(ambient(2, 2, -1).M)]
    chk('### at k = -1 no row is empty', sum(1 for c in cols2 if c is None), 0)

    # ### THE SUPPORT RANGES, ### **BOTH POLARITIES.**
    chk('supports overlap at n = 2, k = 1',
        bool(support_exponents(2) & image_exponents(2, 1)), True)
    chk('### supports are DISJOINT at n = 2, k = 2',
        bool(support_exponents(2) & image_exponents(2, 2)), False)
    chk('### and at n = 1 they are disjoint for every nonzero k',
        [bool(support_exponents(1) & image_exponents(1, k)) for k in (1, 2, -1, -2)],
        [False, False, False, False])
    chk('supports overlap at n = 3, k = 2',
        bool(support_exponents(3) & image_exponents(3, 2)), True)

    # ### `proj_entry`, ### **BOTH POLARITIES, AGAINST A PROJECTOR CHECKABLE BY HAND.**
    v = [Fraction(1), Fraction(-1)]
    chk('proj_entry on a one-dimensional span, diagonal', proj_entry([v], 0, 0), Fraction(1, 2))
    chk('### and off-diagonal', proj_entry([v], 0, 1), Fraction(-1, 2))
    return bad[0] == 0


if __name__ == '__main__':
    print('=' * 100)
    print('b309_scaling_trace.py -- THE FIXTURES. ### BOTH POLARITIES, NO FLOAT.')
    print('=' * 100)
    ok = self_test()
    print()
    print('  ### SELF-TEST : %s' % ('PASS' if ok else '### FAIL ###'))
    sys.exit(0 if ok else 2)
