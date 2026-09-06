# -*- coding: utf-8 -*-
"""b340_ledger.py -- THE UPDATE BLOCK ON THE FACES LEDGER, THROUGH ITS WRITER: ROW L1 AND THE PAIR F1-L1.

### ### **ONE BLOCK, APPEND-ONLY, NAMING THE ROW AND THE PAIR IT BEARS ON.** ### The archimedean constituent of
### `W-ORD-LI-FAMILY-CONTROL` measured by the derived kernel on the Li family against the deposit's channel; the
### trail's remaining constituents (the zero side, the finite side) named and still OWED. ### Every number read from
### `data/b340_control.json` at write time, never typed. ### NO GRADE MOVED.
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
MARK = '<!-- b340 update -->'
RUN = os.path.join(D, 'b340_ledger_run.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def block_lines():
    J = json.load(io.open(os.path.join(D, 'b340_control.json'), encoding='utf-8'))
    idx = J['indices']
    G = json.load(io.open(os.path.join(D, 'b340_diagnose.json'), encoding='utf-8'))
    if J['holds_all']:
        verdict = '**A FOURTH CONTROL, AT ITS ARCHIMEDEAN CONSTITUENT** \u2014 the bar holds at all %d tabulated indices with the pole constant carried' % len(idx)
    else:
        verdict = ('**THE DIFFERING CONSTITUENT, AS SEALED: %s** \u2014 the bar fails at %d of %d indices because the drift between the two sealed quadratures exceeds it, while the identity `I(n) + 1 = \u03bb_A(n)` is within the bar by the theta route alone at %d of %d (worst %s). THE DIAGNOSIS, a reading beside the verdict and not in its place (relay `tools/b340_diagnose.py`): the drift lives entirely in the tail panel `[u_{n\u22121}, \u221e)` under the Gauss\u2013Legendre rule (the finite panels agree to zero; at n = 130 the tail differs by %s between the rules), and the same `u` route by tanh-sinh meets the sealed bar against the theta route at every diagnosed index (at n = 130 within %s) \u2014 the sealed refinement route, not the identity, is what failed; the bar as sealed is NOT MET and is not rewritten'
                   % (J['what'], len(idx) - J['n_hold'], len(idx), J['n_identity'], len(idx), J['worst_miss'], G['parts']['130']['tail_gl_minus_ts'], G['parts']['130']['u_ts_vs_theta']))
    return ['', MARK, '',
            '## UPDATE \u2014 filed 2026-09-06 (b340): row L1 (the Li-to-Weil bridge) and the pair F1\u2013L1 (`W-ORD-LI-FAMILY-CONTROL`): the archimedean constituent measured on the Li family',
            '',
            "*Rows above are never rewritten; an update names the row and the pair it bears on. Written through the writer's `append_block`. A control certifies the instrument, not the object; no grade is conferred; the Li family is not in the lawful class and the Sonin margin is not defined on it (b327, restated).*",
            '',
            '| row / pair | what b340 measured, per index | the verdict, and what stays owed |',
            '|:--|:--|:--|',
            "| **L1** and the pair **F1\u2013L1** (`W-ORD-LI-FAMILY-CONTROL`) | THE LI TEST FUNCTIONS built from the pinned source's (3.2) in the corpus's half-line normalization (`g_n(x) = \u03a3 C(n,j)(\u22121)^{j+1}(\u2212log x)^{j\u22121}/(j\u22121)!` on (0, 1]; its Mellin transform `G_n` re-measured, worst %s; on the line `Re G_n(\u00bd+iu) = 1 \u2212 (\u22121)^n cos(2n arctan 2u)`, worst %s) \u2014 NOT in the lawful class, three of three of Theorem 1's conditions failing (the support on all of (0, 1], `G_n(1) = 1`, a pole of order n at 0, not even). THE ARCHIMEDEAN DISTRIBUTION on them by the derived kernel `h_+(u) = Re \u03c8(\u00bc + iu/2) \u2212 log \u03c0` (b326, b333): `I(n) = (1/2\u03c0)\u222b Re G_n(\u00bd+iu) h_+(u) du` by two quadratures gated by the noise floor (worst drift %s), at the balance keystone's %d tabulated indices %s; against the deposit's channel `\u03bb_A(n)` by the bench's own definitions (two radii agreeing to %s) with the pole constant `L_n[log s] = 1` carried as its own column (worst `\u2212 1` of %s); b327's identity `\u03bb_A = S_\u221e + 1` as the bar (`1e-9 max(1, \u2223\u03bb_A\u2223)`), re-measured against the source's (4.11) at %s. Worst `\u2223I(n) + 1 \u2212 \u03bb_A(n)\u2223` = %s; against the keystone's printed column %s. The finite-range positivity restated at its scope beside the values: the margin `\u03bb_n = \u03bb_A + \u03bb_Z` positive at all %d indices (the keystone's column reproduced to %s); the certificate the deposit's (`partialPositivity_finiteRange`, v0.8.0, to Voros's `N\u2080(T) \u2248 2T\u00b2`, its premises named and open); positivity in a finite range not evidence of the kind the criterion respects (the bench's own sentence). | %s. WHAT STAYS OWED on `W-ORD-LI-FAMILY-CONTROL`: the zero side over the atlas's ordinates with its `O(n log T / T)` tail, and the finite side `S_f(n)` \u2014 neither evaluated here; the trail stays OWED at those constituents. `W-ORD-LI-WEIL-BRIDGE` untouched. NO GRADE MOVED; L1 stays IMPORTED and DERIVED with its corroboration extended by the kernel route; F1 stays MEASURED as a control on the arc's family. The navigator's (L2) (*the fourth control holds with the pole constant carried*): %s. |"
            % (J['worst_f1'], J['worst_f2'], J['worst_drift'], len(idx), idx, J['radii_worst'], J['pole_worst'], J['routeB_worst'], J['worst_miss'], J['worst_keystone'], len(idx), J['keystone_lamZ_worst'],
               verdict, 'MET at the archimedean constituent' if J['holds_all'] else 'NOT MET at the sealed bar (the refinement route failed the gate); the identity it names holds by one route at every index'),
            '',
            '*Filed by b340 (relay `data/b340_the_li_family_control.txt`, `data/b340_control_run.txt`). Nothing about totality, h2, or the roster. M-2 unchanged under its cap. The wave PARKED by the author\u2019s ruling.*']


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
    rec('=' * 100)
    rec('b340 -- THE UPDATE BLOCK ON THE FACES LEDGER (row L1, the pair F1-L1), THROUGH THE WRITER.')
    rec('=' * 100)
    body = block_lines()
    st, det = W.append_block(MARK, body)
    rec('  FACES_LEDGER.md   b340 update   %-16s %s' % (st, det))
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
