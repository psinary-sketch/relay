# -*- coding: utf-8 -*-
"""b679_onset.py -- COMPONENT 4, (R289)(5)(iv) AND (6), H5: n*' RECOMPUTED FROM THE WIDENED PROOF'S CONSTANTS, AND b675'S OBSERVATION RE-READ AS A TEST.

### Rows are the constants with their sources and n*'. The widened remainder's constant is read from the landed statement at the branch tip
### (SIDEExplicitFormula/Schema/Wide/Remainder.lean, Wide.remainder_le's witness, git show), not typed: C' = <its factor> · K, K the sum over the
### rest set as b675 banked it (relay data/b675_li_constants.json bench K, the 358 certified points outside D plus the tail under T-COUNT).
### R, s and c = Σ_D m² / (4 Σ_D m) = 1/4 as banked (sources: Schema/LiConverseCfg.lean :169-:170, :192; Schema/PowerSum.lean :222; the
### widened copy's lines in Schema/Wide/Converse.lean). n*' = the least n with 2 - c·Rⁿ + C'(n + 1)² sⁿ certified below 0 in Arb balls at
### 256 bits, the composition's line. The test: n_obs = 10034 (data/b675_li_bench.txt :848) ≤ n*'; and the window [n*', n*' + 200] re-read
### from the bench's rows along V4's subsequence (2cos(nθ) = Re Σ_D m wⁿ ≥ c), the count of those n and of NEG among them.
### Usage: `python -X utf8 tools/b679_onset.py <rev>` -> data/b679_onset.txt (.json). No lean; nothing in a kernel written.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
KE = 'D:/SIDE-explicit-formula'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import arb, ctx   # noqa: E402

PREC = 256
N_OBS = 10034


def main(rev):
    t0 = time.time()
    ctx.prec = PREC
    src = subprocess.run(['git', '-C', KE, 'show', '%s:SIDEExplicitFormula/Schema/Wide/Remainder.lean' % rev], capture_output=True).stdout.decode('utf-8')
    body = src[src.index('theorem remainder_le'):]
    m = re.search(r'refine ⟨(2 \* \(2 \+ 2 \* \(1 \+ s\) \^ 2\)) \* ∑\'', body)
    if not m:
        sys.exit('### THE WIDENED remainder_le`S WITNESS IS NOT OF THE PLANNED FORM -- NOTHING WRITTEN; read it by hand')
    factor_src = m.group(1)
    cj = json.load(io.open(os.path.join(D, 'b675_li_constants.json'), encoding='utf-8'))
    B = cj['bench']
    R, s, K, C675 = arb(B['R']), arb(B['s']), arb(B['K']), arb(B['C'])
    c = arb(1) / 4
    Cw = 2 * (2 + 2 * (1 + s) ** 2) * K
    same_C = Cw.overlaps(C675)
    n, nstar, expr = 1, None, None
    lnR, lns = R.log(), s.log()
    while n <= 200000:
        e = 2 - c * (n * lnR).exp() + Cw * arb(n + 1) ** 2 * (n * lns).exp()
        if e < 0:
            nstar, expr = n, e
            break
        n += 1
    # ### the window re-read from b675's bench rows along V4's subsequence
    rows = {}
    for l in io.open(os.path.join(D, 'b675_li_bench.txt'), encoding='utf-8'):
        mm = re.match(r'^\s+(\d+)\s+P \[.*?\]\s+U \[.*?\] P\+U \[.*?\]\s+(NEG|NONNEG|UNDECIDED)\s+2cos\(nθ\) (\[[^\]]+\])', l)
        if mm:
            rows[int(mm.group(1))] = (mm.group(2), arb(mm.group(3)))
    win = [k for k in range(nstar, nstar + 201)] if nstar else []
    have = [k for k in win if k in rows]
    on_sub = [k for k in have if rows[k][1] >= c]
    amb = [k for k in have if not (rows[k][1] >= c) and rows[k][1].overlaps(c)]
    neg_on = [k for k in on_sub if rows[k][0] == 'NEG']
    nonneg_on = [k for k in on_sub if rows[k][0] != 'NEG']
    L = ['b679 -- COMPONENT 4, (R289)(6), H5: n*` FROM THE WIDENED PROOF`S CONSTANTS, AND b675`S OBSERVATION RE-READ (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are the constants with their sources and n*`; Arb balls at %d bits.' % PREC, '',
         '  the remainder`s factor   %s -- read from Wide.remainder_le`s witness at %s (SIDEExplicitFormula/Schema/Wide/Remainder.lean), equal in form'
         % (factor_src, rev[:7]),
         '                           to v0.32`s (Schema/LiRemainder.lean :180-:181): the widened strip moved no constant of the bound (plan == 2 :12, :18)',
         '  K                        %s -- relay data/b675_li_constants.json bench K (K_cert over the 358 certified rest points + K_tail under T-COUNT)' % K.str(20),
         '  R                        %s -- bench R (Schema/LiConverseCfg.lean :169-:170; the widened copy`s same lines in Schema/Wide/Converse.lean)' % R.str(22),
         '  s                        %s -- bench s = (s1 + R)/2 (:192)' % s.str(22),
         '  c                        1/4 -- Σ_D m² / (4 Σ_D m), Σ_D m = 2 (Schema/PowerSum.lean :222)',
         '  C`                       %s -- the factor times K; b675`s C %s ; overlapping %s' % (Cw.str(20), C675.str(20), same_C),
         '  n*`                      %s -- the least n with 2 - c·Rⁿ + C`(n + 1)²sⁿ certified below 0; the expression there %s ; b675`s n* %s' % (
             nstar, expr.str(10) if expr is not None else '### NONE', B['n_star']), '',
         '### THE TEST (H5): n_obs = %d (data/b675_li_bench.txt :848) ≤ n*` = %s : %s.' % (N_OBS, nstar, bool(nstar and N_OBS <= nstar)),
         '### THE WINDOW [%s, %s] ALONG V4`S SUBSEQUENCE, re-read from the bench`s rows (2cos(nθ) = Re Σ_D m wⁿ against c = 1/4; data/b675_li_plan.txt :85-:89):' % (
             nstar, (nstar or 0) + 200),
         '    rows in the window %d ; on the subsequence (2cos(nθ) certified ≥ 1/4) %d ; NEG among them %d ; NONNEG or UNDECIDED among them %d %s ;' % (
             len(have), len(on_sub), len(neg_on), len(nonneg_on), nonneg_on[:10] or ''),
         '    balls straddling 1/4 %d %s ; b675`s whole-window line: NEG 102 of 201, the least NEG 63709 (:849).' % (len(amb), amb[:10] or ''),
         '    A NONNEG at an n on the subsequence at or past n*` would stand against the bound`s form: %s.' % ('NONE' if not nonneg_on else '### PRESENT'), '']
    ok = bool(nstar) and N_OBS <= nstar and not nonneg_on and len(have) == 201
    L += ['### ### **n*` %s (b675`s n* %s, C` OVERLAPPING b675`s C %s) ; n_obs %d ≤ n*` %s ; ON THE SUBSEQUENCE %d, NEG %d, OTHER %d ; H5 %s ; %d s.**' % (
        nstar, B['n_star'], same_C, N_OBS, bool(nstar and N_OBS <= nstar), len(on_sub), len(neg_on), len(nonneg_on), 'HELD' if ok else '### NOT HELD',
        int(time.time() - t0))]
    for name, data in (('b679_onset.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b679_onset.json', (json.dumps(dict(rev=rev, factor=factor_src, K=K.str(30), R=R.str(30), s=s.str(30), C=Cw.str(30),
                                                            same_C=same_C, n_star=nstar, n_star_675=B['n_star'], n_obs=N_OBS,
                                                            window=len(have), on_sub=len(on_sub), neg_on=len(neg_on), other_on=nonneg_on,
                                                            straddle=amb, h5='HELD' if ok else 'NOT HELD'), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        p = os.path.join(D, name)
        open(p + '.tmp', 'wb').write(data)
        os.replace(p + '.tmp', p)
    print(L[-1])


if __name__ == '__main__':
    main(sys.argv[1])
