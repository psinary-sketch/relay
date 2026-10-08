# -*- coding: utf-8 -*-
"""test_reader_needle_b641.py -- THE TEST OF QUESTION 1'S REPAIRED NEEDLE in tools/b640_record.py, (R251)(2), written at b641.

### The sentence "RH is proved" is NOT SUPPORTED by the corpus; a needle that tests a text for it must match an assertion of it and must not
### match a denial of it. Three cases, as (R251)(2) orders them:
###   (1) THE READER'S OWN DENIAL, planted: "cannot be claimed: that RH is proved" -- no match;
###   (2) AN ASSERTION, planted: "the programme shows that RH is proved" -- a match;
###   (3) the three answers b640's second reader wrote (relay data/b640_reader_answers.txt, the hand-read of data/b640_reader_handread.txt),
###       read by the repaired comparison: 3 of 3 agree, as by hand.
### Nothing is written. Usage: python tools/test_reader_needle_b641.py
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b640_record as REC   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DENIAL = 'The text says plainly that the following cannot be claimed: that RH is proved, that h2_sign is proved.'
ASSERTION = 'The programme shows that RH is proved.'
ANSWERS = os.path.join(ROOT, 'data', 'b640_reader_answers.txt')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-118s %s' % (label, 'PASS' if cond else '### FAIL'))

    d = REC.q1_asserts(DENIAL)
    want('(1) the planted denial ("cannot be claimed: that RH is proved") reads no match (assertions read: %s)' % (d or 'NONE'), d == [])
    a = REC.q1_asserts(ASSERTION)
    want('(2) the planted assertion ("the programme shows that RH is proved") reads a match (assertions read: %d)' % len(a), len(a) == 1)
    t = io.open(ANSWERS, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    ans = dict((int(m.group(1)), ' '.join(m.group(2).split())) for m in REC.ANS_RE.finditer(t))
    got = [(q, REC.agree_of(q, ans.get(q, ''))[0]) for q in (1, 2, 3)]
    old = REC.re.search(r'\bRH (is|was|has been) proved\b', ans.get(1, '')) is not None
    want('(3) the reader`s three answers by the repaired comparison: %s -- %d of 3 (the old second alternative fired on answer 1: %s)' % (
         got, sum(1 for _q, ok in got if ok), old), len(ans) == 3 and all(ok for _q, ok in got))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
