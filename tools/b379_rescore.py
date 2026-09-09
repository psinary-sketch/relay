# -*- coding: utf-8 -*-
"""b379_rescore.py -- THE DRAFT'S COMPONENT 1 AND ADDITION ONE: ### **THE APPARATUS AXIS RE-SCORED.**

### `b376`'s axis-B predicate required a ### **DOTTED** ### terminal inside a row also carrying kernel,
### pin and grade. ### `b378` swept the citing documents and found ### **NOT ONE OF THEM USES THE
### ### DOTTED CONVENTION ALONE** -- three write the bare dialect only -- so that predicate
### ### **COULD NOT HAVE PASSED THEM HOWEVER COMPLETE THEIR TABLES WERE**, and `b378` named the whole
### `303`-document `B-` column as suspect and did not re-measure it. ### This file re-measures it.

### ### **THE DIRECTION IS REGISTERED ON THE LOCKED FACE, BEFORE THIS RAN:** ### the widened matcher
### accepts everything the old one accepted and more, so ### **A DOCUMENT CAN ONLY MOVE TOWARD
### ### CERTIFYING.** ### The corrected `B+` population is ### **BOUNDED BELOW** ### by the prior one
### and the both-axes quadrant ### **CAN ONLY GROW.**
### ### ### **THAT IS NOT A PREDICTION ABOUT THE CORPUS. ### IT IS A PROPERTY OF THE INSTRUMENT, AND
### ### ### IT IS CHECKED HERE AS A BAR ON THE INSTRUMENT.** ### A document that LOSES a mark is a
### defect in this tool, and it is reported as a defect and never as a finding about the corpus.

### ### **AND EVERY `B-` THIS FILE REPORTS IS AN ABSENCE CLAIM**, so the standing clause applies:
### ### **A POSITIVE CONTROL FINDS A KNOWN PRESENCE FIRST**, and the sweep refuses to report
### otherwise. ### `b378` reported `0` across `270` refs from a search that could not run.

### ### **`b376_axes` IS IMPORTED UNMODIFIED.** ### The prior column is not recomputed from memory or
### from its banked JSON alone -- it is ### **RE-RUN FROM THE ORIGINAL PREDICATE ON THE SAME CORPUS**,
### so the side-by-side table compares two instruments and not an instrument against a recollection.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b376_axes as A6          # noqa: E402  ### THE ORIGINAL PREDICATE, IMPORTED AND NOT EDITED
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# =====================================================================================================
# ### **THE ONE CHANGE, AND IT IS ONE LINE OF PATTERN.**
# ### `b376`: a terminal is a backticked name ### **CONTAINING A DOT.**
# ### `b379`: a terminal is a backticked name containing a dot ### **OR** ### a bare Lean-shaped name
# ### -- lowercase-or-underscore-bearing, as `residue_irreducible` and `fano_two_design` are.
# ### ### **THE WIDENED PATTERN MATCHES A STRICT SUPERSET OF THE OLD ONE**, which is what makes the
# ### monotonicity bar meaningful rather than hopeful. ### Everything else -- kernel, pin, grade, the
# ### table-row test, the concordance rule -- is `b376`'s, imported and untouched.
# =====================================================================================================
WIDE_TERMINAL = re.compile(r'`[A-Za-z_][A-Za-z0-9_₀-₉]*'
                           r'(?:\.[A-Za-z_][A-Za-z0-9_₀-₉]*)+`'      # dotted, as b376 required
                           r'|`[a-zA-Z][A-Za-z0-9₀-₉]*_[A-Za-z0-9_₀-₉]+`')  # bare, with an underscore


def axis_b_wide(txt):
    """### **`b376`'S AXIS B, WITH THE TERMINAL PATTERN WIDENED AND NOTHING ELSE CHANGED.**"""
    best, best_n = None, -1
    for line in txt.split(chr(10)):
        if not A6.TABLE_ROW.match(line):
            continue
        if re.match(r'^\s*\|[\s:|-]+\|\s*$', line):
            continue
        have = (bool(A6.B_KERNEL.search(line)), bool(WIDE_TERMINAL.search(line)),
                bool(A6.B_PIN.search(line)), bool(A6.B_GRADE.search(line)))
        n = sum(have)
        if n > best_n:
            best_n, best = n, (line.strip(), have)
    if best and best_n == 4:
        return 'B+', best[0], 'a table row names kernel, terminal, pin and grade together'
    if A6.B_PROSE_TERMINAL.search(txt) and (best is None or best_n < 4):
        return 'B?', (best[0] if best else ''), 'names terminals in prose or carries a concordance'
    if best:
        names = ('kernel', 'terminal', 'pin', 'grade')
        return 'B-', best[0], 'no row carries all four; the best row carries %s' \
            % (', '.join(n for n, h in zip(names, best[1]) if h) or 'none of the four')
    return 'B-', '', 'the document carries no table row at all'


# ---- THE CONTROLS ----------------------------------------------------------------------------------
CTRL_POS = ('| the residue (§7) | `SIDE-lv-conservation` v0.4.0 | `residue_irreducible` | '
            '`{propext}` | **DERIVES** |')
CTRL_POS_DOT = ('| II.1 | `SIDE-archimedean` v0.1.0 | `SIDEArchimedean.forces_half` | '
                '`{propext}` | **DERIVES** |')
CTRL_NEG = '| a claim in prose | some words | another cell | and a fourth | and a fifth |'


def controls(verbose=True):
    """### **THE SWEEP PROVES IT CAN FIND A PRESENCE BEFORE IT IS ALLOWED TO REPORT AN ABSENCE.**

    ### And it proves the widening is a ### **WIDENING** ### and not a replacement: the dotted row the
    ### old predicate accepted must ### **STILL** ### be accepted.
    """
    cases = [
        ('### **BARE row -- the old predicate REFUSES it**', A6.axis_b(CTRL_POS)[0], 'B-'),
        ('### **BARE row -- the widened predicate ACCEPTS it**', axis_b_wide(CTRL_POS)[0], 'B+'),
        ('DOTTED row -- the old predicate accepts it', A6.axis_b(CTRL_POS_DOT)[0], 'B+'),
        ('### **DOTTED row -- the widened one STILL accepts it**',
         axis_b_wide(CTRL_POS_DOT)[0], 'B+'),
        ('a row with no terminal -- the old one refuses', A6.axis_b(CTRL_NEG)[0], 'B-'),
        ('### **a row with no terminal -- THE WIDENED ONE STILL REFUSES**',
         axis_b_wide(CTRL_NEG)[0], 'B-'),
        ('no table at all -- refused', axis_b_wide('Plain prose, no table.')[0], 'B-'),
    ]
    ok = all(g == w for _l, g, w in cases)
    if verbose:
        for lbl, g, w in cases:
            print('      %-56s got %-3s want %-3s  %s'
                  % (lbl[:56], g, w, 'ok' if g == w else '### MISMATCH ###'))
    return ok, [dict(case=l, got=g, want=w) for l, g, w in cases]


LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(('git', '-C', PP) + a, capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def main():
    rec('=' * 100)
    rec('b379 -- THE APPARATUS AXIS RE-SCORED. ### **THE SUSPECT COLUMN, RE-MEASURED.**')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE CONTROLS, BEFORE ANY ABSENCE IS REPORTED.')
    rec('-' * 100)
    ok, cases = controls(False)
    for c in cases:
        rec('      %-56s got %-3s want %-3s  %s'
            % (c['case'][:56], c['got'], c['want'], 'ok' if c['got'] == c['want'] else '### MISMATCH'))
    rec('    ### ### **CONTROL VERDICT : %s**'
        % ('THE SWEEP FINDS A KNOWN PRESENCE, AND THE WIDENING STILL REFUSES' if ok
           else '### FAILED'))
    rec('    ### **THE FIRST TWO CASES ARE THE WHOLE DEFECT IN MINIATURE:** ### the same complete row,')
    rec('    ### refused by the old predicate and accepted by the widened one, ### **DIFFERING ONLY IN')
    rec('    ### ### WHETHER ITS TERMINAL CARRIES A DOT.**')
    if not ok:
        rec('    ### REFUSING TO RE-SCORE A CORPUS FROM A PREDICATE THAT FAILS ITS OWN CONTROLS.')
        run_clock.write(D, 'b379_rescore_notes', LINES)
        return 2

    # -------------------------------------------------------------------------------- THE SWEEP
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP. ### **BOTH PREDICATES, THE SAME CORPUS, THE SAME RUN.**')
    rec('-' * 100)
    r = git('ls-files', '*.md')
    if r.returncode != 0:
        rec('  ### ### **THE FILE LISTING EXITED %d. ### AN ERROR EXIT IS NOT AN ANSWER.**'
            % r.returncode)
        run_clock.write(D, 'b379_rescore_notes', LINES)
        return 2
    rels = [f for f in r.stdout.split(chr(10)) if f.strip()]
    AX = json.load(io.open(os.path.join(D, 'b376_axes.json'), encoding='utf-8'))
    prior_a = {x['file']: x['axis_a'] for x in AX['scored']}
    prior_b_banked = {x['file']: x['axis_b'] for x in AX['scored']}

    rows, mismatch_prior = [], []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        old_mark, old_row, _w1 = A6.axis_b(txt)
        new_mark, new_row, new_why = axis_b_wide(txt)
        # ### **THE BANKED PRIOR COLUMN IS RE-RUN, NOT TRUSTED.** ### If the re-run disagrees with
        # ### `b376`'s own JSON the corpus moved since, and that is reported rather than absorbed.
        if rel in prior_b_banked and prior_b_banked[rel] != old_mark:
            mismatch_prior.append((rel, prior_b_banked[rel], old_mark))
        a = prior_a.get(rel, 'A?')
        rows.append(dict(file=rel, axis_a=a, prior_b=old_mark, corrected_b=new_mark,
                         prior_quadrant='%s%s' % (a, old_mark),
                         corrected_quadrant='%s%s' % (a, new_mark),
                         moved=(old_mark != new_mark), row=new_row[:300], why=new_why))
    rec('    documents swept : %d' % len(rows))
    rec('    ### **THE BANKED PRIOR COLUMN WAS RE-RUN, NOT TRUSTED.** ### disagreements with `b376`s')
    rec('    ### own JSON : ### **%d** ### %s' % (len(mismatch_prior), mismatch_prior[:3] or ''))
    if mismatch_prior:
        rec('    ### ### **THE CORPUS MOVED SINCE `b376` AND THE SIDE-BY-SIDE TABLE BELOW USES THE')
        rec('    ### ### RE-RUN PRIOR COLUMN**, so both columns are measured on the same bytes.')

    # ------------------------------------------------------------------- THE MONOTONICITY BAR
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE MONOTONICITY BAR. ### **A CHECK ON THE INSTRUMENT, NOT ON THE CORPUS.**')
    rec('-' * 100)
    ORDER = {'B-': 0, 'B?': 1, 'B+': 2}
    lost = [x for x in rows if ORDER[x['corrected_b']] < ORDER[x['prior_b']]]
    gained = [x for x in rows if ORDER[x['corrected_b']] > ORDER[x['prior_b']]]
    pb = sum(1 for x in rows if x['prior_b'] == 'B+')
    cb = sum(1 for x in rows if x['corrected_b'] == 'B+')
    rec('    ### **DOCUMENTS THAT LOST GROUND : %d**' % len(lost))
    for x in lost[:5]:
        rec('      ### ### **%s : %s -> %s**' % (x['file'], x['prior_b'], x['corrected_b']))
    rec('    documents that gained : %d' % len(gained))
    rec('    ### **PRIOR `B+` : %d ### / ### CORRECTED `B+` : %d**' % (pb, cb))
    mono = (not lost) and cb >= pb
    rec('    ### ### **MONOTONICITY : %s**'
        % ('HELD -- the widening behaved as a widening' if mono
           else '### **VIOLATED. ### THIS IS A DEFECT IN THE INSTRUMENT AND IS REPORTED AS ONE.**'))
    if not mono:
        rec('    ### ### ### **THE LOCKED FACE SAID IN ADVANCE THAT A VIOLATION WOULD BE REPORTED AS A')
        rec('    ### ### ### DEFECT AND NOT AS A FINDING ABOUT THE CORPUS. ### IT IS.**')

    # ------------------------------------------------------------------ THE SIDE-BY-SIDE TABLE
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE QUADRANT TABLE. ### **PRIOR AND CORRECTED, SIDE BY SIDE, CELL BY CELL.**')
    rec('-' * 100)
    CELLS = ['A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?']
    pq, cq = {}, {}
    for x in rows:
        pq[x['prior_quadrant']] = pq.get(x['prior_quadrant'], 0) + 1
        cq[x['corrected_quadrant']] = cq.get(x['corrected_quadrant'], 0) + 1
    rec('      %-8s %-10s %-10s %s' % ('cell', 'prior', 'corrected', 'movement'))
    rec('      %s' % ('-' * 74))
    for c in CELLS:
        a, b = pq.get(c, 0), cq.get(c, 0)
        rec('      %-8s %-10d %-10d %s' % (c, a, b, 'same' if a == b else '### **%+d**' % (b - a)))
    rec('      %s' % ('-' * 74))
    rec('      %-8s %-10d %-10d ### **BOTH PARTITION THE SAME %d DOCUMENTS.**'
        % ('total', sum(pq.values()), sum(cq.values()), len(rows)))
    rec('')
    rec('    ### ### **`(F1)` : THE CORRECTED APPARATUS-AXIS POPULATION IS %d AGAINST A PRIOR %d.**'
        % (cb, pb))
    rec('    ### ### **`(F2)` : DOCUMENTS MOVING INTO `A+B+` : %d.**'
        % max(0, cq.get('A+B+', 0) - pq.get('A+B+', 0)))
    into = [x for x in rows if x['corrected_quadrant'] == 'A+B+' and x['prior_quadrant'] != 'A+B+']
    for x in into:
        rec('      ### `%s` ### : %s -> %s' % (x['file'], x['prior_quadrant'],
                                               x['corrected_quadrant']))

    rec('')
    rec('    ### **WHERE THE MOVEMENT LANDED, WHICH IS `(E1)`:**')
    by_from = {}
    for x in rows:
        if x['moved']:
            by_from[x['prior_quadrant']] = by_from.get(x['prior_quadrant'], 0) + 1
    rec('      documents that moved at all : ### **%d**' % sum(by_from.values()))
    for k in sorted(by_from, key=lambda z: -by_from[z]):
        rec('        out of %-6s : %d' % (k, by_from[k]))
    rec('    ### ### **`(E1)` SAID THE MOVEMENT WOULD CONCENTRATE IN `A?B-` RATHER THAN `A+B-`.**')

    # ------------------------------------------------------- WHICH OPTIONS THE CORRECTION WEAKENS
    rec('')
    rec('-' * 100)
    rec('  ### (5) WHICH OF THE RULING`S OPTIONS THE CORRECTION WEAKENS. ### **NONE IS RECOMMENDED.**')
    rec('-' * 100)
    n = len(rows)
    dec_b = sum(1 for x in rows if x['corrected_b'] != 'B?')
    rec('    ### **OPTION 1 -- ONE CLASS ON AXIS B ALONE.** ### Its stated evidence was that axis B is')
    rec('    ### *the axis the documents answer*, decidable for most of the corpus, and that it would')
    rec('    ### admit documents that say nothing about their role.')
    rec('    ###   ### **WHAT THE CORRECTION DOES TO IT:** ### the population it would admit is now')
    rec('    ###     ### **%d RATHER THAN %d.** ### The option is not weakened in its EVIDENCE -- axis'
        % (cb, pb))
    rec('    ###     B is still the decidable axis -- ### **BUT ITS COST IS RESTATED**, because the')
    rec('    ###     documents it admits are more numerous than the option was priced against.')
    rec('    ### **OPTION 2 -- ONE CLASS ON AXIS A ALONE.** ### ### **UNTOUCHED.** ### This act did not')
    rec('    ### run axis A and no document`s `A` mark moved.')
    rec('    ### **OPTION 3 -- BOTH AXES CONJOINED.** ### ### **WEAKENED IN ITS STRICTNESS ARGUMENT.**')
    rec('    ### Its appeal was that the conjunction is the strictest test; the conjunction now holds')
    rec('    ### ### **%d RATHER THAN %d** ### documents, so it is less strict than it was priced as.'
        % (cq.get('A+B+', 0), pq.get('A+B+', 0)))
    rec('    ### **OPTION 4 -- TWO MARKS RATHER THAN ONE CLASS.** ### ### **STRENGTHENED IN ONE')
    rec('    ### ### RESPECT AND NOT IN OTHERS:** ### the correction moves the apparatus column')
    rec('    ### without moving the role column at all, so ### **THE TWO AXES COME APART FURTHER**,')
    rec('    ### which is the observation this option rests on. ### **THAT IS A CONSEQUENCE AND NOT A')
    rec('    ### ### RECOMMENDATION.**')
    rec('    ### **OPTION 5 -- RETIRE THE WORD.** ### ### **UNTOUCHED BY THE CORRECTION.**')
    rec('    ### ### ### **NO OPTION IS RECOMMENDED, RANKED OR PREFERRED, AND THE RULING REMAINS THE')
    rec('    ### ### ### AUTHOR`S.** ### A price that moves is evidence about an option and not a vote')
    rec('    ### ### ### against it.')
    rec('    ### ### **AND THE HONEST WARNING:** ### the corrected column is ### **THIS SEAT`S SECOND')
    rec('    ### ### PREDICATE, NOT A GROUND TRUTH.** ### It is wider than `b376`s and it may still be')
    rec('    ### ### narrower than the corpus. ### **`b376`S COLUMN WAS ALSO BELIEVED WHEN IT WAS')
    rec('    ### ### WRITTEN.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b379_rescore_notes', LINES)
    io.open(os.path.join(D, 'b379_rescore.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(controls_ok=ok, controls=cases, swept=len(rows),
                        prior_bplus=pb, corrected_bplus=cb,
                        prior_quadrants=pq, corrected_quadrants=cq,
                        monotone=mono, lost=[x['file'] for x in lost],
                        gained=[x['file'] for x in gained],
                        moved_into_both=[x['file'] for x in into],
                        prior_column_mismatches=mismatch_prior,
                        decidable_on_b=dec_b, rows=rows,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
