# -*- coding: utf-8 -*-
"""b382_checks.py -- THE GATE SUITE FOR THE SEQUENCE STOPPED AND THE EVIDENCE CLOSED.

### ### **THE ARM THAT MATTERS MOST HERE IS `G-REREAD`.** ### This act's whole product is an ACCOUNT
### of seven prior acts, and ### **AN ACCOUNT THAT MISQUOTES ITS SOURCES IS WORSE THAN NO ACCOUNT** --
### so every line the account quotes is re-read out of its own bank at its own line number, by this
### suite and independently of the tool that wrote it.
### ### **AND `G-NOORDER` MEASURES A NON-EVENT:** ### the obligations are PRICED and none is ORDERED.
### ### **A PRICE IS NOT A PROPOSAL**, and an act that prices a rule and then quietly proposes it has
### ruled by implication.
### ### **`G-CAP` IS THE ONE ARM THIS ACT EXPECTS TO ARGUE WITH ITS OWN FACE:** ### the face caps the
### act at SIX files and its clause description named SEVEN roles. ### **THE NUMBER BINDS.**
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
import b382_extract as EXT    # noqa: E402

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


BANK = d('b382_the_sequence_stopped.txt')
EVID = d('b380_ruling_evidence.txt')
REG = d('b382_registration_2026-09-09.txt')
FERRY = d('b382_ferry_2026-09-09.txt')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b382_ferry_scan.txt'), d('b382_reg_termscan.txt'), d('b382_reg_gate.txt')
CENSUS0, FCEN = d('b382_census_stepzero.txt'), d('b382_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b382_regspec_run.txt'), d('audit_b382_reg_satisfiable.txt')
PINS0 = d('b382_pins_stepzero.txt')
SEAL = '6ace94654d59e423f5199fca41884d7059efbd55bc019e5a618bb53e3965c606'
ROWNUM = '231'
TRAIL_MARK = '<!-- b382 the sequence stopped; the evidence closed -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b382_reads.json'), ('LG', 'b382_lockgate.json'),
                   ('AC', 'b382_account.json'), ('Q', 'b382_desk.json'))}

# ### **RESOLVED BY THE RECORDED CLOCK, NEVER BY NAME** (`b358`).
IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b382_regspec.py', 'tools/b382_extract.py', 'tools/b382_reg_gate.py',
                'tools/b382_account.py', 'tools/b382_desk_bank.py', 'tools/b382_checks.py'}

TOOLNUM = [
    ('the reads', 'tools/b382_extract.py'),
    ('the account, the conclusion, the caution, the open items', 'tools/b382_account.py'),
    ('(R7), the three closing writes, the evidence epilogue and the bank',
     'tools/b382_desk_bank.py'),
    ('the registration gate', 'tools/b382_reg_gate.py'),
    ('the clause spec', 'tools/b382_regspec.py'),
    ('b380`S BANKED ROWS, RE-READ AND NOT RECALLED', 'tools/b380_rescore.py'),
    ('b381`S CONTROL AND EXEMPLARS, RE-READ AND NOT RECALLED', 'tools/b381_control.py'),
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
    ('the bank leads with the author`s stop', BANK,
     '### ### ### **THE AUTHOR STOPPED THE SEQUENCE, AND THIS ACT CLOSES THE EVIDENCE'),
    ('### a reader and not a predicate', BANK,
     '### ### PREDICATE.**'),
    ('### the conclusion, about method and not a class', BANK,
     '### ### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS:'),
    ('### the limit is stated with the conclusion', BANK,
     '### ### **AND THE LIMIT IS STATED WITH THE CONCLUSION AND NOT BELOW IT: TWO FAILED'),
    ('### the count was re-measured and not carried', BANK,
     '### ### **THE LOAD-BEARING COUNT, RE-MEASURED AND NOT CARRIED:**'),
    ('### a price is not a proposal', BANK,
     '### ### ### **A PRICE IS NOT A PROPOSAL.** ### Priced from the record`s own figures,'),
    ('### the unpriced part is named unpriced', BANK,
     '###   ### **(iii)** ### a phased application : ### **UNPRICED, AND NAMED UNPRICED'),
    ('### the exemplar caution', BANK,
     '### ### **THE EXEMPLAR CAUTION.** ### `b381`s gathering set came from a matcher'),
    ('### the open items restated', BANK,
     '### ### **THE OPEN ITEMS, RESTATED FOR THE RULING:** ### the four lists, ### **OPEN BY'),
    ('### nothing closed except the sequence', BANK,
     '### ### ### **NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF.**'),
    ('### the untracked records named and still untracked', BANK,
     '### ### **THE TEN UNTRACKED RUN RECORDS OF EARLIER ACTS, NAMED AND STILL UNTRACKED:**'),
    ('### naming them is the whole of what this act does', BANK,
     '### ### DOES ABOUT THEM** -- so a later act does not rediscover them as a defect.'),
    ('### the tool cap was mis-described and reported', BANK,
     '### ### **AND THIS ACT`S OWN LOCKED FACE MIS-DESCRIBED ITS TOOL CAP.** ### The face'),
    ('### the face stands and the contradiction is reported', BANK,
     '### ### **THE CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED**, which is what'),
    ('### an act that closes evidence states the limit with the conclusion', BANK,
     '### ### ### **NEW -- `AN ACT THAT CLOSES EVIDENCE MUST STATE THE LIMIT WITH THE'),
    ('### a cap is a number, not a list', BANK,
     '### ### ### **NEW -- `A CAP IS A NUMBER, NOT A LIST`.** ### This act`s own face capped'),
    ('### six tools and no shared utility', BANK,
     '### ### **SIX NEW `relay` TOOLS AGAINST A CAP OF SIX, AND NO SHARED UTILITY:** ### this'),
    ('the evidence file is named complete', EVID,
     '### ### ### **THIS FILE IS COMPLETE AS THIS SEQUENCE`S PRODUCT.** ### It is not'),
    ('the evidence file leaves the ruling the author`s', EVID,
     '### ### **THE RULING IS THE AUTHOR`S AND NOTHING HERE MAKES IT.**'),
]

MUST_FAIL = [
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a declaration was moved', BANK, '### A DECLARATION WAS MOVED.'),
    ('the bank never says a list was closed', BANK, '### A LIST WAS CLOSED.'),
    ('the bank never says the declaration rule is ordered', BANK,
     '### THE DECLARATION RULE IS ORDERED.'),
    ('the bank never names a preferred option', BANK, '### THE PREFERRED OPTION IS.'),
    ('the bank never says a quotation did not re-read', BANK, '### A QUOTATION DID NOT RE-READ.'),
    ('the bank never says the evidence file was rewritten', BANK,
     '### THE EVIDENCE FILE WAS REWRITTEN.'),
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
    print('b382 -- GATE SUITE (THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED)')
    print('=' * 100)
    E, LG, AC, Q = _J['E'], _J['LG'], _J['AC'], _J['Q']
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    C81 = json.load(io.open(d('b381_control.json'), encoding='utf-8'))
    EX81 = json.load(io.open(d('b381_exemplars.json'), encoding='utf-8'))
    VD81 = json.load(io.open(d('b381_verdict.json'), encoding='utf-8'))
    RS80 = json.load(io.open(d('b380_rescore.json'), encoding='utf-8'))
    P75 = json.load(io.open(d('b375_population.json'), encoding='utf-8'))
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
    l7 = LG['act'] == 'b382' and not os.path.exists(t('b382_lockgate.py'))
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8 and l8 and l8
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
    # ### ### **EVERY QUOTED LINE RE-READ HERE, INDEPENDENTLY OF THE TOOL THAT WROTE THE ACCOUNT.**
    # ### An account that misquotes its sources is worse than no account.
    quoted = [b for b in E['built'] if b['tag'] in ('SEQ', 'CAUTION', 'EVID')]
    bad = []
    for b in quoted:
        src = d(b['file'])
        if not os.path.exists(src):
            bad.append((b['file'], 'missing'))
            continue
        ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        if b['line'] - 1 >= len(ls) or ls[b['line'] - 1].rstrip(chr(13)) != b['text']:
            bad.append((b['file'], b['line']))
    q1 = not bad
    q2 = AC['reread_ok'] is True and not AC['reread_failures']
    # ### **AND EVERY QUOTED LINE MUST ACTUALLY APPEAR IN THE ACCOUNT**, or it was read and dropped.
    inaccount = sum(1 for b in quoted if b['text'].strip()[:80] in acrun)
    q3 = inaccount >= len([b for b in E['built'] if b['tag'] == 'SEQ'])
    q4 = len(quoted) >= 25
    gq = q1 and q2 and q3 and q4
    print('    ### **QUOTED LINES RE-READ INDEPENDENTLY : %d ; FAILURES : %d** %s'
          % (len(quoted), len(bad), bad[:3] or ''))
    print('    the tool`s own re-read agrees : %s' % q2)
    print('    quoted lines actually present in the account : %d of %d' % (inaccount, len(quoted)))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-REREAD')

    # --------------------------------------------------------------- BAR 3, THE ANCHORED-CLAIM BAR
    print(chr(10) + '  G-ANCHORED / G-COVERAGE (BAR 3):')
    ACTS = ('b375', 'b376', 'b377', 'b378', 'b379', 'b380', 'b381')
    missing_acts = [a for a in ACTS if a not in acrun]
    a1 = not missing_acts and AC['acts_covered'] == len(ACTS)
    # ### ### **THE FIVE THINGS THE ORDER NAMES BY NAME, EACH CARRIED BY A QUOTED LINE.**
    NAMED = [
        ('the three tests and their crossing', 'THREE TESTS CROSSES THE QUADRANTS'),
        ('the definition`s drift between statement and operation',
         'DROPS CLAUSE `(iii)` ENTIRELY AND ADDS A SIZE FLOOR'),
        ('four widenings and none of the role column',
         'LEAVES THE ROLE COLUMN EXACTLY WHERE IT'),
        ('the two structural features and the control that could fail',
         'INDEPENDENT STRUCTURAL FEATURES NOW FAIL THE SAME DISTINCTION'),
        ('the standing count of documents that do not state what they are',
         '340 OF 349 DOCUMENTS'),
    ]
    missing_named = [lbl for lbl, needle in NAMED if needle not in acrun]
    a2 = not missing_named
    # ### **AND EACH ACT IS GIVEN ALL THREE HEADINGS THE ORDER ASKED FOR.**
    a3 = acrun.count('**ASKED:**') >= len(ACTS) and acrun.count('**FOUND:**') >= len(ACTS)
    a4 = acrun.count('**LEFT:**') >= 4
    ga = a1 and a2 and a3 and a4
    print('    acts named in the account : %d of %d %s'
          % (len(ACTS) - len(missing_acts), len(ACTS), missing_acts or ''))
    print('    ### **THE FIVE THINGS THE ORDER NAMES, MISSING : %s**' % (missing_named or 'none'))
    print('    ASKED/FOUND/LEFT headings : %d / %d / %d'
          % (acrun.count('**ASKED:**'), acrun.count('**FOUND:**'), acrun.count('**LEFT:**')))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORED/G-COVERAGE')

    # ------------------------------------------------------------ BAR 4, THE RE-MEASURED-COUNT BAR
    print(chr(10) + '  G-REMEASURED / G-THREEREADINGS (BAR 4):')
    # ### **RECOMPUTED HERE FROM THE SOURCE JSONS, NOT TRUSTED FROM THE ACCOUNT.**
    r1 = AC['population'] == RS80['population']
    r2 = AC['strict_silent'] == RS80['statement_tally'].get('A?', 0)
    r3 = AC['broad_silent'] == RS80['statement_broad_tally'].get('A?', 0)
    r4 = AC['b381_wide'] == EX81['wide_hits'] and AC['b381_scanned'] == EX81['scanned']
    # ### ### **ALL THREE READINGS PRINTED TOGETHER, AND THE CONCLUSION SURVIVES THE MOST GENEROUS.**
    r5 = all(str(x) in bank for x in (AC['strict_silent'], AC['broad_silent'], AC['b381_wide']))
    most_generous = float(AC['b381_wide']) / AC['b381_scanned']
    r6 = AC['generous_minority'] == (most_generous < 0.5)
    r7 = AC['generous_minority'] is True
    gr = r1 and r2 and r3 and r4 and r5 and r6 and r7
    print('    the three readings recompute from their own JSONs : %s / %s / %s' % (r2, r3, r4))
    print('    ### **ALL THREE ARE IN THE BANK** : %s' % r5)
    print('    ### **THE MOST GENEROUS IS %.1f%% AND THE CONCLUSION SURVIVES IT : %s**'
          % (100.0 * most_generous, r7))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-REMEASURED/G-THREEREADINGS')

    # ----------------------------------------------------------------- BAR 5, THE NO-ORDER BAR
    print(chr(10) + '  G-NOORDER / G-PRICED (BAR 5):')
    o_start = bank.find('### WHAT A DECLARATION RULE WOULD OBLIGE')
    o_end = bank.find('### ### **THE EXEMPLAR CAUTION.**')
    region = bank[o_start:o_end] if (o_start >= 0 and o_end > o_start) else ''
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append(m.group(0))
    print('    ### raw preference-word hits in the priced region : %s' % (sorted(set(raw)) or 'none'))
    p1 = not live and bool(region)
    p2 = AC['declaration_rule_ordered'] is False and AC['class_ruled'] is False
    p3 = 'A PRICE IS NOT A PROPOSAL' in bank
    # ### ### **AND THE PART THE RECORD CANNOT PRICE IS NAMED UNPRICED RATHER THAN ESTIMATED.**
    p4 = 'UNPRICED, AND NAMED UNPRICED' in bank and AC['phased_application_priced'] is False
    # ### **THE PRICES THAT ARE GIVEN COME FROM THE RECORD**, recomputed here.
    declared = P75['declared'] if isinstance(P75['declared'], int) else len(P75['declared'])
    notdecl = (P75['not_declared'] if isinstance(P75['not_declared'], int)
               else len(P75['not_declared']))
    p5 = AC['declared_class_line'] == declared and AC['not_declared_class_line'] == notdecl
    p6 = str(notdecl) in bank
    gpo = p1 and p2 and p3 and p4 and p5 and p6
    print('    live preference words : %d ; rule ordered : %s ; class ruled : %s'
          % (len(live), AC['declaration_rule_ordered'], AC['class_ruled']))
    print('    ### **A PRICE IS NOT A PROPOSAL** : %s ; ### **THE UNPRICED PART IS NAMED** : %s'
          % (p3, p4))
    print('    the prices recompute from b375`s population : %s (%d declare, %d do not)'
          % (p5, declared, notdecl))
    print('    %s' % ('PASS' if gpo else '### FAIL ###'))
    if not gpo:
        fails.append('G-NOORDER/G-PRICED')

    # ------------------------------------------------------- BAR 6, THE EVIDENCE-EPILOGUE BAR
    print(chr(10) + '  G-EPILOGUE / G-NOEDITEVID (BAR 6):')
    ev = io.open(EVID, encoding='utf-8').read()
    e1 = Q['evidence_appended'] is True
    e2 = Q['evidence_placeholders'] == 0
    # ### ### **NOTHING ABOVE THE APPENDED BLOCK MOVED**: the committed blob is still a true prefix.
    evblob = blob_of(ROOT, 'data/b380_ruling_evidence.txt')
    e3 = (evblob is not None) and norm(ev).startswith(norm(evblob).rstrip(chr(10)))
    e4 = 'THIS FILE IS COMPLETE AS THIS SEQUENCE`S PRODUCT' in ev
    e5 = 'COMPLETE' in ev and 'THE SEQUENCE ADDS NOTHING FURTHER TO IT' in ev
    e6 = 'THE RULING IS THE AUTHOR`S AND NOTHING HERE MAKES IT' in ev
    # ### **AND b381'S BLOCK IS STILL THERE, UNEDITED** -- the file is closed, not rewritten.
    e7 = '### b381 -- (R14), AND THE SECOND STRUCTURAL FEATURE THAT DOES NOT READ ROLE.' in ev
    ge = e1 and e2 and e3 and e4 and e5 and e6 and e7
    print('    appended, not rewritten : %s ; placeholders : %d' % (e1, Q['evidence_placeholders']))
    print('    ### **THE COMMITTED BLOB IS STILL A TRUE PREFIX** : %s' % e3)
    print('    named complete as this sequence`s product : %s / %s' % (e4, e5))
    print('    the ruling is left the author`s : %s ; b381`s block intact : %s' % (e6, e7))
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-EPILOGUE/G-NOEDITEVID')

    # ---------------------------------------------------------------- BAR 7, THE CAUTION BAR
    print(chr(10) + '  G-CAUTION / G-NOTHINGRESTS (BAR 7):')
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    tblk_early = tblk
    c1 = 'RE-DERIVED AND NOT INHERITED' in bank
    c2 = 're-derived and not inherited' in gate_text.flat(tblk_early).lower()
    c3 = 'RE-DERIVED AND NOT INHERITED' in ev
    # ### ### **THE CLAIM THAT NOTHING RESTS ON THE SET IS CHECKED AGAINST b381'S RECORD.**
    c4 = (C81['corpus_scored'] is False and C81['adopted'] is False
          and VD81['prior_scores_overwritten'] == 0)
    c5 = AC['nothing_rests_on_the_set'] == c4
    c6 = all(str(x) in bank for x in (EX81['loose_hits'], EX81['loose2_hits'], EX81['wide_hits']))
    gc = c1 and c2 and c3 and c4 and c5 and c6
    print('    the caution is in the bank, the trail block and the evidence file : %s / %s / %s'
          % (c1, c2, c3))
    print('    ### **NOTHING RESTS ON IT, CHECKED AGAINST b381`S JSON** : %s (recorded %s)'
          % (c4, AC['nothing_rests_on_the_set']))
    print('    all three matcher counts are in the bank : %s' % c6)
    print('    %s' % ('PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-CAUTION/G-NOTHINGRESTS')

    # ------------------------------------------------------------- BAR 8, THE OPEN-ITEMS BAR
    print(chr(10) + '  G-OPEN / G-CLOSEDONE (BAR 8):')
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    deskrun = io.open(IDX, encoding='utf-8', errors='replace').read()
    n1 = all(x in deskrun for x in lists)
    n2 = all(x in acrun for x in lists)
    n3 = Q['lists_closed'] == 0
    # ### ### **EXACTLY ONE DESK CLOSURE, AND IT IS THE SEQUENCE.**
    n4 = Q['closed'] == 1 and all('sequence' in c['item'] for c in Q['closed_items'])
    n5 = 'NOTHING IS CLOSED BY THIS ACT EXCEPT THE SEQUENCE ITSELF' in bank
    # ### **THE OTHER THREE OPEN ITEMS, EACH RESTATED.**
    n6 = 'registry drift' in bank.lower() and 'THE AUTHOR' in bank
    n7 = str(AC['clusters_without_keystone']) in bank and 'NO KEYSTONE' in bank
    n8 = 'A FLOOR AGAINST THE WIDER' in bank
    gn = n1 and n2 and n3 and n4 and n5 and n6 and n7 and n8
    print('    the four lists named in the desk run and in the account : %s / %s' % (n1, n2))
    print('    ### **LISTS CLOSED : %d ; DESK CLOSED : %d, AND IT IS THE SEQUENCE : %s**'
          % (Q['lists_closed'], Q['closed'], n4))
    print('    the drift, the clusters and the floor each restated : %s / %s / %s' % (n6, n7, n8))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-OPEN/G-CLOSEDONE')

    # ------------------------------------------------------- BAR 9, THE UNTRACKED-RECORDS BAR
    print(chr(10) + '  G-UNTRACKED (BAR 9):')
    named = E['untracked']
    still = set(x[3:].strip() for x in git(ROOT, 'status', '--porcelain').split(chr(10))
                if x.startswith('??'))
    committed = [u for u in named if u not in still]
    u1 = not committed
    u2 = len(named) >= 10
    u3 = all(u in bank for u in named)
    u4 = 'NAMED AND STILL UNTRACKED' in bank
    gu = u1 and u2 and u3 and u4
    print('    named as untracked : %d ; ### **STILL UNTRACKED : %d ; COMMITTED BY THIS ACT : %d**'
          % (len(named), len(named) - len(committed), len(committed)))
    if committed:
        print('        ### ### **THESE WERE NAMED AND THEN COMMITTED : %s**' % committed[:5])
    print('    every one of them is named in the bank : %s' % u3)
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNTRACKED')

    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b382' not in x and x != 'tools/banked_index.py'
                     and x != 'data/b380_ruling_evidence.txt')
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
    c_start = bank.find('### ### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD')
    c_end = bank.find('### THE ACCOUNT, THE CONCLUSION, THE CAUTION AND THE OPEN ITEMS.')
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
    k3 = 'EVIDENCE AND NOT PROOF' in bank
    # ### **THE RELATING-WORD FEATURE WAS NOT BUILT AND NOT BUILT UNDER ANOTHER NAME.**
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b382_') and x.endswith('.py')))
    relating = [x for x in mymods0
                if any(w in strip_prose(t(x)).lower()
                       for w in ('whereas', 'contradicts', 'follows from', 'relating_word'))]
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
    t3 = len(rws) == 1 and anc and 'THE EVIDENCE SEQUENCE CLOSED' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-sequence-stopped-and-the-evidence-closed returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the declarations are moved',
              'the declaration rule is ordered', 'the registry is edited'))
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
    R375 = d('b381_registration_2026-09-09.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b380_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b380`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b381`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b382_hooks.txt'), d('b382_mirror.txt')
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
        ('acts accounted for %d' % AC['acts_covered'], str(AC['acts_covered']) in bank),
        ('quotations failing to re-read %d' % len(AC['reread_failures']),
         str(len(AC['reread_failures'])) in bank),
        ('the population %d' % AC['population'], str(AC['population']) in bank),
        ('strict silent %d' % AC['strict_silent'], str(AC['strict_silent']) in bank),
        ('broad silent %d' % AC['broad_silent'], str(AC['broad_silent']) in bank),
        ('b381 purpose hits %d' % AC['b381_wide'], str(AC['b381_wide']) in bank),
        ('b381 scanned %d' % AC['b381_scanned'], str(AC['b381_scanned']) in bank),
        ('documents lacking a class line %d' % AC['not_declared_class_line'],
         str(AC['not_declared_class_line']) in bank),
        ('clusters without a keystone %d' % AC['clusters_without_keystone'],
         str(AC['clusters_without_keystone']) in bank),
        ('the matcher lineage v1 %d' % EX81['loose_hits'], str(EX81['loose_hits']) in bank),
        ('the matcher lineage v2 %d' % EX81['loose2_hits'], str(EX81['loose2_hits']) in bank),
        ('the matcher lineage v3 %d' % EX81['wide_hits'], str(EX81['wide_hits']) in bank),
        ('synthesis declarers %d' % C81['synthesis_n'], str(C81['synthesis_n']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on account run', AC['run_file'] in bank),
        ('the relied-on extract run', E['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('account', AC), ('desk_bank', Q)):
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
                          if x.startswith('b382_') and x.endswith('.py')))
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
              if x.strip() and 'b382' not in x and x.strip() not in DECLARED]
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
             d('b382_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b382_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries seven prior banks' own lines"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the account IS quotations from seven prior banks"),
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

    marker = '# ### THE SEQUENCE STOPPED, AND THE EVIDENCE CLOSED (b382).'
    nxt = '# ### THE CONTROL REBUILT, AND CO-LOCATION TESTED (b381).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b382_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT SIX NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 6 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    ### ### **AND THE FACE`S OWN CLAUSE DESCRIPTION NAMED SEVEN ROLES AGAINST A DEMAND')
    print('    ### ### OF SIX.** ### The cap is the NUMBER: the desk sweeper and the bank writer')
    print('    ### are one file. ### **THE CONTRADICTION IS REPORTED IN THE BANK RATHER THAN')
    print('    ### ### QUIETLY EXCEEDED** : %s'
          % ('CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED' in bank))
    gcap = gcap and ('CONTRADICTION IS REPORTED RATHER THAN QUIETLY EXCEEDED' in bank)
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b382_hedge_')
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
