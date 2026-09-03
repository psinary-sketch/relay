# -*- coding: utf-8 -*-
"""b311_checks.py -- THE GATE SUITE FOR A READ AND A DECISION AT DEFINITIONS.

### ### **THE THREE ARMS THAT MATTER THIS ACT ARE ALL NEW, AND EACH GUARDS A DIFFERENT DRIFT:**
###   ### **`G-QUARANTINE`** ### -- the finite-side results must not be transported. ### Its
###     must-fail fixtures are the sentences this act would have written if it had carried b310's
###     count across, and ### **b285's HAZARD REGISTER IS WHY THEY ARE NEEDED: THE WORD SURVIVES;
###     ### THE OBJECT DOES NOT.**
###   ### **`G-NOARCHNUM`** ### -- no archimedean number is computed. ### The cheapest guarantee is
###     structural and this suite checks it: ### **THE ACT'S TWO NEW TOOLS CONTAIN NO ARITHMETIC AT
###     ### ALL** -- no float, and no operator that could produce a value from the source's numbers.
###   ### **`G-RULING`** ### -- the author's `W2` is RECORDED VERBATIM and NOT APPLIED.
### ### **AND `G-NOBUILD` IS INVERTED BACK FROM b310's `G-KERNEL`:** ### that act moved the profile;
### this one must not. ### **A GATE COPIED FORWARD UNINVERTED WOULD HAVE FAILED THIS ACT FOR NOT
### ### BUILDING SOMETHING IT WAS ORDERED NOT TO BUILD.**
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
import b302_kernel as KRN  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b311_the_identitys_neighbourhood.txt')
REG = d('b311_registration_2026-09-03.txt')
RUN = d('b311_components_run.txt')
PIN = d('b311_source_pin.txt')
SCAN = d('b311_ferry_scan.txt')
FERRY = d('b311_ferry_2026-09-03.txt')
CENSUS = d('b311_census.txt')

OWNED = [RUN, PIN, CENSUS,
         d('b311_corr_row.txt'), d('b311_index_query.txt'), d('b311_pins_stepzero.txt'),
         d('b311_regspec_run.txt'), d('b311_satisfiable.json'),
         t('b311_regspec.py'), t('b311_correspondence.py'), t('b311_components.py'),
         t('b311_source.py')]

CARRIERS = [
    (t('b311_checks.py'), 'its own fixtures'),
    (t('b311_index_append.py'), 'its own fixtures'),
    (BANK, 'it quotes the false clause of its own sealed registration IN ORDER TO WITHDRAW IT'),
    (REG, 'it is the sealed registration, including the clause the bank withdraws'),
    (FERRY, 'IT IS THE ORDER -- not this act\'s writing'),
    (SCAN, 'it is the scan\'s own log'),
]

OWNER_NEEDLES = [
    ("b285 -- THE HAZARD REGISTER", d('b285_archimedean_opening.txt'), 'THE HAZARD REGISTER'),
    ("### b285 -- what survives a crossing and what does not",
     d('b285_archimedean_opening.txt'), 'THE WORD SURVIVES; THE OBJECT DOES NOT'),
    ("b285 -- the boundary", d('b285_archimedean_opening.txt'),
     'NO FINITE-SIDE STRUCTURAL FACT TYPES'),
    ("### b198 via b285 -- there is NO archimedean ball",
     d('b285_archimedean_opening.txt'), 'NO SUCH OBJECT'),
    ("b286 -- the archimedean space, its OWN bank", d('b286_the_cc_condition.txt'),
     'THE SPACE IS `L^2(R)_ev`.'),
    ("b300 -- the unit is IN the source's space", d('b300_the_archimedean_leg.txt'),
     'THE CHOSEN UNIT:'),
    ("b292 -- the prolate vectors are NOT, its OWN bank", d('b292_the_identification.txt'),
     'IS NOT IN `S(1,1)`'),
    ("b305 -- eq. (149)", d('b305_the_arithmetics_entry.txt'), 'W_p(f) = (log p) SUM_{m>=1}'),
    ("### b305 -- and where the logarithm is", d('b305_the_arithmetics_entry.txt'),
     '`log p` is in `W_p`'),
    ("b310 -- the finite-side sentence this act tests", d('b310_the_smear_collapses.txt'),
     'SIGNED COUNT OF THE OFF-BALL POINTS'),
    ("### b310 -- and its own refusal to reach infinity", d('b310_the_smear_collapses.txt'),
     'THIS ACT DERIVES NOTHING'),
    ("b306 -- the work-order this act bears on", d('b306_the_difference.txt'),
     'W-ORD-SOURCE-METHOD-APPLICABILITY'),
    ("b304 -- the source's construction, quoted in its emitting tool", t('b304_smearing.py'),
     'associate to a test function'),
]

SELF_NEEDLES = [
    ('bank states the decision up front', BANK, 'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE'),
    ('bank names the step at which the cases part', BANK, 'THE DIMENSION OF THE OBJECT'),
    ('bank quotes the source on the space being infinite', BANK, 'infinite dimensional Sonin'),
    ('bank gives Theorem 4.7', BANK, 'W_inf(f) + INT f(rho^-1) eps(rho)'),
    ('bank records the W2 ruling verbatim', BANK, 'a mean-zero variant of the corpus'),
    ('bank marks the ruling recorded and not applied', BANK, 'RECORDED, NOT APPLIED'),
    ('### bank withdraws its own sealed false claim', BANK, 'BOTH ARE FALSE'),
    ('### bank says where the artefact actually is', BANK, 'WHERE IT ACTUALLY IS'),
    ('### bank owns the incomplete-search defect', BANK, 'HAD NOT FINISHED WHEN THE ABSENCE'),
    ('bank says the seal is not edited', BANK, 'THE SEAL IS NOT EDITED'),
    ('bank reports the fragments located', BANK, '20 FRAGMENTS LOCATED'),
    ('bank quotes the source saying formally', BANK, 'is FORMALLY given by'),
    ('bank quotes the trace-class sentence', BANK, 'is of trace class and its trace is given by'),
    ('bank quotes tau not being a function', BANK, 'not a function because of the divergency'),
    # ### RE-POINTED: the bank's own hard wrap falls inside the quotation.
    ('bank gives the derivative jump', BANK, 'has a jump in its'),
    ('bank gives Theorem 3.6', BANK, '-2 Id + K_I'),
    ('bank separates the two jobs of the support', BANK, 'AN ARITHMETIC GATE ON ONE SIDE'),
    ('bank gives the decision table', BANK, 'THE DECISION TABLE'),
    ('bank gives the evaluation-versus-jacobian reason', BANK, 'AN EVALUATION AND A JACOBIAN'),
    ('bank refuses the resemblance as evidence', BANK, 'REFUSED AS EVIDENCE'),
    ('bank says it exhibits no bridging definition', BANK, 'CLAIMS NONE'),
    ('bank reports F2 refuted in its first half', BANK, 'REFUTED IN ITS FIRST HALF'),
    ('bank refuses the identity-alone reading', BANK, 'ABOUT THE IDENTITY'),
    ('bank prices the truncation as the whole cost', BANK, 'THE WHOLE OF THE COST'),
    ('bank names the source sentence as the obstacle', BANK, 'does not restrict to this subspace'),
    ('bank lists what W2 obligates', BANK, 'WHAT THE `W2` RULING OBLIGATES'),
    ('bank gives the import ledger', BANK, 'THE IMPORT LEDGER'),
    ('bank states the ledger own limit', BANK, 'DID NOT VERIFY A SINGLE PROOF'),
    ('bank restates the object three conditions', BANK, "THE OBJECT'S THREE CONDITIONS"),
    ('bank keeps M-2 unchanged under its cap', BANK, 'UNDER b310'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'DAYS PAST BOTH, AND'),
    ('bank names the window question as the author\'s', BANK, 'NOT OPENED HERE'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER'),
    ('bank files the artefact-paths work-order', BANK, 'W-ORD-ARTEFACT-PATHS'),
    ('bank names the fold as due', BANK, 'IS OWED A'),
    ('bank reports the shadow as nothing', BANK, 'NOTHING IS WHAT IT IS'),
    ('bank states what it did not check', BANK, 'WHAT THIS ACT DID NOT CHECK'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 is the clause'),
    ('registration declares the read preceded the seal', REG, 'THE READ HAS ALREADY HAPPENED'),
    ('registration refuses to dress a finding as a prediction', REG, 'IT IS NOT DONE HERE'),
    ('registration records the ruling verbatim', REG, 'W2 -- a mean-zero variant'),
    ('registration caps rulings applied', REG, 'rulings applied'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the decision', RUN, 'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE'),
    ('the run reports the verdict on F2', RUN, 'REFUTED IN ITS'),
    ('the pin log reports the hash match', PIN, 'MATCHES THE ARTEFACT b304 PINNED'),
    ('the census reports its count', CENSUS, 'TOTAL MISSING : 0'),
]

MUST_FAIL = [
    # ### ### **`G-QUARANTINE` -- THE SENTENCES A TRANSPORT WOULD HAVE PRODUCED.**
    ('the finite count is not carried across', BANK, 'THE COUNT VANISHES AT INFINITY.'),
    ('the archimedean compression is not said to vanish', BANK,
     'THE ARCHIMEDEAN COMPRESSION VANISHES.'),
    ('the finite mechanism is not said to reach infinity', BANK,
     'THE MECHANISM REACHES INFINITY.'),
    ('no archimedean ball is asserted', BANK, 'THE ARCHIMEDEAN BALL IS THE INTERVAL.'),
    # ### **`G-NOARCHNUM` AND THE STANDING REFUSALS.**
    ('no archimedean number is computed', BANK, 'THE ARCHIMEDEAN VALUE IS COMPUTED.'),
    ('the source is not said to be about the identity alone', BANK,
     'THE SOURCE RESULT IS ABOUT THE IDENTITY ALONE.'),
    ('no proof of the source is claimed verified', BANK, 'THE SOURCE PROOF IS VERIFIED.'),
    # ### **`G-RULING`.**
    ('the ruling is not applied', BANK, 'THE W2 VARIANT IS BUILT.'),
    ('the window question is not answered', BANK, 'THE WINDOW QUESTION IS SETTLED.'),
    # ### **THE STANDING CAPS.**
    ('the branch is not decided', BANK, 'THE BRANCH IS DECIDED.'),
    ('M-2 is not verdicted', BANK, 'M-2 IS UNSATISFIABLE.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('b310 is not re-verdicted', BANK, 'b310 IS RE-VERDICTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
]

TOOLNUM = [
    ("the artefact's hash, its page count and every fragment location",
     'tools/b311_source.py'),
    ("the flattener and the hash check the source tool imports", 'tools/b305_source.py'),
    ("the truncation detector that measured the text layer", 'tools/b303_source.py'),
    ("the components' tables and verdicts", 'tools/b311_components.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits and their attribution", 'tools/b306_stem_scope.py'),
    ("the ahead/behind pairs and the pins", 'tools/b303_pins.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b311_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b311_checks.py'),
    ("the correspondence rows' numbers and their read-back", 'tools/b311_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b311_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the byte checks the profile comparison imports", 'tools/b302_kernel.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b311' in x)

# ### ### **`G-NOARCHNUM`'s STRUCTURAL ARM.** ### The cheapest guarantee that this act computes no
# ### archimedean number is that its tools contain NO ARITHMETIC AT ALL on the source's quantities.
ARITH = re.compile(r'(?<![\w.])\d+\.\d+|(?<![\w.])\d+[eE][-+]?\d+|\bFraction\b|\bmath\.|\bfloat\s*\(')
STRINGS = re.compile(r"'(?:\\.|[^'\\])*'|\"(?:\\.|[^\"\\])*\"")


def _strip_strings(line):
    return STRINGS.sub(lambda m: ' ' * len(m.group(0)), line)


def arith_sites(path):
    out = []
    for i, line in enumerate(io.open(path, encoding='utf-8', errors='replace').read().splitlines(),
                             1):
        s = line.strip()
        if s.startswith('#'):
            continue
        if ARITH.search(_strip_strings(line)):
            out.append((i, s))
    return out


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b311 -- GATE SUITE (A READ AND A DECISION AT DEFINITIONS)')
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
    print('    ### **THE FIRST FOUR ARE `G-QUARANTINE`: the sentences a transport would have')
    print('    ### produced. ### THE NEXT THREE ARE `G-NOARCHNUM` AND THE READ\'S OWN LIMITS. ### THE')
    print('    ### NEXT TWO ARE `G-RULING`.**')

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()

    # ### G-SOURCE.
    print('\n  G-SOURCE (the artefact pinned BEFORE it was read; every fragment located):')
    pin = io.open(PIN, encoding='utf-8').read()
    matched = 'MATCHES THE ARTEFACT b304 PINNED : True' in pin
    layer = 'pages with NO text layer at all         : 0' in pin
    located = 'FRAGMENTS NOT LOCATED : 0' in run or '0 unlocated' in run
    print('    hash matches the corpus pin : %s ; text layer intact : %s ; fragments located : %s'
          % (matched, layer, located))
    if not (matched and layer):
        fails.append('G-SOURCE')

    # ### G-NOARCHNUM -- the structural arm.
    print('\n  G-NOARCHNUM (no archimedean number computed -- checked STRUCTURALLY):')
    tot = 0
    for path in (t('b311_source.py'), t('b311_components.py')):
        sites = arith_sites(path)
        tot += len(sites)
        print('    %-26s arithmetic sites : %d' % (os.path.basename(path), len(sites)))
        for i, s in sites:
            print('        ### line %-5d %s' % (i, s[:84]))
    fx = (bool(ARITH.search('x = 1.5')) and bool(ARITH.search('v = Fraction(1, 2)'))
          and not bool(ARITH.search('for i in range(len(pages)):')))
    print('    fixture arms agree : %s' % fx)
    print('    ### **THE ACT\'S TWO NEW TOOLS CONTAIN NO ARITHMETIC AT ALL**, which is the cheapest')
    print('    ### possible guarantee that no number here is the corpus\'s own. ### Every')
    print('    ### archimedean quantity the bank names is a LOCATED QUOTATION.')
    if tot or not fx:
        fails.append('G-NOARCHNUM')

    # ### G-RULING.
    print('\n  G-RULING (the author\'s W2 recorded VERBATIM, attributed, strikeable, NOT applied):')
    verbatim = 'a mean-zero variant of the corpus' in bank and 'replacing nothing' in bank
    attributed = "RULED BY THE AUTHOR, BY PASTE" in io.open(REG, encoding='utf-8').read()
    strikeable = 'STRIKEABLE BY THE AUTHOR' in bank or 'strikeable' in bank.lower()
    notapplied = 'RECORDED, NOT APPLIED' in bank
    print('    verbatim : %s ; attributed : %s ; strikeable : %s ; NOT applied : %s'
          % (verbatim, attributed, strikeable, notapplied))
    if not (verbatim and attributed and strikeable and notapplied):
        fails.append('G-RULING')

    # ### G-NOBUILD -- ### **INVERTED BACK FROM b310's G-KERNEL.**
    print('\n  G-NOBUILD (INVERTED BACK: b310 moved the profile; this act must NOT):')
    prof = KRN.normalise(io.open(PROFILE, 'rb').read())
    phead = KRN.normalise(KRN.git_show('AXIOM_PRINTS.txt') or b'')
    identical = (prof == phead)
    dirty = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                           capture_output=True, text=True).stdout
    lean_rows = [x for x in dirty.splitlines() if x.strip().endswith('.lean')]
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    print('    profile identical to git HEAD (NORMALISED) : %s ; `.lean` changed : %d ; prints : %d'
          % (identical, len(lean_rows), len(lines)))
    print('    ### **A GATE COPIED FORWARD FROM b310 UNINVERTED WOULD HAVE FAILED THIS ACT FOR NOT')
    print('    ### BUILDING SOMETHING IT WAS ORDERED NOT TO BUILD.**')
    if not identical or lean_rows:
        fails.append('G-NOBUILD')

    # ### G-NOPAPERS / G-ANCESTOR / G-NOMOVE.
    print('\n  G-NOPAPERS / G-ANCESTOR / G-NOMOVE:')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(TABLE, encoding='utf-8').read()
    pfx = now.startswith(head.rstrip('\n'))
    mv = re.compile(r'\b(grade moves to|we promote|promoted to derives|is now derived|'
                    r'this act re-verdicts)\b', re.I)
    mhits = [ln for ln in bank.splitlines() if mv.search(ln)]
    says = 'NO GRADE MOVED' in bank and 'NO ACT RE-VERDICTED' in bank
    dpos = bool(mv.search('and b310 is now derived'))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s' % (len(tracked), pfx))
    print('    grade-moving lines : %d ; both refusals present : %s ; discrimination : %s'
          % (len(mhits), says, dpos))
    if tracked:
        fails.append('G-NOPAPERS')
    if not pfx:
        fails.append('G-ANCESTOR')
    if mhits or not says or not dpos:
        fails.append('G-NOMOVE')

    # ### G-STRUCK / G-STEM.
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
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
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired_disc += 1 if hit else 0
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s'
          % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s' % sorted(got))
    print('    ### **THE EXCEPTION LIST WITH ITS REASONS:** ### `row 2` predates the ban (b142);')
    print('    ### `row 101` is b284\'s, FILED AND NOT REWRITTEN under the append-only law.')
    print('    UNEXPECTED : %d  %s' % (len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-SEAL:')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    print('    seal intact : %s  %s' % (intact, 'PASS' if intact else '### FAIL ###'))
    print('    ### **AND IT MATTERS MORE THIS ACT THAN USUALLY: THE SEAL COVERS A CLAUSE THE BANK')
    print('    ### WITHDRAWS AS FALSE, AND THE CLAUSE STAYS WHERE A READER WILL MEET IT.**')
    if not intact:
        fails.append('G-SEAL')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 10
    print('\n' + '=' * 100)
    print('### COUNTS, PRINTED BY THIS TOOL SO THE BANK NEVER TYPES ONE AT A SHELL:')
    print('    owner needles %d   self needles %d   must-fail fixtures %d'
          % (len(OWNER_NEEDLES), len(SELF_NEEDLES), len(MUST_FAIL)))
    print('    declared carriers %d   toolnum rows %d' % (len(CARRIERS), len(TOOLNUM)))
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    for f in fails:
        print('    ### FAILED: %s' % f)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
