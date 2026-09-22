# -*- coding: utf-8 -*-
"""b474_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE FOLD'S ONE READING RULE IS THE VERDICT-STRING MATCHER**, and it is rehearsed here on the
### ten closing banks before the face is sealed: every string a row will carry is searched in that act's
### OWN closing, and its count is printed. ### **A STRING THAT MATCHES NOWHERE IS SEEN BEFORE THE FOLD
### CLAIMS IT WAS CARRIED.** ### The rulings of the span and the two ledgers are read at their addresses.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
DIGEST = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
OUT = os.path.join(D, 'b474_extract.txt')
NL = chr(10)
L, MISSES = [], []

# ### THE ROWS. ### Each act, its subject, the verdict strings the fold will carry, and its column.
ROWS = [
    ('b464', 'the eight machine-checked sentences unfolded, each graded against the nearest terminal at its pin',
     ['NOT THE CLAIM 6. ### INTERFACES 1. ### SHELL 1. ### DERIVES 0.',
      'THE POPULATION WAS RE-DERIVED, NOT READ FROM A BANK.'], 'RECORD', ''),
    ('b466', 'the Anthropic proportion result sought at address, and the precondition measured',
     ['FIVE OF FIVE ABSENT, WITH A CONTROL THAT FIRES.',
      'AND EVERY `ABSENT` CARRIES A CONTROL'], 'RECORD', ''),
    ('b467', 'the concordance read for the eight, and the general source`s parameters against (148)`s',
     ['THE CONCORDANCE ASSIGNS A ROW TO `0` OF THE EIGHT, AND THE REASON IS STRUCTURAL.',
      'FORM 3 FAILED ITS OWN POSITIVE CONTROL AND ITS RESULT WAS NOT BANKED.'], 'RECORD', ''),
    ('b468', 'the gate shut: all seven artefacts absent, and the repository name found wrong in the record',
     ['SEVEN OF SEVEN ABSENT, WITH A CONTROL THAT FIRES.',
      'A DISCLOSURE IS NOT AN ARTEFACT'], 'RECORD', ''),
    ('b469', 'the erratum, the live note and (R76) entered beside (R61)',
     ['THIS ACT WROTE TO LIVE SURFACES.',
      'AND THE ENTRY CALLS NOTHING PUBLISHED WRONG.'], 'RECORD', ''),
    ('b468r', 'the proportion result read at address with its artefacts present, site by site under (R76)',
     ['FIVE OF FIVE MATCH; THE CLONE\'S HEAD AGREES.',
      '(R61)/(R76)\'s TRIGGER DOES NOT FIRE.',
      'DERIVES, CONDITIONAL ON AN UNRUN #print axioms'], 'MODEL',
     'BORDERLINE -- it grades a third party`s terminal, which is a statement about a model and not about this record'),
    ('b470', 'zeta23`s explicit formula set against b321`s identity, and the foreground run`s floor measured',
     ['CONTAINS 6 ; DOES NOT 2 ; MATCHES 0.',
      'DIFFERENCES: SIGN 0 ; NORMALIZATION 0 ; SCOPE 3',
      'THE FLOOR, MEASURED: a bare `import Mathlib`, one thread, foreground -- UNFINISHED AT 570 s.'], 'MODEL',
     'BORDERLINE -- the comparison is of two statements of an explicit formula, and the floor is this machine`s'),
    ('b471', 'the axiom run started detached under (R80), and the price of vendoring read from the rules',
     ['MODULES 57 of 316 (18.0%) ; LINES 18,105 of 102,265 (17.7%) ; DIRECT MATHLIB IMPORTS 89',
      'NO FILE COPIED. NOTHING IMPORTED. THE RULING IS THE AUTHOR\'S.'], 'RECORD', ''),
    ('b472', 'the six statements a proof must supply, read from row U1, and the two external results placed',
     ['THE ACT`S OWN FINDING: THE E0 TABLE HAS NO SITE COLUMN.',
      'IN WHOLE : 0 IN BOTH ROWS.'], 'RECORD', ''),
    ('b473', 'the log read to its end, and (R82) decided',
     ['(R82) : VOID FOR WANT OF A RUN. ### (R83) : ITS TRIGGER DID NOT FIRE.',
      'THREE MODULES FAILED, ALL THREE FOR MEMORY:',
      'NO MODULE REPORTED A `sorry`, AN UNSOLVED GOAL OR A TYPE ERROR.'], 'MODEL',
     'BORDERLINE -- a build`s failure is a fact about this machine, and it is what denies the model`s profiles'),
]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


def norm(s):
    """### The matcher`s one normalisation: curly quotes, dashes, backticks and whitespace."""
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '--').replace('–', '-').replace('`', "'")
    return re.sub(r'\s+', ' ', s).strip().upper()


def main():
    rec('=' * 104)
    rec('b474 -- THE SURVEY. ### THE FOLD`S MATCHER, REHEARSED ON TEN CLOSING BANKS BEFORE THE SEAL.')
    rec('=' * 104)

    rec('')
    rec('(P1) THE REHEARSAL, UNDER (R70): EVERY STRING SEARCHED IN ITS OWN ACT`S CLOSING.')
    rec('-' * 104)
    total, matched = 0, 0
    for act, subj, strings, col, note in ROWS:
        bank = os.path.join(D, '%s_closing.txt' % act)
        hay = norm(read(bank))
        if not hay:
            MISSES.append((act, 'closing bank absent'))
        rec('    %-6s [%-6s] %s' % (act, col, subj[:84]))
        for s in strings:
            c = hay.count(norm(s))
            total += 1
            matched += 1 if c >= 1 else 0
            if c < 1:
                MISSES.append((act, s[:60]))
            rec('        count %d  %s' % (c, s[:96]))
    rec('  ### ### **STRINGS %d ; MATCHED %d ; UNMATCHED %d.**' % (total, matched, total - matched))
    cols = {}
    for act, subj, strings, col, note in ROWS:
        cols[col] = cols.get(col, 0) + 1
    rec('  ### columns : %s ### **OBJECT %d**'
        % (' ; '.join('%s %d' % (k, cols[k]) for k in sorted(cols)), cols.get('OBJECT', 0)))

    rec('')
    rec('(P2) THE SPAN, BY THE TOOL, AND WHAT THE LAST FOLD COVERS.')
    rec('-' * 104)
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '474'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'the last fold covers|FILED BY|next span STARTS AT|THE CURRENT SPAN|ACT\(S\)', l):
            rec('    ' + l.strip())
    m = re.search(r'THE CURRENT SPAN : (\d+) ACT', out)
    sp = m.group(1) if m else '?'
    rec('    ### the fold`s own span, this filing act excluded, as at b434, b444, b453 and b463 : 10')

    rec('')
    rec('(P3) THE RULINGS OF THE SPAN, (R74) TO (R84), EACH LOOKED FOR IN THE RECORD.')
    rec('-' * 104)
    ot = read(OT)
    rulings = {}
    for n in range(74, 85):
        key = '(R%d)' % n
        # ### **A `####` SUB-HEADING CONTAINS `### (Rnn)` AS A SUBSTRING**, so b471's trail heading
        # ### *"#### (R81), applied to its own ferry"* read as an entry. ### The test now anchors to a
        # ### line that BEGINS with exactly three hashes -- the entry form (R76) and (R78) use.
        entry = bool(re.search(r'^### \(R%d\)' % n, ot, re.M))
        ferry_hits = sorted(f for f in os.listdir(D)
                            if re.match(r'^b4\d\d_ferry(_refused)?\.txt$', f) and key in read(os.path.join(D, f)))
        rulings[key] = dict(entry_in_open_trails=entry, ferries=ferry_hits)
        rec('    %-6s entry in OPEN_TRAILS : %-5s ; ratified in : %s'
            % (key, entry, ', '.join(x.replace('_ferry.txt', '').replace('_ferry_refused.txt', ' (refused)')
                                     for x in ferry_hits) or 'NOT FOUND'))
    rec('  ### **(R76) AND (R78) ARE THE ONLY TWO WITH THEIR OWN OPEN_TRAILS ENTRY**; the rest are ratified')
    rec('  ### by their pastes and carried in the acts` trail records, which is how the record has held')
    rec('  ### rulings since (R80).')

    rec('')
    rec('(P4) THE TWO LEDGERS, AT THEIR ADDRESSES.')
    rec('-' * 104)
    b360 = [l for l in read(FINDINGS).split(NL) if 'b360' in l and ('h2' in l or 'wall' in l)]
    rec('    the navigator`s, carried by (R81) and (R84):')
    rec('      (1) the two overclaims of 2026-09-22 -- named in (R81), b471_ferry.txt:18-24')
    rec('      (2) (R81) refusing its author`s own next ferry -- b472_refusal.txt, relay eed5f8b')
    rec('      (3) b360`s sentence carried as a rule when it was a measurement -- (R84), b474_ferry.txt')
    rec('    the seat`s, each entered by its own act`s closing:')
    for act in ('b468r', 'b469', 'b470', 'b471', 'b472', 'b473'):
        c = read(os.path.join(D, '%s_closing.txt' % act))
        m2 = re.search(r'### ERRORS?[^\n]*\n', c)
        rec('      %-6s closing carries an errors section : %s' % (act, bool(m2)))

    rec('')
    rec('(P5) THE (R31) DIGEST, AND THE FOLD`S OWN MARKERS.')
    rec('-' * 104)
    dg = read(DIGEST)
    rec('    digest file : %s ; bytes %d' % (os.path.relpath(DIGEST, PP), len(dg)))
    rec('    prior orientation refreshes in it : %d' % dg.count('Orientation refresh'))
    mark_f = '<!-- b474 the fold: b464-b473, the external-reading arc -->'
    rec('    this fold`s FINDINGS marker already present : %s' % (mark_f in read(FINDINGS)))
    rec('    FINDINGS fold sections already filed : %d' % read(FINDINGS).count('— THE FOLD'))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    import json
    json.dump(dict(rows=[dict(act=a, subject=s, strings=st, column=c, note=n) for a, s, st, c, n in ROWS],
                   strings=total, matched=matched, columns=cols, span_tool=sp, rulings=rulings,
                   misses=MISSES),
              io.open(os.path.join(D, 'b474_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
