# -*- coding: utf-8 -*-
"""b710_report.py -- THE CLOSING REPORT'S LINES (the ferry's Component 6), UNSEALED (data/b708_rules.txt row (1), carried).

### Written by the Write tool after the author's word at the root's prompt (2026-10-24, "Root: 1, proceed ... the report tool written and
### run with its five lines") and run before the root. It reads the act's banks and writes data/b710_report.txt (.json), one line each:
### (1) the principles' four rows (terminal, grade, control); (2) the moves tried and untried; (3) the readfirst recommendation; (4) the
### cost's top three files; (5) the four standing figures beside b709's; and (6) the author's order at the root's prompt, landed. Nothing
### else is written. `python -X utf8 tools/b710_report.py`.
"""
import io
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(n):
    p = os.path.join(D, n)
    return io.open(p, encoding='utf-8').read().replace(chr(13), '') if os.path.exists(p) else ''


def jl(n):
    t = rd(n)
    return json.loads(t) if t else {}


def need(m, what):
    if not m:
        sys.exit('### THE BANKS DO NOT CARRY %s -- NOTHING WRITTEN' % what)
    return m


def main():
    r5 = rd('b710_reading5.txt')
    v = ' '.join(' '.join(l[4:] if l.startswith('### ') else l for l in r5[r5.find('### ### **READING 5:'):].split(NL)).split())
    sec = ' '.join(r5[r5.find('## (i)'):r5.find('## (ii)')].split())
    counts = need(re.search(r'THE SECTION`?.S COUNTS: principles 4 ; with a compiled theorem consuming the principle, its grade read from the statement, '
                            r'(\d) of 4 \((.*?)\), the fourth \(I\) compiled as definitions alone ; with a control object (\d) of 4 \((.*?)\) ;', sec),
                  'the principles` counts (data/b710_reading5.txt :104-:108)')
    mv = need(re.search(r'THE MOVES TABLE (\d+) ROWS, TRIED (\d+), UNTRIED (\d+), MOVED (\d+), NARROWED (\d+), RE-PRESENTED (\d+), REAPPEARED (\d+)', v),
              'the moves` counts')
    fl = need(re.search(r'THE FLIP: (\d+) OF (\d+) DEFECTS CAUGHT, (\d+) PATHS DROPPED, (DO NOT FLIP|FLIP)', v), 'the flip')
    cj = jl('b710_r5_cost.json')
    top = (cj.get('top') or [])[:3]
    need(len(top) == 3, 'the cost`s top three (data/b710_r5_cost.json)')
    f10, f9 = jl('b710_standing_figures.json'), jl('b709_standing_figures.json')
    figs = [(k, (f10.get(k) or {}).get('figure'), (f9.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins')]
    need(all(a is not None and b is not None for _k, a, b in figs), 'the four figures')
    ol = (jl('b710_order_lines.json').get('lines') or [{}])[0]
    lines = [
        'THE PRINCIPLES (data/b710_reading5.txt :11-:111): S -- Focus.fe_symmetry (SIDE-kernel v1.8, Kernel/Focus.lean :34), DERIVES, control none located; '
        'I -- SIDEMeta.Independent (SIDE-meta v0.3) and techne_kernel.IndependentConstraints (SIDE-kernel v1.8), DEF, definitions alone as read, control '
        'located: Q0 and dh_witness (SieveCeilingWitness.lean :94) -- the row to be restated at b711 from the terminals the author named at the root`s '
        'prompt (W-ORD-READING5-INDEPENDENCE; defect (h)); D -- TypeLevel.determination_collapse (SIDE-kernel v1.8, Kernel/TypeLevel.lean :15), '
        'INTERFACES, control none located; E -- SIDE_exclusion, structural_exhaustiveness_proved, ostrowski_exhaustive and e_difficulty (SIDE-kernel '
        'v1.8), INTERFACES, control none located ; compiled %s of 4, with a control %s of 4' % (counts.group(1), counts.group(3)),
        'THE MOVES (data/b710_reading5.txt :113-:155): rows %s ; tried at the clause %s ; untried %s ((e), registered for b711) ; moved %s, narrowed %s, '
        're-presented %s, reappeared %s ; entered as W-ORD-MOVES-BY-LOCUS at OPEN_TRAILS :15804' % mv.groups(),
        'THE READFIRST FLIP (data/b710_reading5.txt :157-:177): %s of %s defects caught by the closure, %s prior paths dropped ; the recommendation %s, '
        'the hand list kept with the closure`s prior rows printed into it' % fl.groups(),
        'THE COST (data/b710_r5_cost.txt): %d lines in %d Read calls over b705-b709 ; the top three %s ; %s%% on carried tools' % (
            cj.get('volume'), cj.get('calls'), '; '.join('%s %s' % (t[0], t[1]) for t in top), re.search(r'([0-9.]+)% ON CARRIED', v).group(1)),
        'THE FIGURES (data/b710_standing_figures.txt against data/b709_standing_figures.json): %s' % ' ; '.join('%s b710 %s, b709 %s' % f for f in figs),
        'THE AUTHOR`S ORDER AT THE ROOT`S PROMPT: W-ORD-READING5-INDEPENDENCE landed at OPEN_TRAILS :%s (tools/b710_order.py through the record '
        'tool`s landing; data/b710_order_lines.json), trigger b711' % ol.get('line')]
    at = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    L = ['b710 -- THE CLOSING REPORT`S LINES, THE FERRY`S COMPONENT 6, BY THE UNSEALED tools/b710_report.py (%s)' % at,
         '### written after the author`s word at the root`s prompt and run before the root (data/b708_rules.txt row (1)); every figure read from the bank it names.', '']
    L += ['  (%d) %s' % (i, l) for i, l in enumerate(lines, 1)]
    L += ['', '### ### **REPORT LINES %d ; PRINCIPLES, MOVES, READFIRST, COST, FIGURES AND THE ORDER, EACH FROM ITS BANK.**' % len(lines)]
    for name, body in (('b710_report.txt', NL.join(L) + NL), ('b710_report.json', json.dumps(dict(at=at, lines=lines), indent=1, ensure_ascii=False) + NL)):
        p = os.path.join(D, name)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
