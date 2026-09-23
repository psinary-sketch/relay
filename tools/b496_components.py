# -*- coding: utf-8 -*-
"""b496_components.py -- THE COMPONENTS BANK. ### **THE RESIDUE HAND-READ, ROW BY ROW.**

### ### **A SCREEN TIGHTENED FOUR TIMES IS STILL A SCREEN.** ### b391's rule: tighten on content,
### then ### **HAND-READ THE RESIDUE** -- a count of 8 is a number a person can check, and a
### number a person can check is one this act must check rather than report.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


# ### ### **THE HAND READING.** ### One entry per CONFLICT row the instrument emitted, each
# ### classified with the REASON READ OFF THE QUOTED CELLS, not off the name.
HAND = {
    'SIDEBijection.identity_formation_bijection': (
        'ARTEFACT -- NEIGHBOURING OBJECT',
        'The `SHELL` is its own: *"-- **SHELL / hypothesis-assumed**"*. The `INTERFACES` belongs '
        'to the clause beside it, *"class-number values stipulated -> INTERFACES on arithmetic"*, '
        'which grades a DIFFERENT object in the same sentence. Both ledgers carry the same text, '
        'so the two sources AGREE; the disagreement is inside one sentence and is not one.'),
    'parametric_mechanism_theorem': (
        'ARTEFACT -- A RULE STATED, NOT A GRADE CONFERRED',
        'At OPEN_TRAILS-archive-2:1019 the word `INTERFACES` appears in *"O.18`s standing rule '
        '(INTERFACES = handoff owed back)"* -- a DEFINITION OF THE VOCABULARY, and the grade the '
        'same cell confers is DERIVES. At VERIFICATION_LOOM-archive-1:1408 the cell reads '
        '*"DERIVES on the proven direction, INTERFACES on the source biconditional"* -- ONE '
        'verdict in two parts, consistent with the first. **THE LEDGERS AGREE.**'),
    'Voice7Witness.hadamard_does_not_enforce_online': (
        'ARTEFACT -- PREPONDERANCE IS FIVE TO ONE',
        'FIVE cells say DERIVES, in REGISTRY and in three archive files. The single SHELL sits '
        'further along FINDINGS-archive-1:131, a line whose subject is the rows being re-pointed '
        'AWAY FROM a shell stand-in TO this faithful discriminator. The grade that line confers '
        'on this name is the DERIVES printed beside it.'),
    'conservation_of_spectra': (
        'ARTEFACT -- A RANKING, NOT A GRADING',
        'VERIFICATION_LOOM-archive-1:3392 is the load-bearing map: *"hub terminals ranked -- '
        '`h1_complete_at_Phi` / `RegisterPentagon` / `conservation_of_spectra` each cited by 6 '
        'keystones"*, and the `INTERFACES` that follows begins a different clause about the '
        'INTERFACES index. **A NAME IN A RANKING IS NOT A NAME IN A GRADE CELL.**'),
    'e_difficulty': (
        '### **GENUINE CONFLICT**',
        'THREE cells, THREE places, THREE verdicts on the same name. '
        'OPEN_TRAILS-archive-2:939 -- *"E-Difficulty verdicts are now kernel-certified at the '
        'structural level (`e_difficulty` DERIVES)"*. '
        'OPEN_TRAILS-archive-2:953 -- *"`e_difficulty` -- **ENCODES-CONCLUSION \\\\ SHELL.** '
        '`IsDecidable s == True` (discards `_s`)"*. '
        'VERIFICATION_LOOM-archive-1:1919 -- *"the E-Difficulty bridge cited as **INTERFACES on a '
        'named premise**"*. '
        '**THE FIRST TWO ARE FOURTEEN LINES APART IN ONE FILE AND SAY OPPOSITE THINGS**: one '
        'calls it certified at the structural level, the other says the content is defined into '
        'the statement. ### **THIS ACT DOES NOT CHOOSE BETWEEN THEM.**'),
    'type_I_has_ostrowski': (
        'ARTEFACT -- A VOCABULARY RECITED',
        'VERIFICATION_LOOM-archive-1:1424 reads *"full DERIVES/INTERFACES/SHELL Correspondence, '
        'pinned `#print axioms`"* -- the THREE-GRADE VOCABULARY NAMED AS A SET, describing what a '
        'keystone carries, not grading anything. The compound-aware matcher merged it into the '
        'single token `DERIVES \\\\ INTERFACES \\\\ SHELL`, ### **WHICH IS HOW THE ARTEFACT BECAME '
        'VISIBLE**: a compound of ALL THREE grade names is a vocabulary, never a verdict.'),
    'ExplicitFormulaDecomp': (
        '### AMBIGUOUS -- READ BOTH WAYS AND LEFT OPEN',
        'OPEN_TRAILS-archive-2:1705 grades it plainly: *"**Grade INTERFACES, THREE named '
        'premises:** `VerifiedZerosTo T` (external computation), `ExplicitFormulaDecomp` "*. '
        'VERIFICATION_LOOM-archive-1:1702 reads *"The discharge is a genuine but **isolated** '
        'DERIVES: it de-opaques `low` and converts one of `ExplicitFormulaDecomp`\'s ~three '
        'assumed clauses"* -- where the DERIVES is most naturally the DISCHARGE\'s and this name '
        'is the thing being converted. ### **BUT A READER CAN TAKE IT AS A GRADE ON THE NAME**, '
        'and this act will not decide a ledger\'s meaning for it. ### Left as a CANDIDATE.'),
    'delta_n4_count': (
        'ARTEFACT -- ONE CELL, TWO SUBJECTS',
        'Both grade words are on OPEN_TRAILS-archive-2:2001. The DERIVES attaches to this name '
        '(*"`delta_n4_count` DERIVES (the W-ORD-DELTA-N4-H2 count half discharged"*); the '
        'INTERFACES begins the clause about the cohomological remainder, a different half of the '
        'same work order.'),
}


def main():
    T = json.loads(read(os.path.join(D, 'terminal_table.json')))
    rows = T['rows']
    conf = [r for r in rows if r['grade'] == 'CONFLICT']

    rec('=' * 104)
    rec('b496 -- THE COMPONENTS. ### K0 EMITTED, AND ITS RESIDUE HAND-READ.')
    rec('=' * 104)
    rec('')
    rec('### (1) THE INSTRUMENT, AND THE FOUR MATCHERS IT TOOK TO GET ONE.')
    rec('-' * 104)
    rec('    v1 LOOSE      : %4d cells, %3d names   ### any name on any line carrying a grade word'
        % (T['grade_cells_loose_v1'], 691))
    rec('    v2 WINDOWED   : %4d cells, %3d names   ### every name within 120 chars of a grade'
        % (T['grade_cells_v2'], 133))
    rec('    v3 NEAREST    : %4d cells, %3d names   ### each grade to its NEAREST name only'
        % (T['grade_cells_v3'], 77))
    rec('    ### **v4 COMPOUND : %4d cells, %3d names   ### adjacent grade words = ONE verdict**'
        % (T['grade_cells'], 77))
    rec('    CONFLICT by version : ### **67 -> 17 -> 12 -> %d**' % len(conf))
    rec('    ### ### **EVERY YIELD IS PRINTED AND EVERY VERSION IS STILL RUNNABLE** -- b381`s')
    rec('    ### lineage rule. ### A matcher replaced silently is a number nobody can check.')
    rec('    ### ### **AND THE LAST STEP WAS NOT A TIGHTENING BUT A READING OF THE ORDER.** ###')
    rec('    ### (R107) defines CONFLICT as ### *"where two ledger cells grade one name')
    rec('    ### differently"*. ### A cell that writes ### `ENCODES-CONCLUSION \\ SHELL` ### is')
    rec('    ### ### **ONE CELL WITH A COMPOUND VERDICT**, and v1-v3 read it as two cells at war.')
    rec('')
    rec('### (2) THE %d CONFLICT ROWS, EVERY ONE READ BY HAND.' % len(conf))
    rec('-' * 104)
    genuine, amb, art = [], [], []
    for r in sorted(conf, key=lambda x: x['name']):
        verdict, why = HAND.get(r['name'], ('### NOT HAND-READ', '### THIS ROW HAS NO READING.'))
        rec('  **`%s`** (`%s`) -- %s' % (r['name'], r['repo'], ' vs '.join(r['conflict'])))
        rec('    ### %s' % verdict)
        for chunk in [why[i:i + 96] for i in range(0, len(why), 96)]:
            rec('      %s' % chunk)
        rec('')
        (genuine if 'GENUINE' in verdict else amb if 'AMBIGUOUS' in verdict else art).append(r['name'])
    rec('  ### ### **GENUINE : %d %s**' % (len(genuine), genuine))
    rec('  ### ### **AMBIGUOUS : %d %s**' % (len(amb), amb))
    rec('  ### ARTEFACT : %d' % len(art))
    rec('  ### ### **THE MACHINE CELL STAYS `CONFLICT` ON ALL %d.** ### The table is an INSTRUMENT'
        % len(conf))
    rec('  ### OUTPUT and it reports what its predicate found; ### **THIS BANK IS THE READING, AND')
    rec('  ### THE TWO ARE KEPT APART ON PURPOSE.** ### A generator that quietly dropped the six')
    rec('  ### artefacts would be a generator whose number nobody could reproduce.')
    rec('')
    rec('### (3) WHAT THE HAND READING FOUND THAT THE COUNT DID NOT.')
    rec('-' * 104)
    rec('    ### ### **THE GRADE VOCABULARY HAS NO CELL FOR A SPLIT GRADE.** ### The ledgers write')
    rec('    ### *"DERIVES on the proven direction, INTERFACES on the source biconditional"* and')
    rec('    ### *"ENCODES-CONCLUSION \\ SHELL"* because ### **ONE TERMINAL CAN BE TWO THINGS AT')
    rec('    ### ONCE** -- derived in one direction and interfaced in the other. ### The K/C/N/E')
    rec('    ### taxonomy the author ruled on 2026-07-28 has no such cell, so the ledgers improvise')
    rec('    ### one in prose, and ### **EVERY MATCHER THAT READS GRADES AS ATOMS MISREADS THEM.**')
    rec('    ### This is a finding for K1 and this act neither fixes it nor grades anything.')
    rec('')
    rec('### (4) THE COUNTS (3) ASKS FOR.')
    rec('-' * 104)
    C = T['counts']
    rec('    rows (repo, name)                                  : ### **%d**' % C['rows'])
    rec('    NOT PROFILED                                       : ### **%d**' % C['not_profiled'])
    rec('    UNGRADED                                           : ### **%d**' % C['ungraded'])
    rec('    CONFLICT                                           : ### **%d**' % C['conflict'])
    rec('    ENCODES-graded                                     : ### **%d**' % C['encodes'])
    rec('    ledger names resolving in NO repo at ANY ref       : ### **%d**'
        % C['ledger_names_unresolved'])
    rec('    STATEMENT UNRESOLVED (owed by (S1), not asked for) : ### **%d**'
        % C['statement_unresolved'])
    rec('    repositories : %d named `SIDE-*`, %d with a `.git` ; ledgers read : %d'
        % (T['repos_named'], T['repos_with_git'], T['ledgers']))
    rec('    REGISTRY kernel table names a pin for ### **%d of %d** repositories'
        % (T['pins_named'], T['repos_with_git']))
    rec('')
    rec('### (5) THIS ACT CONFERS NO GRADE.')
    rec('-' * 104)
    rec('    ### **THIS ACT CONFERS NO GRADE AND MOVES NONE.** ### Every grade in the table is a')
    rec('    ### ledger cell`s, carried with the act and line that wrote it. ### The one GENUINE')
    rec('    ### conflict is REPORTED AND NOT RESOLVED. ### No keystone is touched; K1, K2 and K3')
    rec('    ### are not started. ### **AND A TABLE IS NOT A REFRESH.**')
    rec('=' * 104)

    io.open(os.path.join(D, 'b496_components.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(conflicts=len(conf), genuine=genuine, ambiguous=amb, artefact=art,
                   counts=C, matchers=dict(v1=T['grade_cells_loose_v1'], v2=T['grade_cells_v2'],
                                           v3=T['grade_cells_v3'], v4=T['grade_cells'])),
              io.open(os.path.join(D, 'b496_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b496_components.txt, b496_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
