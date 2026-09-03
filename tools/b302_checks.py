# -*- coding: utf-8 -*-
"""b302 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM EMITTING FILES AND FROM THIS ACT'S OWN FILES.
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY, NEVER A SUBSTRING** (b277's species).

### ### **THE THREE GATES THIS ACT ADDS:**
###   ### **`G-RULING` (W1):** ### every clause of the construction the ruling was tested against is
###     pulled from the file that emitted it, and ### **THE BANK IS CHECKED FOR THE SENTENCE IT MUST
###     NOT CONTAIN** -- a claim that the sector membership was established.
###   ### **`G-STALE` (W2):** ### both statements pulled from their own acts, and the bank checked
###     for the shape that would mean it RE-DERIVED rather than CITED.
###   ### **`G-SCOPE` (W3):** ### the Lean module's own terminal names and statements are read and
###     required to mention no norm, no unit vector, no Hilbert space, no square root and no act.
###     ### **ITS ONE DECLARED EXEMPTION IS THE NAMESPACE.** ### `B302` is an act name and it
###     prefixes every terminal in the file -- as `B298`, `B270` and `B271` prefix theirs. ### That
###     is the corpus's universal convention for provenance, not a scope leak, and ### **THE CHECK
###     READS THE THEOREM'S OWN NAME AND ITS STATEMENT AND NOT THE NAMESPACE.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import hedge_audit   # noqa: E402
import ferry_scan    # noqa: E402
import banned_terms  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
MODULE = os.path.join(SIDE, 'Core', 'RationalEnclosureShadow.lean')
PROFILE = os.path.join(SIDE, 'AXIOM_PRINTS.txt')


def d(n):
    return os.path.join(D, n)


BANK = d('b302_the_unit_requirement.txt')
REG = d('b302_registration_2026-09-02.txt')
KRUN = d('b302_kernel_run.txt')
SCAN = d('b302_ferry_scan.txt')
FERRY = d('b302_ferry_2026-09-02.txt')
SPEC = d('b302_satisfiable.json')

OWNED = [BANK, REG, KRUN, SCAN, FERRY, SPEC, MODULE,
         d('b302_corr_row.txt'), d('b302_index_query.txt'),
         os.path.join(ROOT, 'tools', 'b302_kernel.py'),
         os.path.join(ROOT, 'tools', 'b302_regspec.py'),
         os.path.join(ROOT, 'tools', 'b302_correspondence.py')]
FIXTURE_CARRIERS = [os.path.join(ROOT, 'tools', 'b302_checks.py'),
                    os.path.join(ROOT, 'tools', 'b302_index_append.py')]

# ### THE CONSTRUCTION'S CLAUSES THE RULING WAS TESTED AGAINST (W1).
RULING_CLAUSES = [
    ("Def 3.3.1 -- membership, at b197's at-content grade",
     d('b226_stated_choice.txt'), "(Def 3.3.1: 'f_alpha in"),
    ("Def 3.3.1 -- the norm-sum clause",
     d('b226_stated_choice.txt'), 'SUM_v | ||f_v|| - 1 | CONVERGE'),
    ("Lemma 4.1.2 -- unit norm",
     d('b226_stated_choice.txt'), 'with ||f_a|| = 1'),
    ("Def 4.1.1 -- which sequences build the object",
     d('b226_stated_choice.txt'), 'ANY'),
    ("Def 3.3.2 -- when two choices agree",
     d('b226_stated_choice.txt'), 'EQUIVALENT'),
    ("the b225 ruling's sector wording, which A narrows",
     d('b225_serializing_close.txt'), 'with the archimedean unit from the Sonin sector'),
    ("the finite unit is in E_1 BY CONSTRUCTION -- why the ruling has no bite there",
     d('b226_stated_choice.txt'), 'IS IN E_1 **BY CONSTRUCTION**'),
]

STALE_CLAUSES = [
    ("b226's owed step, from the act that incurred it",
     d('b226_stated_choice.txt'), 'THE STEP WANTS A RESULT'),
    ("b226's standing on it",
     d('b226_stated_choice.txt'), 'THE GENERIC ODD PLACE IS *OWED*'),
    ("b268's payment, from the act that paid it",
     d('b268_generator_nonvanishing.txt'), "b226's OWED STEP IS ### PAID ###"),
    ("b268's quantifier, and it is a property of odd q",
     d('b268_generator_nonvanishing.txt'), 'FOR ODD `q`, `gcd(q+2, q^2) = 1`'),
    ("b268's bridge from support to nonvanishing",
     d('b268_generator_nonvanishing.txt'), '`support > 0` IS EXACTLY `u_p != 0`'),
    ("b268's grade, which the closed item carries",
     d('b268_generator_nonvanishing.txt'), 'DERIVES-on-IMP'),
]

OWNER_NEEDLES = RULING_CLAUSES + STALE_CLAUSES + [
    ("b301's requirement census, which this act moves (EMITTER)",
     d('b301_the_object_completed.txt'), '4 MET, 3 OPEN, 1 NOT ASKED'),
    ("b214's bench grade, which is NOT promoted (EMITTER)",
     d('b214_orientation_bits.txt'), 'GRADE **BENCH**'),
    ("the repo's own declared build environment (EMITTER)",
     os.path.join(SIDE, 'README.md'), 'sibling imports via'),
]

SELF_NEEDLES = [
    ('bank executes the ruling', BANK, '`RULE ARCH-UNIT` EXECUTES'),
    ('bank says the text makes no per-place distinction', BANK,
     'MAKES NO PER-PLACE DISTINCTION AT ALL'),
    ('bank says A narrows rather than fulfils', BANK, 'IT DOES NOT FULFIL IT'),
    ('bank retains the sector clause as description', BANK, 'stays in the record as'),
    ('bank refuses to claim the sector membership', BANK, 'IS NOT CLAIMED HERE'),
    ('bank declares the one clause held through a reader', BANK,
     'THROUGH A READER'),
    ('bank names what would overturn the execution', BANK, 'WOULD NEED REVISITING'),
    ('bank keeps the ruling inside its own scope', BANK, 'NOTHING THERE FOR THE'),
    ('bank returns SAME on the stale open', BANK, '(SAME). ### THE OPEN IS STALE AND CLOSES'),
    ('bank refuses the matching wording as evidence', BANK,
     'THAT IS EXACTLY THE EVIDENCE THAT MUST NOT BE USED'),
    ('bank cites rather than re-derives', BANK, 'CITED TO b268 AND NOT RE-DERIVED'),
    ('bank names the staleness species', BANK, 'W-ORD-DEBT-FRESHNESS'),
    ('bank owns the defect as this seat\'s', BANK, 'BOTH THIS SEAT'),
    ('bank records the index could not have answered', BANK, 'NEVER KEYED'),
    ('bank runs the scope test before the build', BANK, 'THE OBJECT IS THE MODEL'),
    ('bank reports the module built', BANK, '11 TERMINALS, ALL'),
    ('bank reports the profile counts', BANK, '438 -> 449 PRINTS'),
    ('bank reports the byte prefix', BANK, 'TRUE BYTE PREFIX'),
    ('bank declares its own kernel tool was wrong', BANK,
     'BASELINE ARM DOING PRECISELY'),
    ('bank restates the construction status', BANK, 'CONDITIONS ARE NOW THREE'),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt', BANK, 'THE SEAM\'S DEBT ITEM 1: ### STILL UNPAID'),
    ('bank states what it did not check', BANK, 'NOT CHECKED THIS ACT'),
    ('registration seals before any lean file', REG, 'SEALED BEFORE ANY `.lean` FILE EXISTS'),
    ('registration records the pre-component index queries', REG, 'generator-nonvanishing'),
    ('registration writes caps that permit the build', REG, '`.lean` FILES CREATED: CAP 1'),
    ('the kernel run reports the baseline byte-identity', KRUN, 'BYTE-IDENTICAL to banked : True'),
    ('the kernel run reports the true byte prefix', KRUN, 'TRUE BYTE PREFIX of the new one : True'),
    ('the kernel run reports no BOM', KRUN, 'BOM on the written file  : False'),
]

MUST_FAIL = [
    ('the sector membership is not claimed', BANK, 'u_inf IS IN THE SONIN SECTOR.'),
    ('the ruling is not called a derivation', BANK, 'RULE ARCH-UNIT IS DERIVED.'),
    ('Q4 is not called met', BANK, 'Q4 IS MET.'),
    ('the bank does not claim to derive b268 result', BANK, 'THIS ACT DERIVES THE NONVANISHING.'),
    ('b268 is not re-verdicted', BANK, 'b268 IS RE-VERDICTED.'),
    ('the terminal is not called evidence about a norm', BANK, 'THE TERMINAL CERTIFIES THE NORM.'),
    ('term 3 is not called constructed', BANK, 'TERM 3 IS CONSTRUCTED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the struck phrase is not used', BANK, 'HANDOFF CURRENT.'),
    ('no bench grade is promoted', BANK, 'c = +1 AT RANK 2 IS DERIVED.'),
]

TOOLNUM = [
    ("the kernel counts, the byte checks and the numstat", 'tools/b302_kernel.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b302_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b302_checks.py'),
    ("the correspondence row's number and its read-back", 'tools/b302_correspondence.py'),
    ("the index keys' read-back and must-not-hit arms", 'tools/b302_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(t for _w, t in TOOLNUM if '/b302' in t)

# ### G-SCOPE's FORBIDDEN VOCABULARY, and the ONE declared exemption (the namespace).
FORBIDDEN = re.compile(r'norm|hilbert|sqrt|sonin|archimedean|unit[ _]vector|\bc0\b|\bb\d{3}\b',
                       re.I)


def git_tracked(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', rel],
                       capture_output=True, text=True)
    return r.returncode == 0


def lean_terminals(path):
    """### RETURN `[(name, statement)]` FROM THE MODULE'S OWN SOURCE.

    ### The statement is everything between the theorem's name and its `:= by`, flattened.
    ### ### **THE NAMESPACE IS NOT INCLUDED** -- see the header's declared exemption.
    """
    src = io.open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'^theorem\s+(\w+)\s*:(.*?):=\s*(?:by)?', src, re.S | re.M):
        out.append((m.group(1), ' '.join(m.group(2).split())))
    return out


def main():
    fails = []
    print('=' * 100)
    print('b302 -- GATE SUITE')
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

    # ### G-RULING and G-STALE are the needle blocks above; their census is printed so the
    # ### falsifiers are visible as counts and not only as PASS lines.
    print('\n  G-RULING (W1) : construction clauses pulled : %d' % len(RULING_CLAUSES))
    print('  G-STALE  (W2) : statements pulled from both acts : %d' % len(STALE_CLAUSES))

    # ### ==========================================================================================
    # ### G-SCOPE (W3) -- ### **THE MODULE'S OWN TERMINALS, READ FROM ITS SOURCE.**
    # ### ==========================================================================================
    print('\n  G-SCOPE (W3: the terminal carries its own scope in its own statement):')
    terms = lean_terminals(MODULE)
    bad = []
    for name, stmt in terms:
        hit = FORBIDDEN.search(name) or FORBIDDEN.search(stmt)
        if hit:
            bad.append((name, hit.group(0)))
    print('    terminals read from the module : %d' % len(terms))
    print('    naming a norm / unit vector / Hilbert space / root / act : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ###'))
    for n, w in bad:
        print('        ### %-60s  <<%s>>' % (n, w))
    disc = bool(FORBIDDEN.search('the_norm_of_the_unit_vector'))
    quiet = not FORBIDDEN.search('explicit_numerators_over_ten_to_the_twenty')
    print('    DISCRIMINATION: fires on a forbidden name : %s ; quiet on a real one : %s'
          % (disc, quiet))
    print('    ### **DECLARED EXEMPTION: THE NAMESPACE.** ### `B302` prefixes every terminal here')
    print('    ### as `B298` prefixes b298\'s -- the corpus\'s provenance convention, not a leak.')
    if bad or not disc or not quiet:
        fails.append('G-SCOPE')

    # ### ==========================================================================================
    # ### G-KERNEL -- ### **THE PROFILE, RE-CHECKED INDEPENDENTLY OF THE BUILD TOOL.**
    # ### ==========================================================================================
    print('\n  G-KERNEL (the profile, re-checked here and not taken from the build\'s own report):')
    prof = io.open(PROFILE, 'rb').read()
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'],
                          capture_output=True).stdout
    lines = [ln for ln in prof.decode('utf-8').splitlines() if ln.strip()]
    zero = sum(1 for ln in lines if ln.rstrip().endswith('does not depend on any axioms'))
    b302 = sum(1 for ln in lines if ln.startswith("'B302."))
    bom = prof.startswith(b'\xef\xbb\xbf')
    prefix = prof.startswith(head)
    ns = subprocess.run(['git', '-C', SIDE, 'diff', '--numstat', '--', 'AXIOM_PRINTS.txt'],
                        capture_output=True, text=True).stdout.split()
    print('    prints on disk           : %d, zero-axiom %d, other %d' % (len(lines), zero,
                                                                          len(lines) - zero))
    print('    of them, this act\'s      : %d' % b302)
    print('    BOM (read as bytes)      : %s  %s' % (bom, 'PASS' if not bom else '### FAIL ###'))
    print('    HEAD is a TRUE BYTE PREFIX : %s  %s'
          % (prefix, 'PASS' if prefix else '### FAIL ###'))
    print('    git numstat on the profile : %s' % (' '.join(ns[:2]) if ns else '(clean)'))
    numstat_ok = (len(ns) >= 2 and ns[1] == '0')
    print('    deletions on the profile : %s  %s'
          % (ns[1] if len(ns) >= 2 else 'n/a', 'PASS' if numstat_ok else '### FAIL ###'))
    if bom or not prefix or (len(lines) - zero) or not numstat_ok or b302 == 0:
        fails.append('G-KERNEL')

    # ### ==========================================================================================
    # ### G-STRUCK, G-STEM, G-TOOLNUM, G-NOPAPERS.
    # ### ==========================================================================================
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
    total = 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                     struck, stem_list)
        total += len(ch)
        if ch:
            print('    ### %-42s hits : %d' % (os.path.basename(p), len(ch)))
            for h in ch:
                print('        line %d col %d  %s' % (h[1], h[2], h[0]))
    print('    files scanned %d   struck-clause hits %d  %s'
          % (len([p for p in OWNED if os.path.exists(p)]), total,
             'PASS' if not total else '### FAIL ###'))
    for p in FIXTURE_CARRIERS:
        ch, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        print('    %-44s hits : %d  ### ITS OWN FIXTURES (stated exception)'
              % (os.path.basename(p) + ' (EXCEPTION)', len(ch)))
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

    print('\n  G-STEM (every file this act wrote):')
    stem_total, swept = 0, 0
    for p in OWNED + FIXTURE_CARRIERS:
        if not os.path.exists(p):
            continue
        swept += 1
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        stem_total += len(sh)
        if sh:
            print('    ### %-40s stem hits : %d' % (os.path.basename(p), len(sh)))
            for h in sh:
                print('        line %d  %s  |  %s' % (h[1], h[0], h[3][:88]))
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    files swept %d   stem hits %d   control fires %s   %s'
          % (swept, stem_total, ctrl, 'PASS' if not stem_total and ctrl else '### FAIL ###'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    print('\n  G-TOOLNUM (ruling 3):')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-32s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-NOPAPERS (W9):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    rows = [x for x in pp.splitlines() if x.strip()]
    tracked = [x for x in rows if not x.startswith('??')]
    untracked = [x for x in rows if x.startswith('??')]
    t0 = os.path.getmtime(REG)
    newer = [x for x in untracked
             if os.path.isfile(os.path.join(PP, x[3:].strip().strip('"').replace('/', os.sep)))
             and os.path.getmtime(os.path.join(PP, x[3:].strip().strip('"').replace('/', os.sep)))
             > t0]
    print('    TRACKED files changed : %d  %s'
          % (len(tracked), 'PASS' if not tracked else '### FAIL ###'))
    print('    untracked rows (pre-existing) : %d ; written after the seal : %d  %s'
          % (len(untracked), len(newer), 'PASS' if not newer else '### FAIL ###'))
    if tracked or newer:
        fails.append('G-NOPAPERS')

    print('\n  HEDGE AUDIT:')
    for lbl, path in [('the bank', BANK), ('the registration', REG)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('        (i) %s' % s[:140])

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 6
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
