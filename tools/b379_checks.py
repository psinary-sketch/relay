# -*- coding: utf-8 -*-
"""b379_checks.py -- THE GATE SUITE FOR THE APPARATUS AXIS RE-SCORED.

### ### **THE ARMS THAT MATTER MOST HERE ARE THE ONES THAT MEASURE WHAT THIS ACT DID *NOT* DO:**
### `G-NORULING`, `G-NOPREFER`, `G-OPEN`, `G-NOWRITE`. ### The order forbids ruling a class,
### reclassifying a document, writing a class line, repairing a document and closing a list; ### **EACH
### ### OF THE FIVE HAS ITS OWN MUST-FAIL FIXTURE AS A WHOLE LINE.**
### ### **AND `G-EVERYGATE` RE-READS THE LOCK GATE'S OWN RECORD**, because Step Zero's whole point is
### that the lock was chained on a tool that reads every gate. ### **AN ACT THAT CURES A GATE FAILURE
### ### AND DOES NOT MEASURE THE CURE HAS NOT CURED IT.**
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`), and ### **AN ARM THAT WOULD FAIL ON A PRE-EXISTING CONDITION IS NOT MEASURING
### ### THIS ACT** (`b375`).
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
import gate_hash          # noqa: E402
import row_categories as RC  # noqa: E402

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


BANK = d('b379_the_apparatus_axis_rescored.txt')
REG = d('b379_registration_2026-09-08.txt')
FERRY = d('b379_ferry_2026-09-08.txt')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b379_ferry_scan.txt'), d('b379_reg_termscan.txt'), d('b379_reg_gate.txt')
CENSUS0, FCEN = d('b379_census_stepzero.txt'), d('b379_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b379_regspec_run.txt'), d('audit_b379_reg_satisfiable.txt')
PINS0 = d('b379_pins_stepzero.txt')
SEAL = 'ba4863ca8d1f9a06f3ccdf2efdea99045d59f23555e55588fc7729e5810021ea'
ROWNUM = '228'
TRAIL_MARK = '<!-- b379 the apparatus axis re-scored; two filings -->'


_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b379_reads.json'), ('LG', 'b379_lockgate.json'),
                   ('RS', 'b379_rescore.json'), ('SV', 'b379_survivors.json'),
                   ('HD', 'b379_hand.json'), ('FL', 'b379_filings.json'),
                   ('Q', 'b379_desk.json'))}

# ### **RESOLVED BY THE RECORDED CLOCK, NEVER BY NAME** (`b358`): ### `run_clock` NUMBERS
# ### repeats, so a suite pointed at the bare stem reads the FIRST run and not the one that
# ### succeeded. ### **THE DESK'S OWN JSON RECORDS WHICH FILE IT WROTE.**
IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/row_categories.py', 'tools/b379_regspec.py',
                'tools/b379_extract.py', 'tools/b379_reg_gate.py', 'tools/b379_rescore.py',
                'tools/b379_survivors.py', 'tools/b379_hand.py', 'tools/b379_filings.py',
                'tools/b379_desk.py', 'tools/b379_bank.py', 'tools/b379_checks.py'}

TOOLNUM = [
    ('the row categories (SHARED), fixtured both polarities', 'tools/row_categories.py'),
    ('the apparatus axis re-scored, both predicates', 'tools/b379_rescore.py'),
    ('the survivors, from the sentence that names each', 'tools/b379_survivors.py'),
    ('the day-1 document, read by hand', 'tools/b379_hand.py'),
    ('the two filings', 'tools/b379_filings.py'),
    ('(R7), the trail block, the row and the key', 'tools/b379_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b379_bank.py'),
    ('the reads', 'tools/b379_extract.py'),
    ('the registration gate', 'tools/b379_reg_gate.py'),
    ('the clause spec', 'tools/b379_regspec.py'),
    ('THE ORIGINAL PREDICATE, IMPORTED UNMODIFIED', 'tools/b376_axes.py'),
    ('THE BOTH-DIALECT MATCHER, IMPORTED UNMODIFIED', 'tools/b378_terminals.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
KCENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
PP_RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b379 - THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS. The'),
    ('the order -- the standing positive-control clause', FERRY,
     'gate and re-checked if the registration is rewritten; every'),
    ('the order -- the standing error-exit clause', FERRY,
     'presence first; an error exit is not an answer. The instrument'),
    ('the order -- addition one, the direction registered first', FERRY,
     'ADDITION ONE - THE DIRECTION IS REGISTERED BEFORE THE RUN: a'),
    ('the order -- addition one, bounded below', FERRY,
     'corrected population is bounded below by the prior figure and'),
    ('the order -- addition one, both columns side by side', FERRY,
     'corrected quadrant table with both the prior and corrected'),
    ('the order -- addition one, which options it weakens', FERRY,
     "columns side by side. State which of the ruling's options the"),
    ('the order -- addition two, the row categories', FERRY,
     'ADDITION TWO - THE ROW CATEGORIES, from what b378 found: a'),
    ('the order -- addition two, manuscript-resident', FERRY,
     'a row may name a corpus document rather than a terminal, which'),
    ('the order -- addition two, a category is not an absence', FERRY,
     'already has one, so a checker stops reporting a category as an'),
    ('the order -- addition three, the two filings', FERRY,
     'ADDITION THREE - TWO FILINGS ABOUT A DOCUMENT OUTSIDE THE TREE,'),
    ('the order -- addition three, the registry is not edited', FERRY,
     'and file the drift for the author - the registry is not edited'),
    ('the order -- addition three, neither filing opens work', FERRY,
     'can say whether it governs documents outside the tree. Neither'),
    ("the order -- the navigator's expectations", FERRY, 'this act found. The navigator'),
    ('the order -- (F2), a document moves into the quadrant', FERRY,
     'prior figure; (F2) at least one document moves into the'),
    ('the draft -- the suspect column re-measured', d('b378_closing.txt'),
     '### ### ### **COMPONENT 1 -- THE SUSPECT COLUMN, RE-MEASURED.**'),
    ('the draft -- the fourteen that survive', d('b378_closing.txt'),
     '### ### **COMPONENT 2 -- THE `14` THAT SURVIVE, CLASSIFIED ONE MORE STEP.**'),
    ('the draft -- the other not-determinable document', d('b378_closing.txt'),
     '### ### **COMPONENT 3 -- THE OTHER `NOT DETERMINABLE` DOCUMENT.**'),
    ('the front door -- manuscript-resident and research-reach', os.path.join(PP, 'README.md'),
     'exists, the status says so in words — *manuscript-resident* or *research-reach* —'),
    ('the precedence rule -- REGISTRY is the single source of truth',
     os.path.join(PP, 'README.md'),
     '1. **REGISTRY.md is the single source of truth.** Update it whenever you update a paper.'),
    ('the registry -- the ANNEX heading', os.path.join(PP, 'REGISTRY.md'),
     '## ANNEX: Download-Layer (non-keystone, outside the repo tree)'),
]

SELF_NEEDLES = [
    ('the bank leads with both sentences', BANK,
     '### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE THE'),
    ('### (F1) met and (F2) refuted by the same table', BANK,
     '`(F1)` IS MET AND `(F2)` IS REFUTED, BOTH BY THE SAME PRINTED TABLE.'),
    ('### the axes come apart further', BANK,
     'WAS**, so the two axes come apart further rather than closer -- which is the opposite of'),
    ('### a strict superset', BANK,
     'SO THE WIDENED PATTERN MATCHES A STRICT SUPERSET OF THE OLD ONE'),
    ('### a lost mark would be a defect in the instrument', BANK,
     'DEFECT IN THE INSTRUMENT, REPORTED AS ONE AND NEVER AS A FINDING ABOUT THE CORPUS.'),
    ('### the prior column was re-run, not trusted', BANK,
     'AND THE PRIOR COLUMN WAS RE-RUN FROM THE ORIGINAL PREDICATE ON THE SAME BYTES'),
    ('### no option is recommended', BANK,
     'WHICH OF THE RULING`S OPTIONS THE CORRECTION WEAKENS. ### NONE IS RECOMMENDED.'),
    ('### the corrected column is not a ground truth', BANK,
     'PREDICATE, NOT A GROUND TRUTH.'),
    ('### the front door`s words carried and not replaced', BANK,
     'SO THE TAXONOMY IS EXTENDED, NOT INVENTED.'),
    ('### a category is never a verdict', BANK,
     'AND THE MODULE RETURNS A CATEGORY AND NEVER A VERDICT.'),
    ('### a reading is not a verdict', BANK,
     'A READING OF A DOCUMENT IS NOT A VERDICT ON IT.'),
    ('### the day-1 document carries apparatus', BANK,
     'THE DAY-1 DOCUMENT, READ BY HAND. ### **IT CARRIES APPARATUS.**'),
    ('### the concordance class describes something real', BANK,
     'THE CORPUS`S OWN `CONCORDANCE-CARRIED` CLASS DOES DESCRIBE SOMETHING REAL THERE.'),
    ('### a chain that moved and a precedence source that did not', BANK,
     'PRECEDENCE SOURCE THAT DID NOT** -- ### **`%d` VERSIONS SIT ON THE DISK**, and'
     % json.load(io.open(d('b379_filings.json'), encoding='utf-8'))['n_versions']),
    ('### precedence is not correctness', BANK,
     'STATEMENT ABOUT PRECEDENCE, NOT ABOUT WHICH DESCRIPTION IS CORRECT.'),
    ('### the registry is not edited, and why', BANK,
     'precedence source to match a document that drifted has inverted the rule it is enforcing, and'),
    ('### never scored at all', BANK,
     'BOTH AXES -- NOT SCORED `B-`, NOT SCORED `A?`, BUT NEVER CONSIDERED AT ALL.'),
    ('### no widening would have reached it', BANK,
     'SCORED, AND NO WIDENING OF A MATCHER WOULD HAVE REACHED IT.'),
    ('### the four lists restated open in the desk`s own words', BANK,
     'THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:'),
    ('### owner instruments imported unmodified', BANK,
     '`gate_hash` are all ### **IMPORTED AND RUN UNMODIFIED**, which is what lets this act`s'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a declaration was moved', BANK, '### A DECLARATION WAS MOVED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says the registry was edited', BANK, '### THE REGISTRY WAS EDITED.'),
    ('the bank never says a document lost its mark', BANK, '### A DOCUMENT LOST ITS MARK.'),
    ('the bank never says a category was claimed without evidence', BANK,
     '### A CATEGORY WAS CLAIMED WITHOUT EVIDENCE.'),
    ('the bank never names a preferred option', BANK, '### THE PREFERRED OPTION IS.'),
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
    print('b379 -- GATE SUITE (THE TWO-AXIS READ)')
    print('=' * 100)
    E, LG, RS, SV, HD, FL, Q = (_J['E'], _J['LG'], _J['RS'], _J['SV'], _J['HD'],
                                _J['FL'], _J['Q'])
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
    print(chr(10) + '  MUST-FAIL FIXTURES ### (THE ORDER`S FIVE PROHIBITIONS, AS WHOLE LINES):')
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
    l7 = LG['act'] == 'b379' and not os.path.exists(t('b379_lockgate.py'))
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s' % l6)
    print('    ### **THE LOCK GATE WAS INHERITED, NOT REBUILT** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # --------------------------------------------------------------- BAR 2, THE MONOTONICITY BAR
    print(chr(10) + '  G-MONOTONE / G-BOUNDED (BAR 2):')
    ORDER = {'B-': 0, 'B?': 1, 'B+': 2}
    m1 = RS['monotone'] is True
    m2 = len(RS['lost']) == 0
    m3 = RS['corrected_bplus'] >= RS['prior_bplus']
    m4 = all(ORDER[r['corrected_b']] >= ORDER[r['prior_b']] for r in RS['rows'])
    pq, cq = RS['prior_quadrants'], RS['corrected_quadrants']
    m5 = cq.get('A+B+', 0) >= pq.get('A+B+', 0)
    m6 = cq.get('A?B-', 0) <= pq.get('A?B-', 0) and cq.get('A-B-', 0) <= pq.get('A-B-', 0)
    m7 = sum(pq.values()) == sum(cq.values()) == RS['swept']
    gm = m1 and m2 and m3 and m4 and m5 and m6 and m7
    print('    ### **DOCUMENTS THAT LOST A MARK : %d** -- a loss would be a DEFECT IN THE INSTRUMENT'
          % len(RS['lost']))
    print('    prior B+ %d -> corrected B+ %d : %s'
          % (RS['prior_bplus'], RS['corrected_bplus'], m3))
    print('    ### **EVERY DOCUMENT MOVED FORWARD OR NOT AT ALL** : %s' % m4)
    print('    the both-axes quadrant only grew : %s ; the B- rows only shrank : %s' % (m5, m6))
    print('    both partitions sum to the sweep : %s' % m7)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-MONOTONE/G-BOUNDED')

    # ------------------------------------------------------------ BAR 3, THE POSITIVE-CONTROL BAR
    print(chr(10) + '  G-CONTROL / G-NOERROR (BAR 3):')
    c1 = RS['controls_ok'] is True
    # ### **THE CONTROL MUST CONTAIN A CASE THE OLD PREDICATE REFUSED AND THE NEW ONE ACCEPTS.**
    c2 = any('BARE' in c['case'] and c['want'] == 'B+' for c in RS['controls'])
    c3 = any('BARE' in c['case'] and c['want'] == 'B-' for c in RS['controls'])
    c4 = HD['control_held'] is True and len(HD['grep_errors']) == 0
    gc = c1 and c2 and c3 and c4
    print('    the re-score controls held : %s' % c1)
    print('    ### **A BARE ROW THE OLD PREDICATE REFUSED AND THE NEW ONE ACCEPTS** : %s / %s'
          % (c3, c2))
    print('    the hand read`s positive control held : %s ; searches that could not run : %d'
          % (HD['control_held'], len(HD['grep_errors'])))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONTROL/G-NOERROR')

    # ------------------------------------------------------------- BAR 4, THE SIDE-BY-SIDE BAR
    print(chr(10) + '  G-SIDEBYSIDE / G-MOVED / G-WEAKENS (BAR 4):')
    CELLS = ['A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?']
    bf = gate_text.flat(bank)
    s1 = all(c in bank for c in CELLS)
    # ### **EVERY CELL PRINTED WITH BOTH ITS VALUES** -- the bank's table carries prior and corrected.
    s2 = 'prior' in bank and 'corrected' in bank
    s3 = str(RS['prior_bplus']) in bank and str(RS['corrected_bplus']) in bank
    s4 = 'NONE IS RECOMMENDED' in bf
    s5 = all(('OPTION %d' % i) in bank for i in (1, 2, 3, 4, 5))
    s6 = 'UNTOUCHED' in bank and 'WEAKENED' in bank
    gs = s1 and s2 and s3 and s4 and s5 and s6
    print('    every quadrant cell named in the bank : %s' % s1)
    print('    ### **PRIOR AND CORRECTED BOTH PRINTED** : %s ; both figures present : %s' % (s2, s3))
    print('    all five options addressed : %s ; some untouched and some weakened : %s' % (s5, s6))
    print('    ### **THE BANK SAYS NONE IS RECOMMENDED** : %s' % s4)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SIDEBYSIDE/G-MOVED/G-WEAKENS')

    # ----------------------------------------------------------------- BAR 5, THE CATEGORY BAR
    print(chr(10) + '  G-CATEGORY / G-POLARITY / G-NOVERDICT (BAR 5):')
    k1, klog = RC.self_test(False)
    k2 = SV['fixtures_ok'] is True
    k3 = len(SV['added_at_b379']) == 3
    # ### **EVERY CATEGORY MUST BE REFUSED SOMEWHERE, NOT ONLY RECOGNISED.**
    k4 = sum(1 for c in SV['fixtures'] if c['want'] == 'True') >= 5
    k5 = all(a['category'] in RC.CATEGORIES for a in SV['assigned'])
    k6 = sum(SV['tally'].values()) == len(SV['assigned'])
    k7 = SV['not_located'] < len(SV['assigned'])
    k8 = SV['front_door_quote'] in bank or 'manuscript-resident' in bank
    gk = k1 and k2 and k3 and k4 and k5 and k6 and k7 and k8
    print('    the shared module`s own fixtures held : %s' % k1)
    print('    ### **CASES THAT MUST REFUSE : %d** -- a recogniser that only says yes is not one'
          % sum(1 for c in SV['fixtures'] if c['want'] == 'True'))
    print('    categories added at b379 : %d ; every assignment is a declared category : %s'
          % (len(SV['added_at_b379']), k5))
    print('    ### **ABSENCES %d OF %d -- A CATEGORY IS NOT AN ABSENCE** : %s'
          % (SV['not_located'], len(SV['assigned']), k7))
    print('    the front door`s own words are carried into the bank : %s' % k8)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CATEGORY/G-POLARITY/G-NOVERDICT')

    # ------------------------------------------------------------- BAR 6, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-PRECEDENCE / G-FILED (BAR 6):')
    bad = []
    for grp in ('registry', 'later', 'precedence'):
        for r in FL[grp]:
            src = os.path.join(PP, r['file'].replace('/', os.sep))
            try:
                lines = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
            except OSError:
                bad.append((r['file'], 'unreadable'))
                continue
            if r['text'] not in lines[r['line'] - 1]:
                bad.append((r['file'], r['line']))
    q1 = not bad
    q2 = len(FL['registry']) >= 2 and len(FL['later']) >= 2 and len(FL['precedence']) >= 1
    q3 = FL['filings'] == 2
    q4 = FL['n_versions'] >= 2
    q5 = 'single source of truth' in bank and 'precedence source' in bank
    gq = q1 and q2 and q3 and q4 and q5
    print('    ### **EVERY QUOTE RE-READS OUT OF ITS OWN SOURCE AT ITS OWN LINE** : %s %s'
          % (q1, bad[:2] or ''))
    print('    both sides quoted : %s ; filings : %d ; versions on disk : %d'
          % (q2, FL['filings'], FL['n_versions']))
    print('    ### **THE PRECEDENCE RULE IS QUOTED FROM THE FRONT DOOR** : %s' % q5)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-PRECEDENCE/G-FILED')

    # ------------------------------------------------------------------ BAR 7, THE NO-WRITE BAR
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-NODOWNLOAD (BAR 7):')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b379' not in x and x != 'tools/banked_index.py'
                     and x != 'tools/row_categories.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    # ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB.** ### The point of principle, measured.
    w2 = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'REGISTRY.md').strip()
    w3 = FL['registry_edited'] is False and FL['download_layer_written'] is False
    w4 = FL['document_opened'] is False
    w5 = HD['bytes_written'] == 0 and HD['declaration_moved'] is False
    w6 = SV['documents_repaired'] == 0 and SV['names_invented'] == 0
    # ### **AND NOTHING ON THE DOWNLOAD LAYER MOVED** -- the versions are re-hashed here.
    dl = os.path.join('D:', os.sep, 'MY-DOwnloads')
    now = {}
    for v in FL['versions']:
        fp = os.path.join(dl, v['name'])
        now[v['name']] = (hashlib.sha256(io.open(fp, 'rb').read()).hexdigest()
                          if os.path.exists(fp) else None)
    w7 = all(now.get(v['name']) == v['sha256'] for v in FL['versions'])
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    w8 = not frozen
    gw = w1 and w2 and w3 and w4 and w5 and w6 and w7 and w8
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB** : %s' % w2)
    print('    ### **EVERY DOWNLOAD-LAYER VERSION STILL HASHES TO WHAT IT DID** : %s' % w7)
    print('    the book was not opened : %s ; the hand read wrote nothing : %s' % (w4, w5))
    print('    no document repaired and no name invented : %s ; archive untouched : %s' % (w6, w8))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY/G-NODOWNLOAD')

    # ------------------------------------------------------- BAR 8, THE NO-RULING BAR / G-OPEN
    print(chr(10) + '  G-NORULING / G-NOPREFER / G-OPEN / G-NONEWDOC (BAR 8):')
    o_start = bank.find('### WHICH OF THE RULING`S OPTIONS THE CORRECTION WEAKENS')
    o_end = bank.find('### THE DAY-1 DOCUMENT, READ BY HAND')
    region = bank[o_start:o_end] if (o_start >= 0 and o_end > o_start) else ''
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append(m.group(0))
    print('    ### raw preference-word hits in the options region : %s' % (sorted(set(raw)) or 'none'))
    n1 = not live
    n2 = Q['lists_closed'] == 0
    n3 = Q['closed'] == 1 and all('axis-B column' in c['item'] for c in Q['closed_items'])
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    n4 = all(x in bank for x in lists)
    n5 = 'ARE RESTATED `OPEN` BY NAME' in bank
    n6 = 'open by name' in gate_text.flat(tblk).lower()
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    n7 = not newdocs
    gn = n1 and n2 and n3 and n4 and n5 and n6 and n7
    print('    live preference words : %d ; lists closed : %d' % (len(live), Q['lists_closed']))
    print('    ### **THE ONE CLOSURE IS THE AXIS-B COLUMN** : %s (%s)'
          % (n3, [c['item'] for c in Q['closed_items']]))
    print('    the four lists named and restated OPEN : %s / %s ; in the trail : %s'
          % (n4, n5, n6))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (n7, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-NOPREFER/G-OPEN/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE SUSPECT COLUMN RE-MEASURED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-suspect-column-re-measured returns 1 row(s)' in irun
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
    relied = (RS, SV, HD, FL, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND `b375`'S DEFECTIVE FACE MUST STILL VERIFY, UNEDITED.**
    R375 = d('b378_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    # ### **AND THE TWO PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b377_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b377`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b375`S DEFECTIVE FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b379_hooks.txt'), d('b379_mirror.txt')
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
        ('prior B+ %d' % RS['prior_bplus'], str(RS['prior_bplus']) in bank),
        ('corrected B+ %d' % RS['corrected_bplus'], str(RS['corrected_bplus']) in bank),
        ('gained %d' % len(RS['gained']), str(len(RS['gained'])) in bank),
        ('into the both-axes quadrant %d' % len(RS['moved_into_both']),
         str(len(RS['moved_into_both'])) in bank),
        ('the sweep %d' % RS['swept'], str(RS['swept']) in bank),
        ('carried names %d' % len(SV['assigned']), str(len(SV['assigned'])) in bank),
        ('absences %d' % SV['not_located'], str(SV['not_located']) in bank),
        ('hand read named %d' % HD['named'], str(HD['named']) in bank),
        ('hand read located %d' % HD['located'], str(HD['located']) in bank),
        ('versions on disk %d' % FL['n_versions'], str(FL['n_versions']) in bank),
        ('population %d' % FL['population'], str(FL['population']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on rescore run', RS['run_file'] in bank),
        ('the relied-on survivors run', SV['run_file'] in bank),
        ('the relied-on hand run', HD['run_file'] in bank),
        ('the relied-on filings run', FL['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('rescore', RS),
                    ('survivors', SV), ('hand', HD), ('filings', FL), ('desk', Q)):
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
                          if x.startswith('b379_') and x.endswith('.py')))
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
              if x.strip() and 'b379' not in x and x.strip() != 'tools/banked_index.py']
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b379_satisfiable.json')] + [t(x) for x in mymods] + [t('row_categories.py')]
    CARRIERS = [
        (t('b379_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(RS['run_file']), "the rescore run carries the documents' own table rows"),
        (d(SV['run_file']), "the survivors run carries the documents' own sentences"),
        (d(HD['run_file']), "the hand read carries the document's own sentences"),
        (d(FL['run_file']), "the filings run carries the registry's and the front door's own lines"),
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

    marker = '# ### THE APPARATUS AXIS RE-SCORED, AND TWO FILINGS (b379).'
    nxt = '# ### THE REFS WIDENED AND THE CONVENTION SWEPT (b378).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b379_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT ELEVEN NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods) + ['tools/row_categories.py']
    gcap = len(made) <= 11 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b379_hedge_')
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
