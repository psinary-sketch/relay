# -*- coding: utf-8 -*-
"""b420_extract.py -- THE SURVEY FOR b420. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### Four components and one ruling: (R36) the lock and the scan; C1 the records the proof dates; C2 the
### proof's reach priced; C3 the face's kernel clauses re-read; C4 the barrier lemma put to positivity.
### ### **NOTHING IS WRITTEN OUTSIDE THIS ACT'S OWN RECORD**, and nothing is compiled.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
FL = os.path.join(PP, 'FACES_LEDGER.md')
SPF = os.path.join(KERN, 'Core', 'SinglePrimeFactor.lean')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
SMG = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
CORR = os.path.join(KERN, 'CORRESPONDENCE.md')
OUT = os.path.join(D, 'b420_extract.txt')
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


def quote(label, path, start, end=None, width=96, cap=900):
    READS[0] += 1
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-44s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = src[i:j + len(end)] if j > i else src[i:i + cap]
    seg = re.sub(r'\s+', ' ', seg).strip()
    say('  %-44s %s line %d' % (label, os.path.basename(path), src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


def lines(label, path, pattern, cap=12, width=150):
    """### A SEARCH READ: every line matching, with its number -- printed, capped, and the cap said."""
    READS[0] += 1
    src = read(path).splitlines()
    hits = [(k + 1, x) for k, x in enumerate(src) if re.search(pattern, x)]
    say('  %-44s %s : %d line(s) match %r%s' % (label, os.path.basename(path), len(hits), pattern,
                                                 ' ; first %d printed' % cap if len(hits) > cap else ''))
    for k, x in hits[:cap]:
        say('      %5d | %s' % (k, x.strip()[:width]))
    if not hits:
        MISS.append('%s : no line matches %r' % (label, pattern))
    return hits


rule('=')
say('b420_extract.py -- THE SURVEY: THE PROOF CITED, THE LOCK RULED, THE LEMMA AIMED.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROW 268 BY ITS MARKER, THE MODULE AND ITS PRINTED TERMINALS.')
rule()
corr = read(CORR)
m268 = [int(m.group(1)) for m in re.finditer(r'(?m)^\| (\d+) \| \*\*THE GENERAL CLAUSE IS PROVED, ZERO AXIOMS', corr)]
say('  row of b419`s marker : %s' % m268)
if m268 != [268]:
    MISS.append('b419`s row is not 268 by its marker')
quote('the general clause, as the module states it', SMG, 'theorem smear_general', ':= by')
prof = read(os.path.join(KERN, 'AXIOM_PRINTS.txt')).splitlines()
say('  AXIOM_PRINTS.txt : %d lines ; its last two :' % len(prof))
for x in prof[-2:]:
    say('      | %s' % x)

rule()
say('### READ 1 -- (R36): THE TWO RULES IT RULES BETWEEN, AND WHERE A TRIGGERED ITEM IS RECORDED.')
rule()
quote('the lock gate`s ferry gate', os.path.join(T, 'b378_lockgate.py'), "('the ferry scan (struck clauses and stems)'", '),')
quote('the scan`s doctrine', os.path.join(T, 'ferry_scan.py'), '# ### (1) ### **A HIT IS A STRING, NOT A FAULT.**', '# ### (2)')
quote('(R23), an item with no trigger is shelved', os.path.join(PP, 'OPEN_TRAILS.md'),
      '**RULING (R23), THE AUTHOR’S, RATIFIED BY THE FERRY AND STRIKEABLE: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS SHELVED.**', None, cap=300)
quote('b419`s trail on the lock', os.path.join(PP, 'OPEN_TRAILS.md'), '**Priced, not resolved.** The lock gate admits only', 'Routed to the author.')

rule()
say('### READ 2 -- COMPONENT 1: THE RECORDS THE PROOF DATES.')
rule()
quote('SinglePrimeFactor: the named open statement', SPF, '## THE NAMED OPEN STATEMENT', 'this module adds none.')
quote('SinglePrimeFactor: the cells` docstring', SPF, 'Every cell `B329.cells` decides satisfies the predicate.', 'this act does not prove it. -/')
m263 = [(int(m.group(1)), m.start()) for m in re.finditer(r"(?m)^\| (\d+) \| \*\*THE KERNEL'S OWN HEADER NAMED THE MISSING IDENTIFICATION", corr)]
say('  b414`s row, by its marker : %s' % [r for r, _ in m263])
if [r for r, _ in m263] != [263]:
    MISS.append('b414`s row is not 263 by its marker')
else:
    row = corr[m263[0][1]:corr.find(NL, m263[0][1])]
    for s in wrap(re.sub(r'\s+', ' ', row)[:700], 96):
        say('      | %s' % s)
    say('  ### row 263 names the statement OPEN : %s' % bool(re.search(r'OPEN|NOT PROVED|not proved', row)))
tw = read(os.path.join(D, 'b419_twentyeight.txt')).splitlines()
qual = [x for x in tw if 'QUALIFIED BY THE PROOF   b414:' in x]
say('  b419`s QUALIFIED rows : %d' % len(qual))
for x in qual:
    f = x.split()[1]
    say('      %-100s ferry banked : %s' % (x.strip()[:100], os.path.exists(os.path.join(D, f))))
b414 = read(os.path.join(D, 'b414_components.txt')).splitlines()
ia = next((k for k, x in enumerate(b414) if 'GROUP A -- A PROOF WOULD MAKE THESE TRUE AS WRITTEN : 8' in x), None)
say('  ### the sentences themselves, as b414 printed them (its lines %s onward) :' % (ia + 2 if ia is not None else '?'))
for x in (b414[ia + 1:ia + 17] if ia is not None else []):
    say('      | %s' % x.strip()[:150])

rule()
say('### READ 3 -- COMPONENT 2: WHAT SEPARATES THE MODEL`S ARITHMETIC FROM THE SOURCE`S TRACE.')
rule()
quote('the seal: what it does not certify', SEAL, 'WHAT IT DOES NOT CERTIFY.', 'NOT COMPILED HERE.')
quote('the kernel`s signed count', SEAL, "/-- b310's signed count at a unit", "(offBallFixed p n u (ballQ p n) : Int)")
quote('b310: the source`s move', os.path.join(D, 'b310_the_smear_collapses.txt'), '### The source\'s move, quoted by b304', 'SUM over k of w_k Tr(theta(p^k) Pi)`.**')
quote('b310: the derivation', os.path.join(D, 'b310_the_smear_collapses.txt'), '### ### **GENERAL IN `p`, `n` AND THE WEIGHT:**', 'THEREFORE `T(w) = w_0 * (p^n - 1)^2`.**')
quote('b310: the unified fixed-point formula', os.path.join(D, 'b310_the_smear_collapses.txt'),
      '### ### **`Tr(theta(t) Pi)` IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO', 'HAAR FACTOR.**')
quote('b310: the formula as registered', os.path.join(D, 'b310_registration_2026-09-03.txt'), '`Tr(theta(t) Pi) = |t| * ( A_N(t) - (1/q) A_q(t) )`', None, cap=500)
lines('b304: the frame and the ambient', os.path.join(D, 'b304_the_demands_shape.txt'), r'(?i)ambient|frame algebra|Haar|L\^2\(Q_p\)|L2\(Q_p\)', cap=14)
lines('b310: the ambient and the embedding', os.path.join(D, 'b310_the_smear_collapses.txt'), r'(?i)ambient|embedding|Haar', cap=10)

rule()
say('### READ 4 -- COMPONENT 3: b419`S KERNEL CLAUSES, AND THE BUILD PROCEDURE IN WRITING.')
rule()
f419 = os.path.join(D, 'b419_registration_2026-09-11.txt')
lines('b419`s face: the kernel write clauses', f419, r'KIND [3-7]\b|BAR 3 --|\(ii\) ### \*\*`AllPrints|\(iii\) ### \*\*`AXIOM_PRINTS', cap=12)
quote('the kernel README: the build section', os.path.join(KERN, 'README.md'), '## Building (the verified path', '## Provenance')
lines('b314: the cold clone`s build lines', os.path.join(D, 'b314_the_fold_and_the_cold_clone.txt'), r'LEAN_PATH|AllPrints|AXIOM_PRINTS', cap=10)

rule()
say('### READ 5 -- COMPONENT 4: THE LEMMA, ITS DEFINITIONS, AND THE ARC`S OWN OBJECTS.')
rule()
quote('Definition 2.1', IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
quote('Definition 2.2', IB, '**Definition 2.2 (Interface).**', None, cap=420)
quote('Definition 2.3', IB, '**Definition 2.3 (Target parameter).**', 'universal statement* for P on M.')
quote('Definition 2.3`s example for xi', IB, '- For M = ξ(s): I can be the product formula', 'Re(x) = 1/2."')
quote('Definition 2.4: P-dark', IB, 'κ = 0 indicates I is *P-dark*', 'without attenuation.')
quote('Definition 2.5, clause 1', IB, '1. The sentences mentioned in π_j', 'to cross I.')
quote('Definition 2.5, a proof factors', IB, '**Proof π factors through I for P** if every inference step', 'for P.')
quote('Theorem 3.1', IB, '**Theorem 3.1 (Sieve Ceiling Lemma).**', '(∀x ∈ M: P(x)).*')
quote('Theorem 3.1: the strongest statement', IB, '*That is: π can establish', 'individual elements.*')
quote('Proposition 3.5: kappa asserted', IB, 'For ξ, I is essential and κ(σ, I) = 0.', None, cap=60)
quote('Corollary 3.6', IB, '**Corollary 3.6 (Bright-interface access).**', 'at some step.*')
quote('the scope: Tier 2 not claimed', IB, 'research-frontier and not claimed', None, cap=80)
quote('section 9: the archimedean row', IB, '**The archimedean row.**', 'not a new theorem.')
quote('section 9: the per-place table', IB, '**The per-place table.**', 'not narrowed here.')
quote('section 10: Theorem 3.1-H', IB, '**Theorem 3.1-H (relativized form).**', 'remains unreached.*')
quote('section 10.1: the consequence', IB, '**Consequence.** Three of the four factor', 'Proposition C.1.')
quote('the ledger`s column law: its writer', FL, '**THE COLUMN LAW.**', None, cap=260)
lines('the ledger: the sole writer', FL, r'b327_faces_row', cap=4, width=220)
quote('row S1: the clause stated', FL, 'S1 -- the clause stated:', 'in the arc\'s vocabulary')
quote('row S1: the grade table', FL, 'THE GRADE TABLE, each grade its owner\'s:', 'UNOWNED, the clause itself.')
quote('row U1: the shape named', FL, 'U1 -- the uniformity obstruction:', 'indexed by it')
quote('row U1: its refusal', FL, 'NOTHING IS CLAIMED ABOUT THE EQUIVALENCE OF* them', 'in either direction*', cap=400)
quote('b400: Theorem 1 as verified', os.path.join(D, 'b400_components_run2.txt'), '### **THEOREM 1 CARRIES A SUPPORT HYPOTHESIS**', 'theta(g)*)."*')
quote('b400: Proposition C.1 as verified', os.path.join(D, 'b400_components_run2.txt'), '### **PROPOSITION C.1 CARRIES NONE**', 'for all z in F."*')
quote('b400: the lawful class and the primes', os.path.join(D, 'b400_components_run2.txt'), 'Theorem 1`s support condition is exactly', 'failure of that condition.')
quote('b334: answer (1)', os.path.join(D, 'b334_the_aim_map.txt'), '### ### **(1) FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN', 'positive at 28 of 28.')
quote('b334: what the map says', os.path.join(D, 'b334_the_aim_map.txt'), '### IT SAYS that for zeta the prime sum is inside the margin', 'NOTHING MORE.**')
quote('b407: the hypothesis that fails', os.path.join(D, 'b407_the_barriers_own_instance.txt'), '### ### **THE ONE THAT FAILS IS THE ONE ABOUT `π`.**', 'HAS NOT DISCHARGED.**')
quote('b410: the certified single-place row', os.path.join(D, 'b410_components.txt'), '### ### **RESTRICTED TO THE DENSITY REGISTER.**', 'two independent routes).')

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : %d' % READS[0])
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')
io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(1 if MISS else 0)
