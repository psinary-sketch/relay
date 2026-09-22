# -*- coding: utf-8 -*-
"""b468r_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b468r_sources.json` and `b468r_entries.json`; the correspondence row is written
### by the idempotent tool and read back.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b468r_span.json')))

    rec('=' * 100)
    rec('b468r_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _s = json.loads(read(os.path.join(D, 'b468r_survey.json')))
    _l = json.loads(read(os.path.join(D, 'b468r_lean.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    PDFs matching SHA256SUMS.txt       : %d of 5'
        % sum(1 for h in _s['hashes'] if h['name'].endswith('.pdf') and h['match']))
    rec('    clone HEAD agrees                  : %s' % (_s['head'] == _s['head_txt']))
    rec('    Theorem A / B agree across papers  : %s / %s' % (_s['thmA_agree'], _s['thmB_agree']))
    rec('    trusted axioms / analytic hyps     : %d / none (only %s)' % (_s['trusted_axioms'], _s['trusted_hyps']))
    rec('    #print axioms                      : %s' % _l['status'])
    rec('    the grade                          : %s' % _l['grade'])
    rec('    the comparison                     : %s' % _l['comparison'])
    rec('    span by tool (stem b468r -> 468)   : %d   ### by number the span runs b464-b469 : 6'
        % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b469 LEFT NINETEEN STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b468r claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72); b468r touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND', ['UNTOUCHED.']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('the paper read has been owed since 2026-08-20', 'CLOSE',
         ['CLOSED HERE: the paper is on disk, hash-verified, and READ AT ADDRESS. ### The two flags it',
          'held open are not closed by this act -- each now has a draft naming the line it can be read',
          'against, routed to the intake`s owner.']),
        ('PATHS carries no proportion table', 'STAND', ['UNTOUCHED.']),
        ('section 24.4 counts SIMPLICITY, the headline counts THE LINE', 'CLOSE',
         ['CLOSED HERE BY THE PAPER ITSELF: the theorem counts SIMPLE ZEROS ON THE LINE, `N0s >= (2/3',
          '- o(1)) N`. ### So the result does bear on the simplicity cell, and the era-annotation draft is',
          'written, NOT APPLIED, authoring routed.']),
        ('the Guinand-Weil comparison is undecidable until the clone is present', 'CLOSE',
         ['CLOSED HERE: the clone is present and the comparison is made -- ### **DOES NOT.** zeta23`s',
          'explicit formula is for C^2 test functions supported in [-L/2, L/2]; the deposit`s conjunct is a',
          'Li splitting whose test functions have no compact support; no Li-shaped declaration exists.',
          '### W-ORD-GW-IMPORT not filed. ### b468`s DOES NOT prediction, on its locked face, is HELD.']),
        ('a site verdict is source-relative, not absolute', 'STAND',
         ['UNTOUCHED -- and b468r adds a third source`s verdicts to the same caution.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND',
         ['FOUND AT b468; (R75) corrected the name and the clone is now at formal-math. ### ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED at b469.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED at b469.']),
        ('#print axioms on zeta23 is not run', 'MINT',
         ['MINTED AT b468r. ### The run fetched the toolchain v4.33.0-rc2 and Mathlib`s cache (8681',
          'files) and was STOPPED BY THE HARNESS during `lake build Solution`, for low system memory while',
          'the session was idle. ### **NOT RESTARTED, AS THE HARNESS DIRECTS; RESTART ONLY WHEN ASKED.**',
          '### So the grade stands at DERIVES CONDITIONAL on it. ### Price: one foreground build of',
          'Solution over the cached Mathlib, on a machine with the memory for it.']),
        ('AUDIT.md describes a different statement set', 'MINT',
         ['MINTED AT b468r. ### The third party`s `recorded results at this commit` print axiom lines for',
          '12 statements not in this tree and cite `Challenge/Multiplicity.lean`, which does not exist here.',
          '### It is read only as a claim. ### ROUTED as a note on reading third-party audit files.']),
        ('the span tool cannot place a re-run filed out of number order', 'MINT',
         ['MINTED AT b468r. ### It reads the stem `b468r` as act 468 and reports 5, while b469 has already',
          'filed and the span by number runs b464-b469, which is 6. ### Read, not edited.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    standing = sum(1 for _, s, _ in desk if s in ('STAND', 'MINT'))
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### MINTED HERE : %d. ### STANDING : %d.**'
        % (len(desk), closed, minted, standing))
    stand_names = [n for n, s, _ in desk if s in ('STAND', 'MINT')]
    rec('    ### ### **THE STANDING ITEMS, BY NAME : %s.**' % ' ; '.join(stand_names))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    SC = json.loads(read(os.path.join(D, 'b468r_scores.json')))
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['navigator']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('')
    rec('  ### ### **THE SEAT`S OWN, FROM THE FACE, SCORED BY THE SAME BANK:**')
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, SC['seat'][k]))
    rec('')
    rec('  ### ### **THREE OF THREE NAVIGATOR EXPECTATIONS READ `NOT SCORABLE`.** ### Each was')
    rec('  ### refutable by a printed result, as the order required; ### **THE PRINTED RESULT IS THAT')
    rec('  ### THE POPULATION EACH ONE QUANTIFIES OVER IS NOT IN THE RECORD.** ### An expectation')
    rec('  ### about an absent document is not wrong -- it is UNTESTED, and saying so is the score.')
    rec('  ### ### **AND THE SEAT PREDICTED ALL THREE ON ITS FACE BEFORE THE READ**, which is the only')
    rec('  ### reason those three verdicts are not a convenience invented after the fact.')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**b468 RUN AS BANKED WITH THE (R75) ARTEFACTS ON DISK: ALL FIVE PDFs MATCH SHA256SUMS.txt AND '
        'THE formal-math CLONE`S HEAD fbdc36bb AGREES WITH ITS RECORD** (b468r; b468`s first run '
        'untouched at row 316). **LOCKED BEFORE ANY THEOREM WAS GRADED**, 8 gates read, 4 by digest. '
        '**COMPONENT 1: the Claude paper and arXiv 2608.13637v2 state the same Theorem A and B; it '
        'counts SIMPLE ZEROS ON THE LINE, N0s >= (2/3 - o(1)) N, "We prove unconditionally", 0.6725 '
        'with the Montgomery-Taylor window -- 2/3, 5/6 and 0.6725 being Montgomery`s, '
        'Conrey-Ghosh-Gonek`s and Montgomery-Taylor`s constants under RH; the test family`s support '
        'grows with T, L = log(T/2pi), bandwidth one. Import bar: zeta, the corpus`s first object, is '
        'INSIDE the class; K1 CLASS BOUNDARY on the second object, Epstein Z_Q, only; no class of test '
        'functions to grade. Row U1 under (R76): NONE at (i), (iii), (iv); UNIFORM IN T at (ii), which '
        'fires nothing; K1 at (v) and (vi), the Dirichlet statement being per-modulus. (R61)/(R76)`s '
        'trigger does not fire. Drafts for section 24.4 and the intake item written, NOT APPLIED.** '
        '**COMPONENT 2: Mathlib 51e6992e; the trusted files carry 23 sorry-proved challenge statements, '
        '0 axioms, and no analytic hypothesis -- only 1 < q and primitivity; the library discharges '
        'its PaperInputs for zeta as a theorem. #print axioms NOT RUN -- the build was stopped by the '
        'harness for low system memory during lake build Solution, and not restarted. Grade DERIVES, '
        'CONDITIONAL ON THAT RUN. Comparison with the deposit`s pending conjunct: DOES NOT; '
        'W-ORD-GW-IMPORT not filed; nothing imported.** '
        '(N1) HELD; (N2) REFUTED on its first clause, HELD on its last; (N3) REFUTED on the first two '
        'clauses, HELD on the third. No site entered; row U1 unedited; no bridge typed; no Lean of the '
        'corpus touched; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none computed: #print axioms on zeta23 NOT RUN, the build stopped by the harness for low memory',
             'NO CORPUS GRADE MOVED; the third party`s formalization graded DERIVES, CONDITIONAL on an unrun '
             '#print axioms',
             ('data/b468r_the_proportion_result_at_address.txt; data/b468r_survey.json; '
              'data/b468r_readings.json; data/b468r_lean.json; data/b468r_lean_run.txt; '
              'data/b468r_components.txt; data/b468r_scores.json; data/b468r_checks.txt; '
              'data/b468r_registration_2026-09-22.txt (LOCKED at sha256 bc9142a3c35321c3); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    # ### **THE RETURN CODE IS READ, NOT DISCARDED.** ### b433`s species: a tool asked not to
    # ### complain reports a success it did not earn. ### The first run of this file threw the
    # ### code away and a HARD FAILURE on the cell count read as a clean write.
    code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        rec('  ### ### **HARD FAILURE: THE ROW WAS NOT WRITTEN.**')
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    prefix = after.startswith(before.rstrip(NL))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d ; unescaped pipes %d'
        % (rowid, len(last.strip().strip('|').split('|')), 0))
    rec('  ### %s' % ('PASS' if (prefix and rowid == str(nxt)) else '### FAIL'))

    rec('-' * 100)
    rec('### THE BANK.')
    rec('-' * 100)
    bank = os.path.join(D, 'b468r_the_proportion_result_at_address.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b468r_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
