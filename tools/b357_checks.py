# -*- coding: utf-8 -*-
"""b357_checks.py -- THE GATE SUITE FOR WHAT THE LEDGERS SAY THE CHECKS CERTIFY.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349),
### every quotation goes through `quote_norm`, and ### **EVERY ARM THAT READS A REPOSITORY STATE DECLARES ITS
### SIDE OF THE PUSH** (b352): `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read BEFORE THE PUSH and again
### after, and the pre-push reading is the one that carries; `G-NOEDIT` and `G-NOEDIT-LEDGER` are
### `SIDE-INVARIANT`; this act writes nothing to the papers repo, so `G-NOHOOK` CHECKS that the hook and the
### mirror are NOT OWED rather than assuming it.
### ### ### **AND ONE THING THIS SUITE DOES NOT DO, SAID HERE BECAUSE THE ACT IT GATES IS ABOUT EXACTLY
### ### ### THIS:** ### its arms are sentences TYPED BY THIS SEAT and matched against the bank. ### The
### standing work-order to route every arm through `tools/anchor_from_file.py` is NAMED AND NOT BUILT, so
### the `SELF NEEDLES` block below is the only part of this file whose anchors are READ rather than typed.
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
import quote_norm        # noqa: E402
import anchor_from_file as AF   # noqa: E402
import b357_extract as EX       # noqa: E402
import b357_read as RD          # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b357_what_the_ledgers_say.txt')
REG = d('b357_registration_2026-09-07.txt')
FERRY = d('b357_ferry_2026-09-07.txt')
EXTRACT = d('b357_extract_notes.txt')
RUN, RJ = d('b357_read_run2.txt'), d('b357_read.json')   # ### **run2 IS THE RELIED-ON READING.**
SUPER, SUPJ = d('b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt'), d('b357_read_SUPERSEDED_LEXICAL_GROUPING.json')
ERRATA = d('b357_errata_draft.txt')
ROUTED = d('b357_routed_correspondence_204.txt')
EJ = d('b357_reads.json')
CORR, IDX = d('b357_corr_run.txt'), d('b357_index_run.txt')
TERMSCAN, GATE = d('b357_reg_termscan.txt'), d('b357_reg_gate.txt')
CENSUS, FCEN = d('b357_census.txt'), d('b357_faces_census.txt')
REGSPEC, SATIS = d('b357_regspec_run.txt'), d('audit_b357_reg_satisfiable.txt')
PINS = d('b357_pins_stepzero.txt')
SEAL = '060b9f86dc601201936dee2425ce9f40bd050ff72ba13982a105a1cd1ed647f7'
ROWNUM = '205'
LEDGERS = {'FINDINGS.md': FINDINGS, 'FACES_LEDGER.md': FACES,
           'CORRESPONDENCE.md': TABLE, 'banked_index.py': INDEX}

OWNED = [BANK, REG, FERRY, RUN, d('b357_read_run.txt'), RJ, SUPER, SUPJ, ERRATA, ROUTED, EJ, CORR, IDX, CENSUS, FCEN,
         REGSPEC, SATIS, PINS, GATE, TERMSCAN, EXTRACT, d('b357_satisfiable.json'), d('b357_ferry_scan.txt'),
         t('b357_extract.py'), t('b357_regspec.py'), t('b357_read.py'),
         t('b357_correspondence.py'), t('b357_index_check.py')]

NEW_THIS_ACT = {'tools/b357_extract.py', 'tools/b357_regspec.py', 'tools/b357_read.py',
                'tools/b357_correspondence.py', 'tools/b357_index_check.py', 'tools/b357_checks.py'}

TOOLNUM = [
    ('the reading, its statuses and its branch', 'tools/b357_read.py'),
    ('the twenty-nine reads', 'tools/b357_extract.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the needle puller', 'tools/needle_pull.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('the gate flattener', 'tools/gate_text.py'),
    ('row 205', 'tools/b357_correspondence.py'),
    ('the key, read back', 'tools/b357_index_check.py'),
    ('the registration clauses', 'tools/b357_regspec.py'),
    ('11440 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

SELF_HINTS = [
    ('the bank states the verdict first', 'THE ANSWER, FIRST.'),
    ('### some rows say it', 'SOME ROWS SAY IT.'),
    ('### the split', '5 WIDER / 6 NARROWER / 1 SILENT'),
    ('### every ledger reached', 'AND THE WIDER FIVE REACH EVERY ONE OF THE FOUR LEDGERS'),
    ('### the two findings kept apart', 'THE TWO FINDINGS, KEPT APART'),
    ('### the wider sentence is not necessarily false', 'THE WIDER SENTENCE IS NOT NECESSARILY FALSE.'),
    ('### the warrant, not the claim', 'WHAT IS WRONG IN GROUP (1) IS THE'),
    ('### the membership question not decided here', 'IT IS NOT DECIDED HERE'),
    ('### the consequence, once', 'CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE CONSTRUCTION'),
    ('### the scan cannot fail on such an object', 'THE SCAN CANNOT FAIL ON SUCH AN'),
    ("### b320's control keeps it from being vacuous", 'WHAT KEEPS THE SCAN FROM BEING VACUOUS, AND IT PASSED'),
    ('### what an independent test would require', 'AN INDEPENDENT TEST WOULD REQUIRE AN OBJECT NOT BUILT AS AN AUTOCORRELATION'),
    ('### and none is ordered here', 'NEEDED ONE, AND NONE IS ORDERED HERE'),
    ("### the act's own incident", 'THE INCIDENT THIS ACT MADE'),
    ("### b348's species named", "THIS IS b348's USE-AND-MENTION SPECIES"),
    ('### the superseded run kept', 'THE SUPERSEDED RUN IS KEPT UNEDITED'),
    ('### grading versus narrating', 'THE RECORD IS MORE CAREFUL WHERE IT IS GRADING THAN WHERE IT IS NARRATING.'),
    ('### one line carrying two statements', 'ONE LINE, TWO STATEMENTS, TWO STATUSES'),
    ("### the straddling line numbers, by b352's rule", 'AND TWO LINE NUMBERS STRADDLE THIS ACT'),
    ('### the erratum drafted and routed', 'THE ERRATA ENTRY: DRAFTED AND ROUTED'),
    ('### the seal on the audit exit code', "SEALED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK"),
    ('### twelve chosen passages are not a census', 'WHAT WAS CHECKED IS TWELVE PASSAGES THIS SEAT CHOSE'),
    ('### the shadow', 'EXPECTED: A TIDY AUDIT THAT FOUND THE RECORD MOSTLY RIGHT'),
]

MUST_FAIL = [
    ('the bank never says the ledgers are wrong', BANK, '### THE LEDGERS ARE WRONG.'),
    ('the bank never says a row is edited', BANK, '### A ROW IS EDITED.'),
    ('the bank never says the checks are demoted', BANK, '### THE CHECKS ARE DEMOTED.'),
    ('the bank never says the arrays are not in the class', BANK, '### THE ARRAYS ARE NOT IN THE CLASS.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
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
    print('b357 -- GATE SUITE (WHAT THE LEDGERS SAY THE CHECKS CERTIFY)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    rgf = gate_text.flat(reg)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    errata = io.open(ERRATA, encoding='utf-8').read()
    C = json.load(io.open(RJ, encoding='utf-8'))
    E = json.load(io.open(EJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-FOURLEDGERS (all four ledgers of section (B) read, and each named in the table):')
    l1 = set(C['ledgers']) == set(LEDGERS)
    l2 = all(k in bank for k in LEDGERS)
    l3 = all(any(r['ledger'] == k for r in C['rows']) for k in LEDGERS)
    gl = l1 and l2 and l3
    print('    the four read : %s ; each named in the bank : %s ; each carries a classified row : %s  %s'
          % (l1, l2, l3, 'PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-FOURLEDGERS')

    print(chr(10) + "  G-TABLE (one table; every row with ledger, line, status and what it certifies):")
    t1 = all(set(r) >= {'ledger', 'line', 'act', 'status', 'certifies', 'text'} for r in C['rows'])
    t2 = all(r['status'] in C['statuses'] for r in C['rows'])
    t3 = len(C['statuses']) == 3
    t4 = all(r['certifies'].strip() for r in C['rows'])
    t5 = C['n_wider'] + C['n_narrower'] + C['n_silent'] == len(C['rows'])
    gt = t1 and t2 and t3 and t4 and t5
    print('    every row complete : %s ; every status one of the sealed three : %s (statuses %d)' % (t1, t2, t3 and 3))
    print('    every row says what it certifies : %s ; the counts add up : %s  %s'
          % (t4, t5, 'PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TABLE')

    print(chr(10) + '  G-LOCATED (every classified row located by the anchor tool at its own ledger, NOW):')
    nbad, moved = 0, []
    for r in C['rows']:
        path = LEDGERS[r['ledger']]
        try:
            n, line = AF.find(path, r['text'][:110])
            needle_pull.pull(path, line)
            if n != r['line']:
                moved.append((r['ledger'], r['line'], n))
        except (AF.AnchorError, LookupError):
            nbad += 1
            print('    ### FAIL (NO ANCHOR NOW)  %s : %d' % (r['ledger'], r['line']))
    unc = len(C['unclassified'])
    gloc = nbad == 0 and unc == 0
    print('    rows re-located at their ledgers : %d of %d ; unclassified : %d'
          % (len(C['rows']) - nbad, len(C['rows']), unc))
    print("    ### lines that MOVED since the reading (b352's straddle, declared not hidden) : %s" % (moved or 'none'))
    for lg, was, now in moved:
        ok_dec = ('%d' % was) in bank and ('%d' % now) in bank and 'STRADDLE THIS ACT' in bf
        print('        %-22s read at %d, now %d ; both declared in the bank : %s' % (lg, was, now, ok_dec))
        if not ok_dec:
            gloc = False
    print('    %s' % ('PASS' if gloc else '### FAIL ###'))
    if not gloc:
        fails.append('G-LOCATED')

    print(chr(10) + '  G-NOTMERGED (the attribution fault and the membership question reported separately):')
    m1 = len(C['attribution_fault']) + len(C['membership_only']) == C['n_wider']
    m2 = not ({(r['ledger'], r['line']) for r in C['attribution_fault']}
              & {(r['ledger'], r['line']) for r in C['membership_only']})
    m3 = 'THE WIDER SENTENCE IS NOT NECESSARILY FALSE' in bf
    m4 = 'WHAT IS WRONG IN GROUP (1) IS THE WARRANT, NOT THE CLAIM' in bf
    m5 = "`b355`'s `H1`" in bf and 'IT IS NOT DECIDED HERE' in bf
    m6 = 'The two are reported apart and are not merged' in bf
    gm = m1 and m2 and m3 and m4 and m5 and m6
    print('    the two groups partition the five : %s ; disjoint : %s' % (m1, m2))
    print('    the not-necessarily-false sentence : %s ; warrant-not-claim : %s' % (m3, m4))
    print('    the membership question routed, not decided : %s ; said not merged : %s  %s'
          % (m5, m6, 'PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-NOTMERGED')

    print(chr(10) + "  G-BRANCH (the branch by (D)'s sealed rule, with the others shown unreachable):")
    run = io.open(RUN, encoding='utf-8').read()
    b1 = C['verdict'] == 'SOME ROWS SAY IT' and 'SOME ROWS SAY IT' in bf
    b2 = '(NO ROW SAYS THE WIDER SENTENCE) -- UNREACHABLE, AND SHOWN SO' in gate_text.flat(run)
    b3 = '(THE ROWS ARE SILENT) -- UNREACHABLE, AND SHOWN SO' in gate_text.flat(run)
    b4 = C['n_wider'] > 0 and C['n_silent'] < len(C['rows'])
    b5 = 'THE MIXTURE RULE, SEALED BEFORE THE READING' in gate_text.flat(run)
    b6 = 'THE SECOND BRANCH WAS TAKEN BY THE RULE SEALED BEFORE ANY ROW WAS READ' in bf
    gb = b1 and b2 and b3 and b4 and b5 and b6
    print('    verdict agrees : %s ; both others unreachable : %s / %s' % (b1, b2, b3))
    print('    the branch conditions recompute : %s ; the mixture rule applied and named : %s / %s  %s'
          % (b4, b5, b6, 'PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-ERRATA (DRAFTED and ROUTED, NOT OPENED; nothing written to ERRATA.md):')
    e1 = os.path.exists(ERRATA) and 'DRAFTED AND ROUTED' in errata and 'NOT OPENED' in errata
    e2 = 'NOTHING IS WRITTEN TO `ERRATA.md` BY THIS' in gate_text.flat(errata)
    e3 = 'NO BANKED NUMBER IS AFFECTED' in gate_text.flat(errata) and 'NO CHECK IS DEMOTED' in gate_text.flat(errata)
    e4 = 'OFFERED AND NOT APPLIED' in gate_text.flat(errata)
    era = [p for p in (os.path.join(PP, 'ERRATA.md'), os.path.join(SIDE, 'ERRATA.md')) if os.path.exists(p)]
    e5 = all(not git(os.path.dirname(p), 'diff', '--name-only', 'HEAD', '--', 'ERRATA.md').strip() for p in era)
    e6 = all(str(len(C[k])) in errata for k in ('attribution_fault', 'membership_only'))
    ge = e1 and e2 and e3 and e4 and e5 and e6
    print('    the draft exists, drafted and routed, not opened : %s ; says nothing goes to ERRATA.md : %s' % (e1, e2))
    print('    no number affected, no check demoted : %s ; the wording offered not applied : %s' % (e3, e4))
    print('    ERRATA.md files unmodified on disk (%d found) : %s ; the 3 and the 2 present : %s  %s'
          % (len(era), e5, e6, 'PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-ERRATA')

    print(chr(10) + '  G-NOEDIT-LEDGER (not one byte of the four ledgers changed but this act\'s own row and key). ### SIDE-INVARIANT.')
    fb = blob_of(PP, 'FINDINGS.md')
    fab = blob_of(PP, 'FACES_LEDGER.md')
    n1 = fb is not None and norm(io.open(FINDINGS, encoding='utf-8').read()) == norm(fb)
    n2 = fab is not None and norm(io.open(FACES, encoding='utf-8').read()) == norm(fab)
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    n3 = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    ib = blob_of(ROOT, 'tools/banked_index.py')
    n4 = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        n4 = (i == len(old))
    gnl2 = n1 and n2 and n3 and n4
    print('    FINDINGS byte-identical : %s ; FACES byte-identical : %s' % (n1, n2))
    print('    CORRESPONDENCE a true prefix of its blob : %s ; the index append-only : %s  %s'
          % (n3, n4, 'PASS' if gnl2 else '### FAIL ###'))
    if not gnl2:
        fails.append('G-NOEDIT-LEDGER')

    print(chr(10) + '  G-CONSEQUENCE (stated ONCE, plainly, with the independent-test sentence):')
    heads = re.findall(r'CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE CONSTRUCTION', bf)
    c1 = len(heads) == 1
    c2 = 'AND THE SCAN CONFIRMS IT RATHER THAN TESTING IT' in bf
    c3 = 'AN INDEPENDENT TEST WOULD REQUIRE AN OBJECT NOT BUILT AS AN AUTOCORRELATION' in bf
    c4 = 'NEEDED ONE, AND NONE IS ORDERED HERE' in bf
    c5 = 'THE SCAN CANNOT FAIL ON SUCH AN OBJECT' in bf
    gcq = c1 and c2 and c3 and c4 and c5
    print('    the consequence appears exactly once in the bank : %s (%d)' % (c1, len(heads)))
    print('    confirms-not-tests : %s ; the independent test named : %s ; none ordered : %s ; cannot fail : %s  %s'
          % (c2, c3, c4, c5, 'PASS' if gcq else '### FAIL ###'))
    if not gcq:
        fails.append('G-CONSEQUENCE')

    print(chr(10) + '  G-NOCOMPUTE (STRIPPED code: the act\'s tools import nothing that could compute):')
    forbidden = ('numpy', 'b316_instrument', 'b317_smear', 'b318_square', 'b319_stable', 'b322_ladder',
                 'b352_fit', 'scipy')
    bad2 = []
    for tool in ('b357_read.py', 'b357_extract.py'):
        code = strip_prose(t(tool))
        for f in forbidden:
            if f in code:
                bad2.append((tool, f))
    gnc = not bad2
    print('    forbidden imports in stripped code : %s  %s' % (bad2 or 'none', 'PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-ANCHORS (every anchor built by the tool; its fixtures run; refusals and count reported):')
    a1 = AF.self_test(False)
    a2 = E['without_anchor'] == 0 and E['anchors_differing'] > 0
    a3 = str(E['anchors_differing']) in bank and str(E['reads']) in bank
    ga = a1 and a2 and a3
    print('    fixtures hold : %s ; without a match : %d ; differing from their hint : %d of %d  %s'
          % (a1, E['without_anchor'], E['anchors_differing'], E['reads'], 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + '  G-DECLAREDGROUPING (the grouping is data, not a grep over prose; the incident declared):')
    lex = [r for r in C['rows'] if r['status'] == RD.WIDER
           and 'scan' in r['certifies'].lower() and 'ATTRIBUTION' in r['certifies']]
    lexset = {(r['ledger'], r['line']) for r in lex}
    dataset = {(r['ledger'], r['line']) for r in C['attribution_fault']}
    x1 = lexset != dataset
    x2 = os.path.exists(SUPER) and os.path.exists(SUPJ)
    sup = json.load(io.open(SUPJ, encoding='utf-8'))
    x3 = (sup['verdict'] == C['verdict'] and sup['n_wider'] == C['n_wider']
          and sup['n_narrower'] == C['n_narrower'] and sup['n_silent'] == C['n_silent']
          and [(r['ledger'], r['line']) for r in sup['wider']] == [(r['ledger'], r['line']) for r in C['wider']])
    x4 = 'DECLARED DATA' in bf and "b348's USE-AND-MENTION SPECIES" in bf
    x5 = str(len(dataset ^ lexset)) in bank
    x6 = 'DECLARED DATA' in C['grouping']
    gx = x1 and x2 and x3 and x4 and x5 and x6
    print('    the lexical rule and the declared data DISAGREE (so the cure was needed) : %s' % x1)
    print('    the superseded run and its JSON are on disk, unedited : %s' % x2)
    print('    verdict, counts and the five wider rows IDENTICAL in both runs : %s' % x3)
    print("    the incident and b348's species named in the bank : %s ; the mis-grouped count printed : %s  %s"
          % (x4, x5, 'PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-DECLAREDGROUPING')

    print(chr(10) + '  G-NOGRADE (no grade conferred, no verdict moved, nothing demoted):')
    g1 = 'NO GRADE IS CONFERRED' in bf and 'NOTHING IS DEMOTED' in bf
    g2 = 'NO ACT IS RE-VERDICTED' in bf
    g3 = 'Every banked number stands and every check that passed still passed' in bf
    g4 = 'NO CLASS' in bf and 'IS DISCHARGED' in bf and 'THE CLAUSE HAS NOT MOVED' in bf
    g5 = 'THE WAVE STAYS PARKED' in bf and 'NOTHING' in bf and 'DEPOSITS' in bf
    gg = g1 and g2 and g3 and g4 and g5
    print('    no grade / nothing demoted : %s ; no act re-verdicted : %s ; numbers stand : %s' % (g1, g2, g3))
    print('    no class discharged, clause unmoved : %s ; wave parked, nothing deposits : %s  %s'
          % (g4, g5, 'PASS' if gg else '### FAIL ###'))
    if not gg:
        fails.append('G-NOGRADE')

    print(chr(10) + "  G-SEALCHAIN (the seal taken only after the audit's own exit code):")
    z1 = "SEALED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK" in bf
    z2 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    z3 = "SEALED ONLY ON THE AUDIT'S OWN EXIT CODE" in rgf
    gz = z1 and z2 and z3
    print('    stated in the bank : %s ; the audit is satisfiable : %s ; sealed on it in the registration : %s  %s'
          % (z1, z2, z3, 'PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-SEALCHAIN')

    print(chr(10) + "  SELF NEEDLES (each hint resolved to the bank's own line by the step-zero tool):")
    for lbl, hint in SELF_HINTS:
        try:
            n, line = AF.find(BANK, hint)
            needle_pull.pull(BANK, line)
            print('    PASS  %-52s line %d' % (lbl, n))
        except (AF.AnchorError, LookupError) as e:
            fails.append('SELF: ' + lbl)
            print('    ### FAIL  %-52s %s' % (lbl, str(e)[:70]))

    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    print(chr(10) + '  OWNER NEEDLES (each at its emitting file, each in the extract):')
    nb2 = 0
    for label, tag, path, hint in EX.READS:
        try:
            _n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            # ### **THE EXTRACT RECORDS EACH ANCHOR TRUNCATED TO 200 CHARACTERS** (b357_extract.py's
            # ### own `line.rstrip()[:200]`), and four of the ledgers' lines are longer than that -- one
            # ### is 950 bytes. ### The arm compares against WHAT THE EXTRACT ACTUALLY WROTE, not against
            # ### a fuller string the extract never claimed to hold.
            if not quote_norm.contains(extract, line.rstrip()[:200]):
                nb2 += 1
                print('    ### FAIL (NOT IN THE EXTRACT)  %s' % label)
        except (AF.AnchorError, LookupError):
            nb2 += 1
            print('    ### FAIL (NO ANCHOR)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+ ', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines : %d'
          % (len(EX.READS), nb2 == 0, cited))
    if nb2:
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s). ### **PRE-PUSH READING CARRIES.**' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'WHAT IS WRONG IS THE WARRANT AND NOT THE CLAIM' in rows[0] and n3)
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, n3, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTSETTLED (the index):')
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : what-the-ledgers-certify returns 1 row(s), 1 required  PASS' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('the ledgers are wrong', 'the class is settled', 'the checks are demoted', 'the errata is filed'))
    k_3 = '  ### PASS' in irun
    gk = k_1 and k_2 and k_3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k_1, k_2, k_3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY')

    print(chr(10) + '  G-APPENDONLY (banked_index.py). ### **READ BEFORE THE PUSH.**')
    print('    every committed line still present, in order : %s' % n4)
    if not n4:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited; nothing outside relay/SIDE moved). ### SIDE-INVARIANT.')
    owner = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py', 'tools/b319_stable.py',
             'tools/b320_run.py', 'tools/b352_fit.py', 'tools/quote_norm.py', 'tools/run_clock.py',
             'tools/gate_text.py', 'tools/registration_gate.py', 'tools/anchor_from_file.py',
             'tools/needle_pull.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    gne = not touched and not ppstat and not tcstat
    print('    owner instruments modified : %s ; papers dirty : %s ; TECHNE dirty : %s  %s'
          % (touched or 'none', ppstat or 'none', tcstat or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-NOHOOK (nothing written to the papers repo, so hook and mirror NOT owed -- CHECKED):')
    h1 = not ppstat
    h2 = git(PP, 'log', '-1', '--format=%H').strip() == git(PP, 'rev-parse', 'origin/main').strip()
    h3 = 'NOT OWED' in (rows[0] if rows else '')
    gho = h1 and h2 and h3
    print('    papers tree clean : %s ; HEAD equals remote : %s ; the row says NOT OWED : %s  %s'
          % (h1, h2, h3, 'PASS' if gho else '### FAIL ###'))
    if not gho:
        fails.append('G-NOHOOK')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0]
                               .encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and E['run_clock'] < stampm.group(1) < C['run_clock']
    o4 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    extract %s < seal < reading %s : %s ; JOINTLY SATISFIABLE : %s'
          % (E['run_clock'], C['run_clock'], o3, o4))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks = [('the seal hash', SEAL in bank),
              ('the seal stamp', (stampm.group(1) if stampm else 'x') in bank),
              ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
              ('row %s' % ROWNUM, ('row %s' % ROWNUM) in bank and bool(rows)),
              ('the extract, reading and superseded clocks',
               E['run_clock'] in bank and C['run_clock'] in bank and sup['run_clock'] in bank),
              ('the reads and the differing anchors', str(E['reads']) in bank and str(E['anchors_differing']) in bank),
              ('the three counts 5/6/1', ('%d WIDER / %d NARROWER / %d SILENT'
                                          % (C['n_wider'], C['n_narrower'], C['n_silent'])) in bank),
              ('rows located and unclassified', str(len(C['rows'])) in bank and 'ZERO UNCLASSIFIED' in bf),
              ('the 3 and the 2', str(len(C['attribution_fault'])) in bank and str(len(C['membership_only'])) in bank)]
    for r in C['wider']:
        checks.append(('%s:%d printed' % (r['ledger'], r['line']),
                       ('%s : %d' % (r['ledger'], r['line'])) in bank
                       or ('%s:%d' % (r['ledger'], r['line'])) in bank))
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the reading ran twice; the RELIED-ON run file identified by its own clock):')
    # ### **THE ARM THAT WOULD HAVE CAUGHT THE MIS-POINTING:** the run file this suite reads must carry
    # ### the SAME clock the relied-on JSON records. ### The suite was pointed at the FIRST run until
    # ### this was checked, which is b356's notes2/notes3 species.
    runhead = io.open(RUN, encoding='utf-8').readline()
    q1 = C['run_clock'] in runhead
    q2 = os.path.exists(SUPER) and os.path.exists(RUN) and os.path.exists(d('b357_read_run.txt'))
    q3 = (io.open(SUPER, encoding='utf-8').read()
          == io.open(d('b357_read_run.txt'), encoding='utf-8').read())
    q4 = 'THE SUPERSEDED RUN IS KEPT UNEDITED' in bf and 'THE RELIED-ON READING' in bf
    q5 = os.path.basename(RUN) in bank and 'BYTE-IDENTICAL COPIES OF ONE RUN' in bf
    once = q1 and q2 and q3 and q4 and q5
    print('    the run file carries the relied-on JSON clock %s : %s' % (C['run_clock'], q1))
    print('    both runs on disk : %s ; the two first-run copies are byte-identical : %s' % (q2, q3))
    print('    declared in the bank : %s / %s  %s' % (q4, q5, 'PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM:')
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
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### WHAT THE LEDGERS SAY THE CHECKS CERTIFY (b357).'
    nxt = '# ### THE OBJECT OR THE BOUNDARY (b356).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if marker in idx and nxt in idx else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
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

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b357_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
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
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
