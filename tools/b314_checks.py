# -*- coding: utf-8 -*-
"""b314_checks.py -- THE GATE SUITE FOR A FILING AND A CERTIFICATION TEST.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-NOREPAIR`** ### -- the act found ninety-one uncertified terminals and repaired
###     nothing. ### Its must-fail fixtures are the sentences an act that had quietly become a
###     BUILD would have written.
###   ### **`G-NOLEAN`** ### -- `.lean` files untouched in both tracked repositories, and
###     `AllPrints.lean` byte-identical to `git HEAD`. ### **THE CERTIFICATION FILE IS THE ONE FILE
###     ### AN ACT LIKE THIS IS MOST LIKELY TO EDIT WITHOUT NOTICING IT HAS.**
###   ### **`G-ADDITIVE`** ### -- both touched ledgers changed with ZERO lines deleted, measured by
###     `numstat`. ### **A FOLD THAT DELETES A LINE IS A FOLD THAT MOVED A GRADE.**
###   ### **`G-ERRATA`** ### -- the entry written, READ BACK from the file, its ID taken from what
###     the file holds, and the owner instrument files byte-identical before and after.
### ### **AND `G-NOARCHNUM` IS NOT IN THIS SUITE AND NEITHER IS `G-NOFIT`.** ### They were b311's,
### b312's and b313's, and a gate copied forward without asking what this act does would fail it
### for doing what it was told.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b302_kernel as KRN  # noqa: E402

D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS_UNTOUCHED = ['tools/e16/qeps_layer.py', 'tools/e16/b38_act10.py',
                    'tools/e16/b264_eps_decay.py', 'tools/e16/carto_atlas.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b314_the_fold_and_the_cold_clone.txt')
REG = d('b314_registration_2026-09-03.txt')
FOLDRUN = d('b314_fold_run.txt')
EMIT = d('b314_fold_emitted.md')
CCRUN = d('b314_coldclone_run.txt')
CRRUN = d('b314_coldrelay_run.txt')
ERRUN = d('b314_errata_run.txt')
SCAN = d('b314_ferry_scan.txt')
FERRY = d('b314_ferry_2026-09-03.txt')
CENSUS = d('b314_census.txt')

OWNED = [FOLDRUN, EMIT, CCRUN, CRRUN, ERRUN, CENSUS,
         d('b314_corr_row.txt'), d('b314_index_query.txt'), d('b314_index_run.txt'),
         d('b314_pins_stepzero.txt'), d('b314_regspec_run.txt'), d('b314_satisfiable.json'),
         t('b314_regspec.py'), t('b314_correspondence.py'), t('b314_fold.py'),
         t('b314_coldclone.py'), t('b314_coldrelay.py'), t('b314_errata.py')]

CARRIERS = [
    (t('b314_checks.py'), 'its own fixtures'),
    (t('b314_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("b307 -- the census that licensed a struck phrase", d('b307_the_fold.txt'),
     'BEFORE: 26 MISSING -- TEN ACTS, FOURTEEN LIVE WORK-ORDERS'),
    ("### b307 -- and the emitter discipline it re-learned", d('b307_the_fold.txt'),
     'QUOTATION OF A QUOTATION IS NOT A SOURCE'),
    ("b308 -- the model a point, the instrument a plane",
     d('b308_the_local_field_instrument.txt'),
     'THE MODEL IS THE POINT `r = s = n`. ### THE INSTRUMENT IS THE PLANE.'),
    ("### b308 -- and the artifact retired for it alone",
     d('b308_the_local_field_instrument.txt'), 'IT IS NOT RETIRED FOR THE MODEL.'),
    ("b309 -- the value", d('b309_the_scaling_trace.txt'),
     'THE VALUE IS EXACTLY ZERO, AT EVERY NONZERO POWER, AT EVERY BANKED CELL'),
    ("### b309 -- and the operator that is alive while its trace is zero",
     d('b309_the_scaling_trace.txt'),
     'REGIME B: THE COMPRESSION IS ALIVE AND ITS TRACE IS ZERO'),
    ("b310 -- one surviving term, no arithmetic in it",
     d('b310_the_smear_collapses.txt'), 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION'),
    ("### b310 -- and its own refusal", d('b310_the_smear_collapses.txt'),
     'THIS ACT DERIVES NOTHING'),
    ("b311 -- the mechanism does not type at infinity",
     d('b311_the_identitys_neighbourhood.txt'), 'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE'),
    ("### b311 -- and the step at which it parts",
     d('b311_the_identitys_neighbourhood.txt'), 'THE DIMENSION OF THE OBJECT'),
    ("b312 -- the verdict", d('b312_the_remainder.txt'), 'NO. ### DIFFERENT.'),
    ("### b312 -- one identity, two conventions, one file", d('b312_the_remainder.txt'),
     'ONE IDENTITY, TWO CONVENTIONS, ONE FILE'),
    ("b313 -- the residue does not collapse", d('b313_the_exponent.txt'),
     'THE RESIDUE DOES NOT COLLAPSE'),
    ("### b313 -- and what it does not account for", d('b313_the_exponent.txt'),
     'IT DOES NOT ACCOUNT FOR THE REST'),
    ("the corpus's declared convention", e('qeps_layer.py'), 'the convention forced by the'),
    ("the identity's two sides in one file", e('b38_act10.py'), 'An[i] = math.sqrt(lamd)'),
    ("the atlas's calibrated sign", e('carto_atlas.py'), 'sign fixed BY the E2 calibration'),
    ("b264 -- the noise-floor work-order", d('b264_eps_even_decay.txt'), 'W-ORD-NTERM-FLOOR'),
    ("the E1 precedent -- the record does not overwrite itself", d('b265_filings.txt'),
     'THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF'),
    ("### and where that clause was discharged", d('b266_filings.txt'), 'E-2026-08-31-1'),
    ("the certification file is a hand-maintained import list",
     os.path.join(SIDE, 'AllPrints.lean'), 'imports every Core module'),
]

SELF_NEEDLES = [
    ('bank states the four findings up front', BANK, 'WHAT THIS ACT ESTABLISHED, FIRST'),
    ('bank gives the fold count', BANK, '14 QUOTATIONS, 0 UNFINDABLE'),
    ('bank gives the raw-byte result', BANK, 'RAW BYTE EQUALITY : True'),
    ('bank gives the coverage answer', BANK, 'FOUND, NOT NOT-FOUND'),
    ('bank names the errata id', BANK, 'E-2026-09-03-1'),
    ('### bank says what the act is not, first', BANK, 'NO GRADE MOVES. ### NO ACT IS'),
    ('bank declares what cold means', BANK, 'NOT A COLD MACHINE'),
    ('bank declares what cold does not mean', BANK, 'THE MACHINE IS THE SAME MACHINE'),
    ('bank shows the toolchain both ways', BANK, 'THE TWO LINES DIFFER'),
    ('bank gives the build result', BANK, '84 OF 84 ELABORATED FROM SOURCE'),
    ('bank gives the byte hazards', BANK, 'byte-order mark -- regenerated'),
    ('bank names the redundant wrappers as redundant', BANK, 'THEY ARE NOT THE FINDING'),
    ('bank says the uncertified modules are not broken', BANK, 'THEY ARE UNMENTIONED'),
    ('bank gives the structural reason', BANK, 'HAND-MAINTAINED IMPORT LIST'),
    ('bank ties it to the blinkered-check law', BANK, 'BECAUSE* IT IS BLINKERED'),
    ('bank reports the cold relay controls', BANK, 'THE FOUR CONTROLS, RUN IN THE CLONE'),
    ('### bank weakens its own pass where the pass is weak', BANK,
     'THE PASS IS REAL AND ITS REACH IS SMALLER THAN IT LOOKS'),
    ('### bank owns the guard that reported the wrong cause', BANK,
     'A GUARD THAT REPORTS THE WRONG CAUSE IS WORSE THAN NO GUARD'),
    ('bank gives the arc as one statement', BANK, 'THE ARC AS ONE STATEMENT'),
    ('bank bounds the arc statement', BANK, 'THE REST OF THE RESIDUE IS OWED'),
    ('bank names the hypothesis as a hypothesis', BANK, 'NAMED HERE AS A HYPOTHESIS'),
    ('bank keeps mechanized and judgement apart', BANK, 'MECHANIZED AND JUDGEMENT KEPT APART'),
    ('bank says why the separation matters', BANK, 'LIKE THE FIRST'),
    ('bank lists the exception-list law', BANK, 'AGREED NOT TO LOOK'),
    ('bank lists the zero-check law', BANK, 'CANNOT SEE A MULTIPLICATIVE FACTOR'),
    ('bank lists the unfinished-search law', BANK, 'STILL RUNNING'),
    ('bank lists the reported-failure law', BANK, 'FAILURE NOBODY HAS TO ACT ON'),
    ('bank gives the desk as one list', BANK, 'THE DESK, AS ONE LIST'),
    ('bank names the truncation as the central cost', BANK, 'THE TRUNCATION NOBODY OWNS'),
    ('bank names the two next reads', BANK, 'THE RATE RE-DERIVATION'),
    ('bank puts the patent clock as the dated item', BANK, 'THE ONE ITEM ON THIS DESK WITH A DATE'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank earns the HANDOFF licence and bounds it', BANK, 'AND FOR THAT LEDGER AND NO'),
    ('bank records the W2 ruling verbatim', BANK, 'RECORDED AND UNAPPLIED'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank files the kernel-coverage work-order', BANK, 'W-ORD-KERNEL-COVERAGE'),
    ('bank files the absolute-paths work-order', BANK, 'W-ORD-ABSOLUTE-PATHS'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration splits which half it precedes', REG, 'IT HAS ALREADY RUN ONCE'),
    ('registration records the ruling verbatim', REG, 'E1 pattern -- an internal-record'),
    ('registration caps lean files', REG, '`.lean` files created or edited'),
    ('registration caps additions to the certification file', REG,
     'modules added to the certification file'),
    ('registration says why the counts are not in it', REG,
     'RIGHT PLACE FOR A COUNT IS THE BANK'),
    ('the fold run reports the quotations', FOLDRUN, 'F-QUOTE  : 14 quotations, 0 unfindable'),
    ('the fold run reports the discrimination control', FOLDRUN,
     'an altered quotation is reported unfindable : True'),
    ('the fold run reports the additive measure', FOLDRUN, 'FINDINGS.md vs HEAD'),
    ('the emitted section carries the arc statement', EMIT, 'The arc as one statement'),
    ('the emitted section carries the scope', EMIT, 'Scope, printed beside it'),
    ('the cold-clone run reports zero pre-build artefacts', CCRUN,
     'COMPILED ARTEFACTS PRESENT IN THE CLONE BEFORE THE BUILD : 0'),
    ('the cold-clone run reports raw equality', CCRUN, 'RAW BYTE EQUALITY        : True'),
    ('the cold-clone run reports the coverage total', CCRUN,
     'NOT IN THE CERTIFICATION PROFILE : 91'),
    ('the cold-clone run reports zero failures', CCRUN, '### CHECKS FAILING : 0'),
    ('the errata run reports the id from the file', ERRUN, 'TAKEN FROM THE FILE : E-2026-09-03-1'),
    ('the errata run reports the owners untouched', ERRUN, 'BEFORE AND AFTER : True'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOREPAIR` -- WHAT AN ACT THAT HAD BECOME A BUILD WOULD HAVE WRITTEN.**
    ('no module is added to the certification file', BANK, 'THE MODULES ARE ADDED.'),
    ('the profile is not regenerated into the repository', BANK, 'THE PROFILE IS UPDATED.'),
    ('the uncertified terminals are not certified', BANK, 'THE TERMINALS ARE CERTIFIED.'),
    ('the uncertified terminals are not called wrong', BANK, 'THE TERMINALS ARE WRONG.'),
    ('the instrument is not repaired', BANK, 'THE ABSOLUTE PATHS ARE FIXED.'),
    # ### **THE FILING'S OWN REFUSALS.**
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b313 IS RE-VERDICTED.'),
    ('the fold is not promoted', BANK, 'THE ARC IS PROVED.'),
    ('no banked number is called wrong', BANK, 'THE BANKED NUMBERS ARE WRONG.'),
    ('the errata is not a retraction', BANK, 'THE DEPOSIT IS RETRACTED.'),
    # ### **THE COLD CLAIM'S OWN LIMIT.**
    ('the cold claim is not widened to the machine', BANK, 'THE MACHINE INHERITED NOTHING.'),
    ('reproduction is not claimed in general', BANK, 'THE CORPUS REPRODUCES FROM ANY CLONE.'),
    # ### **THE STANDING CAPS.**
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the ruling to be recorded is not applied', BANK, 'THE W2 VARIANT IS BUILT.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the fold's quotation counts and the additive measure", 'tools/b314_fold.py'),
    ("the clone, the build, the profile bytes and the coverage", 'tools/b314_coldclone.py'),
    ("the cold reproduction controls and the path counts", 'tools/b314_coldrelay.py'),
    ("the errata entry, its read-back and its ID", 'tools/b314_errata.py'),
    ("the normaliser and print counter the cold clone imports", 'tools/b302_kernel.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b314_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b314_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b314_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b314_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the mirror's three clauses", 'tools/mirror_verify.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b314' in x)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def numstat(repo, path):
    """### **THE BASELINE IS FOUND, NOT ASSUMED** -- b309 (D6), met a third time.

    ### A gate written as `git diff HEAD` measures a PENDING change, and on the far side of the
    ### commit it measures nothing and reports zero. ### **THAT IS NOT THE GATE PASSING; IT IS
    ### THE GATE MEANING SOMETHING ELSE**, and the order's *re-run the suite after the push* is
    ### exactly what surfaces it. ### So: if the path has an uncommitted change, measure that;
    ### otherwise measure what the LAST COMMIT did to it. ### **THE ANSWER IS THE SAME NUMBER ON
    ### BOTH SIDES OF THE COMMIT, WHICH IS THE ONLY WAY THE RE-RUN IS A CHECK.**
    """
    r = subprocess.run(['git', '-C', repo, 'diff', '--numstat', 'HEAD', '--', path],
                       capture_output=True, text=True)
    where = 'working tree vs HEAD'
    if not r.stdout.strip():
        r = subprocess.run(['git', '-C', repo, 'diff', '--numstat', 'HEAD~1', 'HEAD',
                            '--', path], capture_output=True, text=True)
        where = 'HEAD~1 vs HEAD'
    if not r.stdout.strip():
        return 0, 0, where
    q = r.stdout.split()
    return int(q[0]), int(q[1]), where


def main():
    fails = []
    print('=' * 100)
    print('b314 -- GATE SUITE (A FILING AND A CERTIFICATION TEST)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (pulled from emitting files):')
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
    print('    ### **THE FIRST FIVE ARE `G-NOREPAIR`: the sentences an act that had quietly become')
    print('    ### a BUILD would have written. ### THAT IS THE LARGEST SCOPE BREACH THIS ACT HAD')
    print('    ### AVAILABLE TO IT.**')

    bank = io.open(BANK, encoding='utf-8').read()
    foldrun = io.open(FOLDRUN, encoding='utf-8').read()
    ccrun = io.open(CCRUN, encoding='utf-8').read()
    errun = io.open(ERRUN, encoding='utf-8').read()

    # ### G-FOLD.
    print('\n  G-FOLD (the emitter\'s five falsifiers, from its own log):')
    fs = re.findall(r'F-\w+\s+\([^)]*\)\s*:\s*### \*\*(DID NOT FIRE|FIRED)\*\*', foldrun)
    print('    falsifier verdicts : %s' % fs)
    okf = (len(fs) == 5 and all(x == 'DID NOT FIRE' for x in fs))
    print('    all five DID NOT FIRE : %s' % okf)
    if not okf:
        fails.append('G-FOLD')

    # ### G-ADDITIVE.
    print('\n  G-ADDITIVE (both touched ledgers changed with ZERO lines deleted):')
    fa, fd, fw = numstat(PP, 'FINDINGS.md')
    ea, ed, ew = numstat(PP, 'ERRATA.md')
    print('    FINDINGS.md +%d / -%d  [%s] ; ERRATA.md +%d / -%d  [%s]'
          % (fa, fd, fw, ea, ed, ew))
    print('    ### **THE BASELINE IS FOUND, NOT ASSUMED** -- so the measurement is the same')
    print('    ### number before and after the commit, which is the only way the re-run is a')
    print('    ### check. ### b309 (D6), met a third time.')
    oka = (fd == 0 and ed == 0 and fa > 0 and ea > 0)
    print('    purely additive : %s' % oka)
    print('    ### **A FOLD THAT DELETES A LINE IS A FOLD THAT MOVED A GRADE**, and this is the')
    print('    ### measurement rather than the assertion.')
    if not oka:
        fails.append('G-ADDITIVE')

    # ### G-NOLEAN.
    print('\n  G-NOLEAN (nothing built; the certification file byte-identical to HEAD):')
    l1 = subprocess.run(['git', '-C', ROOT, 'status', '--short', '--', '*.lean'],
                        capture_output=True, text=True).stdout.strip()
    l2 = subprocess.run(['git', '-C', SIDE, 'status', '--short', '--', '*.lean'],
                        capture_output=True, text=True).stdout.strip()
    allp_now = KRN.normalise(io.open(os.path.join(SIDE, 'AllPrints.lean'), 'rb').read())
    allp_head = KRN.normalise(KRN.git_show('AllPrints.lean') or b'')
    prof_now = KRN.normalise(io.open(os.path.join(SIDE, 'AXIOM_PRINTS.txt'), 'rb').read())
    prof_head = KRN.normalise(KRN.git_show('AXIOM_PRINTS.txt') or b'')
    print('    `.lean` changed -- relay : %r ; SIDE : %r' % (l1, l2))
    print('    AllPrints.lean identical to HEAD : %s' % (allp_now == allp_head))
    print('    AXIOM_PRINTS.txt identical to HEAD : %s' % (prof_now == prof_head))
    okl = (not l1 and not l2 and allp_now == allp_head and prof_now == prof_head)
    if not okl:
        fails.append('G-NOLEAN')

    # ### G-OWNER-UNTOUCHED.
    print('\n  G-OWNER-UNTOUCHED (the instrument files the errata entry says are untouched):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS_UNTOUCHED,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    if dirty:
        fails.append('G-OWNER-UNTOUCHED')

    # ### G-COLD.
    print('\n  G-COLDPIN / G-COLDTOOL / G-COLDBYTES / G-COVERAGE (from the cold-clone log):')
    ccj = json.load(io.open(d('b314_coldclone_rows.json'), encoding='utf-8'))
    print('    at the pin : %s ; pre-build artefacts : %d ; toolchain in/out differ : %s'
          % (ccj['head'] == ccj['remote'], ccj['pre_oleans'],
             ccj['lean_in'] != ccj['lean_out']))
    print('    built %d, errors %s ; RAW equal : %s ; NORMALISED equal : %s ; differing lines : %d'
          % (ccj['built'], ccj['build_errors'], ccj['raw_same'], ccj['norm_same'],
             ccj['diff_lines']))
    print('    coverage: %d modules outside, %d uncertified targets'
          % (ccj['outside'], ccj['uncertified']))
    okc = (ccj['head'] == ccj['remote'] and ccj['pre_oleans'] == 0
           and ccj['lean_in'] != ccj['lean_out'] and ccj['raw_same'] and ccj['norm_same']
           and ccj['diff_lines'] == 0 and not ccj['build_errors'] and not ccj['fails'])
    print('    ### **ALL FOUR COLD ARMS : %s**' % okc)
    if not okc:
        fails.append('G-COLD*')

    # ### G-COLDRELAY.
    print('\n  G-COLDRELAY (the reproduction controls, cold):')
    crp = d('b314_coldrelay_rows.json')
    if os.path.exists(crp):
        crj = json.load(io.open(crp, encoding='utf-8'))
        rcs = [(r['script'], r['rc']) for r in crj['controls']]
        print('    controls and exit codes : %s' % rcs)
        print('    corpus tracked state unchanged by the run : %s' % crj['corpus_unchanged'])
        print('    instrument files carrying an absolute corpus path : %d'
              % len(crj['e16_hardcoded']))
        okr = all(rc == 0 for _s, rc in rcs) and crj['corpus_unchanged'] and not crj['fails']
        print('    ### **ALL CONTROLS PASSED COLD : %s**' % okr)
        if not okr:
            fails.append('G-COLDRELAY')
    else:
        fails.append('G-COLDRELAY (no log)')
        print('    ### THE COLD-RELAY LOG IS NOT PRESENT.')

    # ### G-ERRATA.
    print('\n  G-ERRATA (written, read back, ID from the file, owners byte-identical):')
    okе = ('TAKEN FROM THE FILE : E-2026-09-03-1' in errun
           and 'BEFORE AND AFTER : True' in errun
           and 'every ID unique : True' in errun
           and errun.count('PASS') >= 6)
    print('    id read back, owners identical, clauses located : %s' % okе)
    if not okе:
        fails.append('G-ERRATA')

    # ### G-ANCESTOR.
    print('\n  G-ANCESTOR (the correspondence table is a TRUE PREFIX of its banked self):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    print('    true prefix : %s' % pfx)
    if not pfx:
        fails.append('G-ANCESTOR')

    # ### G-STRUCK / G-STEM.
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
    print('    ### **AN EXCEPTION LIST IS A LIST OF PLACES A CHECK HAS AGREED NOT TO LOOK**, and')
    print('    ### this one is printed with its reasons rather than filtered silently.')
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    if not intact:
        fails.append('G-SEAL')

    HEDGE_EXEMPT = {
        BANK: ('IT MAY NOT CONCLUDE THAT THE UNCERTIFIED TERMINALS ARE WRONG, OR RIGHT.', [
            'the bank QUOTES the sealed sentence in order to DECLARE the exemption, which is',
            'exactly the carrier species the struck-clause scan already recognises: a document',
            'that quotes a flagged sentence to name it carries the flag.',
            '### **AND SUPPRESSING THE QUOTATION TO QUIET THE AUDIT WOULD HIDE THE EXEMPTION',
            '### THE AUDIT EXISTS TO MAKE VISIBLE.**',
        ]),
        REG: ('IT MAY NOT CONCLUDE THAT THE UNCERTIFIED TERMINALS ARE WRONG, OR RIGHT.', [
            'the tool reads `UNCERTIFIED` as a GRADE TOKEN, where the sentence uses it as an',
            'ADJECTIVE for the terminals; and it reads `may not` as a HEDGE STEM, where the',
            "sentence uses it as a PROHIBITION. ### The tool s own header says every count",
            'reports is a count of SHAPES, not of FAULTS.',
            '### **AND THE FILE IS SEALED: THE SEAL IS NOT EDITED TO MAKE A SHAPE CHECK QUIET.**',
        ]),
    }
    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG),
                      ('the emitted section', EMIT)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            # ### ### **ONE DECLARED EXEMPTION, WITH ITS REASON, AND IT IS THE ONLY ONE.**
            # ### **AN EXCEPTION LIST IS A LIST OF PLACES A CHECK HAS AGREED NOT TO LOOK** --
            # ### this act's own lore section says so -- so the exempt sentence is QUOTED, the
            # ### flag count must be EXACTLY one, and the SEALED file is not edited to make a
            # ### mechanical shape check quiet.
            exempt = HEDGE_EXEMPT.get(path)
            for x in gh:
                print('        FLAGGED: %s' % str(x)[:96])
            matched = bool(exempt) and len(gh) == 1 and exempt[0] in str(gh[0])
            if matched:
                print('        ### **DECLARED EXEMPTION, AND IT IS THE ONLY ONE:**')
                for chunk in exempt[1]:
                    print('        ### %s' % chunk)
            else:
                fails.append('graded hedges in %s' % lbl)

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 12
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL)))
    print('    declared carriers %d   toolnum rows %d' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
