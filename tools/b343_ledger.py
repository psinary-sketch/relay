# -*- coding: utf-8 -*-
"""b343_ledger.py -- THE UPDATE BLOCK ON THE FACES LEDGER, THROUGH ITS WRITER: ROW S1, CONSTITUENT K6.

### ### **ONE BLOCK, APPEND-ONLY, NAMING THE ROW AND THE CONSTITUENT IT BEARS ON.** ### The finer chart's verdict at the
### two reaching widths, and the identity residual's behaviour against the frame at one aimed seed, which prices K6's
### instrument. ### Every number read from `data/b343_crossing.json` and `data/b343_frames.json` at write time.
### ### **NO GRADE CONFERRED. ### A FINER CHART IS A FINER CHART.**
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
MARK = '<!-- b343 update -->'
RUN = os.path.join(D, 'b343_ledger_run.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def block_lines():
    C = json.load(io.open(os.path.join(D, 'b343_crossing.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b343_frames.json'), encoding='utf-8'))
    per = C['per_width']
    nar = '; '.join('a = %s: the room narrowest at \u03b3 = %.2f, `%+.9f`' % (a, per[a]['narrowest']['gamma'], per[a]['narrowest']['room_z']) for a in sorted(per, key=float))
    fr = F['frames']
    rankline = ('CONSTANT at %d' % fr[0]['rank']) if F['rank_constant'] else ('MOVED: %s' % sorted(set(r['rank'] for r in fr)))
    resid = ' \u2192 '.join('`%+.9f`' % r['R_EF'] for r in fr)
    return ['', MARK, '',
            '## UPDATE \u2014 filed 2026-09-06 (b343): row S1, constituent K6 (the decomposition): the finer chart between \u03b3 = 2 and 8, and the identity residual against the frame',
            '',
            "*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer's `append_block`. A finer chart is a finer chart; the residual's behaviour against the frame prices K6's instrument and moves no grade. No grade is conferred.*",
            '',
            '| row / constituent | what b343 measured | what it says, and what it does not |',
            '|:--|:--|:--|',
            "| **S1**, constituent **K6** (the decomposition: the compressed square plus the remainder) | THE FINER CHART: the aim-map's quantities at the thirteen heights \u03b3 = 2.0, 2.5, \u2026 8.0 \u2014 the interval b334's chart named narrowest at both reaching widths \u2014 at a = 40 and a = 81, by b334's own code imported and not edited (the archimedean distribution on two transforms with the (150) witness, the prime sum by two routes, the noise-floor gate on every sign), 26 aims. %s. The two heights this grid shares with b334's coarse one (\u03b3 = 4, \u03b3 = 8, both widths) reproduce its banked values to %s. THE RESIDUAL AGAINST THE FRAME: at one aimed seed (a = 1.41, \u03b3 = 33.650101, the covered point b334 named narrowest for the margin), the square on b319's stable cut at the reference frame and the two larger grid-axis frames \u2014 N = %s at fixed X = 32, NY = 512 \u2014 with the remainder under BOTH conventions, each named (the source's \u03c1^{+1/2}; the corpus's \u03c1^{\u22121/2}), per `E-2026-09-03-1`'s standing clause. The stable-cut rank is %s; the identity residual under the source's convention runs %s. | **%s.** The reaching widths are OUTSIDE the square's reach (X = 32 against a\u00b2 = 1600 and 6561) and outside the eps evaluator's reach (b334's finding, re-measured), so the square and the remainder were not evaluated there and nothing on this leg bears on them. **THE DRAFT'S EXPECTATION THAT THE RESIDUAL GROWS WITH RANK CANNOT BE SCORED ON THE AXIS THE DRAFT NAMES**: that axis holds the rank fixed and grows the grid. What the frames do establish is narrow and is stated as such: %s **NO GRADE MOVED; K6 STAYS MEASURED-AT-COVERED-CELLS; a chart is not a proof.** |"
            % (nar, ('%.3e' % C['shared_worst']), [r['frame'][0] for r in fr], rankline, resid, C['verdict'],
               ("the residual is unchanged across two doublings of N at fixed domain and rank (largest relative change %.3e), so **the grid resolution at fixed domain is not the origin of b339's floor**; the floor's other candidates \u2014 the fixed NY, the cut's \u03c4, the taper \u2014 are untouched by it."
                % max(F['rel_EF'], F['rel_ER'])) if F['unchanged'] else
               ("the residual changed across the doublings (largest relative change %.3e); the size is reported and nothing is concluded about b339's floor." % max(F['rel_EF'], F['rel_ER']))),
            '',
            "*Filed by b343 (relay `data/b343_the_maps_next_reach.txt`, `data/b343_crossing_run.txt`, `data/b343_frames_run.txt`). Nothing about totality, h2, or the roster. M-2 unchanged under its cap. The wave PARKED by the author's ruling.*"]


def main():
    lines = []

    def rec(s=''):
        lines.append(s)
    rec('=' * 100)
    rec('b343 -- THE UPDATE BLOCK ON THE FACES LEDGER (row S1, constituent K6), THROUGH THE WRITER.')
    rec('=' * 100)
    body = block_lines()
    st, det = W.append_block(MARK, body)
    rec('  FACES_LEDGER.md   b343 update   %-16s %s' % (st, det))
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
