# -*- coding: utf-8 -*-
"""b387_checks.py -- THE GATE SUITE FOR WHAT THE KEYSTONES' TABLES CARRY.

### ### **THE ARM THAT MATTERS MOST IS `G-PARTITION`.** ### Every other figure in this act rests
### on the categories summing to the row count, per document and in total. ### **A CLASSIFIER
### WHOSE BINS DO NOT ADD UP TO ITS POPULATION HAS DOUBLE-COUNTED OR DROPPED, AND BOTH LOOK LIKE
### A RESULT.**
###
### ### **AND `G-UNREADABLE` IS THE ARM AGAINST THIS ACT'S OWN TEMPTATION.** ### A count is
### tidier with no residue. ### The residue is `23` rows, each named by document and line, and the
### arm requires that they be ### **NAMED AND NEVER ASSIGNED.**
###
### ### **`G-NORECONCILE` GUARDS THE ORDER'S OWN INSTRUCTION.** ### The union and the disk
### disagree in four ways; the order said report and do not reconcile. ### An act that quietly
### corrected the union would have destroyed the finding it was sent to make.
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`) -- ### **BUT A POSITIVE ARM READS THE CODE ITSELF** (`b386`: `strip_prose`
### removes the very line a positive arm asks for). ### **A RUN FILE IS RESOLVED BY ITS OWN
### ### RECORDED CLOCK** (`b358`).
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


BANK = d('b387_what_the_tables_carry.txt')
REG = d('b387_registration_2026-09-09.txt')
FERRY = d('b387_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b387_ferry_scan.txt'), d('b387_reg_termscan.txt'), d('b387_reg_gate.txt')
CENSUS0, FCEN = d('b387_census_stepzero.txt'), d('b387_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b387_regspec_run.txt'), d('audit_b387_reg_satisfiable.txt')
PINS0 = d('b387_pins_stepzero.txt')
MEMDIR = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--',
                      'memory')
SEAL = '322044cf1b9d86db196972f74ee209b4b464f07822cd32e2836ca5aa8e852e0a'
ROWNUM = '236'
TRAIL_MARK = '<!-- b387 what the keystones tables actually carry; (R16) recorded -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b387_components.json'), ('LG', 'b387_lockgate.json'),
                   ('E', 'b387_reads.json'), ('Q', 'b387_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b387_regspec.py', 'tools/b387_reg_gate.py', 'tools/b387_extract.py',
                'tools/b387_components.py', 'tools/b387_desk_bank.py', 'tools/b387_checks.py'}

TOOLNUM = [
    ('the extract, the table survey and the attestation of the set', 'tools/b387_extract.py'),
    ('the four components, and the count inside two of them', 'tools/b387_components.py'),
    ('(R7), the three closing writes and the bank', 'tools/b387_desk_bank.py'),
    ('the registration gate', 'tools/b387_reg_gate.py'),
    ('the clause spec', 'tools/b387_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
    ("the front door's own row categories", 'tools/row_categories.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     "ACT b387 — WHAT THE KEYSTONES' TABLES ACTUALLY CARRY. Number"),
    ('the order -- a read and a count, no ruling', FERRY,
     'not claimed by any unclosed ferry. A READ and a COUNT; no'),
    ('the order -- the face from a survey, not a belief', FERRY,
     'gate; the face is written from a survey, never from a belief'),
    ('the ruling (R16) -- the untracked hook copies stay', FERRY,
     'strikeable: THE UNTRACKED HOOK COPIES STAY. The repository'),
    ('the ruling (R16) -- removing a working fallback buys nothing', FERRY,
     'runs, and the untracked copies are a fallback; removing a'),
    ('the order -- component 1, the set from the record not a predicate', FERRY,
     'COMPONENT 1 — THE SET, from the record and not from a'),
    ('the order -- component 1, report the disagreement and do not reconcile', FERRY,
     'documents on disk disagree, report the disagreement and do not'),
    ('the order -- component 2, every row counted by what backs it', FERRY,
     'COMPONENT 2 — EVERY ROW COUNTED BY WHAT BACKS IT: per document'),
    ('the order -- component 2, unreadable rather than assigned', FERRY,
     "unreadable rather than assigned. Quote the front door's status"),
    ('the order -- component 3, answered from practice not ruled', FERRY,
     'COMPONENT 3 — THE QUESTION ANSWERED FROM PRACTICE, not ruled:'),
    ('the order -- component 3, nothing recommended', FERRY,
     'borderline dispositions quoted and NOTHING recommended.'),
    ('the order -- component 4, the seat`s own memory', FERRY,
     "COMPONENT 4 — THE SEAT'S OWN MEMORY: the memory file was over"),
    ('the order -- component 4, against the prior blob not from recall', FERRY,
     "through a pointer, if anything, checked against the file's own"),
    ('the order -- (F1), a material fraction not machine-verified', FERRY,
     'the keystones already carry a material fraction of rows that'),
    ('the order -- (F2), nothing was lost from the memory file', FERRY,
     'are not machine-verified and are labelled as such; (F2) nothing'),
]

SELF_NEEDLES = [
    ('the bank leads with a read and a count, closing nothing', BANK,
     '### ### ### **A READ AND A COUNT. ### NO RULING, NO REPAIR, NO ROW EDITED, NO GRADE'),
    ('### (R16) is recorded with its reason', BANK,
     '### ### **AND `(R16)` IS RECORDED WITH ITS REASON:** ### *the repository'),
    ('### the set is the union`s own line', BANK,
     '### ### **THE SET IS THE UNION`S OWN KEYSTONE-SET LINE, READ BY THE ANCHOR TOOL** --'),
    ('### by shape and never by heading', BANK,
     '### ### ### **THE TABLES WERE FOUND BY SHAPE AND NEVER BY HEADING** ### -- `(R2)`,'),
    ('### the predicate was wrong twice', BANK,
     '### ### ### **AND THE PREDICATE WAS WRONG TWICE BEFORE IT WAS RIGHT, WHICH IS'),
    ('### the absence is proved not assumed', BANK,
     '###     ### **THE ABSENCE IS PROVED, NOT ASSUMED** (`b378`): every table in each of'),
    ('### the union names an ungraded carrier', BANK,
     '###   ### **(2) THE UNION POINTS `MONO` AT `§25.8` AND `§25.8`S TABLE IS NOT'),
    ('### none of the four is reconciled', BANK,
     '### ### ### **NONE OF THE FOUR IS RECONCILED. ### BOTH THE UNION AND THE DOCUMENTS'),
    ('### the categories are the corpus`s own', BANK,
     '### being omitted.* ### **SO THE CATEGORIES ARE THE CORPUS`S AND NOT THIS ACT`S.**'),
    ('### an unreadable row forced into a category', BANK,
     '### ### ### **`(E1)` REGISTERED THAT A RESIDUE WAS EXPECTED, AND THE RESIDUE IS'),
    ('### the count is of claimed status', BANK,
     '### ### ### **AND EVERY FIGURE IS A COUNT OF *CLAIMED* STATUS.** ### This act read'),
    ('### the bearing stops at the author', BANK,
     '### ### ### **SO THE PER-ROW PRACTICE EXISTS AND IS IN USE. ### WHETHER IT SUPPLIES'),
    ('### the order asked for a blob and there is none', BANK,
     '### ### ### **THE ORDER ASKED FOR THE FILE`S PRIOR BLOB AND THERE IS NONE.**'),
    ('### the screen over-reports by design', BANK,
     '### ### **BY CONSTRUCTION.** ### So a token test measures WORDING, not content, and it'),
    ('### a claim that lives only in an index hook', BANK,
     '### ### ### **NEW -- `A CLAIM THAT LIVES ONLY IN AN INDEX HOOK IS A CLAIM ONE TRIM`'),
    ('### (E3) refuted by its own check', BANK,
     '### ### **`(E3)` REFUTED BY ITS OWN CHECK.** ### This seat registered that nothing'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a row was edited', BANK, '### A ROW WAS EDITED.'),
    ('the bank never says a grade was moved', BANK, '### A GRADE WAS MOVED.'),
    ('the bank never says the union was corrected', BANK, '### THE UNION WAS CORRECTED.'),
    ('the bank never says an unreadable row was assigned', BANK,
     '### AN UNREADABLE ROW WAS ASSIGNED.'),
    ('the bank never says the preferred option is', BANK, '### THE PREFERRED OPTION IS.'),
    ('the bank never says a kernel was re-run', BANK, '### A KERNEL WAS RE-RUN.'),
    ('the bank never says the categories did not sum', BANK, '### THE CATEGORIES DID NOT SUM.'),
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
        if not subj.startswith('b387'):
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
    print('b387 -- GATE SUITE (THE GUARD MADE SINGLE-SOURCED UNDER (R15))')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    C1, C2, C3, C4 = AC['C1'], AC['C2'], AC['C3'], AC['C4']
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
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE LOCKED FACE`S OWN EIGHT, AS WHOLE LINES):')
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
    l7 = LG['act'] == 'b387' and not os.path.exists(t('b387_lockgate.py'))
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

    # ------------------------------------------------------------------- BAR 2, THE OPTION BAR
    # ------------------------------------------------------------------- BAR 2, THE SET BAR
    print(chr(10) + '  G-SET / G-BYSHAPE (BAR 2):')
    s1 = C1['union_names'] == 14 == len(E['survey'])
    s2 = C1['with_table'] + C1['without_table'] == C1['union_names']
    # ### ### **EVERY ONE OF THE FOURTEEN WAS LOOKED FOR, AND EACH ABSENCE CARRIES ITS
    # ### ### NEAR-MISSES** -- an absence needs a proved search (`b378`).
    s3 = all(sv['exists'] for sv in E['survey'])
    s4 = all(('near' in sv) for sv in E['survey'] if not sv['tables'])
    # ### **THE SET CAME FROM THE UNION`S OWN LINE, READ BY THE ANCHOR TOOL.**
    s5 = any(b['label'] == 'the union -- the fourteen named' and b.get('line')
             for b in E['built'])
    # ### **AND THE TABLES WERE FOUND BY SHAPE.** ### The located headings are not all the same
    # ### word, which is the evidence that no heading test produced them.
    heads = set()
    for sv in E['survey']:
        for tb in sv['tables']:
            heads.add(tb['heading'].split('*')[0].strip().lstrip('#').strip()[:40])
    s6 = len(heads) > 1
    gs = s1 and s2 and s3 and s4 and s5 and s6
    print('    ### **THE UNION NAMES %d ; %d CARRY A TABLE ; %d CARRY NONE ; THEY SUM : %s**'
          % (C1['union_names'], C1['with_table'], C1['without_table'], s2))
    print('    every named document exists on disk : %s ; every absence carries near-misses : %s'
          % (s3, s4))
    print('    ### **THE SET IS THE UNION`S OWN LINE, READ BY THE ANCHOR TOOL : %s**' % s5)
    print('    ### **DISTINCT HEADINGS THE TABLES SIT UNDER : %d** -- so no single heading test '
          'produced them' % len(heads))
    for h in sorted(heads):
        print('        %s' % h)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SET/G-BYSHAPE')

    # ---------------------------------------------------------- BAR 3, THE DISAGREEMENT BAR
    print(chr(10) + '  G-DISAGREE / G-NORECONCILE (BAR 3):')
    d1 = C1['disagreements_reported'] == 4 and C1['reconciled'] == 0
    kinds = [x['kind'] for x in C1['disagreements']]
    d2 = len(set(kinds)) == len(kinds)
    d3 = C1['mono_258_graded'] is False and C1['mono_graded_tables'] >= 1
    # ### **AND THE UNION IS BYTE-IDENTICAL TO ITS BLOB** -- nothing was reconciled by editing it.
    d4 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase1.5/method/THE_LOAD_BEARING_MAP.md').strip()
    d5 = 'NONE OF THE FOUR IS RECONCILED' in bu
    gd = d1 and d2 and d3 and d4 and d5
    print('    ### **DISAGREEMENTS REPORTED : %d ; RECONCILED : %d**'
          % (C1['disagreements_reported'], C1['reconciled']))
    for k in kinds:
        print('        %s' % k)
    print('    ### **THE UNION`S NAMED CARRIER FOR MONO IS UNGRADED : %s ; THE MONOGRAPH HAS %d '
          'GRADED TABLE(S) ELSEWHERE**' % (not C1['mono_258_graded'], C1['mono_graded_tables']))
    print('    ### **THE_LOAD_BEARING_MAP.md IS UNCHANGED SINCE BEFORE THIS ACT : %s**' % d4)
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DISAGREE/G-NORECONCILE')

    # -------------------------------------------------------------- BAR 4, THE PARTITION BAR
    print(chr(10) + '  G-PARTITION (BAR 4):')
    p1 = C2['sums_ok'] is True
    p2 = all(r['sums'] for r in C2['per'])
    p3 = sum(C2['totals'].values()) == C2['rows']
    p4 = sum(r['rows'] for r in C2['per']) == C2['rows']
    # ### **AND THE ROW COUNT AGREES WITH THE SURVEY THAT RAN BEFORE THE LOCK.**
    p5 = C2['rows'] == E['rows_total'] == C1['rows_total']
    gp = p1 and p2 and p3 and p4 and p5
    for r in C2['per']:
        print('    %-8s rows %-4d categories %-4d sums : %s'
              % (r['tag'], r['rows'], sum(r['counts'].values()), r['sums']))
    print('    ### **TOTAL ROWS %d ; CATEGORY TOTAL %d ; PRE-LOCK SURVEY %d**'
          % (C2['rows'], sum(C2['totals'].values()), E['rows_total']))
    print('    ### **A PARTITION THAT DOES NOT SUM IS NOT A PARTITION.**')
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PARTITION')

    # ---------------------------------------------------------------- BAR 5, THE PREMISE BAR
    print(chr(10) + '  G-PREMISE (BAR 5):')
    m1 = C2['interfaces_with_premise'] == C2['totals'].get('INTERFACES', 0)
    # ### **A ROW THAT COULD NOT NAME ITS PREMISE WAS RE-COUNTED UNREADABLE, NOT LEFT IN THE BIN.**
    reclassed = [u for u in C2['unreadable'] if 'no nameable premise' in u['evidence']]
    m2 = 'RE-COUNTED `UNREADABLE` RATHER THAN LEFT IN' in bank or 'RE-COUNTED' in bu
    m3 = 'EVERY INTERFACES ROW NAMES ITS PREMISE' in bu.replace('`', '')
    gm = m1 and m2 and m3
    print('    ### **INTERFACES ROWS : %d ; WITH A NAMED PREMISE : %d**'
          % (C2['totals'].get('INTERFACES', 0), C2['interfaces_with_premise']))
    print('    ### **ROWS RE-COUNTED UNREADABLE FOR WANT OF A NAMEABLE PREMISE : %d**'
          % len(reclassed))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-PREMISE')

    # ------------------------------------------------------------- BAR 6, THE UNREADABLE BAR
    print(chr(10) + '  G-UNREADABLE (BAR 6):')
    u1 = C2['unreadable_n'] == C2['totals'].get('UNREADABLE', 0)
    u2 = all(u.get('tag') and u.get('line') for u in C2['unreadable'])
    # ### **NAMED IN THE RUN RECORD, BY DOCUMENT AND LINE.**
    u3 = all(('`%-7s` line %-6d' % (u['tag'], u['line'])) in acrun for u in C2['unreadable'][:5])
    u4 = 'NEVER ASSIGNED' in bu
    # ### **AND (E1) REGISTERED THAT A RESIDUE WAS EXPECTED. ### A ZERO RESIDUE WOULD MAKE THE
    # ### PREDICATE SUSPECT, AND THE ACT SAID SO IN ADVANCE.**
    u5 = C2['unreadable_n'] > 0
    gu = u1 and u2 and u3 and u4 and u5
    print('    ### **UNREADABLE ROWS : %d, EACH NAMED BY DOCUMENT AND LINE : %s**'
          % (C2['unreadable_n'], u2 and u3))
    print('    ### **NEVER ASSIGNED : %s ; THE RESIDUE IS NON-ZERO AS (E1) REGISTERED : %s**'
          % (u4, u5))
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNREADABLE')

    # ------------------------------------------------- BAR 7, THE NO-RECOMMENDATION BAR
    print(chr(10) + '  G-NORECOMMEND / G-NOPREFER / G-QUESTIONUNMOVED / G-SCOPE (BAR 7):')
    c_start = bank.find('### COMPONENT 3 -- THE QUESTION ANSWERED FROM PRACTICE')
    c_end = bank.find('### COMPONENT 4 -- THE SEAT')
    cregion = bank[c_start:c_end] if (c_start >= 0 and c_end > c_start) else ''
    raw, live = [], []
    for mm in PREFER.finditer(cregion):
        before2 = cregion[max(0, mm.start() - 100):mm.start()]
        raw.append(mm.group(0))
        if not NEG2.search(before2):
            live.append((mm.group(0), cregion[max(0, mm.start() - 60):mm.end() + 20]
                         .replace(chr(10), ' ')))
    n1 = bool(cregion) and not live
    n2 = C3['recommended'] == 0 and C3['question_moved'] is False
    n3 = C3['dispositions_quoted'] == 3
    # ### **THE SCOPE IS NAMED, NOT LEFT TO TRAVEL.**
    n4 = ('THE SCOPE, NAMED SO THE COUNT CANNOT TRAVEL' in bu
          and str(C3['documents_counted']) in bank and str(C3['rows']) in bank)
    n5 = 'A BEARING IS NOT AN ANSWER' in bu
    gn = n1 and n2 and n3 and n4 and n5
    print('    ### raw preference-word hits in Component 3 : %s' % (sorted(set(raw)) or 'none'))
    for w, ctx in live:
        print('        ### ### **LIVE HIT** `%s` : %s' % (w, ctx[:110]))
    print('    ### **RECOMMENDED : %d ; THE QUESTION MOVED : %s ; DISPOSITIONS QUOTED : %d**'
          % (C3['recommended'], C3['question_moved'], C3['dispositions_quoted']))
    print('    ### **THE SCOPE IS NAMED : %s ; A BEARING IS NOT AN ANSWER : %s**' % (n4, n5))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORECOMMEND/G-NOPREFER/G-QUESTIONUNMOVED/G-SCOPE')

    # ----------------------------------------------------------------- BAR 8, THE MEMORY BAR
    print(chr(10) + '  G-MEMORY / G-POINTERS (BAR 8):')
    y1 = C4['pointers_dropped'] == 0 and C4['pointers_unresolved'] == 0
    y2 = C4['entries_after'] >= C4['entries_before']
    y3 = C4['hooks_checked'] > 0 and C4['screen_flagged'] >= C4['lost_n']
    y4 = C4['judged_covered'] + C4['lost_n'] == C4['screen_flagged']
    # ### **NO FLAG WAS LEFT UNJUDGED.** ### An unjudged flag counted either way is a guess.
    y5 = all(j['verdict'] in ('COVERED', 'LOST') for j in C4['judged'])
    # ### **THE COMPARISON IS PRINTED, NOT ASSERTED**, and the artifact is named as an artifact.
    y6 = ('THE ORDER ASKED FOR THE FILE`S PRIOR BLOB AND THERE IS NONE' in bank
          and C4['has_blob'] is False and 'AN ARTIFACT, NOT A BLOB' in bu)
    # ### **AND EVERY RESTORATION WENT INTO A FILE THE INDEX POINTS AT, BY APPENDING.**
    y7 = True
    for r in C4['restored']:
        fp = os.path.join(MEMDIR, r['pointer'])
        y7 = y7 and os.path.exists(fp) and 'Restored b387' in io.open(
            fp, encoding='utf-8', errors='replace').read()
    y8 = len(C4['restored']) == C4['lost_n']
    gy = y1 and y2 and y3 and y4 and y5 and y6 and y7 and y8
    print('    ### **POINTERS DROPPED : %d ; RESOLVING TO NO FILE : %d**'
          % (C4['pointers_dropped'], C4['pointers_unresolved']))
    print('    entries %d -> %d ; hooks checked %d ; screen flagged %d'
          % (C4['entries_before'], C4['entries_after'], C4['hooks_checked'],
             C4['screen_flagged']))
    print('    ### **JUDGED COVERED %d + LOST %d == FLAGGED %d : %s ; NONE LEFT UNJUDGED : %s**'
          % (C4['judged_covered'], C4['lost_n'], C4['screen_flagged'], y4, y5))
    print('    ### **NO PRIOR BLOB, AND THE ARTIFACT IS NAMED AS AN ARTIFACT : %s**' % y6)
    print('    ### **RESTORATIONS : %d, EACH APPENDED INTO THE FILE ITS POINTER NAMES : %s**'
          % (len(C4['restored']), y7 and y8))
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-MEMORY/G-POINTERS')

    # --------------------------------------------- G-NOROWEDIT / G-NOTABLEEDIT / G-R16
    print(chr(10) + '  G-NOROWEDIT / G-NOTABLEEDIT / G-R16:')
    # ### **NOT ONE OF THE FOURTEEN DOCUMENTS MOVED.** ### Measured against the pre-act commit.
    touched = []
    for sv in E['survey']:
        if git(PP, 'diff', '--name-only', preact(PP), '--', sv['rel']).strip():
            touched.append(sv['rel'])
    r1 = not touched
    r2 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'README.md').strip()
    r3 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md').strip()
    # ### **(R16) IS RECORDED WITH ITS REASON, AND NO HOOK COPY WAS DELETED.**
    r4 = ('(R16)' in tblk and 'THE UNTRACKED HOOK COPIES STAY' in tblk.upper()
          and 'fallback' in tblk.lower())
    legacy = [(n, os.path.exists(os.path.join(rp, '.git', 'hooks', 'pre-push')))
              for n, rp in b303_pins.REPOS]
    r5 = all(ex for _n, ex in legacy)
    gr = r1 and r2 and r3 and r4 and r5
    print('    ### **KEYSTONE DOCUMENTS CHANGED SINCE BEFORE THIS ACT : %d** %s'
          % (len(touched), touched or ''))
    print('    README.md unchanged : %s ; the taxonomy unchanged : %s' % (r2, r3))
    print('    ### **(R16) RECORDED IN THE TRAIL BLOCK WITH ITS REASON : %s**' % r4)
    print('    ### **EVERY `.git/hooks/pre-push` STILL PRESENT : %s** %s' % (r5, legacy))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-NOROWEDIT/G-NOTABLEEDIT/G-R16')

    # ------------------------------------------------------------------ G-NOKERNEL
    print(chr(10) + '  G-NOKERNEL:')
    # ### **THIS ACT READ WHAT ROWS SAY AND OPENED NO KERNEL.** ### The claim is on the face and
    # ### in the bank; here it is measured against this act`s own code.
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b387_') and x.endswith('.py')))
    kernelish = ('print axioms', 'lake ', 'lean ', 'LEAN_PATH', '.olean')
    khits = [(x, k) for x in mymods0 for k in kernelish if k in strip_prose(t(x))]
    k1 = not khits
    k2 = 'A COUNT OF *CLAIMED* STATUS' in bank or 'COUNT OF CLAIMED STATUS' in bu
    k3 = 'OPENED NO KERNEL' in bu
    gk = k1 and k2 and k3
    print('    kernel-invoking strings in this act`s stripped code : %s' % (khits or 'none'))
    print('    ### **THE WORD `CLAIMED` IS CARRIED WITH THE FIGURES : %s ; AND THE LIMIT IS '
          'STATED : %s**' % (k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-NOKERNEL')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = 'The four open lists are restated OPEN by name' in tblk
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
               'PLACE-papers': {'OPEN_TRAILS.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b387' not in x)
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
    t3 = len(rws) == 1 and anc and 'NINE OF THE FOURTEEN KEYSTONES' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('what-the-keystones-tables-actually-carry returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the union was corrected', 'a row was edited',
              'the citation question is answered', 'an unreadable row was assigned'))
    t6 = (Q['trail']['says_r16'] and Q['trail']['says_not_reconciled']
          and Q['trail']['says_no_closure'] and Q['trail']['says_claimed'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK RECORDS (R16), SAYS NOT RECONCILED, SAYS A MEASUREMENT IS '
          'NOT A CLOSURE, AND CARRIES THE WORD CLAIMED** : %s' % t6)
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
    mirrorp = d('b387_mirror.txt')
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
        ('face-subject gates %d' % LG['face_subject_gates'], str(LG['face_subject_gates']) in bank),
        ('the union names %d' % C1['union_names'], str(C1['union_names']) in bank),
        ('with a table %d' % C1['with_table'], str(C1['with_table']) in bank),
        ('rows %d' % C2['rows'], str(C2['rows']) in bank),
        ('unreadable %d' % C2['unreadable_n'], str(C2['unreadable_n']) in bank),
        ('not machine-verified %d' % C3['not_machine_verified'],
         str(C3['not_machine_verified']) in bank),
        ('hooks checked %d' % C4['hooks_checked'], str(C4['hooks_checked']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
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
                          if x.startswith('b387_') and x.endswith('.py')))
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
              if x.strip() and 'b387' not in x and x.strip() not in DECLARED_W]
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
             d('b387_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b387_checks.py'), 'its own fixtures'),
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

    marker = '# ### WHAT THE KEYSTONES` TABLES ACTUALLY CARRY (b387).'
    nxt = '# ### THE GUARD MADE SINGLE-SOURCED (b386).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b387_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b387_hedge_')
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
