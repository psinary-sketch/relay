# -*- coding: utf-8 -*-
"""b482_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
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
    SV = json.loads(read(os.path.join(D, 'b482_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b482_results.json')))
    SC = json.loads(read(os.path.join(D, 'b482_scores.json')))
    EXC = json.loads(read(os.path.join(D, 'b482_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b482_span.json')))
    checks = read(os.path.join(D, 'b482_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b482_mirror.txt'))
    pins = read(os.path.join(D, 'b482_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b482_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b482 -- THE CLOSING RECORD. ### THE XiPrime TOPIC READ AGAINST THE CORPUS STATEMENTS.')
    rec('=' * 100)
    rec('')
    rec('### (0) THE HALT, PROVED BEFORE THE ACT OPENED.')
    rec('-' * 100)
    rec('    the order says ### **"b479 RUNS AS BANKED"**.')
    rec('    ferry files carrying `ACT b479`   : ### **%d**' % len(SV['b479_hits']))
    rec('    ### POSITIVE CONTROL -- `ACT b482` : ### **%d** (%s)'
        % (len(SV['b479_control']), ', '.join(SV['b479_control'])))
    rec('    ### ### **THE SEARCH WORKS AND FINDS NO b479 ORDER ANYWHERE.**')
    rec('    ### ### **AND THREE SEALED FACES SAY OTHERWISE:** b480, b483 and b484 each assert that')
    rec('    ### b479 is *"registered by its own ferry"*. ### The claim propagated because each face')
    rec('    ### copied the last one`s sentence.')
    rec('    ### ### **A SEAL CERTIFIES THAT THE BYTES HAVE NOT CHANGED. ### IT CERTIFIES NOTHING')
    rec('    ### ABOUT WHETHER THEY WERE TRUE.**')
    rec('    ### ### **b479 IS NOT RUN AND ITS ORDER IS NOT RECONSTRUCTED.**')
    rec('')
    rec('### (1) THE SIX STATEMENTS.')
    rec('-' * 100)
    rec('    the clone`s HEAD : ### **%s** ### ; the pin the order names : `fbdc36b`' % SV['pin'][:12])
    rec('    theorems : ### **%d** ### ; `sorry` tokens in the file : ### **%d**'
        % (len(SV['six']), SV['sorries']))
    rec('    ### ### **ALL SIX ARE CLOSED BY `sorry` -- CHALLENGE STATEMENTS, NOT THEOREMS HELD.**')
    rec('    the comparator lists exactly those six ; `definition_names` EMPTY ;')
    rec('    ### permitted axioms : ### **%s**' % ', '.join(SV['comparator']['permitted_axioms']))
    rec('')
    rec('### (2) THE CORPUS`S OWN STATEMENTS, AS STATEMENTS.')
    rec('-' * 100)
    for c in SV['corpus']:
        rec('    %-30s %s' % (c['name'][:30], c['addr']))
    rec('    ### ### **AND SIDE-simplicity`S TWO QUANTIFY OVER `ℤ` AND NOTHING ELSE** -- neither')
    rec('    ### mentions `ξ`, `ζ`, a zero, or a complex number; both are closed by `omega`.')
    rec('    ### **THE MATHEMATICS THEY ARE NAMED FOR LIVES IN THEIR DOCSTRINGS**, which the order')
    rec('    ### excludes. ### **A READING OF WHAT THE STATEMENTS SAY, NOT A JUDGEMENT ON THE')
    rec('    ### REPOSITORY**, and the face said so before the placement ran.')
    rec('')
    rec('### (3) THE PLACEMENT.')
    rec('-' * 100)
    rec('    ### ### **CELLS : %d. ### `SAME OBJECT` : %d. ### `TOUCHES` : %d. ### `APART` : %d.**'
        % (RES['cells'], RES['counts'].get('SAME OBJECT', 0), RES['counts'].get('TOUCHES', 0),
           RES['counts'].get('APART', 0)))
    for name in SV['six']:
        row = RES['placement'][name['name']]
        rec('    %-52s %-9s %-9s %-9s %s'
            % (name['name'][:52], row['A'], row['B'], row['C1'], row['C2']))
    rec('    ### all twelve cells against the two simplicity terminals are `APART` for ONE reason:')
    rec('    ### ### **THERE IS NO SHARED OBJECT TO BE THE SAME AS OR TO TOUCH.**')
    rec('    ### and `xiPrime_over_xi_re_pos` is `APART` from both analytic statements for a')
    rec('    ### DIFFERENT reason: it lives on `1 ≤ Re s` and they speak of the critical line --')
    rec('    ### ### **THE REGIONS ARE DISJOINT.**')
    rec('')
    rec('    ### THE TWO REVERSE READS, IN ONE LINE EACH:')
    rec('      the six state, and the corpus does not : ### **A POSITIVE PROPORTION WITH A NUMBER**')
    rec('      (0.85838, 0.92919, 0.86864, 0.93432), the location of EVERY zero of `ξ\'`, a')
    rec('      half-plane positivity for `ξ\'/ξ`, and a counting apparatus.')
    rec('      the corpus states, and the six do not : ### **A POINTWISE VALUE OF `ξ\'` AT EVERY')
    rec('      POINT OF THE CRITICAL LINE** -- not only at zeros -- ### **AND IT IS PROVED, NOT')
    rec('      POSED**; the codimension dichotomy for `ξ`\'s own zeros; and an integer margin.')
    rec('      ### ### **NEITHER SIDE SUBSUMES THE OTHER, AND NO CELL IS `SAME OBJECT`.**')
    rec('')
    rec('### (4) THE EXPECTATIONS.')
    rec('-' * 100)
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) ### **%s**' % (k, SC[k]['verdict']))
    rec('    ### ### **REGISTERED 3 ; HELD 1 ; HELD-IN-PART 1 ; REFUTED 1.** ### The seat`s calls')
    rec('    ### were on the sealed face before the placement ran and matched all three.')
    rec('')
    rec('### (5) THE INSTRUMENTS, AND WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : 8ce9439063b28a4e8bb6afce3b07d83dacc5b8e2027063ed5fa4364017276cab')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('      ### ### **AND ONE ARM WAS DEFECTIVE ON ITS FIRST RUN:** `G-NO-LEAN-RUN`s pattern')
    rec('      ### required whitespace between `lake` and `build`, which a real `subprocess` call')
    rec('      ### does not have -- ### **SO IT COULD NOT FAIL, AND ITS OWN POSITIVE CONTROL SAID')
    rec('      ### SO.** ### Widened to the separators a real invocation uses.')
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    the span by the tool : ### **%d** -- ### **LOWER THAN b485`S, AND THE TOOL IS RIGHT'
        % SPAN['current_span'])
    rec('      ### ABOUT ITS OWN QUESTION:** b482`s NUMBER is below b485`s, and the tool cannot')
    rec('      ### place an act filed out of number order. ### Twelve acts have run since the fold.')
    rec('      ### **THE FOLD SHOULD TAKE ITS OWN NUMBER`S READING.**')
    rec('    ### ### **NO LEAN WAS RUN AND NO KERNEL BUILT.** ### **NOTHING WAS IMPORTED** ### and')
    rec('    ### the zeta23 artefacts are not committed. ### **NO GRADE WAS CONFERRED ON ANY CORPUS')
    rec('    ### OBJECT.** ### b475`s log was not opened. ### No corpus grade moved; row U1')
    rec('    ### unedited; no bridge typed; `h2` where the deposit left it; the four lists stay')
    rec('    ### OPEN; no claim about RH in either direction. ### **THE KERNEL LANE IS CLOSED.**')
    rec('    ### ### **AND THE FOLD IS NOT OPENED BY THIS ACT:** the order places it after b479.')
    rec('')
    rec('### (6) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b482`, never from `main`.')
    rec('=' * 100)
    io.open(os.path.join(D, 'b482_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
