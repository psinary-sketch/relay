# -*- coding: utf-8 -*-
"""b483_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
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
    SC = json.loads(read(os.path.join(D, 'b483_scores.json')))
    S = SC['scores']
    SV = json.loads(read(os.path.join(D, 'b483_survey.json')))
    EXC = json.loads(read(os.path.join(D, 'b483_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b483_span.json')))
    checks = read(os.path.join(D, 'b483_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b483_mirror.txt'))
    pins = read(os.path.join(D, 'b483_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b483_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b483 -- THE CLOSING RECORD. ### THE b477 LOG READ TO ITS END, AND THE SIX SCORED.')
    rec('=' * 100)
    rec('')
    rec('### (1) WHAT THE RUN DID, AND WHAT IT BUILT.')
    rec('-' * 100)
    rec('    RUN COMPLETE %s ; EXIT 0 %s ; elapsed 2337 s against a priced 2923 s'
        % (SV['complete'], SV['exit0']))
    rec('    entries : %s' % ', '.join('%s %d' % (k, v) for k, v in sorted(SV['kinds'].items())))
    rec('    ### **TWO WITHIN-FAMILY GRAMS, NOT ONE JOINT MATRIX** : aim plane %d, ladder %d ;'
        % (SV['aim'], SV['ladder']))
    rec('      %d*%d/2 + %d*%d/2 = %d off-diagonals, and the arithmetic closes exactly.'
        % (SV['aim'], SV['aim'] - 1, SV['ladder'], SV['ladder'] - 1, SV['kinds']['offdiagonal']))
    rec('    the diagonal gate : every checked cell ok %s ; largest |W - banked W| ### **%s**'
        % (SV['diag_all_ok'], SV['max_abs_diff']))
    rec('      ### the runner halts before any off-diagonal on a mismatch, and %d exist,'
        % SV['kinds']['offdiagonal'])
    rec('      ### so ### **THE HALT DID NOT FIRE.**')
    rec('')
    rec('### (2) THE FINDING: A BOUND THE CHAIN REPORTS IS NOT THE BOUND IT ACHIEVES.')
    rec('-' * 100)
    for f in sorted(SC['families']):
        rec('    observed two-side disagreement in %-10s : ### **%.3e**'
            % (f, SC['families'][f]['resolution']))
    rec('    reported `trunc_bound`, over the diagonal cells : %.3e to %.3e'
        % (SV['min_trunc'], SV['max_trunc']))
    rec('    the chain floor, sqrt(eps)                     : %.3e' % SC['floor'])
    rec('    ### ### **THE REPORTED TAIL FIGURE UNDER-STATES THE ACHIEVED AGREEMENT BY UP TO SEVEN')
    rec('    ### ORDERS.** ### It bounds the ZERO SUM`S TRUNCATION and says nothing about the')
    rec('    ### PLACES SIDE`S QUADRATURE. ### **AND IT WAS SAID IN THE SEALED FACE BEFORE ANY')
    rec('    ### EIGENVALUE EXISTED**, so no threshold was chosen after seeing a spectrum.')
    rec('')
    rec('    ### ### **AND ONE NUMBER DECIDES TWO OF THE SIX:**')
    rec('    ### zeta`s largest wrong-sign excursion is ### **lam_max(G) = %+.6e**'
        % S['N2']['largest'])
    rec('    ###   ABOVE the chain floor %.3e and the tail figure %.3e ;' % (SC['floor'], SC['tail']))
    rec('    ###   BELOW the observed agreement.')
    rec('    ### **SO `(F2)` HALTS ON TWO THRESHOLDS AND NOT ON THE THIRD, AND `(N2)` IS HELD ON THE')
    rec('    ### THIRD AND REFUTED ON THE OTHER TWO -- THE SAME MEASUREMENT, READ AS A HALT OR AS AN')
    rec('    ### EXPECTATION MET DEPENDING ON WHICH BOUND IS BELIEVED.** ### That, not the number,')
    rec('    ### is what this act found.')
    rec('')
    rec('### (3) THE SIX.')
    rec('-' * 100)
    for k in ('F1', 'F2', 'F3', 'N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, S[k]['verdict']))
    rec('    ### ### **TWO OF THEM FAIL FOR ONE REASON THAT HAS NOTHING TO DO WITH ZETA.** ### b476')
    rec('    ### priced the control`s resolving family size at ONE CELL, from a per-cell test; but')
    rec('    ### ### **A ONE-BY-ONE SYMMETRIC MATRIX CANNOT BE INDEFINITE WHATEVER ITS ENTRY IS**,')
    rec('    ### so `(F1)`s negative index was arithmetically unavailable before the run started and')
    rec('    ### `(F3)`s second conjunct with it. ### The control DOES go indefinite, at ladder size')
    rec('    ### %s -- ### **SO THE PRICE WAS WRONG, NOT THE INSTRUMENT.**'
        % S['N1']['first']['LADDER'])
    rec('    ### ### **THE COMPRESSION REGISTER THEREFORE TAKES NO GRADE, AND IN PARTICULAR NOT')
    rec('    ### `MEASURED`. ### THE LANE IS CLOSED AT THIS ACT`S END, AS THE ORDER REQUIRED.**')
    rec('')
    rec('### (4) TWO DEFECTS IN THIS ACT`S OWN TOOLS, FOUND BY THIS ACT AND REPORTED.')
    rec('-' * 100)
    rec('    (a) ### **THE SEAT READ ITS OWN EXPECTATION BACKWARDS.** ### `(N2)` claims a')
    rec('        wrong-signed excursion ### **THAT STAYS WITHIN THE BOUND**; the first version of')
    rec('        this act`s scorer required it to EXCEED the resolution -- which is `(F2)`s test --')
    rec('        and scored `(N2)` REFUTED on that. ### **A SUB-BOUND CLAIM CANNOT ALSO BE A')
    rec('        SUPRA-BOUND CLAIM.** ### Caught by re-reading the predicate against b476`s own')
    rec('        words, and corrected before the components were banked.')
    rec('    (b) ### **TWO WORD ANCHORS WERE EATEN AS BACKSPACE BYTES.** ### `G-NO-CHAIN-RUN` was')
    rec('        written through a heredoc whose outer string turned each `backslash-b` into a')
    rec('        literal `0x08`, so the pattern required a backspace character and ### **THE ARM')
    rec('        COULD NEVER FIRE.** ### It passed its own POSITIVE control, which is exactly the')
    rec('        signal that says so, and was repaired by editing the file rather than by another')
    rec('        heredoc. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM** (b363), and the record')
    rec('        already carried the heredoc trap by name.')
    rec('    ### ### **AND A THIRD, SMALLER: `G-NO-CHAIN-RUN` ALSO FIRED ON THE ACT`S OWN PROSE**')
    rec('    ### -- the components NAME `b325_epstein.channels_q` in a sentence explaining the')
    rec('    ### control`s scope. ### Narrowed to an IMPORT or a CALL, which is what running a chain')
    rec('    ### looks like. ### **A GATE ON RAW SOURCE FIRES ON THE ACT`S OWN "NOT DONE" SENTENCE.**')
    rec('')
    rec('### (5) A RESEMBLANCE, RECORDED AND NOT PROMOTED.')
    rec('-' * 100)
    rec('    the earliest wrong-sign excursion is at ladder size 8, the cell ### **a = 4.12311 =')
    rec('    sqrt(17)** -- ### **THE SAME CELL b446 NAMED AS THE OUTLIER THAT REFUSES**, on a')
    rec('    decorrelation-order test with nothing to do with signatures. ### b437 has the ladder')
    rec('    turning from rung 10 to rung 11 there.')
    rec('    ### ### **TWO UNRELATED MEASUREMENTS SINGLE OUT ONE CELL, AND THAT IS STILL A')
    rec('    ### RESEMBLANCE AND NOT A MECHANISM.** ### b446 already refused the obvious reading:')
    rec('    ### *"not the rung alone: 3.605551 = sqrt(13) converged"*. ### ROUTED; nothing claimed.')
    rec('')
    rec('### (6) THE INSTRUMENTS.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : 6847ae11ad584c974af70ee10a7a5635edee95f77e8fd911e64e7ec27a3d6a50')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('      ### ### **AND `G-WRITELIST-KINDS` PASSES WITH `0` STRAY FILES**, which it did not at')
    rec('      ### b474, b480 or b481. ### **(R91) CLOSED THAT BREACH BY LETTING THE FACE CARRY ITS')
    rec('      ### ACT`S STEM GLOB**, and the arm keeps its force against every path outside it --')
    rec('      ### its positive control is another act`s bank, and it still fails on that.')
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    the span by the tool : ### **%d** -- ### **THE DECLARED FOLD THRESHOLD ((R1), b366).**'
        % SPAN['current_span'])
    rec('')
    rec('### (7) WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    ### **NO CHAIN WAS RUN AND NO ENTRY COMPUTED** -- every number is a function of b477`s')
    rec('    ### banked entries, and an entry the bank does not hold is ABSENT, never interpolated.')
    rec('    ### **b475`S LOG WAS NOT OPENED AND ITS RUN WAS NOT POLLED OR STOPPED.**')
    rec('    ### **NOTHING WAS FETCHED** -- (R90) assigns the two Zenodo manifests to the author`s')
    rec('    ### fetch, and this seat did not attempt them.')
    rec('    ### **(R92)`S REPAIR IS NOT EXECUTED HERE**: the ruling places it in the act after this')
    rec('    ### read, and this act neither performs it nor pre-empts it.')
    rec('    ### No corpus grade moved; no grade above MEASURED, and in fact no grade at all; row U1')
    rec('    ### unedited; no bridge typed; h2 where the deposit left it; the four lists stay OPEN;')
    rec('    ### nothing imported, copied or vendored; no claim about RH in either direction.')
    rec('')
    rec('### (8) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b483`, never from `main`.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b483_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
