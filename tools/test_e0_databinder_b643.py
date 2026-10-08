# -*- coding: utf-8 -*-
"""test_e0_databinder_b643.py -- (R253)(3)(a): A DATA BINDER IS DATA, NOT A NAMED PREDICATE.

### tools/e0_rule.py read the binder `n : WithTop ℕ∞` of contDiff_riemannZeta₀ as an application of a name no lexicon lists and graded
### the theorem INTERFACES (relay data/b642_grades.txt, its note). The planted binders -- n : WithTop ℕ∞, n : ℕ, x : ℝ, and the order
### type alone -- must type as data and leave the grade DERIVES; the control -- an application of a premise name the lexicon does not
### list -- must still read as a named predicate, so the repair does not widen the data class past type formers.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CASES = [
    ('n : WithTop ℕ∞ types as data', lambda: E.typing('WithTop ℕ∞')[0] == 'data'),
    ('n : ℕ types as data', lambda: E.typing('ℕ')[0] == 'data'),
    ('x : ℝ types as data', lambda: E.typing('ℝ')[0] == 'data'),
    ('the order type`s symbol ℕ∞ alone types as data, not a predicate', lambda: E.typing('ℕ∞')[0] == 'data'),
    ('WithBot ℤ types as data', lambda: E.typing('WithBot ℤ')[0] == 'data'),
    ('contDiff_riemannZeta₀`s elaborated header grades DERIVES', lambda: E.grade('{n : WithTop ℕ∞} : ContDiff ℂ n riemannZeta₀', 'theorem')[0] == 'DERIVES'),
    ('the planted header with all three data binders grades DERIVES',
     lambda: E.grade('{n : WithTop ℕ∞} (m : ℕ) (x : ℝ) : ContDiff ℂ n riemannZeta₀', 'theorem')[0] == 'DERIVES'),
    ('CONTROL: an unlisted premise name applied still reads as a named predicate',
     lambda: E.typing('PlantedPremiseB643 k')[0] == 'prop' and 'UNLEXED' in E.typing('PlantedPremiseB643 k')[1]),
    ('CONTROL: a header carrying that premise grades INTERFACES, not DERIVES',
     lambda: E.grade('(k : ℝ → ℂ) (hP : FamilyPremiseB643 k) : P k', 'theorem')[0] in ('INTERFACES', 'PREDICATE-UNLISTED')),
    ('the rule`s own self-test still passes', lambda: E.self_test()),
]


def main():
    ok = 0
    for i, (name, f) in enumerate(CASES, 1):
        try:
            r = bool(f())
        except Exception as e:
            r = False
            name += ' (raised %s)' % type(e).__name__
        ok += r
        print('  (%d) %-100s %s' % (i, name, 'PASS' if r else '### FAIL'))
    print('### ### **%d of %d cases as wanted -- %s**' % (ok, len(CASES), 'PASS' if ok == len(CASES) else 'FAIL'))
    return 0 if ok == len(CASES) else 1


if __name__ == '__main__':
    sys.exit(main())
