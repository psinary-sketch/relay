# -*- coding: utf-8 -*-
"""test_composer_b649.py -- THE TESTS OF v5'S COMPOSER'S EDITS, under (R259)(5)-(6) (tools/b649_record.py compose_v5).

### For each edit: its anchor stands once in v4 as b647's composer gives it (the control), is gone from v5 composed with the edit and stays
### when the edit is left out, and the replacement stands in v5 once. Then: v5 with both edits holds no unread figure; (e) and (f) commute;
### b647's composer reproduces v4 as banked.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.argv = sys.argv[:1]
import b649_record as R   # noqa: E402
import b647_record as B7   # noqa: E402
import chain_page as CP   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-100s %s' % (label, 'PASS' if cond else '### FAIL'))

    v4 = B7.compose_v4()
    ve, vf, v5 = R.compose_v5(('e',)), R.compose_v5(('f',)), R.compose_v5()
    m = CP.positivity_mention()
    gl = B7._gl4()
    edits = [('(e%d)' % i, o, (n % m if '%s' in n else n), 'e') for i, (o, n) in enumerate(R.E_ANCHORS, 1)]
    edits += [('(f1)', R.F_ACT, "which an act -- %s -- takes up on the author's word" % R.act_gloss(gl), 'f'),
              ('(f2)', R.F_ONE, "witnessed in the kernel at the constant 1, %s (trivialSummandPremise'_witness)" % gl['the constant 1'].replace(
                  "of TrivialSummandPremise': ", '').rstrip('.'), 'f')]
    for tag, old, new, e in edits:
        with_ = ve if e == 'e' else vf
        without = vf if e == 'e' else ve
        want('%s anchor once in v4 %s ; gone with the edit %s ; kept without it %s ; the replacement once in v5 %s' % (
            tag, v4.count(old) == 1, old not in with_, without.count(old) == 1, v5.count(new) == 1),
             v4.count(old) == 1 and old not in with_ and without.count(old) == 1 and v5.count(new) == 1)
    want('v5 with both edits holds no unread figure', 'NOT READ' not in v5)
    want('the edits commute: (e) then (f) equals (f) applied to the composer with (e)', R._residue(ve) == v5)
    want('b647`s composer reproduces v4 as banked (relay data/b647_deposit_description.txt)', v4 == R.rd(R.V4))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
