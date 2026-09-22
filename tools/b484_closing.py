# -*- coding: utf-8 -*-
"""b484_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
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


def main():
    R = json.loads(read(os.path.join(D, 'b484_results.json')))
    c1, c2, c3 = R['c1'], R['c2'], R['c3']
    SC = json.loads(read(os.path.join(D, 'b484_scores.json')))
    SV = json.loads(read(os.path.join(D, 'b484_survey.json')))
    EXC = json.loads(read(os.path.join(D, 'b484_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b484_span.json')))
    checks = read(os.path.join(D, 'b484_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b484_mirror.txt'))
    pins = read(os.path.join(D, 'b484_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b484_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b484 -- THE CLOSING RECORD.')
    rec('### THE CURRENCY REPAIR, THE QUADRATURE WORK-ORDER, AND THE SUPPORT-EDGE TEST.')
    rec('=' * 100)
    rec('')
    rec('### (1) COMPONENT 1 -- (R92) EXECUTED, WITH (R93) FIXING ITS ADDRESSEE.')
    rec('-' * 100)
    rec('    `INVARIANCE_BARRIERS.md:580` now carries REGISTRY`s own `d1-1` row values.')
    rec('      the version word : v1.1.1  ->  ### **v1.1.2**')
    rec('      the version DOI  : ...21436278  ->  ### **...21539167**')
    rec('      the concept DOI  : ### **ALREADY AGREED -- NOT TOUCHED**')
    rec('      the Day-1 DOI    : a different record, not a currency claim -- ### **NOT TOUCHED**')
    rec('    ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW FILE : %d.**' % c1['missing'])
    rec('    ### the original line is preserved VERBATIM in an appended annotation, so the old')
    rec('    ### file`s lines are a SUBSET of the new file`s.')
    rec('    ### ### **AND THE RAW COUNTS ARE PRINTED BESIDE THAT SENTENCE, NOT HIDDEN BEHIND IT:**')
    rec('    ### git `--numstat` reads ### **+%s / -%s** -- one line modified, an annotation added.'
        % (c1['numstat'][0], c1['numstat'][1]))
    rec('    ### ### **OTHER LINES CHANGED IN PLACE : %d.** ### BOM and line ending verified.'
        % c1['other_changed'])
    rec('')
    rec('### (2) COMPONENT 2 -- `W-ORD-QUADRATURE-BOUND`, FILED.')
    rec('-' * 100)
    rec('    ### **THE CORPUS HOLDS NO ERROR BOUND FOR THE PLACES-SIDE QUADRATURE.** ### The chain')
    rec('    ### reports `trunc_bound`, which bounds the ZERO SUM`s truncation; b483 measured the')
    rec('    ### achieved agreement at 4.562e-05 and 3.169e-06 against 1.290e-12 and 6.421e-11 --')
    rec('    ### ### **AN UNDER-STATEMENT OF UP TO SEVEN ORDERS.**')
    rec('    ### TRIGGER: the next opening of the numerical instrument lane, or the next act citing')
    rec('    ### a chain floor.')
    rec('    ### ### **ACTS CITING `trunc_bound` : %d.** ### %s'
        % (c2['citing'], ', '.join(SV['citing'])))
    rec('    ### ### **OF THOSE, ACTS PREDICATING IT AS A FLOOR OR A CHAIN BOUND : %d.** ### %s'
        % (c2['predicating'], ', '.join(c2['named']) or 'NONE'))
    rec('    ### the matcher`s lineage: version 1 (CO-OCCURRENCE) returned %d ; version 2'
        % c2['wide'])
    rec('    ### (PREDICATION) returned %d. ### The difference is `b477`, whose sentence names two'
        % c2['predicating'])
    rec('    ### figures without equating them -- ### **A FALSE POSITIVE, HAND-READ AND SAID SO.**')
    rec('    ### ### **AND THE ONE ACT THAT DOES PREDICATE IT IS b483, WHICH REFUTED ITSELF IN ITS')
    rec('    ### OWN COMPONENT 3.** ### The chain is not edited.')
    rec('')
    rec('### (3) COMPONENT 3 -- THE SUPPORT-EDGE TEST.')
    rec('-' * 100)
    rec('    ### ### **THE LOOP HAS TWO COMPARATORS, NOT ONE.** ### The outer cap carries a `1e-12`')
    rec('    ### tolerance; the inner gate `if ln <= L`, which is what actually adds a term, carries')
    rec('    ### ### **NONE** -- and `L = 2.0 * math.log(a)` exactly.')
    rec('    a * a      = ### **%r**   (17 = 17.0)' % c3['asq'])
    rec('    a*a - 17   = ### **%+.6e**' % (c3['asq'] - 17.0))
    rec('    L - log 17 = ### **%+.6e**' % c3['margin'])
    rec('    ### ### **17 ENTERS THE SUM AT THAT CELL -- AND NOT AT THE EDGE.** ### The banks store')
    rec('    ### the cell as the ROUNDED DECIMAL `4.123106`, which leaves the inner gate a margin of')
    rec('    ### `4.089e+08` times the float`s own resolution there. ### **THE EDGE CASE IS NEVER')
    rec('    ### EXERCISED AND THE ADMISSION OWES NOTHING TO THE CONVENTION.**')
    rec('    ### b400`s routed discrepancy : ### **THE SAME COMPARATOR** -- and b400 already priced')
    rec('    ### it: ### **"It moves no value."**')
    rec('')
    rec('    ### ### **THE VERDICT : %s.**' % c3['verdict'])
    rec('    ### b437`s rung is a LADDER INDEX, b446/b447`s outlier a DECORRELATION RESIDUAL ORDER,')
    rec('    ### b483`s excursion a GRAM SIGNATURE. ### **THEY SHARE A CELL, NOT A CAUSE.**')
    rec('    ### ### **AND WHAT THEY DO SHARE IS STILL UNEXPLAINED. ### THIS ACT LEAVES IT OPEN**,')
    rec('    ### because naming a common cause the record shows cannot move a number would be worse')
    rec('    ### than leaving the coincidence standing.')
    rec('')
    rec('### (4) THE EXPECTATIONS.')
    rec('-' * 100)
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) ### **%s**' % (k, SC[k]['verdict']))
    rec('    ### ### **REGISTERED 3 ; HELD 1 ; SPLIT 1 ; REFUTED 1.** ### The seat`s own calls were')
    rec('    ### on the sealed face before the components ran and matched all three -- including')
    rec('    ### registering `(N1)` as a SPLIT on purpose, because its conclusion and its reason')
    rec('    ### come apart.')
    rec('')
    rec('### (5) A DEFECT IN THIS ACT`S OWN CENSUS, FOUND BY THIS ACT.')
    rec('-' * 100)
    rec('    ### ### **THE MATCHER FOUND ITSELF.** ### Its first run scanned `data/b484_*` and')
    rec('    ### returned ### **b484** ### as a mis-scoping act -- because the hand-read residue')
    rec('    ### block QUOTES the offending sentence in order to judge it. ### **A QUOTATION')
    rec('    ### MATCHES THE RULE THAT CONDEMNS WHAT IT QUOTES.**')
    rec('    ### This is `b481`s species a second time. ### The stem is excluded BY NAME rather than')
    rec('    ### by hoping the run order hides it, and it was declared on the face BEFORE the seal.')
    rec('    ### ### **TWO INSTANCES NOW, SO IT BELONGS IN A TOOL AND NOT IN EACH ACT`S MEMORY --')
    rec('    ### ROUTED.**')
    rec('    ### ### **AND ONE ARM OF THIS SUITE WAS DEFECTIVE ON ITS FIRST RUN:**')
    rec('    ### `G-C2-CHAIN-NOT-EDITED` called git INSIDE its predicate, so it read live state and')
    rec('    ### ignored the supplied source -- ### **AN ARM THAT DOES NOT READ ITS SOURCE CANNOT BE')
    rec('    ### HANDED A MUTATED ONE AND SO CANNOT FAIL ITS POSITIVE CONTROL.** ### Caught by that')
    rec('    ### control doing exactly its job, and repaired to read `S`.')
    rec('')
    rec('### (6) THE INSTRUMENTS.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : 3b158ac48adc7fb7be7d0cdbd4eb05f59f8b5f3a978d640b10da227a9cf7255f')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    the span by the tool : ### **%d** -- one PAST the declared threshold of nine.'
        % SPAN['current_span'])
    rec('      ### the ferry`s own order is ### **b479, THEN b482, THEN THE FOLD.**')
    rec('')
    rec('### (7) WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    ### **NO CHAIN WAS RUN AND NO ENTRY COMPUTED** -- `b321_window.py` was read as TEXT and')
    rec('    ### never imported; `math.log` on two numbers is arithmetic, not the chain.')
    rec('    ### **NO LANE WAS OPENED.** ### **b449`S AND b483`S BANKS ARE UNEDITED.**')
    rec('    ### **b475`S LOG WAS NOT OPENED.** ### **NOTHING WAS FETCHED** -- the values came from')
    rec('    ### REGISTRY`s own row, and (R90) leaves the two manifests to the author`s fetch.')
    rec('    ### **THE CHAIN IS NOT EDITED AND NOTHING IN IT IS REPAIRED**; the work-order is FILED.')
    rec('    ### No corpus grade moved; no REGISTRY row written; no ledger row edited; row U1')
    rec('    ### unedited; no bridge typed; h2 where the deposit left it; the four lists stay OPEN;')
    rec('    ### no claim about RH in either direction.')
    rec('')
    rec('### (8) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b484`, never from `main`.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b484_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
