# -*- coding: utf-8 -*-
"""b385_checks.py -- THE GATE SUITE FOR THE SIX, THE RULE AND THE THREE.

### ### **THE ARM THAT MATTERS MOST HERE IS `G-REFUTED`.** ### This act contradicts a prior act's
### reported absence. ### An act that quietly replaces a wrong finding with a right one has ###
### **HIDDEN THE ERROR INSIDE THE CORRECTION**, so the arm requires `b383`'s claim to be NAMED as
### refuted, ### **WITH ITS REASON**, in this act's own bank.
###
### ### **AND `G-REREAD` CARRIES A LICENCE THAT IS NOT A SOFTENING.** ### One quoted line was
### repaired by this act under `(R4)` -- preserve by quotation, repair by edit -- so ### **IT
### ### CANNOT RE-READ, BY CONSTRUCTION.** ### The arm therefore requires `reread_failures` to be
### EMPTY and the repaired line to be reported in its own count; ### **IT DOES NOT ACCEPT A
### ### FAILURE RE-LABELLED AS A REPAIR**, because the repaired set is bounded at one and its
### file and line are named.
###
### ### **`G-ENTRIES` READS THE LEDGER AND NOT THE COMPONENT RECORD.** ### The order says the six
### are entered THROUGH THE TRAILS WRITER, so an arm that reads the JSON would pass on an act that
### computed six entries and wrote none.
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`); ### **AN ABSENCE NEEDS A PROVED SEARCH** (`b378`); ### **A RUN FILE IS
### ### RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
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
GUARD = os.path.join(ROOT, '.githooks', 'pre-push')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b385_the_six_on_the_trails.txt')
REG = d('b385_registration_2026-09-09.txt')
FERRY = d('b385_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b385_ferry_scan.txt'), d('b385_reg_termscan.txt'), d('b385_reg_gate.txt')
CENSUS0, FCEN = d('b385_census_stepzero.txt'), d('b385_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b385_regspec_run.txt'), d('audit_b385_reg_satisfiable.txt')
PINS0 = d('b385_pins_stepzero.txt')
SEAL = 'df3c2b776b1caeeb1a70472611dd35f3bb650d8140df70829713f34902ca936d'
ROWNUM = '234'
TRAIL_MARK = '<!-- b385 the six on the trails; the rule found; the three done -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b385_components.json'), ('LG', 'b385_lockgate.json'),
                   ('E', 'b385_reads.json'), ('Q', 'b385_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b385_regspec.py', 'tools/b385_reg_gate.py', 'tools/b385_extract.py',
                'tools/b385_components.py', 'tools/b385_desk_bank.py', 'tools/b385_checks.py'}

TOOLNUM = [
    ('the extract, and every anchor read from its file', 'tools/b385_extract.py'),
    ('the four components, and the (R4) repair inside one', 'tools/b385_components.py'),
    ('(R7), the three closing writes and the bank', 'tools/b385_desk_bank.py'),
    ('the registration gate', 'tools/b385_reg_gate.py'),
    ('the clause spec', 'tools/b385_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
    ('the cluster census this act entered on the trails', 'tools/b375_clusters.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b385 - THE SIX ON THE TRAILS, THE RULE FOUND OR ABSENT, AND'),
    ('the order -- component 1, the clusters on the trails ledger', FERRY,
     'COMPONENT 1 - THE NOT-YET-SYNTHESIZED CLUSTERS, entered on the'),
    ('the order -- component 2, the reservoir rule found or absent', FERRY,
     'COMPONENT 2 - THE RESERVOIR RULE, FOUND OR ABSENT: the'),
    ('the order -- component 3, the three that wait on nothing', FERRY,
     'COMPONENT 3 - THE THREE THAT WAIT ON NOTHING, as the draft'),
    ('the order -- component 3, each done or routed, none partly', FERRY,
     'routed if they do not. Each done or routed, none partly.'),
    ('the order -- component 4, the citation question routed not answered', FERRY,
     'COMPONENT 4 - THE CITATION QUESTION, ROUTED AND NOT ANSWERED:'),
    ('the order -- component 4, recommend nothing', FERRY,
     'failure the tiers exist to prevent quoted beside them. Recommend'),
    ('the order -- (F1), the rule is located and the paraphrase over-stated', FERRY,
     'expectations: (F1) the reservoir rule is LOCATED in a'),
    ('the order -- (F2), all three complete without a ruling', FERRY,
     "over-stated its scope; (F2) all three of Component 3's items"),
]

SELF_NEEDLES = [
    ('the bank leads with the refutation', BANK,
     '### ### ### CLAIM IS REFUTED BY THIS ACT -- SAID FIRST RATHER THAN FOLDED INTO A'),
    ('### the rule is LOCATED', BANK, '### COMPONENT 2 -- THE RESERVOIR RULE. ### **LOCATED.**'),
    ('### the many-to-many rule is beside every entry', BANK,
     '### ### **THE MANY-TO-MANY RULE IS STATED BESIDE EVERY ENTRY -- `6` TIMES IN THE'),
    ('### (F1) is met on both halves', BANK,
     '### ### ### **`(F1)` IS MET ON BOTH HALVES:** ### the rule is LOCATED in a'),
    ('### each done or routed, none partly', BANK,
     '### COMPONENT 3 -- THE THREE THAT WAITED ON NOTHING. ### **EACH DONE OR ROUTED,'),
    ('### the quotation cannot re-read by construction', BANK,
     '### ### ### **AND THE QUOTATION CANNOT RE-READ, BY CONSTRUCTION** -- so it is'),
    ('### confirmed by digest and content, never by filename', BANK,
     '###   ### **CONFIRMED BY DIGEST AND BY CONTENT AND ### NEVER BY FILENAME** -- the'),
    ('### my own registered expectation (E2) is refuted', BANK,
     '### ### ### **AND MY OWN REGISTERED EXPECTATION `(E2)` IS REFUTED BY MY OWN RUN:**'),
    ('### the desk carried it for twenty-five acts', BANK,
     '### ### ROSTER RULING** -- and the desk then carried the item for ### **TWENTY-FIVE'),
    ('### nothing is recommended', BANK,
     '### ### ### **NOTHING IS RECOMMENDED. ### NO OPTION IS RANKED, PREFERRED OR'),
    ('### a controlled search for the wrong string', BANK,
     '### ### ### **NEW -- `A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED`'),
    ('### a desk item without a date', BANK,
     '### ### ### **NEW -- `A DESK ITEM WITHOUT A DATE IS AN ITEM NOBODY HAS RE-READ`.**'),
    ('### a line quoted and then repaired cannot re-read', BANK,
     '### ### ### **NEW -- `A LINE QUOTED AND THEN REPAIRED CANNOT RE-READ, BY`'),
]

# ### **THE MUST-FAIL FIXTURES ARE THE LOCKED FACE`S OWN EIGHT, AS WHOLE LINES.**
MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a standard was edited', BANK, '### A STANDARD WAS EDITED.'),
    ('the bank never says a cluster is owed a keystone', BANK,
     '### A CLUSTER IS OWED A KEYSTONE.'),
    ('the bank never says an archive file was removed', BANK,
     '### AN ARCHIVE FILE WAS REMOVED.'),
    ('the bank never says the filename decided it', BANK, '### THE FILENAME DECIDED IT.'),
    ('the bank never says a quotation did not re-read', BANK,
     '### A QUOTATION DID NOT RE-READ.'),
    ('the bank never says the preferred option is', BANK, '### THE PREFERRED OPTION IS.'),
    ('the bank never says an item was partly done', BANK, '### AN ITEM WAS PARTLY DONE.'),
]

PREFER = re.compile(r'\b(recommend\w*|prefer\w*|the best option|should be adopted|we advise|'
                    r'the right choice|obviously|clearly the|the correct option|I suggest|'
                    r'likeliest|the strongest|the weakest)\b', re.I)
NEG2 = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,70}$', re.I)
MARKS = ('ACCURATE', 'NARROWED', 'OVER-STATED')
DISPOSITIONS = ('DONE', 'ROUTED', 'ALREADY DONE BY THE RECORD',
                'DONE WITH EXCEPTIONS REPORTED')


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


def live_preference(region):
    """### THE PREFERENCE SWEEP, WITH ITS DISCHARGES PRINTED. ### A hit whose own sentence NEGATES
    it (`nothing is recommended`) is ### **NOT A RECOMMENDATION**, and an arm that could not tell
    the two apart would fire on the very sentence that proves the point (`b348`)."""
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 100):m.start()]
        raw.append(m.group(0))
        if not NEG2.search(before):
            live.append((m.group(0), region[max(0, m.start() - 60):m.end() + 20].replace(
                chr(10), ' ')))
    return raw, live


def main():
    fails = []
    print('=' * 100)
    print('b385 -- GATE SUITE (THE SIX ON THE TRAILS, THE RULE FOUND, THE THREE DISPATCHED)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
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
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trails = io.open(TRAILS, encoding='utf-8', newline='').read()
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()

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
    l7 = LG['act'] == 'b385' and not os.path.exists(t('b385_lockgate.py'))
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

    # -------------------------------------------------------------------- BAR 2, THE ENTRY BAR
    print(chr(10) + '  G-ENTRIES / G-MANYTOMANY / G-NOTOPENED (BAR 2):')
    # ### ### **READ OUT OF THE LEDGER, NOT OUT OF THE JSON.** ### The order says the six are
    # ### entered THROUGH THE TRAILS WRITER; an arm reading the component record would pass an act
    # ### that computed six entries and wrote none.
    PARTS = ('Where its material sits:', 'What a synthesis would draw on:',
             'What would make it ripe:', 'The rule, beside the entry:')
    missing, per = [], {}
    for e in AC['entries']:
        head = '**`%s` —' % e['cluster']
        i = tblk.find(head)
        if i < 0:
            missing.append((e['cluster'], 'no entry in the ledger'))
            continue
        j = tblk.find('**`', i + len(head))
        blk = tblk[i:j if j > i else len(tblk)]
        gone = [p for p in PARTS if p not in blk]
        per[e['cluster']] = (len(PARTS) - len(gone), 'NOT-YET-SYNTHESIZED' in blk)
        if gone:
            missing.append((e['cluster'], 'missing %s' % gone))
        if 'NOT-YET-SYNTHESIZED' not in blk:
            missing.append((e['cluster'], 'not marked NOT-YET-SYNTHESIZED'))
    b2a = not missing
    b2b = len(AC['entries']) == AC['entries_written'] == AC['clusters_counted']
    b2c = tblk.count('a cluster may have SEVERAL keystones, ONE, or NONE YET') >= len(AC['entries'])
    b2d = AC['clusters_opened'] == 0
    b2e = Q['entries_in_ledger'] == len(AC['entries'])
    # ### **AND THE RULE`S TWO HALVES ARE BOTH THERE** -- a plurality is not an anomaly AND an
    # ### absence is not a defect. ### An entry carrying only one half would read as a deficiency.
    b2f = tblk.count('not owed and not deficient') >= len(AC['entries'])
    b2g = 'many-to-many' in tblk
    gb2 = b2a and b2b and b2c and b2d and b2e and b2f and b2g
    for c, (n, mk) in sorted(per.items()):
        print('    %-58s parts %d/4 ; marked : %s' % (c[:58], n, mk))
    print('    ### **ENTRIES IN THE LEDGER : %d of %d ; DEFECTS : %s**'
          % (Q['entries_in_ledger'], len(AC['entries']), missing or 'none'))
    print('    ### **THE MANY-TO-MANY RULE BESIDE AN ENTRY : %d TIMES ; `NOT OWED AND NOT '
          'DEFICIENT` : %d TIMES**'
          % (tblk.count('a cluster may have SEVERAL keystones, ONE, or NONE YET'),
             tblk.count('not owed and not deficient')))
    print('    ### **CLUSTERS OPENED, RANKED OR PRIORITISED : %d**' % AC['clusters_opened'])
    print('    %s' % ('PASS' if gb2 else '### FAIL ###'))
    if not gb2:
        fails.append('G-ENTRIES/G-MANYTOMANY/G-NOTOPENED')

    # ---------------------------------------------------------------- BAR 3, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-REREAD (BAR 3):')
    q1 = AC['reread_failures'] == []
    q2 = AC['reread_ok'] is True
    # ### **THE `(R4)` LICENCE IS BOUNDED AND NAMED.** ### Exactly one line, its file and its line
    # ### number recorded, and the repair itself measured -- ### **NOT A FAILURE RE-LABELLED.**
    q3 = AC['repaired_count'] == 1 and len(AC['repaired_quotations']) == 1
    q4 = AC['repair_line_present'] is True and AC['guard_repaired'] is True
    rq = AC['repaired_quotations'][0] if AC['repaired_quotations'] else [None, None, None]
    q5 = rq[1] == 'pre-push' and isinstance(rq[2], int)
    # ### **AND THE REPAIRED LINE IS THE ONE THE GUARD NOW CARRIES** -- the edit happened.
    guard = io.open(GUARD, encoding='utf-8', errors='replace').read().split(chr(10))
    q6 = (len(guard) >= rq[2] and 'core.hooksPath' in guard[rq[2] - 1]
          and '.git/hooks/pre-push' not in guard[rq[2] - 1])
    q7 = E['without_anchor'] == 0 and E['reads'] > 0
    gq = q1 and q2 and q3 and q4 and q5 and q6 and q7
    print('    ### **QUOTATIONS THAT FAILED TO RE-READ : %d**' % len(AC['reread_failures']))
    print('    ### **QUOTATIONS REPAIRED UNDER (R4) : %d** %s'
          % (AC['repaired_count'], AC['repaired_quotations']))
    print('    ### **THE REPAIRED FILE NOW CARRIES THE NEW LINE AND NOT THE OLD** : %s' % q6)
    print('    the extract: %d reads, %d without an anchor' % (E['reads'], E['without_anchor']))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-REREAD')

    # ------------------------------------------------------------------ BAR 4, THE SCORING BAR
    print(chr(10) + '  G-SCORED (BAR 4):')
    marks = [p['mark'] for p in AC['paraphrase']]
    s1 = len(AC['paraphrase']) == AC['clauses_scored'] == 3
    s2 = all(m in MARKS for m in marks)
    s3 = sum(1 for m in marks if m == 'ACCURATE') == AC['accurate']
    s4 = sum(1 for m in marks if m == 'OVER-STATED') == AC['over_stated'] == 1
    # ### **AND EVERY CLAUSE CARRIES THE RULE`S OWN WORDS BESIDE IT IN THE RUN RECORD.**
    beside = []
    for p in AC['paraphrase']:
        i = acrun.find(p['clause'][:60])
        seg = acrun[i:i + 1600] if i >= 0 else ''
        beside.append(bool(seg) and ('REGISTRY.md` line' in seg or 'REGISTRY.md line' in seg))
    s5 = all(beside)
    # ### **THE PARAPHRASE WAS SCORED, NOT ENDORSED**: the over-statement is named EXACTLY.
    s6 = 'NEITHER PLACE MAKES THE WHOLE MANIFEST THE AUTHORITY' in gate_text.flat(bank).upper()
    s7 = AC['rule_located'] is True and E['rule_located'] is True
    gs = s1 and s2 and s3 and s4 and s5 and s6 and s7
    for p, b in zip(AC['paraphrase'], beside):
        print('    %-12s %-84s rule`s words beside it : %s'
              % (p['mark'], p['clause'][:84], b))
    print('    ### **SCORED %d ; ACCURATE %d ; OVER-STATED %d ; NARROWED %d**'
          % (AC['clauses_scored'], AC['accurate'], AC['over_stated'],
             sum(1 for m in marks if m == 'NARROWED')))
    print('    ### **THE OVER-STATEMENT IS NAMED EXACTLY AND NOT GENERALLY** : %s' % s6)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SCORED')

    # --------------------------------------------------------------- BAR 5, THE REFUTATION BAR
    print(chr(10) + '  G-REFUTED (BAR 5):')
    bu = gate_text.flat(bank).upper()
    r1 = 'CLAIM IS REFUTED BY THIS ACT' in bu
    r2 = 'SAID FIRST RATHER THAN FOLDED INTO A' in bu
    # ### **THE REASON, NOT ONLY THE VERDICT.** ### A refutation without its reason teaches nothing.
    r3 = 'SEARCHED FOR' in bu and 'NAME FOR THE RULE' in bu
    r4 = 'A CONTROLLED SEARCH FOR THE WRONG STRING IS STILL A CONTROLLED' in bu
    r5 = 'NOT THAT THE TERM IS THE RIGHT ONE' in bu
    # ### **AND IT LEADS THE BANK** -- inside the first fifth of the file, not buried at the end.
    r6 = bu.index('CLAIM IS REFUTED BY THIS ACT') < len(bu) // 5 if r1 else False
    # ### **AND THE DESK CLOSES b383`S ITEM BY REFUTATION AND NOT BY SILENCE.**
    r7 = any('b383' in m['item'] and m['disposition'] == 'CLOSE' for m in Q['marks'])
    gr = r1 and r2 and r3 and r4 and r5 and r6 and r7
    print('    named as refuted : %s ; said first : %s ; leads the bank : %s' % (r1, r2, r6))
    print('    ### **WITH ITS REASON, AND THE SPECIES MINTED FROM IT** : %s / %s' % (r3, r4))
    print('    the positive control proves the matcher, not the term : %s' % r5)
    print('    the desk closes b383`s item by REFUTATION : %s' % r7)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REFUTED')

    # ------------------------------------------------------------- BAR 6, THE CONFIRMATION BAR
    print(chr(10) + '  G-CONFIRMED / G-NOFILENAME / G-NOTOUCH (BAR 6):')
    c1 = AC['archive_digest_ok'] + AC['archive_digest_bad'] == AC['archive_files']
    c2 = AC['archive_content_ok'] + AC['archive_content_bad'] == AC['archive_files']
    c3 = AC['archive_removed'] == 0
    c4 = AC['filename_used'] is False
    c5 = 'NEVER BY FILENAME' in bu and 'COMPUTED AND PRINTED UNUSED' in bu
    c6 = str(AC['archive_all']) in bank and str(AC['archive_files']) in bank
    # ### **NOTHING UNDER `archive/` MOVED**, measured against the repository and not asserted.
    arch = [x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
            if x.strip().startswith('archive/')]
    c7 = not arch
    unt = [x for x in git(PP, 'status', '--porcelain').split(chr(10))
           if x.strip().startswith('??') and 'archive/' in x]
    c8 = not unt
    # ### **AND THE ONE CONTENT EXCEPTION IS NAMED BY PATH, NOT SWALLOWED BY THE COUNT.**
    c9 = AC['archive_content_bad'] == 0 or 'E_DIFFICULTY_CONJECTURE' in acrun
    gc = c1 and c2 and c3 and c4 and c5 and c6 and c7 and c8 and c9
    print('    digest %d+%d == %d : %s ; content %d+%d == %d : %s'
          % (AC['archive_digest_ok'], AC['archive_digest_bad'], AC['archive_files'], c1,
             AC['archive_content_ok'], AC['archive_content_bad'], AC['archive_files'], c2))
    print('    ### **REMOVED, MOVED OR RENAMED : %d ; FILENAME USED IN A VERDICT : %s**'
          % (AC['archive_removed'], AC['filename_used']))
    print('    nothing under archive/ changed or appeared : %s / %s' % (c7, c8))
    print('    ### **THE ONE CONTENT EXCEPTION IS NAMED BY PATH** : %s' % c9)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CONFIRMED/G-NOFILENAME/G-NOTOUCH')

    # ------------------------------------------------------------- BAR 7, THE THREE-ITEM BAR
    print(chr(10) + '  G-DISPOSITION (BAR 7):')
    items = AC['items']
    d1 = len(items) == 3 == len(AC['dispositions'])
    d2 = all(it['disposition'] in DISPOSITIONS for it in items)
    # ### **EXACTLY ONE DISPOSITION EACH.** ### An item whose line carries two of the words has been
    # ### hedged, and the order said ### **NONE PARTLY.**
    d3 = True
    for it in items:
        hits = [w for w in ('DONE WITH EXCEPTIONS REPORTED', 'ALREADY DONE BY THE RECORD',
                            'ROUTED') if w in it['disposition']]
        base = it['disposition'] in DISPOSITIONS
        d3 = d3 and base and len(hits) <= 1
    d4 = 'PARTLY' not in bu.replace('NONE PARTLY', '')
    d5 = [it['disposition'] for it in items] == AC['dispositions']
    d6 = AC['roster_edited'] is False and AC['faces_present'] is True
    gd = d1 and d2 and d3 and d4 and d5 and d6
    for it in items:
        print('    %-52s ### **%s**' % (it['item'], it['disposition']))
    print('    three items, three dispositions, each from the ruled set : %s / %s' % (d1, d2))
    print('    ### **NONE PARTLY** : %s ; the roster was not edited : %s' % (d4, d6))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-DISPOSITION')

    # ------------------------------------------------------- BAR 8, THE NO-RECOMMENDATION BAR
    print(chr(10) + '  G-NORECOMMEND / G-NOPREFER (BAR 8):')
    c_start = bank.find('### COMPONENT 4 -- THE CITATION QUESTION.')
    c_end = bank.find('### THE DESK, THE WRITES, AND WHAT THIS ACT DID NOT DO.')
    cregion = bank[c_start:c_end] if (c_start >= 0 and c_end > c_start) else ''
    raw, live = live_preference(cregion)
    # ### **AND THE TRAIL BLOCK`S OWN CITATION PARAGRAPH IS SWEPT TOO** -- the bank is not the only
    # ### place this act states the question.
    traw, tlive = live_preference(tblk)
    print('    ### raw preference-word hits in the bank`s Component 4 : %s'
          % (sorted(set(raw)) or 'none'))
    for w, ctx in live:
        print('        ### ### **LIVE HIT** `%s` : %s' % (w, ctx))
    print('    ### raw preference-word hits in the trail block : %s' % (sorted(set(traw)) or 'none'))
    for w, ctx in tlive:
        print('        ### ### **LIVE HIT** `%s` : %s' % (w, ctx))
    p1 = bool(cregion) and not live and not tlive
    p2 = AC['options_recommended'] == 0 and AC['options'] == 3
    p3 = AC['question_answered'] is False and AC['class_ruled'] is False
    # ### **THE OPTIONS ARE STATED WITH OBLIGATIONS RATHER THAN MERITS** -- each names what it
    # ### WOULD OBLIGE, and the count of obligation clauses equals the count of options.
    p4 = cregion.count('WHAT IT WOULD OBLIGE') + cregion.count('*Obliges:*') >= AC['options']
    p5 = 'NOT A FOURTH OPTION' in gate_text.flat(cregion).upper()
    p6 = 'THE FAILURE THE TIERS EXIST TO PREVENT' in gate_text.flat(cregion).upper()
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    live preference words : %d bank / %d trail' % (len(live), len(tlive)))
    print('    ### **OPTIONS %d ; RECOMMENDED %d ; ANSWERED %s**'
          % (AC['options'], AC['options_recommended'], AC['question_answered']))
    print('    each option names what it would oblige : %s ; no fourth invented : %s' % (p4, p5))
    print('    the failure the tiers prevent is quoted beside them : %s' % p6)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-NORECOMMEND/G-NOPREFER')

    # ------------------------------------------------------- G-NORULING / G-NOEDITSTD / G-OPEN
    print(chr(10) + '  G-NORULING / G-NOEDITSTD / G-OPEN / G-NONEWDOC:')
    n1 = AC['class_ruled'] is False and AC['standards_edited'] == 0
    TAXON = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
    n2 = not git(PP, 'diff', '--name-only', 'HEAD', '--',
                 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md').strip()
    n3 = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'REGISTRY.md').strip()
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    open_marks = [m for m in Q['marks'] if m['item'] in LISTS]
    n4 = len(open_marks) == 4 and all(m['disposition'] == 'STAND' for m in open_marks)
    n5 = 'The four open lists are restated OPEN by name' in tblk
    n6 = Q['lists_closed'] == 0
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    n7 = not newdocs
    gn = n1 and n2 and n3 and n4 and n5 and n6 and n7
    print('    class ruled : %s ; standards edited : %d' % (AC['class_ruled'],
                                                            AC['standards_edited']))
    print('    ### **THE TAXONOMY IS BYTE-IDENTICAL TO ITS BLOB** : %s (%s)'
          % (n2, os.path.exists(TAXON)))
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB** : %s' % n3)
    print('    the four lists STAND on the desk : %s ; named OPEN in the block : %s' % (n4, n5))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (n7, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-NOEDITSTD/G-OPEN/G-NONEWDOC')

    # ------------------------------------------------------------------ G-NOWRITE / G-GUARD
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-GUARD:')
    ALLOWED = {'relay': {'.githooks/pre-push', 'tools/banked_index.py'},
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b385' not in x)
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    ppch = [x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip()]
    w2 = set(ppch) <= {'OPEN_TRAILS.md'}
    w3 = not [x for x in ppch if x.startswith('outputs/') or x.startswith('archive/')]
    # ### **THE GUARD REPAIR IS EXACTLY ONE LINE, AND IT IS A COMMENT.** ### `(R4)` licenses a
    # ### repair by edit; ### **IT DOES NOT LICENSE A BEHAVIOUR CHANGE**, so the diff is counted.
    gd_diff = git(ROOT, 'diff', '-U0', '--', '.githooks/pre-push')
    adds = [x for x in gd_diff.split(chr(10)) if x.startswith('+') and not x.startswith('+++')]
    dels = [x for x in gd_diff.split(chr(10)) if x.startswith('-') and not x.startswith('---')]
    w4 = len(adds) == len(dels) == 1
    w5 = adds and adds[0].lstrip('+').lstrip().startswith('#')
    w6 = dels and dels[0].lstrip('-').lstrip().startswith('#')
    w7 = AC['guard_behaviour_unchanged'] is True
    gw = w1 and w2 and w3 and w4 and w5 and w6 and w7
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **THE ONLY PLACE-papers PATH TOUCHED IS OPEN_TRAILS.md** : %s %s' % (w2, ppch))
    print('    ### **THE GUARD DIFF IS ONE LINE IN AND ONE LINE OUT** : %s (+%d/-%d)'
          % (w4, len(adds), len(dels)))
    print('    ### **AND BOTH ARE COMMENTS, SO THE BEHAVIOUR IS UNCHANGED** : %s / %s / %s'
          % (w5, w6, w7))
    for x in adds + dels:
        print('        %s' % x[:120])
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY/G-GUARD')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE REVIEWER-RESERVOIR RULE IS LOCATED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-reservoir-rule-located-and-the-six-on-the-trails returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the rule is not located', 'a cluster is owed a keystone',
              'the citation question is answered', 'an archive file was removed'))
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
    # ### ### **THE ORDER OF THE ACT, MEASURED IN BOTH DIRECTIONS AND NOT ONE.**
    # ### The extract and the lock gate are ### **PRE-LOCK BY CONSTRUCTION** -- the standing clauses
    # ### say extract-to-disk for every read, and the registration is CHAINED ON every pre-lock gate.
    # ### The components and the desk are ### **POST-LOCK BY CONSTRUCTION**, because the face was
    # ### locked before any write. ### **AN ARM THAT DEMANDED `AFTER` OF ALL FOUR WOULD FAIL THE
    # ### ### ACT FOR OBEYING ITS OWN ORDER**, so each is checked against the side it belongs on.
    def clk(x):
        return x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))
    AFTER = (('components', AC), ('desk_bank', Q))
    BEFORE = (('extract', E), ('lockgate', LG))
    o3a = (stampm is not None) and all(clk(x) > stampm.group(1) for _l, x in AFTER)
    # ### **THE PRE-LOCK SIDE IS `<=` AND NOT `<`, AND THAT IS NOT A LOOSENING.** ### The lock
    # ### gate is the LAST thing to run before `reg_seal --lock`, and `reg_seal` stamps its own
    # ### UTC to the second (`b344`), so the two legitimately share a second. ### **A STRICT `<`
    # ### ### WOULD FAIL AN ACT FOR BEING FAST**, which measures the clock's resolution and not
    # ### the act's order.
    o3b = (stampm is not None) and all(clk(x) <= stampm.group(1) for _l, x in BEFORE)
    o3 = o3a and o3b
    for lbl, x in AFTER + BEFORE:
        side = 'AFTER ' if (lbl, x) in [(a2, b2) for a2, b2 in AFTER] else 'BEFORE'
        print('    %-10s %s the lock : run %s vs lock %s'
              % (lbl, side, clk(x), stampm.group(1) if stampm else '?'))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    o8 = 'SEAL INTACT' in (subprocess.run(
        [sys.executable, t('reg_seal.py'), '--verify', d('b384_registration_2026-09-09.txt')],
        capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or '')
    o9 = 'SEAL INTACT' in (subprocess.run(
        [sys.executable, t('reg_seal.py'), '--verify', d('b383_registration_2026-09-09.txt')],
        capture_output=True, text=True, encoding='utf-8', errors='replace').stdout or '')
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    ### **THE TWO POST-LOCK RUNS ARE AFTER IT : %s ; THE TWO PRE-LOCK GATES ARE '
          'BEFORE IT : %s**' % (o3a, o3b))
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b384`S AND b383`S FACES STILL VERIFY, UNEDITED** : %s / %s' % (o8, o9))
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b385_hooks.txt'), d('b385_mirror.txt')
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
        ('face-subject gates %d' % LG['face_subject_gates'], str(LG['face_subject_gates']) in bank),
        ('the rule`s line %d' % Q['rule_line'], str(Q['rule_line']) in bank),
        ('entries written %d' % AC['entries_written'], str(AC['entries_written']) in bank),
        ('clauses scored %d' % AC['clauses_scored'], str(AC['clauses_scored']) in bank),
        ('accurate %d / over-stated %d' % (AC['accurate'], AC['over_stated']),
         str(AC['accurate']) in bank and str(AC['over_stated']) in bank),
        ('archive all %d' % AC['archive_all'], str(AC['archive_all']) in bank),
        ('archive .md %d' % AC['archive_files'], str(AC['archive_files']) in bank),
        ('digest ok %d' % AC['archive_digest_ok'], str(AC['archive_digest_ok']) in bank),
        ('content ok %d' % AC['archive_content_ok'], str(AC['archive_content_ok']) in bank),
        ('options %d' % AC['options'], str(AC['options']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on component run', AC['run_file'] in bank),
        ('the extract run', E['run_file'] in bank),
        ('the control hits %d' % E['control_hits'], str(E['control_hits']) in bank),
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
                          if x.startswith('b385_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid',
              'curve_fit', 'minimize')
    raw2 = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    CALL = {b: re.compile(r'\b' + b + r'\s*\(') for b in banned}
    hits2 = [(x, b) for x in mymods for b in banned if CALL[b].search(strip_prose(t(x)))]
    print('    ### raw substring hits (a substring is not a call) : %s' % (raw2 or 'none'))
    for _x, _b in [r for r in raw2 if r not in hits2]:
        print('        ### DISCHARGED in %s : `%s` occurs only inside a longer identifier'
              % (_x, _b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits2 and not imports
    print('    numerical calls : %d %s ; libraries : %s'
          % (len(hits2), hits2 or '', imports or 'none'))
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
    DECLARED = {'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST '
                                  'WROTE.',
                'the located span': 'the span is located by content and only then indexed.',
                'a parsed table cell': 'the cell index is a COLUMN of a row located by its own '
                                       'shape.',
                'a bounded sample': 'a slice of a list THIS ACT built in memory, not an address.',
                'a line read by its own anchor':
                    'the index is a line number the ANCHOR TOOL returned from the file.'}

    def which(code):
        if "['line'] - 1]" in code or 'lineno' in code or 'rq[2] - 1]' in code:
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
             'tools/b374_hedge.py', 'tools/b375_population.py', 'tools/gate_hash.py',
             'tools/b378_lockgate.py', 'tools/role_structure.py', 'tools/co_location.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    # ### **THE TWO DECLARED WRITES OUTSIDE THIS ACT`S OWN FILES**, both named on the locked face's
    # ### section (F): one key in the index, and ### **ONE COMMENT LINE IN THE GUARD** under `(R4)`.
    DECLARED_W = ('tools/banked_index.py', '.githooks/pre-push')
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b385' not in x and x.strip() not in DECLARED_W]
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files beyond the two declared : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b385_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b385_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the sources' own lines"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the component run carries the rule's own text"),
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

    marker = '# ### THE RULE LOCATED, THE SIX ON THE TRAILS (b385).'
    nxt = '# ### THE FOLD, b371 THROUGH b383 (b384).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b385_stem_'), 'blk.txt')
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
    print('    ### **A CAP IS A NUMBER, NOT A LIST** (`b382`) -- and the number is six.')
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b385_hedge_')
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
