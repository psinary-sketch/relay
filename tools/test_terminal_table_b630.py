# -*- coding: utf-8 -*-
"""test_terminal_table_b630.py -- THE TEST OF THE PROVENANCE COLUMN b630 ADDED TO tools/terminal_table.py, under (R240)(3) and the
author's answer before b630's seal (relay data/b630_author_answers.txt, prompt 1).

### (1)-(4) THE RULE'S READING on statements written here: a theorem with a hypothesis binder reads INTERFACES; a theorem without one
###   reads DERIVES; a definition reads DEF; no statement reads nothing.
### (5)-(8) THE PROVENANCE PASS on rows written here: a row graded by a cell keeps its grade and reads cell; a row new to the table with
###   no cell takes the rule's grade and reads rule; a row in the baseline with no cell keeps UNGRADED and reads none; a cell row whose
###   rule reading differs is returned for printing.
### (9) ONE RULE-GRADED ROW OF THE TABLE: rhoFun_bound, absent from the table at relay 75227e9c and carrying no cell, read from the
###   committed table's statement: the pass grades it DERIVES and marks it rule.
### (10) ONE CELL-GRADED ROW OF THE TABLE: the first SIDE-explicit-formula row the committed table grades by cells: the pass keeps its
###   grade and marks it cell.
### (11) THE BASELINE reads at relay 75227e9c, 1994 rows.
### b632, (R242)(3) and the author's answer before b632's seal (relay data/b632_author_answers.txt, prompt 1): THE BASELINE CONDITION
###   RETIRED. Case (7), whose expectation was the retired condition itself, re-pointed in the same edit: a row in the baseline with no
###   cell now takes the rule's grade and reads rule. (12) THE PLANTED PAIR: a row absent from the table at relay 75227e9c and a row
###   present there, read from the baseline itself, both with no cell, both graded by the rule; beside them a row with no cell and no
###   statement the rule reads stays UNGRADED and reads none.
### Usage: python tools/test_terminal_table_b630.py
"""
import copy
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-110s %s' % (label, 'PASS' if cond else '### FAIL'))

    # ### b637, (R247)(3)-(4) and the author's answer after b637's seal (relay data/b637_author_answers.txt, prompt 1): RE-POINTED. The
    # ### binder grammar reads a bare name no lexicon lists as a binder that reaches no class -- a raised bug, never a grade -- so the
    # ### synthetic premise `SomePremise`, a bare name, stopped this test; it is applied to an argument (`SomePremise 0`), a named premise,
    # ### and the case still wants INTERFACES. The same answer read for this file's other two synthetic premises, `H` of case (6) and `Q`
    # ### of case (12): one-letter names the statement binds nowhere, which the grammar reads as type variables (data), each applied to an
    # ### argument; the stop at (1) hid them from the prompt (b637's defect).
    want('(1) a theorem with a premise binder reads INTERFACES',
         TT.rule_reading('theorem X.foo (hP : SomePremise 0) : P ↔ Q', 'X.foo') == ('theorem', 'INTERFACES'))
    want('(2) a theorem without a hypothesis binder reads DERIVES', TT.rule_reading('theorem X.bar : Antitone f', 'X.bar') == ('theorem', 'DERIVES'))
    want('(3) a definition reads DEF', TT.rule_reading('noncomputable def X.baz (N : ℕ) : ℝ', 'X.baz') == ('def', 'DEF'))
    want('(4) no statement reads nothing', TT.rule_reading(None, 'X.q') == (None, None))
    rows = [dict(repo='R', name='X.cell', grade='DERIVES', grade_cells=[dict(grade='DERIVES')], statement='theorem X.cell : P'),
            dict(repo='R', name='X.new', grade='UNGRADED', grade_cells=[], statement='theorem X.new (h : H 0) : P'),   # ### b637: re-pointed, as (1)
            dict(repo='R', name='X.old', grade='UNGRADED', grade_cells=[], statement='theorem X.old : P'),
            dict(repo='R', name='X.differ', grade='INTERFACES', grade_cells=[dict(grade='INTERFACES')], statement='theorem X.differ : P')]
    rs = copy.deepcopy(rows)
    differ = TT.provenance(rs, {('R', 'X.cell'), ('R', 'X.old'), ('R', 'X.differ')})
    by = {r['name']: r for r in rs}
    want('(5) a cell row keeps its grade and reads cell', by['X.cell']['grade'] == 'DERIVES' and by['X.cell']['provenance'] == 'cell')
    want('(6) a new row with no cell takes the rule`s grade and reads rule', by['X.new']['grade'] == 'INTERFACES' and by['X.new']['provenance'] == 'rule')
    want('(7) a baseline row with no cell takes the rule`s grade and reads rule (b632: the baseline condition retired)',
         by['X.old']['grade'] == 'DERIVES' and by['X.old']['provenance'] == 'rule')
    want('(8) a cell row whose rule reading differs is returned, its grade kept', differ == [('R', 'X.differ', 'INTERFACES', 'DERIVES')]
         and by['X.differ']['grade'] == 'INTERFACES')
    T = json.loads(subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:data/terminal_table.json'], capture_output=True).stdout.decode('utf-8'))
    base = TT.baseline_keys()
    real = [copy.deepcopy(r) for r in T['rows'] if r['name'] == 'SIDEExplicitFormula.NymanBeurling.rhoFun_bound']
    cellrow = [copy.deepcopy(r) for r in T['rows'] if r['repo'] == 'SIDE-explicit-formula' and r.get('grade_cells')][:1]
    TT.provenance(real + cellrow, base or set())
    want('(9) rhoFun_bound, new since 75227e9c and carrying no cell, grades DERIVES from the rule and reads rule (read %s %s)' % (
        real[0]['grade'] if real else None, real[0].get('provenance') if real else None),
         len(real) == 1 and real[0]['grade'] == 'DERIVES' and real[0]['provenance'] == 'rule')
    g0 = [r['grade'] for r in T['rows'] if cellrow and r['name'] == cellrow[0]['name']][:1]
    want('(10) a cell-graded row of the table (%s) keeps its grade %s and reads cell' % (cellrow[0]['name'] if cellrow else None, g0),
         len(cellrow) == 1 and [cellrow[0]['grade']] == g0 and cellrow[0]['provenance'] == 'cell')
    want('(11) the baseline reads at relay %s, %s rows' % (TT.RULE_BASELINE, len(base) if base is not None else None),
         base is not None and len(base) == 1994)
    # ### b632, (R242)(3): THE PLANTED PAIR -- one key absent from the baseline, one key read from it, both with no cell and a statement the
    # ### rule reads; and one with no statement the rule reads.
    present = sorted(base or [])[:1]
    # ### b637: the planted premise re-pointed as (1)'s -- `Q`, a one-letter name the statement binds nowhere, the grammar reads as a type
    # ### variable (data); applied to an argument it is a named premise.
    planted = [dict(repo='SIDE-planted-b632', name='Planted.absent', grade='UNGRADED', grade_cells=[], statement='theorem Planted.absent (hQ : Q 0) : P'),
               dict(repo=present[0][0] if present else '?', name=present[0][1] if present else '?', grade='UNGRADED', grade_cells=[],
                    statement='theorem planted_present : P'),
               dict(repo='SIDE-planted-b632', name='Planted.none', grade='UNGRADED', grade_cells=[], statement=None)]
    TT.provenance(planted, base or set())
    want('(12) the planted pair: absent from the baseline %s/%s, present in it %s/%s, both by the rule; no statement reads none (read %s)' % (
        planted[0]['grade'], planted[0]['provenance'], planted[1]['grade'], planted[1]['provenance'],
        [(p['grade'], p['provenance']) for p in planted]),
         bool(present) and ('SIDE-planted-b632', 'Planted.absent') not in base and present[0] in base
         and (planted[0]['grade'], planted[0]['provenance']) == ('INTERFACES', 'rule')
         and (planted[1]['grade'], planted[1]['provenance']) == ('DERIVES', 'rule')
         and (planted[2]['grade'], planted[2]['provenance']) == ('UNGRADED', 'none'))
    n = sum(res)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
