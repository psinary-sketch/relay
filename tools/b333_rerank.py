# -*- coding: utf-8 -*-
"""b333_rerank.py -- THE RE-RANK UNDER b332's SEALED RULE, WITH K5's GRADES AS THIS ACT CAN CONFER THEM.

### ### The derivation tool's `rerank` added TWO grades to K5 before its verdict was known: `DERIVES-ON-IMPORTS`
### (the chain) and `MEASURED-ON-FAMILIES` (the third route inside the sealed bar). ### The sealed bar was
### NOT met -- by a defect on the sealed face (it paired the bump with a table made for another function),
### diagnosed in `b333_diagnose.py`. ### So `MEASURED-ON-FAMILIES` is NOT conferred by this act: the like-for-
### like reading in the diagnostic is a reading, and the sealed bar is the only bar this act sealed. ### The
### chain holds link by link and is a derivation under the import bar: `DERIVES-ON-IMPORTS` is conferred,
### superseding b315's `DEFINED-ONLY`. ### This file runs the sealed rule with exactly that grade set, and
### beside it the rule with the un-conferred grade added, to show whether the ranking depends on it.
### Nothing else is adjusted; the ORDER, the rule and the other constituents are imported from b332's own
### generator.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b333_rerank_run.txt')
OUTJ = os.path.join(D, 'b333_rerank.json')

import b332_statement as S  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def run_rule(k5_extra):
    cons = []
    for key, name, unfold, grades, reason in S.CONSTITUENTS:
        gs = list(grades)
        if key == 'K5':
            gs = [g for g in gs if g[0] != 'DEFINED-ONLY']
            gs.extend(k5_extra)
        cons.append((key, name, unfold, gs, reason))
    ranking = []
    for key, name, _u, gs, reason in cons:
        soft = min(gs, key=lambda g: S.ORDER.index(g[0]))
        ranking.append((S.ORDER.index(soft[0]), key, name, soft[0], reason))
    ranking.sort(key=lambda r: (r[0], r[1]))
    top = ranking[0][0]
    softest = [r[1] for r in ranking if r[0] == top]
    k5 = [c for c in cons if c[0] == 'K5'][0][3]
    return ranking, softest, k5


def main():
    rec('=' * 100)
    rec("b333 -- THE RE-RANK UNDER b332's SEALED RULE, K5's GRADES AS THIS ACT CAN CONFER THEM.")
    rec('=' * 100)
    rec('  ORDER (imported from b332): %s' % ' < '.join(S.ORDER))
    rec("  the rule (imported): a constituent's rank is its softest grade among its owners; nothing adjusted.")
    conferred = [('DERIVES-ON-IMPORTS', 'b333', "the source's (150)-(153) read link by link under the corpus's conventions; superseding b315's DEFINED-ONLY")]
    not_conferred = [('MEASURED-ON-FAMILIES', 'b333', 'the third route at the thirteen cells -- NOT CONFERRED: the sealed bar was not met')]
    rec('')
    rec('  K5 GRADES CONFERRED BY THIS ACT : %s' % [g[0] for g in conferred])
    rec('  K5 GRADE NOT CONFERRED           : %s (the sealed bar not met; the diagnostic reading is a reading, not a bar)' % [g[0] for g in not_conferred])
    ranking, softest, k5 = run_rule(conferred)
    rec('')
    rec("  THE RE-RANK, K5 = DERIVES-ON-IMPORTS (b333) + MEASURED-AT-COVERED-CELLS (b320):")
    for i, (_o, k, n, g, _r) in enumerate(ranking, 1):
        rec('      %d. %s %-46s %s' % (i, k, n[:46], g))
    rec('  THE NEW SOFTEST : %s' % softest)
    ranking2, softest2, _k = run_rule(conferred + not_conferred)
    same = [(r[1], r[3]) for r in ranking] == [(r[1], r[3]) for r in ranking2] and softest == softest2
    rec('  the same rule with the un-conferred MEASURED-ON-FAMILIES added : softest %s ; ranking identical : %s' % (softest2, same))
    seat = 'MET' if sorted(softest) == ['K5', 'K6'] else 'NOT MET'
    rec('')
    rec("  THE NAVIGATOR'S EXPECTATION FOR THE NEW SOFTEST : NOT STATED IN THE ORDER -- recorded as such, not scored.")
    rec("  THIS SEAT'S EXPECTATION (registered (F): K5 and K6 tie at MEASURED-AT-COVERED-CELLS) : %s" % seat)
    rec("  THE AIM-MAP IS NAMED AS NEXT; ITS TARGET IS THE NEW SOFTEST: %s." % ' and '.join(softest))
    rec('=' * 100)
    payload = dict(order=S.ORDER, k5_grades=[list(g) for g in k5], not_conferred=[list(g) for g in not_conferred],
                   ranking=[list(r) for r in ranking], softest=softest, ranking_with_families_identical=same,
                   seat_expectation=seat, navigator_expectation='NOT STATED IN THE ORDER')
    open(OUTJ + '.tmp', 'wb').write((json.dumps(payload, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8'))
    os.replace(OUTJ + '.tmp', OUTJ)
    return 0


if __name__ == '__main__':
    code = main()
    k, name = 1, OUT
    while os.path.exists(name):
        k += 1
        name = os.path.join(D, 'b333_rerank_run%d.txt' % k)
    io.open(name, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
