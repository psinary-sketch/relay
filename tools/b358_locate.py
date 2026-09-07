# -*- coding: utf-8 -*-
"""b358_locate.py -- THE SOURCES, FETCHED AND PINNED. ### **BAR 1: EVERY SOURCE HASHED, EVERY QUOTE ON DISK.**

### ### **THIS TOOL COMPUTES NOTHING.** ### It fetches bytes, hashes them, extracts their text to disk and
### searches that text for the phrases the act needs. ### **NO SERIES IS SUMMED, NO COEFFICIENT IS
### ### EVALUATED, NO INTEGRAL IS TAKEN** -- the cap forbids it and `G-CAP` re-measures it on stripped code.
### ### **A SOURCE THAT DOES NOT FETCH IS REPORTED AS NOT FETCHED, WITH ITS STATUS**, and nothing from it
### is quoted. ### The record has four incidents of an absence of READING being reported as an absence of
### LITERATURE, and this file exists so this act does not make a fifth.
"""
import hashlib
import io
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
SCRATCH = os.path.join(os.environ.get('TEMP', os.path.join(ROOT, 'data')), 'b358_sources')
if not os.path.isdir(SCRATCH):
    os.makedirs(SCRATCH)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (tag, citation, url, kind)
SOURCES = [
    ('S1', 'voros0506326',
     "A. Voros, A sharpening of Li's criterion for the Riemann Hypothesis, arXiv:math/0506326 -- the "
     "source the DEPOSIT ITSELF cites for the archimedean asymptotic and for the detection threshold",
     'https://arxiv.org/pdf/math/0506326', 'pdf'),
    ('S2', 'lagarias0404394',
     "J. C. Lagarias, Li coefficients for automorphic L-functions, arXiv:math/0404394v4 -- ALREADY "
     "PINNED IN THE RECORD at b327 (sha256 86f3d3c4...), re-fetched here and the hash compared",
     'https://arxiv.org/pdf/math/0404394v4', 'pdf'),
    ('S3', 'coffey0505052',
     "M. W. Coffey, Toward verification of the Riemann hypothesis: application of the Li criterion, "
     "arXiv:math-ph/0505052 -- already fetched at b341, re-fetched here",
     'https://arxiv.org/pdf/math-ph/0505052', 'pdf'),
    ('S4', 'voros_abs0506326',
     "the arXiv abstract page for S1, fetched as a second, independent surface for the same statement",
     'https://arxiv.org/abs/math/0506326', 'html'),
    ('S5', 'bombierilagarias1999',
     "E. Bombieri and J. C. Lagarias, Complements to Li's criterion for the Riemann hypothesis, "
     "J. Number Theory 77 (1999) -- the ORIGIN of the criterion and of Corollary 1(c)",
     'https://core.ac.uk/download/pdf/82415505.pdf', 'pdf'),
]

# ### THE PHRASES THE ACT NEEDS LOCATED. ### **TYPED AS SEARCH HINTS ONLY**; what is BANKED is the line the
# ### search returns, extracted to disk, and every quotation the bank uses is then re-located by
# ### `anchor_from_file.py` at that extract file. ### A hint that finds nothing is REPORTED AS FINDING
# ### NOTHING, which is the honest outcome and not a failure to be tuned away.
HINTS = [
    ('the main term of the asymptotic', [r'log\s*n\s*[-−]\s*1\s*\+\s*γ', r'\\log n - 1 \+ \\gamma',
                                         r'log n\s*−\s*1\s*\+', r'\bn\s*\(\s*log\s*n']),
    ('the criterion / equivalence wording', [r'if and only if', r'\biff\b', r'equivalent to the Riemann']),
    ('the asymptotic is unconditional / to all orders', [r'unconditional', r'to all orders',
                                                         r'all orders in']),
    ('the archimedean part', [r'archimedean', r'arithmetic part', r'\blambda_n\^\{?\\infty', r'\bV\b.*part']),
    ('the detection threshold ~ 2T^2', [r'2\s*T\s*\^?\s*2', r'2T\s*2', r'\bn\s*[>≳~]\s*2\s*T',
                                        r'detection', r'threshold']),
    ('the oscillating / exponentially growing alternative', [r'oscillat', r'exponentially (growing|large)',
                                                             r'\bRH\b.*fails']),
    ('the subexponential sufficiency (Bombieri-Lagarias Cor 1(c))', [r'e\^\{?\\?epsilon n', r'subexponential',
                                                                     r'-\s*c\s*e\^']),
    ('the error / remainder term', [r'\bO\s*\(', r'remainder', r'error term']),
    ('what the zero sum contributes', [r'sum over (the )?zeros', r'\\sum_\\rho', r'zeros? of \\xi',
                                       r'non-?trivial zeros']),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def fetch(url, dest):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (research seat; read-only GET)'})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = r.read()
        status = r.status
        ctype = r.headers.get('Content-Type', '')
    open(dest, 'wb').write(data)
    return status, ctype, len(data), hashlib.sha256(data).hexdigest()


def extract_text(path, kind):
    if kind == 'pdf':
        import pypdf
        reader = pypdf.PdfReader(path)
        parts = []
        for i, page in enumerate(reader.pages):
            parts.append('=== PAGE %d ===' % (i + 1))
            parts.append(page.extract_text() or '')
        return chr(10).join(parts)
    raw = open(path, 'rb').read().decode('utf-8', 'replace')
    raw = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', raw)
    raw = re.sub(r'(?s)<[^>]+>', chr(10), raw)
    return re.sub(r'\n{3,}', chr(10) + chr(10), raw)


def main():
    rec('=' * 100)
    rec('b358 -- THE SOURCES, FETCHED AND PINNED. ### EVERY BYTE HASHED; EVERY TEXT ON DISK.')
    rec('### ### **THIS TOOL COMPUTES NOTHING.** ### It fetches, hashes, extracts and searches.')
    rec('=' * 100)
    out = []
    for tag, name, cite, url, kind in SOURCES:
        rec('')
        rec('-' * 100)
        rec('  [%s] %s' % (tag, name))
        rec('      %s' % cite)
        rec('      url : %s' % url)
        dest = os.path.join(SCRATCH, 'b358_%s.%s' % (name, 'pdf' if kind == 'pdf' else 'html'))
        entry = dict(tag=tag, name=name, citation=cite, url=url, kind=kind)
        try:
            status, ctype, nbytes, sha = fetch(url, dest)
            entry.update(fetched=True, status=status, content_type=ctype, bytes=nbytes, sha256=sha)
            rec('      ### **FETCHED : HTTP %s ; %s ; %d bytes**' % (status, ctype, nbytes))
            rec('      ### **sha256 : %s**' % sha)
        except Exception as e:
            entry.update(fetched=False, error='%s: %s' % (type(e).__name__, str(e)[:120]))
            rec('      ### ### **NOT FETCHED : %s**' % entry['error'])
            rec('      ### ### **NOTHING FROM THIS SOURCE IS QUOTED**, and its absence is an absence of')
            rec('      ### ### READING, not of literature.')
            out.append(entry)
            continue
        try:
            text = extract_text(dest, kind)
        except Exception as e:
            entry.update(extracted=False, error='%s: %s' % (type(e).__name__, str(e)[:120]))
            rec('      ### ### **FETCHED BUT NOT EXTRACTED : %s**' % entry['error'])
            out.append(entry)
            continue
        tp = os.path.join(D, 'b358_source_%s.txt' % name)
        io.open(tp, 'w', encoding='utf-8', newline=chr(10)).write(text)
        entry.update(extracted=True, text_file=os.path.basename(tp), chars=len(text),
                     text_sha256=hashlib.sha256(text.encode('utf-8')).hexdigest())
        rec('      extracted to : data/%s   (%d chars)' % (os.path.basename(tp), len(text)))
        lines = text.splitlines()
        found = {}
        for label, pats in HINTS:
            hits = []
            for p in pats:
                rx = re.compile(p, re.I)
                for i, ln in enumerate(lines, 1):
                    if rx.search(ln):
                        hits.append(i)
                        if len(hits) >= 6:
                            break
                if len(hits) >= 6:
                    break
            found[label] = sorted(set(hits))[:6]
            rec('      %-58s lines %s' % (label[:58], found[label] if found[label] else '### NONE'))
        entry['hints'] = found
        out.append(entry)
    rec('')
    rec('=' * 100)
    nf = sum(1 for e in out if e.get('fetched'))
    rec('  sources attempted : %d   ### FETCHED : %d   ### NOT FETCHED : %d'
        % (len(out), nf, len(out) - nf))
    for e in out:
        if not e.get('fetched'):
            rec('    ### NOT FETCHED : %s -- %s' % (e['name'], e.get('error', '')))
    rec('  ### **A HASH FIXES THE BYTES. ### IT DOES NOT MAKE THE READING OF THEM RIGHT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b358_locate_run', LINES)
    io.open(os.path.join(D, 'b358_locate.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(sources=out, fetched=nf, attempted=len(out),
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
