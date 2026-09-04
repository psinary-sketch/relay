# -*- coding: utf-8 -*-
"""b313_checks.py -- THE GATE SUITE FOR A COMPUTATION THAT CHANGED AN INSTRUMENT IN A COPY.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### **`G-OWNER-UNTOUCHED`** ### -- the three owner files byte-identical to `git HEAD`,
###     normalised. ### **CHECKED AFTER THE RUN AND NOT BEFORE IT**: a file is edited by running
###     things, not by planning to.
###   ### **`G-ROUNDTRIP` / `G-DIFF` / `G-CONTROL` / `G-STRUCTURE`** ### -- the four measurements
###     that make a second column a statement about the exponent rather than about the copying.
###   ### **`G-NOFIT`** ### -- ### **THE ONE THAT GUARDS THE DIFFERENCE BETWEEN THIS ACT AND A
###     ### TUNING EXERCISE.** ### Its must-fail fixtures are the sentences an act that kept a flip
###     because the residue improved would have written.
###   ### **`G-NOISEFLOOR`** ### -- the ladder's gate is in the path and what it removes is printed.
### ### **AND `G-NOARCHNUM` IS NOT IN THIS SUITE, DELIBERATELY.** ### b311 and b312 forbade
### computing an archimedean number; ### **THIS ACT IS ORDERED TO COMPUTE ONE.** ### A gate copied
### forward uninverted would have failed this act for doing what it was told.
"""
import io
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
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS_UNTOUCHED = ['tools/e16/qeps_layer.py', 'tools/e16/b38_act10.py',
                    'tools/e16/b264_eps_decay.py', 'tools/e16/carto_atlas.py',
                    'data/b38_2026-08-18.txt', 'data/b264_rows.json']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def e(n):
    return os.path.join(E16, n)


BANK = d('b313_the_exponent.txt')
REG = d('b313_registration_2026-09-03.txt')
RUN = d('b313_components_run.txt')
FLIPLOG = d('b313_flip_run.txt')
SCAN = d('b313_ferry_scan.txt')
FERRY = d('b313_ferry_2026-09-03.txt')
CENSUS = d('b313_census.txt')

OWNED = [RUN, FLIPLOG, CENSUS, d('b313_corr_row.txt'), d('b313_index_query.txt'),
         d('b313_index_run.txt'), d('b313_pins_stepzero.txt'), d('b313_regspec_run.txt'),
         d('b313_satisfiable.json'), d('b313_source_recheck.txt'),
         t('b313_regspec.py'), t('b313_correspondence.py'), t('b313_flip.py'), t('b313_run.py')]

CARRIERS = [
    (t('b313_checks.py'), 'its own fixtures'),
    (t('b313_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("b176 -- the act that imported the remainder, naming the citation",
     d('b176_seam_and_reads.txt'), 'The corpus cites eps as "their (85)"'),
    ("### b176 -- and quoting the source's own rho^{1/2}",
     d('b176_seam_and_reads.txt'), 'k(rho) = rho^{1/2} INT_0^inf xi(x) zeta(rho x) dx'),
    ("### b176 -- what it DID check", d('b176_seam_and_reads.txt'),
     'ALL THREE TERMS AGREE EXACTLY'),
    ("### b176 -- and what it said it had NOT", d('b176_seam_and_reads.txt'),
     "IT DOES NOT CHECK THAT THE CORPUS"),
    ("the corpus's header convention", e('qeps_layer.py'), 'the convention forced by the'),
    ("### the corpus's remainder line", e('qeps_layer.py'),
     'out[k] = float((lam2 / (1 - lam2) * (r ** -0.5) * I).sum())'),
    ("### the corpus's operator-image line, the OTHER convention", e('qeps_layer.py'),
     'C = (r ** 0.5) * integ'),
    ("### the identity's remainder side", e('b38_act10.py'),
     'out[:, k] = lam2 / (1 - lam2) * (r ** -0.5) * I'),
    ("### the identity's TRACE side, the source's convention", e('b38_act10.py'),
     'An[i] = math.sqrt(lamd)'),
    ("### the identity itself", e('b38_act10.py'), 'resid = TrN - A - E2N'),
    ("### b264's own evaluator, the third site", e('b264_eps_decay.py'),
     'return lam2 / (1 - lam2) * (r ** -0.5) * I'),
    ("the atlas's calibrated sign", e('carto_atlas.py'), 'sign fixed BY the E2 calibration'),
    ("### and the atlas's disclaimer", e('carto_atlas.py'), 'No sign claim is made'),
    ("the owner's banked table, the reference column", d('b38_2026-08-18.txt'),
     'ITEMS 1 + 3 (place set'),
    ("b264 -- the noise-floor work-order", d('b264_eps_even_decay.txt'), 'W-ORD-NTERM-FLOOR'),
    ("b312 -- the identification this act runs", d('b312_the_remainder.txt'), 'NO. ### DIFFERENT.'),
    ("### b312 -- the work-order it filed", d('b312_the_remainder.txt'),
     'W-ORD-REMAINDER-EXPONENT'),
    ("### b312 -- the exact check it named", d('b312_the_remainder.txt'), 'NOTHING ELSE TOUCHED'),
    ("### b312 -- the insensitivity it derived", d('b312_the_remainder.txt'),
     'FOR EVERY `s` WHATEVER'),
    ("the E1 precedent -- the record does not overwrite itself", d('b265_filings.txt'),
     'THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF'),
    ("### and where that clause was discharged", d('b266_filings.txt'), 'E-2026-08-31-1'),
]

SELF_NEEDLES = [
    ('bank states the verdict up front', BANK, 'THE RESIDUE DOES NOT COLLAPSE'),
    ('bank names the branch', BANK, 'BRANCH TWO'),
    ('bank gives the ratios', BANK, '0.9176, 0.8830, 0.8645, 0.8298, 0.8249, 0.8141'),
    ('### bank refuses the retraction reading', BANK, 'IT DOES NOT MEAN THE FLIP WAS WRONG'),
    ('### bank states the standing clause', BANK, 'BY NOTHING THE RESIDUE DOES'),
    ('### bank refuses the verdict-on-a-measurement reading FIRST', BANK,
     'NO BANKED NUMBER IS CALLED WRONG'),
    ('bank says the owner was not edited', BANK, 'THE OWNER INSTRUMENT WAS NOT EDITED'),
    ('bank gives the source three sites', BANK, 'THREE SITES, THREE REGISTERS'),
    ('bank gives the corpus line numbers', BANK, '**line 113**'),
    ('bank quotes the importing act', BANK, 'k(rho) = rho^{1/2} INT_0^inf'),
    ('bank refuses to criticise the importing act', BANK, 'IS NOT CRITICISED BY THIS'),
    ('bank states why the flip is licensed', BANK, 'ANY RESIDUE IS LOOKED AT, AND WHATEVER THE RESIDUE'),
    ('bank records the direction as unpredicted', BANK, 'REGISTERED NO EXPECTATION'),
    ('bank reports the diff counts', BANK, '13 LINES REMOVED, 13 ADDED, 13 DECLARED'),
    ('### bank owns that a control fired on the first run', BANK,
     'IT FIRED, ON A REAL DEFECT, ON THE FIRST RUN'),
    ('### bank owns the worse of the two defects', BANK, 'WROTE THE COPY ANYWAY'),
    ('bank names the axes', BANK, 'EPS_NQ = 700'),
    ('bank says the instrument is not exact', BANK, 'NOT EXACT ANYWHERE IN THIS PATH'),
    ('bank gives the transcription control', BANK, 'WORST ABSOLUTE DEPARTURE FROM THE BANKED'),
    ('bank calls that departure display rounding', BANK, 'THAT IS DISPLAY ROUNDING AND NOT DISAGREEMENT'),
    ('bank gives the positive control', BANK, '78 BITWISE'),
    ('bank gives the two columns', BANK, 'THE TWO COLUMNS, SIDE BY SIDE'),
    ('bank gives the structural measurement', BANK, '5.55e-16'),
    ('bank gives the call-path table', BANK, 'BY CALL PATH'),
    ('bank says the unmoved six were computed twice', BANK, 'COMPUTED TWICE AND'),
    ('bank gives the difference quotient', BANK, '22.99644119'),
    ('bank gives the ladder with the floor columns', BANK, 'floor bkd'),
    ('bank names the floor modes', BANK, 'EVEN-INDEXED FLOOR MODES ARE 8 AND 10'),
    ('bank says a gate nobody prints cannot be checked', BANK, 'IS A GATE NOBODY CAN CHECK'),
    ('bank gives the decay shift', BANK, 'ONE POWER OF `rho`'),
    ('bank prints the derived columns', BANK, 'A+E2 source'),
    ('### bank refuses to interpret the derived column', BANK, 'NOT INTERPRETED BY THIS ACT'),
    ('### bank gives the calibration caution', BANK, 'ITS SIGN WAS CALIBRATED'),
    ('### bank states the direction of that column', BANK, 'IT IS THE OPPOSITE SHAPE'),
    ('bank bounds what the convention accounts for', BANK, 'BETWEEN 8% AND 19%'),
    ('bank refuses to re-read the face-offs', BANK, 'STAND UNAMENDED'),
    ('bank gives the import ledger', BANK, 'THE IMPORT LEDGER'),
    ('bank states the ledger own limit', BANK, 'PROVED NOTHING, VERIFIED NO PROOF'),
    ('bank routes the errata candidate', BANK, 'ERRATA-CLASS CANDIDATE'),
    ('bank cites the E1 precedent', BANK, 'E-2026-08-31-1'),
    ('bank says an erratum is the author\'s instrument', BANK, 'MARKING ITS OWN WORK'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged under its cap', BANK, 'UNDER b310'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND'),
    ('bank records the W2 ruling verbatim', BANK, 'a mean-zero variant of the corpus'),
    ('bank marks the ruling recorded and not applied', BANK, 'RECORDED, NOT APPLIED'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank files the new work-orders', BANK, 'W-ORD-CONVENTION-SWEEP'),
    ('bank names the fold and the act before it', BANK,
     'THE NEXT ACT IS A FRESH-CLONE CERTIFICATION TEST'),
    ('bank gives a fourth reason for that act', BANK, 'THE FOURTH IS THAT'),
    ('bank reports the census with its scope', BANK, 'TOTAL MISSING : 0'),
    ('bank reports the shadow as nothing', BANK, 'NOTHING IS WHAT IT IS'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('bank declares its deviations', BANK, 'DEVIATIONS, DECLARED'),
    ('registration splits its two halves', REG, 'HAVE NOT BEEN RUN'),
    ('registration states the standing clause', REG, 'THE STANDING CLAUSE'),
    ('registration caps owner edits', REG, 'owner instrument files edited'),
    ('registration caps fits', REG, 'comparisons to a target, and fits'),
    ('registration registers no direction', REG, 'REGISTERS NO EXPECTATION ABOUT THE RESIDUE'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives branch two', RUN, 'THE RESIDUE IS NOT THE EXPONENT'),
    ('the run gives the positive control', RUN, 'BITWISE IDENTICAL'),
    ('the flip log shows the round trip', FLIPLOG, 'ROUND TRIP'),
    ('the flip log prints a unified diff', FLIPLOG, 'THE UNIFIED DIFF, PRINTED IN FULL'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-NOFIT` -- WHAT AN ACT THAT TUNED TO AN ANSWER WOULD HAVE WRITTEN.**
    ('the flip is not justified by the residue', BANK, 'THE RESIDUE CONFIRMS THE FLIP.'),
    ('no target is named', BANK, 'THE SOURCE COLUMN IS CLOSER TO THE TARGET.'),
    ('no fit is claimed', BANK, 'THE FLIPPED COLUMN FITS.'),
    ('the residue is not said to be explained', BANK, 'THE EXPONENT EXPLAINS THE RESIDUE.'),
    ('the cancellation is not read', BANK, 'THE IDENTITY CLOSES UNDER THE SOURCE EXPONENT.'),
    # ### **`G-NOREVERDICT`.**
    ('no banked number is called wrong', BANK, 'THE BANKED NUMBERS ARE WRONG.'),
    ('no act is re-verdicted', BANK, 'b38 IS RE-VERDICTED.'),
    ('the face-offs are not re-read', BANK, 'THE FACE-OFFS ARE RE-READ.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the errata is not filed by this seat', BANK, 'THE ERRATUM IS FILED.'),
    # ### **THE STANDING CAPS.**
    ('the owner is not edited', BANK, 'THE OWNER INSTRUMENT IS EDITED.'),
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the ruling is not applied', BANK, 'THE W2 VARIANT IS BUILT.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the fold is not folded', BANK, 'THE FOLD IS DONE.'),
]

TOOLNUM = [
    ("the copies, their diffs and the round trip", 'tools/b313_flip.py'),
    ("both columns, the controls and every table", 'tools/b313_run.py'),
    ("the source's exponent, re-extracted", 'tools/b312_definitions.py'),
    ("the owner instrument the columns run through", 'tools/e16/b38_act10.py'),
    ("the remainder layer", 'tools/e16/qeps_layer.py'),
    ("the ladder's evaluator and its NG law", 'tools/e16/b264_eps_decay.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b313_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b313_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b313_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b313_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the byte checks the profile comparison imports", 'tools/b302_kernel.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b313' in x)


def git_show_relay(rel):
    """### `b302_kernel.git_show` is hard-wired to SIDE-global-section. ### **THIS ONE READS THE
    ### RELAY REPO**, and the NORMALISER is still the imported one -- b309's `core.autocrlf`
    ### defect, which made a clean tree fail a raw byte comparison."""
    r = subprocess.run(['git', '-C', ROOT, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b313 -- GATE SUITE (A COMPUTATION THAT CHANGED AN INSTRUMENT IN A COPY)')
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
    print('    ### **THE FIRST FIVE ARE `G-NOFIT`: the sentences an act that kept a flip BECAUSE')
    print('    ### the residue improved would have written. ### THEY ARE THE ONLY WAY A LICENSED')
    print('    ### FLIP CAN STILL BE DISHONESTLY REPORTED.**')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    flip = io.open(FLIPLOG, encoding='utf-8').read()

    # ### ### G-OWNER-UNTOUCHED -- ### **CHECKED AFTER THE RUN, NOT BEFORE IT.**
    print('\n  G-OWNER-UNTOUCHED (the owner instrument byte-identical to git HEAD, NORMALISED):')
    bad = []
    for rel in OWNERS_UNTOUCHED:
        here = KRN.normalise(io.open(os.path.join(ROOT, rel.replace('/', os.sep)), 'rb').read())
        head = KRN.normalise(git_show_relay(rel) or b'')
        same = (here == head and bool(head))
        print('    %-34s identical to HEAD : %s' % (rel, same))
        if not same:
            bad.append(rel)
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS_UNTOUCHED,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    print('    ### **CHECKED AFTER THE RUN AND NOT BEFORE IT: A FILE IS EDITED BY RUNNING THINGS,')
    print('    ### NOT BY PLANNING TO.**')
    if bad or dirty:
        fails.append('G-OWNER-UNTOUCHED')

    # ### G-DIFF / G-ROUNDTRIP.
    print('\n  G-DIFF / G-ROUNDTRIP (every difference declared; the copy inverts to the original):')
    rt = flip.count('BYTE : True  PASS')
    dm = re.findall(r'THE DIFF: (\d+) line\(s\) removed, (\d+) added; declared substitutions '
                    r'(\d+) ; MATCH : (\w+)', flip)
    print('    round trips passing : %d of 3 ; diff rows : %s' % (rt, dm))
    okdiff = (rt == 3 and len(dm) == 3 and all(x[3] == 'True' for x in dm))
    print('    every difference corresponds to a declared substitution : %s' % okdiff)
    if not okdiff:
        fails.append('G-DIFF/G-ROUNDTRIP')

    # ### G-CONTROL.
    print('\n  G-CONTROL (the copy with the exponent restored reproduces the owner):')
    m = re.search(r'quantities compared : (\d+) ; ### \*\*BITWISE IDENTICAL : (\d+)\*\*', run)
    okc = bool(m) and m.group(1) == m.group(2)
    print('    %s ; identical : %s' % (m.group(0) if m else '### NOT FOUND', okc))
    if not okc:
        fails.append('G-CONTROL')

    # ### G-STRUCTURE.
    print('\n  G-STRUCTURE (the flip is a pointwise rho factor):')
    m2 = re.search(r'rho\s+-\s+1 \|\s+=\s+([\d.]+e-\d+)', run)
    oks = bool(m2) and float(m2.group(1)) <= 1e-12
    print('    measured deviation : %s ; within 1e-12 : %s'
          % (m2.group(1) if m2 else '### NOT FOUND', oks))
    if not oks:
        fails.append('G-STRUCTURE')

    # ### G-TRANSCRIPTION.
    print('\n  G-TRANSCRIPTION (the loop reproduces the owner\'s banked table):')
    m3 = re.search(r'WORST ABSOLUTE DEPARTURE FROM THE BANKED TABLE : ([\d.]+e-\d+)', run)
    okt = bool(m3) and float(m3.group(1)) <= 5e-5
    print('    worst departure : %s ; within the table\'s own display rounding : %s'
          % (m3.group(1) if m3 else '### NOT FOUND', okt))
    if not okt:
        fails.append('G-TRANSCRIPTION')

    # ### G-NOISEFLOOR.
    print('\n  G-NOISEFLOOR (the gate is in the ladder\'s path and what it removes is printed):')
    nf = ('NRES = 7' in run and 'floor modes excluded from the resolved sum' in run
          and 'floor bkd' in run)
    print('    NRES read from b264, floor modes named, removal printed : %s' % nf)
    if not nf:
        fails.append('G-NOISEFLOOR')

    # ### G-NOFIT, the positive arm.
    print('\n  G-NOFIT (positive arm: the act states its own licence and its own bound):')
    lic = ('BY NOTHING THE RESIDUE DOES' in bank
           and 'NO TARGET WAS NAMED AND NO FIT WAS PERFORMED' in bank
           and 'IT DOES NOT ACCOUNT FOR THE REST' in bank)
    print('    licence stated, bound stated, no-fit stated : %s' % lic)
    if not lic:
        fails.append('G-NOFIT')

    # ### G-NOBUILD / G-NOPAPERS / G-ANCESTOR.
    print('\n  G-NOBUILD / G-NOPAPERS / G-ANCESTOR:')
    prof = KRN.normalise(io.open(PROFILE, 'rb').read())
    phead = KRN.normalise(KRN.git_show('AXIOM_PRINTS.txt') or b'')
    identical = (prof == phead)
    sdirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                            capture_output=True, text=True).stdout
    lean_rows = [x for x in sdirty.splitlines() if x.strip().endswith('.lean')]
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    lines_ = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile identical to HEAD : %s ; `.lean` changed : %d ; prints : %d'
          % (identical, len(lean_rows), len(lines_)))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s'
          % (len(tracked), pfx))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')
    if tracked:
        fails.append('G-NOPAPERS')
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

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 13
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
