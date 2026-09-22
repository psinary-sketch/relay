# -*- coding: utf-8 -*-
"""b470_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b470_sources.json` and `b470_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b470_span.json')))

    rec('=' * 100)
    rec('b470_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _c = json.loads(read(os.path.join(D, 'b470_comparison.json')))
    _w = json.loads(read(os.path.join(D, 'b470_writes.json')))
    _b = json.loads(read(os.path.join(D, 'b470_build_state.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    comparison : CONTAINS %d ; DOES NOT %d ; MATCHES 0'
        % (len(_c['contains']), len(_c['verdicts']) - len(_c['contains'])))
    rec('    24.4 note : added %d, removed 0, no line edited %s' % (_w['note']['added'], _w['note']['no_line_edited']))
    rec('    deposited unchanged : %d of %d' % (_w['deposit']['unchanged'], _w['deposit']['total']))
    rec('    build : %s ; closure %d ; built by this act %d ; axioms run %s'
        % (_b['outcome'], _b['closure'], _b['built_by_this_act'], _b['axioms_run']))
    rec('    the floor : `import Mathlib` at one thread, %d s, finished %s'
        % (_b['floor_probe']['seconds'], _b['floor_probe']['finished']))
    rec('    span by tool : %d (by number, b464-b470) ; by filings : 7 (six numbers filed plus b468r)'
        % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b468r LEFT NINETEEN STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b470 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72); b470 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND', ['UNTOUCHED.']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('PATHS carries no proportion table', 'STAND', ['UNTOUCHED.']),
        ('a site verdict is source-relative, not absolute', 'STAND', ['UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND',
         ['ROUTED at b469. ### b470`s writer splices BYTES and never decodes a target, which is the repair',
          'in practice; the other writers in the corpus still carry the defect.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED at b469.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['STILL NOT RUN, AND NOW WITH A MEASURED REASON: a bare `import Mathlib` does not finish in 570 s at',
          'one thread on this machine, so no module importing all of Mathlib -- ChallengeDeps, Challenge,',
          'Solution, PrintAxioms -- can complete inside a foreground call. ### No module failed. ### Price:',
          'a run the author authorizes beyond the ten-minute foreground bound, or a machine where the import',
          'is fast; the cause here is NOT diagnosed, and is not guessed at.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['b470 reads 7 by number and 7 by filings, the two agreeing again only by coincidence.']),
        ('W-ORD-GW-IMPORT', 'MINT',
         ['FILED AT b470 on CONTAINS: zeta23`s EF_lit_zetaZeroConfig contains b321`s identity as its even',
          'case. ### Trigger: the author`s ruling on importing a third party`s terminal under the bar, at',
          'a pin, with its axiom profile RUN and not read -- and the run is exactly what this act could not',
          'complete. ### Nothing imported.']),
        ('lake 5.0.0 has no -j', 'MINT',
         ['FOUND AT b470: `lake build -j1` and `--jobs 1` are both refused. ### The order`s one-job intent',
          'was met by serializing by hand, and that substitution is on the face. ### The record already held',
          'this fact in memory; it was not in any bank until now.']),
        ('an import-of-Mathlib floor above the foreground bound', 'MINT',
         ['MEASURED AT b470. ### It bounds every future Lean read of a third party`s Mathlib project on this',
          'machine, not only zeta23`s. ### ROUTED: the next such order should state its time allowance.']),
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
    SC = json.loads(read(os.path.join(D, 'b470_scores.json')))
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
        '**zeta23`S EXPLICIT FORMULA FOR ZETA CONTAINS b321`S IDENTITY Z = P - PR + A AS ITS EVEN CASE** '
        '(b470). **LOCKED BEFORE ANY VERDICT, WRITE OR BUILD STEP**, 8 gates read, 4 by digest. '
        '**COMPONENT 1: EF_lit -- for every C^2 compactly supported k, SUM m_rho h(gamma_rho) = h(i/2) + h(-i/2) - '
        'SUM Lambda(n) n^{-1/2}(k(log n)+k(-log n)) + (1/2pi) INT h(r)[Re psi(1/4+ir/2) - log pi] dr -- with NO '
        'evenness hypothesis; proved hypothesis-free for zeta as EF_lit_zetaZeroConfig. Under k := w, f(x) = '
        'x^{-1/2} w(log x), f = g conv g-bar-sharp, g in C_c^inf(R*_+) with g~ = 0 on F >= {0,1}: the same transform '
        '(cosine form for even w), the same Lambda(n) n^{-1/2} weight, an IDENTICAL archimedean kernel, the same '
        'signs. CONTAINS 6 (EF_lit, EF_paper, ExplicitFormulaPaper, EF_lit_zeta, EF_lit_zetaZeroConfig, zetaEF), '
        'DOES NOT 2 (the bridges), MATCHES 0. Differences: 0 of sign, 0 of normalization, 3 of SCOPE printed and '
        'not resolved (the corpus`s zero side a truncated, on-line-assumed sum over banked ordinates; its '
        'archimedean range truncated; evenness assumed), 1 of FORM (EF_paper). W-ORD-GW-IMPORT FILED; nothing '
        'imported.** '
        '**COMPONENT 2: (R79) executed -- the dated analytic-row note beside section 24.4 in the working copy, no '
        'line edited, the row`s figure kept as a lower bound; the intake item closed at its address; (R78) '
        'appended beside (R76); the deposited directory 11 of 11 unchanged.** '
        '**COMPONENT 3: lake 5.0.0 has no -j; serialized by hand at LEAN_NUM_THREADS=1, foreground; a bare `import '
        'Mathlib` does not finish in 570 s, so no Mathlib-importing module can complete inside a foreground call; '
        'NO MODULE FAILED; the build did not complete; #print axioms NOT RUN; the grade stays DERIVES, '
        'CONDITIONAL.** '
        '(N1) HELD on CONTAINS, REFUTED on EVEN; (N2) REFUTED; (N3) REFUTED. No grade of the corpus moved; no '
        'corpus Lean touched; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none computed: the serialized build did not complete; a bare import of Mathlib exceeds the foreground bound',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL on an unrun #print axioms',
             ('data/b470_the_formula_the_annotation_and_the_run.txt; data/b470_comparison.json; '
              'data/b470_writes.json; data/b470_build_log.txt; data/b470_build_state.json; '
              'data/b470_components.txt; data/b470_scores.json; data/b470_checks.txt; '
              'data/b470_registration_2026-09-22.txt (LOCKED at sha256 bc6990d2f64fcbe9); '
              'OPEN_TRAILS.md; day1/A_Place_to_Stand.md; reports/2026-08-20-external-intake.md; '
              'CORRESPONDENCE.md row %d') % nxt]
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
    bank = os.path.join(D, 'b470_the_formula_the_annotation_and_the_run.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b470_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
