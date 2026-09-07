# -*- coding: utf-8 -*-
"""b357_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **THIS ACT IS A READ OF THE LEDGERS**, and the extract IS its evidence: every row it classifies must
### be locatable at the file that carries it, and the classification must be defensible against the words on
### that line and not against a memory of them.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull        # noqa: E402
import quote_norm         # noqa: E402
import run_clock          # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- leg 2, with two additions', 'ORDER', d('b357_ferry_2026-09-07.txt'),
     'LEG 2 (b357) - WHAT THE LEDGERS SAY THE CHECKS CERTIFY, as'),
    ('the order -- one table, quotations by the anchor tool', 'ORDER', d('b357_ferry_2026-09-07.txt'),
     'that check certified, in one table, quotations by the anchor'),
    ('the order -- nothing re-verdicted, nothing demoted', 'ORDER', d('b357_ferry_2026-09-07.txt'),
     'tool; nothing re-verdicted, nothing demoted. (ii) The'),
    ('the order -- the consequence stated once, plainly', 'ORDER', d('b357_ferry_2026-09-07.txt'),
     'consequence is stated once, plainly: class membership in this'),
    ('the order -- what an independent test would require', 'ORDER', d('b357_ferry_2026-09-07.txt'),
     'test would require an object not built as an autocorrelation,'),

    # ---- WHAT b355 FOUND ----------------------------------------------------------------------------
    ('b355 -- a scan on an object built as an autocorrelation', 'b355', d('b355_what_the_arrays_are.txt'),
     'applied to an object BUILT as an autocorrelation is'),
    ('b355 -- no act tested membership independently', 'b355', d('b355_what_the_arrays_are.txt'),
     'NO ACT IN THIS FAMILY EVER TESTED CLASS MEMBERSHIP'),
    ('b355 -- the old reading and the new', 'b355', d('b355_what_the_arrays_are.txt'),
     'THE SECOND IS NARROWER AND IT IS TRUE. ### THE FIRST WAS NEVER MEASURED'),
    ('b355 -- a relabelling and not a demotion', 'b355', d('b355_what_the_arrays_are.txt'),
     'A RELABELLING AND NOT A DEMOTION.** ### **EVERY BANKED NUMBER STANDS'),
    ('b355 -- the object integrated is the interpolant', 'b355', d('b355_what_the_arrays_are.txt'),
     'THE CORPUS INTEGRATES A PIECEWISE-LINEAR INTERPOLANT OF A SAMPLED SMOOTH BUMP'),
    ('b355 -- what was routed and not decided', 'b357_route', d('b355_what_the_arrays_are.txt'),
     'AND WHAT IS ROUTED RATHER THAN DECIDED'),

    # ---- THE LEDGER ROWS THEMSELVES -----------------------------------------------------------------
    ('FINDINGS -- the seeds explicitly inside the class, by the scan', 'LEDGER', FINDINGS,
     'The discriminating seeds of b328 are explicitly inside the class'),
    ('FINDINGS -- a local proposition per seed, decided by the scan', 'LEDGER', FINDINGS,
     'a local proposition per seed (lawful or not), decided by b320'),
    ('FINDINGS -- K1 graded MEASURED-ON-FAMILIES', 'LEDGER', FINDINGS,
     'K1** the class | IMPORT-UNDER-THE-BAR (b328) | MEASURED-ON-FAMILIES (b320)'),
    ('FINDINGS -- the clause (S), for every g in the class', 'LEDGER', FINDINGS,
     "**(S)** For every `g` in the source"),
    ('FINDINGS -- the grade these nine acts support', 'LEDGER', FINDINGS,
     'the finite-instance explicit formula is realized on lawful objects'),
    ('FACES -- two seeds built, both lawful at every width', 'LEDGER', FACES,
     'TWO SEEDS BUILT, both lawful at every width (Definition 3.1 scan'),
    ('FACES -- 56 of 56 seeds lawful by Definition 3.1', 'LEDGER', FACES,
     '56 of 56 seeds lawful by Definition 3.1 and the pole conditions'),
    ('FACES -- S1, the clause stated', 'LEDGER', FACES,
     'S1 -- the clause stated: for every g in the source'),
    ('FACES -- F1, realized on lawful objects', 'LEDGER', FACES,
     'the explicit formula Z = P'),
    ('CORRESPONDENCE -- b332 row: the seeds of b328 inside it', 'LEDGER', CORR,
     "the discriminating seeds of b328 inside it), the places sum"),
    ('CORRESPONDENCE -- b355 row: the narrower reading', 'LEDGER', CORR,
     'the reading this act supports is *the seeds are built as autocorrelations'),
    ('the banked index -- b332 row, the same sentence', 'LEDGER', t('banked_index.py'),
     "(S) for every g in the source's class (Definition 3.1 with Proposition C.1"),
    ('the banked index -- b355 row, the narrower reading', 'LEDGER', t('banked_index.py'),
     'lawfulness and every aimed seed at b334, b343, b344 and b349 USED BOTH'),

    # ---- THE CHECKS THEMSELVES ----------------------------------------------------------------------
    ('the scan, and its stated reach', 'CHECK', t('b318_square.py'),
     'show a function is NOT positive definite by exhibiting a negative value, and it cannot prove'),
    ('b320 -- f formed as g conv g-sharp, then tested', 'CHECK', d('b320_the_lawful_function.txt'),
     "formed with the source's own involution, tested by the source's own Definition 3.1"),
    ('b320 -- and the test CAN fail', 'CHECK', d('b320_the_lawful_function.txt'),
     'AND THE TEST CAN FAIL:'),

    # ---- THE STANDING RULES -------------------------------------------------------------------------
    ('b356 -- the boundary, and b354 not re-verdicted', 'RULE', d('b356_the_boundary.txt'),
     'AN ACT THAT NAMED ITS OWN AMBIGUITY IS NOT WRONG'),
    ('b322 -- a price is not a prediction', 'RULE', d('b322_the_membership.txt'),
     'A PRICE IS NOT A PREDICTION.'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b357 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b357_extract_notes', LINES)
        return 2
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    bad, built = 0, []
    for label, tag, path, hint in READS:
        try:
            n, line = AF.find(path, hint)
        except AF.AnchorError as e:
            bad += 1
            rec('  ### ### **NO ANCHOR** : %s' % label)
            rec('      %s' % e)
            continue
        try:
            needle_pull.pull(path, line)
        except LookupError:
            bad += 1
            rec('  ### ### **ANCHOR BUILT BUT UNPULLABLE** : %s' % label)
            continue
        differs = (quote_norm.norm(line) != quote_norm.norm(hint))
        built.append(dict(label=label, tag=tag, file=os.path.basename(path), line=n, differs=bool(differs)))
        rec('')
        rec('  [%-8s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s' % (os.path.basename(path), n, differs))
        rec('      | %s' % line.rstrip()[:200])
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('=' * 100)
    p = run_clock.write(D, 'b357_extract_notes', LINES)
    io.open(d('b357_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
