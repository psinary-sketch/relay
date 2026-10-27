# -*- coding: utf-8 -*-
"""b716_epstein_price.py -- (R326)(6)(ii): W-ORD-EPSTEIN-COUNT-LEAN, PRICED, NOTHING BUILT. Writes data/b716_epstein_count_price.txt.

What a Lean proof of one certified band count at Q0 (x^2 + xy + 6y^2, D = 23) would need. The band: data/b709_pairs.txt :20,
[160.0, 170.0], N 15, on-line 15, off-line 0. What Mathlib supplies at the federation target (data/b716_federation_pin_price.txt (2)):
read from the Mathlib checkout under SIDE-explicit-formula's .lake (its HEAD checked equal to the target, its tree checked clean), each
needle's declarations counted with their first places. The grade vocabulary: the keystone census's status cells at PLACE-papers HEAD.
No lean process runs; no dispatch is made; no request leaves the host.

  python -X utf8 tools/b716_epstein_price.py          writes the bank and prints its foot
"""
import os
import re
import subprocess
import sys
import time
from collections import Counter

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RELAY, 'data')
NL = '\n'
ML = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PP = 'D:/MY-DOwnloads/PLACE-papers'
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md'
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*'
                  r'(theorem|lemma|def|abbrev|structure|class|instance)\s+([^\s:(\[{]+)')
GRADE = re.compile(r'### \*\*([A-Z][A-Z0-9 ,/\-]*?)\*\*')

# (key, what it stands for, the name pattern, the path pattern or None) -- a declaration is a hit when its own name (or its
# namespaced name) matches and its file matches the path pattern; the name's matches outside the path are counted beside it
ANALYSIS = r'^Mathlib/(Analysis|MeasureTheory|NumberTheory/LSeries|Topology)/'
NEEDLES = [
    ('A1', 'Cauchy on a rectangle (the boundary integral)', r'integral_boundary_rect', None),
    ('A2', 'residues, winding numbers, an argument principle by name', r'(?i)residue|winding|argumentPrinciple|argument_principle', ANALYSIS),
    ('A3', 'the logarithmic derivative', r'(^|\.)logDeriv', None),
    ('A4', 'meromorphic order and divisors', r'meromorphicOrderAt|(^|\.)divisor', ANALYSIS),
    ('A5', 'zeros counted by name', r'(?i)card_?zeros|zeros_?card|countZeros|numZeros|zeroCount', None),
    ('A6', 'Jensen`s formula (every declaration of its file)', r'.', r'JensenFormula\.lean$'),
    ('B1', 'the Gamma function', r'^(Complex\.|Real\.)?Gamma', None),
    ('B2', 'the Riemann zeta function and its completion', r'riemannZeta|completedRiemannZeta', None),
    ('B3', 'Bessel functions (special functions, not Sobolev`s potential)', r'(?i)bessel', r'^Mathlib/Analysis/SpecialFunctions/'),
    ('B4', 'Epstein zeta', r'(?i)epstein', None),
    ('B5', 'Dirichlet L-functions', r'LFunction', None),
    ('B6', 'Hurwitz zeta', r'(?i)hurwitz', None),
    ('B7', 'Jacobi theta', r'(?i)jacobiTheta', None),
    ('B8', 'the Mellin functional-equation pairs', r'(?i)FEPair', None),
    ('C1', 'numerical bounds on constants (pi, e, log 2)', r'(?i)pi_gt|pi_lt|exp_one_gt|exp_one_lt|exp_one_near|log_two_near|log_two_gt|log_two_lt', None),
    ('C2', 'interval arithmetic by name', r'(?i)interval_?arith|IntervalArith', None),
    ('C3', 'explicit Taylor bounds for exp', r'(?i)exp_bound|exp_approx', None),
    ('D1', 'the intermediate value theorem', r'(?i)intermediate_value', None),
    ('D2', 'zeta conjugation / the Hardy Z function', r'(?i)hardyZ|riemannSiegel|zeta_conj|Zeta_conj', None),
]
DECL_TABLE = '### The reduction chain’s declarations at their pins'


def git(path, *args):
    r = subprocess.run(['git', '-C', path] + list(args), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace('\r', '') if r.returncode == 0 else None


def main():
    fed = open(os.path.join(D, 'b716_federation_pin_price.txt'), encoding='utf-8').read()
    m = re.search(r'THE TARGET, the newest rev any kernel carries: ([0-9a-f]{12})', fed)
    target = m.group(1) if m else None
    head = (git(ML, 'rev-parse', 'HEAD') or '').strip()
    dirty = git(ML, 'status', '--porcelain', '--untracked-files=no')
    at_target = bool(target) and head.startswith(target)
    files = [f for f in (git(ML, 'ls-tree', '-r', '--name-only', 'HEAD') or '').split(NL)
             if f.startswith('Mathlib/') and f.endswith('.lean')]
    hits = {k: [] for k, _, _, _ in NEEDLES}
    outside = Counter()
    pats = [(k, re.compile(p), re.compile(q) if q else None) for k, _, p, q in NEEDLES]
    ndecl = 0
    for f in files:
        try:
            src = open(os.path.join(ML, f), encoding='utf-8').read().split(NL)
        except OSError:
            continue
        ns = []
        for i, line in enumerate(src, 1):
            nm = re.match(r'^\s*namespace\s+(\S+)', line)
            if nm:
                ns.append(nm.group(1))
                continue
            em = re.match(r'^\s*end\s+(\S+)\s*$', line)
            if em and ns and ns[-1] == em.group(1):
                ns.pop()
                continue
            dm = DECL.match(line)
            if not dm:
                continue
            ndecl += 1
            name = dm.group(2)
            full = '.'.join(ns + [name]) if ns else name
            for k, p, q in pats:
                if p.search(name) or p.search(full):
                    if q is None or q.search(f):
                        hits[k].append((full, f, i, dm.group(1)))
                    else:
                        outside[k] += 1
    census = (git(PP, 'show', 'HEAD:' + CENSUS) or '').split(NL)
    pph = (git(PP, 'rev-parse', 'HEAD') or '').strip()
    grades, foot, start = Counter(), None, None
    for i, line in enumerate(census, 1):
        if line.strip() == DECL_TABLE:
            start = i
            continue
        if start and line.startswith('| ') and not line.startswith('| #'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if len(cells) >= 6 and cells[0].isdigit():
                g = cells[4]
                grades['not graded' if g.startswith('not graded') else g.split()[0]] += 1
        if start and line.startswith('*') and 'declarations:' in line:
            foot = (i, line.strip())
            break

    L = ['b716 -- (R326)(6)(ii): W-ORD-EPSTEIN-COUNT-LEAN, PRICED; NOTHING BUILT, NO LEAN PROCESS, NO DISPATCH (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows: (1) the count priced; (2) what the proof needs, piece by piece; (3) what Mathlib supplies at the target rev, read from its',
         '### sources on this host; (4) what would be built; (5) the dispatches and hours (THE SEAT`S); (6) the grade the result would carry, in',
         '### the census`s own vocabulary. Written by tools/b716_epstein_price.py.', '']
    L += ['## (1) THE COUNT PRICED',
          '  Q0 = x^2 + xy + 6y^2, D = 23 (b711`s and b709`s form; data/b713_list.txt :11 counts b711`s band "at DQ = 23"). THE BAND:',
          '  data/b709_pairs.txt :20, [160.0, 170.0], N 15, on-line 15, off-line 0, COMPLETE -- b667`s half path over [1/2, 2.0] x [160, 170],',
          '  doubled by Lambda_Q0`s symmetry (data/b713_list.txt :3-:7 for the route`s form). Chosen as the band whose whole count is on the line:',
          '  N = on-line, so the argument-principle count (an upper reading) and the 15 sign changes of Z_Q0 (a lower reading) close with no',
          '  off-line rectangle -- the least proof a certified band count admits.', '']
    L += ['## (2) WHAT THE PROOF NEEDS',
          '  (a) THE ARGUMENT PRINCIPLE on a rectangle: for f holomorphic on a neighbourhood of a closed rectangle R and nonzero on its boundary,',
          '      the zeros in R counted with multiplicity equal (1/2 pi i) times the boundary integral of f`/f -- or its discrete form: the change of',
          '      arg f along the boundary, read from finitely many boundary points with a bound on |f - f(z_k)| below |f(z_k)| on each segment.',
          '  (b) Lambda_Q0 IN LEAN: the Epstein zeta of Q0, its continuation and its functional equation Lambda_Q0(s) = Lambda_Q0(1 - s); h(-23) = 3,',
          '      so Q0`s zeta is not a product of Dirichlet L-functions -- it is reached by the Mellin transform of Q0`s theta function or by the',
          '      Chowla-Selberg expansion (zeta(2s), Gamma(s - 1/2)/Gamma(s) zeta(2s - 1), a K-Bessel series -- b667`s engine`s route).',
          '  (c) INTERVAL BOUNDS ON Z_Q0: certified enclosures of Lambda_Q0 at every boundary point of the discrete argument count and at the 16',
          '      points bracketing the 15 sign changes; each enclosure from explicit truncation bounds on the expansion of (b), checked in the kernel.',
          '  (d) THE BAND`S EDGES: the horizontal edges t = 160 and t = 170 and the right edge Re s = 2.0, each with Lambda_Q0 nonzero on it (from',
          '      (c)); the left edge Re s = 1/2 handled by the half path (the symmetry of (b)); the reading N = 15 then the sum (a) gives.', '']
    L += ['## (3) WHAT MATHLIB SUPPLIES AT THE TARGET REV',
          '  the checkout: %s HEAD %s ; the target %s ; AT THE TARGET %s ; its tracked tree %s ; Mathlib/*.lean files %d ; declarations read %d' % (
              ML, head[:12] or '### NOT READ', target or '### NOT READ', at_target, 'CLEAN' if dirty == '' else '### NOT CLEAN OR NOT READ', len(files), ndecl)]
    for k, what, p, q in NEEDLES:
        h = hits[k]
        L.append('  %s %-60s declarations %4d   (name pattern %s%s)' % (
            k, what, len(h), p, '; path %s; the name matched outside it %d' % (q, outside[k]) if q else ''))
        for full, f, i, kind in h[:5]:
            L.append('       %-8s %s  %s :%d' % (kind, full, f, i))
    L += ['  THE POSITIVE CONTROL of the reading: B2 must find riemannZeta (Mathlib`s, at NumberTheory/LSeries) and B1 Complex.Gamma; a zero',
          '  there is the scan`s fault, not Mathlib`s absence.', '']
    L += ['## (4) WHAT WOULD BE BUILT (on SIDE-explicit-formula, the kernel at the target; the piece names THE SEAT`S)',
          '  (a) RectArgumentPrinciple: the discrete argument count on a rectangle from A1 and A3/A4 (local factorisation f = (z - a)^n g).',
          '  (b) EpsteinQ0: Q0`s theta function, its Mellin transform, continuation and functional equation over B7/B8`s pairs where they reach a',
          '      binary form`s theta, else from first principles; the Chowla-Selberg expansion proved equal to it, B3 built where it reads 0.',
          '  (c) EpsteinQ0Bounds: truncation bounds for each term of the expansion, and the enclosures at the boundary points as rational',
          '      inequalities closed by norm_num / decide in the kernel (C1/C3 the only ready bounds; C2 builds where it reads 0).',
          '  (d) BandCount160: the band`s edges, the count N = 15 from (a)-(c), and the 15 sign changes by D1 -- the statement',
          '      "the zeros of Lambda_Q0 in [1/2, 2] x [160, 170] number 15 with multiplicity, all on Re s = 1/2" (doubled by the symmetry).', '']
    L += ['## (5) THE DISPATCHES AND HOURS (THE SEAT`S ESTIMATE; NO MEASUREMENT OF ANY SUCH BUILD EXISTS IN THE RECORD)',
          '  each module dry-built by build-module on SIDE-explicit-formula, read by run id and its artifact`s sha256 (N1`s form); its runs at the',
          '  target take 4.2 to 11.0 min (data/b716_federation_pin_price.txt (3b)). Authoring and dispatches by piece:',
          '    (a) the argument count        800-1,500 lines ;  15-30 dispatches ;  20-40 foreground hours',
          '    (b) Lambda_Q0 and its FE    1,500-3,000 lines ;  25-50 dispatches ;  35-70 foreground hours',
          '    (c) the enclosures          3,000-6,000 lines ;  40-80 dispatches ;  50-100 foreground hours (kernel checking of the',
          '                                                                        enclosures the risk: each must close within the runner`s limit)',
          '    (d) the band                  300-600 lines  ;  10-20 dispatches ;  10-20 foreground hours',
          '    IN ALL                      5,600-11,100 lines ; 90-180 dispatches, 6-33 runner hours ; 115-230 foreground hours, 15-30 acts at',
          '    data/b716_price.txt (6)`s 7.7-hour act. The range is the seat`s judgement of an unbuilt proof, not a bound; its first',
          '    measurement is (a)`s first module`s dispatch, in the act the author rules for it.', '']
    L += ['## (6) THE GRADE THE RESULT WOULD CARRY',
          '  the vocabulary: the shared E0 rule`s (relay tools/e0_rule.py; the census grades by it, census :1490) -- DERIVES, INTERFACES, not',
          '  graded. The census`s declarations table (PLACE-papers %s at HEAD %s, from its head line %s) read here: %s ;' % (
              CENSUS, pph[:8] or '### NOT READ', start or '### NOT FOUND', ' ; '.join('%s %d' % kv for kv in sorted(grades.items())) or '### NONE READ'),
          '  THE CONTROL, the table`s own foot%s' % (' (:%d): %s' % foot if foot else ': ### NOT FOUND'),
          '  the result: a theorem about the Lean-defined Lambda_Q0 whose statement binds no hypothesis -- DERIVES under the E0 rule`s (1),',
          '  "its only binders are domain conditions" (it has none); its axioms read by a banked #print axioms at its pin, expected',
          '  [propext, Classical.choice, Quot.sound] (library lemmas carry them); a route through native_decide adds Lean.ofReduceBool and is',
          '  excluded from the price. ITS SCOPE: the one band at Q0; the other bands, and -15`s and -39`s lists, stay certified by the Python',
          '  engine; the Lean Lambda_Q0 equal to the engine`s Z_Q0 is (b)`s theorem, not a reading.', '']
    zero = [k for k, _, _, _ in NEEDLES if not hits[k]]
    L += ['### ### **THE BAND [160, 170] AT Q0, N 15, ALL ON THE LINE ; MATHLIB AT THE TARGET %s ; NEEDLES %d, READING 0: %s ; BUILT: (a) THE ARGUMENT COUNT, (b) Lambda_Q0, (c) THE ENCLOSURES, (d) THE BAND ; 90-180 DISPATCHES, 115-230 FOREGROUND HOURS (THE SEAT`S) ; THE GRADE DERIVES (E0), ONE BAND ; NOTHING BUILT.**' % (
        'READ' if at_target and dirty == '' else 'NOT READ', len(NEEDLES), ' '.join(zero) or 'none')]
    p = os.path.join(D, 'b716_epstein_count_price.txt')
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(NL.join(L) + NL)
    os.replace(p + '.tmp', p)
    print('bank', p)
    print(L[-1])
    return 0


if __name__ == '__main__':
    sys.exit(main())
