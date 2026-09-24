# -*- coding: utf-8 -*-
"""b505_annotate.py -- THE ANNOTATIONS OF (R115)(1) AND (2). ### `python tools/b505_annotate.py`

### ONE note APPENDED to each of four prior files; the prior bytes are a byte-for-byte prefix of the result,
### proved and printed. ### A second run finds its note present and writes nothing.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
MARK = 'ANNOTATION APPENDED AT b505 UNDER (R115)'
C2 = json.loads(io.open(os.path.join(D, 'b505_c2_results.json'), encoding='utf-8').read())

HEAD = ['', '-' * 100, '### %s%s, 2026-09-23. ### THE TEXT ABOVE IS UNEDITED.', '-' * 100]
SHORT = ('the Epstein bank it summed, `b326_epstein_zeros.json` (146 on-line zeros and 2 off-line), is short of its '
         'own count below height 150: b505`s whole-strip argument-principle count is %d against the bank`s %d '
         '(146 + 2 x 2), so the bank lacks %d.' % (C2['total'], C2['bank_on'] + 4, C2['lacks_strip']))


def margins_note(act, kernels):
    return HEAD[:2] + [HEAD[2] % (MARK, '(1)')] + HEAD[3:] + [
        '### ### **THE EPSTEIN MARGINS OF %s ARE UNVERIFIED.** ### They were read under %s,' % (act, kernels),
        '### which does not close the explicit formula of Z_Q0 at any cell (b326; b504 Component 4: no cell verifies',
        '### under either kernel); ### and ' + SHORT,
        '### A residual read against an incomplete bank is a verdict on nothing. ### The monograph`s step (9)',
        '### Epstein sentence keeps its NO BANK status. ### The control of record is Q0 = x^2 + xy + 6y^2,',
        '### discriminant -23, class number 3.', '-' * 100]


NOTES = {
    'b477_components.txt': margins_note('b477', 'b325`s kernel `kernel_q`'),
    'b502_components.txt': margins_note('b502', 'b325`s kernel `kernel_q`'),
    'b504_components.txt': margins_note('b504', 'b325`s kernel and b326`s derived kernel, neither verifying at any cell'),
    'b502_ferry.txt': HEAD[:2] + [HEAD[2] % (MARK, '(2)')] + HEAD[3:] + [
        '### ### **THE FORM "x^2 + 5y^2" NAMED IN COMPONENT 4 ABOVE IS NOT A FORM THE RECORD HOLDS.** ### The Epstein',
        '### control of record is Q0 = x^2 + xy + 6y^2, discriminant -23, class number 3 -- `b325_epstein.py`',
        '### (DISC = 23; `rep_counts` on x*x + x*y + 6*y*y) and b326`s bank. ### b502`s run used that form, not the',
        '### one named here. ### The navigator`s text above is preserved verbatim; this note is appended under',
        '### (R115)(2).', '-' * 100],
}


def main():
    out = []
    for name, lines in NOTES.items():
        p = os.path.join(D, name)
        before = open(p, 'rb').read()
        if MARK.encode('utf-8') in before:
            out.append(dict(file=name, written=0, note='ALREADY PRESENT'))
            continue
        add = (NL.join(lines) + NL).encode('utf-8')
        open(p, 'ab').write(add)
        after = open(p, 'rb').read()
        bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
        out.append(dict(file=name, written=len(after) - len(before), prefix=after[:len(before)] == before,
                        removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), marks=after.decode('utf-8').count(MARK)))
    for o in out:
        print('  %-22s %s' % (o['file'], o))
    io.open(os.path.join(D, 'b505_annotations.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)


if __name__ == '__main__':
    main()
