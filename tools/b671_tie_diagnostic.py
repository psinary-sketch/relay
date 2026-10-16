# -*- coding: utf-8 -*-
"""b671_tie_diagnostic.py -- THE MAP RUN ONCE MORE AS A DIAGNOSTIC, ITS PRINTS AND NOTHING ELSE CHANGED, under the navigator's answer on
the landing ((R281)(7)).

### tools/b667_epstein_map_balls.py is read as text, unedited on disk; one print line is inserted after its residual line (:348, `res = [...]`,
### the anchor read exactly once): a `say` of each tie control's four residual balls -- the separation's ball, midpoint and radius -- at
### that j. Nothing else changes: the two names tools/b671_epstein_map_narrowed.py reassigns (Q0_CERT to the narrowed list; put's bank
### name, here b671_tie_diagnostic_run, so neither b667's nor b671's control bank is written). The unified diff of the inserted text
### against the map is banked (`diff` route, data/b671_tie_diagnostic_diff.txt) before the run; the map file's sha256 printed before and after.
### data/b671_tie_diagnostic.txt (rows are tie controls) is read from the run's own print lines (OUT) and nothing recomputed here.
### Usage: `python -X utf8 tools/b671_tie_diagnostic.py diff` ; `run` -> the map once, the run bank and the diagnostic bank.
"""
import difflib
import hashlib
import io
import os
import re
import sys
import time
import types

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
MAP = os.path.join(ROOT, 'tools', 'b667_epstein_map_balls.py')
NARROWED = 'b671_epstein_zeros_narrowed.json'
RUN_BANK = 'b671_tie_diagnostic_run'
D = os.path.join(ROOT, 'data')
NL = chr(10)
ANCHOR = '        res = [(acb(aq) + bq * nd) ** 2 * p + 1 for nd, p in zip(nodes, ph)]' + NL
PRINT = ("        say('  TIE %s %d j %d : ' % (name, prec, j) + ' | '.join('mid %s ; |mid| %s ; rad %s ; 0 in %s' % ("
         "x.mid().str(6, radius=False), abs(x.mid()).str(6, radius=False), x.rad().str(6, radius=False), "
         "x.real.contains(0) and x.imag.contains(0)) for x in res))" + NL)
BAR_EXP = -20                    # ### the map's bar, :349 `x.rad() < arb(2) ** -20`
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def source():
    t = io.open(MAP, encoding='utf-8', newline='').read()
    if t.count(ANCHOR) != 1:
        sys.exit('### THE RESIDUAL LINE IS NOT READ EXACTLY ONCE IN THE MAP (%d) -- NOTHING RUN' % t.count(ANCHOR))
    return t, t.replace(ANCHOR, ANCHOR + PRINT)


def put(name, text):
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)


def diff():
    t, u = source()
    d = list(difflib.unified_diff(t.split(NL), u.split(NL), 'b667_epstein_map_balls.py', 'the diagnostic`s text', lineterm=''))
    added = [l for l in d if l.startswith('+') and not l.startswith('+++')]
    removed = [l for l in d if l.startswith('-') and not l.startswith('---')]
    L = ['b671 -- THE TIE DIAGNOSTIC`S DIFF (the navigator`s answer on the landing): tools/b667_epstein_map_balls.py read as text, sha256 %s, '
         'unedited on disk; lines added %d, lines removed %d; the added line a `say` alone. The two names reassigned as '
         'tools/b671_epstein_map_narrowed.py does: Q0_CERT -> %s ; put`s bank name -> %s.' % (sha(MAP), len(added), len(removed), NARROWED, RUN_BANK),
         ''] + d + ['', '### the wrapper, whole (tools/b671_tie_diagnostic.py):'] + io.open(os.path.abspath(__file__), encoding='utf-8').read().split(NL)
    put('b671_tie_diagnostic_diff.txt', NL.join(L) + NL)
    print(NL.join(L[:12]))
    return len(added), len(removed)


def run():
    a, r = diff()
    if (a, r) != (1, 0):
        sys.exit('### THE DIFF IS NOT ONE ADDED LINE -- NOTHING RUN')
    before = sha(MAP)
    _t, u = source()
    MB = types.ModuleType('b667_epstein_map_balls_diag')
    MB.__file__ = MAP
    exec(compile(u, MAP + ' (the diagnostic`s text)', 'exec'), MB.__dict__)
    MB.Q0_CERT = NARROWED
    orig_put = MB.put
    MB.put = lambda recs, name=RUN_BANK: orig_put(recs, name)
    MB.say('### b671 tie diagnostic: the map (sha256 %s) with one print line added after its residual line, run once on data/%s.gz; '
           'data/b671_tie_diagnostic_diff.txt' % (before, NARROWED))
    MB.main()
    after = sha(MAP)
    bank(MB.OUT, before, after)


def bank(out, before, after):
    """rows are tie controls: (cell, bits, j); per control the four residuals` |mid| and radius, the largest of each, the map`s own test,
    and the two readings` tests printed beside the bar."""
    bar = 2.0 ** BAR_EXP
    rows = []
    for l in out:
        m = re.match(r'  TIE (.*) (\d+) j (\d+) : (.*)$', l)
        if not m:
            continue
        parts = [re.match(r'mid (.*) ; \|mid\| (\S+) ; rad (\S+) ; 0 in (True|False)$', x.strip()) for x in m.group(4).split(' | ')]
        mids = [float(p.group(2)) for p in parts]
        rads = [float(p.group(3)) for p in parts]
        zin = [p.group(4) == 'True' for p in parts]
        passed = all(zin) and max(rads) < bar
        # ### the words, the navigator's answer on the two readings: INSTRUMENT -- the ball contains 0 and its radius crosses the bar;
        # ### OBJECT -- the ball wholly beneath the bar, |mid| + radius < 2^-20; a failed control that is neither printed NEITHER
        obj = all(mm + rr < bar for mm, rr in zip(mids, rads))
        ins = all(zin) and max(rads) >= bar
        word = 'PASS' if passed else 'OBJECT' if obj else 'INSTRUMENT' if ins else 'NEITHER'
        rows.append(dict(cell=m.group(1), bits=int(m.group(2)), j=int(m.group(3)), mids=mids, rads=rads, zin=zin,
                         sep=max(mids), rad=max(rads), passed=passed, word=word))
    L = ['b671 -- THE TIE DIAGNOSTIC (the navigator`s answer on the landing, under (R281)(7)) (%s): rows are tie controls -- the cell, the '
         'precision, j; the separation`s ball at each of the four tie nodes by its midpoint`s modulus |mid| and its radius; the largest of each '
         'beside the bar 2^%d = %.6e; the map`s own test (every ball containing 0 with radius below the bar); the radius-to-bar ratio.'
         % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), BAR_EXP, bar), '',
         '### the map tools/b667_epstein_map_balls.py sha256 %s before the run and %s after (%s)' % (before, after, 'EQUAL' if before == after else 'CHANGED'),
         '### the columns: RAD>=BAR -- the radius alone crosses the bar ; |MID|<BAR -- the midpoint`s separation beneath the bar ; '
         '|MID|-RAD>=BAR -- the ball held off zero by more than the bar',
         '### the words (the navigator`s answer on the two readings, under (R281)): INSTRUMENT -- the separation`s ball contains 0 and its '
         'radius crosses the bar, the control undecided by the instrument; OBJECT -- the ball wholly beneath the bar, |mid| + radius < 2^-20, '
         'the separation certified small by the object; a passing control reads PASS, a failed control that is neither NEITHER.', '']
    for x in rows:
        L.append('  %-28s %3d j %2d : |mid| max %.3e ; rad max %.3e ; rad/bar %.3e ; RAD>=BAR %-5s ; |MID|<BAR %-5s ; |MID|-RAD>=BAR %-5s ; '
                 'the map`s test %s ; %s' % (x['cell'], x['bits'], x['j'], x['sep'], x['rad'], x['rad'] / bar, x['rad'] >= bar, x['sep'] < bar,
                                             any(mm - rr >= bar for mm, rr in zip(x['mids'], x['rads'])), 'PASS' if x['passed'] else 'FAIL',
                                             x['word']))
    L.append('')
    for (cell, bits) in sorted(set((x['cell'], x['bits']) for x in rows)):
        g = [x for x in rows if (x['cell'], x['bits']) == (cell, bits)]
        f = [x for x in g if not x['passed']]
        L.append('### ### **%s at %d bits : CONTROLS %d ; PASS %d ; FAIL %d ; of the failed: RAD>=BAR %d, |MID|<BAR %d, |MID|-RAD>=BAR %d ; '
                 'INSTRUMENT %d, OBJECT %d, NEITHER %d ; largest rad/bar over the failed %s.**' % (
                     cell, bits, len(g), len(g) - len(f), len(f), sum(x['rad'] >= bar for x in f), sum(x['sep'] < bar for x in f),
                     sum(any(mm - rr >= bar for mm, rr in zip(x['mids'], x['rads'])) for x in f),
                     sum(x['word'] == 'INSTRUMENT' for x in f), sum(x['word'] == 'OBJECT' for x in f), sum(x['word'] == 'NEITHER' for x in f),
                     ('%.3e' % max(x['rad'] / bar for x in f)) if f else '-'))
    put('b671_tie_diagnostic.txt', NL.join(L) + NL)
    print(NL.join(L[-6:]))


def words():
    """the words added from the run`s own print lines as its bank holds them (data/b671_tie_diagnostic_run.txt); nothing re-run."""
    t = io.open(os.path.join(D, RUN_BANK + '.txt'), encoding='utf-8').read()
    h = re.search(r'the map \(sha256 ([0-9a-f]{64})\)', t)
    if not h or h.group(1) != sha(MAP):
        sys.exit('### THE RUN BANK DOES NOT NAME THE MAP AT ITS PRESENT sha256 -- NOTHING WRITTEN')
    bank(t.split(NL), h.group(1), sha(MAP))


if __name__ == '__main__':
    {'diff': diff, 'run': run, 'words': words}.get(sys.argv[1] if len(sys.argv) > 1 else '', lambda: print('usage: diff | run'))()
