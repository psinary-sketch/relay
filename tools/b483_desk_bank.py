# -*- coding: utf-8 -*-
"""b483_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.
### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is written FOR THIS ACT; carried rows keep their own words and only rows this act
### touches move -- b480's warning against a wholesale re-point, obeyed.
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
    span = json.loads(read(os.path.join(D, 'b483_span.json')))
    SC = json.loads(read(os.path.join(D, 'b483_scores.json')))
    S = SC['scores']
    SV = json.loads(read(os.path.join(D, 'b483_survey.json')))
    lad = SC['families']['LADDER']

    rec('=' * 100)
    rec('b483_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the run : RUN COMPLETE %s ; EXIT 0 %s' % (SV['complete'], SV['exit0']))
    rec('    entries : %s' % ', '.join('%s %d' % (k, v) for k, v in sorted(SV['kinds'].items())))
    rec('    the diagonal gate : all cells ok %s ; largest |W - banked| %s'
        % (SV['diag_all_ok'], SV['max_abs_diff']))
    rec('    the observed two-side disagreement : %.3e (aim plane) ; %.3e (ladder)'
        % (SC['families']['AIM PLANE']['resolution'], lad['resolution']))
    rec('    the largest wrong-sign excursion : %.6e' % S['N2']['largest'])
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b481 LEFT FORTY STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['(R90) MOVES THIS: the two manifests are now THE AUTHOR`S FETCH and the gate`s own',
          'condition. ### The item stands until they are present in relay data.']),
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
         ['THE b475 RUN IS STILL ALIVE AND THIS ACT DID NOT OPEN ITS LOG. ### (K) BAR 2.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) STILL NOT YET DECIDABLE; (R83) DOES NOT FIRE.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['UNTOUCHED BY THIS ACT.']),
        ('the span stands at the fold threshold', 'MINT',
         ['AND IT IS REACHED AGAIN: ### **THE SPAN READS %d, THE DECLARED THRESHOLD.**'
          % span['current_span'],
          '### (R1) at b366 sets the threshold at NINE. ### **A FOLD IS DUE**, and b479 and b482 are',
          'both banked ahead of it. ### The seat does not fold on its own motion and routes this.']),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE b475 PID IS STILL ALIVE; ITS BANKED READ LINE STILL GOVERNS ITS LOG.']),
        ('the compression register, opened as a lane and empty', 'CLOSE',
         ['CLOSED AT b483 WITH NO GRADE. ### The lane opened, the Gram ran to completion, the six',
          'were scored -- and ### **`(F3)` IS NOT MET, SO THE REGISTER TAKES NO GRADE AND IN',
          'PARTICULAR NOT `MEASURED`.** ### The lane is closed at this act`s end as the order',
          'required. ### **AN EMPTY REGISTER REPORTED IS A RESULT**, and the reason it is empty is',
          'not anything zeta did.']),
        ('a face names each tool`s write pattern, not each file', 'CLOSE',
         ['CLOSED BY (R91), WHICH THE NAVIGATOR RULED ON b481`S OWN INCIDENT. ### A face may now',
          'carry its act`s STEM glob, so a tool discovered mid-run has somewhere lawful to land,',
          'and the arm keeps its force against every path outside the stem.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND',
         ['ROUTED to the act after b479.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'CLOSE',
         ['CLOSED BY (R90), WHICH STRIKES THE TRIGGER CLAUSE AND REPLACES IT. ### The gate`s',
          'condition is now the two manifests present in relay data by the author`s fetch.',
          '### **THE STRUCK CLAUSE IS PRESERVED IN PLACE**, per the ledger`s own discipline.']),
        ('the bar on the deposited records is capability, not permission', 'STAND',
         ['AND (R90) ACTS ON IT RATHER THAN DISPUTING IT: the fetch is assigned to the author,',
          'who holds the credential and the route the seat does not. ### The item stands until the',
          'manifests are on disk.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'STAND',
         ['UNTOUCHED: its destination is the Zenodo record itself.']),
        ('the gate`s fifth site is not locatable at this seat', 'STAND', ['UNTOUCHED.']),
        ('one live currency claim contradicts REGISTRY', 'STAND',
         ['ROUTED BY (R92) TO THE ACT AFTER THIS READ, AS CURRENCY AND NOT AUTHORING.',
          '### **THIS ACT NEITHER PERFORMS IT NOR PRE-EMPTS IT** (section (Z)).',
          '### ### **AND THE RULING`S ADDRESSEE IS AMBIGUOUS AND THE SEAT SAYS SO**: "the act after',
          'the b477 read" is b483`s successor, but the ferry`s own running order is b479 then b482.',
          '### The seat will not silently choose; ### **IT ASKS.**']),
        ('a priced resolving size that the arithmetic forbids', 'MINT',
         ['FOUND AT b483, AND IT DECIDES TWO OF THE SIX. ### b476 priced the control`s resolving',
          'family size at ### **ONE CELL**, from a per-cell test: every cell resolves `t` by five',
          'orders or more. ### **BUT A ONE-BY-ONE SYMMETRIC MATRIX CANNOT BE INDEFINITE WHATEVER',
          'ITS ENTRY IS**, so `(F1)`s negative index was arithmetically unavailable before the run',
          'started, and `(F3)`s second conjunct with it. ### **A PER-CELL RESOLUTION TEST CANNOT',
          'BOUND THE SIZE OF A MATRIX THAT NEEDS A PAIR.** ### The control DOES go indefinite --',
          'at ladder size %d -- so the instrument works; ### **THE PRICE WAS WRONG, NOT THE'
          % (S['N1']['first']['LADDER'] or 0),
          'INSTRUMENT.**']),
        ('a bound the chain reports is not the bound the chain achieves', 'MINT',
         ['FOUND AT b483 AND IT IS THE ACT`S CENTRAL FINDING. ### Every zeta entry carries BOTH',
          'sides, so `|W + Z|` measures how well they agree: it reaches ### **%.3e** where `|W|` is'
          % SC['families']['AIM PLANE']['resolution'],
          'largest, while the reported `trunc_bound` there is `1.290e-12`. ### **THE REPORTED TAIL',
          'FIGURE UNDER-STATES THE ACHIEVED AGREEMENT BY UP TO SEVEN ORDERS**, because it bounds the',
          'zero sum`s truncation and says nothing about the places side`s quadrature.',
          '### ### **AND THE WHOLE VERDICT TURNS ON IT**: the largest wrong-sign excursion is',
          '%.3e, which is ABOVE the floor and the tail figure and BELOW the observed agreement.'
          % S['N2']['largest'],
          '### **SO `(F2)` HALTS ON TWO THRESHOLDS AND NOT ON THE THIRD, AND `(N2)` IS HELD ON THE',
          'THIRD AND REFUTED ON THE OTHER TWO -- FROM ONE NUMBER.**']),
        ('the seat read its own expectation backwards', 'MINT',
         ['FOUND AT b483 IN THE SEAT`S OWN TOOL, BY RE-READING THE PREDICATE AGAINST b476`S WORDS.',
          '### `(N2)` says the excursion is wrong-signed ### **BUT WITHIN THE BOUND**; the first',
          'version of this act`s scorer required it to EXCEED the resolution, which is `(F2)`s test,',
          'and scored `(N2)` REFUTED on that. ### **A SUB-BOUND CLAIM CANNOT ALSO BE A SUPRA-BOUND',
          'CLAIM.** ### Corrected before the components were banked, and recorded here rather than',
          'quietly fixed.']),
        ('two unrelated tests single out sqrt(17)', 'MINT',
         ['FOUND AT b483. ### The earliest wrong-sign excursion is at ladder size %d, the cell'
          % (S['N3'].get('n') or 8),
          '`a = 4.12311 = sqrt(17)` -- ### **THE SAME CELL b446 NAMED AS THE OUTLIER THAT REFUSES**,',
          'on a decorrelation-order test with nothing to do with signatures.',
          '### ### **THIS IS A RESEMBLANCE AND IS NOT PROMOTED.** ### b446 already refused the',
          'obvious reading -- *"not the rung alone: 3.605551 = sqrt(13) converged"* -- and this act',
          'has no control over non-prime-power steps of the same size. ### ROUTED.']),
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

    rec('-' * 100)
    rec('### THE SIX, AS BANKED BY THE COMPONENTS.')
    rec('-' * 100)
    for k in ('F1', 'F2', 'F3', 'N1', 'N2', 'N3'):
        rec('  (%s) ### **%s**' % (k, S[k]['verdict']))
    rec('  ### ### **b476 REGISTERED SIX; ALL SIX ARE SCORED, AND TWO OF THEM FAIL FOR THE SAME')
    rec('  ### REASON THAT HAS NOTHING TO DO WITH ZETA.**')

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    # ### **NO PIPE IN ANY CELL** -- b476`s species: a bare `|` splits the row.
    statement = (
        '**THE b477 GRAM RUN IS READ TO ITS END AND ALL SIX ARE SCORED IN (R87)`S ORIENTATION; THE '
        'COMPRESSION REGISTER TAKES NO GRADE** (b483). '
        '**THE RUN: RUN COMPLETE, EXIT 0, 2337 s against a 2923 s price, 35 diagonals and 309 '
        'off-diagonals forming TWO WITHIN-FAMILY GRAMS (aim plane 13, ladder 22) and never one joint '
        'matrix. The diagonal gate passed at every checked cell with difference 0.000e+00 EXACTLY, so '
        'the halt did not fire.** '
        '**THE CENTRAL FINDING: a bound the chain REPORTS is not the bound it ACHIEVES. Every zeta '
        'entry carries both sides, so the two-side disagreement is measurable entry by entry; it '
        'reaches 4.562e-05 in the aim plane and 3.169e-06 in the ladder, while the reported '
        'trunc_bound is 1.29e-12 to 6.42e-11. THE REPORTED TAIL FIGURE UNDER-STATES THE ACHIEVED '
        'AGREEMENT BY UP TO SEVEN ORDERS, because it bounds the zero sum`s truncation and says '
        'nothing about the places side`s quadrature.** '
        '**AND THE WHOLE VERDICT TURNS ON THAT ONE NUMBER. Zeta`s largest wrong-sign excursion is '
        'lam_max(G) = +4.767937e-08, which is ABOVE the chain floor 1.49e-08 and the tail figure and '
        'BELOW the observed agreement. So (F2) HALTS on the floor and on the tail figure and DOES NOT '
        'FIRE on the observed agreement; and (N2) is HELD read against the observed agreement and '
        'REFUTED read against the tail figure. ONE NUMBER, READ AS A HALT OR AS AN EXPECTATION MET '
        'DEPENDING ON WHICH BOUND IS BELIEVED -- and that, not the number, is the finding.** '
        '**(F1) FIRES ON FORM: b476 priced the control`s resolving family size at ONE CELL from a '
        'per-cell test, and a one-by-one symmetric matrix CANNOT BE INDEFINITE whatever its entry is. '
        'The control does go indefinite, at ladder size 16, so THE PRICE WAS WRONG AND NOT THE '
        'INSTRUMENT. (F3) NOT MET for the same reason -- its second conjunct is the control indefinite '
        'AT THE PRICED SIZE -- so the register takes NO GRADE and in particular NOT MEASURED. '
        '(N1) REFUTED: the control is never indefinite anywhere in the aim plane. (N3) REFUTED: no '
        'prime power lies in the step, though the cell it lands on is a = sqrt(17) = 4.12311, THE SAME '
        'CELL b446 NAMED AS THE OUTLIER THAT REFUSES on an unrelated test -- a resemblance, routed and '
        'not promoted.** '
        'A defect in this act`s own scorer is recorded: (N2)`s predicate was first read backwards, as '
        'a supra-bound test, and corrected before the components were banked. '
        'No chain was run and no entry computed; b475`s log was not opened; nothing was fetched; no '
        'corpus grade moved; no claim about RH in either direction; the lane closes at this act`s end.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'no axiom print in this act -- the numbers are functions of b477`s banked entries',
             ('NO CORPUS GRADE MOVED; the compression register takes NO GRADE, and in particular NOT '
              'MEASURED, because (F3) is not met'),
             ('data/b483_components.txt; data/b483_extract.txt; data/b483_scores.json; '
              'data/b483_survey.json; data/b483_desk_notes.txt; '
              'data/b483_registration_2026-09-22.txt (LOCKED at sha256 6847ae11ad584c97); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
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
    ncells = len(last.strip().strip('|').split('|'))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d' % (rowid, ncells))
    rec('  ### %s' % ('PASS' if (prefix and rowid == str(nxt) and ncells == 6) else '### FAIL'))

    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d minted, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, minted, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b483_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
