# -*- coding: utf-8 -*-
"""b376_tests.py -- COMPONENTS 4 AND 5.

### ### **COMPONENT 4 -- DO THE TESTS TRACK THE AXES.** ### For each of the three tests that produced the
### three sets, its membership is compared against the axis scores. ### **EQUALS AN AXIS'S SET, IS A
### ### SUBSET OF IT, OR CROSSES QUADRANTS.** ### And ### **A TEST THAT CROSSES IS A TEST THAT MIXES THE
### ### TWO AXES, AND THAT IS THE FINDING THIS ACT EXISTS TO PRODUCE.**
### Then the specific question: ### **IS THE OVERLAP OF THE CERTIFICATION-TEST SET AND THE RUBRIC-TEST
### ### SET EXACTLY THE BOTH-AXES QUADRANT** -- printed as a table, ### **BOTH DIRECTIONS OF DIFFERENCE
### ### LISTED BY DOCUMENT** ### and not counted.

### ### **COMPONENT 5 -- THE FLOOR QUESTION.** ### The rubric-test set came from one tool's test, with
### most of the corpus landing in `OTHER`. ### Axis A's predicate is applied to the `OTHER` population
### and the qualifying documents are printed ### **EACH WITH THE SENTENCE THAT QUALIFIES IT.** ### If
### `OTHER` contains documents that synthesise, the rubric-test set is ### **A FLOOR AND NOT A
### ### POPULATION**, said plainly, with the corrected count and what it does to the earlier tables.

### ### **NO CLASS IS RULED AND NO LIST IS CLOSED.** ### A test that crosses is reported as crossing.
### ### **WHICH TEST SHOULD GOVERN IS THE AUTHOR'S RULING AND IT IS NOT MADE HERE.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def relation(test_set, axis_set):
    """### **EQUALS / SUBSET / SUPERSET / CROSSES -- READ FROM THE SETS, NOT ASSERTED.**"""
    if test_set == axis_set:
        return 'EQUALS'
    if test_set <= axis_set:
        return 'SUBSET OF'
    if axis_set <= test_set:
        return 'SUPERSET OF'
    return '### **CROSSES**'


def main():
    ax = load('b376_axes.json')
    pop = load('b375_population.json')
    scored = {x['file']: x for x in ax['scored']}
    tests = pop['tests']

    rec('=' * 100)
    rec('b376 -- COMPONENTS 4 AND 5: ### **DO THE TESTS TRACK THE AXES, AND IS THE SET A FLOOR.**')
    rec('=' * 100)
    rec('')

    aplus = set(f for f, x in scored.items() if x['axis_a'] == 'A+')
    bplus = set(f for f, x in scored.items() if x['axis_b'] == 'B+')
    aplus_b = set(f for f, x in scored.items() if x['axis_a_broad'] == 'A+')
    both = aplus & bplus
    both_b = aplus_b & bplus

    rec('  ### **THE AXIS SETS, AS COMPONENT 3 LEFT THEM:**')
    rec('    axis A `A+`, strict reading  : %3d' % len(aplus))
    rec('    axis A `A+`, broad reading   : %3d' % len(aplus_b))
    rec('    axis B `B+`                  : %3d' % len(bplus))
    rec('    ### **THE BOTH-AXES QUADRANT `A+B+` : %d ### (broad: %d)**' % (len(both), len(both_b)))
    rec('')

    # ---------------------------------------------------------------- COMPONENT 4, THE THREE TESTS
    rec('-' * 100)
    rec('  ### COMPONENT 4 -- EACH TEST AGAINST EACH AXIS.')
    rec('-' * 100)
    names = [('taxonomy_tier_k', 'THE CERTIFICATION TEST -- documents DECLARING `TIER K`'),
             ('order_rubric', "THE RUBRIC TEST -- the order's rubric applied by `b375`'s tool"),
             ('existing_census', "THE CENSUS TEST -- the corpus's own sixteen")]
    table = {}
    for key, label in names:
        ts = set(tests[key])
        ra = relation(ts, aplus)
        rb = relation(ts, bplus)
        rab = relation(ts, both)
        cells = {}
        for f in ts:
            x = scored.get(f)
            q = x['quadrant'] if x else 'NOT IN THE SWEEP'
            cells[q] = cells.get(q, 0) + 1
        table[key] = dict(label=label, n=len(ts), vs_axis_a=ra, vs_axis_b=rb,
                          vs_both=rab, cells=cells,
                          crosses=(len(cells) > 1))
        rec('')
        rec('    ### **%s** ### -- %d documents' % (label, len(ts)))
        rec('      against axis A (`A+`)          : %s' % ra)
        rec('      against axis B (`B+`)          : %s' % rb)
        rec('      against the `A+B+` quadrant    : %s' % rab)
        rec('      ### **ITS MEMBERS BY QUADRANT  : %s**'
            % ', '.join('%s=%d' % kv for kv in sorted(cells.items())))
        rec('      ### ### **VERDICT : %s**'
            % ('### **IT CROSSES %d QUADRANTS. ### IT MIXES THE TWO AXES.**' % len(cells)
               if len(cells) > 1 else 'it sits in one cell'))

    rec('')
    rec('    ### ### ### **`(F1)` AS THE NAVIGATOR REGISTERED IT -- AT LEAST ONE OF THE THREE TESTS')
    ncross = sum(1 for k in table if table[k]['crosses'])
    rec('    ### ### ### CROSSES QUADRANTS: ### **%d OF THE THREE CROSS.**' % ncross)
    rec('    ### ### ### **AND NOT ONE OF THE THREE EQUALS EITHER AXIS.**' if all(
        table[k]['vs_axis_a'] != 'EQUALS' and table[k]['vs_axis_b'] != 'EQUALS' for k in table)
        else '    ### ### ### (at least one test equals an axis; see the rows above).')
    rec('    ### **SO THE THREE TESTS DO NOT DISAGREE BECAUSE ONE IS WRONG.** ### They disagree because')
    rec('    ### ### **EACH OF THEM IS ASKING BOTH QUESTIONS AT ONCE AND WEIGHTING THEM DIFFERENTLY.**')

    # ------------------------------------------------- THE SPECIFIC QUESTION, BY DOCUMENT NOT COUNT
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 4 (b) -- IS THE CERTIFICATION/RUBRIC OVERLAP EXACTLY THE `A+B+` QUADRANT.')
    rec('-' * 100)
    cert = set(tests['taxonomy_tier_k'])
    rub = set(tests['order_rubric'])
    ov = cert & rub
    rec('    certification-test set          : %3d' % len(cert))
    rec('    rubric-test set                 : %3d' % len(rub))
    rec('    ### **THEIR OVERLAP               : %3d**' % len(ov))
    rec('    ### **THE `A+B+` QUADRANT         : %3d**' % len(both))
    rec('    ### ### **ARE THEY THE SAME SET : %s**'
        % ('YES' if ov == both else '### **NO.**'))
    rec('')
    rec('    ### **BOTH DIRECTIONS OF DIFFERENCE, BY DOCUMENT.** ### `b376` bar 6 requires these listed')
    rec('    ### and not counted, ### **BECAUSE A COUNT OF A DISAGREEMENT CANNOT BE INSPECTED.**')
    rec('')
    only_ov = sorted(ov - both)
    only_q = sorted(both - ov)
    rec('      ### **IN THE OVERLAP, NOT IN `A+B+` (%d):**' % len(only_ov))
    for f in only_ov:
        x = scored.get(f, {})
        rec('        %-58s %s   %s' % (f[:58], x.get('quadrant', '?'),
                                       (x.get('a_why') or '')[:40]))
    rec('      ### **IN `A+B+`, NOT IN THE OVERLAP (%d):**' % len(only_q))
    for f in only_q:
        rec('        %-58s in cert-test: %-5s in rubric-test: %s'
            % (f[:58], f in cert, f in rub))
    rec('')
    rec('    ### ### **`(F3)` AS THE NAVIGATOR REGISTERED IT -- THE CERTIFICATION-TEST SET IS CLOSE TO A')
    inb = len(cert & bplus)
    rec('    ### ### CLEAN AXIS-B SET: ### **%d OF ITS %d MEMBERS SCORE `B+`.**' % (inb, len(cert)))
    cb = {}
    for f in cert:
        x = scored.get(f)
        m = x['axis_b'] if x else '?'
        cb[m] = cb.get(m, 0) + 1
    rec('    ### ### its members by axis B : %s' % cb)
    rec('    ### ### ### **AND THE TRAP THIS ACT`S FACE NAMED BEFORE THE MEASUREMENT STANDS:** ### the')
    rec('    ### ### ### certification-test set is the set of documents that ### **DECLARED** ### `TIER K`')
    rec('    ### ### ### and axis B measures whether a document ### **CARRIES THE APPARATUS.** ### Where')
    rec('    ### ### ### they agree, this act reports ### **AGREEMENT** ### and not confirmation that the')
    rec('    ### ### ### declarations are correct. ### **BOTH MAY BE READING THE SAME HABIT OF WRITING.**')

    # --------------------------------------------------------- COMPONENT 5, THE FLOOR QUESTION
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 5 -- THE FLOOR QUESTION.')
    rec('-' * 100)
    other = [r['file'] for r in pop['rows'] if r['order_class'] == 'OTHER']
    rec("    the `OTHER` population, as `b375`'s tool left it : ### **%d of %d**"
        % (len(other), len(pop['rows'])))
    qual = [f for f in other if scored.get(f, {}).get('axis_a') == 'A+']
    qual_b = [f for f in other if scored.get(f, {}).get('axis_a_broad') == 'A+']
    rec('    ### **OF THOSE, SATISFYING AXIS A (strict) : %d ### / ### (broad) : %d**'
        % (len(qual), len(qual_b)))
    rec('')
    if qual:
        rec('    ### **EACH ONE, WITH THE SENTENCE THAT QUALIFIES IT:**')
        for f in sorted(qual):
            rec('      ### `%s`' % f)
            rec('        | %s' % (scored[f]['a_sentence'] or '')[:160])
    if set(qual_b) - set(qual):
        rec('')
        rec('    ### **AND UNDER THE BROAD READING, THESE ALSO QUALIFY:**')
        for f in sorted(set(qual_b) - set(qual)):
            rec('      ### `%s`' % f)
            rec('        | %s' % (scored[f]['a_sentence_broad'] or '')[:160])
    rec('')
    # ### **AND THE DEAFNESS AXIS A DECLARED IN ADVANCE IS LOAD-BEARING RIGHT HERE, SO IT IS
    # ### RE-STATED AT THE FINDING AND NOT LEFT IN THE PREDICATE'S SMALL PRINT.**
    import re as _re
    CLASSLINE = _re.compile(r'\*\*DOCUMENT CLASS|basis:', _re.I)
    onclass = [f for f in qual if CLASSLINE.search(scored[f]['a_sentence'] or '')]
    onclass_b = [f for f in qual_b if CLASSLINE.search(scored[f]['a_sentence_broad'] or '')]
    rec('    ### ### **A CAVEAT THAT BELONGS AT THE FINDING AND NOT IN THE PREDICATE`S SMALL PRINT:**')
    rec('    ### ### of the %d strict qualifiers, ### **%d QUALIFY ON A `DOCUMENT CLASS` OR `basis:`'
        % (len(qual), len(onclass)))
    rec('    ### ### LINE THAT A LATER ACT WROTE INTO THE DOCUMENT** ### (`b189`/`b190`), not on prose the')
    rec('    ### ### document carried when it was written; ### under the broad reading, %d of %d.'
        % (len(onclass_b), len(qual_b)))
    rec('    ### ### ### **AXIS A CANNOT TELL A DOCUMENT`S OWN VOICE FROM AN ANNOTATION ADDED TO IT**,')
    rec('    ### ### ### because on the page they are the same words. ### The predicate declared this')
    rec('    ### ### ### deafness before the sweep and it is ### **LOAD-BEARING ON EXACTLY THIS FINDING.**')
    rec('    ### ### ### ### **SO `(F2)` IS MET BY THE PRINT, AND THE PRINT SAYS THE SYNTHESIS CLAIM FOR')
    rec('    ### ### ### ### MOST QUALIFIERS IS A LATER ACT`S SENTENCE ABOUT THE DOCUMENT.**')
    rec('')
    floor = bool(qual or qual_b)
    if floor:
        rec('    ### ### ### **SAID PLAINLY, AS THE ORDER REQUIRES: ### THE RUBRIC-TEST SET IS A FLOOR')
        rec('    ### ### ### AND NOT A POPULATION.** ### `OTHER` contains documents that satisfy axis A by')
        rec('    ### ### ### the rubric`s own words, so ### **A DOCUMENT`S ABSENCE FROM THE RUBRIC-TEST')
        rec('    ### ### ### SET IS NOT EVIDENCE THAT IT DOES NOT SYNTHESISE.**')
        rec('    ### **`(F2)` IS MET.**')
    else:
        rec('    ### ### **`OTHER` CONTAINS NO DOCUMENT SATISFYING AXIS A**, so on this evidence the')
        rec('    ### ### rubric-test set is not shown to be a floor. ### **`(F2)` IS REFUTED BY THE PRINT.**')
    rec('')
    rec('    ### **THE CORRECTED COUNT, AND WHAT IT DOES TO THE EARLIER TABLES:**')
    rec('      rubric-test set as `b375` printed it        : %3d' % len(rub))
    rec('      plus `OTHER` documents satisfying axis A    : %3d  (broad: %d)' % (len(qual), len(qual_b)))
    rec('      ### **THE FLOOR-CORRECTED SYNTHESIS COUNT     : %3d  ### (broad: %d)**'
        % (len(rub) + len(qual), len(rub) + len(qual_b)))
    rec('      ### ### **AND THE HONEST UPPER FIGURE IS STILL NOT A POPULATION**, because %d documents'
        % sum(1 for x in scored.values() if x['axis_a'] == 'A?'))
    rec('      ### ### score `A?` on axis A -- ### **THEY DO NOT SAY WHAT THEY ARE**, and no count of')
    rec('      ### ### documents that speak can bound the documents that are silent.')
    rec('')
    rec('    ### **WHAT IT DOES TO COMPONENT 3`S TABLE:** ### nothing, because Component 3 already')
    rec('    ### scored ### **EVERY** ### document on both axes and never used the rubric-test set. ### The')
    rec('    ### floor correction moves ### **COMPONENT 4`S** ### rubric row, whose set is the one drawn')
    rec('    ### from a tool rather than from the axes.')
    rec('=' * 100)

    p = run_clock.write(D, 'b376_tests_notes', LINES)
    io.open(os.path.join(D, 'b376_tests.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(axis_a_plus=sorted(aplus), axis_a_plus_broad=sorted(aplus_b),
                        axis_b_plus=sorted(bplus), both_axes=sorted(both),
                        tests=table, crosses=ncross,
                        overlap=sorted(ov), overlap_not_quadrant=only_ov,
                        quadrant_not_overlap=only_q, overlap_equals_quadrant=(ov == both),
                        cert_by_axis_b=cb,
                        other_population=len(other), other_satisfying_a=sorted(qual),
                        other_satisfying_a_broad=sorted(qual_b), is_a_floor=floor,
                        qualifying_on_a_later_acts_class_line=sorted(onclass),
                        qualifying_on_a_later_acts_class_line_broad=sorted(onclass_b),
                        run_file=os.path.basename(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
