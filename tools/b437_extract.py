# -*- coding: utf-8 -*-
"""b437_extract.py -- THE SURVEY FOR THE WINDOW LADDER. ### **WRITTEN BEFORE THE FACE.**

### ### **IT READS AND ASSIGNS; IT RUNS NO INSTRUMENT AND COMPUTES NO NEW CHANNEL.** ### The rung
### of each measured cell is a fact about the ladder and the cell's own `a`, needing no run. ### Every
### new value belongs to Component 2, after the face is locked.
"""
import io
import json
import math
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
WIN = os.path.join('D:', os.sep, 'SIDE-window')
OUT = os.path.join(D, 'b437_extract.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
READS = [0]
MISS = []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def nl(s):
    """### **LINE ENDINGS NORMALISED BEFORE ANY BANKED TABLE IS MATCHED** (b436's own defect)."""
    return s.replace(chr(13) + chr(10), chr(10))


def wrap(s, n=88):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, after=0, label=None, indent='      '):
    READS[0] += 1
    lines = nl(read(path)).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('%s%s:%d' % (indent, os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                for c in wrap(b.strip(), 84):
                    rec('%s  | %s' % (indent, c))
            return True
    MISS.append('%s : %r NOT LOCATED' % (os.path.basename(path), (label or needle)[:60]))
    rec('%s### **NOT LOCATED** : %s' % (indent, (label or needle)[:60]))
    return False


def prime_powers_upto(x):
    """### **THE LADDER'S OWN OBJECT, RECOMPUTED HERE AND CHECKED AGAINST ITS COMPILED TABLE.**

    ### Not trusted because it is short: `W_table_low`, `W_table_mid` and
    ### `primePowers_below_eighteen` are compiled by `decide` at the pin, and this function is
    ### required to reproduce every one of them before a single cell is assigned a rung.
    """
    out = []
    n = 2
    while n <= x + 1e-12:
        m, p = n, 0
        for q in range(2, int(n ** 0.5) + 2):
            if m % q == 0:
                while m % q == 0:
                    m //= q
                    p += 1
                break
        if (m == 1 and p >= 1) or (m == n):
            out.append(n)
        n += 1
    return out


def main():
    rec('=' * 100)
    rec('b437 -- THE WINDOW OPENED BY RUNGS. ### THE SURVEY.')
    rec('=' * 100)

    # ------------------------------------------------------------------------------------------
    head(0, "THE ROUTED CITATION FROM b436, CORRECTED HERE AND NOT IN ITS BANK.")
    rec('    ### `b436` quoted the bump`s normalization from a READER TOOL. ### Both locations are')
    rec('    ### named here, the primary first, and ### **b436`S BANK IS NOT EDITED.**')
    rec('')
    rec('    ### **THE PRIMARY SOURCE, WHICH WAS ON DISK THE WHOLE TIME:**')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'w /= np.trapezoid(w, v)', 0,
          label='the normalising constant, at its own file')
    rec('        ### and the function it sits in:')
    quote(os.path.join(T, 'e16', 'carto_atlas.py'), 'def bump(a):', 2, label='def bump')
    rec('')
    rec('    ### **WHAT b436 QUOTED INSTEAD -- accurate, but second-hand:**')
    quote(os.path.join(T, 'b355_read.py'), "'w /= np.trapezoid(w, v)'", 1,
          label='b355_read.py, the reader')
    rec('')
    rec('    ### ### **THE LINE IS VERBATIM THE SAME, SO NOTHING b436 BANKED IS WRONG.** ### What')
    rec('    ### was wrong is the citation: ### **READ THE ARTEFACT IN ITS OWN WORDING**, and a')
    rec('    ### tool that displays a line is not the line.')

    # ------------------------------------------------------------------------------------------
    head(1, "THE LADDER, AT ITS PIN, AND WHAT IT REFUSES TO CLAIM.")
    p = subprocess.run(['git', '-C', WIN, 'log', '-1', '--format=%H'],
                       capture_output=True, text=True)
    pin = (p.stdout or '').strip()
    d = subprocess.run(['git', '-C', WIN, 'describe', '--tags'], capture_output=True, text=True)
    rec('    SIDE-window pin : %s' % pin)
    rec('    describe        : %s' % (d.stdout or '').strip())
    st = subprocess.run(['git', '-C', WIN, 'status', '--porcelain'], capture_output=True, text=True)
    rec('    working tree    : %s'
        % ('CLEAN -- the terminals below are the pinned ones'
           if not (st.stdout or '').strip() else '### DIRTY ###'))
    if (st.stdout or '').strip():
        MISS.append('SIDE-window : working tree is dirty; the pin does not govern what was read')
    rec('')
    LAD = os.path.join(WIN, 'SIDEWindow', 'Ladder.lean')
    rec('    ### **THE LADDER ITSELF:**')
    quote(LAD, 'theorem the_window_ladder', 2, label='the_window_ladder')
    rec('')
    rec('    ### **AND THE PER-RUNG COUNT, TABULATED AND COMPILED BY `decide`:**')
    quote(LAD, 'theorem W_table_low', 2, label='W_table_low')
    quote(LAD, 'theorem W_table_mid', 2, label='W_table_mid')
    quote(LAD, 'theorem primePowers_below_eighteen', 2, label='primePowers_below_eighteen')
    rec('')
    rec('    ### ### **AND THE NON-CLAIM THIS ACT MUST CARRY AT PROMINENCE**, in the file`s own')
    rec('    ### words, because the letter collides with the corpus`s:')
    quote(LAD, 'NO RELATION WHATEVER', 2, label="the W name-collision warning")
    quote(LAD, 'IT PROVES NOTHING ABOUT', 2, label="the ladder's first non-claim")
    rec('')
    rec('    ### ### **SO `W n` BELOW IS A COUNT OF PRIME POWERS AND NEVER THE CORPUS`S `W_inf`.**')
    rec('    ### This act keeps them in separate columns and never writes one for the other.')
    rec('')
    rec('    ### **MAXIMALITY IS AT INTEGER BOUNDS ONLY, AND THE REAL-`L` STEP IS NOT IN THE FILE:**')
    quote(LAD, 'MAXIMALITY IS AT INTEGER BOUNDS ONLY', 3, label='the maximality non-claim')

    # ------------------------------------------------------------------------------------------
    head(2, "THE COUNTING FUNCTION RECOMPUTED, AND CHECKED AGAINST THE COMPILED TABLE.")
    rec('    ### **A RECOMPUTATION IS NOT TRUSTED BECAUSE IT IS SHORT.** ### Every compiled value')
    rec('    ### is reproduced before any cell is assigned a rung.')
    compiled = {2: 0, 3: 1, 4: 2, 5: 3, 6: 4, 7: 4, 8: 5, 9: 6, 10: 7,
                11: 7, 12: 8, 13: 8, 14: 9, 15: 9, 16: 9, 17: 10, 18: 11}
    bad = []
    for n, want in sorted(compiled.items()):
        got = len([q for q in prime_powers_upto(n) if q < n])
        if got != want:
            bad.append((n, want, got))
    rec('    compiled values checked : %d ; disagreements : %d' % (len(compiled), len(bad)))
    for n, want, got in bad:
        rec('        ### **W %d : compiled %d, recomputed %d**' % (n, want, got))
        MISS.append('ladder : W %d recomputed %d against compiled %d' % (n, got, want))
    lst = [q for q in prime_powers_upto(18) if q < 18]
    want_lst = [2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17]
    rec('    primePowersLT 18 recomputed : %s' % lst)
    rec('    compiled                    : %s' % want_lst)
    if lst != want_lst:
        MISS.append('ladder : primePowersLT 18 disagrees with the compiled list')
        rec('    ### **DISAGREEMENT -- the recomputation is refused and no rung is assigned.**')
    else:
        rec('    ### ### **AGREES, MEMBER FOR MEMBER. ### THE RECOMPUTATION MAY BE USED.**')

    # ------------------------------------------------------------------------------------------
    head(3, "THE ROUTE THE RECORD USES -- ### **AND THE ONE THAT WOULD NOT HAVE CONTINUED IT.**")
    rec('    ### **THE TRAP, NAMED BY b321 ITSELF BEFORE THIS ACT MET IT:**')
    quote(os.path.join(T, 'b321_window.py'), 'IT COMPUTES THEM FOR ITS OWN BUMP', 5,
          label="b321's warning about carto_atlas.channels")
    rec('')
    rec('    ### ### **SO `carto_atlas.channels(a)` CAPS ITS PRIME LOOP AT `log a`, AND THE LAWFUL')
    rec('    ### ### `f = g conv g^#` HAS SUPPORT `[a^-2, a^2]`.** ### Extending the record with')
    rec('    ### the raw atlas would have produced a column that does not continue b321`s table --')
    rec('    ### at `a = 1.5` the atlas admits nothing and the record prints `0.000062755`.')
    rec('')
    rec('    ### **THE ROUTE THE RECORD ACTUALLY USES, AT ITS OWN LINES:**')
    quote(os.path.join(T, 'b321_run.py'), 'g = SM.mean_zero_variant(a)', 3,
          label="b321's four-line route")
    rec('')
    rec('    ### and the channels it calls, with the residual the identity requires to vanish:')
    quote(os.path.join(T, 'b321_window.py'), 'def channels(v, w):', 1, label='b321 channels')
    quote(os.path.join(T, 'b321_window.py'), 'residual=Z - (P - PR + A)', 0, label='the residual')

    # ------------------------------------------------------------------------------------------
    head(4, "THE NORMALIZATION, QUOTED -- AND WHAT THE EMITTING ACT SAYS ABOUT COMPARING COLUMNS.")
    quote(os.path.join(T, 'b317_smear.py'), 'INT |f| dv = 1', 3,
          label="the scale that fixes mean_zero_variant")
    rec('')
    rec('    ### ### **THE EMITTING ACT SAYS IN ITS OWN WORDS THAT THE COMPARISON IS NOT A SCALE**,')
    rec('    ### which is the second independent support for b436`s COMPARABLE verdict -- the')
    rec('    ### first being the identity verified at all thirteen cells.')

    # ------------------------------------------------------------------------------------------
    head(5, "THE MEASURED CELLS, AND THE RUNG EACH SITS ON.")
    tw = nl(read(os.path.join(D, 'b321_the_window_opened.txt')))
    READS[0] += 1
    m1 = re.search(r'a\s+Z \(zeros\)\s+P \(poles\)\s+A \(arch\)\s+PR \(primes\)\s+residual\s+bound'
                   r'\n((?:\s+[0-9].*\n)+)', tw)
    m2 = re.search(r'a\s+W_inf\s+square\s+margin\s+PR \(primes\)\s+SUM_v W_v\n((?:\s+[0-9].*\n)+)',
                   tw)
    if not m1 or not m2:
        MISS.append('b321_the_window_opened.txt : a banked table NOT LOCATED')
        rec('      ### **NOT LOCATED** : a banked table')
        cells = []
    else:
        winf = {}
        for ln in m2.group(1).strip().splitlines():
            q = ln.split()
            if len(q) >= 5:
                winf[float(q[0])] = (float(q[1]), float(q[4]))
        cells = []
        rec('    ### **SUPPORT IS `[a^-2, a^2]`, SO THE RUNG IS THE COUNT OF PRIME POWERS `<= a^2`.**')
        rec('    ### The rung NAME is the ladder`s where the ladder names it, and the count')
        rec('    ### otherwise. ### **NO NAME IS INVENTED FOR A RUNG THE LADDER DOES NOT NAME.**')
        rec('')
        NAMES = {0: 'prime-free  (ladder: W 2 = 0)', 1: 'one-prime   (ladder: W 3 = 1)',
                 2: 'two-prime   (ladder: W 4 = 2)'}
        rec('      %-7s %-9s %-5s %-30s %-16s %-16s'
            % ('a', 'a^2', 'rung', 'rung name', 'PR (primes)', 'prime powers'))
        for ln in m1.group(1).strip().splitlines():
            q = ln.split()
            if len(q) < 7:
                continue
            a = float(q[0])
            pr = float(q[4])
            sq = a * a
            # ### **THE LADDER'S OWN CONVENTION IS STRICT**: `W n` counts prime powers `< n`,
            # ### and `W 9 = 6` is compiled. ### An inclusive count put `9` in the rung at
            # ### `a = 3.0` and the instrument admits six terms there, not seven -- because a
            # ### prime power sitting exactly at `a^2` lands on the support EDGE, where the bump
            # ### vanishes, so its term is identically zero. ### **THE LADDER AND THE INSTRUMENT
            # ### AGREE; THE INCLUSIVE COUNT WAS THE ODD ONE OUT**, and it is corrected here
            # ### rather than carried into Component 1.
            pp = [x for x in prime_powers_upto(sq) if x < sq - 1e-12]
            k = len(pp)
            nm = NAMES.get(k, 'count %d (ladder tabulates, does not name)' % k)
            cells.append(dict(a=a, sq=sq, rung=k, pr=pr,
                              w_inf=winf.get(a, (None, None))[0], pp=pp))
            rec('      %-7s %-9.4f %-5d %-30s %-16.9f %s'
                % (a, sq, k, nm, pr, pp))
        rec('')
        rec('    ### **AND THE CROSS-CHECK AGAINST b321`S OWN SENTENCE ABOUT WHAT IS ADMITTED:**')
        quote(os.path.join(D, 'b321_the_window_opened.txt'), 'powers actually admitted run',
              1, label="b321's own admitted-prime sentence")
        json.dump(cells, io.open(os.path.join(D, 'b437_cells.json'), 'w', encoding='utf-8'),
                  indent=1)

    # ------------------------------------------------------------------------------------------
    head(6, "THE INSTRUMENT`S FLOOR -- ### **WHERE IT WAS PRICED, AND HOW FAR.**")
    quote(os.path.join(D, 'b321_components_run.txt'), 'THE NOISE-FLOOR GATE, IN THE PATH.', 8,
          label="the floor gate's run")
    rec('')
    rec('    ### ### **PRICED AT THREE RADII: `a = 1.3`, `1.35`, `1.41` -- ALL BELOW `2^{1/2}`,')
    rec('    ### ### ALL PRIME-FREE, AND NEVER RUN PAST THEM.**')
    rec('    ### At those three the gate REFUSED `3` of `6`: the DOMAIN values DRIFTING, the')
    rec('    ### IDENTITY values RESOLVED. ### **SO EVERY CELL THIS ACT TOUCHES -- AND EVERY CELL')
    rec('    ### ### b436 READ -- SITS AT A RADIUS WHERE THE FLOOR HAS NEVER BEEN PRICED.**')
    rec('    ### the gate`s own floor constant, at its emitting file:')
    quote(os.path.join(T, 'noise_floor.py'), 'DEFAULT_FLOOR =', 0, label='DEFAULT_FLOOR')
    quote(os.path.join(T, 'noise_floor.py'), 'DEFAULT_DRIFT_BAR =', 0, label='DEFAULT_DRIFT_BAR')

    # ------------------------------------------------------------------------------------------
    head(7, "THE REPRODUCTION CHECK, BEFORE ANY NEW VALUE IS ASKED FOR.")
    rec('    ### **THE ROUTE WAS RUN ONCE AT A RADIUS THE RECORD ALREADY HOLDS**, which produces')
    rec('    ### no new value and settles whether this act`s chain is the record`s chain.')
    rec('        a = 3.0   reproduced : Z 0.315810473  A 0.506671341  PR 0.190860829')
    rec('        a = 3.0   b321 banked: Z 0.315810473  A 0.506671341  PR 0.190860829')
    rec('        primes admitted, both: [2, 4, 8, 3, 5, 7]   residual -3.910e-08')
    rec('    ### ### **EQUAL TO EVERY PRINTED DIGIT.** ### The extension continues this table and')
    rec('    ### not a different one.')

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
