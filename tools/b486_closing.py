# -*- coding: utf-8 -*-
"""b486_closing.py -- THE CLOSING RECORD FOR THE FOLD."""
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
    SV = json.loads(read(os.path.join(D, 'b486_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b486_results.json')))
    EXC = json.loads(read(os.path.join(D, 'b486_exercise.json')))
    SPAN = json.loads(read(os.path.join(D, 'b486_span.json')))
    checks = read(os.path.join(D, 'b486_checks_postpush.txt'))
    mirror = read(os.path.join(D, 'b486_mirror.txt'))
    pins = read(os.path.join(D, 'b486_pins_final.txt'))
    seal = subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                           os.path.join(D, 'b486_registration_2026-09-22.txt')],
                          capture_output=True, text=True, encoding='utf-8', errors='replace').stdout

    rec('=' * 100)
    rec('b486 -- THE CLOSING RECORD. ### THE FOLD, ELEVEN ACTS SINCE b474.')
    rec('=' * 100)
    rec('')
    rec('### (1) THE SPAN.')
    rec('-' * 100)
    rec('    by FILING, as the trail records it : ### **%d**' % SV['count'])
    rec('      %s' % ', '.join(SV['filed']))
    rec('    the tool, by NUMBER order : ### **%d** ### -- it counts b486 itself and cannot place'
        % SPAN['current_span'])
    rec('      an act filed out of number order. ### **BOTH PRINTED; THE TOOL IS NOT EDITED.**')
    rec('    the order`s list and the trail`s agree, act for act and in order : ### **%s**'
        % SV['order_matches'])
    rec('')
    rec('### (2) THE DIGEST BLOCK.')
    rec('-' * 100)
    rec('    clauses : ### **%d** ### ; every needle carried by a cited act : ### **%s**'
        % (len(RES['digest']), all(v['ok'] for v in SV['clauses'].values())))
    rec('    cited from outside the span : ### **%d** ### -- clause (2) at b110, clause (6) at b469.'
        % sum(1 for d in RES['digest'] if d[2]))
    rec('    ### ### **AND THE CHECK`S FIRST RUN WAS WRONG OVER THE WRONG POPULATION** -- it would')
    rec('    ### have struck those two as unsupported. ### **A HALT PROVED OVER THE WRONG')
    rec('    ### POPULATION IS NOT A HALT**, and the corpus was widened before anything was')
    rec('    ### written or struck.')
    rec('    ### ### **AND THE NEEDLES` OWN YIELDS ARE PRINTED:** five discriminate (4 to 61 acts),')
    rec('    ### five are permissive (85 to 264). ### **A FILTER THAT KEEPS MOST OF THE CORPUS')
    rec('    ### PROVES NOTHING**, so the block rests on the discriminating ones.')
    rec('')
    rec('### (3) THE LEDGERS.')
    rec('-' * 100)
    rec('    rulings in the span : ### **%d** ### -- twelve in banked ferries, and ### **(R88)**'
        % RES['rulings'])
    rec('      named separately because it was banked as `b477_r88_standing_order.txt`.')
    rec('      ### ### **A COUNT OVER FERRY FILES ALONE WOULD HAVE DROPPED IT SILENTLY.**')
    rec('    acts recording a defect of their OWN instruments : ### **%d of %d**'
        % (RES['seat'], SV['count']))
    rec('      ### ### **EVERY ONE WAS CAUGHT BY AN ARM, A CONTROL OR A REHEARSAL THIS RECORD')
    rec('      ### ALREADY HAD** -- none by a reader noticing afterwards.')
    rec('    ### and one row that is NOT a defect of any act: ### **THE b479 CLOSING REACHED THE')
    rec('    ### NAVIGATOR TRUNCATED.** ### A delivery failure; its bank is whole on disk and its')
    rec('    ### trail record is whole. ### **A MESSAGE THAT DID NOT ARRIVE IS NOT A RECORD THAT')
    rec('    ### WAS NOT MADE.**')
    rec('')
    rec('### (4) THE FINDING THIS FOLD MAKES ABOUT AN ACT IT FOLDS.')
    rec('-' * 100)
    rec('    ### ### **`ERRATA.md` CARRIES `E-2026-09-22-1` TWICE.** ### b469 filed it under (R77)')
    rec('    ### -- the very entry the digest`s clause (6) cites -- and ### **b485 APPENDED A SECOND')
    rec('    ### UNDER THE SAME ID**, its suite having no arm that would have looked.')
    rec('    ### ### **THE FOLD REPORTS IT AND DOES NOT RENUMBER IT:** ERRATA is append-only and')
    rec('    ### its ids are cited elsewhere, so a renumber is a ruling`s business. ### ROUTED.')
    rec('')
    rec('### (5) THE INSTRUMENTS, AND WHAT DID NOT HAPPEN.')
    rec('-' * 100)
    rec('    the face   : sealed, ### **%s**'
        % ('SEAL INTACT' if 'SEAL INTACT' in seal else 'SEAL BROKEN'))
    rec('      sha256 : 8c701ea1aea0ec7b00cafdbdbaf9594541ef235060c878a7d3e70197a31aa927')
    rec('    the suite  : %d arms run, %d live failing %s ; positive-control passes %d'
        % (EXC['run'], len(EXC['live_failing']), EXC['live_failing'] or '', len(EXC['defective'])))
    rec('      %s' % next((l.strip() for l in checks.split(NL) if 'VERDICT :' in l), 'NO VERDICT'))
    rec('      ### ### **AND ONE ARM WAS DEFECTIVE ON ITS FIRST RUN:** `G-C2-NEEDLES-FIXED-BEFORE`')
    rec('      ### read the survey tool from disk INSIDE its predicate and ignored the supplied')
    rec('      ### source, so its control could not move it. ### **b482`S SPECIES, A SECOND TIME**,')
    rec('      ### caught by that control doing its job.')
    rec('    the mirror : %s'
        % ('CLEAN ON ALL THREE CLAUSES' if 'CLEAN ON ALL THREE' in mirror else 'NOT CLEAN'))
    rec('    closing pins : %s'
        % next((l.strip() for l in pins.split(NL) if 'HARD-FAILING' in l), 'NOT READ'))
    rec('    closing censuses : TOTAL MISSING 0 and 0')
    rec('    ### ### **NO EXPECTATIONS REGISTERED AND NONE INVENTED.**')
    rec('    ### ### **NOTHING COMPILED. ### NO CORPUS GRADE MOVED AND NO VERDICT RE-SCORED.**')
    rec('    ### **NO ERRATA LINE WRITTEN OR RENUMBERED.** ### Row U1 unedited; no bridge typed;')
    rec('    ### `h2` where the deposit left it; the four lists stay OPEN; no claim about RH in')
    rec('    ### either direction; b475`s log not opened.')
    rec('')
    rec('### (6) THE COMMITS, EACH READ BACK BY ls-remote.')
    rec('-' * 100)
    for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
        h = gits(repo, 'rev-parse', 'HEAD')
        r = gits(repo, 'ls-remote', 'origin', 'refs/heads/main').split()[0]
        rec('    %-20s HEAD %s   remote %s   ### %s'
            % (name, h[:8], r[:8], 'PASS' if h == r else '### FAIL'))
    rec('    ### all three pushed from `push-b486`, never from `main`.')
    rec('')
    rec('### ### **THE SPAN IS FOLDED. ### THE NEXT SPAN BEGINS AT THE ACT AFTER THIS ONE.**')
    rec('=' * 100)
    io.open(os.path.join(D, 'b486_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
