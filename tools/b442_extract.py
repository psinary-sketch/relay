# -*- coding: utf-8 -*-
"""b442_extract.py -- THE SURVEY. ### **WRITTEN BEFORE THE FACE. IT READS; IT MEASURES NOTHING.**"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CC = os.path.join(D, 'b328_source_text.txt')
LAG = os.path.join(D, 'b358_source_lagarias0404394.txt')
OUT = os.path.join(D, 'b442_extract.txt')
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


def quote(path, needle, after=0, clip=700, label=None, start=0, span=None):
    READS[0] += 1
    lines = read(path).splitlines()
    for i, ln in enumerate(lines):
        if needle in ln:
            rec('      %s:%d' % (os.path.basename(path), i + 1))
            for b in lines[i:i + after + 1]:
                seg = b.strip()
                if span:
                    j = seg.find(needle)
                    seg = seg[max(0, j - start):j + span]
                for c in wrap(seg[:clip], 84):
                    rec('        | %s' % c)
            return i + 1
    MISS.append('%s : %r' % (os.path.basename(path), (label or needle)[:60]))
    rec('      ### **NOT LOCATED** : %s' % (label or needle)[:60])
    return None


def main():
    rec('=' * 100)
    rec('b442 -- THE MINIMUM NAMED, AND SITE (v). ### THE SURVEY.')
    rec('=' * 100)

    head(1, 'COMPONENT 1 -- WHAT THE SOURCES AND THE RECORD SAY ABOUT theta`S MINIMUM')
    quote(CC, 'It is the derivative of 2', after=1, clip=200)
    quote(CC, 'where this function is negative', clip=200)
    for nm, p in (('CC', CC), ('Lagarias', LAG)):
        t = read(p)
        rec('      %-9s "minimum": %d ; "6.28"/"6.29": %d ; "3.53": %d'
            % (nm, len(re.findall(r'minim', t)), len(re.findall(r'6\.2[89]', t)), len(re.findall(r'3\.53', t))))
    hits = []
    for root, dirs, fs in os.walk(PP):
        dirs[:] = [x for x in dirs if x not in ('.git',)]
        for f in fs:
            if f.endswith('.md') and re.search(r'minimum of (the )?(Riemann.?Siegel )?(theta|θ)|θ.{0,12}minimum',
                                                read(os.path.join(root, f))):
                hits.append(f)
    rec('      PLACE-papers files naming theta`s minimum : %d %s' % (len(hits), hits))
    rec('    ### **READ, NOT DECIDED:** neither verified source states theta`s minimum or its value, and no')
    rec('    ### record file names it. ### The value comparison the order asks for has no verified source.')

    head(2, 'COMPONENT 2 -- SITE (v)`S OWN CELL, ROW F7, THE LOCATED THEOREM, AND THE CLASS')
    led = os.path.join(PP, 'FACES_LEDGER.md')
    quote(led, '**(v) THE REPRESENTATION-DEPENDENT CONSTANT**', clip=1500, start=0, span=1500)
    quote(led, '### **`(v)` — KIND: `(b)`. WITNESS: `NONE KNOWN`.**', clip=700, start=0, span=700)
    quote(led, '| F7 | F7 -- the Epstein negative control', clip=700)
    quote(LAG, 'Theorem 6.1. For any irreducible cuspidal', after=6, clip=200)
    quote(LAG, 'Theorem 5.1. For any irreducible cuspidal', after=4, clip=200)
    quote(LAG, 'Dedekind zeta functions of any algebraic', clip=200)
    quote(LAG, 'For the trivial representation', after=1, clip=200)
    quote(os.path.join(D, 'b325_extract_notes.txt'), 'We identify the Euler product', clip=400)
    quote(os.path.join(D, 'b326_the_reach.txt'), 'there is no Euler product to keep it', clip=300)
    quote(os.path.join(D, 'b358_read_run.txt'), '**H-CUSP**', after=2, clip=300)

    head(3, 'THE FOUR PRIOR SITES` KINDS, FROM THEIR OWN BANKED JSON')
    prior = json.loads(read(os.path.join(D, 'b436_prior_sites.json')) or '{}')
    rec('      b436_prior_sites.json keys : %s' % (list(prior)[:6] if isinstance(prior, dict) else type(prior)))
    cand = json.loads(read(os.path.join(D, 'b436_candidates.json')) or '{}')
    rows = cand.get('candidates', cand) if isinstance(cand, dict) else cand
    rec('      b436_candidates.json : %d candidates, kinds %s'
        % (len(rows), sorted(set(r.get('kind') for r in (rows if isinstance(rows, list) else [])))))

    head(4, 'COMPONENT 3 -- b441`S WORDS FOR b440`S TWO CORRECTIONS, AND THE TABLE`S SHAPE')
    b441 = os.path.join(D, 'b441_closing.txt')
    quote(b441, 'VERDICT: THE RECORD NEVER DENIED THE IDENTIFICATION', after=2, clip=300)
    quote(b441, "b440's sentence -- \"b430's defect, still live in every act", after=1, clip=300,
          label='the reach correction')
    quote(b441, "AND b440'S REPAIR WAS DEFECTIVE TOO", after=3, clip=300)
    quote(os.path.join(T, 'b441_checks.py'), "if 'b441' not in subj", after=3, clip=200)
    corr = read(os.path.join(SIDE, 'CORRESPONDENCE.md')).splitlines()
    rows_at = [i for i, ln in enumerate(corr) if re.match(r'^\| \d+ \|', ln)]
    between = [i for i in range(rows_at[0], rows_at[-1]) if i not in rows_at and corr[i].strip()
               and not corr[i].startswith('|')] if rows_at else []
    rec('      CORRESPONDENCE.md rows %d ; last row %s ; non-row lines between the first and last row : %d'
        % (len(rows_at), corr[rows_at[-1]][:8] if rows_at else '-', len(between)))
    rec('    ### **READ, NOT DECIDED:** the lines between rows are a census note, not a correction beside a')
    rec('    ### row; appending is the only write the table takes. How a correction rides "beside" row 289 is')
    rec('    ### the face`s declared reading.')

    rec('')
    rec('=' * 100)
    rec('  ### READS ATTEMPTED : %d' % READS[0])
    rec('  ### MISSES          : %d' % len(MISS))
    for m in MISS:
        rec('      %s' % m)
    rec('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: %s' % os.path.basename(OUT))


if __name__ == '__main__':
    main()
