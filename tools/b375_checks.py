# -*- coding: utf-8 -*-
"""b375_checks.py -- THE GATE SUITE FOR THE KEYSTONE AND CLUSTER CENSUS.

### ### **THE CENSUS'S TWO CAPS ARE SENTENCES UNTIL MEASURED:** ### *nothing written into what it
### read* and *no class conferred on a document that declares its own*. ### `G-NOWRITE` compares every
### rostered repository against its blobs; `G-DECLARED` re-reads every declared class line out of its
### own document and compares it byte-for-byte with what the census banked.
### ### **AND `G-ORDER` VERIFIES BOTH LOCKS** -- the re-issued face that governs, and the first face,
### which is left on the record with its seal intact and must still verify.
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
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402
import b303_pins           # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-effects')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b375_the_keystone_and_cluster_census.txt')
REG = d('b375_registration_2026-09-08_reissued.txt')
REG1 = d('b375_registration_2026-09-08.txt')
FERRY = d('b375_ferry_2026-09-08.txt')
IDX = d('b375_desk_notes.txt')
SCAN, TERMSCAN, GATE = d('b375_ferry_scan.txt'), d('b375_reg_termscan.txt'), d('b375_reg_gate.txt')
CENSUS0, FCEN = d('b375_census_stepzero.txt'), d('b375_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b375_regspec_run.txt'), d('audit_b375_reg_satisfiable.txt')
PINS0 = d('b375_pins_stepzero.txt')
SEAL = '73589d06544449c00a4d5bc5bf078d557c4125503fbe4b376b31f4a8db91f1da'
SEAL1 = '472debac8cbcab2b86061d884c528a563ce0206b5e8d8855ed73fc26e1e060c3'
ROWNUM = '224'
TRAIL_MARK = '<!-- b375 the keystone and cluster census; three tests, one word -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b375_reads.json'), ('P', 'b375_population.json'),
                   ('CL', 'b375_clusters.json'), ('IN', 'b375_integration.json'),
                   ('RB', 'b375_rubric.json'), ('Q', 'b375_desk.json'))}

NEW_THIS_ACT = {'tools/b375_regspec.py', 'tools/b375_extract.py', 'tools/b375_reg_gate.py',
                'tools/b375_population.py', 'tools/b375_clusters.py', 'tools/b375_integration.py',
                'tools/b375_rubric.py', 'tools/b375_desk.py', 'tools/b375_bank.py',
                'tools/b375_checks.py'}

TOOLNUM = [
    ('the population, three columns never merged', 'tools/b375_population.py'),
    ('the clusters, from the documents and the registry', 'tools/b375_clusters.py'),
    ('the integration state, four columns never averaged', 'tools/b375_integration.py'),
    ("b374's audit, run unmodified, with its control", 'tools/b375_rubric.py'),
    ('(R7), the trail block, the row and the key', 'tools/b375_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b375_bank.py'),
    ('the reads', 'tools/b375_extract.py'),
    ('the three-arm registration gate', 'tools/b375_reg_gate.py'),
    ('the clause spec', 'tools/b375_regspec.py'),
    ('22675 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('THE INSTRUMENT, IMPORTED AND UNTOUCHED', 'tools/hedge_audit.py'),
    ("b374's measurement, imported and untouched", 'tools/b374_hedge.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
KCENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b375 - THE KEYSTONE AND CLUSTER CENSUS. Number not claimed'),
    ('the order -- the scope', FERRY,
     'SCOPE: READS and CLASSIFICATION only. NO document repaired, NO'),
    ('the order -- no class conferred on a declarer', FERRY,
     'class conferred on a document that declares its own, NO'),
    ('the order -- the rubric, keystones', FERRY,
     'questions and working notes. KEYSTONES synthesize a cluster'),
    ('the order -- component 1', FERRY,
     'COMPONENT 1 - THE POPULATION, read from content and never from'),
    ('the order -- component 2', FERRY,
     'COMPONENT 2 - THE CLUSTERS: enumerate the subject clusters the'),
    ('the order -- unassigned rather than resemblance', FERRY,
     'cannot be identified from its own text is reported UNASSIGNED'),
    ('the order -- component 3', FERRY,
     'COMPONENT 3 - THE INTEGRATION STATE, four columns kept apart'),
    ('the order -- not determinable', FERRY,
     'own text, it reads NOT DETERMINABLE FROM THE DOCUMENT and the'),
    ('the order -- component 4', FERRY,
     'COMPONENT 4 - THE RUBRIC APPLIED, measured not opined: for each'),
    ('the order -- component 5', FERRY,
     'COMPONENT 5 - WHAT THE CENSUS DOES NOT KNOW, stated plainly:'),
    ('the order -- no new tracking document', FERRY,
     'for where it should live - the census does not create a new'),
    ("the order -- the navigator's expectations", FERRY,
     "The navigator's expectations, registered here: (F1) fewer than"),
    ("the taxonomy -- Tier K, certified at a pin", TAX, '**Tier K — Keystone-certified.**'),
    ('the taxonomy -- Tier C, cluster-synthesis', TAX, '**Tier C — Cluster-synthesis.**'),
    ("the existing census -- its own class test", KCENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
]

SELF_NEEDLES = [
    ('the bank leads with the three tests', BANK,
     'THE WORD `KEYSTONE` NAMES THREE DIFFERENT TESTS IN THIS RECORD, AND THEY DO NOT'),
    ('### which governs is a ruling', BANK, 'WHICH GOVERNS IS A RULING AND NOT A READ.'),
    ('### the same instrument, opposite answers', BANK,
     'DEFINITIONS ONE ACT APART, GIVES OPPOSITE ANSWERS.'),
    ('### a measurement of a layer is of its definition', BANK,
     'DEFINITION OF THAT LAYER YOU USED**, and this bank reports both rather than choosing.'),
    ('### reported and not conferred', BANK,
     'TIERS`.** ### Most carry no tier line. ### **THAT IS REPORTED AND NOT CONFERRED**'),
    ('### NOT PLACED is a declaration', BANK,
     'AND `NOT PLACED` IS A DECLARATION**, not a blank'),
    ('### no document defaulted to SUPPORT', BANK,
     'HAVE MANUFACTURED THE CENSUS`S OWN ANSWER.'),
    ('### a cluster with no keystone is a finding', BANK,
     'A CLUSTER WITH NO KEYSTONE IS A FINDING AND IS REPORTED AS ONE'),
    ('### column (d) by anchor, never summarized', BANK,
     'NEVER SUMMARIZED** -- the order`s own words.'),
    ('### no document pronounced to fail', BANK,
     'AND NO DOCUMENT IS PRONOUNCED TO FAIL THE RUBRIC.'),
    ('### the census does not know, item one', BANK,
     'WHICH OF THE THREE TESTS FOR `KEYSTONE` GOVERNS.'),
    ('### the read this act refused', BANK, 'A READ,'),
    ('### closing nothing is right for an orientation', BANK,
     'CLOSING NOTHING IS THE RIGHT ANSWER FOR AN ORIENTATION AND IS SAID RATHER THAN'),
    ('### (F1) splits three ways', BANK, 'IT SPLITS'),
    ('### the incident filed against itself', BANK,
     'THE FIRST REGISTRATION WAS LOCKED OVER A FACE CARRYING A LIVE STRUCK-STEM USE.'),
    # ### the phrase occurs twice in the bank -- once in the incident, once in the species list --
    # ### and the anchor tool REFUSED it, which is the tool working. ### The hint is lengthened.
    ('### a gate nobody reads is not a gate', BANK,
     'A GATE NOBODY READS IS NOT A GATE`**, which is this record`s own lesson'),
]

MUST_FAIL = [
    ('the bank never says a document was reclassified', BANK, '### A DOCUMENT WAS RECLASSIFIED.'),
    ('the bank never says a declared class was overwritten', BANK,
     '### A DECLARED CLASS WAS OVERWRITTEN.'),
    ('the bank never says a cluster was assigned by resemblance', BANK,
     '### A CLUSTER WAS ASSIGNED BY RESEMBLANCE.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says a document fails the rubric', BANK, '### A DOCUMENT FAILS THE RUBRIC.'),
]


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
    print('b375 -- GATE SUITE (THE KEYSTONE AND CLUSTER CENSUS)')
    print('=' * 100)
    E, P, CL, IN, RB, Q = (_J['E'], _J['P'], _J['CL'], _J['IN'], _J['RB'], _J['Q'])
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
    print(chr(10) + '  MUST-FAIL FIXTURES:')
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

    print(chr(10) + '  G-NOWRITE (BAR 1) ### EVERY ROSTERED REPOSITORY AGAINST ITS BLOBS:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirty = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b375' not in x and x != 'tools/banked_index.py')
        dirty[name] = sorted(x for x in ch if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    n1 = all(not v for v in dirty.values())
    frozen = [x for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and (x.startswith('outputs/') or x.startswith('archive/'))]
    n2 = not frozen
    gn = n1 and n2
    print('    tracked paths changed beyond the declared set : %s' % dirty)
    print('    ### **FROZEN PATHS CHANGED : %s**' % (frozen or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOWRITE')

    print(chr(10) + '  G-DECLARED / G-NOTRANSLATE (BAR 2) ### EVERY CLASS LINE RE-READ FROM ITS DOC:')
    bad = []
    for r in P['rows']:
        if not r['declared_line']:
            continue
        p = os.path.join(PP, r['file'].replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            bad.append((r['file'], 'unreadable'))
            continue
        if r['declared_line'] not in txt:
            bad.append((r['file'], 'the banked class line is not in the document'))
    d1 = not bad
    d2 = P['translated'] == 0 and P['reclassified'] == 0
    # ### **A DECLARED TIER MUST NEVER APPEAR AS THE ORDER'S CLASS FOR THAT ROW.**
    d3 = all(r['order_class'] in ('KEYSTONE', 'SUPPORT', 'LEDGER', 'OTHER') for r in P['rows'])
    d4 = all(not (r['declared_tier'] == 'NOT PLACED' and r['order_class'] == 'KEYSTONE')
             for r in P['rows'])
    gd = d1 and d2 and d3
    print('    every banked class line re-read out of its own document : %s %s' % (d1, bad[:2] or ''))
    print('    translations : %d ; reclassifications : %d' % (P['translated'], P['reclassified']))
    print("    ### **AND EVERY ROW'S ORDER CLASS IS ONE OF THE FOUR RULED WORDS** : %s" % d3)
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DECLARED/G-NOTRANSLATE')

    print(chr(10) + '  G-FOURWORD / G-EVIDENCE / G-NOTPATH (BAR 3, BAR 4):')
    f1 = d3
    f2 = all(r['deciding_sentence'] or r['order_class'] == 'OTHER' for r in P['rows'])
    # ### every READ verdict must quote a sentence located in the document
    miss = []
    for r in P['rows'][:400]:
        if not r['deciding_sentence']:
            continue
        p = os.path.join(PP, r['file'].replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        if r['deciding_sentence'][:50] not in txt:
            miss.append(r['file'])
    f3 = not miss
    src = strip_prose(t('b375_population.py'))
    f4 = 'clusters/' not in src and 'phase1.5/' not in src
    gf = f1 and f2 and f3 and f4
    print('    only the four ruled words : %s ; every non-OTHER row quotes a sentence : %s' % (f1, f2))
    print('    ### **EVERY QUOTED SENTENCE RE-LOCATED IN ITS DOCUMENT** : %s %s' % (f3, miss[:2] or ''))
    print('    ### **AND THE CLASSIFIER NAMES NO DIRECTORY IN ITS STRIPPED CODE** : %s' % f4)
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FOURWORD/G-EVIDENCE/G-NOTPATH')

    print(chr(10) + '  G-DISAGREE / G-CLUSTER / G-UNASSIGNED / G-NOKEYSTONE:')
    c1 = len(P['disagreements']) >= 0 and 'REPORTED AT FULL PROMINENCE' in bf.upper()
    c2 = CL['enumerated_from_directories'] == 0 and CL['assigned_by_resemblance'] == 0
    c3 = isinstance(CL['unassigned'], list)
    c4 = len(CL['subject_clusters_without_keystone']) >= 0
    c5 = 'A CLUSTER WITH NO KEYSTONE IS A FINDING' in bf
    gc = c1 and c2 and c3 and c5
    print('    directory-vs-content disagreements reported : %s (%d)' % (c1, len(P['disagreements'])))
    print('    enumerated from directories : %d ; assigned by resemblance : %d'
          % (CL['enumerated_from_directories'], CL['assigned_by_resemblance']))
    print('    ### **UNASSIGNED KEYSTONES ARE LISTED, NOT ASSIGNED** : %s (%d)'
          % (c3, len(CL['unassigned'])))
    print('    a cluster with no keystone is called a finding : %s' % c5)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-DISAGREE/G-CLUSTER/G-UNASSIGNED/G-NOKEYSTONE')

    print(chr(10) + '  G-COLUMNS / G-ANCHORED / G-NOTDETERMINABLE / G-NOCHECK (BAR 5):')
    i1 = IN['averaged_statuses'] == 0 and IN['kernels_opened'] == 0 and IN['cells_inferred'] == 0
    i2 = all(isinstance(x['d'], list) for x in IN['rows'])
    i3 = all(all(('file' in an and 'line' in an) for an in x['d']) for x in IN['rows'])
    i4 = all(x['a_state'] in ('read', 'NOT DETERMINABLE FROM THE DOCUMENT') for x in IN['rows'])
    isrc = strip_prose(t('b375_integration.py'))
    i5 = 'rev-parse' not in isrc and 'ls-tree' not in isrc
    gi = i1 and i2 and i3 and i4 and i5
    print('    averaged statuses %d ; kernels opened %d ; cells inferred %d'
          % (IN['averaged_statuses'], IN['kernels_opened'], IN['cells_inferred']))
    print('    ### **EVERY COLUMN (d) ENTRY IS A FILE AND A LINE, NOT A SUMMARY** : %s' % i3)
    print('    ### **AND THE INTEGRATION READER RESOLVES NO REF AND OPENS NO KERNEL** : %s' % i5)
    print('    %s' % ('PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-COLUMNS/G-ANCHORED/G-NOTDETERMINABLE/G-NOCHECK')

    print(chr(10) + '  G-UNMODIFIED / G-CONTROL / G-NOOPINE (BAR 6):')
    hb = blob_of(ROOT, 'tools/hedge_audit.py')
    hw = io.open(t('hedge_audit.py'), encoding='utf-8', errors='replace').read()
    u1 = hb is not None and norm(hb) == norm(hw)
    u2 = RB['instrument_selftest'] is True
    u3 = 'SUPPORT' in RB['totals'] and RB['totals']['SUPPORT']['docs'] > 0
    u4 = RB['pronouncements'] == 0 and RB['documents_repaired'] == 0
    u5 = 'NO DOCUMENT IS PRONOUNCED TO FAIL THE RUBRIC' in bf
    gu = u1 and u2 and u3 and u4 and u5
    print('    the instrument is byte-identical to its blob : %s ; its fixtures pass : %s' % (u1, u2))
    print('    ### **THE CONTROL POPULATION IS MEASURED** : %s (%d documents)'
          % (u3, RB['totals']['SUPPORT']['docs']))
    print('    pronouncements %d ; documents repaired %d ; and the bank says so : %s'
          % (RB['pronouncements'], RB['documents_repaired'], u5))
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNMODIFIED/G-CONTROL/G-NOOPINE')

    print(chr(10) + '  G-DOESNOTKNOW / G-OPEN / G-NONEWDOC (BAR 7):')
    k1 = 'WHAT THE CENSUS DOES NOT KNOW' in bf
    k2 = all(x in bf for x in ('A RULING.', 'A KERNEL CHECK.'))
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    k3 = all(x in tblk for x in ('LIST 1', 'LIST 2', 'LIST 3', 'LIST 4')) or \
        all(x.split(' -- ')[0][:30] in tblk for x in lists)
    k3 = k3 and 'OPEN.' in tblk
    k4 = Q['lists_closed'] == 0 and Q['closed'] == 0
    # ### ### **THE ARM ASKS WHETHER *THIS ACT* CREATED A TRACKING DOCUMENT, NOT WHETHER THE TREE IS
    # ### ### CLEAN OF EVERY UNTRACKED FILE.** ### `internal/BLOB_SENSITIVITY_2026-08-29.md` has sat
    # ### untracked since before this act and `b371`'s suite already excluded it by name; counting it
    # ### here would fail this act for somebody else's file. ### **AN ARM THAT FAILS ON A PRE-EXISTING
    # ### ### CONDITION IS NOT MEASURING THE ACT.**
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??')
               and not any(pe in x for pe in PREEXISTING)]
    k5 = not newdocs
    gk = k1 and k2 and k3 and k4 and k5
    print('    the census names what it does not know : %s ; with rulings and a kernel check : %s'
          % (k1, k2))
    print('    ### **THE FOUR LISTS ARE RESTATED OPEN IN THE TRAIL BLOCK** : %s' % k3)
    print('    lists closed : %d ; desk items closed : %d' % (Q['lists_closed'], Q['closed']))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (k5, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-DOESNOTKNOW/G-OPEN/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THREE TESTS, ONE WORD' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = 'three-tests-one-word returns 1 row(s)' in irun and Q['key_ok'] is True
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the classes are conferred', 'the clusters are repaired', 'the lists are closed',
              'the keystone test is ruled'))
    gt = t1 and t2 and t3 and t4 and t5
    print('    trail: mark once and append-only : %s ; blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL/G-ROW/G-KEY')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT ### BOTH LOCKS VERIFIED:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    vr1 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG1], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o2 = ('SEAL INTACT' in (vr1.stdout or ''))
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (P, CL, IN, RB, Q))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    o8 = 'RE-ISSUE' in gate_text.flat(reg)
    go2 = o1 and o2 and stampm and o3 and o4 and o5 and o6 and o7 and o8
    print('    the governing lock recomputes : %s' % o1)
    print('    ### **AND THE FIRST FACE STILL VERIFIES, UN-EDITED** : %s' % o2)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND THE FACE DECLARES ITSELF A RE-ISSUE** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b375_hooks.txt'), d('b375_mirror.txt')
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

    print(chr(10) + '  G-NUMBERS:')
    checks = [
        ('documents %d' % P['documents'], ('`%d` TRACKED' % P['documents']) in bf),
        ('declared %d' % P['declared'], ('`%d` DECLARING' % P['declared']) in bf),
        ('taxonomy tier K %d' % len(P['tests']['taxonomy_tier_k']),
         str(len(P['tests']['taxonomy_tier_k'])) in bank),
        ('order rubric %d' % len(P['tests']['order_rubric']),
         str(len(P['tests']['order_rubric'])) in bank),
        ('all three %d' % len(P['tests']['all_three']),
         ('`%d` DOCUMENTS ARE IN ALL THREE' % len(P['tests']['all_three'])) in bf),
        ('clusters without keystone %d' % len(CL['subject_clusters_without_keystone']),
         str(len(CL['subject_clusters_without_keystone'])) in bank),
        ('column d %d' % IN['d_nonempty'], str(IN['d_nonempty']) in bank),
        ('keystone hedge/k %.1f' % RB['totals']['KEYSTONE']['per_k'],
         ('`%.1f`' % RB['totals']['KEYSTONE']['per_k']) in bank),
        ('desk items %d' % Q['items'], ('`%d` SWEPT' % Q['items']) in bf),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the governing lock hash', SEAL in bank),
        ('the first lock hash', SEAL1 in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on population run', P['run_file'] in bank),
        ('the relied-on rubric run', RB['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('population', P), ('clusters', CL), ('integration', IN),
                    ('rubric', RB), ('desk', Q)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-12s %-30s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                              jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b375_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits), hits or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

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
                'a bounded sample': 'a slice of a list THIS ACT built in memory, not an address.'}

    def which(code):
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
             'tools/b374_hedge.py', 'tools/git-hooks/pre-push']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b375' not in x and x.strip() != 'tools/banked_index.py']
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b375_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b375_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (REG1, "THE FIRST FACE, LEFT ON THE RECORD WITH ITS SEAL INTACT AND ITS DEFECT NAMED"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(P['run_file']), "the population run carries the documents' own class lines"),
        (d(CL['run_file']), "the clusters run carries the registry's own headings"),
        (d(IN['run_file']), "the integration run carries the documents' own sentences"),
        (d(RB['run_file']), "the rubric run carries the documents' own sentences"),
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

    marker = '# ### THE KEYSTONE AND CLUSTER CENSUS (b375).'
    nxt = '# ### THE DESCRIPTIVE LAYER MEASURED, AND THE FUNCTIONAL EQUATION FILED (b374).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b375_stem_'), 'blk.txt')
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

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b375_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
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
