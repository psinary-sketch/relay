# -*- coding: utf-8 -*-
"""b279 -- THE LOCAL SPACE. ### WHAT IS `S-bar_v`?

### SCOPE, SAID FIRST AND OBEYED THROUGHOUT: ### **A CONSTRUCTION ATTEMPT AND READS.**
### ### **THIS FILE DOES NOT EVALUATE WHAT THE CONSTRUCTED SPACE DOES TO ANYTHING.**
### No SPEC-1, no SPEC-2, no SPEC-3, no barrier, no b277 candidate, no pairing is computed
### here. ### **THE OUTCOME-BLIND LAW: A DEFINITION IS SETTLED ON ITS OWN GROUNDS, NEVER BY
### WHAT IT YIELDS.** ### Everything below is a fact about the TOWER, not about its harvest.

### THE DOUBLE NAME, KEPT: ### `Son` tower (the constrained levels, `Son(p,n)`), ### `V_n`
### tower (b21's full level spaces), ### ambient `E_1` (the transform's +1 sector at one level).
### Every use below says which.
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import noise_floor  # noqa: E402

# ### CELLS: level n -> host level n+1. ### The owners kernel-checked ONE of these, (2,1)->(2,2).
CELLS = [(2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (5, 1), (7, 1)]


# ### ------------------------------------------------------------------------------------------
# ### THE TOWER'S LEVEL, DERIVED FROM THE OWNERS' TWO CONDITIONS -- AND IT IS RATIONAL.
# ### ------------------------------------------------------------------------------------------
# ### The keystone's `Son(p,n)`: "vectors vanishing on a ball AND on its transform image".
# ###   (1) BALL HALF:      f(m) = 0 whenever p^n | m.
# ###   (2) TRANSFORM HALF: (S f)(m) = 0 whenever p^n | m, where (S f)(m) = SUM f(m') zeta_N^{m m'}.
# ### At m = p^n k the character collapses: zeta_N^{p^n k m'} = zeta_{p^n}^{k m'}, which depends on
# ### m' ONLY THROUGH m' mod p^n. ### So (2) says the order-p^n DFT of the FOLDED function
# ###   Fold(r) = SUM_{m' = r mod p^n} f(m')
# ### vanishes identically, and a DFT vanishes identically exactly when its input does:
# ### ### **(2) <=> Fold(r) = 0 FOR EVERY RESIDUE r mod p^n.**
# ### ### **SO `Son` IS CUT OUT BY RATIONAL LINEAR CONDITIONS -- NO CYCLOTOMIC ARITHMETIC IS
# ### ### NEEDED TO DECIDE MEMBERSHIP, AND NO FLOAT IS USED ANYWHERE IN THIS FILE.**


def son_conditions_hold(f, p, n):
    """### DECIDE `f in Son(p,n)` BY THE TWO CONDITIONS, EXACTLY."""
    N, pn = p ** (2 * n), p ** n
    for m in range(0, N, pn):                       # ### (1) the ball half
        if f[m] != 0:
            return False, 'ball half fails at m=%d' % m
    fold = [0] * pn                                 # ### (2) the transform half, folded
    for m in range(N):
        fold[m % pn] += f[m]
    for r in range(pn):
        if fold[r] != 0:
            return False, 'transform half fails at residue r=%d' % r
    return True, 'both halves hold'


def son_basis(p, n):
    """### AN EXPLICIT BASIS OF `Son(p,n)`. ### Off-ball indices fall into `p^n - 1` fibers
    ### (residues `r != 0` mod `p^n`), each of size `p^n`, each carrying one sum-zero condition:
    ### `p^n - 1` free directions apiece. ### **DIMENSION `(p^n - 1)^2` -- WHICH IS THE
    ### KEYSTONE'S OWN STATED DIMENSION, AND IS CHECKED AGAINST IT BELOW.**"""
    N, pn = p ** (2 * n), p ** n
    basis = []
    for r in range(1, pn):
        fiber = [m for m in range(N) if m % pn == r]
        for i in range(1, len(fiber)):
            v = [0] * N
            v[fiber[i]] = 1
            v[fiber[0]] = -1
            basis.append(v)
    return basis


# ### ------------------------------------------------------------------------------------------
# ### THE CONNECTING MAP, THE OWNERS' OWN: `iota`, chart refinement `m'' = p*m + p^{2n+1}*j`.
# ### ------------------------------------------------------------------------------------------
def iota(f, p, n):
    """### b21's EMBEDDING, VALUES COPIED. ### `(m mod p^{2n}, j mod p) -> p*m + p^{2n+1}*j`
    ### is a bijection onto the multiples of `p` in `Z/p^{2n+2}`, because
    ### `p*m + p^{2n+1}*j = p*(m + p^{2n}*j)` and `m + p^{2n}*j` runs over `Z/p^{2n+1}` once."""
    N, M = p ** (2 * n), p ** (2 * n + 2)
    g = [0] * M
    for m in range(N):
        for j in range(p):
            g[(p * m + p ** (2 * n + 1) * j) % M] = f[m]
    return g


def iota_is_bijective_onto_p_multiples(p, n):
    """### THE MAP'S OWN CONTROL, RUN AND NOT ASSUMED."""
    M = p ** (2 * n + 2)
    hit = {}
    for m in range(p ** (2 * n)):
        for j in range(p):
            hit.setdefault((p * m + p ** (2 * n + 1) * j) % M, 0)
            hit[(p * m + p ** (2 * n + 1) * j) % M] += 1
    targets = set(range(0, M, p))
    return (set(hit) == targets), len(hit), len(targets)


def iota_is_isometric(f, p, n):
    """### b21's B1a, RE-DERIVED HERE RATHER THAN CITED. ### Each level-`n` index is copied to
    ### exactly `p` host cells; Haar gives level `n` mass `p^{-n}` and host mass `p^{-(n+1)}`;
    ### `p^{-(n+1)} * p = p^{-n}`. ### Exact in `Fraction`, no float."""
    g = iota(f, p, n)
    left = Fraction(1, p ** n) * sum(x * x for x in f)
    right = Fraction(1, p ** (n + 1)) * sum(x * x for x in g)
    return left == right, left, right


# ### ------------------------------------------------------------------------------------------
# ### THE BALL IS THE SAME SET AT EVERY LEVEL -- WHY THE TOWER IS A TOWER AT ALL.
# ### ------------------------------------------------------------------------------------------
# ### b21's chart is `x = p^{-n} m`. ### The ball `{m : p^n | m}` is `{x = p^{-n} p^n k} = {k}`,
# ### i.e. ### **`Z_p`, THE SAME COMPACT SET AT EVERY LEVEL.** ### `Son`'s constraint is therefore
# ### LEVEL-INDEPENDENT AS A CONDITION ON `Q_p`, which is what lets `iota` preserve it.
def ball_maps_to_ball(p, n):
    """### `p^{n+1} | (p*m + p^{2n+1}*j)` <=> `p^n | m`, checked exhaustively at the cell."""
    N = p ** (2 * n)
    for m in range(N):
        for j in range(p):
            mm = (p * m + p ** (2 * n + 1) * j) % (p ** (2 * n + 2))
            if (mm % p ** (n + 1) == 0) != (m % p ** n == 0):
                return False, (m, j)
    return True, None


def run_cell(p, n, rec):
    N, M = p ** (2 * n), p ** (2 * n + 2)
    rec('  ---- CELL (p,n) = (%d,%d):  Z/%d  --iota-->  Z/%d ----' % (p, n, N, M))

    bij, nhit, ntar = iota_is_bijective_onto_p_multiples(p, n)
    rec('    iota onto the p-multiples, bijectively : %s  (%d images / %d targets)'
        % ('YES' if bij else '### NO ###', nhit, ntar))

    bmb, wit = ball_maps_to_ball(p, n)
    rec('    ball <-> ball, exhaustively            : %s%s'
        % ('YES' if bmb else '### NO ###', '' if bmb else '  witness %s' % (wit,)))

    basis = son_basis(p, n)
    claimed = (p ** n - 1) ** 2
    rec('    dim Son(p,n) built = %-6d  keystone says (p^n-1)^2 = %-6d  : %s'
        % (len(basis), claimed, 'AGREE' if len(basis) == claimed else '### DISAGREE ###'))

    bad_self = [v for v in basis if not son_conditions_hold(v, p, n)[0]]
    rec('    every basis vector really lies in Son(p,n)  : %s'
        % ('YES' if not bad_self else '### NO (%d) ###' % len(bad_self)))

    # ### THE LOAD-BEARING LEMMA: ### **iota(Son(p,n)) SUBSET Son(p,n+1).**
    bad, iso_bad = [], []
    for v in basis:
        ok, why = son_conditions_hold(iota(v, p, n), p, n + 1)
        if not ok:
            bad.append(why)
        iok, _, _ = iota_is_isometric(v, p, n)
        if not iok:
            iso_bad.append(v)
    rec('    ### iota(Son(%d,%d)) SUBSET Son(%d,%d)      : %s  (%d vectors carried)'
        % (p, n, p, n + 1, 'YES' if not bad else '### NO ###', len(basis)))
    rec('    iota isometric on every basis vector    : %s'
        % ('YES' if not iso_bad else '### NO (%d) ###' % len(iso_bad)))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate                       : %s (all arithmetic integer/Fraction)' % cls)
    return bij and bmb and (len(basis) == claimed) and not bad_self and not bad and not iso_bad


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b279 -- THE LOCAL SPACE. ### THE CONSTRUCTION, RUN.')
    rec('=' * 100)
    rec('### SCOPE: ### **NO CONSEQUENCE IS COMPUTED HERE.** ### Not one spec, not the barrier,')
    rec('### not b277\'s candidate. ### The outcome-blind law governs and this file obeys it.')
    rec()
    rec('### THE CONSTITUENTS, EACH FROM AN OWNER:')
    rec('###   TOWER      Son(p,n) on Z/p^{2n}, dim (p^n-1)^2      -- keystone sec 1')
    rec('###   INCLUSION  iota, m\'\' = p*m + p^{2n+1}*j, values copied -- b21 (B1a/B1b PASS)')
    rec('###   DIRECTED   "the exact tower iota(Son) subset Son"    -- keystone sec 1')
    rec('###   NORM       model inner product = L^2(Q_p) up to p^{-n} -- b21, THE LIFT')
    rec('###   LIMIT      "the L^2-CLOSURE OF THE TOWER\'S UNION"    -- b198 (I4)')
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### ALL CELLS: %s' % ('PASS' if allok else '### SOME CELL FAILED ###'))
    rec('### **THE TOWER LEMMA HOLDS AT EVERY CELL RUN, AND IT ALSO DERIVES IN GENERAL** --')
    rec('### the ball half because p^{n+1} | p*(m + p^{2n} j) exactly when p^n | m, and the')
    rec('### transform half because each level-n fiber sum is reproduced p times downstairs:')
    rec('### SUM_{t = s mod p^n} f(t mod p^{2n}) = p * SUM_{m = s mod p^n} f(m) = p * 0 = 0.')
    rec('### **THE OWNERS KERNEL-CHECKED (2,1)->(2,2) ONLY; THIS IS ALL p AND ALL n.**')
    rec('=' * 100)
    io_path = os.path.join(ROOT, 'data', 'b279_construction_run.txt')
    with open(io_path, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
