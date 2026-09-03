# -*- coding: utf-8 -*-
"""b307_checks.py -- THE GATE SUITE FOR A FILINGS ACT.

### ### **TWO ARMS ARE INVERTED THIS ACT AND THE INVERSION IS THE POINT:**
###   ### **`G-PAPERS`** ### -- every prior act checked that `PLACE-papers` was NOT touched.
###     ### **THIS ACT TOUCHES IT**, so the gate checks ### WHICH ### file moved and that the move
###     was additive, rather than that nothing moved. ### **A GATE COPIED FORWARD UNINVERTED WOULD
###     HAVE FAILED THE ACT FOR DOING WHAT IT WAS ORDERED TO DO.**
###   ### **`G-STRUCK`** ### -- the registration and the bank both carry the struck phrase ### IN
###     ORDER TO DECLARE IT ### . ### `ferry_scan.py`'s own law covers it: ### **"a ferry that
###     strikes a clause quotes the clause in order to strike it, and that quotation hits."** ###
###     Both are DECLARED CARRIERS, swept and reported separately with their reason.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b307_the_fold.txt')
REG = d('b307_registration_2026-09-03.txt')
FRUN = d('b307_fold_run.txt')
CB = d('b307_census_before.txt')
CA = d('b307_census_after.txt')
EMIT = d('b307_fold_emitted.md')
SCAN = d('b307_ferry_scan.txt')
FERRY = d('b307_ferry_2026-09-03.txt')

OWNED = [FRUN, CB, CA, EMIT,
         d('b307_corr_row.txt'), d('b307_index_query.txt'), d('b307_pins_step_zero.txt'),
         d('b307_regspec_run.txt'), d('b307_satisfiable.json'),
         t('b307_fold.py'), t('b307_handoff_census.py'), t('b307_regspec.py'),
         t('b307_correspondence.py')]
# ### DECLARED CARRIERS. ### **EACH IS A PLACE A CHECK HAS AGREED NOT TO COUNT, AND THE REASON IS
# ### PRINTED WITH IT** -- b306's lore rule, applied to this act's own suite.
CARRIERS = [
    (t('b307_checks.py'), 'its own fixtures'),
    (t('b307_index_append.py'), 'its own fixtures'),
    (BANK, 'it quotes the struck U-2 phrase IN ORDER TO DECLARE IT'),
    (REG, 'it quotes the struck U-2 phrase IN ORDER TO DECLARE IT'),
    (FERRY, 'IT IS THE ORDER -- the struck phrase is the INPUT, not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log and MUST quote the line it hit'),
]

OWNER_NEEDLES = [
    ("b297's design point: the generator is not a review", d('b297_the_fold.txt'),
     'IS THE DOCUMENT'),
    ("b299's incident, which built the ferry scan", d('b299_the_arc_keystone.txt'),
     'THE STRIKE ARRIVED IN THE FERRY AND NOTHING IN THE COMMAND PATH READ THE'),
    ("b298's own headline", d('b298_the_boundary_terminal.txt'),
     'THE KERNEL NOW CARRIES BOTH SIDES OF THE BOUNDARY AT ONE CELL.'),
    ("b300's conditional construction", d('b300_the_archimedean_leg.txt'),
     'THE SPACE: ### (CONSTRUCTED, CONDITIONALLY).'),
    ("b301's four typed conditions", d('b301_the_object_completed.txt'),
     'THE OBJECT IS CONSTRUCTED CONDITIONALLY, AND THE CONDITIONS ARE FOUR, EACH TYPED:'),
    ("b302's narrowing sentence", d('b302_the_unit_requirement.txt'),
     'IT NARROWS THE ORIGINAL WORDING RATHER'),
    ("b303's division", d('b303_the_uniform_family.txt'), 'ONE SENTENCE, TWO OBJECTS'),
    ("b304's one-level sentence", d('b304_the_demands_shape.txt'),
     'IT DOES NOT DISSOLVE, AND CANNOT'),
    ("b305's identification", d('b305_the_arithmetics_entry.txt'),
     'THESE ARE THE SAME EXPRESSION'),
    ("b306's rule", d('b306_the_difference.txt'),
     'A DIFFERENCE OF TWO THINGS IS THE SAME OBJECT ONLY IF BOTH ARE'),
    ("### the U-2 entry and its SURVIVES clause (EMITTER)", d('STRUCK_CLAUSES.md'),
     'the same phrase after a check that has COUNTED WHAT IS MISSING'),
    ("### the author's ruling that U-2 records", d('STRUCK_CLAUSES.md'),
     'may be used only when a check has counted what is missing'),
    ("b260's junction, signed by theorem", d('b260_junction_sign.txt'), 'ON THE OWNERS'),
    ("b261's bench grade", d('b261_e2even_monotone.txt'),
     'HOLDS AT BENCH. ### THE DERIVATION IS NOT CLAIMED'),
]

SELF_NEEDLES = [
    ('bank reports the scan fired on the order', BANK, "IT WAS IN THE ORDER'S OWN"),
    ('bank quotes the SURVIVES clause', BANK, 'COUNTED WHAT IS MISSING'),
    ('bank reports the census both ways', BANK, 'BEFORE: 26 MISSING'),
    ('bank bounds the licence to one ledger', BANK, 'THAT LEDGER AND NO OTHER'),
    ('bank names the instrument working in its built direction', BANK,
     'THE INSTRUMENT WORKING IN THE DIRECTION IT WAS BUILT FOR'),
    ('bank reports the gate fired before emission', BANK, 'IT FIRED BEFORE EMISSION'),
    ('bank owns the mis-attribution the gate caught', BANK, 'ABOUT TO'),
    ('bank declares the tool cannot tell voice from quotation', BANK,
     'CANNOT TELL AN ACT'),
    ('bank gives the arc sentence', BANK, 'THE OBJECT'),
    ('bank prints the scope beside it', BANK, 'THE SCOPE, PRINTED BESIDE IT AND NOT BELOW IT'),
    ('bank refuses to average the grades', BANK, 'average them.'),
    ('bank separates mechanized from judgement lore', BANK, 'THE JUDGEMENT LIST'),
    ('bank gives each lore rule an incident', BANK, 'OR IT IS A SLOGAN'),
    ('bank inventories the instruments with incidents', BANK, 'ITS INCIDENT'),
    ('bank states the suite limit', BANK, 'TELL A TRUE STATEMENT FROM A FALSE ONE'),
    ('bank gives the desk as one list', BANK, 'THE DESK. ### **ONE LIST.**'),
    ('bank puts the patent clock on the desk', BANK, 'THREE DAYS PAST BOTH'),
    ('bank says the patent lane is unverified here', BANK, 'VERIFIED NOTHING IN THAT LANE'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank restates the seam debt', BANK, "THE SEAM'S DEBT ITEM 1: ### STILL UNPAID"),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps M-2 owed', BANK, '`M-2` IS OWED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration declares the struck hit up front', REG, 'THE STRUCK CLAUSE IN THE ORDER ITSELF'),
    ('registration makes the census decide', REG, 'THE CENSUS DECIDES'),
    ('registration is sealed before the bank', REG, 'SEALED BEFORE THE BANK'),
    ('the fold run reports zero unfindable', FRUN, '0 unfindable'),
    ('the fold run reports the discrimination control', FRUN, 'DISCRIMINATION CONTROL'),
    ('the fold run reports additive findings', FRUN, 'F-NOGRADE DID NOT FIRE'),
    ('the census before reports a non-zero total', CB, 'TOTAL MISSING : 26'),
    ('the census after reports zero', CA, 'TOTAL MISSING : 0'),
    ('the census after states the licence', CA, 'SURVIVES'),
]

MUST_FAIL = [
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('no act is re-verdicted', BANK, 'b302 IS RE-VERDICTED.'),
    ('the fold is not called a result', BANK, 'THE FOLD IS A RESULT.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('the arc sentence is not called evidence', BANK, 'THE ARC SENTENCE IS EVIDENCE.'),
    ('the bench half is not promoted', BANK, 'E2even IS DERIVED.'),
    ('no keystone is claimed written', BANK, 'A KEYSTONE IS WRITTEN.'),
    ('the licence is not extended to other ledgers', BANK, 'FINDINGS.md IS CURRENT.'),
    ('the patent lane is not confirmed', BANK, 'THE RECEIPTS ARE CONFIRMED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the fold's quotation counts and the additive measurement", 'tools/b307_fold.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b307_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b307_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b307_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b307_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the mirror's three clauses", 'tools/mirror_verify.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b307' in x)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b307 -- GATE SUITE (A FILINGS ACT)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (pulled from emitting files):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    frun = io.open(FRUN, encoding='utf-8').read()
    cb = io.open(CB, encoding='utf-8').read()
    ca = io.open(CA, encoding='utf-8').read()

    # ### G-CENSUS -- ### **THE LICENCE IS CONDITIONED ON THE AFTER-COUNT, NOT ON THE SEAT.**
    print('\n  G-CENSUS (the U-2 licence is earned, not asserted):')
    before_nonzero = 'TOTAL MISSING : 0' not in cb
    after_zero = 'TOTAL MISSING : 0' in ca
    licensed = 'SURVIVES' in ca and 'MAY BE USED' in ca
    print('    before-count non-zero : %s ; after-count zero : %s ; licence printed : %s'
          % (before_nonzero, after_zero, licensed))
    print('    ### **A CENSUS THAT WAS ZERO BEFORE THE WRITE WOULD HAVE LICENSED NOTHING** --')
    print('    ### it would have meant the check could not tell a current ledger from a stale one.')
    if not (before_nonzero and after_zero and licensed):
        fails.append('G-CENSUS')

    # ### G-QUOTE-FOLD.
    print('\n  G-QUOTE-FOLD (the generator gated the document before writing it):')
    zero_unfindable = '0 unfindable' in frun
    disc = 'DISCRIMINATION CONTROL: an altered quotation is reported unfindable : True' in frun
    print('    0 unfindable at emission : %s ; discrimination control fired : %s'
          % (zero_unfindable, disc))
    if not (zero_unfindable and disc):
        fails.append('G-QUOTE-FOLD')

    # ### G-PAPERS -- ### **INVERTED THIS ACT.**
    print('\n  G-PAPERS (INVERTED: the papers repo IS touched, so WHICH file and HOW):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    rows = [x for x in pp.splitlines() if x.strip()]
    tracked = [x for x in rows if not x.startswith('??')]
    names = sorted(x[3:].strip() for x in tracked)
    only_findings = (names == ['FINDINGS.md'])
    ns = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', 'FINDINGS.md'],
                        capture_output=True, text=True).stdout.split()
    added = int(ns[0]) if len(ns) >= 2 else 0
    removed = int(ns[1]) if len(ns) >= 2 else -1
    additive = (removed == 0 and added > 0)
    ks = [l for l in rows if 'keystone' in l.lower() or '/method/' in l.replace('\\', '/')]
    print('    tracked files changed : %s' % names)
    print('    ONLY FINDINGS.md changed : %s  %s'
          % (only_findings, 'PASS' if only_findings else '### FAIL ###'))
    print('    FINDINGS.md +%d / -%d  -> purely additive : %s  %s'
          % (added, removed, additive, 'PASS' if additive else '### FAIL ###'))
    print('    files under a keystone path : %d  %s'
          % (len(ks), 'PASS' if not ks else '### FAIL ###'))
    if not (only_findings and additive) or ks:
        fails.append('G-PAPERS')

    # ### G-NOBUILD.
    print('\n  G-NOBUILD (nothing built; the profile does not move):')
    prof = io.open(PROFILE, 'rb').read()
    phead = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                           capture_output=True).stdout
    identical = (prof == phead)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout.strip()
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile BYTE-IDENTICAL to git HEAD : %s ; `.lean` changed : %d ; prints : %d'
          % (identical, len(lean_rows), len(lines)))
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### G-ANCESTOR.
    print('\n  G-ANCESTOR (no ancestor correspondence row rewritten):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    prefix = now.startswith(head.rstrip('\n'))
    print('    committed table is a TRUE PREFIX of the current one : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    if not prefix:
        fails.append('G-ANCESTOR')

    # ### G-NOMOVE.
    print('\n  G-NOMOVE (a filings act moves no grade and re-verdicts nothing):')
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVED' in bank and 'NO ACT RE-VERDICTED' in bank
    dpos = bool(mv.search('and E2even is now derived'))
    print('    grade-moving lines : %d ; both refusals present : %s ; discrimination : %s'
          % (len(mhits), says, dpos))
    if mhits or not says or not dpos:
        fails.append('G-NOMOVE')

    # ### G-STRUCK -- ### **WITH THIS ACT'S TWO DECLARED CARRIERS.**
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
    total, scanned = 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                     struck, stem_list)
        total += len(ch)
        if ch:
            print('    ### %-40s hits : %d' % (os.path.basename(p), len(ch)))
    print('    files scanned %d   struck-clause hits %d  %s'
          % (scanned, total, 'PASS' if not total else '### FAIL ###'))
    for p, why in CARRIERS:
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        print('    %-34s hits : %d  ### DECLARED CARRIER -- %s'
              % (os.path.basename(p), len(ch), why))
    fired = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired += 1 if hit else 0
        print('    DISCRIMINATION %-4s comes back hit : %s  %s'
              % (eid, hit, 'PASS' if hit else '### FAIL ###'))
    if total or fired != 3:
        fails.append('G-STRUCK')

    # ### G-STEM at the extended scope.
    print('\n  G-STEM (this act\'s files, EXCEPT the declared carriers):')
    stem_total, swept = 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        swept += 1
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        stem_total += len(sh)
        if sh:
            print('    ### %-40s stem hits : %d' % (os.path.basename(p), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    for p, why in CARRIERS:
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), [], stem_list)
        print('    %-34s stem hits : %d  ### CARRIER -- %s' % (os.path.basename(p), len(sh), why))
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    files swept %d   stem hits %d   control fires %s   %s'
          % (swept, stem_total, ctrl, 'PASS' if not stem_total and ctrl else '### FAIL ###'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    print('\n  G-SHARED (the extended sweep over the shared append-targets):')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s' % sorted(got))
    print('    UNEXPECTED : %d %s  %s'
          % (len(extra), sorted(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-36s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG),
                      ('the emitted fold', EMIT)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            print('        ### %d flagged sentence(s) -- DESCRIBED, NOT QUOTED, so this log does'
                  % len(gh))
            print('        ### not itself acquire the shape it is reporting.')

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 11
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
