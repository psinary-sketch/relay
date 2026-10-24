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
###   (6) with the namespaces opened, (2)'s binder type prints without its namespace prefix;
###   (7) b636, (R246)(4): the reader given SIDE-structural-error-correction reads its d_eff_eq_five -- a theorem, no binder, d_eff = 5 --
###       in that kernel's checkout, and returns to the explicit-formula kernel after.
### The generated file and its output are the scratchpad's; nothing in a repository is written. Usage: python tools/test_elab_reader_b634.py
### b710, (R320)(3): THE TEST READS A BANKED PRINT AND INVOKES NO LEAN. The two calls (:34 and :65 before this repair, b709's defect (c): each
### ran `lake env lean` by subprocess on this host) are replaced by the reader's own parser over the prints lean wrote at b709's last run
### (2026-10-23T19:28Z and 19:31Z, banked in relay byte for byte: data/b710_elab_reader_print.txt, data/b710_elab_reader_print_sec.txt, their
### blobs equal to the scratchpad outputs test_reader.out and test_reader_sec.out); the reader's `call` is replaced for the run by a refusal,
### so no lean process can start from this test. The seven cases read as before.
"""
import hashlib
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
SEC = 'SIDEStructuralErrorCorrection.d_eff_eq_five'     # ### b636, case (7)


PRINT = os.path.join(ROOT, 'data', 'b710_elab_reader_print.txt')          # ### b710: lean's print of the first call, banked
PRINT_SEC = os.path.join(ROOT, 'data', 'b710_elab_reader_print_sec.txt')  # ### b710: lean's print of the kernel's call, banked


def _refuse(*a, **k):
    raise SystemExit('### THE TEST CALLED THE READER`S `call` -- REFUSED: it reads banked prints and runs no lean ((R320)(3))')


def _banked(p):
    b = open(p, 'rb').read()
    print('  the banked print %s : %d bytes ; sha256 %s' % (os.path.relpath(p, ROOT).replace(os.sep, '/'), len(b), hashlib.sha256(b).hexdigest()[:16]))
    return b.decode('utf-8', 'replace')


def main():
    EL.call = _refuse   # ### b710: no lean process can start from this test
    got = EL.parse(_banked(PRINT))
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
    # ### b636, (R246)(4): the reader takes the kernel -- one declaration of SIDE-structural-error-correction at v0.2.2 = 6bf19ab of known
    # ### type, d_eff_eq_five : d_eff = 5 (SIDEStructuralErrorCorrection/Basic.lean :100), read by one call importing its module alone.
    EL.use('SIDE-structural-error-correction')
    try:
        g7 = EL.parse(_banked(PRINT_SEC))   # ### b710: the kernel's call's print, banked; no lean
    finally:
        EL.use(EL.DEFAULT_KERNEL)
    e7 = g7.get(SEC) or dict(kind=None, header=-1, total=-1, binders=[], concl='', missing=True)
    print('  the kernel`s print read for %s (no call made)' % EL.KERNELS['SIDE-structural-error-correction']['KER'])
    want('(7) SIDE-structural-error-correction`s d_eff_eq_five: a theorem, no binder, the conclusion d_eff = 5 (read %s %s of %s, %s)' % (
         e7['kind'], e7['header'], e7['total'], e7['concl']),
         e7['kind'] == 'theorem' and e7['header'] == 0 and e7['total'] == 0 and e7['concl'] == 'd_eff = 5' and EL.KX.KERNEL == 'SIDE-explicit-formula')
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
