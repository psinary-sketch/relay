# -*- coding: utf-8 -*-
"""b377_checks.py -- THE GATE SUITE FOR THE UNBLOCKED OBLIGATION.

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


BANK = d('b377_the_unblocked_obligation.txt')
REG = d('b377_registration_2026-09-08.txt')
FERRY = d('b377_ferry_2026-09-08.txt')
IDX = d('b377_desk_notes.txt')
SCAN, TERMSCAN, GATE = d('b377_ferry_scan.txt'), d('b377_reg_termscan.txt'), d('b377_reg_gate.txt')
CENSUS0, FCEN = d('b377_census_stepzero.txt'), d('b377_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b377_regspec_run.txt'), d('audit_b377_reg_satisfiable.txt')
PINS0 = d('b377_pins_stepzero.txt')
SEAL = '1fe898fbdeade87273a39cd69045dd9b5ca757b84ca879c7bc727d8e09a412b6'
ROWNUM = '226'
TRAIL_MARK = '<!-- b377 the unblocked obligation; the pin was the missing element -->'
ADDENDUM_MARK = '<!-- b377 correspondence addendum; pins read at this act -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b377_reads.json'), ('LG', 'b377_lockgate.json'),
                   ('BR', 'b377_branch.json'), ('EV', 'b377_evidence.json'),
                   ('Q', 'b377_desk.json'))}

NEW_THIS_ACT = {'tools/b377_regspec.py', 'tools/b377_extract.py', 'tools/b377_reg_gate.py',
                'tools/b377_branch.py', 'tools/b377_evidence.py', 'tools/b377_desk.py',
                'tools/b377_bank.py', 'tools/b377_checks.py'}

TOOLNUM = [
    ('STEP ZERO -- the lock that reads every gate, INHERITED', 'tools/b376_lockgate.py'),
    ('the branch, applied and not chosen', 'tools/b377_branch.py'),
    ('the role clause, the five options, the two filings', 'tools/b377_evidence.py'),
    ('(R7), the trail block, the row and the key', 'tools/b377_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b377_bank.py'),
    ('the reads', 'tools/b377_extract.py'),
    ('the registration gate', 'tools/b377_reg_gate.py'),
    ('the clause spec', 'tools/b377_regspec.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
KCENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
PRIORF = d('b375_ferry_2026-09-08.txt')

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     "ACT b377 - THE UNBLOCKED OBLIGATION, AND THE RULING'S EVIDENCE"),
    ('the order -- the scope', FERRY,
     'repair-or-route under an obligation the taxonomy already'),
    ('the order -- nothing ruled, nothing moved', FERRY,
     'class ruled, NO document reclassified, NO declaration moved,'),
    ('the order -- the role clause, first half', FERRY,
     'evidence and not as a ruling: "Keystones are for clarifying'),
    ('the order -- the role clause, second half', FERRY,
     'vision in explanatory clarity just because we have been'),
    ('the order -- the role axis, not the apparatus axis', FERRY, 'they speak to the role'),
    ('the order -- the five options quoted whole', FERRY,
     "COMPONENT 2 - THE FIVE OPTIONS, QUOTED WHOLE: b376's Component"),
    ('the order -- the six documents', FERRY,
     'COMPONENT 3 - THE SIX DOCUMENTS, which do not wait on the'),
    ('the order -- the branch fixed here', FERRY, 'decide by a branch fixed here: if the'),
    ('the order -- route and repair nothing', FERRY, 'cannot be located, ROUTE it with'),
    ('the order -- a document says what it says', FERRY, 'No declaration is'),
    ('the order -- the census drift filed', FERRY,
     "COMPONENT 4 - TWO FILINGS: (i) the prior census document's own"),
    ('the order -- the clusters as a work-order', FERRY,
     'six clusters with registry rows and no keystone, restated'),
    ('the order -- priced and NOT opened', FERRY, 'Filed as a work-order, priced if the record'),
    ("the order -- the navigator's expectations", FERRY,
     'expectations: (F1) most of the six can be met by appending from'),
    ('the amendment -- not determinable is not absent', FERRY,
     'and LEFT - not determinable is not absent, and neither is'),
    ('the amendment -- what would decide it', FERRY,
     'for each what the read could not decide and what would decide'),
    ('the amendment -- the findings layer alone', FERRY,
     'on a keystone and is not in it was taken against the findings'),
    ('the amendment -- the wider question', FERRY,
     "is wider - what bears on a keystone's subject anywhere"),
    ('the amendment -- a FLOOR, not re-measured here', FERRY,
     'banked figure as a FLOOR against the wider question, name the'),
    ("the taxonomy -- Tier K and what it obliges", TAX,
     '**Tier K — Keystone-certified.**'),
    ('the census -- the STATED definition', KCENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the census -- the OPERATIONALISED line', KCENSUS,
     '**OPERATIONALISED:** (i) = an `Abstract` heading or an ORCID block'),
]

SELF_NEEDLES = [
    ('the bank leads with the pin, not the terminal', BANK,
     'THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL.'),
    ('### the predicate had its own share of the defect', BANK,
     'SO THE DEFECT WAS PARTLY THE PREDICATE`S AND NOT THE DOCUMENTS`, AND THIS ACT`S'),
    ('### the lock gate was inherited, not rebuilt', BANK,
     'A CURE THAT HAS TO BE REBUILT EVERY ACT IS NOT A CURE.'),
    ('### the hole was hit in practice', BANK,
     'AND THE HOLE `b376` NAMED WAS HIT IN PRACTICE HERE.'),
    ('### the role clause speaks to the role axis', BANK, 'IT SPEAKS TO THE ROLE AXIS.'),
    ('### a clause on one axis does not rule two', BANK,
     'A CLAUSE THAT BEARS ON ONE AXIS DOES NOT RULE A QUESTION THAT SPANS TWO'),
    ('### none of the five is recommended', BANK,
     'FIVE OPTIONS, FIVE BEARING LINES. ### NONE RECOMMENDED, NONE RANKED, AND THE ORDER'),
    ('### one unresolved terminal sends the document to arm 2', BANK,
     'THE RULE THAT DID THE WORK: ### ONE UNRESOLVED TERMINAL SENDS THE WHOLE DOCUMENT TO'),
    ('### a name in two kernels is not a terminal', BANK,
     'AND A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL THIS ACT CAN WRITE INTO A ROW'),
    ('### the first run was reverted, not kept', BANK,
     'first of several silently, and ### **THAT FIRST RUN`S APPENDS WERE REVERTED, NOT KEPT.**'),
    ('### not determinable is a third answer', BANK,
     '`NOT DETERMINABLE` IS A THIRD ANSWER AND NOT A SOFT `NO`.'),
    ('### both filings are filed and not opened', BANK,
     'FILED. ### NOT OPENED. ### NOT REPAIRED'),
    ('### the banked figure is a floor', BANK,
     'SO THE BANKED FIGURE IS A FLOOR AND NOT AN ANSWER'),
    ('### the act does not re-measure it', BANK, 'AND THIS ACT DOES NOT RE-MEASURE IT.'),
    ('### a document says what it says', BANK, 'A DOCUMENT SAYS WHAT IT SAYS.'),
    ('### every write is an append and a true prefix', BANK,
     'EVERY WRITE INTO A DOCUMENT IS AN APPEND**, and for each the committed blob remains a'),
    ('### no terminal is claimed by this act', BANK,
     'NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN'),
    ('### the four lists restated open in the desk`s own words', BANK,
     'THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:'),
    ('### (F1) refuted by the print', BANK, '`(F1)` REFUTED BY THE PRINT.'),
]

# ### **THE ORDER'S FIVE PROHIBITIONS, EACH AS A WHOLE LINE THE BANK MUST NOT CARRY.**
MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a document was reclassified', BANK, '### A DOCUMENT WAS RECLASSIFIED.'),
    ('the bank never says a declaration was moved', BANK, '### A DECLARATION WAS MOVED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says a terminal went unchecked', BANK,
     '### A TERMINAL WAS WRITTEN WITHOUT BEING CHECKED.'),
    ('the bank never says a not-determinable document was repaired', BANK,
     '### A NOT-DETERMINABLE DOCUMENT WAS REPAIRED.'),
    ('the bank never names a preferred option', BANK, '### THE PREFERRED OPTION IS.'),
]

# ### **`G-NOPREFER` READS THE BEARING LINES ONLY.** ### The order says the bearing lines say whether
# ### and how the role clause bears, ### **WITHOUT RECOMMENDING.**
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
    print('b377 -- GATE SUITE (THE TWO-AXIS READ)')
    print('=' * 100)
    E, LG, BR, EV, Q = (_J['E'], _J['LG'], _J['BR'], _J['EV'], _J['Q'])
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

    # ------------------------------------------------------------------- BAR 1, THE LOCK-GATE BAR
    print(chr(10) + '  G-LOCKGATE / G-EVERYGATE (BAR 1) ### THE TOOL IS b376`S, RUN AS b377:')
    lgrun = io.open(d(LG['run_file']), encoding='utf-8', errors='replace').read()
    l1 = LG['fixture_ok'] is True and LG['permits'] is True
    l2 = LG['gates_read'] == LG['gates_passing'] == 7
    l3 = all(g['passed'] for g in LG['gates'])
    l4 = ('GATES READ : %d. ### PASSING : %d. ### VERDICT : LOCK PERMITTED'
          % (LG['gates_read'], LG['gates_passing'])) in gate_text.flat(lgrun)
    l5 = 'BOTH POLARITIES HELD' in gate_text.flat(lgrun)
    l6 = LG['act'] == 'b377'
    # ### **AND THE TOOL WAS NOT REBUILT** -- the file it ran is b376's, tracked, unmodified.
    l7 = not git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'tools/b376_lockgate.py').strip()
    l8 = not os.path.exists(t('b377_lockgate.py'))
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8
    print('    gates read %d / passing %d ; all pass : %s ; act recorded : %s'
          % (LG['gates_read'], LG['gates_passing'], l3, LG['act']))
    for g in LG['gates']:
        print('      %-46s %-38s %s' % (g['gate'][:46], g['file'][:38],
                                        'PASS' if g['passed'] else '### FAIL ###'))
    print('    the run file carries the verdict : %s ; fixture both polarities : %s' % (l4, l5))
    print('    ### **AND THE LOCK GATE WAS INHERITED, NOT REBUILT** : b376 tool unmodified %s ; '
          'no b377 copy exists %s' % (l7, l8))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LOCKGATE/G-EVERYGATE')

    # ------------------------------------------------ BAR 2, THE APPEND-ONLY BAR / G-NOWRITE / G-NOMOVE
    print(chr(10) + '  G-APPEND / G-PREFIX / G-NOMOVE (BAR 2):')
    written = [r['file'] for r in BR['six'] if r['arm'] == 1]
    pref, moved = [], []
    for rel in written:
        path = os.path.join(PP, rel.replace('/', os.sep))
        cur = io.open(path, encoding='utf-8', newline='').read()
        blob = blob_of(PP, rel)
        if blob is None or not norm(cur).startswith(norm(blob).rstrip(chr(10))):
            pref.append(rel)
    # ### **AND NO DECLARATION MOVED, IN ALL EIGHT DOCUMENTS THIS ACT LOOKED AT** -- the class line
    # ### each of them declares must still be byte-identical to its blob's.
    DECL = '**DOCUMENT CLASS'
    for rel in (BR['six'] + [x['file'] for x in BR['not_determinable']]):
        rel = rel['file'] if isinstance(rel, dict) else rel
        path = os.path.join(PP, rel.replace('/', os.sep))
        cur = [x for x in io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
               if x.startswith(DECL)]
        blob = blob_of(PP, rel) or ''
        old = [x for x in blob.replace(chr(13), '').split(chr(10)) if x.startswith(DECL)]
        if cur != old:
            moved.append(rel)
    a1 = not pref
    a2 = not moved
    # ### **AND EVERY ROSTERED REPOSITORY AGAINST ITS BLOBS.**
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': set(['OPEN_TRAILS.md']) | set(written), 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b377' not in x and x != 'tools/banked_index.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    a3 = all(not v for v in dirtyrepo.values())
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    a4 = not frozen
    ga = a1 and a2 and a3 and a4
    print('    documents written into : %d %s' % (len(written), written))
    print('    ### **THE COMMITTED BLOB IS A TRUE PREFIX OF EVERY ONE** : %s %s' % (a1, pref or ''))
    print('    ### **NO DECLARATION MOVED IN ANY OF THE EIGHT** : %s %s' % (a2, moved or ''))
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    frozen paths changed : %s' % (frozen or 'none'))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-APPEND/G-PREFIX/G-NOMOVE/G-NOWRITE')

    # --------------------------------------------------------- BAR 3 AND BAR 4, TERMINALS AND PINS
    print(chr(10) + '  G-TERMINAL / G-CHECKED / G-PIN / G-OWNPIN (BAR 3, BAR 4):')
    unchecked, ambig, badpin = [], [], []
    for r in BR['six']:
        for row in r['rows']:
            if row['terminal'] not in r['located']:
                unchecked.append((r['file'], row['terminal']))
            if len(r['located_kernels'].get(row['terminal'], [])) != 1:
                ambig.append((r['file'], row['terminal']))
            # ### **THE PIN MUST BE THIS ACT'S OWN READING OF THAT KERNEL'S HEAD**, re-read here.
            live = git(os.path.join('D:', os.sep, row['kernel']), 'rev-parse', 'HEAD').strip()
            if row['pin'] != BR['pins'].get(row['kernel']) or row['pin'] != live:
                badpin.append((r['file'], row['terminal'], row['pin'][:12], live[:12]))
    b1 = not unchecked
    b2 = not ambig
    b3 = not badpin
    # ### **AND EVERY PIN WRITTEN IS RECORDED IN THIS ACT'S BANK.**
    b4 = all(pin in bank for pin in BR['pins'].values())
    gb = b1 and b2 and b3 and b4
    print('    ### **TERMINALS WRITTEN THAT WERE NOT LOCATED AND CHECKED : %d** %s'
          % (len(unchecked), unchecked or ''))
    print('    ### **TERMINALS WRITTEN THAT RESOLVE TO MORE THAN ONE KERNEL : %d** %s'
          % (len(ambig), ambig or ''))
    print('    ### **PINS THAT ARE NOT THIS ACT`S OWN READING OF THAT KERNEL`S LIVE HEAD : %d** %s'
          % (len(badpin), badpin or ''))
    print('    every pin written is recorded in the bank : %s' % b4)
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-TERMINAL/G-CHECKED/G-PIN/G-OWNPIN')

    # ------------------------------------------------------------------------ BAR 5, THE BRANCH BAR
    print(chr(10) + '  G-BRANCH / G-EVIDENCE (BAR 5):')
    c1 = all(r['arm'] in (1, 2) for r in BR['six'])
    c2 = len(BR['six']) == 6
    c3 = all(r['why'] for r in BR['six'])
    # ### **THE BRANCH WAS APPLIED, NOT CHOSEN:** ### arm 1 iff located and nothing unresolved.
    c4 = all((r['arm'] == 1) == (bool(r['located']) and not r['not_resolved']) for r in BR['six'])
    # ### **AND EVERY DOCUMENT'S DECIDING EVIDENCE IS PRINTED IN THE BANK.**
    c5 = all(os.path.basename(r['file'])[:-3] in bank for r in BR['six'])
    gc = c1 and c2 and c3 and c4 and c5
    print('    every document takes exactly one arm : %s ; population is 6 : %s' % (c1, c2))
    print('    every arm carries its why : %s' % c3)
    print('    ### **ARM 1 IFF LOCATED AND NOTHING UNRESOLVED -- THE BRANCH APPLIED, NOT CHOSEN** : %s'
          % c4)
    print('    every document named in the bank : %s' % c5)
    print('    arm 1 : %d ; arm 2 : %d' % (BR['arm1'], BR['arm2']))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-BRANCH/G-EVIDENCE')

    # ---------------------------------------------------------- BAR 6, THE NOT-DETERMINABLE BAR
    print(chr(10) + '  G-NOTDET / G-NOTREPAIRED (BAR 6):')
    ND = BR['not_determinable']
    n1 = len(ND) == 2
    n2 = all(r['repaired'] is False for r in ND)
    n3 = all(r['routed_as_lacking'] is False for r in ND)
    n4 = all(r['counted_among_the_six'] is False for r in ND)
    n5 = all(r['file'] not in [x['file'] for x in BR['six']] for r in ND)
    n6 = all(r['could_not_decide'] and r['what_would_decide'] for r in ND)
    # ### **AND NEITHER WAS WRITTEN INTO** -- their working copies match their blobs exactly.
    n7 = True
    for r in ND:
        cur = io.open(os.path.join(PP, r['file'].replace('/', os.sep)),
                      encoding='utf-8', newline='').read()
        blob = blob_of(PP, r['file'])
        if blob is None or norm(cur).rstrip(chr(10)) != norm(blob).rstrip(chr(10)):
            n7 = False
    gnd = n1 and n2 and n3 and n4 and n5 and n6 and n7
    print('    not-determinable documents reported : %d' % len(ND))
    print('    repaired : %s ; routed as lacking : %s ; counted among the six : %s'
          % (not n2, not n3, not n4))
    print('    ### **AND NEITHER FILE WAS WRITTEN INTO AT ALL** : %s' % n7)
    print('    each states what could not be decided and what would decide it : %s' % n6)
    print('    %s' % ('PASS' if gnd else '### FAIL ###'))
    if not gnd:
        fails.append('G-NOTDET/G-NOTREPAIRED')

    # ----------------------------------------------------------------- BAR 7, THE QUOTATION BAR
    print(chr(10) + '  G-ROLECLAUSE / G-OBLIGATION / G-OPTIONS (BAR 7):')
    ferrylines = io.open(FERRY, encoding='utf-8', errors='replace').read().split(chr(10))
    q1 = all(c['text'] == ferrylines[c['line'] - 1] for c in EV['role_clause'])
    q2 = len(EV['options']) == 5
    b376bank = io.open(d('b376_the_two_axis_read.txt'), encoding='utf-8',
                       errors='replace').read()
    q3 = all(o['text'] and o['text'].split(chr(10))[0] in b376bank for o in EV['options'])
    q4 = all(o['lines'] > 3 for o in EV['options'])
    taxt = io.open(TAX, encoding='utf-8', errors='replace').read()
    q5 = 'grade · terminal · pin' in taxt and 'grade . terminal . pin' in gate_text.flat(bank)
    gq = q1 and q2 and q3 and q4 and q5
    print('    the role clause re-reads out of the ferry at its own lines : %s' % q1)
    print('    options reproduced : %d ; each found in b376`s bank : %s' % (len(EV['options']), q3))
    print('    ### **EACH QUOTED WHOLE, NOT TRUNCATED TO A HEADLINE** : %s (min %d lines)'
          % (q4, min(o['lines'] for o in EV['options'])))
    print('    the taxonomy`s obligation is quoted and carried into the bank : %s' % q5)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-ROLECLAUSE/G-OBLIGATION/G-OPTIONS')

    # ------------------------------------------------------------------ BAR 8, THE NO-RULING BAR
    print(chr(10) + '  G-NOPREFER / G-NORULING (BAR 8):')
    region = chr(10).join(o['bearing'] for o in EV['options'])
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append((m.group(0), region[max(0, m.start() - 60):m.end() + 20]))
    print('    ### raw preference-word hits in the bearing lines : %s' % (sorted(set(raw)) or 'none'))
    for _wd, _ctx in live:
        print('        ### ### **LIVE: %s** | %s' % (_wd, _ctx.replace(chr(10), ' ')))
    r1 = not live
    r2 = Q['lists_closed'] == 0 and Q['closed'] == 0
    r3 = 'NONE RECOMMENDED, NONE RANKED' in gate_text.flat(bank)
    r4 = EV['filing_census']['repaired'] is False and EV['filing_census']['opened'] is False
    r5 = EV['filing_clusters']['opened'] is False
    r6 = EV['floor']['remeasured'] is False and bool(EV['floor']['wider_question'])
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    live preference words : %d ; lists closed : %d' % (len(live), Q['lists_closed']))
    print('    the bank says none is recommended : %s' % r3)
    print('    ### **BOTH FILINGS FILED AND NEITHER OPENED** : census %s / clusters %s' % (r4, r5))
    print('    ### **THE FLOOR IS NOT RE-MEASURED AND THE WIDER QUESTION IS NAMED** : %s' % r6)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-NOPREFER/G-NORULING/G-FLOOR/G-WIDER')

    # --------------------------------------------------------- G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-OPEN / G-NONEWDOC:')
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    k1 = all(x in bank for x in lists)
    k2 = 'ARE RESTATED `OPEN` BY NAME' in bank
    k3 = 'OPEN BY NAME' in gate_text.flat(tblk)
    k4 = Q['lists_closed'] == 0
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    k5 = not newdocs
    gk = k1 and k2 and k3 and k4 and k5
    print('    the four lists are named in the bank in the desk`s words : %s' % k1)
    print('    restated OPEN in the bank : %s ; in the trail block : %s' % (k2, k3))
    print('    lists closed : %d ; desk items closed : %d' % (Q['lists_closed'], Q['closed']))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (k5, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-OPEN/G-NONEWDOC')

    # ------------------------------------------------------------------ G-TRAIL / G-ROW / G-KEY
    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE PIN WAS THE MISSING ELEMENT' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = 'the-pin-was-missing returns 1 row(s)' in irun and Q['key_ok'] is True
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the declarations are moved',
              'the lists are closed', 'the census is repaired'))
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
    relied = (BR, EV, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND `b375`'S DEFECTIVE FACE MUST STILL VERIFY, UNEDITED.**
    R375 = d('b375_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    # ### **AND THE TWO PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b376_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b376`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b375`S DEFECTIVE FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b377_hooks.txt'), d('b377_mirror.txt')
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
    A1 = [r for r in BR['six'] if r['arm'] == 1]
    A2 = [r for r in BR['six'] if r['arm'] == 2]
    NROWS = sum(len(r['rows']) for r in A1)
    checks = [
        ('gates read %d' % LG['gates_read'], str(LG['gates_read']) in bank),
        ('arm 1 %d' % len(A1), str(len(A1)) in bank),
        ('arm 2 %d' % len(A2), str(len(A2)) in bank),
        ('rows appended %d' % NROWS, str(NROWS) in bank),
        ('kernels enumerated %d' % BR['kernels'], str(BR['kernels']) in bank),
        ('pins written %d' % len(BR['pins']), all(v in bank for v in BR['pins'].values())),
        ('census detector %d' % EV['filing_census']['detector'],
         str(EV['filing_census']['detector']) in bank),
        ('census published %d' % EV['filing_census']['published'],
         str(EV['filing_census']['published']) in bank),
        ('census re-applied %d' % EV['filing_census']['reapplied'],
         str(EV['filing_census']['reapplied']) in bank),
        ('clusters with no keystone %d' % EV['filing_clusters']['count'],
         str(EV['filing_clusters']['count']) in bank),
        ('the floor %d of %d' % (EV['floor']['banked'], EV['floor']['of']),
         str(EV['floor']['banked']) in bank and str(EV['floor']['of']) in bank),
        ('options quoted %d' % len(EV['options']), len(EV['options']) == 5),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on branch run', BR['run_file'] in bank),
        ('the relied-on evidence run', EV['run_file'] in bank),
        ('the relied-on lock-gate run', LG['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('branch', BR),
                    ('evidence', EV), ('desk', Q)):
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
                          if x.startswith('b377_') and x.endswith('.py')))
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
              if x.strip() and 'b377' not in x and x.strip() != 'tools/banked_index.py']
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
             d('b377_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b377_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(BR['run_file']), "the branch run carries the documents' own identifiers"),
        (d(EV['run_file']), "the evidence run carries the author's clause and b376's options"),
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

    marker = '# ### THE UNBLOCKED OBLIGATION (b377).'
    nxt = '# ### THE TWO-AXIS READ (b376).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b377_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT EIGHT NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 8 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b377_hedge_')
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
