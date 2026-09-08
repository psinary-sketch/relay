# -*- coding: utf-8 -*-
"""b361_checks.py -- THE GATE SUITE FOR THE HELD ITEM, DECIDED.

### ### **THIS SUITE USES `gate_text.flat` AND DEFINES NO FLATTENER OF ITS OWN**, and every `G-NO*`-shaped
### arm reads STRIPPED CODE or a marked region rather than raw prose -- `b348`'s rule.
### ### **THE ARMS (locked registration section (D)):** ### `G-QUOTE`, `G-BRANCH`, `G-DEFINITION`,
### `G-SCOPE`, `G-ROW`, `G-KEY` with `G-NOTDECIDED`, `G-NOEDIT`, `G-ORDER`, `G-NUMBERS`, `G-TOOLNUM`,
### `G-ONCE`, `G-NOCOMPUTE`, the struck-clause and stem sweeps, `G-SHARED`, the hedge audit, the must-fail
### fixtures. ### Re-run after the push.
### ### **THE SIDES, DECLARED BY `b352`'s RULE:** ### `G-NOEDIT`'s working-tree half and `G-ROW`'s ancestry
### reading are read BEFORE THE PUSH; `G-HOOK` and `G-MIRROR` AFTER THE PUSH; `G-ORDER` SIDE-INVARIANT.
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
import run_clock         # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b361_the_held_item.txt')
REG = d('b361_registration_2026-09-07.txt')
FERRY = d('b361_ferry_2026-09-07.txt')
SRC = d('b358_source_lagarias0404394.txt')
B358 = d('b358_the_li_asymptotics.txt')
CORR, IDX = d('b361_corr_run.txt'), d('b361_index_run.txt')
SCAN, TERMSCAN, GATE = d('b361_ferry_scan.txt'), d('b361_reg_termscan.txt'), d('b361_reg_gate.txt')
CENSUS, FCEN = d('b361_census_stepzero.txt'), d('b361_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b361_regspec_run.txt'), d('audit_b361_reg_satisfiable.txt')
PINS = d('b361_pins_stepzero.txt')
SEAL = '5a4d39eb7c5eeb8f5082eb2d0f4232a17ad1e8acb401f8fdb95b3527ea15f2f7'
ROWNUM = '210'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('R', 'b361_read.json'), ('E', 'b361_reads.json'), ('F', 'b361_faces_row.json'))}

NEW_THIS_ACT = {'tools/b361_regspec.py', 'tools/b361_extract.py', 'tools/b361_read.py',
                'tools/b361_faces_row.py', 'tools/b361_correspondence.py', 'tools/b361_index_append.py',
                'tools/b361_checks.py'}

TOOLNUM = [
    ('the branch, the route and the one square of zero', 'tools/b361_read.py'),
    ('the 35 reads and the 16 differing anchors', 'tools/b361_extract.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the U1 update block', 'tools/b361_faces_row.py'),
    ('the ledger writer it imports', 'tools/b327_faces_row.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 210', 'tools/b361_correspondence.py'),
    ('the key', 'tools/b361_index_append.py'),
    ('49 clauses', 'tools/b361_regspec.py'),
    ('14057 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
]

OWNED = [BANK, REG, FERRY, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, PINS, GATE, TERMSCAN,
         d('b361_satisfiable.json'), d(_J['E']['run_file']), d(_J['R']['run_file']),
         d(_J['F']['run_file']),
         t('b361_regspec.py'), t('b361_extract.py'), t('b361_read.py'), t('b361_faces_row.py'),
         t('b361_correspondence.py'), t('b361_index_append.py')]

CARRIERS = [
    (t('b361_checks.py'), 'its own fixtures'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (d(_J['E']['run_file']), "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ('the order -- leg 1', FERRY, 'LEG 1 (b361) \u2014 THE HELD ITEM, QUOTED THEN BRANCHED.'),
    ('the order -- the branch, fixed before the quotation is seen', FERRY,
     '(b) BRANCH, fixed here before the quotation is seen: if the'),
    ('the order -- the circularity clause over both branches', FERRY,
     'branch the circularity finding stands untouched: the tail'),
    ('the order -- the ledger condition', FERRY,
     'grading table gives it, and the Li row updated through the'),
    ('b358 -- the item', B358, 'H-NGEK` DESERVES ITS OWN SENTENCE.'),
    ('b358 -- the cap clause', B358,
     'THE RECORD ALREADY HOLDS. ### DETERMINED IS NOT COMPUTED**, the cap forbids this act'),
    ('b358 -- the grade class the item sits in', B358, 'THE FIVE THAT ARE `UNDECIDABLE-FROM-THE-RECORD`'),
    ('b358 -- H-CUSP, inherited and not decided', B358,
     '`H-CUSP` (`\u03c0` cuspidal on `GL(N)`): the corpus'),
    ("the draft -- its parking claim, quoted as a claim", d('b360_closing.txt'),
     'the record already holds, ### **AND IT IS NOT AN INSTRUMENT RUN** -- no frame'),
    ('source -- the definition of the constant', SRC, '|\u03baj(\u03c0)|2, (5.3)'),
    ('source -- the archimedean factor', SRC, '\u0393 R(s +\u03baj(\u03c0)), (2.2)'),
    ('source -- the conductor of the trivial representation, stated', SRC, 'using Q(\u03c0triv) = 1.'),
    ("source -- Theorem 5.1's own hypothesis", SRC,
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('source -- the ABSOLUTE implied constant', SRC,
     'and the implied constant in the O-notation is absolute.'),
    ("source -- the introduction's version, for all n >= 1", SRC, 'that for all n \u2265 1,'),
    ('source -- and ITS constant depends on pi', SRC,
     'and the implied constant in the O(1) term depends on \u03c0. Here'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK,
     "### ### ### **DECIDED. ### `K(pi_triv) = 0`, SO THE INDEX CONDITION IS VACUOUS FOR THE CORPUS'S OBJECT.**"),
    ('### the value is identified, not quoted', BANK,
     '### ### ### **AND THE VALUE IS NOT QUOTED FROM THE SOURCE. ### IT IS AN IDENTIFICATION OF TWO OF THE'),
    ('### the circularity finding stands', BANK,
     "### ### CIRCULARITY FINDING STANDS EXACTLY WHERE `b358` LEFT IT**, which is the order's own clause over"),
    ('### the rule that bound the seat', BANK, '### ### **AND THE THIRD RULE IS THE ONE THAT BOUND.**'),
    ('### the branch taken', BANK, '### ### ### **BRANCH A -- DECIDE.**'),
    ("### the draft's claim tested rather than inherited", BANK,
     "### ### ### **AND THE DRAFT'S CLAIM WAS TESTED RATHER THAN INHERITED.**"),
    ('### bar 2 met', BANK, '### ### **BAR 2 -- THE DEFINITION BAR, MET.**'),
    ('### H-CUSP inherited and not decided', BANK,
     '### ### **(i) IT INHERITS `H-CUSP` AND DOES NOT DECIDE IT.**'),
    ('### the two statements, side by side', BANK,
     '### ### ### **THE SOURCE ALWAYS HELD TWO STATEMENTS, AND THE INDEX CONDITION BELONGS TO ONLY ONE OF THEM.**'),
    ('### the reader ran five times, declared', BANK,
     '### ### **(E1) THE READER RAN FIVE TIMES AND ALL FIVE RUN FILES ARE ON DISK.**'),
    ('### the shell patch that failed, declared', BANK,
     '### ### **(E2) A SHELL PATCH FAILED SILENTLY AND THE EDIT WAS MADE WITH A FILE EDITOR INSTEAD.**'),
    ("### the navigator's second clause refuted by a quotation", BANK,
     "###   ### **SECOND CLAUSE: REFUTED, AND REFUTED BY A QUOTATION**, which is what the order asked for."),
    ('### what a vacuous condition means', BANK, '### ### **IT MEANS A CONDITION WAS VACUOUS.**'),
    ('### the shadow', BANK, '### ### **EXPECTED: A SMALL BOOKKEEPING DECISION.**'),
]

MUST_FAIL = [
    ('the bank never says the tail is closed', BANK, '### THE TAIL IS CLOSED.'),
    ('the bank never says the circularity is removed', BANK, '### THE CIRCULARITY IS REMOVED.'),
    ('the bank never says a grade is conferred', BANK, '### A GRADE IS CONFERRED HERE.'),
    ('the bank never says the value is recalled', BANK, '### THE VALUE IS RECALLED.'),
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
    print('b361 -- GATE SUITE (THE HELD ITEM, DECIDED)')
    print('=' * 100)
    extract = io.open(d(_J['E']['run_file']), encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE RELIED-ON EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    R, E, F = _J['R'], _J['E'], _J['F']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    faces = io.open(FACES, encoding='utf-8').read()
    read = io.open(d(R['run_file']), encoding='utf-8', errors='replace').read()

    print(chr(10) + '  G-QUOTE (the extract located every read on its first run; no quotation typed from memory):')
    q1 = E['without_anchor'] == 0 and E['reads'] > 0
    q2 = '### WITHOUT AN ANCHOR : 0' in extract
    q3 = 'RECOLLECTION IS NEVER A SOURCE FOR A VALUE' in gate_text.flat(reg)
    gq = q1 and q2 and q3
    print('    %d of %d reads located, 0 without an anchor : %s ; the run file says so : %s'
          % (E['reads'] - E['without_anchor'], E['reads'], q1, q2))
    print('    and the LOCKED registration fixed the rule against recollection : %s' % q3)
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-QUOTE')

    print(chr(10) + '  G-BRANCH (the branch decided on the quoted text; the other shown unreachable):')
    b1 = R['branch'] == 'A' and R['verdict'] == 'DECIDED'
    b2 = 'BRANCH TAKEN : A -- DECIDE' in read
    b3 = 'AND THE OTHER BRANCH IS SHOWN UNREACHABLE RATHER THAN LEFT UNCLAIMED' in read
    b4 = "AND THE DRAFT'S CLAIM IS TESTED RATHER THAN INHERITED" in read
    gb = b1 and b2 and b3 and b4
    print('    branch %s, verdict %s : %s ; the run says so : %s' % (R['branch'], R['verdict'], b1, b2))
    print('    the other branch shown unreachable : %s ; the draft tested not inherited : %s' % (b3, b4))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BRANCH')

    print(chr(10) + '  G-DEFINITION (bar 2: the definition located at content; the VALUE not quoted from the source):')
    f1 = R['definition_located'] is True
    f2 = R['value_stated_in_source'] is False and R['stated_strings'] == []
    f3 = 'THE VALUE IS NOT QUOTED FROM THE SOURCE' in read
    f4 = 'THE DEFINITION IS LOCATED AT CONTENT AND QUOTED' in read
    f5 = R['K'] == 0 and R['kappa'] == 0
    gf = f1 and f2 and f3 and f4 and f5
    print('    the definition located at content : %s ; the value NOT stated in the source : %s' % (f1, f2))
    print('    the act says so : %s / %s ; the value : kappa=%s K=%s : %s'
          % (f3, f4, R['kappa'], R['K'], f5))
    print('    %s' % ('PASS' if gf else '### FAIL ###'))
    if not gf:
        fails.append('G-DEFINITION')

    print(chr(10) + '  G-SCOPE (the tail untouched; the circularity untouched; H-CUSP inherited; no grade conferred):')
    s1 = 'IT DECIDES AN INDEX CONDITION AND NOTHING ELSE' in read
    s2 = 'THE CIRCULARITY FINDING STANDS EXACTLY WHERE' in read
    # ### **THE NEEDLE IS THE READ FILE'S OWN WORDS.** ### Its first version typed `IT INHERITS` where the
    # ### file says `THE ROUTE INHERITS`, and fired on correct work -- the wrapping species' cousin, a
    # ### mis-typed noun. ### **CORRECTED TO THE FILE, NEVER SOFTENED.**
    s3 = R['inherits'] == 'H-CUSP' and 'INHERITS `H-CUSP` AND DOES NOT DECIDE IT' in read
    s4 = R['grade_conferred_by_seat'] is False and R['row_grade'].startswith('NAMED-ONLY')
    s5 = 'A DECIDED INDEX CONDITION IS NOT A CLOSED TAIL' in bf
    gs = s1 and s2 and s3 and s4 and s5
    print('    an index condition and nothing else : %s ; the circularity stands : %s' % (s1, s2))
    print('    H-CUSP inherited : %s ; no grade conferred, row grade %r : %s' % (s3, R['row_grade'], s4))
    print('    and the bank says a decided condition is not a closed tail : %s' % s5)
    print('    %s' % ('PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SCOPE')

    print(chr(10) + '  G-LEDGER (the row moved, and it moved ONLY because the decision moved it; through the writer)'
          ' ### the ancestry reading READ BEFORE THE PUSH:')
    fb = blob_of(PP, 'FACES_LEDGER.md')
    l1 = R['row_moves'] is True and R['row'] == 'U1'
    l2 = F['status'] in ('WRITTEN', 'DUPLICATE') and F['form'].startswith('UPDATE BLOCK')
    l3 = faces.count('(b361): row U1, the uniformity obstruction') == 1
    l4 = (fb is not None) and norm(faces).startswith(norm(fb).rstrip(chr(10)))
    l5 = F['grade'].startswith('NAMED-ONLY')
    gl = l1 and l2 and l3 and l4 and l5
    print('    the decision moves the row : %s ; written through the writer as an update block : %s' % (l1, l2))
    print('    the block appears once : %s ; the ledger a true prefix of its blob : %s' % (l3, l4))
    print('    the grade is unchanged : %s (%s)' % (l5, F['grade']))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason) ### READ BEFORE THE PUSH:' % ROWNUM)
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0]
            and 'AN INDEX CONDITION DECIDED IS NOT A BOUND PROVED' in rows[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rows) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTDECIDED:')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : index-condition-decided returns 1 row(s)' in irun
    k2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
             ('the tail is closed', 'the circularity is removed',
              'the value is quoted from the source', 'H-CUSP is decided'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the run passed : %s'
          % (k1, k2, k3))
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY/G-NOTDECIDED')

    print(chr(10) + "  G-NOEDIT (no owner instrument; only this act's papers path touched) ### the working-tree "
          "half READ BEFORE THE PUSH; the blob half SIDE-INVARIANT:")
    owner = ['tools/e16/b264_eps_decay.py', 'tools/noise_floor.py', 'tools/reg_seal.py',
             'tools/registration_gate.py', 'tools/gate_text.py', 'tools/run_clock.py',
             'tools/anchor_from_file.py', 'tools/quote_norm.py', 'tools/ferry_scan.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() != 'FACES_LEDGER.md']
    hand = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'HANDOFF.md').strip()
    dep = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'day1/A_Place_to_Stand.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    tech = not git(TC, 'status', '--porcelain').strip() if os.path.isdir(TC) else True
    gne = not touched and not ppbad and hand and dep and fnd and tech
    print('    owner instruments modified : %s ; papers paths beyond FACES_LEDGER.md : %s'
          % (touched or 'none', ppbad or 'none'))
    print('    HANDOFF clean : %s ; the deposited monograph clean : %s ; FINDINGS clean : %s ; TECHNE clean : %s'
          % (hand, dep, fnd, tech))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the lock verifies; EVERY relied-on run is AFTER the lock; nothing before it) '
          '### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (E, R, F))
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY READ OR EVALUATION' in gate_text.flat(reg)
    go = o1 and o2 and o3 and o4 and o5
    print('    the lock recomputes : %s ; it carries its clock (%s) : %s'
          % (o1, stampm.group(1) if stampm else 'none', o2))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('        lock    %s' % (stampm.group(1) if stampm else '?'))
    print('        extract %s   read %s   ledger %s' % (E['run_clock'], R['run_clock'], F['run_clock']))
    print('    the audit reads JOINTLY SATISFIABLE : %s ; the face says LOCKED BEFORE ANY READ : %s' % (o4, o5))
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (the papers repo moves, so both are OWED) ### READ AFTER THE PUSH:')
    hookp, mirrorp = d('b361_hooks.txt'), d('b361_mirror.txt')
    gh = os.path.exists(hookp) and os.path.exists(mirrorp)
    if gh:
        ht = io.open(hookp, encoding='utf-8', errors='replace').read()
        mt = io.open(mirrorp, encoding='utf-8', errors='replace').read()
        h_ok = '### REPOS FAILING : 0' in ht and 'BYTE-IDENTICAL TO THE TRACKED SOURCE : True' in ht
        m_ok = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in mt
        # ### **THE ROSTER SLOT b360 ADDED, EXERCISED:** ### this is the first faces update to reach the
        # ### archive at all, and the arm checks the ledger is IN the rebuilt archive rather than assuming it.
        r_ok = 'FACES_LEDGER.md IS IN THE REBUILT ARCHIVE : True' in mt
        gh = h_ok and m_ok and r_ok
        print('    hook: 0 repos failing, all three byte-identical : %s ; mirror clean on all three : %s'
              % (h_ok, m_ok))
        print('    ### **THE ROSTER SLOT EXERCISED: the faces ledger is IN the rebuilt archive** : %s' % r_ok)
    else:
        print('    ### the hook and the mirror records are NOT YET WRITTEN (they are written at the push).')
    if not gh:
        fails.append('G-HOOK/G-MIRROR (owed, not yet recorded)')

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    cl = re.search(r'clauses\s*:\s*(\d+)', sat)
    sm = re.search(r'### bytes locked : (\d+)', reg)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [
        ('reads %d' % E['reads'], ('`%d`' % E['reads']) in bank),
        ('without an anchor %d' % E['without_anchor'], ('`%d`' % E['without_anchor']) in bank),
        ('anchors differing %d' % E['anchors_differing'], ('`%d`' % E['anchors_differing']) in bank),
        ('the source rendering sha256', E['source_sha256'] in bank),
        ('the source rendering bytes %d' % E['source_bytes'], str(E['source_bytes']) in bank),
        ("b358's pin on the PDF", '86f3d3c4' in bank and '423379' in bank),
        ('row %s' % rn, rn == ROWNUM and ('`%s`' % rn) in bank),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('%s bytes locked' % (sm.group(1) if sm else '?'), ('%s bytes' % (sm.group(1) if sm else 'x')) in bank),
        ('%s clauses' % (cl.group(1) if cl else '?'), ('%s clauses' % (cl.group(1) if cl else 'x')) in bank),
        ('the relied-on extract run file', E['run_file'] in bank),
        ('the relied-on read run file', R['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the relied-on run files resolved by their own recorded clocks, never by name):')
    once = True
    for lbl, jf in (('extract', E), ('read', R), ('ledger', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-8s %-26s clock on disk %s == the JSON's %s : %s" % (lbl, jf['run_file'], st, jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    print(chr(10) + '  G-NOCOMPUTE (nothing computed but one square of zero, RE-MEASURED ON STRIPPED CODE):')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = []
    for p in [t(x) for x in ('b361_regspec.py', 'b361_extract.py', 'b361_read.py', 'b361_faces_row.py',
                             'b361_correspondence.py', 'b361_index_append.py', 'b361_checks.py')]:
        src2 = strip_prose(p)
        for b in banned:
            if b in src2:
                hits.append((os.path.basename(p), b))
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in ('b361_read.py', 'b361_extract.py', 'b361_faces_row.py'))]
    gnc = not hits and not imports
    print("    numerical calls in this act's STRIPPED sources : %d %s" % (len(hits), hits or ''))
    print('    numerical libraries imported : %s' % (imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
            for hh in (ch + sh)[:6]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        if not os.path.exists(p):
            continue
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-44s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    marker = '# ### THE HELD ITEM, QUOTED THEN BRANCHED (b361).'
    nxt = '# ### THE UNIFORMITY ARC, b349-b359 -- THE FOLD (b360).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    blk = faces[faces.index('(b361): row U1'):] if '(b361): row U1' in faces else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ledger block, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', blk),
                      ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the ledger block and the index row):')
    tmpdir = tempfile.mkdtemp(prefix='b361_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the ledger block', blk),
                      ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
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
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
