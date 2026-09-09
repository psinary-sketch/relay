# -*- coding: utf-8 -*-
"""b380_checks.py -- THE GATE SUITE FOR THE ROLE AXIS, SCORED STRUCTURALLY.

### ### **THE ARM THAT MATTERS MOST HERE IS `G-CONTROL`, AND IT IS THE ONE THE ACT FAILED.** ### A
### suite that only measures what an act achieved is a suite that cannot report a failed predicate.
### ### **`G-CONTROL` REQUIRES THE CONTROL TO BE PRINTED AND ITS DISAGREEMENTS NAMED; IT DOES NOT
### ### REQUIRE THE CONTROL TO PASS**, because an act forbidden to move the threshold to fit the
### control must be free to report that the control did not come clean.
### ### **AND `G-NOOVERWRITE` MEASURES THE ORDER`S OWN WORD:** ### the prior statement-based score is
### kept beside the new one and never overwritten, for every document.
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`); ### **AN ARM THAT WOULD FAIL ON A PRE-EXISTING CONDITION IS NOT MEASURING THIS
### ### ACT** (`b375`); and ### **A RUN FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
"""
import ast
import collections
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
import gate_hash          # noqa: E402
import role_structure as RSTR   # noqa: E402
import b380_extract as EX     # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b380_the_role_axis_scored_structurally.txt')
EVID = d('b380_ruling_evidence.txt')
REG = d('b380_registration_2026-09-08.txt')
FERRY = d('b380_ferry_2026-09-08.txt')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b380_ferry_scan.txt'), d('b380_reg_termscan.txt'), d('b380_reg_gate.txt')
CENSUS0, FCEN = d('b380_census_stepzero.txt'), d('b380_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b380_regspec_run.txt'), d('audit_b380_reg_satisfiable.txt')
PINS0 = d('b380_pins_stepzero.txt')
SEAL = '61ed9860968d952776e0b6fc6396a57886ae6311ca4b329817e9910b1e63d7df'
ROWNUM = '229'
TRAIL_MARK = '<!-- b380 the role axis scored structurally -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b380_reads.json'), ('LG', 'b380_lockgate.json'),
                   ('RS', 'b380_rescore.json'), ('VD', 'b380_verdict.json'),
                   ('Q', 'b380_desk.json'))}

# ### **RESOLVED BY THE RECORDED CLOCK, NEVER BY NAME** (`b358`): ### `run_clock` NUMBERS
# ### repeats, so a suite pointed at the bare stem reads the FIRST run and not the one that
# ### succeeded. ### **THE DESK'S OWN JSON RECORDS WHICH FILE IT WROTE.**
IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/role_structure.py', 'tools/b380_regspec.py', 'tools/b380_extract.py',
                'tools/b380_reg_gate.py', 'tools/b380_rescore.py', 'tools/b380_verdict.py',
                'tools/b380_desk.py', 'tools/b380_bank.py', 'tools/b380_checks.py'}

TOOLNUM = [
    ('role read from structure (SHARED), three polarities', 'tools/role_structure.py'),
    ('the premise measured and every document re-scored', 'tools/b380_rescore.py'),
    ('the verdict on the method, and the evidence file', 'tools/b380_verdict.py'),
    ('(R7), the trail block, the row and the key', 'tools/b380_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b380_bank.py'),
    ('the reads', 'tools/b380_extract.py'),
    ('the registration gate', 'tools/b380_reg_gate.py'),
    ('the clause spec', 'tools/b380_regspec.py'),
    ('THE ORIGINAL AXIS PREDICATE, IMPORTED UNMODIFIED', 'tools/b376_axes.py'),
    ('THE CORRECTED APPARATUS COLUMN, RE-READ UNMODIFIED', 'tools/b379_rescore.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

# ### **THE OWNER NEEDLES ARE THE EXTRACT TOOL`S OWN READS TABLE, IMPORTED AND NOT RETYPED.** ###
# ### Each is still re-located in ITS OWN SOURCE FILE by the anchor tool and then required to be in
# ### the extract, so nothing here is trusted from a JSON.
OWNER_NEEDLES = [(lbl, path, hint) for lbl, _tag, path, hint in EX.READS]
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')

SELF_NEEDLES = [
    ('the bank leads with both sentences', BANK,
     '### ### ### **THE ROLE COLUMN MOVED FOR THE FIRST TIME IN FIVE ACTS, AND THE PREDICATE THAT '
     'MOVED'),
    ('### the premise was measured, not assumed', BANK,
     '### ### DO. ### AN ACT THAT ASSUMES ITS OWN PREMISE CANNOT BE REFUTED BY ITS OWN RUN**, so '
     'the'),
    ('### the premise survives its own widening', BANK,
     '### ### ### **THE PREMISE SURVIVES ITS OWN WIDENING.** ### Being generous about what counts '
     'as a'),
    ('### the threshold was declared before the control ran', BANK,
     '### ### ### **THE THRESHOLD IS A CHOICE AND IT WAS DECLARED, NOT DISCOVERED.** ### The '
     'rubric`s own'),
    ('### the threshold was left where it was', BANK,
     '### when the control disagreed ### **THE THRESHOLD WAS LEFT WHERE IT WAS.**'),
    ('### no direction registered because there is none', BANK,
     '### may move in either direction and ### **NO MONOTONICITY BAR APPLIES.** ### Saying so in '
     'advance'),
    ('### the deafnesses are declared in the module itself', BANK,
     '### ### **AND WHAT IT IS DEAF TO IS DECLARED IN THE MODULE ITSELF, NOT DISCOVERED LATER:**'),
    ('### the directory stands in for the subject', BANK,
     '###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT** -- an ADDRESS standing in for a '
     'subject,'),
    ('### the control is printed before any other result', BANK,
     '### ### **THE CONTROL IS PRINTED FIRST, BEFORE ANY OTHER RESULT**, because a predicate`s '
     'agreement'),
    ('### the gatherers are not misfiled', BANK,
     '### ### **THEY ARE NOT MISFILED.** ### `FINDINGS.md` is the corpus`s findings ledger and'),
    ('### the A- column is measuring narrow reach', BANK,
     '### ### ### **SO THE `A-` COLUMN IS NOT MEASURING GATHERING. ### IT IS MEASURING NARROW '
     'REACH**,'),
    ('### a predicate that contradicts its ground truth has failed', BANK,
     '### ### **A PREDICATE THAT CONTRADICTS THE ONLY GROUND TRUTH AVAILABLE HAS FAILED, HOWEVER'),
    ('### agreement reached for the wrong reason is reported as such', BANK,
     '### two citations. ### **AGREEMENT REACHED FOR THE WRONG REASON IS REPORTED AS SUCH.**'),
    ('### reach is not argument', BANK,
     '### ### **WHICH POPULATION IT DOES NOT READ:** ### the `A+` column. ### A document that '
     'reaches'),
    ('### the A+ column is an upper bound', BANK,
     '### ### ### **SO THE `A+` COLUMN IS AN UPPER BOUND ON SYNTHESIS AND THE `A-` COLUMN IS'),
    ('### the obligation is stated and not recommended', BANK,
     '### registration required the branch to state its obligation, and ### **STATED WITHOUT BEING'),
    ('### no class is ruled in any branch', BANK,
     '### ### ### **NO CLASS IS RULED IN THIS BRANCH OR IN EITHER OF THE OTHER TWO.** ### The '
     'verdict is'),
    ('### the evidence file is a relay artifact and not a corpus document', BANK,
     '### ### ### **IT IS A RELAY BANK ARTIFACT AND NOT A TRACKING DOCUMENT IN THE CORPUS**, which '
     'no'),
    ('### a control from one side cannot test the distinction', BANK,
     '### ### DISTINCTION CANNOT TEST THE DISTINCTION**, and reporting the agreement over the seven '
     'and'),
    ('### the quadrant is part earned and part instrument', BANK,
     '### ### **A QUADRANT REACHED BY WIDENING THE OTHER AXIS IS NOT THE SAME AS A QUADRANT THE '
     'CORPUS'),
    ('### the four lists restated OPEN by name', BANK,
     '### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME AND NONE IS CLOSED.**'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a declaration was moved', BANK, '### A DECLARATION WAS MOVED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says a prior score was overwritten', BANK,
     '### A PRIOR SCORE WAS OVERWRITTEN.'),
    ('the bank never says the threshold was moved to fit the control', BANK,
     '### THE THRESHOLD WAS MOVED TO FIT THE CONTROL.'),
    ('the bank never names a preferred branch', BANK, '### THE PREFERRED BRANCH IS.'),
    ('the bank never says the registry was edited', BANK, '### THE REGISTRY WAS EDITED.'),
]

PREFER = re.compile(r'\b(recommend\w*|prefer\w*|the best option|should be adopted|we advise|'
                    r'the right choice|obviously|clearly the|the correct option|I suggest)\b', re.I)


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
    print('b380 -- GATE SUITE (THE ROLE AXIS, SCORED STRUCTURALLY)')
    print('=' * 100)
    E, LG, RS, VD, Q = _J['E'], _J['LG'], _J['RS'], _J['VD'], _J['Q']
    run = io.open(d(RS['run_file']), encoding='utf-8', errors='replace').read()
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 200:
                inx = line.rstrip()[:200] in extract
                trunc = bool(inx)
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl,
                                    '  ### -- ITS RECORDED PREFIX' if trunc
                                    else ('' if inx else '  -- NOT IN THE EXTRACT FILE')))
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
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE ORDER`S PROHIBITIONS, AS WHOLE LINES):')
    for lbl, path, line in MUST_FAIL:
        if GN.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()

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
    l7 = LG['act'] == 'b380' and not os.path.exists(t('b380_lockgate.py'))
    l8 = LG['face_sha'] == SEAL
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s' % l6)
    print('    ### **THE LOCK GATE WAS INHERITED, NOT REBUILT** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # ------------------------------------------------------------------ BAR 2, THE PREMISE BAR
    print(chr(10) + '  G-PREMISE / G-BOTHREADINGS (BAR 2):')
    POP = RS['population']
    TA, TB, TS = RS['statement_tally'], RS['statement_broad_tally'], RS['structural_tally']
    # ### **THE PREMISE MUST BE PRINTED BEFORE THE STRUCTURAL PREDICATE RUNS**, in the run file's
    # ### own order, and BOTH readings must be there -- one reading cannot fail.
    p1 = ('COMPONENT 1' in run and 'COMPONENT 2' in run
          and run.index('COMPONENT 1') < run.index('COMPONENT 2'))
    p2 = run.index('COMPONENT 1') < run.index('COMPONENT 3')
    p3 = sum(TA.values()) == sum(TB.values()) == POP
    p4 = TB.get('A?', 0) < TA.get('A?', 0)
    p5 = RS['decided_statement_broad'] > RS['decided_statement']
    p6 = all(str(x) in bank for x in (TA.get('A?', 0), TB.get('A?', 0), POP))
    p7 = 'SURVIVES ITS OWN WIDENING' in bank
    gp = p1 and p2 and p3 and p4 and p5 and p6 and p7
    print('    ### **THE PREMISE IS PRINTED BEFORE THE PREDICATE RUNS** : %s / %s' % (p1, p2))
    print('    strict NOT DETERMINABLE %d ; broad %d ; both partition the population : %s'
          % (TA.get('A?', 0), TB.get('A?', 0), p3))
    print('    ### **THE BROAD READING IS STRICTLY MORE GENEROUS** : %s / %s' % (p4, p5))
    print('    both figures in the bank : %s ; the premise survives its widening : %s' % (p6, p7))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PREMISE/G-BOTHREADINGS')

    # ------------------------------------------------------------------ BAR 3, THE CONTROL BAR
    print(chr(10) + '  G-CONTROL / G-PROMINENCE (BAR 3):')
    # ### ### **THIS ARM DOES NOT REQUIRE THE CONTROL TO PASS.** ### It requires the control to have
    # ### been RUN OVER EVERY DECLARER, PRINTED BEFORE ANY OTHER RESULT, and its disagreements
    # ### NAMED. ### An act forbidden to move its threshold to fit its control must be free to
    # ### report that the control did not come clean.
    DECL = E['declare_synthesis'] + E['declare_gathering']
    rows = {r['file']: r for r in RS['rows']}
    c1 = len(DECL) == RS['declarers'] == 9
    c2 = all(f in rows for f in DECL)
    c3 = (RS['agreement_over_seven']
          == sum(1 for f in E['declare_synthesis']
                 if rows[f]['statement_a'] == rows[f]['structural_a']))
    c4 = (RS['agreement_over_all']
          == sum(1 for f in DECL if rows[f]['statement_a'] == rows[f]['structural_a']))
    c5 = len(RS['disagreements']) == len(DECL) - RS['agreement_over_all']
    c6 = all(dd['file'] in rows for dd in RS['disagreements'])
    # ### **PRINTED BEFORE ANY OTHER RESULT**, in the run file and in the bank.
    c7 = (run.index('THE CONTROL, REPORTED BEFORE ANY OTHER RESULT')
          < run.index('THE CORRECTED ROLE DISTRIBUTION'))
    c8 = (bank.index('THE CONTROL IS PRINTED FIRST, BEFORE ANY OTHER RESULT')
          < bank.index('THE COLUMN, BEFORE AND AFTER'))
    c9 = all(f in bank for f in DECL) and all(dd['file'] in bank for dd in RS['disagreements'])
    c10 = RS['threshold_moved'] is False and 'THE THRESHOLD WAS LEFT WHERE IT WAS' in bank
    gc = c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9 and c10
    print('    ### **THE CONTROL RAN OVER ALL %d DECLARERS** : %s / %s' % (len(DECL), c1, c2))
    print('    agreement recomputed here : over the seven %s ; over all nine %s' % (c3, c4))
    print('    ### **AGREEMENT %d OF %d -- AND THIS ARM DOES NOT REQUIRE IT TO BE %d**'
          % (RS['agreement_over_all'], RS['declarers'], RS['declarers']))
    print('    every disagreement is named in the bank : %s ; count consistent : %s' % (c9, c5))
    print('    ### **THE CONTROL IS PRINTED BEFORE ANY OTHER RESULT** : run %s ; bank %s' % (c7, c8))
    print('    ### **THE THRESHOLD WAS NOT MOVED TO FIT THE CONTROL** : %s' % c10)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONTROL/G-PROMINENCE')

    # ----------------------------------------------------------------- BAR 4, THE POLARITY BAR
    print(chr(10) + '  G-POLARITY / G-THREEMARKS (BAR 4):')
    f1, flog = RSTR.self_test(False)
    y1 = f1 is True and RS['fixtures_ok'] is True
    y2 = len(flog) >= 8
    y3 = set(x['want'] for x in flog) >= {'A+', 'A-', 'A?'}
    # ### **A PREDICATE THAT CANNOT RETURN ALL THREE MARKS ON REAL DOCUMENTS IS NOT SCORING.**
    y4 = all(TS.get(k, 0) > 0 for k in ('A+', 'A-', 'A?'))
    # ### **AND THE FIXTURES INCLUDE REJECTIONS, NOT ONLY RECOGNITIONS.**
    y5 = any(x['want'] in ('False', '0') for x in flog)
    y6 = ('SIDE-programme' not in RSTR.kernels_named('the SIDE-programme at large'))
    gy = y1 and y2 and y3 and y4 and y5 and y6
    print('    the shared module`s own fixtures held : %s ; cases %d' % (y1, len(flog)))
    print('    ### **ALL THREE MARKS ARE REACHABLE IN THE FIXTURES** : %s' % y3)
    print('    ### **AND ALL THREE OCCUR IN THE CORPUS** : A+ %d / A- %d / A? %d : %s'
          % (TS.get('A+', 0), TS.get('A-', 0), TS.get('A?', 0), y4))
    print('    the fixtures include rejections : %s ; a prose mention is not a kernel : %s'
          % (y5, y6))
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-POLARITY/G-THREEMARKS')

    # ------------------------------------------------------------- BAR 5, THE NO-OVERWRITE BAR
    print(chr(10) + '  G-NOOVERWRITE / G-BOTHSCORES (BAR 5):')
    v1 = RS['prior_scores_overwritten'] == 0
    v2 = all(('statement_a' in r and 'structural_a' in r) for r in RS['rows'])
    v3 = all(r['statement_a'] in ('A+', 'A-', 'A?') for r in RS['rows'])
    v4 = len(RS['rows']) == POP
    # ### **THE PRIOR COLUMN MUST BE RE-DERIVABLE FROM THE ROWS THEMSELVES**, not only asserted.
    recomputed = collections.Counter(r['statement_a'] for r in RS['rows'])
    v5 = dict(recomputed) == TA
    recomp2 = collections.Counter(r['structural_a'] for r in RS['rows'])
    v6 = dict(recomp2) == TS
    v7 = RS['moved_into_nd'] == sum(1 for r in RS['rows']
                                    if r['statement_a'] != 'A?' and r['structural_a'] == 'A?')
    v8 = RS['moved_out_of_nd'] == sum(1 for r in RS['rows']
                                      if r['statement_a'] == 'A?' and r['structural_a'] != 'A?')
    gv = v1 and v2 and v3 and v4 and v5 and v6 and v7 and v8
    print('    ### **PRIOR SCORES OVERWRITTEN : %d** -- the order`s own word'
          % RS['prior_scores_overwritten'])
    print('    every row carries BOTH scores : %s ; rows == population : %s' % (v2, v4))
    print('    ### **BOTH TALLIES RECOMPUTE FROM THE ROWS** : statement %s ; structural %s'
          % (v5, v6))
    print('    out of NOT DETERMINABLE %d recomputes %s ; into it %d recomputes %s'
          % (RS['moved_out_of_nd'], v8, RS['moved_into_nd'], v7))
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-NOOVERWRITE/G-BOTHSCORES')

    # ------------------------------------------------------------- BAR 6, THE SIDE-BY-SIDE BAR
    print(chr(10) + '  G-SIDEBYSIDE (BAR 6):')
    PQ, SQ = RS['quadrants_statement'], RS['quadrants_structural']
    CELLS = sorted(set(list(PQ.keys()) + list(SQ.keys())))
    x1 = all(c in bank for c in CELLS)
    x2 = 'STATEMENT-A' in bank and 'STRUCTURAL-A' in bank
    x3 = sum(PQ.values()) == sum(SQ.values()) == POP
    x4 = SQ.get('A+B+', 0) == RS['both_axes_structural']
    x5 = PQ.get('A+B+', 0) == RS['both_axes_statement']
    x6 = 'BOTH VERSIONS SIDE BY SIDE' in gate_text.flat(bank)
    gx = x1 and x2 and x3 and x4 and x5 and x6
    print('    every quadrant cell named in the bank : %s (%d cells)' % (x1, len(CELLS)))
    print('    ### **BOTH COLUMNS HEADED AND PRINTED TOGETHER** : %s / %s' % (x2, x6))
    print('    both partitions sum to the population : %s ; quadrant figures agree : %s / %s'
          % (x3, x5, x4))
    print('    %s' % ('PASS' if gx else '### FAIL ###'))
    if not gx:
        fails.append('G-SIDEBYSIDE')

    # ---------------------------------------------------------------- BAR 7, THE DEAFNESS BAR
    print(chr(10) + '  G-DEAF / G-REACH / G-VERDICT (BAR 7):')
    DEAFNESSES = [
        ('a document that synthesises without citing', 'SYNTHESISES WITHOUT CITING'),
        ('a document that cites widely and synthesises nothing',
         'CITES WIDELY AND SYNTHESISES NOTHING'),
        ('the directory stands in for the subject', 'THE DIRECTORY STANDS IN FOR THE SUBJECT'),
        ('a citation it does not recognise', 'A CITATION IT DOES NOT RECOGNISE'),
    ]
    missing = [lbl for lbl, needle in DEAFNESSES if needle not in bank]
    z1 = not missing
    # ### **AND EACH IS DECLARED IN THE MODULE ITSELF AND NOT ONLY IN THE BANK.**
    modsrc = io.open(t('role_structure.py'), encoding='utf-8').read()
    z2 = all(needle in modsrc.upper() for _l, needle in DEAFNESSES)
    z3 = VD['branch'] in bank and VD['class_ruled'] is False
    z4 = 'REACH IS NOT ARGUMENT' in bank
    z5 = 'UPPER BOUND ON SYNTHESIS' in bank and 'UNVALIDATED' in bank
    z6 = 'WHICH POPULATIONS THE STRUCTURAL READ DOES READ' in bank
    z7 = 'WHICH POPULATION IT DOES NOT READ' in bank
    z8 = 'NO CLASS IS RULED IN THIS BRANCH OR IN EITHER OF THE OTHER TWO' in bank
    gz = z1 and z2 and z3 and z4 and z5 and z6 and z7 and z8
    print('    deafnesses missing from the bank : %s' % (missing or 'none'))
    print('    ### **EACH IS DECLARED IN THE MODULE ITSELF** : %s' % z2)
    print('    the verdict is printed and no class is ruled : %s ; reach is not argument : %s'
          % (z3, z4))
    print('    ### **WHICH POPULATIONS IT READS AND WHICH IT CANNOT, BOTH NAMED** : %s / %s'
          % (z6, z7))
    print('    upper bound stated and the other column called unvalidated : %s' % z5)
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-DEAF/G-REACH/G-VERDICT')

    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b380' not in x and x != 'tools/banked_index.py'
                     and x != 'tools/role_structure.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    # ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB.** ### The point of principle, measured.
    w2 = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'REGISTRY.md').strip()
    # ### **AND NOT ONE CORPUS DOCUMENT WAS WRITTEN INTO AT ALL** -- OPEN_TRAILS is a LEDGER and the
    # ### only file this act may append to in `PLACE-papers`.
    ppch = [x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip()]
    w3 = ppch == ['OPEN_TRAILS.md'] or not ppch
    frozen = [x for x in ppch if x.startswith('outputs/') or x.startswith('archive/')]
    w4 = not frozen
    # ### **AND NOTHING ON THE DOWNLOAD LAYER MOVED**, measured and not asserted.
    dl = os.path.join('D:', os.sep, 'MY-DOwnloads')
    book = sorted(x for x in (os.listdir(dl) if os.path.isdir(dl) else [])
                  if 'TOOL_MAP_OUT' in x.upper())
    w5 = len(book) == _J['E'].get('download_versions', len(book))
    gw = w1 and w2 and w3 and w4 and w5
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB** : %s' % w2)
    print('    ### **THE ONLY PLACE-papers PATH TOUCHED IS THE LEDGER** : %s %s' % (w3, ppch))
    print('    archive and outputs untouched : %s ; download layer unmoved : %s (%d files)'
          % (w4, w5, len(book)))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY')

    # ------------------------------------------------------- BAR 8, THE NO-RULING BAR / G-OPEN
    print(chr(10) + '  G-NORULING / G-NOPREFER / G-NOMOVE / G-EVIDENCEFILE / G-OPEN / G-NONEWDOC '
          '(BAR 8):')
    o_start = bank.find('### COMPONENT 4 -- THE VERDICT ON THE METHOD')
    o_end = bank.find('### THE RULING`S EVIDENCE, CONSOLIDATED INTO ONE FILE.')
    region = bank[o_start:o_end] if (o_start >= 0 and o_end > o_start) else ''
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append(m.group(0))
    print('    ### raw preference-word hits in the verdict region : %s' % (sorted(set(raw)) or 'none'))
    n1 = not live and bool(region)
    n2 = Q['lists_closed'] == 0 and Q['closed'] == 0
    n3 = VD['class_ruled'] is False
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    deskrun = io.open(IDX, encoding='utf-8', errors='replace').read()
    n4 = all(x in deskrun for x in lists)
    n5 = 'ARE RESTATED `OPEN` BY NAME' in bank
    n6 = 'open by name' in gate_text.flat(tblk).lower()
    # ### **NO DECLARATION MOVED:** ### every declarer's OWN claim is unchanged in the corpus, and
    # ### the act's own table reports the document's claim beside its reading, never in place of it.
    n7 = all(rows[f]['statement_a'] in ('A+', 'A-') for f in DECL)
    # ### **THE EVIDENCE FILE EXISTS, IS IN THE RELAY BANK, AND IS NOT A CORPUS DOCUMENT.**
    n8 = os.path.exists(EVID) and os.path.dirname(os.path.abspath(EVID)) == os.path.abspath(D)
    ev = io.open(EVID, encoding='utf-8', errors='replace').read()
    n9 = '%s' not in ev and '%d' not in ev and len(ev.splitlines()) > 40
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    n10 = not newdocs
    gn = n1 and n2 and n3 and n4 and n5 and n6 and n7 and n8 and n9 and n10
    print('    live preference words in the verdict : %d ; lists closed : %d ; desk closed : %d'
          % (len(live), Q['lists_closed'], Q['closed']))
    print('    ### **NO CLASS RULED IN ANY BRANCH** : %s' % n3)
    print('    the four lists named in the desk run and restated OPEN : %s / %s ; in the trail : %s'
          % (n4, n5, n6))
    print('    ### **NO DECLARATION MOVED -- EVERY DECLARER KEEPS ITS OWN CLAIM** : %s' % n7)
    print('    ### **THE EVIDENCE FILE IS A RELAY BANK ARTIFACT** : %s ; complete : %s' % (n8, n9))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (n10, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-NOPREFER/G-NOMOVE/G-EVIDENCEFILE/G-OPEN/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE ROLE AXIS READ FROM STRUCTURE' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-role-axis-read-from-structure returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the declarations are moved',
              'the lists are closed', 'the registry is edited'))
    gt = t1 and t2 and t3 and t4 and t5
    print('    trail: mark once and append-only : %s ; blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
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
    relied = (RS, VD, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND THE THREE PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    R375 = d('b379_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b378_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b378`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b379`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b380_hooks.txt'), d('b380_mirror.txt')
    gh2 = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh2:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        gh2 = h_ok and m_ok
        print('    hook: 0 failing : %s ; mirror clean : %s' % (h_ok, m_ok))
    else:
        print('    ### the hook/mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh2:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    # --------------------------------------------------------------------------------- G-NUMBERS
    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('face-subject gates %d' % LG['face_subject_gates'],
         str(LG['face_subject_gates']) in bank),
        ('the population %d' % POP, str(POP) in bank),
        ('NOT DETERMINABLE strict %d' % TA.get('A?', 0), str(TA.get('A?', 0)) in bank),
        ('NOT DETERMINABLE broad %d' % TB.get('A?', 0), str(TB.get('A?', 0)) in bank),
        ('structural A+ %d' % TS.get('A+', 0), str(TS.get('A+', 0)) in bank),
        ('structural A- %d' % TS.get('A-', 0), str(TS.get('A-', 0)) in bank),
        ('structural A? %d' % TS.get('A?', 0), str(TS.get('A?', 0)) in bank),
        ('moved out of NOT DETERMINABLE %d' % RS['moved_out_of_nd'],
         str(RS['moved_out_of_nd']) in bank),
        ('moved into NOT DETERMINABLE %d' % RS['moved_into_nd'],
         str(RS['moved_into_nd']) in bank),
        ('declarers %d' % RS['declarers'], str(RS['declarers']) in bank),
        ('agreement over the seven %d' % RS['agreement_over_seven'],
         str(RS['agreement_over_seven']) in bank),
        ('agreement over all %d' % RS['agreement_over_all'],
         str(RS['agreement_over_all']) in bank),
        ('the both-axes quadrant %d' % RS['both_axes_structural'],
         str(RS['both_axes_structural']) in bank),
        ('prior scores overwritten %d' % RS['prior_scores_overwritten'],
         str(RS['prior_scores_overwritten']) in bank),
        ('the branch %s' % VD['branch'], VD['branch'] in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on rescore run', RS['run_file'] in bank),
        ('the relied-on verdict run', VD['run_file'] in bank),
        ('the relied-on desk run', Q['run_file'] in bank),
        ('the relied-on extract run', E['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('rescore', RS),
                    ('verdict', VD), ('desk', Q)):
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
                          if x.startswith('b380_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid',
              'curve_fit', 'minimize')
    raw2 = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    CALL = {b: __import__('re').compile(r'\b' + b + r'\s*\(') for b in banned}
    hits2 = [(x, b) for x in mymods for b in banned if CALL[b].search(strip_prose(t(x)))]
    print('    ### raw substring hits (a substring is not a call) : %s' % (raw2 or 'none'))
    for _x, _b in [r for r in raw2 if r not in hits2]:
        print('        ### DISCHARGED in %s : `%s` occurs only inside a longer identifier'
              % (_x, _b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits2 and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits2), hits2 or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-NOLEAN:')
    lean = [x for x in git(os.path.join('D:', os.sep, 'SIDE-effects'),
                           'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip()]
    gnl = not lean
    print('    .lean or kernel files changed : %s  %s'
          % (lean or 'none', 'PASS' if gnl else '### FAIL ###'))
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
    DECLARED = {'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'the cell index is a COLUMN of a row located by its own shape.',
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

    print(chr(10) + '  G-NOEDIT ### BEFORE THE PUSH:')
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/b374_hedge.py', 'tools/b375_population.py', 'tools/git-hooks/pre-push']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b380' not in x and x.strip() != 'tools/banked_index.py']
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, EVID, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b380_satisfiable.json')] + [t(x) for x in mymods] + [t('role_structure.py')]
    CARRIERS = [
        (t('b380_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(RS['run_file']), "the rescore run carries the documents' own names and sentences"),
        (d(VD['run_file']), "the verdict run carries the rubric's own words"),
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
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in
                [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                 ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                 ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [],
                                     stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or live_bad or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE ROLE AXIS, SCORED STRUCTURALLY (b380).'
    nxt = '# ### THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS (b379).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b380_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT NINE NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods) + ['tools/role_structure.py']
    gcap = len(made) <= 9 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b380_hedge_')
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
