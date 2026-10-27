# -*- coding: utf-8 -*-
"""b718_standing.py -- (R328)(3): THE STANDING CLAUSES AT v7, written at step zero as data/standing_clauses_v7.txt -- v6 unchanged (its 80 rows,
its LINE sections and its row lines copied from data/standing_clauses_v6.txt byte for byte) with (R328)(3)'s row appended as row (81), THE
STANDING LINE OF CONSISTENCY, tagged CLAIM, the author's words cut from (R328)(3) as banked (relay data/b718_ferry.txt :11), the quotation alone.
Carried from tools/b717_standing.py by diff (data/b718_carry_standing.txt) and rewritten whole by the Write tool: b717's tool was the v6 writer
(v5 plus one row); this act's writer appends one row to v6 and keeps v6's bytes, the same form one version on.
### THE CUT: (R328)(3) at :11 of the banked ferry, the quotation from "Every statement is correct" to "by choosing a side.", its marks dropped;
### the cut printed and checked against the transcript's ferry (tools/b718_citation.py ferry, equal True) before the write.
### Routes: `write [dry]` -> data/standing_clauses_v7.txt ; `control [dry]` -> data/b718_standing_control.txt (.json). Writes only those banks.
### THE CONTROL: v7 parses to 81 rows; rows (1)-(80) equal to v6's parse row by row and v6's body bytes found in v7 whole; row (81)'s clause
### equal to the cut and its head tagged CLAIM; the NEG alterations -- one byte of row (12) changed in a copy, and row (81) dropped in a copy --
### each read NOT EQUAL.
"""
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import act_membrane as MEM  # noqa: E402
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PREVB, BANK, FERRY = 'standing_clauses_v6.txt', 'standing_clauses_v7.txt', 'b718_ferry.txt'
ROW_HEAD = '  (%d) STANDING STOP SOURCE (R328)(3) ; first carried in data/b718_ferry.txt under (R328) ; CLAIM'
ROW_RE = re.compile(r'^  \((\d+)\) (\S+) (\S+) (.*)$')
Q_OPEN, Q_CLOSE = '"Every statement is correct', 'by choosing a side."'


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def parse(text):
    """rows of a standing clauses bank: [(n, head line, clause line)], a row its `  (n) KIND SEP ...` line and the clause on the next line."""
    L = text.split(NL)
    out = []
    for i, l in enumerate(L):
        m = ROW_RE.match(l)
        if m and i + 1 < len(L) and L[i + 1].startswith('      '):
            out.append((int(m.group(1)), l, L[i + 1]))
    return out


def body(prev):
    """the previous version's body: from its first `## LINE` section to the line before its foot (`### ### **ROWS`), byte for byte."""
    L = prev.split(NL)
    s = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    e = next(i for i, l in enumerate(L) if l.startswith('### ### **ROWS'))
    while e > s and not L[e - 1].strip():
        e -= 1
    return NL.join(L[s:e])


def cut():
    """(R328)(3) as banked: ferry :11, the quotation between its marks."""
    F = rd(os.path.join(D, FERRY)).split(NL)
    l = F[10] if len(F) > 10 else ''
    i, j = l.find(Q_OPEN), l.find(Q_CLOSE)
    if not l.startswith('(3) THE STANDING LINE') or i < 0 or j < i or l.count(Q_OPEN) != 1:
        sys.exit('### THE CUT DOES NOT STAND AT :11 OF data/b718_ferry.txt -- NOTHING WRITTEN')
    return l[i + 1:j + len(Q_CLOSE) - 1]


def compose():
    prev = rd(os.path.join(D, PREVB))
    rowsp = parse(prev)
    n = len(rowsp) + 1
    clause = cut()
    L = ['b718 -- THE STANDING CLAUSES, VERSION 7, WRITTEN ONCE AT STEP ZERO UNDER (R328)(3): VERSION 6 UNCHANGED (relay data/standing_clauses_v6.txt, its rows '
         '(1)-(%d), its LINE sections and row lines copied byte for byte) WITH (R328)(3)`S ROW, THE STANDING LINE OF CONSISTENCY, AS ROW (%d), TAGGED CLAIM (%s)' % (n - 1, n, utc()), '',
         'VERSION: 7',
         'THE CITATION FORM: a ferry names "standing clauses v7" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v6`s, unchanged, under v6`s own section heads. Row (%d) is (R328)(3), the author`s' % (n - 1, n),
         '### word of 2026-10-27, the quotation of relay data/b718_ferry.txt :11 without its marks, tagged CLAIM on its head line as (R328)(3) orders.',
         '### Where a row and an earlier row speak to one object the later row is the version`s reading; no earlier row is edited.', '',
         body(prev), '',
         '## LINE 11 OF data/b718_ferry.txt -- (R328)(3), THE STANDING LINE OF CONSISTENCY (the delta of v7)',
         ROW_HEAD % n,
         '      ' + clause, '',
         '### ### **ROWS %d ; v6`S ROWS %d UNCHANGED ; (R328)(3)`S ROW, THE STANDING LINE OF CONSISTENCY, TAGGED CLAIM: EVERY STATEMENT READ AGAINST ITS SOURCE AND '
         'AGAINST EACH STATEMENT OF THE RECORD NAMING THE SAME OBJECT, A DISAGREEMENT PRINTED FOR THE AUTHOR AND CARRIED ; VERSION 7.**' % (n, n - 1)]
    return NL.join(L) + NL, clause, rowsp


def write(*a):
    text, clause, rowsp = compose()
    if 'dry' in a:
        print(text[:1400])
        print('...')
        print(NL.join(text.split(NL)[-6:]))
        return
    p = os.path.join(D, BANK)
    if os.path.exists(p):
        sys.exit('### data/%s EXISTS -- WRITTEN ONCE AT STEP ZERO; NOTHING WRITTEN' % BANK)
    MEM.guard_path('b718', p, None)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  data/%s written: rows %d ; v6`s rows %d ; %d bytes' % (BANK, len(parse(text)), len(rowsp), len(text.encode('utf-8'))))


def _check(v7, v6, clause):
    r7, r6 = parse(v7), parse(v6)
    same = len(r7) == len(r6) + 1 and r7[:len(r6)] == r6
    whole = body(v6) in v7
    last = bool(r7) and r7[-1][0] == len(r6) + 1 and r7[-1][2] == '      ' + clause and r7[-1][1].endswith('; CLAIM')
    return same, whole, last


def control(*a):
    v6, v7 = rd(os.path.join(D, PREVB)), rd(os.path.join(D, BANK))
    clause = cut()
    rows = parse(v7)
    L = ['b718 -- THE CONTROL OF data/standing_clauses_v7.txt ((R328)(3)) (%s)' % utc(), '',
         '### v7 against v6 and the cut: rows (1)-(%d) equal row by row, v6`s body found whole, row (%d) the cut tagged CLAIM; two NEG alterations each NOT EQUAL.' % (
             len(rows) - 1, len(rows))]
    same, whole, last = _check(v7, v6, clause)
    L.append('  THE BANK: rows %d ; v6`s rows equal %s ; v6`s body whole %s ; row (%d) the cut, tagged CLAIM %s' % (len(rows), same, whole, len(rows), last))
    alt1 = v7.replace(rows[11][2], rows[11][2][:-1] + ('X' if rows[11][2][-1] != 'X' else 'Y'), 1) if len(rows) > 11 else v7
    a1 = _check(alt1, v6, clause)
    alt2 = v7.replace(rows[-1][1] + NL + rows[-1][2] + NL, '', 1) if rows else v7
    a2 = _check(alt2, v6, clause)
    neg1, neg2 = not all(a1), not all(a2)
    L.append('  NEG (one byte of row (12) changed in a copy): %s -> %s' % (a1, 'NOT EQUAL, AS WANTED' if neg1 else '### EQUAL -- THE CONTROL CANNOT FIRE'))
    L.append('  NEG (row (%d) dropped in a copy): %s -> %s' % (len(rows), a2, 'NOT EQUAL, AS WANTED' if neg2 else '### EQUAL -- THE CONTROL CANNOT FIRE'))
    ok = same and whole and last and neg1 and neg2
    L += ['', '### ### **ROWS %d ; v6 UNCHANGED %s ; ROW (%d) THE CUT, TAGGED CLAIM %s ; NEG 2 OF 2 FAILING AS WANTED %s ; CONTROL AS WANTED %s.**' % (
        len(rows), same and whole, len(rows), last, neg1 and neg2, ok)]
    if 'dry' in a:
        print(NL.join(L))
        return
    for nm, data in (('b718_standing_control.txt', NL.join(L) + NL),
                     ('b718_standing_control.json', json.dumps(dict(at=utc(), rows=len(rows), v6_unchanged=same and whole, row81=last, neg=[neg1, neg2], ok=ok), indent=1) + NL)):
        q = os.path.join(D, nm)
        MEM.guard_path('b718', q, None)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'write': write, 'control': control}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b718_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
