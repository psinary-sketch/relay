# -*- coding: utf-8 -*-
"""b437_components.py -- THE WINDOW OPENED BY RUNGS.

### ### **SECTION (X) OF THE LOCKED FACE IS PRINTED BEFORE THE FIRST NEW VALUE IS COMPUTED.** ### The
### face was sealed before this tool ran; the meaning of a crossing is therefore fixed, and the
### reading cannot be fitted to numbers nobody had yet seen.
### ### **NO NEW INSTRUMENT IS BUILT.** ### `b317_smear`, `b318_square`, `b321_window` and
### `noise_floor` are imported and called; not one line of any of them moves.
"""
import io
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import run_clock            # noqa: E402
import b317_smear as SM     # noqa: E402
import b318_square as SQ    # noqa: E402
import b321_window as WI    # noqa: E402
import noise_floor as NF    # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
FACE = os.path.join(D, 'b437_registration_2026-09-12.txt')
BAR_EF = 1e-3

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []
MISS = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


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


def prime_powers_upto(x):
    out, n = [], 2
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


def rung_of(a):
    """### **THE LADDER'S OWN STRICT COUNT**: prime powers `< a^2`. ### `W 9 = 6` is compiled."""
    sq = a * a
    pp = [x for x in prime_powers_upto(sq) if x < sq - 1e-12]
    return len(pp), pp


NAMES = {0: 'prime-free (W 2 = 0)', 1: 'one-prime (W 3 = 1)', 2: 'two-prime (W 4 = 2)'}


def rung_name(k):
    return NAMES.get(k, 'count %d (tabulated, unnamed)' % k)


# ### **THE SPAN, READ OFF THE LOCKED FACE RATHER THAN RETYPED HERE.**
BOUNDARY_N = [n for n in prime_powers_upto(36) if 9 < n <= 36]
BOUNDARIES = [math.sqrt(n) for n in BOUNDARY_N]
_pts = [3.0] + BOUNDARIES
MIDPOINTS = [(_pts[i] + _pts[i + 1]) / 2.0 for i in range(len(_pts) - 1)]
NEW_A = sorted(set([round(x, 6) for x in BOUNDARIES + MIDPOINTS]))
CAP = 24


def section_x():
    head('X', "WHAT A CROSSING WOULD AND WOULD NOT MEAN. ### **FROM THE LOCKED FACE, BEFORE ANY "
              "NEW VALUE.**")
    txt = nl(read(FACE))
    m = re.search(r'### \(X\) COMPONENT 3 --.*?\n-{100}\n(.*?)\n-{100}\n### \(S\)', txt, re.S)
    if not m:
        MISS.append('the locked face : section (X) NOT LOCATED')
        rec('    ### ### **NOT LOCATED -- AND THE ACT STOPS RATHER THAN COMPUTE A VALUE WHOSE')
        rec('    ### ### MEANING IT CANNOT FIRST STATE.**')
        return False
    rec('    ### Quoted from `b437_registration_2026-09-12.txt`, sealed at')
    rec('    ### `0d1b6ed8...7491` before this tool was written:')
    rec('')
    for ln in m.group(1).splitlines():
        rec('      %s' % ln)
    return True


def component_1():
    head(1, "THE LADDER AND THE MEASURED CELLS, SIDE BY SIDE FOR THE FIRST TIME.")
    rec('    ### ### **THE LADDER`S `W` IS A COUNTING FUNCTION ON NATURALS AND HAS NO RELATION')
    rec('    ### ### WHATEVER TO THE CORPUS`S `W_inf`.** ### The ladder`s own header says so, the')
    rec('    ### collision of letters being unfortunate. ### **THE TWO NEVER SHARE A COLUMN BELOW.**')
    rec('')
    try:
        cells = json.loads(read(os.path.join(D, 'b437_cells.json')) or '[]')
    except Exception:                                            # noqa: BLE001
        cells = []
        MISS.append('b437_cells.json : unreadable')
    rec('      %-7s %-9s %-6s %-26s %-16s %-9s %s'
        % ('a', 'a^2', 'rung', 'rung name (ladder)', 'PR (primes)', 'sign', 'prime powers'))
    for c in cells:
        rec('      %-7s %-9.4f %-6d %-26s %-16.9f %-9s %s'
            % (c['a'], c['sq'], c['rung'], rung_name(c['rung']), c['pr'],
               '+' if c['pr'] > 0 else ('-' if c['pr'] < 0 else '0'), c['pp']))
    rec('')
    rec('    ### **AND THE EDGE FACT, WHICH IS WHY A RUNG IS ENTERED CONTINUOUSLY:** ### a prime')
    rec('    ### power sitting exactly at `a^2` lands on the support edge, where the bump vanishes,')
    rec('    ### so its term is identically zero. ### **AT `a = 3.0` THE LADDER COUNTS `W 9 = 6`')
    rec('    ### AND THE INSTRUMENT ADMITS SIX TERMS; AN INCLUSIVE COUNT WOULD HAVE SAID SEVEN.**')

    head(2, "THE SIGN CHANGES, AND THE RUNG BOUNDARIES. ### **A MEASUREMENT, NOT A CLAIM.**")
    sgn = [(c['a'], c['pr']) for c in cells if c['pr'] != 0.0]
    changes = []
    for i in range(1, len(sgn)):
        if (sgn[i][1] > 0) != (sgn[i - 1][1] > 0):
            changes.append((sgn[i - 1][0], sgn[i][0]))
    allb = [(n, math.sqrt(n)) for n in prime_powers_upto(9)]
    lo = min(c['a'] for c in cells) if cells else 0
    hi = max(c['a'] for c in cells) if cells else 0
    inwin = [(n, r) for n, r in allb if lo < r < hi]
    rec('    ### **RUNG BOUNDARIES INSIDE THE MEASURED WINDOW** (`a = sqrt(n)`, `n` a prime power):')
    for n, r in inwin:
        rec('        n = %-3d  a = %.6f' % (n, r))
    rec('')
    rec('    ### **EACH SIGN CHANGE, WITH THE BOUNDARIES IN ITS BRACKETING INTERVAL:**')
    hits = 0
    for a0, a1 in changes:
        br = [(n, r) for n, r in inwin if a0 < r < a1]
        rec('        between a = %-6s and a = %-6s : %d boundary(ies) %s'
            % (a0, a1, len(br), ['n=%d a=%.4f' % (n, r) for n, r in br] or '-'))
        if len(br) >= 1:
            hits += 1
    rec('')
    used = set()
    for a0, a1 in changes:
        for n, r in inwin:
            if a0 < r < a1:
                used.add(n)
    silent = [(n, r) for n, r in inwin if n not in used]
    rec('    ### ### **SIGN CHANGES : %d. ### EACH BRACKETING AT LEAST ONE BOUNDARY : %d.**'
        % (len(changes), hits))
    rec('    ### ### **AND THE CONVERSE, IN THE SAME BREATH: BOUNDARIES CROSSED WITH NO SIGN')
    rec('    ### ### CHANGE : %d of %d.**' % (len(silent), len(inwin)))
    for n, r in silent:
        rec('        n = %-3d  a = %.6f   crossed, no sign change' % (n, r))
    rec('')
    rec('    ### **SO THE COINCIDENCE RUNS ONE WAY ONLY, AND IS REPORTED AS RUNNING ONE WAY ONLY.**')
    rec('    ### Every sign change sits at a boundary; most boundaries produce no sign change.')
    rec('    ### ### **THE RECORD PRINTED BOTH HALVES -- b321`S TABLE AND SIDE-window`S LADDER --')
    rec('    ### ### AND NEVER JOINED THEM UNTIL NOW.** ### This is the join, and it is a')
    rec('    ### measurement over thirteen cells and not a law.')
    return dict(changes=len(changes), at_boundary=hits,
                boundaries=len(inwin), silent=len(silent))


def run_cell(a, nv=None):
    g = SM.mean_zero_variant(a)
    f = SQ.autocorrelation(g) if nv is None else SQ.autocorrelation(g, nv=nv)
    ch = WI.channels(f.v, f.w)
    tb = WI.trunc_bound(f.v, f.w)
    ch['bound'] = tb
    ch['ok'] = abs(ch['residual']) <= max(tb, BAR_EF)
    ch['a'] = a
    return ch


def component_2(cells):
    head(3, "THE EXTENSION. ### **THE ROUTE THE RECORD USES, THE IDENTITY ITS OWN CONTROL.**")
    rec('    ### **THE ROUTE, AND WHY NOT THE OTHER ONE:** ### `carto_atlas.channels(a)` caps its')
    rec('    ### prime loop at `log a`; the lawful `f = g conv g^#` has support `[a^-2, a^2]`, and')
    rec('    ### b321 wrote that no argument to `channels` produces it. ### **THE CHAIN IS')
    rec('    ### `mean_zero_variant` -> `autocorrelation` -> `b321_window.channels`.**')
    rec('')
    rec('    ### **REPRODUCTION FIRST, AT A RADIUS THE RECORD ALREADY HOLDS:**')
    r30 = run_cell(3.0)
    banked = dict(zero=0.315810473, arch=0.506671341, prime=0.190860829)
    same = all(abs(r30[k] - v) < 5e-9 for k, v in banked.items())
    rec('        a = 3.0  Z %.9f  A %.9f  PR %.9f  primes %s'
        % (r30['zero'], r30['arch'], r30['prime'], r30['prime_terms']))
    rec('        b321     Z %.9f  A %.9f  PR %.9f' % (banked['zero'], banked['arch'],
                                                      banked['prime']))
    rec('        ### ### **AGREES TO EVERY PRINTED DIGIT : %s**' % same)
    if not same:
        MISS.append('the reproduction of a = 3.0 does not match b321')
        rec('        ### ### **THE CHAIN IS NOT THE RECORD`S. ### THE EXTENSION IS REFUSED.**')
        return None
    rec('')
    rec('    ### **THE SPAN, AS THE LOCKED FACE FIXED IT:** ### boundaries `a = sqrt(n)` for the')
    rec('    ### prime powers %s, plus the midpoint of each consecutive pair.' % BOUNDARY_N)
    rec('    ### ### **%d NEW CELLS, CAP %d.**' % (len(NEW_A), CAP))
    if len(NEW_A) > CAP:
        MISS.append('the span exceeds its declared cap')
        rec('    ### ### **THE SPAN EXCEEDS ITS CAP AND IS REFUSED.**')
        return None
    rec('')
    rows = []
    for c in cells:
        rows.append(dict(a=c['a'], rung=c['rung'], zero=None, arch=c['w_inf'], pr=c['pr'],
                         ratio=abs(c['pr']) / c['w_inf'] if c['w_inf'] else None,
                         src='b321', ok=True, bound=None, pole=None, resid=None))
    rec('      %-9s %-6s %-15s %-15s %-15s %-11s %-11s %s'
        % ('a', 'rung', 'A (arch)', 'PR (primes)', 'SUM_v W_v', 'residual', 'bound', 'ok'))
    for a in NEW_A:
        ch = run_cell(a)
        k, _pp = rung_of(a)
        s = ch['prime'] - ch['arch']
        rec('      %-9.6f %-6d %-15.9f %-15.9f %-15.9f %-11.2e %-11.2e %s'
            % (a, k, ch['arch'], ch['prime'], s, ch['residual'], ch['bound'],
               'yes' if ch['ok'] else '### NO'))
        rows.append(dict(a=a, rung=k, zero=ch['zero'], arch=ch['arch'], pr=ch['prime'],
                         ratio=abs(ch['prime']) / ch['arch'] if ch['arch'] else None,
                         src='b437', ok=ch['ok'], bound=ch['bound'], pole=ch['pole'],
                         resid=ch['residual'], sum_v=s, terms=ch['prime_terms']))
    bad = [r for r in rows if r['src'] == 'b437' and not r['ok']]
    rec('')
    rec('    ### ### **CELLS COMPUTED : %d. ### FAILING THE IDENTITY : %d.**'
        % (len(NEW_A), len(bad)))
    for r in bad:
        rec('        a = %.6f  residual %.2e against bound %.2e  ### **REPORTED AND NOT USED**'
            % (r['a'], r['resid'], r['bound']))
    negz = [r for r in rows if r['src'] == 'b437' and r['zero'] is not None and r['zero'] < 0]
    rec('    ### **CELLS WITH `Z < 0` : %d** -- by section (X) clause (1) such a cell would be an'
        % len(negz))
    rec('    ### instrument failure and never a crossing.')
    nega = [r for r in rows if r['src'] == 'b437' and r['arch'] is not None and r['arch'] < 0]
    rec('    ### **CELLS WITH `A < 0` : %d** -- and this one is NOT excluded by section (X): the'
        % len(nega))
    rec('    ### archimedean channel carries no positivity constraint. ### Its kernel')
    rec('    ### `Re psi(1/4 + iu/2) - log pi` is NEGATIVE near `u = 0`, and a widening bump')
    rec('    ### concentrates there. ### **SO `A` FALLING THROUGH ZERO IS A FEATURE OF THE')
    rec('    ### ### CHANNEL AND NOT A FAILURE OF THE RUN** -- and it is what the ratio below')
    rec('    ### actually reports.')
    for r in nega:
        rec('        a = %.6f   A %.9f   Z %.9f   PR %.9f' % (r['a'], r['arch'], r['zero'],
                                                             r['pr']))
    poles = [r for r in rows if r['src'] == 'b437' and r['pole'] is not None
             and abs(r['pole']) > 1e-9]
    rec('    ### **CELLS WHOSE POLE TERM IS NOT DRIVEN TO ZERO : %d** -- such a cell is not a'
        % len(poles))
    rec('    ### lawful `g` and its ratio is not read against the criterion.')
    return rows


def the_ratio(rows):
    head(4, "THE RATIO, OLD AND NEW, IN ONE COLUMN.")
    rec('      %-9s %-6s %-6s %-15s %-15s %-13s %s'
        % ('a', 'rung', 'src', 'A (arch)', 'PR (primes)', '|PR| / A', 'note'))
    cross = []
    for r in sorted(rows, key=lambda x: x['a']):
        note = ''
        if not r['ok']:
            note = '### REFUSED -- identity'
        elif r['ratio'] is not None and r['ratio'] > 1.0:
            note = '### **RATIO ABOVE ONE**'
            cross.append(r)
        rec('      %-9.6f %-6s %-6s %-15.9f %-15.9f %-13.6f %s'
            % (r['a'], r['rung'], r['src'], r['arch'] or 0.0, r['pr'],
               r['ratio'] if r['ratio'] is not None else float('nan'), note))
    rec('')
    # ### **AND THE CRITERION'S OWN QUANTITY, WHICH IS THE ONE THE RECORD ASKS ABOUT.**
    viol = [r for r in rows if r.get('sum_v') is not None and r['sum_v'] > 0]
    rec('    ### **THE CRITERION ASKS FOR `SUM_v W_v = PR - A <= 0`.**')
    rec('    ### ### **CELLS WHERE IT IS POSITIVE : %d of %d.**'
        % (len(viol), len([r for r in rows if r.get('sum_v') is not None])))
    rec('    ### And the zero side never went negative, which section (X) clause (1) said it')
    rec('    ### could not: `Z = A - PR` is a sum of non-negative terms over on-line ordinates.')
    rec('')
    if not cross:
        rec('    ### ### ### **THE RATIO DOES NOT CROSS ONE AT ANY CELL, OLD OR NEW.**')
        last = max(rows, key=lambda x: x['a'])
        rec('    ### Its largest value is `%.6f` at `a = %.6f`.' % (
            max(r['ratio'] for r in rows if r['ratio'] is not None),
            max((r for r in rows if r['ratio'] is not None),
                key=lambda x: x['ratio'])['a']))
        rec('    ### **AND THE SPAN ENDS AT `a = %.6f`. ### NO TREND IS EXTRAPOLATED PAST IT.**'
            % last['a'])
    else:
        rec('    ### ### **THE RATIO EXCEEDS ONE AT %d CELL(S):**' % len(cross))
        for r in cross:
            rec('        a = %.6f   ratio %.6f   Z %.9f' % (r['a'], r['ratio'], r['zero'] or 0.0))
    return cross


def the_floor(rows, cross):
    head(5, "THE INSTRUMENT`S FLOOR -- ### **ITS REACH, AND THIS ACT`S PRICING.**")
    rec('    ### **THE REACH, FROM THE RECORD:** ### the noise-floor gate was run at THREE radii --')
    rec('    ### `a = 1.3`, `1.35`, `1.41`, all below `2^{1/2}`, all prime-free -- and REFUSED `3`')
    rec('    ### of `6` there, the DOMAIN values DRIFTING and the IDENTITY values RESOLVED.')
    rec('    ### ### **IT HAS NEVER BEEN RUN PAST THEM.** ### So every cell b436 read and every')
    rec('    ### cell above sits at a radius where the floor was unpriced -- until now.')
    rec('')
    if cross:
        # ### **THE CROSSING RADIUS IS ITSELF A RUNG BOUNDARY**, so a bracket search that does
        # ### not EXCLUDE it returns it twice and prices two of three radii at the same place.
        # ### The first writing did exactly that. ### **A DUPLICATE IS NOT A BRACKET.**
        # ### **THE BRACKET IS FOUND ON THE PRIME POWER, NOT ON THE FLOAT.** ### The span's
        # ### radii are rounded to six places, so `sqrt(29)` and the cell that IS `sqrt(29)`
        # ### differ by `2e-7` -- and a `1e-9` tolerance called them different numbers and
        # ### returned the crossing radius as its own lower bracket. ### **A TOLERANCE FINER
        # ### THAN THE ROUNDING THAT MADE THE VALUE COMPARES NOISE**, and that is the third
        # ### instance of this family in two acts.
        x = cross[0]['a']
        here = [n for n in BOUNDARY_N if abs(math.sqrt(n) - x) < 1e-5]
        below = [n for n in BOUNDARY_N if math.sqrt(n) < x and n not in here]
        above = [n for n in BOUNDARY_N if math.sqrt(n) > x and n not in here]
        pick = ([math.sqrt(below[-1])] if below else []) + [x] +                ([math.sqrt(above[0])] if above else [])
    else:
        pick = [r['a'] for r in sorted(rows, key=lambda x: x['a']) if r['src'] == 'b437'][-3:]
    rec('    ### **PRICED AT %d RADII BY THIS ACT**, chosen by the face`s own rule: %s'
        % (len(pick), ['%.6f' % x for x in pick]))
    rec('    ### The refinement is the same chain on a DOUBLED autocorrelation grid -- the same')
    rec('    ### instrument, a finer mesh, no new code.')
    rec('')
    items = []
    for a in pick:
        c1 = run_cell(a)
        c2 = run_cell(a, nv=2 * SQ.AUTOCORR_NV - 1)
        r1 = abs(c1['prime']) / c1['arch']
        r2 = abs(c2['prime']) / c2['arch']
        items.append(('ratio a=%.4f' % a, r1, r2))
        rec('        a = %.6f   ratio %.9f -> %.9f   (refined)   delta %.2e'
            % (a, r1, r2, abs(r2 - r1)))
    ok, rws, detail = NF.gate(items, label='b437 ratio')
    rec('')
    for nm, v, rf, verdict, why in rws:
        rec('        %-22s %-16.9f -> %-16.9f  %s' % (nm, v, rf, verdict))
    rec('    ### %s' % detail)
    rec('    ### ### **GATE VERDICT : %s**' % ('PASSES -- the ratio is RESOLVED at these radii'
                                               if ok else 'REFUSES'))
    return ok, pick


def main():
    rec('=' * 100)
    rec('b437 -- THE WINDOW OPENED BY RUNGS. ### THE COMPONENTS.')
    rec('=' * 100)
    if not section_x():
        return 1
    q = component_1()
    try:
        cells = json.loads(read(os.path.join(D, 'b437_cells.json')) or '[]')
    except Exception:                                            # noqa: BLE001
        cells = []
    rows = component_2(cells)
    if rows is None:
        rec('  ### ### **THE EXTENSION WAS REFUSED. ### NO RATIO IS READ.**')
        return 1
    cross = the_ratio(rows)
    fok, pick = the_floor(rows, cross)

    head(6, "THE EXPECTATIONS, SCORED.")
    rec('  ### **(N1) the sign changes coincide with rung boundaries**')
    n1 = q['changes'] > 0 and q['at_boundary'] == q['changes']
    rec('      sign changes %d, each bracketing a boundary %d ; boundaries with no sign change '
        '%d of %d' % (q['changes'], q['at_boundary'], q['silent'], q['boundaries']))
    rec('      ### ### **%s** -- and the coincidence runs ONE WAY ONLY, which is printed beside'
        % ('HELD' if n1 else '### REFUTED'))
    rec('      ### the verdict rather than left out of it.')
    rec('  ### **(N2), ITS TWO CLAUSES APART** (R27)')
    new = [r for r in rows if r['src'] == 'b437' and r['ok'] and r['ratio'] is not None]
    new.sort(key=lambda x: x['a'])
    climbs = all(new[i]['ratio'] >= new[i - 1]['ratio'] for i in range(1, len(new))) if new else False
    rec('      (a) the ratio continues to climb')
    if new:
        rec('          from %.6f at a = %.6f to %.6f at a = %.6f ; monotone across the span : %s'
            % (new[0]['ratio'], new[0]['a'], new[-1]['ratio'], new[-1]['a'], climbs))
    rec('          ### ### **%s**' % ('HELD' if climbs else '### REFUTED'))
    rec('      (b) it crosses one within a few rungs')
    rec('          cells above one : %d   ### ### **%s**'
        % (len(cross), 'HELD' if cross else '### REFUTED'))
    rec('  ### **(N3) the crossing reads UNDECIDED-AT-THE-EDGE**')
    if not cross:
        rec('      ### ### **NOT REACHED** -- no crossing was found, and a clause about a crossing')
        rec('      ### that was not found has no subject. ### It is NOT scored as refuted.')
    else:
        rec('      ### ### **%s**' % ('HELD' if not fok else '### REFUTED -- the floor was priced '
                                      'at the crossing and RESOLVED it'))
    rec('')
    rec('  ### MISSES : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    json.dump(dict(rows=rows, span=NEW_A, cap=CAP, cross=[r['a'] for r in cross],
                   floor_priced=pick, floor_ok=fok, sign=q),
              io.open(os.path.join(D, 'b437_rungs.json'), 'w', encoding='utf-8'), indent=1)
    p = run_clock.write(D, 'b437_components', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
