# -*- coding: utf-8 -*-
"""b696_tails_source.py -- (R306)(3)(a): THE DIGAMMA EXPANSION'S REMAINDER BOUND, SOURCED BY LINE BEFORE THE PLAN CITES IT (N2).
### One route: `fetch` -> data/b696_source_dlmf_5_11.txt, the NIST DLMF section 5.11 (Gamma function, asymptotic expansions) as text, one
### block per line, each formula by its own alttext (the TeX the page carries), the raw page's sha256 and byte count in the head. The request
### carries one header, a generic User-Agent (the library's own refused with 403); no identifier of the author. Nothing is computed here. Written by the Write tool at b696.
"""
import hashlib
import html
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
URL = 'https://dlmf.nist.gov/5.11'
OUT = 'b696_source_dlmf_5_11.txt'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def text_of(raw):
    s = raw.decode('utf-8', 'replace')
    s = re.sub(r'(?is)<(script|style|head)\b.*?</\1>', ' ', s)
    s = re.sub(r'(?is)<math\b[^>]*?alttext="([^"]*)"[^>]*>.*?</math>', lambda m: ' [' + html.unescape(m.group(1)) + '] ', s)
    s = re.sub(r'(?i)<(br|/p|/div|/li|/tr|/h[1-6]|/table|/td|/caption)\b[^>]*>', NL, s)
    s = re.sub(r'(?s)<[^>]+>', ' ', s)
    s = html.unescape(s)
    out = []
    for l in s.split(NL):
        l = re.sub(r'[ \t\r ]+', ' ', l).strip()
        if l:
            out.append(l)
    return out


def fetch(*a):
    q = os.path.join(D, OUT)
    if os.path.exists(q):
        sys.exit('### %s EXISTS -- NOT REFETCHED' % OUT)
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})   # ### a generic agent; the library's own was refused (403)
    raw = urllib.request.urlopen(req, timeout=60).read()
    L = text_of(raw)
    head = ['b696 -- THE SOURCE OF THE DIGAMMA EXPANSION`S REMAINDER BOUND, (R306)(3)(a): NIST DLMF section 5.11, fetched %s' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
            '### %s ; the raw page %d bytes, sha256 %s ; rows are the page`s text blocks, one per line, each formula as the page`s own alttext (TeX) in [ ]'
            % (URL, len(raw), hashlib.sha256(raw).hexdigest()), '']
    open(q + '.tmp', 'wb').write((NL.join(head + L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print('  %s: %d lines ; raw %d bytes ; sha256 %s' % (OUT, len(head + L), len(raw), hashlib.sha256(raw).hexdigest()))


if __name__ == '__main__':
    fn = {'fetch': fetch}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b696_tails_source.py fetch')
        sys.exit(2)
    fn(*sys.argv[2:])
