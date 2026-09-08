# -*- coding: utf-8 -*-
"""b362_locate.py -- THE SOURCES, FETCHED AND PINNED. ### **BAR 1: EVERY SOURCE HASHED, EVERY QUOTE ON DISK.**

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
SCRATCH = os.path.join(os.environ.get('TEMP', os.path.join(ROOT, 'data')), 'b362_sources')
if not os.path.isdir(SCRATCH):
    os.makedirs(SCRATCH)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (tag, citation, url, kind)
SOURCES = [
    ('S1', 'baezduarte0202141',
     "L. Baez-Duarte, A strengthening of the Nyman-Beurling criterion for the Riemann Hypothesis, "
     "arXiv:math/0202141 -- the VARIANT the navigator's hint names, located rather than recalled",
     'https://arxiv.org/pdf/math/0202141', 'pdf'),
    ('S2', 'baezduarte_abs0202141',
     "the arXiv abstract page for S1, fetched as a second, independent surface for the same statement",
     'https://arxiv.org/abs/math/0202141', 'html'),
    ('S3', 'burnol0103058',
     "J.-F. Burnol, A lower bound in an approximation problem involving the zeros of the Riemann zeta "
     "function, arXiv:math/0103058 -- located for the RATE, which is (iii)",
     'https://arxiv.org/pdf/math/0103058', 'pdf'),
    ('S4', 'bagchi1911_04029',
     "B. Bagchi, On a Hilbert space reformulation of the Riemann hypothesis, arXiv:1911.04029 -- "
     "located as a survey surface carrying the CLASSICAL criterion with its hypotheses",
     'https://arxiv.org/pdf/1911.04029', 'pdf'),
    ('S5', 'baezduarte0205003',
     "L. Baez-Duarte, A strengthening of the Nyman-Beurling criterion for the Riemann hypothesis, 2, "
     "arXiv:math/0205003 -- the sequel, fetched because the hint names a family and a sequel may "
     "restate the family differently",
     'https://arxiv.org/pdf/math/0205003', 'pdf'),
]

# ### THE PHRASES THE ACT NEEDS LOCATED. ### **TYPED AS SEARCH HINTS ONLY**; what is BANKED is the line the
# ### search returns, extracted to disk, and every quotation the bank uses is then re-located by
# ### `anchor_from_file.py` at that extract file. ### A hint that finds nothing is REPORTED AS FINDING
# ### NOTHING, which is the honest outcome and not a failure to be tuned away.
# ### ### **AND A NOTE ON HOW THIS BLOCK WAS WRITTEN**, because the record has banked the species
# ### three times in this one session: ### **IT WAS WRITTEN WITH A FILE EDITOR AND NOT THROUGH A
# ### SHELL HEREDOC**, whose escaping collapses doubled backslashes and turns a regex quietly into a
# ### different regex. ### Every pattern below is plain text or built from `BS = chr(92)`, so there is
# ### no doubled backslash in this file for anything to collapse.
BS = chr(92)
B = BS + 'b'
HINTS = [
    ('the criterion as an equivalence', ['if and only if', 'equivalent to the Riemann',
                                         'is true if and only', 'necessary and sufficient']),
    ('the function that must be approximated', ['characteristic function', 'indicator function',
                                                B + 'chi' + B, 'of the interval']),
    ('the family of dilations', ['dilat', 'fractional part', B + 'rho' + B, 'theta */ *x']),
    ('the restriction to integers (the strengthening)', ['natural numbers', B + 'integers?' + B,
                                                         '1 */ *n', 'n *= *1, *2']),
    ('the distance / the sequence d_N', [B + 'd_?N' + B, B + 'distance' + B, B + 'infimum' + B,
                                         B + 'inf' + B]),
    ('the space it is set in', ['L' + BS + '^?2', 'Hilbert space', 'closed (linear )?span',
                                BS + '(0, *1' + BS + ')']),
    ('the RATE, and any lower bound', ['lower bound', B + 'liminf' + B, 'log *N', B + 'asymptotic']),
    ('the sum over the zeros', ['sum over (the )?zeros', 'non-?trivial zeros',
                                'zeros of the Riemann', 'critical line']),
    ('anything conditional on RH', ['assuming the Riemann', 'under (the )?RH',
                                    'if the Riemann hypothesis (is true|holds)',
                                    B + 'conditional' + B]),
    ('the hypotheses the statement carries', [B + 'suppose' + B, B + 'assume' + B, B + 'Theorem' + B,
                                              B + 'where' + B]),
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
    rec('b362 -- THE SOURCES, FETCHED AND PINNED. ### EVERY BYTE HASHED; EVERY TEXT ON DISK.')
    rec('### ### **THIS TOOL COMPUTES NOTHING.** ### It fetches, hashes, extracts and searches.')
    rec('=' * 100)
    out = []
    for tag, name, cite, url, kind in SOURCES:
        rec('')
        rec('-' * 100)
        rec('  [%s] %s' % (tag, name))
        rec('      %s' % cite)
        rec('      url : %s' % url)
        dest = os.path.join(SCRATCH, 'b362_%s.%s' % (name, 'pdf' if kind == 'pdf' else 'html'))
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
        tp = os.path.join(D, 'b362_source_%s.txt' % name)
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
    p = run_clock.write(D, 'b362_locate_run', LINES)
    io.open(os.path.join(D, 'b362_locate.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(sources=out, fetched=nf, attempted=len(out),
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
