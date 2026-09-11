# -*- coding: utf-8 -*-
"""b424_extract.py -- THE SURVEY FOR b424, THE SORTIE'S SECOND LEG: THE WITNESS ARC AT SITE (i).
### **EVERY READ ANCHORED IN THE MARKUP-FOLDED TEXT, EVERY MISS COUNTED, THE CANDIDATE SEARCH PRINTED IN FULL.
### NOTHING WRITTEN OUTSIDE THIS ACT'S RECORD.**
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
OUT = os.path.join(D, 'b424_extract.txt')
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
        say('  %-44s ### **MISS** -- anchor absent in %s' % (label, name))
        return ''
    j = src.find(e0, i + len(s0)) if end else -1
    seg = src[i:j + len(e0)] if j > i else src[i:i + cap]
    say('  %-44s %s' % (label, name))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


rule('=')
say('b424_extract.py -- THE SURVEY: THE WITNESS ARC AT SITE (i), THE SORTIE`S SECOND LEG.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: b423`S ROW BY ITS MARKER.')
rule()
corr = read(os.path.join(KERN, 'CORRESPONDENCE.md'))
m = [int(x.group(1)) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*THE \(R37\) QUESTION READ", corr)]
say('  row of b423`s marker : %s' % m)
if m != [272]:
    MISS.append('b423`s row is not 272 by its marker')

rule()
say('### READ 1 -- THE SITE: ROW U1`S ENTRY (i), ITS WITNESS CELL, AND THE FREEZE.')
rule()
fl = read(FL)
u1 = next((x for x in fl.splitlines() if x.startswith('| U1 ')), '')
say('  row U1 present : %s ; bytes %d' % (bool(u1), len(u1.encode('utf-8'))))
quote('the site, as entered (b332)', FL, "(i) THE CLAUSE'S QUANTIFIER", 'and they are the clause."', text=u1)
quote('the site`s own statement (b332`s bank)', os.path.join(D, 'b332_the_clause_stated.txt'),
      'the quantifiers -- over the class, infinite, and through the explicit formula over', 'they are the clause.')
quote('the WITNESS cell for (i)', FL, '(i) — KIND: NOT EMPTY. WITNESS: UNSTATED.',
      'THE RIGHT KIND OF THING TO LOOK FOR HERE.', text=u1)
quote('what a shared witness is, in the row', FL, 'WITNESS IS SOURCED FROM THE COMPILED THEOREM AND FROM NOWHERE ELSE.',
      'PER-MEMBER WITNESSES DO NOT ADD UP TO A SHARED ONE.', text=u1)
quote('the route to any site, priced (b405)', FL, 'not one of the six sites is stated in those terms',
      'six sites, zero candidates.', text=u1)
quote('the freeze (b409)', FL, 'THE REGISTER IS FROZEN AT SIX, b409.', 'NO SEVENTH SITE IS ENTERED.', text=u1)
quote('what the freeze keeps', FL, 'A FREEZE IS NOT A CLOSURE', 'every cell keeps its text', text=u1)
w = re.findall(r'WITNESS: *`([A-Z ]+)`', u1)
say('  the six WITNESS fields : %s' % w)

rule()
say('### READ 2 -- THE COMPILED FORM, AT THE PIN THE ROW CITES (SIDE-lv-conservation 93c27ec = v0.10.0).')
rule()
t3 = subprocess.run(['git', '-C', LV, 'show', '93c27ec:SIDELvConservation/T3_StepNineBridge.lean'],
                    capture_output=True).stdout.decode('utf-8', 'replace')
tag = subprocess.run(['git', '-C', LV, 'tag', '--points-at', '93c27ec'], capture_output=True, text=True).stdout.strip()
say('  tag at 93c27ec : %s' % tag)
quote('T3prime_shared_witness', 'T3_StepNineBridge.lean@93c27ec', 'theorem T3prime_shared_witness', '⟨Phi, h1, h2⟩', text=t3)
quote('what h1 and h2 are', 'T3_StepNineBridge.lean@93c27ec', 'This is not a weakening of T3;', 'no bookkeeping, no swap.', text=t3)

rule()
say('### READ 3 -- THE STARTING POPULATION: b422`S FOUR, EACH AT ITS RECORD LOCATION AND ITS SOURCE.')
rule()
quote('the opening list, verbatim (b422)', os.path.join(D, 'b422_witness_arc.txt'), "The navigator's first-draft enumeration",
      'nothing more.')
say('')
say('  [A1] the lawful-class bound as a witness on the wrong class')
quote('  CC Theorem 1, its class', CC, 'Theorem 1 Let g P C8', 'Trpϑpgq Sϑpgq˚q. (4)')
quote('  CC, the design', CC, 'In this paper we consider the simplest instance of this', 'so that rational primes are not involved')
quote('  b400: Theorem 1 against Prop. C.1', os.path.join(D, 'b400_closing.txt'), 'THEOREM 1 CARRIES A SUPPORT HYPOTHESIS',
      'THE CRITERION IS STILL IN FORCE')
quote('  CC Proposition C.1, the site`s class', CC, 'Proposition C.1 Let Z Ă C be the set of non-trivial zeros', '@zPF. (155)')
say('')
say('  [A2] the wide-support bound confirmed absent')
quote('  b400: the one absent element (Q400)', os.path.join(D, 'b400_closing.txt'), 'THE ONE ABSENT ELEMENT, AND IT IS THE ONLY ONE:',
      'AGAINST AN ARCHIMEDEAN QUANTITY.')
quote('  b400: the class it would range over', os.path.join(D, 'b400_closing.txt'), 'THE QUESTION. At a support with',
      'is not identically zero:')
quote('  b401: the search`s verdict', os.path.join(D, 'b401_closing.txt'), 'NOTHING EVALUATES OR BOUNDS SUM_p W_p(f) AT a^2 >= 2',
      'or in the corpus.')
say('')
say('  [A3] exhaustion at each radius not across')
quote('  b353: Boas-Kac, as banked', os.path.join(D, 'b353_the_missing_statement.txt'), 'There exists g in Cc^infty(R)', 'f = g * g^*')
quote('  b353: the index boundary', os.path.join(D, 'b353_the_missing_statement.txt'), 'SO: AN EXHAUSTION AT EVERY WIDTH',
      'ACROSS WIDTHS.')
quote('  b353: the import', os.path.join(D, 'b353_the_missing_statement.txt'), 'Boas-Kac internally means proving a factorisation theorem.',
      'NO WORK-ORDER IS OPENED')
say('')
say('  [A4] the approximation register closed')
quote('  b362: the space', os.path.join(D, 'b362_the_approximation_register.txt'), 'the space is K = L2(]0, inf[, dt)', 'over the complex numbers;')
quote('  b362: a criterion is a translation', os.path.join(D, 'b362_the_approximation_register.txt'), 'A CRITERION IS A TRANSLATION',
      'CONDITIONAL RESULT.')
quote('  b362: the verdict', os.path.join(D, 'b362_the_approximation_register.txt'), 'THEREFORE: LOCATED BUT NOT WORTH OPENING', 'fourth branch.')
quote('  b362: the import bar', os.path.join(D, 'b362_the_approximation_register.txt'), 'Every located statement is graded',
      'TRUSTED-AT-CITE')

rule()
say('### READ 4 -- WHAT THE RECORD ALREADY NAMES AS A WITNESS, AND THE OWNED GENERAL STATEMENTS.')
rule()
quote('the navigator`s two named witnesses (U1)', FL, 'AND THE NAVIGATOR NAMED TWO WITNESSES AS ALREADY FOUND',
      'NEITHER SURVIVES THE SITES’ OWN TEXT.', text=u1)
quote('  the abscissa`s convergent sum', FL, 'The abscissa’s convergent sum is a witness for no site of this row',
      'was therefore never entered.', text=u1)
quote('  the finite side`s zero', FL, 'The finite side’s zero is not a shared witness across places either',
      'discharged by decide', text=u1)
quote('Theorem 5.1`s constant, as row (v) reads it', FL, 'Theorem 5.1’s absolute constant is a witness for the ARCHIMEDEAN side',
      'and not for this one.', text=u1)
quote('SmearGeneral.smear_general', os.path.join(KERN, 'Core', 'SmearGeneral.lean'), 'theorem smear_general (p n : Nat)',
      'B329.sumAQ p n')
quote('GridTrace.grid_trace_is_signed_count', os.path.join(KERN, 'Core', 'GridTrace.lean'),
      'theorem grid_trace_is_signed_count (p n t : Nat)', 'B329.signedTrace p n t')

rule()
say('### READ 5 -- THE TWO VERIFIED SOURCES, AT THE STATEMENTS THE RECORD HAS ALREADY MET.')
rule()
quote('CC Theorem 6.11', CC, 'Theorem 6.11 LetgPC8', 'log 2. (141)')
quote('CC, small enough intervals', CC, 'As a preliminary test we prove, using a simple estimate', 'the positivity holds.')
quote('Lagarias Theorem 2.2 (Li`s criterion)', LAG, 'Theorem 2.2. Letπ be an irreducible cuspidal', 'n ≥ 1. (2.21)')
quote('Lagarias Theorem 5.1', LAG, 'Theorem 5.1. For any irreducible cuspidal', '(5.1)')
quote('Lagarias Theorem 6.1', LAG, 'Theorem 6.1. For any irreducible cuspidal', 'depends on π.')

rule()
say('### READ 6 -- THE SEARCH FOR FURTHER CANDIDATES, BY DESCRIPTION, PRINTED IN FULL.')
rule()
say('  THE DESCRIPTION, FIXED BEFORE THE SEARCH: a statement or object that would serve EVERY member of site')
say('  (i)`s class at once -- a positivity, bound or identity quantified over the test functions, or an object')
say('  the record names as a witness.')
SHAPES = [
    ('W1 a witness named', r'(?i)\b(shared|joint|common) witness|\bwitness(es)? (for|on|at|to) '),
    ('W2 quantified over test functions', r'(?i)\bfor (all|any|every) (smooth|positive|test|g\b|f\b|function)'),
    ('W3 a positivity or bound over a class', r'(?i)(positiv\w*|inequalit\w*|bound\w*)[^.]{0,60}\b(for all|for any|for every)\b'),
]
say('')
say('  ### SCOPE A -- THE TWO VERIFIED SOURCES, EVERY HIT PRINTED.')
for sname, spath in (('CC 2006.13771v1', CC), ('Lagarias math/0404394v4', LAG)):
    lines = read(spath).splitlines()
    for lab, rx in SHAPES:
        hits = [(k + 1, ln) for k, ln in enumerate(lines) if re.search(rx, ln)]
        say('  %-24s %-40s hits %d' % (sname, lab, len(hits)))
        for k, ln in hits:
            say('      %5d  %s' % (k, ln.strip()[:120]))
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
        hs = [mm for mm in re.finditer(rx, t)]
        if hs:
            tot += len(hs)
            h = hs[0]
            per.append((os.path.basename(p), len(hs), t[max(0, h.start() - 70):h.end() + 70]))
    say('  %-40s hits %d in %d files' % (lab, tot, len(per)))
    for f, n, ctx in per:
        say('      %-44s %3d  ...%s...' % (f[:44], n, ctx[:150]))

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
