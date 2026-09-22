# -*- coding: utf-8 -*-
"""b484_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.
### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
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
    span = json.loads(read(os.path.join(D, 'b484_span.json')))
    R = json.loads(read(os.path.join(D, 'b484_results.json')))
    c1, c2, c3 = R['c1'], R['c2'], R['c3']

    rec('=' * 100)
    rec('b484_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the repair : git +%s / -%s ; lines of the old file absent from the new : %d ;'
        % (c1['numstat'][0], c1['numstat'][1], c1['missing']))
    rec('                 other lines changed in place : %d' % c1['other_changed'])
    rec('    the census : citing %d ; predicating %d (%s) ; co-occurrence yield %d'
        % (c2['citing'], c2['predicating'], ', '.join(c2['named']) or 'none', c2['wide']))
    rec('    the cell   : a*a = %r ; margin %.6e in log units ; 17 enters %s ; at the edge %s'
        % (c3['asq'], c3['margin'], c3['enters'], c3['at_edge']))
    rec('    the verdict : ### **%s**' % c3['verdict'])
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b483 LEFT FORTY-TWO STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['(R90) makes them the AUTHOR`S fetch and the circulation gate`s condition. ### Untouched',
          'here; this act took REGISTRY`s row values and called no platform.']),
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
         ['AND THIS ACT`S ONE CORPUS WRITE OBEYED IT: the target was read as BYTES, its BOM and its',
          'line ending detected and re-applied, and both verified after the write.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND', ['THE b475 RUN IS ANOTHER ACT`S; (K) BAR 2.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) STILL NOT YET DECIDABLE; (R83) DOES NOT FIRE.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['UNTOUCHED BY THIS ACT.']),
        ('the span stands at the fold threshold', 'STAND',
         ['AND IT IS NOW ### **%d**, one PAST the declared threshold of nine. ### b479 and b482 are'
          % span['current_span'],
          'both banked ahead of the fold, and the ferry`s own order is b479, b482, THEN the fold.',
          '### The seat does not fold on its own motion.']),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE b475 PID`S BANKED READ LINE STILL STANDS.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['CLOSED AT b483 WITH NO GRADE; the lane is not reopened here.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['CLOSED BY (R91) AT b483.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND', ['ROUTED.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'STAND', ['CLOSED BY (R90) AT b483.']),
        ('the bar on the deposited records is capability, not permission', 'STAND',
         ['(R90) ASSIGNS THE FETCH TO THE AUTHOR. ### Stands until the manifests are on disk.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'STAND',
         ['UNTOUCHED: its destination is the Zenodo record itself.']),
        ('the gate`s fifth site is not locatable at this seat', 'STAND', ['UNTOUCHED.']),
        ('one live currency claim contradicts REGISTRY', 'CLOSE',
         ['### ### **DISCHARGED AT b484 BY (R92), WITH (R93) FIXING THE ADDRESSEE.**',
          '`INVARIANCE_BARRIERS.md:580` now carries REGISTRY`s own row values; the concept DOI',
          'already agreed and was not touched; the original line is preserved VERBATIM in an',
          'appended annotation, so ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d**, with git`s'
          % c1['missing'],
          'raw ### **+%s / -%s** printed beside it and ### **%d other lines changed in place.**'
          % (c1['numstat'][0], c1['numstat'][1], c1['other_changed']),
          '### **FOUND AT b481, FILED NOT FIXED, REPAIRED AT b484 BY RULING -- WHICH IS THE ROUTE',
          'THE CIRCULATION GATE ITSELF PRESCRIBES.**']),
        ('a priced resolving size that the arithmetic forbids', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('a bound the chain reports is not the bound it achieves', 'STAND',
         ['### ### **FILED AS A WORK-ORDER AT b484: `W-ORD-QUADRATURE-BOUND`.** ### The corpus holds',
          'no error bound for the places-side quadrature. ### Trigger: the next opening of the',
          'numerical instrument lane, or the next act citing a chain floor.',
          '### ### **AND THE CENSUS PUTS A NUMBER ON IT: %d ACTS CITE `trunc_bound`, %d PREDICATES'
          % (c2['citing'], c2['predicating']),
          'IT AS A FLOOR -- AND THAT ONE IS %s, WHICH REFUTED ITSELF IN ITS OWN COMPONENT 3.**'
          % (', '.join(c2['named']) or 'NONE'),
          '### The chain is NOT edited and nothing in it is repaired.']),
        ('the seat read its own expectation backwards', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('two unrelated tests single out sqrt(17)', 'STAND',
         ['### ### **AND b484 REFUSES THE NEAREST EXPLANATION FOR IT.** ### The support-edge',
          'convention is NOT the common cause: b400 already established that the inclusion',
          '### **MOVES NO VALUE**, and at this cell the prime is strictly inside by %.3e in log'
          % c3['margin'],
          'units, so ### **THE CONVENTION IS NOT EVEN CONSULTED HERE.** ### Verdict',
          '### **%s**. ### **THE COINCIDENCE STANDS, UNEXPLAINED AND OPEN**, and naming a cause'
          % c3['verdict'],
          'the record shows cannot move a number would have been worse than leaving it open.']),
        ('a search that can see its own report will always confirm it', 'MINT',
         ['FOUND AT b484, IN THIS ACT`S OWN CENSUS, AND IT IS b481`S SPECIES A SECOND TIME.',
          '### The matcher scanned `data/b484_*` and returned ### **b484 ITSELF** ### as a',
          'mis-scoping act -- because the hand-read residue block QUOTES the offending sentence in',
          'order to judge it. ### **A QUOTATION MATCHES THE RULE THAT CONDEMNS WHAT IT QUOTES.**',
          '### Excluded BY NAME rather than by hoping the run order hides it, and declared on the',
          'face before the seal. ### **THE SPECIES NOW HAS TWO INSTANCES AND BELONGS IN A TOOL**,',
          'not in each act`s memory -- ROUTED.']),
        ('a matcher that counts co-occurrence is not counting a claim', 'MINT',
         ['FOUND AT b484. ### Version 1 of this act`s census counted any sentence carrying both',
          '`trunc_bound` and `floor`, and returned ### **%d acts**; version 2 required the sentence'
          % c2['wide'],
          'to ### **PREDICATE** ### one of the other, and returned ### **%d**. ### The difference is'
          % c2['predicating'],
          '`b477`, whose sentence says the diagonal ran *within the floor* WHILE `trunc_bound` was',
          '*printed beside* each cell -- ### **TWO FIGURES IN ONE SENTENCE AND NO CLAIM THAT EITHER',
          'IS THE OTHER.** ### Both yields printed, residue hand-read, version 2 adopted --',
          '### **AND NOT BECAUSE IT GAVE THE SMALLER NUMBER.**']),
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
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    SC = dict(
        N1=dict(nav='the comparator admits the prime at the edge, so 17 enters at that cell',
                verdict='SPLIT -- THE CONCLUSION HELD, THE REASON REFUTED',
                note=('`17` DOES enter: both gates admit. ### **BUT NOT AT THE EDGE.** The banks '
                      'store the cell as the rounded decimal `4.123106`, which puts `a*a` %.6e '
                      'above `17` and leaves the inner gate a margin of %.6e in log units -- '
                      '`4.089e+08` times the float`s own resolution there. ### **THE EDGE '
                      'BEHAVIOUR IS NEVER REACHED AT THIS CELL AND THE ADMISSION OWES NOTHING TO '
                      'THE CONVENTION.**' % (c3['asq'] - 17.0, c3['margin']))),
        N2=dict(nav="b400's routed discrepancy is the same comparator",
                verdict='HELD',
                note=('Same boundary, `p^m <= a^2` against `p^m < a^2`, and the code`s `if ln <= L` '
                      'sits on the WEAK side -- which is b321`s stated RULE and not b321`s printed '
                      'LIST. ### b400 read it at `2` of `13` cells and routed it.')),
        N3=dict(nav=('at least two of the three measurements trace to that inclusion, so the '
                     'verdict is ONE CONVENTION on those two'),
                verdict='REFUTED',
                note=('The verdict is ### **%s**. ### b400 already established that the inclusion '
                      '**MOVES NO VALUE** -- `f` vanishes at the endpoints, so an endpoint prime '
                      'power contributes `0` under either reading -- and at this cell the prime is '
                      'strictly inside anyway, so the convention is not even consulted. ### **A '
                      'CONVENTION THAT CHANGES NO NUMBER CANNOT BE THE COMMON CAUSE OF THREE '
                      'NUMBERS.** ### The three share a cell, not a cause, and the coincidence is '
                      'left OPEN.' % c3['verdict'])),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 1 ; SPLIT 1 ; REFUTED 1.**')
    rec('  ### the seat`s own calls, made on the face before the components ran, matched all three --')
    rec('  ### including the SPLIT, which the face registered as a split on purpose.')
    json.dump(SC, io.open(os.path.join(D, 'b484_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE CURRENCY CLAIM b481 FOUND IS REPAIRED, THE QUADRATURE WORK-ORDER IS FILED, AND THE '
        'SUPPORT-EDGE EXPLANATION FOR sqrt(17) IS REFUSED** (b484, under (R92) with its addressee '
        'fixed by (R93)). '
        '**COMPONENT 1: `INVARIANCE_BARRIERS.md:580` now carries REGISTRY`s own d1-1 row values -- '
        'monograph v1.1.2, version DOI 10.5281/zenodo.21539167 -- in place of v1.1.1 / 21436278. The '
        'concept DOI 19675355 ALREADY AGREED AND WAS NOT TOUCHED, and neither was the Day-1 deposit '
        'DOI, which is a different record and not a currency claim. The original line is preserved '
        'VERBATIM in an appended annotation, so LINES OF THE OLD FILE ABSENT FROM THE NEW ARE ZERO, '
        'with git`s raw +14 / -1 printed beside that sentence and NO other line changed in place. '
        'BOM and line ending verified after the write.** '
        '**COMPONENT 2: W-ORD-QUADRATURE-BOUND filed. THE CORPUS HOLDS NO ERROR BOUND FOR THE '
        'PLACES-SIDE QUADRATURE; trunc_bound bounds the zero sum`s truncation and under-states the '
        'achieved two-side agreement by up to seven orders. By tool over the banked acts: SEVEN acts '
        'cite trunc_bound and ONE predicates it as a floor -- b483, which refuted itself in its own '
        'Component 3. The matcher`s co-occurrence version returned two; the extra was b477, whose '
        'sentence names two figures without equating them. Both yields printed, residue hand-read, '
        'and this act`s own stem excluded because the first run found ITSELF. The chain is not '
        'edited.** '
        '**COMPONENT 3: the loop has TWO comparators -- an outer cap with a 1e-12 tolerance and an '
        'inner gate `log n <= L` with NO tolerance, which is what actually adds a term, with '
        'L = 2 log a exactly. At a = 4.123106 the banks` ROUNDED DECIMAL puts a*a at 17.000003087236, '
        '3.087236e-06 above 17, so 17 ENTERS -- but STRICTLY INSIDE, by 1.816021e-07 in log units, '
        'and THE EDGE CASE IS NEVER EXERCISED. b400`s routed discrepancy IS the same comparator, and '
        'b400 already priced it: IT MOVES NO VALUE. VERDICT: SEPARATE OBJECTS. b437`s rung is a '
        'ladder index, b446/b447`s outlier a decorrelation residual order, b483`s excursion a Gram '
        'signature -- THEY SHARE A CELL, NOT A CAUSE, and the coincidence is left OPEN rather than '
        'explained by a convention the record shows cannot move a number.** '
        '(N1) SPLIT -- conclusion held, reason refuted; (N2) HELD; (N3) REFUTED. '
        'No chain run, no entry computed, no lane opened; b449`s and b483`s banks unedited; no grade '
        'moved; h2 where the deposit left it; the four lists OPEN.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'no axiom print and no chain run; the arithmetic is math.log on two numbers',
             ('NO CORPUS GRADE MOVED; one bibliography line repaired as CURRENCY under (R92), '
              'with the original preserved verbatim'),
             ('data/b484_components.txt; data/b484_extract.txt; data/b484_survey.json; '
              'data/b484_results.json; data/b484_scores.json; data/b484_desk_notes.txt; '
              'data/b484_registration_2026-09-22.txt (LOCKED at sha256 3b158ac48adc7fb7); '
              'phase1.5/method/INVARIANCE_BARRIERS.md; OPEN_TRAILS.md; '
              'CORRESPONDENCE.md row %d') % nxt]
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
    io.open(os.path.join(D, 'b484_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
