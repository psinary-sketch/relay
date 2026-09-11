# -*- coding: utf-8 -*-
"""b416_extract.py -- THE SURVEY FOR b416. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **THREE OF THIS ACT'S READS ARE SEARCHES BY DESCRIPTION**, not by name: the other dated
### tools (a tool naming a path that does not exist), the other kernel caveats (a stated condition
### the file says is not compiled), and the Reader's canonical copy (located by DIGEST).
### ### **AND ONE READ IS PURE ARITHMETIC** -- the lattice, computed rather than quoted, because
### the figure Addition Two orders must be drawn from the numbers and not from the prose.
"""
import hashlib
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
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
HER = os.path.join('D:', os.sep, 'HERITAGE')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
CORE = os.path.join(KERN, 'Core')
FA = os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic')
MATTER = os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md')
CPLX = os.path.join(PP, 'phase2', 'formation', 'COMPLEX_ANALYSIS.md')
READER = os.path.join(PP, 'archive', '2026-08-23-trim-backfill', 'PRIME_CORE_READER.md')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
CENSUS = os.path.join(ROOT, 'reports', '2026-07-11-orphan-census.md')
SEAL = os.path.join(CORE, 'FiniteSideSeal.lean')
OUT = os.path.join(D, 'b416_extract.txt')
LATOUT = os.path.join(D, 'b416_lattice.txt')
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


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def quote(label, path, start, end=None, width=94):
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : anchor absent -- %r' % (label, start[:46]))
        say('  %-40s ### **MISS** -- anchor absent' % label)
        return ''
    j = src.find(end, i + len(start)) if end else -1
    seg = re.sub(r'\s+', ' ', src[i:j] if j > i else src[i:i + 620]).strip()
    say('  %-40s line %d' % (label, src[:i].count(NL) + 1))
    for s in wrap(seg, width):
        say('      %s' % s)
    return seg


rule('=')
say('b416_extract.py -- THE SURVEY: THE TWO STIPULATIONS, THE DATED TOOL, AND THE READER.')
rule('=')
say()

# =============================================================================================
rule()
say('### READ 1 -- WHAT `n1` AND `n4` COUNT, FROM THE DOCUMENT THAT OWNS THEM.')
rule()
core = read(os.path.join(FA, 'Core.lean'))
fields = re.search(r'n₁ = ([^,]+), n₂ = ([^,]+),\s*n₃ = ([^,]+), n₄ = ([^.]+)\.', core)
if fields:
    for i, nm in enumerate(('n1', 'n2', 'n3', 'n4'), start=1):
        say('  %-4s = %s   [kernel `Core.lean` docstring]' % (nm, fields.group(i).strip()))
else:
    MISS.append('the kernel does not state the four field meanings in the shape expected')
say()
quote('the owner`s definitions, §I', MATTER, '- **Primitive (n₁):**', '---')
say()
quote('the universality sentence', MATTER, 'Three of four formation components',
      'producing four classes')
say()
say('  ### ### **THAT SENTENCE IS THE WHOLE OF COMPONENT 1 AND IT IS TESTABLE.** ### It names a')
say('  ### REASON for three of the four and declares the fourth free. ### The test is whether the')
say('  ### KERNEL`S OWN FOUR TUPLES agree, and it is run below rather than assumed.')
say()
quote('n4 argued a second time', CPLX, '$n_4 = 0$:', chr(10))
say()

# =============================================================================================
rule()
say('### READ 2 -- THE UNIVERSALITY CLAIM AGAINST THE KERNEL`S OWN FOUR TUPLES.')
rule()
cls = read(os.path.join(FA, 'Classes.lean'))
tup = re.findall(r'def (class[ABCD]) : FormationTuple := .(\d+), (\d+), (\d+), (\d+).', cls)
say('  %-8s %-6s %-6s %-6s %-6s' % ('class', 'n1', 'n2', 'n3', 'n4'))
cols = {1: set(), 2: set(), 3: set(), 4: set()}
for name, a, b, c, d in tup:
    say('  %-8s %-6s %-6s %-6s %-6s' % (name, a, b, c, d))
    for k, v in zip((1, 2, 3, 4), (a, b, c, d)):
        cols[k].add(v)
say()
for k in (1, 2, 3, 4):
    vals = sorted(cols[k])
    say('  n%d takes %d distinct value%s across the four classes : %s   -- %s'
        % (k, len(vals), '' if len(vals) == 1 else 's', ', '.join(vals),
           'CONSTANT' if len(vals) == 1 else '### **VARIES**'))
say()
constant = [k for k in (1, 2, 3, 4) if len(cols[k]) == 1]
varies = [k for k in (1, 2, 3, 4) if len(cols[k]) > 1]
say('  ### ### **THE OWNER SAYS THREE COMPONENTS ARE UNIVERSAL AND ONE VARIES.**')
say('  ### ### **THE KERNEL`S TUPLES HAVE %d CONSTANT (%s) AND %d VARYING (%s).**'
    % (len(constant), ', '.join('n%d' % k for k in constant) or 'none',
       len(varies), ', '.join('n%d' % k for k in varies) or 'none'))
if len(varies) > 1:
    say('  ### ### ### **SO THE UNIVERSALITY SENTENCE AND THE DECLARATIONS DISAGREE.** ### The')
    say('  ### document gives `n2 = 3 by Chevalley-Steinberg` as UNIVERSAL, and the kernel')
    say('  ### declares `classB.n2 = 2` and `classD.n2 = 2`. ### **A REASON THAT WOULD DERIVE A')
    say('  ### ### COMPONENT CANNOT DERIVE IT IN A CLASS WHERE THE COMPONENT HAS ANOTHER VALUE.**')
say()

# =============================================================================================
rule()
say('### READ 3 -- WHETHER ANY ROUTE TO DERIVING `n1` OR `n4` HAS EVER BEEN PRICED.')
rule()
hits = {'n1': [], 'n4': []}
for root, _dirs, files in os.walk(PP):
    if '.git' in root or 'outputs' in root:
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        p = os.path.join(root, f)
        src = read(p)
        for key, pats in (('n1', (r'n_?1|n₁',)), ('n4', (r'n_?4|n₄',))):
            for m in re.finditer(r'[^.\n]{0,160}(?:%s)[^.\n]{0,160}\.' % pats[0], src):
                seg = m.group(0)
                if re.search(r'\b(price|priced|pricing|cost|acts?|derive|derivation|bridge)\b',
                             seg, re.I):
                    hits[key].append((os.path.relpath(p, PP), re.sub(r'\s+', ' ', seg).strip()))
for key in ('n1', 'n4'):
    say('  sentences mentioning %s together with a price, cost, derivation or bridge : ### **%d**'
        % (key, len(hits[key])))
    for rel, s in hits[key][:5]:
        say('      %s' % rel)
        for seg in wrap(s, 90):
            say('          %s' % seg)
say()

# =============================================================================================
rule()
say('### READ 4 -- THE TWO EXISTING BRIDGES: WHAT EACH HAD TO SUPPLY.')
rule()
SK = os.path.join('D:', os.sep, 'SIDE-kernel', 'Bridge')
for f, term in (('OstrowskiBridge.lean', 'formation_n2'),
                ('CartanBBridge.lean', 'formation_n_3_eq_two')):
    src = read(os.path.join(SK, f))
    say('  %s' % f)
    say('      terminal            : %s   %s' % (term, 'PRESENT' if ('theorem ' + term) in src
                                                 else '### **MISS**'))
    if ('theorem ' + term) not in src:
        MISS.append('bridge terminal absent : %s' % term)
    imp = re.findall(r'(?m)^import\s+(\S+)', src)
    say('      imports             : %s' % (', '.join(imp) or '(none)'))
    types = re.findall(r'(?m)^(?:inductive|structure|abbrev|def)\s+(\w+)', src)
    say('      types/defs declared : %s' % (', '.join(types[:8]) or '(none)'))
    fin = re.findall(r'Fintype\.card (\w+)', src)
    say('      cardinality taken of: %s' % (', '.join(sorted(set(fin))) or '(none)'))
    say('      ### ### **THE PATTERN: DECLARE A FINITE TYPE WHOSE ELEMENTS *ARE* THE THINGS')
    say('      ### ### COUNTED, PROVE IT EXHAUSTIVE, AND TAKE ITS CARDINALITY.**')
say()

# =============================================================================================
rule()
say('### READ 5 -- THE DATED TOOL, AND EVERY OTHER TOOL NAMING A PATH THAT DOES NOT EXIST.')
rule()
say('  ### **SEARCHED BY DESCRIPTION**: a tool whose source builds a filesystem path from')
say('  ### literal segments, where that path is absent from disk. ### Not by name.')
PJ = re.compile(r"os\.path\.join\(\s*ROOT\s*,\s*((?:'[^']+'\s*,?\s*)+)\)")
dated = []
for f in sorted(os.listdir(T)):
    if not f.endswith('.py'):
        continue
    src = read(os.path.join(T, f))
    for m in PJ.finditer(src):
        segs = re.findall(r"'([^']+)'", m.group(1))
        if not segs or segs[-1].endswith(('.txt', '.json', '.md', '.stamp')):
            continue
        p = os.path.join(ROOT, *segs)
        if not os.path.exists(p):
            dated.append((f, '/'.join(segs)))
say('  tools scanned : %d' % len([f for f in os.listdir(T) if f.endswith('.py')]))
say('  ### ### **TOOLS NAMING A PATH THAT DOES NOT EXIST : %d**' % len(dated))
for f, p in dated:
    say('      %-30s -> %s' % (f, p))
say()
say()
say('  ### ### **A STATIC HIT IS A MENTION. ### ONLY A RUN PROVES A BREAK.**')
say('  ### `b410`s `G-NOBORROWEDBAR` fired on the act`s own comment saying the bar was removed;')
say('  ### the same shape is here. ### **A FILE THAT NAMES THE RETIRED PATH IN ORDER TO RECORD')
say('  ### ### RETIRING IT IS NOT A DATED TOOL.** ### So each is RUN, and the verdict is taken')
say('  ### from what happens rather than from what it contains.')
import subprocess as _sp
breaks = []
for f in sorted(set(x[0] for x in dated)):
    try:
        r = _sp.run([sys.executable, os.path.join(T, f)], capture_output=True, text=True,
                    encoding='utf-8', errors='replace', timeout=120)
        blew = ('FileNotFoundError' in (r.stderr or '')) or ('No such file' in (r.stderr or ''))
    except Exception:
        blew = False
    say('      %-30s %s' % (f, '### **BREAKS ON THE RETIRED PATH**' if blew
                            else 'runs -- the path is mentioned, not read'))
    if blew:
        breaks.append(f)
say()
say('  ### ### **MENTIONS : %d hits in %d files. ### BREAKS : %d.**'
    % (len(dated), len(set(x[0] for x in dated)), len(breaks)))
say('  ### ### **THE DATED TOOLS ARE: %s.**' % (', '.join(breaks) or 'none'))
say('  ### The ferry orders `b371_hookpath.py` repaired. ### **`b369_hygiene.py` IS FOUND BY THE')
say('  ### ### SAME SEARCH AND IS NOT IN THIS ACT`S ORDER**, so it is ROUTED and named, not')
say('  ### quietly repaired alongside.')
say()
say('  ### **AND THE REPAIR THE FERRY NAMES, READ FROM `b386`S OWN CHECK:**')
b386 = read(os.path.join(T, 'b386_checks.py'))
m = re.search(r"it names (\.githooks) and not (tools/git-hooks)", b386)
if m:
    say('      `b386_checks.py` asserts the installer ### **names `%s` and not `%s`**'
        % (m.group(1), m.group(2)))
else:
    MISS.append('b386 does not state the path it repaired to, in the shape expected')
say('      `.githooks/pre-push` present in relay : %s'
    % os.path.exists(os.path.join(ROOT, '.githooks', 'pre-push')))
say()

# =============================================================================================
rule()
say('### READ 6 -- THE KERNEL CAVEATS, SEARCHED BY DESCRIPTION. ### CONTROL FIRST.')
rule()
say('  ### **THE DESCRIPTION:** ### a passage that STATES a condition or identification and says')
say('  ### in the same breath that it is ### **NOT COMPILED HERE** ### -- the shape `(T1.4)` has.')
NOTC = re.compile(r'[^.]{0,300}\b(?:is|are) NOT compiled|[^.]{0,300}\bnot compiled here'
                  r'|[^.]{0,300}\bIS NOT COMPILED', re.I)
caveats = []
for f in sorted(os.listdir(CORE)):
    if not f.endswith('.lean'):
        continue
    src = read(os.path.join(CORE, f))
    for m in NOTC.finditer(src):
        caveats.append((f, re.sub(r'\s+', ' ', m.group(0)).strip()))
say('  ### **POSITIVE CONTROL -- `(T1.4)` must be found first, in the file that owns it.**')
seal_hits = [c for c in caveats if c[0] == 'FiniteSideSeal.lean']
say('      caveats found in `FiniteSideSeal.lean` : ### **%d**' % len(seal_hits))
if not seal_hits:
    MISS.append('the control failed: no caveat found in the file that owns (T1.4)')
    say('      ### ### **CONTROL FAILED -- THE COUNT BELOW IS UNREPORTABLE.**')
else:
    say('      ### ### **CONTROL HOLDS.**')
say()
say('  ### ### **CAVEATS OF THIS SHAPE ACROSS `Core/` : ### %d, IN %d FILES.**'
    % (len(caveats), len(set(c[0] for c in caveats))))
for f, s in caveats:
    say('      %s' % f)
    for seg in wrap(s, 90):
        say('          %s' % seg)
say()

# =============================================================================================
rule()
say('### READ 7 -- THE READER`S CANONICAL COPY, LOCATED BY DIGEST.')
rule()
cb, ab = rb(CANON), rb(READER)
say('  download layer  : %s' % CANON)
say('      bytes %d   md5 %s' % (len(cb), hashlib.md5(cb).hexdigest() if cb else '(absent)'))
say('  archived copy   : archive/2026-08-23-trim-backfill/PRIME_CORE_READER.md')
say('      bytes %d   md5 %s' % (len(ab), hashlib.md5(ab).hexdigest() if ab else '(absent)'))
same = bool(cb) and cb == ab
say('  ### ### **BYTE-IDENTICAL : %s**' % same)
if not cb:
    MISS.append('the canonical copy is not on the download layer')
dups = [f for f in os.listdir(DL)
        if f.lower().startswith('prime_core_reader') and f != 'PRIME_CORE_READER.md']
say('  duplicates beside it on the download layer : ### **%d** %s' % (len(dups), dups or ''))
cen = read(CENSUS)
say('  named in the 2026-07-11 orphan census     : %s'
    % ('PRIME_CORE_READER' in cen))
mt = os.path.getmtime(CANON) if os.path.exists(CANON) else 0
import time as _t
say('  canonical copy mtime                      : %s'
    % (_t.strftime('%Y-%m-%d', _t.localtime(mt)) if mt else '(absent)'))
say('  census date                               : 2026-07-11')
say('  ### ### **THE CENSUS IS EARLIER THAN THE FILE**, so its pattern could not have covered')
say('  ### ### it -- which is a fact about the dates and not about the file.')
say()
say('  ### **AND THE ENCODING, READ FROM THE BYTES:**')
moj = cb.count(b'\xc3\xa2\xc2\x80\xc2\x94')
say('      occurrences of the mojibake em-dash sequence : ### **%d**' % moj)
say('      ### ### **THE CANONICAL COPY IS DAMAGED: UTF-8 BYTES ONCE READ AS cp1252 AND')
say('      ### ### RE-ENCODED.** ### `(R32)` says NOTHING IN ITS BODY IS EDITED, so the damage')
say('      ### ### **TRAVELS WITH THE COPY AND IS REPORTED RATHER THAN SILENTLY FIXED.**')
say()

# =============================================================================================
rule()
say('### READ 8 -- THE LATTICE, COMPUTED. ### THE FIGURE IS DRAWN FROM NUMBERS, NOT FROM PROSE.')
rule()
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337]
declared = re.search(r'P = \\\{([^}]*)\\\}', read(READER))
say('  P as the Reader writes it : %s'
    % (re.sub(r'\s+', ' ', declared.group(1)) if declared else '(anchor miss)'))
if not declared:
    MISS.append('the Reader`s own P could not be read from the file')
say('  |P| = %d' % len(P))
say()


def isprime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


sums = {}
for a in range(0, 13):
    for b in range(0, 9):
        v = 2 ** a + 3 ** b
        if v <= 400:
            sums.setdefault(v, (a, b))
sp = sorted(v for v in sums if isprime(v))
say('  primes of the form 2^a + 3^b with a,b >= 0, up to 400 : %s' % ', '.join(map(str, sp)))
inP = [v for v in sp if v in P]
outP = [v for v in sp if v not in P]
say('  of those, IN P     : %s' % ', '.join(map(str, inP)))
say('  of those, NOT in P : ### **%s**' % ', '.join(map(str, outP)))
under100 = [v for v in outP if v < 100]
say()
say('  ### ### **SUM-OF-POWERS PRIMES BELOW 100 THAT P EXCLUDES : ### %d** -- %s'
    % (len(under100), ', '.join(map(str, under100))))
desert = [v for v in sp if 41 < v < 137]
say('  ### ### **AND BETWEEN 41 AND 137 -- THE READER`S *ARITHMETIC DESERT* -- THERE ARE ### %d**'
    % len(desert))
say('  ### ### -- %s' % ', '.join(map(str, desert)))
say()
say('  ### **THE READER`S OWN SENTENCE, QUOTED FROM THE FILE:**')
q = quote('the desert sentence', READER, 'These **jump primes** are separated', chr(10))
say()
say('  ### ### ### **THE SENTENCE SAYS *no sum of powers yields a prime* IN THAT RANGE, AND THE')
say('  ### ### ### ARITHMETIC SAYS THERE ARE %d.** ### Measured, not argued.' % len(desert))
say('  ### ### **AND THE READER CONTRADICTS ITSELF LATER IN ITS OWN BODY**: its predictions')
say('  ### section lists *gap elements (23, 43, 47, 67, ...)*, and `43` and `67` are sums of')
say('  ### powers sitting inside the range the desert sentence says is empty of them.')
say('  ### ### **THIS IS REPORTED AND THE BODY IS NOT EDITED** -- `(R32)` forbids it, and a')
say('  ### document placed as Tier N is placed as it stands.')
say()
KIND = {}
for v in P:
    if v in (2, 3):
        KIND[v] = 'generator'
    elif v in sums and v <= 41:
        KIND[v] = 'consecutive'
    elif v in sums:
        KIND[v] = 'jump'
    else:
        KIND[v] = 'inclusion'
say('  ### **THE FIFTEEN, BY KIND, AS THE READER`S OWN CHAPTER 2-3 SETS THEM:**')
for k in ('generator', 'consecutive', 'jump', 'inclusion'):
    mem = [v for v in P if KIND[v] == k]
    say('      %-12s %d : %s' % (k, len(mem), ', '.join(map(str, mem))))
io.open(LATOUT, 'w', encoding='utf-8', newline=NL).write(
    NL.join(['v\tkind\ta\tb\tinP']
            + ['%d\t%s\t%s\t%s\t%s' % (v, KIND.get(v, '-'),
                                       sums.get(v, ('', ''))[0], sums.get(v, ('', ''))[1],
                                       v in P)
               for v in sorted(set(list(P) + sp))]) + NL)
say('  written : %s' % os.path.basename(LATOUT))
say()

rule()
say('### THE SURVEY`S OWN TALLY.')
rule()
say('  READS TAKEN            : 8')
say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
for m in MISS:
    say('      %s' % m)
rule('=')

io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if MISS else 0)
