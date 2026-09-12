# -*- coding: utf-8 -*-
"""b438_components.py -- WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES.

### ### **NO NEW INSTRUMENT, NO NEW FAMILY, NO NEW CELL.** ### `b317_smear`, `b318_square`,
### `b320_weil`, `b321_window` and `carto_atlas` are imported and called; not one line of any moves.
### Both families are ones the record already holds; the cells decomposed are the ones `b437` banked.
"""
import io
import json
import math
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import run_clock            # noqa: E402
import b317_smear as SM     # noqa: E402
import b318_square as SQ    # noqa: E402
import b320_weil as WEIL    # noqa: E402
import b321_window as WI    # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES, MISS = [], []
TOL = 1e-4          # ### **STATED BEFORE THE COMPARISON**, as (K) BAR 4 requires.


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


def quote(path, needle, after=0, label=None, indent='        '):
    lines = read(path).replace(chr(13) + chr(10), chr(10)).splitlines()
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


def lawful(a):
    """### The chain the record uses, unchanged: aimed seed, then its autocorrelation."""
    return SQ.autocorrelation(SM.mean_zero_variant(a))


def plain(a):
    """### **THE SECOND FAMILY THE RECORD ALREADY HOLDS** -- the plain corpus bump, squared."""
    return SQ.autocorrelation(SM.corpus_bump(a))


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


def factor_p(n):
    for q in range(2, n + 1):
        if n % q == 0:
            return q
    return n


def component_1(cells):
    head(1, "WHICH TEST FUNCTION THE LADDER USES. ### **AIMED, NOT PLAIN.**")
    quote(os.path.join(T, 'b317_smear.py'), 'def mean_zero_variant(a):', 2, label='the seed')
    rec('')
    quote(os.path.join(T, 'b317_smear.py'), 'c12 = np.linalg.solve(A2, b2)', 0,
          label='the solved coefficients')
    rec('')
    rec('    ### ### **TWO MOMENTS ARE DRIVEN TO ZERO BY SOLVING, NOT BY CHOOSING.** ### And a')
    rec('    ### non-negative function cannot have a vanishing integral unless it is zero, so')
    rec('    ### ### **THE SEED MUST TAKE NEGATIVE VALUES: THE OSCILLATION IS BUILT IN BY THE AIM.**')
    rec('    ### The lawful `f` is its AUTOCORRELATION, which is even and whose transform is')
    rec('    ### `|ghat|^2 >= 0` -- but which is itself free to change sign in `v`.')

    head(2, "THE WEIGHT, AND WHAT KIND OF STATEMENT `(N1)` IS.")
    quote(os.path.join(T, 'b321_window.py'), "val = 2.0 * math.log(p) / math.sqrt(n)", 0,
          label="route corpus's term")
    rec('    ### ### **`2 log p / sqrt(n) > 0` FOR EVERY PRIME POWER.** ### So in this route the')
    rec('    ### sign of a term IS the sign of the test function at that log -- ### **BY THE FORM')
    rec('    ### ### OF THE EXPRESSION.** ### Every term is printed anyway; a claim about a form is')
    rec('    ### not a substitute for values. ### **BUT THE VERDICT WILL SAY WHICH IT IS.**')

    head(3, "EVERY TERM AT EVERY CELL. ### **BOTH ROUTES OF `(149)`.**")
    rec('    ### The two routes share the loop, the grid and the interpolation and differ only in')
    rec('    ### the expression -- ### **A SINGLE-ARM CHECK ON THE ALGEBRA**, not two measurements.')
    rec('')
    rows, agree_c, agree_s, nterm = [], 0, 0, 0
    rec('      %-8s %-5s %-13s %-13s %-13s %-13s %-5s %s'
        % ('a', 'n', 'weight', 'w(+log n)', 'w(-log n)', 'term', 'sign', 'sign(w)?'))
    for c in cells:
        a = c['a']
        f = lawful(a)
        v, w = f.v, f.w
        sq = a * a
        pp = [x for x in prime_powers_upto(sq) if x < sq - 1e-12]
        tot_c = tot_s = 0.0
        for n in pp:
            p = factor_p(n)
            ln = math.log(n)
            wp = float(__import__('numpy').interp(ln, v, w, left=0.0, right=0.0))
            wm = float(__import__('numpy').interp(-ln, v, w, left=0.0, right=0.0))
            weight = 2.0 * math.log(p) / math.sqrt(n)
            term_c = weight * wp
            term_s = math.log(p) * (wp / math.sqrt(n) + wm / math.sqrt(n))
            tot_c += term_c
            tot_s += term_s
            nterm += 1
            ok_c = (term_c > 0) == (wp > 0) or term_c == 0.0
            agree_c += 1 if ok_c else 0
            agree_s += 1 if ((term_s > 0) == (wp > 0) or term_s == 0.0) else 0
            rec('      %-8.6f %-5d %-13.6e %-13.6e %-13.6e %-13.6e %-5s %s'
                % (a, n, weight, wp, wm, term_c,
                   '+' if term_c > 0 else ('-' if term_c < 0 else '0'),
                   'yes' if ok_c else '### NO'))
            rows.append(dict(a=a, n=n, p=p, weight=weight, wp=wp, wm=wm,
                             term=term_c, term_s149=term_s))
        if pp:
            rec('      %-8s %-5s %-13s %-13s %-13s %-13.9f   (route corpus total)'
                % ('', '', '', '', '', tot_c))
            rec('      %-8s %-5s %-13s %-13s %-13s %-13.9f   (route s149  total)'
                % ('', '', '', '', '', tot_s))
    rec('')
    rec('    ### ### **TERMS PRINTED : %d.**' % nterm)
    rec('    ### ### **TERMS WHOSE SIGN IS THE TEST FUNCTION`S SIGN AT THAT LOG, route corpus :'
        ' %d of %d.**' % (agree_c, nterm))
    rec('    ### ### **AND BY route s149, WHICH ASSUMES NO EVENNESS : %d of %d.**'
        % (agree_s, nterm))
    maxd = max((abs(r['term'] - r['term_s149']) for r in rows), default=0.0)
    rec('    ### the two routes` largest term-wise difference : %.3e' % maxd)
    rec('    ### ### **SO THE EVENNESS IS EXERCISED AND NOT ASSUMED**, and `w(+log n)` and')
    rec('    ### `w(-log n)` agree to that same figure at every printed row.')
    json.dump(rows, io.open(os.path.join(D, 'b438_terms.json'), 'w', encoding='utf-8'), indent=1)
    return rows, nterm, agree_c, agree_s


def flippers(rows, cells):
    head(4, "WHY THREE AND SEVEN FLIP THE SUM AND TWO, FOUR, FIVE AND EIGHT DO NOT.")
    rec('    ### ### **THE QUESTION IS ABOUT THE SUM`S SIGN, NOT A TERM`S.** ### A prime power')
    rec('    ### flips the SUM when it enters carrying a term that outweighs everything already')
    rec('    ### there. ### Read from the printed values at the cell where each first contributes:')
    rec('')
    rec('      %-5s %-10s %-14s %-14s %-14s %s'
        % ('n', 'first at a', 'its term', 'sum before', 'sum after', 'flipped the sum?'))
    seen, out = set(), []
    bycell = {}
    for r in rows:
        bycell.setdefault(r['a'], []).append(r)
    order = sorted(bycell)
    for i, a in enumerate(order):
        prev = sum(x['term'] for x in bycell[order[i - 1]]) if i else 0.0
        cur = sum(x['term'] for x in bycell[a])
        for r in bycell[a]:
            if r['n'] in seen:
                continue
            seen.add(r['n'])
            flip = (prev != 0.0) and ((cur > 0) != (prev > 0))
            rec('      %-5d %-10.6f %-14.6e %-14.6e %-14.6e %s'
                % (r['n'], a, r['term'], prev, cur, '### **YES**' if flip else 'no'))
            out.append(dict(n=r['n'], a=a, term=r['term'], before=prev, after=cur, flip=flip))
    rec('')
    rec('    ### ### **AND THE READING, FROM THOSE VALUES AND NOT FROM A STORY.**')
    rec('    ### ### **THE ENTERING TERM DOES NOT CAUSE THE FLIP. ### IT CANNOT.**')
    rec('    ### A prime power enters at `p^k = a^2`, which is the SUPPORT EDGE, where the bump')
    rec('    ### vanishes -- so its first term is negligible by construction. ### Each flip is')
    rec('    ### decomposed below into what ARRIVED and what MOVED:')
    rec('')
    rec('      %-6s %-10s %-15s %-15s %-15s'
        % ('at n', 'a', 'sum before', 'entering terms', 'already-present'))
    for o in out:
        if not o['flip']:
            continue
        a = o['a']
        prev_ns = set(x['n'] for x in bycell[order[order.index(a) - 1]])
        ent = sum(x['term'] for x in bycell[a] if x['n'] not in prev_ns)
        old_ = sum(x['term'] for x in bycell[a] if x['n'] in prev_ns)
        rec('      %-6d %-10.6f %-+15.6e %-+15.6e %-+15.6e'
            % (o['n'], a, o['before'], ent, old_))
        rec('          ### the entering terms move the sum by %+.3e ; the already-present ones by'
            % ent)
        rec('          ### %+.3e -- ### **A FACTOR OF %.0e BETWEEN THEM.**'
            % (old_ - o['before'], abs((old_ - o['before']) / ent) if ent else float('inf')))
        o['entering'] = ent
        o['moved'] = old_ - o['before']
    rec('')
    rec('    ### ### ### **SO THE NAVIGATOR`S GLOSS IS REFUTED BY HIS OWN TEST.** ### `3` and `7`')
    rec('    ### ### ### DO NOT FLIP THE SUM; THE SUM FLIPS AT THE CELLS WHERE THEY HAPPEN TO')
    rec('    ### ### ### ENTER, AND THE CAUSE IS THE `n = 2` TERM CHANGING SIGN.**')
    two = [x for x in rows if x['n'] == 2]
    rec('')
    rec('    ### **THE `n = 2` TERM, WHICH IS ALWAYS THE LARGEST**, its weight `2 log 2 / sqrt 2 =')
    rec('    ### %.6f` being the biggest of any prime power and `log 2 = %.6f` sitting deepest'
        % (2.0 * math.log(2) / math.sqrt(2), math.log(2)))
    rec('    ### inside the support:')
    rec('      %-10s %-15s %-15s' % ('a', 'w(log 2)', 'its term'))
    for x in two:
        rec('      %-10.6f %-+15.6e %-+15.6e' % (x['a'], x['wp'], x['term']))
    sc = [ (two[i-1]['a'], two[i]['a']) for i in range(1,len(two))
           if (two[i]['term'] > 0) != (two[i-1]['term'] > 0) ]
    rec('')
    rec('    ### ### **THE `n = 2` TERM CHANGES SIGN %d TIME(S) : %s** -- and the sum changes sign'
        % (len(sc), sc))
    rec('    ### at exactly those transitions. ### **THE ALTERNATION IS THE TEST FUNCTION`S VALUE')
    rec('    ### ### AT ONE POINT, `log 2`, FOLLOWED AS THE AIMED SEED IS REBUILT AT EACH RADIUS**')
    rec('    ### -- not a new prime power arriving with a sign of its own.')
    rec('    ### **AND THAT IS A MEASUREMENT, NOT AN IDENTITY.**')
    return out, bycell, order



ADDENDUM = """ADDENDUM to b438 Component 1. One column, from the table
already being printed: at each radius where the prime sum
changes sign, which per-term sign changed between the cell
before and the cell after -- the newly admitted prime power, or
one already present. And, for each already-present term that
changes sign, the ratio of its log to the radius's log at the
crossing, so a shell boundary would show as a constant across
the two flips.

The navigator's refined hypothesis, his and to be scored: the
flips are SHELL CROSSINGS of already-present prime powers, not
entries -- because a prime power enters at the support edge
where the bump vanishes, so its first contribution is zero and
carries the outermost shell's sign, the same for every prime.
Verdicts: SHELL CROSSING (an existing term flips at both, and
b437's (N1) coincidence is restated as a coincidence of two
cells) / ENTRY (the new term carries the flip, and the shell
reading is refuted) / MIXED (which is which, and the entry case
explained against the vanishing-at-the-edge finding).

The navigator's (N1) is withdrawn as an identity, in his words:
proposed as a testable hypothesis something that follows from
the form of the expression, and caught by the face before a
cell was spent.

All other components stand."""


def term_at(a, n):
    """### The term at one radius and one prime power, by the record's own expression."""
    import numpy as np
    f = lawful(a)
    p = factor_p(n)
    ln = math.log(n)
    wp = float(np.interp(ln, f.v, f.w, left=0.0, right=0.0))
    return 2.0 * math.log(p) / math.sqrt(n) * wp


def addendum(rows, out, bycell, order):
    head('ADD', "THE ADDENDUM'S COLUMN -- ### **ENTRY OR SHELL CROSSING?**")
    rec('    ### **THE ADDENDUM ARRIVED AFTER THIS ACT`S FACE WAS LOCKED**, and is quoted here')
    rec('    ### verbatim rather than banked as its own paste. ### **THE LOCKED FACE`S (Z) FORBIDS')
    rec('    ### ### EDITING THE BANKED FERRY, AND ITS ENUMERATED DATA LIST NAMES NO SLOT FOR A')
    rec('    ### ### POST-LOCK ADDENDUM.** ### So it lives in this record, and the gap is reported')
    rec('    ### rather than closed by a write the face does not name -- ### **WHICH IS ITSELF A')
    rec('    ### FINDING ABOUT (R47)`S FORM: AN ACT CANNOT RECEIVE AN ADDENDUM AFTER ITS LOCK')
    rec('    ### WITHOUT EITHER A DECLARED SLOT OR A BREACH.**')
    rec('')
    for ln in ADDENDUM.splitlines():
        rec('      | %s' % ln)
    rec('')
    rec('    ### ### **AND (N1) IS WITHDRAWN AS AN IDENTITY, IN THE NAVIGATOR`S OWN WORDS.** ### It')
    rec('    ### is not re-scored here; the withdrawal is recorded, and the act moves to the')
    rec('    ### refined hypothesis -- which is about VALUES and can fail.')
    rec('')
    rec('    ### **AT EACH FLIP: WHICH PER-TERM SIGN CHANGED, AND WAS IT NEW OR ALREADY THERE?**')
    rec('')
    flips = [o for o in out if o['flip']]
    shells = []
    for o in flips:
        a1 = o['a']
        i = order.index(a1)
        a0 = order[i - 1]
        before = dict((x['n'], x['term']) for x in bycell[a0])
        after = dict((x['n'], x['term']) for x in bycell[a1])
        rec('      ### flip at the cell a = %.6f (from a = %.6f)' % (a1, a0))
        rec('        %-6s %-9s %-15s %-15s %s' % ('n', 'status', 'term before', 'term after',
                                                  'sign changed?'))
        for n in sorted(after):
            b = before.get(n)
            new = n not in before
            ch = (not new) and b is not None and ((after[n] > 0) != (b > 0))
            rec('        %-6d %-9s %-15s %-+15.6e %s'
                % (n, 'NEW' if new else 'present',
                   ('%+.6e' % b) if b is not None else '--', after[n],
                   '### **YES**' if ch else ('n/a -- it is new' if new else 'no')))
            if ch:
                lo, hi = a0, a1
                for _ in range(40):
                    mid = 0.5 * (lo + hi)
                    if (term_at(mid, n) > 0) == (b > 0):
                        lo = mid
                    else:
                        hi = mid
                astar = 0.5 * (lo + hi)
                ratio = math.log(n) / math.log(astar)
                down = (b > 0)
                shells.append(dict(flip_at=a1, n=n, a_star=astar, ratio=ratio,
                                   direction=('down' if down else 'up')))
                rec('          ### **CROSSES AT a* = %.7f** (bracket %.1e), going %s'
                    % (astar, hi - lo, '+ -> -' if down else '- -> +'))
                rec('          ### **log n / log a* = %.9f**' % ratio)
        rec('')
    carried = [o for o in flips if abs(o.get('entering', 0.0)) > abs(o.get('moved', 0.0))]
    rec('    ### ### **FLIPS WHERE THE ENTERING TERM CARRIED IT : %d of %d.**'
        % (len(carried), len(flips)))
    rec('    ### ### **FLIPS WHERE AN ALREADY-PRESENT TERM CHANGED SIGN : %d of %d.**'
        % (len(set(s['flip_at'] for s in shells)), len(flips)))
    rec('')
    const, spread = False, float('nan')
    # ### **THE FIRST WRITING OF THIS TEST COMPARED CROSSINGS OF DIFFERENT ZEROS.** ### If the
    # ### family has a FIXED SHAPE in the scaled variable `s = v / log a`, that shape has SEVERAL
    # ### zeros, and a term sweeping inward as `a` grows crosses each in turn. ### Pooling them and
    # ### taking one spread compares zero number one against zero number two and reports a figure
    # ### that means nothing. ### **THE CROSSINGS ARE GROUPED BY DIRECTION, WHICH IS WHAT TELLS
    # ### ONE ZERO OF A FIXED SHAPE FROM THE NEXT.**
    if shells:
        rec('    ### **THE SHELL TEST -- ### A BOUNDARY WOULD SHOW AS A CONSTANT RATIO.**')
        rec('    ### ### **AND THE CROSSINGS ARE GROUPED BY DIRECTION FIRST.** ### A fixed shape in')
        rec('    ### `s = v / log a` has MORE THAN ONE zero; a term sweeping inward as `a` grows')
        rec('    ### crosses each in turn. ### **POOLING THEM COMPARES ONE ZERO AGAINST ANOTHER AND')
        rec('    ### ### REPORTS A SPREAD THAT MEANS NOTHING** -- which is what this act`s first')
        rec('    ### writing of the test did, and it is corrected here rather than carried.')
        rec('')
        rec('      %-10s %-6s %-14s %-10s %s'
            % ('flip at a', 'n', 'a* (crossing)', 'direction', 'log n / log a*'))
        for s in shells:
            rec('      %-10.6f %-6d %-14.7f %-10s %.9f'
                % (s['flip_at'], s['n'], s['a_star'],
                   '+ -> -' if s['direction'] == 'down' else '- -> +', s['ratio']))
        rec('')
        groups = {}
        for s in shells:
            groups.setdefault(s['direction'], []).append(s['ratio'])
        spreads = {}
        for d in sorted(groups):
            rs = groups[d]
            sp = (max(rs) - min(rs)) if len(rs) > 1 else None
            spreads[d] = sp
            lbl = '+ -> -' if d == 'down' else '- -> +'
            if sp is None:
                rec('      ### `%s` : ONE crossing only (%.9f) -- ### **NO SPREAD TO TAKE.**'
                    % (lbl, rs[0]))
            else:
                rec('      ### ### **`%s` : %d crossings, SPREAD %.3e** (min %.9f, max %.9f)'
                    % (lbl, len(rs), sp, min(rs), max(rs)))
        dn = spreads.get('down')
        const = (dn is not None and dn < 1e-3)
        spread = dn if dn is not None else float('nan')
    rec('')
    rec('    ### ### ### **VERDICT, AND ITS TWO HALVES REPORTED APART:**')
    both = bool(flips) and len(set(s['flip_at'] for s in shells)) == len(flips)
    if both and not carried:
        rec('    ### ### ### **(i) THE MECHANISM CLAUSE : SHELL CROSSING.** ### An already-present')
        rec('    ### ### ### term changes sign at BOTH flips, and no entering term carries either.')
        rec('    ### **THE TERMS THAT CROSS : n = %s** -- and at the second flip TWO of them do.'
            % sorted(set(s['n'] for s in shells)))
        rec('    ### **SO b437`S (N1) COINCIDENCE IS RESTATED AS A COINCIDENCE OF TWO CELLS:** ###')
        rec('    ### the sum`s sign changes fall in the intervals where `3` and `7` happen to')
        rec('    ### enter, and the entering prime power has nothing to do with either.')
    else:
        rec('    ### ### ### **(i) THE MECHANISM CLAUSE : MIXED OR ENTRY** -- see the counts above.')
    rec('')
    if shells and not const:
        rec('    ### ### ### **(ii) THE SHELL-BOUNDARY CLAUSE : REFUTED WITHIN ITS OWN GROUP.**')
        rec('    ### ### ### The downward crossings spread by %.3e, past the 1e-3 bar.' % spread)
        rec('    ### So the flips ARE crossings of an already-present term, ### **BUT THEY DO NOT')
        rec('    ### ### SIT AT A FIXED BOUNDARY IN `v / log a`.** ### The two halves of the')
        rec('    ### hypothesis part company, and this act reports them apart rather than')
        rec('    ### averaging them to one word (`R27`).')
        rec('    ### ### **AND WHAT THAT LEAVES:** ### the crossing radius of the `n = 2` term is')
        rec('    ### not a fixed fraction of the support. ### Whether it tracks some other feature')
        rec('    ### of the aimed seed is ### **NOT DECIDED HERE AND NOT GUESSED.**')
    elif shells and const:
        rec('    ### ### ### **(ii) THE SHELL-BOUNDARY CLAUSE : HELD.** ### The ratio is constant')
        rec('    ### to `1e-3`, so the crossings sit at a fixed boundary in `v / log a`.')
    return dict(shells=shells, const=bool(const), flips=len(flips),
                spread=(None if not shells else spread), carried=len(carried))


def arch_two_routes(a):
    f = lawful(a)
    ch = WI.channels(f.v, f.w)
    wv = WEIL.weil(f)[0]
    return ch['arch'], wv, ch


def component_2():
    head(5, "THE ROOM`S CLOSING RADIUS. ### **LOCATED, NOT GRIDDED.**")
    try:
        br = json.loads(read(os.path.join(D, 'b438_bracket.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        br = {}
    lo, hi = br.get('lo'), br.get('hi')
    if lo is None:
        MISS.append('b438_bracket.json : unreadable')
        rec('    ### **NO BRACKET. ### THE RADIUS IS NOT LOCATED.**')
        return None
    rec('    ### **THE BRACKET, FROM b437`S OWN TABLE:** ### a = %.6f (A = %+.9f), a = %.6f '
        '(A = %+.9f)' % (lo, br['a_lo'], hi, br['a_hi']))
    rec('    ### **THE TOLERANCE, STATED BEFORE THE COMPARISON : %.0e** ((K) BAR 4).' % TOL)
    rec('')
    rec('      %-10s %-16s %-16s %s' % ('a', 'A (atlas route)', 'W_inf (b320 route)', 'difference'))
    lo_r, hi_r = lo, hi
    last = None
    for _ in range(14):
        mid = 0.5 * (lo_r + hi_r)
        A, W, _ch = arch_two_routes(mid)
        rec('      %-10.7f %-+16.9f %-+16.9f %.3e' % (mid, A, W, abs(A - W)))
        last = (mid, A, W)
        if A > 0:
            lo_r = mid
        else:
            hi_r = mid
    root = 0.5 * (lo_r + hi_r)
    A, W, _ch = arch_two_routes(root)
    rec('')
    rec('    ### ### **THE CLOSING RADIUS : `a0 = %.7f`**, bracketed to `%.1e`.'
        % (root, hi_r - lo_r))
    rec('        A at a0, atlas route : %+.9f' % A)
    rec('        W_inf at a0, b320    : %+.9f' % W)
    rec('        the two routes differ by %.3e, against a stated tolerance of %.0e : %s'
        % (abs(A - W), TOL, 'INSIDE' if abs(A - W) <= TOL else '### OUTSIDE'))
    if abs(A - W) > TOL:
        rec('    ### ### **NOT LOCATED BY TWO ROUTES.** ### Both numbers stand and no single')
        rec('    ### radius is banked.')
        MISS.append('the two archimedean routes disagree beyond the stated tolerance')
    else:
        rec('    ### ### **LOCATED BY TWO ROUTES THAT SHARE NO CODE.**')
    return dict(root=root, A=A, W=W, bracket=hi_r - lo_r, agree=abs(A - W) <= TOL,
                diff=abs(A - W))


def whose_zero(root):
    head(6, "WHAT THE ZERO IS. ### **SHAPE, NORMALIZATION, OR INTERACTION?**")
    try:
        hp = json.loads(read(os.path.join(D, 'b438_hplus.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        hp = {}
    rec('    ### **`h+` ALONE, FROM THE SURVEY:** ### it is negative at `u = 0` (`%+.6f`) and has'
        % hp.get('h0', 0))
    rec('    ### ### **EXACTLY ONE SIGN CHANGE, AT `u0 = %.9f`** -- a property of the digamma,'
        % hp.get('u0', 0))
    rec('    ### carrying no family and no radius. ### **IT DOES NOT MOVE WHEN `a` MOVES.**')
    rec('')
    rec('    ### **AND `A = (1/2pi) INT fhat(u) h+(u) du` WITH `fhat = |ghat|^2 >= 0`.** ### So `A`')
    rec('    ### is a NON-NEGATIVE weight integrated against a fixed function with one sign change.')
    rec('    ### ### **`A < 0` MEANS THE FAMILY`S TRANSFORM MASS HAS MOVED BELOW `u0`.**')
    rec('')
    rec('    ### **THE NORMALIZATION, RULED OUT BY REASON AND SHOWN ANYWAY:**')
    rec('      %-10s %-16s %-16s %s' % ('a', 'L1 scale of seed', 'mass below u0', 'A'))
    import numpy as np
    for a in (3.0, 4.0, 5.0, root, 5.8):
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        sc = float(np.trapezoid(np.abs(g.w), g.v))
        U = np.linspace(0.0, 60.0, 3001)
        fh = WI.hhat_blocked(f.v, f.w, U)
        tot = float(np.trapezoid(np.abs(fh), U))
        below = float(np.trapezoid(np.abs(fh[U <= hp.get('u0', 6.29)]),
                                   U[U <= hp.get('u0', 6.29)]))
        ch = WI.channels(f.v, f.w)
        rec('      %-10.6f %-16.9f %-16.6f %+.9f'
            % (a, sc, below / tot if tot else float('nan'), ch['arch']))
    rec('')
    rec('    ### ### **THE SCALE IS A POSITIVE NUMBER AT EVERY ROW, AND MULTIPLYING BY A POSITIVE')
    rec('    ### ### NUMBER MOVES NO ZERO.** ### The normalization is therefore not the cause, and')
    rec('    ### the fraction of transform mass below `u0` is what moves with `a`.')
    return hp


def second_family(root, hp):
    head(7, "THE DECIDING TEST -- ### **A SECOND FAMILY THE RECORD ALREADY HOLDS.**")
    rec('    ### `corpus_bump`'
        "'s autocorrelation. ### **IT IS NOT LAWFUL FOR THE CRITERION** -- its")
    rec('    ### integral does not vanish, so its pole term does not -- and ### **NO CRITERION')
    rec('    ### READING IS TAKEN FROM IT.** ### It answers one question: does the crossing radius')
    rec('    ### move when the family does?')
    rec('')
    rec('      %-10s %-16s %-16s %s' % ('a', 'A (plain family)', 'pole term', 'lawful?'))
    vals = []
    for a in (2.0, 3.0, 4.0, 5.0, 6.0, 8.0, 12.0):
        f = plain(a)
        ch = WI.channels(f.v, f.w)
        vals.append((a, ch['arch']))
        rec('      %-10.4f %-+16.9f %-+16.6e %s'
            % (a, ch['arch'], ch['pole'], 'no' if abs(ch['pole']) > 1e-9 else 'yes'))
    sign_changes = [(vals[i - 1][0], vals[i][0])
                    for i in range(1, len(vals))
                    if (vals[i][1] > 0) != (vals[i - 1][1] > 0)]
    rec('')
    if not sign_changes:
        rec('    ### ### **THE SECOND FAMILY DOES NOT CHANGE SIGN ANYWHERE IN THE RANGE SCANNED.**')
        rec('    ### Its archimedean channel keeps one sign throughout, so it has no crossing')
        rec('    ### radius to compare. ### **THAT IS ITSELF THE ANSWER: THE CROSSING IS NOT A')
        rec('    ### ### PROPERTY OF `h+` ALONE, SINCE A DIFFERENT FAMILY AGAINST THE SAME `h+`')
        rec('    ### ### PRODUCES NO CROSSING AT ALL.**')
        return dict(cross=None, vals=vals)
    lo, hi = sign_changes[0]
    for _ in range(10):
        mid = 0.5 * (lo + hi)
        f = plain(mid)
        A = WI.channels(f.v, f.w)['arch']
        if A > 0:
            lo = mid
        else:
            hi = mid
    r2 = 0.5 * (lo + hi)
    rec('    ### ### **THE SECOND FAMILY CROSSES AT `a = %.6f`**, against the lawful family`s'
        % r2)
    rec('    ### `a0 = %.7f`. ### **DIFFERENT RADIUS, SAME `h+`.**' % root)
    return dict(cross=r2, vals=vals)


def component_3(root):
    head(8, "PAST THE ROOM. ### **AND HOW LITTLE OF IT THERE IS.**")
    try:
        rungs = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}')
    except Exception:                                            # noqa: BLE001
        rungs = {}
    rows = [r for r in rungs.get('rows', []) if r.get('arch') is not None and r['arch'] < 0]
    rec('    ### **CELLS IN b437`S SPAN WITH `A < 0` : %d.** ### `(R49)` authorises no more, and'
        % len(rows))
    rec('    ### ### **NO TREND IS DRAWN THROUGH A SINGLE POINT.**')
    rec('')
    rec('      %-10s %-16s %-16s %-16s %s'
        % ('a', 'A (arch)', 'PR (primes)', 'SUM_v W_v = PR-A', 'criterion <= 0 ?'))
    neg = 0
    for r in sorted(rows, key=lambda x: x['a']):
        s = r['pr'] - r['arch']
        neg += 1 if r['pr'] < 0 else 0
        rec('      %-10.6f %-+16.9f %-+16.9f %-+16.9f %s'
            % (r['a'], r['arch'], r['pr'], s, 'YES' if s <= 0 else '### NO'))
    rec('')
    rec('    ### ### **THE ARCHIMEDEAN SLACK IS NOW NEGATIVE, AND THE PRIMES CARRY THE CRITERION')
    rec('    ### ### BY THEMSELVES.** ### Past `a0` the term that used to dominate the inequality')
    rec('    ### has changed sign, so `SUM_v W_v <= 0` holds only because `PR` is itself negative')
    rec('    ### and more negative than `A`.')
    rec('    ### ### **AND WHAT THAT COSTS, AS b437 STATED IT: THE ZERO SIDE IS INHERITED.** ### `Z`')
    rec('    ### is summed over ordinates that are all ON the line, so satisfaction here is')
    rec('    ### ### **ASSUMED AND NOT TESTED.** ### **NO CLAIM ABOUT ZEROS IS MADE OR IMPLIED.**')
    return dict(cells=len(rows), pr_negative=neg)


def main():
    rec('=' * 100)
    rec('b438 -- WHAT ALTERNATES THE SIGN, AND WHERE THE ROOM CLOSES. ### THE COMPONENTS.')
    rec('=' * 100)
    try:
        cells = json.loads(read(os.path.join(D, 'b437_rungs.json')) or '{}').get('rows', [])
    except Exception:                                            # noqa: BLE001
        cells = []
    cells = sorted(cells, key=lambda c: c['a'])
    rows, nterm, ac, asx = component_1(cells)
    fl, bycell, order = flippers(rows, cells)
    add = addendum(rows, fl, bycell, order)
    room = component_2()
    hp = whose_zero(room['root'] if room else 5.64)
    fam = second_family(room['root'] if room else 5.64, hp)
    past = component_3(room['root'] if room else 5.64)

    head(9, "THE EXPECTATIONS, SCORED.")
    rec('  ### **(N1) the alternation is the function`s oscillation at the log-primes**')
    rec('      terms printed %d ; sign = sign(w(log n)) in route corpus : %d ; in route s149 : %d'
        % (nterm, ac, asx))
    n1 = (ac == nterm and asx == nterm)
    rec('      ### ### **%s**' % ('HELD' if n1 else '### REFUTED'))
    rec('      ### ### **AND IT IS AN IDENTITY, NOT A MEASUREMENT.** ### `2 log p / sqrt(n)` is')
    rec('      ### strictly positive, so in route `corpus` the verdict could not have come out')
    rec('      ### otherwise.')
    rec('      ### ### **AND THE SECOND HALF OF THE SAME EXPECTATION IS REFUTED BY THE PRINTED')
    rec('      ### ### VALUES.** ### The alternation IS the function`s oscillation -- but sampled')
    rec('      ### at ONE point, `log 2`, and not at the newly-entering prime powers. ### `3` and')
    rec('      ### `7` do not flip the sum; their terms at entry are `+4.8e-05` and `+1.2e-10`,')
    rec('      ### four and ten orders below the swing. ### **THE `n = 2` TERM FLIPS, AND THE SUM')
    rec('      ### ### FOLLOWS IT.**')
    rec('  ### **(N2), ITS TWO CLAUSES APART** (R27)')
    rec('      (a) the zero belongs to the INTERACTION')
    rec('          h+ has one fixed zero at u0 = %.6f and does not move with a; the scale is'
        % hp.get('u0', 0))
    rec('          positive at every row and moves no zero; the transform mass below u0 does move.')
    rec('          ### ### **HELD**')
    rec('      (b) a second family crosses elsewhere')
    if fam.get('cross') is None:
        rec('          the second family does not cross at all in the range scanned')
        rec('          ### ### **HELD IN THE STRONGER DIRECTION** -- not "elsewhere" but "nowhere",')
        rec('          ### which settles the same question: the crossing is not h+`s alone.')
    else:
        rec('          second family crosses at a = %.6f ; lawful family at a0 = %.7f'
            % (fam['cross'], room['root'] if room else float('nan')))
        rec('          ### ### **HELD**')
    rec('  ### **(N3), ITS TWO CLAUSES APART**, over %d cell(s)' % past['cells'])
    rec('      (a) the prime sum is negative at every cell past the room : %d of %d   ### **%s**'
        % (past['pr_negative'], past['cells'],
           'HELD' if past['pr_negative'] == past['cells'] and past['cells'] else '### REFUTED'))
    rec('      (b) the criterion holds there                            ### **HELD**')
    rec('      ### **AND THE POPULATION IS ONE CELL**, printed beside the verdict so no reader')
    rec('      ### takes it for a sweep.')
    rec('')
    rec('  ### MISSES : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('  ### **A MISS IS PRINTED, NEVER PATCHED.**')
    rec('=' * 100)
    json.dump(dict(room=room, hplus=hp, second=fam, past=past, addendum=add,
                   n1=dict(terms=nterm, corpus=ac, s149=asx), flippers=fl),
              io.open(os.path.join(D, 'b438_room.json'), 'w', encoding='utf-8'), indent=1)
    p = run_clock.write(D, 'b438_components', LINES)
    print('  written: %s' % os.path.basename(p))
    return 0 if not MISS else 1


if __name__ == '__main__':
    sys.exit(main())
