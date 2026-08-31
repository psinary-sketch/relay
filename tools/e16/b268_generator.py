# -*- coding: utf-8 -*-
"""b268_generator.py -- M-2 CAMPAIGN ACT 2 (A1). ### THE GENERATOR'S NONVANISHING. ### THE RUN.

### **A DERIVATION AT CONTENT WITH EXACT BENCH CONTROLS.** ### Bars fixed in
### `data/b268_registration_2026-08-31.txt`, SEALED `119973a1...`, term-scanned and
### satisfiability-checked BEFORE the seal.

### ### **F-EXACT IS THE ACT'S SPINE: EVERY VANISHING TEST IS REDUCTION MODULO THE CYCLOTOMIC
### ### POLYNOMIAL ON INTEGER COEFFICIENTS. ### NO FLOAT DECIDES ANYTHING.** ### b223's standard:
### *"NO FLOATING POINT ENTERS ANY d_1."*
"""
import io
import json
import os
import re
import sys

from sympy import Poly, cyclotomic_poly, symbols

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
RES = r'D:\SIDE-global-section'
BANK = os.path.join(D, 'b268_run.txt')
ROWS = os.path.join(D, 'b268_rows.json')

X = symbols('x')

# ### THE OWNER QUOTATIONS THIS ACT LEANS ON. ### (label, file, quotation)
QUOTES = [
    ('b226, the chosen level', os.path.join(D, 'b226_stated_choice.txt'),
     'ell(p) := 2 if p = 2, else 1'),
    ('b226, the owed step', os.path.join(D, 'b226_stated_choice.txt'),
     'd_1 > 0 GIVES E_1 != 0. ### IT DOES NOT GIVE u_{1,1} != 0.'),
    ('b226, the generic odd place is owed', os.path.join(D, 'b226_stated_choice.txt'),
     'PASS AT SIX STATED PLACES; THE GENERIC ODD PLACE IS *OWED*.'),
    ('b226, the purity identity', os.path.join(D, 'b226_stated_choice.txt'),
     '4q P_1   = (q + S)(1 + Pi)'),
    ('b226, f_{i,j}', os.path.join(D, 'b226_stated_choice.txt'),
     'f_{i,j}  = e_{i+qj} - e_i,  i,j in [1,q)'),
    ('b226, S', os.path.join(D, 'b226_stated_choice.txt'),
     '(S f)(m) = SUM_{m\'} f(m\') zeta_N^{m m\'},  N = q^2'),
    ('b226, Pi and M', os.path.join(D, 'b226_stated_choice.txt'),
     '(Pi f)(m) = f(-m);  S^2 = q^2 Pi, so M := S/q has M^4 = 1'),
    ('b226, the support observation', os.path.join(D, 'b226_stated_choice.txt'),
     'the support is N - q at all six cells.'),
    ('b226, exact in Z[zeta_N]', os.path.join(D, 'b226_stated_choice.txt'),
     'S u = q u CHECKED EXACTLY IN Z[zeta_N], ENTRY BY ENTRY'),
    ('b223, no floating point', os.path.join(D, 'b223_level_limit_two_places.txt'),
     'NO FLOATING POINT ENTERS ANY d_1.'),
    ('b223, the arrival death', os.path.join(D, 'b223_level_limit_two_places.txt'),
     'NO UNIT: d_1 = 0, the arrival depth'),
    ('kernel, the arrival death is the law own value',
     os.path.join(RES, 'Core', 'SectorNonvanishingShadow.lean'),
     "The death at `(2,1)` is the law's OWN value."),
]

# ### THE REGISTERED PLACES. ### (p, level) -- six b226-measured plus two unmeasured odd.
PLACES = [(2, 2), (3, 1), (5, 1), (7, 1), (11, 1), (13, 1), (17, 1), (19, 1)]
B226_SUPPORT = {2: 12, 3: 6, 5: 20, 7: 42, 11: 110, 13: 156}   # ### b226's table, quoted


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


class Cyc(object):
    """### EXACT ARITHMETIC IN `Z[zeta_N]`. ### An element is an integer coefficient vector on
    ### `zeta^0 .. zeta^{N-1}`; it is ZERO iff the polynomial is divisible by `Phi_N` in `Z[x]`.
    ### ### **NO FLOAT ANYWHERE IN THIS CLASS.**"""

    def __init__(self, N):
        self.N = N
        self.phi = Poly(cyclotomic_poly(N, X), X)

    def is_zero(self, coeffs):
        """`coeffs[j]` = integer coefficient of `zeta^j`."""
        if all(c == 0 for c in coeffs):
            return True
        p = Poly(list(reversed(coeffs)), X)          # ### Poly takes highest-degree first
        return p.rem(self.phi).is_zero


def u_coeffs(q, m):
    """### THE GENERATOR'S VALUE AT `m`, AS AN INTEGER VECTOR OVER `zeta_N`.
    ### From the BANKED identity `4q P_1 = (q + S)(1 + Pi)` applied to `f = e_{1+q} - e_1`:
    ###   `u(m) = q*[(1+Pi)f](m) + ( zeta^{m(1+q)} + zeta^{-m(1+q)} - zeta^{m} - zeta^{-m} )`."""
    N = q * q
    a = (1 + q) % N
    c = [0] * N
    # ### the delta part: q * [(1+Pi)f](m), with (1+Pi)f = e_{1+q} - e_1 + e_{-(1+q)} - e_{-1}
    if m == a:
        c[0] += q
    if m == 1 % N:
        c[0] -= q
    if m == (-a) % N:
        c[0] += q
    if m == (-1) % N:
        c[0] -= q
    # ### the transform part
    c[(m * a) % N] += 1
    c[(-m * a) % N] += 1
    c[m % N] -= 1
    c[(-m) % N] -= 1
    return c


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b268 RUN -- M-2 CAMPAIGN ACT 2 (A1). ### THE GENERATOR\'S NONVANISHING.')
    rec('### Registration SEALED (`119973a1...`), TERM-SCANNED and SATISFIABILITY-CHECKED')
    rec('### ### **BEFORE** ### the seal. ### Ordered by `RULE M2-ORDER: A1 then A2`.')
    rec('### ### **NO AGGREGATION IS ADOPTED, STATED OR REALIZED. ### M-2 REMAINS OWED.**')
    rec('=' * 100)

    # ============================================================ F-QUOTE
    rec('')
    rec('### F-QUOTE -- EVERY OWNER SENTENCE VERBATIM, BEFORE ANY VERDICT IS EMITTED.')
    rec('=' * 100)
    cache, bad = {}, []
    for label, path, q in QUOTES:
        if path not in cache:
            cache[path] = norm(io.open(path, encoding='utf-8', errors='replace').read())
        ok = norm(q) in cache[path]
        if not ok:
            bad.append((label, path, q))
        rec('  %-48s %s' % (label[:48], 'YES' if ok else '### NOT FOUND ###'))
    fquote = (len(bad) == 0)
    for label, path, q in bad:
        rec('    ### NOT FOUND in %s : %r' % (os.path.basename(path), q[:80]))
    tampered = norm(QUOTES[3][2]).replace('(q + S)', '(q + SX)')
    ctrl_q = tampered not in cache[QUOTES[3][1]]
    rec('  ### **%d quotations, %d unfindable.**' % (len(QUOTES), len(bad)))
    rec('  (C1) an altered quotation is reported unfindable : ### **%s**' % ('YES' if ctrl_q else 'NO'))
    rec('  ### ### **F-QUOTE %s**'
        % ('DID NOT FIRE.' if fquote else 'FIRED. ### NO VERDICT IS EMITTED BELOW.'))

    # ============================================================ F-EXACT control
    rec('')
    rec('=' * 100)
    rec('### F-EXACT -- THE EXACT TESTER, POSITIVE-CONTROLLED BEFORE IT IS TRUSTED.')
    rec('=' * 100)
    c9 = Cyc(9)
    known_zero = [0] * 9
    known_zero[0] = 1
    known_zero[3] = 1
    known_zero[6] = 1                       # ### 1 + zeta^3 + zeta^6 = 0 in Z[zeta_9]
    known_nonzero = [0] * 9
    known_nonzero[0] = 1                    # ### 1 != 0
    z_ok = c9.is_zero(known_zero)
    nz_ok = not c9.is_zero(known_nonzero)
    fexact = bool(z_ok and nz_ok)
    rec('  a KNOWN-ZERO element   `1 + z^3 + z^6` in Z[z_9] : reported %s (must be zero)'
        % ('ZERO' if z_ok else '### NONZERO ###'))
    rec('  a KNOWN-NONZERO element `1`            in Z[z_9] : reported %s (must be nonzero)'
        % ('NONZERO' if nz_ok else '### ZERO ###'))
    rec('  ### ### **F-EXACT %s** ### -- the tester can say both.'
        % ('DID NOT FIRE' if fexact else 'FIRED'))

    # ============================================================ S1 / the control table
    rec('')
    rec('=' * 100)
    rec('### S1 + THE CONTROL -- THE SUPPORT, COMPUTED EXACTLY AT EVERY REGISTERED PLACE.')
    rec('###        **THE DERIVATION IS AT (C) OF THE REGISTRATION. ### THIS TABLE IS A CHECK ON')
    rec('###        IT AND NEVER ITS EVIDENCE.**')
    rec('=' * 100)
    rec('  %-6s %-7s %-5s %-6s %-9s %-9s %-8s %-8s %s'
        % ('p', 'level', 'q', 'N', 'support', 'N - q', 'agree', 'b226', 'u_p != 0'))
    rec('  ' + '-' * 86)
    rows, all_agree, all_nonzero, b226_agree = [], True, True, True
    for p, lev in PLACES:
        q = p ** lev
        N = q * q
        cyc = Cyc(N)
        supp = 0
        for m in range(N):
            if not cyc.is_zero(u_coeffs(q, m)):
                supp += 1
        agree = (supp == N - q)
        nonzero = (supp > 0)
        all_agree = all_agree and agree
        all_nonzero = all_nonzero and nonzero
        banked = B226_SUPPORT.get(p if lev == 1 or p == 2 else None)
        bmatch = '--' if banked is None else ('YES' if banked == supp else '### NO ###')
        if banked is not None and banked != supp:
            b226_agree = False
        rows.append(dict(p=p, level=lev, q=q, N=N, support=supp, target=N - q,
                         agree=agree, banked=banked, nonzero=nonzero))
        rec('  %-6d %-7d %-5d %-6d %-9d %-9d %-8s %-8s %s'
            % (p, lev, q, N, supp, N - q, agree, str(banked) if banked else '--',
               'YES' if nonzero else '### NO ###'))
    rec('')
    rec('  ### **EVERY ENTRY DECIDED BY REDUCTION MODULO `Phi_N` ON INTEGER COEFFICIENTS.**')
    rec('  ### **NO FLOATING POINT ENTERS ANY CELL OF THIS TABLE.**')
    rec('  ### **support = N - q at every registered place : ### %s ###**' % all_agree)
    rec('  ### **reproduces b226\'s six measured cells      : ### %s ###**' % b226_agree)
    rec('  ### **`u_p != 0` at every registered place       : ### %s ###**' % all_nonzero)
    rec('  ### ### **AND THE TWO UNMEASURED ODD PRIMES `p = 17, 19` WERE RUN, NOT REFUSED --')
    rec('  ### ### SO THE CONTROL IS NOT CONFINED TO THE CELLS THE FORMULA WAS SEEN ON.**')

    # ============================================================ S2 / S3
    rec('')
    rec('=' * 100)
    rec('### S2 / S3 -- WHAT THE SUPPORT GIVES, AND WHAT IT DOES NOT.')
    rec('=' * 100)
    rec('  ### **S2. ### `support > 0` IS EXACTLY `u_p != 0`.** ### A support is the count of `m`')
    rec('  ### at which the vector is nonzero; positive support IS a nonvanishing vector.')
    rec('  ### **AND `u_p` IS THE IMAGE OF `f_{1,1}` UNDER `4q P_1`, SO ITS NONVANISHING ### IS ###')
    rec('  ### THE `(1,1)` GENERATOR\'S NONVANISHING.**')
    rec('  ### ### **THIS SEAT REGISTERED A DISAGREEMENT WITH THE FERRY\'S FRAMING AT (F) AND IT')
    rec('  ### ### STANDS: the ferry asks S2 to derive that support forces "the (1,1) component')
    rec('  ### ### nonzero", ### AS THOUGH THERE WERE A SECOND STEP. ### THERE IS NOT. ### THE TWO')
    rec('  ### ### ARE THE SAME STATEMENT, AND MANUFACTURING A STEP BETWEEN THEM WOULD BE A')
    rec('  ### ### DOUBLE-NAME ERROR IN THE OTHER DIRECTION.**')
    rec('')
    rec('  ### **S3. ### FOR ODD `p` AT LEVEL 1: `N - q = q^2 - q = q(q-1)`, AND `q = p >= 3`,**')
    rec('  ### ### **SO `support = q(q-1) >= 6 > 0` AND `u_p != 0`. ### AT EVERY ODD PRIME.**')
    rec('  ### **GRADE: ### DERIVES-on-IMP ### , AND THE IMPORTS ARE NAMED AND ARE ALL OWNERS\':**')
    rec('  ###   (i) the objects as b226 defines them (`f_{i,j}`, `S`, `Pi`, `P_1`, `N = q^2`);')
    rec('  ###   (ii) ### **THE BANKED PURITY IDENTITY `4q P_1 = (q + S)(1 + Pi)`** ### -- b226\'s')
    rec('  ###        own line, attributed to the purity report. ### **NOT THIS ACT\'S.**')
    rec('  ###   (iii) elementary congruence arithmetic, which imports nothing.')
    rec('  ### ### **NO NEW IMPORT IS INTRODUCED.**')
    rec('')
    rec('  ### ### ### **AND THE BOUNDARY, REGISTERED BEFORE THE RESULT AND KEPT AFTER IT:**')
    rec('  ### ### ### **A SUPPORT IS NOT A CONTRIBUTION. ### (SPEC-1) WOULD READ A NUMBER THE')
    rec('  ### ### ### AGGREGATION USES; THIS ACT SUPPLIES A VECTOR THAT IS NOT ZERO. ### b226\'s')
    rec('  ### ### ### STEP IS PAID; (SPEC-1) IS NOT TOUCHED.**')

    # ============================================================ p = 2
    rec('')
    rec('=' * 100)
    rec('### p = 2, STATED SEPARATELY AND NOT FOLDED INTO THE ODD RESULT.')
    rec('=' * 100)
    rec('  ### **`d_1(2,1) = 0` IS THE PLACE-2 LAW\'S OWN VALUE** (`4 d_1 = q(q-2)` at `q = 2`),')
    rec('  ### and the kernel says so: ### **"The death at `(2,1)` is the law\'s OWN value."**')
    rec('  ### **SO LEVEL 1 AT `p = 2` HAS NO DATUM AND NO UNIT TO CHOOSE**, and b226\'s step-up')
    rec('  ### `ell(2) = 2` is the corpus\'s answer.')
    rec('  ### **AND THE ODD ARGUMENT DOES NOT COVER IT, BY ITS OWN HINGE:** ### S1\'s second')
    rec('  ### congruence collapses because `gcd(q+2, q^2) = 1` ### FOR ODD `q` ### . ### At')
    rec('  ### `q = 4`, `gcd(6, 16) = 2` and the collapse fails -- ### **THE COUNT STILL LANDS ON')
    rec('  ### `N - q = 12`, BUT BY A DIFFERENT ROUTE, AND THE TABLE ABOVE SHOWS IT.**')
    rec('  ### ### **THEREFORE ANY GENERAL STATEMENT MUST READ: "AT EVERY ODD `p` AT LEVEL 1, AND')
    rec('  ### ### AT `p = 2` AT LEVEL 2." ### "AT EVERY PRIME AT LEVEL 1" WOULD BE FALSE.**')
    rec('  ### **WHAT (SPEC-3) INHERITS -- A CONDITION ON CANDIDATES, NOT A CANDIDATE:** ### any')
    rec('  ### aggregation reading a first-level datum must carry the step-up or an equivalent,')
    rec('  ### ### **OR BE UNDEFINED AT `p = 2`, WHICH FAILS (SPEC-3) OUTRIGHT.**')

    # ============================================================ VERDICTS
    fs3 = bool(all_nonzero and all_agree and b226_agree)
    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 100)
    rec('  F-QUOTE  (owner sentences verbatim)  : ### **%s**' % ('DID NOT FIRE' if fquote else 'FIRED'))
    rec('  F-EXACT  (tester says both)          : ### **%s**' % ('DID NOT FIRE' if fexact else 'FIRED'))
    rec('  F-SUPPORT(derivation vs b226\'s six)  : ### **%s**' % ('DID NOT FIRE' if b226_agree else 'FIRED'))
    rec('  F-S3     (u_p != 0 at every place)   : ### **%s**' % ('DID NOT FIRE' if fs3 else 'FIRED'))
    rec('')
    rec('  ### ### **b226\'s OWED STEP: ### %s ###**'
        % ('PAID -- 4q P_1 f_{1,1} != 0 at every odd p at level 1, DERIVED and exactly controlled'
           if fs3 else 'NOT PAID -- see the firing above'))
    rec('  ### **M-2 REMAINS ### SPECIFIED-NOT-STATED ### . ### NO AGGREGATION IS ADOPTED.**')
    rec('  ### **QUOTED-N: %d owner quotations; %d places computed exactly in Z[zeta_N];'
        % (len(QUOTES), len(rows)))
    rec('  ###   %d total `m` values reduced modulo Phi_N.**' % sum(r['N'] for r in rows))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(f_quote=fquote, unfindable=len(bad), control_quote=ctrl_q,
                   f_exact=fexact, rows=rows, all_agree=all_agree,
                   b226_agree=b226_agree, all_nonzero=all_nonzero, f_s3=fs3,
                   total_m=sum(r['N'] for r in rows)),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0 if (fquote and fexact and fs3) else 1


if __name__ == '__main__':
    sys.exit(main())
