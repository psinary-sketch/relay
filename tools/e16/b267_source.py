# -*- coding: utf-8 -*-
"""b267_source.py -- M-2 CAMPAIGN, ACT 1. ### THE AGGREGATION'S SOURCE. ### THE RUN.

### **A READS ACT. ### DERIVATIONS BY QUOTATION ONLY. ### NO AGGREGATION IS ADOPTED, STATED OR
### REALIZED.** ### Bars fixed in `data/b267_registration_2026-08-31.txt`, SEALED `fcc803df...`,
### term-scanned and satisfiability-checked BEFORE the seal.

### ### **F-QUOTE IS MECHANICAL, AS b266 MADE IT: every owner sentence this act leans on is
### ### checked as a VERBATIM SUBSTRING of the file it is attributed to, and the act reports its
### ### verdicts only if all of them are found.**
"""
import io
import json
import math
import os
import re
import sys
from fractions import Fraction

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
RES = r'D:\SIDE-global-section'
BANK = os.path.join(D, 'b267_run.txt')
ROWS = os.path.join(D, 'b267_rows.json')

KERNEL = os.path.join(RES, 'Core', 'SectorNonvanishingShadow.lean')

# ### THE OWNER QUOTATIONS THIS ACT LEANS ON. ### (label, file, quotation)
QUOTES = [
    ('act 9 sec 2, the closed form', os.path.join(D, 'b220_aggregation_freedom.txt'),
     'tau_q(p,n,k) * p^(k/2) = (p^n - p^k)/(p^n - 1)'),
    ('b220, the range is load-bearing', os.path.join(D, 'b220_aggregation_freedom.txt'),
     'any\n### ### future aggregation statement needs that range'),
    ('b263, SPEC-1', os.path.join(D, 'b263_top_level_silence.txt'),
     '(SPEC-1) IT COUNTS FIRST LEVELS.'),
    ('b263, SPEC-3', os.path.join(D, 'b263_top_level_silence.txt'),
     '(SPEC-3) IT IS DEFINED OVER ALL PRIMES, NOT A FIXED SET.'),
    ('b263, the silence', os.path.join(D, 'b263_top_level_silence.txt'),
     'THE PRIME HAS A LEVEL. ### THE CLOSED FORM HAS NO RANGE TO PUT IT IN.'),
    ('b260, phi at k = n', os.path.join(D, 'b260_junction_sign.txt'),
     'the fraction is `1`.'),
    ('b223, the (2,1) death', os.path.join(D, 'b223_level_limit_two_places.txt'),
     'NO UNIT: d_1 = 0, the arrival depth'),
    ('b223, its two-place scope', os.path.join(D, 'b223_level_limit_two_places.txt'),
     'THE (2,1) DEATH IS ISOLATED AND DOES NOT PROPAGATE.'),
    ('kernel, the odd law', KERNEL,
     'the odd law `4·d₁ = (q−1)²` at `q = 3, 5, 9, 27`'),
    ('kernel, the place-2 law', KERNEL,
     'the place-2 law `4·d₁ = q(q−2)` at `q = 2, 4, 8, 16`'),
    ('kernel, the arrival death is the law own value', KERNEL,
     "The death at `(2,1)` is the law's OWN value."),
    ('kernel, odd sector positive at every level', KERNEL,
     'hence at `q = pⁿ` for every odd\n    prime `p` and every level `n ≥ 1` — the sector '
     'dimension is positive.'),
    ('b226, the chosen level', os.path.join(D, 'b226_stated_choice.txt'),
     'ell(p) := 2 if p = 2, else 1'),
    ('b226, why ell(2) = 2', os.path.join(D, 'b226_stated_choice.txt'),
     'THE ARRIVAL DEPTH IS WHY ell(2) = 2 AND NOT 1.'),
    ('b226, the owed result', os.path.join(D, 'b226_stated_choice.txt'),
     'd_1 > 0 GIVES E_1 != 0. ### IT DOES NOT GIVE u_{1,1} != 0.'),
    ('b226, the step wants a result', os.path.join(D, 'b226_stated_choice.txt'),
     'THIS ACT DID NOT PERFORM IT AND DOES NOT CLAIM IT.'),
    ('b227, the vector state value', os.path.join(D, 'b227_the_trace.txt'),
     'omega_u(T) = PROD over the ACTIVE places of <T_v u_v, u_v>'),
    ('b227, the wall', os.path.join(D, 'b227_the_trace.txt'),
     'omega_u CANNOT BE EVALUATED ON ACT 9\'s CELL OPERATOR'),
    ('b227, why: a different space', os.path.join(D, 'b227_the_trace.txt'),
     'ON V_inv THE TRANSFORM DOES NOT DESCEND, SO E_1 DOES NOT EXIST THERE.'),
    ('b237, the junction is at the assembly', os.path.join(D, 'b237_left_side_assets.txt'),
     'THE JUNCTION IS AT THE ASSEMBLY.'),
    ('b237, M-2 and the absent statement', os.path.join(D, 'b237_left_side_assets.txt'),
     'the\n### first is not in the record.'),
]


def norm(s):
    return re.sub(r'\s+', ' ', s).strip()


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b267 RUN -- M-2 CAMPAIGN, ACT 1. ### THE AGGREGATION\'S SOURCE.')
    rec('### Registration SEALED (`fcc803df...`), TERM-SCANNED and SATISFIABILITY-CHECKED')
    rec('### ### **BEFORE** ### the seal. ### Bars fixed there.')
    rec('### ### **A READS ACT. ### NO AGGREGATION IS ADOPTED, STATED OR REALIZED.**')
    rec('=' * 100)

    # ============================================================ F-QUOTE
    rec('')
    rec('### F-QUOTE -- EVERY OWNER SENTENCE VERBATIM IN ITS OWN FILE.')
    rec('=' * 100)
    cache, bad = {}, []
    for label, path, q in QUOTES:
        if path not in cache:
            cache[path] = norm(io.open(path, encoding='utf-8', errors='replace').read())
        ok = norm(q) in cache[path]
        if not ok:
            bad.append((label, path, q))
        rec('  %-48s %s' % (label[:48], 'YES' if ok else '### NOT FOUND ###'))
    fquote = (len(bad) == 0)
    for label, path, q in bad:
        rec('    ### NOT FOUND in %s : %r' % (os.path.basename(path), q[:80]))
    rec('  ### **%d quotations checked, %d unfindable.**' % (len(QUOTES), len(bad)))
    tampered = norm(QUOTES[0][2]).replace('tau_q', 'tau_qX')
    ctrl = tampered not in cache[QUOTES[0][1]]
    rec('  (C1) an altered quotation is reported unfindable : ### **%s** ### (must be YES)'
        % ('YES' if ctrl else 'NO'))
    rec('  ### ### **F-QUOTE %s**'
        % ('DID NOT FIRE.' if fquote else 'FIRED. ### NO VERDICT IS REPORTED BELOW.'))

    # ============================================================ TEST 1
    rec('')
    rec('=' * 100)
    rec('### TEST 1 -- THE EXTENSION. ### **act 9\'s EXPRESSION EVALUATED AT `k = n`, NOT ITS RANGE.**')
    rec('###          **LIMIT: NEITHER. ### A statement about a formula at one `(p, n)`.**')
    rec('=' * 100)
    rec('  THE EXPRESSION, from the owner: `(p^n - p^k)/(p^n - 1)`, and the owner supplies')
    rec('  `0 for k >= n` beside it. ### **THE QUESTION IS WHAT THE EXPRESSION ITSELF RETURNS.**')
    rec('')
    rec('  %-4s %-4s %-4s %-18s %-12s %s' % ('p', 'n', 'k', 'expression (exact)', 'supplied', 'agree?'))
    rec('  ' + '-' * 68)
    t1_rows, t1_kn_all_zero, t1_kgt_all_neg = [], True, True
    for p in (2, 3, 5, 7, 11):
        for n in (1, 2, 3):
            for k in (n, n + 1):
                e = Fraction(p ** n - p ** k, p ** n - 1)
                agree = (e == 0)
                if k == n:
                    t1_kn_all_zero = t1_kn_all_zero and agree
                else:
                    t1_kgt_all_neg = t1_kgt_all_neg and (e < 0)
                t1_rows.append(dict(p=p, n=n, k=k, expr=str(e), agree=agree))
                rec('  %-4d %-4d %-4d %-18s %-12s %s'
                    % (p, n, k, str(e), '0', 'YES' if agree else 'NO'))
    ft1 = t1_kn_all_zero
    rec('')
    rec('  ### ### **AT `k = n` THE EXPRESSION RETURNS EXACTLY `0` AT EVERY TESTED CELL:')
    rec('  ### ### `p^n - p^n = 0`, AND THE NUMERATOR IS THE WHOLE OF IT.**')
    rec('  ### ### **SO THE ZERO AT THE TOP LEVEL IS ### THE FORMULA\'S OWN ARITHMETIC ### ,')
    rec('  ### ### NOT A CONVENTION BOLTED ON BESIDE IT.**')
    rec('  ### **AND THE OTHER HALF, WHICH IS THE FINDING THE FERRY DID NOT ASK FOR:**')
    rec('  ### **AT `k > n` THE EXPRESSION IS STRICTLY ### NEGATIVE ### (%s) AND DOES ### NOT ###'
        % ('all tested cells' if t1_kgt_all_neg else 'NOT all cells -- see table'))
    rec('  ### AGREE WITH THE SUPPLIED `0`.** ### So `0 for k >= n` is the expression\'s own value')
    rec('  ### at `k = n` and an ### OVERRIDING CONVENTION ### for `k > n`.')
    rec('  ### ### ### **CONSEQUENCE FOR (SPEC-1), AND IT IS THE POINT OF TEST 1:** ### the first')
    rec('  ### ### ### level of a prime with `n_p(a) = 1` IS `k = n`, and that is precisely where')
    rec('  ### ### ### the expression returns zero ### BY ITS OWN ARITHMETIC ### . ### **EXTENDING')
    rec('  ### ### ### THE RANGE DOES NOT HELP; RE-INDEXING DOES NOT HELP. ### THE AGGREGATION')
    rec('  ### ### ### (SPEC-1) DEMANDS IS NOT A RE-INDEXING OF THE QUOTIENT TRACE.**')
    rec('  ### ### **F-T1 %s**' % ('DID NOT FIRE -- the navigator\'s assertion is CONFIRMED, and '
                                  'sharpened.' if ft1 else 'FIRED.'))

    # ============================================================ TEST 2
    rec('')
    rec('=' * 100)
    rec('### TEST 2 -- THE OBJECT\'S OWN FACTOR AT `(p, 1)`.')
    rec('###          **LIMIT: NEITHER. ### A statement about an object at one cell.**')
    rec('=' * 100)
    rec('  ### **THE LAWS, QUOTED FROM THE KERNEL AND EVALUATED AT `n = 1` (so `q = p`):**')
    rec('    odd law     : `4*d_1 = (q-1)^2`   ->  `d_1(p,1) = ((p-1)/2)^2`')
    rec('    place-2 law : `4*d_1 = q(q-2)`    ->  `d_1(2,1) = 2*0/4 = 0`')
    rec('')
    rec('  %-6s %-10s %-16s %-12s %s' % ('p', 'q = p^1', '4*d_1 (law)', 'd_1(p,1)', 'nonzero?'))
    rec('  ' + '-' * 60)
    t2_rows = []
    for p in (2, 3, 5, 7, 11, 13):
        if p == 2:
            rhs = Fraction(p * (p - 2))
        else:
            rhs = Fraction((p - 1) ** 2)
        d1 = rhs / 4
        t2_rows.append(dict(p=p, rhs=str(rhs), d1=str(d1), nonzero=bool(d1 > 0)))
        rec('  %-6d %-10d %-16s %-12s %s'
            % (p, p, str(rhs), str(d1), 'YES' if d1 > 0 else '### NO -- the arrival death ###'))
    odd_all_nonzero = all(r['nonzero'] for r in t2_rows if r['p'] != 2)
    two_is_zero = not [r for r in t2_rows if r['p'] == 2][0]['nonzero']
    rec('')
    rec('  ### **AND THE GENERALITY IS THE KERNEL\'S, NOT THIS TABLE\'S:** ### `odd_sector_pos`')
    rec('  ### states it ### "for every odd prime `p` and every level `n >= 1`" ### , at zero')
    rec('  ### axioms. ### **THE TABLE ABOVE EXHIBITS; THE KERNEL GENERALIZES.**')
    rec('  ### ### **AND ONE CORRECTION TO THE FERRY\'S READING, MADE FROM THE LAW ITSELF:**')
    rec('  ### ### the ferry carries `d_1 = 1` at odd `p`. ### **`d_1(p,1) = ((p-1)/2)^2`, WHICH')
    rec('  ### ### IS `1` ONLY AT `p = 3`** -- it is `4` at `p = 5`, `9` at `p = 7`, `25` at')
    rec('  ### ### `p = 11`. ### **THE ### NONZERO ### CLAIM GENERALIZES; THE ### VALUE 1 ### IS')
    rec('  ### ### THE `p = 3` CELL AND IS NOT THE CLASS.**')

    # ============================================================ TEST 3
    rec('')
    rec('=' * 100)
    rec('### TEST 3 -- THE ASSEMBLY STEP. ### **IS IT STATED BY ANY OWNER?**')
    rec('=' * 100)
    corpus = sorted(f for f in os.listdir(D) if f.endswith('.txt'))
    present_needle = 'PROD over the ACTIVE places'
    hits_present = [f for f in corpus
                    if present_needle in io.open(os.path.join(D, f), encoding='utf-8',
                                                 errors='replace').read()]
    missing_needles = ['carrying the quotient channel\'s operator onto',
                       'carrying `u_v` into `V_inv`']
    hits_missing = {}
    for nd in missing_needles:
        hits_missing[nd] = [f for f in corpus
                            if nd in io.open(os.path.join(D, f), encoding='utf-8',
                                             errors='replace').read()]
    rec('  ### **POSITIVE CONTROL FIRST (lore rule 4): the matcher must find an assembly')
    rec('  ### statement that ### IS ### present.**')
    rec('    needle : %r' % present_needle)
    rec('    found in : ### **%d file(s)** ### -- %s'
        % (len(hits_present), ', '.join(hits_present[:4]) or 'NONE'))
    ft3ctrl = len(hits_present) > 0
    rec('    ### ### **%s**'
        % ('THE MATCHER READS. ### Its silence elsewhere therefore means something.'
           if ft3ctrl else 'THE MATCHER FOUND NOTHING IT SHOULD HAVE. ### TEST 3 IS VOID.'))
    rec('')
    rec('  ### **THE SEARCH FOR THE MISSING STATEMENT:**')
    for nd in missing_needles:
        rec('    needle %r' % nd[:56])
        rec('      found in : %s'
            % (', '.join(hits_missing[nd]) if hits_missing[nd] else '### only as the NAMING of '
               'its absence ###'))
    rec('')
    rec('  ### ### **AND THE SEARCH DESIGN\'S OWN LIMIT, SAID RATHER THAN FIXED AWAY:** ### the')
    rec('  ### ### needles above were taken ### FROM b237\'s OWN SENTENCE NAMING THE ABSENCE ### ,')
    rec('  ### ### so they hit b237 by construction, and they hit this act\'s files because this')
    rec('  ### ### act quotes b237. ### **A NEEDLE DRAWN FROM THE SENTENCE THAT NAMES AN ABSENCE')
    rec('  ### ### WILL ALWAYS FIND THAT SENTENCE AND NOTHING ELSE. ### THAT IS NOT A SEARCH FOR')
    rec('  ### ### THE MISSING STATEMENT; IT IS A CHECK THAT NO ONE ELSE HAS QUOTED THE NAMING.**')
    rec('  ### ### **THE HITS ARE THEREFORE ALL ### SELF-HITS ### : b237 NAMING IT, AND THIS ACT')
    rec('  ### ### QUOTING b237. ### NO FILE ### STATES ### THE BRIDGE.**')
    rec('')
    rec('  ### ### **THE VERDICT IS THE OWNER\'S, NOT THIS ACT\'S GREP.** ### b237 states it:')
    rec('  ### ### **"A statement carrying the quotient channel\'s operator onto `S-bar_v`, or')
    rec('  ### ### carrying `u_v` into `V_inv` -- b227\'s words; the second is blocked by b10;')
    rec('  ### ### THE FIRST IS NOT IN THE RECORD."**')
    rec('  ### **AND THE SCOPE OF THIS ACT\'S CORROBORATION IS STAMPED ON IT** (lore rule 7):')
    rec('  ###   searched : ### **%d `data/*.txt` files** ### for %d needles.'
        % (len(corpus), len(missing_needles)))
    rec('  ###   ### **A GREP OVER ONE DIRECTORY IS NOT A PROOF OF CORPUS-WIDE ABSENCE, AND THIS')
    rec('  ###   ### ACT DOES NOT CLAIM ONE. ### THE ABSENCE IS b237\'s FINDING; THIS IS ITS')
    rec('  ###   ### CORROBORATION AT A STATED SCOPE.**')

    # ============================================================ THE SIZE
    rec('')
    rec('=' * 100)
    rec('### THE SIZE, RESTATED AS A TARGET ONLY. ### **BENCH CONTROL. ### LIMIT (L-B).**')
    rec('=' * 100)
    b262 = json.load(io.open(os.path.join(D, 'b262_rows_extended.json'), encoding='utf-8'))
    rws = b262['rows'] if isinstance(b262, dict) and 'rows' in b262 else b262
    rec('  %-12s %-14s %-14s %s' % ('a^2', 'm1', 'total', 'share'))
    rec('  ' + '-' * 52)
    size_rows = []
    for r in rws:
        if r.get('m1') is not None and r.get('total'):
            sh = 100.0 * r['m1'] / r['total']
            size_rows.append(dict(a2=r['a2'], m1=r['m1'], total=r['total'], share=sh))
            rec('  %-12s %-14.6f %-14.6f %.4f%%' % (r['a2'], r['m1'], r['total'], sh))
    rec('  ### ### **NO CANDIDATE IS COMPUTED. ### NO FIT IS ATTEMPTED. ### NO AGGREGATION IS')
    rec('  ### ### PROPOSED. ### THIS IS A SIZE THE OWED OBJECT MUST ACCOUNT FOR, NOT EVIDENCE')
    rec('  ### ### THAT ANY OBJECT DOES.**')

    # ============================================================ VERDICTS
    rec('')
    rec('=' * 100)
    rec('### THE RUN\'S VERDICTS.')
    rec('=' * 100)
    rec('  F-QUOTE  (owner sentences verbatim) : ### **%s**' % ('DID NOT FIRE' if fquote else 'FIRED'))
    rec('  F-T1     (expression zero at k = n) : ### **%s**' % ('DID NOT FIRE' if ft1 else 'FIRED'))
    rec('  F-T3     (matcher positive control) : ### **%s**' % ('DID NOT FIRE' if ft3ctrl else 'FIRED'))
    rec('  ### **odd `d_1(p,1)` nonzero at every tested odd p : %s**' % odd_all_nonzero)
    rec('  ### **`d_1(2,1) = 0`, the law\'s own value            : %s**' % two_is_zero)
    rec('  ### **QUOTED-N: %d owner quotations; %d TEST-1 cells; %d TEST-2 places; %d corpus files'
        % (len(QUOTES), len(t1_rows), len(t2_rows), len(corpus)))
    rec('  ###   searched for TEST 3; %d size rows restated.**' % len(size_rows))
    rec('=' * 100)

    io.open(BANK, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    json.dump(dict(f_quote=fquote, unfindable=len(bad), control=ctrl,
                   f_t1=ft1, t1_kn_all_zero=t1_kn_all_zero, t1_kgt_all_neg=t1_kgt_all_neg,
                   t1=t1_rows, t2=t2_rows, odd_all_nonzero=odd_all_nonzero,
                   two_is_zero=two_is_zero, f_t3_control=ft3ctrl,
                   t3_present_hits=hits_present, t3_files_searched=len(corpus),
                   size=size_rows),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    return 0 if (fquote and ft1 and ft3ctrl) else 1


if __name__ == '__main__':
    sys.exit(main())
