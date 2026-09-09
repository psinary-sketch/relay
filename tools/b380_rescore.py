# -*- coding: utf-8 -*-
"""b380_rescore.py -- COMPONENTS 1, 2 AND 3: ### **THE PREMISE, THE PREDICATE, AND ITS OWN CONTROL.**

### ### **COMPONENT 1 -- THE PREMISE, MEASURED BEFORE THE METHOD RUNS.** ### The order's reason for
### replacing the method is that the documents do not say what they do. ### That is a claim about the
### corpus, so it is printed ### **FIRST** ### and whatever it says stands.

### ### **COMPONENT 2 -- THE STRUCTURAL PREDICATE**, imported from `tools/role_structure.py`, built
### from the rubric's own sentence and fixtured in three polarities before it scores anything.

### ### **COMPONENT 3 -- EVERY DOCUMENT RE-SCORED, THE PRIOR SCORE KEPT BESIDE IT AND NEVER
### ### OVERWRITTEN**, and ### **THE CONTROL REPORTED BEFORE ANY OTHER RESULT** -- because a predicate
### that contradicts the only ground truth available has failed, however plausible its output looks.
### ### **AND NO MONOTONICITY BAR APPLIES.** ### `b379`'s widening was a superset and could only add;
### ### **THIS IS A DIFFERENT METHOD, NOT A WIDER ONE**, so a document may move either way and neither
### direction is a defect or a discovery on its own.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
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


def git(*a):
    return subprocess.run(('git', '-C', PP) + a, capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def main():
    AX = json.load(io.open(os.path.join(D, 'b376_axes.json'), encoding='utf-8'))
    B9 = json.load(io.open(os.path.join(D, 'b379_rescore.json'), encoding='utf-8'))
    prior_a = {x['file']: x['axis_a'] for x in AX['scored']}
    prior_a_broad = {x['file']: x['axis_a_broad'] for x in AX['scored']}
    a_sent = {x['file']: x['a_sentence'] for x in AX['scored']}
    corrected_b = {r['file']: r['corrected_b'] for r in B9['rows']}

    rec('=' * 100)
    rec('b380 -- THE ROLE AXIS, SCORED STRUCTURALLY.')
    rec('=' * 100)
    rec('')

    # ------------------------------------------------------------------- COMPONENT 1: THE PREMISE
    rec('-' * 100)
    rec('  ### COMPONENT 1 -- THE PREMISE, MEASURED BEFORE THE METHOD RUNS.')
    rec('-' * 100)
    ta, tb = {}, {}
    for f, m in prior_a.items():
        ta[m] = ta.get(m, 0) + 1
    for f, m in prior_a_broad.items():
        tb[m] = tb.get(m, 0) + 1
    n = len(prior_a)
    decided = sum(v for k, v in ta.items() if k != 'A?')
    decided_b = sum(v for k, v in tb.items() if k != 'A?')
    rec('    documents in the population : %d' % n)
    rec('    ### **THE ROLE AXIS AS IT STANDS, `b376`S STRICT READING : %s**' % ta)
    rec('    ### **AND `b376`S BROAD READING, RUN AT `b376` AND NEVER ADOPTED : %s**' % tb)
    rec('')
    rec('    ### ### **SCORED FROM A STATEMENT THE DOCUMENT MAKES : %d strict / %d broad**'
        % (decided, decided_b))
    rec('    ### ### **SCORED `NOT DETERMINABLE`               : %d strict / %d broad**'
        % (ta.get('A?', 0), tb.get('A?', 0)))
    rec('    ### ### ### **SO THE PREMISE HOLDS AS A MEASUREMENT: ### %.1f%% OF THE CORPUS SAYS'
        % (100.0 * ta.get('A?', 0) / n))
    rec('    ### ### ### NOTHING ABOUT ITS OWN ROLE UNDER THE STRICT READING, AND %.1f%% UNDER THE'
        % (100.0 * tb.get('A?', 0) / n))
    rec('    ### ### ### BROAD ONE.** ### The order`s reason for replacing the method is on the record')
    rec('    ### ### ### as a number and not as an assertion.')
    rec('    ### **AND THE BROAD READING IS THE FAIREST AVAILABLE VERSION OF THE OLD METHOD**, so the')
    rec('    ### comparison below is against the better of the two and not the weaker.')

    # ----------------------------------------------------------------- COMPONENT 2: THE PREDICATE
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 -- THE STRUCTURAL PREDICATE, FIXTURED BEFORE IT SCORES ANYTHING.')
    rec('-' * 100)
    ok, cases = RS.self_test(False)
    for c in cases:
        rec('      %-62s got %-5s want %-5s %s'
            % (c['case'][:62], c['got'][:5], c['want'][:5],
               'ok' if c['got'] == c['want'] else '### MISMATCH'))
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('ALL THREE MARKS REACHABLE, AND THE REJECTIONS HOLD' if ok else '### FAILED'))
    rec('    ### **THE RULE, AS THE LOCKED FACE STATED IT BEFORE THIS RAN:** ### `A+` where a document')
    rec('    ### reaches beyond its own subject in ### **AT LEAST TWO DISTINCT PLACES**, counting each')
    rec('    ### foreign cluster it cites into and each kernel it names; `A-` where it draws on')
    rec('    ### something and the reach is under two; `A?` where it draws on nothing.')
    rec('    ### ### **THE THRESHOLD IS A CHOICE AND IT WAS DECLARED, NOT DISCOVERED.**')
    if not ok:
        run_clock.write(D, 'b380_rescore_notes', LINES)
        return 2

    # --------------------------------------------------------------------- COMPONENT 3: THE SWEEP
    r = git('ls-files', '*.md')
    if r.returncode != 0:
        rec('  ### ### **THE FILE LISTING EXITED %d. ### AN ERROR EXIT IS NOT AN ANSWER.**'
            % r.returncode)
        run_clock.write(D, 'b380_rescore_notes', LINES)
        return 2
    rels = [f for f in r.stdout.split(chr(10)) if f.strip()]
    index = RS.build_index(PP)
    rows = []
    for rel in rels:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        mark, why, ev = RS.score(rel, txt, index)
        rows.append(dict(file=rel,
                         statement_a=prior_a.get(rel, 'A?'),
                         statement_a_broad=prior_a_broad.get(rel, 'A?'),
                         structural_a=mark, structural_why=why, evidence=ev,
                         corrected_b=corrected_b.get(rel, 'B-'),
                         statement_sentence=(a_sent.get(rel) or '')[:200]))

    # ### **THE CONTROL FIRST. ### BEFORE ANY OTHER RESULT.** ### BAR 3.
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 3 (a) -- THE CONTROL, REPORTED BEFORE ANY OTHER RESULT.')
    rec('-' * 100)
    decl = [x for x in rows if x['statement_a'] in ('A+', 'A-')]
    syn = [x for x in decl if x['statement_a'] == 'A+']
    gat = [x for x in decl if x['statement_a'] == 'A-']
    agree = [x for x in decl if x['structural_a'] == x['statement_a']]
    disagree = [x for x in decl if x['structural_a'] != x['statement_a']]
    agree_syn = [x for x in syn if x['structural_a'] == 'A+']
    rec('    ### **THE DECLARERS: %d SYNTHESIS + %d GATHERING = %d**' % (len(syn), len(gat), len(decl)))
    rec('')
    rec('    %-52s %-10s %-10s %s' % ('document', 'statement', 'structural', 'agree'))
    rec('    %s' % ('-' * 90))
    for x in decl:
        rec('    %-52s %-10s %-10s %s'
            % (x['file'][:52], x['statement_a'], x['structural_a'],
               'yes' if x['structural_a'] == x['statement_a'] else '### **NO**'))
    rec('')
    rec('    ### ### **AGREEMENT OVER THE SEVEN THAT DECLARE SYNTHESIS : %d OF %d.**'
        % (len(agree_syn), len(syn)))
    rec('    ### ### **AGREEMENT OVER ALL %d DECLARERS               : %d.**' % (len(decl), len(agree)))
    if disagree:
        rec('')
        rec('    ### ### ### **THE DISAGREEMENTS, AT FULL PROMINENCE AND AS A DEFECT IN THE PREDICATE')
        rec('    ### ### ### AND NOT IN THE DOCUMENTS:**')
        for x in disagree:
            rec('      ### `%s`' % x['file'])
            rec('        the document says   : %s -- %s' % (x['statement_a'],
                                                            x['statement_sentence'][:100]))
            rec('        the predicate says  : %s -- %s' % (x['structural_a'], x['structural_why'][:90]))
            rec('        its reach           : %s' % x['evidence'])
        rec('    ### ### **THE THRESHOLD IS NOT MOVED TO MAKE THESE AGREE.** ### The locked face said')
        rec('    ### ### so before the control ran, and ### **A PREDICATE FITTED TO ITS OWN CONTROL HAS')
        rec('    ### ### NO CONTROL.**')
    else:
        rec('    ### ### **NO DISAGREEMENTS.** ### The predicate matches the corpus`s own statements')
        rec('    ### ### wherever the corpus made one.')
    rec('')
    rec('    ### **AND `(E2)` AS THIS FACE REGISTERED IT:** ### three of the seven that declare')
    rec('    ### synthesis are ledgers -- `OPEN_TRAILS`, `REGISTRY`, `VERIFICATION_LOOM` -- which reach')
    rec('    ### everywhere by construction. ### **WHERE THE PREDICATE AGREES WITH THOSE IT MAY BE')
    rec('    ### ### AGREEING FOR THE WRONG REASON**, and their reach is printed so a reader can see')
    rec('    ### how it was reached:')
    for x in decl:
        b = os.path.basename(x['file'])[:-3]
        if b in ('OPEN_TRAILS', 'REGISTRY', 'VERIFICATION_LOOM'):
            rec('      %-24s reach %-4d kernels %-3d foreign clusters %d'
                % (b, x['evidence']['reach'], len(x['evidence']['kernels']),
                   len(x['evidence']['foreign_clusters'])))

    # ------------------------------------------------------------ THE DISTRIBUTION AND THE MOVEMENT
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 3 (b) -- THE CORRECTED ROLE DISTRIBUTION, THE PRIOR ONE KEPT BESIDE IT.')
    rec('-' * 100)
    ts = {}
    for x in rows:
        ts[x['structural_a']] = ts.get(x['structural_a'], 0) + 1
    rec('      %-10s %-12s %-12s %s' % ('mark', 'statement', 'structural', 'movement'))
    rec('      %s' % ('-' * 62))
    for m in ('A+', 'A-', 'A?'):
        a, b = ta.get(m, 0), ts.get(m, 0)
        rec('      %-10s %-12d %-12d %s' % (m, a, b, 'same' if a == b else '### **%+d**' % (b - a)))
    rec('      %s' % ('-' * 62))
    rec('      %-10s %-12d %-12d ### **BOTH PARTITION THE SAME %d DOCUMENTS.**'
        % ('total', sum(ta.values()), sum(ts.values()), len(rows)))
    outof = [x for x in rows if x['statement_a'] == 'A?' and x['structural_a'] != 'A?']
    rec('')
    rec('    ### ### **DOCUMENTS MOVED OUT OF `NOT DETERMINABLE` : %d OF %d (%.1f%%).**'
        % (len(outof), ta.get('A?', 0), 100.0 * len(outof) / max(1, ta.get('A?', 0))))
    rec('    ### ### **`(F1)` : A MAJORITY OUT OF `NOT DETERMINABLE` -- %s.**'
        % ('MET' if len(outof) > ta.get('A?', 0) / 2.0 else '### **REFUTED**'))
    rec('    ### **AND NO MONOTONICITY BAR APPLIES**, as the locked face said: this is a different')
    rec('    ### method and not a wider one, so a document may move either way.')
    back = [x for x in rows if x['statement_a'] != 'A?' and x['structural_a'] == 'A?']
    rec('    ### documents that moved INTO `NOT DETERMINABLE` : %d %s'
        % (len(back), [x['file'] for x in back][:3] or ''))

    # ------------------------------------------------------------------ THE QUADRANT TABLE
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 3 (c) -- THE QUADRANT TABLE, BOTH SCORES` VERSIONS SIDE BY SIDE.')
    rec('-' * 100)
    rec('    ### the apparatus column is `b379`s CORRECTED one in both versions, so only the role')
    rec('    ### column differs between them.')
    CELLS = ['A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?']
    qs, qt = {}, {}
    for x in rows:
        qs['%s%s' % (x['statement_a'], x['corrected_b'])] = \
            qs.get('%s%s' % (x['statement_a'], x['corrected_b']), 0) + 1
        qt['%s%s' % (x['structural_a'], x['corrected_b'])] = \
            qt.get('%s%s' % (x['structural_a'], x['corrected_b']), 0) + 1
    rec('')
    rec('      %-8s %-14s %-14s %s' % ('cell', 'statement-role', 'structural-role', 'movement'))
    rec('      %s' % ('-' * 70))
    for c in CELLS:
        a, b = qs.get(c, 0), qt.get(c, 0)
        rec('      %-8s %-14d %-14d %s' % (c, a, b, 'same' if a == b else '### **%+d**' % (b - a)))
    rec('      %s' % ('-' * 70))
    rec('      %-8s %-14d %-14d ### **BOTH PARTITION THE SAME %d DOCUMENTS.**'
        % ('total', sum(qs.values()), sum(qt.values()), len(rows)))
    rec('')
    rec('    ### ### **`(F3)` : THE BOTH-AXES QUADRANT `A+B+` -- STATEMENT-ROLE %d, STRUCTURAL-ROLE'
        % qs.get('A+B+', 0))
    rec('    ### ### %d.**' % qt.get('A+B+', 0))
    rec('    ### ### **NON-EMPTY : %s.**' % ('YES' if qt.get('A+B+', 0) else '### **NO**'))
    rec('    ### **AND WHAT `(E3)` SAID ABOUT IT:** ### a non-empty quadrant reached by widening the')
    rec('    ### OTHER axis is not the same as a quadrant the corpus earned. ### Of the %d in `A+B+`'
        % qt.get('A+B+', 0))
    inq = [x for x in rows if x['structural_a'] == 'A+' and x['corrected_b'] == 'B+']
    was = sum(1 for x in inq if x['statement_a'] == 'A+')
    rec('    ### structurally, ### **%d ALREADY SAID SO THEMSELVES AND %d ARE THERE ONLY BECAUSE THIS'
        % (was, len(inq) - was))
    rec('    ### ### ACT READ THEIR STRUCTURE.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b380_rescore_notes', LINES)
    io.open(os.path.join(D, 'b380_rescore.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(population=len(rows), fixtures_ok=ok, fixtures=cases,
                        statement_tally=ta, statement_broad_tally=tb, structural_tally=ts,
                        decided_statement=decided, decided_statement_broad=decided_b,
                        not_determinable=ta.get('A?', 0),
                        declarers=len(decl), declarers_synthesis=len(syn),
                        declarers_gathering=len(gat),
                        agreement_over_seven=len(agree_syn), agreement_over_all=len(agree),
                        disagreements=[dict(file=x['file'], statement=x['statement_a'],
                                            structural=x['structural_a'],
                                            why=x['structural_why'], evidence=x['evidence'])
                                       for x in disagree],
                        moved_out_of_nd=len(outof), moved_into_nd=len(back),
                        quadrants_statement=qs, quadrants_structural=qt,
                        both_axes_statement=qs.get('A+B+', 0),
                        both_axes_structural=qt.get('A+B+', 0),
                        both_axes_already_declared=was,
                        threshold_moved=False, prior_scores_overwritten=0,
                        rows=rows, run_file=os.path.basename(p),
                        run_clock=run_clock.read_stamp(p)), indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
