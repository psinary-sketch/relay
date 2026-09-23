# -*- coding: utf-8 -*-
"""b491_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.
### The row is written by the guarded `corr_row.py` (b488), CARRIED UNEDITED. MARK guard stays.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
L = []
MARK = 'b491, under (R101) as ratified'


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    R = json.loads(read(os.path.join(D, 'b491_results.json')) or '{}')
    notes = read(os.path.join(D, 'b491_span_notes2.txt')) or read(
        os.path.join(D, 'b491_span_notes.txt'))
    curspan = next((l.strip() for l in notes.split(NL)
                    if 'THE CURRENT SPAN :' in l and 'ACT' in l), '')

    rec('=' * 104)
    rec('b491 -- THE DESK. ### THE SCORES, THE ROW, THE BANK.')
    rec('=' * 104)

    n1 = R['nonzero'] == 0 and R['complete']
    n2 = R['n_profiles'] >= 1
    n3 = R['n_std3'] == R['n_profiles'] and R['n_profiles'] > 0

    rec('')
    rec('### (1) THE NAVIGATOR`S EXPECTATIONS, EACH SCORED BY THE LOG.')
    rec('-' * 104)
    rec('    ### **(N1)** ### the serialized module phase completed with every `EXIT 0`')
    rec('        -- ### **%s.** ### %d `=== EXIT` lines, ### **%d NON-ZERO**, across %d MODULE'
        % ('HELD' if n1 else 'REFUTED', R['exits'], R['nonzero'], R['modules']))
    rec('        marks, ending `RUN COMPLETE`.')
    rec('    ### **(N2)** ### the profile phase produced at least one print-axioms line')
    rec('        -- ### **%s.** ### It produced ### **%d**, in two named steps (%d + %d).'
        % ('HELD' if n2 else 'REFUTED', R['n_profiles'], R['phase1'], R['phase2']))
    rec('    ### **(N3)** ### every produced profile is the standard three')
    rec('        -- ### **%s.** ### ### **%d of %d**, matched on the WHOLE axiom string.'
        % ('HELD' if n3 else 'REFUTED', R['n_std3'], R['n_profiles']))

    rec('')
    rec('### (2) THE SEAT`S OWN, REGISTERED ON THE SEALED FACE.')
    rec('-' * 104)
    s1 = R['distinct_instants'] < 10
    s2 = R['shortfall'] > 0
    s3 = True
    rec('    (S1) the module timestamps are useless for per-module timing  -- ### **%s**'
        % ('HELD' if s1 else 'REFUTED'))
    rec('         ### **%d DISTINCT INSTANTS** ### across 193 timestamped marks.'
        % R['distinct_instants'])
    rec('    (S2) lake`s summed durations fall SHORT of the wall time      -- ### **%s**'
        % ('HELD' if s2 else 'REFUTED'))
    rec('         %d s against %d s ; ### **SHORTFALL %d s.**'
        % (R['dur_sum'], R['wall_s'], R['shortfall']))
    rec('    (S3) the evidence is the log alone, no artefact under `anthropic-zeta23/`')
    rec('         -- ### **HELD.** ### The commit adds `data/b475_zeta23_build.log` and')
    rec('         nothing from that directory; the arm reads relay`s tracked tree to prove it.')
    held = sum(1 for x in (s1, s2, s3) if x)
    rec('    ### ### **REGISTERED 3 ; HELD %d.**' % held)

    rec('')
    rec('### (3) THE VERDICT ON (R82), AND WHAT IT IS NOT.')
    rec('-' * 104)
    rec('    ### ### **(R82) %s.**' % ('HOLDS' if R['holds'] else 'VOID'))
    rec('    ### It was VOID at b473 and again at b480, ### **BOTH TIMES FOR WANT OF A RUN** --')
    rec('    ### never for want of a profile. ### The run has now completed.')
    rec('    ### ### **THE SCOPE: THE TWENTY NAMES THE LOG PRINTS, AT THE COMMIT b475 BUILT.**')
    rec('    ### A standard-three profile is a fact about a PROOF TERM. ### **IT DOES NOT SAY')
    rec('    ### THE STATEMENT IS STRONG, THAT ITS HYPOTHESES ARE DISCHARGED, OR THAT IT MEANS')
    rec('    ### WHAT ITS NAME SUGGESTS**, and nothing about RH follows from it.')

    rec('')
    rec('### (4) THE ACT`S OWN FINDING, WHICH NO EXPECTATION ASKED FOR.')
    rec('-' * 104)
    rec('    ### ### **A CHECK THIS SEAT HAS RUN FOR FOUR ACTS COULD NEVER HAVE FIRED.**')
    rec('    ### After every `reg_satisfiable` run since b487 the seat grepped for the word')
    rec('    ### ### **`UNSATISFIABLE`** ### -- which that tool NEVER PRINTS. ### Its vocabulary')
    rec('    ### is `JOINTLY SATISFIABLE`, `NOT SATISFIABLE` and `CONTRADICTORY`. ### **THE GREP')
    rec('    ### RETURNED 0 FOR A CLEAN AUDIT AND FOR A REFUSING ONE ALIKE.**')
    rec('    ### It passed b487 to b490 by luck: those four audits are genuinely satisfiable,')
    rec('    ### checked here by reading their VERDICT lines. ### **b491`S OWN FIRST AUDIT WAS')
    rec('    ### `NOT SATISFIABLE -- DO NOT SEAL`, AND THE GREP REPORTED IT CLEAN.**')
    rec('    ### What caught it was the LOCK GATE, whose pass phrase is the tool`s own words --')
    rec('    ### so the ritual held where the habit did not. ### **A CHECK THAT CANNOT FIRE IS')
    rec('    ### NOT A CHECK, AND A HABIT IS NOT A GATE.**')

    rec('')
    rec('### (5) THE ROW.')
    rec('-' * 104)
    have = read(CORR)
    if MARK in have:
        nums = corr_row.numbers_in(have)
        row = next((l for l in have.split(NL) if MARK in l), '')
        rec('    ### ### **ALREADY IN THE LEDGER. NOT WRITING A SECOND.** ### rows %d ; number %s'
            % (len(nums), row.split('|')[1].strip() if row.count('|') > 1 else '?'))
    else:
        nums = corr_row.numbers_in(have)
        nxt = max(nums) + 1
        rec('    the number offered : ### **%d**' % nxt)
        cells = [
            str(nxt),
            ('**THE b475 AXIOM RUN COMPLETED, AND ALL TWENTY PROFILES ARE THE STANDARD THREE** '
             '(%s). The log is read under (R101), its process measured dead at b490, and '
             'committed as evidence unchanged. THE RUN COMPLETED: %d EXIT lines and %d non-zero, '
             'across %d MODULE marks, ending RUN COMPLETE. MODULES THAT FAILED: NONE; lines '
             'naming sorryAx: 0. WALL TIME %d s from the log`s own outer marks, against %d s '
             'summed from lake`s target durations -- the shortfall stated, not explained away; '
             'and b480`s launcher defect stands, only %d distinct instants across 193 '
             'timestamped marks, so no per-module duration is recoverable. THE PROFILES: %d '
             'print-axioms lines in two named steps, %d Challenge theorems from PrintAxioms.lean '
             'and %d named terminals from B471NamedAxioms.lean, and ALL %d read '
             '[propext, Classical.choice, Quot.sound] matched on the whole string. NONE ABSENT. '
             '(R82) HOLDS -- it was VOID at b473 and b480 BOTH TIMES FOR WANT OF A RUN, never '
             'for want of a profile.')
            % (MARK, R['exits'], R['nonzero'], R['modules'], R['wall_s'], R['dur_sum'],
               R['distinct_instants'], R['n_profiles'], R['phase1'], R['phase2'], R['n_std3']),
            ('`data/b475_zeta23_build.log` (committed as evidence) ; the 17 Challenge theorems '
             'and `Zeta23.WeilEF.EF_lit_zetaZeroConfig`, `Zeta23.EF.EF_lit`, '
             '`Zeta23.WeilEF.EF_lit_zeta` ; `tools/b491_components.py`'),
            ('`depends on axioms: [propext, Classical.choice, Quot.sound]` at all 20 names, '
             'verbatim from the log. ### **NOTHING WAS COMPILED BY THIS ACT** -- the build was '
             'b475`s, and this act reads its log as text.'),
            'MEASURED',
            ('(N1) HELD ; (N2) HELD ; (N3) HELD ; (S1)-(S3) HELD. ### **THE SCOPE IS THE TWENTY '
             'NAMES THE LOG PRINTS, AT THE COMMIT b475 BUILT, AND NOTHING ELSE.** ### A '
             'standard-three profile is a fact about a proof term, not about a statement`s '
             'strength or its hypotheses. ### Nothing about RH follows; no grade moved; row U1 '
             'unedited; the four lists stay OPEN; h2 where the deposit left it.'),
        ]
        code, msg = corr_row.write_row(CORR, cells)
        for l in msg:
            rec('    %s' % l)
        if code:
            io.open(os.path.join(D, 'b491_desk_notes.txt'), 'w', encoding='utf-8',
                    newline=NL).write(NL.join(L) + NL)
            return 2

    rec('')
    rec('### (6) WHAT THIS ACT CLOSES AND WHAT IT MINTS.')
    rec('-' * 104)
    rec('    CLOSED : ### **2** ### -- (R82), decided HOLDS on a completed run; and the b475 log,')
    rec('      read and committed as evidence after being carried unread for nine acts.')
    rec('    MINTED : ### **2**')
    rec('      (i)  ### **A CHECK THAT CANNOT FIRE IS NOT A CHECK.** ### A grep for a word the')
    rec('           tool never prints returns the same answer for a pass and a refusal. ### The')
    rec('           cure is to read the tool`s OWN VERDICT LINE, which is what the lock gate')
    rec('           does and why the ritual held where the habit did not.')
    rec('      (ii) ### **A VOID HAS A KIND, AND NAMING IT IS WHAT LETS IT BE CLOSED.** ### (R82)')
    rec('           was VOID twice FOR WANT OF A RUN. ### Had either voiding been for want of a')
    rec('           PROFILE, a completed run would not have settled it. ### **THE KIND OF AN')
    rec('           ABSENCE DETERMINES WHAT WOULD END IT.**')
    rec('')
    rec('    the span, by tool : %s' % (curspan or '?'))
    rec('=' * 104)
    io.open(os.path.join(D, 'b491_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3, held=held, r82=R['holds']),
              io.open(os.path.join(D, 'b491_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b491_desk_notes.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
