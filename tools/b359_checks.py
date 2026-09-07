# -*- coding: utf-8 -*-
"""b359_checks.py -- THE GATE SUITE FOR THE LEDGER CURRENCY PASS.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349),
### every quotation goes through `quote_norm`, and ### **EVERY ARM THAT READS A REPOSITORY STATE DECLARES ITS
### SIDE OF THE PUSH** (b352): `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read BEFORE THE PUSH and again
### after, and the pre-push reading is the one that carries; ### **`G-NOEDIT` STRADDLES TOO AND SAYS SO**
### -- its owner-instrument and TECHNE halves are `SIDE-INVARIANT`, its PAPERS half reads the working tree
### before the push and the HEAD commit's file list after, and PRINTS WHICH SIDE IT IS ON; ### **THIS ACT
### ### WRITES TO THE PAPERS REPO** -- the faces ledger's update block and the errata filing -- ### **SO THE
### ### HOOK AND THE MIRROR ARE OWED AND THIS SUITE CHECKS THEM.**
### ### ### **AND THE ARM THIS SUITE LEANS ON HARDEST:** ### `G-NODEPOSIT`. ### An act that fetches from a
### platform must be able to show it wrote nothing there, and a SENTENCE saying so is worth nothing --
### `G-NODEPOSIT` reads STRIPPED code for a write verb, a method override, a token or a credential.
### ### **EVERY RUN FILE IS RESOLVED BY ITS OWN RECORDED CLOCK AND NEVER BY NAME** (b358 cure): the
### extract, the faces run and the index run all repeated in this act.
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
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import gate_text         # noqa: E402
import quote_norm        # noqa: E402
import reg_seal          # noqa: E402
import anchor_from_file as AF   # noqa: E402
import b359_extract as EX       # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
ERRATA = os.path.join(PP, 'ERRATA.md')
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b359_the_currency_pass.txt')
REG = d('b359_registration_2026-09-07.txt')
FERRY = d('b359_ferry_2026-09-07.txt')
EJ = d('b359_reads.json')
PJ = d('b359_pass.json')
FJ = d('b359_fetch.json')
CORR = d('b359_corr_run.txt')
TERMSCAN, GATE = d('b359_reg_termscan.txt'), d('b359_reg_gate.txt')
CENSUS, FCEN = d('b359_census.txt'), d('b359_faces_census.txt')
REGSPEC, SATIS = d('b359_regspec_run.txt'), d('audit_b359_reg_satisfiable.txt')
PINS, HOOKS = d('b359_pins_stepzero.txt'), d('b359_hooks.txt')
LOCK = '326c9055f6a6511f7e2726c2a51d2b8a0bf4571ce119f623b4593f84e7d5d909'
ROWNUM = '208'
README = os.path.join(PP, 'README.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
ROSTER = t('mirror_roster.json')

OWNED = [BANK, REG, FERRY, EJ, PJ, FJ, CORR,
         d('b359_fetch_F1.json'), d('b359_fetch_F2.json'),
         CENSUS, FCEN, REGSPEC, SATIS, PINS, HOOKS, GATE, TERMSCAN,
         d('b359_satisfiable.json'), d('b359_ferry_scan.txt'), d('b359_faces_row.json'),
         t('b359_fetch.py'), t('b359_extract.py'), t('b359_regspec.py'), t('b359_pass.py'),
         t('b359_correspondence.py'), t('b359_index_check.py'), t('b359_faces_row.py')]

NEW_THIS_ACT = {'tools/b359_fetch.py', 'tools/b359_extract.py', 'tools/b359_regspec.py',
                'tools/b359_pass.py', 'tools/b359_correspondence.py', 'tools/b359_index_check.py',
                'tools/b359_faces_row.py', 'tools/b359_checks.py'}

TOOLNUM = [
    ('the pass, its statuses and its branch', 'tools/b359_pass.py'),
    ('the read-only fetch and its hashes', 'tools/b359_fetch.py'),
    ('the thirty-four reads', 'tools/b359_extract.py'),
    ('the anchors, built by reading', 'tools/anchor_from_file.py'),
    ('the needle puller', 'tools/needle_pull.py'),
    ("the shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('the gate flattener', 'tools/gate_text.py'),
    ('row 208', 'tools/b359_correspondence.py'),
    ('the key, read back', 'tools/b359_index_check.py'),
    ("row U1's second update block", 'tools/b359_faces_row.py'),
    ("the faces ledger's writer, IMPORTED", 'tools/b327_faces_row.py'),
    ('the registration clauses', 'tools/b359_regspec.py'),
    ('19328 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans, and the DEPRECATED arm', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('the hooks', 'tools/b304_hooks.py'),
    ('the roster the mirror reads', 'tools/mirror_roster.json'),
]

SELF_HINTS = [
    ('the bank states the verdict first', 'THE ANSWER, FIRST.'),
    ('### no drift is found', 'NO DRIFT IS FOUND.'),
    ('### the counts', 'SEVEN `CURRENT`, TWO `SILENT`, ZERO'),
    ('### so nothing is appended', 'NOTHING IS APPENDED TO `README.md` OR'),
    ('### both left byte-identical', 'THIS ACT LEAVES THEM BYTE-IDENTICAL'),
    ('### the precedence, quoted', 'Precedence, so a later reader can re-run this'),
    ('### no deposit field checked against disk', 'NO DEPOSIT FIELD WAS CHECKED AGAINST DISK.'),
    ('### the direction was never exercised', 'never exercised -- '),
    ('### the witness is not a fourth rank', 'THE EXTERNAL WITNESS WAS NOT PROMOTED TO A FOURTH RANK.'),
    ('### two GETs, both hashed', 'TWO TARGETS, BOTH `GET`, BOTH HTTP 200, BOTH HASHED'),
    ('### five fields, five agreements', 'FIVE FIELDS, FIVE'),
    ('### the pointer has not drifted', 'SO NO LATEST-VERSION'),
    ('### the eleven', "AND THE `11` IS WORTH ONE LINE."),
    ('### the two silent claims', 'AND BOTH ARE THE SAME SHAPE.'),
    ('### the tense the registration said not to read', 'reading a tense it was told not to read'),
    ('### six asserted, six resolved', 'SIX ASSERTED, SIX RESOLVED, SIX MATCH.'),
    ('### the pin and the head are two objects', 'THEY ARE NOT THE'),
    ('### unresolved was available and not needed', 'AND `UNRESOLVED` WAS AVAILABLE AND WAS NOT NEEDED.'),
    ('### what the archive does not carry', 'IS NOT IN THE MIRROR ROSTER.'),
    ('### the roster is not changed', 'AND THE ROSTER IS NOT CHANGED BY THIS ACT.'),
    ("### the mirror's limit", 'THEY DO NOT CHECK THAT'),
    ('### the expectation, not met', 'NOT MET, AND NOT MET IN ITS FIRST CLAUSE.'),
    ('### the faces run refused and why', 'REFUSED TO WRITE THE BLOCK'),
    ('### registry is read, not written', '`REGISTRY.md` IS NOT WRITTEN.'),
    ('### the shadow', 'EXPECTED: A TIDY AUDIT THAT WOULD FIND A DRIFT AND FILE IT.'),
]

MUST_FAIL = [
    ('the bank never says the deposit is updated', BANK, '### THE DEPOSIT IS UPDATED.'),
    ('the bank never says REGISTRY is repaired from the fetch', BANK,
     '### REGISTRY IS REPAIRED FROM THE FETCH.'),
    ('the bank never says a sentence is edited', BANK, '### A SENTENCE IS EDITED.'),
    ('the bank never says the mirror proves the ledgers true', BANK,
     '### THE MIRROR PROVES THE LEDGERS TRUE.'),
]

def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


# ### ### **THE NUMBERED-REPEAT CURE, GENERALISED (b356 notes2/notes3, b357 run/run2, and TWICE MORE IN
# ### ### THIS ACT).** ### `run_clock` numbers a repeat rather than overwriting, so a suite that NAMES a
# ### run file reads whichever run happened first. ### **THIS RESOLVES THE FILE BY ITS OWN RECORDED CLOCK
# ### ### AND PRINTS WHICH IT CHOSE AND WHY**, so the choice is evidence rather than a habit.
def latest_run(prefix):
    cands = []
    for f in sorted(os.listdir(D)):
        if f.startswith(prefix) and f.endswith('.txt'):
            head = io.open(d(f), encoding='utf-8', errors='replace').readline()
            m = re.search(r'(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)', head)
            if m:
                cands.append((m.group(1), f))
    if not cands:
        return None, None, []
    cands.sort()
    return d(cands[-1][1]), cands[-1][0], cands


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
    print('b359 -- GATE SUITE (THE LEDGER CURRENCY PASS)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    rgf = gate_text.flat(reg)
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-NODEPOSIT (STRIPPED code: nothing this act runs can write to a platform):')
    forbidden = ('POST', 'PUT', 'DELETE', 'PATCH', 'method=', 'get_method', 'token', 'Bearer',
                 'access_token', 'Authorization', 'upload', 'files=', 'data=')
    bad2 = []
    for tool in ('b359_fetch.py', 'b359_pass.py', 'b359_extract.py'):
        code = strip_prose(t(tool))
        for f in forbidden:
            if f in code:
                bad2.append((tool, f))
    F = json.load(io.open(FJ, encoding='utf-8'))
    c1 = not bad2
    c2 = all(x.get('method') == 'GET' for x in F['targets']) and F['method'] == 'GET'
    c3 = F['wrote_anything_remote'] is False
    c4 = 'NOTHING IS DEPOSITED' in bf and 'NOTHING IS WRITTEN AT ZENODO' in bf
    c5 = 'NO DEPOSITED ARTIFACT IS TOUCHED' in bf
    gnd = c1 and c2 and c3 and c4 and c5
    print('    write verbs / tokens / method overrides in stripped code : %s' % (bad2 or 'none'))
    print('    every target recorded as GET : %s ; nothing written remotely : %s' % (c2, c3))
    print('    and the bank says so : %s / %s  %s' % (c4, c5, 'PASS' if gnd else '### FAIL ###'))
    if not gnd:
        fails.append('G-NODEPOSIT')

    print(chr(10) + '  G-FETCH (one read-only fetch per target, hashed, its hash in the bank):')
    f1 = F['fetched'] == F['attempted'] and not F['hard_failure']
    f2 = all(x.get('sha256') for x in F['targets'])
    f3 = all(x['sha256'] in bank or x['sha256'][:16] in bank for x in F['targets'])
    f4 = all(x.get('status') == 200 for x in F['targets'])
    gf = f1 and f2 and f3 and f4
    print('    %d of %d fetched, all HTTP 200 : %s / %s ; hashed : %s ; the hash in the bank : %s  %s'
          % (F['fetched'], F['attempted'], f1, f4, f2, f3, 'PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-FETCH')

    C = json.load(io.open(PJ, encoding='utf-8'))
    E = json.load(io.open(EJ, encoding='utf-8'))

    print(chr(10) + '  G-PRECEDENCE (quoted from the front door, and OBEYED):')
    try:
        pn, pline = AF.find(README,
                            'later reader can re-run this: REGISTRY > README > SPIRAL_MAP for deposits; disk')
        needle_pull.pull(README, pline)
        p1 = True
    except (AF.AnchorError, LookupError):
        p1, pn = False, 0
    p2 = 'REGISTRY > README > SPIRAL_MAP for deposits' in bank
    rb = blob_of(PP, 'REGISTRY.md')
    p3 = (rb is not None) and norm(io.open(REGISTRY, encoding='utf-8').read()) == norm(rb)
    p4 = C['fetch_vs_registry'] == 'AGREE'
    p5 = 'never the reverse' in bf or 'NEVER THE REVERSE' in bf
    gp = p1 and p2 and p3 and p4 and p5
    print('    the precedence sentence located at README.md:%d : %s ; quoted in the bank : %s' % (pn, p1, p2))
    print('    ### **REGISTRY.md IS BYTE-IDENTICAL TO ITS BLOB (READ, NOT WRITTEN)** : %s' % p3)
    print('    fetch and source of truth agree : %s ; the direction is stated : %s  %s'
          % (p4, p5, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PRECEDENCE')

    print(chr(10) + '  G-STATUSES (every claim located and carrying one of the locked three):')
    s1 = all(c['status'] in C['statuses'] for c in C['claims'])
    s2 = len(C['statuses']) == 3
    s3 = not C['unclassified']
    s4 = C['n_current'] + C['n_stale'] + C['n_silent'] == len(C['claims'])
    nbad = 0
    for c in C['claims']:
        path = README if c['doc'] == 'README.md' else MAP
        try:
            needle_pull.pull(path, io.open(path, encoding='utf-8').read().splitlines()[c['line'] - 1])
        except (LookupError, IndexError):
            nbad += 1
    s5 = nbad == 0
    gs = s1 and s2 and s3 and s4 and s5
    print('    %d claims, every status one of the locked three : %s (statuses %d)'
          % (len(C['claims']), s1, len(C['statuses'])))
    print('    none unclassified : %s ; the counts add up : %s ; every line still pullable : %s  %s'
          % (s3, s4, s5, 'PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-STATUSES')

    print(chr(10) + '  G-PINSLIVE (every asserted pin resolved by ls-remote, or UNRESOLVED; none recalled):')
    q1 = C['n_pins'] == len(C['pins']) and C['n_pins'] > 0
    q2 = all(p.get('resolved') or p.get('status') == 'UNRESOLVED' for p in C['pins'])
    q3 = all(p['resolved'].startswith(p['asserted']) for p in C['pins'] if p.get('status') == 'CURRENT')
    q4 = C['n_pins_current'] + C['n_pins_stale'] + C['n_pins_unresolved'] == C['n_pins']
    code = strip_prose(t('b359_pass.py'))
    # ### **`'ls-remote'` IS A STRING LITERAL AND `strip_prose` REMOVES STRINGS**, so looking for it in
    # ### stripped code asks the impossible. ### The arm checks what SURVIVES stripping -- the function and
    # ### its call -- and checks the literal in the RAW source, which is b349's rule: a PRESENCE arm reads
    # ### raw source and a `G-NO*` arm reads stripped code.
    raw = io.open(t('b359_pass.py'), encoding='utf-8').read()
    q5 = ('def ls_remote' in code and 'ls_remote(' in code and "'ls-remote'" in raw)
    gq = q1 and q2 and q3 and q4 and q5
    print('    %d pins, each resolved or UNRESOLVED : %s / %s ; every CURRENT one actually matches : %s'
          % (C['n_pins'], q1, q2, q3))
    print('    the counts add up : %s ; the tool defines and calls ls_remote, and names it raw : %s  %s'
          % (q4, q5, 'PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-PINSLIVE')

    print(chr(10) + '  G-PINHEAD (a deposit-pin and a working head are never merged):')
    lv = [p for p in C['pins'] if p['repo'] == 'SIDE-lv-conservation']
    h1 = len(lv) == 2 and {p['kind'] for p in lv} == {'TAG', 'HEAD'}
    h2 = len({p['asserted'] for p in lv}) == 2
    h3 = 'they are not the same object' in bank
    h4 = 'NOT THE' in bf and 'SAME OBJECT' in bf
    gph = h1 and h2 and h3 and h4
    print('    the lv row is read as TWO objects : %s ; two distinct shas : %s' % (h1, h2))
    print("    the ruling is quoted in the bank : %s / %s  %s" % (h3, h4, 'PASS' if gph else '### FAIL ###'))
    if not gph:
        fails.append('G-PINHEAD')

    print(chr(10) + '  G-APPENDONLY-LEDGER (README and SPIRAL_MAP untouched; REGISTRY byte-identical):')
    a1 = True
    for rel, path in (('README.md', README), ('SPIRAL_MAP.md', MAP), ('REGISTRY.md', REGISTRY)):
        b = blob_of(PP, rel)
        same = (b is not None) and norm(io.open(path, encoding='utf-8').read()) == norm(b)
        print('    %-16s BYTE-IDENTICAL to its blob : %s' % (rel, same))
        a1 = a1 and same
    a2 = C['appended_anything'] is False
    a3 = 'NOTHING IS APPENDED TO `README.md` OR' in bf
    gal = a1 and a2 and a3
    print('    nothing appended : %s ; the bank says so : %s  %s'
          % (a2, a3, 'PASS' if gal else '### FAIL ###'))
    if not gal:
        fails.append('G-APPENDONLY-LEDGER')

    print(chr(10) + '  G-MIRRORCARRIES (rebuilt AFTER the write, three clauses, and what it carries named):')
    mp = d('b359_mirror.txt')
    if os.path.exists(mp):
        mt = io.open(mp, encoding='utf-8', errors='replace').read()
        m1 = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        roster = json.load(io.open(ROSTER, encoding='utf-8'))['files']
        m2 = ('FACES_LEDGER.md' not in roster)
        m3 = 'IS NOT IN THE MIRROR ROSTER' in bf
        m4 = all(x in bank for x in ('README.md', 'SPIRAL_MAP.md', 'REGISTRY.md'))
        rb2 = blob_of(ROOT, 'tools/mirror_roster.json')
        m5 = (rb2 is None) or norm(io.open(ROSTER, encoding='utf-8').read()) == norm(rb2)
        gm = m1 and m2 and m3 and m4 and m5
        print('    clean on all three clauses : %s' % m1)
        print('    ### the faces ledger is genuinely absent from the roster : %s ; reported : %s' % (m2, m3))
        print('    the carried documents named in the bank : %s ; ### **THE ROSTER IS UNCHANGED** : %s  %s'
              % (m4, m5, 'PASS' if gm else '### FAIL ###'))
    else:
        gm = False
        print('    ### the mirror record is NOT YET WRITTEN (it is written AFTER the push).')
    if not gm:
        fails.append('G-MIRRORCARRIES')

    print(chr(10) + "  G-BRANCH (the branch by (H)'s locked rule, the others shown unreachable):")
    RUN, rclock, rcands = latest_run('b359_pass_run')
    print('    ### the pass run is RESOLVED BY ITS OWN CLOCK, not named : %s of %s'
          % (os.path.basename(RUN) if RUN else 'none', [c[1] for c in rcands]))
    run = io.open(RUN, encoding='utf-8').read()
    rf = gate_text.flat(run)
    b1 = C['verdict'] == 'NO DRIFT IS FOUND' and 'NO DRIFT IS FOUND.' in bf
    b2 = '(THE FETCH DID NOT RETURN) -- UNREACHABLE, AND SHOWN SO' in rf
    b3 = '(THE SOURCE OF TRUTH AND THE FETCH DISAGREE) -- UNREACHABLE, AND SHOWN SO' in rf
    b4 = '(A DRIFT IS FOUND AND FILED) -- UNREACHABLE, AND SHOWN SO' in rf
    b5 = C['n_stale'] == 0 and C['n_pins_stale'] == 0 and C['fetch_vs_registry'] == 'AGREE'
    b6 = 'THE MIXTURE RULE, LOCKED BEFORE THE READING' in rf
    gb = b1 and b2 and b3 and b4 and b5 and b6
    print('    verdict agrees : %s ; all three others unreachable : %s / %s / %s' % (b1, b2, b3, b4))
    print('    the branch conditions recompute : %s ; mixture rule named : %s  %s'
          % (b5, b6, 'PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-PRELOCK (the pre-lock reads declared, and no currency claim formed before the lock):')
    k1 = '(A-PRE) THE READS MADE BEFORE THE LOCK' in reg
    k2 = 'NO CLAIM ABOUT THE CURRENCY OF ANY DOCUMENT WAS FORMED' in rgf
    k3 = 'NO FETCH WAS MADE, AND NO PIN WAS RESOLVED' in rgf
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    k4 = (stampm is not None) and stampm.group(1) < F['run_clock'] < E['run_clock'] < C['run_clock']
    k5 = 'THREE PRE-LOCK READS DECLARED' in bf
    gk = k1 and k2 and k3 and k4 and k5
    print('    section (A-PRE) present : %s ; no currency claim formed : %s ; no fetch, no pin : %s'
          % (k1, k2, k3))
    print('    ### **LOCK %s < fetch %s < extract %s < pass %s** : %s ; declared in the bank : %s  %s'
          % (stampm.group(1) if stampm else '?', F['run_clock'], E['run_clock'], C['run_clock'],
             k4, k5, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-PRELOCK')

    print(chr(10) + '  G-ANCHORS (every anchor built by the tool; its fixtures run; the count printed):')
    a_1 = AF.self_test(False)
    a_2 = E['without_anchor'] == 0 and E['anchors_differing'] > 0
    a_3 = str(E['anchors_differing']) in bank and str(E['reads']) in bank
    a_4 = 'REFUSED TO WRITE THE BLOCK' in bf
    ga = a_1 and a_2 and a_3 and a_4
    print('    fixtures hold : %s ; without a match : %d ; differing from their hint : %d of %d'
          % (a_1, E['without_anchor'], E['anchors_differing'], E['reads']))
    print("    the faces writer's refusal is reported : %s  %s" % (a_4, 'PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ANCHORS')

    print(chr(10) + '  G-NOGRADE (no grade conferred, nothing compiled, no act re-verdicted):')
    g1 = 'NO GRADE IS CONFERRED BY A SEAT' in bf
    g2 = 'NO ACT IS RE-VERDICTED' in bf
    g3 = 'NO CLASS IS DISCHARGED' in bf and 'THE CLAUSE HAS NOT MOVED' in bf
    faces = io.open(FACES, encoding='utf-8').read()
    blk = faces.split('## UPDATE — filed 2026-09-07 (b359)')[-1]
    g4 = 'NAMED-ONLY' in blk and 'NOTHING IS COMPILED' in blk
    g5 = 'NO NEW READING IS ADDED BY THIS BLOCK' in blk
    g6 = 'THE WAVE STAYS' in bf and 'NOTHING DEPOSITS' in bf
    gg = g1 and g2 and g3 and g4 and g5 and g6
    print('    no grade / no re-verdict / no class : %s / %s / %s' % (g1, g2, g3))
    print("    the faces block is NAMED-ONLY and compiles nothing : %s ; adds no new reading : %s" % (g4, g5))
    print('    wave parked, nothing deposits : %s  %s' % (g6, 'PASS' if gg else '### FAIL ###'))
    if not gg:
        fails.append('G-NOGRADE')

    print(chr(10) + "  G-LOCKCHAIN (LOCKED, on the audit's own exit code, and the block is a LOCK block):")
    z1 = "LOCKED ONLY AFTER THE AUDIT'S OWN EXIT CODE CAME BACK" in bf
    z2 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    z3 = reg_seal.LOCKMARK in reg and reg_seal.MARK not in reg
    z4 = 'LOCKED BEFORE ANY READ' in rgf
    z5 = reg_seal.selftest(False)
    gz = z1 and z2 and z3 and z4 and z5
    print('    the bank says it : %s ; the audit is satisfiable : %s ; a LOCK block : %s' % (z1, z2, z3))
    print('    locked BEFORE any read : %s ; the tool self-tests on both marks : %s  %s'
          % (z4, z5, 'PASS' if gz else '### FAIL ###'))
    if not gz:
        fails.append('G-LOCKCHAIN')

    print(chr(10) + "  SELF NEEDLES (each hint resolved to the bank's own line by the step-zero tool):")
    for lbl, hint in SELF_HINTS:
        try:
            n, line = AF.find(BANK, hint)
            needle_pull.pull(BANK, line)
            print('    PASS  %-52s line %d' % (lbl, n))
        except (AF.AnchorError, LookupError) as e:
            fails.append('SELF: ' + lbl)
            print('    ### FAIL  %-52s %s' % (lbl, str(e)[:70]))

    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    EXTRACT, eclock, ecands = latest_run('b359_extract_notes')
    print(chr(10) + '  OWNER NEEDLES (each at its emitting file, each in the extract):')
    print('    ### the extract is RESOLVED BY ITS OWN CLOCK, not named : %s of %s'
          % (os.path.basename(EXTRACT) if EXTRACT else 'none', [c[1] for c in ecands]))
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    nb2 = 0
    for label, tag, path, hint in EX.READS:
        try:
            _n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
            if not quote_norm.contains(extract, line.rstrip()[:200]):
                nb2 += 1
                print('    ### FAIL (NOT IN THE EXTRACT)  %s' % label)
        except (AF.AnchorError, LookupError):
            nb2 += 1
            print('    ### FAIL (NO ANCHOR)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+ ', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines : %d'
          % (len(EX.READS), nb2 == 0, cited))
    if nb2:
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s). ### **PRE-PUSH READING CARRIES.**' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'STILL RECONCILED TO THE SOURCE OF TRUTH' in rows[0] and anc)
    print('    row present once : %s ; true prefix of its blob : %s ; %s'
          % (len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTVERIFIED (the index):')
    IDX, iclock, icands = latest_run('b359_index_run')
    print('    ### the index run is RESOLVED BY ITS OWN CLOCK, not named : %s of %s'
          % (os.path.basename(IDX) if IDX else 'none', [c[1] for c in icands]))
    irun = io.open(IDX, encoding='utf-8').read()
    k_1 = 'READ BACK : ledger-currency-pass returns 1 row(s), 1 required  PASS' in irun
    k_2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
              ('the ledgers are verified', 'the deposit is correct',
               'the mirror proves the ledgers', 'the roster is repaired'))
    k_3 = '  ### PASS' in irun
    gkey = k_1 and k_2 and k_3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k_1, k_2, k_3, 'PASS' if gkey else '### FAIL ###'))
    if not gkey:
        fails.append('G-KEY')

    print(chr(10) + '  G-APPENDONLY (banked_index.py, FACES_LEDGER.md). ### **READ BEFORE THE PUSH.**')
    ap = True
    for repo, rel, cur in ((ROOT, 'tools/banked_index.py', idx), (PP, 'FACES_LEDGER.md', faces)):
        b = blob_of(repo, rel)
        one = True
        if b is not None:
            old, new = norm(b).split(chr(10)), norm(cur).split(chr(10))
            i = 0
            for ln in new:
                if i < len(old) and ln == old[i]:
                    i += 1
            one = (i == len(old))
        print('    %-28s every committed line still present, in order : %s' % (rel, one))
        ap = ap and one
    if not ap:
        fails.append('G-APPENDONLY')

    # ### ### **THIS ARM STRADDLES THE PUSH AND SAYS SO** (b352's rule). ### Its OWNER-INSTRUMENT and
    # ### TECHNE halves are SIDE-INVARIANT; ### **ITS PAPERS HALF IS NOT** -- before the push the two
    # ### files are DIRTY, after it the tree is CLEAN and the same fact lives in the HEAD commit's file
    # ### list. ### **THE FIRST WRITING OF THIS ARM DECLARED THE WHOLE THING SIDE-INVARIANT AND FAILED
    # ### ### POST-PUSH ON ITS OWN CORRECT STATE**, which is what b352 minted the rule for.
    print(chr(10) + '  G-NOEDIT (no owner instrument edited beyond the additive modes of R3).')
    print('    ### the owner and TECHNE halves are SIDE-INVARIANT; ### **THE PAPERS HALF STRADDLES.**')
    owner = ['tools/b316_instrument.py', 'tools/b317_smear.py', 'tools/b318_square.py',
             'tools/b319_stable.py', 'tools/b320_run.py', 'tools/b352_fit.py', 'tools/quote_norm.py',
             'tools/run_clock.py', 'tools/gate_text.py', 'tools/registration_gate.py',
             'tools/anchor_from_file.py', 'tools/needle_pull.py', 'tools/b327_faces_row.py',
             'tools/reg_seal.py', 'tools/ferry_scan.py', 'tools/mirror_roster.json',
             'tools/mirror_build.ps1', 'tools/mirror_verify.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    additive = []
    changed_add = []
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip()
              and 'BLOB_SENSITIVITY' not in x]
    ppexp = sorted(x.split()[-1] for x in ppstat)
    WANT = ['FACES_LEDGER.md']
    if ppexp:
        side, ppfiles = 'PRE-PUSH (the working tree)', ppexp
    else:
        head_msg = git(PP, 'log', '-1', '--format=%s').strip()
        ppfiles = sorted(x for x in git(PP, 'show', '--name-only', '--format=', 'HEAD').split() if x)
        side = 'POST-PUSH (the HEAD commit)'
        if not head_msg.startswith('b359'):
            ppfiles = ['### HEAD IS NOT THIS ACT S COMMIT: %s' % head_msg[:40]]
    gne = (not touched) and (not tcstat) and ppfiles == WANT
    print('    owner instruments modified : %s ; TECHNE dirty : %s' % (touched or 'none', tcstat or 'none'))
    print('    ### the two ADDITIVE tools under R3 : %s' % (changed_add or 'none'))
    print('    ### **THE SIDE THIS READING IS ON : %s**' % side)
    print('    the ONLY papers files this act touches : %s  %s'
          % (ppfiles, 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so BOTH ARE OWED):')
    hookp, mirrorp = HOOKS, d('b359_mirror.txt')
    gh = os.path.exists(hookp)
    if gh:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        print('    hook: 0 repos failing, all three byte-identical : %s' % h_ok)
        gh = h_ok
    else:
        print('    ### the hook record is NOT YET WRITTEN.')
    if os.path.exists(mirrorp):
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        print('    mirror: clean on all three clauses : %s' % m_ok)
        gh = gh and m_ok
    else:
        print('    ### the mirror record is NOT YET WRITTEN (it is written AFTER the push).')
        gh = False
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed)')

    print(chr(10) + '  G-ORDER (the lock verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (LOCK in reg)
    body, banked = reg_seal.split_body(reg)
    o1 = o1 and (reg_seal.digest(body) == LOCK == banked)
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and stampm.group(1) < F['run_clock'] < E['run_clock'] < C['run_clock']
    o4 = 'JOINTLY SATISFIABLE' in io.open(SATIS, encoding='utf-8').read()
    go = o1 and o2 and o3 and o4
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **LOCK %s < fetch %s < extract %s < pass %s** : %s'
          % (stampm.group(1) if stampm else '?', F['run_clock'], E['run_clock'], C['run_clock'], o3))
    print('    JOINTLY SATISFIABLE : %s  %s' % (o4, 'PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search('### bytes locked : ' + chr(40) + chr(92) + 'd+' + chr(41), reg).group(1)
    clc = re.search('clauses' + chr(92) + 's*:' + chr(92) + 's*' + chr(40) + chr(92) + 'd+' + chr(41), io.open(SATIS, encoding='utf-8').read()).group(1)
    dep = C['deposit']
    checks = [('the lock hash', LOCK in bank),
              ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
              ('%s bytes locked' % sm, ('%s bytes' % sm) in bank),
              ('%s clauses' % clc, ('%s clauses' % clc) in bank),
              ('row %s' % ROWNUM, ('row 208' in bank) and bool(rows)),
              ('the four clocks', all(x in bank for x in
                                      (stampm.group(1) if stampm else 'x', F['run_clock'],
                                       E['run_clock'], C['run_clock']))),
              ('the reads and the differing anchors',
               str(E['reads']) in bank and str(E['anchors_differing']) in bank),
              ('the claim counts', all(str(x) in bank for x in
                                       (C['n_current'], C['n_silent'], len(C['claims'])))),
              ('the pin counts', str(C['n_pins']) in bank and str(C['n_pins_current']) in bank),
              ('the deposit fields', all(str(dep[k]) in bank for k in
                                         ('version', 'doi', 'conceptdoi', 'publication_date', 'n_files'))),
              ('both fetch hashes', all(x['sha256'] in bank or x['sha256'][:16] in bank
                                        for x in F['targets'])),
              ('the fetch byte counts', all(str(x['bytes']) in bank for x in F['targets'])),
              ('every asserted sha', all(p['asserted'] in bank for p in C['pins'] if p.get('asserted')))]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (every relied-on run file resolved by its OWN CLOCK, never by name):')
    o1 = (EXTRACT is not None) and eclock == max(c[0] for c in ecands) and E['run_clock'] in \
        io.open(EXTRACT, encoding='utf-8').readline()
    o2 = (RUN is not None) and rclock == max(c[0] for c in rcands) and C['run_clock'] in \
        io.open(RUN, encoding='utf-8').readline()
    o3 = (IDX is not None) and iclock == max(c[0] for c in icands)
    FR, fclock, fcands = latest_run('b359_faces_row_run')
    o4 = (FR is not None) and fclock == max(c[0] for c in fcands)
    o5 = os.path.basename(EXTRACT) in bank and 'REFUSED TO WRITE THE BLOCK' in bf
    once = o1 and o2 and o3 and o4 and o5
    print('    the extract resolved to the newest of %d and carrying its JSON clock : %s' % (len(ecands), o1))
    print('    the pass run resolved to the newest of %d and carrying its JSON clock : %s' % (len(rcands), o2))
    print('    the index run resolved to the newest of %d : %s' % (len(icands), o3))
    print('    the faces run resolved to the newest of %d : %s (%s)'
          % (len(fcands), o4, os.path.basename(FR) if FR else 'none'))
    print('    the relied-on extract named in the bank and the refusal declared : %s  %s'
          % (o5, 'PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM:')
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE LEDGER CURRENCY PASS (b359).'
    nxt = '# ### THE LI ASYMPTOTICS, READ UNDER A CAP (b358).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if marker in idx and nxt in idx else ''
    fb2 = faces.split('## UPDATE — filed 2026-09-07 (b359)')[-1] if '(b359)' in faces else ''
    eb2 = ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''),
                      ('the index row', ib2), ('the faces block', fb2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b359_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''),
                      ('the index row', ib2), ('the faces block', fb2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_').replace('(', '').replace(')', '') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
