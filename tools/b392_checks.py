# -*- coding: utf-8 -*-
"""b392_checks.py -- THE GATE SUITE FOR THE TWO RULINGS.

### ### **THE ARM THAT MATTERS MOST IS `G-ADDITIVE`.** ### This act writes into the standing
### taxonomy, the registry and the front door -- three documents the whole corpus rests on -- and
### the one thing it must not do is lose a line of any of them. ### The arm reads every pre-act line
### of all three out of the committed blob and requires each ### **PRESENT AND BYTE-IDENTICAL**,
### with `0` removed.
###
### ### **`G-GUARD` IS AN ARM AGAINST THE RULING ITSELF.** ### A class that is a conjunction of
### Tier K and Tier C is one careless reading away from being a citation licence, and the corpus has
### been hurt by exactly that shape twice. ### The arm requires the guard sentence and ### **BOTH
### ### FAILURES QUOTED IN THE CLASS'S OWN TEXT.**
###
### ### **`G-NOPLATFORM` KEEPS THE CENSUS HONEST.** ### `b389` proved the platform answers nothing;
### this act takes its deposit census from the corpus and ### **NEVER CALLS THE PLATFORM AT ALL.**
###
### ### **AND `G-SEPARATE` GUARDS AN EXPECTATION.** ### `(L2)` wanted three failures and the count
### is two. ### The arm requires the two shapes of failure to stay separate and the withdrawn
### finding to be named as withdrawn -- because ### **AN EXPECTATION IS NOT A TARGET.**
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


BANK = d('b392_the_two_rulings.txt')
REG = d('b392_registration_2026-09-09.txt')
FERRY = d('b392_ferry_2026-09-09.txt')
SCAN, TERMSCAN, GATE = d('b392_ferry_scan.txt'), d('b392_reg_termscan.txt'), d('b392_reg_gate.txt')
CENSUS0, FCEN = d('b392_census_stepzero.txt'), d('b392_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b392_regspec_run.txt'), d('audit_b392_reg_satisfiable.txt')
PINS0 = d('b392_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
THREE = (TAXONOMY, 'REGISTRY.md', 'README.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = 'bec15a4abd5b9beefcae558d0b24401ab802cb8a87280b3e7c23b00c1b4e127c'
ROWNUM = '241'
TRAIL_MARK = ('<!-- b392 the two rulings written: (R19) the finished keystone, (R20) the deposit rule -->')
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b392_components.json'), ('LG', 'b392_lockgate.json'),
                   ('Q', 'b392_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b392_regspec.py', 'tools/b392_reg_gate.py',
                'tools/b392_components.py', 'tools/b392_desk_bank.py', 'tools/b392_checks.py'}

TOOLNUM = [
    ('(R19) and (R20) written, and the deposit census', 'tools/b392_components.py'),
    ('the desk, the ledger writes and the bank', 'tools/b392_desk_bank.py'),
    ('the registration gate', 'tools/b392_reg_gate.py'),
    ('the clause spec', 'tools/b392_regspec.py'),
    ('the anchor that read every quoted line', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- leg 2, the act', FERRY, 'LEG 2 (b392) — THE TWO RULINGS WRITTEN.'),
    ('the order -- (R19), the finished keystone is a named class', FERRY,
     "RULING (R19), the author's, ratified by this paste: THE"),
    ('the order -- (R19), amend additively', FERRY,
     'document-class taxonomy — additively, the prior text preserved'),
    ('the order -- (R19), the obligation', FERRY,
     'every load-bearing claim stated clearly in the body and carried'),
    ('the order -- (R19), the citation rule', FERRY,
     'CITE EACH CONCORDANCE ROW AT ITS STATED GRADE. Its guard,'),
    ('the order -- (R19), the guard', FERRY,
     'written into the class: this class CONFERS NO CITATION LICENSE'),
    ('the order -- (R19), no document reclassified', FERRY,
     'sees why the guard is there. No document is reclassified into'),
    ('the order -- (R20), the deposit rule', FERRY,
     "RULING (R20), the author's, ratified by this paste: THE DEPOSIT"),
    ('the order -- (R20), where it is written', FERRY,
     "corpus's precedence puts deposits — the source of truth first,"),
    ('the order -- (R20), the currency obligation', FERRY,
     'outcome. THE CURRENCY OBLIGATION: every deposited record either'),
    ('the order -- (R20), from the corpus and not the platform', FERRY,
     'list every deposited record the corpus knows of, which the'),
    ('the order -- (R20), the platform is not written to', FERRY,
     'The platform is not written to; the remediation is priced and'),
    ('the order -- (L2)', FERRY, 'three deposited records fail the currency obligation.'),
]

SELF_NEEDLES = [
    ('the bank leads with the two rulings', BANK,
     '### ### ### **TWO THINGS THE CORPUS HAD BEEN DOING WITHOUT A NAME OR A RULE'),
    ('### the guard is written into the class', BANK,
     '### ### ### **AND THE GUARD IS WRITTEN INTO THE CLASS, NOT BESIDE IT:** ###'),
    ('### a class that collapses the distinction is retired', BANK,
     '### ### ### **A CLASS THAT COLLAPSES THE DISTINCTION IS RETIRED; A CLASS THAT'),
    ('### the source of truth first', BANK,
     '### ### **WRITTEN INTO `REGISTRY.md`, WITH `README.md` POINTING AT IT** -- the'),
    ('### there is no third state', BANK,
     '### ### saying it is historical. ### **THERE IS NO THIRD STATE.**'),
    ('### discovered, not imposed', BANK,
     '### ### ### that committed itself). ### **IT IS DISCOVERED, NOT IMPOSED.**'),
    ('### the platform was not asked again', BANK,
     '### ### **THE PLATFORM ANSWERED NOTHING ON SIX ROUTES AT `b389` AND WAS NOT'),
    ('### a DOI is not a record', BANK,
     '###   ### records and their `3` concept DOIs. ### **A DOI IS NOT A RECORD.**'),
    ('### an expectation is not a target', BANK,
     '### ### ### **AN EXPECTATION IS NOT A TARGET, AND A THIRD FAILURE WAS NOT'),
    ('### the elided DOI', BANK,
     '### ### **AND ONE RECORD WAS CLEARED ONLY BY AN ELIDED DOI:** ### the registry`s'),
    ('### proximity is not attachment', BANK,
     '### ### ### **PROXIMITY IS NOT ATTACHMENT.**'),
    ('### the finding is withdrawn', BANK,
     '### support, would have been ### **TUNING FOR A RESULT**. ### **THE FINDING IS'),
]

MUST_FAIL = [
    ('the bank never says a document was reclassified', BANK,
     '### A DOCUMENT WAS RECLASSIFIED.'),
    ('the bank never says prior taxonomy text was edited', BANK,
     '### PRIOR TAXONOMY TEXT WAS EDITED.'),
    ('the bank never says a registry row was edited', BANK, '### A REGISTRY ROW WAS EDITED.'),
    ('the bank never says the platform was asked', BANK, '### THE PLATFORM WAS ASKED.'),
    ('the bank never says a record was convicted by the matcher alone', BANK,
     '### A RECORD WAS CONVICTED BY THE MATCHER ALONE.'),
    ('the bank never says the two failure shapes were added', BANK,
     '### THE TWO FAILURE SHAPES WERE ADDED.'),
    ('the bank never says a third failure was found to meet the expectation', BANK,
     '### A THIRD FAILURE WAS FOUND TO MEET THE EXPECTATION.'),
    ('the bank never says something was deposited', BANK, '### SOMETHING WAS DEPOSITED.'),
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
        if not subj.startswith('b392'):
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
    print('b392 -- GATE SUITE (THE TWO RULINGS WRITTEN)')
    print('=' * 100)
    LG, AC, Q = _J['LG'], _J['AC'], _J['Q']
    extract = io.open(d(Q['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    # ### **THIS ACT HAS NO EXTRACT FILE.** ### `b392` is a five-tool act: the order is read
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
    l7 = LG['act'] == 'b392' and not os.path.exists(t('b392_lockgate.py'))
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

    C1, C2 = AC['c1'], AC['c2']

    # -------------------------------------------------------------------- BAR 2, THE ADDITIVE BAR
    print(chr(10) + '  G-ADDITIVE / G-NODELETE / G-PRIORTEXT (BAR 2):')
    lost, removed, prefixes = [], 0, []
    for rel in THREE:
        pre = blob_of(PP, rel, preact(PP)) or ''
        now = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                      errors='replace').read()
        pl, al = norm(pre).split(chr(10)), norm(now).split(chr(10))
        bad = [k for k, x in enumerate(pl) if k >= len(al) or al[k] != x]
        if bad:
            lost.append((rel, len(bad)))
        removed += max(0, len(pl) - len(al))
        prefixes.append(norm(now).startswith(norm(pre).rstrip(chr(10))))
        print('    %-52s prior lines %-5d all byte-identical %s ; appended below all %s'
              % (rel[:52], len(pl), not bad, prefixes[-1]))
    p1 = not lost and removed == 0 and all(prefixes)
    p2 = C1['file']['deleted'] == 0 and C2['registry']['deleted'] == 0 \
        and C2['readme']['deleted'] == 0
    ga = p1 and p2
    print('    ### **LINES LOST FROM ANY OF THE THREE : %s ; LINES REMOVED : %d**'
          % (lost or 'none', removed))
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ADDITIVE/G-NODELETE/G-PRIORTEXT')

    # ----------------------------------------------------------------------- BAR 3, THE GUARD BAR
    print(chr(10) + '  G-GUARD / G-QUOTED (BAR 3):')
    tax = io.open(os.path.join(PP, TAXONOMY.replace('/', os.sep)), encoding='utf-8',
                  errors='replace').read()
    g1 = 'CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER' in tax
    g2 = 'formation-universality over-claim (June 2026)' in tax
    g3 = 'SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED' in tax
    g4 = 'A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE' in tax
    g5 = C1['guard'] and C1['quoted_failure'] and C1['quoted_retirement'] and C1['citation_rule']
    gg = g1 and g2 and g3 and g4 and g5
    print('    ### **THE GUARD IS IN THE CLASS`S OWN TEXT : %s**' % g1)
    print('    the June 2026 over-claim quoted : %s ; the August 2026 retirement quoted : %s'
          % (g2, g3))
    print('    the citation rule is written for a stranger : %s' % g4)
    print('    %s' % ('PASS' if gg else '### FAIL ###'))
    if not gg:
        fails.append('G-GUARD/G-QUOTED')

    # ----------------------------------------------------------------- BAR 4, THE NO-PLACEMENT BAR
    print(chr(10) + '  G-NOPLACEMENT / G-NOCLASSLINE (BAR 4):')
    n1 = C1['no_placement'] is True
    # ### **NO CLASS LINE ANYWHERE IN THE CORPUS NAMES THE NEW CLASS.**
    named = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in ('.git', 'archive', 'outputs'):
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            r2 = (rel + '/' + f if rel != '.' else f)
            if r2 in (TAXONOMY, 'OPEN_TRAILS.md'):
                continue
            txt2 = io.open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
            for ln in txt2.split(chr(10)):
                if 'Tier KC' in ln and 'DOCUMENT CLASS' in ln:
                    named.append((r2, ln[:60]))
    n2 = not named
    n3 = 'NO DOCUMENT IS RECLASSIFIED AND NO CANDIDATE IS NAMED' in bu
    gn3 = n1 and n2 and n3
    print('    ### **CLASS LINES NAMING `Tier KC` OUTSIDE THE TAXONOMY : %s**' % (named or 'none'))
    print('    the class says so itself : %s ; the bank says so : %s' % (n1, n3))
    print('    %s' % ('PASS' if gn3 else '### FAIL ###'))
    if not gn3:
        fails.append('G-NOPLACEMENT/G-NOCLASSLINE')

    # ------------------------------------------------------------------ BAR 5, THE PRECEDENCE BAR
    print(chr(10) + '  G-PRECEDENCE / G-README (BAR 5):')
    regdoc = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8',
                     errors='replace').read()
    rme = io.open(os.path.join(PP, 'README.md'), encoding='utf-8', errors='replace').read()
    e1 = 'THE DEPOSIT RULE — RULING `(R20)`' in regdoc
    e2 = 'A manuscript wave deposits' in regdoc or 'manuscript wave deposits' in regdoc
    e3 = 'THE CURRENCY OBLIGATION' in regdoc
    e4 = 'The deposit rule is `REGISTRY.md`' in rme
    e5 = ('manuscript wave deposits with its companion papers' not in rme
          and 'THE CURRENCY OBLIGATION' not in rme)
    ge = e1 and e2 and e3 and e4 and e5
    print('    the rule is in REGISTRY.md : %s ; its three limbs : %s ; its obligation : %s'
          % (e1, e2, e3))
    print('    ### **README POINTS AT IT AND DOES NOT RESTATE IT : %s / %s**' % (e4, e5))
    print('    %s' % ('PASS' if ge else '### FAIL ###'))
    if not ge:
        fails.append('G-PRECEDENCE/G-README')

    # ---------------------------------------------------------------- BAR 6, THE NO-PLATFORM BAR
    print(chr(10) + '  G-NOPLATFORM / G-CORPUSONLY (BAR 6):')
    mymods1 = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                           if x.startswith('b392_') and x.endswith('.py')))
    NETY = ('curl', 'urllib', 'requests', 'zenodo.org', 'http://', 'https://', 'ls-remote')
    nhits = [(x, k) for x in mymods1 for k in NETY if k in strip_prose(t(x))]
    m1 = not nhits
    m2 = 'THE PLATFORM ANSWERED NOTHING ON SIX ROUTES' in bu
    m3 = "EVERY FIGURE HERE IS THE CORPUS`S CLAIM ABOUT" in bu or \
        "CLAIM ABOUT ITSELF" in bu
    gm = m1 and m2 and m3
    print('    network tokens in this act`s stripped code : %s' % (nhits or 'none'))
    print('    ### **THE CENSUS IS LABELLED AS THE CORPUS`S OWN CLAIM : %s**' % m3)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-NOPLATFORM/G-CORPUSONLY')

    # --------------------------------------------------------------------- BAR 7, THE LIMB BAR
    print(chr(10) + '  G-LIMBS / G-ELIDED (BAR 7):')
    l1 = C2['unlisted'] == C2['passes'] + C2['fails']
    l2 = C2['known'] == 16 and C2['listed'] == 6
    l3 = 'ELIDED DOI' in bu
    l4 = 'A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE' in bu
    gl3 = l1 and l2 and l3 and l4
    print('    ### **EVERY UNLISTED DOI CARRIES A VERDICT : %s** (%d = %d + %d)'
          % (l1, C2['unlisted'], C2['passes'], C2['fails']))
    print('    ### **THE ELIDED-DOI ARTEFACT IS PRINTED : %s**' % l3)
    print('    %s' % ('PASS' if gl3 else '### FAIL ###'))
    if not gl3:
        fails.append('G-LIMBS/G-ELIDED')

    # --------------------------------------------------------------- BAR 8, THE EXPECTATION BAR
    print(chr(10) + '  G-SEPARATE (BAR 8):')
    s1 = C2['fails'] == 2 and C2['l2'] is False
    s2 = 'IS REPORTED REFUTED' in bu
    s3 = 'AN EXPECTATION IS NOT A TARGET' in bu
    s4 = C2.get('kernel_established') is False and 'WITHDRAWN AS NOT ESTABLISHED' in bu
    s5 = 'PROXIMITY IS NOT ATTACHMENT' in bu
    gs = s1 and s2 and s3 and s4 and s5
    print('    ### **FAILING BOTH LIMBS : %d ; (L2) : %s ; REPORTED REFUTED : %s**'
          % (C2['fails'], C2['l2'], s2))
    print('    ### **THE SECOND SHAPE IS WITHDRAWN, NOT ADDED : %s**' % s4)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SEPARATE')

    # ------------------------------------------------------------------------- G-NOZENODOWRITE
    print(chr(10) + '  G-NOZENODOWRITE / G-NOREGROW:')
    z1 = not [(x, k) for x in mymods1 for k in ("'POST'", "'PUT'", "'DELETE'", 'access_token')
              if k in strip_prose(t(x))]
    pre_reg = blob_of(PP, 'REGISTRY.md', preact(PP)) or ''
    now_reg = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8',
                      errors='replace').read()
    rows_before = len([x for x in norm(pre_reg).split(chr(10)) if x.startswith('| ')])
    rows_after = len([x for x in norm(now_reg).split(chr(10)) if x.startswith('| ')])
    z2 = rows_before == rows_after
    z3 = 'NOTHING DEPOSITS' in bu
    gz = z1 and z2 and z3
    print('    ### **REGISTRY TABLE ROWS : %d BEFORE, %d AFTER -- NO ROW ADDED OR EDITED : %s**'
          % (rows_before, rows_after, z2))
    print('    %s' % ('PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-NOZENODOWRITE/G-NOREGROW')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = ('THE FOUR LISTS STAY OPEN by name' in tblk
          or 'four lists stay OPEN by name' in tblk)
    n3 = Q['lists_closed'] == 0
    # ### **THE CITATION QUESTION IS RESTATED AND NOT MOVED.**
    # ### **THE ITEM THIS ARM WATCHED IS CLOSED BY `(R19)` IN THIS ACT.** ### The inherited
    # ### form demanded it STAND and say `NOT MOVED`; here the author ruled and the question has
    # ### an answer in the standing record. ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY
    # ### ### SET** (`b390`) -- so it now requires the row to be CLOSED and to name the ruling.
    cq = [m for m in Q['marks'] if 'citation question' in m['item']]
    n4 = (len(cq) == 1 and cq[0]['disposition'] == 'CLOSE'
          and '(R19)' in cq[0]['why'])
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
    print('    ### **THE CITATION QUESTION IS CLOSED BY (R19), AND THE ROW NAMES THE '
          'RULING** : %s' % n4)
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
               'PLACE-papers': {'OPEN_TRAILS.md',
                                'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
                                'REGISTRY.md', 'README.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b392' not in x)
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
    t3 = len(rws) == 1 and anc and 'THE TWO RULINGS WRITTEN' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-two-rulings-r19-and-r20 returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('a document was reclassified', 'prior taxonomy text was edited',
              'the platform was asked', 'something was deposited'))
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
    BEFORE = (('lockgate', LG),)
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
    mirrorp = d('b392_mirror.txt')
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
        ('DOIs known %d' % C2['known'], str(C2['known']) in bank),
        ('listed %d' % C2['listed'], str(C2['listed']) in bank),
        ('unlisted %d' % C2['unlisted'], str(C2['unlisted']) in bank),
        ('passing limb b %d' % C2['passes'], str(C2['passes']) in bank),
        ('failing both limbs %d' % C2['fails'], str(C2['fails']) in bank),
        ('the taxonomy diff +%d' % C1['file']['added'], str(C1['file']['added']) in bank
         or str(C1['file']['added'] + C2['registry']['added'] + C2['readme']['added']) in bank),
        ('row %s' % ROWNUM, str(Q['row']) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the component run', AC['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('lockgate', LG), ('components', AC), ('desk_bank', Q)):
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
                          if x.startswith('b392_') and x.endswith('.py')))
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
              if x.strip() and 'b392' not in x and x.strip() not in DECLARED_W]
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
             d('b392_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b392_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE TWO RULINGS (b392).'
    nxt = '# ### THE PHANTOM VERSION REPAIRED (b391).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b392_stem_'), 'blk.txt')
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
    tmpdir = tempfile.mkdtemp(prefix='b392_hedge_')
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
