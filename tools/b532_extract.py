# -*- coding: utf-8 -*-
"""b532_extract.py -- COMPONENT 1`S POPULATION: EVERY DEPOSITED SENTENCE THAT NAMES THE FERRY`S SUBJECTS. ### `python tools/b532_extract.py`

### THE FOUR RECORDS (READING (1)): (M) the monograph v1.1.2, `PLACE-papers/outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md`,
### md5 checked here against the checksum b359 fetched from Zenodo 21539167; (K) the kernel record 21520474 as b493 banked
### it -- its description line in `data/zenodo_listing_2026-09-14_author_screen.txt` (line 36); (R) the kernel README at
### v1.5, `git show 0e5233f:README.md` of SIDE-kernel; (Z) the current Zenodo descriptions, b499`s three fetch-backs
### (`data/b499_fetchback_{21520474,21539068,21539167}.json`), HTML tags stripped.
### ### THE NEEDLES: the ferry`s six (Route 3, ConservationHypothesis, ConservationBridge, register 2, "the open premise",
### "reduction machine-verified") and their widenings, each printed with its yield per record (b381, b388): case-insensitive
### `route 3`, `conservation hypothesis` spelled apart, `second register` / `register two` / `R2`, `open premise`,
### `machine-verified` beside `reduc`, and the monograph`s own enumerator `Second:` inside section 27.3.
### ### A SENTENCE is split at [.!?] followed by whitespace and a capital, a newline pair, or a list bullet; a sentence
### matched by several needles is ONE row.
"""
import hashlib
import html
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
MONO = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NEEDLES = [
    ('Route 3', re.compile(r'\bRoute\s*3\b', re.I)),
    ('ConservationHypothesis', re.compile(r'ConservationHypothesis')),
    ('ConservationBridge', re.compile(r'ConservationBridge')),
    ('register 2', re.compile(r'\bregister[\s-]*2\b|\bsecond register\b|\bregister two\b|\bRegister2', re.I)),
    ('the open premise', re.compile(r'\bthe open premise\b', re.I)),
    ('reduction machine-verified', re.compile(r'reduction[^.]{0,40}machine[- ]verified|machine[- ]verified[^.]{0,40}reduction', re.I)),
    ('W: conservation hypothesis', re.compile(r'\bconservation hypothesis\b', re.I)),
    ('W: open premise', re.compile(r'\bopen premise\b', re.I)),
    ('W: R2', re.compile(r'\bR2\b')),
]


def text_of(src):
    t = html.unescape(re.sub(r'<[^>]+>', ' ', src))
    return re.sub(r'[ \t]+', ' ', t)


def sentences(t):
    t = t.replace(chr(13), '')
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z*(`"“‘#_\[])|\n\s*\n|\n(?=\s*[-*|] )|\n(?=#)', t)
    return [re.sub(r'\s+', ' ', p).strip() for p in parts if p and p.strip()]


def section_of(mono, pos):
    heads = [(m.start(), m.group(0).strip()) for m in re.finditer(r'^#{1,4} .*$', mono, re.M)]
    h = [x for x in heads if x[0] <= pos]
    return h[-1][1][:80] if h else ''


def main():
    recs = {}
    mono = io.open(MONO, encoding='utf-8').read().replace(chr(13), '')
    md5 = hashlib.md5(open(MONO, 'rb').read()).hexdigest()
    f1 = json.load(io.open(os.path.join(D, 'b359_fetch_F1.json'), encoding='utf-8'))
    zmd5 = next((f['checksum'] for f in f1['files'] if f.get('key') == 'A_Place_to_Stand.md'), '')
    recs['M'] = dict(name='monograph v1.1.2 (A_Place_to_Stand.md)', text=mono, md5=md5, zenodo_md5=zmd5, md5_match=('md5:' + md5) == zmd5)
    lst = io.open(os.path.join(D, 'zenodo_listing_2026-09-14_author_screen.txt'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    recs['K'] = dict(name='kernel record 21520474 as b493 banked it (listing line 36)', text=lst[35], title_line=lst[32])
    r = subprocess.run(['git', '-C', SK, 'show', '0e5233f:README.md'], capture_output=True)
    recs['R'] = dict(name='SIDE-kernel README at v1.5 (0e5233f)', text=r.stdout.decode('utf-8', 'replace').replace(chr(13), ''))
    for rid in ('21520474', '21539068', '21539167'):
        fb = json.load(io.open(os.path.join(D, 'b499_fetchback_%s.json' % rid), encoding='utf-8'))
        recs['Z' + rid] = dict(name='Zenodo %s as b499 fetched it back' % rid, text=text_of(fb['metadata']['description']),
                                title=fb['metadata']['title'])
    rows, yields = [], {}
    reg2 = [False]
    for key, rec in recs.items():
        sents = sentences(rec['text'])
        rec['sentences'] = len(sents)
        yields[key] = {n: 0 for n, _ in NEEDLES}
        pos = 0
        for s in sents:
            hit = [n for n, rx in NEEDLES if rx.search(s)]
            for n in hit:
                yields[key][n] += 1
            sec = ''
            if key == 'M':
                i = mono.find(s[:40], pos)
                if i < 0:
                    i = mono.find(s[:25])
                if i >= 0:
                    pos = i
                sec = section_of(mono, max(i, 0))
            in273 = key == 'M' and sec.startswith('## 27.3')
            # ### WIDENING (2), after the first run found the ferry`s "register 2" at 0 everywhere: section 27.3 names its
            # ### registers by ordinal ("Second: ... Third:"), so a register-2 SENTENCE is any sentence of 27.3 from the one
            # ### that opens "Second:" up to the one that opens "Third:". The first run is banked as b532_extract_first.txt.
            if in273 and re.search(r'\bSecond:', s):
                reg2[0] = True
            if in273 and re.search(r'\bThird:', s):
                reg2[0] = False
            if in273 and reg2[0]:
                hit.append('W: 27.3 register 2')
                yields[key].setdefault('W: 27.3 register 2', 0)
                yields[key]['W: 27.3 register 2'] += 1
            if hit:
                rows.append(dict(id='%s-%02d' % (key, sum(1 for x in rows if x['rec'] == key) + 1), rec=key, section=sec, needles=hit, text=s))
    out = dict(records={k: {x: y for x, y in v.items() if x not in ('text',)} for k, v in recs.items()}, yields=yields, rows=rows)
    io.open(os.path.join(D, 'b532_sentences.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1, ensure_ascii=False) + NL)
    L = ['=' * 120, 'b532 -- THE EXTRACT: DEPOSITED SENTENCES NAMING THE FERRY`S SUBJECTS.', '=' * 120,
         '  monograph md5 %s ; Zenodo 21539167 serves %s ; MATCH %s' % (md5, zmd5, recs['M']['md5_match']), '']
    for key, rec in recs.items():
        L.append('### %s -- %s ; %d sentences ; rows %d' % (key, rec['name'], rec['sentences'], sum(1 for x in rows if x['rec'] == key)))
        L.append('    yields : ' + ' ; '.join('%s %d' % (n, c) for n, c in yields[key].items()))
    L.append('')
    for x in rows:
        L.append('%-10s %-40s %s' % (x['id'], x['section'][:40], ','.join(x['needles'])))
        L.append('    ' + x['text'][:1200])
    io.open(os.path.join(D, 'b532_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:20]))
    print('rows total %d' % len(rows))
    return 0


if __name__ == '__main__':
    sys.exit(main())
