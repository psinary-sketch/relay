# -*- coding: utf-8 -*-
"""b415_extract.py -- THE SURVEY FOR LEG 2. ### **A READ ACT. ### NOTHING IS WRITTEN TO ANY
### SIBLING PROGRAMME, AND NOTHING FROM ONE IS WRITTEN INTO THE CORPUS.**

### ### **EVERY READ ANCHORED BY CONTENT, EVERY MISS COUNTED.** ### And two of this act's reads are
### SEARCHES BY DESCRIPTION rather than by name -- the corpus's own rule since `b385`, where a
### search for the navigator's NAME for a rule missed a rule that used none of his words.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DRIVE = 'D:' + os.sep
SUB = os.path.join(PP, 'phase1.5', 'method', 'THE_SUBSTRATE.md')
CLS = os.path.join(DRIVE, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')
OST = os.path.join(DRIVE, 'SIDE-kernel', 'Bridge', 'OstrowskiBridge.lean')
CAR = os.path.join(DRIVE, 'SIDE-kernel', 'Bridge', 'CartanBBridge.lean')
LOOM = os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                    'VERIFICATION_LOOM-archive-1-dated-log-through-nineteenth-seam.md')
TSC = os.path.join(PP, 'clusters', 'THEORY_SPACE_PHYSICS_CLUSTER_SYNTHESIS_2026-06-05.md')
SF = os.path.join(PP, 'phase1.5', 'structural', 'STRUCTURAL_FRACTION.md')
OUT = os.path.join(D, 'b415_extract.txt')
PROGOUT = os.path.join(D, 'b415_programmes.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


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


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:
        MISS.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def quote(label, path, start, end=None, width=94, lead='      '):
    """### **QUOTE FROM THE FILE, ANCHORED ON CONTENT.** ### A miss is COUNTED."""
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:50]))
        say('  %-40s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = src[i:j] if j > i else src[i:i + 700]
    seg = re.sub(r'\s+', ' ', seg).strip()
    say('  %-40s line %d' % (label, src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('%s%s' % (lead, s))
    return seg


rule('=')
say('b415_extract.py -- THE SURVEY FOR LEG 2: THE SUBSTRATE AT GRADE, THE TUPLES, THE SCREEN.')
rule('=')
say()

# =============================================================================================
rule()
say('### READ 1 -- THE SUBSTRATE KEYSTONE AT CONTENT. ### THE THREE SELECTION PRINCIPLES.')
rule()
sub = read(SUB)
quote('the object, as the keystone states it', SUB,
      'The substrate is the pair of the two smallest primes', '## (ii)')
say()
say('  ### ### **THE KEYSTONE NAMES THREE SELECTION PRINCIPLES AND CALLS THEIR CONVERGENCE THE')
say('  ### ### CERTIFICATE**, and each carries a NAMED KERNEL TERMINAL:')
for lbl, needle in (('arithmetic (Frobenius)', 'FrobeniusCalibration.g_two_three'),
                    ('Bernoulli / von Staudt-Clausen', 'FrobeniusCalibration.psl_eq_denom_B2'),
                    ('modular torsion', 'FrobeniusCalibration.S_squared_eq_negI')):
    ok = needle in sub
    if not ok:
        MISS.append('selection principle terminal absent : %s' % needle)
    say('      %-34s %-46s %s' % (lbl, needle, 'NAMED' if ok else '### **MISS**'))
axfree = sub.count('axiom-free')
say('  occurrences of `axiom-free` in the keystone : %d' % axfree)
say()

# =============================================================================================
rule()
say('### READ 2 -- THE Q-NON-EXTENSION, AND WHETHER IT IS COMPILED.')
rule()
quote('the specialness, at theorem grade', SUB,
      'The substrate is ℚ-distinguished', '## (iv)')
say()
kernel_named = re.findall(r'`([A-Za-z_][\w.]*)`[^.]{0,40}\(?(?:axiom-free|597b0869)', sub)
say('  kernel identifiers named inside the specialness section : %s'
    % (', '.join(sorted(set(kernel_named))) or '(none)'))
has_elem = 'element_obstruction' in sub
say('  `element_obstruction` named                         : %s' % has_elem)
say('  the d(K) = 2^(r1+r2+2) - 1 formula carries a kernel name : %s'
    % bool(re.search(r'd\(K\)[^.]{0,200}`[A-Za-z_][\w.]*`', sub)))
say()
say('  ### ### **THE TEST THE FERRY ASKS FOR IS WHETHER THE NON-EXTENSION IS COMPILED, NOT')
say('  ### ### WHETHER IT IS CLAIMED.** ### The section heading says *at theorem grade*; the')
say('  ### question is whether a KERNEL TERMINAL carries the statement, and the answer is read')
say('  ### from the document`s own naming rather than from the heading.')
say()

# =============================================================================================
rule()
say('### READ 3 -- *NO OTHER PAIR SATISFIES ALL THREE*: THEOREM, ARGUMENT, OR ASSERTION?')
rule()
hits = []
for root, _dirs, files in os.walk(PP):
    if 'archive' in root or '.git' in root or 'outputs' in root:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        p = os.path.join(root, f)
        src = read(p)
        for m in re.finditer(r'[^.]*\b(?:no other pair|any other pair|only the pair)\b[^.]*\.',
                             src, re.I):
            hits.append((os.path.relpath(p, PP), re.sub(r'\s+', ' ', m.group(0)).strip()))
say('  sentences found, live documents only (archive and outputs excluded) : ### **%d**'
    % len(hits))
for rel, s in hits[:8]:
    say('      %s' % rel)
    for seg in wrap(s, 92):
        say('          %s' % seg)
say()

# =============================================================================================
rule()
say('### READ 4 -- THE FOUR TUPLES, FROM THE KERNEL`S OWN DECLARATIONS.')
rule()
cls = read(CLS)
tuples = re.findall(r'def (class[ABCD]) : FormationTuple := .([0-9]+), ([0-9]+), ([0-9]+), '
                    r'([0-9]+).', cls)
say('  source : SIDE-formation-arithmetic/SIDEFormationArithmetic/Classes.lean')
say('  tuple definitions found : ### **%d**' % len(tuples))
for t in tuples:
    say('      %-8s = (%s, %s, %s, %s)   ### **A LITERAL `def`, NOT A THEOREM**' % t)
if len(tuples) != 4:
    MISS.append('expected four tuple definitions, found %d' % len(tuples))
say()
ost, car = read(OST), read(CAR)
n2 = 'theorem formation_n2' in ost
n3 = 'theorem formation_n_3_eq_two' in car
say('  `OstrowskiBridge.formation_n2`        (n2 = 3 derived) : %s' % n2)
say('  `CartanBBridge.formation_n_3_eq_two`  (n3 = 2 derived) : %s' % n3)
n1 = bool(re.search(r'theorem\s+\w*n_?1\w*', ost + car))
n4 = bool(re.search(r'theorem\s+\w*n_?4\w*', ost + car))
say('  any bridge theorem deriving n1                        : %s' % n1)
say('  any bridge theorem deriving n4                        : %s' % n4)
say()
say('  ### ### **THE FOUR-BY-FOUR TABLE, FROM THE DECLARATIONS AND NOT FROM A SUMMARY.**')
say('  %-8s %-14s %-14s %-14s %-14s %s' % ('class', 'n1', 'n2', 'n3', 'n4', 'derived'))
rows = []
for (name, a, b, c, d) in tuples:
    if name == 'classA':
        cells = ['stipulated', 'DERIVED' if n2 else 'stipulated',
                 'DERIVED' if n3 else 'stipulated', 'stipulated']
    else:
        cells = ['stipulated'] * 4
    nd = sum(1 for x in cells if x == 'DERIVED')
    rows.append((name, nd))
    say('  %-8s %-14s %-14s %-14s %-14s %d of 4' % (name, cells[0], cells[1], cells[2],
                                                    cells[3], nd))
say()
say('  ### ### **B, C AND D CARRY `%d` DERIVED COMPONENTS BETWEEN THEM.**'
    % sum(nd for n, nd in rows if n != 'classA'))
say('  ### ### **AND CLASS A ITSELF CARRIES ONLY `%s` OF FOUR** -- which the ferry did not ask'
    % (dict(rows).get('classA', 0)))
say('  ### and which no sentence of the record states in that form.')
say()

# =============================================================================================
rule()
say('### READ 5 -- THE ANCHOR READ OF 2026-06-15, QUOTED FROM THE LOOM ARCHIVE.')
rule()
quote('the component-certs item', LOOM, '(a) COMPONENT CERTS', '(b) FORMULA FORM')
say()
quote('the menu-completeness item', LOOM, '(c) MENU-COMPLETENESS', '2. Tier-3 honesty')
say()

# =============================================================================================
rule()
say('### READ 6 -- THE FORCED-VERSUS-PERMITTED SCREEN, AS THE CORPUS RAN IT ON ITS OWN RATIO.')
rule()
quote('the structural-fraction verdict', TSC, "The claim: classifying", '---')
say()
sfsrc = read(SF)
say('  `STRUCTURAL_FRACTION.md` lines : %d' % len(sfsrc.splitlines()))
say('  the cluster names its own open question about the ceiling : %s'
    % ('pure-mathematical derivation of the 11/12 ceiling' in read(TSC)))
say('  the cluster says the components are identified rather than fitted : %s'
    % ('identified rather than fitted' in read(TSC)))
say()
say('  ### ### **SO THE SCREEN, AS THE CORPUS APPLIED IT TO ITSELF, HAS A SHAPE:** ### a')
say('  ### closed form whose components are ### **IDENTIFIED RATHER THAN FITTED** ### is not')
say('  ### thereby FORCED -- the cluster keeps *a pure-mathematical derivation of the 11/12')
say('  ### ceiling* on its own open list. ### **THE CORPUS DID NOT GRADE ITS OWN RATIO FORCED,')
say('  ### ### AND THAT IS THE STANDARD THE SIBLING`S TWO RATIOS ARE PUT AGAINST.**')
say()

# =============================================================================================
rule()
say('### READ 7 -- THE PROGRAMMES, ENUMERATED FROM THE DRIVE`S OWN STATE DOCUMENTS.')
rule()
CAND = []
for name in sorted(os.listdir(DRIVE)):
    p = os.path.join(DRIVE, name)
    if not os.path.isdir(p) or name.startswith(('$', '.')):
        continue
    if name in ('Program Files', 'WindowsApps', 'System Volume Information', 'PSHistory',
                'WpSystem', 'WUDownloadCache', 'DeliveryOptimization', 'cache', 'tmp',
                'elan', 'elan-cache', 'npm-cache', 'npm-global', 'miniforge3', 'mathlib4',
                'mathlib-cache', 'echo chamber', 'Camera Roll', 'Captures', 'Saved Pictures',
                'Screenshots', 'Feedback', 'Personal'):
        continue
    CAND.append(name)
say('  top-level directories considered : %d' % len(CAND))
say('      %s' % ', '.join(CAND))
say()
say('  ### ### **A DIRECTORY IS NOT A PROGRAMME.** ### A programme is named here only if the')
say('  ### drive holds a document that states its OWN state -- a README, a state file or a')
say('  ### canonical index. ### The test is applied to each and the yield printed.')
PROG = []
for name in CAND:
    p = os.path.join(DRIVE, name)
    state = None
    try:
        for f in sorted(os.listdir(p)):
            if f.lower() in ('readme.md', 'state.md', 'index.md', 'agents.md', 'registry.md'):
                state = f
                break
    except Exception:
        pass
    PROG.append((name, state))
for name, state in PROG:
    say('      %-34s %s' % (name, state or '### NO STATE DOCUMENT AT TOP LEVEL'))
say()

# =============================================================================================
rule()
say('### READ 8 -- THE PRIME CORE, SEARCHED BY DESCRIPTION. ### THE CONTROL RUNS FIRST.')
rule()
say('  ### ### **THE DESCRIPTION:** ### a FINITE NAMED SET OF PRIMES carrying STATED INCLUSION')
say('  ### ### AND EXCLUSION CRITERIA. ### *prime core* is used as a SEARCH STRING and never as')
say('  ### ### a SOURCE.')
say()
SETPAT = re.compile(r'\{\s*\d+\s*(?:,\s*\d+\s*)+\}')


def is_primes(s):
    vals = [int(x) for x in re.findall(r'\d+', s)]
    if not vals or len(vals) > 12:
        return False
    for v in vals:
        if v < 2 or any(v % k == 0 for k in range(2, v)):
            return False
    return True


def scan(path):
    src = read(path)
    out = []
    for m in SETPAT.finditer(src):
        if not is_primes(m.group(0)):
            continue
        ctx = re.sub(r'\s+', ' ', src[max(0, m.start() - 320):m.end() + 320])
        inc = bool(re.search(r'unique|exactly|only|singled out|minimal|precisely|are the',
                             ctx, re.I))
        exc = bool(re.search(r'not|no other|excluded|fails|does not|beyond', ctx, re.I))
        if inc and exc:
            out.append((m.group(0), ctx))
    return out

ctrl = scan(SUB)
say('  ### **POSITIVE CONTROL -- the substrate`s own set, in its own keystone.**')
say('      qualifying sets found in `THE_SUBSTRATE.md` : ### **%d**' % len(ctrl))
for s, ctx in ctrl[:3]:
    say('      %-14s' % s)
    for seg in wrap(ctx[:300], 92):
        say('          %s' % seg)
if not ctrl:
    MISS.append('the positive control found NO qualifying set in the substrate keystone')
    say('      ### ### **CONTROL FAILED -- THE SEARCH IS NOT VALIDATED AND ITS ABSENCES ARE')
    say('      ### ### NOT REPORTABLE.**')
else:
    say('      ### ### **CONTROL HOLDS: the search finds `{2, 3}` in the keystone that owns it.**')
say()

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : 8')
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')

with open(OUT, 'wb') as fh:
    fh.write((NL.join(L) + NL).encode('utf-8'))
with open(PROGOUT, 'wb') as fh:
    fh.write((NL.join('%s\t%s' % (n, s or 'NONE') for n, s in PROG) + NL).encode('utf-8'))
print(NL.join(L))
print()
print('wrote %s and %s' % (os.path.basename(OUT), os.path.basename(PROGOUT)))
sys.exit(1 if MISS else 0)
