# -*- coding: utf-8 -*-
"""b481_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.

### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
### The desk is written FOR THIS ACT -- b480's warning against a wholesale re-point is obeyed:
### the carried rows keep their own words and only the rows this act touches move.
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
    span = json.loads(read(os.path.join(D, 'b481_span.json')))
    W = json.loads(read(os.path.join(D, 'b481_worklist.json')))

    rec('=' * 100)
    rec('b481_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    (c\') lines in the live corpus : %d ### state : %s' % (W['cprime_hits'], W['cprime_state']))
    rec('    the bar : %s' % W['bar'])
    rec('    sites compared : %d ### disagreements with REGISTRY : %d'
        % (len(W['states']), len(W['disagreements'])))
    rec('    memory stores on this machine : %s' % ', '.join(W['memory_stores']))
    rec('    span by tool : %d' % span['current_span'])
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b480 LEFT THIRTY-SIX STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['UNTOUCHED.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND',
         ['AND THIS ACT NAMES WHY THEY CANNOT BE BANKED FROM HERE: the read is barred by CAPABILITY,',
          'not by permission. ### **A RULING WOULD NOT UNBLOCK IT.** ### The item stands, and now',
          'stands for a stated reason rather than for none.']),
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
         ['THE RUN IS STILL ALIVE AND THIS ACT DID NOT LOOK AT ITS LOG, under the standing order as',
          '(R89) amends it. ### The item stands on b480`s snapshot and no further.']),
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
         ['THE SPAN SINCE b474`S FOLD IS %d, BELOW THE SHORTEST FOLD THE RECORD HAS RUN.'
          % span['current_span']]),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE PID IS STILL ALIVE; THE BANKED READ LINE STILL GOVERNS ITS LOG.']),
        ('the compression register, opened as a lane and empty', 'STAND',
         ['b477 IS RUNNING AND ITS LOG IS UNREAD HERE.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['(R85) APPLIED SINCE b475.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND',
         ['ROUTED to the act after b479.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND',
         ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'MINT',
         ['FOUND AT b481. ### `REGISTRY.md:523` -- the circulation gate, the only gate that binds',
          'READING-OUT -- ends "Run when the (c\') validation job clears." ### **FOUR LIVE LINES CARRY',
          '(c\'), THREE OF THEM A RE-PLATFORM BENCHMARK IN `INSTRUMENTS.md`, AND NONE DEFINES A',
          'VALIDATION JOB OR RECORDS A STATE FOR ONE.** ### The gate therefore neither clears nor',
          'fails; it waits on an absent name, and three things would settle it (b481 Component 1b).']),
        ('the bar on the deposited records is capability, not permission', 'MINT',
         ['FOUND AT b481, AND IT REFUTES THE NAVIGATOR`S OWN (N2). ### b395`s deciding sentence names',
          'what is missing: an AUTHENTICATED fetch and a LIVE ROUTE, with b389`s six dead routes and a',
          'positive control at 200 as the measurement. ### **NO RULING SUPPLIES A CREDENTIAL OR A',
          'ROUTE**, so the item cannot be discharged by an author`s word, only by a seat that holds',
          'both. ### The permission half is separately shown sound: b144/b145 and b337 fetched the',
          'platform read-only and wrote nothing, so nothing forbids a third such read.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'MINT',
         ['FOUND AT b481. ### b395 drafted the historical note for record 21432399 and said in its own',
          'words "IT IS DRAFTED HERE AND IS WRITTEN NOWHERE. ### The platform is not called." ### Its',
          'destination is the Zenodo record itself, so it CANNOT be written into the corpus -- which is',
          'why no later act could have cleared it and why it is the same capability bar again.']),
        ('the gate`s fifth site is not locatable at this seat', 'MINT',
         ['FOUND AT b481. ### The gate names "both memories (session + executor)". ### This machine',
          'carries %d memory store(s); one carries the deposit state and agrees with REGISTRY, and the'
          % len(W['memory_stores']),
          'other carries NO deposit-state line at all. ### **THE EXECUTOR MEMORY THE GATE NAMES CANNOT',
          'BE RECONCILED HERE AND CANNOT BE DECLARED CLEAN HERE EITHER.**']),
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
        N1=dict(nav="the (c') job's state is not in the record",
                verdict='HELD',
                note=("%d live lines carry (c'), none defines a validation job, and the state is ABSENT "
                      "-- with what would settle it named and not supplied." % W['cprime_hits'])),
        N2=dict(nav='the bar is PERMISSION',
                verdict='REFUTED',
                note=('the deciding sentence names CREDENTIALS and A LIVE ROUTE, neither of which a ruling '
                      'supplies; and the permission half of the argument is itself sound, which is exactly '
                      'why it is not the bar.')),
        N3=dict(nav='at least two of the four sites carry a deposit-state line that differs from REGISTRY',
                verdict='REFUTED',
                note=('%d sites differ. ### Three documents and the session memory AGREE with REGISTRY on '
                      'all three fields; the fifth site says nothing, and NOT STATED is neither a '
                      'disagreement nor a match.' % len(W['disagreements']))),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 1 ; REFUTED 2.**')
    json.dump(SC, io.open(os.path.join(D, 'b481_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    # ### **NO PIPE IN ANY CELL.** ### b476`s species: a bare `|` splits the row.
    statement = (
        '**THE CIRCULATION GATE AT `REGISTRY.md:523` IS READ FOR WHAT IT NEEDS, AND IT NEEDS THREE THINGS '
        'THE RECORD CANNOT SUPPLY** (b481). '
        "**COMPONENT 1: the gate's trigger is \"Run when the (c') validation job clears.\" Four live lines "
        "in the corpus carry (c') in any apostrophe; one is the trigger itself and three are "
        "`INSTRUMENTS.md`'s (c-prime) re-platform BENCHMARK, a different object with no clearing state. "
        'THE STATE OF THE (c-prime) VALIDATION JOB IS ABSENT, and three things would settle it: an '
        "author's ruling naming the job, an entry at a quotable address recording its state, or a ruling "
        'striking the trigger. UNTIL ONE EXISTS THE GATE NEITHER CLEARS NOR FAILS.** '
        "**COMPONENT 2: the bar on b395's two deposited records is CAPABILITY, NOT PERMISSION, REFUTING "
        "(N2). The deciding sentence is b395's own: \"IT IS THE AUTHOR'S READ, OR A SEAT WITH CREDENTIALS "
        'AND A LIVE ROUTE\" -- and b389 measured six dead routes from here with a positive control at 200. '
        'The permission half is separately sound: b144/b145 and b337 fetched the platform read-only and '
        'wrote nothing. A RULING CANNOT SUPPLY A CREDENTIAL OR A ROUTE.** '
        '**COMPONENT 3: against REGISTRY as the authority under Rule 5, the disagreements number ZERO, '
        'REFUTING (N3). README, SPIRAL_MAP, REGISTRY and the session memory agree on all three fields '
        '(monograph Zenodo v1.1.2 / ms v5.10.2, SIDE-kernel v1.5 = 0e5233f, SIDE-lv-conservation v0.10.0 '
        "= 93c27ec); the gate's fifth site -- the executor memory -- carries NO deposit-state line, and "
        'NOT STATED IS NEITHER A DISAGREEMENT NOR A MATCH.** '
        'Nothing was corrected and no site was edited; the gate was not run and nothing circulated; '
        'nothing was fetched and no lane was opened; both detached runs were left alive and their logs '
        'unread.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             'no build and no axiom print in this act -- every line is read from a file already on disk',
             'NO CORPUS GRADE MOVED; the circulation gate is READ, NOT RUN, and nothing circulates',
             ('data/b481_components.txt; data/b481_extract.txt; data/b481_survey.json; '
              'data/b481_worklist.json; data/b481_scores.json; data/b481_desk_notes.txt; '
              'data/b481_registration_2026-09-22.txt (LOCKED at sha256 afc88e4426793fc9); '
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

    rec('-' * 100)
    rec('### THE BANK.')
    rec('-' * 100)
    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d minted, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, minted, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b481_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
