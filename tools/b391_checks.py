# -*- coding: utf-8 -*-
"""b391_checks.py -- THE GATE SUITE FOR THE PHANTOM VERSION AND THE FIVE CLUSTERS.

### ### **THE ARM THAT MATTERS MOST IS `G-EXCLUDED`.** ### This act repairs a string, and three of
### the thirty-two places that string appears are ### **LEDGER LINES REPORTING THE DEFECT ITSELF** --
### two of them `b390`'s own record of finding it. ### A careless pass would have swept them up with
### the rest and ### **ERASED THE RECORD OF WHAT IT WAS REPAIRING.** ### The arm reads all eight
### excluded instances out of the files after the write and requires them ### **BYTE-IDENTICAL TO
### ### THE PRE-ACT BLOB.**
###
### ### **`G-ONESTRING` BOUNDS A FACE THE ORDER MADE WIDE.** ### On every line that differs from the
### pre-act blob, the only difference is `v1.2` -> `v0.5.4`; no line count changes; nothing else in
### any of the eleven documents moves.
###
### ### **`G-RESIDUE` AND `G-YIELDS` GUARD THE WIDENED SCREEN.** ### Four tightenings, every yield
### printed, and every surviving candidate carrying a hand verdict -- because ### **A SCREEN THAT
### ### OVER-REPORTS BY DESIGN MUST BE MARKED AS A SCREEN AND ITS RESIDUE READ.**
###
### ### **AND `G-SCOPE` KEEPS THIS LEG OUT OF THE NEXT.** ### `(R19)` and `(R20)` are `b392`'s;
### ### **A LEG DOES NOT REACH INTO THE NEXT LEG'S SCOPE.**
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`). ### **A RUN FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`). ### **AND
### ### EVERY DIFF ARM MEASURES AGAINST THE PRE-ACT BLOB** (`b352`, `b388`, `b389`, `b390`).
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


BANK = d('b391_the_phantom_repaired.txt')
REG = d('b391_registration_2026-09-09.txt')
FERRY = d('b391_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b391_ferry_scan.txt'), d('b391_reg_termscan.txt'), d('b391_reg_gate.txt')
CENSUS0, FCEN = d('b391_census_stepzero.txt'), d('b391_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b391_regspec_run.txt'), d('audit_b391_reg_satisfiable.txt')
PINS0 = d('b391_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
OLD, NEW = 'v1.2', 'v0.5.4'
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = '80e96487f126f52fff38cc22a76fa183c04d5943b72f11e2aac87d4d5a584fab'
ROWNUM = '240'
TRAIL_MARK = '<!-- b391 the phantom version repaired; the five clusters read -->'
C2_SUPERSEDED = 66
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b391_components.json'), ('LG', 'b391_lockgate.json'),
                   ('E', 'b391_reads.json'), ('Q', 'b391_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b391_regspec.py', 'tools/b391_reg_gate.py', 'tools/b391_extract.py',
                'tools/b391_components.py', 'tools/b391_desk_bank.py', 'tools/b391_checks.py'}

TOOLNUM = [
    ('the extract, and the three surveys inside it', 'tools/b391_extract.py'),
    ('components 0, 1 and 2, and the repair inside component 1', 'tools/b391_components.py'),
    ('the desk, the ledger writes and the bank', 'tools/b391_desk_bank.py'),
    ('the registration gate', 'tools/b391_reg_gate.py'),
    ('the clause spec', 'tools/b391_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- leg 1, the act', FERRY,
     'LEG 1 (b391) — THE PHANTOM VERSION, AND THE FIVE CLUSTERS.'),
    ('the order -- both faces wide within their named scopes', FERRY,
     'PURPOSE within their named scopes: each may repair what it'),
    ('the order -- component 0, the five clusters', FERRY,
     "COMPONENT 0 — THE FIVE CLUSTERS, ordered at b390's closing and"),
    ('the order -- component 0, no cluster reshaped', FERRY,
     'quotation. No cluster reshaped; the reshaping is the author'),
    ('the order -- component 1, the phantom pass', FERRY,
     'COMPONENT 1 — THE PHANTOM VERSION PASS: the methodology'),
    ('the order -- component 1, a count quoted forward', FERRY,
     "b390's count — a count quoted forward is a count nobody"),
    ('the order -- component 1, the two exclusions', FERRY,
     'as written. Then repair, with two exclusions stated before any'),
    ('the order -- component 1, the phantom`s origin', FERRY,
     "search for the phantom's origin — where the wrong version was"),
    ('the order -- component 2, widened once', FERRY,
     'COMPONENT 2 — THE SAME CHECK, WIDENED ONCE: run the same test'),
    ('the order -- component 2, superseded is a currency item', FERRY,
     'that exists but is superseded is a currency item, not a'),
    ('the order -- (L1)', FERRY, 'expectations: (L1) the phantom count re-measured differs from'),
]

SELF_NEEDLES = [
    ('the bank leads with the phantom', BANK,
     '### ### ### **THE METHODOLOGY PAPER WAS CITED AT A VERSION IT HAS NEVER HAD, AND THE'),
    ('### a count quoted forward', BANK,
     '### `b390` published ### **`28` ACROSS `11`.** ### **A COUNT QUOTED FORWARD IS A'),
    ('### the phantom was a bundle label', BANK,
     '### ### ### **THE PHANTOM WAS A BUNDLE LABEL ON THE REGISTRY`S OWN ROW. ### IT WAS'),
    ('### a correction that does not propagate', BANK,
     '### ### ### **A CORRECTION THAT DOES NOT PROPAGATE IS A CORRECTION IN ONE PLACE AND'),
    ('### the corpus already named the species', BANK,
     '### **AND THE CORPUS HAD ALREADY NAMED THE SPECIES IN THE SAME PASS** -- a'),
    ('### repairing a report of an error erases the report', BANK,
     '###   document. ### **REPAIRING A REPORT OF AN ERROR ERASES THE REPORT**, and two of'),
    ('### the registry`s own reconciliation, quoted', BANK,
     "###   > ### while the paper's own header is the `v0.5` lineage; both now `v0.5.2`).*"),
    ('### four tightenings, every yield printed', BANK,
     '### ### **FOUR TIGHTENINGS, EVERY ONE BEFORE A FINDING WAS FILED AND EVERY ONE'),
    ('### superseded is a currency item', BANK,
     '### ### **`%d` SUPERSEDED -- REPORTED AND LEFT.** ### **A VERSION THAT EXISTS BUT IS'
     % C2_SUPERSEDED),
    ('### a screen must be marked as a screen', BANK,
     '### ### ### **A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A SCREEN AND'),
    ('### CONSTANCE declares no matching version', BANK,
     '### ### cite `CONSTANCE.md`, which ### **DECLARES NO MATCHING VERSION ANYWHERE IN'),
    ('### the count is a floor', BANK,
     '### ### exactly how the methodology paper hid. ### **THE COUNT IS A FLOOR.**'),
    ('### the reshaping is the author`s', BANK,
     "### ### ### THAT PRECEDES IT.**"),
]

MUST_FAIL = [
    ('the bank never says a provenance entry was edited', BANK,
     '### A PROVENANCE ENTRY WAS EDITED.'),
    ('the bank never says a preserved block was edited', BANK,
     '### A PRESERVED BLOCK WAS EDITED.'),
    ('the bank never says a report of the defect was edited', BANK,
     '### A REPORT OF THE DEFECT WAS EDITED.'),
    ('the bank never says a superseded version was repaired', BANK,
     '### A SUPERSEDED VERSION WAS REPAIRED.'),
    ('the bank never says the count was carried forward', BANK,
     '### THE COUNT WAS CARRIED FORWARD.'),
    ('the bank never says the residue was not read', BANK,
     '### THE SCREEN`S RESIDUE WAS NOT READ.'),
    ('the bank never says a cluster was reshaped', BANK, '### A CLUSTER WAS RESHAPED.'),
    ('the bank never says the taxonomy was amended', BANK, '### THE TAXONOMY WAS AMENDED.'),
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
        if not subj.startswith('b391'):
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
    print('b391 -- GATE SUITE (THE PHANTOM VERSION AND THE FIVE CLUSTERS)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, _line = GN.present(extract, path, hint)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
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
    l7 = LG['act'] == 'b391' and not os.path.exists(t('b391_lockgate.py'))
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

    C0, C1, C2 = AC['c0'], AC['c1'], AC['c2']

    # ---------------------------------------------------------------- BAR 2, THE RE-MEASURE BAR
    print(chr(10) + '  G-REMEASURE / G-NOFORWARD (BAR 2):')
    q1 = C1['total'] == 32 and C1['docs'] == 13
    q2 = (C1['total'], C1['docs']) != (28, 11)
    # ### **b390's PAIR APPEARS ONLY AS THE FIGURE BEING CORRECTED.**
    q3 = '28' in bank and 'A COUNT QUOTED FORWARD IS A' in bu
    q4 = E['s2']['total'] == C1['total']
    gq = q1 and q2 and q3 and q4
    print('    ### **RE-MEASURED : %d ACROSS %d ; b390 SAID 28/11 : %s**'
          % (C1['total'], C1['docs'], q2))
    print('    the older pair appears only as the figure being corrected : %s' % q3)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-REMEASURE/G-NOFORWARD')

    # ----------------------------------------------------------------- BAR 3, THE EXCLUSION BAR
    print(chr(10) + '  G-EXCLUDED / G-PROVENANCE / G-PRESERVED / G-MENTION (BAR 3):')
    # ### **EVERY EXCLUDED INSTANCE RE-READ OUT OF ITS FILE AND COMPARED TO THE PRE-ACT BLOB.**
    excl = [h for h in E['s2']['hits'] if h['cls'] != 'CITATION']
    intact, checked = 0, 0
    for h in excl:
        rel = h['file']
        pre = blob_of(PP, rel, preact(PP))
        if pre is None:
            continue
        now = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                      errors='replace').read()
        pl, al = norm(pre).split(chr(10)), norm(now).split(chr(10))
        k = h['line'] - 1
        checked += 1
        if k < len(pl) and k < len(al) and pl[k] == al[k] and OLD in al[k]:
            intact += 1
    e1 = checked == len(excl) == 8 and intact == checked
    e2 = C1['by_class'].get('PROVENANCE', 0) == 4
    e3 = C1['by_class'].get('PRESERVED', 0) == 1
    e4 = C1['by_class'].get('MENTION', 0) == 3
    e5 = 'REPAIRING A REPORT OF AN ERROR ERASES THE REPORT' in bu
    ge = e1 and e2 and e3 and e4 and e5
    print('    ### **EXCLUDED INSTANCES STILL CARRYING `%s`, BYTE-IDENTICAL TO THE PRE-ACT BLOB : '
          '%d OF %d**' % (OLD, intact, checked))
    print('    provenance %d ; preserved %d ; mention %d'
          % (C1['by_class'].get('PROVENANCE', 0), C1['by_class'].get('PRESERVED', 0),
             C1['by_class'].get('MENTION', 0)))
    print('    ### **THE THIRD EXCLUSION IS STATED IN WORDS AS WELL AS COUNTED : %s**' % e5)
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-EXCLUDED/G-PROVENANCE/G-PRESERVED/G-MENTION')

    # ----------------------------------------------------------------- BAR 4, THE ONE-STRING BAR
    print(chr(10) + '  G-ONESTRING / G-NODELETE (BAR 4):')
    o1 = C1['repaired'] == 24 and C1['by_class'].get('CITATION', 0) == 24
    o2 = C1['removed'] == 0 and C1['line_counts_unchanged'] is True
    o3 = C1['only_version'] is True
    # ### **RE-MEASURED HERE AGAINST THE PRE-ACT BLOB, NOT TRUSTED FROM THE JSON.**
    bad, diffs = [], 0
    for rel in sorted(C1['files']):
        pre = blob_of(PP, rel, preact(PP))
        now = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                      errors='replace').read()
        pl, al = norm(pre or '').split(chr(10)), norm(now).split(chr(10))
        if len(pl) != len(al):
            bad.append((rel, 'line count'))
            continue
        for x, y in zip(pl, al):
            if x != y:
                diffs += 1
                if x.replace(OLD, NEW) != y:
                    bad.append((rel, x[:40]))
    o4 = (not bad) and diffs == 24
    go = o1 and o2 and o3 and o4
    print('    ### **REPAIRED %d ; LINES REMOVED %d ; LINE COUNTS UNCHANGED %s**'
          % (C1['repaired'], C1['removed'], C1['line_counts_unchanged']))
    print('    ### **LINES DIFFERING FROM THE PRE-ACT BLOB, RE-MEASURED HERE : %d**' % diffs)
    print('    ### **LINES WHERE THE CHANGE IS NOT ONLY THE VERSION : %s**' % (bad or 'none'))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ONESTRING/G-NODELETE')

    # -------------------------------------------------------------- BAR 5, THE SCREEN-RESIDUE BAR
    print(chr(10) + '  G-RESIDUE (BAR 5):')
    r1 = C2['candidates'] == 4 and C2['repaired'] == 0
    r2 = sum(C2['verdicts'].values()) == C2['candidates']
    r3 = 'UNREAD' not in C2['verdicts']
    r4 = 'A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A SCREEN' in bu
    r5 = C2['superseded'] == 66
    gr = r1 and r2 and r3 and r4 and r5
    print('    ### **CANDIDATES %d ; EVERY ONE CARRIES A HAND VERDICT : %s ; REPAIRED %d**'
          % (C2['candidates'], r2 and r3, C2['repaired']))
    print('    verdicts : %s ; superseded reported and left : %d' % (C2['verdicts'], C2['superseded']))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RESIDUE')

    # ---------------------------------------------------------------------- BAR 6, THE YIELD BAR
    print(chr(10) + '  G-YIELDS (BAR 6):')
    y = [C2['raw'], C2['tokened'], C2['adjacent'], C2['screened']]
    y1 = all(str(v) in bank for v in y)
    y2 = y == sorted(y, reverse=True)
    y3 = '196' in bank and C2['raw'] > C2['screened']
    gy = y1 and y2 and y3
    print('    ### **THE YIELDS %s, EVERY ONE PRINTED IN THE BANK : %s**' % (y, y1))
    print('    monotonically narrowing : %s' % y2)
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-YIELDS')

    # -------------------------------------------------------------------- BAR 7, THE NO-RESHAPE BAR
    print(chr(10) + '  G-NORESHAPE (BAR 7):')
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()
    pre_map = blob_of(PP, 'SPIRAL_MAP.md', preact(PP)) or ''
    rows_before = len([x for x in norm(pre_map).splitlines()
                       if x.startswith('|') and x.count('|') >= 5])
    rows_after = len([x for x in norm(maptxt).splitlines()
                      if x.startswith('|') and x.count('|') >= 5])
    n1 = C0['reshaped'] == 0 and C0['clusters'] == 5
    n2 = rows_before == rows_after
    n3 = 'THE RESHAPING IS THE AUTHOR' in bu
    n4 = '<!-- b389 (R18) HEAD NOTE' in maptxt
    gn2 = n1 and n2 and n3 and n4
    print('    ### **CLUSTERS REPORTED %d ; RESHAPED %d**' % (C0['clusters'], C0['reshaped']))
    print('    map table rows %d before, %d after : %s' % (rows_before, rows_after, n2))
    print('    the (R18) head note still stands : %s' % n4)
    print('    %s' % ('PASS' if gn2 else '### FAIL ###'))
    if not gn2:
        fails.append('G-NORESHAPE')

    # ------------------------------------------------------------------------ BAR 8, THE SCOPE BAR
    print(chr(10) + '  G-SCOPE / G-NOTAXONOMY (BAR 8):')
    s1 = not git(PP, 'diff', '--name-only', preact(PP), '--', TAXONOMY).strip()
    s2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    s3 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'README.md').strip()
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b391_') and x.endswith('.py')))
    s4 = not [(x, k) for x in mymods1 for k in ('R19', 'R20', 'deposit rule')
              if k in strip_prose(t(x))]
    s5 = "A LEG DOES NOT REACH INTO THE NEXT LEG" in bu
    gs = s1 and s2 and s3 and s4 and s5
    print('    the standing taxonomy unchanged : %s ; REGISTRY unchanged : %s' % (s1, s2))
    print('    ### **NO (R19)/(R20) MACHINERY IN THIS LEG`S CODE : %s**' % s4)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SCOPE/G-NOTAXONOMY')

    # ---------------------------------------------------------------------------- G-NOZENODOWRITE
    print(chr(10) + '  G-NOZENODOWRITE:')
    WRITEY = ("'POST'", "'PUT'", "'PATCH'", "'DELETE'", "'-X'", "'--data'", 'access_token',
              'zenodo')
    whits = [(x, k) for x in mymods1 for k in WRITEY if k in strip_prose(t(x))]
    z1 = not whits
    z2 = 'NOTHING WAS WRITTEN AT ZENODO' in bu or 'NOTHING IS WRITTEN AT ZENODO' in bu
    gz = z1 and z2
    print('    platform tokens in this act`s stripped code : %s' % (whits or 'none'))
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-NOZENODOWRITE')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = ('OPEN' in tblk and 'Nothing here is closed' in tblk)
    n3 = Q['lists_closed'] == 0
    # ### **THE CITATION QUESTION IS RESTATED AND NOT MOVED.**
    cq = [m for m in Q['marks'] if 'citation question' in m['item']]
    n4 = len(cq) == 1 and cq[0]['disposition'] == 'STAND' and 'NOT MOVED' in cq[0]['why'].upper()
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
    print('    ### **THE CITATION QUESTION IS RESTATED AS AWAITING THE AUTHOR AND NOT MOVED** : %s'
          % n4)
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
               'PLACE-papers': set(['OPEN_TRAILS.md']
                                   + sorted(_J['AC']['c1']['files'])),
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b391' not in x)
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    w2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
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
    print('    ### **REGISTRY.md UNCHANGED SINCE BEFORE THIS ACT** : %s' % w2)
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
    t3 = len(rws) == 1 and anc and 'THE PHANTOM VERSION REPAIRED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-phantom-version-repaired returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('a provenance entry was edited', 'a superseded version was repaired',
              'a cluster was reshaped', 'the taxonomy was amended'))
    t6 = (Q['trail']['says_remeasured'] and Q['trail']['says_origin']
          and Q['trail']['says_not_propagated'] and Q['trail']['says_report']
          and Q['trail']['says_currency'] and Q['trail']['says_no_reshape'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK SAYS RE-MEASURED, NAMES THE ORIGIN, SAYS THE CORRECTION '
          'DID NOT PROPAGATE, PROTECTS THE REPORTS, CALLS SUPERSEDED A CURRENCY ITEM, AND '
          'RESHAPES NOTHING** : %s' % t6)
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
    mirrorp = d('b391_mirror.txt')
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
        ('instances %d' % C1['total'], str(C1['total']) in bank),
        ('documents %d' % C1['docs'], str(C1['docs']) in bank),
        ('repaired %d' % C1['repaired'], str(C1['repaired']) in bank),
        ('provenance %d' % C1['by_class'].get('PROVENANCE', 0),
         str(C1['by_class'].get('PROVENANCE', 0)) in bank),
        ('mentions %d' % C1['by_class'].get('MENTION', 0),
         str(C1['by_class'].get('MENTION', 0)) in bank),
        ('the origin line %d' % C1['origin_line'], str(C1['origin_line']) in bank),
        ('the screen raw %d' % C2['raw'], str(C2['raw']) in bank),
        ('the screen screened %d' % C2['screened'], str(C2['screened']) in bank),
        ('superseded %d' % C2['superseded'], str(C2['superseded']) in bank),
        ('candidates %d' % C2['candidates'], str(C2['candidates']) in bank),
        ('clusters %d' % C0['clusters'], str(C0['clusters']) in bank),
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
    for lbl, jf in (('extract', E), ('lockgate', LG), ('components', AC), ('desk_bank', Q)):
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
                          if x.startswith('b391_') and x.endswith('.py')))
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
              if x.strip() and 'b391' not in x and x.strip() not in DECLARED_W]
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
             d('b391_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b391_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the sources' own lines"),
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

    marker = '# ### THE PHANTOM VERSION REPAIRED (b391).'
    nxt = '# ### THE FIRST PROOFREADING PASS (b390).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b391_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b391_hedge_')
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
    print('  ### needles refused : %d ; owner needles not in the extract file : %d'
          % (refused, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
