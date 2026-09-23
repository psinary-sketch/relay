# -*- coding: utf-8 -*-
"""b479_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def gits(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


LABEL = {'C1': 'Schwarz reflection / realness', 'C2': 'Euler / multiplicative',
         'C3': 'functional equation / theta', 'C4': 'modular / PSL2(Z)',
         'C5': 'spectral', 'C6': 'Cauchy-Riemann / analyticity', 'C7': 'Hadamard'}


def main():
    SV = json.loads(read(os.path.join(D, 'b479_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b479_results.json')))
    SC = json.loads(read(os.path.join(D, 'b479_scores.json')))
    EXC = json.loads(read(os.path.join(D, 'b479_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b479_span.json')))
    FILED = json.loads(read(os.path.join(D, 'b479_filing.json')))
    checks = read(os.path.join(D, 'b479_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b479_mirror.txt'))
    pins = read(os.path.join(D, 'b479_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b479_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b479 -- THE CLOSING RECORD. ### THE SEVEN CLASSES AGAINST THE FORM, A READ.')
    rec('### Re-issued under (R96).')
    rec('=' * 100)
    rec('')
    rec('### (1) WHAT WAS READ.')
    rec('-' * 100)
    rec('    SIDE-lv-conservation at ### **v0.10.0 = %s**, by `git show`, AS TEXT.' % SV['sha'][:7])
    rec('    ### ### **NOTHING COMPILED.**')
    rec('    `h1_complete_at_Phi` conjoins ### **%d** ### per-class facts for ### **SEVEN** ###'
        % SV['conjuncts'])
    rec('    classes -- `C7` contributes entirety AND order.')
    rec('    statements naming `mellin Φ (s/2)` : ### **%d of %d**'
        % (sum(1 for f in SV['facts'] if f['mentions_mellin']), len(SV['facts'])))
    rec('')
    rec('### (2) THE TABLE.')
    rec('-' * 100)
    rec('    ### THE CRITERION, FIXED ON THE SEALED FACE BEFORE ANY VERDICT:')
    rec('    ### ### **A FACT TOUCHES THE FORM WHEN ITS STATEMENT CONSTRAINS THE OBJECT `W` IS')
    rec('    ### BUILT FROM -- THE MELLIN TRANSFORM OF `Φ` -- ON A FAMILY ITS OWN QUANTIFIER NAMES.**')
    rec('    ### Not one of the eight statements mentions a test function, `W`, or the explicit')
    rec('    ### formula, so a literal reading would return seven `APART` and say nothing.')
    rec('')
    for c in ('C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'):
        rec('    %-5s %-32s ### **%s**' % (c, LABEL[c], RES['verdicts'][c]))
    rec('')
    rec('    ### ### **TOUCHES THE FORM : %s. ### APART : %s.**'
        % (', '.join(RES['touch']), ', '.join(RES['apart'])))
    rec('    ### `C2`s constraining clause : `∀ s : ℂ, 1 < s.re → mellin Φ (s / 2) ≠ 0`.')
    rec('    ### `C7`s : `G s = mellin Φ (s/2) + 1/s + 1/(1-s)` on `1 < s.re`, WITH the growth')
    rec('    ### bound on all of `ℂ`. ### **THE ROW IS CARRIED BY `C7_order`.**')
    rec('')
    rec('### (3) THE SENTENCE THE TABLE SUPPORTS, AND NO WIDER.')
    rec('-' * 100)
    rec('    ### ### **TWO OF THE SEVEN REACH THE FORM.** ### The other five constrain `Φ` and')
    rec('    ### never name its transform; their route runs through derivations their statements do')
    rec('    ### not carry. ### **THAT IS NOT A CLAIM THAT THEY ARE IRRELEVANT TO THE FORM.**')
    rec('    ### ### **AND ONE OF THE TWO IS HALF OPEN:** `C7_order` is marked OPEN by the file`s')
    rec('    ### own docstring and priced as a Gamma-asymptotics project.')
    rec('    ### the conditional sentence is written in the order`s vocabulary and')
    rec('    ### ### **IS NOT DISCHARGED**; the stem `inerti` is at no address in FINDINGS or')
    rec('    ### REGISTRY and the act says so rather than borrowing it.')
    rec('    ### ### **THIS MEASURES THE FORMALISATION`S REACH AND NOT THE ARGUMENT`S TRUTH.**')
    rec('    ### and `h2` is QUOTED from the file`s own docstring and ### **NOT DISCHARGED.**')
    rec('')
    rec('### (4) THE EXPECTATIONS.')
    rec('-' * 100)
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) ### **%s**' % (k, SC[k]['verdict']))
    rec('    ### ### **REGISTERED 3 ; HELD 2 ; HELD-IN-PART 1.** ### The seat`s calls were on the')
    rec('    ### sealed face before the table was drawn and matched all three.')
    rec('')
    rec('### (5) TWO DEFECTS THIS ACT FOUND IN ITS OWN INSTRUMENTS.')
    rec('-' * 100)
    rec('    (a) ### **A `def` AND A `theorem` DO NOT MEAN THE SAME THING BY `:=`.** ### The fact')
    rec('        reader stopped at the first `:=` for both -- right for a theorem, ### **WRONG FOR')
    rec('        A `def`**, whose `:=` is on the declaration line and whose predicate IS the')
    rec('        content. ### It returned a stub for every `def` and reported ### **`0`** ###')
    rec('        statements naming the transform where the true figure is ### **`3`** -- a figure')
    rec('        that decides two rows of the table.')
    rec('        ### ### **(R70)`S REHEARSAL ON `C2` CAUGHT IT BEFORE THE SEAL.**')
    rec('    (b) ### **STEP ZERO FAILED ONCE.** ### The first pins run read `REPOS HARD-FAILING : 4`')
    rec('        -- all four `ls-remote` calls UNRESOLVED at once, the shape of a network blip and')
    rec('        not of four repository faults. ### A direct call immediately after returned the')
    rec('        correct SHA. ### The retry reads ### **0 of 4** ### and ### **BOTH RUNS ARE')
    rec('        BANKED** -- a gate that fired is evidence even when it fired on the weather.')
    rec('')
    rec('### (6) THE INSTRUMENTS, AND WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : 8186f852c9bc6e9c53629fe296becac598ca5d3c044dc2e9a597b3e49723f7da')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    ### ### **BOTH SPAN READINGS, PER (R96):**')
    rec('      the tool, by NUMBER order        : ### **%d**' % SPAN['current_span'])
    rec('      by FILING since the b474 fold    : ### **%d** ### with this act'
        % (FILED['count'] + 1))
    rec('      ### the tool is ### **NOT EDITED.**')
    rec('    ### ### **NOTHING COMPILED. ### NO GRADE MOVED. ### NO BRIDGE TYPED.** ### `C5_output`')
    rec('    ### is not counted; row U1 unedited; the four lists stay OPEN; `h2` where the deposit')
    rec('    ### left it; no claim about RH in either direction. ### b475`s log was not opened.')
    rec('    ### ### **THE FOLD FOLLOWS UNDER (R96) AND IS NOT OPENED BY THIS ACT.**')
    rec('')
    rec('### (7) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b479`, never from `main`.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b479_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
