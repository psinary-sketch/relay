# -*- coding: utf-8 -*-
"""b705_cc_source.py -- (R315)(8): THE SMALL-SUPPORT POSITIVITY RESULT READ AT SOURCE BEFORE THE REGISTRATION IS WRITTEN.
### One route: `fetch` -> data/b705_source_cc_2006_13771.pdf (untracked, its sha256 banked) and data/b705_source_cc_2006_13771.txt, the text
### of Connes-Consani, "Weil positivity and trace formula, the archimedean place" (arXiv:2006.13771), one line per text line with a
### `== PAGE n` marker before each page, read by pypdf; the raw bytes` sha256 and count in the head. The request carries one header, a generic
### User-Agent; no identifier of the author. Nothing is computed here. Written by the Write tool at b705 (b696_tails_source.py`s form).
"""
import hashlib
import io
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
URL = 'https://arxiv.org/pdf/2006.13771'
PDF = 'b705_source_cc_2006_13771.pdf'
OUT = 'b705_source_cc_2006_13771.txt'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def fetch(*a):
    from pypdf import PdfReader
    q, p = os.path.join(D, OUT), os.path.join(D, PDF)
    if os.path.exists(q):
        sys.exit('### %s EXISTS -- NOT REFETCHED' % OUT)
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    raw = urllib.request.urlopen(req, timeout=120).read()
    sha = hashlib.sha256(raw).hexdigest()
    open(p + '.tmp', 'wb').write(raw)
    os.replace(p + '.tmp', p)
    R = PdfReader(io.BytesIO(raw))
    L = []
    for i, pg in enumerate(R.pages, 1):
        L.append('== PAGE %d' % i)
        for l in (pg.extract_text() or '').replace(chr(13), '').split(NL):
            l = re.sub(r'[ \t ]+', ' ', l).rstrip()
            L.append(l)
    head = ['b705 -- THE SOURCE OF THE SMALL-SUPPORT POSITIVITY RESULT, (R315)(8): Connes-Consani, arXiv:2006.13771, fetched %s' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            '### %s ; the raw PDF %d bytes, sha256 %s (data/%s, untracked) ; %d pages ; rows are the PDF`s text lines by pypdf, a `== PAGE n` row before each page'
            % (URL, len(raw), sha, PDF, len(R.pages)), '']
    open(q + '.tmp', 'wb').write((NL.join(head + L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print('  %s: %d lines ; %d pages ; raw %d bytes ; sha256 %s' % (OUT, len(head + L), len(R.pages), len(raw), sha))


if __name__ == '__main__':
    fn = {'fetch': fetch}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b705_cc_source.py fetch')
        sys.exit(2)
    fn(*sys.argv[2:])
