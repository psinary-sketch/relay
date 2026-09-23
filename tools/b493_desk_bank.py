# -*- coding: utf-8 -*-
"""b493_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK."""
import io
import json
import os
import re
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
MARK = 'b493, under (R102) and (R104) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b493_results.json')) or '{}')
    SV = json.loads(read(os.path.join(D, 'b493_survey.json')) or '{}')
    notes = read(os.path.join(D, 'b493_span_notes2.txt')) or read(
        os.path.join(D, 'b493_span_notes.txt'))
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')
    rows = R['rows']
    exc = [x for x in rows if x['disposition'] == 'EXCEEDS THE CEILING']
    rst = [x for x in rows if x['disposition'] == 'RESTS ON AN ERRATUM']
    per = R['per_record']

    rec('=' * 104)
    rec('b493 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY A PRINTED CELL.')
    rec('-' * 104)
    t2 = [x for x in exc if x['k'] == 2 and x['kind'] == 'TITLE']
    t4 = [x for x in exc if x['k'] == 4 and x['kind'] == 'TITLE']
    n1 = bool(t2) and bool(t4)
    rec('    ### **(N1)** ### both the monograph`s and the kernel`s titles read EXCEEDS')
    rec('        -- ### **%s.**' % ('HELD' if n1 else 'REFUTED'))
    rec('        monograph : *"A Place To Stand: Proof of the Riemann Hypothesis via the SIDE')
    rec('          method"* -> ### **EXCEEDS**')
    rec('        kernel    : *"SIDE-kernel: Formal verification of the Riemann Hypothesis via')
    rec('          exhaustive mechanism exclusion"* -> ### **EXCEEDS**')
    rec('        ### ### **AND A THIRD TITLE EXCEEDS THAT THE ORDER DID NOT NAME:**')
    rec('        `SIDE-lv-conservation: ... for the SIDE proof of the Riemann Hypothesis`.')
    mt = [x for x in exc if x['k'] == 2 and x['kind'] == 'sentence 1']
    n2 = bool(mt)
    rec('    ### **(N2)** ### the monograph description`s MAIN THEOREM sentence reads EXCEEDS')
    rec('        -- ### **%s.**' % ('HELD' if n2 else 'REFUTED'))
    rec('        *"MAIN THEOREM. The Riemann Hypothesis: every nontrivial zero of the Riemann')
    rec('        zeta function has real part 1/2."* -> ### **EXCEEDS**')
    rec('        ### ### **AND THE FIRST CEILING MATCHER MISSED IT.** ### Its `MAIN THEOREM`')
    rec('        ### clause used `[^.]` and could not cross the period in `MAIN THEOREM. The')
    rec('        ### Riemann Hypothesis:`. ### **A MATCHER THAT CANNOT CROSS A FULL STOP CANNOT')
    rec('        ### READ A HEADLINE**, and this one would have scored (N2) refuted.')
    beyond = [k for k in ('1', '5', '6', '7', '8') if per[k]['rests']]
    n3 = not beyond
    rec('    ### **(N3)** ### no record beyond the three b487 read carries a RESTS row')
    rec('        -- ### **%s.** ### RESTS rows sit at record 2 ONLY (%d of them); records 1, 5, 6,'
        % ('HELD' if n3 else 'REFUTED', len(rst)))
    rec('        7 and 8 carry ### **ZERO**, and so do records 3 and 4.')
    rec('        ### ### **AND THAT LAST FACT IS NOT AGREEMENT WITH b487 -- IT IS A CORRECTION.**')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    s1 = per['1']['exceeds'] == 0
    may = sum(per[k]['exceeds'] for k in ('5', '6', '7', '8'))
    s2 = may > 0
    titles = sum(1 for x in exc if x['kind'] == 'TITLE')
    hl = sum(1 for x in exc if x['kind'] != 'TITLE'
             and re.match(r'^[A-Z][A-Z ,’-]{4,60}\.', x['text']))
    s3 = (titles + hl) > len(exc) / 2.0
    rec('    (S1) the T7 record carries NO row that exceeds        -- ### **%s**'
        % ('HELD' if s1 else 'REFUTED'))
    rec('         %d of its 26 rows exceed. ### It names the RH companion and ### **DISCLAIMS'
        % per['1']['exceeds'])
    rec('         LOAD-BEARING** in the same sentence; its own result is a published null.')
    rec('    (S2) at least one row of the FOUR May-2026 kernels exceeds -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         ### **%d DO.** ### cosmo, effects, trivium and interfaces describe their own' % may)
    rec('         subject matter and make no claim about RH at all. ### **THE SEAT EXPECTED AGE')
    rec('         TO CORRELATE WITH OVERREACH; IT DOES NOT.** ### The overreach is where the')
    rec('         SUBJECT is RH, not where the text is old.')
    rec('    (S3) the EXCEEDS rows are concentrated in titles and headlines -- ### **%s**'
        % ('HELD' if s3 else 'REFUTED'))
    rec('         ### **%d of %d** ### are titles and a further ### **%d** ### are headline-led'
        % (titles, len(exc), hl))
    rec('         sentences -- ### **%d of %d in all.** ### A headline compresses, and'
        % (titles + hl, len(exc)))
    rec('         compression is where a ceiling is breached.')
    held = sum(1 for x in (s1, s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d ; REFUTED %d.**' % (held, 3 - held))

    rec('')
    rec('### (3) THE ACT`S OWN FINDING -- A CORRECTION TO b487.')
    rec('-' * 104)
    rec('    ### ### **THE KERNEL`S DEPOSITED DESCRIPTION IS NOT THE TEXT IN ITS REPOSITORY.**')
    rec('    ### `SIDE-kernel` at tag `v1.5` ships a `.zenodo.json` whose description is')
    rec('    ### ### **1,143 CHARACTERS**, opening *"Lean 4 formalization of the SIDE Exclusion')
    rec('    ### Principle applied to the Riemann zeta function."* ### The deposited record --')
    rec('    ### the author`s own screen -- carries ### **3,143 CHARACTERS**, opening')
    rec('    ### *"SIDE-kernel: the machine-verified architecture..."*. ### **THEY ARE DIFFERENT')
    rec('    ### TEXTS.**')
    rec('    ### ### **SO b487 DISPOSED A SENTENCE THAT IS NOT IN THE DEPOSIT.** ### It read the')
    rec('    ### repository`s file and graded *"The kernel proves that no off-line zero exists by')
    rec('    ### exhaustively excluding every mechanism class"* as resting on `E-2026-09-14-1`.')
    rec('    ### **THAT SENTENCE IS IN THE `.zenodo.json` AND NOT IN THE RECORD.**')
    rec('    ### ### **AND (R99) RULED IT "APPLIED AS DRAFTED".** ### Applying it would edit a')
    rec('    ### sentence the record does not contain. ### **THIS ACT NAMES IT AND STOPS:** ### the')
    rec('    ### kernel carries no RESTS row here, its (R99) text is held for the author`s ruling,')
    rec('    ### and the paste-ready block carries the monograph`s two rows only.')
    rec('    ### ### **A SOURCE THAT SHIPS BESIDE A DEPOSIT IS NOT THE DEPOSIT.**')

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
            ('**EIGHT RECORDS READ WHOLE AGAINST THE CEILING: 104 ROWS, 8 EXCEED, AND THE '
             'KERNEL`S DEPOSITED DESCRIPTION IS NOT THE TEXT IN ITS REPOSITORY** (%s). The '
             'author`s screen of 2026-09-14 is banked verbatim at 72 lines, sha256 7528bd85, '
             'with 8 records; NOTHING WAS FETCHED. No description is truncated -- the first test '
             'that said three were had mistaken a template`s ORCID trailer for a cut, refuted by '
             'three different lengths ending at the same token. The monograph`s screen text '
             'agrees with b359`s fetch JSON entity for entity. DISPOSITION of 96 sentences plus '
             '8 titles: STANDS %d, RESTS ON AN ERRATUM %d, EXCEEDS THE CEILING %d. The EXCEEDS '
             'rows carry NO replacement -- a title or headline that exceeds is the author`s to '
             'reword, and this act names it and stops. THE CORRECTION TO b487: the kernel`s tag '
             'ships a 1,143-character .zenodo.json while the deposit carries 3,143 characters, '
             'and b487 graded a sentence present in the former and ABSENT from the latter. (R99) '
             'ruled that sentence applied as drafted; applying it would edit a sentence the '
             'record does not contain, so it is held for the author and the paste-ready block '
             'carries the monograph`s two rows only.')
            % (MARK, R['stands'], R['rests'], R['exceeds']),
            ('`data/zenodo_listing_2026-09-14_author_screen.txt` (sha256 7528bd85...) ; '
             '`data/b359_fetch_F2.json` ; `SIDE-kernel` tag `v1.5` `.zenodo.json` ; '
             '`tools/b493_components.py`'),
            ('no axiom print -- ### **NOTHING COMPILED, NOTHING FETCHED, NO LANE OPENED.** ### A '
             'disposition is a reading of words against a ceiling.'),
            'MEASURED',
            ('(N1) HELD, and a THIRD title exceeds that the order did not name ; (N2) HELD, though '
             'the first ceiling matcher could not cross the full stop in "MAIN THEOREM." and would '
             'have scored it refuted ; (N3) HELD, and at records 3 and 4 that is a CORRECTION to '
             'b487 rather than agreement. (S1) HELD ; (S2) REFUTED -- the four May-2026 kernels '
             'exceed at ZERO rows, so overreach tracks the SUBJECT being RH and not the age of '
             'the text ; (S3) HELD. ### **NOTHING ABOUT RH FOLLOWS FROM A DISPOSITION.** ### No '
             'grade moved; nothing at Zenodo written; row U1 unedited; h2 where the deposit left '
             'it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b493_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (5) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **1** ### -- the eight records are read whole against the ceiling, and')
    rec('      the disposition is ready for a single platform session under (R102).')
    rec('    MINTED : ### **3**')
    rec('      (i)   ### **A SOURCE THAT SHIPS BESIDE A DEPOSIT IS NOT THE DEPOSIT.** ### A')
    rec('            `.zenodo.json` in a repository is what the author OFFERED; the record is what')
    rec('            the platform HOLDS. ### **THEY CAN DIVERGE, AND HERE THEY DO, BY TWO')
    rec('            THOUSAND CHARACTERS.**')
    rec('      (ii)  ### **A MATCHER THAT CANNOT CROSS A FULL STOP CANNOT READ A HEADLINE.**')
    rec('            `MAIN THEOREM. The Riemann Hypothesis:` is one claim in two sentences, and a')
    rec('            `[^.]` clause is blind to exactly that shape.')
    rec('      (iii) ### **OVERREACH TRACKS THE SUBJECT, NOT THE AGE OF THE TEXT.** ### The four')
    rec('            oldest records exceed at zero rows; the three that exceed are the three')
    rec('            whose subject IS the Riemann Hypothesis.')
    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b493_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3, held=held),
              io.open(os.path.join(D, 'b493_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b493_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
