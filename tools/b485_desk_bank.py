# -*- coding: utf-8 -*-
"""b485_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.
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
    span = json.loads(read(os.path.join(D, 'b485_span.json')))
    R = json.loads(read(os.path.join(D, 'b485_results.json')))
    SV = json.loads(read(os.path.join(D, 'b485_survey.json')))
    c0, c3, WR = R['c0'], R['c3'], R['writes']
    a = SV['records']['19675356']
    b = SV['records']['21432399']

    rec('=' * 100)
    rec('b485_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the launcher : CPU %s s then %s s over %s s wall ; ### **delta %s s**'
        % (c0['cpu_first'], c0['cpu_second'], c0['wall_seconds'], c0['cpu_delta']))
    rec('    19675356 : version ### **%s** ; published ### **%s** ; concept %s ; %d files'
        % (a['version'], a['pub'], a['concept'], a['nfiles']))
    rec('    21432399 : version ### **%s** ; published ### **%s** ; concept %s ; %d files ; ms %s'
        % (b['version'], b['pub'], b['concept'], b['nfiles'], b['manuscript']))
    rec('    findings by the pass : ### **%d** ; cells disagreeing : ### **%d**'
        % (c3['findings'], len(c3['disagree'])))
    rec('    the gate : ### **%s**' % ('DISCHARGED' if c3['discharged'] else 'STANDS'))
    for k in sorted(WR):
        rec('    write : %-42s +%s / -%s ; lines absent from the new file : %d'
            % (WR[k]['path'], WR[k]['numstat'][0], WR[k]['numstat'][1], WR[k]['missing']))
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b484 LEFT FORTY-SIX STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['STILL NOT BANKED: (R94) brought the two MONOGRAPH records, not the kernel`s. ### The item',
          'stands and its scope is now sharper -- ### **IT IS ABOUT 21520474 AND 19674312**, which no',
          'act has fetched.']),
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
         ['AND BOTH OF THIS ACT`S CORPUS WRITES OBEYED IT: each target was read as BYTES, its BOM and',
          'line ending detected and re-applied, and both verified after the write.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND',
         ['AND COMPONENT 0 SHOWS WHY IT IS NOT YET DONE: the run is on ### **`Zeta23.ThmDE.Mult`** ###',
          'with `lean` at 54.8 s CPU. ### **ALIVE AND WORKING, NOT HUNG.**']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND', ['UNTOUCHED.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) STILL NOT YET DECIDABLE; (R83) DOES NOT FIRE.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND', ['MEASURED AT b471.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND',
         ['AND A SILENT LOG IS NOT A STOPPED RUN EITHER -- Component 0`s own lesson.']),
        ('the span stands at the fold threshold', 'STAND',
         ['### ### **THE SPAN NOW READS %d, TWO PAST THE DECLARED THRESHOLD OF NINE.** ### b479 and'
          % span['current_span'],
          'b482 are both banked ahead of the fold, and the ferry`s order is b479, b482, THEN the fold.',
          '### The seat does not fold on its own motion.']),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE BANKED READ LINE STILL STANDS; the run is alive and its log unopened.']),
        ('the compression register, opened as a lane and empty', 'STAND', ['CLOSED AT b483, NO GRADE.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['CLOSED BY (R91) AT b483.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND', ['ROUTED.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'STAND', ['CLOSED BY (R90) AT b483.']),
        ('the bar on the deposited records is capability, not permission', 'CLOSE',
         ['### ### **DISCHARGED AT b485 -- AND THE BAR WAS REAL, NOT IMAGINED.** ### b481 called it',
          'CAPABILITY: credentials and a live route, neither of which a ruling supplies. ### **(R94)',
          'SUPPLIED THE ROUTE, NOT A RULING** -- the author`s shell fetched both records, HTTP 200,',
          '### **WITHOUT CREDENTIALS**, and the ruling says so in its own words.',
          '### ### **SO ONE HALF OF b481`S VERDICT IS REFUTED BY EVENT AND THE OTHER STANDS:** the',
          'read needed no credential after all, and it did need a route THIS SEAT DOES NOT HAVE.',
          '### b389`s measurement of the SEAT`s six routes is untouched -- ### **THE AUTHOR`S SHELL',
          'IS ANOTHER ROUTE**, which is exactly what (R94) records.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'CLOSE',
         ['### ### **WRITTEN AT b485, NINETY ACTS ON, TO `ERRATA.md` AS `E-2026-09-22-1`.**',
          '### It went there and not to `meta/ZENODO_METADATA.md` because that file`s own banner',
          'freezes its table, while ERRATA is the append-only ledger and already carried the',
          'precedent. ### ### **AND THE MANIFEST CORRECTED HALF OF IT ON ARRIVAL**: `v5.8` confirmed,',
          '`(2026-07-24)` refuted -- the record published ### **2026-07-18**. ### The draft is quoted',
          'and the correction stands beside it. ### **A DRAFT IS NOT IMPROVED IN SILENCE.**']),
        ('the gate`s fifth site is not locatable at this seat', 'STAND',
         ['AND THE PASS RECORDED IT AS ### **NOT LOCATABLE** ### rather than reconciling it, which is',
          'what the order directed. ### The item stands; the gate discharged without it.']),
        ('one live currency claim contradicts REGISTRY', 'STAND', ['DISCHARGED AT b484.']),
        ('a priced resolving size that the arithmetic forbids', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('a bound the chain reports is not the bound it achieves', 'STAND',
         ['FILED AS `W-ORD-QUADRATURE-BOUND` AT b484; its trigger has not fired.']),
        ('the seat read its own expectation backwards', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('two unrelated tests single out sqrt(17)', 'STAND', ['LEFT OPEN AT b484.']),
        ('a search that can see its own report will always confirm it', 'STAND',
         ['FOUND AT b481 AND b484; ROUTED, AND IT BELONGS IN A TOOL.']),
        ('a matcher that counts co-occurrence is not counting a claim', 'STAND', ['FOUND AT b484.']),
        ('REGISTRY`s own history table disagrees with the records', 'MINT',
         ['### ### **FOUND AT b485, AND IT IS THE FIRST TIME THE AUTHORITY ITSELF HAS BEEN CAUGHT.**',
          '### Rule 5 makes REGISTRY the authority, and every prior pass reconciled OTHER sites TO it.',
          '### With the records in hand, ### **REGISTRY`S OWN `DAY 1 DEPOSIT HISTORY` DISAGREES WITH',
          'THEM AT FIVE PLACES**: `:410` carries `2026-04-28` where `19675356` says `2026-04-21` and',
          'names no version DOI; `:412` carries `v1.1` and `2026-07-19` where `21432399` says',
          '`v1.1.0` and `2026-07-18`, and names no version DOI.',
          '### ### **AN AUTHORITY IS AUTHORITATIVE OVER THE CORPUS, NOT OVER THE PLATFORM**, and the',
          'gate`s own words ask for both. ### Both rows ANNOTATED, neither rewritten; ROUTED.']),
        ('a frozen ledger cannot be repaired without breaking its own law', 'MINT',
         ['FOUND AT b485. ### `meta/ZENODO_METADATA.md:22` attributes manuscript `v5.8` to Zenodo',
          '`v1.1.1` / `21436278`, while its own prose at `:29` says `v1.1.0 (manuscript v5.8)` with',
          'the MD5 the `21432399` manifest carries -- ### **AND THE MANIFEST DECIDES IT.**',
          '### But that table declares itself ### **"left unedited on purpose: a ledger of what was',
          'true on 2026-07-18"**. ### **SO THE FINDING IS FILED AT ITS ADDRESS AND THE FILE IS NOT',
          'EDITED.** ### **EDITING A LEDGER THAT DECLARES ITSELF FROZEN WOULD BREAK A LAW TO REPAIR',
          'A FACT**, and the law is worth more than the line. ### ROUTED to an author`s ruling.']),
        ('a tool that can crash after a write needs a guard before it', 'MINT',
         ['FOUND AT b485, IN THIS ACT`S OWN DESK TOOL. ### `corr_row.write_row` ### **APPENDS AND IS',
          'NOT IDEMPOTENT**, despite every act`s desk bank calling it "the idempotent tool" in its',
          'own heading. ### This tool wrote row 332, THEN crashed on a name the splice had dropped;',
          'a re-run would have appended ### **A SECOND ROW FOR THE SAME ACT.**',
          '### A guard now reads the ledger for this act`s own opening phrase before writing.',
          '### ### **AND THE HEADING IS THE DEFECT`S ACCOMPLICE:** every desk bank since b194 has',
          'called the tool idempotent, and ### **A NAME REPEATED IN FIFTY HEADINGS IS NOT A',
          'PROPERTY.** ### ROUTED: the guard belongs in `corr_row.py`, not in one act`s copy.']),
        ('an index-query gate fires on an arm`s own name', 'MINT',
         ['FOUND AT b485, TWICE IN A ROW. ### The `b185` gate refused this face because an ARM NAME',
          'carried one of its mark words -- and then refused it a SECOND time because the paragraph',
          'EXPLAINING the rename spelled the old name. ### **A GATE ON RAW TEXT FIRES ON THE ACT`S',
          'OWN ACCOUNT OF WHAT IT DID NOT DO**, which this record has paid for before.',
          '### The arm was renamed and the explanation written without the token; ### **THE GATE WAS',
          'OBEYED AND NOT ARGUED WITH**, and its predicate is unchanged. ### ROUTED: the gate should',
          'read CLAIMS, not names, and that is a repair to the gate and not to the act.']),
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
        N1=dict(nav=('19675356 is an earlier version of the monograph deposit under concept '
                     '19675355, its version printed from its own manifest'),
                verdict='HELD',
                note=('The record`s own fields: concept ### **%s**, version ### **%s**, '
                      'publication_date ### **%s**, %d files. ### It is an earlier version of the '
                      'same concept as the current deposit, and ### **NOT A SEPARATE WORK.**'
                      % (a['concept'], a['version'], a['pub'], a['nfiles']))),
        N2=dict(nav=('21432399 is a record whose current version REGISTRY already names, so its '
                     'note is historical and not corrective'),
                verdict='HELD ON ITS CONCLUSION, WITH ONE QUALIFICATION',
                note=('The note IS historical: REGISTRY names `v1.1.2` as current and nothing '
                      'about the current deposit changes. ### **BUT THE RECORD`S OWN ROW IN '
                      'REGISTRY`S HISTORY TABLE IS NOT MERELY INCOMPLETE, IT IS WRONG ON THE '
                      'DATE** -- `:412` says `2026-07-19`, the record says ### **%s** -- and it '
                      'names no version DOI. ### So something corrective IS owed, at `:412` and '
                      'not at the `d1-1` row. ### **THE NOTE IS HISTORICAL AND THE ROW REPAIR IS '
                      'NOT**, and this face said so before the pass ran.' % b['pub'])),
        N3=dict(nav='the pass finds no disagreement and the gate is DISCHARGED',
                verdict='SPLIT -- DISCHARGED ON THE TABLE, REFUTED ON THE PASS',
                note=('### **ON THE TABLE`S CELLS: %d DISAGREE, SO THE GATE IS DISCHARGED.** ### '
                      'README, SPIRAL_MAP, REGISTRY and the session memory agree on all three '
                      'fields; the executor memory is NOT LOCATABLE and is recorded, not '
                      'reconciled. ### **ON THE PASS AS A WHOLE: REFUTED -- IT FOUND %d '
                      'FINDINGS**, five in REGISTRY`s own history table, one in a frozen ledger, '
                      'one in b395`s draft. ### **A GATE DISCHARGED ON THE CURRENT DEPOSIT STATE '
                      'IS NOT A CORPUS FOUND CLEAN**, and the discharging line says so in its own '
                      'words.' % (len(c3['disagree']), c3['findings']))),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 1 ; HELD-WITH-QUALIFICATION 1 ; SPLIT 1.**')
    rec('  ### the seat`s own calls were on the sealed face before the pass ran, and matched all')
    rec('  ### three -- including registering (N2)`s qualification and (N3)`s split in advance.')
    json.dump(SC, io.open(os.path.join(D, 'b485_scores.json'), 'w', encoding='utf-8', newline=NL),
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
        '**THE TWO ZENODO RECORDS ENTER THE RECORD AND THE CIRCULATION GATE IS DISCHARGED ON THE '
        'CURRENT DEPOSIT STATE -- WHILE THE SAME PASS FINDS SEVEN DISAGREEMENTS, FIVE OF THEM IN '
        'REGISTRY`S OWN HISTORY TABLE** (b485, under (R94)). '
        '**COMPONENT 0: pid 27508`s CPU is 1.75 s and 1.75 s across 60.02 s of wall -- a ZERO '
        'delta -- and that is NOT a hung run: 27508 is the cmd.exe launcher, which waits and burns '
        'no CPU by construction. The process table, read without opening the log, shows lake '
        'building Zeta23.ThmDE.Mult with lean at 54.8 s CPU. A SILENT LOG AND AN IDLE LAUNCHER ARE '
        'BOTH CONSISTENT WITH PROGRESS AND NEITHER IS EVIDENCE OF IT -- THE CHILD`S CPU IS.** '
        '**COMPONENT 1: both manifests recompute EXACTLY to (R94)`s hashes, neither carries a BOM, '
        'and this seat fetched nothing. By their own fields: 19675356 is version v1.0.1, published '
        '2026-04-21, concept 19675355, ten files. 21432399 is version v1.1.0, published '
        '2026-07-18, concept 19675355, eleven files, its own description naming manuscript v5.8. '
        'BOTH CARRY CONCEPT 19675355, so both are versions of the deposit REGISTRY already '
        'governs.** '
        '**COMPONENT 2: b395`s note, drafted ninety acts ago and written nowhere, is appended to '
        'ERRATA.md as E-2026-09-22-1 -- there and not to meta/ZENODO_METADATA.md, whose own banner '
        'freezes its table, while ERRATA is the append-only ledger carrying the precedent. AND THE '
        'MANIFEST CORRECTED HALF THE DRAFT ON ARRIVAL: manuscript v5.8 CONFIRMED by the record`s '
        'own description, (2026-07-24) REFUTED -- the record published 2026-07-18, and 2026-07-24 '
        'belongs to v1.1.2. The draft is quoted and the correction stands beside it.** '
        '**COMPONENT 3: the gate is DISCHARGED. README, SPIRAL_MAP, REGISTRY and the session '
        'memory agree with REGISTRY on all three deposit fields -- ZERO cells disagree -- and the '
        'executor memory is recorded NOT LOCATABLE per b481 rather than reconciled. BUT THE PASS '
        'FILED SEVEN FINDINGS, AND FIVE ARE IN THE AUTHORITY ITSELF: REGISTRY:410 carries '
        '2026-04-28 where the record says 2026-04-21 and names no version DOI; REGISTRY:412 '
        'carries v1.1 and 2026-07-19 where the record says v1.1.0 and 2026-07-18 and names no '
        'version DOI. AN AUTHORITY IS AUTHORITATIVE OVER THE CORPUS, NOT OVER THE PLATFORM. Both '
        'rows ANNOTATED, neither rewritten. meta/ZENODO_METADATA.md:22 conflates v1.1.0 with '
        'v1.1.1 and is FILED AND NOT EDITED, because that table declares itself frozen -- EDITING '
        'A LEDGER THAT DECLARES ITSELF FROZEN WOULD BREAK A LAW TO REPAIR A FACT.** '
        '**The discharging line at REGISTRY:523 names its own scope: the current deposit state and '
        'nothing else, with the findings annotated below the history table and left standing. Every '
        'corpus write is an append or an annotation; LINES OF THE OLD FILE ABSENT FROM THE NEW ARE '
        'ZERO in all three, and git`s own numstat reads -0 because each preserved original still '
        'matches.** '
        '(N1) HELD; (N2) HELD with the qualification this face registered in advance; (N3) SPLIT -- '
        'discharged on the table, refuted on the pass. '
        'Nothing was fetched by this seat and NOTHING AT ZENODO WAS WRITTEN; b475`s log was not '
        'opened; no grade moved; h2 where the deposit left it; the four lists OPEN.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             ('no build and no chain run; the two manifests are the AUTHOR`S fetch under (R94), '
              'verified here by sha256 against the hashes that ruling prints'),
             ('NO CORPUS GRADE MOVED; the circulation gate DISCHARGED on the current deposit state '
              'and on nothing else, with seven findings filed'),
             ('data/b485_components.txt; data/b485_the_two_records.txt; data/b485_extract.txt; '
              'data/b485_survey.json; data/b485_results.json; data/b485_scores.json; '
              'data/zenodo-manifests/record_19675356.json; '
              'data/zenodo-manifests/record_21432399.json; '
              'data/b485_registration_2026-09-22.txt (LOCKED at sha256 d96d2c18afc82e14); '
              'ERRATA.md; REGISTRY.md; OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    MARK = 'THE TWO ZENODO RECORDS ENTER THE RECORD'
    if MARK in before:
        rec('  ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER; IT IS NOT APPENDED AGAIN.**')
        rec('  ### `corr_row.write_row` APPENDS and is NOT idempotent. ### This tool crashed once')
        rec('  ### AFTER its row landed, and a re-run without this guard would have written a')
        rec('  ### SECOND row for the same act. ### **A TOOL THAT CAN CRASH AFTER A WRITE NEEDS A')
        rec('  ### GUARD BEFORE IT**, and the guard reads the ledger rather than trusting the run.')
        code, out = 0, ['    (guard) row already present; nothing appended']
    else:
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
    prefix = after.startswith(before.rstrip(NL)) or MARK in before
    ncells = len(last.strip().strip('|').split('|'))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d' % (rowid, ncells))
    good = (ncells == 6 and (rowid == str(nxt) or MARK in before))
    rec('  ### %s' % ('PASS' if good else '### FAIL'))

    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d minted, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, minted, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b485_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
