# -*- coding: utf-8 -*-
"""b711_standing.py -- (R321)(2): THE STANDING CLAUSES AT v2, written at step zero as data/standing_clauses_v2.txt -- v1 unchanged (its 51 rows
copied from data/standing_clauses_v1.txt byte for byte, its three LINE sections and its row lines as banked) with the four deltas appended as
numbered rows (52)-(55), each delta the ruling's own words cut from (R321)(2) as banked (relay data/b711_ferry.txt :9), its control the ruling's
own clause within it; and the control: v2's rows read back by b710's parser (tools/b710_standing.py parse), its first 51 equal to v1's row for
row, each delta equal to its span of the ferry, the version line 2, a NEG copy with one delta altered differing.

### THE CUT OF THE DELTAS: (R321)(2) at :9 of the banked ferry, from "(i) THE EVENTS SECTION" to the next numeral's head ("(ii) THE MEMBRANE",
### "(iii) ARMS READ STRUCTURE", "(iv) CONTROLS THAT CAN FAIL") and the last to the sentence "The other b710 items repaired at carry time" (the
### item repairs are the carry's, not rows of the clauses). Each row: KIND STANDING (carried by version from b712), SEP STOP (the deltas
### re-assemble as the ruling's sentences joined by ". " -- the last END), TAG SOURCE (R321)(2)(i)..(iv).
### Routes: `write [dry]` -> data/standing_clauses_v2.txt ; `control [dry]` -> data/b711_standing_control.txt (.json). Writes only those banks.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b710_standing as S1   # noqa: E402  ### b710's parser and re-assembly, imported unchanged

NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

V1, BANK, FERRY, FLINE = 'standing_clauses_v1.txt', 'standing_clauses_v2.txt', 'b711_ferry.txt', 9
HEADS = ('(i) THE EVENTS SECTION', '(ii) THE MEMBRANE', '(iii) ARMS READ STRUCTURE', '(iv) CONTROLS THAT CAN FAIL')
STOP = ' The other b710 items repaired at carry time'
NUMERALS = ('i', 'ii', 'iii', 'iv')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def deltas():
    """[(numeral, text)] -- the four deltas verbatim from the banked ferry's :9, each ending at its full stop."""
    line = S1.rd(FERRY).split(NL)[FLINE - 1]
    if not line.startswith('(2) THE FOUR RECURRING REACTIONS'):
        sys.exit('### THE BANKED FERRY`S :%d IS NOT (R321)(2) -- NOTHING WRITTEN' % FLINE)
    idx = [line.find(h) for h in HEADS] + [line.find(STOP)]
    if min(idx) < 0 or idx != sorted(idx):
        sys.exit('### A DELTA`S HEAD OR THE STOP NOT FOUND IN ORDER (%s) -- NOTHING WRITTEN' % idx)
    return [(NUMERALS[k], line[idx[k]:idx[k + 1]].strip()) for k in range(4)]


def v1_body():
    """v1's lines from its first LINE section to its last row (the head and the verdict line excluded), byte for byte."""
    L = S1.rd(V1).split(NL)
    a = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    b = max(i for i, l in enumerate(L) if l.startswith('      '))
    return L[a:b + 1]


def text_of():
    dl = deltas()
    body = v1_body()
    rows1 = S1.parse(S1.rd(V1))
    n0 = rows1[-1][0]
    L = ['b711 -- THE STANDING CLAUSES, VERSION 2, WRITTEN ONCE AT STEP ZERO UNDER (R321)(2): VERSION 1 UNCHANGED (relay data/standing_clauses_v1.txt, its rows (1)-(%d) '
         'copied byte for byte) WITH THE FOUR DELTAS APPENDED AS ROWS (%d)-(%d) (%s)' % (n0, n0 + 1, n0 + len(dl), utc()), '',
         'VERSION: 2',
         'THE CITATION FORM: a ferry names "standing clauses v2" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v1`s, unchanged. Rows (%d)-(%d) are (R321)(2)`s four deltas, each the ruling`s own' % (n0, n0 + 1, n0 + len(dl)),
         '### words cut from relay data/b711_ferry.txt :9, each carrying its control in its own clause ("control: ..."); the item repairs of the same',
         '### paragraph (the head-line builder, G-SEALED-AFTER-COMPONENTS, the answer check) are the carry`s and are not rows. Where a delta and a v1 row',
         '### speak to one object the later row is the version`s reading; no v1 row is edited.', '']
    L += body
    L += ['', '## LINE %d OF data/b711_ferry.txt -- (R321)(2), the four recurring reactions repaired as structure (the deltas of v2)' % FLINE]
    for k, (num, t) in enumerate(dl):
        L.append('  (%d) STANDING %s SOURCE (R321)(2)(%s) ; first carried in data/b711_ferry.txt under (R321)' % (n0 + 1 + k, 'STOP' if k < len(dl) - 1 else 'END', num))
        L.append('      ' + t)
    L += ['', '### ### **ROWS %d ; v1`S ROWS %d UNCHANGED ; DELTAS %d (THE EVENTS SECTION, THE MEMBRANE, ARMS READ STRUCTURE, CONTROLS THAT CAN FAIL), EACH WITH ITS '
          'CONTROL ; VERSION 2.**' % (n0 + len(dl), n0, len(dl))]
    return L


def _membrane(p):
    """(R321)(2)(ii), standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    import b711_record as REC
    MEM.guard_path('b711', p, REC.R.ROOT_EXCLUDE)


def write(*a):
    L = text_of()
    if 'dry' in a:
        print(NL.join(L[:10] + L[-12:]))
        return
    p = os.path.join(D, BANK)
    import subprocess
    tracked = subprocess.run(['git', '-C', ROOT, 'ls-files', '--error-unmatch', 'data/' + BANK], capture_output=True).returncode == 0
    if tracked or os.path.exists(p):
        sys.exit('### data/%s EXISTS%s -- A VERSION IS WRITTEN ONCE; NOTHING WRITTEN' % (BANK, ' AND IS COMMITTED' if tracked else ''))
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])


def control(*a):
    v1, v2 = S1.rd(V1), S1.rd(BANK)
    r1, r2 = S1.parse(v1), S1.parse(v2)
    dl = deltas()
    n0 = len(r1)
    first_equal = r2[:n0] == r1
    v1_lines_equal = all(l in v2.split(NL) for l in v1_body())
    dres = []
    for k, (num, t) in enumerate(dl):
        row = r2[n0 + k] if len(r2) > n0 + k else None
        dres.append(dict(n=n0 + 1 + k, delta=num, equal=bool(row) and row[4] == t, control_in=bool(row) and 'control:' in row[4] or (bool(row) and 'given a control that fails' in row[4]),
                         chars=len(t)))
    neg = v2.replace('refuses to write once the act’s root is appended', 'writes once the act’s root is appended', 1)
    neg_rows = S1.parse(neg)
    neg_equal = len(neg_rows) > n0 + 1 and neg_rows[n0 + 1][4] == dl[1][1]
    ver = re.search(r'^VERSION: (\d+)$', v2, re.M)
    ok = first_equal and v1_lines_equal and all(d['equal'] and d['control_in'] for d in dres) and len(r2) == n0 + 4 and not neg_equal and bool(ver) and ver.group(1) == '2'
    L = ['b711 -- STEP ZERO, (R321)(2): THE CONTROL OF THE STANDING CLAUSES v2 -- v1`S ROWS UNCHANGED AND THE FOUR DELTAS EQUAL TO THE RULING`S WORDS (%s)' % utc(), '',
         '### rows are checks. v2 read back by b710`s parser (tools/b710_standing.py parse): %d rows ; v1 %d rows. The deltas cut from relay data/b711_ferry.txt :9.' % (len(r2), n0),
         '### The NEG control: a copy of v2 with delta (ii)`s "refuses to write once the act’s root is appended" altered to "writes once ...", its row compared again.', '',
         '  v2`s rows (1)-(%d) equal to v1`s row for row (number, kind, separator, tag, clause, source line): %s' % (n0, first_equal),
         '  v1`s body lines (its LINE sections and rows) present in v2 line for line: %s' % v1_lines_equal]
    L += ['  (%d) delta (%s): equal to its span of the ferry %s ; its control within it %s ; %d characters' % (d['n'], d['delta'], d['equal'], d['control_in'], d['chars']) for d in dres]
    L += ['  NEG: the altered copy`s delta (ii) equal to the ferry %s (wanted False)' % neg_equal,
          '  VERSION %s (wanted 2)' % (ver.group(1) if ver else 'NONE'), '',
          '### ### **ROWS %d ; v1`S %d UNCHANGED %s ; DELTAS %d EQUAL %s ; THE NEG COPY DIFFERS %s ; VERSION 2 %s ; THE CONTROL AS WANTED %s.**' % (
              len(r2), n0, first_equal and v1_lines_equal, len(dres), all(d['equal'] for d in dres), not neg_equal, bool(ver) and ver.group(1) == '2', ok)]
    if 'dry' not in a:
        for name, data in (('b711_standing_control.txt', NL.join(L) + NL),
                           ('b711_standing_control.json', json.dumps(dict(at=utc(), rows=dres, first_equal=first_equal, v1_lines_equal=v1_lines_equal, neg_equal=neg_equal,
                                                                          n=len(r2), ok=ok), indent=1) + NL)):
            p = os.path.join(D, name)
            _membrane(p)
            with open(p + '.tmp', 'wb') as fh:
                fh.write(data.encode('utf-8'))
            os.replace(p + '.tmp', p)
    print(NL.join(L[5:]))
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    fn = {'write': write, 'control': control}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b711_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
