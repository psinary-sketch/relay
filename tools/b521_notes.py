# -*- coding: utf-8 -*-
"""b521_notes.py -- (R130)(1): b518`s AND b519`s Q0 CELLS RE-MARKED VERIFIED-EST-TAIL, BY APPENDED NOTE. ### `python tools/b521_notes.py`

### A cell is re-marked iff it was VERIFIED-EST (|r| <= B) and its tail majorant exceeded the rest of its bound,
### E_tail > B' = E_u + E_k + E_round -- read from the cell banks, not retyped. ### The note is APPENDED to each act`s
### components bank; the prior bytes are proved an unchanged prefix (sha256 before = sha256 of the new file`s head).
### ### Refuses to write a second time: a bank already carrying the note is left alone and the refusal printed.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
MARK = '### (R130)(1) NOTE, APPENDED AT b521'
BANKS = (('b518', 'b518_components.txt', ['b518_cells.jsonl']),
         ('b519', 'b519_components.txt', ['b519_cells_A.jsonl', 'b519_cells_B.jsonl', 'b519_cells_C.jsonl']))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def census(files):
    rows = []
    for f in files:
        for l in io.open(os.path.join(D, f), encoding='utf-8'):
            if not l.strip():
                continue
            c = json.loads(l)
            q = c['q']
            bp = q['Eu'] + q['Ek'] + q['Eround']
            rows.append(dict(file=f, a=c['a'], verified=q['verified'], ratio=q['Etail'] / bp, tail_led=q['Etail'] > bp))
    return rows


def main():
    out = []
    for act, bank, files in BANKS:
        path = os.path.join(D, bank)
        raw = open(path, 'rb').read()
        rows = census(files)
        ver = [r for r in rows if r['verified']]
        led = [r for r in ver if r['tail_led']]
        rec = dict(act=act, bank=bank, cells=len(rows), verified=len(ver), remarked=len(led),
                   ratio_min=min(r['ratio'] for r in led) if led else None, ratio_max=max(r['ratio'] for r in led) if led else None,
                   per_file={f: sum(1 for r in led if r['file'] == f) for f in files}, before_sha=hashlib.sha256(raw).hexdigest(),
                   before_bytes=len(raw))
        if MARK.encode('utf-8') in raw:
            rec['written'] = False
            rec['refused'] = 'the bank already carries the note'
            print('  %s : REFUSED -- %s' % (bank, rec['refused']))
            out.append(rec)
            continue
        note = [MARK + ' -- the lines below are appended; every byte above them is unchanged.',
                '### **%d of %d VERIFIED-EST Q0 CELLS OF %s ARE RE-MARKED VERIFIED-EST-TAIL** (%s): each one`s tail majorant for'
                % (len(led), len(ver), act, ', '.join('%s %d' % (f, n) for f, n in rec['per_file'].items())),
                '### zeros above the bank`s height 150 exceeded the rest of its bound B` = E_u + E_k + E_round, by factors %.1e to %.1e,'
                % (rec['ratio_min'], rec['ratio_max']) if led else '### (no cell re-marked)',
                '### so the sign was decided beyond a bound the quadrature did not set. The signs stand; what they were verified against',
                '### is now named: the tail majorant. ### Read from the cell banks by tools/b521_notes.py; no cell is recomputed.',
                '=' * 132]
        text = (NL if not raw.endswith(b'\n') else '') + NL.join(note) + NL
        io.open(path, 'a', encoding='utf-8', newline=NL).write(text)
        new = open(path, 'rb').read()
        rec['after_bytes'] = len(new)
        rec['prefix_proved'] = hashlib.sha256(new[:len(raw)]).hexdigest() == rec['before_sha']
        rec['written'] = True
        print('  %s : %d cells, %d verified, %d re-marked ; tail/B` %.1e .. %.1e ; prefix proved %s'
              % (bank, rec['cells'], rec['verified'], rec['remarked'], rec['ratio_min'] or 0, rec['ratio_max'] or 0, rec['prefix_proved']))
        out.append(rec)
    io.open(os.path.join(D, 'b521_notes.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
