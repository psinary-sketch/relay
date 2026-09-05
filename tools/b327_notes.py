# -*- coding: utf-8 -*-
"""b327_notes.py -- THE ONE CHECKABLE FACT IN THE CUBIT NOTE, CHECKED BEFORE IT IS FILED.

### ### **THE NOTE SAYS:** ### each of the 256 elementary rules is a function on `(Z/2)^3`; rule 110's
### one-set is a five-point subset of the Fano plane's seven points containing two of its seven lines.
### ### **THIS TOOL COUNTS BOTH**, from the rule's binary expansion and the Fano plane's own definition
### (points: the seven nonzero vectors of `(Z/2)^3`; lines: the seven triples `{a, b, a+b}`).
### ### **IF THE COUNTS ARE NOT FIVE AND TWO THE NOTE IS FILED WITH THE MEASURED COUNTS** -- the
### registration, section (4), says so before this file ran.

### ### **WHAT IT DOES NOT DO:** ### it does not answer the note's question (which Fano subsets define
### universal rules); it does not touch the corpus's cubit; it makes no claim.
"""
import io
import itertools
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rule_table(k):
    """### WOLFRAM'S CONVENTION: bit `i` of `k` is the output on the neighbourhood whose binary value is `i`."""
    return {(a, b, c): (k >> (4 * a + 2 * b + c)) & 1 for a in (0, 1) for b in (0, 1) for c in (0, 1)}


def fano_lines():
    pts = [p for p in itertools.product((0, 1), repeat=3) if any(p)]
    lines = set()
    for a in pts:
        for b in pts:
            if a < b:
                c = tuple((x + y) % 2 for x, y in zip(a, b))
                lines.add(frozenset([a, b, c]))
    return pts, lines


def one_set(k):
    return frozenset(nb for nb, v in rule_table(k).items() if v == 1)


def count(k):
    pts, lines = fano_lines()
    S = one_set(k)
    S_fano = frozenset(p for p in S if any(p))
    inside = [L for L in lines if L <= S_fano]
    return S, S_fano, inside, pts, lines


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b327_notes.py -- RULE 110 ON THE FANO PLANE. ### A COUNT, NOT A CLAIM.')
    rec('=' * 100)
    pts, lines = fano_lines()
    rec('  Fano points (nonzero vectors of (Z/2)^3) : %d ; Fano lines ({a, b, a+b}) : %d' % (len(pts), len(lines)))
    # ### fixtures: rule 0 has an empty one-set (0 lines); rule 255 has all eight (7 lines); rule 150 (a+b+c) has 4 points, 0 lines
    fx = [(0, 0, 0), (255, 7, 7), (150, 4, 0)]
    okf = True
    for k, npts, nl in fx:
        S, Sf, ins, _p, _l = count(k)
        good = (len(Sf) == npts and len(ins) == nl)
        okf = okf and good
        rec('  fixture rule %3d : Fano points %d (expect %d), lines inside %d (expect %d)  %s' % (k, len(Sf), npts, len(ins), nl, 'PASS' if good else '### FAIL ###'))
    S, Sf, ins, _p, _l = count(110)
    rec('  rule 110 table    : %s' % ' '.join('%d%d%d->%d' % (a, b, c, v) for (a, b, c), v in sorted(rule_table(110).items(), reverse=True)))
    rec('  rule 110 one-set  : %s  (%d neighbourhoods; 000 is %s in it)' % (sorted(S, reverse=True), len(S), 'IN' if (0, 0, 0) in S else 'not'))
    rec('  ### FANO POINTS IN THE ONE-SET : %d' % len(Sf))
    rec('  ### FANO LINES INSIDE IT       : %d  %s' % (len(ins), sorted(sorted(L) for L in ins)))
    five_two = (len(Sf) == 5 and len(ins) == 2)
    rec('  ### THE ORDER\'S NUMBERS (five points, two lines) : %s' % ('AS STATED' if five_two else '### NOT AS STATED -- filed with the measured counts ###'))
    rec('  ### (rule 110 is a function on (Z/2)^3 with 000 -> 0, so its one-set lies inside the Fano plane\'s point set.)')
    rec('=' * 100)
    rec_out = dict(points=len(Sf), lines=len(ins), lines_list=[sorted(L) for L in ins], one_set=sorted(S, reverse=True),
                   as_stated=five_two, fixtures_pass=okf)
    io.open(os.path.join(D, 'b327_notes.json'), 'w', encoding='utf-8', newline='\n').write(json.dumps(rec_out, indent=1) + '\n')
    io.open(os.path.join(D, 'b327_notes_run.txt'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
    return 0 if okf else 1


if __name__ == '__main__':
    sys.exit(main())
