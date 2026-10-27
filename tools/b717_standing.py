# -*- coding: utf-8 -*-
"""b717_standing.py -- (R327)(2): THE STANDING CLAUSES AT v6, written at step zero as data/standing_clauses_v6.txt -- v5 unchanged (its 79 rows,
its LINE sections and its row lines copied from data/standing_clauses_v5.txt byte for byte) with (R327)(2)'s row appended as row (80), CLAIM AND
CLOSE, the ruling's own words cut from (R327)(2) as banked (relay data/b717_ferry.txt :9-:13), joined into one clause line.
Carried from tools/b716_standing.py by diff (data/b717_carry_standing.txt) and rewritten whole by the Write tool: b716's tool was b714's v5
writer carried unused (b716 wrote no standing clauses); this act's writer appends one row to v5 and keeps v5's bytes.
### THE CUT: (R327)(2) at :9 of the banked ferry, from "(2) CLAIM AND CLOSE" to the paragraph's end at :13 ("and prints the counter."), its
### lines :9, :11, :12, :13 joined by single spaces; the cut printed and checked against the transcript's ferry (tools/b717_citation.py ferry,
### equal True) before the write.
### Routes: `write [dry]` -> data/standing_clauses_v6.txt ; `control [dry]` -> data/b717_standing_control.txt (.json). Writes only those banks.
### THE CONTROL: v6 parses to 80 rows; rows (1)-(79) equal to v5's parse row by row and v5's body bytes found in v6 whole; row (80)'s clause
### equal to the cut; the NEG alterations -- one byte of row (12) changed in a copy, and row (80) dropped in a copy -- each read NOT EQUAL.
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

V5, BANK, FERRY = 'standing_clauses_v5.txt', 'standing_clauses_v6.txt', 'b717_ferry.txt'
ROW_HEAD = '  (%d) STANDING STOP SOURCE (R327)(2) ; first carried in data/b717_ferry.txt under (R327)'
ROW_RE = re.compile(r'^  \((\d+)\) (\S+) (\S+) (.*)$')


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


def body(v5):
    """v5's body: from its first `## LINE` section to the line before its foot (`### ### **ROWS`), byte for byte."""
    L = v5.split(NL)
    s = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    e = next(i for i, l in enumerate(L) if l.startswith('### ### **ROWS'))
    while e > s and not L[e - 1].strip():
        e -= 1
    return NL.join(L[s:e])


def cut():
    """(R327)(2) as banked: ferry :9 from "(2) CLAIM AND CLOSE" and :11-:13, joined."""
    F = rd(os.path.join(D, FERRY)).split(NL)
    if not F[8].startswith('(2) CLAIM AND CLOSE') or not F[12].endswith('and prints the counter.'):
        sys.exit('### THE CUT DOES NOT STAND AT :9-:13 OF data/b717_ferry.txt -- NOTHING WRITTEN')
    return ' '.join(x.strip() for x in (F[8], F[10], F[11], F[12]))


def compose():
    v5 = rd(os.path.join(D, V5))
    rows5 = parse(v5)
    n = len(rows5) + 1
    clause = cut()
    L = ['b717 -- THE STANDING CLAUSES, VERSION 6, WRITTEN ONCE AT STEP ZERO UNDER (R327)(2): VERSION 5 UNCHANGED (relay data/standing_clauses_v5.txt, its rows '
         '(1)-(%d), its LINE sections and row lines copied byte for byte) WITH (R327)(2)`S ROW, CLAIM AND CLOSE, AS ROW (%d) (%s)' % (n - 1, n, utc()), '',
         'VERSION: 6',
         'THE CITATION FORM: a ferry names "standing clauses v6" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v5`s, unchanged, under v5`s own section heads. Row (%d) is (R327)(2), CLAIM AND' % (n - 1, n),
         '### CLOSE, cut from relay data/b717_ferry.txt :9-:13 and its four lines joined by single spaces. Where a row and an earlier row speak to one',
         '### object the later row is the version`s reading; no earlier row is edited.', '',
         body(v5), '',
         '## LINES 9-13 OF data/b717_ferry.txt -- (R327)(2), CLAIM AND CLOSE (the delta of v6)',
         ROW_HEAD % n,
         '      ' + clause, '',
         '### ### **ROWS %d ; v5`S ROWS %d UNCHANGED ; (R327)(2)`S ROW, CLAIM AND CLOSE: EVERY EVENT AND DEFECT FROM b716`S CORRIGENDUM ON TAGGED CLAIM OR CLOSE, '
         'EVERY ARM TAGGED IN data/arm_tags.json, THE CLOSING PRINTING THE CLAIM ARMS` FIGURE AND THE COUNTER ; VERSION 6.**' % (n, n - 1)]
    return NL.join(L) + NL, clause, rows5


def write(*a):
    text, clause, rows5 = compose()
    if 'dry' in a:
        print(text[:1200])
        print('...')
        print(NL.join(text.split(NL)[-6:]))
        return
    p = os.path.join(D, BANK)
    if os.path.exists(p):
        sys.exit('### data/%s EXISTS -- WRITTEN ONCE AT STEP ZERO; NOTHING WRITTEN' % BANK)
    MEM.guard_path('b717', p, None)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('  data/%s written: rows %d ; v5`s rows %d ; %d bytes' % (BANK, len(parse(text)), len(rows5), len(text.encode('utf-8'))))


def _check(v6, v5, clause):
    r6, r5 = parse(v6), parse(v5)
    same = len(r6) == len(r5) + 1 and r6[:len(r5)] == r5
    whole = body(v5) in v6
    last = bool(r6) and r6[-1][0] == len(r5) + 1 and r6[-1][2] == '      ' + clause
    return same, whole, last


def control(*a):
    v5, v6 = rd(os.path.join(D, V5)), rd(os.path.join(D, BANK))
    clause = cut()
    L = ['b717 -- THE CONTROL OF data/standing_clauses_v6.txt ((R327)(2)) (%s)' % utc(), '',
         '### v6 against v5 and the cut: rows (1)-(79) equal row by row, v5`s body found whole, row (80) the cut; two NEG alterations each NOT EQUAL.']
    same, whole, last = _check(v6, v5, clause)
    L.append('  THE BANK: rows %d ; v5`s rows equal %s ; v5`s body whole %s ; row (80) the cut %s' % (len(parse(v6)), same, whole, last))
    rows = parse(v6)
    alt1 = v6.replace(rows[11][2], rows[11][2][:-1] + ('X' if rows[11][2][-1] != 'X' else 'Y'), 1) if len(rows) > 11 else v6
    a1 = _check(alt1, v5, clause)
    alt2 = v6.replace(rows[-1][1] + NL + rows[-1][2] + NL, '', 1) if rows else v6
    a2 = _check(alt2, v5, clause)
    neg1, neg2 = not all(a1), not all(a2)
    L.append('  NEG (one byte of row (12) changed in a copy): %s -> %s' % (a1, 'NOT EQUAL, AS WANTED' if neg1 else '### EQUAL -- THE CONTROL CANNOT FIRE'))
    L.append('  NEG (row (80) dropped in a copy): %s -> %s' % (a2, 'NOT EQUAL, AS WANTED' if neg2 else '### EQUAL -- THE CONTROL CANNOT FIRE'))
    ok = same and whole and last and neg1 and neg2
    L += ['', '### ### **ROWS %d ; v5 UNCHANGED %s ; ROW (80) THE CUT %s ; NEG 2 OF 2 FAILING AS WANTED %s ; CONTROL AS WANTED %s.**' % (
        len(rows), same and whole, last, neg1 and neg2, ok)]
    if 'dry' in a:
        print(NL.join(L))
        return
    for nm, data in (('b717_standing_control.txt', NL.join(L) + NL),
                     ('b717_standing_control.json', json.dumps(dict(at=utc(), rows=len(rows), v5_unchanged=same and whole, row80=last, neg=[neg1, neg2], ok=ok), indent=1) + NL)):
        q = os.path.join(D, nm)
        MEM.guard_path('b717', q, None)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data.encode('utf-8'))
        os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'write': write, 'control': control}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b717_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
