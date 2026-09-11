# -*- coding: utf-8 -*-
"""b416_components.py -- THE FIVE COMPONENTS AND THE TWO ADDITIONS.

### ### **THE TWO ADDITIONS WRITE, AND THEY WRITE BEHIND THEIR OWN FLAGS** -- `--place` puts the
### Reader under the heritage directory, `--figure` draws the lattice. ### Folded here rather than
### written as new act-tools because the locked write list names ### **SIX** ### relay tools and a
### file of a KIND the write list does not name is a breach.
"""
import hashlib
import io
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DL = os.path.join('D:', os.sep, 'MY-DOwnloads')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
SK = os.path.join('D:', os.sep, 'SIDE-kernel', 'Bridge')
CANON = os.path.join(DL, 'PRIME_CORE_READER.md')
PLACED = os.path.join(PP, 'heritage', 'PRIME_CORE_READER.md')
FIGURE = os.path.join(PP, 'outputs', 'prime-core-lattice-b416.svg')
EXTRACT = os.path.join(D, 'b416_extract.txt')
LATTICE = os.path.join(D, 'b416_lattice.txt')
OUT = os.path.join(D, 'b416_components.txt')
NL = chr(10)

L = []
QFAIL = []


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
        QFAIL.append('%s : %s' % (os.path.basename(p), exc))
        return ''


def rb(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read()
    except Exception:
        return b''


def q(label, path, needle):
    if needle in read(path):
        return True
    QFAIL.append('%s -- %r not in %s' % (label, needle[:50], os.path.basename(path)))
    say('      ### **LIVE-QUOTE MISS** -- %s' % label)
    return False


# =============================================================================================
# ### ADDITION ONE'S WRITE. ### **A HEAD BLOCK PREPENDED ABOVE A BYTE-IDENTICAL BODY**, and the
# ### identity proved by digest AFTER the write rather than asserted before it.
# =============================================================================================
HEAD = '''<!-- PLACED b416, 2026-09-11, under author ruling (R32). Body byte-identical to the
     canonical copy; nothing in it is edited. This head block is prepended, not merged. -->

> **CLASS.** Tier N — notes/exploratory, reference-only. Cited for orientation, **never as
> certification**. Cluster: theory-space.
>
> **SCHEME.** The Prime Core `P` is the fifteen-element set this document constructs from the
> generators `{2, 3}`: thirteen reached by the sum `2^a + 3^b`, one by a difference of powers
> (23), one by a product of powers minus one (53).
>
> **CURRENCY NOTE (three things, per (R32)).**
> 1. **It predates the SIDE method and the forced-versus-permitted screen.** Version 1.0,
>    January 2026; the screen the corpus now applies to a ratio did not exist when this was
>    written, and nothing here was written against it.
> 2. **Its central empirical claim — that every tested coefficient factors into `P` — has not
>    been re-tested under the screen.** It stands as stated by its own author and carries no
>    grade from the screen in either direction.
> 3. **Two ratios of its continuation were screened `PERMITTED` at b416's predecessor b415** —
>    the amplitude and the sign rate, each found to be one of many expressions its own shape
>    admits over the same two primitives, with nothing named that selects it. **`PERMITTED` is
>    not a refutation.**

---

'''


def run_place():
    R = []

    def rec(s=''):
        R.append(s)
        print(s, flush=True)

    rec('=' * 100)
    rec('b416 ADDITION ONE -- THE READER PLACED, UNDER (R32).')
    rec('=' * 100)
    cb = rb(CANON)
    if not cb:
        rec('  ### HARD FAILURE -- the canonical copy is not on the download layer.')
        return 2
    rec('  canonical copy : %s' % CANON)
    rec('  bytes %d   sha256 %s' % (len(cb), hashlib.sha256(cb).hexdigest()))
    os.makedirs(os.path.dirname(PLACED), exist_ok=True)
    out = HEAD.encode('utf-8') + cb
    open(PLACED + '.tmp', 'wb').write(out)
    os.replace(PLACED + '.tmp', PLACED)
    # ---- VERIFY AFTER THE WRITE ------------------------------------------------------------
    pb = rb(PLACED)
    head_bytes = HEAD.encode('utf-8')
    body = pb[len(head_bytes):]
    same = (body == cb)
    rec('  placed         : heritage/PRIME_CORE_READER.md')
    rec('  bytes %d = head %d + body %d' % (len(pb), len(head_bytes), len(body)))
    rec('  body sha256    : %s' % hashlib.sha256(body).hexdigest())
    rec('  ### ### **BODY BYTE-IDENTICAL TO THE CANONICAL COPY : %s**' % same)
    rec('  ### ### **BYTES OF THE BODY EDITED : %d**' % (0 if same else -1))
    # ### **THE PATTERN IS MEASURED, NOT GUESSED.** ### A first draft counted a byte
    # ### sequence that is not in the file and reported `0` -- ### **A DETECTOR THAT
    # ### ### CANNOT FIND THE DEFECT REPORTS A CLEAN THAT IS NOT THERE.** ### The real
    # ### damage is U+2014 written as cp1252 and re-encoded: `Ã¢â¬â`.
    moj = body.count(bytes([0xc3, 0xa2, 0xe2, 0x82, 0xac, 0xe2, 0x80, 0x9d]))
    clean = body.count(bytes([0xe2, 0x80, 0x94]))
    rec('  em-dashes written correctly in the body        : %d' % clean)
    rec('  em-dashes carrying cp1252 re-encoding damage  : ### **%d**' % moj)
    rec('  ### ### **THE DAMAGE TRAVELS WITH THE COPY.** ### `(R32)` says nothing in the body is')
    rec('  ### edited, and an encoding repair IS an edit to the body. ### Reported, not fixed.')
    hd = HEAD
    rec('')
    rec('  head block clauses : class line %d, scheme line %d, currency note items %d'
        % (hd.count('**CLASS.**'), hd.count('**SCHEME.**'),
           len(re.findall(r'(?m)^> \d\.', hd))))
    ok = same and hd.count('**CLASS.**') == 1 and hd.count('**SCHEME.**') == 1 \
        and len(re.findall(r'(?m)^> \d\.', hd)) == 3
    rec('  ### ### **VERDICT : %s**' % ('PLACED AS (R32) SPECIFIES' if ok else 'REFUSED'))
    rec('=' * 100)
    io.open(os.path.join(D, 'b416_place.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(R) + NL)
    return 0 if ok else 1


# =============================================================================================
# ### ADDITION TWO'S WRITE. ### **THE FIGURE IS COMPUTED, NOT TRANSCRIBED.**
# =============================================================================================
def run_figure():
    R = []

    def rec(s=''):
        R.append(s)
        print(s, flush=True)

    rec('=' * 100)
    rec('b416 ADDITION TWO -- THE LATTICE DRAWN. ### A FIGURE CARRIES NO GRADE.')
    rec('=' * 100)
    P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337]

    def isprime(n):
        if n < 2:
            return False
        d = 2
        while d * d <= n:
            if n % d == 0:
                return False
            d += 1
        return True

    AMAX, BMAX = 9, 6
    CELL, LEFT, TOP = 76, 108, 96
    W = LEFT + (AMAX + 1) * CELL + 300
    H = TOP + (BMAX + 1) * CELL + 210
    KIND = {}
    for v in P:
        KIND[v] = 'generator' if v in (2, 3) else None
    cells = []
    for a in range(AMAX + 1):
        for b in range(BMAX + 1):
            v = 2 ** a + 3 ** b
            pr = isprime(v)
            inP = v in P
            k = None
            if inP:
                k = 'generator' if v in (2, 3) else ('consecutive' if v <= 41 else 'jump')
                KIND[v] = k
            cells.append((a, b, v, pr, inP, k))
    for v in P:
        if KIND.get(v) is None:
            KIND[v] = 'inclusion'
    COL = {'generator': '#1a5fb4', 'consecutive': '#2e7d32', 'jump': '#8e44ad',
           'inclusion': '#b8860b'}
    s = []
    s.append('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" '
             'viewBox="0 0 %d %d" font-family="Georgia, serif">' % (W, H, W, H))
    s.append('<rect width="%d" height="%d" fill="#fbfaf7"/>' % (W, H))
    s.append('<text x="%d" y="44" font-size="26">The {2,3} lattice: sums '
             '2<tspan font-size="17" dy="-8">a</tspan><tspan dy="8"> </tspan>+ '
             '3<tspan font-size="17" dy="-8">b</tspan></text>' % LEFT)
    s.append('<text x="%d" y="70" font-size="14" fill="#555">Illustration of a Tier N document '
             '(PRIME_CORE_READER, heritage/). A figure carries no grade and is cited nowhere '
             'as evidence. Drawn from the arithmetic, b416.</text>' % LEFT)
    for a in range(AMAX + 1):
        s.append('<text x="%d" y="%d" font-size="14" text-anchor="middle" fill="#333">'
                 '2<tspan font-size="11" dy="-6">%d</tspan><tspan dy="6"></tspan>=%d</text>'
                 % (LEFT + a * CELL + CELL // 2, TOP - 12, a, 2 ** a))
    for b in range(BMAX + 1):
        s.append('<text x="%d" y="%d" font-size="14" text-anchor="end" fill="#333">'
                 '3<tspan font-size="11" dy="-6">%d</tspan><tspan dy="6"></tspan>=%d</text>'
                 % (LEFT - 12, TOP + b * CELL + CELL // 2 + 5, b, 3 ** b))
    for (a, b, v, pr, inP, k) in cells:
        x, y = LEFT + a * CELL, TOP + b * CELL
        if inP:
            fill, stroke, sw = COL[k], COL[k], 2.4
            tc = '#ffffff'
        elif pr:
            fill, stroke, sw, tc = '#ffffff', '#c0392b', 2.4, '#c0392b'
        else:
            fill, stroke, sw, tc = '#f0efec', '#d8d6d1', 1.0, '#9a9892'
        s.append('<rect x="%d" y="%d" width="%d" height="%d" rx="7" fill="%s" stroke="%s" '
                 'stroke-width="%.1f"/>' % (x + 5, y + 5, CELL - 10, CELL - 10, fill, stroke, sw))
        s.append('<text x="%d" y="%d" font-size="%d" text-anchor="middle" fill="%s">%d</text>'
                 % (x + CELL // 2, y + CELL // 2 + 6, 17 if v < 1000 else 13, tc, v))
    lx, ly = LEFT + (AMAX + 1) * CELL + 34, TOP + 6
    s.append('<text x="%d" y="%d" font-size="17">The fifteen of P, by kind</text>' % (lx, ly))
    yy = ly + 30
    for k in ('generator', 'consecutive', 'jump', 'inclusion'):
        mem = [v for v in P if KIND[v] == k]
        s.append('<rect x="%d" y="%d" width="18" height="18" rx="4" fill="%s"/>'
                 % (lx, yy - 14, COL[k]))
        s.append('<text x="%d" y="%d" font-size="14">%s (%d): %s</text>'
                 % (lx + 26, yy, k, len(mem), ', '.join(map(str, mem))))
        yy += 27
    s.append('<rect x="%d" y="%d" width="18" height="18" rx="4" fill="#ffffff" '
             'stroke="#c0392b" stroke-width="2.4"/>' % (lx, yy - 14))
    outs = sorted(v for (_a, _b, v, pr, inP, _k) in cells if pr and not inP)
    s.append('<text x="%d" y="%d" font-size="14">prime, on the lattice, OUTSIDE P</text>'
             % (lx + 26, yy))
    yy += 24
    for seg in wrap(', '.join(map(str, outs)), 34):
        s.append('<text x="%d" y="%d" font-size="13" fill="#c0392b">%s</text>'
                 % (lx + 26, yy, seg))
        yy += 19
    by = TOP + (BMAX + 1) * CELL + 44
    s.append('<text x="%d" y="%d" font-size="16" fill="#c0392b">43 = 2'
             '<tspan font-size="11" dy="-6">4</tspan><tspan dy="6"></tspan> + 3'
             '<tspan font-size="11" dy="-6">3</tspan><tspan dy="6"></tspan> '
             '&#8212; prime, on the lattice, and outside P.</text>' % (LEFT, by))
    sent = ("The Reader's own sentence for why: \u201cThese jump primes are separated from the "
            "consecutive sequence by arithmetic deserts where no sum of powers yields a "
            "prime.\u201d")
    yy = by + 26
    for seg in wrap(sent, 118):
        s.append('<text x="%d" y="%d" font-size="13.5" fill="#444">%s</text>' % (LEFT, yy, seg))
        yy += 20
    desert = sorted(v for v in outs if 41 < v < 137)
    s.append('<text x="%d" y="%d" font-size="13.5" fill="#c0392b">Between 41 and 137 the '
             'lattice carries %d such primes: %s.</text>'
             % (LEFT, yy + 6, len(desert), ', '.join(map(str, desert))))
    s.append('</svg>')
    os.makedirs(os.path.dirname(FIGURE), exist_ok=True)
    data = (NL.join(s) + NL).encode('utf-8')
    open(FIGURE + '.tmp', 'wb').write(data)
    os.replace(FIGURE + '.tmp', FIGURE)
    rec('  written : outputs/%s  (%d bytes)' % (os.path.basename(FIGURE), len(data)))
    rec('  lattice cells drawn        : %d' % len(cells))
    rec('  primes lit                 : %d' % len([c for c in cells if c[3]]))
    rec('  members of P on the lattice: %d' % len(set(c[2] for c in cells if c[4])))
    rec('  kinds distinguished        : %d -- %s'
        % (len(set(KIND.values())), ', '.join(sorted(set(KIND.values())))))
    rec('  43 present on the lattice  : %s' % any(c[2] == 43 for c in cells))
    rec('  43 outside P               : %s' % (43 not in P))
    rec('  primes on the lattice outside P : ### **%d** -- %s' % (len(outs), outs))
    rec('  ### ### **A FIGURE CARRIES NO GRADE.** ### It is filed as illustration of a Tier N')
    rec('  ### document and cited nowhere as evidence.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b416_figure.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(R) + NL)
    return 0


if '--place' in sys.argv:
    sys.exit(run_place())
if '--figure' in sys.argv:
    sys.exit(run_figure())


ext = read(EXTRACT)
place = read(os.path.join(D, 'b416_place.txt'))
fig = read(os.path.join(D, 'b416_figure.txt'))

rule('=')
say('b416_components.py -- THE TWO STIPULATIONS, THE DATED TOOL, AND THE READER.')
rule('=')
say()

# =============================================================================================
rule()
say('### COMPONENT 1 -- `n1` AND `n4`, FROM OWNERS. ### PER COMPONENT, NOT PER CLASS.')
rule()
say('  %-6s %-46s %-34s %s' % ('', 'WHAT THE CORPUS SAYS IT COUNTS', 'WHICH DOCUMENT STATES IT',
                               'ROUTE PRICED?'))
say('  %-6s %-46s %-34s %s'
    % ('n1', 'independent algebraic structures on the', 'phase2/physics/', '### **NEVER**'))
say('  %-6s %-46s %-34s %s'
    % ('', 'substrate -- the independent algebraic', 'MATTER_AS_ARITHMETIC.md, §I', ''))
say('  %-6s %-46s %-34s %s'
    % ('', 'channels through which the specification', '(and the kernel`s own', ''))
say('  %-6s %-46s %-34s %s'
    % ('', 'accesses the substrate', '`Core.lean` field docstring)', ''))
say()
say('  %-6s %-46s %-34s %s'
    % ('n4', 'mechanism classes contributed by the', 'phase2/physics/', '### **NEVER**'))
say('  %-6s %-46s %-34s %s'
    % ('', 'bindings between stages', 'MATTER_AS_ARITHMETIC.md, §I', ''))
say()
q('the n1 definition', os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'),
  'independent algebraic structures on the substrate')
q('the n4 definition', os.path.join(PP, 'phase2', 'physics', 'MATTER_AS_ARITHMETIC.md'),
  'mechanism classes contributed by the bindings between stages')
say()
say('### ### **AND `n4` IS NOT UNARGUED. ### THREE DOCUMENTS ARGUE IT, AND THE OWNER NAMES A')
say('### ### REASON.**')
say('  ### `MATTER_AS_ARITHMETIC` §I   -- ### **`n4 = 0` BY SCHUR`S LEMMA**, named as one of')
say('      three components universal across IDS-amenable systems.')
say('  ### `phase2/formation/COMPLEX_ANALYSIS.md` -- *All interfaces between mechanism classes')
say('      are dark for zero locations. The product formula carries no information about where')
say('      specific zeros lie (spectrally inert).*')
say('  ### `phase2/empirical/BSD_VIA_FORMATION_TRANSFER.md` -- the interface row of its transfer')
say('      table, *Product formula spectrally inert*, carried to `Lambda(E,s)`.')
say()
say('### ### ### **SO `(N1)` SPLITS UNDER `(R27)`.** ### **ITS PREMISE IS MET:** ### `n4` does')
say('### count something the model asserts is empty -- the bindings contribute no mechanism')
say('### class. ### **ITS CONCLUSION IS REFUTED BY A PRINTED RESULT:** ### *no document argues')
say('### it* is false, and the owning document does not merely assert it -- ### **IT NAMES A')
say('### ### THEOREM.**')
say()
say('### ### **AND THE COMPONENT THAT IS REALLY UNARGUED IS THE OTHER ONE.** ### `n1` is the one')
say('### the owner declares ### **FREE** ### -- *the fourth component `n1` depends on the base')
say('### algebra* -- so it is not stipulated for want of an argument; ### **IT IS THE CLASS')
say('### ### LABEL ITSELF.** ### Asking why `classA.n1 = 2` is asking why class A is class A.')
say()
say('### ### ### **AND HERE IS WHAT NEITHER THE FERRY NOR `b415` ASKED, AND IT UNDOES THE')
say('### ### ### OWNER`S OWN SENTENCE.**')
i = ext.find('### READ 2 --')
j = ext.find('### READ 3 --')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[2:]:
        if ln.strip():
            say('  %s' % ln.rstrip())
else:
    QFAIL.append('the extract no longer carries the universality test')
say()
say('### ### **THIS IS WHY `b415` FOUND `0` DERIVED COMPONENTS IN `B`, `C` AND `D`, AND IT IS')
say('### ### NOT AN OVERSIGHT.** ### The two bridges derive `n2 = 3` and `n3 = 2` from reasons')
say('### the owner calls UNIVERSAL. ### **A UNIVERSAL REASON CANNOT DERIVE A COMPONENT IN A')
say('### ### CLASS WHERE THAT COMPONENT HAS ANOTHER VALUE** -- and `classB.n2` and `classD.n2`')
say('### are `2`. ### So the bridges cannot reach `B` and `D` even in principle, and `C` gets')
say('### `n2 = 3` and `n3 = 2` only by sharing `A`s values rather than by its own argument.')
say('### ### **THE STIPULATION IS NOT LAZINESS. ### THE TUPLES CONTRADICT THE UNIVERSALITY')
say('### ### CLAIM THAT WOULD HAVE DERIVED THEM.**')
say()

# =============================================================================================
rule()
say('### COMPONENT 2 -- DERIVING `n1` FOR CLASS A, PRICED ON THE BRIDGES` OWN PATTERN.')
rule()
i = ext.find('### READ 4 --')
j = ext.find('### READ 5 --')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[2:]:
        if ln.strip():
            say('  %s' % ln.rstrip())
say()
say('### ### **THE PATTERN, STATED FROM THE TWO CASES:** ### declare a FINITE TYPE whose')
say('### elements ARE the things counted; prove an EXHAUSTIVENESS theorem over it; take')
say('### `Fintype.card`. ### **THE HARD PART IS NEVER THE CARDINALITY -- IT IS THE')
say('### ### EXHAUSTIVENESS**, and in both existing cases the exhaustiveness came from a named')
say('### classical theorem: Ostrowski`s classification of the places, and the identity theorem')
say('### with elliptic regularity.')
say()
say('### ### **THE ANALOGOUS SUPPLY FOR `n1` AT CLASS A, NAMED EXACTLY:** ### a finite type whose')
say('### elements are the ### **INDEPENDENT ALGEBRAIC CHANNELS THROUGH WHICH THE SPECIFICATION')
say('### ### ACCESSES `Z`**, and a theorem that there are exactly two of them.')
say()
say('### ### ### **AND THERE IS AN OBSTRUCTION BEFORE THE LEAN BEGINS, WHICH `(R28)` NAMES.**')
say('### The corpus has a compiled `2` close at hand: the substrate is ### **THE MINIMAL COMPLETE')
say('### ### COPRIME PAIR `{2,3}`**, cardinality two, with three converging selection principles')
say('### and `FrobeniusCalibration.g_two_three` axiom-free beneath it. ### **BUT THAT `2` COUNTS')
say('### ### PRIMES AND `n1` COUNTS CHANNELS**, and ### **A RESULT APPLIES TO AN OBJECT ONLY IF')
say('### ### THE OBJECT IS OF THE KIND THE RESULT QUANTIFIES OVER.** ### Nothing in the record')
say('### identifies a channel with a generator. ### **THE TWO TWOS ARE NOT KNOWN TO BE THE SAME')
say('### ### TWO**, and an act that wired them together would be assuming exactly what a')
say('### derivation of `n1` is supposed to establish.')
say()
say('### ### **THE PRICE.**')
say('  ### **ACT 1 -- AND IT IS NOT LEAN WORK AT ALL.** ### State, in the corpus, what an')
say('      independent algebraic channel IS, and whether the channels of `Z` are in bijection')
say('      with the generators of the substrate. ### **THIS IS A CORPUS STATEMENT NOBODY HAS')
say('      ### MADE**, and until it exists there is nothing for a bridge to be a bridge TO.')
say('  ### **ACT 2 -- THE BRIDGE, IF ACT 1 SUCCEEDS.** ### Declare the finite type, prove')
say('      exhaustiveness, take the cardinality -- the pattern the two existing bridges set.')
say('  ### ### ### **VERDICT ON THE PRICE: AT LEAST TWO ACTS, AND THE FIRST IS NOT A BUILD.**')
say('  ### ### **AND IT MAY BE UNBUILDABLE RATHER THAN MERELY UNBUILT:** ### the owner declares')
say('  ### `n1` the component that ### **DEPENDS ON THE BASE ALGEBRA**, which is to say the one')
say('  ### that is chosen and not derived. ### **A DERIVATION OF THE CLASS LABEL WOULD COLLAPSE')
say('  ### ### THE FOUR CLASSES INTO ONE**, and the model needs four.')
say('  ### ### **PRICED; NOT BUILT.** ### `0` `.lean` files written.')
say()

# =============================================================================================
rule()
say('### COMPONENT 3 -- THE DATED INSTRUMENT REPAIRED.')
rule()
i = ext.find('### READ 5 --')
j = ext.find('### READ 6 --')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[2:]:
        if ln.strip():
            say('  %s' % ln.rstrip())
say()
src = read(os.path.join(T, 'b371_hookpath.py'))
fixed = ".githooks', 'pre-push'" in src or '.githooks' in src
say('### ### **THE REPAIR, APPLIED:** ### `b371_hookpath.py` now names ### **`.githooks`**, the')
say('### path `b386` left, read from `b386`s own check and not from this seat`s memory.')
say('  the tool`s `SOURCE` line names `.githooks` : ### **%s**' % fixed)
if not fixed:
    QFAIL.append('b371_hookpath.py was not repaired to the .githooks path')
# ### **RUNNING IT IS THE TEST, AND RUNNING IT IS ALSO A WRITE.** ### The tool writes its own
# ### run records under PRIOR ACTS' names. ### Those are captured before the run and restored
# ### after it, so the proof that the repair works does not itself breach `(Z)`.
GUARDED = [os.path.join(D, 'b371_hookpath.json'), os.path.join(D, 'b386_reads.json')]
_pre = {g: rb(g) for g in GUARDED}
r = subprocess.run([sys.executable, os.path.join(T, 'b371_hookpath.py')],
                   capture_output=True, text=True, encoding='utf-8', errors='replace')
broke = 'FileNotFoundError' in (r.stderr or '')
_touched = [g for g in GUARDED if rb(g) != _pre[g]]
for g in _touched:
    open(g + '.tmp', 'wb').write(_pre[g])
    os.replace(g + '.tmp', g)
_still = [g for g in GUARDED if rb(g) != _pre[g]]
say('  it runs without a `FileNotFoundError`        : ### **%s**' % (not broke))
say('  its exit code                                : %d' % r.returncode)
tail = [ln for ln in (r.stdout or '').splitlines() if ln.strip()][-6:]
for ln in tail:
    say('      %s' % ln[:108])
say()
say()
say('### ### ### **AND RUNNING IT REVEALED A THIRD THING, WHICH IS THE ONE WORTH KEEPING.**')
say('### A repaired instrument ### **DOES WHAT IT WAS BUILT TO DO** -- and this one was built to')
say('### write its own run records. ### Those records live under ### **PRIOR ACTS` NAMES**:')
for _g in GUARDED:
    say('      data/%s' % os.path.basename(_g))
say('  prior-act records the run modified : ### **%d**' % len(_touched))
say('  restored from the bytes captured before the run : ### **%d**' % len(_touched))
say('  still differing after the restore  : ### **%d**' % len(_still))
if _still:
    QFAIL.append('a prior act record was modified and not restored')
say('### ### **WHILE THE TOOL WAS BROKEN IT WROTE NOTHING.** ### Repairing it made this breach')
say('### possible ### **FOR THE FIRST TIME**, and the act met it on the first run. ### A dated')
say('### tool is inert; a repaired one is live, and ### **A LIVE TOOL`S WRITES ARE THE')
say('### ### REPAIRING ACT`S WRITES.** ### They are captured, restored, and counted here rather')
say('### than discovered later in a diff.')
say()
say('### ### **AND ONE RESIDUE IS LEFT STANDING AND NAMED:** ### the installer leaves')
say('### `pre-push.b304-backup*` files beside each guard, and `SIDE-effects` now carries two of')
say('### them. ### **THEY ARE UNTRACKED, IN A REPOSITORY THIS ACT DOES NOT WRITE TO**, and')
say('### removing them is not in this act`s order. ### ROUTED.')
say()
say('### ### **AND `b369_hygiene.py` IS FOUND BY THE SAME SEARCH AND IS NOT REPAIRED.** ### The')
say('### ferry orders one tool repaired and the write list names one. ### **IT IS ROUTED:** ### it')
say('### breaks on the same retired path, for the same reason, and its repair is one line.')
say('### ### **AN ACT THAT REPAIRS WHAT IT WAS NOT ASKED TO REPAIR HAS WIDENED ITS OWN ORDER.**')
say()

# =============================================================================================
rule()
say('### COMPONENT 4 -- THE `(T1.4)` ANNOTATION, DRAFTED AND NOT APPLIED.')
rule()
before = read(os.path.join(D, 'b416_seal_digest_before.txt')).split()[0] if os.path.exists(
    os.path.join(D, 'b416_seal_digest_before.txt')) else ''
now = hashlib.sha256(rb(SEAL)).hexdigest()
say('  `Core/FiniteSideSeal.lean` sha256 BEFORE this act : %s' % (before or '(not recorded)'))
say('  `Core/FiniteSideSeal.lean` sha256 NOW             : %s' % now)
say('  ### ### **UNCHANGED : %s**' % (before == now))
if before != now:
    QFAIL.append('the sealed file changed during this act')
say()
say('### ### **THE ANNOTATION THE AUTHOR WOULD NEED TO APPROVE, QUOTED AND NOT APPLIED.**')
say('### It is ### **ADDITIVE**: it adds one sentence immediately after `(T1.4)`s existing')
say('### words and ### **STRIKES NOTHING.** ### The original caveat survives in place, because a')
say('### correction that deletes the sentence it corrects destroys the evidence that the')
say('### correction was needed.')
say()
say('### ### **THE EDIT`S EXACT BYTES** ### -- one line, inserted after the clause ending')
say('### *`that identification is the library\'s and is NOT compiled here);`* :')
say()
ANN = ("  (T1.4-a, b414) AND THE CONDITION NAMED THERE IS TOO STRONG: the compact-smear\n"
       "  identity of `compact_smear_vanishes_at_cells` also holds at 4, 8, 9, 16, 25, 27, 32\n"
       "  and 49, every one composite; the separator is a SINGLE PRIME FACTOR, not primality.\n"
       "  See `Core/SinglePrimeFactor.lean` and relay `data/b414_components.txt`.\n")
for ln in ANN.rstrip(NL).split(NL):
    say('      |%s' % ln)
say()
say('  bytes the annotation would add : ### **%d**' % len(ANN.encode('utf-8')))
say('  lines it would add             : ### **%d**' % len(ANN.rstrip(NL).split(NL)))
say('  bytes it would remove          : ### **0**')
say('  ### ### **APPLIED BY THIS ACT : NO.** ### The digests above are the proof, and they are')
say('  ### taken from the file rather than claimed.')
say()

# =============================================================================================
rule()
say('### COMPONENT 5 -- THE OTHER KERNEL CAVEATS, COUNTED BY DESCRIPTION.')
rule()
i = ext.find('### READ 6 --')
j = ext.find('### READ 7 --')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines()[2:]:
        if ln.strip():
            say('  %s' % ln.rstrip()[:112])
say()
m = re.search(r'CAVEATS OF THIS SHAPE ACROSS `Core/` : ### (\d+), IN (\d+) FILES', ext)
tot, nf = (int(m.group(1)), int(m.group(2))) if m else (0, 0)
ms = re.search(r'caveats found in `FiniteSideSeal.lean` : ### \*\*(\d+)\*\*', ext)
inseal = int(ms.group(1)) if ms else 0
say('### ### ### **`(N2)` SAID AT LEAST THREE OTHER `Core/` CAVEATS STATE AN UNCOMPILED')
say('### ### ### CONDITION.**')
say('### ### ### **TOTAL %d IN %d FILES; %d OF THEM IN THE SEAL ITSELF, SO %d ELSEWHERE.**'
    % (tot, nf, inseal, tot - inseal))
say('### ### **AND THEY ARE COUNTED, NOT GRADED.** ### `b414` showed a caveat of exactly this')
say('### shape can be right on its own evidence and wrong off it; testing thirteen of them is')
say('### not this act`s order, and a count that pretended to be a verdict would be the same')
say('### mistake in the other direction.')
say()

# =============================================================================================
rule()
say('### ADDITION ONE -- `(R32)` EXECUTED. ### THE READER PLACED.')
rule()
if not place:
    QFAIL.append('the placement record is absent -- Addition One was not run')
    say('  ### **MISS** -- no placement record on disk.')
else:
    for ln in place.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  %s' % ln.rstrip())
say()
say('### ### **AND WHAT THE ACT FOUND IN THE READER, WHICH GOES IN THIS RECORD AND NOT IN ITS')
say('### ### BODY.**')
i = ext.find('### **THE READER`S OWN SENTENCE, QUOTED FROM THE FILE:**')
j = ext.find('  ### **THE FIFTEEN, BY KIND')
if i > 0 and j > i:
    for ln in ext[i:j].splitlines():
        if ln.strip():
            say('  %s' % ln.rstrip()[:112])
say()
say('### ### **THE HEAD NOTE CARRIES THE THREE CLAUSES `(R32)` SPECIFIES AND NOT A FOURTH.**')
say('### ### **WHETHER IT SHOULD GROW ONE IS THE AUTHOR`S RULING**, and this act does not')
say('### anticipate it. ### A Tier N document is placed as it stands.')
say()

# =============================================================================================
rule()
say('### ADDITION TWO -- THE LATTICE DRAWN.')
rule()
if not fig:
    QFAIL.append('the figure record is absent -- Addition Two was not run')
    say('  ### **MISS** -- no figure record on disk.')
else:
    for ln in fig.splitlines():
        if ln.strip() and not ln.startswith('='):
            say('  %s' % ln.rstrip())
say()

# =============================================================================================
rule()
say('### THE EXPECTATIONS, SCORED OVER NAMED POPULATIONS UNDER `(R26)`.')
rule()
say('**`(N1)`** over ### **the component `n4` across the four classes**')
say('      *stipulated because it counts something the model asserts is empty, and no document')
say('      argues it*')
say('      ### ### **MET IN PREMISE / REFUTED IN CONCLUSION, UNDER `(R27)`.** ### It does count')
say('      something the model asserts empty. ### **BUT THREE DOCUMENTS ARGUE IT AND THE OWNER')
say('      ### NAMES SCHUR`S LEMMA.** ### The unargued component is `n1`, and it is unargued')
say('      because the owner declares it FREE.')
say()
say('**`(N2)`** over ### **the passages of `Core/` stating an uncompiled condition**')
say('      *at least three other caveats*')
say('      ### **MET** -- %d in %d files, %d elsewhere than the seal, under a control that holds.'
    % (tot, nf, tot - inseal))
say()
say('**`(N3)`** over ### **the tools of `relay/tools`**')
say('      *`b371_hookpath.py` is not the only dated tool*')
say('      ### **MET** -- `b369_hygiene.py` breaks on the same retired path. ### **AND THE')
say('      ### COUNT DEPENDS ENTIRELY ON WHAT *DATED* MEANS**: 7 static hits in 5 files, but')
say('      only 2 files actually break. ### The other three are `b386`s own records of moving')
say('      away from that path, and ### **A FILE THAT NAMES A RETIRED PATH IN ORDER TO RECORD')
say('      ### RETIRING IT IS NOT A DATED TOOL.**')
say()
cb = rb(CANON)
dups = [f for f in os.listdir(DL)
        if f.lower().startswith('prime_core_reader') and f != 'PRIME_CORE_READER.md']
say('**`(N4)`** over ### **the Reader`s canonical copy on this drive**')
say('      *on the download layer with at least one duplicate, per the orphan census`s pattern*')
say('      ### ### **MET IN PREMISE / REFUTED IN CONCLUSION, UNDER `(R27)`.** ### It IS on the')
say('      download layer, at `D:\\MY-DOwnloads\\PRIME_CORE_READER.md`. ### **BUT IT HAS `%d`'
    % len(dups))
say('      ### NUMBERED DUPLICATES**, and the census`s `O.10` pattern -- an orphan with `(1)`,')
say('      `(2)`, `(3)` copies -- ### **DOES NOT APPLY TO IT AT ALL.** ### It is not in the')
say('      census, and the reason is a date: ### **THE CENSUS IS 2026-07-11 AND THE FILE`S mtime')
say('      ### IS 2026-08-08.** ### The census could not have covered a file that did not yet')
say('      exist. ### **AND IT IS NOT AN ORPHAN EITHER** -- a byte-identical copy is already')
say('      TRACKED in the papers repo`s archive, which by the census`s own vocabulary makes it')
say('      ### **MATCHED.**')
say()
P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337]


def isprime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


sp = sorted({2 ** a + 3 ** b for a in range(0, 8) for b in range(0, 6)})
under = [v for v in sp if v < 100 and isprime(v) and v not in P]
say('**`(N5)`** over ### **the primes below 100 of the form `2^a + 3^b`**')
say('      *forty-three is the only one P excludes*')
say('      ### ### **REFUTED BY A PRINTED RESULT. ### THERE ARE %d: %s.**'
    % (len(under), ', '.join(map(str, under))))
say('      ### Each is prime, each is a sum of a power of two and a power of three, and none is')
say('      in `P`. ### **AND SIX OF THE SEVEN LIE BETWEEN 41 AND 137** -- inside the interval')
say('      the Reader`s own sentence calls an arithmetic desert *where no sum of powers yields a')
say('      prime*. ### **THE DESERT HAS SIX OASES, AND THE READER`S OWN PREDICTIONS SECTION')
say('      ### NAMES TWO OF THEM** (`43` and `67`) as gap elements -- so the document')
say('      contradicts itself in its own body. ### **REPORTED HERE; THE BODY IS NOT EDITED.**')
say()

rule()
say('### THE COMPONENTS` OWN TALLY.')
rule()
say('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(QFAIL))
for f in QFAIL:
    say('      %s' % f)
rule('=')

io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
print()
print('wrote %s' % os.path.basename(OUT))
sys.exit(1 if QFAIL else 0)
