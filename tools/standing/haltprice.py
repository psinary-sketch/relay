# -*- coding: utf-8 -*-
"""standing/haltprice.py -- v1.33.0, (R363)(7)(iv), b752 events (7), (8): A HALT PRICES FROM THE EXERCISE BANKS AND THE CAPS.

b752's seat priced a halt's two routes at the suite arm G-ANSWERS-BANKED, an arm in no part's exercise bank of that act's run, and read the
face's registered cap ("questions asked of the author at the root", cap 1) only after the author's ruling named it. Before a halt is put, each
arm it names as a route's cost is read in the act's exercise banks (data/<act>_exercise_<part>.json: the parts that run it, live or not), and
the face's registered caps (data/<act>_satisfiable.json) whose clause carries the halt's words are read beside it, each with its cap and demand.
An arm in no exercise bank costs no route of this act's run; a cap at its demand refuses a route that adds to it. Reads only.

  python -X utf8 -u tools/standing/haltprice.py price <act> --arm <ARM> [--arm ...] --cap <words> [--cap ...]
  python -X utf8 -u tools/standing/haltprice.py control
"""
import glob
import io
import json
import os
import sys

RELAY = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(RELAY, 'data')


def exercise(act, d=D):
    """{part: {arm: row}} from the act's exercise banks; {} where none is written."""
    out = {}
    for f in sorted(glob.glob(os.path.join(d, '%s_exercise_*.json' % act))):
        part = os.path.basename(f)[len('%s_exercise_' % act):-len('.json')]
        out[part] = (json.load(io.open(f, encoding='utf-8')).get('exercise') or {})
    return out


def caps(act, d=D):
    p = os.path.join(d, '%s_satisfiable.json' % act)
    return list(json.load(io.open(p, encoding='utf-8')).get('clauses') or []) if os.path.isfile(p) else None


def price(act, arms, words, d=D):
    """(lines, figures): each arm's parts; each cap matching any of the words, case ignored."""
    ex = exercise(act, d)
    cs = caps(act, d)
    L = ['### THE HALT PRICED, %s ((R363)(7)(iv)): EXERCISE BANKS %d (%s) ; THE FACE`S CAPS %s' % (
        act, len(ex), ', '.join(ex) or 'NONE WRITTEN', ('%d clauses' % len(cs)) if cs is not None else 'ABSENT (no satisfiable bank)')]
    fig = dict(arms={}, caps=[])
    for a in arms:
        parts = [(p, r.get(a)) for p, r in ex.items() if a in r]
        fig['arms'][a] = [p for p, _r in parts]
        L.append('   ARM %s: in %d part(s) %s%s' % (a, len(parts), ['%s (live %s)' % (p, (r or {}).get('live')) for p, r in parts] or '',
                                                   '' if parts else ' -- IN NO PART`S RUN: NO ROUTE OF THIS ACT`S RUN COSTS IT'))
    for c in cs or []:
        if any(w.lower() in (c.get('clause') or '').lower() for w in words):
            at = c.get('demand', 0) >= c.get('cap', 0)
            fig['caps'].append((c.get('clause'), c.get('cap'), c.get('demand')))
            L.append('   CAP "%s": cap %s, demand %s %s%s -- %s' % (c.get('clause'), c.get('cap'), c.get('demand'), c.get('units'),
                                                                 ' AT ITS CAP: A ROUTE ADDING ONE REFUSES' if at else '', (c.get('from') or '')[:120]))
    if words and not fig['caps']:
        L.append('   CAP: no registered clause carries %s' % (list(words),))
    return L, fig


def control():
    """(ok, lines): b752's halt replayed -- G-ANSWERS-BANKED in no part of 10; the root cap read at cap 1, demand 1; a planted arm present in
    one part (G-DELETES-ONE-BRANCH, the act part) found."""
    L, f = price('b752', ['G-ANSWERS-BANKED', 'G-DELETES-ONE-BRANCH'], ['questions asked of the author at the root'])
    ok = f['arms'].get('G-ANSWERS-BANKED') == [] and f['arms'].get('G-DELETES-ONE-BRANCH') == ['act'] and \
        f['caps'] == [('questions asked of the author at the root', 1, 1)]
    return ok, L + ['### (halt) b752`s G-ANSWERS-BANKED IN NO PART ; THE ROOT CAP 1 AT DEMAND 1 ; THE PLANTED ARM IN THE ACT PART ; THE CONTROL %s' % (
        'AS WANTED' if ok else 'NOT AS WANTED')]


def main(a):
    if a[:1] == ['control']:
        ok, L = control()
        print('\n'.join(L))
        return 0 if ok else 1
    if a[:1] == ['price'] and len(a) >= 2:
        arms = [a[i + 1] for i, x in enumerate(a) if x == '--arm' and i + 1 < len(a)]
        words = [a[i + 1] for i, x in enumerate(a) if x == '--cap' and i + 1 < len(a)]
        print('\n'.join(price(a[1], arms, words)[0]))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
