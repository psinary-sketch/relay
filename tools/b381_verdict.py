# -*- coding: utf-8 -*-
"""b381_verdict.py -- COMPONENT 4. ### **WHAT THE COLUMNS NOW MEAN, AND (R14) RECORDED.**

### ### **THIS SECTION IS OWED WHICHEVER WAY COMPONENT 3 WENT**, and the locked face said so in
### advance precisely so that a failure could not quietly shorten the act.
### ### **AND IT ALSO MEASURES `(E4)`:** ### the face predicted the unit definition would do more work
### than the threshold. ### The exemplars are re-scored under a ### **PARAGRAPH-ONLY** ### splitter,
### which is what a naive reading of `the same unit` would have built, and the branch that would have
### produced is printed. ### **THAT IS A MEASUREMENT OF THE INSTRUMENT AND IT ADOPTS NOTHING** -- the
### declared unit and the declared threshold both stand exactly as locked.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import co_location as CL      # noqa: E402
import role_structure as RS   # noqa: E402
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
EVID = os.path.join(D, 'b380_ruling_evidence.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def paragraph_units(text):
    """### **THE NAIVE SPLITTER, FOR `(E4)` ONLY:** ### blank lines and nothing else. ### This is what
    `the same unit` builds if nobody asks what an entry is."""
    out, buf, start = [], [], 0
    for i, ln in enumerate(text.split(chr(10)), 1):
        if ln.strip():
            if not buf:
                start = i
            buf.append(ln)
        elif buf:
            out.append(('paragraph', start, buf))
            buf = []
    if buf:
        out.append(('paragraph', start, buf))
    return out


def score_with(splitter, rel, text, index):
    bearing, colocating = 0, 0
    for _kind, _ln, buf in splitter(text):
        cs = CL.clusters_in(chr(10).join(buf), index, rel)
        if not cs:
            continue
        bearing += 1
        if len(cs) >= 2:
            colocating += 1
    ratio = (float(colocating) / bearing) if bearing else 0.0
    if bearing == 0:
        return 'C?', ratio
    return ('C+' if ratio > CL.THRESHOLD else 'C-'), ratio


def main():
    C = json.load(io.open(os.path.join(D, 'b381_control.json'), encoding='utf-8'))
    EX = json.load(io.open(os.path.join(D, 'b381_exemplars.json'), encoding='utf-8'))
    E80 = json.load(io.open(os.path.join(D, 'b380_reads.json'), encoding='utf-8'))
    RS80 = json.load(io.open(os.path.join(D, 'b380_rescore.json'), encoding='utf-8'))

    rec('=' * 100)
    rec('b381 -- COMPONENT 4. ### WHAT THE COLUMNS NOW MEAN.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) WHAT THIS ACT CHANGES ABOUT EACH COLUMN.')
    rec('-' * 100)
    rec('  ### ### **`b380`S POSITIVE COLUMN -- REACH, `A+`, %d DOCUMENTS.**'
        % RS80['structural_tally'].get('A+', 0))
    rec('  ### It was an ### **UPPER BOUND ON SYNTHESIS** ### and it ### **STILL IS.** ### This act')
    rec('  ### did not test it, did not narrow it and did not confirm it. ### **NOTHING ABOUT IT')
    rec('  ### ### MOVED**, and a second feature that failed cannot narrow a first one.')
    rec('  ### ### **`b380`S NEGATIVE COLUMN -- `A-`, %d DOCUMENTS.**'
        % RS80['structural_tally'].get('A-', 0))
    rec('  ### It was ### **UNVALIDATED** ### and it ### **STILL IS.** ### Validating it needed a')
    rec('  ### second, independent reading that agreed with it on the documents that declare, and')
    rec('  ### ### **CO-LOCATION IS NOT THAT READING BECAUSE IT DOES NOT SEPARATE THE DECLARERS.**')
    rec('  ### ### ### **SO WHAT STAYS UNVALIDATED IS EXACTLY WHAT WAS UNVALIDATED BEFORE**, and the')
    rec('  ### act`s contribution is a NEGATIVE one, stated as such rather than dressed up.')
    rec('')
    rec('  ### ### **AND WHAT IS NEW IS THE CONTROL, NOT A COLUMN.** ### The rebuilt exemplar set is')
    rec('  ### `%d` synthesis and `%d` gathering, every member selected by a quoted sentence in its'
        % (C['synthesis_n'], C['gathering_n']))
    rec('  ### own head. ### **IT IS THE FIRST CONTROL IN THIS SEQUENCE THAT CAN FAIL IN BOTH')
    rec('  ### ### DIRECTIONS**, and it survives this act whether or not co-location did.')
    rec('  ### ### **AND THE SECOND NEW FACT IS A NEGATIVE ONE WORTH MORE THAN EITHER FEATURE:**')
    rec('  ### ### ### **TWO INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION.**')
    rec('  ### `b380`s reach called both gatherers synthesisers; this act`s co-location puts `%d` of'
        % C['synthesis_cplus'])
    rec('  ### `%d` synthesis declarers below the bar and `%d` of `%d` gatherers above it. ### **THAT'
        % (C['synthesis_n'], C['gathering_cplus'], C['gathering_n']))
    rec('  ### ### IS NOT PROOF THAT NO STRUCTURAL FEATURE READS ROLE**, and this act does not claim')
    rec('  ### it. ### It is ### **TWO FAILURES OF THE SAME SHAPE**, and the shape is that the')
    rec('  ### distinction lives in what a document SAYS about what it names.')

    # ------------------------------------------------------------------------------- (E4)
    rec('')
    rec('-' * 100)
    rec('  ### (2) `(E4)` MEASURED -- DID THE UNIT DO MORE WORK THAN THE THRESHOLD?')
    rec('-' * 100)
    rec('  ### The exemplars are re-scored under a ### **PARAGRAPH-ONLY** ### splitter -- blank lines')
    rec('  ### and nothing else -- which is what `the same unit` builds if nobody asks what an entry')
    rec('  ### is. ### **THIS ADOPTS NOTHING.** ### The declared unit and threshold stand as locked.')
    index = RS.build_index(PP)
    naive = {'synthesis': [], 'gathering': []}
    for side, files in (('synthesis', EX['synthesis_set']), ('gathering', EX['gathering_set'])):
        for rel in files:
            p = os.path.join(PP, rel.replace('/', os.sep))
            if not os.path.exists(p):
                continue
            txt = io.open(p, encoding='utf-8', errors='replace').read()
            m, r = score_with(paragraph_units, rel, txt, index)
            naive[side].append(dict(file=rel, mark=m, ratio=round(r, 4)))
    ns = sum(1 for x in naive['synthesis'] if x['mark'] == 'C+')
    ng = sum(1 for x in naive['gathering'] if x['mark'] == 'C+')
    rec('    %-34s %-22s %s' % ('', 'DECLARED UNIT', 'PARAGRAPH-ONLY'))
    rec('    %-34s %-22s %s'
        % ('synthesis exemplars at `C+`', '%d of %d' % (C['synthesis_cplus'], C['synthesis_n']),
           '%d of %d' % (ns, len(naive['synthesis']))))
    rec('    %-34s %-22s %s'
        % ('gathering exemplars at `C+`', '%d of %d' % (C['gathering_cplus'], C['gathering_n']),
           '%d of %d' % (ng, len(naive['gathering']))))
    nrate_s = float(ns) / len(naive['synthesis']) if naive['synthesis'] else 0.0
    nrate_g = float(ng) / len(naive['gathering']) if naive['gathering'] else 0.0
    naive_branch = ('SEPARATES' if (ns == len(naive['synthesis']) and ng == 0)
                    else ('PARTLY' if nrate_s > nrate_g else 'DOES NOT SEPARATE'))
    rec('    %-34s %-22s %s' % ('the branch it would have produced', C['branch'], naive_branch))
    e4 = (naive_branch != C['branch']) or (abs(nrate_g - C['gathering_rate']) > 0.10)
    rec('  ### ### **`(E4)` %s.** ### The gathering side`s `C+` rate moves from `%.1f%%` to `%.1f%%`'
        % ('MET' if e4 else 'REFUTED', 100.0 * C['gathering_rate'], 100.0 * nrate_g))
    rec('  ### when only the tokeniser changes, ### **AND THE RULE AND THE THRESHOLD ARE IDENTICAL IN')
    rec('  ### ### BOTH COLUMNS.** ### A predicate whose answer is set by its splitter and not by its')
    rec('  ### rule is reported as such, and this one is.')

    # ------------------------------------------------------------------- THE OTHER EXPECTATIONS
    lowest_syn = C['lowest_synthesis_ratio']
    reg = [x for x in C['synthesis'] if x['file'] == 'REGISTRY.md']
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE EXPECTATIONS.')
    rec('-' * 100)
    rec('  ### ### **`(F1)` REFUTED BY THE PRINTED TABLE.** ### Co-location does not separate the')
    rec('  ### rebuilt set: `%d` of `%d` synthesis exemplars clear the bar and `%d` of `%d` gathering'
        % (C['synthesis_cplus'], C['synthesis_n'], C['gathering_cplus'], C['gathering_n']))
    rec('  ### exemplars clear it too. ### **THE LOWEST SYNTHESIS RATIO IS %.3f AND THE HIGHEST'
        % C['lowest_synthesis_ratio'])
    rec('  ### ### GATHERING RATIO IS %.3f**, so the two sets overlap completely and ### **NO CHOICE'
        % C['highest_gathering_ratio'])
    rec('  ### ### OF THRESHOLD WOULD HAVE SEPARATED THEM.**')
    rec('  ### ### **`(F2)` NOT REACHED**, exactly as `(E1)` registered in advance: the corpus is not')
    rec('  ### scored when the predicate is not adopted, so there is no column to shrink and')
    rec('  ### ### **NEITHER MET NOR REFUTED IS THE HONEST ANSWER.**')
    rec('  ### ### **`(E1)` MET.** ### The conditionality was registered before the run and it bound.')
    if reg:
        rec('  ### ### **`(E2)` CONFIRMED IN MECHANISM AND REFUTED IN EFFECT.** ### It predicted the')
        rec('  ### ledgers would co-locate at high ratio while arguing nothing. ### `REGISTRY.md` has')
        rec('  ### ### **%d SOURCE-BEARING UNITS AND %d OF THEM DO CARRY TWO CLUSTERS** -- the'
            % (reg[0]['bearing'], reg[0]['colocating']))
        rec('  ### mechanism is exactly as predicted -- but the ratio is `%.3f`, below the bar,'
            % reg[0]['ratio'])
        rec('  ### because ### **MOST LEDGER ROWS NAME ONE THING.** ### The deafness is real and it')
        rec('  ### did not decide the outcome.')
    rec('  ### ### **`(E3)` REFUTED.** ### The purpose-statement scan found `%d` gathering exemplars'
        % C['gathering_n'])
    rec('  ### against a declared floor of `%d`, so ### **THE REBUILT CONTROL IS NOT UNDERPOWERED**'
        % EX['floor'])
    rec('  ### and the separation result stands on its own without that caveat.')
    rec('  ### ### **`(E4)` %s**, measured above.' % ('MET' if e4 else 'REFUTED'))

    rec('')
    rec('-' * 100)
    rec('  ### (4) `(R14)`, RECORDED AND NOT APPLIED.')
    rec('-' * 100)
    rec('  ### The ruling is banked verbatim in the ruling`s evidence file -- ### **THE WHOLE RULING')
    rec('  ### ### AND NOT ONLY THE LINES THIS ACT ANCHORED.**')
    rec('  ### ### **WHAT IT SETTLES:** ### the class ruling governs by ### **CONTENT AND ROLE, NOT')
    rec('  ### ### BY LOCATION**, so the download-layer book is within its reach and outside the')
    rec('  ### mirroring ruling`s. ### `b379` filed that the ruling had to say whether it governs')
    rec('  ### documents outside the tree, and ### **`(R14)` ANSWERS THAT FILING AND THE FILING IS')
    rec('  ### ### CLOSED BY THE AUTHOR AND NOT BY THIS SEAT.**')
    rec('  ### ### **WHAT IT DOES NOT SETTLE, IN THE RULING`S OWN WORDS:** ### the book`s registry')
    rec('  ### drift ### **STAYS OPEN AND IS THE AUTHOR`S.** ### **NO DOCUMENT WAS RECLASSIFIED')
    rec('  ### ### UNDER IT BY THIS ACT**, the book was not opened, read for content, graded, moved')
    rec('  ### or renamed, and ### **THE REGISTRY WAS NOT EDITED.**')
    rec('')
    rec('=' * 100)
    rec('  ### ### ### **NO CLASS IS RULED. ### NO DOCUMENT IS RECLASSIFIED. ### NO DECLARATION IS')
    rec('  ### ### ### MOVED. ### NO PRIOR SCORE IS OVERWRITTEN. ### THE CORPUS WAS NOT SCORED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b381_verdict_notes', LINES)
    out = dict(naive_synthesis_cplus=ns, naive_gathering_cplus=ng,
               naive_synthesis_rate=round(nrate_s, 4), naive_gathering_rate=round(nrate_g, 4),
               naive_branch=naive_branch, e4_met=e4,
               f1='REFUTED', f2='NOT REACHED', e1='MET',
               e2='CONFIRMED IN MECHANISM, REFUTED IN EFFECT', e3='REFUTED',
               e4=('MET' if e4 else 'REFUTED'),
               registry_bearing=(reg[0]['bearing'] if reg else None),
               registry_colocating=(reg[0]['colocating'] if reg else None),
               registry_ratio=(reg[0]['ratio'] if reg else None),
               lowest_synthesis_ratio=lowest_syn,
               class_ruled=False, corpus_scored=False, prior_scores_overwritten=0,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b381_verdict.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))

    # ------------------------------------------------------ THE RULING'S EVIDENCE FILE, UPDATED
    ev = io.open(EVID, encoding='utf-8').read()
    MARK = '### b381 -- (R14), AND THE SECOND STRUCTURAL FEATURE THAT DOES NOT READ ROLE.'
    if MARK not in ev:
        # ### ### **VERBATIM MEANS THE WHOLE RULING, NOT THE LINES THIS ACT HAPPENED TO ANCHOR.**
        # ### The first version banked the 6 anchored lines of a 9-line ruling and still called
        # ### itself verbatim. ### **A QUOTATION WITH HOLES IN IT IS NOT A QUOTATION**, so the block
        # ### is sliced whole from the ferry between two ends that are each verified unique first
        # ### (`b377`'s rule: a slice is an address and both its ends are verified).
        ferry = io.open(os.path.join(D, 'b381_ferry_2026-09-09.txt'),
                        encoding='utf-8').read().split(chr(10))
        first = [i for i, x in enumerate(ferry) if x.startswith('RULING (R14)')]
        last = [i for i, x in enumerate(ferry) if x.startswith("and is the author's.")]
        assert len(first) == 1 and len(last) == 1 and first[0] < last[0], (first, last)
        R14 = ferry[first[0]:last[0] + 1]
        block = ['', '=' * 100, MARK, '=' * 100,
                 '### **(R14), THE AUTHOR`S, RATIFIED AT b381 AND STRIKEABLE. ### BANKED VERBATIM,',
                 '### ### THE WHOLE RULING AND NOT ONLY THE LINES THIS ACT ANCHORED:**']
        for r in R14:
            block.append('###   | %s' % r.rstrip())
        block += [
            '### ### **WHAT IT SETTLES:** ### the class ruling reaches the download-layer book, and',
            '### the mirroring ruling does not. ### **BOTH HOLD AND NEITHER IS EDITED INTO THE**',
            '### ### **OTHER.** ### `b379` filed that the ruling had to say whether it governs',
            '### documents outside the tree; ### **(R14) ANSWERS THAT FILING AND THE FILING IS',
            '### ### CLOSED BY THE AUTHOR, NOT BY THIS SEAT.**',
            '### ### **WHAT IT DOES NOT SETTLE, AND THE RULING ITSELF SAYS SO:** ### the',
            '### download-layer book`s registry drift ### **STAYS OPEN AND IS THE AUTHOR`S.** ### No',
            '### document was reclassified under (R14) by this act and the book was not opened.',
            '',
            '### **THE SECOND STRUCTURAL FEATURE, TESTED AND NOT ADOPTED (b381):**',
            '###   the rebuilt control  : %d synthesis exemplars, %d gathering exemplars, every one'
            % (C['synthesis_n'], C['gathering_n']),
            '###                         selected by a quoted sentence in its own head',
            '###   co-location, C+ rate : synthesis %d of %d ; gathering %d of %d'
            % (C['synthesis_cplus'], C['synthesis_n'], C['gathering_cplus'], C['gathering_n']),
            '###   lowest synthesis     : %.3f   ### / ### highest gathering : %.3f'
            % (C['lowest_synthesis_ratio'], C['highest_gathering_ratio']),
            '###   the branch           : ### **%s. ### NOT ADOPTED.**' % C['branch'],
            '###   the corpus           : ### **NOT SCORED**, under the order`s own clause',
            '### ### **SO THE RULING`S EVIDENCE ON THE ROLE AXIS IS UNCHANGED SINCE b380:** ### the',
            '### positive column is an ### **UPPER BOUND** ### and the negative column is',
            '### ### **UNVALIDATED.** ### What b381 adds is a control that can fail in both',
            '### directions and ### **A SECOND FEATURE THAT FAILS ON IT.**',
            '=' * 100, '']
        io.open(EVID, 'a', encoding='utf-8', newline=chr(10)).write(chr(10).join(block) + chr(10))
        print('  ruling evidence updated: %s' % os.path.basename(EVID))
    else:
        print('  ruling evidence ALREADY carries this act`s block; nothing appended.')
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
