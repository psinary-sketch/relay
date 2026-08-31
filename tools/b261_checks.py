# -*- coding: utf-8 -*-
"""b261_checks.py -- the b261 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED** (b242's species; numpy truth).
### ### **THE `ast` STRIPPER IS APPLIED ONLY TO PYTHON SOURCE** -- b260's second defect was
### ### reaching for it by habit on a plain-text bank, where `ast.parse` raised.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was written after the answer was known and back-dated.
###       ### Gate 1: the term scan ran BEFORE banking (b260's lesson), the registration was NOT
###       ### touched after the run, and its mtime genuinely precedes the run's.
###   (2) that b255's E2even column was the premise and the "derivation" was reverse-engineered.
###       ### Gate 2, in SOURCE ORDER: b255 is not read until after every step has its number.
###   (3) that S1's reduction is a model rather than the instrument. ### Gate 3: two independent
###       ### routes agree to 1e-13, and the perturbation control shows the bar can fail.
###   (4) that F4 was explained away. ### Gate 4: the artefact hypothesis was tested at BOTH axes
###       ### and the sweep is shown able to see a real failure.
###   (5) that the moved rho-axis was smuggled. ### Gate 5: declared in the registration BEFORE
###       ### any value, and the G-REPRO cost printed.
###   (6) that a compile was claimed without a printed profile. ### Gate 6.
###   (7) that the refutation is an artefact of the machinery. ### Gate 7: the constant-kernel
###       ### discriminator must produce NO rise.
###   (8) that the instruments were edited or re-typed. ### Gate 8, with the diagnostic replica
###       ### declared and checked against the instrument.
###   (9) that J2's grade was over-read. ### Gate 9: the bench ingredient is named in both files.
###  (10) that h2 or the register sentence moved. ### Gate 10.
###  (11) that the patent tree was written or swept in. ### Gate 11.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b261_registration_2026-08-30.txt')
BANK = os.path.join(D, 'b261_e2even_monotone.txt')
FIL = os.path.join(D, 'b261_filings.txt')
RUN = os.path.join(D, 'b261_run.txt')
DIAG = os.path.join(D, 'b261_diagnostics.txt')
ROWS = os.path.join(D, 'b261_rows.json')
PROF = os.path.join(D, 'b261_shadow_profile.txt')
B255B = os.path.join(D, 'b255_limit_profile.txt')
B260B = os.path.join(D, 'b260_junction_sign.txt')
B255J = os.path.join(D, 'b255_rows.json')
SRC = os.path.join(E16, 'b261_e2even.py')
DSRC = os.path.join(E16, 'b261_diagnostics.py')
SHADOW = os.path.join(RES, 'Core', 'E2EvenMonotoneShadow.lean')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'b255_ladder.py']


def py_code_only(path):
    """### SCOPE CONTROL with the `ast` comment/docstring stripper (b142; b248; b260).
    ### ### **PYTHON SOURCE ONLY. ### b260's SECOND DEFECT WAS APPLYING IT TO A .txt BANK.**"""
    import ast
    src = io.open(path, encoding='utf-8').read()
    doc = set()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            if node.body and isinstance(node.body[0], ast.Expr) \
                    and isinstance(node.body[0].value, ast.Constant) \
                    and isinstance(node.body[0].value.value, str):
                s0 = node.body[0]
                for ln in range(s0.lineno, (s0.end_lineno or s0.lineno) + 1):
                    doc.add(ln)
    return '\n'.join(l.split('#', 1)[0] for i, l in enumerate(src.split('\n'), 1) if i not in doc)


def code_line_of(path, needle):
    """### THE LINE NUMBER OF `needle` IN COMMENT-STRIPPED CODE, or -1.
    ### ### **ANCHOR ON THE ### USE ### , NEVER ON A PATH CONSTANT** -- b260's third defect, where
    ### a matcher found the NAME and not the USE and the gate was weak in the flattering direction."""
    for i, l in enumerate(py_code_only(path).split('\n'), 1):
        if needle in l:
            return i
    return -1


def git_unchanged(rel):
    """### `git -C`, RULE 4.8. ### A cwd-dependent git caused b259's near-miss."""
    p = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                       capture_output=True, text=True)
    return p.returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def main():
    h = Harness(repo_root=ROOT, act='b261')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    rows = R['rows']
    probe = [r for r in rows if r['a2'] < 2]
    ladder = sorted([r for r in rows if r['a2'] >= 2], key=lambda r: r['a2'])
    base = [r for r in rows if r['a2'] == 2][0]['E2even']

    # 1 -- ### THE REGISTRATION WAS TERM-SCANNED, THEN BANKED, THEN LEFT ALONE. b260's LESSON.
    h.run('registration-scanned-then-banked-then-untouched',
          check=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(RUN)
                             and os.path.getmtime(REG) < os.path.getmtime(ROWS)
                             and contains(REG, 'TERM-SCANNED BEFORE BANKING')
                             and contains(REG, 'REGISTRATION CLOSED')
                             and contains(REG, '`1e-12` absolute')
                             and contains(BANK, 'THE REGISTRATION SCANNED')
                             # ### b260's cost is named as the reason this gate can exist at all
                             and contains(BANK, 'b260')),
          # ### FIXTURE: the BANK was written AFTER the run, so "bank precedes run" must FAIL.
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(RUN)),
          witness=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(BANK)))

    # 2 -- ### b255 IS A CONTROL, NOT A PREMISE. ### CHECKED IN SOURCE ORDER, ANCHORED ON THE LOAD.
    LOAD = 'json.load(io.open(B255J'
    h.run('b255-read-only-after-every-step',
          check=lambda: bool(code_line_of(SRC, LOAD) > code_line_of(SRC, 'def e2_reduced')
                             and code_line_of(SRC, LOAD) > code_line_of(SRC, 'smaller = [r for r')
                             and code_line_of(SRC, LOAD) > code_line_of(SRC, 'f1 = bool(')
                             and contains(RUN, 'b255 IS READ ### HERE ### AND NOWHERE EARLIER')
                             and contains(BANK, 'b255 IS NOT RE-VERDICTED')),
          # ### FIXTURE: claim the LOAD precedes the reduced-form definition. ### It does not.
          fixture=lambda: bool(code_line_of(SRC, LOAD) < code_line_of(SRC, 'def e2_reduced')),
          witness=lambda: bool(code_line_of(SRC, LOAD) > 0))

    # 3 -- ### S1's REDUCTION IS THE INSTRUMENT, CONFIRMED BY TWO INDEPENDENT ROUTES.
    h.run('dilation-reduction-confirmed-two-routes',
          check=lambda: bool(R['worst_f1'] < 1e-12
                             and R['worst_red'] < 1e-11
                             and R['worst_f1'] > 0.0
                             and all(abs(r['E2even'] - r['reduced']) < 1e-11 for r in rows)
                             and contains(RUN, 'F1 DID NOT FIRE')
                             and contains(BANK, 'THE REDUCTION IS THE INSTRUMENT AND NOT A MODEL')),
          # ### FIXTURE: claim some cell's two routes disagree beyond the bar. ### None does.
          fixture=lambda: bool(any(abs(r['E2even'] - r['reduced']) > 1e-11 for r in rows)),
          # ### WITNESS: the measure is not identically zero -- it can register a difference.
          witness=lambda: bool(R['worst_f1'] > 0.0))

    # 4 -- ### F4 FIRED AND WAS NOT EXPLAINED AWAY. ### BOTH AXES SWEPT; THE SWEEP CAN SEE FAILURE.
    h.run('f4-fired-and-the-artefact-hypothesis-was-killed',
          check=lambda: bool(contains(RUN, 'F4 FIRED')
                             and contains(DIAG, 'NG-STABLE: True')
                             and contains(DIAG, 'NQ-STABLE: True')
                             and contains(DIAG, 'THE OSCILLATION IS THE ### OBJECT')
                             and contains(DIAG, 'THE AXIS TEST DISCRIMINATES')
                             and contains(BANK, 'F4 FIRED')
                             and contains(BANK, 'THE OSCILLATION IS IN THE ### LEADING ### MODE')),
          # ### FIXTURE: b260's bank predates this finding and carries no F4 at all.
          fixture=lambda: contains(B260B, 'NG-STABLE'),
          witness=lambda: contains(DIAG, 'starved'))

    # 5 -- ### THE MOVED rho-AXIS WAS DECLARED BEFORE ANY VALUE, AND ITS COST PRINTED.
    h.run('moved-axis-declared-before-any-value-and-priced',
          check=lambda: bool(contains(REG, 'EXTENDED DOWNWARD TO `rho = 1` EXACTLY')
                             and contains(REG, 'DECLARED, PRICED AND REPORTED')
                             and contains(RUN, 'THE AXIS THAT MOVES, DECLARED')
                             and contains(RUN, 'THE G-REPRO CONTROL')
                             and R['worst_grepro'] > 0.0
                             and R['worst_grepro'] < 1e-3
                             and contains(BANK, '5.338e-04')),
          # ### FIXTURE: claim the G-REPRO deviation is zero. ### It is not -- the grid DID move,
          # ### and a gate that expected agreement would be hiding the change it exists to price.
          fixture=lambda: bool(R['worst_grepro'] == 0.0),
          witness=lambda: bool(R['worst_grepro'] > 0.0))

    # 6 -- ### THE SHADOW'S PROFILE IS PRINTED, ZERO-AXIOM, AND ITS POLARITY CONTROL REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 11
                             and contains(PROF, 'ALL THREE REFUSED. lean exit code 1')
                             and contains(PROF, 'proved that the proposition')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and contains(SHADOW, 'the_ladder_predicate_fails_below_the_turn')
                             and contains(SHADOW, 'kernel_is_not_monotone')
                             and contains(BANK, '11 TERMINALS, ZERO AXIOMS')),
          # ### FIXTURE: demand 12 terminals. ### There are 11.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 12),
          witness=lambda: contains(PROF, 'import took'))

    # 7 -- ### THE REFUTATION IS THE KERNEL'S, NOT THE MACHINERY'S. ### THE CONSTANT-KERNEL CONTROL.
    h.run('refutation-is-the-kernel-not-the-pipeline',
          check=lambda: bool(len(probe) == 6
                             and all(r['E2even'] < base for r in probe)
                             and all(sorted(probe, key=lambda x: x['a2'])[i]['E2even']
                                     < sorted(probe, key=lambda x: x['a2'])[i + 1]['E2even']
                                     for i in range(len(probe) - 1))
                             and contains(RUN, 'rises detected : ### **0** ### (must be 0)')
                             and contains(BANK, 'THE RISE IS A PROPERTY OF ### THIS ### KERNEL')),
          # ### FIXTURE: claim some probe cell is NOT smaller than at a^2 = 2. ### All six are.
          fixture=lambda: bool(any(r['E2even'] >= base for r in probe)),
          witness=lambda: bool(len(probe) == 6))

    # 8 -- ### NO INSTRUMENT EDITED; THE DIAGNOSTIC REPLICA IS DECLARED AND MATCHES.
    h.run('instruments-unedited-and-replica-declared',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'def e2_of_grid' not in py_code_only(SRC)
                             and 'def per_mode_eps_grids' not in py_code_only(SRC)
                             and 'import b38_act10' in py_code_only(SRC)
                             and 'def per_mode' in py_code_only(DSRC)
                             and contains(DSRC, 'NOTHING HERE SHIPS AS A VALUE')
                             and contains(DIAG, 'THE REPLICA IS THE INSTRUMENT')),
          # ### FIXTURE: claim the RUN script defines the instrument. ### It imports it. ### The
          # ### DIAGNOSTIC does define a replica, which is why that one is declared, not hidden.
          fixture=lambda: bool('def e2_of_grid' in py_code_only(SRC)),
          witness=lambda: bool('def per_mode' in py_code_only(DSRC)))

    # 9 -- ### J2's GRADE CARRIES ITS BENCH INGREDIENT IN BOTH FILES.
    h.run('j2-grade-carries-its-bench-ingredient',
          check=lambda: bool(contains(BANK, 'IT DOES NOT PROVE `eps_even >= 0`')
                             and contains(BANK, 'THE SUM\'S SIGN IS A CANCELLATION FACT')
                             and contains(BANK, 'NO DERIVATION IS CLAIMED')
                             and contains(FIL, 'THE GRADE CARRIES THAT INGREDIENT')
                             and contains(FIL, 'W-ORD-EPS-DECAY')
                             and contains(FIL, 'BENCH-ONLY')
                             # ### and the FOOT's projection is answered rather than quietly dropped
                             and contains(FIL, 'NEITHER BRANCH WAS TAKEN')),
          # ### FIXTURE: b255's bank is a bench act and carries no such grade language.
          fixture=lambda: contains(B255B, 'THE GRADE CARRIES THAT INGREDIENT'),
          witness=lambda: contains(FIL, 'W-ORD-EPS-DECAY'))

    # 10 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE; NO DEFICIT LANGUAGE (R-III).
    h.run('register-sentence-exact-and-h2-unmoved',
          check=lambda: bool(contains(BANK, 'RH reduced to a single located clause, reduction '
                                            'machine-verified. h2 is the clause.')
                             and contains(BANK, 'NOTHING DEPOSITS')
                             and contains(BANK, 'NOTHING ABOUT `h2` BEYOND THE REGISTER SENTENCE '
                                                'EXACT')
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()
                             and 'shortfall' not in io.open(BANK, encoding='utf-8').read().lower()),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    # 11 -- ### THE PATENT TREE WAS NOT WRITTEN AND NOTHING UNDER IT IS STAGED.
    h.run('patent-tree-untouched-and-nothing-staged',
          check=lambda: bool('patent-package' not in staged()
                             and 'PLACE-papers' not in staged()
                             and contains(FIL, 'NOTHING UNDER `patent-package/` WAS WRITTEN OR '
                                               'STAGED')
                             and contains(FIL, 'no `git add -A` was run')
                             # ### REPAIRED. ### The first version's needle read
                             # ### `THE HOOK IS ### NOT ### EXERCISED THIS ACT`, dropping
                             # ### `` `place_add.py` `` from the middle of the actual sentence.
                             # ### ### **THE NORMALIZER FOLDS WHITESPACE AND CASE; IT DOES NOT
                             # ### ### INSERT MISSING WORDS.** ### A needle that is NEARLY the
                             # ### sentence is not the sentence -- b229's species, and b260 was
                             # ### caught by it too. ### Third act running; the habit is the hazard.
                             and contains(FIL, 'THE `place_add.py` HOOK IS ### NOT ### EXERCISED '
                                               'THIS ACT')),
          # ### FIXTURE: claim a patent path IS staged. ### None is.
          fixture=lambda: bool('patent-package' in staged()),
          witness=lambda: contains(FIL, 'b259\'s BANK REMAINS UNTRACKED'))

    # 12 -- ### THE LADDER'S FIFTEEN FALLS AND THE PROBE'S SIX RISES RECONCILE WITH THE SHADOW.
    h.run('counts-reconcile-rows-run-and-shadow',
          check=lambda: bool(len(rows) == 22
                             and len(probe) == 6
                             and len(ladder) == 16
                             and all(ladder[i]['E2even'] > ladder[i + 1]['E2even']
                                     for i in range(len(ladder) - 1))
                             and contains(RUN, '22 cells (6 probe + 16 ladder)')
                             and contains(SHADOW, 'cell_and_step_counts')
                             and contains(SHADOW, 'probe_cells_rise_monotonically')),
          # ### FIXTURE: claim the ladder rises somewhere. ### It falls at all fifteen steps.
          fixture=lambda: bool(any(ladder[i]['E2even'] <= ladder[i + 1]['E2even']
                                   for i in range(len(ladder) - 1))),
          witness=lambda: bool(len(rows) == 22))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
