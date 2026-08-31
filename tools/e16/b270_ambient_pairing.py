# -*- coding: utf-8 -*-
"""b270_ambient_pairing.py -- M-2 CAMPAIGN, ACT 4. ### THE AMBIENT PAIRING'S PROPERTIES.

### WHAT THIS COMPUTES, AND WHAT IT REFUSES TO CALL IT.
###   THE PAIRING   `P(k) = <U^k S_quot u_v, u_v>`  -- a SINGLE MATRIX ELEMENT.
###   THE TRACE     `T_quot(k) = |Tr(U^k S_quot)|`  -- b10's AMBIENT TRACE, choice-free.
###   act 9's       `tau_q(p,n,k) p^{k/2} = (p^n - p^k)/(p^n - 1)`, `1 <= k <= n-1`; `0` for
###                 `k >= n`.
### ### **THESE ARE THREE OBJECTS. ### NO VALUE COMPUTED HERE IS PLACED IN A TABLE HEADED BY
### ### act 9's CLOSED FORM, AND NO COMPARISON TO ANY TARGET IS RUN.** ### The pairing is
### DERIVED AGAINST the specs; ### **IT IS NOT ADOPTED, AND M-2 REMAINS OWED IN EVERY BRANCH.**

### THE INSTRUMENT IS ITS OWNERS', NOT RECONSTRUCTED:
###   `b8_sonin_dim.model/scaling_matrix` -- `N = p^(2n)`, ball = multiples of `p^n`,
###     `U e_m = e_{pm mod N} / sqrt(p)`.
###   `b10_cells.quotient_basis` -- union-find on `m ~ pm` restricted to BOTH off-ball;
###     `S_quot = K K^T` = AVERAGING WITHIN EACH ORBIT CLASS, ZERO ON THE BALL.
###   `b268_generator.u_coeffs` -- `u_v = 4q P_1 f_{1,1}`, imported, not re-derived.

### ### **NO FLOAT DECIDES ANYTHING HERE.** ### Every verdict is taken in `Q(zeta_N)` by
### reduction modulo `Phi_N`. ### Floats appear in ONE place -- the printed magnitude of an
### already-exact rational -- and decide nothing (F-EXACT).
"""
import io
import os
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sympy import Poly, cyclotomic_poly, symbols

from b268_generator import u_coeffs

X = symbols('X')

# ### b226's CHOICE OF LEVEL, AND b268's PLACES UNCHANGED: ell(p) = 1 for odd p, ell(2) = 2.
# ### THE MODEL CELL IS (p, n) WITH n = ell(p), because u_v lives on Z/q^2 = Z/p^{2 ell} and the
# ### model at (p,n) is Z/p^{2n}. ### **THEY COINCIDE ONLY AT n = ell.**
PLACES = [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]


# ---------------------------------------------------------------------------------------------
# ### EXACT ARITHMETIC. ### Elements of Q[zeta_N] as sparse dicts {exponent mod N: Fraction}.
# ### zeta^N = 1, so multiplication is convolution of exponents mod N. ### ZERO-TESTING and the
# ### canonical value both go through reduction modulo Phi_N, which is what makes this the
# ### CYCLOTOMIC FIELD and not merely the group algebra.
# ---------------------------------------------------------------------------------------------
def spmul(a, b, N):
    out = {}
    for i, ca in a.items():
        for j, cb in b.items():
            k = (i + j) % N
            out[k] = out.get(k, Fraction(0)) + ca * cb
    return {k: v for k, v in out.items() if v != 0}


def spadd(a, b):
    out = dict(a)
    for j, c in b.items():
        out[j] = out.get(j, Fraction(0)) + c
    return {k: v for k, v in out.items() if v != 0}


def spscale(a, s):
    if s == 0:
        return {}
    return {j: c * s for j, c in a.items()}


def spconj(a, N):
    """### COMPLEX CONJUGATION ON Q(zeta_N): zeta -> zeta^{-1}. ### The coefficients are
    ### rational, so conjugation acts on the EXPONENTS alone."""
    out = {}
    for j, c in a.items():
        k = (-j) % N
        out[k] = out.get(k, Fraction(0)) + c
    return {k: v for k, v in out.items() if v != 0}


class Field(object):
    """### THE CYCLOTOMIC FIELD Q(zeta_N), carrying Phi_N once per cell."""

    def __init__(self, N):
        self.N = N
        self.phi = Poly(cyclotomic_poly(N, X), X)

    def reduce(self, a):
        """### CANONICAL FORM: the remainder modulo Phi_N, as a coefficient list on
        ### zeta^0 .. zeta^{deg Phi_N - 1}. ### THIS IS THE ONLY PLACE A VERDICT IS TAKEN."""
        if not a:
            return [Fraction(0)]
        coeffs = [Fraction(0)] * self.N
        for j, c in a.items():
            coeffs[j] = c
        p = Poly(list(reversed(coeffs)), X, domain='QQ')
        r = p.rem(self.phi)
        cs = list(reversed(r.all_coeffs()))
        return [Fraction(str(c)) for c in cs]

    def is_zero(self, a):
        return all(c == 0 for c in self.reduce(a))

    def eq(self, a, b):
        return self.is_zero(spadd(a, spscale(b, Fraction(-1))))

    def is_rational(self, a):
        """### True iff the reduced element lies in Q, i.e. only the zeta^0 coefficient is
        ### nonzero. ### Needed because a pairing is a NUMBER only if it is one."""
        r = self.reduce(a)
        return all(c == 0 for c in r[1:])


def from_int_vec(c):
    return {j: Fraction(v) for j, v in enumerate(c) if v != 0}


# ---------------------------------------------------------------------------------------------
# ### THE OWNERS' MODEL, AT CONTENT.
# ---------------------------------------------------------------------------------------------
def ball_of(N, p, n):
    """### b8's `model`: ball = { m : m % p^n == 0 }."""
    pn = p ** n
    return [m for m in range(N) if m % pn == 0]


def orbit_classes(N, p, ballset):
    """### b10's `quotient_basis`, at content: union-find over `m ~ pm` restricted to BOTH
    ### off-ball. ### The classes ARE the columns of K; S_quot averages within each."""
    parent = list(range(N))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for m in range(N):
        if m in ballset:
            continue
        m2 = (p * m) % N
        if m2 not in ballset:
            union(m, m2)
    classes = {}
    for m in range(N):
        if m not in ballset:
            classes.setdefault(find(m), []).append(m)
    return list(classes.values())


def run_cell(p, ell, rec):
    q = p ** ell
    n = ell
    N = q * q
    F = Field(N)
    ballset = set(ball_of(N, p, n))
    classes = orbit_classes(N, p, ballset)
    cls_of = {}
    for C in classes:
        for m in C:
            cls_of[m] = C

    # ### u_v, from b268's OWN generator. ### Not re-derived here.
    u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]

    res = {'p': p, 'ell': ell, 'n': n, 'q': q, 'N': N,
           'nball': len(ballset), 'nclasses': len(classes),
           'orbit_pairs': sum(1 for m in range(N)
                              if m not in ballset and (p * m) % N not in ballset)}

    # --- CONTROL: b268's derived support, re-established here, exactly. -----------------------
    zeros = [m for m in range(N) if F.is_zero(u[m])]
    res['zeroset_is_ball'] = (set(zeros) == ballset)
    res['support'] = N - len(zeros)
    res['support_matches_b268'] = (res['support'] == N - q)

    # --- S1: THE PROJECTION. ------------------------------------------------------------------
    Su = []
    for m in range(N):
        if m in ballset:
            Su.append({})
            continue
        C = cls_of[m]
        acc = {}
        for m2 in C:
            acc = spadd(acc, u[m2])
        Su.append(spscale(acc, Fraction(1, len(C))))
    res['Su_is_zero'] = all(F.is_zero(x) for x in Su)
    res['Su_equals_u'] = all(F.eq(Su[m], u[m]) for m in range(N))
    res['Su_support'] = sum(0 if F.is_zero(x) else 1 for x in Su)

    # ### F-S1 POSITIVE CONTROL: a vector supported ON the ball must project to exactly 0.
    ballvec = [({0: Fraction(1)} if m in ballset else {}) for m in range(N)]
    Sb = []
    for m in range(N):
        if m in ballset:
            Sb.append({})
        else:
            C = cls_of[m]
            acc = {}
            for m2 in C:
                acc = spadd(acc, ballvec[m2])
            Sb.append(spscale(acc, Fraction(1, len(C))))
    res['ctrl_ball_projects_to_zero'] = all(F.is_zero(x) for x in Sb)

    # --- THE PAIRING, k = 1 .. 2n-1, b10's own range. ----------------------------------------
    # ### P(k) = p^{-k/2} * SUM_m (S_quot u_v)(m) * conj( u_v(p^k m mod N) ).
    # ### THE FACTOR p^{-k/2} IS CARRIED SYMBOLICALLY; the exact object is P(k) * p^{k/2}.
    pair = {}
    for k in range(1, 2 * n):
        acc = {}
        pk = pow(p, k, N)
        for m in range(N):
            if not Su[m]:
                continue
            acc = spadd(acc, spmul(Su[m], spconj(u[(pk * m) % N], N), N))
        pair[k] = {'zero': F.is_zero(acc),
                   'rational': F.is_rational(acc),
                   'reduced': F.reduce(acc),
                   'raw': acc}
    res['pair'] = pair

    # --- b10's AMBIENT TRACE, exactly, as a control on the DOUBLE-NAME hazard. ---------------
    # ### Tr(U^k S_quot) = p^{-k/2} * SUM_{m off-ball} (S_quot)_{m, p^k m}, and (S_quot)_{m,m'}
    # ### is 1/|C| when m, m' share an off-ball class and 0 otherwise.
    tr = {}
    for k in range(1, 2 * n):
        pk = pow(p, k, N)
        s = Fraction(0)
        for m in range(N):
            if m in ballset:
                continue
            m2 = (pk * m) % N
            if m2 not in ballset and cls_of[m] is cls_of[m2]:
                s += Fraction(1, len(cls_of[m]))
        tr[k] = s
    res['trace'] = tr

    # ### F-DISTINCT, AS ONE EXACT EQUALITY AND NOT AS A BRANCHING PREDICATE.
    # ### **THE FIRST DRAFT OF THIS CHECK BRANCHED ON `rational` AND HAD NO ARM FOR THE CASE
    # ### THAT ACTUALLY OCCURRED -- A PAIRING THAT IS NOT A RATIONAL NUMBER -- SO IT PRINTED
    # ### "THEY AGREE" OVER A COMPARISON IT NEVER MADE.** ### Declared at the deviations.
    # ### Both sides are reduced modulo Phi_N and compared as VECTORS; the trace enters as the
    # ### element `s * zeta^0`. ### No branch, no `or`, one equality.
    agree = {}
    for k in range(1, 2 * n):
        agree[k] = F.eq(pair[k]['raw'], {0: tr[k]} if tr[k] != 0 else {})
    res['pair_eq_trace'] = agree

    # --- SPEC-2's RANGE, AND act 9's TERM AT THE CELLS WHERE THE RANGE IS NOT EMPTY. ----------
    # ### THIS IS A DERIVED COMPARISON OF TWO STATED FORMULAE, NOT A FIT TO ANY TARGET.
    spec2 = []
    for k in range(1, n):
        theta = Fraction(p ** n - p ** k, p ** n - 1)     # ### = tau_q(p,n,k) * p^{k/2}
        got = pair[k]['reduced']
        is_rat = all(c == 0 for c in got[1:])
        agrees = is_rat and got[0] == theta
        spec2.append({'k': k, 'theta_times_pk2': theta,
                      'pairing_times_pk2': got[0] if is_rat else None,
                      'pairing_is_rational': is_rat, 'agrees': agrees})
    res['spec2'] = spec2
    res['spec2_range_empty'] = (n - 1 < 1)
    return res


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b270 -- COMPONENT 1. ### THE AMBIENT PAIRING, DERIVED. ### EXACT ARITHMETIC IN Q(zeta_N).')
    rec('### REGISTRATION data/b270_registration_2026-08-31.txt SEALED 96ac5b1e BEFORE ANY VALUE.')
    rec('### **THE PAIRING IS DERIVED AGAINST SPEC-1/2/3. ### IT IS NOT ADOPTED. ### M-2 IS OWED.**')
    rec('=' * 100)
    rec()

    results = [run_cell(p, ell, rec) for (p, ell) in PLACES]

    rec('-' * 100)
    rec('### (1) THE CELLS, AND THE CONTROLS ON THE INSTRUMENT.')
    rec('-' * 100)
    rec('  %-6s %-4s %-6s %-7s %-8s %-9s %-11s %s'
        % ('(p,n)', 'q', 'N', '|ball|', 'classes', 'orb.pairs', 'supp(u_v)', 'zero set = ball?'))
    for r in results:
        rec('  %-6s %-4d %-6d %-7d %-8d %-9d %-11d %s'
            % ('(%d,%d)' % (r['p'], r['n']), r['q'], r['N'], r['nball'], r['nclasses'],
               r['orbit_pairs'], r['support'], 'YES' if r['zeroset_is_ball'] else '### NO ###'))
    rec()
    rec('  ### CONTROL A -- b268\'s DERIVED SUPPORT N - q, RE-ESTABLISHED EXACTLY HERE: %s'
        % ('ALL 8 CELLS' if all(r['support_matches_b268'] for r in results) else '### FAILED ###'))
    rec('  ### CONTROL B -- THE ZERO SET OF u_v IS EXACTLY THE BALL: %s'
        % ('ALL 8 CELLS' if all(r['zeroset_is_ball'] for r in results) else '### FAILED ###'))
    rec('  ### ### **THAT IS THE WHOLE OF b10\'s BALL-AVOIDANCE HALF, MET BY u_v OUTRIGHT --')
    rec('  ### ### NOT ARRANGED, BUT INHERITED FROM b268\'s ALREADY-BANKED RESULT.**')
    rec()

    rec('-' * 100)
    rec('### (2) S1 -- THE PROJECTION. ### **WHAT IS S_quot u_v?**')
    rec('-' * 100)
    rec('  %-6s %-12s %-16s %-14s %s'
        % ('(p,n)', 'S_quot u_v', 'supp(S_quot u_v)', '= u_v exactly?', 'ball vector -> 0? (F-S1 ctrl)'))
    for r in results:
        rec('  %-6s %-12s %-16d %-14s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               'ZERO' if r['Su_is_zero'] else 'NONZERO',
               r['Su_support'],
               'YES' if r['Su_equals_u'] else 'no',
               'YES' if r['ctrl_ball_projects_to_zero'] else '### NO ###'))
    # ### ONE UNAMBIGUOUS LINE FOR S1's VERDICT, so a gate reads a fact and not a table column.
    # ### **THE FIRST GATE FOR THIS FACT MATCHED THE PAIRING TABLE'S `ZERO` INSTEAD AND SO
    # ### TESTED NOTHING; ### the fix is here, at the source, not in a looser matcher.**
    nz = sum(1 for r in results if not r['Su_is_zero'])
    rec('  ### S1 VERDICT: S_quot u_v %s at %d of %d cells'
        % ('NONZERO' if nz == len(results) else 'ZERO', nz, len(results)))
    rec()

    rec('-' * 100)
    rec('### (3) THE PAIRING P(k) AND b10\'s TRACE T_quot(k), SIDE BY SIDE, NAMED SEPARATELY.')
    rec('### **THIS IS NOT A TABLE HEADED BY act 9\'s CLOSED FORM. ### NO TARGET APPEARS IN IT.**')
    rec('-' * 100)
    rec('  %-6s %-3s %-14s %-11s %-22s %s'
        % ('(p,n)', 'k', 'P(k)*p^{k/2}', 'P(k) zero?', 'Tr(U^k S_quot)*p^{k/2}', 'k vs n'))
    for r in results:
        n = r['n']
        for k in sorted(r['pair']):
            pr = r['pair'][k]
            val = ('%s' % pr['reduced'][0]) if pr['rational'] else '(not rational)'
            if pr['zero']:
                val = '0'
            rel = 'k = n' if k == n else ('k < n' if k < n else 'k > n')
            rec('  %-6s %-3d %-14s %-11s %-22s %s'
                % ('(%d,%d)' % (r['p'], n), k, val,
                   '### ZERO ###' if pr['zero'] else 'nonzero',
                   '%s' % r['trace'][k], rel))
    rec()

    rec('-' * 100)
    rec('### (4) S4 -- (SPEC-1) AT k = n. ### **THE BINDING TEST.**')
    rec('-' * 100)
    allzero = True
    for r in results:
        n = r['n']
        z = r['pair'][n]['zero']
        allzero = allzero and z
        rec('  (%d,%d)  P(n) %s' % (r['p'], n, 'IS EXACTLY ZERO' if z else '### IS NONZERO ###'))
    rec()
    rec('  ### **(SPEC-1) "IT COUNTS FIRST LEVELS": %s**'
        % ('REFUTED AT EVERY CELL -- THE PAIRING VANISHES AT k = n'
           if allzero else 'NOT REFUTED -- F-SPEC1 HAS FIRED'))
    rec()

    rec('-' * 100)
    rec('### (5) S3 -- (SPEC-2) AT k <= n-1.')
    rec('-' * 100)
    nonvac = [r for r in results if not r['spec2_range_empty']]
    rec('  cells where 1 <= k <= n-1 IS AN EMPTY RANGE : %d of %d'
        % (len(results) - len(nonvac), len(results)))
    rec('  ### ### **AT EVERY ODD PLACE b226 PUTS THE UNIT AT LEVEL 1, SO n = 1 AND (SPEC-2) HAS')
    rec('  ### ### NO CELL TO SPEAK ABOUT. ### THE SPEC IS VACUOUS THERE, NOT SATISFIED.**')
    for r in nonvac:
        for s in r['spec2']:
            rec('  (%d,%d) k=%d : pairing*p^{k/2} = %s   act 9 term*p^{k/2} = %s   AGREE: %s'
                % (r['p'], r['n'], s['k'],
                   s['pairing_times_pk2'] if s['pairing_is_rational'] else '(not rational)',
                   s['theta_times_pk2'],
                   'YES' if s['agrees'] else '### NO ###'))
        for s in r['spec2']:
            if not s['pairing_is_rational']:
                red = r['pair'][s['k']]['reduced']
                rec('    ### THE PAIRING\'S EXACT VALUE THERE, ON zeta^0..zeta^{phi(N)-1}:')
                rec('    ###   %s' % ' '.join(str(c) for c in red))
                rec('    ### ### **IT IS NOT A RATIONAL NUMBER. ### act 9\'s TERM IS %s, A'
                    % s['theta_times_pk2'])
                rec('    ### ### RATIONAL. ### THE TWO DO NOT DIFFER IN VALUE; THEY DIFFER IN')
                rec('    ### ### KIND, AND NO CHOICE OF NORMALISATION CLOSES THAT.**')
                # ### AND THE KIND IS IDENTIFIED, EXACTLY, NOT ASSERTED: the element
                # ### x = zeta^2 - zeta^6 satisfies x^2 = 2 in Q(zeta_16), CERTIFIED BY THE
                # ### SAME REDUCER THAT TOOK EVERY OTHER VERDICT IN THIS RUN.
                FF = Field(r['N'])
                x = {2: Fraction(1), 6: Fraction(-1)}
                sq2 = FF.eq(spmul(x, x, r['N']), {0: Fraction(2)})
                claim = spscale(spadd({0: Fraction(1)}, x), Fraction(64, 3))
                same = FF.eq(r['pair'][s['k']]['raw'], claim)
                rec('    ### CERTIFIED EXACTLY: (zeta^2 - zeta^6)^2 = 2 : %s' % ('YES' if sq2 else '### NO ###'))
                rec('    ### CERTIFIED EXACTLY: the pairing = (64/3)(1 + (zeta^2 - zeta^6)) : %s'
                    % ('YES' if same else '### NO ###'))
                if sq2 and same:
                    rec('    ### ### **SO P(1) * 2^{1/2} = (64/3)(1 + 2^{1/2}), AN IRRATIONAL REAL,')
                    rec('    ### ### WHERE act 9\'s TERM IS %s. ### THE MISMATCH IS ALGEBRAIC AND'
                        % s['theta_times_pk2'])
                    rec('    ### ### EXACT, AND IT IS NOT A MATTER OF SCALE.**')
    rec()

    rec('-' * 100)
    rec('### (6) F-NONTRIV -- THE POSITIVE CONTROL AGAINST A TRIVIALLY ZERO OBJECT.')
    rec('-' * 100)
    witnesses = [(r['p'], r['n'], k) for r in results for k in sorted(r['pair'])
                 if not r['pair'][k]['zero']]
    rec('  (cell, k) with P(k) NONZERO : %d' % len(witnesses))
    if witnesses:
        rec('  witnesses : %s' % ', '.join('(%d,%d) k=%d' % w for w in witnesses[:8]))
        rec('  ### **THE PAIRING IS NOT THE ZERO OBJECT. ### ITS VANISHING AT k = n IS A FACT')
        rec('  ### ABOUT k = n, NOT AN ARTEFACT OF A DEAD INSTRUMENT.**')
    else:
        rec('  ### **NO WITNESS. ### THE ACT MEASURED NOTHING AND SAYS SO.**')
    rec()

    rec('-' * 100)
    rec('### (7) F-DISTINCT -- THE DOUBLE-NAME HAZARD, SETTLED BY MEASUREMENT.')
    rec('-' * 100)
    diff = [(r['p'], r['n'], k) for r in results for k in sorted(r['pair'])
            if not r['pair_eq_trace'][k]]
    rec('  ### THE TEST IS ONE EXACT EQUALITY OF REDUCED VECTORS IN Q(zeta_N), NOT A BRANCHING')
    rec('  ### PREDICATE. ### **THE BRANCHING FIRST DRAFT HAD NO ARM FOR A NON-RATIONAL PAIRING')
    rec('  ### AND SO REPORTED AGREEMENT OVER A COMPARISON IT NEVER MADE. ### DECLARED.**')
    rec('  (cell,k) where P(k) AND Tr(U^k S_quot) DISAGREE : %d' % len(diff))
    if diff:
        rec('  %s' % ', '.join('(%d,%d) k=%d' % d for d in diff[:8]))
        rec('  ### **THE PAIRING AND THE TRACE ARE DIFFERENT OBJECTS, PROVED BY MEASUREMENT AND')
        rec('  ### NOT BY ASSERTION. ### THAT IS b227\'s DOUBLE-NAME HAZARD MADE ARITHMETIC.**')
    else:
        rec('  ### **THEY AGREE WHEREVER BOTH WERE COMPUTED. ### THE DISTINCTNESS OF THE TWO')
        rec('  ### OBJECTS THEN RESTS ON THE DERIVATION AT S2, NOT ON A MEASURED DIFFERENCE,')
        rec('  ### AND IS REPORTED AS SUCH.**')
    rec()

    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', '..', 'data', 'b270_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b270_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
