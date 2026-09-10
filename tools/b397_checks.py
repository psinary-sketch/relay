# -*- coding: utf-8 -*-
"""b397_checks.py -- THE GATE SUITE FOR THE UNLANDED WORK.

### ### **THE ARM THAT MATTERS MOST IS `G-BOTHWAYS`.** ### This act's finding turns entirely on a
### direction, and its first survey read the direction backwards: `rev-list --left-right --count
### main...b` puts the count of commits ### **ONLY IN MAIN** ### on the left, and eight merged
### branches read as one commit ahead. ### **THE FINDING WOULD HAVE BEEN THE EXACT OPPOSITE OF THE
### ### TRUTH.** ### The arm requires every branch to carry an `ahead`, a `behind` and a `--merged`
### verdict, ### **EACH RE-MEASURED HERE BY ITS OWN COMMAND**, and requires the misreading to be
### named in the bank with the number it produced.
###
### ### **`G-READONLY` PROVES THE BRANCH READ LEFT NO MARK.** ### Every repository's branch and
### `HEAD` must be byte-identical to what the components recorded before they ran, and `0` merges,
### `0` pushes, `0` checkouts, `0` clones and `0` builds.
###
### ### **`G-TRUEDISCLOSURE` IS THE ARM AGAINST THIS ACT'S OWN TEMPTATION.** ### The rule demands
### a disclosure and the rule's own instance is stale, so the arm requires that ### **NO ROW WHOSE
### ### TERMINAL IS ON `main` WAS ANNOTATED** -- writing it would put a false statement in a status
### column under the authority of a rule.
###
### ### **AND `G-NOTBUILT` REFUSES A DRESSED-UP UNKNOWN.** ### There is no printed profile on the
### live ref, so no axiom profile is asserted for it, `(F1)` reads `NOT ESTABLISHED`, and the arm
### requires the bank to say ### **NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD.**
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


def raw(n):
    """### **THE TOOL'S OWN BYTES.** ### `t()` returns a PATH, and three arms of this suite
    ### tested a substring OF A FILENAME on their first run -- always False, and a positive arm
    ### that cannot pass is not an arm. ### **AND IT MUST NOT BE `strip_prose`**: that deletes
    ### string-span lines, which is exactly what a positive arm about a LITERAL needs to see
    ### (`b387`)."""
    return io.open(t(n), encoding='utf-8', errors='replace').read()


BANK = d('b397_the_unlanded_work.txt')
REG = d('b397_registration_2026-09-10.txt')
FERRY = d('b397_ferry_2026-09-10.txt')
SCAN, TERMSCAN, GATE = d('b397_ferry_scan.txt'), d('b397_reg_termscan.txt'), d('b397_reg_gate.txt')
CENSUS0, FCEN = d('b397_census_stepzero.txt'), d('b397_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b397_regspec_run.txt'), d('audit_b397_reg_satisfiable.txt')
PINS0 = d('b397_pins_stepzero.txt')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
TAXONOMY = 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md'
UNTOUCHED = (TAXONOMY, 'REGISTRY.md', 'README.md', 'SPIRAL_MAP.md', 'FINDINGS.md',
             'phase2/method/THE_KEYSTONE_CENSUS.md',
             'phase1.5/spectral/GRH_CASCADE.md',
             'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
             'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md')
CONSTMAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SEAL = 'fb4d36f4fe434e33c3070872a04df9b340e81c210bb59303beec3c83ce9fce4b'
ROWNUM = '246'
TRAIL_MARK = ('<!-- b397 the unlanded work: eight of nine landed, and a queue with triggers -->')
_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('AC', 'b397_components.json'), ('LG', 'b397_lockgate.json'),
                   ('E', 'b397_reads.json'), ('Q', 'b397_desk.json'))}

IDX = d(_J['Q']['run_file'])

NEW_THIS_ACT = {'tools/b397_regspec.py', 'tools/b397_reg_gate.py', 'tools/b397_extract.py',
                'tools/b397_components.py', 'tools/b397_desk_bank.py', 'tools/b397_checks.py'}

TOOLNUM = [
    ('the extract, and the four surveys inside it', 'tools/b397_extract.py'),
    ('the inventory, the sweep and the board', 'tools/b397_components.py'),
    ('the desk, the queue, the ledger writes and the bank', 'tools/b397_desk_bank.py'),
    ('the registration gate', 'tools/b397_reg_gate.py'),
    ('the clause spec', 'tools/b397_regspec.py'),
    ('the anchor, with the preserved-block mode b396 added', 'tools/anchor_from_file.py'),
    ('the lock gate that checks what each gate read', 'tools/b378_lockgate.py'),
    ('the face-subject stamps', 'tools/gate_hash.py'),
    ('%s bytes on disk, and the lock clock' % os.path.getsize(REG), 'tools/reg_seal.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the roster, imported and not typed', 'tools/b303_pins.py'),
]

OWNER_NEEDLES = [
    ('the order -- (R22)', FERRY, 'RULING (R22), the author'),
    ('the order -- the audit lane parked', FERRY,
     'strikeable: THE INSTRUMENT-AUDIT LANE IS PARKED. b396 measured'),
    ('the order -- a trigger each', FERRY,
     'Remaining audit items go to the trails with a TRIGGER each —'),
    ('the order -- content is not audit work', FERRY,
     'sake. Reading the corpus for CONTENT is not audit work and is'),
    ('the order -- the act', FERRY, 'ACT b397 — THE UNLANDED WORK. Number not claimed by any'),
    ('the order -- read for content', FERRY,
     'COMPONENT 1 — WHAT IS ON THE HELD BRANCHES, read for content'),
    ('the order -- the question this act answers', FERRY,
     'exists to answer: WHAT HAS THE PROGRAMME COMPILED THAT IT'),
    ('the order -- read only', FERRY,
     'branch, no branch checked out destructively; read only. Where a'),
    ('the order -- retired is not unlanded', FERRY,
     "terminal's own text says RETIRED, that is reported as retired"),
    ('the order -- the disclosure rule', FERRY,
     'COMPONENT 2 — THE DISCLOSURE RULE, APPLIED. The record'),
    ('the order -- swept and repaired apart', FERRY,
     'precedent. Report rows swept and rows repaired apart. Where a'),
    ('the order -- the queue with triggers', FERRY,
     'COMPONENT 3 — THE QUEUE, WITH TRIGGERS. Enter on the trails'),
    ('the order -- the board from the record', FERRY,
     'COMPONENT 4 — THE RESEARCH BOARD, RESTATED FROM THE RECORD and'),
    ('the order -- (F1)', FERRY,
     "navigator's expectations: (F1) at least one held branch carries"),
    ('the order -- (F2)', FERRY,
     'disclosure sweep repairs fewer rows than it sweeps, because'),
]

SELF_NEEDLES = [
    ('the bank leads with the eight that landed', BANK,
     '### ### ### **EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED. ### WHAT IS'),
    ('### (R22) is recorded', BANK, '### RULING `(R22)`, RECORDED.'),
    ('### content is not audit work', BANK,
     '### ### **AND THE CLAUSE THAT KEEPS THIS ACT LEGAL:** ### *reading the corpus for'),
    ('### the prose did not follow it', BANK,
     '### ### ### PROPAGATED. ### THE WORK LANDED AND THE PROSE DID NOT FOLLOW IT** --'),
    ('### the counting trap', BANK,
     '### ### THE EXACT OPPOSITE OF THE TRUTH.** ### Caught by one branch reading `0 0`,'),
    ('### against main, where a reader resolves it', BANK,
     '### ### **THE CITATION TEST IS AGAINST `main`, WHERE A READER RESOLVES IT** -- and'),
    ('### expected is not printed', BANK,
     '### ### comment says ### *Expected: ... axiom-free* ### -- ### **EXPECTED, NOT'),
    ('### no evidence of a build', BANK,
     '### ### PRINTED.** ### **NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD**, a'),
    ('### the rule`s instance is stale', BANK,
     '### ### branch is ### **MERGED.** ### **WRITING THE DEMANDED DISCLOSURE THERE WOULD'),
    ('### the rule is not amended here', BANK,
     '### ### **THE RULE IS NOT STRUCK AND NOT AMENDED HERE. ### ITS INSTANCE IS ROUTED.**'),
    ('### swept and repaired apart', BANK, '### ### **REPORTED APART AND NEVER ADDED.**'),
    ('### a prediction met for the wrong reason', BANK,
     '### ### is owed. ### **A PREDICTION MET FOR THE WRONG REASON IS REPORTED WITH THE'),
    ('### a trigger is not a plan', BANK,
     '### ### **A TRIGGER IS NOT A PLAN AND A QUEUE IS NOT A COMMITMENT.**'),
    ('### a quotation of an absence', BANK,
     '### ### ABOUT ONE.**'),
    ('### a queued item is not discharged', BANK,
     '### ### and ### **A QUEUED ITEM IS NOT A DISCHARGED ITEM.**'),
]

MUST_FAIL = [
    ('the bank never says a direction was assumed', BANK, '### A DIRECTION WAS ASSUMED.'),
    ('the bank never says a branch was merged', BANK, '### A BRANCH WAS MERGED.'),
    ('the bank never says a branch was checked out', BANK, '### A BRANCH WAS CHECKED OUT.'),
    ('the bank never says a build was run', BANK, '### A BUILD WAS RUN.'),
    ('the bank never says an unknown was compiled', BANK,
     '### AN UNKNOWN WAS REPORTED AS COMPILED.'),
    ('the bank never says a false disclosure was written', BANK,
     '### A FALSE DISCLOSURE WAS WRITTEN.'),
    ('the bank never says an item was opened', BANK, '### AN ITEM WAS OPENED.'),
    ('the bank never says the platform was called', BANK, '### THE PLATFORM WAS CALLED.'),
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
        if not subj.startswith('b397'):
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
    print('b397 -- GATE SUITE (THE UNLANDED WORK)')
    print('=' * 100)
    LG, AC, Q, E = _J['LG'], _J['AC'], _J['Q'], _J['E']
    extract = io.open(d(Q['run_file']), encoding='utf-8', errors='replace').read()
    acrun = io.open(d(AC['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES ### (THE ORDER, AS THE EXTRACT RECORDED IT):')
    # ### **THIS ACT HAS NO EXTRACT FILE.** ### `b397` is a five-tool act: the order is read
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
    # ### **THE EXTRACT'S OWN RUN FILE, READ BY ITS RECORDED CLOCK** (`b358`), so the arms that
    # ### test WHAT THE SURVEY PRINTED read the survey and not this suite's memory of it.
    ext = io.open(os.path.join(D, E['run_file']), encoding='utf-8', errors='replace').read()
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
    l7 = LG['act'] == 'b397' and not os.path.exists(t('b397_lockgate.py'))
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

    C1, C2, C4 = AC['c1'], AC['c2'], AC['c4']
    S1, S2, S3 = E['s1'], E['s2'], E['s3']

    # ------------------------------------------------------------- BAR 2, THE BOTH-DIRECTIONS BAR
    print(chr(10) + '  G-BOTHWAYS / G-MERGED / G-LEFTRIGHT (BAR 2) ### THE ARM THAT MATTERS:')
    # ### **EVERY BRANCH IS RE-MEASURED HERE, BY ITS OWN COMMAND, AND NOT TAKEN FROM THE JSON.**
    bad = []
    for x in S1['rows']:
        rp = os.path.join('D:' + os.sep, x['repo'])
        ah = git(rp, 'rev-list', '--count', 'main..' + x['branch']).strip()
        bh = git(rp, 'rev-list', '--count', x['branch'] + '..main').strip()
        mg = x['branch'] in [z.strip().lstrip('* ') for z in
                             git(rp, 'branch', '--merged', 'main').split(chr(10))]
        if int(ah or 0) != x['ahead'] or int(bh or 0) != x['behind'] or mg != x['merged']:
            bad.append((x['repo'], x['branch'], ah, bh, mg))
    d1 = not bad
    d2 = C1['landed'] == 8 and C1['live'] == 1 and C1['research'] == 9
    d3 = 'THE EXACT OPPOSITE OF THE TRUTH' in bu
    d4 = 'ONLY IN MAIN' in bu and '0 0' in bank
    d5 = C1['push'] == 2 and 'EXCLUDED' in bu
    gd = d1 and d2 and d3 and d4 and d5
    print('    ### **EVERY BRANCH RE-MEASURED HERE AGREES WITH THE SURVEY : %s**  %s'
          % (d1, bad[:2] or 'none'))
    print('    ### **RESEARCH %d ; LANDED %d ; LIVE %d ; PUSH EXCLUDED %d**'
          % (C1['research'], C1['landed'], C1['live'], C1['push']))
    print('    the misreading is named with the number it produced : %s' % (d3 and d4))
    print('    %s' % ('PASS' if gd else '### FAIL ###'))
    if not gd:
        fails.append('G-BOTHWAYS/G-MERGED/G-LEFTRIGHT')

    # ------------------------------------------------------------------ BAR 3, THE READ-ONLY BAR
    print(chr(10) + '  G-READONLY / G-NOMERGE / G-NOCHECKOUT / G-HEADSAME (BAR 3):')
    now = {}
    for k in AC['refs_after']:
        rp = ROOT if k == 'relay' else (PP if k == 'PLACE-papers'
                                        else os.path.join('D:' + os.sep, k))
        now[k] = dict(branch=git(rp, 'rev-parse', '--abbrev-ref', 'HEAD').strip(),
                      head=git(rp, 'rev-parse', 'HEAD').strip()[:12])
    # ### relay legitimately moves onto its own push branch, so it is compared by REPOSITORY
    # ### and the kernel repositories are the ones that must not have moved at all.
    # ### **THE POPULATION IS THE REPOSITORIES WHOSE BRANCHES THIS ACT READ, TAKEN FROM THE
    # ### SURVEY AND NOT FROM A NAME PREFIX.** ### A `SIDE-*` prefix also catches
    # ### `SIDE-global-section`, which is the CORRESPONDENCE LEDGER this act declares as a
    # ### write target in section (G) -- so the arm fired on a write the face permits.
    # ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`).
    kernels = sorted(set(x['repo'] for x in S1['rows']))
    moved = [k for k in kernels if now[k] != AC['refs_after'][k]]
    r1 = not moved
    r2 = AC['readonly'] is True
    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b397_') and x.endswith('.py')))
    # ### **`merge` AS A SUBSTRING MATCHES `--merged`, WHICH IS A READ.** ### The arm
    # ### fired on this act's own extract for using the very flag that PROVES the branches
    # ### were not merged by it. ### **AN ARM THAT FORBIDS A WORD FORBIDS ITS READING TOO**,
    # ### so the verbs are matched as COMMANDS and not as substrings.
    FORBID = ('git merge', 'merge --', 'git checkout', 'checkout -', 'git clone',
              'lake ', 'LEAN_PATH', 'push origin')
    hits = [(x, k) for x in mymods for k in FORBID if k in strip_prose(t(x))]
    r3 = not hits
    # ### **NO `.lean` FILE MOVED IN ANY KERNEL REPOSITORY.**
    leans = []
    for k in kernels:
        rp = os.path.join('D:' + os.sep, k)
        st = git(rp, 'status', '--porcelain')
        leans += [z for z in st.split(chr(10)) if z.strip().endswith('.lean')]
    r4 = not leans
    gr = r1 and r2 and r3 and r4
    print('    ### **KERNEL REPOSITORIES WHOSE BRANCH OR HEAD MOVED : %s**' % (moved or 'none'))
    print('    the components measured read-only before and after : %s' % r2)
    print('    forbidden verbs in this act`s tools : %s' % (hits or 'none'))
    print('    ### **`.lean` FILES DIRTY IN ANY KERNEL REPOSITORY : %s**' % (leans or 'none'))
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-READONLY/G-NOMERGE/G-NOCHECKOUT/G-HEADSAME')

    # -------------------------------------------------------- BAR 4, THE CITATION-AGAINST-MAIN BAR
    print(chr(10) + '  G-AGAINSTMAIN / G-CITABLE (BAR 4):')
    absent = [o for o in S2['decls'] if not o['on_main']]
    onmain = [o for o in S2['decls'] if o['on_main']]
    m1 = len(absent) == C1['absent'] == 4
    m2 = all(o['main_files'] for o in onmain) or not onmain
    m3 = C1['cited'] == 3 and C1['uncited'] == 1
    m4 = 'WHERE A READER RESOLVES IT' in bu
    # ### **THE TWO THAT LANDED MUST BE NAMED AS CITABLE.**
    m5 = 'invariance_barrier' in bank and 'DeterminedBy' in bank
    gm = m1 and m2 and m3 and m4 and m5
    print('    ### **DECLARATIONS %d ; ABSENT FROM main %d ; CITED %d ; UNCITED %d**'
          % (len(S2['decls']), len(absent), C1['cited'], C1['uncited']))
    print('    the two that already stand on main are named citable : %s' % m5)
    print('    %s' % ('PASS' if gm else '### FAIL ###'))
    if not gm:
        fails.append('G-AGAINSTMAIN/G-CITABLE')

    # ------------------------------------------------------------------ BAR 5, THE NOT-BUILT BAR
    print(chr(10) + '  G-NOTBUILT / G-NOPROFILE / G-NOBUILD (BAR 5):')
    n1 = C1['printed_profiles'] == 0
    n2 = 'NOT BUILT' in bu
    n3 = 'NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO BUILD' in bu
    n4 = C1['f1'] == 'NOT ESTABLISHED' and 'NOT ESTABLISHED' in bu
    n5 = 'EXPECTED, NOT' in bu
    # ### **AND NO AXIOM LIST IS ASSERTED FOR THE LIVE BRANCH IN THIS ACT'S OWN PROSE.**
    n6 = 'depends on axioms' not in bank
    gn = n1 and n2 and n3 and n4 and n5 and n6
    print('    ### **PRINTED PROFILES ON THE LIVE REF : %d ; NOT BUILT SAID : %s**'
          % (C1['printed_profiles'], n2))
    print('    ### **(F1) : %s** ; expected-is-not-printed said : %s' % (C1['f1'], n5))
    print('    no axiom list asserted for the live branch : %s' % n6)
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOTBUILT/G-NOPROFILE/G-NOBUILD')

    # ------------------------------------------------------- BAR 6, THE TRUE-DISCLOSURE BAR
    print(chr(10) + '  G-TRUEDISCLOSURE / G-SWEPTAPART / G-NODELETE / G-PRESERVED (BAR 6):')
    # ### **NO ROW WHOSE TERMINAL IS ON `main` MAY CARRY THIS ACT'S DISCLOSURE.**
    landed_names = sorted(set(o['name'] for o in S2['decls'] if o['on_main']))
    falsely = []
    for w in C2['written']:
        body = io.open(os.path.join(PP, w['doc'].replace('/', os.sep)), encoding='utf-8',
                       errors='replace').read()
        for ln in body.split(chr(10)):
            if 'BRANCH-RESIDENT: this terminal is on' not in ln:
                continue
            if any(nm in ln for nm in landed_names):
                falsely.append(w['doc'])
    t1 = not falsely
    t2 = C2['repaired'] < C2['swept'] and C2['repaired'] == 6 and C2['swept'] == 15
    t3 = C2['lost'] == 0
    t4 = all(str(v) in bank for v in (C2['swept'], C2['repaired'], C2['already'], C2['routed']))
    t5 = 'FALSE STATEMENT IN A STATUS COLUMN' in bu
    t6 = all('line ' in io.open(os.path.join(PP, w['doc'].replace('/', os.sep)),
                                encoding='utf-8', errors='replace').read().split(C2['mark'])[-1]
             for w in C2['written'])
    gt = t1 and t2 and t3 and t4 and t5 and t6
    print('    ### **ROWS ANNOTATED WHOSE TERMINAL IS ON main : %s**' % (falsely or 'none'))
    print('    ### **SWEPT %d ; REPAIRED %d ; SWEPT-NOT-REPAIRED %d ; ROUTED %d**'
          % (C2['swept'], C2['repaired'], C2['already'], C2['routed']))
    print('    ### **CONTENT LOST : %d** ; the pre-edit lines are quoted with their numbers : %s'
          % (C2['lost'], t6))
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRUEDISCLOSURE/G-SWEPTAPART/G-NODELETE/G-PRESERVED')

    # ------------------------------------------------------------------- BAR 7, THE TRIGGER BAR
    print(chr(10) + '  G-TRIGGERS / G-NOTHINGOPENED (BAR 7):')
    trig = Q.get('triggers', 0)
    q1 = trig == 6
    q2 = bank.count('TRIGGER:') >= 6
    q3 = 'A TRIGGER IS NOT A PLAN AND A QUEUE IS NOT A COMMITMENT' in bu
    q4 = Q['lists_closed'] == 0
    gq = q1 and q2 and q3 and q4
    print('    ### **QUEUE ITEMS %d ; TRIGGER LINES IN THE BANK %d**' % (trig,
                                                                        bank.count('TRIGGER:')))
    print('    nothing opened, no list closed : %s' % (q3 and q4))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-TRIGGERS/G-NOTHINGOPENED')

    # ------------------------------------------------------------------ BAR 8, THE QUOTATION BAR
    print(chr(10) + '  G-QUOTED / G-NONEWCLAIM (BAR 8):')
    v1 = C4['new_claims'] == 0
    v2 = C4['clause_lines'] > 0 and C4['faces_rows'] > 0
    v3 = str(C4['faces_rows']) in bank
    v4 = 'QUOTATION, NOT COMPOSITION' in bu
    v5 = 'A QUOTATION OF AN ABSENCE' in bu
    gv = v1 and v2 and v3 and v4 and v5
    print('    ### **NEW CLAIMS BY THE BOARD : %d ; CLAUSE LINES %d ; FACES ROWS %d**'
          % (C4['new_claims'], C4['clause_lines'], C4['faces_rows']))
    print('    the absence is quoted rather than claimed : %s' % v5)
    print('    %s' % ('PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-QUOTED/G-NONEWCLAIM')

    # ------------------------------------------------------- G-R22 / G-NOSWEEP / G-NORULEAMEND
    print(chr(10) + '  G-R22 / G-NOSWEEP / G-NORULEAMEND:')
    y1 = 'THE INSTRUMENT-AUDIT LANE IS PARKED' in bu
    y2 = 'is not audit work' in bank
    # ### **THE RULE THIS ACT FOUND STALE MUST BE BYTE-IDENTICAL TO THE PRE-ACT BLOB.**
    y3 = True
    for rel in ('REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS.md'):
        pr = blob_of(PP, rel, preact(PP)) or ''
        nw = io.open(os.path.join(PP, rel.replace('/', os.sep)), encoding='utf-8',
                     errors='replace').read()
        if norm(pr) != norm(nw):
            y3 = False
    y4 = 'NOT STRUCK AND NOT AMENDED' in bu
    gy = y1 and y2 and y3 and y4
    print('    ### **(R22) RECORDED : %s ; the content clause carried : %s**' % (y1, y2))
    print('    ### **THE RULE AND THE CENSUS BYTE-IDENTICAL TO THE PRE-ACT BLOB : %s**' % y3)
    print('    the act says it neither struck nor amended it : %s' % y4)
    print('    %s' % ('PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-R22/G-NOSWEEP/G-NORULEAMEND')

    # ------------------------------------------------------------- G-NOWRITE / G-NOPLATFORM
    print(chr(10) + '  G-NOWRITE / G-NOPLATFORM:')
    edited = set(w['doc'] for w in C2['written']) | {'OPEN_TRAILS.md'}
    ptouched = sorted(x for x in git(PP, 'diff', '--name-only', preact(PP)).split(chr(10))
                      if x.strip())
    w1 = set(ptouched) <= edited
    mymods1 = mymods
    NETY = ('zenodo.org', 'doi.org', 'urllib', 'requests', 'curl')
    nhits = [(x, k) for x in mymods1 for k in NETY if k in strip_prose(t(x))]
    w2 = not nhits
    gw2 = w1 and w2
    print('    ### **PLACE-papers FILES CHANGED : %s**' % (ptouched or 'none'))
    print('    ### **ALL WITHIN THE DECLARED SET : %s**' % w1)
    print('    zenodo/http tokens : %s' % (nhits or 'none'))
    print('    %s' % ('PASS' if gw2 else '### FAIL ###'))
    if not gw2:
        fails.append('G-NOWRITE/G-NOPLATFORM')

    # ------------------------------------------------- G-NORULING / G-OPEN / G-NONEWDOC
    print(chr(10) + '  G-NORULING / G-OPEN / G-NONEWDOC:')
    LISTS = ('LIST 1 -- the rows that cite at a ref nobody can name',
             'LIST 2 -- the rows grading a declaration the record has classified absent',
             'LIST 3 -- the undated figures across the roster',
             'LIST 4 -- the bibliography entries nothing cites')
    om = [m for m in Q['marks'] if m['item'] in LISTS]
    n1 = len(om) == 4 and all(m['disposition'] == 'STAND' for m in om)
    n2 = 'four lists stay OPEN by name' in tblk
    n3 = Q['lists_closed'] == 0
    # ### **THE CITATION QUESTION IS RESTATED AND NOT MOVED.**
    # ### **THE ITEM THIS ARM WATCHED IS CLOSED BY `(R19)` IN THIS ACT.** ### The inherited
    # ### form demanded it STAND and say `NOT MOVED`; here the author ruled and the question has
    # ### an answer in the standing record. ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY
    # ### ### SET** (`b390`) -- so it now requires the row to be CLOSED and to name the ruling.
    # ### the item this arm watched was CLOSED at b392; here it is gone from the desk,
    # ### and what stands in its place is the reshaping, which must STAND with the five named.
    cq = [m for m in Q['marks'] if 'stale `HELD` prose' in m['item']]
    n4 = (len(cq) == 1 and cq[0]['disposition'] == 'STAND'
          and 'REWRITING THE PROSE IS AUTHORING' in cq[0]['why'].upper())
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
    print('    ### **THE STALE `HELD` PROSE STANDS AS AN OPEN ITEM** : %s' % n4)
    print('    no new tracking document in PLACE-papers : %s %s' % (n5, newdocs[:2] or ''))
    print('    ### **UNTRACKED PATHS THAT ARE NOT TRACKING DOCUMENTS, EXCLUDED AND NAMED** : %s'
          % (notdocs or 'none'))
    print('    %s' % ('PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NORULING/G-OPEN/G-NONEWDOC')

    # ------------------------------------ G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE
    print(chr(10) + '  G-NOWRITE / G-NOREGISTRY / G-NOHOOKSDELETE:')
    # ### **THE ANCHOR TOOL IS THE ONE OWNER INSTRUMENT SECTION `(F)` DECLARES**, and it
    # ### is allowed HERE BY NAME so that a second undeclared owner edit still fails.
    ALLOWED = {'relay': {'tools/banked_index.py', 'tools/anchor_from_file.py'},
               'SIDE-global-section': {'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md',
                                'phase1.5/rcurve/R_CURVE_CRITERION.md',
                                'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md',
                                'phase1.5/method/THE_LOAD_BEARING_MAP.md',
                                'phase1.5/proofs/HELD_WMINEDERIV_crystallization.md'},
               'SIDE-effects': set()}
    dirtyrepo = {}
    for name, repo in b303_pins.REPOS:
        ch = set(x.strip() for x in
                 git(repo, 'diff', '--name-only', preact(repo)).split(chr(10)) if x.strip())
        if name == 'relay':
            ch = set(x for x in ch if 'b397' not in x)
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
    t3 = len(rws) == 1 and anc and 'EIGHT OF THE NINE HELD BRANCHES' in rws[0]
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    t4 = ('the-unlanded-work returns 1 row(s)' in irun
          and Q['key_ok'] is True)
    t5 = all(('%-44s NO KEY after  : True' % qq) in irun for qq in
             ('a branch was merged', 'a branch was checked out',
              'a build was run', 'the platform was called'))
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
    mirrorp = d('b397_mirror.txt')
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
        ('research branches %d' % C1['research'], str(C1['research']) in bank),
        ('landed %d' % C1['landed'], str(C1['landed']) in bank),
        ('live %d' % C1['live'], str(C1['live']) in bank),
        ('declarations %d' % C1['decls'], str(C1['decls']) in bank),
        ('absent from main %d' % C1['absent'], str(C1['absent']) in bank),
        ('rows swept %d' % C2['swept'], str(C2['swept']) in bank),
        ('rows repaired %d' % C2['repaired'], str(C2['repaired']) in bank),
        ('swept-not-repaired %d' % C2['already'], str(C2['already']) in bank),
        ('documents edited %d' % C2['docs'], str(C2['docs']) in bank),
        ('content lost %d' % C2['lost'], str(C2['lost']) in bank),
        ('faces rows %d' % C4['faces_rows'], str(C4['faces_rows']) in bank),
        ('the rule line %d' % S3['rule_registry_line'],
         str(S3['rule_registry_line']) in bank),
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
    for lbl, jf in (('extract', E), ('lockgate', LG), ('components', AC),
                    ('desk_bank', Q)):
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
                          if x.startswith('b397_') and x.endswith('.py')))
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
    # ### **ONE OWNER INSTRUMENT IS EDITED AND THE FACE NAMES IT:** ### section (F) declares
    # ### `tools/anchor_from_file.py` -- one added, opt-in, default-off mode and its fixtures.
    # ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`), and this face set a bar
    # ### that permits exactly this file and no other.
    owner = ['tools/reg_seal.py', 'tools/registration_gate.py', 'tools/gate_text.py',
             'tools/run_clock.py', 'tools/anchor_from_file.py', 'tools/quote_norm.py',
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/hedge_audit.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b374_hedge.py',
             'tools/b375_population.py', 'tools/gate_hash.py', 'tools/b378_lockgate.py',
             'tools/role_structure.py', 'tools/co_location.py']
    # ### **THE ONE OWNER INSTRUMENT THIS FACE DECLARES IS EXCLUDED FROM THE UNDECLARED LIST**,
    # ### and it is excluded BY NAME so that a second one would still be caught.
    OWNER_DECLARED = ('tools/anchor_from_file.py',)
    touched = [p for p in owner
               if p not in OWNER_DECLARED
               and git(ROOT, 'diff', '--name-only', preact(ROOT), '--', p).strip()]
    # ### **`tools/b304_hooks.py` IS AN OWNER INSTRUMENT AND IT IS EDITED -- DECLARED ON THE FACE
    # ### BEFORE THE ACT, IN SECTION `(F)`.** ### It is therefore NOT on the list above; a
    # ### declared write is not an undeclared one, and the declaration is what makes the
    # ### difference. ### **THE FACE WAS NOT WIDENED MID-ACT TO ACCOMMODATE IT.**
    DECLARED_W = ('tools/banked_index.py', 'tools/anchor_from_file.py')
    others = [x for x in git(ROOT, 'diff', '--name-only', preact(ROOT)).split(chr(10))
              if x.strip() and 'b397' not in x and x.strip() not in DECLARED_W]
    e1 = not touched and not others
    # ### **b396 EDITED AN OWNER INSTRUMENT AND THIS ACT DOES NOT**, so the inherited clause
    # ### requiring the face to name `anchor_from_file.py` as a WRITE is dropped. ### **AN ARM
    # ### ### MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`), and this face declares the
    # ### index key and the status cells and nothing else in `relay`.
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
             d('b397_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b397_checks.py'), 'its own fixtures'),
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

    marker = '# ### THE UNLANDED WORK (b397).'
    nxt = '# ### THE BACKTICK SWEPT (b396).'
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
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b397_stem_'), 'blk.txt')
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

    print(chr(10) + '  G-CAP ### THE REGISTRATION CAPPED THIS ACT AT EIGHT NEW TOOL FILES:')
    made = sorted('tools/' + x for x in mymods)
    gcap = len(made) <= 8 and set(made) == NEW_THIS_ACT
    print('    new relay tools this act : %d  %s' % (len(made), made))
    print('    %s' % ('PASS' if gcap else '### FAIL ###'))
    if not gcap:
        fails.append('G-CAP')

    print(chr(10) + "  HEDGE AUDIT ON THIS ACT'S OWN PROSE:")
    tmpdir = tempfile.mkdtemp(prefix='b397_hedge_')
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
