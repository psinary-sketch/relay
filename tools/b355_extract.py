# -*- coding: utf-8 -*-
"""b355_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE** (the sortie's step zero).

### ### **THIS ACT IS A READ, AND THE EXTRACT IS ITS EVIDENCE.** ### The question is what the corpus's test
### functions ARE -- discretisations of members of the source's class, or the members themselves -- and the
### answer has to be found at emitting lines rather than reasoned about.
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
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


READS = [
    # ---- THE ORDER --------------------------------------------------------------------------------
    ('the order -- leg 2, what the arrays are', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     'LEG 2 (b355) - WHAT THE ARRAYS ARE, as drafted, with two'),
    ('the order -- the two failed hypotheses answered separately', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     "the corpus's arrays are answered separately and not merged:"),
    ('the order -- the object or a description of it', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     "whether the record's own word for them is the object or a"),
    ('the order -- closed AT a width and open ACROSS widths', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     'equivalence applies at each fixed width and the width'),
    ('the order -- confirm but not strengthen', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     'is the same sentence b353 wrote and this act may confirm but'),
    ('the order -- which used the scan, which used the equivalence', 'ORDER', d('b355_ferry_2026-09-07.txt'),
     'of them used the scan, which used the equivalence, and what'),

    # ---- WHAT b353 LEFT ---------------------------------------------------------------------------
    ('b353 -- H1 refutable against the arrays', 'b353', d('b353_the_missing_statement.txt'),
     'IS NOT `C^infty`. ### IT IS NOT EVEN `C^1`.'),
    ('b353 -- the record does not settle what the arrays are', 'b353', d('b353_the_missing_statement.txt'),
     'THEM AS DISCRETISATIONS OF SMOOTH FUNCTIONS OR AS THE OBJECTS THEMSELVES IS A QUESTION THE RECORD'),
    ('b353 -- H3 undecidable, the tool says why', 'b353', d('b353_the_missing_statement.txt'),
     'it cannot prove one IS beyond the interval scanned'),
    ('b353 -- an exhaustion at every width is not one across widths', 'b353', d('b353_the_missing_statement.txt'),
     'SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS'),
    ('b353 -- the located statement and its hypotheses', 'b353', d('b353_the_missing_statement.txt'),
     'A STATEMENT EXISTS -- AND IT DOES NOT CLOSE THE WIDTH COORDINATE, AND CANNOT'),

    # ---- WHAT THE ARRAYS ACTUALLY ARE, AT THEIR EMITTING LINES ------------------------------------
    ('THE GENERATING FORMULA -- the atlas bump is the smooth one', 'ARRAY', t('e16/carto_atlas.py'),
     'w[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))'),
    ('THE GENERATING FORMULA -- sampled on NV nodes', 'ARRAY', t('e16/carto_atlas.py'),
     'v = np.linspace(-L, L, NV)'),
    ('THE GENERATING FORMULA -- normalised by the TRAPEZOID rule', 'ARRAY', t('e16/carto_atlas.py'),
     'w /= np.trapezoid(w, v)'),
    ('THE OBJECT -- evaluation IS piecewise-linear interpolation', 'ARRAY', t('b317_smear.py'),
     'EVALUATION IS PIECEWISE-LINEAR INTERPOLATION OF THAT GRID AND ZERO OUTSIDE IT'),
    ('THE OBJECT -- and the REASON the record gives for it', 'ARRAY', t('b317_smear.py'),
     "function this act integrates is the function the corpus's number was formed from"),
    ('THE OBJECT -- the call that makes it so', 'ARRAY', t('b317_smear.py'),
     'return np.interp(np.log(rho), self.v, self.w, left=0.0, right=0.0)'),
    ('THE OBJECT -- each bump is piecewise linear on its own nodes', 'ARRAY', t('b317_smear.py'),
     'THE UNION GRID IS NOT A CONVENIENCE EITHER.** ### Each bump is piecewise linear on its'),
    ('THE OBJECT -- the trapezoid rule is EXACT on it', 'ARRAY', t('b317_smear.py'),
     'rule is EXACT on a piecewise-linear function over a grid containing its breakpoints'),
    ('THE OBJECT -- f itself is piecewise linear on the uniform grid', 'ARRAY', t('b326_closure.py'),
     "is piecewise linear on b318's uniform grid, and its transform has"),
    ('THE OBJECT -- and its transform aliases because of that', 'ARRAY', t('b326_closure.py'),
     'alias peaks at every multiple of'),

    # ---- WHAT EACH CHECK ACTUALLY DID -------------------------------------------------------------
    ('THE SCAN -- Definition 3.1, and its stated reach', 'CHECK', t('b318_square.py'),
     'show a function is NOT positive definite by exhibiting a negative value, and it cannot prove'),
    ('THE SCAN -- it runs in units of the cell own width', 'CHECK', t('b318_square.py'),
     "The scan runs in units of the cell's own width `L = log a`, so a narrow cell is scanned as"),
    ('THE CONSTRUCTION -- f is formed as g conv g-sharp', 'CHECK', d('b320_the_lawful_function.txt'),
     "formed with the source's own involution, tested by the source's own Definition 3.1"),
    ('THE CONSTRUCTION -- 13 of 13, and the floor', 'CHECK', d('b320_the_lawful_function.txt'),
     'definite if and only if `f-hat >= 0` pointwise* -- gives'),
    ('THE CONTROL -- and the test CAN fail', 'CHECK', d('b320_the_lawful_function.txt'),
     'AND THE TEST CAN FAIL:'),
    ("THEOREM 1's three conditions, per cell", 'CHECK', d('b320_the_lawful_function.txt'),
     "THEOREM 1's THREE CONDITIONS, PER CELL."),
    ('the covered cells named from the check', 'CHECK', d('b320_the_lawful_function.txt'),
     'THE COVERED CELLS ARE NAMED FROM THE CHECK AND NOT FROM THE WISH'),
    ('b328 -- lawfulness, measured and not assumed', 'CHECK', d('b328_registration_2026-09-05.txt'),
     'LAWFULNESS, MEASURED AND NOT ASSUMED'),
    ('b349 -- three lawful seeds mean these three did not', 'CHECK', d('b349_the_room_relative.txt'),
     'NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT'),

    # ---- THE STANDING RULES ------------------------------------------------------------------------
    ('b354 -- the sixth rung, and what it could not separate', 'RULE', d('b354_the_sixth_frame.txt'),
     'SO THE TWO THINGS HAPPEN AT THE SAME RUNG, AND THIS ACT CANNOT SEPARATE THEM'),
    ('b352 -- a fit is a description and not a fact', 'RULE', d('b352_the_fourth_candidate.txt'),
     'A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING.** ### The registration fixed'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def main():
    rec('=' * 100)
    rec('b355 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec("  ### the step-zero tool's fixtures, run here before it is trusted:")
    ok = AF.self_test(True)
    rec('  ### anchor_from_file fixtures : %s' % ok)
    if not ok:
        run_clock.write(D, 'b355_extract_notes', LINES)
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
        built.append(dict(label=label, tag=tag, file=os.path.relpath(path, ROOT).replace(os.sep, '/'),
                          line=n, differs=bool(differs)))
        rec('')
        rec('  [%-5s] %s' % (tag, label))
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.relpath(path, ROOT).replace(os.sep, '/'), n, differs))
        rec('      | %s' % line.rstrip())
    ndiff = sum(1 for b in built if b['differs'])
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), bad))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (ndiff, len(built)))
    rec('  ### ### **AN EXTRACT IS A QUOTATION AT A LINE. ### IT IS NOT A READING OF THE ARGUMENT AROUND IT.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b355_extract_notes', LINES)
    io.open(d('b355_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(reads=len(READS), without_anchor=bad, anchors_differing=ndiff, built=built,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if not bad else 1


if __name__ == '__main__':
    sys.exit(main())
