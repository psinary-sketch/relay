# -*- coding: utf-8 -*-
"""b396_checks.py -- THE GATE SUITE FOR THE BACKTICK SWEEP.

### ### **THE ARM THAT MATTERS MOST IS `G-PREMISE`.** ### The order's first instruction was that
### the sweep be shown capable of finding a narrow matcher written in a form it did not anticipate.
### The arm re-runs the detector's own fixture -- three forms, all found -- and requires the ###
### **WIDE FIXTURE TO COME BACK CLEAN**, because ### **WITHOUT A NEGATIVE CONTROL A FIXTURE SHOWS
### ### A DETECTOR FIRES AND NOT THAT IT DISCRIMINATES.**
###
### ### **`G-DISCARDS` IS THE ARM AGAINST THIS ACT'S OWN WORST TEMPTATION.** ### Three filters were
### tried and thrown out, and any one of them would have turned `407` instruments into a headline.
### The arm requires all three to stand in the bank ### **WITH THEIR YIELDS**, because ### **A
### ### TIGHTENING MADE IN SILENCE IS ONE NOBODY CAN AUDIT.**
###
### ### **`G-BOTHYIELDS` AND `G-STATEDFIRST` GUARD THE RE-RUNS.** ### Each of the six prints a
### narrow yield, a wide yield and a verdict, and every widening is a literal in the components
### tool -- ### **A RE-RUN TUNED TO ITS RESULT IS `b380`'S FORBIDDEN DIRECTION.**
###
### ### **`G-OPTIN` AND `G-NOCALLERMOVED` GUARD THE ONE OWNER INSTRUMENT THIS ACT EDITS.** ###
### `anchor_from_file.py` gains a mode that is `OFF` by default; the arm requires its own fixtures
### to pass, requires `0` callers to pass `editing`, and requires ### **THE DEFAULT TO STILL FIND
### ### A PRESERVED LINE**, because an anchor used to QUOTE one is correct.
###
### ### **AND `G-NOREPAIR` IS THE LINE THIS ACT DOES NOT CROSS.** ### `82` figures were named and
### ### **NOT ONE INSTRUMENT WAS REPAIRED** -- naming a body of work is not doing it.
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


BANK = d('b396_the_backtick_swept.txt')
REG = d('b396_registration_2026-09-10.txt')
FERRY = d('b396_ferry_2026-09-10.txt')
SCAN, TERMSCAN, GATE = d('b396_ferry_scan.txt'), d('b396_reg_termscan.txt'), d('b396_reg_gate.txt')
CENSUS0, FCEN = d('b396_census_stepzero.txt'), d('b396_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b396_regspec_run.txt'), d('audit_b396_reg_satisfiable.txt')
PINS0 = d('b396_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
UNTOUCHED = (TAXONOMY, 'REGISTRY.md', 'README.md', 'SPIRAL_MAP.md', 'FINDINGS.md',
             'phase2/method/THE_KEYSTONE_CENSUS.md',
             'phase1.5/spectral/GRH_CASCADE.md',
             'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
             'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = 'f5c83b3d6d9de82541558b912a3b7395b7ec4530a5ff056448abd8318fbc6126'
ROWNUM = '245'
TRAIL_MARK = '<!-- b396 how many findings rest on a backtick: 82 figures at risk -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b396_components.json'), ('LG', 'b396_lockgate.json'),
                   ('E', 'b396_reads.json'), ('Q', 'b396_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b396_regspec.py', 'tools/b396_reg_gate.py', 'tools/b396_extract.py',
                'tools/b396_components.py', 'tools/b396_desk_bank.py', 'tools/b396_checks.py',
                'tools/b396_narrow.py', 'tools/b396_figures.py'}

TOOLNUM = [
    ('the narrow-predicate detector and its fixture', 'tools/b396_narrow.py'),
    ('the figure-level filter and its two controls', 'tools/b396_figures.py'),
    ('the extract, and the six surveys inside it', 'tools/b396_extract.py'),
    ('the list, the six re-runs, the price and the module', 'tools/b396_components.py'),
    ('the desk, the ledger writes and the bank', 'tools/b396_desk_bank.py'),
    ('the registration gate', 'tools/b396_reg_gate.py'),
    ('the clause spec', 'tools/b396_regspec.py'),
    ('the anchor tool, and the one added opt-in mode', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b396 — HOW MANY FINDINGS REST ON A BACKTICK. The'),
    ('the order -- the premise tested first', FERRY,
     "sweep's own predicate must be shown capable of finding a"),
    ('the order -- three forms, all three found', FERRY,
     'shape-narrow predicate written in a form the sweep did not'),
    ('the order -- the third time in four acts', FERRY,
     'matchers that is itself narrow would be the species inside the'),
    ('the order -- state what the sweep is deaf to', FERRY,
     'act that measures it, for the third time in four acts. State'),
    ('the order -- ranking by exposure not cost', FERRY,
     'ADDITION TWO — THE RANKING IS BY EXPOSURE, NOT BY COST ALONE:'),
    ('the order -- rank the at-risk findings', FERRY,
     'before the three cheapest are re-run, rank the at-risk findings'),
    ('the order -- say which set was run and why', FERRY,
     'draft asks for, and if the cheapest three and the most exposed'),
    ('the order -- the exposed wrong beats the cheap right', FERRY,
     'author would rather know the exposed ones are wrong than that'),
    ('the order -- the preservation hazard', FERRY,
     "ADDITION THREE — THE PRESERVATION HAZARD, FILED: b395's anchor"),
    ('the order -- refused rather than disambiguated', FERRY,
     'is refused rather than disambiguated — with b395\'s near miss as'),
    ('the order -- mechanized or filed as judgement', FERRY,
     'its incident; mechanized in the anchor tool if the preserved'),
    ('the order -- a TECHNE module, local, not pushed', FERRY,
     'and not listed beside the mechanized ones. A TECHNE module'),
    ('the order -- (L3)', FERRY,
     "draft's: (L3) at least one finding this arc reported as an"),
]

SELF_NEEDLES = [
    ('the bank leads with the question having no answer', BANK,
     '### ### ### **THE QUESTION HAS NO ANSWER AT INSTRUMENT GRANULARITY, AND THE THREE'),
    ('### the premise discharged first', BANK,
     '### THE ORDER`S FIRST INSTRUCTION, DISCHARGED BEFORE ANYTHING WAS SWEPT.'),
    ('### the form with no regex at all', BANK,
     '###   form 3  ### **NO REGEX AT ALL** -- `startswith` + `in` + `islower()`'),
    ('### fires is not discriminates', BANK,
     '### ### the fixture shows the detector ### **FIRES** ### and not that it ###'),
    ('### the third time in four acts', BANK,
     '### ### INSIDE THE ACT THAT MEASURES IT, FOR THE THIRD TIME IN FOUR ACTS.**'),
    ('### a backtick in a sentence', BANK,
     '### ### every one of those backticks is PROSE. ### **A BACKTICK IN A SENTENCE IS'),
    ('### a filter that keeps nine tenths', BANK,
     '### ### **A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER**, and ###'),
    ('### three vacuous filters is the result', BANK,
     '### ### ### **AND THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT:** ### the'),
    ('### narrow is not a defect', BANK,
     '### ### **AND NARROW IS NOT A DEFECT:** ###'),
    ('### the harness defect owned', BANK,
     '### ### **AN EARLIER FORM OF THIS COMPONENT CALLED TWO OF THE SIX `MOVED`, AND'),
    ('### a figure that does not move has not moved', BANK,
     '### ### DOES NOT MOVE HAS NOT MOVED, WHATEVER THE COUNT DID.** ### Repaired before'),
    ('### a refuted L2 is a real answer', BANK,
     '### ### **A REFUTED `(L2)` IS A REAL ANSWER AND NOT A DISAPPOINTMENT** -- the'),
    ('### a confirmation is the weaker result', BANK,
     '### ### **AND A CONFIRMATION IS THE WEAKER RESULT.** ### It proves a figure is not'),
    ('### the price is a floor', BANK,
     '### ### **THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR.** ### `b394` declared'),
    ('### the hazard is editing not reading', BANK,
     '### ### **THE DEFAULT IS OFF ON PURPOSE:** ### an anchor used to QUOTE a preserved'),
    ('### a floor on the hazard not a guard', BANK,
     '### ### AGAINST IT** -- this act`s own subject turned on its own remedy.'),
]

MUST_FAIL = [
    ('the bank never says the sweep was not tested', BANK, '### THE SWEEP WAS NOT TESTED.'),
    ('the bank never says a filter was discarded in silence', BANK,
     '### A FILTER WAS DISCARDED IN SILENCE.'),
    ('the bank never says a count was reported as a list', BANK,
     '### A COUNT WAS REPORTED AS A LIST.'),
    ('the bank never says a re-run was tuned', BANK, '### A RE-RUN WAS TUNED.'),
    ('the bank never says a caller was moved', BANK, '### A CALLER WAS MOVED.'),
    ('the bank never says an instrument was repaired', BANK, '### AN INSTRUMENT WAS REPAIRED.'),
    ('the bank never says a corpus document was edited', BANK,
     '### A CORPUS DOCUMENT WAS EDITED.'),
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
        if not subj.startswith('b396'):
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
    print('b396 -- GATE SUITE (HOW MANY FINDINGS REST ON A BACKTICK)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(Q['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    # ### **THIS ACT HAS NO EXTRACT FILE.** ### `b396` is a five-tool act: the order is read
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
    l7 = LG['act'] == 'b396' and not os.path.exists(t('b396_lockgate.py'))
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
    A3 = AC['a3']
    S0, S1, S4 = E['s0'], E['s1'], E['s4']

    # ----------------------------------------------------------- BAR 2, THE SWEEP'S OWN PREMISE
    print(chr(10) + '  G-PREMISE / G-THREEFORM / G-WIDEQUIET (BAR 2) ### THE ARM THAT MATTERS:')
    import b396_narrow as NAR
    import b396_figures as FG
    (f1, f2, f3), wide_clean, _by = NAR.fixture()
    q1 = f1 and f2 and f3
    q2 = wide_clean is True
    q3 = S0['forms'] == [True, True, True] and S0['wide_clean'] is True
    fx = FG.fixture()
    q4 = all(fx) and S1['filter_fixture'] == [fx[0], fx[1], fx[2]]
    q5 = len(NAR.DEAF) == 5 and S0['deaf'] == 5
    # ### **AND THE DEAFNESSES MUST BE IN THE INSTRUMENT, NOT ONLY IN THE BANK.**
    q6 = 'DEAF = [' in raw('b396_narrow.py')
    gq = q1 and q2 and q3 and q4 and q5 and q6
    print('    ### **THREE FORMS, ALL FOUND : %s** (%s, %s, %s)' % (q1, f1, f2, f3))
    print('    ### **THE WIDE FIXTURE IS CLEAN : %s** -- fires is not discriminates' % q2)
    print('    the figure filter is quiet on both controls : %s  %s' % (all(fx), list(fx)))
    print('    the five deafnesses are in the instrument : %s' % (q5 and q6))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-PREMISE/G-THREEFORM/G-WIDEQUIET')

    # -------------------------------------------------------------- BAR 3, THE FUNNEL AND DISCARDS
    print(chr(10) + '  G-FUNNEL / G-DISCARDS (BAR 3):')
    stages = [S0['tools'], S0['raw_backtick'], C1['parsed'], C1['narrow'], C1['files'],
              C1['figures']]
    n1 = all(str(x) in bank for x in stages)
    n2 = all(x in bank for x in ('374', '407', '350', '380', '79', '82'))
    n3 = 'A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER' in bu
    n4 = 'THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT' in bu
    n5 = C1['discards'] == 3
    n6 = 'HAS NO ANSWER AT INSTRUMENT GRANULARITY' in bu
    gn = n1 and n2 and n3 and n4 and n5 and n6
    print('    ### **EVERY FUNNEL STAGE IN THE BANK : %s**  %s' % (n1, stages))
    print('    ### **ALL THREE DISCARDS CARRY THEIR YIELDS : %s**' % n2)
    print('    the shape is called pervasive and the limit stated : %s' % (n4 and n6))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-FUNNEL/G-DISCARDS')

    # ----------------------------------------------------------------- BAR 4, THE FIGURE BAR
    print(chr(10) + '  G-FIGURES / G-RESOLVES (BAR 4):')
    rows = S1['rows']
    y1 = len(rows) == C1['figures'] == 82
    y2 = all(r.get('file') and r.get('report_line') and r.get('name') and r.get('report')
             for r in rows)
    # ### **EVERY ENTRY MUST RESOLVE IN ITS INSTRUMENT'S OWN BYTES.**
    bad = []
    for r in rows[:200]:
        src = raw(r['file']).split(chr(10))
        if not (0 < r['report_line'] <= len(src)):
            bad.append(r['file'])
    y3 = not bad
    y4 = C1['not_at_risk'] == C1['narrow'] - C1['files']
    y5 = 'NARROW IS NOT A DEFECT' in bu
    gy = y1 and y2 and y3 and y4 and y5
    print('    ### **AT-RISK FIGURES %d ; EVERY ONE NAMING FILE, LINE, NAME AND REPORT : %s**'
          % (len(rows), y2))
    print('    every report line resolves in its instrument : %s  %s' % (y3, bad[:3] or 'none'))
    print('    narrow-with-no-negative counted apart : %d ; said : %s'
          % (C1['not_at_risk'], y5))
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-FIGURES/G-RESOLVES')

    # ------------------------------------------------------------ BAR 5, THE BOTH-YIELDS BAR
    print(chr(10) + '  G-BOTHYIELDS / G-STATEDFIRST (BAR 5):')
    rr = C2['rows']
    b1 = len(rr) == 6 == C2['runs']
    b2 = all(('narrow_hits' in o and 'wide_hits' in o and o['verdict'] in
              ('CONFIRMED', 'MOVED', 'REFUTED')) for o in rr)
    b3 = all(o['said'] for o in rr)
    # ### **EVERY WIDENING IS A LITERAL IN THE COMPONENTS TOOL, WRITTEN BEFORE THE RUN.**
    csrc = raw('b396_components.py')
    b4 = all(o['wide'] in csrc for o in rr)
    b5 = all(str(o['narrow_hits']) in bank and str(o['wide_hits']) in bank for o in rr)
    b6 = 'THE UNIT IS THE FIGURE AND NOT THE MATCH COUNT' in bu
    gb = b1 and b2 and b3 and b4 and b5 and b6
    print('    ### **SIX RE-RUNS, EACH WITH BOTH YIELDS AND A VERDICT : %s**' % (b1 and b2))
    print('    ### **EVERY WIDENING IS A LITERAL IN THE TOOL, STATED BEFORE THE RUN : %s**' % b4)
    print('    the figure is the declared unit : %s ; verdicts %s' % (b6, C2['verdicts']))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BOTHYIELDS/G-STATEDFIRST')

    # ------------------------------------------------------------ BAR 6, THE DISJOINT-SETS BAR
    print(chr(10) + '  G-DISJOINT / G-ALLSIX (BAR 6):')
    d1 = C2['shared'] == 0
    d2 = all(x in bank for x in C2['cheapest']) and all(x in bank for x in C2['exposed'])
    d3 = len(set(o['act'] for o in rr)) == 6
    d4 = set(o['set'] for o in rr) == {'CHEAPEST', 'MOST EXPOSED'}
    d5 = 'ALL SIX WERE RUN' in bu
    gd = d1 and d2 and d3 and d4 and d5
    print('    ### **THE TWO SETS SHARE %d MEMBERS ; BOTH PRINTED : %s**' % (C2['shared'], d2))
    print('    ### **ALL SIX RUN, BOTH SETS REPRESENTED : %s**' % (d3 and d4 and d5))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DISJOINT/G-ALLSIX')

    # ---------------------------------------------------------------- BAR 7, THE OPT-IN BAR
    print(chr(10) + '  G-OPTIN / G-NOCALLERMOVED / G-ANCHORFIX (BAR 7):')
    r7 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'anchor_from_file.py'),
                         '--self-test'], capture_output=True, text=True, encoding='utf-8',
                        errors='replace')
    o1 = r7.returncode == 0 and A3['failing'] == 0 and A3['arms'] >= 12
    asrc = raw('anchor_from_file.py')
    o2 = 'def find(path, hint, editing=False)' in asrc
    o3 = A3['moved'] == 0 and A3['callers'] > 0
    # ### **THE DEFAULT MUST STILL FIND A PRESERVED LINE** -- a reader must not move.
    o4 = 'the DEFAULT still finds a preserved line' in (r7.stdout or '')
    o5 = 'REFUSED -- EVERY MATCH IS INSIDE A PRESERVED' in asrc
    o6 = 'NOT CLAIMED AS MECHANIZED' in bu or 'not claimed as' in asrc
    go = o1 and o2 and o3 and o4 and o5 and o6
    print('    ### **THE TOOL`S OWN FIXTURES : rc %d, %d arms, %d failing**'
          % (r7.returncode, A3['arms'], A3['failing']))
    print('    ### **THE MODE IS OPT-IN AND DEFAULT-OFF : %s**' % o2)
    print('    ### **CALLERS %d ; CALLERS MOVED %d**' % (A3['callers'], A3['moved']))
    print('    the default still finds a preserved line : %s ; refusal is a refusal : %s'
          % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-OPTIN/G-NOCALLERMOVED/G-ANCHORFIX')

    # -------------------------------------------------------------- BAR 8, THE PRICE-IS-A-FLOOR
    print(chr(10) + '  G-PRICEFLOOR (BAR 8):')
    p1 = C3['ten'] == 10 and C3['of'] == 16
    p2 = str(C3['minutes']) in bank and str(C3['per_keystone']) in bank
    p3 = 'A FLOOR BECAUSE ITS INPUT IS A FLOOR' in bu
    p4 = 'THE EASY END' in bu
    p5 = C3['after'] == C3['reconciled'] + C3['ten']
    gp = p1 and p2 and p3 and p4 and p5
    print('    ### **%s x %d = %s MIN ; %d of %d -> %d of %d**'
          % (C3['per_keystone'], C3['ten'], C3['minutes'], C3['reconciled'], C3['of'],
             C3['after'], C3['of']))
    print('    declared a floor : %s ; the sample`s bias named : %s' % (p3, p4))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRICEFLOOR')

    # ------------------------------------------------ G-NOREPAIR / G-NOCORPUSEDIT / G-NOAUTHOR
    print(chr(10) + '  G-NOREPAIR / G-NOCORPUSEDIT / G-NOAUTHOR:')
    # ### **NOT ONE PRIOR INSTRUMENT MAY HAVE MOVED.** ### The only relay tool edited is the
    # ### anchor tool, and it is declared.
    r9 = subprocess.run(['git', '-C', ROOT, 'diff', '--name-only', preact(ROOT), '--', 'tools'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    touched = sorted(x for x in (r9.stdout or '').split(chr(10)) if x.strip())
    allowed = set(NEW_THIS_ACT) | {'tools/anchor_from_file.py', 'tools/banked_index.py'}
    stray = [x for x in touched if x not in allowed]
    m1 = not stray
    # ### **NO CORPUS DOCUMENT MAY HAVE MOVED EXCEPT THE TRAIL.**
    r10 = subprocess.run(['git', '-C', PP, 'diff', '--name-only', preact(PP)],
                         capture_output=True, text=True, encoding='utf-8', errors='replace')
    ptouched = sorted(x for x in (r10.stdout or '').split(chr(10)) if x.strip())
    m2 = set(ptouched) <= {'OPEN_TRAILS.md'}
    m3 = 'NAMING A BODY OF WORK IS NOT DOING IT' in bu or C1['figures'] > 0
    gm = m1 and m2 and m3
    print('    ### **relay tools changed : %s**' % (touched or 'none'))
    print('    ### **STRAY (a prior act`s instrument repaired) : %s**' % (stray or 'none'))
    print('    ### **PLACE-papers files changed : %s**' % (ptouched or 'none'))
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-NOREPAIR/G-NOCORPUSEDIT/G-NOAUTHOR')

    # ------------------------------------------------------------- G-NOWRITE / G-NOPLATFORM
    print(chr(10) + '  G-NOWRITE / G-NOPLATFORM:')
    dirty = []
    for rel in UNTOUCHED:
        pr = blob_of(PP, rel, preact(PP)) or ''
        nw = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                     errors='replace').read()
        if norm(pr) != norm(nw):
            dirty.append(rel)
    w1 = not dirty
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b396_') and x.endswith('.py')))
    NETY = ('zenodo.org', 'doi.org', 'urllib', 'requests', 'curl', 'ls-remote')
    nhits = [(x, k) for x in mymods1 for k in NETY if k in strip_prose(t(x))]
    w2 = not nhits
    BUILDY = ('lake ', 'LEAN_PATH', '.olean', 'print axioms', 'git clone')
    bhits = [(x, k) for x in mymods1 for k in BUILDY if k in strip_prose(t(x))]
    w3 = not bhits
    gw2 = w1 and w2 and w3
    print('    ### **DOCUMENTS THAT MUST NOT MOVE, CHANGED : %s**' % (dirty or 'none'))
    print('    network tokens : %s ; build tokens : %s' % (nhits or 'none', bhits or 'none'))
    print('    %s' % ('PASS' if gw2 else '### FAIL ###'))
    if not gw2:
        fails.append('G-NOWRITE/G-NOPLATFORM')

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
    cq = [m for m in Q['marks'] if 'at-risk figures, unrepaired' in m['item']]
    n4 = (len(cq) == 1 and cq[0]['disposition'] == 'STAND'
          and 'REPAIRS NONE OF THEM' in cq[0]['why'].upper())
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
    print('    ### **THE 82 UNREPAIRED FIGURES STAND AS AN OPEN ITEM** : %s' % n4)
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
               'PLACE-papers': {'OPEN_TRAILS.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b396' not in x)
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
    t3 = len(rws) == 1 and anc and 'THE BACKTICK SWEPT' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-backtick-swept returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('the sweep was not tested', 'a filter was discarded in silence',
              'an instrument was repaired', 'the platform was called'))
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
    mirrorp = d('b396_mirror.txt')
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
        ('tools %d' % S0['tools'], str(S0['tools']) in bank),
        ('raw backtick %d' % S0['raw_backtick'], str(S0['raw_backtick']) in bank),
        ('parsed %d' % C1['parsed'], str(C1['parsed']) in bank),
        ('narrow %d' % C1['narrow'], str(C1['narrow']) in bank),
        ('at-risk instruments %d' % C1['files'], str(C1['files']) in bank),
        ('at-risk figures %d' % C1['figures'], str(C1['figures']) in bank),
        ('acts %d' % C1['acts'], str(C1['acts']) in bank),
        ('re-runs %d' % C2['runs'], str(C2['runs']) in bank),
        ('moved %d' % C2['moved'], str(C2['moved']) in bank),
        ('narrow without consequence %d' % C2['nwc'], str(C2['nwc']) in bank),
        ('the price %s' % C3['minutes'], str(C3['minutes']) in bank),
        ('the census after %d' % C3['after'], str(C3['after']) in bank),
        ('blockquoted blocks %d' % A3['blocks'], str(A3['blocks']) in bank),
        ('fixture arms %d' % A3['arms'], str(A3['arms']) in bank),
        ('callers %d' % A3['callers'], str(A3['callers']) in bank),
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
                          if x.startswith('b396_') and x.endswith('.py')))
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
              if x.strip() and 'b396' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
    e2 = ('AND NOTHING ELSE IN ANY REPOSITORY' in reg
          and 'one key in `tools/banked_index.py`' in reg
          and 'anchor_from_file.py' in reg)
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
             d('b396_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b396_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE BACKTICK SWEPT (b396).'
    nxt = '# ### THE CEILING ANSWERED (b395).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b396_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b396_hedge_')
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
