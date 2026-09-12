# -*- coding: utf-8 -*-
"""b443r_extract.py -- THE SURVEY (THE RE-ISSUE). ### **WRITTEN BEFORE THE FACE. IT READS; IT MEASURES NOTHING.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KEY = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
LED = os.path.join(PP, 'FACES_LEDGER.md')
OUT = os.path.join(D, 'b443r_extract.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L, READS, MISS = [], [0], []


def rec(s=''):
    L.append(s)
    print(s)


def head(n, t):
    rec('')
    rec('-' * 100)
    rec('  ### (%s) %s' % (n, t))
    rec('-' * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13) + NL, NL)
    except Exception:
        return ''


def wrap(s, n=86):
    out, cur = [], ''
    for w in (s or '').split():
        if cur and len(cur) + 1 + len(w) > n:
            out.append(cur)
            cur = w
        else:
            cur = (cur + ' ' + w).strip()
    if cur:
        out.append(cur)
    return out or ['']


def quote(path, needle, clip=700, span=None, after=0):
    READS[0] += 1
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('      %s:%d' % (os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                seg = b.strip()
                if span:
                    j = seg.find(needle)
                    seg = seg[j:j + span]
                for c in wrap(seg[:clip], 84):
                    rec('        | %s' % c)
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), needle[:60]))
    rec('      ### **NOT LOCATED** : %s' % needle[:60])
    return None


def main():
    rec('=' * 100)
    rec('b443 -- SITE (vi), AND THE ARC`S PRODUCT NAMED. ### THE SURVEY.')
    rec('=' * 100)

    head(1, 'SITE (vi)`S OWN CELL, AND ITS WITNESS-KIND ENTRY')
    quote(LED, '**(vi) THE TYPE-D RESIDUE AT EVERY FINITE MODULUS**', clip=1500, span=1500)
    quote(LED, '### **`(vi)` — KIND: NOT EMPTY. WITNESS: `NONE KNOWN`.**', clip=600, span=600)

    head(2, 'THE CONSPIRACY KEYSTONE -- ITS RESIDUE LINES, ITS SIEVE SENTENCE, ITS PLACEHOLDER')
    for ndl in ('the density lower bound is the whole of the remaining weight',
                'the representation lower bound',
                'the sieve density bound is the whole of the remaining weight',
                "Brun's sieve (1919)",
                'sorry  -- M5, open',
                '`density_positive : True`',
                'The boundary is a local-to-global interchange.'):
        quote(KEY, ndl, clip=520, span=520)

    head(3, 'THE COMPILED LEMMA -- b431`S READING, FROM ITS BANK')
    quote(os.path.join(D, 'b431_components.txt'), 'moduli := {L}', clip=200)
    quote(LED, 'a theorem about a SHAPE is not a theorem about any instance of it', clip=300, span=300)
    quote(LED, '| **B14** the compiled shared-witness theorem', clip=500)

    head(4, 'THE VERIFIED SOURCES -- ANY DENSITY LOWER BOUND ACROSS MODULI?')
    for nm, fn in (('Lagarias', 'b358_source_lagarias0404394.txt'), ('CC', 'b328_source_text.txt')):
        t = read(os.path.join(D, fn))
        hits = [(i + 1, ln.strip()[:120]) for i, ln in enumerate(t.splitlines())
                if re.search(r'density|modul|positive proportion|sieve|twin prime|Goldbach', ln, re.I)]
        rec('      %-9s hits %d' % (nm, len(hits)))
        for i, ln in hits:
            rec('        %5d  %s' % (i, ln))
    rec('    ### **READ, NOT DECIDED:** the components classify every hit.')

    head(5, 'THE PRIOR FIVE SITES` TALLIES, FROM BANKED JSON')
    prior = json.loads(read(os.path.join(D, 'b442_site_v.json')) or '{}')
    for act, t in (prior.get('tallies') or {}).items():
        cb = t.get('CLASS BOUNDARY', 0)
        rec('      %-5s %2d candidates ; CLASS BOUNDARY %2d ; majority %s'
            % (act, sum(t.values()), cb, cb * 2 > sum(t.values())))
    rec('      union after five sites : %s' % prior.get('union_all'))

    head(6, 'b341`S SPECIES, (R38)`S RULE, AND THE SPAN TOOL')
    quote(os.path.join(PP, 'FINDINGS.md'), '- **b341 — the two Li coefficients located', clip=400)
    quote(os.path.join(PP, 'OPEN_TRAILS.md'), '**`(R38)`** keys the lane', clip=520)
    rec('      span tool : tools/b363_span.py exists %s' % os.path.exists(os.path.join(ROOT, 'tools', 'b363_span.py')))
    t = read(os.path.join(PP, 'OPEN_TRAILS.md')) + read(os.path.join(PP, 'EMERGING_RESEARCH_PROGRAMMES.md'))
    rec('      "fast radio burst" / "FRB" / "dispersion measure" in OPEN_TRAILS + ERP : %d / %d / %d'
        % (len(re.findall(r'fast.radio.burst', t, re.I)), len(re.findall(r'\bFRB', t)),
           len(re.findall(r'dispersion measure', t, re.I))))

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)


if __name__ == '__main__':
    main()
