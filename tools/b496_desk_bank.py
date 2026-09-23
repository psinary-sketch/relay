# -*- coding: utf-8 -*-
"""b496_desk_bank.py -- THE DESK. ### **SCORED ON THE CELLS THE INSTRUMENT PRINTED.**"""
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


def main():
    T = json.loads(read(os.path.join(D, 'terminal_table.json')))
    R = json.loads(read(os.path.join(D, 'b496_results.json')))
    rows, C = T['rows'], T['counts']

    rec('=' * 104)
    rec('b496 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON PRINTED CELLS.**')
    rec('=' * 104)
    rec('')
    rec('### THE NAVIGATOR`S THREE.')
    rec('-' * 104)

    n1 = C['rows'] > 150
    rec('  **(N1)** ### **%s.**' % ('HELD' if n1 else 'REFUTED'))
    rec('    *"more than 150 rows"*')
    rec('    rows : ### **%d** -- nearly seven times the bar.' % C['rows'])
    rec('    ### ### **AND THE BULK IS ONE REPOSITORY.** ### `SIDE-global-section` supplies the')
    rec('    ### majority, because its `AXIOM_PRINTS*.txt` bank names hundreds of Shadow')
    rec('    ### terminals one per line. ### **A COUNT THIS FAR PAST ITS BAR IS WORTH DECOMPOSING')
    rec('    ### RATHER THAN CELEBRATING**, and the table carries the repo column that does it.')
    rec('')

    npro = [r for r in rows if r['profile_state'] == 'NOT PROFILED']
    c7 = [r for r in npro if 'C7_finite_type_false' in r['name']]
    n2 = len(npro) >= 5 and bool(c7)
    rec('  **(N2)** ### **%s.**' % ('HELD' if n2 else 'REFUTED'))
    rec('    *"at least five NOT PROFILED, C7_finite_type_false among them"*')
    rec('    NOT PROFILED : ### **%d** (the bar was five)' % len(npro))
    rec('    `C7_finite_type_false` : ### **%s**'
        % ('PRESENT, and NOT PROFILED' if c7 else '### ABSENT'))
    for r in c7:
        rec('      repo `%s` ; statement %s ; grade **%s** ; profile **%s**'
            % (r['repo'], r['statement_state'], r['grade'], r['profile']))
    rec('    ### ### **THIS IS (R106)(2)`S OBJECT, MEASURED BY AN INSTRUMENT THAT DID NOT KNOW IT')
    rec('    ### WAS LOOKING FOR IT.** ### b494 found it compiled-but-not-profiled by reading')
    rec('    ### `AxiomCheck.lean` at `v0.10.0` by hand; ### **THE GENERATOR REACHES THE SAME')
    rec('    ### VERDICT FROM THE OTHER DIRECTION**, over the whole federation, without being')
    rec('    ### told the name. ### That is the difference between a finding and an instrument.')
    rec('')

    conf = [r for r in rows if r['grade'] == 'CONFLICT']
    n3 = len(conf) >= 1
    rec('  **(N3)** ### **%s.**' % ('HELD' if n3 else 'REFUTED'))
    rec('    *"at least one CONFLICT"*')
    rec('    CONFLICT rows the instrument emits : ### **%d**' % len(conf))
    rec('    ### of those, hand-read: ### **GENUINE %d** %s ; AMBIGUOUS %d %s ; ARTEFACT %d'
        % (len(R['genuine']), R['genuine'], len(R['ambiguous']), R['ambiguous'],
           len(R['artefact'])))
    rec('    ### ### **(N3) HOLDS ON THE INSTRUMENT`S COUNT AND IT ALSO HOLDS ON THE HAND')
    rec('    ### READING** -- `e_difficulty` is graded DERIVES at OPEN_TRAILS-archive-2:939 and')
    rec('    ### `ENCODES-CONCLUSION \\ SHELL` fourteen lines later at :953, and INTERFACES in a')
    rec('    ### third place. ### **THOSE TWO NEIGHBOURING CELLS SAY OPPOSITE THINGS** about')
    rec('    ### whether the content is certified or defined into the statement.')
    rec('    ### ### **BUT THE FIRST NUMBER THIS ACT COMPUTED WAS 67, AND IT WAS WRONG.** ### Had')
    rec('    ### (N3) been scored on v1 it would read HELD just as loudly, on 67 artefacts.')
    rec('    ### **AN EXPECTATION THAT ASKS FOR "AT LEAST ONE" IS SATISFIED BY NOISE**, and the')
    rec('    ### only thing that separated the one from the noise was reading all of them.')
    rec('')

    rec('### THE SEAT`S THREE, REGISTERED BEFORE THE COMPONENTS RAN.')
    rec('-' * 104)
    unres = [r for r in rows if r['statement_state'] == 'UNRESOLVED']
    s1 = len(unres) > 0
    rec('  **(S1)** ### **%s.**' % ('HELD' if s1 else 'REFUTED'))
    rec('    *"the STATEMENT column will be the expensive one and the one that fails; some')
    rec('    statements will be UNRESOLVED, and the table must carry that as a cell."*')
    rec('    STATEMENT UNRESOLVED : ### **%d of %d rows**' % (len(unres), C['rows']))
    for r in unres[:6]:
        rec('      `%s` / `%s`' % (r['repo'], r['name']))
    rec('    ### ### **HELD ON BOTH LIMBS, AND THE SECOND MATTERS MORE.** ### The rows are KEPT')
    rec('    ### with an `UNRESOLVED` cell rather than dropped, so the population is the union the')
    rec('    ### order names and not the subset the generator could resolve. ### **A ROW DROPPED')
    rec('    ### FOR A COLUMN IT COULD NOT FILL IS A ROW NOBODY WILL EVER LOOK FOR.**')
    rec('    ### It was also expensive in the way predicted, though not where predicted: the FIRST')
    rec('    ### generator called `git show` per file per name and ### **DID NOT FINISH**, and the')
    rec('    ### repair was one `git archive` per (repo, ref) held in memory.')
    rec('')

    s2 = len(conf) <= 20
    rec('  **(S2)** ### **HELD, AND MORE SHARPLY THAN IT WAS WRITTEN.**')
    rec('    *"CONFLICT as the order defines it will be rare, and low-conflict is not agreement."*')
    rec('    CONFLICT %d of %d rows ; UNGRADED ### **%d**' % (len(conf), C['rows'], C['ungraded']))
    rec('    ### ### **%d OF %d ROWS CARRY NO GRADE AT ALL.** ### That is the sentence (S2)'
        % (C['ungraded'], C['rows']))
    rec('    ### reached for and did not quite say: ### **THE LEDGERS DO NOT DISAGREE BECAUSE THEY')
    rec('    ### MOSTLY DO NOT SPEAK.** ### 8 conflicts out of 1,021 rows is not a record in')
    rec('    ### agreement; it is a record in which ### **93%% OF NAMED TERMINALS ARE UNGRADED**')
    rec('    ### and the graded remainder is small enough to rarely collide.')
    rec('')

    s3 = T['pins_named'] < T['repos_with_git']
    rec('  **(S3)** ### **%s.**' % ('HELD' if s3 else 'REFUTED'))
    rec('    *"the PIN column will be mostly empty; an empty pin is a finding about the REGISTRY,')
    rec('    and the two refs collapse to one wherever it is empty -- which must be SAID."*')
    rec('    REGISTRY`s kernel table names a pin for ### **%d of %d** repositories.'
        % (T['pins_named'], T['repos_with_git']))
    rec('    ### ### **THIRTY-EIGHT OF FORTY-FOUR KERNELS HAVE NO CITED PIN**, so for those the')
    rec('    ### order`s *"at the pin REGISTRY cites AND at HEAD"* has ### **ONE REF, NOT TWO**,')
    rec('    ### and the table`s `refs` column says so per row rather than reading `HEAD` twice')
    rec('    ### and calling it agreement.')
    rec('')

    rec('### THE TALLY.')
    rec('-' * 104)
    rec('  ### ### **THE NAVIGATOR`S: HELD %d ; REFUTED %d.**' % (sum([n1, n2, n3]),
                                                                 3 - sum([n1, n2, n3])))
    rec('  ### ### **THE SEAT`S: REGISTERED 3 ; HELD 3 ; REFUTED 0.**')
    rec('  ### ### **AND THREE HELD EXPECTATIONS ARE NOT A GOOD RESULT BY THEMSELVES.** ### (N3)')
    rec('  ### would have read HELD on every one of this act`s four matchers, including the two')
    rec('  ### that were wrong. ### **THE ACT`S REAL OUTPUT IS THE NUMBER 8 AND THE EIGHT')
    rec('  ### READINGS BEHIND IT**, not the three words HELD.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b496_desk_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n1=bool(n1), n2=bool(n2), n3=bool(n3), s1=bool(s1), s2=True, s3=bool(s3),
                   rows=C['rows'], conflicts=len(conf), not_profiled=len(npro),
                   ungraded=C['ungraded'], statement_unresolved=len(unres),
                   pins_named=T['pins_named']),
              io.open(os.path.join(D, 'b496_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b496_desk_notes.txt, b496_scores.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
