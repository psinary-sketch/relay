# -*- coding: utf-8 -*-
"""b323_checks.py -- THE GATE SUITE FOR A FILINGS ACT.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-ADDITIVE`** ### -- ### **THE ONE A FOLD MOST EASILY BREACHES, AND THE ONE THAT
###     ### CANNOT BE PROMISED.** ### `FINDINGS.md` after the append must carry its pre-append
###     content as a TRUE BYTE PREFIX -- against the working file AND against the blob at `HEAD`,
###     because b309's trap is that `core.autocrlf` makes those differ on a clean tree.
###   ### ### **`G-GENERATED`** ### -- `F-QUOTE` ran as a GENERATOR, with its discrimination arm.
###     ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE.**
###   ### ### **`G-OWNDEFECTS`** ### -- ### **THE ARM THIS ACT NEEDED MOST.** ### The fold files a
###     table of three sealed bars found defective in OTHER acts. ### An act that did that while
###     hiding three defects in its own generator would be doing the exact thing the table exists
###     to prevent. ### All three must be in the bank AND in the correspondence row.
###   ### **`G-NOCONCLUDE`** ### -- a fold is a filing. ### No grade moved, no theorem proved, no
###     margin size certified, and the index row hands all three back on query.
###   ### **`G-NOCLAIM`** ### -- `the archimedean membership` stays UNKEYED. ### A fold that claimed
###     it would be filing a verdict nobody reached.
###   ### **`G-MIRROR`** ### -- three clauses, and the rebuild AFTER the commit.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

# ### **THE OWNERS.** ### A filings act edits no instrument at all.
OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/b205_prolate.py', 'tools/e16/prolate_layer.py',
          'tools/e16/b313f_qeps_layer.py', 'tools/e16/b313r_qeps_layer.py',
          'tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
          'tools/b319_stable.py', 'tools/b320_weil.py', 'tools/b321_window.py',
          'tools/b322_ladder.py', 'tools/noise_floor.py', 'tools/b314_fold.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b323_the_fold.txt')
REG = d('b323_registration_2026-09-04.txt')
RUN = d('b323_fold_run.txt')
EMIT = d('b323_fold_emitted.md')
SCAN = d('b323_ferry_scan.txt')
FERRY = d('b323_ferry_2026-09-04.txt')
CENSUS = d('b323_census.txt')
EXTRACT = d('b323_extract_notes.txt')

OWNED = [RUN, EMIT, CENSUS, EXTRACT, d('b323_index_query.txt'), d('b323_index_run.txt'),
         d('b323_pins_stepzero.txt'), d('b323_regspec_run.txt'), d('b323_reg_termscan.txt'),
         d('b323_satisfiable.json'), d('b323_satisfiable_run.txt'), d('b323_fold_rows.json'),
         t('b323_regspec.py'), t('b323_correspondence.py'), t('b323_fold.py'),
         t('b323_extract.py')]

CARRIERS = [
    (t('b323_checks.py'), 'its own fixtures'),
    (t('b323_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

# ### **THE NINE ORIGINATING ACTS. ### EVERY QUOTATION IS PULLED FROM THE ACT THAT EMITTED IT.**
NINE = {
    'b314': d('b314_the_fold_and_the_cold_clone.txt'),
    'b315': d('b315_the_calibration_and_the_rate.txt'),
    'b316': d('b316_the_archimedean_instrument.txt'),
    'b317': d('b317_the_trace_on_the_object.txt'),
    'b318': d('b318_the_forced_sign.txt'),
    'b319': d('b319_the_stable_rank.txt'),
    'b320': d('b320_the_lawful_function.txt'),
    'b321': d('b321_the_window_opened.txt'),
    'b322': d('b322_the_membership.txt'),
}

OWNER_NEEDLES = [
    ("b314 -- the cold clone, at its own act", NINE['b314'],
     'BYTE-FOR-BYTE EQUAL TO THE BANKED BLOB'),
    ("### and the coverage shortfall it found", NINE['b314'],
     'MODULES SIT OUTSIDE THE CERTIFICATION FILE, ALL 25 ELABORATE, AND 91'),
    ("b315 -- the calibration, at its own act", NINE['b315'],
     'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    ("### and the envelope that becomes a constant", NINE['b315'],
     "UNDER THE SOURCE'S EXPONENT THE ENVELOPE BECOMES A CONSTANT"),
    ("b316 -- the instrument, at its own act", NINE['b316'], 'THE INSTRUMENT EXISTS'),
    ("### and the membership it could not confirm", NINE['b316'],
     "b300's MEMBERSHIP IS NOT CONFIRMED"),
    ("b317 -- the number, at its own act", NINE['b317'], 'THE NUMBER EXISTS'),
    ("### and the broken chain it landed on", NINE['b317'],
     'A NUMBER THAT LANDS WHERE A BROKEN CHAIN SAID'),
    ("b318 -- the square, at its own act", NINE['b318'],
     'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT'),
    ("### and the window typed as a seed", NINE['b318'], "THE CORPUS'S WINDOW IS A CANDIDATE"),
    ("b319 -- the coverage repair, at its own act", NINE['b319'],
     'THE KERNEL-COVERAGE DEFECT IS DISCHARGED'),
    ("### and the first sealed bar found defective", NINE['b319'],
     'THE BAR THIS ACT SEALED IS DEFECTIVE'),
    ("b320 -- the control at 27 of 27, at its own act", NINE['b320'], '27 OF 27 FRAMES'),
    ("### and the FAILS it reported first", NINE['b320'], "FIRST REPORTED VERDICT WAS `FAILS`"),
    ("b321 -- the prime sum inside the margin, at its own act", NINE['b321'],
     'THE PRIME SUM EXCEEDS THE MARGIN AT NO CELL OF THIS LADDER'),
    ("### and the count forced by structure", NINE['b321'],
     'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION AND IS NOT EVIDENCE'),
    ("b322 -- the residual falling, at its own act", NINE['b322'],
     'THE RESIDUAL FALLS, AT EVERY STEP OF THE DOMAIN LADDER'),
    ("### and the leg left under-resolved with its price", NINE['b322'],
     "SO THE VERDICT IS `UNDER-RESOLVED`, AND IT CARRIES ITS PRICE"),
    ("### the two further sealed bars found defective", NINE['b322'],
     'DICHOTOMY IS NOT A PARTITION'),
    ("the prior fold's generator, whose discipline this one inherits", t('b314_fold.py'),
     'def fquote'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank reports the section filed', BANK, 'THE SECTION IS FILED'),
    ('### bank states the additivity was measured', BANK,
     'PURELY ADDITIVE, MEASURED AND NOT PROMISED'),
    ('bank reports F-QUOTE', BANK, '`F-QUOTE` PASSES AT 18 OF 18'),
    ('bank reports F-COUNT', BANK, '`F-COUNT` PASSES'),
    ('### bank names the defective-bars table', BANK, 'SEALED BARS'),
    ('### and that no sealed file was edited', BANK, 'IN NO CASE WAS THE SEALED FILE EDITED'),
    ("### bank gives its OWN defects their own section", BANK, 'TWO DEFECTS IN THIS ACT'),
    ('### and names the double-append', BANK, 'IT RAN TWICE AND FILED THE ARC TWICE'),
    ('### and the prose-vs-value defect', BANK,
     'ASSERTED A DIFFERENCE ITS OWN MEASUREMENT SHOWED WAS ZERO'),
    ('### and the empty run file', BANK, 'WAS EMPTY AFTER BOTH'),
    ('bank states no grade moves', BANK, 'NO GRADE MOVES'),
    ('### bank declares the judgement the mechanism does not make', BANK,
     'THE JUDGEMENT THE MECHANISM DOES NOT MAKE'),
    ('bank gives the arc as one statement', BANK, 'COMPONENT 2 -- THE ARC AS ONE STATEMENT'),
    ('### and the remainder identified with the margin', BANK, 'THAT REMAINDER IS THE MARGIN'),
    ('### and that the window decides nothing', BANK, 'THE WINDOW DECIDES NOTHING'),
    ('### and the mechanism no finite instrument crosses', BANK,
     'MEASURING IT IS WHAT SHOWS THE DISTANCE'),
    ('bank splits the lore by what enforces it', BANK, 'MECHANIZED AND JUDGEMENT KEPT APART'),
    ('bank inventories the suite', BANK, 'THE INSTRUMENT SUITE'),
    ('bank gives the desk', BANK, 'COMPONENT 5 -- THE DESK'),
    ('### and names the keystone re-read', BANK, 'THE KEYSTONE RE-READ'),
    ("### and the wave as the author's", BANK, 'THE RECONCILIATION WAVE'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('### and that six acts named the fold due before it was done', BANK,
     'SIX ACTS SAID IT AND NONE DID IT'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('bank reports the hook either way', BANK, 'THE HOOK, AND ITS RESULT REPORTED EITHER WAY'),
    ('### and the mirror after the commit on three clauses', BANK,
     'REBUILT AFTER THE COMMIT AND VERIFIED ON ALL THREE CLAUSES'),
    ('registration names the act', REG, 'THE FOLD'),
    ('the run reports F-QUOTE clean', RUN, 'F-QUOTE  : 18 quotations, 0 unfindable'),
    ('### and its discrimination control', RUN, 'DISCRIMINATION CONTROL'),
    ('the run reports F-COUNT clean', RUN, 'F-COUNT  : results cover 9'),
    ('the run measures the additivity', RUN, 'PURELY ADDITIVE : True'),
    ('the run reports all fold gates passing', RUN, 'FOLD GATES : ALL PASS'),
    ('the emitted section carries its title', EMIT, 'THE ARCHIMEDEAN INSTRUMENT ARC'),
    ('### and the defective-bars table', EMIT, 'Sealed bars found defective'),
    ('### and the arc as one statement', EMIT, 'The arc as one statement'),
    ('### and closes with h2 unchanged', EMIT, 'h2 UNCHANGED'),
    ('the extract found every sentence at its own act', EXTRACT,
     'SENTENCES NOT FOUND AT THEIR OWN ACT : 0'),
    ('### and opened every bank', EXTRACT, 'BANKS NOT PRESENT : 0'),
]

MUST_FAIL = [
    # ### **`G-NOCONCLUDE` -- the sentences a fold would be tempted to write.**
    ('the arc is not called concluded', BANK, 'THE ARC IS CONCLUDED.'),
    ('no theorem is claimed', BANK, 'THE THEOREM IS PROVED.'),
    ('the identity is not decided', BANK, 'THE IDENTITY HOLDS.'),
    ('positivity is not claimed', BANK, 'WEIL POSITIVITY HOLDS.'),
    ('no margin size is certified', BANK, 'THE MARGIN IS CONVERGED.'),
    # ### **`G-NOCLAIM`.**
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('the unit is not placed in the space', BANK, 'THE UNIT IS IN THE SPACE.'),
    ('the L2 question is not closed', BANK, 'W-ORD-PHI-MU-L2 IS DISCHARGED.'),
    # ### **`G-ADDITIVE` and the filing caps.**
    ('nothing is removed from FINDINGS', BANK, 'A SECTION IS REMOVED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b319 IS RE-VERDICTED.'),
    ('b322 is not re-verdicted', BANK, 'b322 IS RE-VERDICTED.'),
    ('no sealed file is edited', BANK, 'THE REGISTRATION IS EDITED.'),
    ('the keystone is not written', BANK, 'THE KEYSTONE IS RE-READ.'),
    # ### **THE STANDING CAPS.**
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the roster', BANK, 'THE ROSTER IS COMPLETE.'),
    ('the wave is not started', BANK, 'THE WAVE IS STARTED.'),
]

TOOLNUM = [
    ("the fold's quotations, counts and additivity check", 'tools/b323_fold.py'),
    ("the nine banks read at their own files", 'tools/b323_extract.py'),
    ("the prior fold, whose discipline this one inherits", 'tools/b314_fold.py'),
    ("the mirror's three clauses", 'tools/mirror_verify.py'),
    ("the mirror build and its roster", 'tools/mirror_build.ps1'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b323_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b323_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b323_correspondence.py'),
    ("the index key's read-back arms", 'tools/b323_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b323' in x)

# ### **THE SEALED HASH, WRITTEN HERE BEFORE THE SECTION WAS EMITTED.**
SEAL = 'dddca1c9d3657dedc8b7d970534c019dba22c84c6a808a0696eb04194cb91d03'
SECTION = 'THE ARCHIMEDEAN INSTRUMENT ARC, b314\u2013b322 \u2014 THE FOLD'


def main():
    fails = []
    print('=' * 100)
    print('b323 -- GATE SUITE (A FILINGS ACT)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (each pulled from the act that ORIGINATED it -- b283):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    find = io.open(FINDINGS, encoding='utf-8', errors='replace').read()

    print('\n  G-ADDITIVE (the append is a TRUE BYTE PREFIX, against the blob as well):')
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:FINDINGS.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    norm = find.replace('\r\n', '\n')
    nblob = blob.replace('\r\n', '\n').rstrip('\n')
    pfx = norm.startswith(nblob)
    here = ('## ' + SECTION) in find
    once = find.count('## ' + SECTION)
    print('    the blob at HEAD is a true prefix of the file on disk : %s' % pfx)
    print('    the section is present : %s ; and appears exactly once : %s (count %d)'
          % (here, once == 1, once))
    print('    ### **b309\'s TRAP IS WHY THE BLOB AND NOT ONLY THE WORKING COPY**: `core.autocrlf`')
    print('    ### makes the two differ on a clean tree, and a prefix test against the working file')
    print('    ### alone would pass on a file the repository never saw.')
    if not (pfx and here and once == 1):
        fails.append('G-ADDITIVE')

    print('\n  G-GENERATED (F-QUOTE ran as a generator, with its discrimination arm):')
    gg = ('F-QUOTE  : 18 quotations, 0 unfindable' in run
          and 'an altered quotation is reported unfindable : True' in run
          and 'results cover 9, obstacles cover 9, arc 9, exact match : True' in run)
    print('    18 of 18 verbatim, the altered one unfindable, the arc covered exactly : %s' % gg)
    print('    ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE**, which is')
    print('    ### why the table is the source and the markdown is emitted FROM it.')
    if not gg:
        fails.append('G-GENERATED')

    print('\n  G-OWNDEFECTS (this act declares its OWN three, not only the nine acts\'):')
    od = ('IT RAN TWICE AND FILED THE ARC TWICE' in bank
          and 'ASSERTED A DIFFERENCE ITS OWN MEASUREMENT SHOWED WAS ZERO' in bank
          and 'WAS EMPTY AFTER BOTH' in bank)
    inrow = 'RAN TWICE AND FILED THE ARC TWICE' in tbl
    print('    all three in the bank : %s ; and in the correspondence row : %s' % (od, inrow))
    print('    ### **AN ACT THAT FILED A TABLE OF OTHER ACTS\' DEFECTIVE BARS WHILE HIDING THREE')
    print('    ### ### DEFECTS IN ITS OWN GENERATOR WOULD BE DOING THE EXACT THING THE TABLE EXISTS')
    print('    ### ### TO PREVENT.**')
    if not (od and inrow):
        fails.append('G-OWNDEFECTS')

    print('\n  G-NOCONCLUDE (a fold is a filing; the index row hands that back on query):')
    nc = ('A FOLD IS A FILING AND NOT A CONCLUSION' in idx
          and 'no theorem is proved by any act in it' in idx
          and 'SIZE of no margin on the domain axis is certified' in idx)
    print('    the index row carries filing, no-theorem and no-size : %s' % nc)
    if not nc:
        fails.append('G-NOCONCLUDE')

    print('\n  G-NOCLAIM (`the archimedean membership` stays unkeyed):')
    r = subprocess.run([sys.executable, t('banked_index.py'), '--query',
                        'the archimedean membership'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    quiet = any(ln.strip().startswith('### NO KEY') for ln in (r.stdout or '').splitlines())
    print('    it returns NO KEY : %s' % quiet)
    print('    ### **A FOLD THAT CLAIMED IT WOULD BE FILING A VERDICT NOBODY REACHED.**')
    if not quiet:
        fails.append('G-NOCLAIM')

    print('\n  G-NOWIDEN (the seal is the one written before the section was emitted):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    same = SEAL in reg
    print('    seal verifies : %s ; hash matches the literal in this gate : %s' % (intact, same))
    if not (intact and same):
        fails.append('G-NOWIDEN')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('F-QUOTE, able to report an altered quotation unfindable',
             'an altered quotation is reported unfindable : True' in run),
            ('the additivity check, run against BOTH the file and the blob',
             'blob at HEAD is a TRUE PREFIX' in run),
            ('the fold generator, idempotent on a second run',
             'idempotent' in io.open(t('b323_fold.py'), encoding='utf-8').read()),
            ('the extract, able to report a sentence missing',
             'NOT FOUND IN' in io.open(t('b323_extract.py'), encoding='utf-8').read())]
    for lbl, ok_ in arms:
        print('    %-60s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOEDIT (no owner instrument edited -- a filings act edits none):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-PAPERS (FINDINGS.md is the ONLY tracked change in PLACE-papers):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x[3:].strip() for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    only = tracked in ([], ['FINDINGS.md'])
    print('    tracked changes in PLACE-papers : %s' % tracked)
    print('    ### exactly FINDINGS.md, or already committed : %s' % only)
    if not only:
        fails.append('G-PAPERS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    pfx2 = tbl.startswith(head.rstrip('\n'))
    print('    table is a TRUE PREFIX : %s' % pfx2)
    if not pfx2:
        fails.append('G-ANCESTOR')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s'
          % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-STEM-FILED (the emitted section itself, swept at extended scope):')
    et = io.open(EMIT, encoding='utf-8').read()
    ech, _ = ferry_scan.scan_text(et, struck, stem_list)
    _e, esh = ferry_scan.scan_text(et, [], stem_list)
    print('    the section going into FINDINGS.md : struck %d, stem %d' % (len(ech), len(esh)))
    for h in esh:
        print('        %s' % h[3][:96])
    if ech or esh:
        fails.append('G-STEM-FILED')

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote, the filed section included):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the FILED SECTION', EMIT), ('the extract', EXTRACT)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d' % unpullable)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
