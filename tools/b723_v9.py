# -*- coding: utf-8 -*-
"""b723_v9.py -- STANDING CLAUSES v9, (R333)(2)(v): VERSION 8 UNCHANGED WITH ONE ROW ADDED, THE REPEAT RULE. Written whole at b723 by the
Write tool, in tools/b722_v8.py's form. `dry` prints; `write` writes data/standing_clauses_v9.txt (committed by a commit of its own). v8's lines
:10-:199 (v7's sections and rows (1)-(81), v8's section and row (82), the blank after it) are copied byte for byte; its head (:1-:9) and closing
line (:200) are v8's own and are replaced by v9's; row (83) is quoted from relay data/b723_ferry.txt :15, the quotation without its marks,
checked present in the ferry before anything is written.
"""
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROW83 = ('A defect of a class a previous act recorded is met with a repair, its control printed, or with a ruling line saying why not; the '
         'closing prints the count of repeats, and a class that repeats in three acts running is the next act\'s opening component.')


def main(mode):
    v8 = open(os.path.join(D, 'standing_clauses_v8.txt'), 'rb').read().decode('utf-8')
    L8 = v8.split(NL)
    ferry = open(os.path.join(D, 'b723_ferry.txt'), encoding='utf-8').read().split(NL)
    if ('"%s"' % ROW83) not in ferry[14] or not L8[9].startswith('## LINE 49 OF data/b709_ferry.txt') \
            or not L8[195].startswith('## LINE 23 OF data/b722_ferry.txt') or L8[198] != '' or not L8[199].startswith('### ### **ROWS 82 ;'):
        sys.exit('### v8 OR THE FERRY NOT AS READ (ferry :15 carries the row: %s ; v8 :10 %r ; v8 :196 %r ; v8 :199 %r ; v8 :200 %r) -- NOTHING WRITTEN' % (
            ('"%s"' % ROW83) in ferry[14], L8[9][:30], L8[195][:30], L8[198], L8[199][:20]))
    body = L8[9:199]                                  # ### v8 :10-:199, byte for byte
    head = ['b723 -- THE STANDING CLAUSES, VERSION 9, WRITTEN UNDER (R333)(2)(v): VERSION 8 UNCHANGED (relay data/standing_clauses_v8.txt, its rows '
            '(1)-(82), its LINE sections and row lines copied byte for byte) WITH (R333)(2)(v)`S ROW, THE REPEAT RULE, AS ROW (83) (%s)' %
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
            'VERSION: 9',
            'THE CITATION FORM: a ferry names "standing clauses v9" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
            '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
            '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(82) are v8`s, unchanged, under v8`s own section heads. Row (83) is (R333)(2)(v), the author`s',
            '### ruling (R333), the quotation of relay data/b723_ferry.txt :15 without its marks.',
            '### Where a row and an earlier row speak to one object the later row is the version`s reading; no earlier row is edited.', '']
    tail = ['## LINE 15 OF data/b723_ferry.txt -- (R333)(2)(v), THE REPEAT RULE (the delta of v9)',
            '  (83) STANDING STOP SOURCE (R333)(2)(v) ; first carried in data/b723_ferry.txt under (R333)',
            '      ' + ROW83, '',
            '### ### **ROWS 83 ; v8`S ROWS 82 UNCHANGED ; (R333)(2)(v)`S ROW, THE REPEAT RULE: A DEFECT OF A CLASS A PREVIOUS ACT RECORDED IS MET WITH A '
            'REPAIR, ITS CONTROL PRINTED, OR A RULING LINE SAYING WHY NOT; THE CLOSING PRINTS THE COUNT OF REPEATS; A CLASS REPEATING IN THREE ACTS '
            'RUNNING IS THE NEXT ACT`S OPENING COMPONENT ; VERSION 9.**', '']
    out = NL.join(head + body + tail)
    if NL.join(body) not in out or NL.join(body) != NL.join(L8[9:199]):
        sys.exit('### v8`S BODY NOT CARRIED BYTE FOR BYTE -- NOTHING WRITTEN')
    print(NL.join(head + ['  [v8 :10-:199, %d lines, byte for byte]' % len(body)] + tail))
    if mode != 'write':
        return
    p = os.path.join(D, 'standing_clauses_v9.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(out.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/standing_clauses_v9.txt')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
