# -*- coding: utf-8 -*-
"""b512_notes.py -- (R121)(1): THE LADDER'S SHAPE FINDINGS WITHDRAWN AS WINDOW ARTEFACTS, BY APPENDED NOTE.
### `python tools/b512_notes.py` -- ONE note appended to each bank that carries them (b489, b490, b502, b503, b504
### components) and ONE to `FINDINGS.md`, whose last section is b507's fold, beside the lines that carry them. ### Each
### prior byte string proved a true prefix of the result; the lines removed counted. ### Refuses on a second run."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
FIND = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'FINDINGS.md')
NL = chr(10)
MARK = 'NOTE APPENDED AT b512 UNDER (R121)(1)'
RULE = '-' * 100
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK_NOTE = NL.join(['', RULE, '### %s, 2026-09-24. ### THE TEXT ABOVE IS UNEDITED.' % MARK, RULE,
    '### ### **THE SHAPE READINGS ABOVE ARE WITHDRAWN AS WINDOW ARTEFACTS.** ### b511 measured xi`s margin in a B-spline family',
    '### inside classK and found it falling at every one of the 118 steps: the extrema of the piecewise-linear family (4.062,',
    '### 5.196, 13.153), their attribution to the terms of zeros 1 and 4, the rise after the minimum, and the c/a^2 reading are',
    '### readings of the old windows` slope jumps, not of the object. ### The identity m = Z - P stands: it is `b321_identity`,',
    '### not a reading. ### Every verified cell above is VERIFIED-EST under (R121)(3).', RULE, ''])

FIND_NOTE = NL.join(['', '*Note appended at b512 under `(R121)(1)`, to the section above (b507`s fold).* **The shape findings it',
    'carries are withdrawn as window artefacts**: the margin`s *two turning points* (b489) and the ladder`s *three extrema*',
    '(b502), with their attribution to zeros 1 and 4 (b503, b504), the rise after the minimum and the `c/a²` reading, are',
    'readings of the piecewise-linear windows` slope jumps. In a B-spline family inside `classK` (b511) ξ`s margin falls at',
    'all 118 steps. **The identity `m = Z − P` stands** (`b321_identity`); every verified cell of the record is',
    'VERIFIED-EST under `(R121)(3)`. Nothing above this note is edited.', ''])

TARGETS = ['b489_components.txt', 'b490_components.txt', 'b502_components.txt', 'b503_components.txt', 'b504_components.txt']


def append(p, note, mark):
    before = open(p, 'rb').read()
    if mark.encode('utf-8') in before:
        sys.exit('### REFUSED -- %s ALREADY CARRIES THE NOTE; NOTHING WRITTEN.' % os.path.basename(p))
    add = note.encode('utf-8')
    if not before.endswith(b'\n'):
        add = b'\n' + add
    open(p, 'ab').write(add)
    after = open(p, 'rb').read()
    bl, al = before.split(b'\n'), after.split(b'\n')
    return dict(file=os.path.basename(p), written=len(after) - len(before), prefix=after.startswith(before),
                bom_kept=after[:3] == before[:3],
                removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b) - (0 if before.endswith(b'\n') else 1),
                marks=after.decode('utf-8').count(mark))


def main():
    out = [append(os.path.join(D, n), BANK_NOTE, MARK) for n in TARGETS]
    out.append(append(FIND, FIND_NOTE, 'Note appended at b512 under `(R121)(1)`'))
    for o in out:
        print('  %(file)-24s written %(written)4d ; prefix %(prefix)s ; BOM kept %(bom_kept)s ; removed %(removed)d ; marks %(marks)d' % o)
    io.open(os.path.join(D, 'b512_notes.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
