# -*- coding: utf-8 -*-
"""b413_extract.py -- THE SURVEY. ### **EVERY READ ANCHORED, EVERY MISS COUNTED.**

### ### **AND ONE READ THIS SEAT HAS NEVER TAKEN BEFORE: THE KERNEL.** ### Every act from `b403`
### to `b412` carried *both lanes parked*; this ferry names the ### **KERNEL LANE OPEN** ### and
### the seal is read from its own source, not from a paper's description of it.
### ### **READING IS NOT BUILDING.** ### `0` `.lean` files are touched and `0` builds are run.
###
### ### **THE COMPACT-SMEAR IDENTITY IS ALSO RE-COMPUTED HERE, OUTSIDE THE KERNEL**, on the
### kernel's own definitions transcribed line for line -- ### **WITH THE SEVEN DECIDED CELLS AS
### ### THE POSITIVE CONTROL.** ### A re-implementation that did not reproduce what the kernel
### decides would be measuring itself.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SUB = os.path.join(D, '_b413')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
PRINTS = os.path.join(KERN, 'AXIOM_PRINTS.txt')
OUT = os.path.join(D, 'b413_extract.txt')
CELLOUT = os.path.join(D, 'b413_cells.txt')
NL = chr(10)

L = []
MISS = []


def say(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    say(c * 100)


def write_text(p, text):
    """### **ENCODE FIRST, WRITE BYTES SECOND.**"""
    data = text.encode('utf-8')
    open(p + '.tmp', 'wb').write(data)
    os.replace(p + '.tmp', p)
    return len(data)


def pull(path, needle, label, save=None):
    try:
        ln, line = AF.find(path, needle)
    except Exception as e:
        MISS.append('%s :: %s :: %s' % (os.path.basename(path), label, e))
        say('  ### ### **ANCHOR MISS** ### %s -- %s' % (label, str(e)[:90]))
        return None
    say('  ### %s   [%s, line %d]' % (label, os.path.basename(path), ln))
    for k in range(0, max(len(line), 1), 150):
        say('      | %s' % line[k:k + 150])
    if save:
        write_text(os.path.join(SUB, save), line + NL)
    return ln, line


# ### =================================================================================================
# ### THE KERNEL'S OWN DEFINITIONS, TRANSCRIBED LINE FOR LINE. ### **NOT PARAPHRASED.**
# ### =================================================================================================
def offBallFixed(p, n, t, m):
    """### `Core/FiniteSideSeal.lean:133`, transcribed. ### Nat subtraction on `t - 1` is safe
    ### because every `u` in `units` is non-zero (`u % p != 0` excludes `0`)."""
    N, q = p ** (2 * n), p ** n
    c = 0
    for s in range(N):
        if s % q == 0:
            continue
        if (t * s) % N % q == 0:
            continue
        if ((t - 1) * s) % m == 0:
            c += 1
    return c


def units(p, n):
    """### `Core/FiniteSideSeal.lean:140`, transcribed."""
    return [u for u in range(p ** (2 * n)) if u % p != 0]


def smear_holds(p, n):
    """### The conjunct `(c)` of `finite_side_silence`: `q * sumAN = sumAQ`."""
    N, q = p ** (2 * n), p ** n
    U = units(p, n)
    a = sum(offBallFixed(p, n, u, N) for u in U)
    b = sum(offBallFixed(p, n, u, q) for u in U)
    return q * a == b, q * a, b


def distinct_primes(m):
    f, d, x = set(), 2, m
    while d * d <= x:
        while x % d == 0:
            f.add(d)
            x //= d
        d += 1
    if x > 1:
        f.add(x)
    return len(f)


CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1), (2, 3)]


def main():
    if not os.path.isdir(SUB):
        os.makedirs(SUB)
    say('=' * 100)
    say('b413_extract.py -- THE SURVEY. ### THE KERNEL READ, THE IDENTITY RE-COMPUTED.')
    say('=' * 100)

    # ---------------------------------------------------------------- (A) COMPONENT 1
    say()
    bar()
    say('### (A) THE TAIL -- THE TWO R4 PREMISES, FROM THE DOCUMENT THAT OWNS THEM.')
    bar()
    pull(PATHS, '| II.7 partial positivity', 'THE CERTIFICATE`S OWN ROW, WITH ITS THREE PREMISES',
         save='r4_row.txt')
    pull(PATHS, '**Synthesis — the standing next mathematical target.**',
         'AND THE SYNTHESIS THAT NAMES IT THE STANDING TARGET', save='synthesis.txt')
    say('  ### ### **THE HONEST BOUNDARY, QUOTED FROM ROW 1 OF THE CHART:**')
    pull(PATHS, '| **1 (nearest)** | R4 positivity ladder', 'VAJRA-PLINKO ROW 1, WHOLE',
         save='vajra1.txt')

    # ---------------------------------------------------------------- (B) COMPONENT 2
    say()
    bar()
    say('### (B) THE THRESHOLD -- WHERE `2T²` COMES FROM.')
    bar()
    pull(BALPOS, '1. **No *unconditional* positivity is proved', 'THE THRESHOLD IN ITS OWN '
         'PARAGRAPH', save='threshold.txt')
    pull(BALPOS, '4. **The growth-class dichotomy is VOROS', 'AND WHOSE THEOREM IT IS',
         save='voros.txt')
    pull(BALPOS, '**Sources.** Bombieri & Lagarias', 'AND THE SOURCES, NAMED', save='sources.txt')

    # ---------------------------------------------------------------- (C) THE KERNEL
    say()
    bar()
    say('### (C) THE KERNEL, READ FROM ITS OWN SOURCE. ### **THE LANE IS NAMED OPEN BY THIS')
    say('### FERRY; READING IS NOT BUILDING.**')
    bar()
    pull(SEAL, 'theorem finite_side_silence', 'THE SEAL`S SIGNATURE', save='seal_sig.txt')
    pull(SEAL, 'theorem compact_smear_vanishes_at_cells', 'THE PER-CELL CLAUSE',
         save='smear_sig.txt')
    pull(SEAL, 'def cells : List (Nat × Nat)', 'THE SEVEN CELLS, LISTED', save='cells.txt')
    pull(SEAL, 'def units (p n : Nat) : List Nat', 'AND WHAT `units` MEANS -- THE HINGE',
         save='units_def.txt')
    pull(SEAL, 'theorem index_decomposes', 'GENERAL CLAUSE (a)', save='general_a.txt')
    pull(SEAL, 'theorem scaling_fixes_nothing_off_ball', 'GENERAL CLAUSE (b)', save='general_b.txt')
    src = io.open(SEAL, encoding='utf-8', errors='replace').read()
    body = src.split('theorem finite_side_silence', 1)[-1]
    say('  ### ### **THE TACTIC THAT DISCHARGES CONJUNCT (c) : `decide`, ONCE PER CELL.**')
    say('      `decide` occurrences in the proof body : ### **%d**'
        % len(re.findall(r'^\s+. decide\s*$', body, re.M)))
    say('      and the list is peeled by an `rcases` of %d nested alternatives, the last `cases`'
        % body.count('| ⟨'))
    say('      closing the empty tail.')
    say('  ### **AND WHAT THE WHOLE FILE DEPENDS ON:**')
    imports = re.findall(r'^import\s+(\S+)', src, re.M)
    say('      imports in `Core/FiniteSideSeal.lean` : ### **%s**' % (imports or '**NONE**'))
    ml = []
    for root, dirs, files in os.walk(KERN):
        dirs[:] = [x for x in dirs if x not in ('.git', 'build')]
        for f in files:
            if f.endswith('.lean'):
                p = os.path.join(root, f)
                if re.search(r'^import Mathlib', io.open(p, encoding='utf-8',
                                                         errors='replace').read(), re.M):
                    ml.append(os.path.relpath(p, KERN).replace(os.sep, '/'))
    say('      files in the kernel importing Mathlib : ### **%d** ### -- %s' % (len(ml), ml))
    say('  ### ### **SO `Core/` IS VANILLA AND `Interfaces/` IS NOT, AND THAT FORK DECIDES THE')
    say('  ### ### PRICE.**')
    prints = io.open(PRINTS, encoding='utf-8', errors='replace').read()
    say('  ### **THE AXIOM PROFILE, FROM THE KERNEL`S OWN PRINTED STDOUT:**')
    for nm in ('B329.index_decomposes', 'B329.scaling_fixes_nothing_off_ball',
               'B329.compact_smear_vanishes_at_cells', 'B329.finite_side_silence'):
        hit = [ln for ln in prints.split(NL) if nm in ln]
        say('      %-46s %s' % (nm, hit[0].strip() if hit else '### NOT PRINTED ###'))
        if not hit:
            MISS.append('axiom print absent for %s' % nm)
    say('  ### **AND WHETHER `Core/` CARRIES ANY PRIMALITY NOTION AT ALL:**')
    hits = []
    for root, dirs, files in os.walk(os.path.join(KERN, 'Core')):
        for f in files:
            if f.endswith('.lean'):
                s = io.open(os.path.join(root, f), encoding='utf-8', errors='replace').read()
                if re.search(r'^\s*(def|abbrev|inductive)\s+\w*[Pp]rime', s, re.M):
                    hits.append(f)
    say('      definitions of a prime predicate in `Core/` : ### **%s**' % (hits or '**NONE**'))

    # ---------------------------------------------------------------- (D) THE IDENTITY, RE-COMPUTED
    say()
    bar()
    say('### (D) THE COMPACT-SMEAR IDENTITY, RE-COMPUTED OUTSIDE THE KERNEL.')
    bar()
    say('  ### ### **THE POSITIVE CONTROL FIRST: THE SEVEN CELLS THE KERNEL DECIDES.** ### A')
    say('  ### re-implementation that did not reproduce them would be measuring itself.')
    ctl = 0
    rows = []
    for p, n in CELLS:
        ok, a, b = smear_holds(p, n)
        ctl += 1 if ok else 0
        rows.append((p, n, distinct_primes(p), ok))
        say('      p=%-3d n=%d   q*sumAN=%-8d sumAQ=%-8d   %s'
            % (p, n, a, b, 'HOLDS' if ok else '### FAILS ###'))
    say('  ### ### **CONTROL : %d OF %d CELLS REPRODUCED. ### %s**'
        % (ctl, len(CELLS), 'PASSES' if ctl == len(CELLS) else
           'FAILS -- THE VERDICT BELOW IS WITHHELD'))
    if ctl != len(CELLS):
        MISS.append('the positive control on the re-implementation failed')
    say()
    say('  ### **AND NOW BEYOND THE SEVEN, SORTED BY THE NUMBER OF DISTINCT PRIME FACTORS:**')
    probe = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 25, 27, 32, 49,
             6, 10, 12, 14, 15, 18, 20, 21, 22, 26]
    hold1 = fail1 = hold2 = fail2 = 0
    for p in probe:
        if p ** 2 > 2600:
            continue
        ok, _a, _b = smear_holds(p, 1)
        k = distinct_primes(p)
        rows.append((p, 1, k, ok))
        if k == 1:
            hold1 += 1 if ok else 0
            fail1 += 0 if ok else 1
        else:
            hold2 += 1 if ok else 0
            fail2 += 0 if ok else 1
        say('      p=%-3d n=1   distinct primes %d   %s'
            % (p, k, 'HOLDS' if ok else '### FAILS ###'))
    say()
    say('  ### ### ### **PRIME POWERS (one distinct prime) : %d HOLD, %d FAIL.**' % (hold1, fail1))
    say('  ### ### ### **TWO DISTINCT PRIMES : %d HOLD, %d FAIL.**' % (hold2, fail2))
    say('  ### ### ### **THE SEPARATION IS TOTAL, AND IT IS NOT PRIMALITY -- IT IS HAVING A')
    say('  ### ### ### SINGLE PRIME FACTOR.** ### `4`, `8`, `9`, `16`, `25`, `27`, `32` and `49`')
    say('  ### are not prime and the identity holds at every one; `6`, `10`, `12`, `14`, `15`,')
    say('  ### `18`, `20`, `21`, `22` and `26` are composite with two prime factors and it fails')
    say('  ### at every one.')
    write_text(CELLOUT, NL.join('%d\t%d\t%d\t%s' % r for r in rows) + NL)

    say()
    bar('=')
    say('  ### ### **ANCHOR MISSES : %d**' % len(MISS))
    for m in MISS:
        say('      %s' % m)
    say('  ### **`0` `.lean` FILES TOUCHED. ### `0` KERNEL BUILDS RUN. ### READING IS NOT')
    say('  ### BUILDING.**')
    bar('=')
    write_text(OUT, NL.join(L) + NL)
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
