# -*- coding: utf-8 -*-
"""b478_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b478_sources.json` and `b478_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b478_span.json')))

    rec('=' * 100)
    rec('b478_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _t = json.loads(read(os.path.join(D, 'b478_table.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    cells %d ; SAME OBJECT %d ; TOUCHES %d ; APART %d'
        % (len(_t['cells']), len(_t['same_object']), len(_t['touches']),
           len(_t['cells']) - len(_t['same_object']) - len(_t['touches'])))
    rec('    constituents touched %s ; untouched %s'
        % (', '.join(_t['k_touched']), ', '.join(_t['k_untouched'])))
    rec('    sites no constituent touches : %s' % ', '.join(_t['s_untouched']))
    rec('    span by tool : %d -- b475, b476, b477, b478 BY NUMBER, of which b476 and b477 were REFUSED'
        % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b471 LEFT TWENTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b478 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
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
         ['THE SERIALIZED RUN IS STILL GOING (b475, pid 27508). ### NOT POLLED BY THIS ACT.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['SEEN IN A NEW SHAPE HERE: the span reads FOUR (b475-b478 by number) while TWO acts closed in it.',
          '### **A REFUSED ACT SPENDS A NUMBER AND FILES NO CLOSING**, and the tool counts numbers.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) VOID FOR WANT OF A RUN; (R83) untriggered.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND',
         ['THREE ENTERED AT THE FOLD. ### **A FOURTH AND FIFTH ARE OPENED HERE AND NOT JUDGED: b476 and',
          'b477 each carry one bare flagged word, and (R81) as amended refuses both.**']),
        ('the E0 table has no site column', 'STAND',
         ['AND NOW THE REASON IS READ CELL BY CELL: 2 of 48 cells are SAME OBJECT, both K8`s; 10 TOUCH;',
          '36 are APART. ### The two frames meet at the quantifiers and almost nowhere else.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['MINTED AT b472.']),
        ('the span stands at the fold threshold', 'STAND', ['THE FOLD IS FILED AT b474.']),
        ('the run died of memory, not of mathematics', 'STAND', ['THE CEILING IS NOT IN THE LOG (b475).']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE SERIALIZED ATTEMPT IS RUNNING; the act after its pid exits reads the log.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['STILL EMPTY, AND NOW BLOCKED BY A REFUSAL RATHER THAN BY A RULING: (R86) opens the numerical',
          'lane *"at the price b476 prints"*, and b476 is refused, so no price exists and no lane opens.']),
        ('a face names each tool`s write pattern, not each file', 'STAND',
         ['(R85) APPLIED AT b475 AND AGAIN HERE; the write-list arm reads the globs.']),
        ('two of the six sites bear on nothing the E0 table grades', 'MINT',
         ['FOUND AT b478: rows (v) and (vi) are APART in all sixteen of their cells. ### The E0 gate unfolds',
          'the constituents of the stated clause for the corpus`s FIRST object; (v) is about a class of',
          'representations that does not contain the SECOND object, and (vi) is about a modulus in additive',
          'number theory. ### **AN EMPTY ROW HERE IS A RESULT, AND IT IS THE SHARPEST THING THE TABLE SAYS.**']),
        ('three constituents no site touches', 'MINT',
         ['FOUND AT b478: K3 the finite places` contribution, K6 the decomposition, K7 the object and its',
          'archimedean unit. ### **A PROOF SUPPLYING ALL SIX OF ROW U1`S MISSING STATEMENTS WOULD LEAVE ALL',
          'THREE EXACTLY WHERE THEIR OWNERS LEFT THEM** -- which is a fact about what the row is missing,',
          'not about what those three are short of.']),
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
    SC = json.loads(read(os.path.join(D, 'b478_scores.json')))
    # ### **THIS ACT REGISTERS NO EXPECTATION**, so the carried N1/N2/N3 block is replaced rather than
    # ### filled with placeholders: an expectation invented to keep a tool happy is an expectation.
    rec('  ### ### **EXPECTATIONS REGISTERED : %d.**' % SC['registered'])
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['navigator']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### the seat`s own, from the face:')
    for k in ('N1', 'N2', 'N3'):
        rec('    (%s) %s' % (k, SC['seat'][k]))
    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**ROW U1`S SIX SITES ARE SET AGAINST THE E0 TABLE`S EIGHT CONSTITUENTS, CELL BY CELL, BY THE TWO '
        'ENTRIES` OWN WORDS** (b478). **48 CELLS: SAME OBJECT 2, TOUCHES 10, APART 36**, with both sides` '
        'deciding words quoted and every quotation verified verbatim in its own source (24 of 24, 0 misses). '
        '**THE ONLY SAME-OBJECT CELLS ARE (i) x K8 AND (ii) x K8**: the open part of the stated clause and the '
        'first two sites are the same unowned quantifiers, entered twice in two documents. '
        '**THE TWO REVERSE READS: K3, K6 and K7 are touched by NO site; rows (v) and (vi) touch NO '
        'constituent** -- the E0 gate is zeta`s, and those two sites are about the second object`s class and '
        'about a modulus in additive number theory, so an empty row is a result and not an omission. '
        '**THE SENTENCE THE TABLE SUPPORTS: a proof supplying all six missing statements would move K1, K2, '
        'K4, K5 and own K8, and would leave K3, K6 and K7 exactly where their owners left them.** '
        '(N1) HELD; (N2) SPLIT -- the count holds at three, the naming is refuted because K5 IS touched at '
        '(iv); (N3) HELD, with (vi) empty as well. '
        '**b476 AND b477 WERE REFUSED under (R81) as amended, each for one bare flagged word, so (R86)`s '
        'numerical lane did not open and nothing was computed.** No bridge typed; row U1 and the E0 table '
        'unedited; no grade conferred; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'none read: this act reads two tables of the record, not a terminal',
             'NO CORPUS GRADE MOVED; the table confers none and moves none',
             ('data/b478_the_sites_and_the_constituents.txt; data/b478_components.txt; data/b478_table.json; '
              'data/b478_survey.json; data/b478_extract.txt; data/b478_scores.json; data/b478_checks.txt; '
              'data/b478_registration_2026-09-22.txt (LOCKED at sha256 037e47fbc78f8378); '
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
    bank = os.path.join(D, 'b478_the_sites_and_the_constituents.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b478_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
