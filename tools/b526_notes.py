# -*- coding: utf-8 -*-
"""b526_notes.py -- COMPONENT 0: (R136)(1)`S SENTENCE APPENDED BESIDE THE FOLD`S SUMMARY. ### `python tools/b526_notes.py`

### The sentence is QUOTED from `b526_ferry.txt` (the paste`s line breaks collapsed), appended once to `FINDINGS.md` (whose
### last section is b525`s fold) and once to the digest (whose last block is b525`s); each prior byte string is proved a
### true prefix; the writer refuses a second note.
"""
import hashlib
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
NL = chr(10)
MARK = '**Appended at b526 under `(R136)`(1)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sentence():
    f = io.open(os.path.join(D, 'b526_ferry.txt'), encoding='utf-8').read()
    i = f.index('"the numbers cited')
    j = f.index('the instances differ."', i) + len('the instances differ."')
    return ' '.join(f[i:j].split())


def main():
    s = sentence()
    notes = {
        FIND: NL + '%s, beside the summary sentence of THE WITNESS ARC, b517–b524 — THE FOLD above, which cites the measured '
                   'window and the kernel`s together:** %s' % (MARK, s) + NL,
        DIG: NL + '%s, beside the b525 block above, whose quoted statement cites the measured window and the kernel`s '
                  'together:** %s' % (MARK, s) + NL,
    }
    out = []
    for path, text in notes.items():
        before = open(path, 'rb').read()
        if MARK.encode('utf-8') in before:
            print('  %s : REFUSED -- the note is already present' % os.path.basename(path))
            out.append(dict(file=os.path.basename(path), written=False))
            continue
        open(path, 'ab').write(text.encode('utf-8'))
        after = open(path, 'rb').read()
        rec = dict(file=os.path.basename(path), written=True, before=len(before), after=len(after),
                   prefix=hashlib.sha256(after[:len(before)]).hexdigest() == hashlib.sha256(before).hexdigest(),
                   marks=after.decode('utf-8').count(MARK))
        out.append(rec)
        print('  %(file)s : %(before)d -> %(after)d bytes ; prefix proved %(prefix)s ; notes %(marks)d' % rec)
    io.open(os.path.join(D, 'b526_notes.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(sentence=s, writes=out), indent=1, ensure_ascii=False) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
