# -*- coding: utf-8 -*-
"""test_e0_rule.py -- THE TEST OF tools/e0_rule.py's CLASS-MEMBERSHIP CLAUSE, (R180)(2)(f), written at b570.

### Both polarities on headers, and the rule's own seven-case self-test:
###   (1) the rule's self_test (b568's seven headers) still passes;
###   (2) b569's two χ headers, as Lean's source states them at v0.11 (read here from the kernel), read DERIVES;
###   (3) a class predicate on a variable the conclusion mentions is a domain condition (synthetic);
###   (4) a class predicate on a variable the conclusion does NOT mention reads as a premise (INTERFACES) -- the ruling's
###       named negative case;
###   (5) a named Prop premise beside a class binder still reads INTERFACES;
###   (6) `conclusion` reads past ( ), { }, [ ] binder groups to the ':'.
### Usage: python tools/test_e0_rule.py
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
V011 = '19b7d1e48a40ca22618722306194404423dca224'


def header(rel, short):
    src = subprocess.run(['git', '-C', KER, 'show', '%s:%s' % (V011, rel)], capture_output=True).stdout.decode('utf-8')
    m = re.search(r'^theorem ' + re.escape(short) + r'(?![\w\'])(.*?):=', src, re.M | re.S)
    return ' '.join(m.group(1).split()) if m else None


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    want('(1) the rule`s own self-test (b568`s seven headers)', E0.self_test())
    for rel, short in (('SIDEExplicitFormula/Chi/LocalCount.lean', 'LFunction_zeros_finite_of_isCompact'),
                       ('SIDEExplicitFormula/Chi/ZeroSummability.lean', 'EF_zero_sum_summable_chi')):
        h = header(rel, short)
        g = E0.grade(h or '', 'theorem')
        want('(2) %s at v0.11 reads DERIVES (read %s; %s)' % (short, g[0], g[1][:60]), h is not None and g[0] == 'DERIVES')
    g3 = E0.grade('{k : ℝ → ℂ} (hk : ContDiff ℝ 2 k) (hkc : HasCompactSupport k) : Summable (fun n => k n)', 'theorem')
    want('(3) a class binder on a variable the conclusion mentions: DERIVES (read %s)' % g3[0], g3[0] == 'DERIVES')
    g4 = E0.grade('{f k : ℝ → ℂ} (hf : ContDiff ℝ 2 f) : Summable (fun n => k n)', 'theorem')
    want('(4) a class binder on a variable the conclusion does NOT mention: INTERFACES (read %s)' % g4[0], g4[0] == 'INTERFACES')
    g5 = E0.grade('{k : ℝ → ℂ} (hk : ContDiff ℝ 2 k) (hX : LiLimitExchange n) : P k', 'theorem')
    want('(5) a named premise beside a class binder: INTERFACES (read %s)' % g5[0], g5[0] == 'INTERFACES')
    c6 = E0.conclusion('{N : ℕ} [NeZero N] (h1 : χ ≠ 1) {K : Set ℂ} (hK : IsCompact K) : (K ∩ s).Finite')
    want('(6) conclusion reads past the binder groups (read %r)' % c6, c6.strip() == '(K ∩ s).Finite')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
