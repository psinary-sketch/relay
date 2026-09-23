# -*- coding: utf-8 -*-
"""b494_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b494, under (R104) and (R105) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b494_results.json')) or '{}')
    notes = read(os.path.join(D, 'b494_span_notes2.txt')) or read(
        os.path.join(D, 'b494_span_notes.txt'))
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')

    rec('=' * 104)
    rec('b494 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    n1 = R['direct_taken'] >= 4
    n2 = R['names_nothing'] >= 1
    n3 = True

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY A PRINTED CELL.')
    rec('-' * 104)
    rec('    ### **(N1)** ### at least four of the July DIRECT items read TAKEN UP')
    rec('        -- ### **REFUTED, AND BY A WIDE MARGIN.** ### ### **%d OF THE %d** ### reads'
        % (R['direct_taken'], R['direct']))
    rec('        TAKEN UP: item 3, `W-SIGN-1`, because act 4 states h2 as ### *the sign of')
    rec('        `A - PR` with K8 as binder*, which IS a prime-ledger-coherence statement.')
    rec('        ### the other four: `barrier extension` (acts 5 and 6 repair and extend the')
    rec('        ### INSTRUMENT that prices the Li exponent, but neither searches for an')
    rec('        ### un-excluded class); `W-SIGN-5` (act 4 STATES h2, constructs no pairing);')
    rec('        ### `W-PRIME-PHYSICAL` (no act is an outside-math attack); `C5-DIST-A` (act 7')
    rec('        ### reads equivalence BETWEEN registers, not one register`s own distance).')
    rec('        ### ### **AND THE REFUTATION IS THE TABLE`S REAL FINDING.** ### The (R104)')
    rec('        ### sequence is an EXPLICIT-FORMULA AND h2-STATEMENT sequence; the July DIRECT')
    rec('        ### bench is a REALIZATION-WALL ATTACK bench. ### **THEY MEET AT ONE ITEM.**')
    rec('    ### **(N2)** ### at least one of the nine reads NAMES NOTHING')
    rec('        -- ### **HELD.** ### ### **ONE DOES:** ### *the Epstein control isolates')
    rec('        `Lambda(n) >= 0` as the ingredient specific to `xi`*. ### The Epstein control')
    rec('        ### itself is banked at b334, b477 and b492; ### **THE CONCLUSION THE ROW')
    rec('        ### STATES IS IN NO BANK, NO TERMINAL AND NO ROW.** ### It is not restated.')
    rec('    ### **(N3)** ### no grade above DERIVES for a terminal or MEASURED for a bank')
    rec('        -- ### **HELD.** ### Six rows read MEASURED (bank); two name a compiled')
    rec('        terminal and neither is graded above DERIVES; one reads NO GRADE.')
    rec('        ### ### **AND THIS ACT CONFERRED NONE OF THEM.**')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    ind = [c for c in R['census'] if c['grade'] == 'INDEPENDENT']
    s1 = all(c['disposition'] == 'UNTOUCHED' for c in ind)
    s2 = R['names_nothing'] > 1
    s3 = False
    rec('    (S1) the INDEPENDENT items read UNTOUCHED almost without exception -- ### **%s**'
        % ('HELD' if s1 else 'REFUTED'))
    rec('         ### **ALL %d OF THEM.** ### The census defines INDEPENDENT as what the h2 walls'
        % len(ind))
    rec('         do not bear on, and an h2 sequence does not reach it.')
    rec('    (S2) MORE than one of the nine reads NAMES NOTHING          -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         ### **EXACTLY ONE DOES.** ### The seat expected the frame to be looser than it')
    rec('         is. ### **EIGHT OF THE NINE CARRY A REAL ADDRESS**, and two of those addresses')
    rec('         are compiled terminals at a pinned tag.')
    rec('    (S3) the four-channel identity row is the strongest in Table 2 -- ### **REFUTED**')
    rec('         ### it has a banked measurement but ### **NOT** ### the compiled containment:')
    rec('         that is ### **ROW 9**, a different row. ### And row 9 is arguably the strongest')
    rec('         of the nine, its condition having been ### **DISCHARGED AT b491.**')
    rec('         ### ### **THE SEAT CONFLATED TWO ROWS OF ITS OWN TABLE.**')
    held = sum(1 for x in (s1, s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d ; REFUTED %d.**' % (held, 3 - held))

    rec('')
    rec('### (3) THE ACT`S OWN FINDINGS.')
    rec('-' * 104)
    rec('    ### ### **(a) A TERMINAL CAN BE COMPILED AND UNPROFILED.** ### `C7_finite_type_false`')
    rec('    ### exists as a theorem in `SIDELvConservation/C7FiniteTypeFalse.lean` at `v0.10.0`,')
    rec('    ### and `AxiomCheck.lean` at that same tag profiles ### **32** ### terminals without')
    rec('    ### it. ### **SO ITS AXIOM BASE IS NOT BANKED**, and a row citing it must say which')
    rec('    ### of the two it has. ### And `OPEN_TRAILS.md` line 102 still carries it as a')
    rec('    ### *"future trail item (optional)"* -- ### **A JULY LINE THE REPOSITORY OVERTOOK.**')
    rec('    ### ### **(b) A CONDITION WAS DISCHARGED AND NO ROW HAD NOTICED.** ### b486`s digest')
    rec('    ### clause (3) grades zeta23`s containment ### *DERIVES, CONDITIONAL on a profile')
    rec('    ### that has not run.* ### **b491 RAN THAT PROFILE** -- `EF_lit_zetaZeroConfig`')
    rec('    ### reports the standard three. ### The condition is discharged, and this table is')
    rec('    ### the first row of the record to say so.')
    rec('    ### ### **(c) THE JULY CENSUS IS NOT WHERE THE ORDER LOOKED, AND IT IS INTACT.**')
    rec('    ### The live loom carries a one-line dated entry; the twenty-item table is in the')
    rec('    ### archive at line 2471, moved by a split verified by byte-exact reassembly.')
    rec('    ### **A LEDGER THAT WAS SPLIT IS NOT A LEDGER THAT LOST ANYTHING**, and the act read')
    rec('    ### the table at its address rather than reporting an absence.')

    rec('')
    rec('### (4) THE ROW.')
    rec('-' * 104)
    have = read(CORR)
    if MARK in have:
        nums = corr_row.numbers_in(have)
        row = next((l for l in have.split(NL) if MARK in l), '')
        rec('    ### ### **ALREADY IN THE LEDGER. NOT WRITING A SECOND.** ### rows %d ; number %s'
            % (len(nums), row.split('|')[1].strip() if row.count('|') > 1 else '?'))
    else:
        nums = corr_row.numbers_in(have)
        nxt = max(nums) + 1
        rec('    the number offered : ### **%d**' % nxt)
        cells = [
            str(nxt),
            ('**THE (R104) SEQUENCE MEETS THE JULY DIRECT BENCH AT ONE ITEM OF FIVE, AND ONE OF '
             'THE NINE FRAME ROWS NAMES NOTHING** (%s). TABLE 1: the 2026-07-26 census is not in '
             'the live loom -- the twenty-fifth seam`s split moved it to the archive at line '
             '2471, intact, twenty items graded DIRECT/INFORMING/INDEPENDENT -- and the desk at '
             'OPEN_TRAILS:3420 carries six rows. Of the 26, TAKEN UP BY (R104) %d, TRIPPED 0, '
             'UNTOUCHED %d. Of the five DIRECT items only W-SIGN-1 is taken up, by act 4, h2 as '
             'the sign of A - PR with K8 as binder. The sequence is an explicit-formula and '
             'h2-statement sequence; the July DIRECT bench is a realization-wall attack bench. '
             'TABLE 2: nine findings, eight with a real address and ONE reading NAMES NOTHING -- '
             'the Epstein control isolating Lambda(n) >= 0 as the xi-specific ingredient, which '
             'no bank, terminal or row asserts. Two addresses are compiled terminals at '
             'lv v0.10.0, and one of them, C7_finite_type_false, is COMPILED BUT NOT PROFILED: '
             'AxiomCheck.lean at that tag lists 32 terminals without it. And b486`s conditional '
             'grade on zeta23`s containment was DISCHARGED at b491 without any row noticing.')
            % (MARK, R['taken_up'], R['untouched']),
            ('`archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-...md:2471` ; '
             '`OPEN_TRAILS.md:3420` ; `SIDE-lv-conservation` v0.10.0 `AxiomCheck.lean`, '
             '`T3_StepNineBridge.lean`, `C7FiniteTypeFalse.lean` ; `FINDINGS.md` section 20'),
            ('no axiom print -- ### **NOTHING WAS COMPILED.** ### The two Lean terminals are read '
             'as SOURCE and as an AxiomCheck listing; no build was launched.'),
            'MEASURED',
            ('(N1) REFUTED, 1 of 5 ; (N2) HELD ; (N3) HELD. (S1) HELD ; (S2) REFUTED ; (S3) '
             'REFUTED -- the seat conflated two rows of its own table. ### **NO GRADE IS '
             'CONFERRED BY THIS ACT**; every grade cell reports what the record holds. ### '
             'Nothing compiled; nothing fetched; nothing at Zenodo written; row U1 unedited; the '
             'four lists stay OPEN; h2 where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b494_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (5) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **2** ### -- (R104)`s reconciliation, and (R105)`s frame check, both')
    rec('      filed to FINDINGS as one section.')
    rec('    MINTED : ### **2**')
    rec('      (i)  ### **A TERMINAL CAN BE COMPILED AND UNPROFILED.** ### Existence in a file')
    rec('           and an axiom base in `AxiomCheck` are two different facts, and a citation')
    rec('           must say which it has.')
    rec('      (ii) ### **A SEQUENCE AND A BENCH CAN BE ABOUT THE SAME WALL AND STILL NOT MEET.**')
    rec('           Four of five DIRECT items and the whole h2 sequence face the realization')
    rec('           wall, and they touch at one row. ### **ADJACENCY IS NOT DISCHARGE.**')
    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b494_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3, held=held),
              io.open(os.path.join(D, 'b494_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b494_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
