# -*- coding: utf-8 -*-
"""b757 -- (R367)(8)(i): THE ANSWERS BANK READ CUT BEFORE THE ROOT'S APPENDED SECTION.

The ruling's words (data/b757_ferry.txt :25): "(i) (F5): the check carried into tools/acts/b757.py reads the answers bank cut before the
root's appended section; on b756's bank whole it passes, and on a second RESULT line planted inside the put's own section it fails."
(F5) (:9): "G-COUNT-ROUTE-PRICED failing in both suites on tools/acts/b756.py :946-:947, which wants one RESULT line where the root's answer,
appended by design, makes two (data/b756_author_answers.txt :18, :27)." `record answers` appends a later prompt's answers under a line
opening "## APPENDED BY `record answers` AT" (b756's at :20), and writes no other line so.

  cut(text)      the bank's text before its first line opening "## APPENDED BY "; the whole text where there is none
  results(text)  the RESULT lines of the cut text, each a line opening "RESULT ("
  carried(putj, lines)  the check of tools/acts/b756.py :946-:947, unchanged but for the lines it is handed: the put's json carrying three
                 questions, one RESULT line, three answers each "(Recommended)"

THE CONTROLS, on b756's banks (data/b756_put_1.json, data/b756_author_answers.txt) read whole and on plants made in memory, nothing written
but this tool's bank: (1) the bank whole and uncut: two RESULT lines (:18, :27), the carried check FAILS, as both of b756's suites read it;
(2) the bank whole, cut: one RESULT line (:18), the cut at :20, the carried check PASSES; (3) a second RESULT line planted inside the put's
own section (a copy of :18 inserted at :19): the cut reads two and the carried check FAILS; (4) a text with no appended head: the cut equal
to the whole. Imported by the act's checks (tools/acts/b757.py, G-COUNT-ROUTE-PRICED) for b757's own answers bank.

usage: python -X utf8 -u tools/b757_cut.py [--bank]      the controls; with --bank, data/b757_cut.txt
"""
import io
import json
import os
import re
import sys
import time

RELAY = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(RELAY, 'data')
NL = '\n'
HEAD = '## APPENDED BY '
BANK = os.path.join(D, 'b757_cut.txt')


def cut(text):
    """the text before the first line opening "## APPENDED BY "; the whole where there is none."""
    L = (text or '').split(NL)
    k = next((i for i, l in enumerate(L) if l.startswith(HEAD)), None)
    return NL.join(L if k is None else L[:k])


def cut_line(text):
    """1-based line of the first appended head, or None."""
    return next((i + 1 for i, l in enumerate((text or '').split(NL)) if l.startswith(HEAD)), None)


def results(text):
    return [l for l in cut(text).split(NL) if l.startswith('RESULT (')]


def carried(putj, rl_):
    """tools/acts/b756.py :947, unchanged but for the RESULT lines it is handed."""
    return len((putj or {}).get('questions') or []) == 3 and len(rl_) == 1 and len(re.findall(r'="[^"]*\(Recommended\)"', rl_[0])) == 3


def controls():
    putj = json.load(io.open(os.path.join(D, 'b756_put_1.json'), encoding='utf-8'))
    txt = io.open(os.path.join(D, 'b756_author_answers.txt'), encoding='utf-8').read()
    L = txt.split(NL)
    whole = [l for l in L if l.startswith('RESULT (')]
    at = [i + 1 for i, l in enumerate(L) if l.startswith('RESULT (')]
    planted = NL.join(L[:18] + [L[17]] + L[18:])
    plain = NL.join(L[:19])
    rows = [
        ('(1) b756`s bank whole and uncut: RESULT lines %s at %s ; the carried check %s' % (len(whole), at, 'PASSES' if carried(putj, whole) else 'FAILS'),
         len(whole) == 2 and at == [18, 27] and not carried(putj, whole)),
        ('(2) b756`s bank whole, cut at :%s: RESULT lines %d ; the carried check %s' % (cut_line(txt), len(results(txt)), 'PASSES' if carried(putj, results(txt)) else 'FAILS'),
         cut_line(txt) == 20 and len(results(txt)) == 1 and carried(putj, results(txt))),
        ('(3) a second RESULT line planted inside the put`s own section (:18 copied to :19), cut at :%s: RESULT lines %d ; the carried check %s' % (
            cut_line(planted), len(results(planted)), 'PASSES' if carried(putj, results(planted)) else 'FAILS'),
         cut_line(planted) == 21 and len(results(planted)) == 2 and not carried(putj, results(planted))),
        ('(4) a text with no appended head (b756`s :1-:19): the cut %s the whole' % ('EQUAL TO' if cut(plain) == plain else 'NOT EQUAL TO'),
         cut_line(plain) is None and cut(plain) == plain),
    ]
    return rows


def main(argv):
    rows = controls()
    ok = all(w for _x, w in rows)
    out = ['b757 -- (R367)(8)(i): THE ANSWERS BANK READ CUT BEFORE THE ROOT`S APPENDED SECTION (%s, tools/b757_cut.py)' % time.strftime(
               '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
           '## THE CONTROLS, on data/b756_put_1.json and data/b756_author_answers.txt read whole, the plants made in memory']
    out += ['  %s -> %s' % (w, 'AS WANTED' if g else 'NOT AS WANTED') for w, g in rows]
    out += ['', '### ### **(8)(i): CONTROLS %d OF %d AS WANTED ; ON b756`S BANK WHOLE THE CUT CHECK %s, ON THE PLANTED SECOND RESULT %s.**' % (
        sum(1 for _x, g in rows if g), len(rows), 'PASSES' if rows[1][1] else 'DOES NOT PASS', 'FAILS' if rows[2][1] else 'DOES NOT FAIL')]
    text = NL.join(out) + NL
    print(text)
    if '--bank' in argv:
        with io.open(BANK + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
            f.write(text)
        os.replace(BANK + '.tmp', BANK)
        print('BANKED: data/b757_cut.txt')
    return 0 if ok else 3


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
