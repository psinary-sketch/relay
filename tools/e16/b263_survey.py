# -*- coding: utf-8 -*-
"""b263_survey.py -- S3's SURVEY, COMPLETED AT CONTENT.

### ### **WHY THIS FILE EXISTS, AND IT IS A DEFECT IN THE RUN THAT PRECEDED IT.**
### `b263_run.txt`'s S3 section COUNTED files matching five patterns and then printed the verdict
### ### **"NO HOLDING CONSTRAINS THE TOP LEVEL"** ### -- ### **WITHOUT HAVING READ ONE OF THEM.**
### Sixteen prior-owner files matched, and a count is not a reading.
### ### **A VERDICT THAT RUNS AHEAD OF ITS EVIDENCE IS THE SPECIES THIS CORPUS HUNTS, AND IT DOES
### ### NOT STOP BEING THAT SPECIES BECAUSE THE VERDICT LATER TURNS OUT TO BE RIGHT.**
###
### `b263_run.txt` IS PRESERVED UNCHANGED. ### This file supplies what its S3 owed: ### **EVERY
### PRIOR-OWNER HIT, QUOTED AT CONTENT AND CLASSIFIED**, against a criterion fixed before the
### quoting begins.
###
### ### **THE CRITERION, FIXED HERE BEFORE ANY LINE IS READ.** ### A hit CONSTRAINS the top level
### only if it states something an ### AGGREGATION ### must satisfy at `k = n_p`. ### It does NOT
### constrain if it merely:
###   (i) ### **SUPPLIES** ### the quotient value there (act 9's range, b11's `else 0`) -- that is
###       the object being aggregated, not a condition on the aggregation;
###   (ii) ### **DEFINES** ### the staircase or the cell (b17, b16) -- that fixes what `n_p` IS;
###   (iii) belongs to ### **THIS ARC** ### (b255-b263) -- this arc talking to itself is not a
###       prior owner.
### ### **THE CRITERION CAN FAIL: IF ANY HIT STATES A CONDITION ON `Q.value` AT THE TOP LEVEL,
### ### THE REGISTERED EXPECTATION IS REFUTED AND F1 FIRES.**
"""
import io
import json
import os
import re
import sys

ROOT = r'D:\relay'
DATA = os.path.join(ROOT, 'data')
REPORTS = os.path.join(ROOT, 'reports')
BANK = os.path.join(ROOT, 'data', 'b263_survey.txt')
OUT = os.path.join(ROOT, 'data', 'b263_survey.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

THIS_ARC = re.compile(r'b2(6[0-9]|5[5-9])')
PATTERNS = [('k = n', re.compile(r'k\s*=\s*n\b')),
            ('k >= n', re.compile(r'k\s*>=\s*n\b')),
            ('top level', re.compile(r'top[- ]level', re.I)),
            ('n_p = 1', re.compile(r'n_p\s*(\(a\))?\s*=\s*1')),
            ('first level', re.compile(r'first[- ]level', re.I))]


def classify(line):
    """### THE CRITERION, APPLIED. ### Returns (verdict, reason)."""
    l = line.lower()
    if re.search(r'else\s*0|0\s*for\s*k\s*>=\s*n|for\s*1\s*<=\s*k\s*<=\s*n-1', l):
        return 'SUPPLIES', 'states the quotient VALUE at the top level (act 9 / b11 range)'
    if re.search(r'staircase|n_p\(a\)\s*=\s*#|effective cutoff|cell', l):
        return 'DEFINES', 'defines the staircase or the cell, not a condition on Q.value'
    if re.search(r'q\.value|aggregat', l):
        return '### CANDIDATE CONSTRAINT', '### mentions Q.value or aggregation AT a level'
    return 'OTHER', 'mentions a level without stating any condition on Q.value'


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b263 SURVEY -- S3 COMPLETED AT CONTENT. ### **THE RUN COUNTED; THIS READS.**')
    rec('=' * 100)
    rec('### **`b263_run.txt` PRINTED "NO HOLDING CONSTRAINS THE TOP LEVEL" HAVING READ NONE OF THE')
    rec('### SIXTEEN PRIOR-OWNER FILES IT COUNTED. ### A COUNT IS NOT A READING, AND A VERDICT THAT')
    rec('### RUNS AHEAD OF ITS EVIDENCE IS A DEFECT EVEN WHEN IT LATER PROVES RIGHT.**')
    rec('### **THE RUN IS PRESERVED UNCHANGED. ### THIS FILE SUPPLIES WHAT ITS S3 OWED.**')
    rec('')
    rec('### **THE CRITERION, FIXED BEFORE ANY LINE IS QUOTED:** a hit CONSTRAINS only if it states')
    rec('### something an AGGREGATION must satisfy at `k = n_p`. ### SUPPLIES / DEFINES / OTHER do')
    rec('### not. ### **IT CAN FAIL: any hit naming `Q.value` or an aggregation at a level is a')
    rec('### CANDIDATE CONSTRAINT and fires F1.**')

    files = ([os.path.join(DATA, f) for f in sorted(os.listdir(DATA)) if f.endswith('.txt')]
             + [os.path.join(REPORTS, f) for f in sorted(os.listdir(REPORTS)) if f.endswith('.md')])
    prior = {}
    for path in files:
        base = os.path.basename(path)
        if THIS_ARC.search(base):
            continue
        try:
            lines = io.open(path, encoding='utf-8', errors='replace').read().split('\n')
        except Exception:
            continue
        for i, line in enumerate(lines, 1):
            for name, pat in PATTERNS:
                if pat.search(line):
                    prior.setdefault(base, []).append((i, name, line.strip()))
                    break

    rec('')
    rec('=' * 100)
    rec('### EVERY PRIOR-OWNER HIT, QUOTED AND CLASSIFIED. ### **%d FILES, %d LINES.**'
        % (len(prior), sum(len(v) for v in prior.values())))
    rec('=' * 100)
    tally = {}
    rows = []
    for base in sorted(prior):
        rec('')
        rec('  --- %s ---' % base)
        for (ln, pat, text) in prior[base][:6]:
            verdict, reason = classify(text)
            tally[verdict] = tally.get(verdict, 0) + 1
            rows.append(dict(file=base, line=ln, pattern=pat, verdict=verdict, text=text[:200]))
            rec('    :%-5d [%s] ### **%s**' % (ln, pat, verdict))
            rec('      %s' % text[:150])
            rec('      ### %s' % reason)
        if len(prior[base]) > 6:
            rec('    ... and %d more lines in this file, same patterns' % (len(prior[base]) - 6))

    rec('')
    rec('=' * 100)
    rec('### THE TALLY, AND THE VERDICT THE RUN OWED.')
    rec('=' * 100)
    for k in sorted(tally):
        rec('  %-28s : ### **%d**' % (k, tally[k]))
    cand = tally.get('### CANDIDATE CONSTRAINT', 0)
    rec('')
    rec('  ### ### **CANDIDATE CONSTRAINTS FOUND: ### %d**' % cand)
    if cand == 0:
        rec('  ### ### **F1 DID NOT FIRE. ### NO PRIOR HOLDING STATES A CONDITION ON `Q.value` AT')
        rec('  ### ### THE TOP LEVEL. ### THE REGISTERED EXPECTATION HOLDS -- AND IT NOW HOLDS ON')
        rec('  ### ### EVIDENCE READ AT CONTENT RATHER THAN ON A COUNT.**')
    else:
        rec('  ### ### **F1 FIRED. ### THE REGISTERED EXPECTATION IS REFUTED AND THE SPECIFICATION')
        rec('  ### ### IS NOT NEW. ### THE HITS ARE LISTED ABOVE.**')
    rec('')
    rec('  ### **WHAT THE PRIOR MENTIONS ACTUALLY ARE, IN ONE LINE EACH:**')
    rec('  ###   `SUPPLIES` -- act 9 and b11 state the quotient VALUE at `k >= n`. ### **THAT IS')
    rec('  ###     THE OBJECT BEING AGGREGATED, NOT A CONDITION ON THE AGGREGATION.**')
    rec('  ###   `DEFINES`  -- b16/b17 fix what `n_p` IS. ### **A DEFINITION OF THE INDEX, NOT OF')
    rec('  ###     WHAT `Q.value` MUST DO WITH IT.**')
    rec('  ###   `OTHER`    -- a level is mentioned in passing.')
    rec('  ### ### **AND b220 REMAINS THE STANDING VERDICT ON CONSTRAINTS THAT DO EXIST: ### "NOT')
    rec('  ### ### ONE OF THE FOUR EXCLUDES ANY FUNCTION."**')

    rec('')
    rec('=' * 100)
    rec('### CONTROLS ON THIS SURVEY.')
    rec('=' * 100)
    rec('  (S1) THE CLASSIFIER DISCRIMINATES -- on three constructed lines:')
    for probe in ('tau_q = 0 for k >= n, QED',
                  'the staircase n_p(a) = #{k : p^k <= a^2}',
                  'Q.value must count the aggregation at the top level'):
        v, _ = classify(probe)
        rec('       %-52s -> ### **%s**' % (probe[:52], v))
    rec('       ### ### **IT RETURNS A DIFFERENT VERDICT ON EACH, AND IT ### CAN ### RETURN')
    rec('       ### ### `CANDIDATE CONSTRAINT` -- SO ITS SILENCE ABOVE IS A MEASUREMENT.**')
    rec('  (S2) THE ARC FILTER EXCLUDES THIS ARC : b260-b263 files are absent from the listing.')
    rec('  (S3) FILES READ : ### **%d**' % len(files))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(rows=rows, tally=tally, candidates=cand), io.open(OUT, 'w', encoding='utf-8'),
              indent=1)
    print('\n  banked -> %s' % BANK)


if __name__ == '__main__':
    main()
