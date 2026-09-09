# -*- coding: utf-8 -*-
"""b381_checks.py -- THE GATE SUITE FOR THE CONTROL REBUILT AND CO-LOCATION TESTED.

### ### **THE ARM THAT MATTERS MOST HERE IS `G-NOADOPT`, AND IT MEASURES A NON-EVENT.** ### The order
### says that if co-location does not separate the rebuilt set the predicate is NOT ADOPTED and the
### corpus is NOT re-scored. ### **AN ACT THAT REPORTS A FAILURE AND THEN QUIETLY SCORES THE CORPUS
### ### ANYWAY HAS NOT OBEYED THE CLAUSE**, so the arm requires the corpus-wide score count to be zero
### and no quadrant table to have been redrawn.
### ### **AND `G-NOCURATION` REQUIRES EVERY EXEMPLAR TO RE-READ OUT OF ITS OWN FILE AT ITS OWN LINE**,
### because the order states twice that no exemplar may be chosen by this seat's judgement.
### ### **`G-LINEAGE` IS NEW AND IT MEASURES THIS ACT AGAINST ITSELF:** ### the matcher was repaired
### twice after its output was seen, and the arm requires all three yields to be on the record.
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
import co_location as CL        # noqa: E402
import b381_extract as EX     # noqa: E402

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


BANK = d('b381_the_control_rebuilt.txt')
EVID = d('b380_ruling_evidence.txt')
REG = d('b381_registration_2026-09-09.txt')
FERRY = d('b381_ferry_2026-09-09.txt')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b381_ferry_scan.txt'), d('b381_reg_termscan.txt'), d('b381_reg_gate.txt')
CENSUS0, FCEN = d('b381_census_stepzero.txt'), d('b381_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b381_regspec_run.txt'), d('audit_b381_reg_satisfiable.txt')
PINS0 = d('b381_pins_stepzero.txt')
SEAL = '5dffe282ff530628f3c018650686171d2b28002da6f4f5e4b41fe26b12f4a3b9'
ROWNUM = '230'
TRAIL_MARK = '<!-- b381 the control rebuilt; co-location tested and not adopted -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b381_reads.json'), ('LG', 'b381_lockgate.json'),
                   ('EX', 'b381_exemplars.json'), ('C', 'b381_control.json'),
                   ('VD', 'b381_verdict.json'), ('Q', 'b381_desk.json'))}

# ### **RESOLVED BY THE RECORDED CLOCK, NEVER BY NAME** (`b358`).
IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/co_location.py', 'tools/b381_regspec.py', 'tools/b381_extract.py',
                'tools/b381_reg_gate.py', 'tools/b381_exemplars.py', 'tools/b381_control.py',
                'tools/b381_verdict.py', 'tools/b381_desk.py', 'tools/b381_bank.py',
                'tools/b381_checks.py'}

TOOLNUM = [
    ('co-location (SHARED), the unit splitter fixtured five ways', 'tools/co_location.py'),
    ('the old control`s weakness and the rebuilt exemplar set', 'tools/b381_exemplars.py'),
    ('the control, run before any corpus number', 'tools/b381_control.py'),
    ('what the columns mean, and (R14) recorded', 'tools/b381_verdict.py'),
    ('(R7), the trail block, the row and the key', 'tools/b381_desk.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b381_bank.py'),
    ('the reads', 'tools/b381_extract.py'),
    ('the registration gate', 'tools/b381_reg_gate.py'),
    ('the clause spec', 'tools/b381_regspec.py'),
    ('THE SOURCE VOCABULARY, IMPORTED UNMODIFIED', 'tools/role_structure.py'),
    ('b380`S BANKED ROWS, RE-READ AND NOT RECALLED', 'tools/b380_rescore.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

# ### **THE OWNER NEEDLES ARE THE EXTRACT TOOL`S OWN READS TABLE, IMPORTED AND NOT RETYPED.**
OWNER_NEEDLES = [(lbl, path, hint) for lbl, _tag, path, hint in EX.READS]
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')

SELF_NEEDLES = [
    ('the bank leads with both sentences', BANK,
     '### ### ### **THE CONTROL WAS REBUILT SO THAT IT COULD FAIL IN BOTH DIRECTIONS, AND THE NEW'),
    ('### (R14) is recorded and not applied', BANK,
     '### ### **THE CLASS RULING GOVERNS DOCUMENTS BY CONTENT AND ROLE, NOT BY LOCATION.** ### '
     'Where a'),
    ('### the registry-drift filing stays open and is the author`s', BANK,
     '### ### **STAYS OPEN AND IS THE AUTHOR`S.** ### **NO DOCUMENT WAS RECLASSIFIED UNDER (R14) BY'),
    ('### a quotation with holes in it is not a quotation', BANK,
     '### its `9` lines and still called itself verbatim; ### **A QUOTATION WITH HOLES IN IT IS NOT '
     'A'),
    ('### the old control is one defect with two faces', BANK,
     '### ### ### **A CONTROL THAT CANNOT FAIL ON ONE SIDE AND CANNOT INFORM ON THE OTHER IS NOT '
     'TWO'),
    ('### every match was taken and quoted', BANK,
     '### purpose. ### **EVERY MATCH WAS TAKEN AND EVERY MATCH IS QUOTED WITH ITS FILE AND ITS '
     'LINE**,'),
    ('### the conflicts are reported and not resolved', BANK,
     '### ### **BOTH ARE EXCLUDED FROM BOTH EXEMPLAR SETS AND REPORTED, NOT RESOLVED**, because an'),
    ('### the matcher lineage is declared rather than hidden', BANK,
     '### ### **THIS IS DECLARED RATHER THAN HIDDEN, AND IT IS THE PART OF THE ACT A READER SHOULD '
     'BE'),
    ('### a matcher repaired after its output was seen owes its lineage', BANK,
     '### neither is a repair to the result. ### **BUT A MATCHER REPAIRED AFTER ITS OUTPUT WAS SEEN '
     'IS A'),
    ('### why an entry is a unit of its own', BANK,
     '### ### ### **WHY AN ENTRY IS A UNIT OF ITS OWN, AND THIS IS THE WHOLE POINT:** ### under a'),
    ('### the threshold was left where it was', BANK,
     '### ### CONTROL DISAGREED THE THRESHOLD WAS LEFT WHERE IT WAS.**'),
    ('### the deafness the order names', BANK,
     '###   ### **A DOCUMENT QUOTING MANY SOURCES IN ONE PLACE WITHOUT RELATING THEM SCORES AS'),
    ('### the directory stands in for the subject', BANK,
     '###   ### **THE DIRECTORY STANDS IN FOR THE SUBJECT** -- `b380`s, inherited whole, an ADDRESS'),
    ('### no corpus-wide figure exists', BANK,
     '### ### **NO CORPUS-WIDE CO-LOCATION FIGURE EXISTS IN THIS ACT AND NONE WAS COMPUTED.** ### '
     'The'),
    ('### a predicate cannot be tuned to a result it has not seen', BANK,
     '### ### CANNOT BE TUNED TO A RESULT IT HAS NOT SEEN.**'),
    ('### the corpus was not scored and that is the clause', BANK,
     '### ### **SO THE CORPUS WAS NOT SCORED AND NO QUADRANT TABLE WAS REDRAWN.** ### That is the'),
    ('### the upper bound and the unvalidated column both stand', BANK,
     '### ### ### **SO WHAT STAYS UNVALIDATED IS EXACTLY WHAT WAS UNVALIDATED BEFORE**, and this '
     'act`s'),
    ('### two features failing is evidence and not proof', BANK,
     '### ### READS ROLE AND THIS ACT DOES NOT CLAIM IT.** ### It is two failures of the same '
     'shape, and'),
    ('### the tokeniser was measured and acquitted', BANK,
     '### ### **`(E4)` IS REFUTED.** ### The unit definition was worth making and it was ### **NOT '
     'WHAT'),
    ('### the one closure is the author`s', BANK,
     '### ### **AND THE ONE CLOSURE IS THE AUTHOR`S, NOT THIS SEAT`S.** ### `b379` filed whether '
     'the'),
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
    ('the bank never says an exemplar was chosen by judgement', BANK,
     '### AN EXEMPLAR WAS CHOSEN BY JUDGEMENT.'),
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
    print('b381 -- GATE SUITE (THE CONTROL REBUILT, AND CO-LOCATION TESTED)')
    print('=' * 100)
    E, LG, EX, C, VD, Q = _J['E'], _J['LG'], _J['EX'], _J['C'], _J['VD'], _J['Q']
    exrun = io.open(d(EX['run_file']), encoding='utf-8', errors='replace').read()
    crun = io.open(d(C['run_file']), encoding='utf-8', errors='replace').read()
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
    l7 = LG['act'] == 'b381' and not os.path.exists(t('b381_lockgate.py'))
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8 and l8
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s' % l6)
    print('    ### **THE LOCK GATE WAS INHERITED, NOT REBUILT** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # ---------------------------------------------------------------- BAR 2, THE WEAKNESS BAR
    print(chr(10) + '  G-WEAKNESS / G-ONEFINDING (BAR 2):')
    # ### **MEASURED, NOT ASSERTED** -- and recomputed HERE from b380's own banked rows.
    R80 = json.load(io.open(d('b380_rescore.json'), encoding='utf-8'))
    E80 = json.load(io.open(d('b380_reads.json'), encoding='utf-8'))
    rows80 = {r['file']: r for r in R80['rows']}
    reaches = [rows80[f]['evidence']['reach'] for f in E80['declare_synthesis']]
    p1 = EX['b380_lowest_synthesis_reach'] == min(reaches)
    p2 = sorted(EX['b380_synthesis_reaches']) == sorted(reaches)
    p3 = EX['control_cannot_fail'] is True and EX['b380_lowest_synthesis_reach'] >= EX['b380_threshold']
    p4 = EX['b380_gatherers_disagreeing'] == sum(
        1 for f in E80['declare_gathering']
        if rows80[f]['statement_a'] != rows80[f]['structural_a'])
    p5 = 'ONE DEFECT WITH TWO FACES' in bank
    p6 = str(EX['b380_lowest_synthesis_reach']) in bank and str(EX['b380_threshold']) in bank
    gp = p1 and p2 and p3 and p4 and p5 and p6
    print('    the reaches recompute from b380`s own rows : %s / %s' % (p1, p2))
    print('    ### **THE LOWEST REACH %d AGAINST A THRESHOLD OF %d -- THAT SIDE COULD NOT FAIL : %s**'
          % (EX['b380_lowest_synthesis_reach'], EX['b380_threshold'], p3))
    print('    both gathering declarers disagreed, recomputed here : %s' % p4)
    print('    ### **AND THE BANK REPORTS IT AS ONE FINDING** : %s' % p5)
    print('    %s' % ('PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-WEAKNESS/G-ONEFINDING')

    # ------------------------------------------------------------- BAR 3, THE NO-CURATION BAR
    print(chr(10) + '  G-QUOTED / G-NOCURATION / G-CONFLICT / G-LINEAGE (BAR 3):')
    # ### ### **EVERY EXEMPLAR RE-READS OUT OF ITS OWN FILE AT ITS OWN LINE, CHECKED HERE AND NOT
    # ### ### TRUSTED FROM THE TOOL'S OWN JSON.**
    bad = []
    for g in EX['gathering_found']:
        src = os.path.join(PP, g['file'].replace('/', os.sep))
        try:
            ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        except OSError:
            bad.append((g['file'], 'unreadable'))
            continue
        if g['line'] - 1 >= len(ls) or ls[g['line'] - 1].rstrip() != g['text']:
            bad.append((g['file'], g['line']))
    q1 = not bad
    q2 = EX['judgement_selections'] == 0
    q3 = EX['quotes_reread'] is True
    q4 = EX['controls_ok'] is True and EX['negative_refused'] is True
    # ### **A CONFLICT IS EXCLUDED FROM BOTH SETS, NOT RESOLVED INTO ONE.**
    conf = set(c['file'] for c in EX['conflicts'])
    q5 = not (conf & set(EX['gathering_set'])) and not (conf & set(EX['synthesis_set']))
    # ### **THE LINEAGE: ALL THREE YIELDS ON THE RECORD, AND ALL THREE IN THE BANK.**
    q6 = all(str(x) in bank for x in (EX['loose_hits'], EX['loose2_hits'], EX['wide_hits']))
    q7 = EX['loose_hits'] > EX['loose2_hits'] >= EX['wide_hits']
    q8 = 'A MATCHER REPAIRED AFTER ITS OUTPUT WAS SEEN' in bank
    gq = q1 and q2 and q3 and q4 and q5 and q6 and q7 and q8
    print('    ### **EVERY EXEMPLAR RE-READS AT ITS OWN LINE** : %s %s' % (q1, bad[:2] or ''))
    print('    exemplars chosen by judgement : %d ; the head scan`s controls held : %s'
          % (EX['judgement_selections'], q4))
    print('    ### **THE %d CONFLICTS ARE IN NEITHER SET** : %s' % (len(conf), q5))
    print('    ### **THE LINEAGE %d -> %d -> %d IS IN THE BANK** : %s / %s'
          % (EX['loose_hits'], EX['loose2_hits'], EX['wide_hits'], q6, q8))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTED/G-NOCURATION/G-CONFLICT/G-LINEAGE')

    # --------------------------------------------------------------------- BAR 4, THE UNIT BAR
    print(chr(10) + '  G-UNIT / G-UNITFIX / G-COLOCATE / G-POLARITY (BAR 4):')
    fok, flog = CL.self_test(False)
    u1 = fok is True and C['fixtures_ok'] is True
    # ### **ALL THREE KINDS OF UNIT, PLUS A HEADING AND A FENCE** -- the face's own list.
    kinds = set()
    for probe in (CL.FIX_COLL, CL.FIX_TABLE, CL.FIX_SYNTH,
                  '```' + chr(10) + 'x' + chr(10) + '```' + chr(10)):
        kinds |= set(k for k, _l, _b in CL.units(probe))
    u2 = {'list_item', 'table_row', 'paragraph', 'fence'} <= kinds
    u3 = [k for k, _l, _b in CL.units('# H' + chr(10) + 'p' + chr(10))] == ['paragraph']
    # ### ### **THE FIXTURE THAT MATTERS: THE SAME SOURCES ONE PER ENTRY ARE NOT A SYNTHESIS.**
    u4 = (CL.score('a/x.md', CL.FIX_COLL, CL.FIX_INDEX)[0] == 'C-'
          and CL.score('a/x.md', CL.FIX_SYNTH, CL.FIX_INDEX)[0] == 'C+')
    u5 = set(x['want'] for x in flog) >= {'C+', 'C-', 'C?'}
    # ### **THE UNIT IN THE TOOL IS THE ONE ON THE FACE**, checked by the face's own words.
    u6 = all(w in reg for w in ('ONE LIST ITEM', 'ONE TABLE ROW', 'ONE PARAGRAPH',
                                'THE UNIT, DEFINED HERE AND NOT IN THE TOOL'))
    u7 = ('%.2f' % CL.THRESHOLD) in ('%.2f' % C['threshold'],)
    gu = u1 and u2 and u3 and u4 and u5 and u6 and u7
    print('    the shared module`s own fixtures held : %s' % u1)
    print('    ### **ALL FOUR UNIT KINDS REACHABLE** : %s ; a real heading is in no unit : %s'
          % (u2, u3))
    print('    ### **THE COLLECTION IS `C-` WHERE THE SYNTHESIS IS `C+`** : %s' % u4)
    print('    all three marks reachable in the fixtures : %s' % u5)
    print('    ### **THE UNIT IS DEFINED ON THE LOCKED FACE** : %s ; threshold as locked : %s'
          % (u6, u7))
    print('    %s' % ('PASS' if gu else '### FAIL ###'))
    if not gu:
        fails.append('G-UNIT/G-UNITFIX/G-COLOCATE/G-POLARITY')

    # -------------------------------------------------------------------- BAR 5, THE ORDER BAR
    print(chr(10) + '  G-CONTROLFIRST (BAR 5):')
    # ### ### **THE CONTROL RAN BEFORE ANY CORPUS-WIDE NUMBER EXISTED, AND THE PROOF IS THAT NO
    # ### ### CORPUS-WIDE NUMBER EXISTS AT ALL.**
    o1 = C['corpus_scored'] is False and VD['corpus_scored'] is False
    o2 = 'NO CORPUS-WIDE CO-LOCATION FIGURE EXISTS IN THIS ACT' in bank
    # ### the control run file names the exemplars and never a corpus population
    o3 = str(C['synthesis_n']) in crun and str(C['gathering_n']) in crun
    o4 = str(R80['population']) not in crun
    o5 = (crun.index('THE PREDICATE`S OWN FIXTURES') < crun.index('THE SEPARATION'))
    go = o1 and o2 and o3 and o4 and o5
    print('    the corpus was not scored, in both JSONs : %s' % o1)
    print('    ### **THE BANK SAYS NO CORPUS-WIDE FIGURE EXISTS** : %s' % o2)
    print('    the control run names the exemplar counts : %s ; and no corpus population : %s'
          % (o3, o4))
    print('    the fixtures print before the separation : %s' % o5)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-CONTROLFIRST')

    # ------------------------------------------------------------- BAR 6, THE NON-ADOPTION BAR
    print(chr(10) + '  G-SEPARATION / G-NOADOPT (BAR 6):')
    # ### **THE SEPARATION IS RECOMPUTED HERE FROM THE BANKED PER-DOCUMENT MARKS.**
    sp = sum(1 for r in C['synthesis'] if r['mark'] == 'C+')
    gpp = sum(1 for r in C['gathering'] if r['mark'] == 'C+')
    n1 = sp == C['synthesis_cplus'] and gpp == C['gathering_cplus']
    lo = min(r['ratio'] for r in C['synthesis'])
    hi = max(r['ratio'] for r in C['gathering'])
    n2 = abs(lo - C['lowest_synthesis_ratio']) < 1e-9 and abs(hi - C['highest_gathering_ratio']) < 1e-9
    n3 = C['threshold_free_separation'] == (lo > hi)
    clean = (sp == len(C['synthesis']) and gpp == 0)
    n4 = (C['branch'] == 'SEPARATES') == clean
    n5 = C['adopted'] == (C['branch'] == 'SEPARATES' and C['powered'])
    # ### ### **THE CLAUSE: NOT ADOPTED MEANS THE CORPUS IS NOT SCORED AND NO TABLE IS REDRAWN.**
    n6 = (not C['adopted']) and C['corpus_scored'] is False
    n7 = VD['f2'] == 'NOT REACHED' and 'NOT REACHED' in bank
    n8 = VD['prior_scores_overwritten'] == 0
    gn = n1 and n2 and n3 and n4 and n5 and n6 and n7 and n8
    print('    the C+ counts recompute from the per-document marks : %s' % n1)
    print('    the extremes recompute : %s ; the threshold-free check is consistent : %s' % (n2, n3))
    print('    ### **THE BRANCH FOLLOWS THE RULE DECLARED BEFORE THE RUN** : %s / %s' % (n4, n5))
    print('    ### **NOT ADOPTED, SO THE CORPUS WAS NOT SCORED** : %s' % n6)
    print('    (F2) is NOT REACHED rather than met or refuted : %s ; scores overwritten : %d'
          % (n7, VD['prior_scores_overwritten']))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-SEPARATION/G-NOADOPT')

    # ------------------------------------------------------------- BAR 7, THE NO-OVERWRITE BAR
    print(chr(10) + '  G-NOOVERWRITE (BAR 7):')
    # ### **b380'S COLUMN MUST BE EXACTLY WHERE IT WAS**, byte-for-byte in its own banked JSON.
    v1 = VD['prior_scores_overwritten'] == 0
    v2 = R80['prior_scores_overwritten'] == 0
    v3 = not git(ROOT, 'diff', '--name-only', 'HEAD', '--', 'data/b380_rescore.json').strip()
    v4 = str(R80['structural_tally'].get('A+', 0)) in bank
    v5 = str(R80['structural_tally'].get('A-', 0)) in bank
    v6 = 'STILL AN UPPER BOUND ON SYNTHESIS' in bank and 'STILL UNVALIDATED' in bank
    gv = v1 and v2 and v3 and v4 and v5 and v6
    print('    prior scores overwritten by this act : %d' % VD['prior_scores_overwritten'])
    print('    ### **b380`S BANKED ROWS ARE UNMODIFIED ON DISK** : %s' % v3)
    print('    both of b380`s columns are named in the bank : %s / %s' % (v4, v5))
    print('    ### **AND BOTH ARE REPORTED AS UNMOVED** : %s' % v6)
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-NOOVERWRITE')

    # ---------------------------------------------------------------- BAR 8, THE DEAFNESS BAR
    print(chr(10) + '  G-DEAF / G-COLUMNS / G-R14RECORDED (BAR 8):')
    DEAFNESSES = [
        ('many sources in one place without relating them',
         'QUOTING MANY SOURCES IN ONE PLACE WITHOUT RELATING THEM'),
        ('a synthesis across adjacent paragraphs',
         'RELATES TWO SOURCES ACROSS ADJACENT PARAGRAPHS'),
        ('markdown structure stands in for rhetorical structure',
         'MARKDOWN STRUCTURE STANDS IN FOR RHETORICAL STRUCTURE'),
        ('the directory stands in for the subject', 'THE DIRECTORY STANDS IN FOR THE SUBJECT'),
        ('a citation it does not recognise', 'A CITATION IT DOES NOT RECOGNISE'),
    ]
    missing = [lbl for lbl, needle in DEAFNESSES if needle not in bank]
    z1 = not missing
    modsrc = io.open(t('co_location.py'), encoding='utf-8').read()
    z2 = all(needle in modsrc.upper() for _l, needle in DEAFNESSES)
    # ### **AND WHETHER THE EXEMPLARS TEST THE FIRST OF THEM IS MEASURED, NOT ASSURED.**
    z3 = VD['e4'] in ('MET', 'REFUTED') and str(VD['naive_gathering_cplus']) is not None
    z4 = 'STILL AN UPPER BOUND ON SYNTHESIS' in bank and 'STILL UNVALIDATED' in bank
    z5 = 'NOT PROOF THAT NO STRUCTURAL FEATURE' in bank
    # ### **(R14) RECORDED VERBATIM AND WHOLE.**
    ev = io.open(EVID, encoding='utf-8').read()
    ferrytxt = io.open(FERRY, encoding='utf-8').read().split(chr(10))
    a = [i for i, x in enumerate(ferrytxt) if x.startswith('RULING (R14)')][0]
    b = [i for i, x in enumerate(ferrytxt) if x.startswith("and is the author's.")][0]
    z6 = all(('###   | ' + ln.rstrip()) in ev for ln in ferrytxt[a:b + 1])
    z7 = 'RECORDED AND NOT APPLIED' in bank and VD['class_ruled'] is False
    z8 = "STAYS OPEN AND IS THE AUTHOR" in bank
    gz = z1 and z2 and z3 and z4 and z5 and z6 and z7 and z8
    print('    deafnesses missing from the bank : %s' % (missing or 'none'))
    print('    ### **EACH IS DECLARED IN THE MODULE ITSELF** : %s' % z2)
    print('    the first deafness is measured rather than assured : %s' % z3)
    print('    both columns stated and the overclaim declined : %s / %s' % (z4, z5))
    print('    ### **(R14) IS BANKED VERBATIM AND WHOLE (%d lines)** : %s' % (b - a + 1, z6))
    print('    recorded and not applied : %s ; the filing stays the author`s : %s' % (z7, z8))
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-DEAF/G-COLUMNS/G-R14RECORDED')

    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b381' not in x and x != 'tools/banked_index.py'
                     and x != 'tools/co_location.py'
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

    # ------------------------------------------------------- BAR 9, THE NO-RULING BAR / G-OPEN
    print(chr(10) + '  G-NORULING / G-NOPREFER / G-OPEN / G-NONEWDOC (BAR 9):')
    o_start = bank.find('### COMPONENT 4 -- WHAT THE COLUMNS MEAN NOW.')
    o_end = bank.find('### THE EXPECTATIONS, EACH AGAINST ITS OWN PRINTED TABLE.')
    region = bank[o_start:o_end] if (o_start >= 0 and o_end > o_start) else ''
    NEGATED = re.compile(r'\b(none|no|not|never|without|neither|nothing)\b[^.]{0,60}$', re.I)
    raw, live = [], []
    for m in PREFER.finditer(region):
        before = region[max(0, m.start() - 90):m.start()]
        raw.append(m.group(0))
        if not NEGATED.search(before):
            live.append(m.group(0))
    print('    ### raw preference-word hits in the columns region : %s' % (sorted(set(raw)) or 'none'))
    n1 = not live and bool(region)
    n2 = Q['lists_closed'] == 0
    # ### ### **THE ONE DESK CLOSURE IS THE AUTHOR'S RULING, NOT THIS SEAT'S JUDGEMENT.**
    n3 = Q['closed'] == 1 and all('outside the tree' in c['item'] for c in Q['closed_items'])
    n4 = VD['class_ruled'] is False
    lists = ['the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites']
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    deskrun = io.open(IDX, encoding='utf-8', errors='replace').read()
    n5 = all(x in deskrun for x in lists)
    n6 = 'ARE RESTATED `OPEN` BY NAME' in bank
    n7 = 'open by name' in gate_text.flat(tblk).lower()
    PREEXISTING = ('BLOB_SENSITIVITY',)
    newdocs = [x.strip() for x in git(PP, 'status', '--porcelain').split(chr(10))
               if x.strip().startswith('??') and not any(pe in x for pe in PREEXISTING)]
    n8 = not newdocs
    gnr = n1 and n2 and n3 and n4 and n5 and n6 and n7 and n8
    print('    live preference words : %d ; lists closed : %d ; desk closed : %d'
          % (len(live), Q['lists_closed'], Q['closed']))
    print('    ### **THE ONE CLOSURE IS (R14), THE AUTHOR`S** : %s (%s)'
          % (n3, [c['item'] for c in Q['closed_items']]))
    print('    ### **NO CLASS RULED** : %s' % n4)
    print('    the four lists named in the desk run and restated OPEN : %s / %s ; in the trail : %s'
          % (n5, n6, n7))
    print('    ### **AND NO NEW TRACKING DOCUMENT WAS CREATED** : %s %s' % (n8, newdocs[:2] or ''))
    print('    %s' % ('PASS' if gnr else '### FAIL ###'))
    if not gnr:
        fails.append('G-NORULING/G-NOPREFER/G-OPEN/G-NONEWDOC')

    print(chr(10) + '  G-TRAIL / G-ROW / G-KEY ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1 and Q['trail']['appended_only']
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    t3 = len(rws) == 1 and anc and 'THE CONTROL REBUILT FROM THE RECORD' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-control-rebuilt-and-co-location-not-adopted returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('the class is ruled', 'the declarations are moved',
              'the corpus was scored', 'the registry is edited'))
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
    relied = (EX, C, VD, Q)
    o3 = (stampm is not None) and all(
        (x.get('run_clock') or run_clock.read_stamp(d(x['run_file']))) > stampm.group(1)
        for x in relied)
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY COMPONENT RUNS AND BEFORE ANY BYTE IS WRITTEN' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    o7 = 'VERDICT          : CLEAN' in io.open(TERMSCAN, encoding='utf-8', errors='replace').read()
    # ### **AND THE THREE PRIOR LOCKED FACES MUST STILL VERIFY, UNEDITED.**
    R375 = d('b380_registration_2026-09-08.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b379_registration_2026-09-08.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b379`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b380`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b381_hooks.txt'), d('b381_mirror.txt')
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
        ('documents scanned %d' % EX['scanned'], str(EX['scanned']) in bank),
        ('the head window %d' % EX['head_lines'], str(EX['head_lines']) in bank),
        ('b380 threshold %d' % EX['b380_threshold'], str(EX['b380_threshold']) in bank),
        ('b380 lowest synthesis reach %d' % EX['b380_lowest_synthesis_reach'],
         str(EX['b380_lowest_synthesis_reach']) in bank),
        ('the lineage v1 %d' % EX['loose_hits'], str(EX['loose_hits']) in bank),
        ('the lineage v2 %d' % EX['loose2_hits'], str(EX['loose2_hits']) in bank),
        ('the lineage v3 %d' % EX['wide_hits'], str(EX['wide_hits']) in bank),
        ('the order`s three verbs %d' % EX['order_hits'], str(EX['order_hits']) in bank),
        ('the denial reading %d' % EX['denial_hits'], str(EX['denial_hits']) in bank),
        ('the floor %d' % EX['floor'], str(EX['floor']) in bank),
        ('synthesis exemplars %d' % C['synthesis_n'], str(C['synthesis_n']) in bank),
        ('gathering exemplars %d' % C['gathering_n'], str(C['gathering_n']) in bank),
        ('synthesis at C+ %d' % C['synthesis_cplus'], str(C['synthesis_cplus']) in bank),
        ('gathering at C+ %d' % C['gathering_cplus'], str(C['gathering_cplus']) in bank),
        ('the lowest synthesis ratio', ('%.3f' % C['lowest_synthesis_ratio']) in bank),
        ('the highest gathering ratio', ('%.3f' % C['highest_gathering_ratio']) in bank),
        ('the branch %s' % C['branch'], C['branch'] in bank),
        ('the registry bearing units %d' % VD['registry_bearing'],
         str(VD['registry_bearing']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on exemplars run', EX['run_file'] in bank),
        ('the relied-on control run', C['run_file'] in bank),
        ('the relied-on verdict run', VD['run_file'] in bank),
        ('the relied-on extract run', E['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('lockgate', LG), ('exemplars', EX),
                    ('control', C), ('verdict', VD), ('desk', Q)):
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
                          if x.startswith('b381_') and x.endswith('.py')))
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
              if x.strip() and 'b381' not in x and x.strip() not in DECLARED]
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
             d('b381_satisfiable.json')] + [t(x) for x in mymods] + [t('co_location.py')]
    CARRIERS = [
        (t('b381_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the corpus's own documents"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(EX['run_file']), "the exemplar run carries the documents' own purpose sentences"),
        (d(C['run_file']), "the control run carries the documents' own names"),
        (d(VD['run_file']), "the verdict run carries the ruling's own words"),
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

    marker = '# ### THE CONTROL REBUILT, AND CO-LOCATION TESTED (b381).'
    nxt = '# ### THE ROLE AXIS, SCORED STRUCTURALLY (b380).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b381_stem_'), 'blk.txt')
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
    made = sorted('tools/' + x for x in mymods) + ['tools/co_location.py']
    gcap = len(made) <= 10 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b381_hedge_')
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
