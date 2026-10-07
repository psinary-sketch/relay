# -*- coding: utf-8 -*-
"""test_elab_reader_b634.py -- THE TEST OF tools/b634_elab.py, THE ELABORATED READER, under (R244)(4).

### One call of the reader's own generator and driver, importing SIDEExplicitFormula.PlattRung at the kernel's checkout, under the
### hold (the free memory read before it), its output read back by the reader's own parser. Three declarations of known type:
###   (1) SIDEExplicitFormula.PlattRung.rh_upto -- a def, one explicit binder T : ℝ, the conclusion Prop;
###   (2) SIDEExplicitFormula.PlattRung.rh_upto_platt -- a theorem, one explicit binder hP on PlattTrudgianHeight, the conclusion rh_upto;
###   (3) Nat.add_comm -- a theorem, explicit n and m of ℕ, the conclusion n + m = m + n;
### and the header's cut and the absent name:
###   (4) a theorem planted in the generated file, (n : Nat) : n = n → n = n -- HEADER 1 of TOTAL 2, the arrow kept in the conclusion;
###   (5) a name the environment lacks prints MISSING;
###   (6) with the namespaces opened, (2)'s binder type prints without its namespace prefix.
### The generated file and its output are the scratchpad's; nothing in a repository is written. Usage: python tools/test_elab_reader_b634.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b634_elab as EL   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PR = 'SIDEExplicitFormula.PlattRung.'
NAMES = [PR + 'rh_upto', PR + 'rh_upto_platt', 'Nat.add_comm', 'b634PlantedArrow', PR + 'b634_no_such_name']
EXTRA = 'theorem b634PlantedArrow (n : Nat) : n = n → n = n := fun h => h'


def main():
    c = EL.call('SIDEExplicitFormula/PlattRung', NAMES, 'test_reader', extra=EXTRA)
    print('  the call: started %s ; exit %s ; %s s ; free before %s MB ; lowest %s MB' % (c.get('started'), c.get('rc'), c.get('seconds'),
                                                                                     c.get('free_before'), c.get('low')))
    got = EL.parse(open(c['out'], 'rb').read().decode('utf-8', 'replace')) if c.get('started') else {}
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    def b(n):
        return got.get(n) or dict(kind=None, header=-1, total=-1, binders=[], concl='', missing=True)

    e1, e2, e3, e4, e5 = (b(n) for n in NAMES)
    want('(1) rh_upto: a def, one explicit binder T : ℝ, the conclusion Prop (read %s %s %s)' % (e1['kind'], e1['binders'], e1['concl']),
         e1['kind'] == 'def' and [(x['kind'], x['name'], x['type']) for x in e1['binders']] == [('explicit', 'T', 'ℝ')] and e1['concl'] == 'Prop')
    want('(2) rh_upto_platt: a theorem, explicit hP on PlattTrudgianHeight, the conclusion rh_upto (read %s %s)' % (
         [(x['name'], x['type']) for x in e2['binders']], e2['concl']),
         e2['kind'] == 'theorem' and len(e2['binders']) == 1 and e2['binders'][0]['name'] == 'hP' and e2['binders'][0]['kind'] == 'explicit'
         and 'PlattTrudgianHeight' in e2['binders'][0]['type'] and e2['concl'].startswith('rh_upto'))
    want('(3) Nat.add_comm: explicit n and m of ℕ, the conclusion n + m = m + n (read %s %s)' % (
         [(x['name'], x['type']) for x in e3['binders']], e3['concl']),
         [(x['kind'], x['name'], x['type']) for x in e3['binders']] == [('explicit', 'n', 'ℕ'), ('explicit', 'm', 'ℕ')] and e3['concl'] == 'n + m = m + n')
    want('(4) a planted arrow: HEADER 1 of TOTAL 2, the arrow kept in the conclusion (read %s of %s, %s)' % (e4['header'], e4['total'], e4['concl']),
         e4['header'] == 1 and e4['total'] == 2 and e4['concl'] == 'n = n → n = n')
    want('(5) an absent name prints MISSING', e5['missing'] is True and NAMES[4] in got)
    want('(6) the namespaces opened: (2)`s binder printed without its prefix', bool(e2['binders']) and PR not in e2['binders'][0]['type'])
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
