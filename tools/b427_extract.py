# -*- coding: utf-8 -*-
"""b427_extract.py -- THE SURVEY FOR b427, THE SORTIE'S SECOND LEG: THE WITNESS ARC AT SITE (ii).
### **EVERY READ ANCHORED IN THE MARKUP-FOLDED TEXT, EVERY MISS COUNTED, THE CANDIDATE SEARCH PRINTED IN FULL.
### NOTHING WRITTEN OUTSIDE THIS ACT'S RECORD. ### RUN EXACTLY AS b424 RAN SITE (i).**
"""
import io
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
OUT = os.path.join(D, 'b427_extract.txt')
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
    """### MARKUP FOLDED BEFORE MATCHING: banks hard-wrap through `###` and bold marks."""
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
        say('  %-48s ### **MISS** -- anchor absent in %s' % (label, name))
        return ''
    j = src.find(e0, i + len(s0)) if end else -1
    seg = src[i:j + len(e0)] if j > i else src[i:i + cap]
    say('  %-48s %s' % (label, name))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


rule('=')
say('b427_extract.py -- THE SURVEY: THE WITNESS ARC AT SITE (ii), THE SORTIE`S SECOND LEG.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: b426`S ROW BY ITS MARKER.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m = [int(x.group(1)) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*THE FALSIFIER RE-READ BY ADDRESS UNDER \(R38\)", corr)]
say('  row of b426`s marker : %s' % m)
if m != [275]:
    MISS.append('b426`s row is not 275 by its marker')

rule()
say('### READ 1 -- THE SITE: ROW U1`S ENTRY (ii), ITS WITNESS CELL, AND THE FREEZE.')
rule()
fl = read(FL)
u1 = next((x for x in fl.splitlines() if x.startswith('| U1 ')), '')
say('  row U1 present : %s ; bytes %d' % (bool(u1), len(u1.encode('utf-8'))))
quote('the site, as entered (b351)', FL, "(ii) THE HEIGHT COORDINATE'S ENUMERATION",
      'BOUNDED BY A MEASUREMENT and not by an argument.', text=u1)
quote('the WITNESS cell for (ii)', FL, '(ii) — KIND: NOT EMPTY. WITNESS: NONE KNOWN.',
      'could not do for the height', text=u1)
quote('what a shared witness is, in the row', FL, 'WITNESS IS SOURCED FROM THE COMPILED THEOREM AND FROM NOWHERE ELSE.',
      'PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.', text=u1)
quote('the route to any site, priced (b405)', FL, 'not one of the six sites is stated in those terms',
      'six sites, zero candidates.', text=u1)
quote('the freeze (b409)', FL, 'THE REGISTER IS FROZEN AT SIX, b409.', 'NO SEVENTH SITE IS ENTERED.', text=u1)
w = re.findall(r'WITNESS: *`([A-Z ]+)`', u1)
say('  the six WITNESS fields : %s' % w)

rule()
say('### READ 2 -- THE SITE`S OWN STATEMENT, IN THE ACT THAT ENTERED IT (b351).')
rule()
B351 = os.path.join(D, 'b351_the_partition_question.txt')
quote('the height, its kind of bound', B351, 'THE HEIGHT `gamma`. ### **BOUNDED BY A MEASUREMENT',
      'THE COORDINATE IS NOT.')
quote('where the census stopped', B351, 'THE NUMBER `150` IS WHERE THE CENSUS STOPPED',
      'IT IS NOT A PROPERTY OF THE OBJECT.')
quote('the class that would have to be proved silent', B351, 'THE CLASS THAT WOULD HAVE TO BE PROVED SILENT: `gamma > 150`',
      'A CLASS IS NOT MADE OF INSTANCES.')
quote('the missing statement, typed', B351, '`(M-gamma)` *"there exist `T0` and finitely many classes',
      'the statement needs a class.')
quote('the sentence the WITNESS cell cites', B351, 'one convergent series did what sixty boxes of argument principle',
      'those two kinds of work.')
quote('the census itself, and its count', B351, 'The completeness census ran the argument principle',
      "`180` ZEROS OF `Lambda_Q` WITH `0 < t < 150`")
quote('the main term that says the instances never run out', B351, 'The Riemann-von Mangoldt main term',
      'A CLASS IS NOT MADE OF INSTANCES.')

rule()
say('### READ 3 -- THE COMPILED FORM, AT THE PIN THE ROW CITES (SIDE-lv-conservation 93c27ec = v0.10.0).')
rule()
t3 = subprocess.run(['git', '-C', LV, 'show', '93c27ec:SIDELvConservation/T3_StepNineBridge.lean'],
                    capture_output=True).stdout.decode('utf-8', 'replace')
tag = subprocess.run(['git', '-C', LV, 'tag', '--points-at', '93c27ec'], capture_output=True, text=True).stdout.strip()
say('  tag at 93c27ec : %s' % tag)
quote('T3prime_shared_witness', 'T3_StepNineBridge.lean@93c27ec', 'theorem T3prime_shared_witness', '⟨Phi, h1, h2⟩', text=t3)
quote('why both clauses are needed', 'T3_StepNineBridge.lean@93c27ec', 'This is not a weakening of T3;',
      'no bookkeeping, no swap.', text=t3)

rule()
say('### READ 4 -- THE STARTING POPULATION: THE NAVIGATOR`S THREE, EACH AT ITS RECORD LOCATION.')
rule()
say('')
say('  [B1] THE CLASSICAL ZERO-FREE REGION AS BOUNDING ABSCISSA, NOT MARGIN')
quote('  the region itself, in the corpus`s words', os.path.join(PP, 'day1', 'Which_Structure_Confines.md'),
      'The Euler product converges absolutely for σ > 1', 'no zero-free region.')
quote('  its behaviour in height', os.path.join(PP, 'meta', 'RAIL_ONLY_PRESERVATION_2026-08-09.md'),
      'The persistence finding: stripping the Gamma envelope', 'widens without bound.')
quote('  what it reaches, and what it never does', os.path.join(PP, 'day1', 'A_Place_to_Stand.md'),
      'The boundary is exact: Λ(n) ≥ 0 yields the edge of the strip', 'crosses to the critical line.')
say('')
say('  [B2] A GROWTH BOUND ON THE MARGIN IN HEIGHT')
quote('  the growth, and the range it was measured over', os.path.join(PP, 'meta', 'RAIL_ONLY_PRESERVATION_2026-08-09.md'),
      'stabilizes at approximately $0.251 \\pm 0.055$ across 30 zeros', 'widens without bound.')
quote('  the record`s own word for a bound of this kind', B351, 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE.')
say('')
say('  [B3] THE DENSITY THEOREMS AS THE REGISTER THE CHANNELS ARE BRIGHT FOR')
quote('  the register, named', os.path.join(PP, 'day1', 'Silence_of_Foundations.md'),
      'Classical sieve methods operate through this coupling.', 'is κ = 0.')
quote('  the standing screen, I-7', os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'),
      'The screen, one question, asked of the DEFINITION', 'REFUSE THE COMPUTATION, and state why.')
quote('  its evidence base, four routes one boundary', os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md'),
      'The evidence base — four independent derivations of the same boundary',
      'the density register does not reach placement.')
quote('  the barrier stated as a theorem about the channel', os.path.join(PP, 'internal', 'TECHNE_ELEMENTS.md'),
      'The sieve operates through the distributive interface', 'through which classical tools operate.')

rule()
say('### READ 5 -- THE TWO VERIFIED SOURCES, AT THE STATEMENTS THAT QUANTIFY OVER A HEIGHT OR A ZERO SET.')
rule()
quote('CC Proposition C.1, over the whole zero set', CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)')
quote('CC Theorem 1, its support hypothesis', CC, 'Theorem 1 Let g P C8', 'Trpϑpgq Sϑpgq˚q. (4)')
quote('CC Theorem 6.11', CC, 'Theorem 6.11 LetgPC8', 'log 2. (141)')
quote('CC, small enough intervals', CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')
quote('Lagarias Theorem 2.2 (Li`s criterion), all n', LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', 'n ≥ 1. (2.21)')
quote('Lagarias Theorem 5.1, a constant K(pi) from some n on', LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)')
quote('Lagarias Theorem 6.1, an O-term in n', LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')

rule()
say('### READ 6 -- THE SEARCH FOR FURTHER CANDIDATES, BY DESCRIPTION, PRINTED IN FULL.')
rule()
say('  THE DESCRIPTION, FIXED BEFORE THE SEARCH: a statement or object that would serve EVERY height at once --')
say('  one argument valid for all `gamma` (or all `T`), or an object the record names as a witness in height,')
say('  against a method that produces zeros one at a time.')
SHAPES = [
    ('H1 quantified over all heights', r'(?i)\bfor (all|any|every) (t|T|gamma|γ|heights?|zeros?)\b|\ball (heights|zeros)\b'),
    ('H2 uniform or unconditional in height', r'(?i)\buniform(ly)? in (t|T|gamma|γ|height)|\bunconditional\w*\b[^.]{0,50}\b(zero|height|T)\b'),
    ('H3 a bound or region valid above some height', r'(?i)\b(for|when|whenever)\s+(t|T|gamma|γ)\s*[>≥]|\bT_?0\b|\babove\s+(some\s+)?height\b'),
]
say('')
say('  ### SCOPE A -- THE TWO VERIFIED SOURCES, EVERY HIT PRINTED.')
for sname, spath in (('CC 2006.13771v1', CC), ('Lagarias math/0404394v4', LAG)):
    lines = read(spath).splitlines()
    for lab, rx in SHAPES:
        hits = [(k + 1, ln) for k, ln in enumerate(lines) if re.search(rx, ln)]
        say('  %-24s %-44s hits %d' % (sname, lab, len(hits)))
        for k, ln in hits[:30]:
            say('      %5d  %s' % (k, ln.strip()[:118]))
        if len(hits) > 30:
            say('      ... %d further hits not printed' % (len(hits) - 30))
say('')
say('  ### SCOPE B -- THE RECORD: every relay act bank (`data/b3NN_the_*.txt`, `data/b4NN_the_*.txt`), FACES_LEDGER.md,')
say('  FINDINGS.md and the four documents the starting population cites; per file, the hit count and the first hit.')
banks = sorted(f for f in os.listdir(D) if re.match(r'b[34]\d\d_the_.*\.txt$', f))
files = ([os.path.join(D, f) for f in banks] + [FL, os.path.join(PP, 'FINDINGS.md')]
         + [os.path.join(PP, 'day1', 'Which_Structure_Confines.md'),
            os.path.join(PP, 'day1', 'Silence_of_Foundations.md'),
            os.path.join(PP, 'meta', 'RAIL_ONLY_PRESERVATION_2026-08-09.md'),
            os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')])
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
    say('  %-44s hits %d in %d files' % (lab, tot, len(per)))
    for f, n, ctx in per:
        say('      %-44s %3d  ...%s...' % (f[:44], n, ctx[:150]))

rule()
say('### READ 7 -- SITE (i)`S OWN FAILURE COUNTS, SO THE ARC CAN BE COMPARED RATHER THAN RECALLED.')
rule()
quote('b424`s first failing steps, counted', os.path.join(D, 'b424_the_witness_arc_at_site_i.txt'),
      'NO WITNESS HELD. 16 candidates, 0 held.', 'on the site’s own text.')
quote('b424`s three steps, in their fixed order', os.path.join(D, 'b424_the_witness_arc_at_site_i.txt'),
      'Each was attempted by three steps in the order the locked face fixed', 'failed at the first it failed:')

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
