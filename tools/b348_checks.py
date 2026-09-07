# -*- coding: utf-8 -*-
"""b348_checks.py -- THE GATE SUITE FOR THE FOLD.

### ### **THIS SUITE USES `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN**, and every `G-NO*`-shaped arm below
### reads STRIPPED CODE or a marked region rather than raw prose -- ### **WHICH IS THE RULE THIS ACT MINTS, APPLIED
### TO THE ACT THAT MINTS IT.**
### ### **THE ARMS (registration section (G)):** `G-QUOTE`, `G-ADDITIVE`, `G-NOGRADE`, `G-ARC`, `G-SPECIES`,
### `G-CENSUS`, `G-DESK`, `G-MODULE`, `G-ROW`, `G-KEY` / `G-NOTEXPLAINED`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`,
### `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the sweeps, `G-SHARED`, the hedge audit, the must-fail
### fixtures; re-run after the push.
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402
import run_clock         # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b348_the_fold.txt')
REG = d('b348_registration_2026-09-07.txt')
FERRY = d('b348_ferry_2026-09-07.txt')
EXTRACT = d('b348_extract_notes.txt')
FRUN, FJ = d('b348_fold_run.txt'), d('b348_fold.json')
EMIT = d('b348_fold_emitted.md')
CORR, IDX = d('b348_corr_run.txt'), d('b348_index_run.txt')
SCAN, TERMSCAN, GATE = d('b348_ferry_scan.txt'), d('b348_reg_termscan.txt'), d('b348_reg_gate.txt')
CENSUS, FCEN = d('b348_census.txt'), d('b348_faces_census.txt')
REGSPEC, SATIS = d('b348_regspec_run.txt'), d('audit_b348_reg_satisfiable.txt')
PINS, INDEXQ = d('b348_pins_stepzero.txt'), d('audit_b348_index_query.txt')
SEAL = '34ff90211cc84b826621b6820482453cd844a6281d1ab5b6e72387cf44b379f3'
SECTION = 'THE PRICED-AND-RESOLVED ARC, b339\u2013b347 \u2014 THE FOLD'
ROWNUM = '196'
MODULE = os.path.join(MOD, 'USE_AND_MENTION.md')

OWNED = [BANK, REG, FERRY, FRUN, FJ, EMIT, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, TERMSCAN,
         d('b348_satisfiable.json'), EXTRACT,
         t('b348_extract.py'), t('b348_regspec.py'), t('b348_fold.py'), t('b348_correspondence.py'),
         t('b348_index_append.py')]

CARRIERS = [
    (t('b348_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]
NEW_THIS_ACT = {'tools/b348_extract.py', 'tools/b348_regspec.py', 'tools/b348_fold.py',
                'tools/b348_correspondence.py', 'tools/b348_index_append.py', 'tools/b348_checks.py'}

TOOLNUM = [
    ('the fold, F-QUOTE, F-NOGRADE, F-ADDITIVE and the emission', 'tools/b348_fold.py'),
    ("the run file's clock", 'tools/run_clock.py'),
    ('the repaired flattener this suite uses', 'tools/gate_text.py'),
    ('the census the fold restates', 'tools/b347_repairs.py'),
    ('row 196', 'tools/b348_correspondence.py'),
    ('the key', 'tools/b348_index_append.py'),
    ('29 clauses', 'tools/b348_regspec.py'),
    ('17288 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('b339 -- UNAFFORDABLE at the sealed ceiling', d('b339_the_exponent_resolved.txt'),
     'THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.'),
    ('b340 -- the refinement failed, not the identity', d('b340_the_li_family_control.txt'),
     'REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.'),
    ('b342 -- the order arm is a defective bar', d('b342_the_two_rules_as_modules.txt'),
     '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`'),
    ('b344 -- one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('b345 -- a fourth control holds', d('b345_the_li_control_rerun.txt'),
     '### ### ### **A FOURTH CONTROL HOLDS.**'),
    ('b346 -- resolved on the rate axis', d('b346_the_exponent_by_rate.txt'),
     '### ### ### **AND ON THE RATE AXIS THE QUESTION IS RESOLVED, AT A RESOLVING POWER OF `63.6`.**'),
    ('b347 -- a sharper instrument is not a result', d('b347_the_three_repairs.txt'),
     '### ### ### **A SHARPER INSTRUMENT IS NOT A RESULT.**'),
    ('b317 -- the species in its own words', d('b317_gates.txt'),
     '    ### **THE SCAN IS OVER STRIPPED CODE.** ### A docstring saying the unit is never'),
    ('the order -- the species minted', FERRY,
     'COMPONENT 3 \u2014 THE LORE, with one species MINTED: a scanner over'),
    ('the order -- the partition named and NOT opened', FERRY,
     'as a research proposal and NOT opened \u2014 a finite classification'),
    ('the last fold -- a filings section moves no grade', FINDINGS,
     '**Four acts, 2026-09-06.** A filings section: **no grade moves here, no act is re-verdicted, and nothing below is new mathematics.**'),
]

SELF_NEEDLES = [
    ('the bank states what a fold is first', BANK,
     '### ### ### **A FOLD IS A SUMMARY OF ITS ACTS AT THEIR OWN GRADES. ### IT PROVES NOTHING, DISCHARGES'),
    ('### the no-grade check is mechanical', BANK, '### **AND IN THIS FOLD THE NO-GRADE-MOVED'),
    ('### the gate refused once before it passed', BANK, '### ### **AND THE GATE REFUSED ONCE BEFORE IT PASSED**'),
    ('### it happened rather than being claimed', BANK, '### ### FINDINGS DOCUMENT, AND THAT IS NOT A CLAIM HERE -- IT HAPPENED.**'),
    ('### the arc statement, and what it does not make correct', BANK,
     '### ### **A QUESTION PRICED UNAFFORDABLE ON ONE AXIS WAS RESOLVED ON ANOTHER THE RECORD ALREADY HELD.**'),
    ('### the trail stays owed', BANK, '### `W-ORD-LI-FAMILY-CONTROL` ### **STAYS OWED**'),
    ('### the floor is not explained', BANK, '### ### *Scope:* one axis of three. ### **THE FLOOR IS NOT EXPLAINED.**'),
    ('### the species itself', BANK,
     '### ### ### **A SCANNER OVER PROSE CANNOT TELL USE FROM MENTION: A SENTENCE DENYING A THING CONTAINS THE'),
    ('### the direction of the species', BANK, '### ### **THE DIRECTION: FALSE ALARM, NEVER FALSE CLEARANCE.**'),
    ('### the cure, and what it forbids', BANK,
     '### ### **THE CURE: ARMS SCOPED TO CODE LINES, OR TO MARKED MENTION-REGIONS -- NEVER A SOFTENED NEEDLE.**'),
    ('### filed as a judgement rule, not listed as mechanized', BANK,
     '### ### **SO IT IS FILED AS A JUDGEMENT RULE AND IS DELIBERATELY NOT LISTED BESIDE THE MECHANIZED ONES**,'),
    ('### naming it is not building it', BANK, '### in a different act. ### **NAMING IT IS NOT BUILDING IT.**'),
    ('### the census means absence, not approval', BANK,
     '### ### **SO THE RECORD\'S QUIET IS MOSTLY THE ABSENCE OF STATED NUMERICAL BARS, NOT BARS CHECKED AND'),
    ('### the gate is prospective', BANK, '### ### **AND THE GATE IS PROSPECTIVE.**'),
    ('### this act clears the arms because it states no bar', BANK,
     '### **IT CLEARS BECAUSE IT STATES NO BAR, NOT BECAUSE IT PRICED ONE**'),
    ('### the partition named and not opened', BANK,
     '### ### ### **THE FAILURE-MODE PARTITION -- NAMED HERE AS A RESEARCH PROPOSAL AND NOT OPENED.**'),
    ('### no such partition is known to exist', BANK, '### ### SUCH PARTITION IS KNOWN TO EXIST.**'),
    ('### the expectation refuted, and usefully', BANK, '### ### **REFUTED, AND USEFULLY.**'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING. ### AND NOTHING IS WHAT A FOLD RETURNS.**'),
]

MUST_FAIL = [
    ('the bank never says the fold proves it', BANK, '### THE FOLD PROVES IT.'),
    ('the bank never says a convention is correct', BANK, '### A CONVENTION IS CORRECT.'),
    ('the bank never says the partition is opened', BANK, '### THE PARTITION IS OPENED.'),
    ('the bank never says the census clears the record', BANK, '### THE CENSUS CLEARS THE RECORD.'),
    ('the bank never says the rule is enforced', BANK, '### THE RULE IS ENFORCED.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    """### THE SOURCE WITH COMMENTS AND STRING LITERALS REMOVED. ### **THE CURE THIS ACT MINTS, APPLIED HERE.**"""
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b348 -- GATE SUITE (THE FOLD, AND THE RULE IT MINTS APPLIED TO ITSELF)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    F = json.load(io.open(FJ, encoding='utf-8'))
    C = F['census']
    fnd = io.open(FINDINGS, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    emit = io.open(EMIT, encoding='utf-8').read()
    run = io.open(FRUN, encoding='utf-8').read()

    print(chr(10) + '  G-QUOTE (every quotation located at the act that ORIGINATED it, by the emitter, before the section was written):')
    q1 = F['quotes_failing'] == 0
    q2 = 'quotations failing : 0' in run
    # ### the emitted markdown's quotations must ALSO be findable now, re-checked here independently of the emitter
    SRCMAP = {'b339': 'b339_the_exponent_resolved.txt', 'b340': 'b340_the_li_family_control.txt',
              'b341': 'b341_the_two_coefficients.txt', 'b342': 'b342_the_two_rules_as_modules.txt',
              'b343': 'b343_the_maps_next_reach.txt', 'b344': 'b344_the_floor_priced.txt',
              'b345': 'b345_the_li_control_rerun.txt', 'b346': 'b346_the_exponent_by_rate.txt',
              'b347': 'b347_the_three_repairs.txt'}
    recheck, bad_re = 0, []
    for m in re.finditer(r'- \*\*(b3\d\d) \u2014 .*?\n  - Its own words: \u201c\u2026(.*?)\u2026\u201d', emit, re.S):
        act, q = m.group(1), m.group(2).strip()
        recheck += 1
        def same(s):
            return gate_text.flat(s.replace('###', ' ').replace('**', ' '))
        src = same(io.open(d(SRCMAP[act]), encoding='utf-8', errors='replace').read())
        if same(q) not in src:
            bad_re.append((act, q[:60]))
    q3 = recheck == 9 and not bad_re
    gq = q1 and q2 and q3
    print('    the emitter reported 0 failing : %s ; its run file says so : %s' % (q1, q2))
    print('    re-checked here INDEPENDENTLY against the originating banks : %d of 9 found, misses %s' % (recheck - len(bad_re), bad_re or 'none'))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + '  G-ADDITIVE (the findings document a TRUE PREFIX of its blob; the section once; nothing edited):')
    fb = blob_of(PP, 'FINDINGS.md')
    a1 = (fb is not None) and norm(fnd).startswith(norm(fb).rstrip(chr(10)))
    a2 = fnd.count('## ' + SECTION) == 1
    a3 = F['prefix_working'] and F['prefix_blob'] and F['once']
    a4 = F['lines_added'] > 0
    ga = a1 and a2 and a3 and a4
    print('    a true prefix of its committed blob : %s ; the section present once : %s' % (a1, a2))
    print('    the emitter measured the same at write time : %s ; lines added %d' % (a3, F['lines_added']))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADDITIVE')

    print(chr(10) + "  G-NOGRADE (every grade anchored verbatim in its own act's bank; MECHANICAL):")
    n1 = F['grades_failing'] == 0
    n2 = 'grade anchors failing : 0' in run
    n3 = 'no grade moves here' in fnd[fnd.index('## ' + SECTION):] and 'no act is re-verdicted' in fnd[fnd.index('## ' + SECTION):]
    n4 = 'the no-grade-moved claim is itself mechanical' in fnd[fnd.index('## ' + SECTION):]
    gn = n1 and n2 and n3 and n4
    print('    0 grade anchors failing : %s ; the run file says so : %s' % (n1, n2))
    print('    the section states the filings law : %s ; and says the check is mechanical : %s' % (n3, n4))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOGRADE')

    sec = fnd[fnd.index('## ' + SECTION):]
    print(chr(10) + '  G-ARC (the arc carries its scope and claims no grade its acts do not; the quantifier named unowned):')
    r1 = 'it does not make a convention correct' in sec.lower()
    r2 = '**stays owed**' in sec.lower()
    r3 = 'the floor is not explained' in sec.lower()
    r4 = 'unowned' in sec.lower() and 'K8' in sec
    r5 = sec.lower().count('*scope:*') >= 4
    gr = r1 and r2 and r3 and r4 and r5
    print('    no convention made correct : %s ; the trail stays owed : %s ; the floor not explained : %s' % (r1, r2, r3))
    print('    K8 named unowned : %s ; a scope sentence beside each claim (%d) : %s' % (r4, sec.lower().count('*scope:*'), r5))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-ARC')

    print(chr(10) + '  G-SPECIES (five incidents each at its own act; the direction; the cure; the mechanizability decided and reported):')
    s1 = len(F['incidents']) == 5 and set(F['incidents']) == {'b316', 'b317', 'b345', 'b346', 'b347'}
    s2 = 'false alarm, never false clearance' in sec.lower()
    s3 = 'never a softened needle' in sec.lower()
    s4 = (F['species']['mechanized'] is False) and 'judgement rule' in sec.lower() and 'not listed beside the mechanized ones' in sec.lower()
    s5 = 'NOT MECHANIZABLE IN THE REGISTRATION GATE' in run
    gs = s1 and s2 and s3 and s4 and s5
    print('    five incidents, each at its own act : %s (%s)' % (s1, F['incidents']))
    print('    the direction stated : %s ; the cure stated : %s' % (s2, s3))
    print('    decided NOT mechanizable and filed as a judgement rule, not listed as mechanized : %s ; reported in the run : %s' % (s4, s5))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SPECIES')

    print(chr(10) + '  G-CENSUS (the figures identical to the producing record by EXACT DECIMAL STRING; the sentence; prospective):')
    rr = io.open(d('b347_repairs_run.txt'), encoding='utf-8', errors='replace').read()
    m = re.search(r'registrations gated : (\d+) ; would FIRE on at least one arm : (\d+) ; CLEAR : (\d+)', rr)
    m2 = re.search(r'of the (\d+) that would not fire, (\d+) carry NEITHER', rr)
    c1 = (C['gated'], C['fire'], C['clear'], C['nothing']) == (m.group(1), m.group(2), m.group(3), m2.group(2))
    c2 = all(x in sec for x in (C['gated'], C['fire'], C['clear'], C['nothing']))
    c3 = 'absence of stated numerical bars' in sec.lower()
    c4 = 'prospective' in sec.lower()
    gc = c1 and c2 and c3 and c4
    print('    the four figures identical to the producing record : %s' % c1)
    print('    all four appear in the section : %s ; the absence sentence : %s ; prospective : %s' % (c2, c3, c4))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CENSUS')

    print(chr(10) + '  G-DESK (the partition present, named a proposal, NOT opened, with the sentence that none is known to exist):')
    k1 = 'failure-mode partition' in sec.lower()
    k2 = 'not opened' in sec.lower() and 'research proposal' in sec.lower()
    k3 = 'no such partition is known to exist' in sec.lower()
    k4 = 'naming it is not opening it' in sec.lower()
    k5 = all(x in sec for x in ('`M-2`', 'K8', 'W-ORD-FLOOR-HELD-AXES', 'patent receipts'))
    gk = k1 and k2 and k3 and k4 and k5
    print('    named a research proposal and NOT opened : %s / %s ; none known to exist : %s' % (k1, k2, k3))
    print('    naming is not opening : %s ; the standing desk items present : %s' % (k4, k5))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-DESK')

    print(chr(10) + '  G-MODULE (the September shape; local commit; the TECHNE remote UNMOVED; it confers no grade):')
    mod = io.open(MODULE, encoding='utf-8').read()
    d1 = all(h in mod for h in ('## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE'))
    d2 = 'confers none' in mod and 'not a result' in mod
    d3 = all(a in mod for a in ('b316', 'b317', 'b345', 'b346', 'b347'))
    tch = git(TC, 'rev-parse', '--short', 'HEAD').strip()
    rem = subprocess.run(['git', '-C', TC, 'ls-remote', 'origin', 'main'], capture_output=True, text=True,
                         encoding='utf-8', errors='replace').stdout.split()
    d4 = bool(tch) and (not rem or not rem[0].startswith(tch))
    d5 = not git(TC, 'status', '--porcelain').strip()
    gm = d1 and d2 and d3 and d4 and d5
    print('    the September shape : %s ; grade-honest : %s ; all five incidents : %s' % (d1, d2, d3))
    print('    TECHNE local HEAD %s ; the remote does NOT carry it (NOT PUSHED) : %s ; tree clean : %s' % (tch, d4, d5))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MODULE')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'A FOLD RESTATES ITS ACTS AT THEIR OWN GRADES' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTEXPLAINED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : priced-and-resolved-fold returns 1 row(s)' in irun
    k_2 = all(('%-38s NO KEY after  : True  PASS' % q) in irun for q in
              ('the fold proves it', 'the convention is correct', 'the partition is opened', 'the census clears the record'))
    k_3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gkk = k_1 and k_2 and k_3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s' % (k_1, k_2, k_3))
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTEXPLAINED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    ib = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument; no keystone; the deposit and HANDOFF clean; only this act\'s papers path touched):')
    owner = ['tools/e16/b264_eps_decay.py', 'tools/b340_li_control.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FINDINGS.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    key = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md').strip()
    gne = not touched and not ppbad and hand and dep and key
    print('    owner instruments modified : %s ; papers paths beyond FINDINGS.md : %s' % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; the keystone clean : %s' % (hand, dep, key))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies through its owning tool; the ordering read from two clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and F['run_clock'] is not None and F['run_clock'] > stampm.group(1)
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; it carries its clock (%s) : %s' % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    the ordering from two clocks: seal %s < fold run %s : %s' % (stampm.group(1) if stampm else '?', F['run_clock'], o3))
    print('    the audit reads JOINTLY SATISFIABLE : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED):')
    hookp, mirrorp = d('b348_hooks.txt'), d('b348_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht, mt = io.open(hookp, encoding='utf-8', errors='replace').read(), io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh = h_ok and m_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror: clean on all three clauses : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = [
        ('quotations failing %d' % F['quotes_failing'], ('`%d`' % F['quotes_failing']) in bank),
        ('grade anchors failing %d' % F['grades_failing'], ('`%d`' % F['grades_failing']) in bank),
        ('lines added %d' % F['lines_added'], ('`%d`' % F['lines_added']) in bank),
        ('the three tables (%d, %d, %d)' % (F['corrections'], F['defective'], F['seat_defects']),
         all(('`%d`' % x) in bank for x in (F['corrections'], F['defective'], F['seat_defects']))),
        ('the census figures', all(('`%s`' % x) in bank for x in (C['gated'], C['fire'], C['clear'], C['nothing']))),
        ('the TECHNE commit', ('`%s`' % tch) in bank),
        ('the seal hash', SEAL in bank),
        ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
    ]
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    checks.append(('%s clauses' % cl, ('%s clauses' % cl) in bank))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path):')
    once = (all(os.path.exists(p) for p in [FRUN, CORR, IDX, EMIT])
            and not os.path.exists(d('b348_fold_run2.txt')))
    print('    %s' % once)
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib2 = idx[idx.index('# ### THE PRICED-AND-RESOLVED ARC, b339-b347 -- THE FOLD (b348).'):idx.index('# ### THE THREE REPAIRS AND THE TWO RULES (b347).')] if '# ### THE PRICED-AND-RESOLVED ARC, b339-b347 -- THE FOLD (b348).' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the section, the module, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the section', sec), ('the module', mod), ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the section, the module and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b348_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the section', sec), ('the module', mod),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
