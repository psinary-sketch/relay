# -*- coding: utf-8 -*-
"""b339_ledger.py -- THE UPDATE BLOCK ON THE FACES LEDGER, THROUGH ITS WRITER: ROW F2 AND ROW S1's CONSTITUENT K6.

### ### **ONE BLOCK, APPEND-ONLY, NAMING THE ROWS IT BEARS ON.** ### The exponent question priced under b322's sealed
### rule; UNAFFORDABLE at the sealed ceiling at every covered cell; the price banked; the cost census's price for
### F2 (b336) joined by this act's number. ### Every number read from `data/b339_price.json` and `data/b339_limit.json`
### at write time, never typed. ### NO GRADE MOVED. ### NO CANDIDATE PREFERRED.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
MARK = '<!-- b339 update -->'
RUN = os.path.join(D, 'b339_ledger_run.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def block_lines():
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b339_limit.json'), encoding='utf-8'))
    c = {k: P['cells'][k] for k in P['cells']}
    cell_txt = '; '.join('a = %s: rate `X^-%.3f` (rms %.3f; the last step `X^-%.3f`), `R(128)/s = %.2f`, `X_req = %.0f` (ratio %.2f to the reached `X = 128`; by the last step %.0f)'
                         % (k, c[k]['p'] * -1, c[k]['rms'], -c[k]['p_last'], c[k]['ratio_now'], c[k]['x_req'], c[k]['x_req'] / 128.0, c[k]['x_req_last'])
                         for k in sorted(c, key=float))
    lim_txt = '; '.join('a = %s: `m_inf` %.6f (by the last step %.6f), above the source\'s copy by %.2f s and the corpus\'s by %.2f s'
                        % (k, L[k]['m_inf'], L[k]['m_inf_last'], L[k]['off_ef'] / c[k]['s'], L[k]['off_er'] / c[k]['s']) for k in sorted(L, key=float))
    return ['', MARK, '',
            '## UPDATE \u2014 filed 2026-09-06 (b339): row F2 (the Sonin margin) and row S1, constituent K6 (the decomposition): the exponent priced, UNAFFORDABLE at the sealed ceiling',
            '',
            "*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer's `append_block`. A price is not a prediction (b322); no candidate is preferred; no grade is conferred; no bar moved.*",
            '',
            '| row / constituent | what b339 priced, under b322\'s sealed rule | the verdict, and the status |',
            '|:--|:--|:--|',
            "| **F2** (the Sonin margin) and **S1**, constituent **K6** (the decomposition: the compressed square plus the remainder) | THE EXPONENT PRICED: the identity residual `R(X) = (W_\u221e \u2212 Tr(X)) \u2212 INT` under the source's convention along b320's domain ladder (`X = 8 \u2026 128`, `N = 128X`, `NY = 512`), reproduced from the record at every covered cell, fitted by b322's own `fit_power`; the split criterion `R \u2264 s/2` with `s` the two copies' separation (b321's *apart by* column); the price `X_req = 128 (R(128)/(s/2))^(1/p)`, an extrapolation of a fitted slope and labelled as one; the ceiling `X = 512` (`N = 65536`) sealed before the price was computed. "
            + cell_txt + '. THE SIDE READING on the same five frames (not a verdict arm): the margin\u2019s descent fitted as `m_\u221e + C X^\u2212p` from its successive differences puts the limit ABOVE BOTH candidates at every cell \u2014 '
            + lim_txt + ' \u2014 so the residual the price extrapolates is descending toward a floor and not toward zero, and the price is an under-estimate. | **UNAFFORDABLE at the sealed ceiling at every covered cell; the price banked.** No frame was built; no remainder was evaluated at a new domain; NO CANDIDATE PREFERRED (the limit sits above both, and nearer the larger by exactly their separation, which is arithmetic and not a preference). The cost census\u2019s price for F2 (b336: the unit\u2019s domain factor `3.104e+02`; the exponent\u2019s ratio) is joined by this act\u2019s: the exponent\u2019s own domain factor `%.2f` at the widest separation and `%.2f` at the narrowest, before the floor is priced. K6 stays MEASURED-AT-COVERED-CELLS; F2 stays MEASURED, the sign certified and the size not certified; the exponent question stays UNDER-RESOLVED, NOT OPEN. The navigator\u2019s expectation (L1) (*the price fits and the identity prefers the source\u2019s convention*) NOT MET at this ceiling; this seat\u2019s (the price fits at a = 1.41 alone) NOT MET. The convention erratum E-2026-09-03-1 is untouched; its standing clause governs. |'
            % (c['1.41']['x_req'] / 128.0, c['1.3']['x_req'] / 128.0),
            '',
            '*Filed by b339 (relay `data/b339_the_exponent_resolved.txt`, `data/b339_price_run.txt`, `data/b339_limit_run.txt`). Nothing about totality, h2, or the roster. M-2 unchanged under its cap. The wave PARKED by the author\u2019s ruling.*']


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
    rec('=' * 100)
    rec('b339 -- THE UPDATE BLOCK ON THE FACES LEDGER (rows F2 and S1/K6), THROUGH THE WRITER.')
    rec('=' * 100)
    body = block_lines()
    st, det = W.append_block(MARK, body)
    rec('  FACES_LEDGER.md   b339 update   %-16s %s' % (st, det))
    txt = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    rec('  marks on disk : %d ; lines now : %d' % (txt.count(MARK), len(txt.splitlines())))
    ok = st in ('WRITTEN', 'DUPLICATE') and txt.count(MARK) == 1
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    rec('=' * 100)
    out = RUN if not os.path.exists(RUN) else RUN.replace('_run.txt', '_rerun.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
