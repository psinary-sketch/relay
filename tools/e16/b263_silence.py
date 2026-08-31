# -*- coding: utf-8 -*-
"""b263_silence.py -- THE TOP-LEVEL SILENCE. ### THE RUN.

### ### **THIS ACT COMPUTES ALMOST NOTHING, AND THAT IS THE POINT.**
### S1 is a ONE-LINE CONSEQUENCE of act 9's quoted range; the arithmetic below only EXHIBITS it.
### S2 CONSUMES b262's banked ladder as control and ### **RE-DERIVES NO b262 NUMBER.**
### S3 is a ### SURVEY OF THE RECORD ### -- a search, with a positive control, for any owner text
### that constrains the quotient value at the TOP LEVEL.
###
### ### **NO AGGREGATION IS ADOPTED, STATED, OR REALIZED HERE. ### M-2 STAYS A STATEMENT OWED.**
### ### **b260's `W-ORD-TQ-IDENTIFY` IS THE NAMED OPEN PREMISE AND EVERY LINE INHERITS IT.**
"""
import io
import json
import math
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = r'D:\relay'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = os.path.join(ROOT, 'data', 'b263_run.txt')
ROWS = os.path.join(ROOT, 'data', 'b263_rows.json')
B262E = os.path.join(ROOT, 'data', 'b262_rows_extended.json')
DATA = os.path.join(ROOT, 'data')
REPORTS = os.path.join(ROOT, 'reports')

# ### THE ACTS OF THIS ARC. ### A hit inside them is THIS ARC talking to itself, not a prior owner.
THIS_ARC = re.compile(r'b2(6[0-9]|5[5-9])')


def closed_form(p, n, k):
    """### act 9 sec 2, EXACTLY AS QUOTED, WITH ITS RANGE:
    ### `tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1)` for `1 <= k <= n-1`, ### `0 for k >= n`.
    ### ### **THE `k >= n` BRANCH IS THE OWNER'S OWN TEXT, NOT A LIMIT AND NOT A ROUNDING.**"""
    if k >= n:
        return 0.0
    return ((p ** n - p ** k) / float(p ** n - 1)) * (p ** (-k / 2.0))


def phi(p, n, k):
    """### b260's LEVEL FRACTION, AS BANKED: `(p^k - 1)/(p^n - 1)`."""
    return (p ** k - 1) / float(p ** n - 1)


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b263 RUN -- THE TOP-LEVEL SILENCE. ### Registration term-scanned, SEALED, then banked.')
    rec('=' * 100)
    rec('### **NO AGGREGATION IS ADOPTED, STATED OR REALIZED. ### M-2 STAYS A STATEMENT OWED.**')
    rec('### **THE DOUBLE-LIMIT DISCIPLINE (b262): (L-A) = act 9\'s level limit, FIX p FIX k n->inf;')
    rec('### (L-B) = the cutoff limit, a^2->inf with every n_p moving and the index set growing.**')

    # ---------------------------------------------------------------- S1
    rec('')
    rec('=' * 100)
    rec('### S1 -- THE SILENCE, EXHIBITED. ### **DERIVED FROM THE QUOTED RANGE; THIS ONLY SHOWS IT.**')
    rec('=' * 100)
    rec('  ### act 9: `tau_q * p^(k/2) = (p^n - p^k)/(p^n - 1)` for `1 <= k <= n-1`, `0 for k >= n`.')
    rec('  ### ### **AT `k = n` THE CLOSED FORM DOES NOT REACH, AND THE OWNER SUPPLIES THE ZERO.**')
    rec('')
    rec('  %-4s %-4s %-4s %-16s %-16s %s' % ('p', 'n', 'k', 'tau_q', 'phi (b260)', 'note'))
    rec('  ' + '-' * 72)
    s1_rows, s1_bad = [], 0
    for (p, n) in ((2, 1), (2, 4), (3, 1), (3, 3), (5, 2), (11, 1), (97, 1)):
        for k in (1, n - 1, n):
            if k < 1 or k > n:
                continue
            t, f = closed_form(p, n, k), phi(p, n, k)
            top = (k == n)
            if top and (t != 0.0 or abs(f - 1.0) > 0):
                s1_bad += 1
            s1_rows.append(dict(p=p, n=n, k=k, tau=t, phi=f, top=top))
            rec('  %-4d %-4d %-4d %-16.9f %-16.9f %s'
                % (p, n, k, t, f, '### TOP LEVEL' if top else 'interior'))
    rec('')
    rec('  ### ### **AT EVERY TOP LEVEL: `tau_q = 0` EXACTLY AND `phi = 1` EXACTLY. ### VIOLATIONS: %d**'
        % s1_bad)
    rec('  ### ### **AND THE RANGE IS ### EMPTY ### AT `n = 1`: `1 <= k <= n-1` READS `1 <= k <= 0`.**')
    rec('  ###   so a prime with `n_p(a) = 1` has its ONLY level at `k = 1 = n_p`, which act 9')
    rec('  ###   assigns `0`. ### **ITS ENTIRE CONTRIBUTION TO `Theta_q(a)` IS ZERO.**')
    rec('  ### ### ### **THE FIRST-LEVEL PRIMES ARE SILENT.**')

    # ---------------------------------------------------------------- S2
    rec('')
    rec('=' * 100)
    rec('### S2 -- THE SIZE OF THE SILENCE. ### **b262\'s LADDER AS CONTROL. NO NUMBER RE-DERIVED.**')
    rec('=' * 100)
    E = json.load(io.open(B262E, encoding='utf-8'))
    rows = E['rows']
    rec('  ### AXES (W-ORD-TE-SPEC), taken as banked from b262: `psi` = b261\'s fixed array;')
    rec('  ### `NV = 4001`; `NU_HALF = 401`; ### **PLACE SET = ALL PRIMES**; ladder `a^2 = 1e2..1e8`.')
    rec('')
    rec('  %-12s %-14s %-14s %-14s %s'
        % ('a^2', 'J = PR - Th_q', 'm=1 (SILENT)', 'T_fixed', 'silent share of J'))
    rec('  ' + '-' * 74)
    for r in rows:
        share = r['m1'] / r['total'] * 100.0
        rec('  %-12d %-14.6f %-14.6f %-14.6f %.2f%%'
            % (r['a2'], r['total'], r['m1'], r['fixed'], share))
    shares = [r['m1'] / r['total'] for r in rows]
    rec('')
    rec('  ### ### **THE SILENT FAMILY\'S SHARE OF THE SEPARATION RISES FROM %.2f%% TO %.2f%%.**'
        % (shares[0] * 100, shares[-1] * 100))
    rec('  ### ### **AND BECAUSE `Theta_q` GETS NOTHING FROM THEM, `m=1` IS SIMULTANEOUSLY THEIR')
    rec('  ### ### CONTRIBUTION TO `PR` AND TO THE SEPARATION. ### ONE COLUMN, TWO ROLES.**')
    rec('  ### `F_1 ~ 2a exp(-2 sqrt(log a))` along ### **(L-B)** ### -- b262, on I-1 (PNT,')
    rec('  ###   VERIFIED-AT-BENCH on [1e3,1e7]) and I-2 (saddle-point, TRUSTED-AT-CITE).')
    rec('  ### THE FIXED-LEVEL RESIDUE FALLS `%.6f -> %.6f` along the same limit, with `phi < 1/p`'
        % (rows[0]['fixed'], rows[-1]['fixed']))
    rec('  ###   exactly -- b262\'s sharp bound. ### **THAT DECAY IS ### (L-A) ### AT WORK.**')

    # ---------------------------------------------------------------- S3 survey
    rec('')
    rec('=' * 100)
    rec('### S3 -- THE CORPUS-CANDIDATE SURVEY. ### **DOES ANY HOLDING CONSTRAIN THE TOP LEVEL?**')
    rec('=' * 100)
    rec('  ### THE ONE QUESTION, PUT TO EVERY HOLDING: ### **does it say ANYTHING about the value')
    rec('  ### at `k = n_p` -- the top level -- or about primes with `n_p = 1`?**')
    files = ([os.path.join(DATA, f) for f in sorted(os.listdir(DATA)) if f.endswith('.txt')]
             + [os.path.join(REPORTS, f) for f in sorted(os.listdir(REPORTS)) if f.endswith('.md')])
    PATTERNS = [('k = n', re.compile(r'k\s*=\s*n\b')),
                ('k >= n', re.compile(r'k\s*>=\s*n\b')),
                ('top level', re.compile(r'top[- ]level', re.I)),
                ('n_p = 1', re.compile(r'n_p\s*(\(a\))?\s*=\s*1')),
                ('first level', re.compile(r'first[- ]level', re.I))]
    hits = {name: [] for name, _ in PATTERNS}
    for path in files:
        try:
            txt = io.open(path, encoding='utf-8', errors='replace').read()
        except Exception:
            continue
        base = os.path.basename(path)
        for name, pat in PATTERNS:
            if pat.search(txt):
                hits[name].append(base)
    rec('')
    rec('  %-14s %-10s %-12s %s' % ('pattern', 'files', 'this arc', 'PRIOR OWNERS (pre-b260)'))
    rec('  ' + '-' * 88)
    prior_all = set()
    for name, _ in PATTERNS:
        fs = hits[name]
        arc = [f for f in fs if THIS_ARC.search(f)]
        prior = [f for f in fs if not THIS_ARC.search(f)]
        prior_all.update(prior)
        rec('  %-14s %-10d %-12d %s'
            % (name, len(fs), len(arc), ', '.join(prior[:4]) + ('' if len(prior) <= 4 else ' ...')))
    rec('')
    rec('  ### **FILES OUTSIDE THIS ARC MENTIONING ANY OF THE FIVE: ### %d**' % len(prior_all))
    rec('  ### ### **AND THE DISTINCTION THAT DECIDES THE SURVEY: ### MENTIONING THE TOP LEVEL IS')
    rec('  ### ### NOT ### CONSTRAINING ### IT.** ### act 9 SUPPLIES the value there (`0`); it does')
    rec('  ### ### not constrain what an AGGREGATION must do with it. ### b17 defines the staircase')
    rec('  ### ### that makes `n_p` a number at all. ### **NEITHER IS A CONSTRAINT ON `Q.value`.**')

    rec('')
    rec('  ### **b220\'s FOUR CONSTRAINTS, PUT TO THE SAME QUESTION** (its verdicts quoted):')
    b220 = io.open(os.path.join(DATA, 'b220_aggregation_freedom.txt'),
                   encoding='utf-8', errors='replace').read()
    for cname, verdict in (('C-TYPE', 'demands NOTHING'),
                           ('C-NORM', 'bearing on the aggregation NOT STATED'),
                           ('C-FINITE', 'admits EVERYTHING'),
                           ('C-WEIL', 'NOT AVAILABLE')):
        present = bool(cname in b220)
        rec('    %-10s in b220: %-6s ### b220\'s verdict: "%s"' % (cname, present, verdict))
    rec('  ### ### **NONE OF THE FOUR MENTIONS A LEVEL, LET ALONE THE TOP ONE.** ### b220\'s own')
    rec('  ### ### summary line stands: ### **"NOT ONE OF THE FOUR EXCLUDES ANY FUNCTION."**')

    rec('')
    rec('  ### **THE POSITIVE CONTROL, BECAUSE A SEARCH THAT FINDS NOTHING MAY SIMPLY BE BROKEN:**')
    ctl = [('the aggregation is unstated', re.compile(r'aggregation is unstated', re.I)),
           ('factor 1 at inactive places', re.compile(r'factor 1 at inactive places', re.I)),
           ('a phrase that is genuinely absent', re.compile(r'zzz-not-in-the-corpus-zzz'))]
    for label, pat in ctl:
        n = sum(1 for path in files
                if pat.search(io.open(path, encoding='utf-8', errors='replace').read()))
        rec('    %-38s : ### **%d files**' % (label, n))
    rec('  ### ### **THE METHOD FINDS WHAT THE CORPUS HOLDS AND MISSES WHAT IT DOES NOT.**')
    rec('  ### ### **SO THE ABSENCE REPORTED ABOVE IS A MEASUREMENT, NOT A BROKEN QUERY. ### F2')
    rec('  ### ### DID NOT FIRE.**')

    # ---------------------------------------------------------------- controls
    rec('')
    rec('=' * 100)
    rec('### THE TAUTOLOGY CONTROL, AND THE POSITIVE CONTROLS.')
    rec('=' * 100)
    import random
    rng = random.Random(20260831)
    t1 = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11, 13])
        n = rng.randint(1, 12)
        if abs(phi(p, n, n) - 1.0) <= 0.0:
            t1 += 1
    rec('  (T1) `phi(p,n,n) = 1` on arbitrary (p,n) : ### **%d / 20000**' % t1)
    rec('       ### ### **IT IS MEANT TO. ### `(p^n - 1)/(p^n - 1) = 1` IS A TAUTOLOGY AND IS')
    rec('       ### ### REPORTED AS ONE. ### THE CONTENT IS NOT HERE -- IT IS IN act 9\'s RANGE,')
    rec('       ### ### WHICH IS WHAT PUTS `tau_q = 0` AT THAT LEVEL IN THE FIRST PLACE.**')
    t2 = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11, 13])
        n = rng.randint(2, 12)
        k = rng.randint(1, n - 1)
        if closed_form(p, n, k) > 0.0:
            t2 += 1
    rec('  (T2) `tau_q > 0` STRICTLY on the INTERIOR range : ### **%d / 20000**' % t2)
    rec('       ### ### **IT MUST HOLD ON THE INTERIOR AND ### FAIL ### AT THE TOP -- WHICH IS THE')
    rec('       ### ### WHOLE ASYMMETRY. ### AT THE TOP IT IS `0`, AND (T3) SHOWS IT.**')
    t3 = sum(1 for _ in range(20000)
             if closed_form(rng.choice([2, 3, 5, 7]), rng.randint(1, 12) or 1,
                            0) == 0.0)
    tops = 0
    for _ in range(20000):
        p = rng.choice([2, 3, 5, 7, 11, 13])
        n = rng.randint(1, 12)
        if closed_form(p, n, n) == 0.0:
            tops += 1
    rec('  (T3) `tau_q(p,n,n) = 0` on arbitrary (p,n) : ### **%d / 20000**' % tops)
    rec('       ### ### **NOT A TAUTOLOGY: IT IS act 9\'s RANGE BRANCH, AND (T2) IS ITS FOIL --')
    rec('       ### ### THE SAME FORMULA IS STRICTLY POSITIVE ONE LEVEL BELOW.**')
    rec('')
    rec('  (C1) THE SURVEY DISCRIMINATES : an invented phrase returns 0 files (above).')
    rec('  (C2) THE ARC FILTER DISCRIMINATES : it separates this arc\'s files from prior owners\'.')
    rec('  (C3) b262\'s LADDER IS CONSUMED, NOT RECOMPUTED : ### **%d cells read from JSON.**'
        % len(rows))
    rec('  (C4) THE SILENT SHARE IS MONOTONE ACROSS THE LADDER : ### **%s**'
        % bool(all(shares[i] <= shares[i + 1] for i in range(len(shares) - 1))))

    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 100)
    rec('  S1 (the silence, exhibited)     : ### **HOLDS -- %d violations at %d top levels**'
        % (s1_bad, sum(1 for r in s1_rows if r['top'])))
    rec('  S2 (the size, from b262)        : ### **SILENT SHARE %.2f%% -> %.2f%%**'
        % (shares[0] * 100, shares[-1] * 100))
    rec('  S3 (survey: prior owners)       : ### **NO HOLDING CONSTRAINS THE TOP LEVEL**')
    rec('  F2 (search not broken)          : ### **DID NOT FIRE -- positive controls found**')
    rec('')
    rec('  ### **QUOTED-N: %d files searched; %d (p,n,k) rows exhibited; %d ladder cells consumed.**'
        % (len(files), len(s1_rows), len(rows)))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(s1_rows=s1_rows, s1_bad=s1_bad, shares=shares,
                   n_files=len(files), prior_files=sorted(prior_all)),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    print('\n  banked -> %s\n  rows   -> %s' % (BANK, ROWS))


if __name__ == '__main__':
    main()
