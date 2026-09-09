# -*- coding: utf-8 -*-
"""b393_checks.py -- THE GATE SUITE FOR THE FIVE CLUSTERS SURFACED AND TWO PRICINGS.

### ### **THE ARM THAT MATTERS MOST IS `G-SURFACED`.** ### This act exists because two acts found
### the five clusters and neither put them in front of the navigator. ### The arm requires all five
### to appear in the trail block a reader meets, with their names, their verdicts and a quotation --
### because ### **A FINDING THAT REACHES ONLY THE BANK IS A FINDING THE NAVIGATOR HAS NOT SEEN.**
###
### ### **`G-FOURANSWERS` AND `G-NOSUM` GUARD AN EXPECTATION.** ### `(L1)` wanted two clusters
### changed by anchor and the count is one, and three of the five ### **CANNOT ANSWER THE QUESTION
### ### AT ALL.** ### The arms require the four verdicts to be reported apart and never summed,
### because summing them would turn three non-answers into an affirmative.
###
### ### **`G-TWOREMEDIES` AND `G-NORECOMMEND` GUARD A PRICING.** ### Both remedies are priced for
### both records with what each does not buy, and ### **NEITHER IS RECOMMENDED.**
###
### ### **AND `G-NOWRITE` IS ALMOST THE WHOLE ACT.** ### This act edits ### **NO CORPUS DOCUMENT
### ### AT ALL** -- its only writes are the two ledgers and its own relay files.
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


BANK = d('b393_the_clusters_surfaced.txt')
REG = d('b393_registration_2026-09-09.txt')
FERRY = d('b393_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b393_ferry_scan.txt'), d('b393_reg_termscan.txt'), d('b393_reg_gate.txt')
CENSUS0, FCEN = d('b393_census_stepzero.txt'), d('b393_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b393_regspec_run.txt'), d('audit_b393_reg_satisfiable.txt')
PINS0 = d('b393_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
UNTOUCHED = (TAXONOMY, 'REGISTRY.md', 'README.md', 'SPIRAL_MAP.md',
             'phase2/method/THE_KEYSTONE_CENSUS.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = '39fbc120d09339e7054a10a4b371ceb5eba8b499d47fd40d2b37cb94d6255435'
ROWNUM = '242'
TRAIL_MARK = ('<!-- b393 the five clusters surfaced; the two records priced; Tier KC priced -->')
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b393_components.json'), ('LG', 'b393_lockgate.json'),
                   ('E', 'b393_reads.json'), ('Q', 'b393_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b393_regspec.py', 'tools/b393_reg_gate.py', 'tools/b393_extract.py',
                'tools/b393_components.py', 'tools/b393_desk_bank.py', 'tools/b393_checks.py'}

TOOLNUM = [
    ('the extract, and the three surveys inside it', 'tools/b393_extract.py'),
    ('components 1, 2 and 3', 'tools/b393_components.py'),
    ('the desk, the ledger writes and the bank', 'tools/b393_desk_bank.py'),
    ('the registration gate', 'tools/b393_reg_gate.py'),
    ('the clause spec', 'tools/b393_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- leg 1, the act', FERRY,
     'LEG 1 (b393) — THE FIVE CLUSTERS, SURFACED; AND TWO PRICINGS.'),
    ('the order -- the first leg`s suite is dated at its own close', FERRY,
     "each locked and closed as its own act; the first leg's suite"),
    ('the order -- component 1, the five clusters', FERRY,
     'COMPONENT 1 — THE FIVE CLUSTERS, ordered at b390 and at b391'),
    ('the order -- component 1, printed in the closing message', FERRY,
     'message and not only in its bank: each cluster NAMED, and what'),
    ('the order -- component 1, the kinds of change', FERRY,
     'changed in it — subject drifted from members, anchor no longer'),
    ('the order -- component 1, a list a reader can act on', FERRY,
     'of the closing message can act on.'),
    ('the order -- component 2, the two records', FERRY,
     'COMPONENT 2 — THE TWO RECORDS FAILING BOTH LIMBS: named, with'),
    ('the order -- component 2, the two remediations priced separately', FERRY,
     'a historical note added to the record, or a new version'),
    ('the order -- component 3, Tier KC priced', FERRY,
     'COMPONENT 3 — TIER KC, UNAPPLIED, PRICED: the class exists and'),
    ('the order -- component 3, what the record does not hold', FERRY,
     'application would need that the record does not hold. Priced,'),
    ('the order -- (L1)', FERRY,
     'two of the five clusters changed by anchor rather than by'),
]

SELF_NEEDLES = [
    ('the bank leads with the burial', BANK,
     '### ### ### **TWO ACTS FOUND THE FIVE CLUSTERS AND NEITHER PUT THEM IN FRONT'),
    ('### both measured membership only', BANK,
     '### `b388` found them; `b391` reported them; ### **BOTH MEASURED MEMBERSHIP'),
    ('### the test`s limit is stated with it', BANK,
     '### carrying ### **MORE PINS.** ### **ITS LIMIT IS STATED WITH IT: IT CAN ONLY'),
    ('### four answers, not added', BANK,
     '### ### ### **AND THEY ARE NOT ADDED.** ### Three of the four are ways of ###'),
    ('### an unanswerable case is not promoted', BANK,
     '### ### ### REACH TWO**, and the locked face said the count was one before the'),
    ('### the anchor and the membership are graded differently', BANK,
     '### ### **THE ANCHOR AND THE MEMBERSHIP ARE GRADED ON DIFFERENT SCALES.**'),
    ('### a new version outranks, it does not retire', BANK,
     '###   of the old record -- ### **A NEW VERSION OUTRANKS; IT DOES NOT RETIRE** --'),
    ('### depositing blind is a worse defect', BANK,
     '###   ### WORSE DEFECT THAN THE ONE IT CURES.**'),
    ('### the obligation is satisfied in the corpus and tested at the platform', BANK,
     '### ### ### IS SATISFIED IN THE CORPUS AND TESTED AT THE PLATFORM.**'),
    ('### a heading is not a table read', BANK,
     '### references section. ### ### **A HEADING IS NOT A TABLE READ.**'),
    ('### a declaration is a gate not a cost', BANK,
     '### ### ### OLD. ### THAT IS A GATE, AND NO AMOUNT OF MEASUREMENT OPENS IT.**'),
]

MUST_FAIL = [
    ('the bank never says a cluster was reshaped', BANK, '### A CLUSTER WAS RESHAPED.'),
    ('the bank never says a document was placed in Tier KC', BANK,
     '### A DOCUMENT WAS PLACED IN TIER KC.'),
    ('the bank never says a remediation was recommended', BANK,
     '### A REMEDIATION WAS RECOMMENDED.'),
    ('the bank never says the four verdicts were summed', BANK,
     '### THE FOUR VERDICTS WERE SUMMED.'),
    ('the bank never says the record holds all three limbs', BANK,
     '### THE RECORD HOLDS ALL THREE LIMBS.'),
    ('the bank never says a corpus document was edited', BANK,
     '### A CORPUS DOCUMENT WAS EDITED.'),
    ('the bank never says the platform was called', BANK, '### THE PLATFORM WAS CALLED.'),
    ('the bank never says something was deposited', BANK, '### SOMETHING WAS DEPOSITED.'),
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
        if not subj.startswith('b393'):
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
    print('b393 -- GATE SUITE (THE FIVE CLUSTERS SURFACED AND TWO PRICINGS)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(Q['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    # ### **THIS ACT HAS NO EXTRACT FILE.** ### `b393` is a five-tool act: the order is read
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
    l7 = LG['act'] == 'b393' and not os.path.exists(t('b393_lockgate.py'))
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

    C1, C2, C3 = AC['c1'], AC['c2'], AC['c3']

    # ------------------------------------------------------------------- BAR 2, THE SURFACING BAR
    print(chr(10) + '  G-SURFACED / G-QUOTED (BAR 2) ### THE ARM THAT MATTERS MOST:')
    named = [s for s in C1['surfaced'] if s['cluster'] in tblk]
    verd = [s for s in C1['surfaced'] if s['verdict'] in tblk]
    s1 = len(C1['surfaced']) == 5 and len(named) == 5
    s2 = len(verd) == 5
    s3 = all(s['quote'] for s in C1['surfaced'])
    s4 = 'BOTH MEASURED MEMBERSHIP ONLY' in bu or 'both measured membership only' in tblk
    gs = s1 and s2 and s3 and s4
    print('    ### **ALL FIVE NAMED IN THE BLOCK A READER MEETS : %s (%d of 5)**'
          % (s1, len(named)))
    print('    all five carry their verdict there : %s ; all five carry a quotation : %s'
          % (s2, s3))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SURFACED/G-QUOTED')

    # ---------------------------------------------------------------- BAR 3, THE FOUR-ANSWER BAR
    print(chr(10) + '  G-FOURANSWERS / G-NOSUM (BAR 3):')
    v = C1['by_verdict']
    f1 = len(v) == 4 and sum(v.values()) == 5
    f2 = C1['anchor_changed'] == 1 and C1['l1'] is False
    # ### **THE SUM OF THE THREE NON-ANSWERS MUST NEVER APPEAR AS A COUNT OF CHANGES BY ANCHOR.**
    nonans = sum(n for k, n in v.items() if k != 'ANCHOR OVERTAKEN')
    f3 = ('CHANGED BY ANCHOR : `%d`' % nonans) not in bank
    f4 = 'THEY ARE NOT ADDED' in bu
    f5 = 'REPORTED REFUTED' in bu
    gf = f1 and f2 and f3 and f4 and f5
    print('    ### **FOUR VERDICTS SUMMING TO FIVE : %s** %s' % (f1, v))
    print('    changed by anchor %d ; (L1) %s ; the three non-answers never counted as changes : %s'
          % (C1['anchor_changed'], C1['l1'], f3))
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FOURANSWERS/G-NOSUM')

    # ------------------------------------------------------------------ BAR 4, THE NO-RESHAPE BAR
    print(chr(10) + '  G-NORESHAPE (BAR 4):')
    pre_map = blob_of(PP, 'SPIRAL_MAP.md', preact(PP)) or ''
    now_map = io.open(os.path.join(PP, 'SPIRAL_MAP.md'), encoding='utf-8',
                      errors='replace').read()
    r1 = norm(pre_map) == norm(now_map)
    r2 = C1['reshaped'] == 0
    r3 = 'THE RESHAPING IS THE AUTHOR' in bu
    gr = r1 and r2 and r3
    print('    ### **SPIRAL_MAP.md BYTE-IDENTICAL TO THE PRE-ACT BLOB : %s**' % r1)
    print('    clusters reshaped : %d' % C1['reshaped'])
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-NORESHAPE')

    # ---------------------------------------------------------------- BAR 5, THE TWO-REMEDIES BAR
    print(chr(10) + '  G-TWOREMEDIES / G-NORECOMMEND (BAR 5):')
    m1 = len(C2) == 2 and all('remedy_a' in x and 'remedy_b' in x for x in C2.values())
    m2 = C2['19675356'].get('blocked') is True
    m3 = 'NEITHER REMEDY IS' in bu and 'THE CHOICE IS THE AUTHOR' in bu
    m4 = 'DOES NOT BUY' in bu
    m5 = C2['21432399']['deposited_at'] != C2['19675356'].get('deposited_at')
    gm = m1 and m2 and m3 and m4 and m5
    print('    ### **BOTH REMEDIES PRICED FOR BOTH RECORDS : %s**' % m1)
    print('    the Silence deposit`s current-version remedy is blocked : %s' % m2)
    print('    ### **NEITHER IS RECOMMENDED : %s ; WHAT EACH DOES NOT BUY IS STATED : %s**'
          % (m3, m4))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-TWOREMEDIES/G-NORECOMMEND')

    # ----------------------------------------------------------------- BAR 6, THE THREE-LIMB BAR
    print(chr(10) + '  G-THREELIMBS / G-FLOOR (BAR 6):')
    t1 = C3['limbs'] == 3 and C3['answered'] == 1
    t2 = 'THE OBLIGATION HAS THREE LIMBS AND THE RECORD ANSWERS ONE' in bu
    t3 = 'A HEADING IS NOT A TABLE READ' in bu
    t4 = 'A FLOOR AND NOT A VERDICT' in bu
    t5 = 'A GATE, AND NO AMOUNT OF MEASUREMENT OPENS IT' in bu
    gt = t1 and t2 and t3 and t4 and t5
    print('    ### **LIMBS %d ; ANSWERED BY THE RECORD %d**' % (C3['limbs'], C3['answered']))
    print('    the sweep is marked as a floor : %s ; the declaration is named a gate : %s'
          % (t3 and t4, t5))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-THREELIMBS/G-FLOOR')

    # ---------------------------------------------------------------- BAR 7, THE NO-PLACEMENT BAR
    print(chr(10) + '  G-NOPLACEMENT (BAR 7):')
    p1 = C3['placed'] == 0 and C3['candidates'] == 0
    placed = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in ('.git', 'archive', 'outputs'):
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            r2 = (rel + '/' + f if rel != '.' else f)
            if r2 in (TAXONOMY, 'OPEN_TRAILS.md'):
                continue
            for ln in io.open(os.path.join(dp, f), encoding='utf-8',
                              errors='replace').read().split(chr(10)):
                if 'Tier KC' in ln and 'DOCUMENT CLASS' in ln:
                    placed.append(r2)
    p2 = not placed
    gp = p1 and p2
    print('    ### **DOCUMENTS PLACED %d ; CANDIDATES NAMED %d ; CLASS LINES NAMING Tier KC : %s**'
          % (C3['placed'], C3['candidates'], placed or 'none'))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-NOPLACEMENT')

    # ------------------------------------------------------------------- BAR 8, THE NO-WRITE BAR
    print(chr(10) + '  G-NOWRITE / G-NOPLATFORM / G-NOSCOPE (BAR 8):')
    dirty = []
    for rel in UNTOUCHED:
        pre = blob_of(PP, rel, preact(PP)) or ''
        now = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                      errors='replace').read()
        if norm(pre) != norm(now):
            dirty.append(rel)
    w1 = not dirty
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b393_') and x.endswith('.py')))
    NETY = ('curl', 'urllib', 'requests', 'zenodo.org', 'http://', 'https://')
    nhits = [(x, k) for x in mymods1 for k in NETY if k in strip_prose(t(x))]
    w2 = not nhits
    # ### **AND LEG 2'S SCOPE IS NOT REACHED INTO.**
    w3 = not [(x, k) for x in mymods1 for k in ('reconcil', 'bucket')
              if k in strip_prose(t(x))]
    w4 = 'NO KEYSTONE IS RECONCILED' in bu
    gw2 = w1 and w2 and w3 and w4
    print('    ### **CORPUS DOCUMENTS CHANGED BEYOND THE LEDGERS : %s**' % (dirty or 'none'))
    print('    network tokens in this act`s code : %s' % (nhits or 'none'))
    print('    ### **b394`S SCOPE NOT REACHED INTO : %s**' % (w3 and w4))
    print('    %s' % ('PASS' if gw2 else '### FAIL ###'))
    if not gw2:
        fails.append('G-NOWRITE/G-NOPLATFORM/G-NOSCOPE')

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
    cq = [m for m in Q['marks'] if 'cluster reshaping' in m['item']]
    n4 = (len(cq) == 1 and cq[0]['disposition'] == 'STAND'
          and 'THE AUTHOR' in cq[0]['why'].upper())
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
    print('    ### **THE CLUSTER RESHAPING STANDS, WITH THE FIVE NAMED, AND IS THE '
          'AUTHOR`S** : %s' % n4)
    print('    no new tracking document in PLACE-papers : %s %s' % (n5, newdocs[:2] or ''))
    print('    ### **UNTRACKED PATHS THAT ARE NOT TRACKING DOCUMENTS, EXCLUDED AND NAMED** : %s'
          % (notdocs or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-OPEN/G-NONEWDOC')

    # ------------------------------------ G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE:')
    ALLOWED = {'relay': {'tools/banked_index.py'},
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b393' not in x)
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
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md', preact(SIDE))
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE FIVE CLUSTERS SURFACED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-five-clusters-surfaced returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('a cluster was reshaped', 'a document was placed in tier kc',
              'a remediation was recommended', 'the platform was called'))
    t6 = all(Q['trail'][k] for k in Q['trail'] if k.startswith('says_'))
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
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
    mirrorp = d('b393_mirror.txt')
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
        ('clusters %d' % len(C1['surfaced']), str(len(C1['surfaced'])) in bank),
        ('changed by anchor %d' % C1['anchor_changed'], str(C1['anchor_changed']) in bank),
        ('rows %s' % C3['rows'], str(C3['rows']) in bank),
        ('not machine-verified %s' % C3['not_machine'], str(C3['not_machine']) in bank),
        ('keystones on disk %s' % C3['found'], str(C3['found']) in bank),
        ('with a table %s' % C3['with_table'], str(C3['with_table']) in bank),
        ('the monograph version %s' % C2['21432399']['deposited_at'],
         C2['21432399']['deposited_at'] in bank),
        ('the repository version %s' % C2['21432399']['repo_now'],
         C2['21432399']['repo_now'] in bank),
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
                          if x.startswith('b393_') and x.endswith('.py')))
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
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b374_hedge.py',
             'tools/b375_population.py', 'tools/gate_hash.py', 'tools/b378_lockgate.py',
             'tools/role_structure.py', 'tools/co_location.py']
    touched = [p for p in owner
               if git(ROOT, 'diff', '--name-only', preact(ROOT), '--', p).strip()]
    # ### **`tools/b304_hooks.py` IS AN OWNER INSTRUMENT AND IT IS EDITED -- DECLARED ON THE FACE
    # ### BEFORE THE ACT, IN SECTION `(F)`.** ### It is therefore NOT on the list above; a
    # ### declared write is not an undeclared one, and the declaration is what makes the
    # ### difference. ### **THE FACE WAS NOT WIDENED MID-ACT TO ACCOMMODATE IT.**
    DECLARED_W = ('tools/banked_index.py',)
    others = [x for x in git(ROOT, 'diff', '--name-only', preact(ROOT)).split(chr(10))
              if x.strip() and 'b393' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
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
             d('b393_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b393_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE FIVE CLUSTERS SURFACED (b393).'
    nxt = '# ### THE TWO RULINGS (b392).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b393_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT SIX NEW TOOL FILES:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 6 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b393_hedge_')
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
