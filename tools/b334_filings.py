# -*- coding: utf-8 -*-
"""b334_filings.py -- ONE APPEND-ONLY FILING IN PLACE-papers, GENERATED FROM THE ACT'S OWN RECORDS.

### ### `FACES_LEDGER.md` -- an UPDATE block through the writer's `append_block` (b327_faces_row.py), naming row
### `S1` (constituents K5 and K6), row `F7` (the Epstein negative control) and b328's update block (the
### discriminating family), each with its per-aim status from the chart. ### No row is rewritten; no grade
### is conferred; the standing sentence that a chart is not a proof and that the quantifier stays unowned
### is in the block. ### Every value is read from `b334_chart.json`, `b334_grid.json` and the leg records;
### nothing is typed from memory of a run. ### One path, one run file, numbered on a repeat writing run.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
MARK_L = '<!-- b334 update -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def texts():
    ch = load('b334_chart.json')
    g = load('b334_grid.json')
    nav, seat = ch['navigator'], ch['seat']
    n_seeds = len(g['seeds'])
    n_lawful = sum(1 for r in g['seeds'] if r['lawful'])
    n_aims = sum(len(r['aims']) for r in g['seeds'])
    n_reached = sum(1 for r in g['seeds'] for q in r['aims'] if q['reached'])
    reach_rows = [b for b in ch['block'] if b['leg'] == 'reaching']
    cov_rows = [b for b in ch['block'] if b['leg'] == 'covered']
    neg = sum(1 for b in reach_rows if b['sign_z'] == '-')
    narrow = '; '.join('%s: gamma %.6f, %+.6f' % (k, v['gamma'], v['room']) for k, v in sorted(ch['narrowest'].items()))
    cross = '; '.join('a = %g, gamma %.6f (places_q %+.6f)' % (a, gm, p) for (_leg, a, gm, p) in ch['crossing']) or 'EMPTY'
    heights = '; '.join('%s: %s' % (h, v if v else 'NONE') for h, v in ch['contains'].items())
    tr_range = (min(b['Tr'] for b in cov_rows), max(b['Tr'] for b in cov_rows))
    margin_range = (min(b['margin'] for b in cov_rows), max(b['margin'] for b in cov_rows))
    faces = [
        '', MARK_L, '',
        '## UPDATE — filed 2026-09-06 (b334): row S1 (constituents K5 and K6), row F7, and b328\'s update (the discriminating family)',
        '',
        '*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer\'s `append_block`. A chart is not a proof; the quantifier K8 stays unowned; no grade is conferred — the softest pair gains a behaviour over aims, not a grade.*',
        '',
        '| row / constituent | what b334 charted, per aim | the status over aims |',
        '|:--|:--|:--|',
        '| **S1**, constituents **K5** (the archimedean distribution) and **K6** (the decomposition) | THE AIM-MAP: b328\'s sine-aimed even seed built at every height of the sealed grid (γ over %d heights, β over %d abscissae from the line to the first Epstein off-line zero\'s) at the reaching widths a = 40, 81 and the covered widths a = 1.3, 1.41; %d of %d seeds lawful by Definition 3.1 and the pole conditions; the phase at %d of %d aims past the 45° threshold (every reaching-leg aim off the line; none on the covered leg). For ζ, on f = E ⋆ E♯ at every (γ, a): the archimedean distribution by the derived kernel on two transforms and by the principal-value witness (150), the prime sum by two routes, the places side gated (refine 1 against 4); on the covered leg also the square on the stable cut at two frames (Tr from %.6f to %.6f) and the remainder integral by two quadratures, the identity residual printed per aim. | K5 over aims: A_z certified at every aim, negative on the reaching leg and positive on the covered leg (like for like, by name); its per-aim convergence s5 printed. K6 over aims: margin A_z − Tr from %.6f to %.6f on the covered leg, the square and the remainder NOT REACHED on the reaching leg (the frame\'s X = 32 against a² = 1600, 6561; the eps evaluator past ρ = 100, measured). **Soften together: Spearman(s5, s6) = %+.4f — (F3) %s.** The narrowest points of the room: %s. **(F1) the prime sum inside the margin at every aim: %s** (places_z certified negative at %d of %d reaching aims). |'
        % (len(g['gammas']), len(g['betas']), n_lawful, n_seeds, n_reached, n_aims, tr_range[0], tr_range[1], margin_range[0], margin_range[1],
           ch['spearman_s5_s6'], nav['F3'], narrow, nav['F1'], neg, len(reach_rows)),
        '| **F7** (the Epstein negative control) and **b328\'s update** (the discriminating family) | THE SAME FOUR FOR Z_Q at every aim: the archimedean channel by the derived kernel on two transforms (b325\'s halved kernel printed beside, unused), the finite side with the representation numbers by two Λ_Q routes, the places side gated; the square and the remainder for Z_Q are NOT AN INSTRUMENT THE RECORD HAS, said on every line. | THE CROSSING REGION (places_q certified positive with no zero used): %s. Against the off-line zeros\' heights on the grid: %s. **(F2) the crossing region contains the banked off-line zeros\' aims: %s.** The negative control charted, and nothing more. |'
        % (cross, heights, nav['F2']),
        '',
        '*A chart is not a proof. The quantifier stays unowned. Nothing about totality, h2, or the roster. M-2 unchanged under its cap. Filed by b334 (relay `data/b334_the_aim_map.txt`).*',
    ]
    return faces, ch


def main():
    fails = []
    rec('=' * 100)
    rec('b334 -- THE FILING. ### THE LEDGER UPDATE THROUGH THE WRITER.')
    rec('=' * 100)
    faces, ch = texts()
    rec('  read from the chart record : navigator %s ; seat %s ; crossing members %d' % (ch['navigator'], ch['seat'], len(ch['crossing'])))
    st, det = W.append_block(MARK_L, faces)
    rec('  FACES_LEDGER.md   %-16s %s' % (st, det))
    if st not in ('WRITTEN', 'DUPLICATE'):
        fails.append('FACES_LEDGER')
    st2 = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    rec('  git status over outputs/DEPOSITED-v1.1.2 : %r ; THE DEPOSIT IS BYTE-UNCHANGED : %s' % (st2, not st2))
    if st2:
        fails.append('DEPOSIT')
    rec('  ### FILING CHECKS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    code = main()
    wrote = any('WRITTEN' in x for x in LINES)
    base = 'b334_filings_run' if wrote else 'b334_filings_rerun'
    k, name = 1, base + '.txt'
    while os.path.exists(os.path.join(D, name)):
        k += 1
        name = '%s%d.txt' % (base, k)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    sys.exit(code)
