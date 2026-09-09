# -*- coding: utf-8 -*-
"""b389_checks.py -- THE GATE SUITE FOR THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED
### REPOSITORY.

### ### **THE ARM THAT MATTERS MOST IS `G-NOSUBST`.** ### The order sent this act to the platform
### and the platform did not answer. ### The corpus`s own record of what it has deposited sits on
### disk, one read away, and would have produced a confident-looking answer to `(F2)`.
### ### ### **A RECOLLECTION DRESSED AS A LIVE READ IS THE WORST OUTCOME AVAILABLE TO THIS ACT**,
### ### ### and the arm proves the substitution did not happen.
###
### ### **`G-PROVED` AND `G-CONTROL` PAY `b378`'S PRICE.** ### An absence needs a proved search:
### every route recorded with its code and byte count, and ### **A POSITIVE CONTROL THAT ANSWERS**,
### so the record shows the platform was asked rather than that the act did not ask.
###
### ### **`G-READONLY` AND `G-NOZENODOWRITE` PROVE THE STANDING CLAUSE MECHANICALLY.** ### No
### `POST`, `PUT`, `PATCH`, `DELETE`, no `-X`, no `--data` and no token anywhere in this act`s own
### code. ### **THE CLAUSE IS NOT ASSERTED; IT IS MEASURED.**
###
### ### **`G-HEADSKEPT` AND `G-MAPHEADONLY` GUARD `(R18)`'S BOUNDARY**, and they diff against
### ### **THE PRE-ACT BLOB** ### rather than within the run -- `b388`'s `G-PRESERVED` read `False`
### on an idempotent re-run for exactly that reason. ### **AN ARM MUST MEASURE THE SAME THING ON
### ### EVERY RUN** (`b352`).
###
### ### **AND `G-WITHDRAWN` IS AN ARM AGAINST THIS SEAT.** ### It requires the bank to say, in
### whole lines, that `b388`'s finding was wrong and why -- because ### **A SEAT THAT CORRECTS A
### ### PRIOR ACT'S ERROR BY QUIETLY REPORTING A DIFFERENT ANSWER HAS HIDDEN THE ERROR INSIDE THE
### ### CORRECTION**, and this act must also say it about ### **ITS OWN LOCKED FACE.**
###
### ### **EVERY `G-NO*`-SHAPED ARM READS STRIPPED CODE OR WHAT A TOOL PRINTS, NEVER RAW PROSE**
### (`b348`, `b373`) -- ### **BUT A POSITIVE ARM READS THE CODE ITSELF** (`b386`). ### **A RUN
### ### FILE IS RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`).
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


BANK = d('b389_the_look_see.txt')
REG = d('b389_registration_2026-09-09.txt')
FERRY = d('b389_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b389_ferry_scan.txt'), d('b389_reg_termscan.txt'), d('b389_reg_gate.txt')
CENSUS0, FCEN = d('b389_census_stepzero.txt'), d('b389_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b389_regspec_run.txt'), d('audit_b389_reg_satisfiable.txt')
PINS0 = d('b389_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
NOTE_MARK = '<!-- b389 (R18) HEAD NOTE -- TWO MAPS, TWO KEYS, 2026-09-09 -->'
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = '2aba01833be61e8ceae0be51ef5ac5699e75cc361b7140072b4cc31ebab7dacd'
ROWNUM = '238'
TRAIL_MARK = '<!-- b389 the look-see, the deposited layer, and the unreached repository; (R18) -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b389_components.json'), ('LG', 'b389_lockgate.json'),
                   ('E', 'b389_reads.json'), ('Q', 'b389_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b389_regspec.py', 'tools/b389_reg_gate.py', 'tools/b389_extract.py',
                'tools/b389_components.py', 'tools/b389_desk_bank.py', 'tools/b389_checks.py'}

TOOLNUM = [
    ('the extract, and the three surveys inside it', 'tools/b389_extract.py'),
    ('components 1, 2 and 3', 'tools/b389_components.py'),
    ('component 4, (R7), the three closing writes and the bank', 'tools/b389_desk_bank.py'),
    ('the registration gate', 'tools/b389_reg_gate.py'),
    ('the clause spec, with three clauses measured and not typed', 'tools/b389_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY,
     'ACT b389 — THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED'),
    ('the ruling (R18) -- two maps, two keys', FERRY,
     'strikeable: TWO MAPS, TWO KEYS. A CLUSTER map keys on subjects'),
    ('the ruling (R18) -- what a constellation map keys on', FERRY,
     'and domains. A CONSTELLATION map keys on interrelated verified'),
    ('the ruling (R18) -- which map is which', FERRY,
     'kernels that carry them. The federation map is the cluster map;'),
    ('the order -- component 1, more than six, and subjects the map does not carry', FERRY,
     "map's table as now refreshed. Report whether more than six"),
    ('the order -- the closing, the constellation map`s currency entered not opened', FERRY,
     "constellation map's own currency entered as an item (five named"),
]

SELF_NEEDLES = [
    ('the bank leads with the ruling', BANK,
     '### ### ### **THE AUTHOR RULED `(R18)`: TWO MAPS, TWO KEYS.**'),
    ('### the three populations are never added', BANK,
     '### ### ### **THE THREE ARE NEVER ADDED AND NO AVERAGE IS TAKEN.**'),
    ('### a 200 carrying an empty result is an empty result', BANK,
     "### ### ### **A `200` CARRYING AN EMPTY RESULT IS AN EMPTY RESULT**, and `b378`'s"),
    ('### (F2) is untested and not guessed', BANK,
     '### ### ### **SO `(F2)` IS `UNTESTED`: NEITHER MET NOR REFUTED.**'),
    ('### nothing substituted from the corpus', BANK,
     '### The order said ### **READ LIVE**, and ### **NO FIGURE IN THAT HALF WAS SOURCED'),
    ('### a recollection dressed as a live read', BANK,
     '### ### **A RECOLLECTION DRESSED AS A LIVE READ WOULD HAVE BEEN THE WORST OUTCOME'),
    ('### the two laws quoted and named as not it', BANK,
     '### ### **BOTH ARE QUOTED AT THEIR OWN LINES SO THE READING CAN BE OVERTURNED.**'),
    ('### the seat did not write the missing rule', BANK,
     '### ### SEAT THAT SUPPLIES THE WORDS HAS WRITTEN A NEW RULE UNDER AN OLD NAME.**'),
    ('### an unauthenticated read cannot tell absent from private', BANK,
     '### ### UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE** -- this seat`s own'),
    ('### all three branches leave the document correct', BANK,
     '### ### **ALL THREE BRANCHES -- ABSENT, PRIVATE, UNDECIDABLE -- LEAVE THE CITING'),
    ('### b388`s finding is withdrawn', BANK,
     "### ### ### **SO `b388`'S FINDING IS WITHDRAWN.**"),
    ('### a predicate that knows one shape', BANK,
     '### ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, and here it found'),
    ('### the answer was on disk and the instrument walked past it', BANK,
     '### ### kernels.* ### **THE ANSWER WAS ON DISK AND THE INSTRUMENT WALKED PAST IT.**'),
    ('### the map row is routed and not repaired', BANK,
     '### ### SAME REASON AND THIS ACT DOES NOT TOUCH IT.** ### `(R18)` adds a head note'),
    ('### the head note replaces nothing', BANK,
     '### ### ### ADDED BENEATH THEM AND REPLACES NOTHING.**'),
    ('### this act`s own face carried a wrong figure', BANK,
     "### ### **AND THIS ACT`S OWN LOCKED FACE CARRIED A WRONG FIGURE.**"),
    ('### the locked face is not edited', BANK,
     '### ### **THE LOCKED FACE IS NOT EDITED.** ### Both figures are printed, here and in'),
    ('### (E2) is reported part-refuted rather than re-read to fit', BANK,
     '###   ### **REPORTED AS PART-REFUTED RATHER THAN RE-READ TO FIT.**'),
]

MUST_FAIL = [
    ('the bank never says a cluster was added to the map', BANK,
     '### A CLUSTER WAS ADDED TO THE MAP.'),
    ('the bank never says the layer was enumerated', BANK,
     '### THE DEPOSITED LAYER WAS ENUMERATED.'),
    ('the bank never says a deposit rule was written', BANK, '### A DEPOSIT RULE WAS WRITTEN.'),
    ('the bank never says the citing document was wrong', BANK,
     '### THE CITING DOCUMENT WAS WRONG.'),
    ('the bank never says a prior head was replaced', BANK, '### A PRIOR HEAD WAS REPLACED.'),
    ('the bank never says a record was read from the corpus instead', BANK,
     '### A RECORD WAS READ FROM THE CORPUS INSTEAD.'),
    ('the bank never says something was written at Zenodo', BANK,
     '### SOMETHING WAS WRITTEN AT ZENODO.'),
    ('the bank never says b388 was right about the kernel', BANK,
     '### b388 WAS RIGHT ABOUT THE KERNEL.'),
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
        if not subj.startswith('b389'):
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
    print('b389 -- GATE SUITE (THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED REPOSITORY)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    C1, C2, C3 = AC['c1'], AC['c2'], AC['c3']
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
    l7 = LG['act'] == 'b389' and not os.path.exists(t('b389_lockgate.py'))
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

    C4 = Q['C4']
    maptxt = io.open(MAP, encoding='utf-8', errors='replace').read()
    consttxt = io.open(CONSTMAP, encoding='utf-8', errors='replace').read()

    # ------------------------------------------------------------ BAR 2, THE THREE-POPULATION BAR
    print(chr(10) + '  G-THREEPOP / G-NOADD (BAR 2):')
    # ### **THE THREE FIGURES MUST BE REPORTED AND MUST NOT BE ADDED.** ### The arm looks for each
    # ### separately in the bank and requires their sum to be absent as a figure.
    p1 = C1['disk'] == 8 and C1['reg'] == 6 and C1['map'] >= 1
    p2 = C1['nests'] is False
    p3 = ('ON DISK : `%d`' % C1['disk']).upper() in bu and ('SUPPORT TIER : `%d`'
                                                           % C1['reg']).upper() in bu
    total = C1['disk'] + C1['reg'] + C1['map']
    p4 = ('`%d` CLUSTER SYNTHESES' % total) not in bu and ('TOTAL OF %d' % total) not in bu
    # ### **AND NOTHING WAS ADDED TO EITHER MAP`S TABLE.** ### Measured on the cluster table`s own
    # ### row count, before and after, from the pre-act blob.
    pre_map = blob_of(PP, 'SPIRAL_MAP.md', preact(PP)) or ''
    rows_before = len([x for x in norm(pre_map).splitlines()
                       if x.startswith('|') and x.count('|') >= 5])
    rows_after = len([x for x in norm(maptxt).splitlines()
                      if x.startswith('|') and x.count('|') >= 5])
    p5 = rows_before == rows_after
    p6 = E['syn_on_disk'] == C1['disk']
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    ### **DISK %d / REGISTRY %d / MAP %d, EACH REPORTED ON ITS OWN : %s**'
          % (C1['disk'], C1['reg'], C1['map'], p3))
    print('    the populations do not nest : %s ; their sum never appears as a figure : %s'
          % (p2, p4))
    print('    ### **TABLE ROWS IN THE MAP : %d BEFORE, %d AFTER -- NOTHING ADDED : %s**'
          % (rows_before, rows_after, p5))
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-THREEPOP/G-NOADD')

    # ------------------------------------------------------------- BAR 3, THE PROVED-ABSENCE BAR
    print(chr(10) + '  G-PROVED / G-CONTROL (BAR 3):')
    probes = E['probes']
    r1 = len(probes) >= 6
    r2 = all(('code' in x and 'bytes' in x) for x in probes)
    r3 = E['routes_answering'] == 0 and C2['routes_answering'] == 0
    r4 = str(E['control'].get('code')) == '200'
    r5 = len(E['dois']) == C2['dois'] == 17 and C2['records'] == 0
    r6 = 'POSITIVE CONTROL' in bu and 'THE NETWORK IS NOT THE CAUSE' in bu
    gr = r1 and r2 and r3 and r4 and r5 and r6
    print('    routes probed with code and byte count : %d ; answering : %d'
          % (len(probes), E['routes_answering']))
    print('    ### **THE POSITIVE CONTROL RETURNED %s** ### -- so the platform was asked : %s'
          % (E['control'].get('code'), r4))
    print('    DOIs swept %d ; records enumerated %d' % (C2['dois'], C2['records']))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-PROVED/G-CONTROL')

    # --------------------------------------------------------- BAR 4, THE NO-SUBSTITUTION BAR
    print(chr(10) + '  G-NOSUBST (BAR 4) ### THE ARM THAT MATTERS MOST:')
    s1 = C2['f2'] == 'UNTESTED'
    s2 = 'NEITHER MET NOR REFUTED' in bu
    # ### **NO FIGURE IN THE LIVE HALF IS SOURCED FROM THE CORPUS.** ### The bank must not claim a
    # ### version, a record count or a `is_last` for the platform; and where the corpus`s own claim
    # ### IS reported, it must be labelled as the corpus`s claim.
    s3 = 'LABELLED AS THE CORPUS`S CLAIM AND NOT AS A' in bu
    s4 = 'RECORDS ENUMERATED FROM THE PLATFORM : `3`' not in bu
    s5 = C2['records'] == 0 and 'ENUMERATED' in bu
    s6 = 'A RECOLLECTION DRESSED AS A LIVE READ' in bu
    gs = s1 and s2 and s3 and s4 and s5 and s6
    print('    ### **(F2) IS `%s`, NEITHER MET NOR REFUTED : %s**' % (C2['f2'], s1 and s2))
    print("    the corpus's own claim is reported AND labelled as a claim : %s" % s3)
    print('    ### **THE SUBSTITUTION IS NAMED AS THE WORST AVAILABLE OUTCOME : %s**' % s6)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-NOSUBST')

    # -------------------------------------------------------------- BAR 5, THE RULE-SEARCH BAR
    print(chr(10) + '  G-RULESEARCH (BAR 5):')
    u1 = C2['rule_located'] is False and E['rule_located'] is False
    u2 = len(E['rule_name_hits']) >= 8 and all(v == 0 for v in E['rule_name_hits'].values())
    u3 = len(E['rule_content_hits']) >= 4 and any(v for v in E['rule_content_hits'].values())
    u4 = 'INTERNAL-UNTIL-FRUIT' in bu and 'SEQUENCING LAW' in bu
    u5 = 'AND NEITHER IS ONE' in bu
    u6 = 'AS OBSERVATION AND NEVER AS' in bu
    gu = u1 and u2 and u3 and u4 and u5 and u6
    print('    ### **BY NAME : %d TERMS, ALL RETURNING 0 FILES : %s**'
          % (len(E['rule_name_hits']), u2))
    print('    ### **BY CONTENT : %d PROBES, AND THE HALF THAT FOUND ANYTHING : %s**'
          % (len(E['rule_content_hits']), u3))
    print('    both nearest laws quoted and named as NOT a deposit rule : %s / %s' % (u4, u5))
    print('    the practice is stated as observation and not as rule : %s' % u6)
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-RULESEARCH')

    # ----------------------------------------------------------------- BAR 6, THE WITHDRAWAL BAR
    print(chr(10) + '  G-WITHDRAWN / G-DOCCORRECT (BAR 6) ### AN ARM AGAINST THIS SEAT:')
    v1 = C3['withdrawn'] == 1 and C3['doc_correct'] is True
    v2 = "SO `b388`'S FINDING IS WITHDRAWN" in bu or "SO `B388`'S FINDING IS WITHDRAWN" in bu
    v3 = 'A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE' in bu
    v4 = 'THE ANSWER WAS ON DISK AND THE INSTRUMENT WALKED PAST IT' in bu
    v5 = 'LEAVE THE CITING' in bu and 'CORRECT AS WRITTEN' in bu
    # ### **AND THE SEAT MUST SAY IT ABOUT ITS OWN FACE TOO.**
    v6 = 'OWN LOCKED FACE CARRIED A WRONG FIGURE' in bu
    v7 = 'THE LOCKED FACE IS NOT EDITED' in bu
    # ### **AND THE MAP ROW `b388` WROTE FROM THE SAME MISREADING IS ROUTED, NOT REPAIRED.**
    v8 = 'THIS ACT DOES NOT TOUCH IT' in bu
    gv = v1 and v2 and v3 and v4 and v5 and v6 and v7 and v8
    print('    ### **b388 FINDINGS WITHDRAWN : %d ; THE CITING DOCUMENT CORRECT : %s**'
          % (C3['withdrawn'], C3['doc_correct']))
    print('    the mechanism is named, not just the verdict : %s ; and the answer was on disk : %s'
          % (v3, v4))
    print("    ### **THE SEAT SAYS IT OF ITS OWN LOCKED FACE TOO : %s ; AND DOES NOT EDIT IT : "
          "%s**" % (v6, v7))
    print('    the map row is routed and NOT repaired : %s' % v8)
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-WITHDRAWN/G-DOCCORRECT')

    # ------------------------------------------------------------------ BAR 7, THE HEAD-NOTE BAR
    print(chr(10) + '  G-HEADNOTE / G-HEADSKEPT / G-MAPHEADONLY (BAR 7):')
    h1 = maptxt.count(NOTE_MARK) == 1 and consttxt.count(NOTE_MARK) == 1
    h2 = C4['heads_removed'] == 0 and C4['deleted'] == 0
    # ### **EVERY PRIOR HEAD DECLARATION RE-READ OUT OF THE FILE, AGAINST THE PRE-ACT BLOB.**
    pre_const = blob_of(PP, 'phase1.5/method/THE_LOAD_BEARING_MAP.md', preact(PP)) or ''
    heads = []
    for pre, now in ((pre_map, maptxt), (pre_const, consttxt)):
        for ln in norm(pre).splitlines()[:40]:
            if ln.startswith('**DOCUMENT CLASS'):
                heads.append(ln in norm(now))
    h3 = bool(heads) and all(heads)
    # ### **AND NOT ONE LINE OUTSIDE EITHER HEAD BLOCK MOVED.** ### Measured by diffing the body
    # ### below the PURPOSE line against the pre-act blob -- ### **NOT WITHIN THIS RUN** (`b352`).
    def body(x):
        ls = norm(x).split(chr(10))
        k = 0
        for i, ln in enumerate(ls[:60]):
            if ln.startswith('**PURPOSE:**'):
                k = i + 1
        return chr(10).join(ls[k:])
    h4 = body(pre_map) in body(maptxt) and body(pre_const) in body(consttxt)
    h5 = C4['cluster']['deleted'] == 0 and C4['constellation']['deleted'] == 0
    h6 = 'NEITHER MAP IS MERGED INTO THE OTHER' in bu
    h7 = 'ADDED BENEATH THEM AND REPLACES NOTHING' in bu
    gh = h1 and h2 and h3 and h4 and h5 and h6 and h7
    print('    ### **ONE HEAD NOTE PER MAP, MARKED ONCE EACH : %s**' % h1)
    print('    ### **PRIOR HEAD DECLARATIONS RE-READ OUT OF THE FILES : %d OF %d ; REMOVED : %d**'
          % (sum(1 for x in heads if x), len(heads), C4['heads_removed']))
    print('    ### **EVERY LINE BELOW EITHER HEAD BLOCK UNCHANGED AGAINST THE PRE-ACT BLOB : %s**'
          % h4)
    print('    lines deleted from either map : %d ; neither merged : %s' % (C4['deleted'], h6))
    print('    %s' % ('PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-HEADNOTE/G-HEADSKEPT/G-MAPHEADONLY')

    # ------------------------------------------------------------------- BAR 8, THE READ-ONLY BAR
    print(chr(10) + '  G-READONLY / G-NOZENODOWRITE (BAR 8):')
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b389_') and x.endswith('.py')))
    WRITEY = ("'POST'", "'PUT'", "'PATCH'", "'DELETE'", "'-X'", "'--data'", "'-d'",
              'ACCESS_TOKEN', 'access_token', "'--upload-file'", "'-T'")
    whits = [(x, k) for x in mymods1 for k in WRITEY if k in strip_prose(t(x))]
    z1 = not whits
    # ### **AND THE ONLY VERBS THIS ACT`S CODE USES AGAINST THE PLATFORM ARE `curl -sL` GETS.**
    z2 = all('requests.post' not in strip_prose(t(x)) for x in mymods1)
    z3 = 'NOTHING WAS WRITTEN AT ZENODO' in bu or 'NOTHING IS WRITTEN AT ZENODO' in bu
    gz = z1 and z2 and z3
    print('    write-shaped tokens in this act`s stripped code : %s' % (whits or 'none'))
    print('    ### **NO WRITE PATH TO THE PLATFORM EXISTS IN THIS ACT AT ALL : %s**' % (z1 and z2))
    print('    the clause is stated in the bank as well as measured : %s' % z3)
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-READONLY/G-NOZENODOWRITE')

    # ---------------------------------------------------------------------------- G-NOKERNEL
    print(chr(10) + '  G-NOKERNEL:')
    kernelish = ('print axioms', 'lake ', 'LEAN_PATH', '.olean')
    khits = [(x, k) for x in mymods1 for k in kernelish if k in strip_prose(t(x))]
    k1 = not khits
    k2 = 'AN UNAUTHENTICATED READ CANNOT TELL ABSENT FROM PRIVATE' in bu
    gkn = k1 and k2
    print('    kernel-invoking strings in this act`s stripped code : %s' % (khits or 'none'))
    print('    ### **THE LIMIT OF THE UNAUTHENTICATED READ IS STATED : %s**' % k2)
    print('    %s' % ('PASS' if gkn else '### FAIL ###'))
    if not gkn:
        fails.append('G-NOKERNEL')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = ('no list is closed' in tblk.lower()
          and 'which is not a closure' in tblk.lower())
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
                                'phase1.5/method/THE_LOAD_BEARING_MAP.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b389' not in x)
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
    t3 = len(rws) == 1 and anc and 'IS WITHDRAWN AS WRONG' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('two-maps-two-keys-and-the-layer-unread returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('the deposited layer was enumerated', 'a deposit rule was written',
              'the citing document was wrong', 'a cluster was added to the map'))
    t6 = (Q['trail']['says_r18'] and Q['trail']['says_untested']
          and Q['trail']['says_withdrawn'] and Q['trail']['says_own_face']
          and Q['trail']['says_not_widened'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    trail: mark once and append-only : %s ; pre-act blob a true prefix : %s' % (t1, t2))
    print('    row %s present once and a true prefix : %s' % (ROWNUM, t3))
    print('    key read back : %s ; four overreadings NO KEY after : %s' % (t4, t5))
    print('    ### **THE BLOCK NAMES (R18), SAYS (F2) IS UNTESTED, SAYS THE FINDING IS '
          'WITHDRAWN, CORRECTS THIS ACT`S OWN FACE, AND SAYS THE FACE WAS NOT WIDENED** : %s'
          % t6)
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
    mirrorp = d('b389_mirror.txt')
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
        ('syntheses on disk %d' % C1['disk'], str(C1['disk']) in bank),
        ('named in the registry %d' % C1['reg'], str(C1['reg']) in bank),
        ('carried by the map %d' % C1['map'], str(C1['map']) in bank),
        ('zenodo routes answering %d of %d' % (C2['routes_answering'], C2['routes']),
         str(C2['routes']) in bank),
        ('the positive control %d' % C2['control'], str(C2['control']) in bank),
        ('DOIs swept %d' % C2['dois'], str(C2['dois']) in bank),
        ('records enumerated %d' % C2['records'], str(C2['records']) in bank),
        ('corpus citations of the name %d' % E['cites_total'], str(E['cites_total']) in bank),
        ('of which hedged %d' % E['cites_hedged'], str(E['cites_hedged']) in bank),
        ('public repositories %d' % len(E['gh_names']), str(len(E['gh_names'])) in bank),
        ('head notes %d' % C4['notes'], str(C4['notes']) in bank),
        ('prior heads removed %d' % C4['heads_removed'], str(C4['heads_removed']) in bank),
        ('the cluster map bytes %d -> %d'
         % (C4['cluster']['before'], C4['cluster']['after']),
         str(C4['cluster']['before']) in bank and str(C4['cluster']['after']) in bank),
        ('the constellation map bytes %d -> %d'
         % (C4['constellation']['before'], C4['constellation']['after']),
         str(C4['constellation']['before']) in bank
         and str(C4['constellation']['after']) in bank),
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
                          if x.startswith('b389_') and x.endswith('.py')))
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
              if x.strip() and 'b389' not in x and x.strip() not in DECLARED_W]
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
             d('b389_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b389_checks.py'), 'its own fixtures'),
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

    marker = '# ### TWO MAPS TWO KEYS, AND THE LAYER UNREAD (b389).'
    nxt = '# ### THE MAP REFRESHED UNDER (R17) (b388).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b389_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b389_hedge_')
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
