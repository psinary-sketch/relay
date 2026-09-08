# -*- coding: utf-8 -*-
"""b372_checks.py -- THE GATE SUITE FOR THE EOL PIN, THE README FIGURES AND THE FIRST BATCH.

### ### **`G-ATTR` AND `G-FRESH` RE-MEASURE THE FILESYSTEM AND ASK GIT AGAIN**, rather than trusting the
### attribute tool's own JSON -- `b371`'s destructive incident was caught only because an arm re-read the
### filesystem instead of believing the mover.
### ### **`G-NOROWREPAIR` COMPARES EVERY FLAGGED ROW AGAINST ITS COMMITTED BLOB.** ### The cap of this
### act is that no row moved, and a cap nobody measures is a sentence.
### ### **THE SIDES, BY `b352`:** ### `G-NOEDIT`'s, `G-TRAIL`'s and `G-ROW`'s working-tree readings are
### BEFORE THE PUSH; the hook and the mirror AFTER; `G-ORDER` is SIDE-INVARIANT.
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
import b317_checks as K7   # noqa: E402
import gate_text          # noqa: E402
import run_clock          # noqa: E402
import gate_needle as GN   # noqa: E402
import b366_sweep as SW    # noqa: E402
import b303_pins           # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KER = os.path.join('D:', os.sep, 'SIDE-effects')
SK = os.path.join('D:', os.sep, 'SIDE-kernel')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
GUARD = '.githooks/pre-push'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b372_the_first_batch.txt')
REG = d('b372_registration_2026-09-08.txt')
FERRY = d('b372_ferry_2026-09-08.txt')
CORR, IDX = d('b372_corr_run.txt'), d('b372_index_run.txt')
SCAN, TERMSCAN, GATE = d('b372_ferry_scan.txt'), d('b372_reg_termscan.txt'), d('b372_reg_gate.txt')
CENSUS0, FCEN = d('b372_census_stepzero.txt'), d('b372_faces_census_stepzero.txt')
REGSPEC, SATIS = d('b372_regspec_run.txt'), d('audit_b372_reg_satisfiable.txt')
PINS0 = d('b372_pins_stepzero.txt')
SEAL = 'a4af7650995b760afb79b0cc001713d8192f6723f9ea497a2f3008548370e0c0'
ROWNUM = '221'
TRAIL_MARK = '<!-- b372 the eol pin, the readme figures, the first batch of row checks -->'

_J = {k: json.load(io.open(d(v), encoding='utf-8'))
      for k, v in (('E', 'b372_reads.json'), ('A', 'b372_eol.json'),
                   ('R', 'b372_readme.json'), ('B', 'b372_batch.json'),
                   ('Q', 'b372_desk.json'), ('F', 'b372_filing.json'))}

LICENSED = set()
NEW_THIS_ACT = {'tools/b372_regspec.py', 'tools/b372_extract.py', 'tools/b372_reg_gate.py',
                'tools/b372_eol.py', 'tools/b372_readme.py', 'tools/b372_batch.py',
                'tools/b372_desk.py', 'tools/b372_filing.py', 'tools/b372_bank.py',
                'tools/b372_correspondence.py', 'tools/b372_index_append.py',
                'tools/b372_checks.py'}

TOOLNUM = [
    ('the attribute, asked of git, and the fresh checkout', 'tools/b372_eol.py'),
    ('what each figure counts, at the ref that introduced it', 'tools/b372_readme.py'),
    ('the twelve rows, opened at pin or head', 'tools/b372_batch.py'),
    ('(R7), with every closure naming a killing file', 'tools/b372_desk.py'),
    ('the closures and the routing filed', 'tools/b372_filing.py'),
    ('every figure in the bank, read from the JSONs', 'tools/b372_bank.py'),
    ('the reads', 'tools/b372_extract.py'),
    ('the three-arm registration gate', 'tools/b372_reg_gate.py'),
    ("(R2)'s detector, turned on this act", 'tools/b366_sweep.py'),
    ('the anchor built by reading its line', 'tools/anchor_from_file.py'),
    ('the needle helper', 'tools/gate_needle.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ('row 221', 'tools/b372_correspondence.py'),
    ('the key', 'tools/b372_index_append.py'),
    ('the clause spec', 'tools/b372_regspec.py'),
    ('22273 bytes locked, and the lock clock', 'tools/reg_seal.py'),
    ('the guard exercised across the roster', 'tools/b304_hooks.py'),
    ('the roster itself, imported and not typed', 'tools/b303_pins.py'),
    ("the pinless rows this act did not pin", 'tools/b371_inventory.py'),
]

OWNER_NEEDLES = [
    ('the order -- the act', FERRY, 'ACT b372 - THE README, THE EOL PIN, AND THE FIRST BATCH.'),
    ('the order -- (R8)', FERRY, 'strikeable: A ROW WITHOUT A PIN IS NOT CHECKABLE THE WAY THE'),
    ('the order -- checked at head', FERRY, "kernel's live head, and the head is recorded in the checking"),
    ('the order -- a separate ruling', FERRY, 'separate ruling, priced and not attempted.'),
    ('the order -- component 1', FERRY, 'COMPONENT 1 - THE EOL PIN, first because it protects the rest:'),
    ('the order -- the verification named', FERRY,
     "tracked file's working bytes equal its blob's after a fresh"),
    ('the order -- say so rather than writing twice', FERRY,
     'checkout. Where a repository already carries it, say so rather'),
    ('the order -- component 2', FERRY, 'COMPONENT 2 - THE README, WHICH TRAVELS WITH A CLONE: the'),
    ('the order -- the three-clause description', FERRY,
     "exclusion kernel's README states a headline figure, a breakdown"),
    ('the order -- removed rather than restated', FERRY,
     'the bank, and a figure REMOVED rather than restated unless the'),
    ('the order -- component 3', FERRY, 'COMPONENT 3 - THE FIRST BATCH under (R6) and (R8): the twelve'),
    ('the order -- no repairs', FERRY, 'rows is reported and routed.'),
    ("the order -- the navigator's expectations", FERRY,
     "navigator's expectations: (F1) the README's three figures count"),
    ("the exclusion kernel's README -- its ONE count line", os.path.join(KER, 'README.md'),
     '3 theorems, 3 sorrys (each at a marked analytic boundary), 0 axioms.'),
    ("the papers repository's attribute, and why", os.path.join(PP, '.gitattributes'),
     '# eol=lf makes checkout match storage. Do not remove without'),
]

SELF_NEEDLES = [
    ('the bank states the attribute first', BANK,
     'THE TWO THAT FAILED WERE EXACTLY THE TWO WITHOUT'),
    ('### one quantity at three refs', BANK,
     'QUANTITY AT THREE DIFFERENT REFS**, and each was exact when it was written.'),
    ('### none names its ref', BANK,
     'AND NONE OF THE THREE NAMES THE REF IT HOLDS AT'),
    ('### the comparison that argues (R8)', BANK,
     'AND ONE COMPARISON INSIDE THIS ACT IS THE WHOLE ARGUMENT FOR'),
    ('### rows repaired zero, pins added zero', BANK, 'ROWS REPAIRED : `0`. ### PINS ADDED : `0`.'),
    ('### one polarity cannot tell a fix from the weather', BANK,
     'A ONE-POLARITY CHECK OF A FIX CANNOT DISTINGUISH THE FIX FROM THE'),
    ('### the attribute fixes the next checkout, not this disk', BANK,
     'WHAT IS FIXED IS WHAT THE NEXT CHECKOUT PRODUCES'),
    ('### the object identified by the description', BANK,
     'THE OBJECT IS IDENTIFIED BY THE DESCRIPTION, BECAUSE A DESCRIPTION IS CHECKABLE AGAINST A'),
    ('### neither kernel ships a printed profile', BANK,
     'NEITHER SHIPS A PRINTED AXIOM PROFILE.'),
    ('### a pattern that knows one shape, the other way', BANK,
     'ONE SHAPE ALSO MATCHES THINGS THAT ARE NOT THAT SHAPE.'),
    ("### the ledger's own lacunae", BANK, 'THE LEDGER`S OWN LACUNAE, FILED AND NOT INVENTED'),
    ('### why a pin written at the head is worthless', BANK,
     'WRITTEN AT THE HEAD PINS A ROW TO A STATE IN WHICH THE ROW IS FALSE.'),
    ('### a figure that was exact is not a figure that is wrong', BANK,
     'A FIGURE THAT WAS EXACT IS NOT A FIGURE THAT IS WRONG'),
    ('### a pin is a date that survives', BANK, 'NEW -- `A PIN IS A DATE THAT SURVIVES`'),
    ('### (F1) splits', BANK, 'THE FIRST HALF IS REFUTED, THE SECOND CONFIRMED.'),
    ('### (E1) is not an expectation', BANK,
     'AND IT WAS DECIDED BEFORE THE LOCK AND SO IS `NOT AN EXPECTATION`'),
    ('### the heading predicate that reported the opposite', BANK,
     'THIRD ONE REPORTED EVERY TERMINAL AS ABSENT, CONFIDENTLY'),
    ('### the destructive incident named', BANK,
     'ACT A MOVER THAT THOUGHT IT WAS BEING CAREFUL DESTROYED UNCOMMITTED WORK IN FOUR'),
]

MUST_FAIL = [
    ('the bank never says a row was repaired', BANK, '### A ROW WAS REPAIRED.'),
    ('the bank never says a build was run', BANK, '### A BUILD WAS RUN.'),
    ('the bank never says a working file was deleted', BANK,
     '### A WORKING FILE WAS DELETED TO FORCE A CHECKOUT.'),
    ('the bank never says a repository was renormalised', BANK,
     '### A REPOSITORY WAS RENORMALISED.'),
    ('the bank never says a pinless row was checked at its pin', BANK,
     '### A PINLESS ROW WAS CHECKED AT ITS PIN.'),
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
    print('b372 -- GATE SUITE (THE EOL PIN, THE README FIGURES, THE FIRST BATCH)')
    print('=' * 100)
    E, A, R, B, Q, F = (_J['E'], _J['A'], _J['R'], _J['B'], _J['Q'], _J['F'])
    extract = io.open(d(E['run_file']), encoding='utf-8', errors='replace').read()
    refused, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES:')
    for lbl, path, hint in OWNER_NEEDLES:
        try:
            inx, _n, line = GN.present(extract, path, hint)
            trunc = False
            if not inx and len(line.rstrip()) > 230:
                inx = line.rstrip()[:230] in extract
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
    print(chr(10) + '  MUST-FAIL FIXTURES:')
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
    REPOS = dict(b303_pins.REPOS)

    # ---------------------------------------------------------------- COMPONENT 1
    print(chr(10) + '  G-ATTR / G-FRESH (BAR 1) ### RE-MEASURED HERE, NOT TAKEN FROM THE JSON:')
    attr, fresh = {}, {}
    tmp = tempfile.mkdtemp(prefix='b372chk_')
    for nm, rp in REPOS.items():
        out = git(rp, 'check-attr', 'text', 'eol', '--', GUARD)
        vals = {}
        for ln in out.split(chr(10)):
            if ': ' in ln:
                parts = ln.rsplit(': ', 2)
                if len(parts) == 3:
                    vals[parts[1]] = parts[2].strip()
        attr[nm] = vals.get('eol', 'unspecified')
        outdir = os.path.join(tmp, nm)
        os.makedirs(outdir, exist_ok=True)
        pref = outdir.replace(os.sep, '/').rstrip('/') + '/'
        subprocess.run(['git', '-C', rp, 'checkout-index', '-f', '--prefix=' + pref, '--', GUARD],
                       capture_output=True)
        dest = os.path.join(outdir, GUARD.replace('/', os.sep))
        got = open(dest, 'rb').read() if os.path.exists(dest) else None
        blob = subprocess.run(['git', '-C', rp, 'show', 'HEAD:' + GUARD],
                              capture_output=True).stdout
        fresh[nm] = (got is not None and got == blob)
        print('    %-22s eol=%-12s fresh checkout == blob : %s' % (nm, attr[nm], fresh[nm]))
    ga1 = all(v == 'lf' for v in attr.values()) and all(fresh.values())
    ga2 = A['fixture_ok'] is True and A['fixture']['with the attribute']['equal'] is True \
        and A['fixture']['without it']['equal'] is False
    tracked_attr = all(bool(git(rp, 'ls-files', '--', '.gitattributes').strip())
                       for rp in REPOS.values())
    ga = ga1 and ga2 and tracked_attr
    print('    ### **BOTH POLARITIES HELD IN THE FIXTURE** : %s' % ga2)
    print('    ### **AND `.gitattributes` IS TRACKED IN EVERY ROSTERED REPOSITORY** : %s' % tracked_attr)
    print('    %s' % ('PASS' if ga else '### FAIL ###'))
    if not ga:
        fails.append('G-ATTR/G-FRESH')

    print(chr(10) + '  G-NOWRITETWICE / G-NORENORM / G-NODELETE:')
    wrote = A['wrote']
    w1 = all(v['action'] != 'WRITTEN' for k, v in wrote.items()
             if A['state'][k]['governed'])
    kept = A['state']['relay']['lines']
    ga_relay = io.open(os.path.join(ROOT, '.gitattributes'), encoding='utf-8').read()
    w2 = all(l in ga_relay.split(chr(10)) for l in kept)
    # ### **NO TRACKED FILE'S CONTENT WAS REWRITTEN BY THE ATTRIBUTE**: only the declared paths differ.
    ALLOWED = {'relay': {'.gitattributes', 'tools/banked_index.py'},
               'SIDE-global-section': {'README.md', 'CORRESPONDENCE.md'},
               'PLACE-papers': {'OPEN_TRAILS.md'},
               'SIDE-effects': {'.gitattributes'}}
    renorm = {}
    for nm, rp in REPOS.items():
        ch = set(x.strip() for x in git(rp, 'diff', '--name-only', 'HEAD').split(chr(10)) if x.strip())
        ch |= set(x[3:].strip() for x in git(rp, 'status', '--porcelain').split(chr(10))
                  if x.strip() and x[:2] in ('A ', 'M ', 'AM', 'MM'))
        renorm[nm] = sorted(x for x in ch if x not in ALLOWED[nm]
                            and 'b372' not in x and 'BLOB_SENSITIVITY' not in x)
    w3 = all(not v for v in renorm.values())
    src = ' '.join(strip_prose(t(x)) for x in ('b372_eol.py', 'b372_readme.py', 'b372_batch.py'))
    w4 = ('renormalize' not in src and 'os.remove' not in src and 'reset' not in src
          and 'checkout -b' not in src)
    gw = w1 and w2 and w3 and w4
    print('    repositories already carrying it were NOT written to : %s' % w1)
    print("    ### **relay's pre-existing line survives verbatim** : %s %s" % (w2, kept))
    print('    tracked paths changed beyond the declared set : %s' % renorm)
    print('    ### **NO DELETE, NO RESET, NO BRANCH CREATION IN THE STRIPPED SOURCES** : %s' % w4)
    print('    %s' % ('PASS' if gw else '### FAIL ###'))
    if not gw:
        fails.append('G-NOWRITETWICE/G-NORENORM/G-NODELETE')

    # ---------------------------------------------------------------- COMPONENT 2
    print(chr(10) + '  G-OBJECT / G-LABEL (the discrepancy reported, the object identified):')
    o1 = len(R['fitting']) == 1 and 'SIDE-global-section' in R['fitting'][0]
    o2 = not any(v['fits'] for k, v in R['candidates'].items() if 'SIDE-effects' in k)
    o3 = not git(KER, 'diff', '--name-only', 'HEAD', '--', 'README.md').strip()
    o4 = 'THE ORDER NAMED ONE OBJECT AND DESCRIBED ANOTHER' in bf
    go = o1 and o2 and o3 and o4
    print('    exactly one candidate fits all three clauses : %s' % o1)
    print("    ### **AND THE LABELLED ONE DOES NOT** : %s ; its README is untouched : %s" % (o2, o3))
    print('    the bank reports the discrepancy : %s' % o4)
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-OBJECT/G-LABEL')

    print(chr(10) + '  G-README / G-REMOVED / G-PRESERVED / G-SCOPE / G-ROUTED (BAR 3, BAR 4):')
    rd = io.open(os.path.join(SIDE, 'README.md'), encoding='utf-8').read()
    removed = [x['text'] for x in R['originals']]
    p1 = all(GN.norm(x) in GN.norm(bank) for x in removed)
    p2 = R['verify']['removed_still_present'] == []
    p3 = R['verify']['census_preserved'] and R['verify']['linecount_unchanged']
    p4 = 'AXIOM_PRINTS.txt' in rd and '**212 terminals**' not in rd and '(250/250)' not in rd
    census = None
    for c in R['candidates'].values():
        if c['breakdown']:
            census = c['breakdown']['text']
    p5 = census is not None and census in rd
    p6 = R['table'][0]['total'] == R['table'][0]['prints']
    p7 = 'ROUTED' in bank and 'A CLAIM AND NOT A NUMBER' in bf
    gr = p1 and p2 and p3 and p4 and p5 and p6 and p7
    print('    every original appears VERBATIM in the bank before the edit : %s' % p1)
    print('    the removed figures are gone from the README : %s / %s' % (p2, p4))
    print('    ### **THE CENSUS SURVIVES VERBATIM AND THE LINE COUNT IS UNCHANGED** : %s / %s'
          % (p5, p3))
    print('    the scope claim rests on a measurement at the introducing ref : %s' % p6)
    print('    the claim-shaped repair is ROUTED and named as one : %s' % p7)
    print('    %s' % ('PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-README/G-REMOVED/G-PRESERVED/G-SCOPE/G-ROUTED')

    # ---------------------------------------------------------------- COMPONENT 3
    print(chr(10) + '  G-BATCH / G-ATHEAD / G-PINRESOLVES / G-QUOTED / G-NOFIFTH (BAR 5, BAR 6):')
    rows = B['rows']
    WORDS = {'PRESENT', 'RETIRED', 'RENAMED', 'ABSENT'}
    b1 = len(rows) == 12
    b2 = all(v['verdict'] in WORDS for r in rows for v in r['verdicts'])
    b3 = all((r['mode'] == 'AT-PIN') == any(p['resolves'] and p['commit'] == r['ref']
                                            for p in r['pins']) for r in rows)
    b4 = all(r['mode'] == 'CHECKED-AT-HEAD'
             for r in rows if not any(p['resolves'] for p in r['pins']))
    b5 = all(r['ref'] == B['heads'][r['kernel']]['head']
             for r in rows if r['mode'] == 'CHECKED-AT-HEAD')
    b6 = all(v['quote'] for r in rows for v in r['verdicts'] if v['verdict'] == 'RETIRED')
    b7 = all(v['declared'] for r in rows for v in r['verdicts'] if v['verdict'] == 'PRESENT')
    # ### **AND NO HEAD IS WRITTEN INTO A ROW** -- the ruling's own prohibition, measured.
    heads = [v['head'] for v in B['heads'].values()]
    b8 = not any(h[:7] in r['text'] for r in rows for h in heads)
    b9 = all(h in bank for h in heads)
    gb = b1 and b2 and b3 and b4 and b5 and b6 and b7 and b8 and b9
    print('    twelve rows classified : %s ; only the four ruled words : %s' % (b1, b2))
    print('    every AT-PIN ref IS a resolving pin the row names : %s' % b3)
    print('    ### **EVERY ROW WITHOUT A RESOLVING PIN IS MARKED CHECKED-AT-HEAD** : %s' % b4)
    print('    and its ref is the head this act recorded : %s' % b5)
    print('    every RETIRED quotes the kernel : %s ; every PRESENT shows a declaration : %s'
          % (b6, b7))
    print('    ### **NO HEAD APPEARS IN ANY ROW** : %s ### ; every head is in the bank : %s' % (b8, b9))
    print('    %s' % ('PASS' if gb else '### FAIL ###'))
    if not gb:
        fails.append('G-BATCH/G-ATHEAD/G-PINRESOLVES/G-QUOTED/G-NOFIFTH')

    print(chr(10) + '  G-NOROWREPAIR (BAR 7) ### EVERY FLAGGED ROW COMPARED AGAINST ITS BLOB:')
    moved = []
    for r in rows:
        blob = blob_of(PP, r['file'])
        if blob is None:
            moved.append((r['file'], 'no blob'))
            continue
        lines = norm(blob).split(chr(10))
        if r['line'] - 1 >= len(lines) or lines[r['line'] - 1].rstrip() != r['text']:
            moved.append((r['file'], r['line']))
    papers_changed = sorted(x.strip() for x in git(PP, 'diff', '--name-only', 'HEAD').split(chr(10))
                            if x.strip())
    n1 = not moved
    n2 = papers_changed in ([], ['OPEN_TRAILS.md'])
    gnr = n1 and n2
    print('    rows differing from their committed blob : %s' % (moved or 'none'))
    print('    ### **TRACKED PAPERS FILES CHANGED : %s** -- only the trail may appear' % papers_changed)
    print('    %s' % ('PASS' if gnr else '### FAIL ###'))
    if not gnr:
        fails.append('G-NOROWREPAIR')

    print(chr(10) + '  G-PRICE (the separate ruling priced, not attempted):')
    q1 = 'THE PRICE OF THE SEPARATE RULING' in bf
    q2 = 'THIS ACT ATTEMPTS NONE OF IT' in bf
    q3 = all(not any(p['resolves'] for p in r['pins']) or r['mode'] == 'AT-PIN' for r in rows)
    inv = json.load(io.open(d('b371_inventory.json'), encoding='utf-8'))
    q4 = str(inv['without_pin']) in bank
    gq = q1 and q2 and q3 and q4
    print('    the price is given : %s ; and refused : %s ; the pinless count is named : %s'
          % (q1, q2, q4))
    print('    %s' % ('PASS' if gq else '### FAIL ###'))
    if not gq:
        fails.append('G-PRICE')

    print(chr(10) + '  G-NOBUILD / G-NOLEAN:')
    src2 = ' '.join(strip_prose(t(x)) for x in ('b372_batch.py', 'b372_readme.py'))
    l1 = 'lake' not in src2 and 'AllPrints' not in src2
    l2 = not [x for x in git(SIDE, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    l3 = not [x for x in git(KER, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    l4 = not [x for x in git(SK, 'status', '--porcelain').split(chr(10)) if x.strip().endswith('.lean')]
    gl = l1 and l2 and l3 and l4
    print('    no build invocation in stripped sources : %s' % l1)
    print('    ### **NO `.lean` FILE IS DIRTY IN ANY KERNEL READ** : %s %s %s' % (l2, l3, l4))
    print('    %s' % ('PASS' if gl else '### FAIL ###'))
    if not gl:
        fails.append('G-NOBUILD/G-NOLEAN')

    # ---------------------------------------------------------------- THE DESK AND THE RECORD
    print(chr(10) + '  G-CLOSED / G-KILLFILE:')
    k1 = Q['items'] == Q['closed'] + Q['standing']
    k2 = all(m.get('killing_file') and m.get('exists') and m.get('carries') and m.get('date')
             for m in Q['marks'] if m['disposition'] == 'CLOSE')
    k3 = all(m.get('why') for m in Q['marks'] if m['disposition'] == 'STAND')
    bad = []
    for m in Q['marks']:
        if m['disposition'] != 'CLOSE':
            continue
        p = d(m['killing_file'])
        if not os.path.exists(p) or GN.norm(m['sentence']) not in GN.norm(
                io.open(p, encoding='utf-8', errors='replace').read()):
            bad.append(m['killing_file'])
    k4 = not bad
    k5 = all(m['own_act'] for m in Q['marks'] if m['disposition'] == 'CLOSE') \
        and 'FLAGGED: THE KILLING FILE IS THIS ACT`S OWN' in bf
    gk = k1 and k2 and k3 and k4 and k5
    print('    the dispositions partition the desk : %s (%d = %d + %d)'
          % (k1, Q['items'], Q['closed'], Q['standing']))
    print('    every closure names a file that exists and carries its sentence : %s' % k2)
    print('    ### **AND EVERY KILLING FILE IS RE-READ HERE** : %s %s' % (k4, bad or ''))
    print("    ### **AND THIS ACT'S OWN CLOSURES ARE FLAGGED AS SUCH** : %s" % k5)
    print('    %s' % ('PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-CLOSED/G-KILLFILE')

    print(chr(10) + '  G-TRAIL (one append-only block) ### BEFORE THE PUSH:')
    tb = blob_of(PP, 'OPEN_TRAILS.md')
    t1 = trails.count(TRAIL_MARK) == 1
    t2 = (tb is not None) and norm(trails).startswith(norm(tb).rstrip(chr(10)))
    t3 = F['appended_only'] and F['committed_prefix_intact']
    t4 = F['prior_present'] is True
    t5 = '%' not in TRAIL_MARK and 'None' not in trails.split(TRAIL_MARK)[-1]
    gt = t1 and t2 and t3 and t4 and t5
    print('    the mark appears once : %s ; blob is a true prefix : %s' % (t1, t2))
    print('    append-only both ways : %s ; the prior block is present and unedited : %s' % (t3, t4))
    print('    ### **NO UNFILLED PLACEHOLDER IN THE APPENDED BLOCK** : %s' % t5)
    print('    %s' % ('PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TRAIL')

    print(chr(10) + '  G-ROW (row %s) ### BEFORE THE PUSH:' % ROWNUM)
    rws = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = (len(rws) == 1 and 'NO ROW WAS REPAIRED' in rws[0]
            and 'NO HEAD WAS WRITTEN INTO A ROW' in rws[0]
            and 'ONE QUANTITY AT THREE DIFFERENT REFS' in rws[0] and anc)
    print('    row %s present once : %s ; true prefix of its blob : %s' % (ROWNUM, len(rws) == 1, anc))
    print('    %s' % ('PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW')

    print(chr(10) + '  G-KEY / G-NOTCHECKED:')
    irun = io.open(IDX, encoding='utf-8', errors='replace').read()
    kk1 = 'READ BACK : pin-is-a-date returns 1 row(s)' in irun
    kk2 = all(('%-40s NO KEY after  : True  PASS' % qq) in irun for qq in
              ('the rows are repaired', 'the pins are added', 'the disk is normalised',
               'the federation is audited'))
    kk3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    kk4 = ('NO ROW WAS REPAIRED AND NO PIN WAS ADDED' in idx
           and 'A CHECK AT A HEAD IS WEAKER THAN A CHECK AT A PIN' in idx)
    gkk = kk1 and kk2 and kk3 and kk4
    print('    one key and one row : %s ; four overreadings NO KEY after : %s ; run passed : %s'
          % (kk1, kk2, kk3))
    print('    ### **AND THE KEY SAYS NO ROW WAS REPAIRED AND A HEAD-CHECK IS WEAKER** : %s' % kk4)
    print('    %s' % ('PASS' if gkk else '### FAIL ###'))
    if not gkk:
        fails.append('G-KEY/G-NOTCHECKED')

    print(chr(10) + '  G-ORDER ### SIDE-INVARIANT:')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True,
                        text=True, encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(
        norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION LOCK')[0].encode('utf-8')
    ).hexdigest() == SEAL
    stampm = re.search(r'### locked at \(UTC\) : (\S+)', reg)
    o3 = (stampm is not None) and all(x['run_clock'] > stampm.group(1) for x in (A, R, B, Q, F))
    sat = io.open(SATIS, encoding='utf-8').read() if os.path.exists(SATIS) else ''
    o4 = 'JOINTLY SATISFIABLE' in sat
    o5 = 'LOCKED BEFORE ANY WRITE' in gate_text.flat(reg)
    o6 = 'GATE VERDICT : CLEAR' in io.open(GATE, encoding='utf-8', errors='replace').read()
    go2 = o1 and stampm and o3 and o4 and o5 and o6
    print('    the lock recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    ### **EVERY RELIED-ON RUN IS AFTER THE LOCK** : %s' % o3)
    print('    audit JOINTLY SATISFIABLE : %s ; face says LOCKED BEFORE ANY WRITE : %s ; gate CLEAR : %s'
          % (o4, o5, o6))
    print('    %s' % ('PASS' if go2 else '### FAIL ###'))
    if not go2:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR ### AFTER THE PUSH:')
    hookp, mirrorp = d('b372_hooks.txt'), d('b372_mirror.txt')
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

    print(chr(10) + '  G-NUMBERS:')
    T = R['table']
    TV = B['terminal_tally']
    checks = [
        ('the rostered count %d' % len(A['after']),
         ('ALL `%d` ROSTERED REPOSITORIES' % len(A['after'])) in bf),
        ('the before count', ('Before this act it was `%d` of `%d`'
                              % (sum(1 for v in A['before'].values() if v['fresh_equals_blob']),
                                 len(A['before']))) in bf),
        ('the first ref %s' % T[0]['ref'][:7], T[0]['ref'][:7] in bank),
        ('the second ref %s' % T[1]['ref'][:7], T[1]['ref'][:7] in bank),
        ('the profile at head %d' % T[-1]['prints'], str(T[-1]['prints']) in bank),
        ('the breakdown sum %d' % T[1]['total'], str(T[1]['total']) in bank),
        ('retired %d' % TV.get('RETIRED', 0),
         ('`%d` NAMED TERMINALS RETIRED' % TV.get('RETIRED', 0)) in bf),
        ('present %d / absent %d' % (TV.get('PRESENT', 0), TV.get('ABSENT', 0)),
         ('`%d` PRESENT, `%d` ABSENT' % (TV.get('PRESENT', 0), TV.get('ABSENT', 0))) in bf),
        ('desk items %d' % Q['items'], ('`%d` SWEPT' % Q['items']) in bf),
        ('closed %d' % Q['closed'], ('`%d` CLOSED' % Q['closed']) in bf),
        ('the pinless inventory %d' % inv['without_pin'], str(inv['without_pin']) in bank),
        ('row %s' % ROWNUM, re.search(r'row to append : (\d+)',
                                      io.open(CORR, encoding='utf-8').read()).group(1) == ROWNUM),
        ('the lock hash', SEAL in bank),
        ('the lock stamp', (stampm.group(1) if stampm else 'x') in bank),
        ('the relied-on attribute run', A['run_file'] in bank),
        ('the relied-on batch run', B['run_file'] in bank),
    ]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE:')
    once = True
    for lbl, jf in (('extract', E), ('eol', A), ('readme', R), ('batch', B),
                    ('desk', Q), ('filing', F)):
        p = d(jf['run_file'])
        st = run_clock.read_stamp(p) if os.path.exists(p) else None
        ok = os.path.exists(p) and st == jf['run_clock']
        once = once and ok
        print("    %-10s %-28s clock %s == JSON's %s : %s" % (lbl, jf['run_file'], st,
                                                              jf['run_clock'], ok))
    print('    %s' % ('PASS' if once else '### FAIL ###'))
    if not once:
        fails.append('G-ONCE')

    mymods = tuple(sorted(x for x in os.listdir(os.path.join(ROOT, 'tools'))
                          if x.startswith('b372_') and x.endswith('.py')))
    print(chr(10) + '  G-NOCOMPUTE:')
    banned = ('quad', 'integrate', 'linalg', 'svd', 'eig', 'fft', 'trapezoid', 'curve_fit', 'minimize')
    hits = [(x, b) for x in mymods for b in banned if b in strip_prose(t(x))]
    imports = [x for x in ('numpy', 'scipy', 'mpmath')
               if any(x in strip_prose(t(y)) for y in mymods)]
    gnc = not hits and not imports
    print('    numerical calls : %d %s ; libraries : %s' % (len(hits), hits or '', imports or 'none'))
    print('    %s' % ('PASS' if gnc else '### FAIL ###'))
    if not gnc:
        fails.append('G-NOCOMPUTE')

    print(chr(10) + '  G-BYCONTENT:')
    selfhits = []
    for p in [t(x) for x in mymods]:
        ml = SW.masked_lines(p)
        if ml is None:
            continue
        for i, c in ml:
            if SW.CAND.search(c):
                selfhits.append((os.path.basename(p), i, c.strip()[:110]))
    DECLARED = {
        'last-row cells': 'it takes `[-1:]` -- the LAST line of the table THIS ACT JUST WROTE.',
        'the located span': 'the span is located by content and only then indexed.',
        'the table this act built': 'the row is indexed inside a list THIS ACT built in memory.',
    }

    def which(code):
        if '[-1:]' in code or '[-1]' in code:
            return 'last-row cells'
        if 'split(' in code or 'find(' in code or 'findall' in code:
            return 'the located span'
        if 'table[' in code or 'TBL[' in code or 'T[' in code or 'rows[' in code:
            return 'the table this act built'
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
             'tools/ferry_scan.py', 'tools/gate_needle.py', 'tools/gate_content.py',
             'tools/b327_faces_row.py', 'tools/mirror_roster.json', 'tools/mirror_verify.py',
             'tools/b366_sweep.py', 'tools/b303_pins.py', 'tools/b304_hooks.py',
             'tools/b363_span.py', 'tools/git-hooks/pre-push', 'tools/b371_inventory.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    unlicensed = [p for p in touched if p not in LICENSED]
    others = [x for x in git(ROOT, 'diff', '--name-only', 'HEAD').split(chr(10))
              if x.strip() and 'b372' not in x and x.strip() != 'tools/banked_index.py'
              and x.strip() != '.gitattributes']
    ppstat = [x for x in git(PP, 'status', '--porcelain').split(chr(10))
              if x.strip() and 'BLOB_SENSITIVITY' not in x]
    ppbad = [x for x in ppstat if x[3:].strip() not in ('OPEN_TRAILS.md',)]
    faces_clean = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FACES_LEDGER.md').strip()
    fnd = not git(PP, 'diff', '--name-only', 'HEAD', '--', 'FINDINGS.md').strip()
    gse = [x for x in git(SIDE, 'status', '--porcelain').split(chr(10))
           if x.strip() and x[3:].strip() not in ('CORRESPONDENCE.md', 'README.md')]
    kse = [x for x in git(KER, 'status', '--porcelain').split(chr(10))
           if x.strip() and x[3:].strip() not in ('.gitattributes',)
           and 'b304-backup' not in x]
    ske = [x for x in git(SK, 'status', '--porcelain').split(chr(10)) if x.strip()]
    gne = (not unlicensed and not others and not ppbad and faces_clean and fnd
           and not gse and not kse and not ske)
    print('    owner instruments modified : %s' % (touched or 'none'))
    print('    ### **UNLICENSED : %s** ### -- this act licenses none' % (unlicensed or 'none'))
    print('    other relay files of other acts : %s' % (others or 'none'))
    print('    papers paths beyond the trail : %s' % (ppbad or 'none'))
    print('    construction-kernel paths beyond the row and the README : %s' % (gse or 'none'))
    print('    exclusion-kernel paths beyond the attribute : %s' % (kse or 'none'))
    print('    ### **SIDE-kernel IS UNTOUCHED (it was opened READ-ONLY)** : %s' % (not ske))
    print('    ### **FACES_LEDGER UNTOUCHED** : %s ; FINDINGS clean : %s' % (faces_clean, fnd))
    print('    %s' % ('PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    OWNED = [BANK, REG, CORR, IDX, CENSUS0, FCEN, REGSPEC, SATIS, PINS0, GATE,
             d('b372_satisfiable.json')] + [t(x) for x in mymods]
    CARRIERS = [
        (t('b372_checks.py'), 'its own fixtures'),
        (FERRY, 'IT IS THE ORDER'), (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's log"),
        (d(E['run_file']), "the extract carries the kernels' own documents"),
        (d(A['run_file']), "the attribute run carries the repositories' own lines"),
        (d(R['run_file']), "the README run carries the document's own figures"),
        (d(B['run_file']), "the batch carries the rows' and the ledger's own text"),
        (d(Q['run_file']), "the desk run carries the items' own sentences"),
        (d(F['run_file']), 'the filing carries the closures and the routing'),
        (t('b372_batch.py'), "ITS ROW HINTS ARE THE ROWS' OWN TEXT"),
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
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
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

    marker = '# ### THE EOL PIN, THE README FIGURES, THE FIRST BATCH OF ROW CHECKS (b372).'
    nxt = '# ### THE FIRST TARGET SETTLED, THE DESK CLOSED, THE GUARD MOVED (b371).'
    ib2 = idx[idx.index(marker):idx.index(nxt)] if (marker in idx and nxt in idx) else ''
    tblk = trails.split(TRAIL_MARK)[-1] if TRAIL_MARK in trails else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the trail block, the index row):' % ROWNUM)
    for lbl, b2 in (('row %s' % ROWNUM, rws[0] if rws else ''), ('the trail block', tblk),
                    ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(b2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(b2, [], stem_list)
        print('    %-22s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(b2)))
        if ch or not b2:
            fails.append('G-STEM-APPENDED ' + lbl)
        if sh:
            tmp2 = os.path.join(tempfile.mkdtemp(prefix='b372_stem_'), 'blk.txt')
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
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
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
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b372_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
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
