# -*- coding: utf-8 -*-
"""b339_limit.py -- THE LIMIT READING ON THE EXISTING LADDER. ### A SIDE READING, LABELLED; NOT A VERDICT ARM.

### ### **WHY THIS FILE EXISTS.** ### The sealed verdict rule (registration (D), reading R2) fits the margin's descent
### `m(X) = W_inf - Tr(X)` as `m_inf + C X^(-p)` from the successive differences `d(X) = m(X) - m(2X)` and reads
### `m_inf` against the two candidates. ### That reading was sealed as part of the run at the priced domain, and the
### price did not fit the ceiling, so ### **NO VERDICT IS READ HERE.** ### What this file does is apply the same
### arithmetic to the FIVE FRAMES THE RECORD ALREADY HOLDS (b320's domain ladder), because the price tool's own
### output shows the fitted rate steepening toward `X^-1.0` at the last step, and the next pricing needs to know
### whether the residual `R = m - INT` is descending to zero or to a floor. ### No frame is built. ### Every number
### is read from `data/b339_price.json`, which read them from the record.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b322_ladder as LA        # noqa: E402  ### fit_power, IMPORTED never edited

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
RUN = os.path.join(D, 'b339_limit_run.txt')
OUT = os.path.join(D, 'b339_limit.json')


def main():
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    XS = P['xs']
    lines = []

    def rec(s=''):
        lines.append(s)

    rec('=' * 100)
    rec('b339 -- THE LIMIT READING ON THE EXISTING LADDER. ### A SIDE READING, LABELLED. ### NOT A VERDICT; NO FRAME BUILT.')
    rec('=' * 100)
    rec('  ### m(X) = W_inf - Tr(X) at X = %s (b320\'s five frames, read through b339_price.json);' % XS)
    rec('  ### d(X) = m(X) - m(2X) ; fit_power on d against X gives p ; m_inf = m(128) - d(64) 2^-p / (1 - 2^-p).')
    rec('  ### the candidates: INT_EF (the source\'s convention) and INT_ER (the corpus\'s); s their separation.')
    rec('')
    out = {}
    for key in sorted(P['cells'], key=float):
        c = P['cells'][key]
        m = c['margin']
        d = [m[i] - m[i + 1] for i in range(len(m) - 1)]
        xd = XS[:-1]
        p, A, rms = LA.fit_power(xd, d)
        q = 2.0 ** (-abs(p))
        m_inf = m[-1] - d[-1] * q / (1.0 - q)
        ratios = [d[i] / d[i + 1] for i in range(len(d) - 1)]
        p_last = math.log(d[-2] / d[-1]) / math.log(2.0)
        q2 = 2.0 ** (-p_last)
        m_inf_last = m[-1] - d[-1] * q2 / (1.0 - q2)
        ef, er, s = c['int_ef'], c['int_er'], c['s']
        rec('  ### a = %-5g   INT_EF = %.9f   INT_ER = %.9f   s = %.9f' % (float(key), ef, er, s))
        rec('    d(X) at X = %s : %s' % (xd, ['%.9f' % v for v in d]))
        rec('    successive ratios d(X)/d(2X) : %s   (a clean X^-p descent keeps them at 2^p)' % ['%.3f' % r for r in ratios])
        rec('    fitted p on d : %.6f (rms %.4f)   the last-step p : %.6f' % (abs(p), rms, p_last))
        rec('    m(128) = %.9f ; m_inf by the fitted p : %.9f ; by the last-step p : %.9f' % (m[-1], m_inf, m_inf_last))
        rec('    m_inf - INT_EF = %+.9f  (%.2f s) ; m_inf - INT_ER = %+.9f  (%.2f s)     [fitted p]' % (m_inf - ef, (m_inf - ef) / s, m_inf - er, (m_inf - er) / s))
        rec('    m_inf - INT_EF = %+.9f  (%.2f s) ; m_inf - INT_ER = %+.9f  (%.2f s)     [last-step p]' % (m_inf_last - ef, (m_inf_last - ef) / s, m_inf_last - er, (m_inf_last - er) / s))
        rec('')
        out[key] = dict(d=d, ratios=ratios, p=abs(p), rms=rms, p_last=p_last, m_inf=m_inf, m_inf_last=m_inf_last,
                        off_ef=m_inf - ef, off_er=m_inf - er, off_ef_last=m_inf_last - ef, off_er_last=m_inf_last - er)
    rec('  ### ### **WHAT THIS SAYS AND WHAT IT DOES NOT.** ### The descent\'s ratios fall from step to step, so the ladder')
    rec('  ### is not on a clean power law yet and `m_inf` is an extrapolation whose two readings disagree by the amount')
    rec('  ### printed; where both readings sit MANY SEPARATIONS from BOTH candidates, the residual the price tool')
    rec('  ### extrapolated is descending toward a floor and not toward zero, and a price computed from its slope is')
    rec('  ### an UNDER-estimate. ### NOT A VERDICT. ### NO CANDIDATE PREFERRED. ### REPORTED FOR THE NEXT PRICING.')
    rec('=' * 100)
    io.open(RUN, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(out, indent=1))
    print(chr(10).join(lines))
    return 0


if __name__ == '__main__':
    sys.exit(main())
