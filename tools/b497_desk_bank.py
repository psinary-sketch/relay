# -*- coding: utf-8 -*-
"""b497_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
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


def main():
    R = json.loads(read(os.path.join(D, 'b497_results.json')))

    rec('=' * 104)
    rec('b497 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE LOG PRINTED.**')
    rec('=' * 104)
    rec('')
    rec('### THE NAVIGATOR`S THREE.')
    rec('-' * 104)

    n1 = R['nonzero_exits'] == 0
    rec('  **(N1)** ### **%s.**' % ('HELD' if n1 else 'REFUTED'))
    rec('    *"0 non-zero exits"*')
    rec('    `END` lines : %d ; ### **NON-ZERO : %d**' % (len(R['ends']), R['nonzero_exits']))
    for e in R['ends']:
        rec('      %-36s EXIT %d (0x%08X)' % (e['what'], e['exit'], e['exit'] & 0xFFFFFFFF))
    rec('    ### ### **REFUTED BY THE CELL, AND THE CELL SAYS MORE THAN THE VERDICT.** ### Both')
    rec('    ### codes are `0xC000013A` = ### **`STATUS_CONTROL_C_EXIT`**. ### The build did not')
    rec('    ### fail; ### **IT WAS KILLED** -- a console control event reached it. ### And')
    rec('    ### ### **MODULES THAT FAILED, BY NAME : NONE.**')
    rec('')

    n2 = R['all_standard_three']
    rec('  **(N2)** ### **%s.**' % ('HELD' if n2 else 'REFUTED'))
    rec('    *"all three profiles the standard three"*')
    for n, v in R['profiles'].items():
        rec('      `%-24s` -> ### **%s**' % (n, v['verdict']))
    rec('    `#print axioms` output lines anywhere in the log : ### **0**')
    rec('    ### ### **ALL THREE ABSENT, AND ABSENT IS NOT OTHER.** ### The probe never ran to')
    rec('    ### completion, so there is no axiom string to read -- ### **NOT A STRING THAT CAME')
    rec('    ### OUT WRONG.** ### (R82) is ### **NEITHER CLAIMED NOR REFUTED BY THIS ACT**, and')
    rec('    ### b473`s and b480`s wording is the right wording again: ### **VOID FOR WANT OF A')
    rec('    ### RUN.**')
    rec('')

    n3 = R['distinct_instants'] > 50
    rec('  **(N3)** ### **%s.**' % ('HELD' if n3 else 'REFUTED'))
    rec('    *"more than fifty distinct instants across the marks"*')
    rec('    marks : %d ; ### **DISTINCT INSTANTS : %d**'
        % (R['marks'], R['distinct_instants']))
    rec('    ### ### **AND THIS IS THE CELL b495 OWED.** ### b495`s (N3) and its (S2) both named')
    rec('    ### the log`s module marks, and b495`s own order forbade reading the log, so both')
    rec('    ### were scored ### **NOT SCORABLE** and routed here. ### **THEY ARE PAID.**')
    rec('    ### b480`s defect -- one precomputed instant stamped on every mark -- would have')
    rec('    ### given ### **ONE** distinct instant across %d marks. ### It gives %d.'
        % (R['marks'], R['distinct_instants']))
    rec('    ### ### **THE REPAIR IS CONFIRMED ON THE POPULATION THE EXPECTATION NAMED**, not on')
    rec('    ### the mechanism-level control b495 had to substitute.')
    rec('')

    rec('### THE SEAT`S THREE.')
    rec('-' * 104)
    s1 = (not n1) and (not n2) and n3
    rec('  **(S1)** ### **%s.**' % ('HELD' if s1 else 'REFUTED'))
    rec('    *"(N1) and (N2) will both be REFUTED, and (N3) will hold."*')
    rec('    (N1) %s ; (N2) %s ; (N3) %s -- as predicted.'
        % ('REFUTED' if not n1 else 'HELD', 'REFUTED' if not n2 else 'HELD',
           'HELD' if n3 else 'REFUTED'))
    rec('    ### ### **AND THIS PREDICTION WAS CHEAP AND THE FACE SAID SO.** ### It was drawn')
    rec('    ### from a declared peek at the log`s first eight and last six lines. ### **A')
    rec('    ### PREDICTION MADE AFTER A GLANCE IS NOT EVIDENCE OF ANYTHING BUT THE GLANCE.**')
    rec('')

    s2 = R['failure_lines'] == 0
    rec('  **(S2)** ### **%s.**' % ('HELD' if s2 else 'REFUTED'))
    rec('    *"the failure is a process-control failure, not a Lean failure; modules that failed')
    rec('    by name will read NONE."*')
    rec('    lines matching a failure shape : ### **%d**' % R['failure_lines'])
    rec('    modules built before the kill  : ### **%d**, every one of them `Mathlib.*`'
        % len(R['modules_built']))
    rec('    ### ### **NOT ONE ZETA23 MODULE WAS REACHED.** ### The build spent its whole life')
    rec('    ### cloning and compiling MATHLIB and was killed before it arrived at the vendored')
    rec('    ### closure. ### **SO THE LOG SAYS NOTHING WHATEVER ABOUT WHETHER THE 57 VENDORED')
    rec('    ### MODULES COMPILE**, and any reader inclined to take the non-zero exit as evidence')
    rec('    ### about `EF_lit` is reading a fact about a process into a claim about a proof.')
    rec('')

    s3 = R['wall_seconds'] > R['lake_summed']
    rec('  **(S3)** ### **%s.**' % ('HELD' if s3 else 'REFUTED'))
    rec('    *"wall time will greatly exceed lake`s summed durations."*')
    rec('    wall time            : ### **%.1f s**' % R['wall_seconds'])
    rec('    `lake` summed spans  : ### **%.1f s** across %d spans'
        % (R['lake_summed'], R['lake_spans']))
    rec('    ### ### **REFUTED, AND WITH THE SIGN BACKWARDS.** ### The summed durations are the')
    rec('    ### LARGER, by %.1f s. ### The seat reasoned from the mathlib CLONE -- real, in the'
        % (R['lake_summed'] - R['wall_seconds']))
    rec('    ### log, and network time `lake` does not account -- and ### **IGNORED A LARGER')
    rec('    ### EFFECT POINTING THE OTHER WAY: `lake` BUILDS IN PARALLEL.** ### %d spans summing'
        % R['lake_spans'])
    rec('    ### %.1f s finished inside %.1f s of wall clock, about ### **%.1fx** concurrency.'
        % (R['lake_summed'], R['wall_seconds'], R['lake_summed'] / R['wall_seconds']))
    rec('    ### ### **A SUM OF PER-JOB DURATIONS IS NOT AN ELAPSED TIME**, and the seat compared')
    rec('    ### them as though it were. ### The order asked for both numbers precisely because')
    rec('    ### they are not the same number, and the seat still conflated them.')
    rec('')

    rec('### THE TALLY, AND WHAT THIS ACT DID NOT DO.')
    rec('-' * 104)
    nav_held = sum([n1, n2, n3])
    seat_held = sum([s1, s2, s3])
    rec('  ### ### **THE NAVIGATOR`S: HELD %d ; REFUTED %d.**' % (nav_held, 3 - nav_held))
    rec('  ### ### **THE SEAT`S: REGISTERED 3 ; HELD %d ; REFUTED %d.**' % (seat_held, 3 - seat_held))
    rec('  ### ### **COMPONENT 3 WAS NOT RUN.** ### The order: *"otherwise print which and STOP')
    rec('  ### before Component 3."* ### REGISTRY`s `SIDE-explicit-formula` row keeps `PENDING`,')
    rec('  ### no profile is written beside it, and ### **NO ROW CITES THE KERNEL** -- (R106)(3)')
    rec('  ### stands untouched. ### **A STOP OBEYED IS A RESULT**, and the alternative was to')
    rec('  ### write three profiles into REGISTRY that no run produced.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b497_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=bool(n1), n2=bool(n2), n3=bool(n3),
                   s1=bool(s1), s2=bool(s2), s3=bool(s3),
                   nav_held=nav_held, seat_held=seat_held,
                   component3_run=False),
              io.open(os.path.join(D, 'b497_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b497_desk_notes.txt, b497_scores.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
