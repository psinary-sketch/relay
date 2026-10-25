# -*- coding: utf-8 -*-
"""b712_standing.py -- (R322)(3): THE STANDING CLAUSES AT v3, written at step zero as data/standing_clauses_v3.txt -- v2 unchanged (its 55 rows
copied from data/standing_clauses_v2.txt byte for byte, its four LINE sections and its row lines as banked) with the five deltas appended as
numbered rows (56)-(60), each delta the ruling's own words cut from (R322)(3) as banked (relay data/b712_ferry.txt :11), its control the ruling's
own clause within it; and the control: v3's rows read back by b710's parser (tools/b710_standing.py parse), its first 55 equal to v2's row for
row, each delta equal to its span of the ferry, the version line 3, a NEG copy with one delta altered differing.
Carried from tools/b711_standing.py by diff: the base v1 -> v2, the bank v2 -> v3, the ferry's line :9 -> :11, the heads and the stop of (R322)(3),
the NEG alteration on delta (ii), the version 2 -> 3, the act b711 -> b712 (the membrane's exclusion none: b712's record tool not yet written).

### THE CUT OF THE DELTAS: (R322)(3) at :11 of the banked ferry, from "(i) THE FACE NAMES THE ROOT’S PROMPT BY FORM" to the next numeral's head
### ("(ii) THE GATE’S COMMIT READ FROM THE STEP BANK", "(iii) THE HEAD LINE BUILT FROM BANKS", "(iv) THE MIRROR’S ORDER", "(v) THE COMMAND
### SCREEN READS A FRESH BANK") and the last to the sentence "The throughstone report of b711 carried forward" (the standing report tool and the
### NEXT line's repair are the carry's, not rows of the clauses). Each row: KIND STANDING, SEP STOP (the last END), TAG SOURCE (R322)(3)(i)..(v).
### Routes: `write [dry]` -> data/standing_clauses_v3.txt ; `control [dry]` -> data/b712_standing_control.txt (.json). Writes only those banks.
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

V1, BANK, FERRY, FLINE = 'standing_clauses_v2.txt', 'standing_clauses_v3.txt', 'b712_ferry.txt', 11
HEADS = ('(i) THE FACE NAMES THE ROOT’S PROMPT BY FORM', '(ii) THE GATE’S COMMIT READ FROM THE STEP BANK', '(iii) THE HEAD LINE BUILT FROM BANKS',
         '(iv) THE MIRROR’S ORDER', '(v) THE COMMAND SCREEN READS A FRESH BANK')
STOP = ' The throughstone report of b711 carried forward'
NUMERALS = ('i', 'ii', 'iii', 'iv', 'v')


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def deltas():
    """[(numeral, text)] -- the five deltas verbatim from the banked ferry's :11, each ending at its full stop."""
    line = S1.rd(FERRY).split(NL)[FLINE - 1]
    if not line.startswith('(3) FIVE FACES OF THE CLOSE, GIVEN STRUCTURE'):
        sys.exit('### THE BANKED FERRY`S :%d IS NOT (R322)(3) -- NOTHING WRITTEN' % FLINE)
    idx = [line.find(h) for h in HEADS] + [line.find(STOP)]
    if min(idx) < 0 or idx != sorted(idx):
        sys.exit('### A DELTA`S HEAD OR THE STOP NOT FOUND IN ORDER (%s) -- NOTHING WRITTEN' % idx)
    return [(NUMERALS[k], line[idx[k]:idx[k + 1]].strip()) for k in range(len(HEADS))]


def v1_body():
    """v2's lines from its first LINE section to its last row (the head and the verdict line excluded), byte for byte."""
    L = S1.rd(V1).split(NL)
    a = next(i for i, l in enumerate(L) if l.startswith('## LINE '))
    b = max(i for i, l in enumerate(L) if l.startswith('      '))
    return L[a:b + 1]


def text_of():
    dl = deltas()
    body = v1_body()
    rows1 = S1.parse(S1.rd(V1))
    n0 = rows1[-1][0]
    L = ['b712 -- THE STANDING CLAUSES, VERSION 3, WRITTEN ONCE AT STEP ZERO UNDER (R322)(3): VERSION 2 UNCHANGED (relay data/standing_clauses_v2.txt, its rows (1)-(%d) '
         'copied byte for byte) WITH THE FIVE DELTAS APPENDED AS ROWS (%d)-(%d) (%s)' % (n0, n0 + 1, n0 + len(dl), utc()), '',
         'VERSION: 3',
         'THE CITATION FORM: a ferry names "standing clauses v3" and carries its deltas alone, each delta a numbered row of the next version (data/b710_rules.txt row (1)).',
         '### rows are clauses, in v1`s form: (n) KIND SEP TAG on the row`s first line, the clause verbatim on the next line after six spaces (v1`s head',
         '### lines :5-:9 give KIND, SEP and TAG). Rows (1)-(%d) are v2`s, unchanged. Rows (%d)-(%d) are (R322)(3)`s five deltas, each the ruling`s own' % (n0, n0 + 1, n0 + len(dl)),
         '### words cut from relay data/b712_ferry.txt :11, each carrying its control in its own clause ("control: ..."); the item repairs of the same',
         '### paragraph (the standing report tool, the NEXT line) are the carry`s and are not rows. Where a delta and an earlier row speak to one object',
         '### the later row is the version`s reading; no earlier row is edited.', '']
    L += body
    L += ['', '## LINE %d OF data/b712_ferry.txt -- (R322)(3), five faces of the close given structure (the deltas of v3)' % FLINE]
    for k, (num, t) in enumerate(dl):
        L.append('  (%d) STANDING %s SOURCE (R322)(3)(%s) ; first carried in data/b712_ferry.txt under (R322)' % (n0 + 1 + k, 'STOP' if k < len(dl) - 1 else 'END', num))
        L.append('      ' + t)
    L += ['', '### ### **ROWS %d ; v2`S ROWS %d UNCHANGED ; DELTAS %d (THE ROOT`S PROMPT BY FORM, THE GATE`S COMMIT FROM THE STEP BANK, THE HEAD LINE FROM BANKS, '
          'THE MIRROR`S ORDER, THE FRESH COMMAND SCREEN), EACH WITH ITS CONTROL ; VERSION 3.**' % (n0 + len(dl), n0, len(dl))]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b712', p, None)


def write(*a):
    L = text_of()
    if 'dry' in a:
        print(NL.join(L[:10] + L[-14:]))
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
        dres.append(dict(n=n0 + 1 + k, delta=num, equal=bool(row) and row[4] == t, control_in=bool(row) and 'control:' in row[4], chars=len(t)))
    neg = v2.replace('reads the gate’s commit from the act’s step bank row marked gate', 'reads the gate’s commit from the face', 1)
    neg_rows = S1.parse(neg)
    neg_equal = len(neg_rows) > n0 + 1 and neg_rows[n0 + 1][4] == dl[1][1]
    ver = re.search(r'^VERSION: (\d+)$', v2, re.M)
    ok = first_equal and v1_lines_equal and all(d['equal'] and d['control_in'] for d in dres) and len(r2) == n0 + len(HEADS) and not neg_equal and bool(ver) and ver.group(1) == '3'
    L = ['b712 -- STEP ZERO, (R322)(3): THE CONTROL OF THE STANDING CLAUSES v3 -- v2`S ROWS UNCHANGED AND THE FIVE DELTAS EQUAL TO THE RULING`S WORDS (%s)' % utc(), '',
         '### rows are checks. v3 read back by b710`s parser (tools/b710_standing.py parse): %d rows ; v2 %d rows. The deltas cut from relay data/b712_ferry.txt :11.' % (len(r2), n0),
         '### The NEG control: a copy of v3 with delta (ii)`s "reads the gate’s commit from the act’s step bank row marked gate" altered to "... from the face", its row compared again.', '',
         '  v3`s rows (1)-(%d) equal to v2`s row for row (number, kind, separator, tag, clause, source line): %s' % (n0, first_equal),
         '  v2`s body lines (its LINE sections and rows) present in v3 line for line: %s' % v1_lines_equal]
    L += ['  (%d) delta (%s): equal to its span of the ferry %s ; its control within it %s ; %d characters' % (d['n'], d['delta'], d['equal'], d['control_in'], d['chars']) for d in dres]
    L += ['  NEG: the altered copy`s delta (ii) equal to the ferry %s (wanted False)' % neg_equal,
          '  VERSION %s (wanted 3)' % (ver.group(1) if ver else 'NONE'), '',
          '### ### **ROWS %d ; v2`S %d UNCHANGED %s ; DELTAS %d EQUAL %s ; THE NEG COPY DIFFERS %s ; VERSION 3 %s ; THE CONTROL AS WANTED %s.**' % (
              len(r2), n0, first_equal and v1_lines_equal, len(dres), all(d['equal'] for d in dres), not neg_equal, bool(ver) and ver.group(1) == '3', ok)]
    if 'dry' not in a:
        for name, data in (('b712_standing_control.txt', NL.join(L) + NL),
                           ('b712_standing_control.json', json.dumps(dict(at=utc(), rows=dres, first_equal=first_equal, v1_lines_equal=v1_lines_equal, neg_equal=neg_equal,
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
        print('usage: b712_standing.py write [dry] | control [dry]')
        sys.exit(2)
    fn(*sys.argv[2:])
