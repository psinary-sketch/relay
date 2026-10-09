# -*- coding: utf-8 -*-
"""test_met_b646.py -- (R256)(4)(d): TrivialSummandPremise' ENTERS THE E0 RULE'S MET LIST BY RULING; dedekind_rhs' READS INTERFACES ON ITS
TWO NAMED PREMISES.

### Numbered cases `  (n) ... PASS|FAIL` ((R233)(3)). The statement is the gate's own, as b642 banked it (relay data/b642_grades.txt, the row
### `PREDICATE-UNLISTED  theorem  SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'` and its `statement:` line), graded by tools/e0_rule.py
### at HEAD, and against MET without the entry (the grade before the ruling) so the move is the entry's and nothing else's.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NAME = "SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'"
ENTRY = "TrivialSummandPremise'"


def statement():
    t = io.open(os.path.join(ROOT, 'data', 'b642_grades.txt'), encoding='utf-8').read().replace(chr(13), '').split(chr(10))
    i = [k for k, l in enumerate(t) if l.split() == ['PREDICATE-UNLISTED', 'theorem', NAME]][0]
    return t[i + 1].split('statement: ', 1)[1]


def main():
    out, bad = [], 0
    st = statement()
    met = E.MET
    cases = []
    cases.append(('the entry is in MET at HEAD', ENTRY in met))
    cases.append(('MET at HEAD is the earlier list and the entry, nothing else', set(met) - {ENTRY} == set(met[:-1]) and met[-1] == ENTRY
                  and len(met) == 52))
    g1, why1, _r = E.grade(st, 'theorem')
    cases.append(('dedekind_rhs` reads INTERFACES at HEAD (got %s)' % g1, g1 == 'INTERFACES'))
    cases.append(('its premises are its two named binders, hT : TrivialSummandPremise` k and hE : Family.EulerFactorPremise q (got %r)' % why1,
                  why1 == "hT : TrivialSummandPremise' k, hE : Family.EulerFactorPremise q"))
    E.MET = tuple(x for x in met if x != ENTRY)
    try:
        g0, why0, _r = E.grade(st, 'theorem')
    finally:
        E.MET = met
    cases.append(('without the entry it reads PREDICATE-UNLISTED on hT, as b642 banked it (got %s, %r)' % (g0, why0),
                  g0 == 'PREDICATE-UNLISTED' and why0 == "hT : TrivialSummandPremise' k"))
    cases.append(('the rule`s own self-test passes at HEAD', bool(E.self_test()) if hasattr(E, 'self_test') else False))
    for n, (what, ok) in enumerate(cases, 1):
        bad += not ok
        print('  (%d) %s -- %s' % (n, what, 'PASS' if ok else 'FAIL'))
    print('### ### **%d of %d cases as wanted -- %s**' % (len(cases) - bad, len(cases), 'PASS' if not bad else 'FAIL'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
