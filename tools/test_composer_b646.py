# -*- coding: utf-8 -*-
"""test_composer_b646.py -- (R256)(4): THE FOUR COMPOSITION RULES OF THE DESCRIPTION'S COMPOSER, ONE TEST EACH, AND THE CARRIED REPRODUCTION.

### Numbered cases `  (n) ... PASS|FAIL` ((R233)(3)). Each rule is read on v3 (every rule applied) and, as its control, on the text with that
### rule withheld -- the rule's effect must be present in the one and absent in the other, so no case passes on a text that never had the
### defect. The composer is relay tools/b646_record.py compose_v3; Zenodo's tags are relay data/b646_zenodo_tags.json.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.argv = [sys.argv[0], 'test']
import b646_record as R  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def text(h):
    return re.sub(r'<[^>]+>', ' ', h)


def main():
    ALL = R.ALL_RULES
    v3 = R.compose_v3(rules=ALL)
    v2 = R.rd(R.V2)
    wo = dict((r, R.compose_v3(rules=tuple(x for x in ALL if x != r))) for r in ALL)
    lis = re.findall(r'<li>(.*?)</li>', v3)
    cases = []
    # ### (a) a header factored
    cases.append(('(a) the theorems` header verbatim, once', v3.count(R.HEAD_THEOREMS) == 1))
    cases.append(('(a) the premises` header verbatim, once', v3.count(R.HEAD_PREMISES) == 1))
    cases.append(('(a) no theorem row carries its kernel, tag or axiom print (rows %d)' % len(lis),
                  not any('at its tag' in x or '#print axioms' in x for x in lis) and v3.count('82550e4') == 1))
    cases.append(('(a) no premise row carries the default discharge clause', R.DEFAULT_DC not in v3))
    cases.append(('(a) control: without (a) the rows carry the tag %d times and the default clause' % wo['a'].count('at its tag'),
                  wo['a'].count('at its tag') >= 13 and R.DEFAULT_DC in wo['a'] and R.HEAD_THEOREMS not in wo['a']))
    # ### (b) a list emitted, in Zenodo's tags
    tags = set(re.findall(r'</?([a-zA-Z0-9]+)', v3))
    heads = re.findall(r'<p><strong>(.*?)</strong></p>', v3)
    cases.append(('(b) the five parts headed in order (%s)' % heads, heads == [h.rstrip('.') for h in R.PART_HEADS]))
    cases.append(('(b) the theorems and the premises by status are lists (<ul> %d, <li> %d)' % (v3.count('<ul>'), v3.count('<li>')),
                  v3.count('<ul>') >= 2 and all(n in ' '.join(lis) for n in ('h2_sign_iff_rh', 'BoundPremises', 'PlattTrudgianHeight'))))
    cases.append(('(b) every tag used is one Zenodo accepts (%s)' % sorted(tags), tags <= R._allowed_tags() and 'h1' not in tags))
    cases.append(('(b) control: without (b) no list and no head tag', '<ul>' not in wo['b'] and '<strong>' not in wo['b']))
    # ### (c) the exhaustiveness sentence verbatim, the old clause absent
    cases.append(('(c) the exhaustiveness sentence verbatim, once', text(v3).count(R.EXHAUST) == 1))
    cases.append(('(c) THE_UNCONDITIONAL_SURROUND section 6a cited by its words',
                  'section 6a: "The attribution face asks whether every zero is single-class-produced (covers_all)' in v3
                  and 'Both are equivalent to RH given the surround."' in v3))
    cases.append(('(c) the old clause absent ("bounds by its mechanism exclusions", "Its mechanism exclusions are")',
                  'bounds by its mechanism exclusions' not in v3 and 'Its mechanism exclusions are' not in v3))
    cases.append(('(c) control: without (c) the old clause present and the sentence absent',
                  'bounds by its mechanism exclusions' in wo['c'] and R.EXHAUST not in wo['c']))
    # ### (d) no PREDICATE-UNLISTED
    cases.append(('(d) no PREDICATE-UNLISTED in the text', 'PREDICATE-UNLISTED' not in v3))
    cases.append(('(d) dedekind_rhs` reads INTERFACES on its two premises, named',
                  any(x.startswith("dedekind_rhs' -- INTERFACES -- it holds on the premises TrivialSummandPremise'") and 'EulerFactorPremise' in x
                      for x in lis)))
    cases.append(('(d) control: without (d) the PREDICATE-UNLISTED definition present', 'PREDICATE-UNLISTED' in wo['d']))
    # ### the carried composer and the size
    cases.append(('the composer with no rule reproduces v2 byte for byte from the table at v2',
                  R.compose_v3(rules=(), TR=R._tr(R.V2_TABLE_REV)) == v2))
    cases.append(('v3 is shorter than v2 (%d < %d bytes)' % (len(v3.encode('utf-8')), len(v2.encode('utf-8'))),
                  len(v3.encode('utf-8')) < len(v2.encode('utf-8'))))
    cases.append(('no unread figure in v3', not re.search(r'NOT READ|NOT BANKED|not in the table|None', v3)))
    bad = 0
    for n, (what, ok) in enumerate(cases, 1):
        bad += not ok
        print('  (%d) %s -- %s' % (n, what, 'PASS' if ok else 'FAIL'))
    print('### ### **%d of %d cases as wanted -- %s**' % (len(cases) - bad, len(cases), 'PASS' if not bad else 'FAIL'))
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
