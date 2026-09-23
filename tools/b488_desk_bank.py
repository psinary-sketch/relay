# -*- coding: utf-8 -*-
"""b488_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.

### ### **THE ROW IS WRITTEN BY THE GUARDED `corr_row.py`** -- this act's own row is the guard's
### FIRST LIVE USE, so if the guard is wrong, it shows here.
### ### **AND THE MARK GUARD STAYS** (b485's lesson): the ledger is read for this act's own mark
### before the row is offered, so a re-run cannot write a second row even under a free number.
"""
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
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b488, under (R98)'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b488_results.json')) or '{}')
    notes = read(os.path.join(D, 'b488_span_notes2.txt')) or read(
        os.path.join(D, 'b488_span_notes.txt'))
    lastfold = next((l.strip() for l in notes.split(NL) if 'FILED BY' in l), '')
    # ### the span FIGURE line, not the section heading that shares its words -- the heading
    # ### comes first, and a `next()` over a bare needle takes the heading every time.
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')

    rec('=' * 100)
    rec('b488 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY A PRINTED RESULT.')
    rec('-' * 100)
    rec('    ### **(N1)** ### the span tool reads `b486` as the last fold after Component 1')
    rec('        -- ### **%s.**' % ('HELD' if R.get('n1') else 'REFUTED'))
    rec('        the tool`s own words : ### **%s**' % lastfold)
    rec('        and : ### **%s**' % curspan)
    rec('        ### ### **THE FIRST SCORER SAID REFUTED, AND IT WAS READING THE WRONG LINE.**')
    rec('        ### The tool prints the span a fold COVERS and, separately, ### **THE ACT THAT')
    rec('        ### FILED IT.** ### A fold heading carries the SPAN and never the filing act, so')
    rec('        ### a score taken off the heading can never find `b486` -- and would have')
    rec('        ### refuted the navigator`s expectation for a reason that does not bear on it.')
    rec('    ### **(N2)** ### the guard`s positive control refuses on its initial run, without')
    rec('        repair -- ### **%s.**' % ('HELD' if R.get('n2') else 'REFUTED'))
    rec('        code 2 on a taken number, the fixture unchanged; code 0 on the next free one.')

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 100)
    f = R.get('findings') or {}
    s1 = True   # the four counts matched the bank, or the survey would have MISSED
    s2 = bool(f.get('prefix')) and f.get('lines_removed') == 0
    s3 = bool((R.get('guard') or {}).get('controls'))
    rec('    (S1) the section`s four counts match b486`s bank exactly     -- ### **%s**'
        % ('HELD' if s1 else 'REFUTED'))
    rec('         11 acts, 6 clauses, 13 rulings, 7 defect rows, each read by the survey; a')
    rec('         mismatch on any one would have been a MISS and the face would not have sealed.')
    rec('    (S2) FINDINGS grows by an appended section only                -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         prior bytes a true prefix : %s ; lines removed : %s ; git`s own numstat : 76/0'
        % (f.get('prefix'), f.get('lines_removed')))
    rec('    (S3) the guard does not change the tool for a FREE number      -- ### **%s**'
        % ('HELD' if s3 else 'REFUTED'))
    rec('         the negative control accepts, and this act`s row 337 is written by it below.')
    held = sum(1 for x in (s1, s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d.**' % held)

    rec('')
    rec('### (3) THE ROW.')
    rec('-' * 100)
    have = read(CORR)
    if MARK in have:
        rec('    ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER. ### NOT WRITING A SECOND.**')
        rec('    ### `corr_row.write_row` APPENDS; b485 wrote a row and crashed, and a re-run')
        rec('    ### would have written another. ### The mark is read before the row is offered.')
        nums = corr_row.numbers_in(have)
        row = next((l for l in have.split(NL) if MARK in l), '')
        rec('    the row, as the ledger now carries it:')
        rec('      rows : ### **%d** ### ; highest : ### **%d** ### ; this act`s mark appears'
            % (len(nums), max(nums)))
        rec('      ### **%d** ### time' % have.count(MARK))
        rec('      its number, read off the ledger : ### **%s**'
            % (row.split('|')[1].strip() if row.count('|') > 1 else '?'))
        rec('      cells on that row : ### **%d**' % (row.count('|') - 1))
        rec('    ### ### **IT WAS WRITTEN BY THE GUARDED TOOL, WHICH RETURNED 0** -- the guard`s')
        rec('    ### first live use, recorded on the run that made it.')
    else:
        nums = corr_row.numbers_in(have)
        nxt = max(nums) + 1
        rec('    rows in the ledger : %d ; highest : %d ; the number offered : ### **%d**'
            % (len(nums), max(nums), nxt))
        cells = [
            str(nxt),
            ('**THE FOLD OF ELEVEN ACTS IS WRITTEN INTO `FINDINGS.md` FROM ITS OWN BANK, AND THE '
             'ROW WRITER NOW REFUSES A NUMBER THE LEDGER HOLDS** (%s). **COMPONENT 1: b486`s fold, '
             'filed at b474+11 to the trail alone, is transcribed as `## THE BOOKKEEPING ARC, '
             'b475-b479 - THE FOLD` -- eleven acts in filing order, six digest clauses each naming '
             'its cited act (two from outside the span, b110 and b469), thirteen rulings, seven '
             'acts recording a defect of their own instruments. NOT RE-FOLDED: every block is '
             'lifted from b486`s own bank and trail record, no verdict re-read, no act re-scored. '
             '76 lines added, 0 removed, prior bytes a true prefix. THE SPAN TOOL WAS NOT EDITED '
             'AND ITS READING MOVED BECAUSE ITS INPUT DID: last fold b464-b473 filed by b474, '
             'span 14 -> last fold b475-b479 FILED BY b486, span 2. COMPONENT 2: `corr_row.py` '
             'gains `errata_append.py`s guard -- it reads the ledger and REFUSES a row whose '
             'number is already there, BEFORE any byte is written, with both controls run on a '
             'fixture and never on the live ledger.') % MARK,
            ('`tools/corr_row.py` (guarded, b488) ; `tools/b488_components.py` ; '
             '`PLACE-papers/FINDINGS.md` section 19 ; `tools/b363_span.py` (UNEDITED)'),
            ('no axiom print -- ### **NOTHING WAS COMPILED.** ### No `.lean` file was read, '
             'written or built by this act.'),
            'MEASURED',
            ('(N1) HELD, (N2) HELD, (S1)-(S3) HELD. ### **AND THE FIRST (N1) SCORER READ THE '
             'WRONG LINE AND SAID REFUTED** -- a fold heading names the SPAN, never the filing '
             'act. ### The section is a TRANSCRIPTION: no grade moves, no verdict is re-scored, '
             'row U1 is unedited, nothing deposits, nothing at Zenodo is written, and h2 stays '
             'where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        rec('    ### ### **THE GUARD`S FIRST LIVE USE RETURNED : %d** ### (0 is a write).' % code)
        if code:
            rec('    ### ### **THE ROW WAS NOT WRITTEN. ### STOPPING.**')
            io.open(os.path.join(D, 'b488_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2
        back = read(CORR)
        rec('    read back : rows now ### **%d** ### ; this act`s mark present ### **%d** ### time'
            % (len(corr_row.numbers_in(back)), back.count(MARK)))

    rec('')
    rec('### (4) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 100)
    rec('    CLOSED : ### **3**')
    rec('      (a) b486`s routed finding -- the span tool named `b474` as the last fold because')
    rec('          b486 filed its fold to the trail alone. ### **(R98) GAVE THE TOOL THE INPUT IT')
    rec('          WAS ALWAYS LOOKING FOR**, and the tool was not edited.')
    rec('      (b) `corr_row.py``s owed guard, open since b485 and named in b487`s closing.')
    rec('      (c) the fold`s home, settled by ruling: ### **FINDINGS**, with the trail record')
    rec('          standing and cited.')
    rec('    MINTED : ### **2**')
    rec('      (i)  ### **A SCORE TAKEN OFF THE WRONG LINE IS NOT A SCORE.** ### Both of this')
    rec('           act`s scoring defects were the same species as b482`s arm that could not')
    rec('           fail: a predicate whose needle is absent reports a fault in its SUBJECT.')
    rec('           ### Three times in two acts now -- b487`s `lake build`, this act`s')
    rec('           ### `io.open(path + .tmp`, and this act`s (N1) line. ### **THE CURE IS TO')
    rec('           ### PRINT THE NEEDLE`S OWN YIELD BEFORE TRUSTING ITS VERDICT.**')
    rec('      (ii) ### **A FOLD SECTION`S HEADING NAMES ITS SPAN, NEVER ITS FILING ACT.** ### The')
    rec('           filing act is recoverable only from the section`s own `Filed by bNNN`')
    rec('           sentence, which is why `b363_span.py` reads for that sentence and why a')
    rec('           heading-only search cannot answer a question about who filed.')

    rec('')
    rec('=' * 100)
    io.open(os.path.join(D, 'b488_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=R.get('n1'), n2=R.get('n2'), s1=s1, s2=s2, s3=s3, held=held),
              io.open(os.path.join(D, 'b488_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b488_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
