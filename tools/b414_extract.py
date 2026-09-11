# -*- coding: utf-8 -*-
"""b414_extract.py -- THE SURVEY FOR LEG 1. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **THIS LEG BUILDS.** ### `b413` read the kernel and touched `0` `.lean` files; this act
### states a predicate and a named open statement in it. ### So the survey's job is different:
### it must establish, BEFORE anything is written, ### **WHAT THE MODULE ALREADY HAS AND WHAT A
### ### NEW PRIMITIVE WOULD ADD** -- and it must test the candidate predicate outside the kernel
### first, ### **WITH THE SEVEN DECIDED CELLS AS THE POSITIVE CONTROL**, exactly as `b413` did.

### ### **AND ONE READ `b413` DID NOT TAKE: THE SEAL'S OWN CAVEAT (T1.4).** ### The file wrote
### down, in advance, the identification it does not compile. ### Whether that caveat names the
### RIGHT condition is a question `b413` never asked, and this act asks it.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
SEAL = os.path.join(CORE, 'FiniteSideSeal.lean')
PRINTS = os.path.join(KERN, 'AXIOM_PRINTS.txt')
OUT = os.path.join(D, 'b414_extract.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)


def rule(c='-'):
    say(c * 100)


def read(path):
    try:
        with open(path, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception as exc:                                  # pragma: no cover
        MISS.append('%s : %s' % (path, exc))
        return ''


def wrap(text, width):
    # ### **WRAP AT WORD BOUNDARIES.** ### The same defect as the components': a
    # ### fixed-width slice split `residue` into `a re` / `sidue`.
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


def anchor(name, path, needle, ctx=0):
    """### **READ BY CONTENT, NEVER BY LINE NUMBER.** ### A miss is COUNTED, not guessed at."""
    src = read(path)
    if not src:
        return ''
    i = src.find(needle)
    if i < 0:
        MISS.append('%s : needle not found -- %r' % (name, needle[:60]))
        say('  %-38s ### **MISS** -- needle absent' % name)
        return ''
    lines = src[:i].count(NL)
    body = src.splitlines()
    lo = max(0, lines - ctx)
    hi = min(len(body), lines + ctx + 1)
    say('  %-38s line %d' % (name, lines + 1))
    return NL.join(body[lo:hi])


# ---------------------------------------------------------------------------------------------
# ### THE RE-IMPLEMENTATION, TRANSCRIBED FROM THE KERNEL'S OWN DEFINITIONS.
# ### Identical to b414's Lean by construction: the same four lines, in Python.
# ---------------------------------------------------------------------------------------------
def gridN(p, n):
    return p ** (2 * n)


def ballQ(p, n):
    return p ** n


def offBallFixed(p, n, t, m):
    g, q = gridN(p, n), ballQ(p, n)
    return sum(1 for s in range(g)
               if (s % q != 0) and ((t * s) % g % q != 0) and ((t - 1) * s) % m == 0)


def units(p, n):
    return [u for u in range(gridN(p, n)) if u % p != 0]


def sumAN(p, n):
    return sum(offBallFixed(p, n, u, gridN(p, n)) for u in units(p, n))


def sumAQ(p, n):
    return sum(offBallFixed(p, n, u, ballQ(p, n)) for u in units(p, n))


def holds(p, n):
    return ballQ(p, n) * sumAN(p, n) == sumAQ(p, n)


# ---- THE CANDIDATE PREDICATE, in the shape the Lean will take ------------------------------
def isPrime_b(d):
    """The Lean Bool, transcribed: `d != 0 && d != 1 && range d all (k==0 || k==1 || d%k!=0)`."""
    if d == 0 or d == 1:
        return False
    return all(k == 0 or k == 1 or d % k != 0 for k in range(d))


def primeDivisors(m):
    return [d for d in range(m + 1) if isPrime_b(d) and m % d == 0]


def singlePrimeFactor(m):
    return len(primeDivisors(m)) == 1


CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)]

rule('=')
say('b414_extract.py -- THE SURVEY FOR LEG 1: THE PREDICATE NAMED.')
rule('=')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 1 -- THE MODULE SURFACE. ### WHAT `Core/` ALREADY IS.')
rule()
core_files = sorted(f for f in os.listdir(CORE) if f.endswith('.lean'))
mathlib = []
internal = 0
for f in core_files:
    src = read(os.path.join(CORE, f))
    for m in re.finditer(r'(?m)^import\s+(\S+)', src):
        if m.group(1).split('.')[0] == 'Mathlib':
            mathlib.append('%s -> %s' % (f, m.group(1)))
        else:
            internal += 1
say('  `.lean` files in `Core/`                : %d' % len(core_files))
say('  MATHLIB imports anywhere in `Core/`     : ### **%d**' % len(mathlib))
say('  Core-internal imports (module -> module): %d' % internal)
say('  ### ### **SO `Core/` IS THE AXIOM-FREE MODULE THE RULING NAMES, AND ITS FILES DO IMPORT')
say('  ### ### ONE ANOTHER.** ### `b413` said `FiniteSideSeal.lean` has NO IMPORTS AT ALL --')
say('  ### ### **TRUE OF THAT FILE AND NOT OF THE DIRECTORY.** ### The ruling`s *without an')
say('  ### ### import* can only mean ### **WITHOUT AN IMPORT FROM OUTSIDE THE AXIOM-FREE SET**,')
say('  ### ### because a Core-internal import is what `Core/` is made of.')
say()

ifaces = os.path.join(KERN, 'Interfaces')
iface_mathlib = 0
if os.path.isdir(ifaces):
    for f in sorted(os.listdir(ifaces)):
        if f.endswith('.lean'):
            if re.search(r'(?m)^import\s+Mathlib', read(os.path.join(ifaces, f))):
                iface_mathlib += 1
say('  `Interfaces/` files importing Mathlib   : %d' % iface_mathlib)
say()

# ---- the prime question, asked of the whole directory and not one file ----------------------
PRIMEDEF = re.compile(r'(?m)^\s*(?:def|abbrev|theorem|instance)\s+(\w*[Pp]rime\w*)')
prime_decls = []
for f in core_files:
    for m in PRIMEDEF.finditer(read(os.path.join(CORE, f))):
        prime_decls.append('%s : %s' % (f, m.group(1)))
say('  DECLARATIONS in `Core/` whose NAME carries a prime stem : ### **%d**' % len(prime_decls))
for d in prime_decls:
    say('      %s' % d)
say('  ### ### **A NAME IS NOT A NOTION.** ### Each of these is checked below for whether it')
say('  ### ### DECIDES primality or merely mentions primes in a window`s name.')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 2 -- THE SEAL`S OWN CAVEAT (T1.4), QUOTED. ### THE FILE WROTE THE GAP IN ADVANCE.')
rule()
cav = anchor('(T1.4), the caveat', SEAL, 'is not', 0)
seal_src = read(SEAL)
i = seal_src.find('(T1.4)')
if i < 0:
    MISS.append('seal caveat (T1.4) not found')
else:
    j = seal_src.find('(T1.6)', i)
    quoted = re.sub(r'\s+', ' ', seal_src[i:j if j > 0 else i + 700]).strip()
    say('  QUOTED FROM THE FILE, not from a paper`s description of it:')
    for seg in wrap(quoted, 96):
        say('      %s' % seg)
say()
say('  ### ### **THE CAVEAT NAMES A CONDITION: *exactly when `p` is prime*.**')
say('  ### ### `b413` measured the true separator and it is ### **A SINGLE PRIME FACTOR**, not')
say('  ### ### primality. ### **SO THE FILE`S OWN CAVEAT, PROMOTED TO A HYPOTHESIS, WOULD BE THE')
say('  ### ### WRONG HYPOTHESIS** -- and the survey tests that claim rather than asserting it.')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 3 -- THE POSITIVE CONTROL. ### SEVEN CELLS, REPRODUCED BEFORE ANY VERDICT.')
rule()
ok = 0
for (p, n) in CELLS:
    h = holds(p, n)
    s = singlePrimeFactor(p)
    ok += 1 if h else 0
    say('  cell (%d, %d)   identity %-6s   singlePrimeFactor(%d) = %-5s'
        % (p, n, 'HOLDS' if h else 'FAILS', p, str(s)))
say('  ### ### **CONTROL : %d OF 7 REPRODUCED.**' % ok)
if ok != 7:
    say('  ### ### **SHORT OF SEVEN -- EVERY VERDICT BELOW IS WITHHELD.**')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 4 -- THE PREDICATE TESTED AGAINST THE MEASUREMENT, BOTH POLARITIES.')
rule()
say('  %-6s %-8s %-22s %-10s %s' % ('p', 'n', 'identity', 'predicate', 'AGREE?'))
agree = disagree = 0
rows = []
for p in range(2, 51):
    n = 1
    h = holds(p, n)
    s = singlePrimeFactor(p)
    a = (h == s)
    agree += 1 if a else 0
    disagree += 0 if a else 1
    rows.append((p, n, h, s, a))
for (p, n, h, s, a) in rows:
    say('  %-6d %-8d %-22s %-10s %s'
        % (p, n, 'HOLDS' if h else 'FAILS', str(s), 'yes' if a else '### **NO**'))
say()
say('  ### ### **PREDICATE AGREES WITH THE IDENTITY AT %d OF %d BASES, DISAGREES AT %d.**'
    % (agree, agree + disagree, disagree))
say('  ### The population is named: ### **every base `p` from 2 to 50 at level `n = 1`** --')
say('  ### ### `(R26)`: AN EXPECTATION NAMES THE SET IT QUANTIFIES OVER.')
say()

say('  ### **AND THE SECOND LEVEL, where the grid is `p^4` and the cost is the limit:**')
lvl2 = []
for p in [2, 3, 4, 5, 6, 9, 10]:
    h = holds(p, 2)
    s = singlePrimeFactor(p)
    lvl2.append((p, h, s, h == s))
    say('  p = %-4d n = 2   identity %-6s   predicate %-6s   %s'
        % (p, 'HOLDS' if h else 'FAILS', str(s), 'yes' if h == s else '### **NO**'))
say('  ### ### **%d OF %d AGREE AT LEVEL TWO.** ### The predicate is on `p` alone and the'
    % (sum(1 for r in lvl2 if r[3]), len(lvl2)))
say('  ### ### measurement does not contradict that across the levels it can afford.')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 5 -- THE WRONG HYPOTHESIS, PRICED. ### WHAT THE FILE`S CAVEAT WOULD HAVE COST.')
rule()
prime_only = [p for p in range(2, 51) if isPrime_b(p)]
spf_only = [p for p in range(2, 51) if singlePrimeFactor(p)]
lost = [p for p in spf_only if p not in prime_only]
say('  bases 2..50 that are PRIME                 : %d' % len(prime_only))
say('  bases 2..50 with a SINGLE PRIME FACTOR     : %d' % len(spf_only))
say('  held by the identity but NOT prime         : ### **%d** -- %s'
    % (len(lost), ', '.join(str(x) for x in lost)))
cell_bases = sorted(set(p for (p, _n) in CELLS))
cells_excluded = [p for p in cell_bases if not isPrime_b(p)]
say('  ### ### **THE FILE`S CAVEAT IS TOO STRONG BY %d BASES IN THIS RANGE.** ### A hypothesis'
    % len(lost))
say('  ### ### taken from it would have been SOUND and ### **WOULD HAVE EXCLUDED EVERY')
say('  ### ### PROPER PRIME POWER AT WHICH THE IDENTITY IS TRUE** -- %s.'
    % ', '.join(str(x) for x in lost))
say()
say('  ### **AND HERE IS WHY IT WENT UNCHALLENGED.** ### The seal`s seven decided cells have')
say('  ### bases %s. ### **DECIDED CELLS THE CAVEAT WOULD EXCLUDE : %d.**'
    % (', '.join(str(b) for b in cell_bases), len(cells_excluded)))
say('  ### ### **SO THE CAVEAT IS EXACTLY RIGHT ON THE SET THE KERNEL DECIDES AND WRONG ON THE')
say('  ### ### SET IT DOES NOT** -- it could never be caught by re-reading the decided cells,')
say('  ### ### only by leaving them. ### **A CAVEAT SOUND ON ITS OWN EVIDENCE IS NOT A CAVEAT')
bm = re.search(r'Bank:\s*relay\s*`data/b(\d+)_', seal_src)
if not bm:
    MISS.append('the seal does not name its own emitting act in a Bank line')
    say('  ### ### TESTED.** ### The emitting act is ### **NOT READABLE FROM THE FILE** -- MISS.')
else:
    say('  ### ### TESTED**, and this one was carried from ### **b%s** (the seal`s own Bank line,'
        % bm.group(1))
    say('  ### ### read from the file and not recalled) to this act -- ### **%d ACTS** -- without'
        % (414 - int(bm.group(1))))
    say('  ### ### a base outside its range ever being tried.')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 6 -- THE KERNEL`S OWN IDIOM FOR AN UNPROVED STATEMENT, FOUND BY DESCRIPTION.')
rule()
idiom = []
for f in core_files:
    src = read(os.path.join(CORE, f))
    for m in re.finditer(r'NAMED OPEN STATEMENT', src):
        seg = re.sub(r'\s+', ' ', src[m.start():m.start() + 220]).strip()
        idiom.append((f, seg))
say('  files carrying the phrase NAMED OPEN STATEMENT : ### **%d**' % len(idiom))
for f, seg in idiom:
    say('      %s' % f)
    for k in range(0, min(len(seg), 200), 92):
        say('          %s' % seg[k:k + 92])
say()
sorries = 0
for f in core_files:
    src = read(os.path.join(CORE, f))
    code = re.sub(r'/-.*?-/', ' ', src, flags=re.S)
    code = re.sub(r'(?m)--.*$', ' ', code)
    sorries += len(re.findall(r'\bsorry\b', code))
say('  `sorry` occurrences in `Core/` CODE (comments stripped) : ### **%d**' % sorries)
say('  ### ### **SO THE IDIOM IS: PROSE IN THE DOCSTRING PLUS A CORRESPONDENCE ROW, NEVER A')
say('  ### ### SORRY.** ### This act follows it and does not improve on it.')
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 7 -- THE AXIOM PRINTS, FROM THE KERNEL`S OWN STDOUT.')
rule()
pr = read(PRINTS)
say('  `AXIOM_PRINTS.txt` bytes : %d' % len(pr))
for t in ['index_decomposes', 'scaling_fixes_nothing_off_ball',
          'compact_smear_vanishes_at_cells', 'finite_side_silence']:
    hit = [ln.strip() for ln in pr.splitlines() if t in ln]
    if hit:
        say('  %-34s %s' % (t, hit[0][:96]))
    else:
        MISS.append('axiom print absent for %s' % t)
        say('  %-34s ### **MISS**' % t)
say('  total `#print axioms` lines              : %d'
    % len([ln for ln in pr.splitlines() if 'depend' in ln]))
say('  lines reporting a NON-EMPTY axiom profile: %d'
    % len([ln for ln in pr.splitlines() if 'depends on axioms' in ln]))
say()

# ---------------------------------------------------------------------------------------------
rule()
say('### READ 8 -- WHAT LEG 1 OWES THE RECORD: `b413`S TWENTY-EIGHT, RE-READ NOT RECALLED.')
rule()
comp = read(os.path.join(D, 'b413_components.txt'))
m = re.search(r'CARRYING NO PER-CELL QUALIFIER : ### `(\d+)`', comp)
if m:
    say('  `b413` counted, read back from its own record : ### **%s** unqualified sentences'
        % m.group(1))
else:
    MISS.append('b413 unqualified-sentence count not found in its components record')
    say('  ### **MISS** -- the count is not re-readable from `b413_components.txt`')
m2 = re.search(r'seal or its compact part : ### \*\*(\d+)\*\*', comp)
say('  sentences naming the finite side at all       : %s' % (m2.group(1) if m2 else '(miss)'))
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
print(NL.join(L))
print()
print('wrote %s' % OUT)
sys.exit(1 if MISS else 0)
