# -*- coding: utf-8 -*-
"""test_e0_existential.py -- THE TEST OF tools/e0_rule.py's EXISTENTIAL-BINDER CLAUSE, (R201)(3), written at b591.

### Both polarities on headers, the rule's own self-test and b570's test run unchanged:
###   (1) the rule's self_test (b568's seven headers) still passes;
###   (2) b570's test of the class clause, run as written, still passes;
###   (3) `membership_load_bearing` at SIDE-explicit-formula v0.16 = c404e72, read from the kernel's source, reads DERIVES --
###       its `hP` lies inside the existential of its conclusion;
###   (4) `epstein_not_h2_sign_cfg` at v0.16, whose `hP` is an outer binder, still reads INTERFACES -- the ruling's named case;
###   (5) a synthetic header with an outer premise binder AND an inner existential binder reads INTERFACES;
###   (6) a synthetic header with the existential binder alone reads DERIVES;
###   (7) `exist_spans` stops at the existential's top-level comma: a binder after that comma (inside a nested ∀) is not
###       covered by the span. ### b637, (R247)(3)-(4), RE-POINTED: the binder after the comma lies inside the existential's body, and the
###       binder grammar reads the statement's binders as Lean's (the header's groups and the conclusion's leading telescope), so it is no
###       binder of the statement but part of the conclusion -- (R201)(3)'s words, "a binder inside an existential in a theorem's
###       conclusion is part of the conclusion"; the case wanted INTERFACES, the old pattern's reach; it now wants DERIVES, the span's
###       reading unchanged. No row of the terminal table moves by it (relay data/b637_rerun.txt).
### Usage: python tools/test_e0_existential.py
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

KER = 'D:/SIDE-explicit-formula'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'


def header(rel, short):
    src = subprocess.run(['git', '-C', KER, 'show', '%s:%s' % (V016, rel)], capture_output=True).stdout.decode('utf-8')
    m = re.search(r'^theorem ' + re.escape(short) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
    return ' '.join(m.group(1).split()) if m else None


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-108s %s' % (label, 'PASS' if cond else '### FAIL'))

    want('(1) the rule`s own self-test (b568`s seven headers)', E0.self_test())
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'test_e0_rule.py')], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    want('(2) b570`s test of the class clause, run unchanged (exit %d)' % r.returncode, r.returncode == 0 and '-- PASS**' in r.stdout)
    h3 = header('SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'membership_load_bearing')
    g3 = E0.grade(h3 or '', 'theorem')
    want('(3) membership_load_bearing at v0.16 reads DERIVES (read %s; %s)' % (g3[0], g3[1][:50]), h3 is not None and g3[0] == 'DERIVES')
    h4 = header('SIDEExplicitFormula/Schema/Epstein.lean', 'epstein_not_h2_sign_cfg')
    g4 = E0.grade(h4 or '', 'theorem')
    want('(4) epstein_not_h2_sign_cfg at v0.16, an outer binder, reads INTERFACES (read %s; %s)' % (g4[0], g4[1][:50]),
         h4 is not None and g4[0] == 'INTERFACES' and g4[1].startswith('hP : EpsteinPremises'))
    g5 = E0.grade('(hX : LiLimitExchange n) : ∃ (Z : Cfg) (hP : Premises Z), P Z', 'theorem')
    want('(5) an outer premise binder beside an inner existential binder: INTERFACES on the outer (read %s; %s)' % (g5[0], g5[1]),
         g5[0] == 'INTERFACES' and g5[1] == 'hX : LiLimitExchange n')
    g6 = E0.grade(': ∃ (Z : Cfg) (rhs : ℝ → ℂ) (hP : Premises Z rhs), P Z', 'theorem')
    want('(6) the existential binder alone: DERIVES (read %s)' % g6[0], g6[0] == 'DERIVES')
    h7 = ': ∃ (Z : Cfg), ∀ (hQ : Premises Z), P Z'
    sp = E0.exist_spans(h7)
    q = h7.index('(hQ')
    g7 = E0.grade(h7, 'theorem')[0]
    want('(7) the span ends at the existential`s top-level comma (spans %s; the binder after it at %d uncovered); the binder inside the '
         'existential`s body part of the conclusion, DERIVES (read %s)' % (sp, q, g7),
         len(sp) == 1 and not any(a <= q < b for a, b in sp) and g7 == 'DERIVES')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
