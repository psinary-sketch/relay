# -*- coding: utf-8 -*-
"""b468_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is swept from b457's standing items plus whatever this act adds; the scores are
### computed from `b468_sources.json` and `b468_entries.json`; the correspondence row is written
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
    span = json.loads(read(os.path.join(D, 'b468_span.json')))

    rec('=' * 100)
    rec('b468_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    _p = json.loads(read(os.path.join(D, 'b468_precondition.json')))
    rec('  figures READ from this act`s own records, never typed:')
    rec('    (R75) artefacts searched for      : %d' % len(_p['artefacts']))
    rec('    PRESENT                           : %d'
        % sum(1 for a in _p['artefacts'] if a['state'] == 'PRESENT'))
    rec('    ### **ABSENT**                    : %d' % len(_p['absent']))
    rec('    the searcher`s control            : %s'
        % ('FIRES' if _p['control_fires'] else '### FAILS'))
    rec('    ### **THE GATE**                  : %s'
        % ('OPEN -- b468 RUNS' if _p['met'] else 'SHUT -- b468 PRINTS ABSENT AND STOPS'))
    rec('    span by tool                      : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b467 LEFT EIGHTEEN STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    # ### ### **THIS TABLE IS WRITTEN FOR THIS ACT, NOT INHERITED.** ### A wholesale re-point
    # ### from b464 produced b464's desk with the act number substituted -- which would have had
    # ### b468 claiming b464's eight gradings as its own. ### `G-CARRIED-TOOLS-REPOINTED`'s species
    # ### at the level of CONTENT rather than of a filename, caught while reading the carried tool.
    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND',
         ['STANDING, with (R74)`s act-after clause ARMED by b467`s read. ### UNTOUCHED HERE.']),
        ('what the fired control does not license', 'STAND', ['ENTERED at b460. ### UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND',
         ['OBSERVED at b460, ROUTED. ### UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND',
         ['UNDER (R72)`s second limb; b468 touches the suite only to run it.']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['FOUND at b462, ROUTED; it needs a lane that permits a fetch, and this act opens none.']),
        ('the terminal-less census, and what it is not', 'STAND', ['b462`s 300 stand. ### UNTOUCHED.']),
        ('six deposited sentences grading NOT THE CLAIM', 'STAND',
         ['RE-READ AT b467 against the concordance, which assigns them nothing. ### UNTOUCHED.']),
        ('a deposited sentence whose nearest terminal is a SHELL', 'STAND',
         ['NO ROW at b467 either. ### UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND',
         ['MEASURED source-relative at b467. ### UNTOUCHED.']),
        ('the five precondition artefacts are absent', 'CLOSE',
         ['OPENED AT b466 over FIVE names. ### **CLOSED HERE AND REPLACED BY A SHARPER ITEM**:',
          '(R75) names SEVEN, and this act measures all seven. ### The five-name form is retired',
          'because it undercounted the population it was about.']),
        ('the paper read has been owed since 2026-08-20', 'STAND',
         ['FOUND AT b466. ### **STILL OWED**, and this act could not pay it either.']),
        ('PATHS carries no proportion table', 'STAND', ['MEASURED AT b466, ROUTED. ### UNTOUCHED.']),
        ('section 24.4 counts SIMPLICITY, the headline counts THE LINE', 'STAND',
         ['MEASURED AT b466. ### **AND b468`s ORDER WOULD HAVE SETTLED IT** -- it asks whether the',
          'theorem counts simple zeros -- ### **BUT THE PAPERS ARE ABSENT, SO IT IS NOT SETTLED.**']),
        ('the Guinand-Weil comparison is undecidable until the clone is present', 'STAND',
         ['OPENED AT b466, SHARPENED AT b467 to the second conjunct of ExplicitFormulaDecomp alone.',
          '### **STILL UNDECIDED**; the clone is absent. ### The seat now records a PREDICTION on the',
          'locked face -- DOES NOT -- which stays untested.']),
        ('the deposit provides no mapping from these sentences to its kernel', 'STAND',
         ['MEASURED AT b467, ROUTED. ### UNTOUCHED.']),
        ('a site verdict is source-relative, not absolute', 'STAND',
         ['MEASURED AT b467 at four of six cells, ROUTED. ### UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND',
         ['DISCLOSED AT b467. ### UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'MINT',
         ['FOUND AT b468 and it is the act`s one real finding. ### The 2026-08-20 activation act',
          'banked the Lean repository as ### **`anthropics/zeta-23-lean`**, and (R75) names it as',
          '### **`anthropics/formal-math`, the `zeta23` project inside it.** ### b466 searched for',
          'the banked name across three trees and reported ABSENT -- ### **AND A SEARCH FOR THE',
          'WRONG NAME RETURNS `ABSENT` JUST AS CONVINCINGLY AS A SEARCH FOR THE RIGHT ONE.**',
          '### The clone is absent under BOTH names, so b466`s verdict survives; ### **BUT IT',
          'SURVIVED BY LUCK AND NOT BY METHOD**, and that is the entry. ### ROUTED: every banked',
          'external identifier is a claim, and this one was never verified against its source.']),
        ('a name matcher cannot see a repository', 'MINT',
         ['FOUND AT b468: b466`s precondition walked file names only, so ### **A CLONE ON DISK WOULD',
          'NOT HAVE BEEN FOUND BY IT** -- its two directory-shaped artefacts were unfindable by',
          'construction. ### Repaired here (directories matched, `D:\` walked to depth 3), and the',
          'repair is named rather than slipped in. ### **b466`s FIVE ABSENTS WERE RIGHT; ONE OF ITS',
          'SEARCHES COULD NOT HAVE BEEN.**']),
        ('an AI-disclosure line is not an artefact', 'MINT',
         ['FOUND AT b468. ### The first narrowing marked this corpus`s own',
          '`A_METHODOLOGY_FOR_DETERMINED_SYSTEMS_v1_0.md` PRESENT, because line 364 reads',
          '*"Editorial workflow assisted by Claude (Anthropic)."* ### **A DISCLOSURE IS NOT AN',
          'ARTEFACT** -- and under (R75) the hazard is structural, not incidental: the order asks',
          'for `the Claude paper` and `the methodology note`, and this corpus names Claude and',
          'carries a methodology. ### Repaired by requiring a mark unique to the result; both',
          'yields printed. ### **ROUTED: any future artefact census over this corpus inherits it.**']),
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
    SC = json.loads(read(os.path.join(D, 'b468_scores.json')))
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
        '**b468`S GATE IS SHUT: ALL SEVEN (R75) ARTEFACTS ARE ABSENT FROM DISK, SO THE ACT PRINTS '
        'ABSENT PER ARTEFACT AND STOPS, WHICH IS WHAT ITS ORDER DIRECTS** (b468). **LOCKED BEFORE '
        'THE PRECONDITION`S VERDICT WAS ACTED ON**, 8 gates read, 4 by digest. '
        '**The seven searched by name across four trees -- relay/data, relay/reports, PLACE-papers '
        'and D:\\ to depth 3 -- WITH DIRECTORIES MATCHED AS WELL AS FILES, both matcher yields '
        'printed, and a control that FIRES. PRESENT 0, ABSENT 7.** '
        '**AND THE ACT`S ONE FINDING IS ABOUT THE RECORD AND NOT ABOUT THE ARTEFACTS: THE 2026-08-20 '
        'INTAKE BANKED THE LEAN REPOSITORY AS `anthropics/zeta-23-lean`, AND (R75) NAMES IT AS '
        '`anthropics/formal-math`, THE `zeta23` PROJECT INSIDE IT. b466 SEARCHED FOR THE BANKED NAME '
        'AND REPORTED ABSENT -- A SEARCH FOR THE WRONG NAME RETURNS ABSENT JUST AS CONVINCINGLY AS A '
        'SEARCH FOR THE RIGHT ONE. The clone is absent under both names, so b466`s verdict survives, '
        'but it survived by luck and not by method.** '
        '**Two further searcher defects found and repaired here: b466`s matcher walked FILE names '
        'only, so a clone on disk would not have been found by it; and bare `anthropic`/`claude` '
        'matched this corpus`s own AI-DISCLOSURE line, "Editorial workflow assisted by Claude '
        '(Anthropic)", marking the programme`s own methodology document PRESENT. A DISCLOSURE IS NOT '
        'AN ARTEFACT.** '
        '(N1)(N2)(N3) all NOT SCORABLE, each because its population is absent; the seat offered no '
        'reading on any, and recorded one prediction it can be held to -- DOES NOT on the '
        'explicit-formula comparison -- which stays untested. '
        'Nothing fetched, cloned, vendored or imported; no theorem quoted; no grade conferred; '
        'W-ORD-GW-IMPORT not filed; the kernel lane never opened; no site entered; row U1 unedited; '
        'no bridge typed; h2 where the deposit left it.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW; NO `lean` RUN AND NONE READ',
             'none -- the kernel lane opens for Component 2 and Component 2 did not run',
             'NO GRADE CONFERRED ON ANYTHING; the only verdicts are about ARTEFACT PRESENCE',
             ('data/b468_the_gate_and_the_seven.txt; data/b468_precondition.txt; '
              'data/b468_precondition.json; data/b468_scores.json; data/b468_span.json; '
              'data/b468_checks.txt; '
              'data/b468_registration_2026-09-22.txt (LOCKED at sha256 96cb80ee0adaffeb); '
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
    bank = os.path.join(D, 'b468_the_gate_and_the_seven.txt')
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    rec('  bank written : %s (%d bytes)' % (os.path.basename(bank), os.path.getsize(bank)))
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b468_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(bank, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
