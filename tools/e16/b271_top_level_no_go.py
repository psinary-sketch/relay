# -*- coding: utf-8 -*-
"""b271_top_level_no_go.py -- M-2 CAMPAIGN, ACT 5. ### THE TOP-LEVEL NO-GO.

### THE QUESTION, IN ONE SENTENCE: ### **DOES `E_1` MEMBERSHIP FORCE VANISHING ON THE BALL?**

### THE TWO SPACES THIS ACT REFUSES TO CONFLATE (the registration's hazard (C)):
###   `E_1`      -- the `+1` sector of `M = S/q` on the AMBIENT space `Z/N`, `N = q^2`.
###   `E_1(Son)` -- that sector RESTRICTED to `Son(p,n)`, which carries BALL-VANISHING IN ITS
###                 OWN DEFINITION.
### ### **AN ACT THAT DID NOT SEPARATE THEM WOULD REPORT A THEOREM WHERE THERE IS A TAUTOLOGY.**

### NOTHING HERE IS ADOPTED. ### An exhibited vector is ### A WITNESS TO A CLASS, NOT A
### CANDIDATE ### ; ### **(SPEC-2) AND (SPEC-3) ARE NOT TESTED FOR IT AND ARE NOT SPECULATED
### ABOUT.** ### M-2 remains owed.

### THE ARITHMETIC IS b270's, IMPORTED AS A MODULE RATHER THAN REBUILT, AND `u_v` IS b268's,
### ALSO IMPORTED. ### **NO FLOAT DECIDES ANYTHING HERE.**
"""
import io
import os
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from b268_generator import u_coeffs
from b270_ambient_pairing import (PLACES, Field, ball_of, from_int_vec, orbit_classes,
                                  spadd, spconj, spmul, spscale)


def shift(a, s, N):
    """### MULTIPLICATION BY `zeta^s`: it moves exponents and touches no coefficient."""
    out = {}
    for j, c in a.items():
        k = (j + s) % N
        out[k] = out.get(k, Fraction(0)) + c
    return {k: v for k, v in out.items() if v != 0}


def apply_S(vec, N):
    """### b226's OPERATOR, APPLIED AS A SUM AND NEVER MATERIALIZED AS A MATRIX:
    ### `(S f)(m) = SUM_{m'} f(m') zeta_N^{m m'}`. ### That is why (J2)'s demand is zero."""
    out = []
    for m in range(N):
        acc = {}
        for mp in range(N):
            v = vec[mp]
            if not v:
                continue
            acc = spadd(acc, shift(v, (m * mp) % N, N))
        out.append(acc)
    return out


def in_E1(vec, q, N, F):
    """### `M g = g` MEANS `S g = q g`. ### CHECKED, NEVER ASSUMED FROM PROVENANCE."""
    Sv = apply_S(vec, N)
    for m in range(N):
        if not F.eq(Sv[m], spscale(vec[m], Fraction(q))):
            return False
    return True


def vanishes_on_ball(vec, ballset, F):
    return all(F.is_zero(vec[m]) for m in ballset)


def project(vec, N, ballset, cls_of):
    """### b10's `S_quot`, at content: average within each off-ball orbit class, zero on ball."""
    out = []
    for m in range(N):
        if m in ballset:
            out.append({})
            continue
        C = cls_of[m]
        acc = {}
        for m2 in C:
            acc = spadd(acc, vec[m2])
        out.append(spscale(acc, Fraction(1, len(C))))
    return out


def absorption_functional(f, g, p, n, N):
    """### S1's LEMMA, EVALUATED: ### `SUM_m f(m) * conj( g(p^n m mod N) )`.
    ### **NO HYPOTHESIS IS PLACED ON `f` ANYWHERE IN THIS FUNCTION.**"""
    pn = pow(p, n, N)
    acc = {}
    for m in range(N):
        if not f[m]:
            continue
        acc = spadd(acc, spmul(f[m], spconj(g[(pn * m) % N], N), N))
    return acc


def run_cell(p, ell):
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

    # ### THE VECTORS. ### `u_v` is b268's, IMPORTED. ### `g` is the registered witness.
    u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]
    g = [({0: Fraction(2 * q + 2)} if m == 0 else {0: Fraction(2)}) for m in range(N)]
    e0 = [({0: Fraction(1)} if m == 0 else {}) for m in range(N)]
    e1 = [({0: Fraction(1)} if m == 1 % N else {}) for m in range(N)]
    ones = [{0: Fraction(1)} for _ in range(N)]

    r = {'p': p, 'n': n, 'q': q, 'N': N, 'nball': len(ballset)}

    # --- F-CTRL (c): THE `E_1` TEST MUST BITE IN BOTH DIRECTIONS. ----------------------------
    r['E1_u'] = in_E1(u, q, N, F)        # ### must be TRUE  -- a known member
    r['E1_g'] = in_E1(g, q, N, F)        # ### must be TRUE  -- the witness, CHECKED
    r['E1_e1'] = in_E1(e1, q, N, F)      # ### must be FALSE -- or the test proves nothing

    # --- F-CTRL (a),(b): THE BALL-VANISHING DETECTOR MUST BITE IN BOTH DIRECTIONS. -----------
    r['ball_u'] = vanishes_on_ball(u, ballset, F)    # ### must be TRUE
    r['ball_g'] = vanishes_on_ball(g, ballset, F)    # ### must be FALSE
    r['ball_e0'] = vanishes_on_ball(e0, ballset, F)  # ### must be FALSE

    # ### AND THE WITNESS MUST BE NONZERO AS A VECTOR (F-ESCAPE (ii)).
    r['g_nonzero'] = any(not F.is_zero(x) for x in g)
    # ### AND NONZERO AT SOME BALL POINT (F-ESCAPE (iii)), NAMED EXPLICITLY.
    r['g_ball_witness'] = [m for m in sorted(ballset) if not F.is_zero(g[m])][:3]

    # --- S1: THE LEMMA, IN BOTH POLARITIES (F-LEMMA). ---------------------------------------
    # ### WITH TWO DIFFERENT `f`, TO SHOW `f` IS GENUINELY UNCONSTRAINED.
    r['lemma_u_ones'] = F.is_zero(absorption_functional(ones, u, p, n, N))
    r['lemma_u_u'] = F.is_zero(absorption_functional(u, u, p, n, N))
    r['lemma_g_ones'] = F.is_zero(absorption_functional(ones, g, p, n, N))

    # --- S2b: IS THE ESCAPE MATERIAL? ### A PROPERTY OF THE CLASS, NOT A CANDIDATE. ----------
    Sg = project(g, N, ballset, cls_of)
    pair = absorption_functional(Sg, g, p, n, N)
    r['pair_zero'] = F.is_zero(pair)
    red = F.reduce(pair)
    r['pair_rational'] = all(c == 0 for c in red[1:])
    r['pair_value'] = red[0] if r['pair_rational'] else None
    r['pair_predicted'] = Fraction(4 * (N - q))
    r['pair_matches'] = (r['pair_rational'] and red[0] == r['pair_predicted'])

    # ### AND THE SAME PAIRING FOR b268's `u_v`, WHICH b270 FOUND ZERO -- CARRIED HERE ONLY AS
    # ### THE LEMMA'S NEGATIVE POLARITY, ### NOT AS A RE-VERDICT OF b270 (b246).
    Su = project(u, N, ballset, cls_of)
    r['pair_u_zero'] = F.is_zero(absorption_functional(Su, u, p, n, N))

    # --- THE ESCAPE CLASS, NAMED BY ITS PROPERTIES RATHER THAN GESTURED AT. -----------------
    # ### b226's `Son` demands BOTH halves: vanishing on the ball AND its TRANSFORM IMAGE
    # ### vanishing there. ### The witness is an EIGENVECTOR (`S g = q g`), so its transform is
    # ### a nonzero multiple of itself and ### **BOTH HALVES FAIL AT ONCE, FOR ONE REASON.**
    Sgt = apply_S(g, N)
    r['son_half1'] = vanishes_on_ball(g, ballset, F)      # ### expected FALSE
    r['son_half2'] = vanishes_on_ball(Sgt, ballset, F)    # ### expected FALSE
    r['transform_is_multiple'] = all(
        F.eq(Sgt[m], spscale(g[m], Fraction(q))) for m in range(N))
    return r


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b271 -- COMPONENT 1. ### THE TOP-LEVEL NO-GO, DERIVED. ### EXACT ARITHMETIC IN Q(zeta_N).')
    rec('### REGISTRATION data/b271_registration_2026-08-31.txt SEALED 3e2469d0 BEFORE ANY VALUE.')
    rec('### **THE QUESTION: DOES `E_1` MEMBERSHIP FORCE VANISHING ON THE BALL?**')
    rec('### **NOTHING IS ADOPTED. ### AN EXHIBITED VECTOR IS A WITNESS TO A CLASS.**')
    rec('=' * 100)
    rec()

    results = [run_cell(p, ell) for (p, ell) in PLACES]

    rec('-' * 100)
    rec('### (1) F-CTRL -- THE CONTROLS, RUN BEFORE THE DERIVATION IS BELIEVED.')
    rec('### **THE CONTROL CHECKS THE DERIVATION AND IS NEVER ITS EVIDENCE.**')
    rec('-' * 100)
    rec('  %-7s %-4s %-6s | %-9s %-9s %-10s | %-11s %-11s %s'
        % ('(p,n)', 'q', 'N', 'E1: u_v', 'E1: g', 'E1: e_1', 'ball: u_v', 'ball: g', 'ball: e_0'))
    rec('  %-7s %-4s %-6s | %-9s %-9s %-10s | %-11s %-11s %s'
        % ('', '', '', 'want YES', 'want YES', 'want NO', 'want YES', 'want NO', 'want NO'))
    for r in results:
        rec('  %-7s %-4d %-6d | %-9s %-9s %-10s | %-11s %-11s %s'
            % ('(%d,%d)' % (r['p'], r['n']), r['q'], r['N'],
               'YES' if r['E1_u'] else '### NO ###',
               'YES' if r['E1_g'] else '### NO ###',
               'NO' if not r['E1_e1'] else '### YES ###',
               'YES' if r['ball_u'] else '### NO ###',
               'NO' if not r['ball_g'] else '### YES ###',
               'NO' if not r['ball_e0'] else '### YES ###'))
    ctrl_ok = all(r['E1_u'] and r['E1_g'] and (not r['E1_e1'])
                  and r['ball_u'] and (not r['ball_g']) and (not r['ball_e0'])
                  for r in results)
    rec()
    rec('  ### **ALL SIX CONTROLS BEHAVE AS REQUIRED AT ALL %d CELLS: %s**'
        % (len(results), 'YES' if ctrl_ok else '### NO -- THE INSTRUMENT IS NOT TRUSTED ###'))
    rec('  ### The `E_1` test ACCEPTS a known member and REJECTS `e_1`; the ball detector')
    rec('  ### ACCEPTS `u_v` and REJECTS `e_0`. ### **A TEST THAT ONLY EVER SAYS YES IS NOT A')
    rec('  ### TEST, WHICH IS WHY BOTH POLARITIES ARE RUN AT EVERY CELL.**')
    rec()

    rec('-' * 100)
    rec('### (2) S1 -- THE BALL-ABSORPTION LEMMA, IN BOTH POLARITIES.')
    rec('-' * 100)
    rec('  LEMMA. ### N = p^{2n}; B = { m : p^n | m }; g vanishing on B; ### **f ARBITRARY, WITH')
    rec('  NO HYPOTHESIS ON IT WHATEVER.** ### THEN SUM_m f(m) conj( g(p^n m) ) = 0.')
    rec('  PROOF. p^n m is a multiple of p^n for EVERY m, so it lies in B for every m, so every')
    rec('  factor conj(g(p^n m)) is 0. ### **THE SUM IS ZERO TERMWISE, NOT BY CANCELLATION.**')
    rec()
    rec('  %-7s %-22s %-22s %s'
        % ('(p,n)', 'f=ones, g=u_v (0?)', 'f=u_v, g=u_v (0?)', 'f=ones, g=witness (0?)'))
    for r in results:
        rec('  %-7s %-22s %-22s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               'ZERO' if r['lemma_u_ones'] else '### NONZERO ###',
               'ZERO' if r['lemma_u_u'] else '### NONZERO ###',
               'NONZERO' if not r['lemma_g_ones'] else '### ZERO ###'))
    # ### ONE UNAMBIGUOUS LINE FOR S1's POLARITY, so a gate reads a fact and not a table row.
    lem = sum(1 for r in results
              if r['lemma_u_ones'] and r['lemma_u_u'] and (not r['lemma_g_ones']))
    rec()
    rec('  ### S1 VERDICT: %s at %d of %d cells'
        % ('lemma holds in BOTH polarities' if lem == len(results)
           else 'LEMMA POLARITY FAILED', lem, len(results)))
    rec('  ### **TWO DIFFERENT `f` GIVE ZERO AGAINST A BALL-VANISHING `g`, AND THE SAME `f`')
    rec('  ### GIVES NONZERO AGAINST A `g` THAT DOES NOT VANISH THERE. ### THE LEMMA IS MEASURING')
    rec('  ### ITS HYPOTHESIS AND NOT ITS INSTRUMENT.**')
    rec()

    rec('-' * 100)
    rec('### (3) S2 -- THE FORCING QUESTION. ### **DOES `E_1` MEMBERSHIP FORCE BALL-VANISHING?**')
    rec('-' * 100)
    rec('  THE WITNESS, IN CLOSED FORM FROM b226\'s OWN IDENTITY 4q P_1 = (q + S)(1 + Pi):')
    rec('    Pi e_0 = e_0, so (1 + Pi) e_0 = 2 e_0;  (S e_0)(m) = zeta^0 = 1, so S e_0 = 1.')
    rec('    ### **g := 4q P_1 e_0 = 2q e_0 + 2 * 1,  i.e.  g(m) = 2q [m = 0] + 2.**')
    rec('  MEMBERSHIP IS CHECKED, NOT INHERITED FROM PROVENANCE: (S g)(m) = 2q + 2N [m=0] and')
    rec('  q g(m) = 2N [m=0] + 2q, using q^2 = N. ### **THEY AGREE, SO M g = g.**')
    rec()
    rec('  %-7s %-12s %-12s %-22s %s'
        % ('(p,n)', 'M g = g?', 'g nonzero?', 'ball points g != 0', 'forces ball-vanishing?'))
    for r in results:
        rec('  %-7s %-12s %-12s %-22s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               'YES' if r['E1_g'] else '### NO ###',
               'YES' if r['g_nonzero'] else '### NO ###',
               ','.join(str(m) for m in r['g_ball_witness']),
               '### NO ###' if not r['ball_g'] else 'yes'))
    rec()
    escape = all(r['E1_g'] and r['g_nonzero'] and (not r['ball_g']) for r in results)
    rec('  ### ### **F-BARRIER: %s**'
        % ('THE BARRIER IS REFUTED FOR THE AMBIENT `E_1`. ### ONE WITNESS SUFFICES, AND THERE '
           'ARE EIGHT.' if escape else 'NO WITNESS FOUND -- THE BARRIER STANDS ON THIS AXIS.'))
    rec('  ### **`g` VANISHES NOWHERE AT ALL, SO IT IS NOT A NEAR MISS.**')
    rec()

    rec('-' * 100)
    rec('### (4) S2b -- IS THE ESCAPE MATERIAL, OR MERELY FORMAL?')
    rec('### **A PROPERTY OF THE CLASS. ### NOT A CANDIDATE. ### NOT A TABLE HEADED BY act 9.**')
    rec('-' * 100)
    rec('  %-7s %-26s %-20s %-10s %s'
        % ('(p,n)', '<U^n S_quot g, g> p^{n/2}', 'predicted 4(N-q)', 'agrees?', 'same for u_v'))
    for r in results:
        rec('  %-7s %-26s %-20s %-10s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               ('0' if r['pair_zero'] else
                (str(r['pair_value']) if r['pair_rational'] else '(not rational)')),
               str(r['pair_predicted']),
               'YES' if r['pair_matches'] else '### NO ###',
               'ZERO' if r['pair_u_zero'] else '### NONZERO ###'))
    rec()
    material = all((not r['pair_zero']) and r['pair_matches'] for r in results)
    rec('  ### ### **%s**'
        % ('THE ESCAPE IS MATERIAL: THE WITNESS GIVES A NONZERO VALUE AT k = n AT EVERY CELL, '
           'AND IT MATCHES THE CLOSED FORM REGISTERED BEFORE IT WAS COMPUTED.' if material
           else 'THE ESCAPE IS FORMAL ONLY -- THE WITNESS GIVES ZERO AT k = n.'))
    rec('  ### The `u_v` column is b268/b270\'s vector, carried ONLY as the lemma\'s negative')
    rec('  ### polarity. ### **IT IS NOT A RE-VERDICT OF b270** (b246); b270\'s verdict stands.')
    rec()

    rec('-' * 100)
    rec('### (5) THE TWO SPACES, KEPT APART. ### **THE HALF THAT IS A TAUTOLOGY.**')
    rec('-' * 100)
    rec('  b226 defines Son(p,n) as ### "the vectors on Z/p^{2n} vanishing on a ball AND on its')
    rec('  transform image". ### **SO EVERY VECTOR OF Son VANISHES ON THE BALL BY DEFINITION,')
    rec('  ### AND S1 THEN GIVES ZERO AT k = n FOR EVERY ONE OF THEM.**')
    rec('  ### ### **THAT IS A NO-GO, AND ITS SCOPE IS `Son(p,n)` -- NOT `E_1`, NOT THE MODEL.**')
    rec('  ### ### **IT IS A TAUTOLOGY AND NOT A THEOREM, AND IT IS REPORTED AS ONE.**')
    rec('  ### ### **IT COVERS EVERY SONIN UNIT AND NOT ONLY b226\'s f_{1,1}, WHICH IS THE ONE')
    rec('  ### ### THING IT ADDS BEYOND b270.**')
    rec()

    rec('-' * 100)
    rec('### (6) THE ESCAPE CLASS, NAMED BY ITS PROPERTIES. ### **NOT SURVEYED, AND SAID SO.**')
    rec('-' * 100)
    rec('  %-7s %-20s %-24s %s'
        % ('(p,n)', 'g vanishes on ball', 'S g vanishes on ball', 'S g = q g exactly'))
    for r in results:
        rec('  %-7s %-20s %-24s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               'NO' if not r['son_half1'] else '### YES ###',
               'NO' if not r['son_half2'] else '### YES ###',
               'YES' if r['transform_is_multiple'] else '### NO ###'))
    both = all((not r['son_half1']) and (not r['son_half2']) for r in results)
    rec()
    rec('  ### **THE WITNESS FAILS BOTH HALVES OF b226\'s `Son` AT ONCE, AND FOR ONE REASON:')
    rec('  ### IT IS AN EIGENVECTOR, `S g = q g`, SO ITS TRANSFORM IS A NONZERO MULTIPLE OF')
    rec('  ### ITSELF AND CANNOT VANISH WHERE IT DOES NOT: %s**' % ('CONFIRMED' if both else '### NOT CONFIRMED ###'))
    rec('  ### ### **SO THE CLASS THAT ESCAPES IS `E_1` MINUS `Son` -- THE `+1` SECTOR WITH')
    rec('  ### ### NONZERO BALL MASS. ### THAT IS AN ADDRESS, NOT A CANDIDATE.**')
    rec('  ### **WHAT THIS ACT DOES NOT DO: IT DOES NOT SURVEY THE CLASS.** ### One witness was')
    rec('  ### exhibited because one witness is what a refutation needs. ### **WHETHER THE CLASS')
    rec('  ### STILL HAS MEMBERS AFTER ANY FURTHER CONDITION IS IMPOSED IS NOT TESTED HERE, AND')
    rec('  ### (SPEC-2) AND (SPEC-3) ARE NOT TESTED FOR ANY MEMBER OF IT.**')
    rec()

    io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         '..', '..', 'data', 'b271_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b271_run.txt')
    print('  ### SUMMARY: controls_ok=%s  escape=%s  material=%s' % (ctrl_ok, escape, material))
    return 0


if __name__ == '__main__':
    sys.exit(main())
