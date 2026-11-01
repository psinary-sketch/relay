# -*- coding: utf-8 -*-
"""b731_fields.py -- THE GRADES OF THE logDeriv AND zeros FIELDS, (R341)(3)-(4), N1, N3. ### READS THE DISPATCH ROWS AND zq-b730 AT ITS TIP; WITH --bank WRITES data/b731_<field>.txt AND .json ALONE.

### b730_continuation.py's predicate, one tool for the two fields: CLOSED is a read row of exit 0 for the field, no sorryAx, every terminal at the standard three in the artifact's own lines,
### and no `sorry` or `axiom` in the field's modules at the tip; anything else is OPEN. The conclusion of the run is printed and read by nothing: the exit file governs. The controls print before the figures (N2).

  python -X utf8 -u tools/b731_fields.py logderiv [--bank]
  python -X utf8 -u tools/b731_fields.py zeros [--bank]
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
ENTERING = '5688816e'
CAP = 6
THREE = '[propext, Classical.choice, Quot.sound]'
NS = 'SIDEExplicitFormula.Schema.ZQ.'
FIELDS = dict(
    logderiv=dict(name='logDeriv', item='(3)', terminals=('zq_logDeriv', 'zq_ne_zero_of_three_halves_le', 'cQ', 'zq_three_halves_tsum_lt'), modules=('Bound', 'LogDeriv'),
                  plan='data/b731_logderiv_plan.txt', planned='about 430 lines, 3-6 dispatches', bank='200-400 lines, 3-8 dispatches (data/b729_count_price.txt :23)',
                  statement='ZQPremises.logDeriv at Schema/EpsteinZQ.lean :140',
                  claus=(('the coefficients', 'cQ', 'Schema/ZQ/LogDeriv.lean'), ('the hypothesis Z_Q(3/2) < 4', 'zq_three_halves_tsum_lt', 'Schema/ZQ/Bound.lean'),
                         ('no zero in Re s >= 3/2', 'zq_ne_zero_of_three_halves_le', 'Schema/ZQ/LogDeriv.lean'), ('the series on Re s >= 3/2', 'zq_logDeriv', 'Schema/ZQ/LogDeriv.lean')),
                  isnot=['zq_logDeriv says ZQPremises.logDeriv for zqFn and cQ and no more. The series is -Z`/Z on Re s >= 3/2 and nothing is claimed left of that line. cQ is real by construction; its sign, its size and any Euler form are not stated.',
                         'zq_three_halves_lt bounds one number: Z_Q(3/2) < 4 from above. The figure 3.9867 stands in the plan and the float control, not in the theorem. The zero-free half-plane is Re s >= 3/2 alone; it locates no zero and proves no RH or GRH.']),
    zeros=dict(name='zeros', item='(4)', terminals=('zq_zeros', 'exists_zq_zeros', 'zqZeroConfig', 'zq_conj'), modules=('Zeros',),
               plan='data/b731_zeros_plan.txt', planned='about 340 lines, 2-6 dispatches', bank='300-600 lines, 5-10 dispatches (data/b729_count_price.txt :22)',
               statement='ZQPremises.zeros at Schema/EpsteinZQ.lean :139, ZQZeros at :99-:101',
               claus=(('Schwarz reflection off 1', 'zq_conj', 'Schema/ZQ/Zeros.lean'), ('the configuration', 'zqZeroConfig', 'Schema/ZQ/Zeros.lean'), ('ZQZeros zqFn zqZeroConfig', 'zq_zeros', 'Schema/ZQ/Zeros.lean'),
                      ('the existential', 'exists_zq_zeros', 'Schema/ZQ/Zeros.lean')),
               isnot=['zq_zeros says ZQZeros zqFn zqZeroConfig and no more: the zeros of Lambda_Q off 0, 1 and the trivial zeros, with their orders, form a WideConfig. It does not say the carrier is nonempty, counts nothing, and places no zero on any line.',
                      'The strip is the open (-1/2, 3/2) the class asks for, not the critical strip. Wide.HCount, the field count, and Wide.HExcl are not touched. It proves no RH or GRH.']))


def git(*a):
    return subprocess.run(['git', '-C', EF] + list(a), capture_output=True, text=True, encoding='utf-8').stdout


def grade(rows, srcs, terminals):
    """pure: (CLOSED or OPEN, the reason). rows the field's dispatch rows, srcs the field's modules' text at the tip."""
    reads = [r for r in rows if r.get('kind') == 'read']
    if not reads:
        return 'OPEN', 'no read'
    last = reads[-1]
    if str(last.get('build_exit')) != '0':
        return 'OPEN', 'the last read`s exit %s' % last.get('build_exit')
    if last.get('sorryAx'):
        return 'OPEN', 'sorryAx in the axiom print'
    for t in terminals:
        if not any(("'%s%s' depends on axioms: %s" % (NS, t, THREE)) in l for l in last.get('axioms_lines') or []):
            return 'OPEN', '%s not at the standard three' % t
    for n, s in srcs.items():
        if not s.strip():
            return 'OPEN', '%s absent at the tip' % n
        if re.search(r'(?m)^\s*(axiom\b|.*\bsorry\b)', s):
            return 'OPEN', '%s carries sorry or axiom' % n
    return 'CLOSED', 'exit 0 ; every terminal at the standard three ; no sorry'


def controls(terminals):
    ok = ["'%s%s' depends on axioms: %s" % (NS, t, THREE) for t in terminals]
    good = [dict(kind='read', build_exit='0', conclusion='success', sorryAx=False, axioms_lines=ok)]
    src = {'X': 'theorem a : True := trivial'}
    cases = [('a read of exit 0, every terminal at the three, a clean source', good, src, 'CLOSED'),
             ('the conclusion success with build exit 1 (this act`s runs 41316031450, 41316963968)', [dict(good[0], build_exit='1')], src, 'OPEN'),
             ('a sorryAx in the print', [dict(good[0], sorryAx=True)], src, 'OPEN'),
             ('a terminal at the three plus sorryAx in its line', [dict(good[0], axioms_lines=ok[:-1] + [ok[-1].replace('Quot.sound]', 'Quot.sound, sorryAx]')])], src, 'OPEN'),
             ('one terminal missing from the print', [dict(good[0], axioms_lines=ok[:-1])], src, 'OPEN'),
             ('a `sorry` in the source at the tip', good, {'X': 'theorem a : True := by' + NL + '  sorry'}, 'OPEN'),
             ('an `axiom` in the source at the tip', good, {'X': 'axiom a : True'}, 'OPEN'),
             ('a module absent at the tip', good, {'X': ''}, 'OPEN'),
             ('no read at all', [], src, 'OPEN')]
    out, n = [], 0
    for what, r, s, want in cases:
        got = grade(r, s, terminals)[0]
        n += got == want
        out.append('  %-86s %-6s %s' % (what, got, 'AS WANTED' if got == want else 'NOT AS WANTED'))
    return out, n, len(cases)


def main():
    key = sys.argv[1]
    F = FIELDS[key]
    allrows = json.load(open(os.path.join(D, 'b731_dispatch_rows.json'), encoding='utf-8'))
    rows = [r for r in allrows if str(r.get('item', '')).startswith(F['item']) or r.get('kind') == 'push' and any(c.get('sha') == r.get('sha') and str(c.get('item', '')).startswith(F['item']) for c in allrows if c.get('kind') == 'commit')]
    tip = git('rev-parse', 'refs/heads/' + BRANCH).strip()
    rem = git('rev-parse', 'refs/remotes/origin/' + BRANCH).strip()
    srcs = dict((m, git('show', '%s:SIDEExplicitFormula/Schema/ZQ/%s.lean' % (tip, m))) for m in F['modules'])
    disp = [r for r in rows if r.get('kind') == 'dispatch']
    reads = [r for r in rows if r.get('kind') == 'read']
    lines = dict((m, len(s.split(NL)) - 1) for m, s in srcs.items())
    total = sum(lines.values())
    L = ['b731 -- THE %s FIELD, ITS GRADE, (R341)(%s), N1, N3 (%s)' % (F['name'], F['item'][1], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### The statement: %s. Branch %s of SIDE-explicit-formula, entering at %s, tip %s, read back at origin %s.' % (F['statement'], BRANCH, ENTERING, tip[:8], rem == tip), '']
    L += ['## THE CONTROLS FIRST (the grade`s own predicate, on planted rows)']
    c, cn, ct = controls(F['terminals'])
    L += c + ['  CONTROLS %d OF %d AS WANTED' % (cn, ct), '']
    L += ['## THE DISPATCHES, EACH BY ITS RUN ID (the conclusion printed and governing nothing; relay data/b731_dispatch_rows.json)']
    for r in reads:
        L.append('  %d  %-30s run %s  ref %s  conclusion %s  build exit %s  %s  free before %d MB  runner low %s MB%s' % (
            r['n'], r['item'], r['run'], r['built_ref'][:8], r['conclusion'], r['build_exit'], r['verdict'], r['free_mb'], r['runner_low_mb'],
            ''.join(NL + '       error: ' + e for e in r.get('errors') or [])))
    L += ['', '## THE LINES, MODULE BY MODULE (the plan %s)' % F['plan']]
    for m in F['modules']:
        L.append('  %-13s %4d lines' % (m, lines[m]))
    L += ['  THE SUM %d LEAN LINES, spent %d dispatches of at most %d' % (total, len(disp), CAP),
          '  against the prices: the bank`s %s ; the plan`s %s. Every estimate was the seat`s.' % (F['bank'], F['planned']), '']
    L += ['## THE FIELD`S THEOREMS']
    last = reads[-1] if reads else {}
    al = last.get('axioms_lines') or []
    for f, t, where in F['claus']:
        line = [l for l in al if ("'%s%s' depends on axioms" % (NS, t)) in l]
        L.append('  %-30s %-32s %-26s %s' % (f, t, where, line[0].split(': ', 1)[1] if line else 'NOT PRINTED'))
    L += ['', '## THE AXIOM PRINT OF THE TERMINALS, THE ARTIFACT`S OWN LINES (run %s, out/axioms.txt)' % last.get('run')]
    L += ['  ' + l for l in al if any(("'%s%s'" % (NS, t)) in l for t in F['terminals'])]
    L += ['']
    L += ['## WHAT THE THEOREM IS NOT'] + ['  ' + x for x in F['isnot']] + ['  The files are on the branch alone: not on main, no tag. The fields count and explicitFormula stay named premises; the instance`s theorems still bind the whole bundle; the instance`s grade does not move.', '']
    g, why = grade(rows, srcs, F['terminals'])
    sorry = [m for m, s in srcs.items() if re.search(r'\bsorry\b', s)]
    res = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), field=F['name'], grade=g, why=why, tip=tip, remote_equal=rem == tip, dispatches=len(disp), cap=CAP, lines=total, lines_by_module=lines,
               sorry=sorry, terminals=list(F['terminals']), controls=[cn, ct], runs=[r['run'] for r in disp])
    if g == 'CLOSED':
        L.append('### ### **THE %s FIELD CLOSED: %s COMPILED ; AXIOMS propext, Classical.choice, Quot.sound ; NO sorry ; DISPATCHES %d OF AT MOST %d ; LINES %d.**' % (F['name'], F['terminals'][0], len(disp), CAP, total))
    else:
        L.append('### ### **THE %s FIELD OPEN (%s) ; DISPATCHES %d OF AT MOST %d ; LINES %d.**' % (F['name'], why, len(disp), CAP, total))
    t = NL.join(L) + NL
    print(t)
    if '--bank' in sys.argv:
        stem = {'logderiv': 'b731_logderiv', 'zeros': 'b731_zeros'}[key]
        with open(os.path.join(D, stem + '.txt'), 'w', encoding='utf-8', newline=NL) as fh:
            fh.write(t)
        with open(os.path.join(D, stem + '.json'), 'w', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(res, ensure_ascii=False, indent=1) + NL)
        print('written data/%s.txt and .json' % stem)
    return 0 if cn == ct else 1


if __name__ == '__main__':
    sys.exit(main())
