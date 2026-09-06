# -*- coding: utf-8 -*-
"""b331_extract.py -- THE EXTRACT STEP FOR THE FOLD, b323-b330. ### **EVERY READ, TO DISK, WITH ITS LINE.**

### ### **WHAT THIS ACT IS READING FOR.** ### Each of the eight acts' own sentences -- the result, the
### obstacle, the correction, the defect -- at the bank that ORIGINATED it (never at a quoter); the
### prior fold's generator and section, whose rules this fold inherits; the lore's entries since the
### prior fold; the ledgers and trails the desk restates; the findings document's last section and
### line count before the append. ### b283's law: every quotation located at its emitting file and its
### line before it is written anywhere else; the generator's F-QUOTE re-checks every one at emission.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TC = r'D:\MY-DOwnloads\TECHNE-Core'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b331_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


WANTED = [
    # ### ---- b323: the prior fold and the defective-bars table
    ('b323 -- the section is filed', d('b323_the_fold.txt'), 'THE SECTION IS FILED.'),
    ('### purely additive, measured', d('b323_the_fold.txt'), 'A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD'),
    ('### the defective-bars table', d('b323_the_fold.txt'), 'IN NO CASE WAS THE SEALED FILE EDITED.'),
    ('### F-QUOTE 18 of 18', d('b323_the_fold.txt'), '`F-QUOTE` PASSES AT 18 OF 18, AND ITS DISCRIMINATION ARM FIRES.'),
    ('### the two generator defects', d('b323_the_fold.txt'), "TWO DEFECTS IN THIS ACT'S OWN GENERATOR, DECLARED."),
    ('### the in-flight register', d('b323_the_fold.txt'), 'THE IN-FLIGHT REGISTER.'),
    ('### the resolving power priced twice', d('b323_the_fold.txt'), 'THE RESOLVING POWER HAS BEEN PRICED TWICE'),
    ('### the exponent ratio', d('b323_the_fold.txt'), 'a ratio of `0.393`'),
    ('### the prior generator: a quotation of a quotation is not a source', t('b323_fold.py'), 'A QUOTATION OF A'),
    ('### the prior generator: the judgement is the seat\'s', t('b323_fold.py'), 'IS THE SEAT\'S, AND IS DECLARED'),
    ('### the prior fold section title', os.path.join(PP, 'FINDINGS.md'), 'THE ARCHIMEDEAN INSTRUMENT ARC, b314'),
    # ### ---- b324: the keystones re-read
    ('b324 -- the wall: different', d('b324_the_keystones_reread.txt'), 'THE WALL: ### DIFFERENT. ### (F1) IS REFUTED, AND BOTH ITS HALVES FALL.'),
    ('### the source graded as stalling', d('b324_the_keystones_reread.txt'), 'STALL AT THE REALIZATION CLAUSE.'),
    ('### the margin undecided', d('b324_the_keystones_reread.txt'), 'THE MARGIN: ### UNDECIDED -- AND FOR A SHARPER REASON THAN (F2) REGISTERED.'),
    ('### withheld by design', d('b324_the_keystones_reread.txt'), 'THE DEPOSIT DELIBERATELY WITHHOLDS IT'),
    ('### the margins differ at six of seven', d('b324_the_keystones_reread.txt'), 'AND THE TWO MARGINS DIFFER AT SIX OF SEVEN CONSTITUENTS.'),
    ('### the bridging statement typed as owed', d('b324_the_keystones_reread.txt'), 'THE BRIDGING STATEMENT, TYPED AS OWED AND FILED AS THE ARC\'S MOST VALUABLE OPEN ITEM:'),
    ('### the seven contacts', d('b324_the_keystones_reread.txt'), 'THE SEVEN CONTACTS: ### 3 CORROBORATED, 4 UNTOUCHED, 0 IN TENSION.'),
    ('### the wave\'s candidate list, typed', d('b324_the_keystones_reread.txt'), "THE WAVE'S CANDIDATE LIST, TYPED. ### NO RECOMMENDATION, NO RANKING."),
    ('### the Epstein test handed to a successor', d('b324_the_keystones_reread.txt'), 'THE ARC NEVER RAN ITS INSTRUMENT ON AN'),
    # ### ---- b325: the negative control at the arc's cells
    ('b325 -- does not see it at the arc\'s cells', d('b325_the_negative_control.txt'), 'AT THE ARC\'S CELLS: ### DOES NOT SEE IT. ### THE REGISTERED EXPECTATION IS'),
    ('### negative at all thirteen', d('b325_the_negative_control.txt'), 'NEGATIVE AT ALL THIRTEEN CELLS'),
    ('### the form represents nothing between 1 and 4', d('b325_the_negative_control.txt'), 'NOTHING BETWEEN 1 AND 4'),
    ('### the finite channel identically zero until a = 2', d('b325_the_negative_control.txt'), 'IDENTICALLY ZERO UNTIL `a = 2`'),
    ('### the positive control fired', d('b325_the_negative_control.txt'), 'THE POSITIVE CONTROL FIRED, AND CAUGHT A REAL DEFECT IN AN INHERITED CONSTANT.'),
    ('### a control whose answer is known', d('b325_the_negative_control.txt'), 'A CONTROL WHOSE CORRECT ANSWER IS KNOWN IN ADVANCE HAD GIVEN THE WRONG'),
    ('### the seat ran ahead', d('b325_the_negative_control.txt'), 'THE SEAT RAN AHEAD OF ITS OWN EXECUTION BLOCK.'),
    ('### bars marked ORDER or POST-HOC', d('b325_the_negative_control.txt'), 'EVERY BAR IS MARKED `[ORDER]` OR `[SEAT, POST-HOC]`'),
    # ### ---- b326: the reach
    ('b326 -- the arc\'s family to a = 400', d('b326_the_reach.txt'), "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
    ('### the priced crossing an artefact', d('b326_the_reach.txt'), 'THE PRICED CROSSING WAS AN ARTEFACT, AND THE CLOSURE DECIDED IT.'),
    ('### the kernel halved', d('b326_the_reach.txt'), 'Epstein archimedean kernel was ### **HALF** ### the derived'),
    ('### 146 on the line, 17 off', d('b326_the_reach.txt'), 'THE EPSTEIN ZEROS: 146 ON THE LINE TO `T = 150`, 17 OFF IT, AND THE COUNT'),
    ('### the explicit formula closes for both', d('b326_the_reach.txt'), 'THE EXPLICIT FORMULA CLOSES FOR BOTH.'),
    ('### the aimed family, separate', d('b326_the_reach.txt'), 'THE AIMED FAMILY, DECLARED AND SEPARATE : DOES NOT SEE IT EITHER'),
    ('### three estimates failed their own gates', d('b326_the_reach.txt'), "THREE OF THIS ACT'S OWN ESTIMATES FAILED THEIR OWN GATES AND ARE DECLARED:"),
    ('### it does not say the instrument cannot see', d('b326_the_reach.txt'), 'IT DOES NOT SAY THE INSTRUMENT CANNOT SEE A FAILURE.'),
    ('### b325 not re-verdicted', d('b326_the_reach.txt'), 'IT DOES NOT RE-VERDICT b325'),
    # ### ---- b327: the faces ledger and the bridge
    ('b327 -- the ledger exists', d('b327_the_faces_ledger.txt'), 'THE LEDGER EXISTS: `PLACE-papers/FACES_LEDGER.md`, THIRTEEN ROWS, SEVENTY-EIGHT PAIRS,'),
    ('### it certifies nothing', d('b327_the_faces_ledger.txt'), 'The ledger certifies nothing and says so before its purpose does.'),
    ('### the bridge read: different on both', d('b327_the_faces_ledger.txt'), 'THE BRIDGE, READ: DIFFERENT ON BOTH QUESTIONS, WITH THE MAP DERIVED AND THE BRIDGE'),
    ('### different by the constant 1', d('b327_the_faces_ledger.txt'), 'DIFFERENT, constituent quoted: by the constant `1`'),
    ('### one distribution on two families', d('b327_the_faces_ledger.txt'), 'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.'),
    ('### the map derived and corroborated', d('b327_the_faces_ledger.txt'), 'The map `lambda_A(n) = S_inf(n) + 1` was derived on paper into the sealed registration and'),
    ('### the bench disagrees with the keystone at two indices', d('b327_the_faces_ledger.txt'), "And the bench's own literature dict disagrees with the balance keystone's literature column"),
    ('### at n = 3 and n = 5', d('b327_the_faces_ledger.txt'), 'at `n = 3` and `n = 5` -- a typed fixture, filed and not edited; the computation matches the'),
    ('### the three owed bridges by ID', d('b327_the_faces_ledger.txt'), 'THE THREE OWED BRIDGES ARE ON THE TRAILS BY ID:'),
    ('### it does not say any two faces are equivalent', d('b327_the_faces_ledger.txt'), 'IT DOES NOT SAY ANY TWO FACES ARE EQUIVALENT'),
    # ### ---- b328: the discriminating family
    ('b328 -- sees it at seven of eight', d('b328_the_discriminating_family.txt'), 'SEES IT -- AT SEVEN OF EIGHT CELLS.'),
    ('### zeta held at every cell', d('b328_the_discriminating_family.txt'), 'THE ZETA CONTROL HELD AT EVERY CELL: THE PERMITTED SIGN, CERTIFIED, AND THE FORMULA'),
    ('### the condition derives', d('b328_the_discriminating_family.txt'), 'THE CONDITION DERIVES AS ASSERTED, WITH THE QUADRUPLE'),
    ('### negative past forty-five degrees', d('b328_the_discriminating_family.txt'), 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE'),
    ('### F2 met', d('b328_the_discriminating_family.txt'), '(F2) IS MET.'),
    ('### the exception E20', d('b328_the_discriminating_family.txt'), 'THE ONE CELL THAT DOES NOT SEE IT IS THE NARROWEST EVEN ONE'),
    ('### three sealed bars defective', d('b328_the_discriminating_family.txt'), 'THREE SEALED BARS FOUND DEFECTIVE BY RUNNING THEM, NONE EDITED, EACH MEASURED:'),
    ('### the signs do not rest on them', d('b328_the_discriminating_family.txt'), 'THE SIGNS DO NOT REST ON ANY OF THE THREE'),
    ('### not counterexamples in general', d('b328_the_discriminating_family.txt'), 'IT DOES NOT SAY THE INSTRUMENT SEES COUNTEREXAMPLES.'),
    ('### nothing about totality', d('b328_the_discriminating_family.txt'), 'NOTHING ABOUT TOTALITY.'),
    # ### ---- b329: the finite-side seal
    ('b329 -- one compiled module', d('b329_the_finite_side_seal.txt'), "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS"),
    ('### never averaged', d('b329_the_finite_side_seal.txt'), 'FOR THE COMPACT PART, NEVER AVERAGED.**'),
    ('### the axiom finding', d('b329_the_finite_side_seal.txt'), 'THE AXIOM FINDING, WHICH THIS SEAT DID NOT EXPECT'),
    ('### equations with witnesses', d('b329_the_finite_side_seal.txt'), 'STATED AS EQUATIONS WITH THEIR WITNESSES AND PROVED FROM THE AXIOM-FREE PART OF CORE PLUS SIX'),
    ('### primality nowhere', d('b329_the_finite_side_seal.txt'), 'CONSEQUENTLY PRIMALITY IS USED NOWHERE IN THE MODULE'),
    ('### D1', d('b329_the_finite_side_seal.txt'), '(D1) THE REGISTERED (T1.4) IS NOT MET IN ITS REGISTERED FORM:'),
    ('### not general for the compact part', d('b329_the_finite_side_seal.txt'), "IT DOES NOT SAY THE COMPACT PART'S SILENCE IS PROVED IN GENERAL."),
    ('### 566 -> 590', d('b329_the_finite_side_seal.txt'), '566 -> 590 PRINTS, 566 -> 590 ZERO-AXIOM, 0 -> 0 OTHERWISE, 40885 -> 42320 BYTES, THE'),
    ('### autocrlf, b309\'s species', d('b329_the_finite_side_seal.txt'), "THE POST-PUSH SUITE FIRED `G-ORDER`, AND THE CAUSE IS b309's SPECIES:"),
    # ### ---- b330: the TECHNE extraction
    ('b330 -- the modules in the private core', d('b330_the_techne_extraction.txt'), "THE ARC'S METHODS ARE CLAIM-SHAPED MODULE DRAFTS IN TECHNE'S PRIVATE CORE, WITH THEIR"),
    ('### not pushed', d('b330_the_techne_extraction.txt'), 'THE LOCAL TECHNE COMMIT: `75ab3ff` -- NOT PUSHED.'),
    ('### the kernel no longer drifts', d('b330_the_techne_extraction.txt'), 'THE KERNEL NO LONGER DRIFTS ON LINE ENDINGS.'),
    ('### the patent day has material', d('b330_the_techne_extraction.txt'), 'THE PATENT DAY HAS MATERIAL'),
    ('### not novel in law', d('b330_the_techne_extraction.txt'), 'IT DOES NOT SAY ANY METHOD IS NOVEL IN LAW.'),
    ('### the august files routed', d('b330_the_techne_extraction.txt'), 'IT DOES NOT COMMIT THE AUGUST FILES.'),
    ('### the sweep fired on the seat', d('b330_the_techne_extraction.txt'), "THE SWEEP FIRED ON THIS SEAT'S OWN WRITING, WHICH IS WHAT IT"),
    ('### F8 on two modules', d('b330_the_techne_extraction.txt'), 'THE SEALED BAR (F8) IS NOT MET IN ITS LITERAL FORM ON TWO MODULES, AND SAID:'),
    # ### ---- the lore since the prior fold
    ('lore -- scope-bound constant', t('lore_rules.py'), "rule='A constant is scope-bound and its scope is written down. A tuple that was '"),
    ('lore -- the phase condition', t('lore_rules.py'), "rule='A lawful test function\\'s four-term sum at an off-line quadruple is 4 Re(G_e^2 - G_o^2): '"),
    ('lore -- general and per-cell', t('lore_rules.py'), "rule='General and per-cell are stated in the module header, never averaged: a kernel module '"),
    ('lore -- the standing caution', t('lore_rules.py'), 'A GATE THAT HAS NEVER FIRED IS NOT A GATE THAT PASSED.'),
    # ### ---- the desk's sources
    ('HANDOFF -- M-2 remains', os.path.join(ROOT, 'HANDOFF.md'), 'REMAINS `(SPECIFIED-NOT-STATED)`.'),
    ('### the patent receipts, three days past both dates', os.path.join(ROOT, 'HANDOFF.md'), 'receipts are pending on the ferry\'s word, **three days past both dates.**'),
    ('OPEN_TRAILS -- the li-weil bridge', os.path.join(PP, 'OPEN_TRAILS.md'), 'W-ORD-LI-WEIL-BRIDGE'),
    ('### the discriminating family trail, partly paid', os.path.join(PP, 'OPEN_TRAILS.md'), 'PARTLY PAID (b328)'),
    ('FACES -- F5 proved-general / at-cells', os.path.join(PP, 'FACES_LEDGER.md'), 'PROVED-GENERAL (the scaling part'),
    ('TECHNE index -- the august files untracked', os.path.join(TC, 'modules', 'INDEX.md'), '**The August files are untouched**'),
    ('### the divergence not resolved', os.path.join(TC, 'modules', 'INDEX.md'), 'Reported at b257, read again at b330, not resolved.'),
    # ### ---- the findings document before the append
    ('FINDINGS -- the last section before this fold', os.path.join(PP, 'FINDINGS.md'), '## THE FACES LEDGER \u2014 b327'),
    ('### how findings move', os.path.join(PP, 'FINDINGS.md'), '## How findings move'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b331_extract.py -- THE FOLD, b323-b330. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
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
        short = path.replace(TC, '<techne>').replace(PP, '<papers>').replace(SIDE, '<side>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    fl = os.path.join(PP, 'FINDINGS.md')
    txt = io.open(fl, encoding='utf-8', errors='replace').read()
    rec('### ==== FINDINGS.md before the append : %d lines, %d bytes, %d sections' % (len(txt.splitlines()), len(txt.encode('utf-8')), len([x for x in txt.splitlines() if x.startswith('## ')])))
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline='\n').write('\n'.join(lines) + '\n')
    print('\n'.join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
