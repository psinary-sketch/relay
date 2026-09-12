# -*- coding: utf-8 -*-
"""b442_filings.py -- TWO UPDATE BLOCKS THROUGH THE WRITER'S `append_block`, GENERATED FROM THIS ACT'S RECORDS.

### ### (1) `<!-- b442 update: u0 -->` -- row S1, constituent K5, after b441's: the name with its quantifier.
### ### (2) `<!-- b442 update: site (v) -->` -- row U1, entry (v): the exhausted list.
### ### **EVERY QUOTATION VERIFIED BY THE WRITER'S `verify_quotes` FIRST; A MISS AND THAT BLOCK IS NOT FILED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
RUN = os.path.join(D, 'b442_filings_run.txt')
NL = chr(10)
SRC = {'b358_source_lagarias0404394.txt': os.path.join(D, 'b358_source_lagarias0404394.txt'),
       'b328_source_text.txt': os.path.join(D, 'b328_source_text.txt'),
       'b326_the_reach.txt': os.path.join(D, 'b326_the_reach.txt'),
       'FACES_LEDGER.md': os.path.join(PP, 'FACES_LEDGER.md')}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def esc(s):
    return s.replace('|', chr(92) + '|')


def main():
    rec('=' * 100)
    rec('b442_filings.py -- TWO BLOCKS THROUGH THE WRITER.')
    rec('=' * 100)
    th = json.load(io.open(os.path.join(D, 'b442_theta.json'), encoding='utf-8'))
    sv = json.load(io.open(os.path.join(D, 'b442_site_v.json'), encoding='utf-8'))
    comp = os.path.join(D, 'b442_components.txt')
    b440 = os.path.join(D, 'b440_components.txt')

    # ---------------------------------------------------------------- block 1
    if th.get('held'):
        q1 = [(SRC['b328_source_text.txt'], 'It is the derivative of 2', False),
              (SRC['b328_source_text.txt'], 'where this function is negative', False),
              (comp, 'COMPONENT 1 VERDICT : HOLDS, WITH ITS QUANTIFIER', False),
              (b440, 'IT AGREES AT 9 OF 10 CELLS', False)]
        miss = W.verify_quotes(q1)
        rec('  block u0 : quotations %d, misses %d %s' % (len(q1), len(miss), miss or ''))
        if not miss:
            body = [
                '<!-- b442 update: u0 -->', '',
                '## UPDATE — filed 2026-09-12 (b442): row S1, constituent K5 only — u0 named as the minimum of the Riemann–Siegel theta',
                '',
                '*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer’s `append_block`, directly after b441’s block, every quotation verified first. No grade is conferred by a seat.*',
                '',
                '| u0’s status | what the record holds | its grade, and where it comes from |',
                '|:--|:--|:--|',
                '| **name** | **u0 is the minimum of the Riemann–Siegel theta on `0 <= t <= 50`** — theta is odd, so there is no minimum on the whole line, and `-u0` is its maximum on `-50 <= t <= 0` | **DERIVES-ON-IMPORTS** — one line on K5’s import, *"It is the derivative of 2 θpτq, where θ is the Riemann-Siegel angular function"* (CC (153)–(154)): theta falls while `h+ < 0` and rises while `h+ > 0`. Checked at b442: the argmin found from theta’s values alone, never from `h+`, agrees with b440’s `u0` to `%.1e`; `h+` changes sign once on `(0, 50]`; theta is odd at five heights |' % th['argmin_gap'],
                '| **defining equation** | `Re psi(1/4 + iu/2) = log pi` | HELD (b439, b440) |',
                '| **classical asymptote** | `2 pi`, the zero of `log(u / 2 pi)` — which is not `u0` | HELD (b440) |',
                '| **closed form** | none | **NOT HELD** — a name is not a closed form |',
                '| **theta at u0** | `%s` | **MEASURED** by two routes sharing no code (`loggamma`; `quad` over `digamma`), agreeing to `%.1e`; **no verified source states the value**, and none is supplied from memory |' % (th['theta_B'][:22], th['route_gap']),
                '',
                '*The room’s mechanism in this vocabulary, with its qualifier kept: the archimedean slack on the seed family closes when half the seed’s transform mass lies above the height at which theta attains its minimum on `t >= 0` — **a heuristic, right at 9 of 10 cells and wrong for the second family at `a = 1.2`, exactly as b440 measured it**. A new vocabulary does not upgrade it. Filed by b442 (relay `data/b442_the_minimum.txt`).*',
            ]
            st, msg = W.append_block('<!-- b442 update: u0 -->', body)
            rec('  block u0 append_block : %s -- %s' % (st, msg))
    else:
        rec('  block u0 : Component 1 NOT HELD -- NOTHING FILED')

    # ---------------------------------------------------------------- block 2
    q2 = []
    for r in sv['candidates']:
        fn, ndl = r['quotes'][0]
        q2.append((SRC[fn], ndl, False))
    miss2 = W.verify_quotes(q2)
    rec('  block site (v) : quotations %d, misses %d %s' % (len(q2), len(miss2), miss2 or ''))
    if not miss2 and sv['held'] == 0:
        kinds = {}
        for r in sv['candidates']:
            kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
        body = [
            '<!-- b442 update: site (v) -->', '',
            '## UPDATE — filed 2026-09-12 (b442): row U1, entry (v) — the witness column’s exhausted list',
            '',
            '*Rows above are never rewritten; an update names the row it bears on. Written through the writer’s `append_block`. Row U1’s line, entry (v)’s `KIND: (b)` and `WITNESS: NONE KNOWN`, and the freeze at six (b409) stand as they read; no seventh site is entered.*',
            '',
            '| candidate | first failing step | the quoted step, and the reason |',
            '|:--|:--|:--|',
        ]
        for r in sv['candidates']:
            fn, ndl = r['quotes'][0]
            where = ('PLACE-papers `%s`' % fn) if fn.endswith('.md') else ('relay `data/%s`' % fn)
            body.append('| **%s** %s | %s — %s | *"%s"* (%s); %s |'
                        % (r['id'], esc(r['name']), r['step'], r['kind'], esc(ndl), where, esc(r['why'])))
        body += [
            '',
            '*%d candidates — the navigator’s opening list read as eight, and two supplied by description from the verified sources under a cap of six, every hit hand-read and the eleven non-candidates named with their reasons in relay `data/b442_components.txt`. **No witness held.** First failing steps: %s. The site’s own cell was quoted first and stands.*'
            % (len(sv['candidates']), '; '.join('%s %d' % kv for kv in sorted(kinds.items(), key=lambda x: -x[1]))),
            '',
            '*__At the scale the order set, the obstruction is membership, not uniformity.__ The corpus holds two objects, and over a finite class the maximum of the constants is one constant; every theorem in the verified sources that carries a representation-dependent constant assumes cuspidality, and the record measured that the Epstein function has no Euler product. The near-miss is Lagarias’s citation of a counting error *"with an absolute constant, which involves the analytic conductor"* — uniform across cuspidal representations, about the counting function rather than the finite-place sum, and outside the class for the second object.*',
            '',
            '*__The boundary count at five sites, read from banked JSON.__ Union of kinds across the four earlier sites %d, across all five %d; %d of %d of this site’s failures land at a kind an earlier site used, and it adds no new kind. And one transcription noted and not repaired: this row’s entry (v) writes Theorem 6.1 as `S_f(n,π) = λ_n(n,π) + O(n log n)`; the source reads `λn(√n,π∨) + O(√n log n)`. The dependence of the constant on π is the same in both. No grade is conferred, no bridge typed, nothing claimed about `h2`. The arc is checkpointed after (v). Filed by b442 (relay `data/b442_site_v.json`).*'
            % (sv['union_before'], sv['union_all'], len([r for r in sv['candidates'] if r['kind'] not in sv['new_kinds']]), len(sv['candidates'])),
        ]
        st2, msg2 = W.append_block('<!-- b442 update: site (v) -->', body)
        rec('  block site (v) append_block : %s -- %s' % (st2, msg2))
    else:
        rec('  block site (v) : NOT FILED')
    rec('=' * 100)
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)


if __name__ == '__main__':
    main()
