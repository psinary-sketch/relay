# -*- coding: utf-8 -*-
"""b376_checks.py -- THE GATE SUITE FOR THE TWO-AXIS READ.

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


BANK = d('b376_the_two_axis_read.txt')
REG = d('b376_registration_2026-09-08.txt')
FERRY = d('b376_ferry_2026-09-08.txt')
IDX = d('b376_desk_notes.txt')
SCAN, TERMSCAN, GATE = d('b376_ferry_scan.txt'), d('b376_reg_termscan.txt'), d('b376_reg_gate.txt')
CENSUS0, FCEN = d('b376_census_stepzero.txt'), d('b376_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b376_regspec_run.txt'), d('audit_b376_reg_satisfiable.txt')
PINS0 = d('b376_pins_stepzero.txt')
SEAL = 'fa1db1b211259086c8d97631918ef25572e39d89b1923d2225dad35d4c395298'
SEAL375 = '73589d06544449c00a4d5bc5bf078d557c4125503fbe4b376b31f4a8db91f1da'
ROWNUM = '225'
TRAIL_MARK = '<!-- b376 the two-axis read; every test crosses -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b376_reads.json'), ('LG', 'b376_lockgate.json'),
                   ('PR', 'b376_prior.json'), ('AX', 'b376_axes.json'),
                   ('TS', 'b376_tests.json'), ('Q', 'b376_desk.json'))}

NEW_THIS_ACT = {'tools/b376_regspec.py', 'tools/b376_extract.py', 'tools/b376_reg_gate.py',
                'tools/b376_lockgate.py', 'tools/b376_prior.py', 'tools/b376_axes.py',
                'tools/b376_tests.py', 'tools/b376_desk.py', 'tools/b376_bank.py',
                'tools/b376_checks.py'}

TOOLNUM = [
    ('STEP ZERO -- the lock that reads every gate', 'tools/b376_lockgate.py'),
    ("the corpus's own prior attempt, heard first", 'tools/b376_prior.py'),
    ('the two axes and every document scored on both', 'tools/b376_axes.py'),
    ('the crossings and the floor', 'tools/b376_tests.py'),
    ('(R7), the trail block, the row and the key', 'tools/b376_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b376_bank.py'),
    ('the reads', 'tools/b376_extract.py'),
    ('the registration gate', 'tools/b376_reg_gate.py'),
    ('the clause spec', 'tools/b376_regspec.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('THE GRADE TOKENS AXIS B READS, IMPORTED UNTOUCHED', 'tools/hedge_audit.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
KCENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
PRIORF = d('b375_ferry_2026-09-08.txt')

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b376 - THE TWO-AXIS READ. Number not claimed by any'),
    ('the order -- the scope', FERRY,
     'unclosed ferry. SCOPE: READS and CLASSIFICATION only. NO class'),
    ('the order -- it makes no ruling', FERRY,
     "evidence the author's class ruling needs and makes no ruling."),
    ('the order -- step zero, the lock reads every gate', FERRY,
     "STEP ZERO - THE LOCK READS EVERY GATE. b375's incident: the"),
    ('the order -- component 1, heard first', FERRY,
     "COMPONENT 1 - THE CORPUS'S OWN PRIOR ATTEMPT, heard first: read"),
    ('the order -- component 1, operation not prose', FERRY,
     'location; state what test it actually applies, read from its'),
    ('the order -- component 2, quoted not invented', FERRY,
     'COMPONENT 2 - THE TWO AXES, QUOTED NOT INVENTED: AXIS A -'),
    ('the order -- axis B, in the order`s words', FERRY,
     'AXIS B - certifies at pins, meaning a correspondence table'),
    ('the order -- what each predicate is deaf to', FERRY,
     'with fixtures in both polarities, and state what each predicate'),
    ('the order -- component 3, both axes independently', FERRY,
     'COMPONENT 3 - EVERY DOCUMENT SCORED ON BOTH AXES,'),
    ('the order -- component 4', FERRY,
     'COMPONENT 4 - DO THE TESTS TRACK THE AXES: for each of the'),
    ('the order -- a test that crosses mixes the axes', FERRY,
     'of it, or crosses quadrants. A test that crosses is a test that'),
    ('the order -- component 5, the floor question', FERRY,
     "COMPONENT 5 - THE FLOOR QUESTION, the author's: the rubric-test"),
    ('the order -- a floor and not a population', FERRY,
     'plainly that the rubric-test set is a FLOOR and not a'),
    ('the order -- component 6, without recommending', FERRY,
     'COMPONENT 6 - WHAT THIS READ CANNOT DECIDE: the ruling. State'),
    ('the order -- two marks rather than one class', FERRY,
     'without recommending - including, if the quadrants support it,'),
    ("the order -- the navigator's expectations", FERRY,
     "proposing only what this act found. The navigator's"),
    ('axis A -- the rubric, KEYSTONE half', PRIORF,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('axis B -- Tier K in the taxonomy', TAX, '**Tier K — Keystone-certified.**'),
    ("the prior attempt -- the STATED definition", KCENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the prior attempt -- the OPERATIONALISED line', KCENSUS,
     '**OPERATIONALISED:** (i) = an `Abstract` heading or an ORCID block'),
]

SELF_NEEDLES = [
    ('the bank leads with every test crossing', BANK,
     'EVERY ONE OF THE THREE TESTS CROSSES THE QUADRANTS, AND SO DOES THE CORPUS`S OWN'),
    ('### it rules nothing', BANK, 'THIS ACT RULES NOTHING.'),
    ('### the conflict was already inside the first test', BANK,
     'INSIDE THE FIRST ONE**, and that is `(E1)` met by quotation rather than by count.'),
    ('### the lock was chained on the gate that reads every gate', BANK,
     'AND THE LOCK WAS CHAINED ON THAT TOOL`S EXIT CODE AND NOT ON ANY ONE GATE`S.'),
    ('### a gate that has only ever said yes', BANK,
     'A GATE THAT HAS ONLY EVER SAID YES IS NOT A GATE:'),
    ('### what the lock gate still cannot do', BANK,
     'WAS RUN AGAINST THE RIGHT THING**, and a stale record from an earlier run of the same act'),
    ('### the census is quoted, not repaired', BANK,
     'AND THE CENSUS IS QUOTED, NOT REPAIRED.'),
    ('### each predicate declares what it is deaf to', BANK,
     'AND EACH DECLARES WHAT IT IS DEAF TO, IN ITS OWN SOURCE AND ON THIS PAGE:'),
    ('### not determinable is a full answer', BANK, 'NOT DETERMINABLE IS A FULL ANSWER.'),
    ('### the apparatus and the prose come apart', BANK,
     'DOCUMENTS THAT SAY NOTHING ABOUT THEIR ROLE WOULD BECOME KEYSTONES BY APPARATUS.'),
    ('### both directions of the difference by document', BANK,
     'BOTH DIRECTIONS OF THE DIFFERENCE, BY DOCUMENT AND NOT COUNTED'),
    ('### agreement is not confirmation', BANK,
     'CONFIRMATION THAT THE DECLARATIONS ARE CORRECT** -- both may be reading the same habit of'),
    ('### the floor said plainly', BANK,
     'THE RUBRIC-TEST SET IS A FLOOR AND NOT A'),
    ('### the caveat printed at the finding', BANK,
     'AND THE CAVEAT IS PRINTED AT THE FINDING, NOT LEFT IN THE PREDICATE`S SMALL PRINT:'),
    ('### component 6 recommends nothing', BANK,
     'NONE IS RECOMMENDED, NONE IS RANKED, AND NO ORDERING BELOW IS AN ORDERING OF'),
    ('### what the evidence does not support', BANK,
     'the evidence does not support the claim that one of the three existing'),
    ('### a mark on an axis is not a class', BANK,
     'A MARK ON AN AXIS IS NOT A CLASS.'),
    ('### the four lists restated open in the desk`s own words', BANK,
     'THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS AND NOT IN'),
]

# ### **THE ORDER'S FIVE PROHIBITIONS, EACH AS A WHOLE LINE THE BANK MUST NOT CARRY.**
MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a document was reclassified', BANK, '### A DOCUMENT WAS RECLASSIFIED.'),
    ('the bank never says a class line was written', BANK, '### A CLASS LINE WAS WRITTEN.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never names a preferred option', BANK, '### THE PREFERRED OPTION IS.'),
]

# ### **`G-NOPREFER` READS THE OPTIONS REGION ONLY**, located by content, and looks for words that
# ### would make one option the seat's choice. ### The order says `without recommending`.
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
    print('b376 -- GATE SUITE (THE TWO-AXIS READ)')
    print('=' * 100)
    E, LG, PR, AX, TS, Q = (_J['E'], _J['LG'], _J['PR'], _J['AX'], _J['TS'], _J['Q'])
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 230:
                inx = line.rstrip()[:230] in extract
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

    # ------------------------------------------------------------------- BAR 1, THE LOCK-GATE BAR
    print(chr(10) + '  G-LOCKGATE / G-EVERYGATE / G-FIXTURE (BAR 1):')
    lgrun = io.open(d(LG['run_file']), encoding='utf-8', errors='replace').read()
    l1 = LG['fixture_ok'] is True and LG['permits'] is True
    l2 = LG['gates_read'] == LG['gates_passing'] == 7
    l3 = all(g['passed'] for g in LG['gates'])
    # ### **THE ARM READS WHAT THE TOOL PRINTS, NOT ITS SOURCE** (`b373`).
    l4 = ('GATES READ : %d. ### PASSING : %d. ### VERDICT : LOCK PERMITTED'
          % (LG['gates_read'], LG['gates_passing'])) in gate_text.flat(lgrun)
    l5 = 'BOTH POLARITIES HELD' in gate_text.flat(lgrun)
    # ### **AND THE DIRTY POLARITY MUST HAVE REFUSED FOR THE RIGHT GATE, NOT MERELY REFUSED.**
    dirty = LG['fixture']['one gate dirty (the term scan)']
    l6 = dirty['permits'] is False and len(dirty['failing']) == 1
    l7 = LG['fixture']['all gates clean']['permits'] is True
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7
    print('    gates read %d / passing %d ; all pass : %s' % (LG['gates_read'],
                                                              LG['gates_passing'], l3))
    for g in LG['gates']:
        print('      %-46s %-38s %s' % (g['gate'][:46], g['file'][:38],
                                        'PASS' if g['passed'] else '### FAIL ###'))
    print('    ### **THE RUN FILE ITSELF CARRIES THE VERDICT** : %s' % l4)
    print('    fixture both polarities held : %s ; clean permits : %s' % (l5, l7))
    print('    ### **AND THE DIRTY POLARITY REFUSED FOR EXACTLY ONE GATE** : %s %s'
          % (l6, dirty['failing']))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LOCKGATE/G-EVERYGATE/G-FIXTURE')

    # -------------------------------------------------------------------- BAR 2, THE NO-WRITE BAR
    print(chr(10) + '  G-NOWRITE (BAR 2) ### EVERY ROSTERED REPOSITORY AGAINST ITS BLOBS:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b376' not in x and x != 'tools/banked_index.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    n1 = all(not v for v in dirtyrepo.values())
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    n2 = not frozen
    gn = n1 and n2
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **FROZEN PATHS CHANGED : %s**' % (frozen or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOWRITE')

    # ------------------------------------------- BAR 3, THE QUOTATION BAR / G-PRIOR G-STATED G-APPLIED
    print(chr(10) + '  G-PRIOR / G-STATED / G-APPLIED / G-AXISQUOTED (BAR 3):')
    ktxt = io.open(KCENSUS, encoding='utf-8', errors='replace').read().split(chr(10))
    q1 = PR['stated']['KEYSTONE']['text'] in ktxt[PR['stated']['KEYSTONE']['line'] - 1]
    q2 = PR['operationalised_text'] in ktxt[PR['operationalised_line'] - 1]
    q3 = len(PR['mapping']) == 4 and any('NOT OPERATIONALISED' in m['operates']
                                         for m in PR['mapping'])
    q4 = PR['agree'] is False
    # ### **EVERY AXIS QUOTE RE-READ OUT OF ITS OWN SOURCE FILE, AT ITS OWN LINE.**
    SRC = {'b375_ferry_2026-09-08.txt': PRIORF, 'THE_DOCUMENT_CLASS_TAXONOMY.md': TAX,
           'b376_ferry_2026-09-08.txt': FERRY}
    qbad = []
    for tag, q in AX['quotes'].items():
        src = SRC.get(q['file'])
        if not src:
            qbad.append((tag, 'no source'))
            continue
        lines = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        if q['text'] not in lines[q['line'] - 1]:
            qbad.append((tag, 'the banked quote is not at its banked line'))
    q5 = not qbad
    # ### **AND EVERY AXIS MARK THAT IS NOT `NOT DETERMINABLE` QUOTES A SENTENCE IN ITS DOCUMENT.**
    mbad = []
    for x in AX['scored']:
        if x['axis_a'] in ('A+', 'A-') and not x['a_sentence']:
            mbad.append((x['file'], 'axis A mark with no sentence'))
        if x['axis_b'] == 'B+' and not x['b_row']:
            mbad.append((x['file'], 'axis B mark with no row'))
    q6 = not mbad
    gq = q1 and q2 and q3 and q4 and q5 and q6
    print('    the stated definition is at its banked line : %s' % q1)
    print('    the OPERATIONALISED line is at its banked line : %s' % q2)
    print('    ### **THE MAPPING NAMES A CLAUSE THAT IS NOT OPERATIONALISED AT ALL** : %s' % q3)
    print('    the act reports the two do NOT agree : %s' % q4)
    print('    every axis quote re-read at its own line : %s %s' % (q5, qbad[:2] or ''))
    print('    every decided mark carries its sentence : %s %s' % (q6, mbad[:2] or ''))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-PRIOR/G-STATED/G-APPLIED/G-AXISQUOTED')

    # ---------------------------------------- BAR 4, THE POLARITY BAR / G-DEAF / G-BOTHMARKS
    print(chr(10) + '  G-FIXTURE(AXES) / G-DEAF / G-BOTHMARKS / G-NOTDETERMINABLE (BAR 4):')
    p1 = AX['fixtures_ok'] is True
    p2 = all(f['got'] == f['want'] for f in AX['fixtures'])
    # ### **BOTH POLARITIES MEANS AT LEAST ONE FIXTURE PER AXIS MUST HAVE SAID NO.**
    p3 = any(f['want'] == 'A-' for f in AX['fixtures']) and \
        any(f['want'] == 'B-' for f in AX['fixtures'])
    p4 = all(x['axis_a'] in ('A+', 'A-', 'A?') and x['axis_b'] in ('B+', 'B-', 'B?')
             for x in AX['scored'])
    p5 = all(x['axis_a_broad'] in ('A+', 'A-', 'A?') for x in AX['scored'])
    p6 = 'DEAF TO' in bf and 'AXIS A IS DEAF TO' in bf and 'AXIS B IS DEAF TO' in bf
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    axis fixtures held : %s ; every fixture matched : %s' % (p1, p2))
    print('    ### **AND A NEGATIVE FIXTURE EXISTS ON BOTH AXES** : %s' % p3)
    print('    every document carries two marks from the declared alphabets : %s' % p4)
    print('    the broad reading also scored every document : %s' % p5)
    print('    ### **THE BANK STATES WHAT EACH PREDICATE IS DEAF TO** : %s' % p6)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-FIXTURE(AXES)/G-DEAF/G-BOTHMARKS/G-NOTDETERMINABLE')

    # ------------------------------------------------------------------ BAR 5, THE PARTITION BAR
    print(chr(10) + '  G-PARTITION (BAR 5):')
    N = len(AX['scored'])
    r1 = sum(AX['quadrants'].values()) == N
    r2 = sum(AX['quadrants_broad'].values()) == N
    r3 = len(set(x['file'] for x in AX['scored'])) == N
    DECLARED9 = {'A+B+', 'A+B-', 'A-B+', 'A-B-', 'A+B?', 'A-B?', 'A?B+', 'A?B-', 'A?B?'}
    r4 = set(AX['quadrants']) <= DECLARED9 and set(AX['quadrants_broad']) <= DECLARED9
    gr = r1 and r2 and r3 and r4
    print('    strict cells sum to the sweep : %s ; broad cells sum to the sweep : %s' % (r1, r2))
    print('    ### **NO DOCUMENT APPEARS TWICE** : %s' % r3)
    print('    no cell outside the declared nine : %s' % r4)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-PARTITION')

    # ---------------------------------------------- BAR 6, THE DIFFERENCE-BY-DOCUMENT BAR
    print(chr(10) + '  G-TRACK / G-CROSSES / G-BYDOCUMENT (BAR 6):')
    c1 = TS['crosses'] == 3
    c2 = all(TS['tests'][k]['crosses'] for k in TS['tests'])
    c3 = all(TS['tests'][k]['vs_axis_a'] != 'EQUALS' and TS['tests'][k]['vs_axis_b'] != 'EQUALS'
             for k in TS['tests'])
    # ### **BOTH DIRECTIONS LISTED BY DOCUMENT, NOT COUNTED:** ### every named document must appear
    # ### in the bank by its own path.
    named = TS['overlap_not_quadrant'] + TS['quadrant_not_overlap']
    missing = [f for f in named if f not in bank]
    c4 = not missing
    c5 = TS['overlap_equals_quadrant'] is False
    gc = c1 and c2 and c3 and c4 and c5
    print('    all three tests cross : %s ; none equals either axis : %s' % (c1 and c2, c3))
    print('    ### **BOTH DIRECTIONS LISTED BY DOCUMENT IN THE BANK** : %s %s'
          % (c4, missing[:2] or ''))
    print('    the overlap is NOT the both-axes quadrant : %s' % c5)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-TRACK/G-CROSSES/G-BYDOCUMENT')

    # ---------------------------------------------------------- G-FLOOR / G-BOTHCOUNTS
    print(chr(10) + '  G-FLOOR / G-BOTHCOUNTS:')
    f1 = TS['is_a_floor'] is True
    f2 = 'FLOOR AND NOT A' in bf
    # ### **EACH QUALIFIER PRINTED WITH THE SENTENCE THAT QUALIFIES IT.**
    fmiss = [f for f in TS['other_satisfying_a'] if f not in bank]
    f3 = not fmiss
    f4 = len(TS['qualifying_on_a_later_acts_class_line']) >= 0 and 'CAVEAT IS PRINTED' in bf
    f5 = str(len(TS['other_satisfying_a'])) in bank and \
        str(len(TS['other_satisfying_a_broad'])) in bank
    gf = f1 and f2 and f3 and f4 and f5
    print('    the floor is reported as a floor : %s ; said plainly in the bank : %s' % (f1, f2))
    print('    every qualifier printed with its sentence : %s %s' % (f3, fmiss[:2] or ''))
    print('    ### **AND THE LATER-ACT-CLASS-LINE CAVEAT IS AT THE FINDING** : %s' % f4)
    print('    both counts (strict and broad) are in the bank : %s' % f5)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FLOOR/G-BOTHCOUNTS')

    # ------------------------------------------------ BAR 7, THE NO-RULING BAR / G-OPTIONS G-NOPREFER
    print(chr(10) + '  G-OPTIONS / G-NOPREFER / G-NORULING (BAR 7):')
    o_start = bank.find('### COMPONENT 6 -- WHAT THIS READ CANNOT DECIDE.')
    o_end = bank.find('### WHAT THIS ACT DID NOT DO.')
    region = bank[o_start:o_end] if (o_start >= 0 and o_end > o_start) else ''
    n_opts = len(re.findall(r'### \*\*OPTION \d+ --', region))
    b1 = n_opts >= 3
    b2 = all(x in region for x in ('THE EVIDENCE FOR IT:', 'WHAT IT WOULD OBLIGE:'))
    # ### **AND THE OPTION THE ORDER NAMES BY NAME MUST BE AMONG THEM.**
    b3 = 'TWO MARKS RATHER THAN ONE CLASS' in region
    # ### `G-NOPREFER` READS THE OPTIONS REGION ONLY, LOCATED BY CONTENT.
    # ### **THE USE-AND-MENTION SPECIES, AND THE ARM IS BUILT AGAINST IT** (`b348`). ### A sentence
    # ### that says `NONE IS RECOMMENDED` contains the word and ### **ASSERTS ITS NEGATION.** ### The
    # ### arm reports EVERY raw hit and then discharges only those whose own clause negates them, so
    # ### the discharge is inspectable rather than silent. ### **AN ARM THAT FIRES ON A SENTENCE
    # ### ### SAYING THE THING WAS NOT DONE IS NOT MEASURING THE THING.**
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append((m.group(0),
                         region[max(0, m.start() - 60):m.end() + 20].replace(chr(10), ' ')))
    hits = sorted(set(x[0] for x in live))
    print('    ### raw preference-word hits : %s' % (sorted(set(raw)) or 'none'))
    for _wd, _ctx in live:
        print('        ### ### **LIVE: %s** | %s' % (_wd, _ctx))
    b4 = not hits
    b5 = 'NONE IS RECOMMENDED, NONE IS RANKED' in gate_text.flat(region)
    b6 = Q['lists_closed'] == 0 and Q['closed'] == 0
    gb = b1 and b2 and b3 and b4 and b5 and b6
    print('    options stated : %d ; each with its evidence and its obligation : %s' % (n_opts, b2))
    print('    ### **THE ORDER`S OWN OPTION -- TWO MARKS RATHER THAN ONE CLASS -- IS AMONG THEM** : %s'
          % b3)
    print('    ### **PREFERENCE WORDS IN THE OPTIONS REGION : %s**' % (hits or 'none'))
    print('    the region says none is recommended : %s ; lists closed : %d'
          % (b5, Q['lists_closed']))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-OPTIONS/G-NOPREFER/G-NORULING')

    # --------------------------------------------------------- G-OPEN / G-NONEWDOC / G-NOCHECK
    print(chr(10) + '  G-OPEN / G-NONEWDOC / G-NOCHECK:')
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    # ### **THE ARM READS THE DESK'S OWN STRINGS, NOT A PARAPHRASE OF THEM** -- a list restated
    # ### in different words is a different list.
    k1 = all(x in bank for x in lists)
    k2 = 'ARE RESTATED `OPEN` BY NAME' in bank or 'RESTATED OPEN BY NAME' in bf
    k3 = 'STAY OPEN BY NAME' in gate_text.flat(tblk) or 'OPEN BY NAME' in gate_text.flat(tblk)
    k4 = Q['lists_closed'] == 0
    # ### **AN ARM THAT WOULD FAIL ON A PRE-EXISTING CONDITION IS NOT MEASURING THIS ACT** (`b375`).
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    k5 = not newdocs
    # ### **NO KERNEL WAS OPENED AND NO PIN RESOLVED -- READ FROM THE BANK'S OWN DECLARATION.**
    k6 = 'NO KERNEL WAS OPENED, NO PIN WAS RESOLVED, NO CITATION WAS CHECKED.' in bf
    gk = k1 and k2 and k3 and k4 and k5 and k6
    print('    the four lists are named in the bank : %s ; restated OPEN : %s' % (k1, k2))
    print('    ### **AND RESTATED OPEN IN THE TRAIL BLOCK** : %s' % k3)
    print('    lists closed : %d ; desk items closed : %d' % (Q['lists_closed'], Q['closed']))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (k5, newdocs[:2] or ''))
    print('    the bank declares no kernel opened and no pin resolved : %s' % k6)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-OPEN/G-NONEWDOC/G-NOCHECK')

    # ------------------------------------------------------------------ G-TRAIL / G-ROW / G-KEY
    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'EVERY TEST CROSSES' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = 'every-test-crosses returns 1 row(s)' in irun and Q['key_ok'] is True
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the documents are reclassified',
              'the lists are closed', 'the keystone test is settled'))
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
    relied = (PR, AX, TS, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND `b375`'S DEFECTIVE FACE MUST STILL VERIFY, UNEDITED.**
    R375 = d('b375_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b375`S DEFECTIVE FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b376_hooks.txt'), d('b376_mirror.txt')
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
    QD = AX['quadrants']
    checks = [
        ('documents %d' % N, str(N) in bank),
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('the operation returns %d' % len(PR['operation_returns']),
         str(len(PR['operation_returns'])) in bank),
        ('the census printed %d' % len(PR['census_named']), str(len(PR['census_named'])) in bank),
        ('tests crossing %d' % TS['crosses'], str(TS['crosses']) in bank),
        ('the overlap %d' % len(TS['overlap']), str(len(TS['overlap'])) in bank),
        ('the A+B+ quadrant %d' % len(TS['both_axes']), str(len(TS['both_axes'])) in bank),
        ('axis B plus %d' % len(TS['axis_b_plus']), str(len(TS['axis_b_plus'])) in bank),
        ('apparatus-only %d' % (QD.get('A-B+', 0) + QD.get('A?B+', 0)),
         str(QD.get('A-B+', 0) + QD.get('A?B+', 0)) in bank),
        ('silent on axis A %d' % AX['axis_a_tally'].get('A?', 0),
         str(AX['axis_a_tally'].get('A?', 0)) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on axes run', AX['run_file'] in bank),
        ('the relied-on tests run', TS['run_file'] in bank),
        ('the relied-on lock-gate run', LG['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    # ----------------------------------------------------------------------------------- G-ONCE
    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('prior', PR), ('axes', AX),
                    ('tests', TS), ('desk', Q)):
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
                          if x.startswith('b376_') and x.endswith('.py')))
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
              if x.strip() and 'b376' not in x and x.strip() != 'tools/banked_index.py']
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
             d('b376_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b376_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(PR['run_file']), "the prior run carries the census's own sentences"),
        (d(AX['run_file']), "the axes run carries the documents' own sentences"),
        (d(TS['run_file']), "the tests run carries the documents' own sentences"),
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

    marker = '# ### THE TWO-AXIS READ (b376).'
    nxt = '# ### THE KEYSTONE AND CLUSTER CENSUS (b375).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b376_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT TEN NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 10 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b376_hedge_')
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
