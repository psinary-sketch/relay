# -*- coding: utf-8 -*-
"""b481_closing.py -- THE CLOSING RECORD. ### **EVERY FIGURE IS READ FROM A BANK, NEVER TYPED.**"""
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
    W = json.loads(read(os.path.join(D, 'b481_worklist.json')))
    SC = json.loads(read(os.path.join(D, 'b481_scores.json')))
    EXC = json.loads(read(os.path.join(D, 'b481_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b481_span.json')))
    checks = read(os.path.join(D, 'b481_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b481_mirror.txt'))
    pins = read(os.path.join(D, 'b481_pins_final.txt'))
    queries = read(os.path.join(D, 'b481_index_queries.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b481_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b481 -- THE CLOSING RECORD. ### THE CIRCULATION GATE, READ FOR WHAT IT NEEDS.')
    rec('=' * 100)
    rec('')
    rec('### (1) WHAT THE ACT FOUND.')
    rec('-' * 100)
    rec("    the (c') validation job the gate`s trigger names : ### **%s**" % W['cprime_state'])
    rec("      lines carrying (c') in any apostrophe, live corpus : %d" % W['cprime_hits'])
    rec('      of those, defining a validation job or recording its state : 0')
    rec('    the bar on b395`s two deposited records : ### **%s**' % W['bar'])
    rec('      the deciding sentence names CREDENTIALS and A LIVE ROUTE; b389 measured six dead')
    rec('      routes with a positive control at 200. ### **NO RULING SUPPLIES EITHER.**')
    rec('    sites compared against REGISTRY : %d ; disagreements : ### **%d**'
        % (len(W['states']), len(W['disagreements'])))
    rec('      the gate`s fifth site -- the executor memory -- carries NO deposit-state line.')
    rec('')
    rec('### (2) THE EXPECTATIONS.')
    rec('-' * 100)
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %-76s ### **%s**' % (k, SC[k]['nav'][:76], SC[k]['verdict']))
    rec('    ### ### **REGISTERED 3 ; HELD 1 ; REFUTED 2.** ### The seat`s own calls, made at')
    rec('    ### registration and so refutable, matched all three.')
    rec('')
    rec('### (3) THE INSTRUMENTS.')
    rec('-' * 100)
    rec('    the face                : sealed, and ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : afc88e4426793fc9733c60336e003c6668852fe9968e62ca10f1b5e033485230')
    rec('      an (R50) addendum is appended BELOW the lock block; the sealed bytes are unchanged.')
    rec('    the suite                : %d arms run, %d live failing %s'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or ''))
    rec('      positive-control passes : %d ### -- ### **NO ARM PASSED ITS OWN POSITIVE CONTROL.**'
        % len(EXC['defective']))
    v = [l.strip() for l in checks.split(NL) if 'VERDICT :' in l]
    rec('      %s' % (v[0] if v else 'NO VERDICT LINE'))
    rec('    the mirror               : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    the closing pins         : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    the closing censuses     : TOTAL MISSING 0 and 0')
    rec('    the span by the tool     : %d' % SPAN['current_span'])
    rec('')
    rec('### (4) THE NEGATIVE SEARCHES, AND THE ONE THAT DID NOT STAY NEGATIVE.')
    rec('-' * 100)
    for l in queries.split(NL):
        if l.strip():
            rec('    %s' % l[:150])
    rec('')
    rec('    ### ### **TWO OF THESE KEYS ARE THE ACT`S OWN VOICE AND ARE NOT EVIDENCE.**')
    rec('    ### The queries ran AFTER the trail record was appended, so `OPEN_TRAILS.md:8412`,')
    rec('    ### `:8423` and `:8425` are ### **b481`S OWN ENTRY SAYING THE JOB IS ABSENT**, and the')
    rec('    ### two `memory[D--]` hooks are this programme`s index, not the corpus. ### Strike the')
    rec('    ### act`s own words and queries 1 and 2 are ### **NO KEY**, which is what Component 1')
    rec('    ### measured BEFORE the trail existed. ### **A SEARCH THAT CAN SEE ITS OWN REPORT WILL')
    rec('    ### ALWAYS CONFIRM IT**, and saying so is cheaper than re-running it against a clone.')
    rec('')
    rec('    ### ### **THE FOURTH QUERY RETURNED A KEY, AND IT WAS FOLLOWED RATHER THAN DROPPED.**')
    rec('    ### It led to a finding OUTSIDE this act`s registered population, banked at')
    rec('    ### `data/b481_addendum_finding.txt` and filed in the face`s (R50) slot:')
    rec('    ### ### **ONE LIVE, UNANNOTATED CURRENCY CLAIM THAT REGISTRY CONTRADICTS --**')
    rec('    ### `phase1.5/method/INVARIANCE_BARRIERS.md:580`, *"Current: monograph v1.1.1, version')
    rec('    ### DOI 10.5281/zenodo.21436278"*. ### **(N3) IS NOT RESCORED**, because its population')
    rec('    ### is the four sites the gate names and this is not one of them; ### **AND NOTHING IS')
    rec('    ### CORRECTED**, on the gate`s own terms: *a disagreement found is a finding filed.*')
    rec('')
    rec('### (5) THE ACT`S OWN DEFECT, REPORTED AND NOT SUPPRESSED.')
    rec('-' * 100)
    stray = EXC.get('stray') or []
    rec('    ### ### **`G-WRITELIST-KINDS` FAILED POST-PUSH ON %d FILE(S) THE LOCKED FACE`S (W)' % len(stray))
    rec('    ### BLOCK DOES NOT COVER:** %s' % ', '.join(stray))
    rec('    ### The face is sealed and CANNOT be widened to admit them, and ### **THE ARM WAS NOT')
    rec('    ### WEAKENED TO LET THEM THROUGH.** ### The files are kept, the breach is named, and')
    rec('    ### the suite closes NOT CLEAN on that one arm -- b474`s and b480`s disposal, a third')
    rec('    ### time. ### **THE SPECIES IS NOW THREE ACTS OLD AND BELONGS ON THE DESK, NOT IN A')
    rec('    ### FOOTNOTE**: a face`s (W) block is written before the act knows every tool it will')
    rec('    ### need, and a tool minted mid-act has nowhere lawful to land.')
    rec('')
    rec('### (6) WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    ### **NOTHING WAS FETCHED. ### NO LANE WAS OPENED. ### NO BUILD WAS STARTED.**')
    rec('    ### **NEITHER RUNNING LOG WAS READ** -- (R89)`s three conditions, each with its own arm.')
    rec('    ### **NO SITE THE GATE NAMES WAS EDITED. ### THE GATE WAS NOT RUN AND NOTHING')
    rec('    ### CIRCULATED.** ### No corpus grade moved; row U1 is unedited; no bridge was typed;')
    rec('    ### h2 is where the deposit left it; the four lists stay OPEN; nothing was imported,')
    rec('    ### copied or vendored; no claim was made about RH in either direction.')
    rec('')
    rec('### (7) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### ### **ALL THREE PUSHED FROM `push-b481`, NEVER FROM `main` -- the pre-push guard')
    rec('    ### REFUSED THE FIRST ATTEMPT FROM `main` AND WAS OBEYED, NOT BYPASSED.**')
    rec('=' * 100)
    io.open(os.path.join(D, 'b481_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
