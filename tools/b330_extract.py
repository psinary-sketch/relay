# -*- coding: utf-8 -*-
"""b330_extract.py -- THE EXTRACT STEP FOR THE TECHNE EXTRACTION. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### Each method the order names, at the file that EMITTED it --
### the tool's own header where a tool mechanizes it, the lore's entry where the lore carries it, the
### bank where an act minted it -- so that every provenance line in a TECHNE module (act, incident,
### tool path) is pulled and not typed; the August modules and their index, which the September ones
### cross-reference and never edit; TECHNE's own stated principles, which the modules map to; the
### two-clone state, read and not resolved. ### b283's law: every quotation located at its emitting
### file and its line before it is written anywhere else; the gate suite pulls its needles from THIS file.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
TC = r'D:\MY-DOwnloads\TECHNE-Core'
PP = r'D:\MY-DOwnloads\PLACE-papers'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b330_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def m(n):
    return os.path.join(TC, 'modules', '2026-08', n)


WANTED = [
    # ### ---- the ferry-intake scan and the strikes
    ('ferry_scan -- a reader on the input', t('ferry_scan.py'), 'IT IS A READER ON THE INPUT.'),
    ('### the incident: b299 applied a struck clause', t('ferry_scan.py'), 'EMITTED A DOCUMENT APPLYING A CLAUSE THE AUTHOR HAD STRUCK IN THE VERY'),
    ('### the record of strikes, machine-read', d('STRUCK_CLAUSES.md'), 'THE STRUCK LIST'),
    ('### a strike survives in part', d('STRUCK_CLAUSES.md'), 'SURVIVES: the numeral half'),
    # ### ---- the hedge audit
    ('hedge_audit -- a tool, not a resolution', t('hedge_audit.py'), 'A TOOL, NOT A RESOLUTION.'),
    ('### a grade is a commitment; a hedge is a retreat', t('hedge_audit.py'), 'GRADE IS A COMMITMENT; A HEDGE IS A RETREAT FROM ONE.'),
    ('### the lore entry', t('lore_rules.py'), "rule='A graded claim must not also hedge, and an assertion must say its footing.'"),
    # ### ---- needle pulling
    ('needle_pull -- three acts lost a gate to a typed needle', t('needle_pull.py'), 'THREE ACTS RUNNING, EACH TIME'),
    ('### the exact line from the file', t('needle_pull.py'), 'it returns the ### EXACT LINE ### from'),
    ('### the lore entry: pulled, never typed, including self', t('lore_rules.py'), "rule='A needle is pulled from the emitting file, never typed from memory -- '"),
    ('### never from a quoter', d('b283_registration_2026-09-01.txt'), 'NEEDLES PULLED FROM EMITTING FILES, NEVER FROM A QUOTER.'),
    ('### whole-line must-fail', t('needle_pull.py'), 'A STRING THAT IS MERELY A SUBSTRING OF A'),
    # ### ---- the constructive quotation gate
    ('the constructive quotation gate -- the lore entry', t('lore_rules.py'), "rule='A quotation that cannot be verified verbatim is not emitted.'"),
    ('### a generator cannot emit a paraphrase', t('lore_rules.py'), 'only report a paraphrase; one that GENERATES the writing cannot emit one.'),
    ('### F-QUOTE at b266', t('b266_checks.py'), 'Gate 2 -- F-QUOTE, and the emitted table.'),
    # ### ---- the idempotent row-writer, the notation guard, the read-back
    ('b302 -- idempotent: the marker is a literal prefix', t('b302_correspondence.py'), 'IDEMPOTENT: THE MARKER IS A LITERAL PREFIX OF THE STATEMENT WRITTEN.'),
    ('### the blank-cell check is line-scoped', t('b302_correspondence.py'), 'THE BLANK-CELL CHECK IS LINE-SCOPED'),
    ('b303 -- the notation guard: bars are literal pipes', t('b303_correspondence.py'), 'mathematical notation whose bars are ### LITERAL PIPES'),
    ('### raw_pipes', t('b303_correspondence.py'), 'def raw_pipes(text):'),
    ('b327 -- the ledger writer refuses duplicates and reads back', t('b327_faces_row.py'), 'REFUSES DUPLICATES, GUARDS NOTATION, VERIFIES'),
    ('### two paths, two run files', t('b327_faces_row.py'), 'TWO PATHS, TWO RUN FILES'),
    # ### ---- the noise-floor gate
    ('noise_floor -- four of eleven modes were not eigenvalues', t('noise_floor.py'), 'FOUR OF THEM WERE NOT EIGENVALUES.'),
    ('### a magnitude test alone would have passed all four', t('noise_floor.py'), 'A MAGNITUDE TEST ALONE WOULD HAVE PASSED ALL FOUR'),
    ('### the lore entry: the drift arm is the tool', t('lore_rules.py'), "tool='noise_floor.classify -- the DRIFT arm, not the magnitude arm, is the tool; '"),
    # ### ---- registration: seal, satisfiability, order, post-hoc marking
    ('reg_seal -- a hash banked at writing time is proof', t('reg_seal.py'), 'A HASH TAKEN AFTERWARDS IS A DESCRIPTION. ### A HASH BANKED AT WRITING TIME IS PROOF.'),
    ('### a file cannot contain its own hash', t('reg_seal.py'), 'A FILE CANNOT CONTAIN ITS OWN HASH.'),
    ('reg_satisfiable -- two clauses that cannot both be honoured', t('reg_satisfiable.py'), 'THOSE TWO CLAUSES CANNOT BOTH BE'),
    ('b300_regspec -- every number from a committed tool with fixtures', t('b300_regspec.py'), 'EVERY NUMBER AN ACT REPORTS COMES FROM A COMMITTED TOOL THAT CARRIES FIXTURES.'),
    ('registration_gate -- the index did not fail, it was not asked', t('registration_gate.py'), 'THE INDEX DID NOT FAIL. IT WAS NOT ASKED.'),
    ('b325 -- the seat ran ahead of its own execution block', d('b325_the_negative_control.txt'), 'THE SEAT RAN AHEAD OF ITS OWN EXECUTION BLOCK.'),
    ('### every bar marked ORDER or SEAT, POST-HOC', d('b325_the_negative_control.txt'), 'EVERY BAR IS MARKED `[ORDER]` OR `[SEAT, POST-HOC]`'),
    ('### the sealed file carries it as its section (0)', d('b325_the_negative_control.txt'), 'THE SEALED FILE CARRIES THIS AS ITS SECTION (0), BEFORE ANY BAR'),
    # ### ---- the extract-to-disk reading protocol
    ('b283 -- every needle from an emitting file', d('b283_registration_2026-09-01.txt'), 'EVERY NEEDLE FROM AN EMITTING FILE.'),
    ('b329 -- the extract step, as the last act phrased it', t('b329_extract.py'), 'every quotation located at its emitting file and its line before it is'),
    # ### ---- exposure graded by call path
    ('b308 -- exposure by call path', d('b308_the_local_field_instrument.txt'), '(4c) EXPOSURE BY CALL PATH.'),
    ('### the narrative and the tool disagreed, and the defect was the narrative', d('b308_the_local_field_instrument.txt'), 'THE DEFECT WAS THE'),
    ('### b265 decided exposure by call path', d('b265_filings.txt'), 'decided by CALL PATH and tested in code (F-EXPOSURE, positive-controlled).'),
    ('### the August lore already carries it as rule 20', m('HARNESS_LORE.md'), '## 20. ### Exposure is graded by call path before it is measured'),
    # ### ---- the vacuity taxonomy
    ('b277 -- the inverted fixture', d('b277_aggregation_stated.txt'), 'a dead fixture; it is an INVERTED one, and gate 13'),
    ('### the substring species', d('b277_aggregation_stated.txt'), 'WHICH IS A SUBSTRING OF THE CORRECT'),
    ('b278 -- the inverted fixture named as a species', d('b278_registration_2026-09-01.txt'), 'THE INVERTED FIXTURE'),
    ('b275 -- an empty range makes a spec vacuous', d('b275_the_rule_stated.txt'), 'VACUOUS THERE --'),
    ('b312 -- a check at a zero cannot see a factor', d('b312_the_remainder.txt'), 'SO A CROSS-CHECK TAKEN AT A ZERO OF THE FUNCTION CANNOT SEE A MULTIPLICATIVE FACTOR'),
    ('b265 -- a check that has never said no', d('b265_registration_2026-08-31.txt'), 'A CHECK THAT HAS NEVER SAID NO IS'),
    ('b315 -- a gate added where it fires', t('b315_coverage_gate.py'), 'A GATE ADDED IN THE STATE WHERE IT'),
    ('lore -- a gate that has never fired', t('lore_rules.py'), 'A GATE THAT HAS NEVER FIRED IS NOT A GATE THAT PASSED.'),
    ('lore -- an UNAVAILABLE arm is never a pass', t('lore_rules.py'), "rule='A control arm that cannot exist reports UNAVAILABLE -- never a pass.'"),
    ('August HARNESS_LORE -- a must-fail fixture must fail for a structurally different reason', m('HARNESS_LORE.md'), '## 1. A must-fail fixture must fail for a **structurally different reason**'),
    ('### the tautology control', m('HARNESS_LORE.md'), '## 3. The tautology control'),
    ('### positive controls on absences', m('HARNESS_LORE.md'), '## 4. Positive controls on absences'),
    # ### ---- sealed bars found defective; two routes; resolving power; weaker branch; scope-bound constant
    ('b328 -- three sealed bars found defective by running them', d('b328_the_discriminating_family.txt'), 'THREE SEALED BARS FOUND DEFECTIVE BY RUNNING THEM, NONE EDITED, EACH MEASURED:'),
    ('b323 -- the fold: a second route sharing no code', d('b323_the_fold.txt'), 'one identity, two conventions, one file; a second route sharing no code before the first number'),
    ('### two quadratures over one integrand are a limit, not a corroboration', d('b323_the_fold.txt'), 'two quadratures over one integrand are a limit, not a corroboration;'),
    ('b322 -- the resolving-power rule', d('b322_the_membership.txt'), 'THE RESOLVING-POWER RULE: ### A QUESTION IS UNDER-RESOLVED, NOT OPEN, WHEN THE'),
    ('### the price is the ratio', d('b322_the_membership.txt'), 'PRICE IS THE RATIO.**'),
    ('### a price is not a prediction', d('b322_the_membership.txt'), 'A PRICE IS NOT A PREDICTION.'),
    ('b323 -- the weaker branch', d('b323_the_fold.txt'), 'equally, take the weaker; a dichotomy that is not a partition cannot be read either way; a ranker'),
    ('lore -- a constant is scope-bound', t('lore_rules.py'), "rule='A constant is scope-bound and its scope is written down. A tuple that was '"),
    ('### the incident: a prime tuple carried past its reach', t('lore_rules.py'), "incident='b325 -- `b321_window.PRIMES = (2, ..., 31)`, copied from the atlas\\'s own '"),
    # ### ---- cold-clone certification and the coverage gate
    ('b314 -- the fold and the cold clone', d('b314_the_fold_and_the_cold_clone.txt'), 'THIS IS A COLD CACHE AND A COLD CHECKOUT, NOT A COLD MACHINE.'),
    ('### nothing in the build fails when a module is left out', t('b315_coverage_gate.py'), 'NOTHING IN THE BUILD FAILS WHEN A MODULE IS LEFT OUT OF IT.'),
    ('lore -- compiled is not certified', t('lore_rules.py'), "rule='Compiled is not certified. A terminal outside the certification file is a file '"),
    ('### the gate compares filenames and says so', t('lore_rules.py'), 'it compares FILENAMES, so'),
    # ### ---- the census that licenses a phrase
    ('b307 -- the census: U-2 is struck, conditionally', t('b307_handoff_census.py'), 'SURVIVES: the same phrase after a check that has COUNTED WHAT'),
    ('### it counts names and not understanding', t('b307_handoff_census.py'), 'NAMES rather than understanding'),
    # ### ---- general and per-cell
    ('b329 -- the header gate', t('b329_header_gate.py'), 'a check that the header SAYS which is which'),
    ('### the lore entry', t('lore_rules.py'), "rule='General and per-cell are stated in the module header, never averaged: a kernel module '"),
    # ### ---- the negative-control protocol
    ('b325 -- the negative control', d('b325_the_negative_control.txt'), 'b325 -- THE NEGATIVE CONTROL.'),
    ('b326 -- the arc\'s family does not see it', d('b326_the_reach.txt'), "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
    ('### the aimed family, declared and separate', d('b326_the_reach.txt'), 'THE AIMED FAMILY, DECLARED AND SEPARATE : DOES NOT SEE IT EITHER'),
    ('### the library as the fourth link', d('b326_the_reach.txt'), 'THE COMPLETENESS CENSUS -- THE FOURTH LINK, MEASURED TO THE LIBRARY\'S TOP.'),
    ('b328 -- sees it, on this family, at this reach', d('b328_the_discriminating_family.txt'), 'IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES.'),
    # ### ---- certification of an instrument against theorems it did not prove
    ('b320 -- the sign certified, the size not', d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ('### a computation on the space, as certified', d('b320_the_lawful_function.txt'), 'This is a computation on the space, as certified.'),
    ('b302 -- a compiled terminal reads as certifying whatever the act was about', t('b302_correspondence.py'), 'a compiled terminal in a'),
    # ### ---- TECHNE: the principles the modules map to, and the August index
    ('TECHNE -- formalize logic, keep assessment informal', os.path.join(TC, 'CLAUDE.md'), '**Formalize LOGIC, keep ASSESSMENT informal.**'),
    ('### zero sorry, zero axioms on the core path', os.path.join(TC, 'CLAUDE.md'), '**Zero sorry, zero axioms on core path.**'),
    ('### the SIDE method: enumerate, certify completeness, check, conclude by exclusion', os.path.join(TC, 'CLAUDE.md'), 'The SIDE method: enumerate mechanism classes, certify completeness'),
    ('August index -- eight module drafts', m('INDEX.md'), 'Eight module drafts, extracted 2026-08-29 from the b234'),
    ('### grade-honest', m('INDEX.md'), 'a module states the grade its owning act carries and confers none'),
    ('### the two-clone divergence stands unresolved', m('INDEX.md'), 'The two-clone divergence stands unresolved:'),
    ('### not pushed', m('INDEX.md'), 'TECHNE-Core is PRIVATE and was NOT pushed by the act that wrote these files.'),
    ('August HARNESS_LORE -- rule 13, satisfiability before sealing', m('HARNESS_LORE.md'), '## 13. ### Registrations are satisfiability-checked before sealing'),
    ('### rule 11, a falsifier bounded by resolution', m('HARNESS_LORE.md'), "## 11. ### A falsifier's verdict is bounded by its instrument's resolution"),
    ('### rule 14, price before refusing', m('HARNESS_LORE.md'), '## 14. ### Price before refusing'),
    ('### rule 19, scope statements travel with results', m('HARNESS_LORE.md'), '## 19. ### Scope statements travel with results'),
    ('August DISCRIMINATOR_PROTOCOL -- registered before the number', m('DISCRIMINATOR_PROTOCOL.md'), 'A discriminator is registered before the number, or it is not a discriminator.'),
    ('### a falsifier that does not fire is not a prediction confirmed', m('DISCRIMINATOR_PROTOCOL.md'), 'A falsifier that does not fire is not a prediction confirmed.'),
    ('August IMPORT_LEDGER -- no third category', m('IMPORT_LEDGER.md'), 'reproduced longhand or named as an import and graded. There is no'),
    ('b257 -- the canonical clone and the second clone', d('b257_methodology_sweep.txt'), 'CANONICAL CLONE: `D:\\\\MY-DOwnloads\\\\TECHNE-Core`, HEAD `22739c9`'),
    ('### modules untracked, not pushed', d('b257_methodology_sweep.txt'), 'TECHNE-Core WAS *NOT* PUSHED. ### HEAD REMAINS `22739c9` AND `modules/` IS UNTRACKED.'),
    # ### ---- the August lines the September modules quote in their cross-references
    ('### rule 15, a count is not a reading', m('HARNESS_LORE.md'), '## 15. ### A count is not a reading'),
    ('### rule 18, replicates sharing an error source', m('HARNESS_LORE.md'), '## 18. ### Convergence needs interleaved axes'),
    ('### rule 21, a check\'s scope', m('HARNESS_LORE.md'), "## 21. ### A check's scope is stated as precisely as its finding"),
    ('### rule 9, a guard minted after an incident', m('HARNESS_LORE.md'), '## 9. ### A guard minted after an incident audits the past it was minted against'),
    ('### rule 5, a matcher reads code', m('HARNESS_LORE.md'), '## 5. A matcher must read code, not prose'),
    ('### DISCRIMINATOR step 1', m('DISCRIMINATOR_PROTOCOL.md'), 'State the question so that **two named outcomes are possible**.'),
    ('### IMPORT_LEDGER verified-where-tooled', m('IMPORT_LEDGER.md'), '| `VERIFIED-WHERE-TOOLED` | a tool checked it'),
    ('### the prints-are-the-verdict law', m('IMPORT_LEDGER.md'), 'the verification column and the prints-are-the-verdict law'),
    ('b323 -- a judgement rule fires only if a seat applies it', d('b323_the_fold.txt'), 'if a seat applies it.'),
    ('### a ranker does not know what causes what', d('b323_the_fold.txt'), 'does not know what causes what.'),
    ('lore -- the rounded-printout rule, verbatim', t('lore_rules.py'), "rule='A fixture built from a rounded printout is not the measurement.'"),
    ('b329 -- the row tool\'s closing line', t('b329_correspondence.py'), 'and that means THE CELLS SURVIVED. It does not mean they are true.'),
    ('lore -- the UNAVAILABLE rule, verbatim', t('lore_rules.py'), 'reports UNAVAILABLE -- never a pass.'),
    # ### ---- the hygiene fix's model
    ('PLACE-papers .gitattributes -- disk bytes must equal blob bytes', os.path.join(PP, '.gitattributes'), 'Disk bytes must equal blob bytes.'),
    ('### eol=lf makes checkout match storage', os.path.join(PP, '.gitattributes'), '* text=auto eol=lf'),
    ('b329 -- the autocrlf incident this act fixes', d('b329_the_finite_side_seal.txt'), "THE POST-PUSH SUITE FIRED `G-ORDER`, AND THE CAUSE IS b309's SPECIES:"),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b330_extract.py -- THE TECHNE EXTRACTION. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(TC, '<techne>').replace(PP, '<papers>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
