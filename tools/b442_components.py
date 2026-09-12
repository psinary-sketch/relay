# -*- coding: utf-8 -*-
"""b442_components.py -- THE COMPONENTS. ### **RUN AFTER THE LOCK, NEVER BEFORE.**

### ### **COMPONENT 1** -- u0 against theta's minimum: the argmin located from theta's VALUES alone, theta
### at u0 by two routes that share no code, oddness and the one-zero pattern measured.
### ### **COMPONENT 2** -- site (v): the cell first, ten candidates at b424's three steps, the boundary
### count at five sites from banked JSON.
### ### **COMPONENT 3** -- b440's two corrections, in b441's words, verified; written into the row by
### `b442_desk_bank.py`.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
LED = os.path.join(PP, 'FACES_LEDGER.md')
OUT = os.path.join(D, 'b442_components.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, MISS = [], []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('=' * 100)
    rec('  ### ### **%s -- %s**' % (n, t))
    rec('=' * 100)


def sub(t):
    rec('')
    rec('-' * 100)
    rec('  ### %s' % t)
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def wrap(s, n=84):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, clip=500, span=None):
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('      %s:%d' % (os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                seg = b.strip()
                if span:
                    j = seg.find(needle)
                    seg = seg[j:j + span]
                for c in wrap(seg[:clip], 82):
                    rec('        | %s' % c)
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), needle[:50]))
    rec('      ### **NOT LOCATED** : %s' % needle[:60])
    return None


# ### ==============================================================================================
def component_1():
    head('COMPONENT 1', 'IS u0 THE MINIMUM OF THE RIEMANN-SIEGEL theta?')
    from mpmath import mp, mpf, mpc, log, pi, digamma, loggamma, quad, im, re as mre
    mp.dps = 40

    def theta(t):                                   # ### ROUTE B -- loggamma, no quadrature, no digamma
        return im(loggamma(mpc(mpf(1) / 4, mpf(t) / 2))) - (mpf(t) / 2) * log(pi)

    def hplus(u):
        return mre(digamma(mpc(mpf(1) / 4, mpf(u) / 2))) - log(pi)

    u0b = mpf(json.loads(read(os.path.join(D, 'b440_u0.json')))['u0'])
    rec('    ### u0 as banked by b440 (the root of h+) : %s' % mp.nstr(u0b, 30))

    sub('(a) THE ARGMIN FROM theta`S VALUES ALONE -- GOLDEN SECTION, NO h+ (face, BAR 5)')
    a, b = mpf(5), mpf(8)
    g = (mp.sqrt(5) - 1) / 2
    c, d = b - g * (b - a), a + g * (b - a)
    fc, fd = theta(c), theta(d)
    it = 0
    while b - a > mpf('1e-30') and it < 400:
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - g * (b - a)
            fc = theta(c)
        else:
            a, c, fc = c, d, fd
            d = a + g * (b - a)
            fd = theta(d)
        it += 1
    am = (a + b) / 2
    gap = abs(am - u0b)
    rec('      golden-section argmin on [5, 8] : %s   (%d iterations)' % (mp.nstr(am, 25), it))
    rec('      |argmin - u0|                    : %.3e   against the stated 1e-12' % float(gap))
    ok_arg = gap < mpf('1e-12')

    sub('(b) theta AT u0 BY TWO ROUTES THAT SHARE NO CODE')
    tB = theta(u0b)
    tA = quad(lambda u: hplus(u) / 2, [0, u0b])
    rec('      route B  loggamma            theta(u0) = %s' % mp.nstr(tB, 25))
    rec('      route A  quad over digamma/2 theta(u0) = %s' % mp.nstr(tA, 25))
    rec('      |A - B|                                 = %.3e   against the stated 1e-12' % float(abs(tA - tB)))
    ok_val = abs(tA - tB) < mpf('1e-12')
    rec('      theta at the argmin, route B          = %s' % mp.nstr(theta(am), 25))
    rec('    ### ### **NO VERIFIED CLASSICAL VALUE IS PRINTED BESIDE IT** (face, BAR 1): neither verified source')
    rec('    ### states theta`s minimum or its value, and none is supplied from memory.')

    sub('(c) THE QUANTIFIER -- ODDNESS, AND THE SIGN PATTERN OF h+ ON (0, 50]')
    odd = []
    for t in (1, 3, 6.29, 20, 50):
        s_ = theta(t) + theta(-t)
        odd.append(float(abs(s_)))
        rec('      theta(%-5s) + theta(-%-5s) = %.3e' % (t, t, float(abs(s_))))
    ok_odd = max(odd) < 1e-30
    grid = [mpf(k) / 20 for k in range(1, 1001)]
    signs = [1 if hplus(u) > 0 else -1 for u in grid]
    changes = [(float(grid[i]), float(grid[i + 1])) for i in range(len(signs) - 1) if signs[i] != signs[i + 1]]
    rec('      h+ on (0, 50], step 0.05 : first sign %+d, last sign %+d, sign changes %d at %s'
        % (signs[0], signs[-1], len(changes), changes))
    ok_one = len(changes) == 1 and signs[0] < 0 and signs[-1] > 0 and changes[0][0] < float(u0b) < changes[0][1]
    rec('    ### ### **theta IS ODD (%s), FALLS WHILE h+ < 0 AND RISES WHILE h+ > 0, AND h+ CHANGES SIGN ONCE ON'
        % ('MEASURED' if ok_odd else 'NOT MEASURED'))
    rec('    ### ### (0, 50] (%s). SO u0 IS THE MINIMUM OF theta ON 0 <= t <= 50 -- AND, theta BEING ODD, THE'
        % ('MEASURED' if ok_one else 'NOT MEASURED'))
    rec('    ### ### LINE`S MIRROR POINT -u0 IS ITS MAXIMUM ON -50 <= t <= 0. THERE IS NO GLOBAL MINIMUM ON THE LINE.**')
    rec('    ### The range beyond 50 is not measured here; the grid does not reach it, and the sentence filed')
    rec('    ### names the range it holds on.')
    held = ok_arg and ok_val and ok_odd and ok_one
    rec('')
    rec('    ### ### **COMPONENT 1 VERDICT : %s.**' % ('HOLDS, WITH ITS QUANTIFIER' if held else 'NOT HELD'))

    sub('(d) THE MECHANISM, RESTATED WITH b440`S QUALIFIER (face, BAR 3)')
    quote(os.path.join(D, 'b440_components.txt'), 'IT AGREES AT', clip=200)
    quote(os.path.join(D, 'b440_components.txt'), 'NEVER CROSSING:', clip=200)
    rec('    ### **RESTATED:** the archimedean slack on the seed family closes when half the seed`s transform')
    rec('    ### mass lies above the height at which theta attains its minimum on t >= 0 -- ### **A HEURISTIC,')
    rec('    ### RIGHT AT 9 OF 10 CELLS, WRONG FOR THE SECOND FAMILY AT a = 1.2, EXACTLY AS b440 MEASURED IT.**')

    sub('(e) THE STATUSES THE RECORD NOW HOLDS FOR u0, APART (face, BAR 4)')
    rec('      DEFINING EQUATION   : HELD   -- Re psi(1/4 + iu/2) = log pi (b439, b440)')
    rec('      CLASSICAL ASYMPTOTE : HELD   -- 2 pi, the zero of log(u / 2 pi), which is not u0 (b440)')
    rec('      NAME                : %s -- the minimum of the Riemann-Siegel theta on 0 <= t <= 50,'
        % ('HELD  ' if held else 'NOT HELD'))
    rec('                                    DERIVES-ON-IMPORTS: one line on K5`s imported h+ = 2 theta`')
    rec('      CLOSED FORM         : NOT HELD -- a name is not a closed form; no expression in named constants')
    rec('      CLASSICAL VALUE     : NOT SOURCED -- theta(u0) is computed; no verified source states it')
    json.dump(dict(u0_banked=str(u0b), argmin=str(am), argmin_gap=float(gap), theta_B=str(tB), theta_A=str(tA),
                   route_gap=float(abs(tA - tB)), odd_max=max(odd), sign_changes=changes, held=held),
              io.open(os.path.join(D, 'b442_theta.json'), 'w', encoding='utf-8'), indent=1)
    return held, tB


# ### ==============================================================================================
CLASS_LINE = 'Theorem 6.1. For any irreducible cuspidal'
CANDS = [
    ('V1', 'Theorem 6.1`s own hypotheses, against the Epstein form', 'S1', 'CLASS BOUNDARY',
     [(LAG, CLASS_LINE), (os.path.join(D, 'b326_the_reach.txt'), 'there is no Euler product to keep it'),
      (LAG, 'Each completed automorphic L-function')],
     'Theorem 6.1 ranges over cuspidal automorphic representations, whose L-functions each carry an Euler '
     'product; the record measured that the Epstein function has none. The second object is outside the '
     'class by hypothesis.'),
    ('V2', 'Theorem 6.1 over the two-element class {zeta, Z_Q} by the finite maximum', 'S1', 'CLASS BOUNDARY',
     [(LAG, CLASS_LINE), (LED, 'the corpus’s second object is **not established to be one**')],
     'Over a finite class the maximum of the constants IS one constant, so the interchange is free (BAR 7) -- '
     'but the maximum needs a constant for each member, and Theorem 6.1 supplies none for Z_Q. The failure is '
     'membership, not uniformity.'),
    ('V3', 'Lagarias`s Dedekind-zeta sentence', 'S1', 'CLASS BOUNDARY',
     [(LAG, 'Dedekind zeta functions of any algebraic'), (os.path.join(D, 'b326_the_reach.txt'),
                                                          'there is no Euler product to keep it')],
     'The sentence reports Li`s criterion for Dedekind zeta functions, which carry Euler products; it states no '
     'constant, and its class does not contain the single-form Epstein function the record holds.'),
    ('V4', 'Theorem 5.1`s absolute constant', 'S1', 'COORDINATE BOUNDARY',
     [(LED, 'Theorem 5.1’s absolute constant is a witness for the ARCHIMEDEAN side and not for this one')],
     'The absolute constant is on the archimedean term; site (v) needs one on the finite-place term.'),
    ('V5', 'Theorem 2.1(4)`s counting law', 'S1', 'CLASS BOUNDARY',
     [(LAG, 'Theorem 2.1. Letπ be a irreducible cuspidal')],
     'Same hypothesis, same exclusion; and its constant depends on pi besides.'),
    ('V6', 'CC`s statements', 'S1', 'CLASS BOUNDARY',
     [(CC, 'multi-set of non-trivial zeros of the Riemann zeta function')],
     'CC`s objects are the zeros of the Riemann zeta function; the class holds one member, not two.'),
    ('V7', 'row F7`s own measured statements', 'S2', 'BOUNDED BY A MEASUREMENT',
     [(LED, 'the formula closes for the Epstein function at 21 of 21 cells below its ceiling')],
     'The row speaks of both objects, so S1 passes; but what it holds is measured at finitely many cells, and a '
     'measurement is not a constant serving every representation.'),
    ('V8', 'b325`s transfer of the archimedean distribution', 'S2', 'REFUTED',
     [(LED, 'THE ARCHIMEDEAN DISTRIBUTION DOES NOT TRANSFER')],
     'A constant shared across the two objects would need the archimedean side to transfer between them; the '
     'record measured that it does not.'),
    ('S1*', 'the counting error with an absolute constant via the analytic conductor (Lagarias citing IK 5.8)',
     'S1', 'CLASS BOUNDARY',
     [(LAG, 'with an absolute constant, which involves the analytic conductor'), (LAG, CLASS_LINE)],
     'THE NEAR-MISS OF THE SITE: the constant IS uniform across representations, carried by the conductor -- but '
     'only across cuspidal ones, it bounds the counting function and not the finite-place sum, and Lagarias '
     'cites it from a source the record does not hold. It fails first at the class.'),
    ('S2*', 'Theorem 3.1 on the Li class L of test functions', 'S1', 'CLASS BOUNDARY',
     [(LAG, 'Theorem 3.1. Letπ be an irreducible cuspidal')],
     'The test-function class L does not depend on the object, which is why it was hand-picked; the theorem '
     'that uses it still quantifies over cuspidal pi.'),
]
NOT_CANDIDATES = [
    (1395, 'a constant independent of z, a proof variable'), (1457, 'an absolute constant inside a proof estimate'),
    (1630, 'an absolute constant inside a proof estimate'), (1652, 'independent of a contour, not an object'),
    (1770, 'a constant independent of z'), (2441, 'uniform convergence in z'), (2483, 'uniform convergence on a disc'),
    (2794, 'the uniform norm on test functions'), ('CC 2713', 'a numerical uniform approximation'),
    ('CC 4062', 'a uniform bound in rho for zeta`s construction'), (697, 'the class A of test functions, '
                                                                          'O-constant depending on the function'),
]


def component_2():
    head('COMPONENT 2', 'THE WITNESS ARC AT SITE (v), THE REPRESENTATION-DEPENDENT CONSTANT')
    sub('THE SITE`S OWN CELL, QUOTED FIRST')
    quote(LED, '**(v) THE REPRESENTATION-DEPENDENT CONSTANT**', clip=1400, span=1400)
    quote(LED, '### **`(v)` — KIND: `(b)`. WITNESS: `NONE KNOWN`.**', clip=700, span=700)
    sub('THE CELL`S TRANSCRIPTION AGAINST ITS SOURCE (face, BAR 8)')
    quote(LED, 'S_f(n,π) = λ_n(n,π) + O(n log n)', clip=160, span=160)
    quote(LAG, CLASS_LINE, after=6, clip=120)
    rec('    ### ### **THE ROW WRITES `lambda_n(n,pi) + O(n log n)`; THE SOURCE READS `lambda_n(sqrt n, pi-dual) +')
    rec('    ### ### O(sqrt n log n)`.** The dependence of the constant on pi -- the site`s content -- is the same in')
    rec('    ### both. ### **THE ROW IS NOT REWRITTEN.**')

    rows = []
    for cid, name, step, kind, qs, why in CANDS:
        sub('%s -- %s' % (cid, name))
        ok = True
        for path, ndl in qs:
            if quote(path, ndl, clip=420, span=420) is None:
                ok = False
        rec('      attempted : S1 CLASS%s' % (' -> S2 HELD' if step in ('S2', 'S3') else ''))
        if not ok:
            rec('      ### **NOT QUOTABLE -- DROPPED** (section (S)).')
            continue
        rec('      ### ### **FAILED AT %s -- %s.**' % (step, kind))
        for c in wrap(why, 84):
            rec('        %s' % c)
        rows.append(dict(id=cid, name=name, step=step, kind=kind, why=why,
                         quotes=[(os.path.basename(p), n) for p, n in qs]))
    sub('THE SEARCH HITS READ AND NOT MADE CANDIDATES -- EACH WITH ITS REASON')
    for at, why in NOT_CANDIDATES:
        rec('      %-9s %s' % (at, why))
    held = [r for r in rows if r['kind'] == 'HELD']
    kinds = {}
    for r in rows:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    rec('')
    rec('    ### ### **%d CANDIDATES, %d HELD. FIRST FAILING STEPS: %s.**'
        % (len(rows), len(held), '; '.join('%s %d' % kv for kv in sorted(kinds.items(), key=lambda x: -x[1]))))

    sub('THE BOUNDARY COUNT AT FIVE SITES -- FROM BANKED JSON, NEVER TYPED')
    prior = json.loads(read(os.path.join(D, 'b436_prior_sites.json')))
    cand4 = json.loads(read(os.path.join(D, 'b436_candidates.json')))
    rows4 = cand4.get('candidates', cand4) if isinstance(cand4, dict) else cand4
    t4 = {}
    for r in rows4:
        t4[r['kind']] = t4.get(r['kind'], 0) + 1
    tallies = dict(prior['tallies'])
    tallies['b436'] = t4
    tallies['b442'] = kinds
    for act, t in tallies.items():
        rec('      %-5s %2d candidates  %d kinds  %s' % (act, sum(t.values()), len(t), dict(t)))
    before = set().union(*[set(t) for a_, t in tallies.items() if a_ != 'b442'])
    new = sorted(set(kinds) - before)
    rec('      union across the four earlier sites : %d ; across all five : %d'
        % (len(before), len(before | set(kinds))))
    rec('      this site`s failures landing at a kind an earlier site used : %d of %d ; new kinds : %s'
        % (sum(v for k, v in kinds.items() if k in before), len(rows), new))
    cb = kinds.get('CLASS BOUNDARY', 0)
    rec('    ### ### **CLASS BOUNDARY : %d of %d. THE OTHER %d LAND ELSEWHERE -- %s.**'
        % (cb, len(rows), len(rows) - cb, sorted(k for k in kinds if k != 'CLASS BOUNDARY')))
    rec('    ### ### **AND THE FINITE CLASS SAYS WHY THE CLASS BOUNDARY DOMINATES:** over the two objects the corpus')
    rec('    ### ### holds, uniformity is free once both are members; every theorem the verified sources hold with')
    rec('    ### ### a representation-dependent constant assumes cuspidality, and the record measured that the')
    rec('    ### ### Epstein function has no Euler product. ### **The obstruction at this scale is membership.**')
    rec('')
    rec('    ### **SITE (v) IS EXHAUSTED WITH NO WITNESS HELD. The arc is checkpointed after (v); (vi) remains.**')
    json.dump(dict(candidates=rows, tallies=tallies, union_before=len(before), union_all=len(before | set(kinds)),
                   new_kinds=new, held=len(held)),
              io.open(os.path.join(D, 'b442_site_v.json'), 'w', encoding='utf-8'), indent=1)
    return rows, kinds


def component_3():
    head('COMPONENT 3', 'b440`S TWO CORRECTIONS, IN b441`S WORDS -- VERIFIED BEFORE THE ROW IS WRITTEN')
    B441 = os.path.join(D, 'b441_closing.txt')
    for ndl in ('VERDICT: THE RECORD NEVER DENIED THE IDENTIFICATION',
                'b440\'s sentence -- "b430\'s defect, still live in every act',
                "AND b440'S REPAIR WAS DEFECTIVE TOO"):
        quote(B441, ndl, after=2, clip=300)
    rec('    ### **THE WRONG RULE, IN b440`S TOOL AS IT STANDS (NOT EDITED):**')
    quote(os.path.join(T, 'b440_checks.py'), "remote = git(ROOT, 'rev-parse', 'origin/main')", after=1, clip=160)
    rec('    ### **AND b439`S PREDICATE AS RESTORED IN b441`S COMMITTED SUITE:**')
    quote(os.path.join(T, 'b441_checks.py'), "if 'b441' not in subj", after=3, clip=160)


def main():
    rec('=' * 100)
    rec('b442 -- THE MINIMUM NAMED, AND SITE (v). ### THE COMPONENTS, RUN AFTER THE LOCK.')
    rec('=' * 100)
    held, tB = component_1()
    rows, kinds = component_2()
    component_3()
    rec('')
    rec('=' * 100)
    rec('  ### ### **COMPONENT 1 : %s ; COMPONENT 2 : %d candidates, 0 held, %s ; MISSES %d %s**'
        % ('HOLDS WITH ITS QUANTIFIER' if held else 'NOT HELD', len(rows), kinds, len(MISS), MISS or ''))
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(OUT))


if __name__ == '__main__':
    main()
