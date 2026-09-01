# -*- coding: utf-8 -*-
"""b280 -- THE CONSEQUENCE. ### SPEC-1 ON THE OBJECT'S OWN LOCAL SPACE.

### THE DOUBLE NAME, KEPT AT EVERY USE:
###   ### **AMBIENT `E_1`**  -- the transform's `+1` sector at ONE finite level, inside `V_n`.
###                            ### b271's escape class lives HERE and nowhere else.
###   ### **`E_1(Son)`**     -- the `+1` sector INSIDE the constrained level `Son(p,n)`.
###   ### **`S-bar_p`**      -- the `L^2(Q_p)`-closure of `UNION iota(Son(p,n))` (b279).
### AND THE BALL, WHICH MOVES:
###   ### **`ball_n`** = `{ m in Z/p^{2n} : p^n | m }`; ### **`ball_{n+1}`** = `{ m'' in
###   Z/p^{2n+2} : p^{n+1} | m'' }`. ### **THESE ARE DIFFERENT SETS OF DIFFERENT AMBIENTS.**
###   ### In b21's chart `x = p^{-n} m` BOTH are the SAME compact set `Z_p` -- which is why the
###   condition is level-coherent, and b279 checked `ball <-> ball` under `iota` exhaustively.
### ### **SAYING "THE BALL" WITHOUT A LEVEL IS THE NAMED HAZARD OF THIS ACT.**
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                              # noqa: E402
from b270_ambient_pairing import Field, ball_of, orbit_classes  # noqa: E402
from b271_top_level_no_go import project                        # noqa: E402
from b279_local_space import son_basis, iota, son_conditions_hold  # noqa: E402
from b279_son_control import as_field_vector                    # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


def pairing_rescaled(u_int, p, k, n):
    """### b270's AMBIENT PAIRING, ITS OWN FORMULA, RESCALED BY `p^{k/2}` SO THE VALUE IS EXACT:
    ###   `P(k) * p^{k/2} = SUM_m (S_quot u)(m) * conj( u(p^k m mod N) )`.
    ### ### **THE RESCALING IS BY A POSITIVE FACTOR AND DECIDES NOTHING** -- `P(k) = 0` exactly
    ### when the rescaled value is `0`. ### It exists only to keep every token rational and keep
    ### `sqrt(p)` out of a deciding runner."""
    N = p ** (2 * n)
    F = Field(N)
    ballset = set(ball_of(N, p, n))
    classes = orbit_classes(N, p, ballset)
    cls_of = {}
    for C in classes:
        for m in C:
            cls_of[m] = C
    u = as_field_vector(u_int)
    su = project(u, N, ballset, cls_of)
    pk = pow(p, k, N)
    acc = {}
    from b270_ambient_pairing import spadd, spmul, spconj
    for m in range(N):
        if not su[m]:
            continue
        acc = spadd(acc, spmul(su[m], spconj(u[(pk * m) % N], N), N))
    return acc, F


def run_cell(p, n, rec):
    N = p ** (2 * n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d,  ball_n = {m : %d | m} ----' % (p, n, N, p ** n))
    basis = son_basis(p, n)

    # ### S1 AT THIS LEVEL: every Son(p,n) vector vanishes on ball_n -- its OWN first condition.
    ballset = set(ball_of(N, p, n))
    van = all(all(v[m] == 0 for m in ballset) for v in basis)
    rec('    S1  every Son(%d,%d) vector vanishes on ball_n        : %s'
        % (p, n, 'YES' if van else '### NO ###'))

    # ### S3 AT THIS LEVEL: the pairing at k = n, by b270's own formula.
    dead_at_n, alive_somewhere = True, None
    for v in basis:
        val, F = pairing_rescaled(v, p, n, n)
        if not F.is_zero(val):
            dead_at_n = False
    rec('    S3  P(k=n) * p^{n/2} = 0 for EVERY Son vector         : %s  (%d vectors)'
        % ('YES' if dead_at_n else '### NO ###', len(basis)))

    # ### THE NOT-DEAD WITNESS (b270's F-NONTRIV, re-run here): the SAME instrument must be
    # ### NONZERO at some `k < n`, or the zero above is an artefact of a dead instrument.
    # ### ### **THE ARMS ARE EXHAUSTIVE AND THE SECOND ONE IS REAL** (W-ORD-PREDICATE-ARM):
    # ### ### AT `n = 1` THERE IS NO `k < n` AT ALL. ### The control is UNAVAILABLE at level 1 --
    # ### ### which is a fact about the level, not a failure of the object, and must not be
    # ### ### reported as either a pass or a fail.
    witness_ok = None                        # ### None = arm B, not applicable at this level
    if n >= 2:
        for k in range(1, n):
            for v in basis:
                val, F = pairing_rescaled(v, p, k, n)
                if not F.is_zero(val):
                    alive_somewhere = (k, F.reduce(val)[:3])
                    break
            if alive_somewhere:
                break
        witness_ok = alive_somewhere is not None
        rec('    ### NOT-DEAD WITNESS (k < n): %s'
            % ('nonzero at k = %d, value head %s' % alive_somewhere if alive_somewhere
               else '### NONE FOUND -- INSTRUMENT MAY BE DEAD ###'))
    else:
        # ### ARM B: no `k < n` exists. ### Report instead that the instrument is not trivially
        # ### dead -- `S_quot u` is itself nonzero -- and label it as NOT a `k < n` witness.
        Nb = p ** (2 * n)
        Fb = Field(Nb)
        bs = set(ball_of(Nb, p, n))
        cl = orbit_classes(Nb, p, bs)
        co = {}
        for C in cl:
            for m in C:
                co[m] = C
        nz = sum(1 for v in basis
                 if any(not Fb.is_zero(x) for x in project(as_field_vector(v), Nb, bs, co)))
        rec('    ### NOT-DEAD WITNESS (k < n): ### **UNAVAILABLE AT LEVEL 1 -- NO `k < n` EXISTS.**')
        rec('        availability control instead: S_quot u nonzero for %d/%d Son vectors'
            % (nz, len(basis)))
        rec('        ### **THIS IS NOT A k < n WITNESS AND IS NOT COUNTED AS ONE.**')

    # ### S1 ACROSS THE MAP: iota carries the vanishing to ball_{n+1}, the HOST's ball.
    Nh = p ** (2 * n + 2)
    ballh = set(ball_of(Nh, p, n + 1))
    carried = all(all(iota(v, p, n)[m] == 0 for m in ballh) for v in basis)
    rec('    S1  iota(Son(%d,%d)) vanishes on ball_{n+1}           : %s'
        % (p, n, 'YES' if carried else '### NO ###'))
    insn = all(son_conditions_hold(iota(v, p, n), p, n + 1)[0] for v in basis)
    rec('        ... and lands in Son(%d,%d) (b279 re-run)         : %s'
        % (p, n + 1, 'YES' if insn else '### NO ###'))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate                                     : %s' % cls)
    # ### ARM B (n = 1) CONTRIBUTES NO WITNESS REQUIREMENT, AND SAYS SO RATHER THAN
    # ### SILENTLY PASSING: `witness_ok is None` means NOT APPLICABLE, not TRUE.
    return van and dead_at_n and carried and insn and (witness_ok is not False)


def escape_check(p, n, rec):
    """### b271's ESCAPE VECTOR, TESTED FOR `Son` MEMBERSHIP. ### **THE POINT OF THIS CHECK IS
    ### THAT IT MUST FAIL** -- `g_0` is an ambient `E_1` vector, and if it were also a `Son`
    ### vector the barrier and b271 would contradict each other."""
    N = p ** (2 * n)
    q = p ** n
    g0 = [2] * N
    g0[0] += 2 * q                       # ### g_0 = 2q e_0 + 2 * 1
    ok, why = son_conditions_hold(g0, p, n)
    rec('    (%d,%d)  g_0 ball value = %-6d   in Son(%d,%d)? %-4s  (%s)'
        % (p, n, g0[0], p, n, 'YES' if ok else 'NO', why))
    return not ok


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b280 -- THE CONSEQUENCE. ### SPEC-1 ON `S-bar_p`, AT THE FINITE PLACES.')
    rec('=' * 100)
    rec('### S2 -- THE CLOSURE STEP -- IS ANALYSIS AND IS **NOT** COMPUTED HERE.')
    rec('### This runner establishes the FINITE-LEVEL facts exactly. ### The passage to the')
    rec('### closure is derived in the bank and is NOT a computation.')
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        rec()
    rec('-' * 100)
    rec('### b271\'s ESCAPE VECTOR vs `Son` -- ### **IT MUST NOT BE A `Son` VECTOR:**')
    esc = True
    for p, n in CELLS:
        esc &= escape_check(p, n, rec)
    rec('### ### **g_0 IS OUTSIDE `Son` AT EVERY CELL: %s** -- so b271 (ambient E_1) and this'
        % ('YES' if esc else '### NO ###'))
    rec('### act (`S-bar_p`) speak about DIFFERENT VECTORS and do not collide.')
    rec('=' * 100)
    rec('### ALL CELLS: %s' % ('PASS' if (allok and esc) else '### FAILED ###'))
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b280_consequence_run.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if (allok and esc) else 1


if __name__ == '__main__':
    sys.exit(main())
