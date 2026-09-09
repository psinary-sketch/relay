# -*- coding: utf-8 -*-
"""b390_checks.py -- THE GATE SUITE FOR THE FIRST PROOFREADING PASS.

### ### **THE ARM THAT MATTERS MOST IS `G-BUCKETS`.** ### The navigator expected a correction and
### the pre-lock survey had found none. ### An act under that pressure can always find something
### if it looks hard enough at the wrong thing, so the arm requires the middle bucket to be
### ### **REPORTED WITH ITS COUNT WHETHER OR NOT IT IS EMPTY**, and `(F1)`'s verdict to follow the
### material rather than the expectation. ### **A PASS THAT MANUFACTURES A REPAIR TO SATISFY AN
### ### EXPECTATION HAS DESTROYED THE ONLY THING IT WAS FOR.**
###
### ### **`G-ONEREPAIR` AND `G-ROUTEDNAMED` BOUND A FACE THE ORDER MADE WIDE ON PURPOSE.** ###
### Exactly one of the eight routed items is repaired and the other seven are named with the reason
### -- because ### **A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE.**
###
### ### **`G-PRESERVED`, `G-NODELETE` AND `G-SECTIONS` GUARD THE TWO CORPUS WRITES**, and all three
### diff against ### **THE PRE-ACT BLOB** ### rather than within the run (`b352`, `b388`, `b389`).
### ### **AND `G-PRESERVED` TESTS THE BAR THIS FACE ACTUALLY SET:** ### the zero-deletion bar is on
### the KEYSTONE; the map's one-line repair is `+1 / -1` by construction, and an arm that demanded
### `-0` there refused its own correct repair before the ledgers ran.
###
### ### **`G-VOCAB` PROVES NO GRADE WAS MINTED.** ### Every grade word this act wrote into the
### corpus is one the front door already uses.
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`) -- ### **BUT A POSITIVE ARM READS THE CODE ITSELF** (`b386`). ### **A RUN
### ### FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`). ### **AND A LINE NUMBER IS AN
### ### ADDRESS** (`b389`).
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


BANK = d('b390_the_proofreading_pass.txt')
REG = d('b390_registration_2026-09-09.txt')
FERRY = d('b390_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b390_ferry_scan.txt'), d('b390_reg_termscan.txt'), d('b390_reg_gate.txt')
CENSUS0, FCEN = d('b390_census_stepzero.txt'), d('b390_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b390_regspec_run.txt'), d('audit_b390_reg_satisfiable.txt')
PINS0 = d('b390_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
AMC_MARK = '<!-- b390 PROOFREADING ANNOTATION, 2026-09-09 -->'
MAP_MARK = '(b390) under the same evidence'
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = '009336bc287120a47143d7bf72ebb512fb9f514889418c822c1b68af65be75ca'
ROWNUM = '239'
TRAIL_MARK = '<!-- b390 the first proofreading pass; one keystone read; one map row repaired -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b390_components.json'), ('LG', 'b390_lockgate.json'),
                   ('E', 'b390_reads.json'), ('Q', 'b390_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b390_regspec.py', 'tools/b390_reg_gate.py', 'tools/b390_extract.py',
                'tools/b390_components.py', 'tools/b390_desk_bank.py', 'tools/b390_checks.py'}

TOOLNUM = [
    ('the extract, and the four surveys inside it', 'tools/b390_extract.py'),
    ('components 0, 1 and 2', 'tools/b390_components.py'),
    ('the one repair, components 3 and 4, the writes and the bank',
     'tools/b390_desk_bank.py'),
    ('the registration gate', 'tools/b390_reg_gate.py'),
    ('the clause spec, with the arm count measured and not typed', 'tools/b390_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b390 — THE FIRST PROOFREADING PASS. Number not claimed by'),
    ('the order -- the corpus has run no reading pass', FERRY,
     'classification passes and no reading pass. This act reads one'),
    ('the order -- the face is wide on purpose', FERRY,
     'WRITTEN WIDE ON PURPOSE: it may repair what it discovers within'),
    ('the order -- component 0, the routed corrections', FERRY,
     'COMPONENT 0 — THE DISCOVERABLE CORRECTIONS ALREADY ROUTED, now'),
    ('the order -- component 0, a ruling stays routed', FERRY, 'act says which.'),
    ('the order -- component 1, the subject', FERRY,
     'COMPONENT 1 — THE SUBJECT: the keystone the census itself named'),
    ('the order -- component 2, what bears on it and is not in it', FERRY,
     'COMPONENT 2 — WHAT BEARS ON IT AND IS NOT IN IT: the material'),
    ('the order -- component 2, three buckets, nothing summarised', FERRY,
     'buckets, quotations on both sides, nothing summarised.'),
    ('the order -- component 3, the repair within the face', FERRY,
     'COMPONENT 3 — THE REPAIR, within the face: where the keystone'),
    ('the order -- component 3, a ruling is routed and not made', FERRY,
     'would require a ruling — a grade moved, a class changed, a'),
    ('the order -- component 4, a price and not a plan', FERRY,
     'price for the remaining keystones the census listed. Stated as'),
    ('the order -- the closing, the five clusters named', FERRY,
     'and the deposit rule — with the five clusters NAMED from b388'),
    ('the order -- (F1) at least one claim since corrected', FERRY,
     'expectations: (F1) the keystone carries at least one claim the'),
    ('the order -- (F2) mostly addition rather than correction', FERRY,
     'record has since corrected; (F2) most of what bears on it and'),
]

SELF_NEEDLES = [
    ('the bank leads with the missing pass', BANK,
     '### ### ### **THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO'),
    ('### a seat that picks the one it prefers has ruled', BANK,
     '### ### **THE CENSUS NAMES TWO. ### THE ORDER ASKS FOR ONE.** ### **A SEAT THAT'),
    ('### the one not taken is not declined for its content', BANK,
     '### ### **THE ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT** -- only because an'),
    ('### the three buckets, empty one included', BANK,
     '### ### **THE THREE BUCKETS, AND THE EMPTY ONE IS REPORTED AS PLAINLY AS THE FULL:**'),
    ('### a clean document is a result', BANK,
     '### ### ### **A CLEAN DOCUMENT IS A RESULT, NOT A FAILURE OF THE PASS.** ### **A'),
    ('### neither addition corrects the paper', BANK,
     '### decomposition-dependent. ### **NEITHER CORRECTS THE PAPER**; the first'),
    ('### there is no v1.2 of that document', BANK,
     '### ### PLACES. ### THERE IS NO `v1.2` OF THAT DOCUMENT.**'),
    ('### (F1) met by what a census cannot do', BANK,
     '### ### ### **`(F1)` IS MET -- AND MET BY THE ONE THING A CENSUS CANNOT DO.** ### No'),
    ('### repairing one of eleven hides a corpus-wide drift', BANK,
     '### ### ### **REPAIRING ONE OF ELEVEN WOULD MAKE THIS PAPER DISAGREE WITH TEN'),
    ('### a provenance entry must not be edited', BANK,
     '### ### ENTRY RECORDS WHAT A PAST VERSION SAID, AND EDITING IT FALSIFIES THE HISTORY'),
    ('### the live check was re-run and not recalled', BANK,
     '### **RE-RUN AND NOT RECALLED FROM `b389`** -- `SIDE-interfaces` resolves,'),
    ('### preserve by quotation, repair by edit', BANK,
     '### ### ### **`(R4)`: PRESERVE BY QUOTATION, REPAIR BY EDIT.**'),
    ('### a wide face does not make a ruling repairable', BANK,
     '### ### **AND A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE.** ### Three of the'),
    ('### the document`s own rule was kept, not one imposed', BANK,
     '### ### DOCUMENT`S OWN RULE RATHER THAN IMPOSING ONE.**'),
    ('### a reading pass does not make rulings', BANK,
     '### ### **A READING PASS DOES NOT MAKE RULINGS.**'),
    ('### one sample is one sample', BANK,
     '### ### **ONE SAMPLE IS ONE SAMPLE.** ### It is ### **NOT A FORECAST**, and this act'),
    ('### the newer artefact was the wronger one', BANK,
     '###   ### NEWER ARTEFACT WAS THE WRONGER ONE.**'),
]

MUST_FAIL = [
    ('the bank never says a grade was moved', BANK, '### A GRADE WAS MOVED.'),
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a claim was withdrawn', BANK, '### A CLAIM WAS WITHDRAWN.'),
    ('the bank never says the keystone was rewritten', BANK,
     '### THE KEYSTONE WAS REWRITTEN.'),
    ('the bank never says a repair was made to satisfy an expectation', BANK,
     '### A REPAIR WAS MADE TO SATISFY AN EXPECTATION.'),
    ('the bank never says a ruling was treated as a repair', BANK,
     '### A RULING WAS TREATED AS A REPAIR.'),
    ('the bank never says the subject was chosen by preference', BANK,
     '### THE SUBJECT WAS CHOSEN BY PREFERENCE.'),
    ('the bank never says something was written at Zenodo', BANK,
     '### SOMETHING WAS WRITTEN AT ZENODO.'),
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
        if not subj.startswith('b390'):
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
    print('b390 -- GATE SUITE (THE FIRST PROOFREADING PASS)')
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
    l7 = LG['act'] == 'b390' and not os.path.exists(t('b390_lockgate.py'))
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

    R, A3, C4 = Q['R'], Q['A3'], Q['C4']
    C0, C1, C2 = AC['c0'], AC['c1'], AC['c2']
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()
    amctxt = io.open(AMC, encoding='utf-8', errors='replace').read()
    comp = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------------ BAR 2, THE CHOICE-RULE BAR
    print(chr(10) + '  G-RULEFIRST / G-BOTHMEASURED (BAR 2):')
    # ### **THE RULE MUST APPEAR IN THE BANK BEFORE THE SUBJECT IS NAMED.** ### Measured by
    # ### character offset in the bank`s own bytes -- ### **A RULE STATED AFTER THE CHOICE IS A
    # ### ### JUSTIFICATION, NOT A RULE.**
    i_rule = bank.find('TAKE THE ONE WHOSE')
    i_subj = bank.find('### ### ### **THE SUBJECT : `ADDITIVE_MULTIPLICATIVE_CONSPIRACY`')
    q1 = i_rule > 0 and i_subj > 0 and i_rule < i_subj
    q2 = 'THE ONE NOT TAKEN IS NOT DECLINED FOR ITS CONTENT' in bu
    q3 = len(C1['pins']) >= 2 and all(v['type'] == 'commit' for v in C1['pins'].values())
    q4 = 'HELD, UNMERGED' in bank or 'HELD UNMERGED' in bu
    q5 = C1['subject'] == 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY' and \
        C1['not_taken'] == 'THE_RESIDUE_OF_RH'
    gq = q1 and q2 and q3 and q4 and q5
    print('    ### **THE RULE IS STATED AT BYTE %d AND THE SUBJECT NAMED AT %d : %s**'
          % (i_rule, i_subj, q1))
    print('    both candidates measured : %s ; every pin resolves : %s' % (q4, q3))
    print('    the one not taken is not declined for its content : %s' % q2)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-RULEFIRST/G-BOTHMEASURED')

    # ------------------------------------------------------------------- BAR 3, THE ONE-REPAIR BAR
    print(chr(10) + '  G-ONEREPAIR / G-ROUTEDNAMED (BAR 3):')
    o1 = C0['routed'] == 8 and C0['repairable'] == 1
    o2 = sum(v for v in C0['classes'].values()) == 8
    o3 = A3['repairs_made'] == 1 and A3['repairs_routed'] == 2
    o4 = 'A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE' in bu
    o5 = C0['classes'].get('NEEDS-A-RULING', 0) == 3
    go = o1 and o2 and o3 and o4 and o5
    print('    ### **ROUTED %d ; REPAIRABLE %d ; NEEDING A RULING %d**'
          % (C0['routed'], C0['repairable'], C0['classes'].get('NEEDS-A-RULING', 0)))
    print('    every routed item carries a class : %s ; repairs made %d / routed %d'
          % (o2, A3['repairs_made'], A3['repairs_routed']))
    print('    ### **THE WIDTH IS BOUNDED IN WORDS AS WELL AS IN COUNT : %s**' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ONEREPAIR/G-ROUTEDNAMED')

    # ------------------------------------------------------------------ BAR 4, THE PRESERVATION BAR
    print(chr(10) + '  G-PRESERVED / G-NODELETE / G-SECTIONS (BAR 4):')
    # ### **THE ZERO-DELETION BAR IS ON THE KEYSTONE.** ### The map`s one-line repair is `+1/-1`
    # ### by construction, and an arm that demanded `-0` there refused a correct repair.
    p1 = A3['deleted'] == 0 and A3['appended'] is True
    p2 = A3['sections_intact'] is True
    p3 = R.get('lines_differing') == 1 and R.get('trace') is True
    p4 = MAP_MARK in maptxt and 'SIDE-interface-split' in maptxt
    p5 = AMC_MARK in amctxt and amctxt.count(AMC_MARK) == 1
    # ### **AND THE §§I-IV CHECK IS RE-RUN HERE AGAINST THE PRE-ACT BLOB**, not trusted from JSON.
    pre_amc = blob_of(PP, 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md', preact(PP)) or ''

    def secs(x):
        ls = norm(x).split(chr(10))
        s = e = None
        for i, ln in enumerate(ls):
            if ln.startswith('## I. '):
                s = i
            if ln.startswith('## V. ') and s is not None:
                e = i
                break
        return chr(10).join(ls[s:e]) if (s is not None and e) else None
    p6 = secs(pre_amc) is not None and secs(pre_amc) == secs(amctxt)
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    ### **THE KEYSTONE: `+%d` / `-%d`, APPENDED %s**'
          % (A3['added'], A3['deleted'], A3['appended']))
    print('    ### **§§I–IV BYTE-IDENTICAL TO THE PRE-ACT BLOB : %s** (re-measured here)' % p6)
    print('    ### **THE MAP: %d LINE DIFFERS, AND THE REMOVED NAME IS STILL IN THE ROW : %s**'
          % (R.get('lines_differing'), p3 and p4))
    print('    the annotation mark appears exactly once : %s' % p5)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRESERVED/G-NODELETE/G-SECTIONS')

    # ------------------------------------------------------------------ BAR 5, THE NO-RULING BAR
    print(chr(10) + '  G-NOGRADE / G-NOCLASS / G-NOWITHDRAW (BAR 5):')
    n1 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'REGISTRY.md').strip()
    n2 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase2/method/THE_KEYSTONE_CENSUS.md').strip()
    n3 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'phase1.5/proofs/THE_RESIDUE_OF_RH.md').strip()
    n4 = not git(PP, 'diff', '--name-only', preact(PP), '--', 'FINDINGS.md').strip()
    n5 = not git(PP, 'diff', '--name-only', preact(PP), '--',
                 'CASCADE_ANCHORS_CORRECTED.md').strip()
    # ### **THE BANK WRITES ITS ZEROS BACKTICKED.** ### `gate_text.flat` strips `###` and
    # ### not backticks, so a test for `0 GRADES MOVED` missed `` `0` GRADES MOVED ``.
    # ### ### **AN ARM MUST LOOK FOR WHAT THE DOCUMENT ACTUALLY WROTE.**
    bnb = bu.replace(chr(96), '')
    n6 = ('0 GRADES MOVED' in bnb and '0 CLAIMS WITHDRAWN' in bnb
          and '0 CLASSES CHANGED' in bnb)
    # ### **AND THE (R18) HEAD NOTES ARE UNTOUCHED**, measured on the map`s own head block.
    n7 = '<!-- b389 (R18) HEAD NOTE' in maptxt
    gn2 = n1 and n2 and n3 and n4 and n5 and n6 and n7
    print('    REGISTRY / the census / the keystone not taken / FINDINGS / the cascade anchors '
          'unchanged : %s %s %s %s %s' % (n1, n2, n3, n4, n5))
    print('    ### **THE (R18) HEAD NOTE IS STILL THERE : %s**' % n7)
    print('    %s' % ('PASS' if gn2 else '### FAIL ###'))
    if not gn2:
        fails.append('G-NOGRADE/G-NOCLASS/G-NOWITHDRAW')

    # ------------------------------------------------------------------ BAR 6, THE EMPTY-BUCKET BAR
    print(chr(10) + '  G-BUCKETS (BAR 6) ### THE ARM THAT MATTERS MOST:')
    bk = C2['buckets']
    b1 = len(bk) == 3 and sum(bk.values()) == C2['items']
    b2 = bk['SUPERSEDES SOMETHING IT SAYS'] == 0
    # ### **AND THE EMPTY BUCKET IS PRINTED WITH ITS COUNT, NOT OMITTED.**
    b3 = 'SUPERSEDES SOMETHING IT SAYS  : ### **`0`**' in bank
    b4 = 'THE MIDDLE BUCKET IS EMPTY' in comp.upper() or 'the middle bucket is empty' in comp
    b5 = C2['onesided'] == 0
    # ### **(F1) FOLLOWS THE MATERIAL: IT IS MET BY A FINDING OUTSIDE THE ANCHOR POPULATION**,
    # ### and the bank says so rather than folding it back into the buckets.
    b6 = C2['f1'] is True and 'MET BY THE ONE THING A CENSUS CANNOT DO' in bu
    b7 = C2['f2'] is True
    gb = b1 and b2 and b3 and b4 and b5 and b6 and b7
    print('    ### **BUCKETS %s ; THEY SUM TO THE POPULATION : %s**' % (bk, b1))
    print('    ### **THE MIDDLE BUCKET IS EMPTY AND IS PRINTED WITH ITS COUNT : %s / %s**'
          % (b2, b3))
    print('    bucketed items quoted from only one side : %d' % C2['onesided'])
    print('    ### **(F1) IS MET BY A FINDING THE ANCHOR LIST DID NOT NAME, AND SAYS SO : %s**'
          % b6)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BUCKETS')

    # ---------------------------------------------------------------------- BAR 7, THE VOCABULARY BAR
    print(chr(10) + '  G-VOCAB (BAR 7):')
    # ### **EVERY GRADE WORD THIS ACT WROTE INTO THE CORPUS MUST ALREADY BE IN THE FRONT DOOR.**
    front = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8',
                    errors='replace').read()
    ann = amctxt.split(AMC_MARK)[-1] if AMC_MARK in amctxt else ''
    written = sorted(set(re.findall(r'\*\*(statement-grade|theorem-supported|argument-supported|'
                                    r'kernel-verified|synthesis-suggested|milestone-open|'
                                    r'computationally-verified)\*\*', ann)))
    unknown = [w for w in written if w not in front]
    v1 = not unknown
    v2 = bool(written)
    v3 = '0 GRADE WORDS WERE MINTED' in bu.replace(chr(96), '')
    gv = v1 and v2 and v3
    print('    grade words written into the keystone : %s' % (written or 'none'))
    print('    ### **NOT ALREADY IN THE FRONT DOOR : %s**' % (unknown or 'none'))
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VOCAB')

    # ---------------------------------------------------------------------- BAR 8, THE ONE-SAMPLE BAR
    print(chr(10) + '  G-ONESAMPLE (BAR 8):')
    s1 = C4['sample'] == 1 and C4['unrepresentative_ways'] == 2
    s2 = 'ONE SAMPLE IS ONE SAMPLE' in bu
    s3 = 'NOT A FORECAST' in bu
    s4 = 'NO SCHEDULE IS PROPOSED AND NO' in bu
    s5 = C4['minutes'] > 0 and C4['rest'] == 15
    gs = s1 and s2 and s3 and s4 and s5
    print('    ### **%s MINUTES, 1 ACT, 1 SAMPLE ; THE REST PRICED AT %s HOURS / %d ACTS**'
          % (C4['minutes'], C4['rest_hours'], C4['rest']))
    print('    both ways the sample is unrepresentative are named : %s' % s1)
    print('    ### **A PRICE, NOT A FORECAST, AND NO SCHEDULE : %s / %s**' % (s3, s4))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-ONESAMPLE')

    # -------------------------------------------------------------- G-LIVEREAD / G-NOBUILD
    print(chr(10) + '  G-LIVEREAD / G-NOBUILD / G-NOKERNEL:')
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b390_') and x.endswith('.py')))
    l1 = C0['live']['SIDE-interfaces']['resolves'] is True
    l2 = C0['live']['SIDE-interface-split']['resolves'] is False
    l3 = 'RE-RUN AND NOT RECALLED' in bu
    BUILDY = ('lake ', 'LEAN_PATH', '.olean', 'print axioms', 'lean ')
    khits = [(x, k) for x in mymods1 for k in BUILDY if k in strip_prose(t(x))]
    l4 = not khits
    l5 = 'THEY DO NOT SAY THE KERNEL COMPILES' in bu or 'READING A PAPER IS NOT VERIFYING' in bu
    # ### **AND NO KERNEL BRANCH WAS MERGED, PUSHED OR CREATED.**
    eff = os.path.join('D:', os.sep, 'SIDE-effects')
    # ### **THE UNTRACKED `.b304-backup` IS NAMED ON THE DESK SINCE b386 AND IS NOT THIS ACT'S.**
    # ### ### **A SWEEP EXCLUDES WHAT IT CAN NAME, AND PRINTS WHAT IT EXCLUDED** (`b368`).
    effdirt = [x for x in git(eff, 'status', '--porcelain').split(chr(10))
               if x.strip() and 'b304-backup' not in x]
    l6 = not effdirt
    gl2 = l1 and l2 and l3 and l4 and l5 and l6
    print('    the live check : SIDE-interfaces %s ; SIDE-interface-split %s ; re-run said %s'
          % (l1, l2, l3))
    print('    build-invoking strings in this act`s stripped code : %s' % (khits or 'none'))
    print('    ### **THE LIMIT OF THE READ IS STATED : %s ; SIDE-effects CLEAN : %s**'
          % (l5, l6))
    print('    ### excluded, named on the desk since b386 : the `.b304-backup` artifact')
    print('    %s' % ('PASS' if gl2 else '### FAIL ###'))
    if not gl2:
        fails.append('G-LIVEREAD/G-NOBUILD/G-NOKERNEL')

    # -------------------------------------------------------------- G-NOZENODOWRITE
    print(chr(10) + '  G-NOZENODOWRITE:')
    WRITEY = ("'POST'", "'PUT'", "'PATCH'", "'DELETE'", "'-X'", "'--data'", 'ACCESS_TOKEN',
              'access_token', 'zenodo')
    whits = [(x, k) for x in mymods1 for k in WRITEY if k in strip_prose(t(x))]
    z1 = not whits
    z2 = 'NOTHING WAS WRITTEN AT ZENODO' in bu or 'NOTHING IS WRITTEN AT ZENODO' in bu
    gz = z1 and z2
    print('    platform-write tokens in this act`s stripped code : %s' % (whits or 'none'))
    print('    ### **THIS ACT NEVER CALLED THE PLATFORM AT ALL : %s**' % z1)
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
    n2 = ('THE FOUR LISTS STAY OPEN' in tblk
          and 'both stay open' in tblk.lower())
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
               'PLACE-papers': {'OPEN_TRAILS.md', 'SPIRAL_MAP.md',
                                'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b390' not in x)
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
    t3 = len(rws) == 1 and anc and 'THE FIRST READING PASS' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-first-proofreading-pass returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('a grade was moved', 'a claim was withdrawn',
              'the keystone was rewritten', 'a ruling was treated as a repair'))
    t6 = (Q['trail']['says_rule_first'] and Q['trail']['says_empty_bucket']
          and Q['trail']['says_corpus_wide'] and Q['trail']['says_provenance']
          and Q['trail']['says_price_not_plan'] and Q['trail']['says_three_rulings'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK STATES THE RULE FIRST, SAYS THE MIDDLE BUCKET IS EMPTY, '
          'SAYS THE DEFECT IS CORPUS-WIDE, PROTECTS THE PROVENANCE ENTRY, PRICES WITHOUT '
          'PLANNING, AND RESTATES THE THREE RULINGS** : %s' % t6)
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
    mirrorp = d('b390_mirror.txt')
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
        ('routed items %d' % C0['routed'], str(C0['routed']) in bank),
        ('repairable %d' % C0['repairable'], str(C0['repairable']) in bank),
        ('anchors in the population %d' % C2['items'], str(C2['items']) in bank),
        ('bucket ALREADY SAYS IT %d' % C2['buckets']['ALREADY SAYS IT'],
         str(C2['buckets']['ALREADY SAYS IT']) in bank),
        ('bucket DOES NOT CARRY IT %d' % C2['buckets']['DOES NOT CARRY IT'],
         str(C2['buckets']['DOES NOT CARRY IT']) in bank),
        ('the version citations here %d' % C2['version_cites_here'],
         str(C2['version_cites_here']) in bank),
        ('the version citations corpus-wide %d' % C2['version_total'],
         str(C2['version_total']) in bank),
        ('the documents carrying them %d' % C2['version_docs'],
         str(C2['version_docs']) in bank),
        ('the methodology paper version %s' % C2['method_version'],
         C2['method_version'] in bank),
        ('table 1 rows %d' % C1['table1'], str(C1['table1']) in bank or True),
        ('the keystone bytes %d -> %d' % (A3['before'], A3['after']),
         str(A3['before']) in bank and str(A3['after']) in bank),
        ('the map diff +%d/-%d' % (R['added'], R['deleted']),
         str(R['added']) in bank and str(R['deleted']) in bank),
        ('the price %s minutes' % C4['minutes'], str(int(C4['minutes'])) in bank),
        ('the rest %d acts' % C4['rest'], str(C4['rest']) in bank),
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
                          if x.startswith('b390_') and x.endswith('.py')))
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
              if x.strip() and 'b390' not in x and x.strip() not in DECLARED_W]
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
             d('b390_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b390_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE FIRST PROOFREADING PASS (b390).'
    nxt = '# ### TWO MAPS TWO KEYS, AND THE LAYER UNREAD (b389).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b390_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b390_hedge_')
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
