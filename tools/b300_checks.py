# -*- coding: utf-8 -*-
"""b300 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM EMITTING FILES AND FROM THIS ACT'S OWN FILES.
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated at b299.

### ### **THE GATE THIS ACT ADDS IS `G-MEMBER`, AND IT IS THE ONE THE FERRY'S FALSIFIER NAMES.**
### T1 says membership is decided against BOTH of Definition 4.4's conditions, each by a quotation
### from an emitting file or an elementary identity whose hypothesis is quoted. ### **SO THE GATE
### PULLS EVERY INPUT OF THE CHAIN FROM THE FILE THAT EMITTED IT, AND CARRIES A DISCRIMINATION ARM
### SO A CHAIN THAT PULLS EVERYTHING IS NOT MISTAKEN FOR A CHAIN THAT CHECKS ANYTHING.**
### ### **WHAT IT CANNOT DO, SAID HERE RATHER THAN DISCOVERED LATER: ### IT CANNOT CHECK THAT THE
### ### QUOTED SENTENCES ENTAIL THE CONCLUSION.** ### That is the bank's prose and a reader's job.
### The gate closes the typo class and the missing-owner class, and those only.
"""
import io
import os
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


def d(n):
    return os.path.join(D, n)


BANK = d('b300_the_archimedean_leg.txt')
REG = d('b300_registration_2026-09-02.txt')
SRC = d('b300_source_read.txt')
E0 = d('b300_e0_gate.txt')
RECORD = d('STRUCK_CLAUSES.md')
SCAN0 = d('b300_ferry_scan.txt')
SCAN1 = d('b300_ferry_scan_after.txt')
SPEC = d('b300_satisfiable.json')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

# ### **THE SCOPE IS EVERY FILE THIS ACT WROTE, AND IT WAS NOT, AND THAT IS b183's SPECIES.**
# ### The first version of this list held the bank, the registration, the reads and three tools --
# ### and OMITTED `b300_roster_add.py` and `b300_index_append.py`, which this act also wrote.
# ### ### **A BANNED STEM SHIPPED IN ONE OF THEM AND `G-STEM` REPORTED A CLEAN SWEEP**, because
# ### the file was not in the sweep. ### The stand-alone `banned_terms.py --new` run over the
# ### act's files is what caught it. ### **A CHECK WHOSE SCOPE EXCLUDES THE DEFECT IS NOT A
# ### CHECK, AND THE FIX IS THE SCOPE AND NOT THE WORD** -- though the word was corrected too.
OWNED = [BANK, REG, SRC, E0, SCAN0, SCAN1, SPEC, d('b300_ferry_2026-09-02.txt'),
         d('b300_roster.txt'), d('b300_index_query.txt'), d('b300_corr_row.txt'),
         d('b300_mirror_verify.txt'), d('b300_pins.txt'),
         os.path.join(ROOT, 'tools', 'e16', 'b300_the_space.py'),
         os.path.join(ROOT, 'tools', 'b300_correspondence.py'),
         os.path.join(ROOT, 'tools', 'b300_roster_add.py'),
         os.path.join(ROOT, 'tools', 'b300_index_append.py'),
         os.path.join(ROOT, 'tools', 'mirror_roster.json')]

# ### THE FIXTURE-CARRYING TOOLS. ### **THEY CARRY STRUCK CLAUSES ON PURPOSE, BECAUSE A CHECK'S
# ### POSITIVE FIXTURE ### IS ### THE CLAUSE.** ### `ferry_scan.py` and `b299_checks.py` already
# ### have this property and it is not new with this act. ### **THEY ARE SCANNED AND REPORTED
# ### SEPARATELY, NEVER EXCLUDED FROM THE SWEEP AND THEN FORGOTTEN**, and the precedent is
# ### checked rather than asserted.
FIXTURE_CARRIERS = [os.path.join(ROOT, 'tools', 'b300_regspec.py'),
                    os.path.join(ROOT, 'tools', 'b300_checks.py')]
PRECEDENTS = [os.path.join(ROOT, 'tools', 'ferry_scan.py'),
              os.path.join(ROOT, 'tools', 'b299_checks.py')]

# ### =============================================================================================
# ### THE MEMBERSHIP CHAIN. ### **EVERY INPUT, WITH THE FILE THAT EMITTED IT.**
# ### (step, role, emitting file, anchor)
# ### =============================================================================================
MEMBER_CHAIN = [
    ("THE UNIT", "the corpus's chosen archimedean unit, from where the choice was made",
     d('b226_stated_choice.txt'), 'rank-2 Sonin-sector eigenfunction'),
    ("THE UNIT'S MEASURED DESCRIPTION", "its eigenvalue and its grade",
     d('b214_orientation_bits.txt'), 'EVEN (rank 2, mu = -20.48057322913694697'),
    ("THE EIGENVALUE'S SIGN", "that rank 2 is the first even NEGATIVE eigenvalue, measured",
     d('b212_odd_family.txt'), 'First even negative eigenvalue'),
    ("THE AMBIENT -- EVENNESS", "CM Lemma 3.1: the unique EVEN solution",
     d('b202_sum_test.txt'), 'which is zero on [-1,1] and agrees with'),
    ("THE AMBIENT -- L^2", "the residue: the leading term is given only as PROPORTIONAL TO",
     d('b202_sum_test.txt'), 'PROPORTIONAL TO'),
    ("CONDITION ONE", "CM Lemma 3.1: phi_mu vanishes on [-1,1]",
     d('b202_sum_test.txt'), 'even and VANISHES ON [-1,1]'),
    ("CONDITION TWO, STEP 1 -- THE EIGENRELATION", "b211 (C3), DERIVES on I8 + I6 + I10",
     d('b211_alternation_derived.txt'), 'F phi_mu = c phi_mu for'),
    ("CONDITION TWO, STEP 1 -- I8", "CM Thm 2.6(i): W_sa commutes with the Fourier transform",
     d('b211_alternation_derived.txt'), 'commutes with the Fourier transform'),
    ("CONDITION TWO, STEP 1 -- I6", "RRT Lemma 2(ii): the eigenspace is one-dimensional",
     d('b211_alternation_derived.txt'), 'the dimension of the eigenspace E_mu is one'),
    ("THE DEFINITION MEMBERSHIP IS TESTED AGAINST", "CC Definition 4.4, equation (72)",
     d('b287_the_two_papers.txt'), 'S(lambda,mu) subset L^2(R)_ev'),
    ("SCALAR-INVARIANCE OF MEMBERSHIP", "b292 (2c), derived there in both directions",
     d('b292_the_identification.txt'), 'IF AND ONLY IF `cv` IS'),
    ("(a) -- WHAT THE SECTOR NAME MEANS", "b206's adopted name, from the file that adopted it",
     d('b206_variable_passage.txt'), '+1 eigenspace of F on the archimedean Sonin space'),
    ("(a) -- BOTH VALUES OF c OCCUR", "b211 (C3), DERIVES: the containment is PROPER",
     d('b211_alternation_derived.txt'), 'BOTH VALUES OF c OCCUR'),
    ("(a) -- THE MEMBERSHIP OF THE c = -1 WITNESS", "CM Cor 3.2, b211's I9",
     d('b202_sum_test.txt'), 'assume mu is a negative eigenvalue'),
    ("(2d) ROUTE ONE -- THE REFUTATION", "b291: psi_n fails Sonin's second condition",
     d('b291_the_involution.txt'), 'P1 F_eR psi_n = (1 - lambda(n)^2) xi_n'),
    ("(2d) ROUTE TWO -- THE ORTHOGONALITY STATEMENT", "CC, via b287's at-content read",
     d('b287_the_two_papers.txt'), 'orthogonal to `S(1,1)` and so are'),
    ("(2d) -- THE SOURCES' OWN SEPARATION", "b287's standing citation hazard",
     d('b287_the_two_papers.txt'), 'FOR THE PROLATE MATERIAL'),
    ("R1 -- THE PRODUCT CONSTRUCTION'S FIRST REQUIREMENT", "von Neumann Def 4.1.1, via b226",
     d('b226_stated_choice.txt'), 'H_a be the closed'),
    ("R2 -- ITS SECOND", "von Neumann Lemma 4.1.2, via b226",
     d('b226_stated_choice.txt'), 'with ||f_a|| = 1'),
    ("WHAT IS NOT UNBLOCKED", "b221: the halt is at the finite places",
     d('b221_cell_level_assembly.txt'), 'the halt is at the FINITE places, not at infinity'),
    ("WHAT IS STILL OWED", "b226's G-SECTOR at the generic odd finite place",
     d('b226_stated_choice.txt'), 'THE GENERIC ODD PLACE IS *OWED*'),
    ("THE CORROBORATION, AT ITS OWN GRADE", "b214's G-SONIN, quoted and not computed from",
     d('b214_orientation_bits.txt'), '8.4e-15'),
]

OWNER_NEEDLES = [
    ("N-OPEN-B in its owner's own words (EMITTER)",
     d('b285_archimedean_opening.txt'), 'the real-fiber measure/normalization'),
    ("b287's picture residue, which (16) discharges on one arm (EMITTER)",
     d('b292_the_identification.txt'), 'NO OWNER STATES THE IDENTIFICATION OF THE TWO PICTURES'),
    ("the source's size statement (EMITTER)",
     d('b286_the_cc_condition.txt'), 'infinite dimensional Sonin'),
    ("the projection that makes the space closed (EMITTER)",
     d('b287_the_two_papers.txt'), 'orthogonal projection on Sonin'),
    ("the involutivity sentence (EMITTER)",
     d('b291_the_involution.txt'), 'is its own inverse'),
    ("F_eR phi_mu = xi_mu, the source's own relation (EMITTER)",
     d('b202_sum_test.txt'), 'F_eR phi_mu = xi_mu'),
    ("the sector-name's provenance, which travels with it (EMITTER)",
     d('b226_stated_choice.txt'), 'CONVERSATION LAYER, 2026-08-27'),
    ("W-ORD-WSA-PSI-LINK's grade (EMITTER)",
     d('b287_the_two_papers.txt'), 'TRUSTED-AT-CITE'),
]

SELF_NEEDLES = [
    ('bank returns (IN, DERIVED)', BANK, '(IN, DERIVED)'),
    ('bank returns DIFFERENT on (a)', BANK, 'DIFFERENT, DERIVED'),
    ('bank returns the space CONSTRUCTED CONDITIONALLY', BANK, 'CONSTRUCTED, CONDITIONALLY'),
    ('bank says the sign of c is never used', BANK, 'THE SIGN OF `c` IS NEVER USED'),
    ('bank says the derivation needs neither the import nor the link', BANK,
     'NEEDS NEITHER CM COROLLARY 3.2'),
    ('bank refuses the sector-name route', BANK, 'IT IS NOT TAKEN'),
    ('bank names the ambient residue', BANK, 'W-ORD-PHI-MU-L2'),
    ('bank splits N-OPEN-B rather than closing it', BANK, 'STILL OPEN (C9)'),
    ('bank discharges the picture residue on one arm only', BANK,
     'DISCHARGED ON THE ADDITIVE ARM'),
    ('bank explains the second zero rather than displaying it', BANK,
     'A ZERO THAT IS EXPLAINED IS EVIDENCE'),
    ('bank declares the under-report the record caught', BANK, 'PREDICTED TERMINAL'),
    ('bank declares its own gate scope hole', BANK, "OWN `G-STEM` HAD A SCOPE HOLE"),
    ('bank keeps M-2 unchanged', BANK, '`M-2` REMAINS `(SPECIFIED-NOT-STATED)`'),
    ('bank restates the seam debt unpaid', BANK, 'THE SEAM\'S DEBT ITEM 1: ### STILL UNPAID'),
    ('bank states what it did not check, per ruling (2)', BANK, 'NOT CHECKED THIS ACT'),
    ('bank says the halt is not moved', BANK, 'IT DOES NOT UNBLOCK TERM 3'),
    ('bank separates the unit from the instruments', BANK, 'THEY ARE ### DIFFERENT VECTORS'),
    ('source read carries (16) verbatim', SRC, 'We normalize the inner product'),
    ('source read states the transmission', SRC, 'THE PUBLIC arXiv IDENTIFIER ONLY'),
    ('source read records what the route did NOT reach', SRC, 'WHAT IT DID NOT REACH'),
    ('registration carries the membership falsifier', REG, 'T1 -- THE MEMBERSHIP FALSIFIER'),
    ('registration records the seats disagreeing', REG, 'THE SEATS DO NOT AGREE'),
    ('registration records the index query result', REG, '--query archimedean-leg'),
    ('record carries the author\'s U-1 wording verbatim', RECORD,
     'a predicted count creates pressure to hit it'),
    ('record carries the author\'s U-2 condition', RECORD,
     'the act states what it wrote and what it did not check'),
    ('record reports the empty candidate list rather than dropping it', RECORD,
     'THE LIST IS EMPTY AT b300'),
    ('record files U-1\'s site as found by the check', RECORD, 'PREDICTED TERMINAL COUNT'),
    ('E0 output reports the census', E0, 'SUPPLIED            : 8'),
    ('scan run one is on the record as b299 left it', SCAN0, 'struck entries loaded         : 1'),
    ('scan run two is on the updated record', SCAN1, 'struck entries loaded         : 3'),
]

MUST_FAIL = [
    ('the space is not called unconditionally constructed', BANK,
     'VERDICT ON THE SPACE: (CONSTRUCTED).'),
    ('N-OPEN-B is not closed', BANK, 'N-OPEN-B IS CLOSED.'),
    ('sector membership is not claimed', BANK, 'THE SECTOR MEMBERSHIP IS DERIVED.'),
    ('the unit is not identified with the prolate vector', BANK,
     'THE CHOSEN UNIT IS THE CORPUS PROLATE VECTOR.'),
    ('no act is re-verdicted', BANK, 'b292 IS RE-VERDICTED.'),
    ('term 3 is not unblocked', BANK, 'TERM 3 IS UNBLOCKED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the struck phrase is not used in the closing', BANK, 'HANDOFF CURRENT.'),
    ('no unit is proposed', BANK, 'THIS SEAT PROPOSES A UNIT.'),
]

# ### THE NUMBERS THIS ACT REPORTS, EACH WITH THE COMMITTED TOOL THAT PRODUCED IT (ruling 3).
# ### **THE LIMIT: ### IT CHECKS THAT A TOOL EXISTS AND IS TRACKED BY GIT, NOT THAT THE NUMBER
# ### CAME OUT OF IT.** ### A number typed into the bank beside a real tool's name passes here.
# ### The cap this enforces is on ORPHAN numbers -- ones with no committed producer at all.
NEW_THIS_ACT = ('tools/e16/b300_the_space.py', 'tools/b300_regspec.py',
                'tools/b300_checks.py', 'tools/b300_correspondence.py')

TOOLNUM = [
    ("the E0 census (constituents, supplied, open, unpullable)", 'tools/e16/b300_the_space.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b300_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("both ferry scans' entry/pattern/hit counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate counts, needle counts and hedge counts", 'tools/b300_checks.py'),
    ("the correspondence row's number and its read-back", 'tools/b300_correspondence.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]


def git_tracked(repo, relpath):
    p = subprocess.run(['git', '-C', repo, 'ls-files', '--error-unmatch', relpath],
                       capture_output=True, text=True)
    return p.returncode == 0


def main():
    fails = []
    print('=' * 100)
    print('b300 -- GATE SUITE')
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
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s' % lbl)

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    # ### ==========================================================================================
    # ### G-MEMBER -- ### **EVERY INPUT OF THE MEMBERSHIP CHAIN, FROM THE FILE THAT EMITTED IT.**
    # ### ==========================================================================================
    print('\n  G-MEMBER (T1: both conditions, each input pulled from its emitting file):')
    bad = 0
    for step, role, path, anchor in MEMBER_CHAIN:
        try:
            needle_pull.pull(path, anchor)
            mark = 'PULLED'
        except LookupError:
            mark, bad = '### UNPULLABLE ###', bad + 1
        print('    %-8s %-46s %s' % (mark, step[:46], os.path.basename(path)))
        if mark != 'PULLED':
            print('             role: %s   anchor: %r' % (role, anchor))
    # ### THE DISCRIMINATION ARM, BUILT BY MUTATING EACH REAL ANCHOR RATHER THAN INVENTING ONE.
    slipped = 0
    for _s, _r, path, anchor in MEMBER_CHAIN:
        try:
            needle_pull.pull(path, anchor[:-1] + 'Z~')
            slipped += 1
        except LookupError:
            pass
    print('    chain inputs %d   unpullable %d   mutated-anchor slips %d   %s'
          % (len(MEMBER_CHAIN), bad, slipped,
             'PASS' if not bad and not slipped else '### FAIL ###'))
    print('    ### **THE GATE CLOSES THE TYPO CLASS AND THE MISSING-OWNER CLASS. ### IT CANNOT')
    print('    ### CHECK THAT THE QUOTED SENTENCES ENTAIL THE CONCLUSION.**')
    if bad or slipped:
        fails.append('G-MEMBER')

    # ### ==========================================================================================
    # ### G-STRUCK -- ### **THE FILES AS THEY LANDED, AGAINST THE UPDATED RECORD.**
    # ### ==========================================================================================
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (record: %d struck entries, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(e['patterns']) for e in struck), unconf))
    total = 0
    for p in OWNED:
        ch, _sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                       struck, stem_list)
        total += len(ch)
        print('    %-44s struck-clause hits : %d  %s'
              % (os.path.basename(p), len(ch), 'PASS' if not ch else '### FAIL ###'))
        for h in ch:
            print('        line %d col %d  %s' % (h[1], h[2], h[0]))
    # ### THE STATED EXCEPTION. ### `b300_regspec.py` CARRIES U-1 IN ITS OWN POSITIVE FIXTURES,
    # ### exactly as `ferry_scan.py` and `b299_checks.py` carry S-1 in theirs. ### **IT IS SCANNED
    # ### AND REPORTED, NOT EXCLUDED FROM THE SWEEP AND THEN FORGOTTEN.**
    ncar = 0
    for p in FIXTURE_CARRIERS:
        c, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        ncar += len(c)
        print('    %-44s struck-clause hits : %d  ### ITS OWN POSITIVE FIXTURES'
              % (os.path.basename(p) + ' (EXCEPTION, STATED)', len(c)))
    nprec = 0
    for p in PRECEDENTS:
        c, _ = ferry_scan.scan_text(io.open(p, encoding='utf-8').read(), struck, stem_list)
        nprec += len(c)
        print('    %-44s struck-clause hits : %d  ### SAME SHAPE, NOT NEW WITH THIS ACT'
              % (os.path.basename(p) + ' (precedent)', len(c)))
    prec = ncar > 0 and nprec > 0
    print('    the exception has a precedent in the tool that owns the check : %s  %s'
          % (prec, 'PASS' if prec else '### FAIL -- then it is not an exception, it is a defect'))
    # ### THE DISCRIMINATION ARM, ONE PER STRUCK ENTRY, SO A ZERO IS A FINDING.
    probes = [('S-1', 'a title must name its objects and conditions, not claim an achieved '
                      'property'),
              ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
              ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
    fired = 0
    for eid, text in probes:
        hit = bool(ferry_scan.scan_text(text, struck, stem_list)[0])
        fired += 1 if hit else 0
        print('    DISCRIMINATION %-4s a text carrying the clause comes back hit : %s  %s'
              % (eid, hit, 'PASS' if hit else '### FAIL ###'))
    if total or fired != len(probes) or not prec:
        fails.append('G-STRUCK')

    # ### ==========================================================================================
    # ### G-STEM -- ### **BANNED AND RETIRED STEMS OVER THIS ACT'S OWN FILES.**
    # ### ==========================================================================================
    print('\n  G-STEM (banned + retired stems, read from the tools that own them):')
    stem_total = 0
    for p in OWNED + FIXTURE_CARRIERS + [RECORD]:
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
          % (len(OWNED) + len(FIXTURE_CARRIERS) + 1, stem_total, ctrl,
             'PASS' if not stem_total and ctrl else '### FAIL ###'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    # ### ==========================================================================================
    # ### G-TOOLNUM, G-NODEPOSIT, G-NOPAPERS, G-SHADOW -- ### **THE FOUR PLANNED ZEROS, RE-MEASURED
    # ### AGAINST WHAT LANDED RATHER THAN AGAINST WHAT WAS PLANNED.**
    # ### ==========================================================================================
    print('\n  G-TOOLNUM (ruling 3: every reported number has a committed producer):')
    orphan = 0
    for what, tool in TOOLNUM:
        exists = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tracked = git_tracked(ROOT, tool)
        ok = exists and (tracked or tool in NEW_THIS_ACT)
        orphan += 0 if ok else 1
        print('    %-58s %-34s exists=%s tracked=%s' % (what[:58], tool, exists, tracked))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    print('    ### **THE LIMIT: IT CHECKS A PRODUCER EXISTS, NOT THAT THE NUMBER CAME OUT OF IT.**')
    print('    ### A number typed beside a real tool\'s name passes here. ### The cap it enforces')
    print('    ### is on ORPHAN numbers -- ones with no committed producer at all.')
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  G-NOPAPERS / G-NODEPOSIT (PLACE-papers read only; nothing deposits):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    rows = [x for x in pp.splitlines() if x.strip()]
    tracked_changes = [x for x in rows if not x.startswith('??')]
    untracked = [x for x in rows if x.startswith('??')]
    print('    PLACE-papers TRACKED files changed by anyone : %d  %s'
          % (len(tracked_changes), 'PASS' if not tracked_changes else '### FAIL ###'))
    for x in tracked_changes[:10]:
        print('        %s' % x)
    # ### THE UNTRACKED ROWS ARE REPORTED, NOT SWALLOWED -- ### **AND THE CLAIM THAT THEY ARE NOT
    # ### THIS ACT'S IS MEASURED AGAINST THE SEAL'S OWN mtime, NOT ASSERTED.** ### b299 met the
    # ### same rows and left them exactly where they sit; this gate says WHY it may.
    t0 = os.path.getmtime(REG)
    newer = []
    for x in untracked:
        rel = x[3:].strip().strip('"')
        f = os.path.join(PP, rel.replace('/', os.sep))
        if os.path.exists(f) and os.path.getmtime(f) > t0:
            newer.append(rel)
        elif os.path.isdir(f):
            for root, _dd, ff in os.walk(f):
                for nm in ff:
                    if os.path.getmtime(os.path.join(root, nm)) > t0:
                        newer.append(os.path.join(root, nm))
    print('    PLACE-papers untracked rows (PRE-EXISTING, left where they sit) : %d'
          % len(untracked))
    for x in untracked[:10]:
        print('        %s' % x)
    print('    of those, WRITTEN AFTER THIS ACT REGISTRATION WAS SEALED : %d  %s'
          % (len(newer), 'PASS' if not newer else '### FAIL ###'))
    for x in newer[:10]:
        print('        ### %s' % x)
    if tracked_changes or newer:
        fails.append('G-NOPAPERS')

    print('\n  G-SHADOW (T8: nothing built -- measured, not asserted):')
    sd = subprocess.run(['git', '-C', SIDE, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    lean = [x for x in sd.splitlines() if x.strip().endswith('.lean')]
    print('    `.lean` files moved in the kernel repo : %d  %s'
          % (len(lean), 'PASS' if not lean else '### FAIL ###'))
    for x in lean[:10]:
        print('        %s' % x)
    if lean:
        fails.append('G-SHADOW')

    # ### ==========================================================================================
    # ### THE HEDGE AUDIT, OVER EVERY FILE THIS ACT WROTE IN PROSE.
    # ### ==========================================================================================
    print('\n  HEDGE AUDIT (every prose file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG),
                      ('the source read', SRC), ('the struck-clause record', RECORD)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('        (i) a graded sentence also hedges: %d characters' % len(s))

    ngates = (len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 7)
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
