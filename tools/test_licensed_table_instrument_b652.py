# -*- coding: utf-8 -*-
"""test_licensed_table_instrument_b652.py -- THE PLANTED CASES OF THE INSTRUMENT VERDICT, (R262)(5), b652.

### A row whose verdict came from an arm's mis-binding reads INSTRUMENT(<arm>) with its ARM cell; a row with a real contradiction keeps the
### arm's own verdict; the cell is refused where it does not belong; the four verdicts before it read as they did.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import licensed_table as LT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
res = []


def case(n, what, ok):
    res.append(ok)
    print('  (%d) %s -- %s' % (n, what, 'PASS' if ok else 'FAIL'))


def row(**kw):
    r = dict(id='t', source='SIDE-kernel/MetaKernel.lean:140', stated='a sentence', licensed='what the corpus licenses', by='HAND',
             cited=['SIDE-kernel@b0f2a3a:MetaKernel.lean:140'])
    r.update(kw)
    return r


inst = row(verdict='INSTRUMENT', arm='G-AXIOM-CLAIM', action='TO THE ARM: bind the claim to the object it is said of')
case(1, 'an INSTRUMENT row with its ARM cell and a repair to the arm is taken (faults %s)' % LT.check(inst), LT.check(inst) == [])
case(2, 'it prints INSTRUMENT(<arm>): %s' % LT.label(inst), LT.label(inst) == 'INSTRUMENT(G-AXIOM-CLAIM)')
noarm = dict(inst)
noarm.pop('arm')
case(3, 'an INSTRUMENT row without an ARM cell is refused (%s)' % LT.check(noarm), any('ARM cell' in f for f in LT.check(noarm)))
stray = row(verdict='OVERREACHES', arm='G-AXIOM-CLAIM', action='RE-CUT: a sentence proposed here')
case(4, 'an ARM cell on an OVERREACHES row is refused (%s)' % LT.check(stray), any('ARM cell on' in f for f in LT.check(stray)))
case(5, 'arm_verdict: a mis-binding reads INSTRUMENT', LT.arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', True) == 'INSTRUMENT')
case(6, 'arm_verdict: a real contradiction stays CONTRADICTED', LT.arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', False) == 'CONTRADICTED')
real = [LT.arm_verdict('G-AXIOM-CLAIM', 'CONTRADICTED', False) for _ in ('SteaneExemplar :6', 'Integration :215', 'MetaKernel :3', 'AxiomCheck :8')]
case(7, 'the four real contradictions of b651 (rows 1, 3, 4, 6) stay CONTRADICTED: %s' % real, real == ['CONTRADICTED'] * 4)
old = row(verdict='OVERREACHES', action='RE-CUT: a sentence proposed here')
counts, faults = LT.table([dict(old, id='a'), dict(inst, id='b')])
case(8, 'the table takes a row of the four verdicts as before and counts INSTRUMENT apart: %s' % dict(counts or {}),
     LT.check(old) == [] and counts and counts['OVERREACHES'] == 1 and counts['INSTRUMENT'] == 1)
gen = row(verdict='INSTRUMENT', arm='licensed_table.docstring_row D4 (the generated rule)', action='TO THE ARM: read the sentence its rule names')
case(9, 'a generated rule names its arm the same way (%s)' % LT.label(gen), LT.check(gen) == [])
noact = row(verdict='INSTRUMENT', arm='G-AXIOM-CLAIM', action='none')
case(10, 'an INSTRUMENT row with no repair to the arm is refused', any('repair to the arm' in f for f in LT.check(noact)))

n = sum(res)
print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
sys.exit(0 if n == len(res) else 1)
