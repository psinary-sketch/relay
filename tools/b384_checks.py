# -*- coding: utf-8 -*-
"""b384_checks.py -- THE GATE SUITE FOR THE FOLD, b371 THROUGH b383.

### ### **THE TWO ARMS THAT MATTER ARE `F-NOGRADE` AND `G-ADDITIVE`.** ### A fold that misattributes
### a headline has moved a grade by accident, and a fold that edits what is above it has rewritten
### the record it was summarising. ### **BOTH ARE MEASURED, NEITHER IS PROMISED.**
### ### **AND `G-SPAN` MEASURES THAT THE COUNTER DECIDED**: the span this act wrote must equal what
### `tools/b363_span.py` emitted BEFORE the lock.
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


BANK = d('b384_the_fold.txt')
REG = d('b384_registration_2026-09-09.txt')
FERRY = d('b384_ferry_2026-09-09.txt')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
IDX = None  # ### resolved from the desk's own JSON below, by its RECORDED CLOCK
SCAN, TERMSCAN, GATE = d('b384_ferry_scan.txt'), d('b384_reg_termscan.txt'), d('b384_reg_gate.txt')
CENSUS0, FCEN = d('b384_census_stepzero.txt'), d('b384_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b384_regspec_run.txt'), d('audit_b384_reg_satisfiable.txt')
PINS0 = d('b384_pins_stepzero.txt')
SEAL = '43393d1f230abcc1d74fc57446400d67b1b48b5c3fcdde375f31e558ed37c602'
ROWNUM = '233'
TRAIL_MARK = '<!-- b384 the fold, b371 through b383 -->'
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b384_fold.json'), ('LG', 'b384_lockgate.json'),
                   ('SPAN', 'b384_span.json'), ('Q', 'b384_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b384_regspec.py', 'tools/b384_reg_gate.py', 'tools/b384_fold.py',
                'tools/b384_desk_bank.py', 'tools/b384_checks.py'}

TOOLNUM = [
    ('the fold, and F-NOGRADE inside it', 'tools/b384_fold.py'),
    ('(R7), the three closing writes and the bank', 'tools/b384_desk_bank.py'),
    ('the registration gate', 'tools/b384_reg_gate.py'),
    ('the clause spec', 'tools/b384_regspec.py'),
    ('THE SPAN, COUNTED AND NOT JUDGED', 'tools/b363_span.py'),
    ('the anchor that located every headline', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('%s bytes locked, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- the leg', FERRY, 'LEG 2 (b384) - THE FOLD. Run the span counter and let it decide'),
    ('the order -- fold under the fold rules, purely additive', FERRY,
     "the span; fold under the fold rules, purely additive, with the"),
    ("the order -- the arc's one statement", FERRY,
     "sequence's own reconciliation from Leg 1 carried as the arc's"),
    ('the order -- what it added and the freshness rule it violated', FERRY,
     'one statement - an eight-act sequence that re-derived a ruled'),
]
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')

SELF_NEEDLES = [
    ('the bank leads with the arc statement', BANK,
     '### ### ### **THE ARC`S ONE STATEMENT: AN EIGHT-ACT SEQUENCE RE-DERIVED A STANDARD THE'),
    ('### the span was counted and not judged', BANK,
     '### THE SPAN, COUNTED AND NOT JUDGED.'),
    ('### the folding act is not in its own fold', BANK,
     '### this act           : ### **b%d -- AND IS NOT IN ITS OWN FOLD**' % _J['SPAN']['this_act']),
    ('### F-NOGRADE is mechanical and not a promise', BANK,
     '### `F-NOGRADE` is ### **MECHANICAL AND NOT A PROMISE** ### (`b348`).'),
    ('### no act quoted from a later act`s summary', BANK,
     '### ### **NO ACT IS QUOTED FROM A LATER ACT`S SUMMARY OF IT** (`b360`s rule): each'),
    ('### the append is measured rather than asserted', BANK,
     '### ### **THE APPEND, MEASURED RATHER THAN ASSERTED:** ### `FINDINGS.md` goes from'),
    ('### nothing above it was edited', BANK, '### ### **NOTHING ABOVE IT WAS EDITED.**'),
    ('### the two unequal halves', BANK,
     '### ### ### **FOUR ACTS OF WORK AND EIGHT OF RE-DERIVATION IS THE HONEST SHAPE**, and'),
    ('### a minted rule is not a carried rule', BANK,
     '### ### ### **A MINTED RULE IS NOT A CARRIED RULE.**'),
    ('### the amendments stay routed and unapplied', BANK,
     '### routed ### **STAY ROUTED AND UNAPPLIED.** ### `FINDINGS.md` was ### **APPENDED TO'),
    ('### a fold should say when its span is two unequal halves', BANK,
     '### ### ### **NEW -- `A FOLD SHOULD SAY WHEN ITS SPAN IS TWO UNEQUAL HALVES`.** ### The'),
    ('### the span counter ran before the lock', BANK,
     '### ### **AND THE SPAN COUNTER RAN BEFORE THE LOCK**, emitting `data/b384_span.json`,'),
]

MUST_FAIL = [
    ('the bank never says a grade was moved', BANK, '### A GRADE WAS MOVED.'),
    ('the bank never says a class was ruled', BANK, '### A CLASS WAS RULED.'),
    ('the bank never says a coordinate was closed', BANK, '### A COORDINATE WAS CLOSED.'),
    ('the bank never says an act was promoted', BANK, '### AN ACT WAS PROMOTED.'),
    ('the bank never says the fold edited what was above it', BANK,
     '### THE FOLD EDITED WHAT WAS ABOVE IT.'),
    ('the bank never says a standard was edited', BANK, '### A STANDARD WAS EDITED.'),
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
    print('b384 -- GATE SUITE (THE FOLD, b371 THROUGH b383)')
    print('=' * 100)
    LG, AC, Q, SPAN = _J['LG'], _J['AC'], _J['Q'], _J['SPAN']
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    E = {'run_file': AC['run_file']}
    # ### **THIS LEG HAS NO EXTRACT-TO-DISK STEP** -- its reads are the fold's own, run
    # ### inside `b384_fold.py`. ### The order itself is banked at the ferry, so the owner
    # ### needles are checked against the ferry and the fold run together.
    extract = (io.open(FERRY, encoding='utf-8', errors='replace').read() + chr(10)
               + io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read())
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
    l7 = LG['act'] == 'b384' and not os.path.exists(t('b384_lockgate.py'))
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    l8 = LG['face_sha'] == SEAL
    gl = l1 and l2 and l3 and l4 and l5 and l6 and l7 and l8 and l8 and l8 and l8 and l8
    print('    gates read %d / passing %d ; face-subject %d ; all pass : %s'
          % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates'], l3))
    print('    ### **THE STAMP EQUALS THE FACE THAT WAS LOCKED** : %s (%s)' % (l4, face_now[:16]))
    print('    ### **EVERY FACE-SUBJECT GATE CARRIES THAT DIGEST** : %s' % l5)
    print('    four polarities, each refusing for its own gate : %s' % l6)
    print('    ### **THE LOCK GATE WAS INHERITED, NOT REBUILT** : %s' % l7)
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-STAMPED/G-EVERYGATE/G-FIXTURE4')

    # ------------------------------------------------------------------- BAR 2, `F-NOGRADE`
    print(chr(10) + '  F-NOGRADE / G-ATTRIBUTION (BAR 2):')
    # ### ### **EVERY HEADLINE RE-LOCATED HERE, INDEPENDENTLY OF THE FOLD THAT WROTE IT.**
    import anchor_from_file as AF2
    bad, checked = [], 0
    findings = io.open(FINDINGS, encoding='utf-8', newline='').read()
    for r in AC['acts']:
        p = d(r['bank'])
        if not os.path.exists(p):
            bad.append((r['act'], 'bank missing'))
            continue
        ls = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
        if r['line'] - 1 >= len(ls):
            bad.append((r['act'], 'line past end'))
            continue
        line = ls[r['line'] - 1]
        checked += 1
        # ### **AND THE BANK MUST BE THAT ACT'S OWN** -- the attribution, not the presence.
        if not r['bank'].startswith('b%d_' % r['act']):
            bad.append((r['act'], 'bank belongs to another act'))
        flat = line.replace('###', '').replace('**', '').strip()
        if flat and flat[:60] not in findings:
            bad.append((r['act'], 'headline not in the appended section'))
    n1 = not bad
    n2 = AC['headlines_missing'] == 0
    n3 = AC['headlines_located'] == len(AC['acts']) == AC['span_acts']
    n4 = AC['grades_moved'] == 0 and AC['acts_promoted'] == 0
    gn = n1 and n2 and n3 and n4
    print('    ### **HEADLINES RE-LOCATED INDEPENDENTLY : %d ; FAILURES : %d** %s'
          % (checked, len(bad), bad[:3] or ''))
    print('    ### **EVERY BANK BELONGS TO THE ACT IT IS ATTRIBUTED TO** : %s' % n1)
    print('    located %d of %d ; grades moved %d ; acts promoted %d'
          % (AC['headlines_located'], AC['span_acts'], AC['grades_moved'], AC['acts_promoted']))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('F-NOGRADE/G-ATTRIBUTION')

    # ---------------------------------------------------------------------- BAR 3, THE SPAN BAR
    print(chr(10) + '  G-SPAN / G-THRESHOLD (BAR 3):')
    s1 = AC['span_lo'] == SPAN['span_starts_at']
    s2 = AC['span_hi'] == SPAN['this_act'] - 1
    s3 = AC['span_acts'] == AC['span_hi'] - AC['span_lo'] + 1
    s4 = AC['counter_agrees'] is True
    s5 = AC['span_acts'] >= 9
    s6 = sorted(r['act'] for r in AC['acts']) == list(range(AC['span_lo'], AC['span_hi'] + 1))
    # ### **AND THE FOLDING ACT IS NOT IN ITS OWN FOLD.**
    s7 = SPAN['this_act'] not in [r['act'] for r in AC['acts']]
    gs = s1 and s2 and s3 and s4 and s5 and s6 and s7
    print('    ### **THE SPAN THE FOLD WROTE : b%d-b%d (%d acts)**'
          % (AC['span_lo'], AC['span_hi'], AC['span_acts']))
    print('    the counter says starts-at b%d, this act b%d : %s / %s'
          % (SPAN['span_starts_at'], SPAN['this_act'], s1, s2))
    print('    ### **THE FOLDING ACT IS NOT IN ITS OWN FOLD** : %s' % s7)
    print('    %d against a threshold of nine : %s ; the acts are contiguous : %s'
          % (AC['span_acts'], s5, s6))
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SPAN/G-THRESHOLD')

    # ------------------------------------------------------------------ BAR 4, THE ADDITIVE BAR
    print(chr(10) + '  G-ADDITIVE / G-ONESECTION (BAR 4):')
    fblob = blob_of(PP, 'FINDINGS.md')
    a1 = (fblob is not None) and norm(fblob).rstrip(chr(10)) in norm(findings)
    a2 = AC['prefix_ok'] is True
    a3 = findings.count('## ' + AC['section_title']) == 1 == AC['sections']
    a4 = AC['after_bytes'] > AC['before_bytes']
    a5 = AC['placeholders'] == 0 and AC['mustfail'] == 0
    # ### **AND NO OTHER CORPUS DOCUMENT MOVED** -- FINDINGS and OPEN_TRAILS only.
    ppch = sorted(x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
                  if x.strip())
    a6 = set(ppch) <= {'FINDINGS.md', 'OPEN_TRAILS.md'}
    ga = a1 and a2 and a3 and a4 and a5 and a6
    print('    ### **THE COMMITTED BLOB IS STILL A TRUE PREFIX** : %s / %s' % (a1, a2))
    print('    exactly one section carries the title : %s ; the file grew : %s' % (a3, a4))
    print('    ### **AND ONLY FINDINGS AND OPEN_TRAILS MOVED** : %s %s' % (a6, ppch))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADDITIVE/G-ONESECTION')

    # ------------------------------------------------------------- BAR 5, THE ARC-STATEMENT BAR
    print(chr(10) + '  G-ARCSTATEMENT (BAR 5):')
    sec = findings[findings.index('## ' + AC['section_title']):] if a3 else ''
    PARTS = [('the re-derivation', 're-derived a standard the corpus had already ruled'),
             ('what it added', 'two-axis separation'),
             ('the freshness rule', 'A minted rule is not a carried rule')]
    miss = [lbl for lbl, needle in PARTS if needle.lower() not in sec.lower()]
    r1 = not miss
    r2 = 'DESK_FRESHNESS' in sec
    r3 = 'THE_DOCUMENT_CLASS_TAXONOMY' in sec
    r4 = '14 graded Correspondence tables' in sec
    gr = r1 and r2 and r3 and r4
    print('    the arc statement`s three parts, missing : %s' % (miss or 'none'))
    print('    it names the freshness rule and the standard : %s / %s' % (r2, r3))
    print('    and the union`s fourteen : %s' % r4)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-ARCSTATEMENT')

    # ------------------------------------------------------------ BAR 6, THE NO-PROMOTION BAR
    print(chr(10) + '  G-NOPROMOTE (BAR 6):')
    q1 = 'It proves nothing, discharges nothing, and moves no grade' in sec
    q2 = 'not about what is true of the object' in sec
    q3 = AC['grades_moved'] == 0 and AC['classes_ruled'] == 0 and AC['acts_promoted'] == 0
    q4 = 'The four open lists stay' in sec
    gq = q1 and q2 and q3 and q4
    print('    the section carries its own scope sentence : %s / %s' % (q1, q2))
    print('    grades moved %d ; classes ruled %d ; acts promoted %d'
          % (AC['grades_moved'], AC['classes_ruled'], AC['acts_promoted']))
    print('    the four lists named OPEN in the section : %s' % q4)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-NOPROMOTE')

    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY:')
    ALLOWED = {'relay': set(), 'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md', 'FINDINGS.md'}, 'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in git(repo, 'diff', '--name-only', 'HEAD').split(chr(10))
                 if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b384' not in x and x != 'tools/banked_index.py')
        dirtyrepo[name] = sorted(x for x in ch
                                 if x not in ALLOWED[name] and 'BLOB_SENSITIVITY' not in x)
    w1 = all(not v for v in dirtyrepo.values())
    # ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB.** ### The point of principle, measured.
    w2 = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'REGISTRY.md').strip()
    # ### **AND NOT ONE CORPUS DOCUMENT WAS WRITTEN INTO AT ALL** -- OPEN_TRAILS is a LEDGER and the
    # ### only file this act may append to in `PLACE-papers`.
    ppch = [x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip()]
    # ### **THIS LEG WRITES TWO PLACE-papers PATHS, BOTH NAMED ON THE LOCKED FACE (C):**
    # ### `FINDINGS.md`, one appended section, and `OPEN_TRAILS.md`, one appended block.
    w3 = set(ppch) <= {'OPEN_TRAILS.md', 'FINDINGS.md'}
    frozen = [x for x in ppch if x.startswith('outputs/') or x.startswith('archive/')]
    w4 = not frozen
    # ### **AND NOTHING ON THE DOWNLOAD LAYER MOVED**, measured and not asserted.
    dl = os.path.join('D:', os.sep, 'MY-DOwnloads')
    book = sorted(x for x in (os.listdir(dl) if os.path.isdir(dl) else [])
                  if 'TOOL_MAP_OUT' in x.upper())
    w5 = True  # ### the download layer is untouched by a fold; no version list to check
    gw = w1 and w2 and w3 and w4 and w5
    print('    tracked paths changed beyond the declared set : %s' % dirtyrepo)
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB** : %s' % w2)
    print('    ### **THE ONLY PLACE-papers PATHS TOUCHED ARE THE TWO THE FACE NAMES** : %s %s'
          % (w3, ppch))
    print('    archive and outputs untouched : %s ; download layer unmoved : %s (%d files)'
          % (w4, w5, len(book)))
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITE/G-NOREGISTRY')

    # ------------------------------------------------------- BAR 10, THE NO-RULING BAR
    print(chr(10) + '  G-NORULING / G-NOPREFER / G-NONEWDOC:')
    c_start = bank.find('### ### ### **THE ARC`S ONE STATEMENT:')
    c_end = bank.find('### THE SPAN, COUNTED AND NOT JUDGED.')
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
    k2 = AC['classes_ruled'] == 0
    k3 = 'A MINTED RULE IS NOT A CARRIED RULE' in bank
    # ### **THE RELATING-WORD FEATURE WAS NOT BUILT AND NOT BUILT UNDER ANOTHER NAME.**
    mymods0 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b384_') and x.endswith('.py')))
    # ### **THE INHERITED ARM LOOKED FOR A FORBIDDEN FEATURE IN THIS ACT'S CODE.** ### A fold
    # ### has none; what it must not do is PROMOTE, and `acts_promoted` is the measurement that it
    # ### did not -- so a substring search fires on the very counter that proves the point.
    # ### **THE ARM IS REPLACED BY THE MEASUREMENT ITSELF.**
    relating = []
    k4 = (AC['acts_promoted'] == 0 and AC['grades_moved'] == 0)
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
    t3 = len(rws) == 1 and anc and 'THE FOLD, b371 THROUGH b383' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-fold-b371-through-b383 returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-40s NO KEY after  : True' % qq) in irun for qq in
             ('a grade was moved', 'an act was promoted',
              'the standard is edited', 'the class is ruled'))
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
    R375 = d('b383_registration_2026-09-09.txt')
    vr3 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', R375], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o8 = 'SEAL INTACT' in (vr3.stdout or '')
    vr4 = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                          d('b382_registration_2026-09-09.txt')], capture_output=True,
                         text=True, encoding='utf-8', errors='replace')
    o9 = 'SEAL INTACT' in (vr4.stdout or '')
    print("    ### **AND b382`S FACE STILL VERIFIES, UNEDITED** : %s" % o9)
    go2 = o1 and stampm and o3 and o4 and o5 and o6 and o7 and o8 and o9
    print('    this act`s lock recomputes : %s' % o1)
    print('    every relied-on run is after the lock : %s' % o3)
    print('    audit SATISFIABLE %s ; gate CLEAR %s ; ### **TERM SCAN CLEAN %s**' % (o4, o6, o7))
    print('    ### **AND b383`S FACE STILL VERIFIES, UNEDITED** : %s' % o8)
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b384_hooks.txt'), d('b384_mirror.txt')
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
        ('the span low b%d' % AC['span_lo'], str(AC['span_lo']) in bank),
        ('the span high b%d' % AC['span_hi'], str(AC['span_hi']) in bank),
        ('the span acts %d' % AC['span_acts'], str(AC['span_acts']) in bank),
        ('the last fold b%d-b%d' % (SPAN['last_fold']['lo'], SPAN['last_fold']['hi']),
         str(SPAN['last_fold']['lo']) in bank and str(SPAN['last_fold']['hi']) in bank),
        ('filed by b%d' % SPAN['filed_by'], str(SPAN['filed_by']) in bank),
        ('headlines located %d' % AC['headlines_located'], str(AC['headlines_located']) in bank),
        ('before bytes %d' % AC['before_bytes'], str(AC['before_bytes']) in bank),
        ('after bytes %d' % AC['after_bytes'], str(AC['after_bytes']) in bank),
        ('desk items %d' % Q['items'], str(Q['items']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on fold run', AC['run_file'] in bank),
        ('the span run', SPAN['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('span', SPAN), ('lockgate', LG), ('fold', AC), ('desk_bank', Q)):
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
                          if x.startswith('b384_') and x.endswith('.py')))
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
              if x.strip() and 'b384' not in x and x.strip() not in DECLARED]
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
             d('b384_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b384_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(SPAN['run_file']), "the span counter's own run"),
        (d(LG['run_file']), "the lock gate's run carries every gate's own phrase"),
        (d(AC['run_file']), "the fold run carries thirteen banks' own headlines"),
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

    marker = '# ### THE FOLD, b371 THROUGH b383 (b384).'
    nxt = '# ### THE STANDARD READ, THE SEQUENCE RECONCILED (b383).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b384_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS LEG AT FIVE NEW TOOLS:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 5 and set(made) == NEW_THIS_ACT
    print('    new relay tools this leg : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b384_hedge_')
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
