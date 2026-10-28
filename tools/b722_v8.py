# -*- coding: utf-8 -*-
"""b722_v8.py -- STANDING CLAUSES v8, (R332)(8): VERSION 7 UNCHANGED WITH ONE ROW ADDED, THE PROPAGATION READ. Written whole at b722 by the
Write tool. `dry` prints; `write` writes data/standing_clauses_v8.txt (committed by a commit of its own). v7's lines :10-:195 (its sections and
rows (1)-(81)) are copied byte for byte; its head (:1-:9) and closing line (:196) are v7's own and are replaced by v8's; row (82) is quoted from
relay data/b722_ferry.txt :23, the quotation without its marks, checked present in the ferry before anything is written.
"""
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROW82 = ('When the record corrects a statement, every statement naming the same object is read, and each that now reads wrong gets a dated '
         'note beside it; no line is rewritten.')


def main(mode):
    v7 = open(os.path.join(D, 'standing_clauses_v7.txt'), 'rb').read().decode('utf-8')
    L7 = v7.split(NL)
    ferry = open(os.path.join(D, 'b722_ferry.txt'), encoding='utf-8').read().split(NL)
    if ('"%s"' % ROW82) not in ferry[22] or not L7[9].startswith('## LINE 49 OF data/b709_ferry.txt') or not L7[195].startswith('### ### **ROWS 81 ;'):
        sys.exit('### v7 OR THE FERRY NOT AS READ (ferry :23 carries the row: %s ; v7 :10 %r ; v7 :196 %r) -- NOTHING WRITTEN' % (
            ('"%s"' % ROW82) in ferry[22], L7[9][:30], L7[195][:20]))
    body = L7[9:195]                                  # ### v7 :10-:195, byte for byte
    head = ['b722 -- THE STANDING CLAUSES, VERSION 8, WRITTEN UNDER (R332)(8): VERSION 7 UNCHANGED (relay data/standing_clauses_v7.txt, its rows '
            '(1)-(81), its LINE sections and row lines copied byte for byte) WITH (R332)(8)`S ROW, THE PROPAGATION READ, AS ROW (82) (%s)' %
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
            'VERSION: 8',
            'THE CITATION FORM: a ferry names "standing clauses v8" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
            '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
            '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(81) are v7`s, unchanged, under v7`s own section heads. Row (82) is (R332)(8), the author`s',
            '### word of 2026-10-28, the quotation of relay data/b722_ferry.txt :23 without its marks.',
            '### Where a row and an earlier row speak to one object the later row is the version`s reading; no earlier row is edited.', '']
    tail = ['## LINE 23 OF data/b722_ferry.txt -- (R332)(8), THE PROPAGATION READ (the delta of v8)',
            '  (82) STANDING STOP SOURCE (R332)(8) ; first carried in data/b722_ferry.txt under (R332)',
            '      ' + ROW82, '',
            '### ### **ROWS 82 ; v7`S ROWS 81 UNCHANGED ; (R332)(8)`S ROW, THE PROPAGATION READ: WHEN THE RECORD CORRECTS A STATEMENT, EVERY STATEMENT '
            'NAMING THE SAME OBJECT IS READ, EACH THAT NOW READS WRONG GETS A DATED NOTE BESIDE IT, NO LINE REWRITTEN ; VERSION 8.**', '']
    out = NL.join(head + body + tail)
    if NL.join(body) not in out or NL.join(body) != NL.join(L7[9:195]):
        sys.exit('### v7`S BODY NOT CARRIED BYTE FOR BYTE -- NOTHING WRITTEN')
    print(NL.join(head + ['  [v7 :10-:195, %d lines, byte for byte]' % len(body)] + tail))
    if mode != 'write':
        return
    p = os.path.join(D, 'standing_clauses_v8.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write(out.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/standing_clauses_v8.txt')


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
