# -*- coding: utf-8 -*-
"""b421_extract.py -- THE SURVEY FOR b421. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### Three components and one added line: C1 the finite ambient built or priced; C2 hypothesis 1's missing
### specification priced; C3 the span counted; and the navigator's three b420 conflations entered with the
### seat's corrections. ### **NOTHING IS COMPILED HERE AND NOTHING IS WRITTEN OUTSIDE THIS ACT'S RECORD.**
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
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
SMG = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
CORR = os.path.join(KERN, 'CORRESPONDENCE.md')
OUT = os.path.join(D, 'b421_extract.txt')
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
    seg = re.sub(r'\s+', ' ', src[i:j + len(end)] if j > i else src[i:i + cap]).strip()
    say('  %-44s %s line %d' % (label, os.path.basename(path), src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      | %s' % s)
    return seg


rule('=')
say('b421_extract.py -- THE SURVEY: THE FINITE AMBIENT, THE SPECIFICATION, THE SPAN, AND THE CONFLATIONS.')
rule('=')

rule()
say('### READ 0 -- THE ORIENTATION: ROW 269 BY ITS MARKER, AND THE TWO RECORDS THE FERRY CITES.')
rule()
corr = read(CORR)
m269 = [int(m.group(1)) for m in re.finditer(r"(?m)^\| (\d+) \| \*\*THE BARRIER LEMMA DOES NOT REACH THE ARC'S POSITIVITY", corr)]
say('  row of b420`s marker : %s' % m269)
if m269 != [269]:
    MISS.append('b420`s row is not 269 by its marker')
quote('b420 part (i), priced', os.path.join(D, 'b420_c2_priced.txt'), 'PART (i) -- ON THE FINITE AMBIENT', 'OPERATOR AND ITS TRACE.**')
quote('b420 hypothesis 1, as read', os.path.join(D, 'b420_c4_barrier.txt'), '### **FOR THE STRUCTURE WHOSE ELEMENTS ARE THE CLASS`S TEST FUNCTIONS', 'the keystone does not.')

rule()
say('### READ 1 -- COMPONENT 1: WHAT THE KERNEL ALREADY STATES, AND WHAT b310 SAYS THE TRACE COUNTS.')
rule()
for label, start, end in (('the grid', 'def gridN (p n : Nat)', ':= p ^ (2 * n)'),
                          ('the ball', 'def ballQ (p n : Nat)', ':= p ^ n'),
                          ('the fixed off-ball count', "/-- The off-ball points that multiplication by `t` fixes modulo `m`, counted.", '% m == 0)).length'),
                          ('the signed count', "/-- b310's signed count at a unit", '(offBallFixed p n u (ballQ p n) : Int)')):
    quote(label, SEAL, start, end)
quote('b310: the unified formula', os.path.join(D, 'b310_registration_2026-09-03.txt'), '`Tr(theta(t) Pi) = |t| * ( A_N(t) - (1/q) A_q(t) )`', '(t - 1) s = 0 mod M }`.**')
quote('b310: the reading of that formula', os.path.join(D, 'b310_the_smear_collapses.txt'), '### ### **`Tr(theta(t) Pi)` IS A SIGNED COUNT OF THE OFF-BALL POINTS `t` FIXES, IN THE TWO', 'HAAR FACTOR.**')
quote('the seal: the scope the new lemma inherits', SEAL, 'WHAT IT DOES NOT CERTIFY.', 'NOT COMPILED HERE.')
quote('the kernel`s character', os.path.join(KERN, 'Core', 'SinglePrimeFactor.lean'), 'Lean 4 (v4.29.1, pinned)', 'never assumed.')
names = re.findall(r'(?m)^theorem (\S+)', read(SMG))
say('  SmearGeneral`s theorems available to import : %d ; the remainder and filter helpers among them :' % len(names))
say('      %s' % ', '.join(n for n in names if re.search(r'mod|filter|sumf|ind|range|beq|length', n))[:900])
ap = read(os.path.join(KERN, 'AllPrints.lean'))
say('  AllPrints.lean : imports %d, the last %r ; prints %d' % (len(re.findall(r'(?m)^import ', ap)),
                                                          re.findall(r'(?m)^import .*', ap)[-1], len(re.findall(r'(?m)^#print axioms', ap))))
pb = subprocess.run(['git', '-C', KERN, 'show', 'HEAD:AXIOM_PRINTS.txt'], capture_output=True).stdout
say('  AXIOM_PRINTS.txt at HEAD : %d lines' % pb.count(b'\n'))
quote('b420: the corrected AllPrints form', os.path.join(D, 'b420_c3_clauses.txt'), 'CORRECTED FORM : AllPrints.lean: ONE import line INSERTED', 'nothing else.')

rule()
say('### READ 2 -- COMPONENT 2: WHAT "DETERMINED" MEANS, IN BOTH DOCUMENTS THAT DEFINE IT.')
rule()
quote('the keystone`s logic', IB, 'Throughout, we work in classical first-order logic.', 'in a domain |M|.')
quote('the keystone`s Definition 2.1', IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.')
quote('the keystone`s scope line on its proof', IB, 'The proof uses standard first-order logic and basic model theory', 'are required.')
k = read(IB)
say('  the keystone names Lowenheim-Skolem, categoricity or second-order semantics : %s'
    % bool(re.search(r'(?i)l(ö|o)wenheim|categoric|second-order semantics', k)))
quote('the monograph`s formal definition', MONO, '**Formal:** System X is determined by specification S', 'logical consequences of S.')
quote('the monograph`s specification of xi', MONO, 'For ξ(s): the specification is θ(τ) = Σ exp(πin²τ)', 'No human choices enter.')
quote('the monograph`s one-line claim', MONO, '**(1)** The completed zeta function ξ(s) is determined by the specification', 'No free parameters.')
quote('the class the structure would have to carry', os.path.join(D, 'b400_components_run2.txt'), '### **PROPOSITION C.1 CARRIES NONE**', 'for all z in F."*')
quote('b407: hypothesis 1 as b407 read it', os.path.join(D, 'b407_the_barriers_own_instance.txt'), '### Four of Theorem 3.1’s five hypotheses are', 'κ(σ, I) = 0."*')
hits = []
for root, dirs, files in os.walk(PP):
    dirs[:] = [x for x in dirs if x not in ('.git', 'archive')]
    for f in files:
        if f.endswith('.md'):
            s = read(os.path.join(root, f))
            if re.search(r'(?i)specification[^.\n]{0,80}(test function|C_c|the class)', s):
                hits.append(os.path.relpath(os.path.join(root, f), PP))
say('  documents in PLACE-papers (live) naming a specification near the test functions or the class : %d' % len(hits))
for h in hits[:12]:
    say('      %s' % h)

rule()
say('### READ 3 -- COMPONENT 3: THE SPAN, COUNTED BY THE TOOL IN ITS READ MODE (IT WRITES NOTHING).')
rule()
READS[0] += 1
r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'b363_span.py')], capture_output=True, text=True,
                   encoding='utf-8', errors='replace')
say('  b363_span.py exit : %d' % r.returncode)
for ln in (r.stdout or '').splitlines():
    if re.search(r'(?i)span|threshold|fold|last|act', ln) and ln.strip():
        say('      | %s' % ln.rstrip()[:150])
if r.returncode != 0:
    MISS.append('the span tool did not exit 0')
quote('(R1), the threshold', os.path.join(D, 'b366_extract_notes.txt'), '(R1) THE FOLD THRESHOLD is NINE acts.', None, cap=260)

rule()
say('### READ 4 -- THE CLOSING`S ADDED LINE: THE THREE b420 CONFLATIONS, AND THE CORRECTIONS b420 PRINTED.')
rule()
c4 = os.path.join(D, 'b420_c4_barrier.txt')
quote('(1) the navigator`s words for the theorem', os.path.join(D, 'b420_ferry.txt'), 'the general clause proved at b419, which returns', 'nothing about its sign;')
quote('    the seat`s correction', c4, '### **b419`S TERMINAL DOES NOT MENTION A TEST FUNCTION', 'Component 2 prices.')
quote('(2) the compressed trace against the place`s term', c4, '### **AND THE FINITE PLACE`S TERM IN THE', 'the prime`s powers.')
quote('    the source b420 quoted for it', os.path.join(D, 'b310_the_smear_collapses.txt'), 'The arithmetic is in the distribution, not in', 'as its prime sum.')
quote('(3) the navigator`s words for the map', os.path.join(D, 'b420_ferry.txt'), 'the aim map measured — every aim', 'at any height.')
quote('    the map`s own scope sentence', os.path.join(D, 'b334_the_aim_map.txt'), '### IT SAYS that for zeta the prime sum is inside the margin', 'NOTHING MORE.**')
quote('    the seat`s correction', c4, '### **THE WORDING DIFFERS, AND THE SOURCE GOVERNS:**', 'at any height*.')

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
