# -*- coding: utf-8 -*-
"""b383_checks.py -- THE GATE SUITE FOR THE STANDARD READ AND THE SEQUENCE RECONCILED.

### ### **THE ARM THAT MATTERS MOST HERE IS `G-NOEDITSTD`.** ### This leg reads three author-ruled
### standing documents and drafts amendments to one of them, and ### **A SEAT THAT DRAFTS AN
### ### AMENDMENT AND THEN APPLIES IT HAS RULED**, so the three are checked byte-identical to their
### blobs at the end of the act.
### ### **`G-REREAD` IS SECOND:** ### the whole of Component 1 is quotation, and an account that
### misquotes a standard is worse than none.
### ### **AND `G-CLUSTERRULE` MEASURES THE AUTHOR'S AMENDMENT:** ### wherever a cluster-to-keystone
### count is printed, the many-to-many rule appears beside it, so ### **A PLURALITY IS NEVER READ AS
### ### AN ANOMALY AND AN ABSENCE IS NEVER READ AS A DEFECT.**
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`); ### **A RUN FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
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
import b383_extract as EXT    # noqa: E402

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


BANK = d('b383_the_standard_read.txt')
REG = d('b383_registration_2026-09-09.txt')
FERRY = d('b383_ferry_2026-09-09.txt')
AMEND = d('b383_amendment_2026-09-09.txt')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b383_ferry_scan.txt'), d('b383_reg_termscan.txt'), d('b383_reg_gate.txt')
CENSUS0, FCEN = d('b383_census_stepzero.txt'), d('b383_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b383_regspec_run.txt'), d('audit_b383_reg_satisfiable.txt')
PINS0 = d('b383_pins_stepzero.txt')
SEAL = '5ed21930bc425a0a44a9100cca6aa109bffdaf1e297db0594fde66ee67883c5c'
ROWNUM = '232'
TRAIL_MARK = '<!-- b383 the standard read; the sequence reconciled -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b383_reads.json'), ('LG', 'b383_lockgate.json'),
                   ('AC', 'b383_components.json'), ('Q', 'b383_desk.json'))}

# ### **RESOLVED BY THE RECORDED CLOCK, NEVER BY NAME** (`b358`).
IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b383_regspec.py', 'tools/b383_extract.py', 'tools/b383_reg_gate.py',
                'tools/b383_components.py', 'tools/b383_desk_bank.py', 'tools/b383_checks.py'}

TOOLNUM = [
    ('the reads, and the controlled reservoir sweep', 'tools/b383_extract.py'),
    ('the standard, the reconciliation, the model, the amendments', 'tools/b383_components.py'),
    ('(R7), the three closing writes and the bank', 'tools/b383_desk_bank.py'),
    ('the registration gate', 'tools/b383_reg_gate.py'),
    ('the clause spec', 'tools/b383_regspec.py'),
    ("b375's population and clusters, RE-READ AND NOT RECALLED", 'tools/b375_population.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

# ### **THE OWNER NEEDLES ARE THE EXTRACT TOOL`S OWN READS TABLE, IMPORTED AND NOT RETYPED.**
OWNER_NEEDLES = [(lbl, path, hint) for lbl, _tag, path, hint in EXT.READS]
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')

SELF_NEEDLES = [
    ('the bank leads with the uncited standard', BANK,
     '### ### ### **THE CORPUS ALREADY CARRIED AN AUTHOR-RULED ANSWER TO THE CLASS'),
    ('### the four tiers, obligation and citation rule', BANK,
     '### ### **THE FOUR TIERS, IN THE STANDARD`S OWN TERMS:**'),
    ('### Tier C is never cited as certification', BANK,
     '###     ### CERTIFICATION.** ### The standard calls this ### **ITS LOAD-BEARING RULE.**'),
    ('### Tier E cites Tier K and nothing cites Tier E', BANK,
     '###     ### TIER E.**'),
    ('### the failure the taxonomy was built to prevent', BANK,
     '### ### ### **AND THE FAILURE IT WAS BUILT TO PREVENT, IN ITS OWN WORDS:** ### *the'),
    ('### the reconciliation, without defence', BANK,
     '### COMPONENT 2 -- THE SEQUENCE RECONCILED, WITHOUT DEFENCE.'),
    ('### none of the eight acts cited the three sources', BANK,
     '### ### ### **THE STANDARD HAD ALREADY RULED THE CLASS QUESTION AND NONE OF THE EIGHT'),
    ('### the sequence violated the freshness rule', BANK,
     '### ### ### **AND THE SEQUENCE VIOLATED A FRESHNESS RULE THIS SEAT MINTED AT `b368`.**'),
    ('### the conjunction is excluded, not merely unnamed', BANK,
     '### ### **WRONG IN ONE PARTICULAR, AND IT MATTERS: THE CONJUNCTION IS NOT MERELY'),
    ('### the predecessor scheme was retired for spanning the two', BANK,
     '###   ### **(c)** ### and `b186`s predecessor scheme was ### **RETIRED** ### precisely'),
    ('### a real amendment and not a clarification', BANK,
     '### ### ### **SO THE AUTHOR`S FINISHED KEYSTONE IS A REAL AMENDMENT AND NOT A'),
    ('### the model is recorded and not applied', BANK,
     '### ### **IT IS BANKED AS THE AUTHOR`S STATEMENT AND NOT ADOPTED AS THIS SEAT`S'),
    ('### the author`s reason, it is a laboratory', BANK,
     '### ### **THE AUTHOR`S REASON, BANKED VERBATIM:** ### *it is a laboratory -- an ongoing'),
    ('### the cluster rule stated beside the count', BANK,
     '###   ### **THE RULE:** ### a cluster may have SEVERAL keystones, ONE, or NONE YET;'),
    ('### not-yet-synthesized, not owed and not deficient', BANK,
     '###   ### KEYSTONE IS `NOT-YET-SYNTHESIZED`, NOT OWED AND NOT DEFICIENT.**'),
    ('### a plurality is not an anomaly and an absence is not a defect', BANK,
     '###   ### ### **SO A PLURALITY IS NEVER READ AS AN ANOMALY AND AN ABSENCE IS NEVER'),
    ('### the sweep priced and not ordered', BANK,
     '### ### **THE SWEEP, PRICED FROM THE RECORD`S OWN FIGURES AND ### NOT ORDERED:**'),
    ('### the unpriced part is named unpriced', BANK,
     '### ### RATHER THAN ESTIMATED. ### A PRICE IS NOT A PROPOSAL.**'),
    ('### a seat cannot restate a rule it cannot read', BANK,
     '### ### **A SEAT CANNOT RESTATE A RULE IT CANNOT READ**, and a seat that supplies the'),
    ('### quoting a standard is not amending it', BANK,
     '### ### ### **QUOTING A STANDARD IS NOT AMENDING IT, AND DRAFTING AN AMENDMENT IS NOT'),
    ('### an eight-act sequence can re-derive a ruled standard', BANK,
     '### ### ### **NEW -- `AN EIGHT-ACT SEQUENCE CAN RE-DERIVE A RULED STANDARD WITHOUT`'),
    ('### a minted rule is not a carried rule', BANK,
     '### ### ### CARRIED RULE**, which is `b378`s species arriving one level up.'),
    ('### the amendment arrived before the lock', BANK,
     '### ### **AND THE AUTHOR`S AMENDMENT TO COMPONENT 4(ii) ARRIVED BEFORE THIS LOCK**, so'),
]

MUST_FAIL = [
    ('the bank never says a standard was edited', BANK, '### A STANDARD WAS EDITED.'),
    ('the bank never says an amendment was applied', BANK, '### AN AMENDMENT WAS APPLIED.'),
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says a quotation did not re-read', BANK, '### A QUOTATION DID NOT RE-READ.'),
    ('the bank never says the mirror was read', BANK, '### THE MIRROR WAS READ.'),
    ('the bank never says a cluster is owed a keystone', BANK,
     '### A CLUSTER IS OWED A KEYSTONE.'),
    ('the bank never names a preferred reading', BANK, '### THE PREFERRED READING IS.'),
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
    print('b383 -- GATE SUITE (THE STANDARD READ, THE SEQUENCE RECONCILED)')
    print('=' * 100)
    E, LG, AC, Q = _J['E'], _J['LG'], _J['AC'], _J['Q']
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    P75 = json.load(io.open(d('b375_population.json'), encoding='utf-8'))
    CL375 = json.load(io.open(d('b375_clusters.json'), encoding='utf-8'))
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
    # ### the trail block this act appended, located by its own mark
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
    l7 = LG['act'] == 'b383' and not os.path.exists(t('b383_lockgate.py'))
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8 and l8 and l8 and l8
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s' % l6)
    print('    ### **THE LOCK GATE WAS INHERITED, NOT REBUILT** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # ------------------------------------------------------------------ BAR 2, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-REREAD (BAR 2):')
    quoted = [b for b in E['built']
              if b['tag'] in ('STANDARD', 'REGISTRY', 'UNION', 'FRESH', 'AMEND', 'SEQ')]
    bad = []
    for b in quoted:
        src = b.get('path') or d(b['file'])
        if not os.path.exists(src):
            bad.append((b['file'], 'missing'))
            continue
        ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        if b['line'] - 1 >= len(ls) or ls[b['line'] - 1].rstrip(chr(13)) != b['text']:
            bad.append((b['file'], b['line']))
    q1 = not bad
    q2 = AC['reread_ok'] is True and not AC['reread_failures']
    inrun = sum(1 for b in quoted if b['text'].strip()[:70] in acrun)
    q3 = inrun >= 20
    gq = q1 and q2 and q3
    print('    ### **QUOTED LINES RE-READ INDEPENDENTLY : %d ; FAILURES : %d** %s'
          % (len(quoted), len(bad), bad[:3] or ''))
    print('    the tool`s own re-read agrees : %s ; present in the components run : %d'
          % (q2, inrun))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-REREAD')

    # ---------------------------------------------------------------- BAR 3, THE FOUR-TIER BAR
    print(chr(10) + '  G-FOURTIERS / G-OBLIGATION / G-CITATION (BAR 3):')
    TIERS = ('Tier K', 'Tier C', 'Tier N', 'Tier E')
    missing_t = [t_ for t_ in TIERS
                 if not any(t_ in b['text'] for b in quoted if b['tag'] == 'STANDARD')]
    a1 = not missing_t and AC['tiers_quoted'] == 4
    # ### ### **EACH TIER'S QUOTED LINE MUST CARRY BOTH ITS OBLIGATION AND ITS CITATION RULE.**
    tierlines = [b['text'] for b in quoted if b['tag'] == 'STANDARD' and 'Tier' in b['text'][:12]]
    a2 = sum(1 for x in tierlines if 'Obligation' in x) >= 4
    a3 = sum(1 for x in tierlines if 'Citation rule' in x) >= 4
    a4 = 'two failures structurally impossible' in acrun
    a5 = 'may be cited as certification' in acrun.lower()
    a6 = 'never as certification' in acrun.lower()
    a7 = AC['sources_read'] == 3
    ga = a1 and a2 and a3 and a4 and a5 and a6 and a7
    print('    all four tiers quoted : %s %s' % (a1, missing_t or ''))
    print('    ### **EACH CARRIES ITS OBLIGATION (%d) AND ITS CITATION RULE (%d)**'
          % (sum(1 for x in tierlines if 'Obligation' in x),
             sum(1 for x in tierlines if 'Citation rule' in x)))
    print('    the failure it prevents is quoted : %s ; both citation poles present : %s / %s'
          % (a4, a5, a6))
    print('    sources read : %d' % AC['sources_read'])
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-FOURTIERS/G-OBLIGATION/G-CITATION')

    # ------------------------------------------------------------ BAR 4, THE CANONICAL-DRIVE BAR
    print(chr(10) + '  G-CANONICAL / G-NOMIRROR (BAR 4):')
    corpus = [b for b in quoted if b['tag'] in ('STANDARD', 'REGISTRY', 'UNION')]
    c1 = all((b.get('path') or '').startswith(PP) for b in corpus)
    c2 = E['mirror_opened'] is False
    c3 = E['canonical_drive'] == PP
    # ### **AND NO ZIP WAS OPENED BY ANY OF THIS ACT'S TOOLS** -- measured on stripped code.
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b383_') and x.endswith('.py')))
    zipuse = [x for x in mymods0
              if 'zipfile' in strip_prose(t(x)) or 'mirror-refresh' in strip_prose(t(x))]
    c4 = not zipuse
    gc = c1 and c2 and c3 and c4
    print('    ### **EVERY CORPUS QUOTATION RESOLVES UNDER THE WORKING TREE** : %s (%d lines)'
          % (c1, len(corpus)))
    print('    the mirror was not opened : %s ; canonical drive recorded : %s' % (c2, c3))
    print('    no tool of this act reads a zip : %s %s' % (c4, zipuse or ''))
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CANONICAL/G-NOMIRROR')

    # ---------------------------------------------------------- BAR 5, THE RECONCILIATION BAR
    print(chr(10) + '  G-RECONCILE / G-COVERAGE (BAR 5):')
    ACTS = ('b375', 'b376', 'b377', 'b378', 'b379', 'b380', 'b381', 'b382')
    rows = AC['rows']
    r1 = len(rows) == len(ACTS) == AC['acts_reconciled']
    r2 = sorted(x['act'] for x in rows) == sorted(ACTS)
    r3 = all(x['verdict'] in ('DUPLICATED', 'ADDS') for x in rows)
    r4 = (AC['duplicated'] == sum(1 for x in rows if x['verdict'] == 'DUPLICATED')
          and AC['adds'] == sum(1 for x in rows if x['verdict'] == 'ADDS'))
    r5 = AC['duplicated'] + AC['adds'] == len(ACTS)
    r6 = all(x['act'] in bank for x in rows)
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    acts covered : %d of %d ; every act named : %s' % (len(rows), len(ACTS), r2))
    print('    every verdict is DUPLICATED or ADDS : %s ; counts recompute : %s' % (r3, r4))
    print('    ### **DUPLICATED %d / ADDS %d** ; all in the bank : %s'
          % (AC['duplicated'], AC['adds'], r6))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-RECONCILE/G-COVERAGE')

    # ----------------------------------------------------------------- BAR 6, THE VERDICT BAR
    print(chr(10) + '  G-VERDICT / G-TESTED (BAR 6):')
    v1 = AC['verdict'] in ('CONFIRMED', 'CORRECTED', 'REFUTED')
    v2 = AC['verdict'] in bank
    # ### ### **THE LINE THAT DECIDES IT MUST BE PRESENT** -- the retired-scheme quotation.
    v3 = 'spanned Tier K and Tier C at once' in acrun
    v4 = 'Read the panels as C, the pinned terminals as K' in acrun
    v5 = 'IT IS EXCLUDED' in bank
    v6 = 'A REAL AMENDMENT AND NOT A' in bank
    gv = v1 and v2 and v3 and v4 and v5 and v6
    print('    ### **VERDICT : %s** ; one of the three : %s ; in the bank : %s'
          % (AC['verdict'], v1, v2))
    print('    the deciding lines are quoted : retired-scheme %s ; CATALOGOS %s' % (v3, v4))
    print('    the bank says excluded rather than unnamed : %s' % v5)
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT/G-TESTED')

    # ---------------------------------------------------------------- BAR 7, THE VERBATIM BAR
    print(chr(10) + '  G-VERBATIM (BAR 7):')
    ferry = io.open(FERRY, encoding='utf-8').read().split(chr(10))
    a_ = [i for i, x in enumerate(ferry) if x.startswith("COMPONENT 3 - THE AUTHOR'S MODEL")]
    b_ = [i for i, x in enumerate(ferry) if x.startswith('with glossary, bibliography and other')]
    m1 = len(a_) == 1 and len(b_) == 1 and a_[0] < b_[0]
    m2 = AC['model_lines'] == (b_[0] - a_[0] + 1) if m1 else False
    m3 = AC['model_dropped'] == 0
    m4 = all(('###   | ' + ln.rstrip()) in acrun for ln in ferry[a_[0]:b_[0] + 1]) if m1 else False
    gm = m1 and m2 and m3 and m4
    print('    both slice ends unique : %s ; lines %d ; dropped %d'
          % (m1, AC['model_lines'], AC['model_dropped']))
    print('    ### **EVERY LINE OF THE MODEL IS IN THE RUN RECORD** : %s' % m4)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-VERBATIM')

    # ------------------------------------------------------------------ BAR 8, THE NO-EDIT BAR
    print(chr(10) + '  G-NOEDITSTD / G-NOAMEND (BAR 8):')
    STD = ('phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'REGISTRY.md',
           'phase1.5/method/THE_LOAD_BEARING_MAP.md')
    live_ok = {}
    for rel in STD:
        bl = blob_of(PP, rel)
        live = io.open(os.path.join(PP, rel.replace('/', os.sep)),
                       encoding='utf-8', newline='').read()
        live_ok[rel] = (bl is not None) and norm(live) == norm(bl)
    e1 = all(live_ok.values())
    e2 = AC['standards_edited'] == 0 and AC['amendments_applied'] == 0
    e3 = AC['amendments_drafted'] == 4
    e4 = all(bool(v) for v in AC['standards_unedited'].values())
    e5 = 'QUOTING A STANDARD IS NOT AMENDING IT' in bank
    ge = e1 and e2 and e3 and e4 and e5
    for rel in STD:
        print('    %-56s byte-identical : %s' % (rel, live_ok[rel]))
    print('    ### **STANDARDS EDITED : %d ; AMENDMENTS APPLIED : %d ; DRAFTED : %d**'
          % (AC['standards_edited'], AC['amendments_applied'], AC['amendments_drafted']))
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-NOEDITSTD/G-NOAMEND')

    # -------------------------------------------------------------- BAR 9, THE CLUSTER-RULE BAR
    print(chr(10) + '  G-CLUSTERRULE / G-NOTYET (BAR 9):')
    nokey = len(CL375['subject_clusters_without_keystone'])
    k1 = AC['clusters_without_keystone'] == nokey
    k2 = AC['clusters_owed'] == 0
    k3 = 'NOT-YET-SYNTHESIZED' in bank
    k4 = 'NOT OWED AND NOT DEFICIENT' in bank
    # ### ### **THE RULE MUST SIT BESIDE THE COUNT, NOT ELSEWHERE IN THE FILE.**
    i_count = bank.find('SUBJECT CLUSTERS HAVE REGISTRY ROWS AND NO KEYSTONE')
    window = bank[i_count:i_count + 1400] if i_count >= 0 else ''
    k5 = ('SEVERAL keystones, ONE, or NONE YET' in window and 'NOT-YET-SYNTHESIZED' in window)
    k6 = 'A PLURALITY IS NEVER READ AS AN ANOMALY' in bank
    k7 = AC['grades_moved'] == 0
    gk = k1 and k2 and k3 and k4 and k5 and k6 and k7
    print('    clusters without a keystone : %d ; described as owed : %d' % (nokey, AC['clusters_owed']))
    print('    ### **THE RULE SITS BESIDE THE COUNT** : %s' % k5)
    print('    not-yet-synthesized / not owed / plurality-not-anomaly : %s / %s / %s'
          % (k3, k4, k6))
    print('    grades moved : %d' % AC['grades_moved'])
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CLUSTERRULE/G-NOTYET')

    # ------------------------------------------------------------ BAR 10, THE PROVED-ABSENCE BAR
    print(chr(10) + '  G-PROVEDABSENCE / G-PRICED (BAR 10):')
    p1 = E['control_hits'] > 0
    p2 = E['reservoir_located'] is False
    p3 = 'A SEAT CANNOT RESTATE A RULE IT CANNOT READ' in bank
    p4 = 'ROUTED AS A REQUEST' in bank
    # ### **THE SWEEP EXCLUDED THIS ACT'S OWN FILES** -- measured on the tool's stripped code.
    # ### **THIS IS A PRESENCE CHECK, NOT A PROHIBITION**, and the guard it looks for IS a
    # ### string literal -- so it reads the raw source. ### A G-NO* arm would read stripped
    # ### code; this one would find nothing there by construction.
    src83 = io.open(t('b383_extract.py'), encoding='utf-8').read()
    p5 = ("if 'b383' in f" in src83 and 'WRITES_OF_THIS_ACT' in src83)
    p6 = 'NAMED UNPRICED' in bank and 'A PRICE IS NOT A PROPOSAL' in bank
    p7 = (str(AC['declared_class_line']) in bank
          and str(AC['not_declared_class_line']) in bank)
    gp = p1 and p2 and p3 and p4 and p5 and p6 and p7
    print('    ### **POSITIVE CONTROL FIRED ON %d FILE(S)** ; rule located : %s'
          % (E['control_hits'], E['reservoir_located']))
    print('    the sweep excludes this act`s own files : %s' % p5)
    print('    routed as a request, not restated : %s / %s' % (p3, p4))
    print('    the sweep priced with the record`s figures and the rest named unpriced : %s / %s'
          % (p7, p6))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PROVEDABSENCE/G-PRICED')

    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b383' not in x and x != 'tools/banked_index.py')
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

    # ------------------------------------------------------- BAR 10, THE NO-RULING BAR
    print(chr(10) + '  G-NORULING / G-NOPREFER / G-NONEWDOC:')
    c_start = bank.find('### ### ### **THE NAVIGATOR`S READING :')
    c_end = bank.find('### COMPONENT 3 -- THE AUTHOR`S MODEL, BANKED VERBATIM.')
    cregion = bank[c_start:c_end] if (c_start >= 0 and c_end > c_start) else ''
    NEG2 = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    craw, clive = [], []
    for m in PREFER.finditer(cregion):
        before = cregion[max(0, m.start() - 90):m.start()]
        craw.append(m.group(0))
        if not NEG2.search(before):
            clive.append(m.group(0))
    print('    ### raw preference-word hits in the conclusion : %s' % (sorted(set(craw)) or 'none'))
    k1 = not clive and bool(cregion)
    k2 = AC['class_ruled'] is False
    k3 = 'A REAL AMENDMENT AND NOT A' in bank
    # ### **THE RELATING-WORD FEATURE WAS NOT BUILT AND NOT BUILT UNDER ANOTHER NAME.**
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b383_') and x.endswith('.py')))
    relating = [x for x in mymods0
                if 'AMENDMENT_APPLIED' in strip_prose(t(x))]
    k4 = not relating
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    k5 = not newdocs
    gk = k1 and k2 and k3 and k4 and k5
    print('    live preference words in the conclusion : %d ; class ruled : %s' % (len(clive), k2))
    print('    ### **THE LIMIT IS STATED WITH THE CONCLUSION** : %s' % k3)
    print('    ### **THE RELATING-WORD FEATURE WAS NOT BUILT** : %s %s' % (k4, relating or ''))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (k5, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-NORULING/G-NOPREFER/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE STANDING STANDARD ALREADY RULED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-standing-standard-read-and-the-sequence-reconciled returns 1 row(s)'
          in irun and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the standard is edited', 'the amendment is applied',
              'a cluster is owed a keystone', 'the class is ruled'))
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
    relied = (AC, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND THE THREE PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    R375 = d('b382_registration_2026-09-09.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b381_registration_2026-09-09.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b381`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b382`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b383_hooks.txt'), d('b383_mirror.txt')
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
        ('sources read %d' % AC['sources_read'], str(AC['sources_read']) in bank),
        ('tiers quoted %d' % AC['tiers_quoted'], str(AC['tiers_quoted']) in bank),
        ('the union`s fourteen tables', '14 GRADED CORRESPONDENCE TABLES' in bank),
        ('acts reconciled %d' % AC['acts_reconciled'], str(AC['acts_reconciled']) in bank),
        ('duplicated %d' % AC['duplicated'], str(AC['duplicated']) in bank),
        ('adds %d' % AC['adds'], str(AC['adds']) in bank),
        ('quotations failing to re-read %d' % len(AC['reread_failures']),
         str(len(AC['reread_failures'])) in bank),
        ('the verdict %s' % AC['verdict'], AC['verdict'] in bank),
        ('model lines %d' % AC['model_lines'], str(AC['model_lines']) in bank),
        ('amendments drafted %d' % AC['amendments_drafted'],
         str(AC['amendments_drafted']) in bank),
        ('clusters without a keystone %d' % AC['clusters_without_keystone'],
         str(AC['clusters_without_keystone']) in bank),
        ('documents carrying a class line %d' % AC['declared_class_line'],
         str(AC['declared_class_line']) in bank),
        ('documents carrying none %d' % AC['not_declared_class_line'],
         str(AC['not_declared_class_line']) in bank),
        ('the control hits %d' % AC['control_hits'], str(AC['control_hits']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on components run', AC['run_file'] in bank),
        ('the relied-on extract run', E['run_file'] in bank),
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
                          if x.startswith('b383_') and x.endswith('.py')))
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
    # ### **THE RULING-EVIDENCE FILE IS A DECLARED WRITE OF THIS ACT**, named on the locked face's
    # ### section (F) -- `the ruling-evidence file updated`. ### It carries b380's name because b380
    # ### created it, and ### **AN ARM THAT FAILS ON A WRITE THE FACE LICENSED IS NOT MEASURING THIS
    # ### ### ACT.**
    DECLARED = ('tools/banked_index.py', 'data/b380_ruling_evidence.txt')
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b383' not in x and x.strip() not in DECLARED]
    gne = (not touched and not others)
    print('    owner instruments modified : %s ### -- this act licenses NONE' % (touched or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    # ------------------------------------------------------------------------ G-STRUCK / G-STEM
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, AMEND, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b383_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b383_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d('b383_amendment_scan.txt'), "the amendment's own scan log"),
        (d(E['run_file']), "the extract carries three standing documents' own lines"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the components ARE quotations from the standing standard"),
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

    marker = '# ### THE STANDARD READ, THE SEQUENCE RECONCILED (b383).'
    nxt = '# ### THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED (b382).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b383_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS LEG AT SIX NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 6 and set(made) == NEW_THIS_ACT
    print('    new relay tools this leg : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b383_hedge_')
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
