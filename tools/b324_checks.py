# -*- coding: utf-8 -*-
"""b324_checks.py -- THE GATE SUITE FOR A READS ACT WITH TWO DEFINITIONAL VERDICTS.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NORESEMBLE`** ### -- ### **THE ONE THIS ACT WOULD MOST EASILY HAVE BREACHED.**
###     The order refuses resemblance BY NAME. ### This arm requires the bank to carry the refusal,
###     the operational test, and -- decisively -- the SEVEN-CONSTITUENT table, so that a reader can
###     see the verdict does not rest on a word both records use.
###   ### ### **`G-NOTMOVED`** ### -- the wall verdict came back DIFFERENT, so ### **THE ACT MAY NOT
###     ### SAY THE ARC MOVED THE WALL**, and must say the second half of (F1) does not arise.
###   ### ### **`G-DEPOSIT`** ### -- ### **NO FILE UNDER `outputs/DEPOSITED-v1.1.2/` IS WRITTEN.**
###     Measured by `git status` over that path, not promised.
###   ### **`G-APPEND`** ### -- both keystones append-only, against the working file AND the blob.
###   ### **`G-PROVENANCE`** ### -- the phrase census ran, and the bank carries the finding that the
###     wall's naming is INTERNAL rather than deposited.
###   ### **`G-NORECOMMEND`** ### -- the wave's candidate list is TYPED, not ranked.
###   ### **`G-OWNDEFECT`** ### -- b323's fourth defect recurred here and the bank says so.
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
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')

OWNERS = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
          'tools/b319_stable.py', 'tools/b320_weil.py', 'tools/b321_window.py',
          'tools/b322_ladder.py', 'tools/b323_fold.py', 'tools/noise_floor.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b324_the_keystones_reread.txt')
REG = d('b324_registration_2026-09-04.txt')
RUN = d('b324_reread_run.txt')
FIL = d('b324_filings_run.txt')
EXTRACT = d('b324_extract_notes.txt')
SCAN = d('b324_ferry_scan.txt')
FERRY = d('b324_ferry_2026-09-04.txt')
CENSUS = d('b324_census.txt')

OWNED = [RUN, FIL, CENSUS, EXTRACT, d('b324_filings_rerun.txt'), d('b324_index_run.txt'),
         d('b324_pins_stepzero.txt'), d('b324_regspec_run.txt'), d('b324_reg_termscan.txt'),
         d('b324_satisfiable.json'), d('b324_satisfiable_run.txt'),
         t('b324_regspec.py'), t('b324_correspondence.py'), t('b324_reread.py'),
         t('b324_filings.py'), t('b324_extract.py')]

CARRIERS = [
    (t('b324_checks.py'), 'its own fixtures'),
    (t('b324_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("the wall, at the residue keystone", RESIDUE, 'The space is the wall'),
    ("### and the object the two eras cross at", RESIDUE, 'the positive space on the zeros'),
    ("### and the arc's source, already graded there", RESIDUE, 'reduces RH to a Weil positivity'),
    ("the margin, at the balance keystone", BALANCE, 'is the margin in the inequality'),
    ("### its positivity and its minimum", BALANCE, 'stays positive throughout'),
    ("### and the channel that is not eventually positive", BALANCE,
     'The differential channel is not eventually positive'),
    ("the fifth register, AT THE VERIFIED DEPOSIT COPY",
     os.path.join(DEPOSIT, 'A_Place_to_Stand.md'), 'no positive pairing is known'),
    ("### the fourth register's channel inequality, at the deposit",
     os.path.join(DEPOSIT, 'A_Place_to_Stand.md'), 'the premise is the inequality'),
    ("### ### and the equivalences the deposit DELIBERATELY does not compile",
     os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
     'deliberately **not** compiling the cross-register equivalences'),
    ("### h2's three classical faces", os.path.join(DEPOSIT, 'A_Place_to_Stand.md'),
     'The obligation h2 is, in each of the classical faces'),
    ("spectral inertness, at the deposit", os.path.join(DEPOSIT, 'Spectral_Inertness.md'),
     'spectrally inert'),
    ("the confinement keystone, at the deposit",
     os.path.join(DEPOSIT, 'Which_Structure_Confines.md'),
     'it does not confine zeros to it'),
    ("b323 -- the fold this act was named next by", d('b323_the_fold.txt'),
     'THE KEYSTONE RE-READ'),
    ("b320 -- the margins this act compares", d('b320_the_lawful_function.txt'), 'VERDICT : HOLDS'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### bank gives the wall verdict', BANK, 'THE WALL: ### DIFFERENT'),
    ('### and reports the expectation refuted', BANK, '(F1) IS REFUTED'),
    ('### and declines the question its answer removed', BANK,
     'THE SECOND HALF OF (F1) DOES NOT ARISE'),
    ('### and that the keystone had already graded the source', BANK,
     'STALL AT THE REALIZATION CLAUSE'),
    ('### bank gives the margin verdict', BANK, 'THE MARGIN: ### UNDECIDED'),
    ('### and that the deposit withholds the bridge deliberately', BANK,
     'THE DEPOSIT DELIBERATELY WITHHOLDS IT'),
    ('### and the distinction that keeps it honest', BANK,
     'EQUIVALENCE OF THE OBLIGATIONS IS NOT'),
    ('### and types the owed statement', BANK, 'THE BRIDGING STATEMENT, TYPED'),
    ('### bank reports the provenance finding', BANK,
     'APPEARS ZERO TIMES IN THE DEPOSITED MONOGRAPH'),
    ('bank gives the contact tally', BANK, '3 CORROBORATED, 4 UNTOUCHED, 0 IN TENSION'),
    ('### and refuses to read the zero as a relief', BANK,
     'AND THE ZERO IS REPORTED AS A MEASUREMENT AND NOT AS A RELIEF'),
    ('### bank reports the deposit byte-unchanged', BANK, 'THE DEPOSIT IS BYTE-UNCHANGED'),
    ('### bank reports its own recurrence of b323 defect four', BANK,
     "b323's FOURTH DEFECT RECURRED IN THIS ACT'S OWN TOOL"),
    ('### and the structural fix', BANK, 'THE TWO PATHS NOW WRITE TO TWO FILES'),
    ('bank lists the drives before concluding', BANK, 'F: IS NOT MOUNTED THIS SESSION'),
    ('### and names the copy refused', BANK, 'THE PROJECT MIRROR'),
    ('bank refuses to recommend', BANK, 'IT RECOMMENDS NOTHING'),
    ('bank gives the filings', BANK, 'COMPONENT 4 -- THE FILINGS'),
    ('### with the wave list typed', BANK, 'REFINEMENT-OF-DEPOSITED'),
    ("### and the wave as the author's", BANK, 'THE WAVE IS THE AUTHOR'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### and hands on the Epstein test', BANK, 'Epstein'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('registration names the act', REG, 'THE KEYSTONES RE-READ'),
    ('the run gives the wall verdict', RUN, 'VERDICT -- THE WALL : DIFFERENT'),
    ('the run gives the margin verdict', RUN, 'VERDICT -- THE MARGIN : UNDECIDED'),
    ('the run names the first differing constituent', RUN, 'FIRST DIFFERING CONSTITUENT'),
    ('the run gives the contact tally', RUN, 'THE TALLY'),
    ('the run reports zero checks failing', RUN, 'CHECKS FAILING : 0'),
    ('the filings report append-only', FIL, 'APPEND-ONLY : True'),
    ('### and the deposit byte-unchanged', FIL, 'THE DEPOSIT IS BYTE-UNCHANGED : True'),
    ('### and zero filing failures', FIL, 'FILING CHECKS FAILING : 0'),
    ('the extract found every quotation', EXTRACT, 'QUOTATIONS NOT FOUND : 0'),
    ('### and every path', EXTRACT, 'PATHS NOT PRESENT : 0'),
]

MUST_FAIL = [
    # ### **`G-NOTMOVED` -- the sentences the act may not write.**
    ('the arc did not move the wall', BANK, 'THE ARC MOVED THE WALL.'),
    ('the spaces are not called the same', BANK, 'THE TWO SPACES ARE THE SAME.'),
    ('the wall is not called crossed', BANK, 'THE WALL IS CROSSED.'),
    # ### **`G-NORESEMBLE`.**
    ('no verdict rests on a shared word', BANK, 'THEY BOTH SAY SPACE.'),
    ('the margins are not called the same', BANK, 'THE TWO MARGINS ARE ONE OBJECT.'),
    ('the bridge is not supplied', BANK, 'THE BRIDGE IS DERIVED.'),
    # ### **`G-DEPOSIT` and the filing caps.**
    ('no deposited text is edited', BANK, 'THE DEPOSIT IS EDITED.'),
    ('no keystone claim is altered', BANK, "THE KEYSTONE'S CLAIM IS CORRECTED."),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b300 IS RE-VERDICTED.'),
    ('b322 is not re-verdicted', BANK, 'b322 IS RE-VERDICTED.'),
    # ### **`G-NORECOMMEND`.**
    ('the wave is not started', BANK, 'THE WAVE IS STARTED.'),
    ('nothing is recommended', BANK, 'THE RECOMMENDED NEXT ACT IS THE EPSTEIN TEST.'),
    # ### **THE STANDING CAPS.**
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
]

TOOLNUM = [
    ("the two verdicts and their constituent tables", 'tools/b324_reread.py'),
    ("the append-only filings and their prefix checks", 'tools/b324_filings.py'),
    ("the quotations, the phrase census and the drives", 'tools/b324_extract.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b324_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b324_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b324_correspondence.py'),
    ("the index key's read-back arms", 'tools/b324_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b324' in x)

SEAL = '767a15700973c4b146a38cdf230c2bdb6461c711f1e5f1e0f3244928a02b99de'


def main():
    fails = []
    print('=' * 100)
    print('b324 -- GATE SUITE (A READS ACT WITH TWO DEFINITIONAL VERDICTS)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it; the deposit at its VERIFIED copy):')
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
    fil = io.open(FIL, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    ext = io.open(EXTRACT, encoding='utf-8').read()

    print('\n  G-NORESEMBLE (no verdict rests on a shared word):')
    nr = ('RESTS ON NO SHARED WORD' in tbl
          and 'resemblance argument' in bank
          and 'THE SEVEN CONSTITUENTS' in bank)
    tabled = run.count('DIFFERS') >= 12
    print('    the bank carries the refusal and the operational test : %s' % nr)
    print('    ### and the constituent tables are in the run (%d DIFFERS rows) : %s'
          % (run.count('DIFFERS'), tabled))
    print('    ### **BOTH RECORDS WRITE "SPACE". ### THE VERDICT DOES NOT REST ON IT** -- it rests')
    print('    ### on seven constituents, and a reader can check every one.')
    if not (nr and tabled):
        fails.append('G-NORESEMBLE')

    print('\n  G-NOTMOVED (the wall verdict was DIFFERENT, so the arc did not move it):')
    nm = ('VERDICT -- THE WALL : DIFFERENT' in run
          and 'THE SECOND HALF OF (F1) DOES NOT ARISE' in bank
          and 'THE ARC DID NOT MOVE' in idx)
    print('    run, bank and INDEX ROW all carry it : %s' % nm)
    print('    ### **THE INDEX ROW IS WHERE A LATER READER ARRIVES FIRST.**')
    if not nm:
        fails.append('G-NOTMOVED')

    print('\n  G-DEPOSIT (no file under outputs/DEPOSITED-v1.1.2/ is written):')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain',
                         'outputs/DEPOSITED-v1.1.2'], capture_output=True, text=True).stdout.strip()
    print('    git status over the deposit path : %r' % st)
    print('    ### ### **BYTE-UNCHANGED : %s**' % (not st))
    if st:
        fails.append('G-DEPOSIT')

    print('\n  G-APPEND (both keystones append-only, against the file AND the blob):')
    ok_all = True
    for rel in ('phase1.5/proofs/THE_RESIDUE_OF_RH.md',
                'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'):
        blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel],
                              capture_output=True).stdout.decode('utf-8', 'replace')
        now = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        pfx = now.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
        once = now.count('<!-- b324 cross-reference -->')
        print('    %-46s blob is a TRUE PREFIX : %s ; block appears %d time(s)'
              % (rel, pfx, once))
        ok_all = ok_all and pfx and once == 1
    if not ok_all:
        fails.append('G-APPEND')

    print('\n  G-PROVENANCE (the phrase census ran and the finding is in the bank):')
    pv = ('THE PHRASE CENSUS' in ext
          and 'APPEARS ZERO TIMES IN THE DEPOSITED MONOGRAPH' in bank
          and 'INTERNAL' in ext)
    print('    census in the extract, finding in the bank : %s' % pv)
    print('    ### **A CLAIM THAT LIVES ONLY INTERNALLY CANNOT BE REFINED FROM THE DEPOSIT**, and')
    print('    ### this is the measurement that stopped the act from saying otherwise.')
    if not pv:
        fails.append('G-PROVENANCE')

    print('\n  G-NORECOMMEND (the wave list is typed, not ranked):')
    nrc = ('IT RECOMMENDS NOTHING' in bank and 'THE WAVE IS THE AUTHOR' in bank
           and 'NO RECOMMENDATION' in bank)
    print('    the bank refuses to recommend and says the wave is the author\'s : %s' % nrc)
    if not nrc:
        fails.append('G-NORECOMMEND')

    print('\n  G-OWNDEFECT (b323\'s fourth defect recurred here and the bank says so):')
    od = ("b323's FOURTH DEFECT RECURRED IN THIS ACT'S OWN TOOL" in bank
          and 'THE TWO PATHS NOW WRITE TO TWO FILES' in bank
          and os.path.exists(d('b324_filings_rerun.txt')))
    print('    declared, fixed structurally, and both records exist on disk : %s' % od)
    print('    ### **A LESSON FILED IN A BANK AND NOT BUILT INTO A TOOL IS A LESSON THAT WILL BE')
    print('    ### ### LEARNED AGAIN** -- one act between the filing and the repetition.')
    if not od:
        fails.append('G-OWNDEFECT')

    print('\n  G-NOWIDEN (the seal is the one written before any verdict):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    same = SEAL in reg
    print('    seal verifies : %s ; hash matches the literal in this gate : %s' % (intact, same))
    if not (intact and same):
        fails.append('G-NOWIDEN')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the phrase census, able to return INTERNAL', 'INTERNAL' in ext),
            ('### and able to return DEPOSITED', 'DEPOSITED' in ext),
            ('the verdict, computed from the table not typed',
             'def verdict' in io.open(t('b324_reread.py'), encoding='utf-8').read()),
            ('the filing tool, able to REFUSE a deposited target',
             'REFUSED -- deposited path targeted' in io.open(t('b324_filings.py'),
                                                             encoding='utf-8').read()),
            ('the filings, idempotent on a second run', 'ALREADY FILED' in
             io.open(d('b324_filings_rerun.txt'), encoding='utf-8').read()
             if os.path.exists(d('b324_filings_rerun.txt')) else False)]
    for lbl, ok_ in arms:
        print('    %-58s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOEDIT (no owner instrument edited -- a reads act edits none):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-PAPERS (only the two keystones changed in PLACE-papers):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = sorted(x[3:].strip() for x in pp.splitlines()
                     if x.strip() and not x.startswith('??'))
    allowed = sorted(['phase1.5/proofs/THE_RESIDUE_OF_RH.md',
                      'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'])
    only = tracked in ([], allowed)
    print('    tracked changes : %s' % tracked)
    print('    ### exactly the two keystones, or already committed : %s' % only)
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

    print('\n  G-STEM-APPENDED (the two appended blocks, swept):')
    for rel in ('phase1.5/proofs/THE_RESIDUE_OF_RH.md',
                'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'):
        txt = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        blk = txt[txt.index('<!-- b324 cross-reference -->'):] \
            if '<!-- b324 cross-reference -->' in txt else ''
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-46s struck : %d   stem : %d' % (rel, len(ch), len(sh)))
        for h in sh:
            print('        %s' % h[3][:92])
        if ch or sh:
            fails.append('G-STEM-APPENDED')

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

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN),
                      ('the filings', FIL), ('the extract', EXTRACT)]:
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
