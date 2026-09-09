# -*- coding: utf-8 -*-
"""b380_verdict.py -- COMPONENT 4: ### **THE VERDICT ON THE METHOD, NOT ON THE CLASS.**

### One of three, chosen by the printed tables and not by preference:
###   ### **ROLE IS STRUCTURALLY READABLE** ### -- the column moved, the quadrant populated.
###   ### **ROLE IS NOT READABLE** ### -- the column did not move, and role must be DECLARED.
###   ### **PARTLY** ### -- the reach stated, with which populations it reads and which it cannot.
### ### ### **NO CLASS IS RULED IN ANY BRANCH.** ### A method that works is not a ruling either.

### ### **AND THIS FILE ALSO WRITES THE CONSOLIDATED RULING-EVIDENCE FILE** the closing asks for.
### ### **NO SUCH FILE EXISTED**; the evidence was spread across four banks. ### It is written
### ### **IN THE RELAY BANK AND NOT AS A NEW TRACKING DOCUMENT IN THE CORPUS**, which every act since
### `b375` has been forbidden to create and this one creates none either.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
EVID = os.path.join(D, 'b380_ruling_evidence.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


def main():
    RS = J('b380_rescore')
    B9 = J('b379_rescore')
    AX = J('b376_axes')
    TS = J('b376_tests')
    EV7 = J('b377_evidence')

    rec('=' * 100)
    rec('b380 -- COMPONENT 4: ### **THE VERDICT ON THE METHOD, NOT ON THE CLASS.**')
    rec('=' * 100)
    rec('')

    # ------------------------------------------------------------------------- THE THREE READINGS
    moved = RS['moved_out_of_nd']
    nd = RS['not_determinable']
    frac = 100.0 * moved / max(1, nd)
    ag7 = RS['agreement_over_seven']
    ag9 = RS['agreement_over_all']
    ndecl = RS['declarers']
    quad = RS['both_axes_structural']
    dis = RS['disagreements']
    ts = RS['structural_tally']

    rec('-' * 100)
    rec('  ### WHAT THE TABLES SAY, BEFORE THE BRANCH IS CHOSEN.')
    rec('-' * 100)
    rec('    documents moved out of `NOT DETERMINABLE` : ### **%d of %d (%.1f%%)**' % (moved, nd, frac))
    rec('    the corrected role distribution           : ### **%s**' % ts)
    rec('    the both-axes quadrant                    : ### **%d** ### (was %d)'
        % (quad, RS['both_axes_statement']))
    rec('    agreement on the seven that declare synthesis : ### **%d of 7**' % ag7)
    rec('    ### **AGREEMENT ON ALL %d DECLARERS            : %d -- AND THE TWO IT MISSES ARE BOTH**'
        % (ndecl, ag9))
    rec('    ### **THE GATHERERS.**')
    for x in dis:
        rec('      ### `%s` ### -- the document says `%s`, the predicate says `%s`, reach %d'
            % (x['file'], x['statement'], x['structural'], x['evidence']['reach']))

    # ------------------------------------------------------------------------------ THE BRANCH
    rec('')
    rec('-' * 100)
    rec('  ### THE BRANCH, CHOSEN BY THE TABLES.')
    rec('-' * 100)
    column_moved = moved > nd / 2.0
    control_clean = (ag9 == ndecl)
    if column_moved and control_clean:
        branch = 'ROLE IS STRUCTURALLY READABLE'
    elif not column_moved:
        branch = 'ROLE IS NOT READABLE'
    else:
        branch = 'PARTLY'
    rec('    the column moved      : %s (%d of %d)' % (column_moved, moved, nd))
    rec('    the control is clean  : %s (%d of %d declarers)' % (control_clean, ag9, ndecl))
    rec('')
    rec('    ### ### ### **THE VERDICT : %s.**' % branch)
    rec('')
    if branch == 'PARTLY':
        rec('    ### **WHY NOT `STRUCTURALLY READABLE`, THOUGH THE COLUMN MOVED AND THE QUADRANT')
        rec('    ### ### POPULATED:** ### the predicate`s own control refuses it. ### It agrees with')
        rec('    ### every document that declares SYNTHESIS and with ### **NEITHER OF THE TWO THAT')
        rec('    ### ### DECLARE GATHERING.** ### Both gatherers reach widely -- one names %d kernels'
            % max(len(x['evidence']['kernels']) for x in dis))
        rec('    ### and the other %d -- and the predicate reads reach and calls it synthesis.'
            % min(len(x['evidence']['kernels']) for x in dis))
        rec('    ### ### ### **THAT IS THE DEAFNESS THIS ACT`S LOCKED FACE NAMED BEFORE THE RUN:**')
        rec('    ### ### ### `A DOCUMENT THAT CITES WIDELY AND SYNTHESISES NOTHING` ### and')
        rec('    ### ### ### `REACH IS NOT ARGUMENT`. ### **IT WAS NAMED AS A LIMIT AND IT ARRIVED AS')
        rec('    ### ### ### A MEASURED FAILURE ON THE ONLY GROUND TRUTH AVAILABLE.**')
        rec('')
        rec('    ### **WHAT THE PREDICATE READS, STATED AS A REACH AND NOT AS A SCORE:**')
        rec('    ###   ### **IT READS PRESENCE OF REACH RELIABLY.** ### %d of %d documents draw on'
            % (ts.get('A+', 0) + ts.get('A-', 0), RS['population']))
        rec('    ###     something this predicate can see, and it finds them. ### That is what moved')
        rec('    ###     `%d` documents out of `NOT DETERMINABLE`.' % moved)
        rec('    ###   ### **IT DOES NOT READ THE DISTINCTION THE RUBRIC IS ABOUT.** ### The rubric')
        rec('    ###     separates SYNTHESIS from GATHERING; ### **ON THE ONLY TWO DOCUMENTS WHERE THE')
        rec('    ###     ### CORPUS STATES THAT DISTINCTION, THE PREDICATE GETS BOTH WRONG.**')
        rec('    ###   ### **SO THE `A-` COLUMN IT PRODUCES IS NOT MEASURING GATHERING.** ### It is')
        rec('    ###     measuring ### **NARROW REACH**, which is a different thing that happens to')
        rec('    ###     share a name. ### `%d` documents carry it and none of them is validated.'
            % ts.get('A-', 0))
        rec('    ###   ### **AND THE `A+` COLUMN IS AN UPPER BOUND ON SYNTHESIS, NOT A COUNT OF IT.**')
        rec('    ###     `%d` documents reach widely; ### **HOW MANY OF THEM ARGUE ACROSS WHAT THEY'
            % ts.get('A+', 0))
        rec('    ###     ### REACH IS NOT MEASURED HERE AND THIS ACT DOES NOT ESTIMATE IT.**')
        rec('')
        rec('    ### **WHICH POPULATIONS IT READS, AND WHICH IT CANNOT:**')
        rec('    ###   ### **READS:** ### documents that cite -- by path, by backticked name, or by')
        rec('    ###     naming a kernel. ### That is most of the corpus.')
        rec('    ###   ### **CANNOT READ:** ### a document that synthesises in prose without citing')
        rec('    ###     (invisible, scored `A?`); a document that cites widely and argues nothing')
        rec('    ###     (scored `A+` wrongly, and the control proves it); and any subject boundary')
        rec('    ###     that is not a directory boundary, because ### **THE DIRECTORY STANDS IN FOR')
        rec('    ###     ### THE SUBJECT** ### and that is an address doing a subject`s work.')
        rec('')
        rec('    ### **WHAT WOULD SEPARATE THE TWO, NAMED AND NOT ATTEMPTED:** ### a document that')
        rec('    ### synthesises makes a claim ### **ABOUT THE RELATION BETWEEN** ### the things it')
        rec('    ### draws on; a document that gathers puts them side by side. ### **THAT IS A')
        rec('    ### ### DISTINCTION IN THE SENTENCES, NOT IN THE CITATION GRAPH**, and no structural')
        rec('    ### predicate over what a document draws on can reach it.')
    rec('')
    rec('    ### ### ### **AND NO CLASS IS RULED IN THIS BRANCH OR IN ANY OTHER.** ### The verdict is')
    rec('    ### ### ### about whether a method works. ### **A METHOD THAT PARTLY WORKS IS NOT A')
    rec('    ### ### ### RULING EITHER.**')

    # ------------------------------------------------- WHAT THE 'NOT READABLE' BRANCH WOULD OBLIGE
    rec('')
    rec('-' * 100)
    rec('  ### AND WHAT THE SECOND BRANCH WOULD HAVE OBLIGED, STATED BECAUSE THE ORDER ASKS.')
    rec('-' * 100)
    rec('    ### The order says: if role is not readable, ### **THE FINDING IS THAT ROLE MUST BE')
    rec('    ### ### DECLARED, WHICH MAKES THE RULING A DECLARATION RULE RATHER THAN A')
    rec('    ### ### CLASSIFICATION.**')
    rec('    ### **THIS ACT DID NOT REACH THAT BRANCH** -- the column moved. ### But the control`s')
    rec('    ### failure means ### **THE PART OF THE ROLE AXIS THE RUBRIC IS ACTUALLY ABOUT IS STILL')
    rec('    ### ### NOT READABLE**, so what that branch would oblige is stated anyway:')
    rec('    ###   every document would carry a declared role line, as `%d` already do;' % ndecl)
    rec('    ###   the `%d` that declare none would each need one written, which is a judgement per'
        % RS['statement_tally'].get('A?', 0))
    rec('    ###     document and not a sweep;')
    rec('    ###   and the class would become ### **A RULE ABOUT WHAT A DOCUMENT MUST SAY**, not a')
    rec('    ###     test a checker can apply to a document that says nothing.')
    rec('    ### ### **IT IS NOT RECOMMENDED, AND NO BRANCH ABOVE IS PREFERRED OVER ANOTHER.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b380_verdict_notes', LINES)
    io.open(os.path.join(D, 'b380_verdict.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(branch=branch, column_moved=column_moved, control_clean=control_clean,
                        moved=moved, not_determinable=nd, fraction=frac,
                        agreement_over_seven=ag7, agreement_over_all=ag9, declarers=ndecl,
                        both_axes=quad, disagreements=len(dis), class_ruled=False,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))

    # -------------------------------------------------------- THE CONSOLIDATED RULING-EVIDENCE FILE
    E = []
    B = '=' * 100
    S = '-' * 100
    E.append(B)
    E.append('THE CLASS RULING -- THE EVIDENCE, CONSOLIDATED. ### **AS OF b380, 2026-09-08.**')
    E.append(B)
    E.append('### ### **THIS FILE CONSOLIDATES EVIDENCE FOUR ACTS PRODUCED. ### IT MAKES NO RULING.**')
    E.append('### It is a ### **RELAY BANK ARTIFACT** ### and ### **NOT A TRACKING DOCUMENT IN THE')
    E.append('### ### CORPUS**, which no act since `b375` has been permitted to create.')
    E.append('### ### **THE RULING IS THE AUTHOR`S AND NOTHING BELOW RECOMMENDS ONE.**')
    E.append('')
    E.append(S)
    E.append('### (1) THE QUESTION.')
    E.append(S)
    E.append('### ### **WHAT DOES `KEYSTONE` NAME?** ### `b375` found the corpus carries THREE tests')
    E.append('### for the word and they select overlapping but different documents. ### `b376` found')
    E.append('### that ### **ALL THREE CROSS TWO INDEPENDENT AXES** ### and none equals either:')
    E.append('###   ### **AXIS A -- ROLE** ### : *synthesizes a cluster against other available')
    E.append('###     content* versus *gathers a subject`s research at a point in time*.')
    E.append('###   ### **AXIS B -- APPARATUS** ### : carries a correspondence table naming kernel,')
    E.append('###     terminal, pin and grade that a stranger can traverse, or does not.')
    E.append('### ### ### **THE THREE TESTS DO NOT DISAGREE BECAUSE ONE IS WRONG. ### EACH ASKS BOTH')
    E.append('### ### ### QUESTIONS AT ONCE AND WEIGHTS THEM DIFFERENTLY.**')
    E.append('')
    E.append(S)
    E.append('### (2) THE AUTHOR`S OWN ROLE CLAUSE, BANKED AT b377 AS EVIDENCE.')
    E.append(S)
    E.append('###   `Keystones are for clarifying results and as well as for exploring ramifications')
    E.append('###   and insights`')
    E.append('###   `the keystones should cover any and all pertinent or interesting materials, not')
    E.append('###   just having tunnel vision in explanatory clarity just because we have been')
    E.append('###   relentlessly focused on a particular problem at a particular research phase`')
    E.append('### ### **IT SPEAKS TO THE ROLE AXIS AND NOT THE APPARATUS AXIS**, and a clause that')
    E.append('### bears on one axis does not rule a question that spans two.')
    E.append('')
    E.append(S)
    E.append('### (3) THE APPARATUS AXIS, AS IT NOW STANDS.')
    E.append(S)
    E.append('### `b376` scored it with a predicate requiring a DOTTED terminal. ### `b378` found')
    E.append('### ### **NOT ONE CITING DOCUMENT USES THE DOTTED CONVENTION ALONE.** ### `b379`')
    E.append('### re-scored it with a both-dialect matcher, the direction registered first.')
    E.append('###   ### **`B+` : %d, was %d. ### NONE LOST.**' % (B9['corrected_bplus'],
                                                                  B9['prior_bplus']))
    E.append('###   and every document that moved came out of a row where the role axis said `A?`.')
    E.append('### ### **THE APPARATUS COLUMN IS THE ONE THE CORPUS ANSWERS.**')
    E.append('')
    E.append(S)
    E.append('### (4) THE ROLE AXIS, AS IT NOW STANDS -- AND THIS IS WHERE THE EVIDENCE IS THIN.')
    E.append(S)
    E.append('### **SCORED FROM WHAT DOCUMENTS SAY ABOUT THEMSELVES** (`b376`):')
    E.append('###   ### **%s** ### -- ### **%.1f%% SAY NOTHING.**'
             % (RS['statement_tally'], 100.0 * RS['not_determinable'] / RS['population']))
    E.append('### **SCORED FROM WHAT DOCUMENTS DRAW ON** (`b380`):')
    E.append('###   ### **%s** ### -- `%d` moved out of `NOT DETERMINABLE`.' % (ts, moved))
    E.append('### ### ### **BUT THE STRUCTURAL SCORE FAILS ITS OWN CONTROL ON THE DISTINCTION THE')
    E.append('### ### ### RUBRIC IS ABOUT.** ### It agrees with all %d documents that declare' % ag7)
    E.append('### ### ### SYNTHESIS and with ### **NEITHER OF THE TWO THAT DECLARE GATHERING.**')
    E.append('### ### **SO THE `A+` COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE `A-` COLUMN IS NOT')
    E.append('### ### MEASURING GATHERING AT ALL.**')
    E.append('')
    E.append(S)
    E.append('### (5) THE QUADRANTS, ON BOTH ROLE SCORES, OVER THE CORRECTED APPARATUS COLUMN.')
    E.append(S)
    E.append('###   %-8s %-16s %s' % ('cell', 'statement-role', 'structural-role'))
    for c in ('A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?'):
        E.append('###   %-8s %-16d %d' % (c, RS['quadrants_statement'].get(c, 0),
                                          RS['quadrants_structural'].get(c, 0)))
    E.append('### ### **THE BOTH-AXES QUADRANT IS NON-EMPTY FOR THE FIRST TIME : %d** -- and ### **%d'
             % (quad, RS['both_axes_already_declared']))
    E.append('### ### OF THOSE SAID SO THEMSELVES; THE REST ARE THERE BECAUSE A PREDICATE THAT FAILS')
    E.append('### ### ITS OWN CONTROL PUT THEM THERE.**')
    E.append('')
    E.append(S)
    E.append('### (6) THE OPTIONS, AS b376 STATED THEM AND b379 RE-PRICED THEM. ### **NONE IS')
    E.append('### RECOMMENDED.**')
    E.append(S)
    for o in EV7['options']:
        E.append('### **%s** ### -- `b376_the_two_axis_read.txt` lines %d-%d'
                 % (o['name'], o['start'], o['end']))
    E.append('### ### **`b379` RE-PRICED THEM:** ### option 1`s cost restated (`%d` not `%d`); option'
             % (B9['corrected_bplus'], B9['prior_bplus']))
    E.append('### 3`s strictness argument weakened; options 2 and 5 untouched; option 4 strengthened')
    E.append('### only in that the axes came apart further.')
    E.append('### ### **AND `b380` ADDS ONE FACT THAT BEARS ON ALL OF THEM:** ### the role axis can be')
    E.append('### moved by reading structure, but ### **THE MOVEMENT DOES NOT MEASURE THE RUBRIC`S OWN')
    E.append('### ### DISTINCTION**, so an option resting on axis A rests on a column whose `A-` half')
    E.append('### is unvalidated.')
    E.append('')
    E.append(S)
    E.append('### (7) WHAT THE EVIDENCE STILL DOES NOT SETTLE.')
    E.append(S)
    E.append('### ### **WHETHER THE RULING GOVERNS DOCUMENTS OUTSIDE THE REPOSITORY TREE** (`b379`).')
    E.append('### The download-layer book is called a narrative keystone in one place and')
    E.append('### non-keystone in another, and it was never in the population on either axis.')
    E.append('### ### **WHETHER ROLE CAN BE READ AT ALL WITHOUT BEING DECLARED** (`b380`). ### The')
    E.append('### structural method reads reach and not argument, and ### **THE DISTINCTION THE RUBRIC')
    E.append('### ### IS ABOUT LIVES IN SENTENCES AND NOT IN A CITATION GRAPH.**')
    E.append('### ### **AND WHETHER THE CORPUS`S OWN PRIOR DEFINITION SHOULD GOVERN** (`b376`), which')
    E.append('### states three clauses and applies two through proxies.')
    E.append(B)
    io.open(EVID, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(E) + chr(10))
    print('  written: %s  (%d lines)' % (os.path.basename(EVID), len(E)))
    bad = [i + 1 for i, s in enumerate(E) if '%s' in s or '%d' in s]
    print('  ### UNFILLED PLACEHOLDERS IN THE EVIDENCE FILE : %s' % (bad or 'none'))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
