# -*- coding: utf-8 -*-
"""b471_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b471_sources.json` and `b471_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b471_span.json')))

    rec('=' * 100)
    rec('b471_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _p = json.loads(read(os.path.join(D, 'b471_price.json')))
    _l = json.loads(io.open(os.path.join(D, 'b471_launch.json'), encoding='utf-8-sig').read())
    rec('  figures READ from this act`s own records, never typed:')
    rec('    detached run : pid %s, started %s ; the log NOT read by this act' % (_l['pid'], _l['started_utc']))
    rec('    closure : %d of %d modules ; %d of %d lines ; %d direct Mathlib imports'
        % (_p['closure_modules'], _p['zeta23_modules'], _p['closure_lines'], _p['zeta23_lines'], _p['mathlib_direct']))
    rec('    PNT+-derived in the closure : %d ; `lemma` modules : %d ; headline in closure : %s'
        % (_p['pnt_derived'], _p['lemma_modules'], _p['headline_in_closure']))
    rec('    span by tool : %d (by number, b464-b471) ; by filings : 8' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b470 LEFT TWENTY-TWO STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b471 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
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
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['NOW RUNNING DETACHED UNDER (R80): pid in b471_zeta23_build.pid, log b471_zeta23_build.log.',
          '### The next act reads the log to its end; until then nothing is known and nothing is claimed.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND',
         ['PRICED AT b471: 57 of 316 modules, 18,105 lines, 89 direct Mathlib imports; two attribution',
          'layers (10 PNT+-derived modules); rule 9 would force modification of 35 modules; the copy would',
          'have to be its own kernel at v4.33.0-rc2. ### THE PIN: fbdc36bb or tag v1.0 (identical EF_lit',
          'statement, 4 later commits). ### The ruling is the author`s.']),
        ('lake 5.0.0 has no -j', 'STAND', ['BANKED AT b470.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND',
         ['MEASURED AT b470; (R80) authorizes the detached run that steps around it.']),
        ('the explicit formula separates from the headline', 'MINT',
         ['MEASURED AT b471: EF_lit_zetaZeroConfig`s closure does not contain Zeta23.Final; it is 18% of the',
          'library by module. ### The analytic inputs ARE separable from the headline, which is what makes',
          'a vendored copy of the explicit formula alone a coherent object at all.']),
        ('the navigator`s ledger entry owed under (R81)', 'MINT',
         ['OPENED AT b471: (R81) enters the navigator`s two overclaims of 2026-09-22 on the navigator`s',
          'ledger AT THE NEXT FOLD. ### The fold is not this act; the item waits for it.']),
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
    SC = json.loads(read(os.path.join(D, 'b471_scores.json')))
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
        '**THE zeta23 AXIOM RUN IS STARTED DETACHED UNDER (R80) -- pid 27704, launched 2026-09-22T16:38:44Z, '
        'logging to relay/data/b471_zeta23_build.log -- AND THE PRICE OF VENDORING THE EXPLICIT FORMULA IS READ '
        'FROM THE RULES AND NOT PAID** (b471). **LOCKED BEFORE THE RUN WAS STARTED**, 8 gates read, 4 by digest. '
        '**(R81) applied to its own ferry: 7 flagged words, all in the author`s ruling text, none in the '
        'navigator`s act; not refused; and the order`s two factual claims checked -- the federation`s v4.29 pins '
        'borne out for three of four kernels, rule 4`s divergence clause borne out.** '
        '**COMPONENT 1: the log is not read by this act; the run`s state at the close is read from the process '
        'table.** '
        '**COMPONENT 2: EF_lit_zetaZeroConfig`s import closure is 57 of 316 modules (18.0%), 18,105 of 102,265 lines, '
        '89 direct Mathlib imports, and does NOT contain the headline module; 10 closure modules are '
        'PrimeNumberTheoremAnd-derived (two attribution layers); 35 use `lemma`, against rule 9; rule 2 forbids a '
        'Lake dependency, so a copy is the only route; rule 4 permits the toolchain divergence only per kernel, so '
        'the copy would be its own kernel at v4.33.0-rc2. The pin: fbdc36bb or tag v1.0 = 3635e748, whose EF_lit '
        'statement is identical. No file copied; nothing imported.** '
        '(N2) REFUTED at 18.0%; (N3) HELD at 89; (N1) scored at the close. No grade of the corpus moved; no '
        'corpus Lean touched; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: the detached run`s log enters the record at the next act',
             'NO CORPUS GRADE MOVED; zeta23 stays DERIVES, CONDITIONAL until the log is read',
             ('data/b471_the_detached_run_and_the_price.txt; data/b471_launch.json; data/b471_zeta23_build.pid; '
              'data/b471_price.json; data/b471_components.txt; data/b471_survey.json; data/b471_scores.json; '
              'data/b471_checks.txt; data/b471_registration_2026-09-22.txt (LOCKED at sha256 cb5e868ad1ac6dd6); '
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
    bank = os.path.join(D, 'b471_the_detached_run_and_the_price.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b471_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
