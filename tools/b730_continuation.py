# -*- coding: utf-8 -*-
"""b730_continuation.py -- THE GRADE OF THE continuation FIELD, (R340)(4), N1, N3. ### READS THE DISPATCH ROWS AND zq-b730 AT ITS TIP; WITH --bank WRITES data/b730_continuation.txt AND .json ALONE.

### The grade is computed, not typed: CLOSED is a read row of exit 0, no sorryAx, the two terminals each at the standard three in the artifact's own lines, and no `sorry` or
### `axiom` in the field's modules at the tip; anything else is OPEN at the last group. The conclusion of the run is printed and read by nothing: the exit file governs (b729's
### (5), and this act's own first read). The controls print before the figures (N2).
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
EF = 'D:/SIDE-explicit-formula'
BRANCH = 'zq-b730'
BASE = 'badacccb867e5c8bab8ec4ff240c30e7e9d7f3fe'
CAP = 12
THREE = '[propext, Classical.choice, Quot.sound]'
NS = 'SIDEExplicitFormula.Schema.ZQ.'
TERMINALS = ('zq_continuation', 'exists_zq_continuation')
MODULES = ('Lattice', 'Theta', 'FEPair', 'Continuation')
PLAN = (('A', 'Lattice', 200), ('B', 'Theta', 150), ('C', 'FEPair', 150), ('D', 'Continuation', 215))   # ### data/b730_continuation_plan.txt :21-:35, summed by group
CLAUSES = (('summable', 'zq_summable', 'Schema/ZQ/Lattice.lean'), ('agrees', 'zqFn_agrees', 'Schema/ZQ/Continuation.lean'), ('holomorphic', 'zqFn_holomorphic', 'Schema/ZQ/Continuation.lean'),
           ('functional_equation', 'zqFn_functional_equation', 'Schema/ZQ/Continuation.lean'), ('real_on_real', 'zqFn_real', 'Schema/ZQ/Continuation.lean'))


def git(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


def grade(rows, srcs):
    """pure: (CLOSED or OPEN, the reason). rows the dispatch rows, srcs the field's modules' text at the tip."""
    reads = [r for r in rows if r.get('kind') == 'read']
    if not reads:
        return 'OPEN', 'no read'
    last = reads[-1]
    if str(last.get('build_exit')) != '0':
        return 'OPEN', 'the last read`s exit %s' % last.get('build_exit')
    if last.get('sorryAx'):
        return 'OPEN', 'sorryAx in the axiom print'
    for t in TERMINALS:
        if not any(("'%s%s' depends on axioms: %s" % (NS, t, THREE)) in l for l in last.get('axioms_lines') or []):
            return 'OPEN', '%s not at the standard three' % t
    for n, s in srcs.items():
        if re.search(r'(?m)^\s*(axiom\b|.*\bsorry\b)', s):
            return 'OPEN', '%s carries sorry or axiom' % n
    return 'CLOSED', 'exit 0 ; the two terminals at the standard three ; no sorry'


def controls(rows, srcs):
    ok_axioms = ["'%s%s' depends on axioms: %s" % (NS, t, THREE) for t in TERMINALS]
    good = [dict(kind='read', build_exit='0', conclusion='success', sorryAx=False, axioms_lines=ok_axioms)]
    src = {'X': 'theorem a : True := trivial'}
    cases = [('a read of exit 0, the two terminals at the three, a clean source', good, src, 'CLOSED'),
             ('the conclusion success with build exit 1 (b729`s (5), this act`s run 41292290796)', [dict(good[0], build_exit='1')], src, 'OPEN'),
             ('a sorryAx in the print', [dict(good[0], sorryAx=True)], src, 'OPEN'),
             ('a terminal at the three plus sorryAx in its line', [dict(good[0], axioms_lines=[ok_axioms[0], ok_axioms[1].replace('Quot.sound]', 'Quot.sound, sorryAx]')])], src, 'OPEN'),
             ('one terminal missing from the print', [dict(good[0], axioms_lines=ok_axioms[:1])], src, 'OPEN'),
             ('a `sorry` in the source at the tip', good, {'X': 'theorem a : True := by' + NL + '  sorry'}, 'OPEN'),
             ('an `axiom` in the source at the tip', good, {'X': 'axiom a : True'}, 'OPEN'),
             ('no read at all', [], src, 'OPEN')]
    out, n = [], 0
    for what, r, s, want in cases:
        got = grade(r, s)[0]
        n += got == want
        out.append('  %-82s %-6s %s' % (what, got, 'AS WANTED' if got == want else 'NOT AS WANTED'))
    return out, n, len(cases)


def main():
    rows = json.load(open(os.path.join(D, 'b730_dispatch_rows.json'), encoding='utf-8'))
    tip = git('rev-parse', 'refs/heads/' + BRANCH).strip()
    rem = git('rev-parse', 'refs/remotes/origin/' + BRANCH).strip()
    srcs = dict((m, git('show', '%s:SIDEExplicitFormula/Schema/ZQ/%s.lean' % (tip, m))) for m in MODULES)
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    lines = dict((m, len(s.split(NL)) - 1) for m, s in srcs.items())
    total = sum(lines.values())
    L = ['b730 -- THE continuation FIELD, ITS GRADE, (R340)(4), N1, N3 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### The statement: ZQContinuation at Schema/EpsteinZQ.lean :80-:86, the field `continuation` of ZQPremises at :138. Branch %s of SIDE-explicit-formula, cut from main %s, tip %s, read back at origin %s.' % (BRANCH, BASE[:8], tip[:8], rem == tip), '']
    L += ['## THE CONTROLS FIRST (the grade`s own predicate, on planted rows)']
    c, cn, ct = controls(rows, srcs)
    L += c + ['  CONTROLS %d OF %d AS WANTED' % (cn, ct), '']
    L += ['## THE DISPATCHES, EACH BY ITS RUN ID (the conclusion printed and governing nothing; relay data/b730_dispatch_rows.json)']
    for r in reads:
        L.append('  %d  %-12s run %s  ref %s  conclusion %s  build exit %s  %s  free before %d MB  runner low %s MB%s' % (
            r['n'], r['item'], r['run'], r['built_ref'][:8], r['conclusion'], r['build_exit'], r['verdict'], r['free_mb'], r['runner_low_mb'],
            ''.join(NL + '       error: ' + e for e in r.get('errors') or [])))
    L += ['', '## THE LINES, MODULE BY MODULE AGAINST THE PLAN (data/b730_continuation_plan.txt)']
    for g, m, p in PLAN:
        L.append('  group %s  %-13s %4d lines ; planned about %d ; dispatches %d' % (g, m, lines[m], p, sum(1 for r in disp if r.get('item') == '(4) group ' + g)))
    L += ['  THE SUM %d LEAN LINES ; print_targets.txt 11 lines beside them' % total,
          '  against the prices: the bank`s 1,500-3,000 lines and 25-50 dispatches (data/b729_count_price.txt :21) ; the re-price`s 500-900 lines and 8-12 dispatches (data/b730_stepzero.txt :43) ; the plan`s about 715 lines and 5-12 ;',
          '  spent %d lines and %d dispatches. Every estimate was the seat`s; the b729 bank`s stood high by about two to four times on lines and four to eight on dispatches, the route through Mathlib`s even kernel being the difference.' % (total, len(disp)), '']
    L += ['## THE CLAUSES OF ZQContinuation, EACH A THEOREM']
    last = reads[-1] if reads else {}
    al = last.get('axioms_lines') or []
    for f, t, where in CLAUSES:
        line = [l for l in al if ("'%s%s' depends on axioms" % (NS, t)) in l]
        L.append('  %-20s %-26s %-30s %s' % (f, t, where, line[0].split(': ', 1)[1] if line else 'NOT PRINTED'))
    L += ['', '## THE AXIOM PRINT OF THE TERMINALS, THE ARTIFACT`S OWN LINES (run %s, out/axioms.txt)' % last.get('run')]
    L += ['  ' + l for l in al if any(("'%s%s'" % (NS, t)) in l for t in ('thetaU_inversion', 'thetaC_feq') + TERMINALS)]
    L += ['  the workflow`s name grammar passes ASCII names alone: zqPair_Λ_one_sub and zqPair_Λ_eq_of_re, in print_targets.txt, did not reach out/Axioms.lean (not in out/axioms.txt); each stands in the closure of zq_continuation, which printed.',
          '  the print`s other lines, `Unknown constant` for names of modules the target does not import, are the carried list`s and not this field`s.', '']
    L += ['## WHAT THE THEOREM IS NOT',
          '  zq_continuation says ZQContinuation zqFn and no more: one field of the five of ZQPremises. The fields logDeriv, zeros, count and explicitFormula stay named premises; the instance`s theorems still bind them; the instance`s grade does not move.',
          '  It proves no zero`s place, RH or GRH. Its functional equation is the clause`s, on the open strip; holomorphy off 1 is the clause`s and nothing is claimed of the pole at 1. The file is on the branch alone: not on main, no tag.', '']
    g, why = grade(rows, srcs)
    sorry = [m for m, s in srcs.items() if re.search(r'\bsorry\b', s)]
    res = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), grade=g, why=why, tip=tip, remote_equal=rem == tip, dispatches=len(disp), cap=CAP, lines=total, lines_by_module=lines,
               sorry=sorry, terminals=list(TERMINALS), controls=[cn, ct], runs=[r['run'] for r in disp])
    if g == 'CLOSED':
        L.append('### ### **THE continuation FIELD CLOSED: zq_continuation AND exists_zq_continuation COMPILED ; AXIOMS propext, Classical.choice, Quot.sound ; NO sorry ; DISPATCHES %d OF AT MOST %d ; LINES %d ; ONE FIELD OF FIVE, FOUR OPEN.**' % (len(disp), CAP, total))
    else:
        L.append('### ### **THE continuation FIELD OPEN (%s) ; DISPATCHES %d OF AT MOST %d ; LINES %d ; ONE FIELD OF FIVE, FOUR OPEN.**' % (why, len(disp), CAP, total))
    t = NL.join(L) + NL
    print(t)
    if '--bank' in sys.argv:
        with open(os.path.join(D, 'b730_continuation.txt'), 'w', encoding='utf-8', newline=NL) as fh:
            fh.write(t)
        with open(os.path.join(D, 'b730_continuation.json'), 'w', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(res, ensure_ascii=False, indent=1) + NL)
        print('written data/b730_continuation.txt and .json')
    return 0 if g in ('CLOSED', 'OPEN') and cn == ct else 1


if __name__ == '__main__':
    sys.exit(main())
