# -*- coding: utf-8 -*-
"""b341_locate.py -- THE LITERATURE UNDER THE IMPORT BAR: THREE SOURCES, EACH FETCHED READ-ONLY, HASHED, ITS TEXT
### EXTRACTED AND BANKED, AND SEARCHED FOR THE THIRD AND FIFTH LI COEFFICIENTS (registration (C), sealed first).

### ### **WHAT LOCATED MEANS (sealed):** a decimal string in the extracted text whose first eight significant digits
### agree with either candidate at `n = 3` or `n = 5` after the source's own normalization (Keiper's `lambda_n / n`,
### Li's `lambda_n`), quoted verbatim at its line. ### A source that returns no PDF or carries no such string is
### declared NOT READ, with the reason. ### **NO PDF IS COMMITTED**: the bytes stay in the session's scratchpad; only
### the extracted text is banked (`data/b341_source_text_<tag>.txt`).
"""
import hashlib
import io
import json
import os
import re
import sys
import time
import urllib.request

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SCRATCH = os.environ.get('B341_SCRATCH') or os.path.join(os.path.expandvars(r'%LOCALAPPDATA%'), 'Temp', 'claude', 'D--',
                                                           '41ec74a6-756c-4480-bbf3-5e7c45e947a9', 'scratchpad')
RUN = os.path.join(D, 'b341_locate_run.txt')
OUT = os.path.join(D, 'b341_locate.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SOURCES = [
    ('S1', 'keiper1992', "J. B. Keiper, Power series expansions of Riemann's xi-function, Math. Comp. 58 (1992) -- the source's [34]",
     'https://www.ams.org/journals/mcom/1992-58-198/S0025-5718-1992-1122072-5/S0025-5718-1992-1122072-5.pdf', 'keiper'),
    ('S2', 'maslanka0406312', "K. Maslanka, Effective method of computing Li's coefficients and their properties, arXiv math/0406312 -- the source's [40]",
     'https://arxiv.org/pdf/math/0406312', 'li'),
    ('S3', 'coffey0505052', 'M. W. Coffey, Toward verification of the Riemann hypothesis: application of the Li criterion, arXiv math-ph/0505052',
     'https://arxiv.org/pdf/math-ph/0505052', 'li'),
]

# ### the two candidates at each index, as the two emitters print them (the extract file locates both at their lines)
CANDIDATES = {3: {'bench': '0.2077580993', 'keystone': '0.20763892059268'},
              5: {'bench': '0.5747345', 'keystone': '0.57554271443'}}
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def sig8(x):
    """### the first eight significant digits of a decimal string, as a string of digits."""
    s = mp.nstr(mp.mpf(x), 8, strip_zeros=False)
    return re.sub(r'[^0-9]', '', s.lstrip('0.').replace('e', ''))[:8]


def fetch(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research seat; read-only GET)'})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
        status = r.status
        ctype = r.headers.get('Content-Type', '')
    open(dest, 'wb').write(data)
    return status, ctype, len(data), hashlib.sha256(data).hexdigest()


def extract_text(pdf):
    import pypdf
    reader = pypdf.PdfReader(pdf)
    parts = []
    for i, page in enumerate(reader.pages):
        parts.append('=== PAGE %d ===' % (i + 1))
        parts.append(page.extract_text() or '')
    return chr(10).join(parts)


def lines_of(text):
    return text.splitlines()


def search(text, normalization):
    """### every decimal string in the text; matched at n = 3 and n = 5 against both candidates under the normalization."""
    hits = {3: [], 5: []}
    lines = text.splitlines()
    with mp.workdps(30):
        want = {}
        for n, c in CANDIDATES.items():
            for who, v in c.items():
                val = mp.mpf(v)
                if normalization == 'keiper':
                    val = val / n
                want[(n, who)] = sig8(val)
        for i, ln in enumerate(lines):
            for m in re.finditer(r'\d*\.\d{6,}', ln):
                s8 = sig8(m.group(0)) if m.group(0) not in ('.',) else ''
                if len(s8) < 8:
                    continue
                for (n, who), w in want.items():
                    if s8 == w:
                        hits[n].append(dict(line=i + 1, string=m.group(0), agrees_with=who, normalization=normalization, context=ln.strip()[:160]))
    return hits, want


def main():
    t0 = time.time()
    rec('=' * 100)
    rec('b341 -- THE LITERATURE UNDER THE IMPORT BAR. ### three sources, fetched read-only, hashed, extracted, searched.')
    rec('=' * 100)
    os.makedirs(SCRATCH, exist_ok=True)
    out = {}
    for sid, tag, desc, url, normz in SOURCES:
        rec('')
        rec('  (%s) %s' % (sid, desc))
        rec('      URL : %s ; normalization read for the search : %s' % (url, "Keiper's lambda_n / n" if normz == 'keiper' else "Li's lambda_n"))
        dest = os.path.join(SCRATCH, 'b341_%s.pdf' % tag)
        entry = dict(id=sid, tag=tag, url=url, normalization=normz)
        try:
            status, ctype, nbytes, sha = fetch(url, dest)
            entry.update(status=status, content_type=ctype, bytes=nbytes, sha256=sha)
            rec('      fetched : HTTP %s ; %s ; %d bytes ; sha256 %s' % (status, ctype, nbytes, sha))
        except Exception as e:  # noqa: BLE001
            entry.update(status='ERROR', reason=str(e)[:200], read=False)
            rec('      ### NOT READ -- the fetch failed : %s' % str(e)[:200])
            out[sid] = entry
            continue
        if b'%PDF' not in open(dest, 'rb').read(1024):
            entry.update(read=False, reason='the response is not a PDF')
            rec('      ### NOT READ -- the response is not a PDF (first bytes %r)' % open(dest, 'rb').read(24))
            out[sid] = entry
            continue
        try:
            text = extract_text(dest)
        except Exception as e:  # noqa: BLE001
            entry.update(read=False, reason='text extraction failed: %s' % str(e)[:160])
            rec('      ### NOT READ -- text extraction failed : %s' % str(e)[:160])
            out[sid] = entry
            continue
        tpath = os.path.join(D, 'b341_source_text_%s.txt' % tag)
        io.open(tpath, 'w', encoding='utf-8', newline=chr(10)).write(text)
        entry['text_file'] = os.path.basename(tpath)
        entry['text_chars'] = len(text)
        hits, want = search(text, normz)
        entry['wanted_sig8'] = {'%d/%s' % k: v for k, v in want.items()}
        entry['hits'] = {str(n): h for n, h in hits.items()}
        rec('      text banked : %s (%d chars) ; strings sought (eight significant digits) : %s' % (os.path.basename(tpath), len(text), entry['wanted_sig8']))
        for n in (3, 5):
            if hits[n]:
                for h in hits[n][:4]:
                    rec("      n = %d : LOCATED at line %d -- %r agrees with the %s's value under %s ; context: %s" % (n, h['line'], h['string'], h['agrees_with'], h['normalization'], h['context'][:110]))
            else:
                rec('      n = %d : NOT READ -- no decimal string in the text matches either candidate to eight significant digits' % n)
        # ### READINGS BESIDE THE RULE (labelled; NOT LOCATED under the sealed eight-digit decimal-string rule): a mantissa the
        # ### text layer split at its decimal point (digits joined across spaces), or a six-digit print of the value.
        beside = {3: [], 5: []}
        with mp.workdps(30):
            for n in (3, 5):
                for who, v in CANDIDATES[n].items():
                    val = mp.mpf(v) / n if normz == 'keiper' else mp.mpf(v)
                    w8, w6 = sig8(val), sig8(val)[:6]
                    for i, ln in enumerate(lines_of(text)):
                        joined = re.sub(r'\s+', '', ln)
                        if w8 in re.sub(r'[^0-9]', '', joined) and not any(h['line'] == i + 1 for h in hits[n]):
                            beside[n].append(dict(line=i + 1, kind='split-mantissa (digits joined across spaces)', agrees_with=who, context=ln.strip()[:120]))
                        for m in re.finditer(r'\d*\.\d{5,7}(?!\d)', ln):
                            # ### a six-digit print agrees when it is the value rounded to its own digits
                            digs = len(m.group(0).split('.')[1])
                            if abs(mp.mpf(m.group(0)) - val) <= mp.mpf(10) ** (-digs) / 2 and w6:
                                beside[n].append(dict(line=i + 1, kind='%d-decimal print' % digs, string=m.group(0), agrees_with=who, context=ln.strip()[:120]))
                for b in beside[n]:
                    rec('      n = %d : READING BESIDE THE RULE, NOT LOCATED -- line %d, %s, agrees with the %s\'s value ; context: %s' % (n, b['line'], b['kind'], b['agrees_with'], b['context'][:100]))
        entry['beside'] = {str(n): b for n, b in beside.items()}
        entry['read'] = True
        out[sid] = entry
    rec('')
    located = {n: [(s['id'], h['agrees_with']) for s in out.values() if s.get('read') for h in s['hits'][str(n)]] for n in (3, 5)}
    rec('  ### LOCATED, by index : n = 3 -> %s ; n = 5 -> %s' % (located[3], located[5]))
    rec('  ### NO PDF COMMITTED ; the bytes are in the scratchpad ; the extracted texts are banked.')
    rec('  ### elapsed : %.0f s' % (time.time() - t0))
    rec('=' * 100)
    run_path, k = RUN, 1
    while os.path.exists(run_path):
        k += 1
        run_path = RUN.replace('_run.txt', '_run%d.txt' % k)
    io.open(run_path, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(sources=out, located={str(k): v for k, v in located.items()}), indent=1))
    return 0


if __name__ == '__main__':
    sys.exit(main())
