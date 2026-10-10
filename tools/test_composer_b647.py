# -*- coding: utf-8 -*-
"""test_composer_b647.py -- (R257)(4): THE FOUR EDITS OF THE DESCRIPTION AT v4, ONE TEST EACH, EACH WITH ITS CONTROL.

### Numbered cases `  (n) ... PASS|FAIL` ((R233)(3)). Each edit is read on v4 (every edit applied) and, as its control, on the text with that
### edit withheld -- the edit's effect must be present in the one and absent in the other, so no case passes on a text that never had the
### defect. The composer is relay tools/b647_record.py compose_v4 over b646's sealed compose_v3; the glossary is relay data/glossary.txt.
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.argv = [sys.argv[0], 'test']
import b647_record as R  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

OPEN_PHRASE = re.compile(r'carr\w+ as (?:the|its) one open premise')


def parts(h):
    segs = re.split(r'<p><strong>(.*?)</strong></p>', h)
    return dict((segs[i], segs[i + 1]) for i in range(1, len(segs) - 1, 2))


def main():
    ALL = R.V4_EDITS
    v4 = R.compose_v4(ALL)
    wo = dict((e, R.compose_v4(tuple(x for x in ALL if x != e))) for e in ALL)
    gl = R._gl4()
    P, Pw = parts(v4), dict((e, parts(wo[e])) for e in ALL)
    cases = []
    # ### (a) the glossed passages
    cases.append(('(a) not_trivialSummandPremise glossed in six words',
                  R.NOT_TSP[1] in v4 and len(R.NOT_TSP[1].split(' -- ')[-1].replace('</li>', '').split()) == 6))
    cases.append(("(a) dedekind_rhs': its two premises separated (a colon, then a semicolon before the second)", R.DED[1] in v4 and R.DED[0] not in v4))
    cases.append(('(a) Phi and the bracket: one plain-words bracket', v4.count('[in plain words: Phi is the fixed function') == 1))
    cases.append(('(a) the squeeze and its jaws: one plain-words bracket', v4.count('[In plain words: one jaw is the region') == 1))
    cases.append(('(a) the surround given its glossary entry, once, in THE CLAIM',
                  v4.count(gl['the surround']) == 1 and gl['the surround'] in P.get('THE CLAIM', '')))
    cases.append(('(a) control: without (a) none of the five present',
                  not any(x in wo['a'] for x in (R.NOT_TSP[1], R.DED[1], 'Phi is the fixed function', 'one jaw is the region', gl['the surround']))))
    # ### (b) exhaustiveness said once
    cases.append(('(b) "complete over its named classes" once, in the "On exhaustiveness" sentence',
                  v4.count('complete over its named classes') == 1 and 'On exhaustiveness: the seven-class catalogue is complete over its named classes' in v4))
    cases.append(('(b) the parenthesis absent', R.EXH_PAREN not in v4))
    cases.append(('(b) control: without (b) the parenthesis present and the statement twice',
                  R.EXH_PAREN in wo['b'] and wo['b'].count('complete over its named classes') == 2))
    # ### (c) the open-premise phrase twice: once in THE CLAIM, once in WHAT IS OPEN, nowhere else
    n = dict((k, len(OPEN_PHRASE.findall(v))) for k, v in P.items())
    cases.append(('(c) the open-premise phrase by part %s' % n, n.get('THE CLAIM') == 1 and n.get('WHAT IS OPEN') == 1 and sum(n.values()) == 2))
    nw = dict((k, len(OPEN_PHRASE.findall(v))) for k, v in Pw['c'].items())
    cases.append(('(c) control: without (c) THE CLAIM carries it twice %s' % nw, nw.get('THE CLAIM') == 2))
    # ### (d) the definitions paragraph at the glossary's one-sentence forms, the glossary named, the lists untouched
    A, Aw = P.get('WHAT THE LOAD-BEARING THEOREMS ASSUME', ''), Pw['d'].get('WHAT THE LOAD-BEARING THEOREMS ASSUME', '')
    forms = [gl['premise'], gl['own evidence'].replace('of a premise: ', ''), gl['HINGE'].replace(' (the entry above)', ''), gl['W-ORD'],
             gl['priced'].replace('of a work-order: ', ''), gl['OPEN_TRAILS']]
    cases.append(('(d) every definition the glossary`s form, verbatim (%d)' % len(forms), all(f.rstrip('.') in A for f in forms)))
    cases.append(('(d) the glossary named', "the programme's glossary's, one sentence each" in A))
    cases.append(('(d) the plain-words brackets that were not glossary forms absent',
                  '[In plain words: own evidence' not in v4 and '[In plain words: a hinge' not in v4))
    ul = lambda h: re.findall(r'<ul>.*</ul>', h, re.S)
    cases.append(('(d) the lists untouched: the status lists byte for byte as without (d)', ul(A) == ul(Aw) and bool(ul(A))))
    cases.append(('(d) control: without (d) the brackets present and the glossary not named',
                  '[In plain words: own evidence' in wo['d'] and "the programme's glossary's" not in wo['d']))
    # ### the carried composer, and the whole
    cases.append(('the carried composer reproduces v3 byte for byte', R.v3_same()))
    cases.append(('no edit leaves NOT READ', 'NOT READ' not in v4))
    k = 0
    for i, (label, ok) in enumerate(cases, 1):
        k += bool(ok)
        print('  (%d) %s ... %s' % (i, label, 'PASS' if ok else 'FAIL'))
    print('  %d of %d PASS' % (k, len(cases)))
    return 0 if k == len(cases) else 1


if __name__ == '__main__':
    sys.exit(main())
