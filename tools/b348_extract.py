# -*- coding: utf-8 -*-
"""b348_extract.py -- THE EXTRACT STEP FOR THE FOLD. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **THE EMITTER DISCIPLINE (b283), WHICH IS THE WHOLE OF WHY THIS FILE EXISTS:** every quotation the fold
### emits is located at ### THE ACT THAT ORIGINATED IT, ### never at an act that quoted it. ### A fold is the place
### where a sentence most easily drifts, because nine acts are being restated by a seat that did not run eight of
### them, and the cheapest guard is to make the seat find each sentence at its owner before it may write it down.
### ### **WHAT IS BEING READ FOR:** one core sentence per act of `b339`-`b347`, in that act's own voice, to carry its
### row; the supports for the arc statement; the five incidents of the species this act mints, EACH AT ITS OWN ACT --
### including the two earliest, which are not in this sortie at all; the census figures at their producing record;
### and the desk's standing items at the acts that own them.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b348_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


FERRY = d('b348_ferry_2026-09-07.txt')

WANTED = [
    # ### ================= THE NINE ACTS, EACH AT ITS OWN BANK =================
    ('b339 -- the verdict, UNAFFORDABLE at the sealed ceiling', d('b339_the_exponent_resolved.txt'),
     'THE VERDICT: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL; THE PRICE BANKED.'),
    ('b339 -- the floor side-reading', d('b339_the_exponent_resolved.txt'),
     'is that the residual the price extrapolated is descending toward a FLOOR and not'),
    ('b340 -- the verdict as sealed', d('b340_the_li_family_control.txt'),
     'THE VERDICT AS SEALED: THE DIFFERING CONSTITUENT -- A QUADRATURE FAILURE, THE GATE REFUSING THE SEALED'),
    ('b340 -- the refinement failed, not the identity', d('b340_the_li_family_control.txt'),
     'REFINEMENT ROUTE, NOT THE IDENTITY, IS WHAT FAILED. ### THE BAR AS SEALED IS NOT MET AND IS NOT REWRITTEN.'),
    ('b341 -- the bench carries the defect', d('b341_the_two_coefficients.txt'),
     'THE BENCH CARRIES THE DEFECT'),
    ('b342 -- the order arm is a defective bar', d('b342_the_two_rules_as_modules.txt'),
     '### ### **(4) THE ORDER ARM IS A DEFECTIVE BAR, RUN AND TABLED RATHER THAN EDITED INTO PASSING.** ### `G-ORDER`'),
    ('b343 -- no crossing at both widths', d('b343_the_maps_next_reach.txt'),
     'NO CROSSING'),
    ('b344 -- the residual moves with NY, of the size the floor requires', d('b344_the_floor_priced.txt'),
     '### ### **(1) THE RESIDUAL MOVES WITH `NY`, AND BY THE SEALED RULE THE MOVEMENT IS OF THE SIZE THE FLOOR'),
    ('b344 -- one axis moved is one axis moved', d('b344_the_floor_priced.txt'),
     '### **ONE AXIS MOVED IS ONE AXIS MOVED: NOTHING IS CONCLUDED ABOUT THE TWO HELD, AND THE FLOOR IS NOT'),
    ('b345 -- a fourth control holds', d('b345_the_li_control_rerun.txt'),
     '### ### ### **A FOURTH CONTROL HOLDS.**'),
    ('b345 -- b340 is not rewritten', d('b345_the_li_control_rerun.txt'),
     "### ### **b340's BAR IS NOT REWRITTEN. ### ITS VERDICT IS NOT RE-VERDICTED. ### ITS BANK IS NOT EDITED.**"),
    ('b346 -- a floor is present', d('b346_the_exponent_by_rate.txt'),
     '### ### ### **A FLOOR IS PRESENT. ### SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE.**'),
    ('b346 -- resolved on the rate axis', d('b346_the_exponent_by_rate.txt'),
     '### ### ### **AND ON THE RATE AXIS THE QUESTION IS RESOLVED, AT A RESOLVING POWER OF `63.6`.**'),
    ('b346 -- the banked values carry the corpus\'s own convention', d('b346_the_exponent_by_rate.txt'),
     "### ### ### **THE BANKED VALUES CARRY THE CORPUS'S OWN `r ** -0.5`.**"),
    ('b347 -- a sharper instrument is not a result', d('b347_the_three_repairs.txt'),
     '### ### ### **A SHARPER INSTRUMENT IS NOT A RESULT.**'),
    ('b347 -- the rule itself', d('b347_the_three_repairs.txt'),
     '### ### ### **THE RULE:** ### **A NUMERICAL BAR IS STATED WITH THE FLOOR OF THE OBJECT IT TESTS; A BAR'),
    # ### ================= THE ACTS' CORRECTIONS TO THEIR OWN READINGS =================
    ("b346 -- b339's ratios reading is narrower than its sentence", d('b346_the_exponent_by_rate.txt'),
     "### ### **AND ONE READING OF b339's IS NARROWER THAN ITS SENTENCE, MEASURED HERE AND REPORTED.**"),
    ('b342 -- the extract law was broken and the act says where', d('b342_the_two_rules_as_modules.txt'),
     'E3'),
    ('b345 -- a draft ran at parameters the act did not seal', d('b345_the_li_control_rerun.txt'),
     '### ### **(E1) A DRAFT RAN AT PARAMETERS THIS ACT DID NOT SEAL, AND WAS STOPPED.**'),
    # ### ================= THE SEALED BARS FOUND DEFECTIVE =================
    ('b345 -- the fixture could not separate', d('b345_the_li_control_rerun.txt'),
     '### ### **THE TWO CANNOT BOTH HOLD, AND RUNNING THE FIXTURE IS WHAT SHOWED IT.**'),
    ('b346 -- the arm that did no work', d('b346_the_exponent_by_rate.txt'),
     '### ### **(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK, AND THE SEALED PAIRING IS DEFECTIVE.**'),
    ('b345 -- the ordering is not recoverable after a checkout', d('b345_the_li_control_rerun.txt'),
     '### ### RUNNING ITS OWN SUITE TWICE.**'),
    # ### ================= THE SPECIES THIS ACT MINTS: FIVE INCIDENTS, EACH AT ITS OWN ACT =================
    ('the species at b317, in its own words', d('b317_gates.txt'),
     '    ### **THE SCAN IS OVER STRIPPED CODE.** ### A docstring saying the unit is never'),
    ('### and the sentence that completes it', d('b317_gates.txt'),
     '    ### called is not a call, and the first version of this gate could not tell.'),
    ('the species at b316, the arm it fired on', d('b316_gates.txt'),
     '  G-NOTRACE (no trace computed, no smear assembled -- read off the emitting files):'),
    ('the species at b345, the arm that read a wrapped sentence raw', d('b345_checks_after.txt'),
     '  G-SCOPE (both certification lists as the prior leg listed them; the certificate at its line; the Sonin margin not evaluated):'),
    ('the species at b346, in b346\'s own closing record', d('b346_checks_after.txt'),
     '  G-AXIS (the rate along the ARGUMENT, with b315\'s reason quoted; no cutoff quantity computed):'),
    ('the species at b347, the arm that found its own search string', d('b347_the_three_repairs.txt'),
     '###   ### **(iii) THE GATE MATCHES TEXT.**'),
    ('the cure, as b317 already stated it', d('b317_gates.txt'),
     '    the act says so : True ; and no unit call appears in either tool : True'),
    # ### ================= THE CENSUS, AT ITS PRODUCING RECORD =================
    ('the census, at its producing record', d('b347_repairs_run.txt'),
     '    registrations gated : 333 ; would FIRE on at least one arm : 52 ; CLEAR : 281'),
    ('### and what the quiet means', d('b347_repairs_run.txt'),
     '    ### of the 281 that would not fire, 276 carry NEITHER a threshold NOR a multi-arm passage for the arms to see'),
    ('### the arms bind what comes after them', d('b347_the_three_repairs.txt'),
     '### ### **A QUIET ROW IS MOSTLY QUIET BECAUSE THERE WAS NOTHING FOR THE ARM TO LOOK AT, NOT BECAUSE THE ARM'),
    # ### ================= THE DESK =================
    ('the desk -- M-2 under its cap', d('b332_the_clause_stated.txt'), 'M-2'),
    ('the desk -- the clause stated, the quantifier unowned', d('b332_the_clause_stated.txt'),
     'K8'),
    ("the desk -- the floor's two held axes, priceable without re-running", d('b344_the_floor_priced.txt'),
     "### later act can price them without re-running this one: the cut's `tau = 1.0e-06` in force, with `2`"),
    ("the desk -- the room's minimum bracketed at the lowest height", d('b344_the_floor_priced.txt'),
     'BRACKETED'),
    ('the desk -- the patent receipts, the one item with a date', os.path.join(PP, 'FINDINGS.md'),
     'ABSENT ON THE MOUNTED VOLUMES for both applications (b337)'),
    ('the desk -- the Li-to-Weil bridge still owed', os.path.join(PP, 'FINDINGS.md'),
     '| **The Li-to-Weil bridge** | OWED at L1'),
    # ### ================= THE FOLD'S OWN LAW, FROM THE LAST FOLD =================
    ('the last fold -- a filings section moves no grade', os.path.join(PP, 'FINDINGS.md'),
     '**Four acts, 2026-09-06.** A filings section: **no grade moves here, no act is re-verdicted, and nothing below is new mathematics.**'),
    ('the last fold -- the section it ends at', os.path.join(PP, 'FINDINGS.md'),
     '## THE STATED-CLAUSE ARC, b331\u2013b334 \u2014 THE FOLD'),
    # ### ================= THE ORDER =================
    ('the order -- the scope', FERRY, 'Scope: FILINGS only; NO'),
    ('the order -- component 3, the species minted', FERRY,
     'COMPONENT 3 \u2014 THE LORE, with one species MINTED: a scanner over'),
    ('the order -- the cure it names', FERRY,
     '(arms scoped to code lines or to marked mention-regions, never'),
    ('the order -- the census as a finding', FERRY,
     'COMPONENT 4 \u2014 THE CENSUS AS A FINDING about the record, not a'),
    ('the order -- the failure-mode partition, named and NOT opened', FERRY,
     'as a research proposal and NOT opened \u2014 a finite classification'),
    ('the order -- no such partition is known to exist', FERRY,
     'sentence that no such partition is known to exist; the wave'),
    ('the order -- the foot', FERRY, 'FOOT: after this act nine acts are one section, one species is'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b348_extract.py -- THE FOLD. ### EVERY QUOTATION AT THE ACT THAT ORIGINATED IT, WITH ITS LINE.')
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
        short = path.replace(PP, '<papers>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
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
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
