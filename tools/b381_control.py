# -*- coding: utf-8 -*-
"""b381_control.py -- COMPONENT 3. ### **THE CONTROL, RUN BEFORE ANY CORPUS NUMBER EXISTS.**

### ### **THIS FILE PRINTS NO CORPUS-WIDE FIGURE AND COMPUTES NONE.** ### The order's construction is
### that co-location is scored on the exemplar set ALONE and reported, and only then -- and only if it
### separates -- does the corpus get scored. ### **A PREDICATE CANNOT BE TUNED TO A RESULT IT HAS NOT
### ### SEEN**, and the separation is the guarantee rather than a promise.

### ### ### **SEPARATION IS DEFINED HERE, BEFORE THE SCORES EXIST, IN THREE BRANCHES:**
###   ### **SEPARATES** ### -- every synthesis exemplar scores `C+` and no gathering exemplar does.
###     ### **ONLY THIS BRANCH ADOPTS.**
###   ### **PARTLY** ### -- the `C+` rate is higher among the synthesis exemplars than among the
###     gathering ones, but the two sets overlap. ### **THIS DOES NOT ADOPT**, and what would be
###     needed is stated.
###   ### **DOES NOT SEPARATE** ### -- the `C+` rate among gathering exemplars is at least as high as
###     among synthesis ones. ### **THIS DOES NOT ADOPT.**
### ### **AND THE THRESHOLD-FREE CHECK IS REPORTED BESIDE ALL THREE:** ### whether the lowest synthesis
### ratio exceeds the highest gathering ratio, which is separation no choice of threshold could
### manufacture. ### **IT CANNOT ADOPT WHAT THE DECLARED THRESHOLD REJECTED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import co_location as CL      # noqa: E402
import role_structure as RS   # noqa: E402
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b381 -- COMPONENT 3. ### THE CONTROL, RUN BEFORE ANY CORPUS NUMBER EXISTS.')
    rec('=' * 100)

    # ---------------------------------------------------------------- THE FIXTURES, PRINTED FIRST
    rec('')
    rec('-' * 100)
    rec('  ### THE PREDICATE`S OWN FIXTURES, BEFORE IT SCORES ANY REAL DOCUMENT.')
    rec('-' * 100)
    ok, log = CL.self_test(False)
    for c in log:
        rec('    %-72s got %-14s want %-14s %s'
            % (c['case'][:72], c['got'][:14], c['want'][:14],
               'ok' if c['got'] == c['want'] else '### MISMATCH ###'))
    rec('  ### ### **FIXTURES : %s**' % ('ALL PASS' if ok else '### FAILED'))
    rec('  ### ### **THE ONE THAT MATTERS IS THE COLLECTION:** ### the SAME two sources, one per')
    rec('  ### entry, score `C-` where one paragraph scores `C+`. ### **A BLANK-LINE-ONLY SPLITTER')
    rec('  ### ### WOULD HAVE SCORED THEM IDENTICALLY**, which is why the unit was fixed on the face.')
    if not ok:
        run_clock.write(D, 'b381_control_notes', LINES)
        return 1

    EX = json.load(io.open(os.path.join(D, 'b381_exemplars.json'), encoding='utf-8'))
    index = RS.build_index(PP)
    rec('')
    rec('  ### the document index the predicate resolves names through : %d entries' % len(index))

    def score_set(files):
        out = []
        for rel in files:
            p = os.path.join(PP, rel.replace('/', os.sep))
            if not os.path.exists(p):
                continue
            txt = io.open(p, encoding='utf-8', errors='replace').read()
            mark, why, ev = CL.score(rel, txt, index)
            out.append(dict(file=rel, mark=mark, why=why, ratio=ev['ratio'],
                            bearing=ev['source_bearing_units'], colocating=ev['colocating_units'],
                            units=ev['units'], kinds=ev['bearing_kinds']))
        return out

    syn = score_set(EX['synthesis_set'])
    gat = score_set(EX['gathering_set'])

    rec('')
    rec('-' * 100)
    rec('  ### THE SYNTHESIS EXEMPLARS (%d) -- the record`s own class declarations.' % len(syn))
    rec('-' * 100)
    rec('    %-62s %-5s %-8s %s' % ('DOCUMENT', 'MARK', 'RATIO', 'CO-LOCATING / BEARING'))
    for r in sorted(syn, key=lambda x: -x['ratio']):
        rec('    %-62s %-5s %-8.3f %d / %d'
            % (r['file'], r['mark'], r['ratio'], r['colocating'], r['bearing']))

    rec('')
    rec('-' * 100)
    rec('  ### THE GATHERING EXEMPLARS (%d) -- the record`s own purpose statements.' % len(gat))
    rec('-' * 100)
    rec('    %-62s %-5s %-8s %s' % ('DOCUMENT', 'MARK', 'RATIO', 'CO-LOCATING / BEARING'))
    for r in sorted(gat, key=lambda x: -x['ratio']):
        rec('    %-62s %-5s %-8.3f %d / %d'
            % (r['file'], r['mark'], r['ratio'], r['colocating'], r['bearing']))

    # ------------------------------------------------------------------------ THE SEPARATION
    syn_plus = [r for r in syn if r['mark'] == 'C+']
    gat_plus = [r for r in gat if r['mark'] == 'C+']
    syn_rate = float(len(syn_plus)) / len(syn) if syn else 0.0
    gat_rate = float(len(gat_plus)) / len(gat) if gat else 0.0
    clean = (len(syn_plus) == len(syn) and not gat_plus and bool(syn) and bool(gat))
    if clean:
        branch = 'SEPARATES'
    elif syn_rate > gat_rate:
        branch = 'PARTLY'
    else:
        branch = 'DOES NOT SEPARATE'
    adopted = (branch == 'SEPARATES') and EX['powered']

    lo_syn = min(r['ratio'] for r in syn) if syn else 0.0
    hi_gat = max(r['ratio'] for r in gat) if gat else 0.0
    threshold_free = lo_syn > hi_gat

    rec('')
    rec('=' * 100)
    rec('  ### THE SEPARATION, AT THE DECLARED THRESHOLD OF %.2f.' % CL.THRESHOLD)
    rec('=' * 100)
    rec('  ### synthesis exemplars scoring `C+` : ### **%d of %d (%.1f%%)**'
        % (len(syn_plus), len(syn), 100.0 * syn_rate))
    rec('  ### gathering exemplars scoring `C+` : ### **%d of %d (%.1f%%)**'
        % (len(gat_plus), len(gat), 100.0 * gat_rate))
    rec('  ### ### **THE LOWEST SYNTHESIS RATIO : %.3f ### / ### THE HIGHEST GATHERING RATIO : %.3f**'
        % (lo_syn, hi_gat))
    rec('  ### ### **THE THRESHOLD-FREE CHECK -- NO THRESHOLD COULD SEPARATE THEM UNLESS THIS HOLDS :')
    rec('  ### ### %s**' % threshold_free)
    if gat_plus:
        rec('')
        rec('  ### ### **THE GATHERING EXEMPLARS THAT SCORED `C+` ANYWAY (%d), NAMED:**' % len(gat_plus))
        for r in sorted(gat_plus, key=lambda x: -x['ratio'])[:12]:
            rec('      %-62s %.3f  %d / %d'
                % (r['file'], r['ratio'], r['colocating'], r['bearing']))
        if len(gat_plus) > 12:
            rec('      ### ... and %d more, all in the banked JSON.' % (len(gat_plus) - 12))
    rec('')
    rec('  ### ### ### **THE BRANCH : %s.**' % branch)
    rec('  ### ### **THE EXEMPLAR SET IS %s** -- gathering side %d against the declared floor of %d.'
        % ('POWERED' if EX['powered'] else 'UNDERPOWERED', len(EX['gathering_set']), EX['floor']))
    if not EX['powered']:
        rec('  ### ### **SO THE RESULT IS REPORTED AS NOT DECISIVE**, as the locked face required.')
    rec('  ### ### ### **THE PREDICATE IS %s.**' % ('ADOPTED' if adopted else 'NOT ADOPTED'))
    if not adopted:
        rec('  ### ### **SO THE CORPUS IS NOT RE-SCORED AND NO QUADRANT TABLE IS REDRAWN.** ### That')
        rec('  ### is the order`s own clause and it binds here. ### **THE FINDING IS THAT CO-LOCATION')
        rec('  ### ### DOES NOT READ ROLE EITHER, AND THAT IS A RESULT.**')
        rec('  ### **WHAT WOULD HAVE BEEN NEEDED:** ### every one of the %d synthesis exemplars at'
            % len(syn))
        rec('  ### `C+` and none of the %d gathering exemplars there. ### The distance is %d gathering'
            % (len(gat), len(gat_plus)))
        rec('  ### exemplars above the threshold and %d synthesis exemplars below it.'
            % (len(syn) - len(syn_plus)))
    rec('=' * 100)

    p = run_clock.write(D, 'b381_control_notes', LINES)
    out = dict(fixtures_ok=ok, threshold=CL.THRESHOLD,
               synthesis=syn, gathering=gat,
               synthesis_n=len(syn), gathering_n=len(gat),
               synthesis_cplus=len(syn_plus), gathering_cplus=len(gat_plus),
               synthesis_rate=round(syn_rate, 4), gathering_rate=round(gat_rate, 4),
               lowest_synthesis_ratio=lo_syn, highest_gathering_ratio=hi_gat,
               threshold_free_separation=threshold_free,
               branch=branch, adopted=adopted, powered=EX['powered'],
               corpus_scored=False,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b381_control.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
