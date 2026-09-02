# -*- coding: utf-8 -*-
"""b299 -- THE GATE SUITE.

### NEEDLES ARE PULLED FROM EMITTING FILES AND FROM THIS ACT'S OWN FILES.
### ### **EVERY MUST-FAIL FIXTURE ASSERTS WHOLE-LINE EQUALITY VIA `absent_exact`, NEVER A
### SUBSTRING** -- the b277 inverted-fixture species, closed at b278 and re-gated here.

### ### **THE GATE THIS ACT ADDS IS `G-STRUCK`, AND IT IS RUN INDEPENDENTLY OF THE GENERATOR.**
### The generator checked the document IT WAS ABOUT TO WRITE; this suite scans ### **THE FILE ON
### DISK, THE BANK, THE RUN LOG AND THE APPENDED POINTER TEXT** ### -- because a gate that only
### ever reads the generator's in-memory string cannot see what actually landed. ### That is the
### b183 species (a check whose scope excludes the defect) and this act will not repeat it inside
### the very tool built against it.

### ### **AND THE BANK IS SCANNED TOO, WHICH IS THE ORDER'S OWN WORDING: ### the struck clause
### ### applied NOWHERE -- not in the title, not in the document, ### NOT IN THE BANK.**
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import hedge_audit   # noqa: E402
import ferry_scan    # noqa: E402
import b299_keystone as KS  # noqa: E402  ### the pointer text is IMPORTED, never retyped

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'

BANK = os.path.join(D, 'b299_the_arc_keystone.txt')
REG = os.path.join(D, 'b299_registration_2026-09-02.txt')
RECORD = os.path.join(D, 'STRUCK_CLAUSES.md')
FERRY = os.path.join(D, 'b299_ferry_2026-09-02.txt')
SCANOUT = os.path.join(D, 'b299_ferry_scan.txt')
RUNLOG = os.path.join(D, 'b299_keystone_run.txt')
DOC = KS.DOC
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNER_NEEDLES = [
    ("the author's strike, from the ferry as pasted (EMITTER)",
     FERRY, 'never claimed properties'),
    ("the surviving half, from the ferry as pasted (EMITTER)",
     FERRY, 'numeral is itself the finding'),
    ("b293's family, by its own name (EMITTER)",
     os.path.join(D, 'b293_the_finite_family.txt'), 'THE FAMILY IS CONSTRUCTED.'),
    ("b295's criterion (EMITTER)",
     os.path.join(D, 'b295_the_second_mechanism.txt'), '`a >= 0`  ###  OR  ###  `b >= n - 1`'),
    ("b296's equivalence (EMITTER)",
     os.path.join(D, 'b296_the_asymmetry.txt'), 'IF AND ONLY IF'),
    ("b298's terminal, by name (EMITTER)",
     os.path.join(D, 'b298_the_boundary_terminal.txt'),
     'boundary_value_at_cell_2_2_on_member_radii_neg1_0'),
    ("the deposit's ceiling, from README.md (EMITTER)",
     os.path.join(PP, 'README.md'), 'Not supportable: *RH proved.*'),
    ("the voices ruling, from its own file (EMITTER)",
     os.path.join(PP, 'phase2', 'method', 'SIGN_ARRANGEMENT_RECONCILIATION.md'),
     'frozen, errata-only'),
    ("the corpus still carries the struck clause at F.2026-07-29 (EMITTER, FILED NOT EDITED)",
     os.path.join(PP, 'FINDINGS.md'), 'Title law extended'),
    ("the surviving half has its own site in REGISTRY (EMITTER)",
     os.path.join(PP, 'REGISTRY.md'), 'numeral-title law'),
]

SELF_NEEDLES = [
    ('bank names the strike and its record', BANK, '`data/STRUCK_CLAUSES.md`, MINTED THIS ACT'),
    ('bank says only the numeral half stands', BANK, 'ONLY THE NUMERAL HALF STANDS'),
    ('bank declares the conflict with the seal', BANK, 'THE SEAL IS NOT EDITED'),
    ('bank states the ruling wins over the wording', BANK,
     "THE DOCUMENT FOLLOWS THE AUTHOR'S RULING OVER THE REGISTRATION'S WORDING"),
    ('bank names all three sites the clause was applied at', BANK,
     'THE THREE SITES THE FIRST PASS APPLIED IT AT'),
    ('bank reports the ferry scan with both arms', BANK, '2 STRUCK-CLAUSE HITS'),
    ('bank says a hit is not a fault', BANK, 'A HIT IS A STRING, NOT A FAULT'),
    ('bank lists the unconfirmed candidates and promotes none', BANK, 'NONE PROMOTED'),
    ('bank declares the line-scoping defect', BANK, 'REPORTS A HIT BY LUCK'),
    ('bank declares the idempotence trap', BANK, 'WOULD HAVE DEFEATED THE ORDER TO REGENERATE'),
    ('bank declares its own banned-stem slip', BANK, 'WROTE A BANNED STEM INTO ITS OWN NEW TOOL'),
    ('bank names the untracked files it did not stage', BANK, 'LEFT EXACTLY WHERE THEY SIT'),
    ('bank keeps M-2 unchanged', BANK, 'M-2 REMAINS (SPECIFIED-NOT-STATED). ### UNCHANGED'),
    ('bank restates print coverage with its count', BANK, '25 STILL OUTSIDE'),
    ('bank files the install work-order as the author\'s', BANK, 'W-ORD-FERRY-SCAN-INSTALL'),
    ('record carries the strike verbatim', RECORD, 'is STRUCK; only the numeral half stands'),
    ('record refuses to promote a candidate', RECORD,
     "author's word and cannot happen by a tool"),
    ('record files the sites without editing them', RECORD, 'FILED AND NOT EDITED'),
    ('scan output reports both arms', SCANOUT, 'BANNED/RETIRED-STEM HITS'),
    ('run log shows Q-STRUCK with its arm', RUNLOG, 'DISCRIMINATION ARM: a text carrying'),
    ('registration fixed the clause before the seal', REG, 'THE TITLE OBEYS THE TITLE LAW'),
    ('the document states grades and confers none', DOC, 'states grades and confers'),
    ('the correspondence row says it has no terminal', TABLE, 'NO TERMINAL. THIS ROW IS A DOCUMENT'),
]

MUST_FAIL = [
    ('the struck clause is not asserted of the title in the bank', BANK,
     "This document's title names its objects and its conditions and claims no achieved property."),
    ('the seal is not called amended', BANK, 'THE REGISTRATION IS RE-SEALED.'),
    ('no candidate is promoted', BANK, 'U-1 IS STRUCK.'),
    ('no route is claimed', BANK, 'THE DOCUMENT IS A ROUTE.'),
    ('no aggregation is stated', BANK, 'THE AGGREGATION IS STATED.'),
    ('M-2 is not advanced', BANK, 'M-2 IS STATED.'),
    ('no act is re-verdicted', BANK, 'b298 IS RE-VERDICTED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('the document claims no achieved property about itself', DOC,
     'This document claims an achieved property.'),
]


def main():
    fails = []
    print('=' * 100)
    print('b299 -- GATE SUITE')
    print('=' * 100)

    print('\n  OWNER NEEDLES (pulled from emitting files):')
    unpullable = 0
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
    # ### G-STRUCK -- ### **THE FILES AS THEY LANDED, NOT THE GENERATOR'S IN-MEMORY STRING.**
    # ### ==========================================================================================
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK (independent re-scan of what LANDED; record: %d struck, %d unconfirmed'
          ' not loaded):' % (len(struck), unconf))
    targets = [('the document ON DISK', io.open(DOC, encoding='utf-8').read()),
               ('the bank ON DISK', io.open(BANK, encoding='utf-8').read()),
               ('the run log', io.open(RUNLOG, encoding='utf-8').read()),
               ('the title', KS.TITLE),
               ('pointer -> THE_GLOBAL_SECTION.md', KS.POINTER_GLOBAL),
               ('pointer -> THE_IDENTITY_CHAIN.md', KS.POINTER_CHAIN)]
    total = 0
    for lbl, text in targets:
        ch, _sh = ferry_scan.scan_text(text, struck, stem_list)
        total += len(ch)
        print('    %-34s struck-clause hits : %d  %s'
              % (lbl, len(ch), 'PASS' if not ch else '### FAIL ###'))
        for h in ch:
            print('        line %d col %d  %s' % (h[1], h[2], h[0]))
    disc = bool(ferry_scan.scan_text(
        'a title must name its objects and conditions, not claim an achieved property',
        struck, stem_list)[0])
    print('    DISCRIMINATION ARM: a text carrying the clause comes back hit : %s  %s'
          % (disc, 'PASS' if disc else '### FAIL ###'))
    print('    ### THE RECORD ITSELF IS NOT SCANNED -- it carries the clause BY DESIGN, which is')
    print('    ### how the check knows what to look for. Scanning it would be scanning the rule.')
    if total or not disc:
        fails.append('G-STRUCK')

    # ### ==========================================================================================
    # ### G-STEM -- ### **THE RETIRED STEM OVER THIS ACT'S OWN FILES.**
    # ### ==========================================================================================
    # ### `stem_sweep.py` sweeps a FIXED act range (b268-b279) and cannot see b299; `banned_terms`
    # ### owns `gap`/`blind` over the act's diff but not the RETIRED phrase. ### **THE ARM THAT
    # ### COVERS BOTH IS `ferry_scan.stems()`, WHICH READS BOTH LISTS FROM THE TOOLS THAT OWN
    # ### THEM** -- so this is a third reader of one source, never a third copy.
    print('\n  G-STEM (banned + retired stems over this act\'s own files, read from their tools):')
    stem_files = [BANK, RECORD, FERRY, SCANOUT, RUNLOG,
                  os.path.join(ROOT, 'tools', 'ferry_scan.py'),
                  os.path.join(ROOT, 'tools', 'b299_keystone.py'),
                  os.path.join(ROOT, 'tools', 'b299_correspondence.py'),
                  DOC]
    stem_total = 0
    for p in stem_files:
        _c, sh = ferry_scan.scan_text(io.open(p, encoding='utf-8', errors='replace').read(),
                                      [], stem_list)
        stem_total += len(sh)
        if sh:
            print('    ### %-40s stem hits : %d' % (os.path.basename(p), len(sh)))
            for h in sh:
                print('        line %d  %s' % (h[1], h[0]))
    print('    files swept %d   stem hits %d  %s'
          % (len(stem_files), stem_total, 'PASS' if not stem_total else '### FAIL ###'))
    print('    ### CONTROL, SO A ZERO IS NOT A DEAD SCANNER: the stem arm fires on a synthetic')
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % __import__('banned_terms').STEMS[0],
                                     [], stem_list)[1])
    print('    ### line built from the loaded list : %s  %s' % (ctrl, 'PASS' if ctrl else '### FAIL'))
    if stem_total or not ctrl:
        fails.append('G-STEM')

    # ### THE ONE NUMBER THE ORDER NAMES: the keystone appends must be purely additive, measured
    # ### here a SECOND TIME and from git rather than from the generator's own report.
    # ### DEFECT FIXED IN THIS SUITE'S OWN CLOSING RUN (b299). ### The first version measured
    # ### `diff HEAD` only. ### **ONCE THE COMMIT LANDS, THAT DIFF IS EMPTY AND THE GATE PRINTED
    # ### `+0 / -0  PASS -- originals untouched`** -- a verdict over an empty scope, which is
    # ### b167's law and the exact shape this record has had to write a line against four times.
    # ### ### **A GATE THAT PASSES BOTH BEFORE AND AFTER THE THING IT CHECKS IS NOT CHECKING IT.**
    # ### It now measures the WORKING TREE while the change is uncommitted and ### THE COMMIT
    # ### ITSELF ### once it is, says which of the two it read, and ### **HARD-FAILS ON AN EMPTY
    # ### SCOPE RATHER THAN PASSING IT.**
    import subprocess
    dirty = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD'],
                           capture_output=True, text=True).stdout.strip()
    rng = ['HEAD'] if dirty else ['HEAD~1', 'HEAD']
    src = 'the WORKING TREE vs HEAD' if dirty else 'THE COMMIT ITSELF (HEAD~1..HEAD)'
    print('\n  G-ADDITIVE (measured from git, independently of the generator):')
    print('    scope read : %s' % src)
    tot_a = tot_d = 0
    for rel in ['phase2/method/THE_GLOBAL_SECTION.md', 'phase2/method/THE_IDENTITY_CHAIN.md']:
        p = subprocess.run(['git', '-C', PP, 'diff', '--numstat'] + rng + ['--', rel],
                           capture_output=True, text=True)
        parts = p.stdout.split()
        a, d = (int(parts[0]), int(parts[1])) if parts else (0, 0)
        tot_a += a
        tot_d += d
        print('    %-44s +%d / -%d' % (rel, a, d))
    empty = (tot_a == 0 and tot_d == 0)
    print('    TOTAL +%d / -%d  %s'
          % (tot_a, tot_d,
             '### FAIL -- EMPTY SCOPE, NOT A PASS' if empty else
             ('PASS -- originals untouched' if tot_d == 0 else '### FAIL -- lines were deleted')))
    if tot_d != 0 or empty:
        fails.append('G-ADDITIVE')

    # ### HEDGE AUDIT OVER EVERY FILE THIS ACT WROTE, ### **INCLUDING THE EMITTED DOCUMENT.**
    print('\n  HEDGE AUDIT (every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the emitted document', DOC),
                      ('the struck-clause record', RECORD)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-28s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        if gh:
            fails.append('graded hedges in %s' % lbl)
            for s in gh:
                print('        (i) a graded sentence also hedges: %d characters, described'
                      ' not quoted' % len(s))

    ngates = len(OWNER_NEEDLES) + len(SELF_NEEDLES) + len(MUST_FAIL) + 3
    print('\n' + '=' * 100)
    print('### GATES: %d PASS / %d FAIL / 0 ERROR / 0 REFUSED   (unpullable: %d)'
          % (ngates - len(fails), len(fails), unpullable))
    print('=' * 100)
    return 1 if fails else 0


if __name__ == '__main__':
    sys.exit(main())
