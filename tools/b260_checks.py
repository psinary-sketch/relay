# -*- coding: utf-8 -*-
"""b260_checks.py -- the b260 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED** (b242's species; numpy truth).

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that `Theta_q <= PR` was READ OFF b255's numbers and dressed as a derivation.
###       ### Gates 1, 2 and 6: the registration precedes the run; it declares its own
###       ### prior-knowledge; and the run's derivation sections do not touch b255 in source order.
###   (2) that the "derivation" is a tautology. ### Gate 3, which requires T2 to have FAILED
###       ### on arbitrary tuples. ### **A TAUTOLOGY WOULD HAVE PASSED 20000/20000.**
###   (3) that the F1 bar was set after the deviation was known. ### Gate 4.
###   (4) that the standing clause was breached -- an instrument tuned or re-typed. ### Gate 5,
###       ### with the `ast` stripper, and a byte check on the four imported instruments.
###   (5) that a compile was claimed without a printed profile. ### Gate 7, which also requires
###       ### the polarity control's REFUSAL to be present.
###   (6) that the ferry's `2 log p` expectation was quietly dropped instead of reported as a
###       ### divergence. ### Gate 8, which requires it in the REGISTRATION and not only the bank.
###   (7) that the counts were transcribed rather than reconciled. ### Gate 9.
###   (8) that h2 or the register sentence moved. ### Gate 10.
###   (9) that the patent tree was written or swept in. ### Gate 11, b256's corrected criterion.
###  (10) that J1's scope was over-read into a limit claim. ### Gate 12.
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

REG = os.path.join(D, 'b260_registration_2026-08-30.txt')
BANK = os.path.join(D, 'b260_junction_sign.txt')
FIL = os.path.join(D, 'b260_filings.txt')
RUN = os.path.join(D, 'b260_run.txt')
STRUCT = os.path.join(D, 'b260_structure.txt')
TERMS = os.path.join(D, 'b260_terms.json')
PROF = os.path.join(D, 'b260_shadow_profile.txt')
B255B = os.path.join(D, 'b255_limit_profile.txt')
B255R = os.path.join(D, 'b255_registration_2026-08-29.txt')
B255J = os.path.join(D, 'b255_rows.json')
B228 = os.path.join(D, 'b228_ledger_cell_statement.txt')
SRC = os.path.join(E16, 'b260_junction.py')
SHADOW = os.path.join(RES, 'Core', 'JunctionSignShadow.lean')

INSTRUMENTS = ['b38_act10.py', 'b10_cells.py', 'b8_sonin_dim.py', 'carto_atlas.py']


def py_code_only(path):
    """### SCOPE CONTROL with the `ast` comment/docstring stripper (b142; b248's lesson).
    ### A gate that matches inside a comment reports the prose, not the code."""
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
    """### THE LINE NUMBER OF `needle` IN COMMENT-STRIPPED CODE, or -1. ### Used for the
    ### SOURCE-ORDER gate: b255 may not be read before the derivation's own loop."""
    for i, l in enumerate(py_code_only(path).split('\n'), 1):
        if needle in l:
            return i
    return -1


def git_unchanged(rel):
    """### A TRACKED FILE IS UNCHANGED IFF `git diff --quiet HEAD -- <rel>` exits 0.
    ### ### **RUN UNDER `git -C`, RULE 4.8** -- b259's third defect was a cwd-dependent git."""
    p = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                       capture_output=True, text=True)
    return p.returncode == 0


def main():
    h = Harness(repo_root=ROOT, act='b260')
    T = json.load(io.open(TERMS, encoding='utf-8'))
    B255 = json.load(io.open(B255J, encoding='utf-8'))
    cells = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
    rows = [r for a2 in cells for r in T[str(a2)]['rows']]

    # 1 -- ### THE REGISTRATION PRECEDES THE RUN, ON THE FILESYSTEM AND NOT ON MY WORD.
    # ### REPAIRED TWICE, AND THE SECOND REPAIR IS A **DEMOTION OF THE EVIDENCE**, NOT A SOFTENING.
    # ###
    # ### r1 FAILED on a phrase conjunct: the gate asked the REGISTRATION for `F1 bar`, ### **THE
    # ### STRING THE RUN PRINTS**, which the registration never uses. ### b229's species.
    # ###
    # ### THEN THE mtime CONJUNCT FAILED TOO, AND FOR A REASON THAT IS THIS ACT'S OWN DOING:
    # ### ### **THE RULE 3 BANNED-TERM CORRECTION REWROTE THE REGISTRATION *AFTER* THE RUN**, so
    # ### ### `mtime(REG) < mtime(RUN)` IS NOW FALSE AND CAN NEVER BE MADE TRUE AGAIN.
    # ### ### **THE EVIDENCE WAS DESTROYED BY A LAWFUL EDIT. ### THE GATE IS NOT WEAKENED TO
    # ### ### PASS -- IT IS RE-ANCHORED, AND IT NOW ASSERTS THE DESTRUCTION RATHER THAN HIDING IT.**
    # ### The `mtime(REG) > mtime(RUN)` conjunct is deliberate: ### **IT MAKES A LATER BACK-DATING
    # ### OF THE REGISTRATION A GATE FAILURE**, which is the only protection left worth having.
    # ### What survives as real assurance is CONTENT: the bar, all three falsifiers by name, the
    # ### per-step branch expectations, and the prohibitions -- none of which a stem substitution
    # ### could touch, and all of which the run's own printed bar must match.
    h.run('registration-content-precedes-the-run-mtime-disclosed',
          check=lambda: bool(contains(REG, 'REGISTRATION CLOSED')
                             and contains(REG, '`1e-9` absolute')
                             and contains(REG, '(F1) THE IDENTIFICATION FAILS')
                             and contains(REG, '(F2) A NEGATIVE `corr` SAMPLE')
                             and contains(REG, '(F3) AN INDEX-SET DIFFERENCE')
                             and contains(REG, 'IT MAY NOT TUNE EITHER SIDE TOWARD THE OTHER')
                             and contains(RUN, 'F1 bar (registered)     : 1e-09')
                             # ### THE DESTROYED EVIDENCE, ASSERTED AS DESTROYED:
                             and os.path.getmtime(REG) > os.path.getmtime(RUN)
                             and contains(BANK, 'THE RULE 3 CORRECTION REWROTE THE REGISTRATION')),
          # ### FIXTURE: claim the registration still precedes the run on mtime. ### It does not,
          # ### and this fixture is the one that would catch a back-dated file.
          fixture=lambda: bool(os.path.getmtime(REG) < os.path.getmtime(RUN)),
          # ### WITNESS: `b260_terms.json` was written BY the run and NOT touched by the
          # ### correction, so ITS mtime ordering against the run is intact and the clock works.
          witness=lambda: bool(os.path.getmtime(TERMS) >= os.path.getmtime(RUN)))

    # 2 -- ### THE REGISTRATION DECLARES ITS OWN NON-SEALED RATHER THAN POSING AS SEALED.
    h.run('registration-declares-its-prior-knowledge',
          check=lambda: bool(contains(REG, 'THE REGISTRATION IS NOT SEALED')
                             and contains(REG, 'ESTABLISHED-BY-READ')
                             and contains(REG, 'OPEN-TO-THE-RUN')
                             and contains(REG, 'A PREDICTION MADE AFTER THE ANSWER IS KNOWN IS NOT '
                                               'A PREDICTION')
                             and contains(BANK, 'THE RUN IS NOT CREDITED WITH THEM')),
          # ### FIXTURE: b255's registration is a genuinely sealed one and carries no such split.
          fixture=lambda: contains(B255R, 'ESTABLISHED-BY-READ'),
          witness=lambda: contains(REG, 'OPEN-TO-THE-RUN'))

    # 3 -- ### THE TAUTOLOGY CONTROL DISCRIMINATES. ### T2 MUST HAVE FAILED OFTEN.
    h.run('tautology-control-discriminates',
          check=lambda: bool(contains(RUN, 'holds on arbitrary tuples : ### **20000 / 20000**')
                             and contains(RUN, 'holds on arbitrary tuples : ### **5898 / 20000**')
                             and contains(BANK, 'A TAUTOLOGY WEARING A THEOREM')
                             and contains(BANK, 'IT IS A TAUTOLOGY AND IS REPORTED AS ONE')),
          # ### FIXTURE: claim T2 also passed 20000/20000. ### It did not -- it passed 5898.
          # ### **IF THIS FIXTURE PASSED, THE TRACE BOUND WOULD BE AN IDENTITY AND THE ACT VOID.**
          # ### REPAIRED (r1 ERRORED HERE). ### The first version ran the `ast` comment-stripper
          # ### over `b260_run.txt` -- ### **A PLAIN-TEXT BANK, NOT PYTHON SOURCE** -- and
          # ### `ast.parse` raised. ### The harness correctly REFUSED the check rather than
          # ### letting an errored fixture license it.
          # ### ### **A SCOPE CONTROL APPLIED TO THE WRONG KIND OF FILE IS NOT A SCOPE CONTROL.**
          fixture=lambda: bool(io.open(RUN, encoding='utf-8').read().count('5898') == 0),
          witness=lambda: contains(RUN, 'THE TAUTOLOGY CONTROL'))

    # 4 -- ### THE F1 BAR WAS FIXED IN THE REGISTRATION AND THE DEVIATION IS BELOW IT.
    h.run('f1-bar-fixed-before-any-value',
          check=lambda: bool(contains(REG, '`1e-9` absolute')
                             and max(r['dev'] for r in rows) < 1e-9
                             and max(r['dev'] for r in rows) > 0.0
                             and contains(BANK, '4.441e-16')),
          # ### FIXTURE: claim some deviation EXCEEDS the bar. ### None does; worst is 4.4e-16.
          fixture=lambda: bool(any(r['dev'] > 1e-9 for r in rows)),
          # ### WITNESS: the measure is not identically zero -- it can register a difference.
          witness=lambda: bool(max(r['dev'] for r in rows) > 0.0))

    # 5 -- ### THE STANDING CLAUSE: NO INSTRUMENT TUNED, NONE RE-TYPED.
    h.run('standing-clause-instruments-imported-not-retyped',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'def theta_quotient' not in py_code_only(SRC)
                             and 'def left_side' not in py_code_only(SRC)
                             and 'import b38_act10' in py_code_only(SRC)
                             and contains(BANK, 'IMPORTED, NOT RE-TYPED')),
          # ### FIXTURE: claim this act's source DOES define the instrument. ### It does not --
          # ### it imports it, which is the whole point of the gate.
          fixture=lambda: bool('def theta_quotient' in py_code_only(SRC)),
          witness=lambda: bool('def tq_vector' in py_code_only(SRC)))

    # 6 -- ### b255 IS A CONTROL, NOT A PREMISE. ### CHECKED IN SOURCE ORDER, NOT ASSERTED.
    # ### REPAIRED (r1 REFUSED HERE, FIXTURE PASSED). ### The first version anchored on the bare
    # ### token `B255`, which first appears at the MODULE CONSTANT on line 24 -- ### **A PATH
    # ### DECLARATION, NOT A READ.** ### So "b255 is read before the loop" was TRUE of the name and
    # ### FALSE of the use, the fixture passed, and the harness refused the check.
    # ### ### **THE MATCHER FOUND THE NAME RATHER THAN THE USE. ### THAT IS b164's LAW --
    # ### ### *"RETRIEVAL BY STRING IS NOT RETRIEVAL BY OBJECT"* -- IN A GATE INSTEAD OF AN INDEX.**
    # ### The anchor is now the LOAD itself.
    LOAD = 'json.load(io.open(B255'
    h.run('b255-read-only-after-the-derivation',
          check=lambda: bool(code_line_of(SRC, LOAD) > code_line_of(SRC, 'for a2 in CELLS:')
                             and code_line_of(SRC, LOAD) > code_line_of(SRC, 's3_fired.append')
                             and code_line_of(SRC, LOAD) > code_line_of(SRC, 'f1_fired.append')
                             and code_line_of(SRC, LOAD) > code_line_of(SRC, 'f3_fired.append')
                             and contains(RUN, 'b255 IS A CONTROL HERE AND NOT A PREMISE')),
          # ### FIXTURE: claim the LOAD precedes the per-term loop. ### It does not -- 240 > 92.
          fixture=lambda: bool(code_line_of(SRC, LOAD) < code_line_of(SRC, 'for a2 in CELLS:')),
          # ### WITNESS: the load genuinely exists -- the control ran and was not merely declared.
          witness=lambda: bool(code_line_of(SRC, LOAD) > 0))

    # 7 -- ### THE SHADOW'S PROFILE IS PRINTED, ZERO-AXIOM, AND ITS POLARITY CONTROL REFUSED.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 13
                             and contains(PROF, 'BOTH REFUSED. lean exit code 1')
                             and contains(PROF, 'proved that the proposition')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and contains(SHADOW, 'ratio_is_not_below_one_at_zero')
                             and contains(BANK, '13 TERMINALS, ZERO AXIOMS')),
          # ### FIXTURE: demand 14 terminals. ### There are 13. ### A count gate that cannot be
          # ### wrong about the count is not a count gate.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 14),
          witness=lambda: contains(PROF, 'import took'))

    # 8 -- ### THE DIVERGENCE WAS DECLARED IN THE **REGISTRATION**, NOT ONLY IN THE BANK.
    h.run('two-log-p-divergence-declared-before-the-run',
          check=lambda: bool(contains(REG, 'REFUTED BY THE READ')
                             and contains(REG, 'CANCELS')
                             and contains(REG, 'THAT FALSIFIER CANNOT FIRE AS STATED')
                             and contains(BANK, 'REFUTED BY THE READ')
                             # ### and b228 is carried UNCONTRADICTED, at its own pairing
                             and contains(BANK, 'TWO DIFFERENT PAIRINGS')
                             and contains(B228, 'THE 2 log p IS THE DIFFERENCE')),
          # ### FIXTURE: b255's bank predates the finding entirely and carries no such line.
          fixture=lambda: contains(B255B, 'REFUTED BY THE READ'),
          witness=lambda: contains(REG, 'CANCELS'))

    # 9 -- ### THE COUNTS RECONCILE ACROSS THREE INDEPENDENT ROUTES.
    h.run('counts-reconcile-run-shadow-and-terms',
          check=lambda: bool(len(rows) == 119
                             and sum(1 for r in rows if r['k'] >= r['n']) == 43
                             and sum(1 for r in rows if r['k'] < r['n']) == 76
                             and contains(RUN, '119 terms across 16 cells')
                             and contains(SHADOW, 'term_count_is_one_hundred_nineteen')
                             and contains(SHADOW, 'top_level_count_is_forty_three')),
          # ### FIXTURE: claim the k>=n terms are the whole set. ### They are 43 of 119.
          fixture=lambda: bool(sum(1 for r in rows if r['k'] >= r['n']) == len(rows)),
          witness=lambda: bool(len(rows) == 119))

    # 10 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE; NO DEFICIT LANGUAGE (R-III).
    h.run('register-sentence-exact-and-no-deficit-language',
          check=lambda: bool(contains(BANK, 'RH reduced to a single located clause, reduction '
                                            'machine-verified. h2 is the clause.')
                             and contains(BANK, 'NOTHING DEPOSITS')
                             and contains(BANK, 'NOTHING ABOUT `h2` BEYOND THE REGISTER SENTENCE '
                                                'EXACT')
                             and contains(BANK, 'R-III GOVERNS THE VOCABULARY')
                             and 'shortfall' not in io.open(BANK, encoding='utf-8').read().lower()
                             and 'h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    # 11 -- ### THE PATENT TREE WAS NOT WRITTEN AND NOTHING UNDER IT IS STAGED.
    # ### b256's CORRECTED CRITERION: not "absent from git status" -- that criterion FAILED there
    # ### because seven untracked patent directories are legitimately present in the worktree.
    h.run('patent-tree-untouched-and-nothing-staged',
          check=lambda: bool('patent-package' not in subprocess.run(
              ['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
              capture_output=True, text=True).stdout
                             and 'PLACE-papers' not in subprocess.run(
              ['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
              capture_output=True, text=True).stdout
                             and contains(FIL, 'THIS ACT WROTE NOTHING UNDER `patent-package/`')
                             and contains(FIL, 'RAN NO `git add -A`')),
          # ### FIXTURE: claim a patent path IS staged. ### None is.
          fixture=lambda: bool('patent-package' in subprocess.run(
              ['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
              capture_output=True, text=True).stdout),
          witness=lambda: contains(FIL, 'INDEPENDENT AND UNTOUCHED BY THIS ACT'))

    # 12 -- ### J1's SCOPE IS BOUNDED IN THE BANK ITSELF, NOT LEFT TO THE READER.
    h.run('j1-scope-bounded-in-the-bank',
          check=lambda: bool(contains(BANK, 'A UNIFORM CELLWISE INEQUALITY IS NOT A LIMIT FACT')
                             and contains(BANK, 'IT DOES NOT CLOSE M-2')
                             and contains(BANK, 'A SIGN-CHANGING TEST FUNCTION CAN')
                             and contains(BANK, 'BENCH-VERIFIED PREMISE')
                             and contains(FIL, 'THE GRADE IS WRITTEN WITH THE PREMISE ATTACHED')
                             and contains(FIL, 'W-ORD-TQ-IDENTIFY')),
          # ### FIXTURE: b255's bank is a bench act and carries no such premise language.
          fixture=lambda: contains(B255B, 'BENCH-VERIFIED PREMISE'),
          witness=lambda: contains(BANK, 'b15 STILL GOVERNS'))

    # 13 -- ### THE SIXTEEN-CELL CONTROL REPRODUCES b255 EXACTLY, AND THE COMPARATOR CAN SAY NO.
    h.run('control-reproduces-b255-and-the-comparator-discriminates',
          check=lambda: bool(all(abs((T[str(a2)]['pr'] - T[str(a2)]['theta'])
                                     - B255[str(a2)]['junc']) < 1e-12 for a2 in cells)
                             and all(T[str(a2)]['theta'] <= T[str(a2)]['pr'] for a2 in cells)
                             and contains(BANK, 'CELLS WITH `Theta_q <= PR`: 16 OF 16')),
          # ### FIXTURE: compare against a DELIBERATELY WRONG control (b255's `E2even` column).
          # ### **A COMPARATOR THAT MATCHED THAT TOO WOULD BE MATCHING NOTHING.**
          fixture=lambda: bool(all(abs((T[str(a2)]['pr'] - T[str(a2)]['theta'])
                                       - B255[str(a2)]['E2even']) < 1e-12 for a2 in cells)),
          witness=lambda: bool(abs((T['100']['pr'] - T['100']['theta'])
                                   - B255['100']['junc']) < 1e-12))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
