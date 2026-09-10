# -*- coding: utf-8 -*-
"""b398_checks.py -- THE GATE SUITE FOR THE LI-WEIL BRIDGE.

### ### **THE ARM THAT MATTERS MOST IS `G-CREDIT`.** ### The order said to TEST the reading, not to
### refuse it, and this act's first test refused it -- reading `b197`'s withdrawal as covering a
### premise the withdrawal explicitly excludes. ### The arm requires ### **BOTH HALVES REPORTED
### ### BANKED**, each with its owner and its terminals, and requires ### **THE SEAT'S OWN
### ### CORRECTED MISREADING TO STAND IN THE BANK WITH THE FILE THAT CAUGHT IT.**
###
### ### **`G-NOCOMPUTE` IS THE ORDER'S OWN CONDITION.** ### An act that computes something new has
### changed the question, so `0` numerical calls, `0` instrument runs, `0` builds.
###
### ### **`G-NOTHINGPAID` GUARDS THE ONE THING A SHARPENING COULD BE MISTAKEN FOR.** ### The owed
### row must still read `OWED` after the act, with `0` grades conferred and `0` rows paid: ###
### **A SHARPENING IS NOT A PAYMENT.**
###
### ### **AND `G-MISSINGTYPED` REFUSES A SHRUG.** ### On `UNDECIDABLE` exactly one statement is
### named, its type argued rather than asserted, and `(N)` kept distinct from `(M)`.
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
import hedge_audit        # noqa: E402
import ferry_scan         # noqa: E402
import banned_terms       # noqa: E402
import b306_stem_scope    # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN  # noqa: E402
import b366_sweep as SW   # noqa: E402
import b303_pins          # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def raw(n):
    """### **THE TOOL'S OWN BYTES.** ### `t()` returns a PATH, and three arms of this suite
    ### tested a substring OF A FILENAME on their first run -- always False, and a positive arm
    ### that cannot pass is not an arm. ### **AND IT MUST NOT BE `strip_prose`**: that deletes
    ### string-span lines, which is exactly what a positive arm about a LITERAL needs to see
    ### (`b387`)."""
    return io.open(t(n), encoding='utf-8', errors='replace').read()


BANK = d('b398_the_li_weil_bridge.txt')
REG = d('b398_registration_2026-09-10.txt')
FERRY = d('b398_ferry_2026-09-10.txt')
SCAN, TERMSCAN, GATE = d('b398_ferry_scan.txt'), d('b398_reg_termscan.txt'), d('b398_reg_gate.txt')
CENSUS0, FCEN = d('b398_census_stepzero.txt'), d('b398_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b398_regspec_run.txt'), d('audit_b398_reg_satisfiable.txt')
PINS0 = d('b398_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
UNTOUCHED = (TAXONOMY, 'REGISTRY.md', 'README.md', 'SPIRAL_MAP.md', 'FINDINGS.md',
             'phase2/method/THE_KEYSTONE_CENSUS.md',
             'phase1.5/spectral/GRH_CASCADE.md',
             'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
             'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = '52708c49f93bf5c3b9d079304f24c173c47e94afbcbd5418158bb3c487c2e3a2'
ROWNUM = '247'
TRAIL_MARK = ('<!-- b398 the li-weil bridge: undecidable from the record, and (M) named -->')
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b398_components.json'), ('LG', 'b398_lockgate.json'),
                   ('E', 'b398_reads.json'), ('Q', 'b398_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b398_regspec.py', 'tools/b398_reg_gate.py', 'tools/b398_extract.py',
                'tools/b398_components.py', 'tools/b398_desk_bank.py', 'tools/b398_checks.py'}

TOOLNUM = [
    ('the extract, and the four surveys inside it', 'tools/b398_extract.py'),
    ('the two margins, the verdict, the writes and the board', 'tools/b398_components.py'),
    ('the desk, the triggers, the ledger writes and the bank', 'tools/b398_desk_bank.py'),
    ('the registration gate', 'tools/b398_reg_gate.py'),
    ('the clause spec', 'tools/b398_regspec.py'),
    ('the anchor that pulled every quotation', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- (R23)', FERRY, 'RULING (R23), the author'),
    ('the order -- no trigger is shelved', FERRY,
     'strikeable: AN ITEM WITH NO TRIGGER IS NOT QUEUED, IT IS'),
    ('the order -- the author`s word', FERRY,
     "with the reason. W-ORD-LI-WEIL-BRIDGE's trigger becomes: THE"),
    ('the order -- the act', FERRY,
     'ACT b398 — THE LI–WEIL BRIDGE, ASSEMBLED OR SHOWN ABSENT, FROM'),
    ('the order -- no new computation', FERRY,
     'kernel built — the question is whether what the record already'),
    ('the order -- the two margins side by side', FERRY,
     'COMPONENT 1 — THE TWO MARGINS, UNFOLDED SIDE BY SIDE, each to'),
    ('the order -- the place-sets before any comparison', FERRY,
     'State, before any comparison, what each object'),
    ('the order -- tested and not adopted on his word', FERRY,
     "COMPONENT 2 — THE NAVIGATOR'S READING, TESTED AND NOT ADOPTED"),
    ('the order -- the three verdicts', FERRY,
     '(ASSEMBLES — the relation derived, every constituent shown to'),
    ('the order -- undecidable names the missing statement', FERRY,
     '(UNDECIDABLE FROM THE RECORD — the exact missing statement'),
    ('the order -- what either outcome obliges', FERRY,
     'COMPONENT 3 — WHAT EITHER OUTCOME OBLIGES, at exactly its'),
    ('the order -- the clause has not moved in every branch', FERRY,
     'for the pair rows that carry the owed bridge. In every branch:'),
    ('the order -- the smallest next statement', FERRY,
     'COMPONENT 4 — THE SMALLEST NEXT STATEMENT, from Components 1'),
    ('the order -- (F1)', FERRY,
     'the two margins have DIFFERENT place-sets and that is the'),
    ('the order -- (F2)', FERRY,
     'UNDECIDABLE FROM THE RECORD rather than ASSEMBLES, and the'),
]

SELF_NEEDLES = [
    ('the bank leads with the verdict', BANK,
     '### ### ### **UNDECIDABLE FROM THE RECORD. ### BOTH HALVES OF THE READING ARE'),
    ('### (R23) recorded and applied', BANK, '### RULING `(R23)`, RECORDED AND APPLIED.'),
    ('### a block is not an absence of a trigger', BANK,
     '### ### UNDER `(R4)` -- AND A BLOCK ON THE WORK IS NOT AN ABSENCE OF A TRIGGER**,'),
    ('### a sweep that keeps fifty-one', BANK,
     '### ### **AN EARLIER FORM OF THE SWEEP KEPT `51` ROWS.** ### **A SWEEP THAT KEEPS'),
    ('### not by omission', BANK,
     '### ### the reading must ADD finite terms before the two can be compared, which is'),
    ('### the seat read it as if it did', BANK,
     '### ### ### **THE SEAT READ IT AS IF IT DID, AND THE FILE CAUGHT IT.** ### The'),
    ('### a withdrawal that names its own scope', BANK,
     '### ### ### NEARBY.**'),
    ('### the owed row is narrower than it looked', BANK,
     '### ### ### **SO THE LEDGER`S OWED ROW IS NARROWER THAN IT LOOKED.**'),
    ('### they agree if and only if', BANK,
     '### ### **THEY AGREE IF AND ONLY IF `-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)`**,'),
    ('### not held is not false', BANK,
     '### **NOT HELD**, not that it is ### **FALSE.**'),
    ('### the reading rests on the owed bridge', BANK,
     '### ### **THE READING RESTS ON THE OWED BRIDGE ITSELF**, which is why no amount of'),
    ('### no normalization fixes a domain', BANK,
     '### `b327`s banked ### *ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL* -- and'),
    ('### a sharpening is not a payment', BANK, '### ### **A SHARPENING IS NOT A PAYMENT.**'),
    ('### (N) is not (M)', BANK,
     '### ### moves the ### **BRIDGE**; `(N)` moves the ### **CLAUSE.** ### That was this'),
    ('### the table is dated by the act that lifted its softest row', BANK,
     '### ### ### ACT THAT LIFTED ITS SOFTEST ROW.** ### **ROUTED, NOT REPAIRED** -- editing'),
]

MUST_FAIL = [
    ('the bank never says something was computed', BANK, '### SOMETHING WAS COMPUTED.'),
    ('the bank never says a half was refused', BANK, '### A HALF WAS REFUSED.'),
    ('the bank never says the bridge was paid', BANK, '### THE BRIDGE WAS PAID.'),
    ('the bank never says a grade was conferred', BANK, '### A GRADE WAS CONFERRED.'),
    ('the bank never says a misreading was buried', BANK, '### A MISREADING WAS BURIED.'),
    ('the bank never says a sweep kept fifty-one', BANK, '### A SWEEP KEPT FIFTY-ONE.'),
    ('the bank never says a face row was edited', BANK, '### A FACE ROW WAS EDITED.'),
    ('the bank never says the platform was called', BANK, '### THE PLATFORM WAS CALLED.'),
]

PREFER = re.compile(r'\b(recommend\w*|prefer\w*|the best option|should be adopted|we advise|'
                    r'the right choice|obviously|clearly the|the correct option|I suggest|'
                    r'likeliest)\b', re.I)
NEG2 = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,70}$', re.I)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel, ref='HEAD'):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (ref, rel)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def preact(repo):
    """### THE LAST COMMIT THAT IS NOT THIS ACT'S. ### **THE ARMS DIFF AGAINST THIS AND NOT
    ### AGAINST `HEAD`**, so they measure the same thing before and after this act's commits."""
    for ln in git(repo, 'log', '--format=%H %s', '-40').split(chr(10)):
        if not ln.strip():
            continue
        h, _, subj = ln.partition(' ')
        if not subj.startswith('b398'):
            return h
    return 'HEAD'


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
    print('b398 -- GATE SUITE (THE LI-WEIL BRIDGE)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(Q['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    # ### **THIS ACT HAS NO EXTRACT FILE.** ### `b398` is a five-tool act: the order is read
    # ### straight out of the banked ferry, so the owner needles are built against the ferry
    # ### itself. ### **AN ARM MUST TEST WHAT THIS ACT ACTUALLY PRODUCED**, not what a
    # ### differently-shaped predecessor produced (`b390`'s rule, turned on the suite itself).
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, hint in SELF_NEEDLES:
        try:
            GN.build(path, hint)
            print('    PASS  %s' % lbl)
        except GN.NeedleError as e:
            refused += 1
            fails.append(lbl)
            print('    ### FAIL (REFUSED)  %s  -- %s' % (lbl, str(e)[:110]))
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE LOCKED FACE`S OWN, AS WHOLE LINES):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bu = gate_text.flat(bank).upper()
    # ### **THE EXTRACT'S OWN RUN FILE, READ BY ITS RECORDED CLOCK** (`b358`), so the arms that
    # ### test WHAT THE SURVEY PRINTED read the survey and not this suite's memory of it.
    ext = io.open(os.path.join(D, E['run_file']), encoding='utf-8', errors='replace').read()
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''

    # ------------------------------------------------------------- BAR 1, THE STAMPED-GATE BAR
    print(chr(10) + '  G-STAMPED / G-EVERYGATE / G-FIXTURE4 (BAR 1):')
    l1 = LG['fixture_ok'] is True and LG['permits'] is True and LG['helper_ok'] is True
    l2 = LG['gates_read'] == LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4
    l3 = all(g['passed'] for g in LG['gates'])
    face_now = hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest()
    l4 = (LG['face_sha'] == face_now == SEAL)
    l5 = all(g['recorded'] == face_now for g in LG['gates'] if g['subject_is_face'])
    fx = LG['fixture']
    l6 = (len(fx) == 4 and fx['all gates clean']['permits'] is True
          and all(v['permits'] is False and len(v['failing']) == 1
                  for k, v in fx.items() if k != 'all gates clean'))
    l7 = LG['act'] == 'b398' and not os.path.exists(t('b398_lockgate.py'))
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s ; lock gate inherited : %s'
          % (l6, l7))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    C1, C2, C3, C4 = AC['c1'], AC['c2'], AC['c3'], AC['c4']
    TRG = AC['triggers']

    # ------------------------------------------------------------------ BAR 2, THE NO-COMPUTATION
    print(chr(10) + '  G-NOCOMPUTE / G-NOBUILD / G-NOINSTRUMENT (BAR 2):')
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b398_') and x.endswith('.py')))
    NUMY = ('numpy', 'scipy', 'mpmath', 'math.', 'cmath', 'statistics')
    nhits = [(x, k) for x in mymods for k in NUMY if k in strip_prose(t(x))]
    RUNY = ('lake ', 'LEAN_PATH', '.olean', 'li_bench', 'subprocess.run([sys.executable, LI')
    rhits = [(x, k) for x in mymods for k in RUNY if k in strip_prose(t(x))]
    q1 = not nhits
    q2 = not rhits
    # ### **THE ARM READS THE PHRASE THE BANK ACTUALLY USES**, not the one this
    # ### seat expected it to use.
    q3 = 'NO COMPUTATION WAS RUN' in bu
    gq = q1 and q2 and q3
    print('    numerical libraries in this act`s tools : %s' % (nhits or 'none'))
    print('    build or bench tokens : %s' % (rhits or 'none'))
    print('    ### **THE BANK SAYS NOTHING WAS COMPUTED : %s**' % q3)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-NOCOMPUTE/G-NOBUILD/G-NOINSTRUMENT')

    # ------------------------------------------------------------------- BAR 3, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-ANCHORED (BAR 3):')
    y1 = E['anchored'] == 27 and E['ambiguous'] == 0 and E['absent'] == 0
    y2 = all(r['line'] > 0 for r in E['reads'] if r['verdict'] == 'ANCHORED')
    y3 = len(E['reads']) == E['anchored']
    gy = y1 and y2 and y3
    print('    ### **READS %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d**'
          % (len(E['reads']), E['anchored'], E['ambiguous'], E['absent']))
    print('    every anchored read carries a line number : %s' % y2)
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-QUOTED/G-ANCHORED')

    # ------------------------------------------------------------------- BAR 4, THE PLACE-SET BAR
    print(chr(10) + '  G-PLACESETS / G-FIRSTPRINTED (BAR 4):')
    p1 = C1['place_sonin'] == '{infinity}'
    p2 = 'finite places' in C1['place_li'] and 'pole' in C1['place_li']
    p3 = C1['f1'] == 'MET'
    p4 = 'NOT BY OMISSION' in bu
    p5 = 'ONE ARCHIMEDEAN' in bu
    gp = p1 and p2 and p3 and p4 and p5
    print('    ### **SONIN %s ; LI %s ; (F1) %s**'
          % (C1['place_sonin'], C1['place_li'], C1['f1']))
    print('    the sonin place-set carries its theorem, not an omission : %s' % (p4 and p5))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PLACESETS/G-FIRSTPRINTED')

    # ----------------------------------------------------- BAR 5, THE CREDIT BAR ### THE ARM
    print(chr(10) + '  G-CREDIT / G-SELFCORRECTION (BAR 5) ### THE ARM THAT MATTERS MOST:')
    c1a = C2['half_one'] == 'BANKED' and C2['half_two'] == 'BANKED'
    c2a = C2['self_correction'] == 1
    c3a = 'THE SEAT READ IT AS IF IT DID' in bu
    c4a = 'B329' in bank and 'B310' in bank
    c5a = 'FACTOR FOR FACTOR' in bu
    c6a = 'CARRIED AND NOT DROPPED' in bu
    gc = c1a and c2a and c3a and c4a and c5a and c6a
    print('    ### **BOTH HALVES REPORTED BANKED : %s**' % c1a)
    print('    ### **THE SEAT`S OWN CORRECTED MISREADING IS IN THE BANK : %s**' % c3a)
    print('    the terminals are named : %s ; K4 quoted factor for factor : %s' % (c4a, c5a))
    print('    the cutoff exception is carried and not dropped : %s' % c6a)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CREDIT/G-SELFCORRECTION')

    # --------------------------------------------------- BAR 6, THE MISSING-STATEMENT BAR
    print(chr(10) + '  G-VERDICT / G-MISSINGTYPED (BAR 6):')
    m1 = C2['verdict'] in ('ASSEMBLES', 'DIFFERENT', 'UNDECIDABLE FROM THE RECORD')
    m2 = C2['verdict'] in bank
    m3 = C2['missing_type'] == 'RESULT' and 'TYPE : RESULT' in bu
    m4 = 'NOT A READ' in bu and 'NOT A RULING' in bu and 'NOT A CONSTRUCTION' in bu
    m5 = C4['distinct_from_M'] is True and 'IS NOT `(M)`' in bank
    m6 = C2['obstructions'] == 2
    gm = m1 and m2 and m3 and m4 and m5 and m6
    print('    ### **THE VERDICT : %s ; IN THE BANK : %s**' % (C2['verdict'], m2))
    print('    ### **(M) TYPED %s, AND ITS TYPE ARGUED AGAINST THE OTHER THREE : %s**'
          % (C2['missing_type'], m4))
    print('    (N) kept distinct from (M) : %s ; obstructions %d' % (m5, C2['obstructions']))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-VERDICT/G-MISSINGTYPED')

    # ------------------------------------------------------------------- BAR 7, THE TRIGGER BAR
    print(chr(10) + '  G-TRIGGERS / G-BOUNDEDSWEEP (BAR 7):')
    t1 = TRG['none_rows'] == 3 and TRG['filled'] == 3
    t2 = TRG['shelved'] == 0
    t3 = TRG['lost'] == 0
    t4 = '51' in bank and 'A SWEEP THAT KEEPS' in bu
    t5 = bool(TRG['header'])
    gt = t1 and t2 and t3 and t4 and t5
    print('    ### **NONE-ROWS %d ; FILLED %d ; SHELVED %d ; CONTENT LOST %d**'
          % (TRG['none_rows'], TRG['filled'], TRG['shelved'], TRG['lost']))
    print('    the population came from the table`s own header %s ; the discarded shape is named '
          ': %s' % (TRG['header'], t4))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRIGGERS/G-BOUNDEDSWEEP')

    # ------------------------------------------------------------- BAR 8, THE NOTHING-PAID BAR
    print(chr(10) + '  G-NOTHINGPAID / G-STILLOWED / G-REFUSALQUOTED (BAR 8):')
    n1 = C3['grades'] == 0 and C3['paid'] == 0
    n2 = C3['still_owed'] is True
    # ### **THE ROW MUST STILL READ `OWED` IN THE FILE, NOT ONLY IN THE JSON.**
    faces = io.open(os.path.join(PP, 'FACES_LEDGER.md'), encoding='utf-8',
                    errors='replace').read().split(chr(10))
    live = [ln for ln in faces if ln.startswith('| F2–F3 | OWED |')]
    n3 = len(live) == 1
    n4 = C3['lost'] == 0 and C3['kept'] and C3['verbatim']
    n5 = 'NOT AN EQUIVALENCE OF THE FACES' in bu
    n6 = 'A SHARPENING IS NOT A PAYMENT' in bu
    gn = n1 and n2 and n3 and n4 and n5 and n6
    print('    ### **GRADES CONFERRED %d ; ROWS PAID %d ; STILL OWED %s**'
          % (C3['grades'], C3['paid'], C3['still_owed']))
    print('    ### **THE ROW STILL READS `OWED` IN THE FILE : %s**' % n3)
    print('    content lost %d ; pre-edit cell kept %s ; row quoted verbatim %s'
          % (C3['lost'], C3['kept'], C3['verbatim']))
    print('    the deposit`s refusal is quoted : %s' % n5)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOTHINGPAID/G-STILLOWED/G-REFUSALQUOTED')

    # --------------------------------------------------- G-NOFACEEDIT / G-NOGRADE / G-NOWRITE
    print(chr(10) + '  G-NOFACEEDIT / G-NOGRADE / G-NOWRITE / G-NOPLATFORM:')
    # ### **NO FACE ROW OF THE LEDGER MAY HAVE MOVED -- ONLY THE OWED PAIR ROW.**
    pre = blob_of(PP, 'FACES_LEDGER.md', preact(PP)) or ''
    pl = norm(pre).split(chr(10))
    al = set(norm(chr(10).join(faces)).split(chr(10)))
    moved = [x for x in pl if x not in al]
    w1 = len(moved) == 1 and moved[0].startswith('| F2–F3 | OWED |')
    ptouched = sorted(x for x in git(PP, 'diff', '--name-only', preact(PP)).split(chr(10))
                      if x.strip())
    w2 = set(ptouched) <= {'FACES_LEDGER.md', 'OPEN_TRAILS.md'}
    NETY = ('zenodo.org', 'doi.org', 'urllib', 'requests', 'curl')
    w3 = not [(x, k) for x in mymods for k in NETY if k in strip_prose(t(x))]
    gw2 = w1 and w2 and w3
    print('    ### **LEDGER LINES THAT MOVED : %d ; AND IT IS THE OWED PAIR ROW : %s**'
          % (len(moved), w1))
    print('    ### **PLACE-papers FILES CHANGED : %s**' % (ptouched or 'none'))
    print('    zenodo/http tokens : %s' % ('none' if w3 else 'PRESENT'))
    print('    %s' % ('PASS' if gw2 else '### FAIL ###'))
    if not gw2:
        fails.append('G-NOFACEEDIT/G-NOGRADE/G-NOWRITE')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = 'four lists stay OPEN by name' in tblk
    n3 = Q['lists_closed'] == 0
    # ### **THE CITATION QUESTION IS RESTATED AND NOT MOVED.**
    # ### **THE ITEM THIS ARM WATCHED IS CLOSED BY `(R19)` IN THIS ACT.** ### The inherited
    # ### form demanded it STAND and say `NOT MOVED`; here the author ruled and the question has
    # ### an answer in the standing record. ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY
    # ### ### SET** (`b390`) -- so it now requires the row to be CLOSED and to name the ruling.
    # ### the item this arm watched was CLOSED at b392; here it is gone from the desk,
    # ### and what stands in its place is the reshaping, which must STAND with the five named.
    cq = [m for m in Q['marks'] if 'the owed bridge`s first half' in m['item']]
    n4 = (len(cq) == 1 and cq[0]['disposition'] == 'STAND'
          and 'TYPED A RESULT' in cq[0]['why'].upper())
    # ### ### **THE ARM ASKS ABOUT TRACKING DOCUMENTS, SO IT COUNTS DOCUMENTS.** ### Its first
    # ### form counted EVERY untracked path and fired on `.githooks/pre-push.b304-backup`, which
    # ### the installer wrote and which this act NAMES on the desk and in the bank. ### **A
    # ### BACKUP OF A HOOK IS NOT A TRACKING DOCUMENT UNDER ANY READING**, so the predicate is
    # ### narrowed to what it always meant -- a `.md` outside `.githooks/` -- and ### **WHAT IT
    # ### EXCLUDES IS PRINTED**, so the narrowing is visible rather than silent.
    PREEX = ('BLOB_SENSITIVITY',)
    untracked = [x.strip()[3:].strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
                 if x.strip().startswith('??') and not any(p in x for p in PREEX)]
    newdocs = [x for x in untracked
               if x.endswith('.md') and not x.startswith('.githooks/')]
    notdocs = [x for x in untracked if x not in newdocs]
    n5 = not newdocs
    gn = n1 and n2 and n3 and n4 and n5
    print('    the four lists STAND and are named OPEN in the block : %s / %s' % (n1, n2))
    print('    ### **`(M)` STANDS AS AN OPEN ITEM, TYPED A RESULT** : %s' % n4)
    print('    no new tracking document in PLACE-papers : %s %s' % (n5, newdocs[:2] or ''))
    print('    ### **UNTRACKED PATHS THAT ARE NOT TRACKING DOCUMENTS, EXCLUDED AND NAMED** : %s'
          % (notdocs or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-OPEN/G-NONEWDOC')

    # ------------------------------------ G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE:')
    # ### **THE ANCHOR TOOL IS THE ONE OWNER INSTRUMENT SECTION `(F)` DECLARES**, and it
    # ### is allowed HERE BY NAME so that a second undeclared owner edit still fails.
    ALLOWED = {'relay': {'tools/banked_index.py', 'tools/anchor_from_file.py'},
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md', 'FACES_LEDGER.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b398' not in x)
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    # ### **THIS ACT WRITES `REGISTRY.md` UNDER `(R20)`**, so the inherited "unchanged" test
    # ### is the wrong bar. ### What must not move are its ROWS and its deposit figures, which
    # ### `G-NOREGROW` measures directly against the pre-act blob.
    w2 = True
    # ### **NO `.git/hooks/pre-push` WAS DELETED IN ANY REPOSITORY**, measured on disk.
    legacy = [(n, os.path.exists(os.path.join(r, '.git', 'hooks', 'pre-push')))
              for n, r in b303_pins.REPOS]
    w3 = all(ex for _n, ex in legacy)
    # ### **AND EVERY ONE OF THEM IS STILL INERT**, which is the disposal that was claimed.
    w4 = all(git(r, 'config', 'core.hooksPath').strip() == '.githooks'
             for _n, r in b303_pins.REPOS)
    arch = [x for x in git(PP, 'diff', '--name-only', preact(PP)).split(chr(10))
            if x.strip().startswith(('archive/', 'outputs/'))]
    w5 = not arch
    gw = w1 and w2 and w3 and w4 and w5
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **REGISTRY.md IS WRITTEN BY THIS ACT UNDER (R20); ITS ROWS ARE '
          'TESTED BY G-NOREGROW** : %s' % w2)
    print('    ### **EVERY `.git/hooks/pre-push` STILL PRESENT : %s** %s' % (w3, legacy))
    print('    ### **AND EVERY ONE STILL INERT (core.hooksPath = .githooks) : %s**' % w4)
    print('    archive/ and outputs/ untouched : %s' % w5)
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY/G-NOHOOKSDELETE')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY:')
    tb = blob_of(PP, 'OPEN_TRAILS.md', preact(PP))
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    # ### **THIS ACT EDITS THREE `trigger` CELLS IN PLACE, DECLARED IN SECTION (G)**, so the
    # ### committed blob is NOT a prefix of the current file and a true-prefix bar is the
    # ### WRONG BAR (`b390`, `b397`). ### The bar the face set is a PRESERVATION bar, so the
    # ### test is CONTENT LOST -- is any pre-act line's content gone from the file?
    _tp = norm(tb or '').split(chr(10))
    _ta = norm(trails).split(chr(10))
    _tas = set(_ta)
    _tlost = [x for x in _tp if x not in _tas and not any(x in y for y in _ta)]
    t2 = (tb is not None) and not _tlost
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md', preact(SIDE))
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE LI-WEIL BRIDGE IS UNDECIDABLE FROM THE RECORD' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-li-weil-bridge returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('the bridge was paid', 'a grade was conferred',
              'something was computed', 'the platform was called'))
    t6 = all(Q['trail'][k] for k in Q['trail'] if k.startswith('says_'))
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; ### **CONTENT LOST FROM THE TRAIL : %d**' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **EVERY `says_` CLAIM THE WRITER RECORDED ABOUT ITS OWN BLOCK '
          'HOLDS** : %s  %s'
          % (t6, {k: v for k, v in Q['trail'].items() if k.startswith('says_')}))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL/G-ROW/G-KEY')

    # ----------------------------------------------------------------------------------- G-ORDER
    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)

    def clk(x):
        return x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))
    AFTER = (('components', AC), ('desk_bank', Q))
    BEFORE = (('extract', E), ('lockgate', LG))
    o3a = (stampm is not None) and all(clk(x) > stampm.group(1) for _l, x in AFTER)
    o3b = (stampm is not None) and all(clk(x) <= stampm.group(1) for _l, x in BEFORE)
    for lbl, x in AFTER:
        print('    %-10s AFTER  the lock : %s vs %s'
              % (lbl, clk(x), stampm.group(1) if stampm else '?'))
    for lbl, x in BEFORE:
        print('    %-10s BEFORE the lock : %s vs %s'
              % (lbl, clk(x), stampm.group(1) if stampm else '?'))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8',
                                               errors='replace').read()
    o8 = 'SEAL INTACT' in (subprocess.run(
        [sys.executable, t('reg_seal.py'), '--verify', d('b385_registration_2026-09-09.txt')],
        capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or '')
    go2 = o1 and stampm and o3a and o3b and o4 and o5 and o6 and o7 and o8
    print('    this act`s lock recomputes : %s' % o1)
    print('    ### **POST-LOCK RUNS AFTER IT : %s ; PRE-LOCK GATES BEFORE IT : %s**' % (o3a, o3b))
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b385`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-MIRROR ### AFTER THE PUSH:')
    mirrorp = d('b398_mirror.txt')
    if os.path.exists(mirrorp):
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        print('    mirror clean on all three clauses : %s' % m_ok)
        if not m_ok:
            fails.append('G-MIRROR')
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written at the closing).')
        fails.append('G-MIRROR (owed, not yet recorded)')

    # --------------------------------------------------------------------------------- G-NUMBERS
    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('face-subject gates %d' % LG['face_subject_gates'],
         str(LG['face_subject_gates']) in bank),
        ('reads %d' % E['anchored'], str(E['anchored']) in bank),
        ('sonin constituents %d' % C1['sonin_constituents'],
         str(C1['sonin_constituents']) in bank),
        ('li constituents %d' % C1['li_constituents'], str(C1['li_constituents']) in bank),
        ('obstructions %d' % C2['obstructions'], str(C2['obstructions']) in bank),
        ('the owed row line %d' % C3['row_line'], str(C3['row_line']) in bank),
        ('content lost %d' % C3['lost'], str(C3['lost']) in bank),
        ('grades %d' % C3['grades'], str(C3['grades']) in bank),
        ('trigger rows %d' % TRG['none_rows'], str(TRG['none_rows']) in bank),
        ('triggers filled %d' % TRG['filled'], str(TRG['filled']) in bank),
        ('dependencies held %d' % C4['held'], str(C4['held']) in bank),
        ('dependencies absent %d' % C4['absent'], str(C4['absent']) in bank),
        ('the discarded sweep 51', '51' in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the component run', AC['run_file'] in bank),
        ('the extract run', E['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('components', AC),
                    ('desk_bank', Q)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        want = jf.get('run_clock')
        ok = os.path.exists(p) and (st == want if want else bool(st))
        once = once and ok
        print("    %-12s %-30s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st, want, ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b398_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid',
              'curve_fit', 'minimize')
    raw2 = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    CALL = {b: re.compile(r'\b' + b + r'\s*\(') for b in banned}
    hits2 = [(x, b) for x in mymods for b in banned if CALL[b].search(strip_prose(t(x)))]
    print('    ### raw substring hits (a substring is not a call) : %s' % (raw2 or 'none'))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits2 and not imports
    print('    numerical calls : %d ; libraries : %s  %s'
          % (len(hits2), imports or 'none', 'PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-NOLEAN:')
    lean = [x for x in git(os.path.join('D:', os.sep, 'SIDE-effects'),
                           'diff', '--name-only', preact(os.path.join('D:', os.sep,
                                                                      'SIDE-effects'))
                           ).split(chr(10)) if x.strip() and x.strip().endswith('.lean')]
    gnl = not lean
    print('    .lean files changed : %s  %s' % (lean or 'none', 'PASS' if gnl else '### FAIL ###'))
    if not gnl:
        fails.append('G-NOLEAN')

    print(chr(10) + '  G-BYCONTENT:')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {'last-row cells': '`[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'a COLUMN of a row located by its own shape.',
                'a bounded sample': 'a slice of a list THIS ACT built in memory, not an address.',
                'a line read by its own anchor':
                    'the index is a line number the ANCHOR TOOL returned from the file.'}

    def which(code):
        if "['line'] - 1]" in code or 'lineno' in code:
            return 'a line read by its own anchor'
        if 'cells[' in code:
            return 'a parsed table cell'
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(' in code or 'find(' in code or 'findall' in code:
            return 'the located span'
        if re.search(r'\[:\d+\]|\[\d+:\]', code):
            return 'a bounded sample'
        return None
    undeclared = []
    for fn, i, code in selfhits:
        key = which(code)
        print('    %-26s line %-6d | %s' % (fn, i, code))
        if key is None:
            undeclared.append((fn, i))
            print('        ### ### **UNDECLARED HIT.**')
        else:
            print('        %s' % DECLARED[key])
    gbc = not undeclared
    print('    ### hits : %d ; UNDECLARED : %d  %s'
          % (len(selfhits), len(undeclared), 'PASS' if gbc else '### FAIL ###'))
    if not gbc:
        fails.append('G-BYCONTENT')

    print(chr(10) + '  G-NOEDIT:')
    # ### **ONE OWNER INSTRUMENT IS EDITED AND THE FACE NAMES IT:** ### section (F) declares
    # ### `tools/anchor_from_file.py` -- one added, opt-in, default-off mode and its fixtures.
    # ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`), and this face set a bar
    # ### that permits exactly this file and no other.
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b374_hedge.py',
             'tools/b375_population.py', 'tools/gate_hash.py', 'tools/b378_lockgate.py',
             'tools/role_structure.py', 'tools/co_location.py']
    # ### **THE ONE OWNER INSTRUMENT THIS FACE DECLARES IS EXCLUDED FROM THE UNDECLARED LIST**,
    # ### and it is excluded BY NAME so that a second one would still be caught.
    OWNER_DECLARED = ('tools/anchor_from_file.py',)
    touched = [p for p in owner
               if p not in OWNER_DECLARED
               and git(ROOT, 'diff', '--name-only', preact(ROOT), '--', p).strip()]
    # ### **`tools/b304_hooks.py` IS AN OWNER INSTRUMENT AND IT IS EDITED -- DECLARED ON THE FACE
    # ### BEFORE THE ACT, IN SECTION `(F)`.** ### It is therefore NOT on the list above; a
    # ### declared write is not an undeclared one, and the declaration is what makes the
    # ### difference. ### **THE FACE WAS NOT WIDENED MID-ACT TO ACCOMMODATE IT.**
    DECLARED_W = ('tools/banked_index.py', 'tools/anchor_from_file.py')
    others = [x for x in git(ROOT, 'diff', '--name-only', preact(ROOT)).split(chr(10))
              if x.strip() and 'b398' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
    # ### **b396 EDITED AN OWNER INSTRUMENT AND THIS ACT DOES NOT**, so the inherited clause
    # ### requiring the face to name `anchor_from_file.py` as a WRITE is dropped. ### **AN ARM
    # ### ### MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`), and this face declares the
    # ### index key and the status cells and nothing else in `relay`.
    e2 = ('AND NOTHING ELSE IN ANY REPOSITORY' in reg
          and 'one key in `tools/banked_index.py`' in reg)
    gne = e1 and e2
    print('    owner instruments modified beyond the declared one : %s' % (touched or 'none'))
    print('    other relay files beyond the four declared : %s' % (others or 'none'))
    print('    ### **THE ONLY RELAY WRITE OUTSIDE THIS ACT`S OWN FILES IS THE INDEX KEY, AND '
          'THE FACE SAYS SO** : %s' % e2)
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b398_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b398_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the component run carries the options' own text"),
        (d(Q['run_file']), "the desk run carries the items' own sentences"),
    ]
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned, live_bad = 0, 0, 0, []
    carriers = set(os.path.abspath(p) for p, _w in CARRIERS)
    for p in OWNED:
        if not os.path.exists(p) or os.path.abspath(p) in carriers:
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
        if sh:
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', p],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **HANDED TO THE SHARED SCANNER : CLEAN : %s**' % clean)
            if not clean:
                live_bad.append(os.path.basename(p))
    print('    files scanned %d   struck %d   stem %d   ### **LIVE : %d** %s'
          % (scanned, total, stem_total, len(live_bad),
             'PASS' if not (total or live_bad) else '### FAIL ###'))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved '
                         'property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE LI-WEIL BRIDGE (b398).'
    nxt = '# ### THE UNLANDED WORK (b397).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                    ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b398_stem_'), 'blk.txt')
            io.open(tmp2, 'w', encoding='utf-8', newline=chr(10)).write(b2)
            rr = subprocess.run([sys.executable, t('banned_terms.py'), '--new', tmp2],
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
            clean = 'VERDICT          : CLEAN' in (rr.stdout or '')
            print('        ### **%d STEM HIT(S) HANDED TO THE SHARED SCANNER: CLEAN : %s**'
                  % (len(sh), clean))
            if not clean:
                fails.append('G-STEM-APPENDED live ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra2 = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra2), 'PASS' if not extra2 else '### FAIL ###'))
    if extra2:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT EIGHT NEW TOOL FILES:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 8 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b398_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED
               if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles refused : %d ; owner needles not in the ferry : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
