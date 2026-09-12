# -*- coding: utf-8 -*-
"""b428_extract.py -- THE SURVEY FOR b428: SITE (iii), AND THE TWO FILINGS FROM OUTSIDE.
### **EVERY READ ANCHORED IN THE MARKUP-FOLDED TEXT, EVERY MISS COUNTED, THE CANDIDATE SEARCH PRINTED IN FULL.
### THE CORPUS, THE TWO VERIFIED SOURCES AND THE KERNELS AT THEIR PINS ONLY -- NOTHING IS FETCHED BY THIS TOOL.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
FL = os.path.join(PP, 'FACES_LEDGER.md')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
B353 = os.path.join(D, 'b353_the_missing_statement.txt')
B334 = os.path.join(D, 'b334_the_aim_map.txt')
B328 = os.path.join(D, 'b328_the_discriminating_family.txt')
B325 = os.path.join(D, 'b325_the_negative_control.txt')
B326 = os.path.join(D, 'b326_the_reach.txt')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
RDM = os.path.join(PP, 'README.md')
OUT = os.path.join(D, 'b428_extract.txt')
NL = chr(10)
L, MISS = [], []
READS = [0]


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def fold(s):
    return re.sub(r'\s+', ' ', (s or '').replace('###', ' ').replace('**', '').replace('`', '')).strip()


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def quote(label, src_or_path, start, end=None, width=96, cap=700, text=None):
    READS[0] += 1
    src = fold(text if text is not None else read(src_or_path))
    s0, e0 = fold(start), fold(end) if end else ''
    i = src.find(s0)
    name = os.path.basename(src_or_path)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-50s ### **MISS** -- anchor absent in %s' % (label, name))
        return ''
    j = src.find(e0, i + len(s0)) if end else -1
    seg = src[i:j + len(e0)] if j > i else src[i:i + cap]
    say('  %-50s %s' % (label, name))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


rule('=')
say('b428_extract.py -- THE SURVEY: SITE (iii), THE DISPROOF LANE, AND THE EXTERNAL READ.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROWS 275 AND 276 BY THEIR MARKERS, AND THE TWO EXHAUSTED-LIST BLOCKS.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
for lab, rx, want in (('b426`s row', r'(?m)^\| (\d+) \| \*\*THE FALSIFIER RE-READ BY ADDRESS UNDER \(R38\)', 275),
                      ('b427`s row', r'(?m)^\| (\d+) \| \*\*THE WITNESS ARC AT SITE \(ii\)', 276)):
    READS[0] += 1
    got = [int(x.group(1)) for x in re.finditer(rx, corr)]
    say('  %-16s by its marker : %s   (expected [%d])' % (lab, got, want))
    if got != [want]:
        MISS.append('%s is not %d by its marker' % (lab, want))
fl = read(FL)
for mk in ('<!-- b424 update -->', '<!-- b427 update -->'):
    READS[0] += 1
    n = fl.count(mk)
    say('  the uniformity row`s exhausted-list block %-24s present %d time(s)' % (mk, n))
    if n != 1:
        MISS.append('block %s present %d times' % (mk, n))

rule()
say('### READ 1 -- THE SITE: ROW U1`S ENTRY (iii), ITS WITNESS CELL, AND THE FREEZE.')
rule()
u1 = next((x for x in fl.splitlines() if x.startswith('| U1 ')), '')
say('  row U1 present : %s ; bytes %d' % (bool(u1), len(u1.encode('utf-8'))))
quote('the site, as entered (b353)', FL, "(iii) THE WIDTH COORDINATE'S UNION",
      'quantifies over the union of all supports.', text=u1)
quote('the WITNESS cell for (iii)', FL, '(iii) — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.',
      'No such `g` is named.', text=u1)
quote('what a shared witness is, in the row', FL, 'WITNESS IS SOURCED FROM THE COMPILED THEOREM AND FROM NOWHERE ELSE.',
      'PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.', text=u1)
quote('the freeze (b409)', FL, 'THE REGISTER IS FROZEN AT SIX, b409.', 'NO SEVENTH SITE IS ENTERED.', text=u1)
w = re.findall(r'WITNESS: *`([A-Z ]+)`', u1)
say('  the six WITNESS fields : %s' % w)

rule()
say('### READ 2 -- THE SITE`S OWN STATEMENT, IN THE ACT THAT ENTERED IT (b353).')
rule()
quote('Boas-Kac, quoted at the pinned source', B353, 'Let f in Cc^infty(R) have support in the interval [-A, A]',
      'such that f = g * g^*."')
quote('what it exhausts, and where it stops', B353, 'IT IS AN EQUIVALENCE, WHICH IS STRONGER THAN THE DENSITY',
      'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.')
quote('the criterion`s own quantifier, over the union', B353, 'RH <=> sum_v W_v(g * gbar^#) <= 0, for all g in',
      'for all z in F."')
quote('the missing statement, typed', B353, 'THE MISSING STATEMENT, TYPED:', 'implies it on the union over all `A`."')
quote('why the increasing union is not automatic', B353, 'AND WHY THE SECOND HALF IS NOT AUTOMATIC',
      'INSTRUMENT THAT DOES NOT REACH.')
quote('the price of the crossing half', B353, 'THE CROSSING HALF IS UNPRICEABLE FROM BANKED FIGURES.',
      'IT IS NOT ATTEMPTED.')
quote('what was looked for and not found', B353, 'WHAT WAS LOOKED FOR AND NOT FOUND:',
      'NOT LOCATED** in the pinned source.')
quote('the hypotheses, graded twice', B353, 'H1  f in Cc^infty(R), compactly supported', 'MET TO A MEASURED TOLERANCE')
quote('the scan that is a range result', B353, 'it can show a function is NOT positive definite',
      'THAT IS A RANGE RESULT WHERE THE HYPOTHESIS IS A GLOBAL ONE.')

rule()
say('### READ 3 -- THE COMPILED FORM, AT THE PIN THE ROW CITES (SIDE-lv-conservation 93c27ec = v0.10.0).')
rule()
t3 = subprocess.run(['git', '-C', LV, 'show', '93c27ec:SIDELvConservation/T3_StepNineBridge.lean'],
                    capture_output=True).stdout.decode('utf-8', 'replace')
quote('T3prime_shared_witness', 'T3_StepNineBridge.lean@93c27ec', 'theorem T3prime_shared_witness', '⟨Phi, h1, h2⟩', text=t3)

rule()
say('### READ 4 -- THE STARTING POPULATION: THE NAVIGATOR`S THREE, EACH AT ITS RECORD LOCATION.')
rule()
say('')
say('  [C1] MONOTONICITY IN THE RADIUS -- the increasing union')
quote('  the increasing union, and its condition', B353, 'The union is an increasing union, and non-negativity on each',
      'IF THE FUNCTIONAL IS THE SAME FUNCTIONAL ON EACH.')
quote('  the record does not establish it', B353, 'The record does not establish that the object it evaluates at',
      'past `rho = 100`.')
say('')
say('  [C2] A LIMIT ACROSS RADII')
quote('  Boas-Kac carries no limit argument', B353, 'positivity of the Weil functional on the seed family at half-width',
      'WITH NO LIMIT ARGUMENT AND NO TOPOLOGY.')
quote('  the search that did not find one', B353, 'a statement carrying positivity from one support to a larger one',
      'NOT LOCATED** in the pinned source;')
say('')
say('  [C3] BOAS-KAC AT EACH RADIUS, THE EXISTENTIAL THE SITE OWNS')
quote('  the existential, as the row reads it', FL, 'THIS IS THE ONE SITE OF THE SIX WHOSE OWN BANKED TEXT SUPPLIES',
      'No such `g` is named.', text=u1)
quote('  and every conclusion at the same A', B353, 'AND EVERY CONCLUSION IT GIVES IS AT THE SAME `A` IT WAS GIVEN.',
      'PASSING FROM ONE `A` TO A LARGER')

rule()
say('### READ 5 -- THE TWO VERIFIED SOURCES, AT THE STATEMENTS THAT CARRY OR REFUSE A SUPPORT CONDITION.')
rule()
quote('CC Theorem 1, its support hypothesis', CC, 'Theorem 1 Let g P C8', 'Trpϑpgq Sϑpgq˚q. (4)')
quote('CC, the design: primes not involved', CC, 'In this paper we consider the simplest instance of this',
      'so that rational primes are not involved')
quote('CC Theorem 6.11', CC, 'Theorem 6.11 LetgPC8', 'log 2. (141)')
quote('CC, small enough intervals', CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')
quote('CC Proposition C.1, no support hypothesis', CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)')
quote('Lagarias Theorem 2.2', LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', '(2.20)')
quote('Lagarias Theorem 5.1', LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)')
quote('Lagarias Theorem 6.1', LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')

rule()
say('### READ 6 -- THE REACHING WIDTHS AND THE INSTRUMENT`S OWN LIMIT.')
rule()
quote('the charted widths, and the evaluator`s reach', B334, "The frame's X = 32 against f's support a^2 = 1600",
      "outside the evaluator's reach.")
quote('the square for Z_Q', B334, 'The square and the remainder for Z_Q: NOT AN INSTRUMENT THE RECORD HAS',
      'said on every Epstein line.')

rule()
say('### READ 7 -- THE SEARCH FOR FURTHER CANDIDATES, BY DESCRIPTION, PRINTED IN FULL.')
rule()
say('  THE DESCRIPTION, FIXED BEFORE THE SEARCH: a statement or object that would serve EVERY support width at')
say('  once -- one `g`, one bound or one argument valid across all `A`, against a theorem that exhausts the class')
say('  AT each `A` and says nothing about passing between them.')
SHAPES = [
    ('W1 across or uniform in the width', r'(?i)uniform(ly)? in (a|A|the (support|width))|across (all )?widths?|for all (A|a)\b|over the union'),
    ('W2 a support or radius condition', r'(?i)support (of|in|contained in|inside)|\bradius\b|\bwidth\b|\[-?A[,/ ]'),
    ('W3 an existential in the class', r'(?i)there exists (a )?[gf]\b|\bexists\b[^.]{0,40}\bsuch that\b'),
]
say('')
say('  ### SCOPE A -- THE TWO VERIFIED SOURCES, EVERY HIT PRINTED (capped per shape, the cap stated).')
for sname, spath in (('CC 2006.13771v1', CC), ('Lagarias math/0404394v4', LAG)):
    lines = read(spath).splitlines()
    for lab, rx in SHAPES:
        hits = [(k + 1, ln) for k, ln in enumerate(lines) if re.search(rx, ln)]
        say('  %-24s %-40s hits %d' % (sname, lab, len(hits)))
        for k, ln in hits[:24]:
            say('      %5d  %s' % (k, ln.strip()[:116]))
        if len(hits) > 24:
            say('      ... %d further hits not printed (cap 24 per shape per source)' % (len(hits) - 24))
say('')
say('  ### SCOPE B -- THE RECORD: every relay act bank (`data/b3NN_the_*.txt`, `data/b4NN_the_*.txt`), FACES_LEDGER.md')
say('  and FINDINGS.md; per file, the hit count and the first hit.')
banks = sorted(f for f in os.listdir(D) if re.match(r'b[34]\d\d_the_.*\.txt$', f))
files = [os.path.join(D, f) for f in banks] + [FL, os.path.join(PP, 'FINDINGS.md')]
say('  files in scope : %d' % len(files))
for lab, rx in SHAPES:
    tot, per = 0, []
    for p in files:
        t = fold(read(p))
        hs = list(re.finditer(rx, t))
        if hs:
            tot += len(hs)
            h = hs[0]
            per.append((os.path.basename(p), len(hs), t[max(0, h.start() - 70):h.end() + 70]))
    say('  %-40s hits %d in %d files' % (lab, tot, len(per)))
    for f, n, ctx in per:
        say('      %-44s %3d  ...%s...' % (f[:44], n, ctx[:150]))

rule()
say('### READ 8 -- SITES (i) AND (ii): THEIR OWN COUNTS, FROM THEIR OWN BANKED JSON.')
rule()
for lab, jf in (('site (i), b424', 'b424_candidates.json'), ('site (ii), b427', 'b427_candidates.json')):
    READS[0] += 1
    try:
        J = json.loads(read(os.path.join(D, jf)))
    except Exception as exc:
        MISS.append('%s : %s' % (jf, exc))
        say('  %-18s ### **MISS** -- %s' % (lab, exc))
        continue
    t = {}
    for c in J.get('candidates', []):
        if c.get('first') is not None:
            t[c['kind']] = t.get(c['kind'], 0) + 1
    say('  %-18s %d candidates ; %s' % (lab, len(J.get('candidates', [])),
                                        ' ; '.join('%s %d' % (k, v) for k, v in sorted(t.items(), key=lambda x: -x[1]))))

rule()
say('### READ 9 -- COMPONENT 2`S MATERIALS: THE DISPROOF INSTRUMENT, AND THE BARRIER`S OWN WORDS.')
rule()
quote('row F7, the Epstein negative control', FL, "F7 -- the Epstein negative control at b326's result",
      'a positive Li ledger with RH false', text=next((x for x in fl.splitlines() if x.startswith('| F7 ')), ''))
quote('  what the family cannot do', FL, 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN',
      'priced, not built.', text=next((x for x in fl.splitlines() if x.startswith('| F7 ')), ''))
quote('  the entailment', FL, 'IS A TEST THIS FAMILY CANNOT FAIL',
      text=next((x for x in fl.splitlines() if x.startswith('| F7 ')), ''))
quote('the phase condition (b328)', B328, 'the four-term sum at {rho, conj rho, 1 - rho, 1 - conj rho}',
      'negative only BELOW forty-five.')
quote('the aim map`s reach (b334)', B334, 'THE SQUARE AND THE REMAINDER, ON THE REACHING LEG: NOT REACHED',
      "outside the evaluator's reach.")
quote('the barrier keystone, Lemma 3.4`s reading', IB, 'That is: π can establish "P holds for x in a density-one subset',
      'but cannot certify individual elements.')
quote('the barrier keystone, Theorem 3.1-H`s clause', IB, 'the strongest statement `π` can establish has the form',
      'the individual element remains unreached.')
quote('the Epstein witness, Proposition 3.5', IB, 'Proposition 3.5 (Epstein witness).', 'is false.')

rule()
say('### READ 10 -- HAS ANY LANE ASKED THE DISPROOF QUESTION? A SEARCH, EVERY HIT PRINTED.')
rule()
DSHAPES = [('a counterexample lane', r'(?i)counterexampl\w*|disproof|disprove|refut\w* the hypothesis|RH is false'),
           ('a feasible-reach question', r'(?i)feasible reach|at what (height|reach)|what would a counterexample')]
for lab, rx in DSHAPES:
    tot, per = 0, []
    for p in files:
        t = fold(read(p))
        hs = list(re.finditer(rx, t))
        if hs:
            tot += len(hs)
            per.append((os.path.basename(p), len(hs), t[max(0, hs[0].start() - 70):hs[0].end() + 70]))
    say('  %-40s hits %d in %d files' % (lab, tot, len(per)))
    for f, n, ctx in per[:18]:
        say('      %-44s %3d  ...%s...' % (f[:44], n, ctx[:140]))
    if len(per) > 18:
        say('      ... %d further files not printed' % (len(per) - 18))

rule()
say('### READ 11 -- COMPONENT 3`S MATERIALS: THE THREE GRADES, AND WHAT THE CORPUS SAYS OF NAVIER-STOKES.')
rule()
quote('the three grades, in the corpus`s own README', RDM, '### The three grades', 'labelled as such wherever they appear.')
quote('the three grades, in the exclusion keystone', os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md'),
      'Every kernel citation in this paper carries one of three grades', 'A shell is a work-order, not a citation.')
quote('what the corpus says of Navier-Stokes', os.path.join(PP, 'day1', 'A_Place_to_Stand.md'),
      'For Navier-Stokes, three structural conflicts', 'on their own terms.')
NS = []
for p in files:
    t = fold(read(p))
    if re.search(r'(?i)navier', t):
        NS.append(os.path.basename(p))
say('  relay banks and ledgers naming Navier-Stokes : %d %s' % (len(NS), NS[:10]))
say('  ### **THE CORPUS HAS NEVER GRADED A PROOF IT DID NOT WRITE**, and the search above is the evidence offered')
say('  ### for that sentence rather than a recollection; the act states it as a search result and not as a fact.')

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : %d' % READS[0])
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for x in MISS:
    say('      %s' % x)
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if MISS else 0)
