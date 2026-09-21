# -*- coding: utf-8 -*-
"""b463_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE FOLD'S ONE READING RULE IS THE VERDICT-STRING MATCHER**, and it is rehearsed here on
### the nine closing banks before the face is sealed: every string a row will carry is searched in
### that act's OWN closing, and its count is printed. ### **A STRING THAT MATCHES NOWHERE IS SEEN
### BEFORE THE FOLD CLAIMS IT WAS CARRIED.**
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
OUT = os.path.join(D, 'b463_extract.txt')
NL = chr(10)
L, MISSES = [], []

# ### THE ROWS. ### Each act, its subject, the verdict strings the fold will carry, and its column.
ROWS = [
    ('b454', '(R63) executed under (R64), and the span-heading work-order repaired',
     ['THE TWO COUNTS : ADDED 7 ; CLAIMED BY THE KEYSTONE AND HELD BY NO LEDGER 8 ; SUM 15 OF 15.',
      'TERMINAL VERDICT: NO RELATION IS DERIVES. THE CENSUS STAYS AT FIFTEEN OF SIXTEEN.'], 'RECORD', ''),
    ('b455', 'the deposit`s exhaustiveness claim read against its own route terminal',
     ['C2     MACHINE-CHECKED      NOT THE CLAIM',
      'C6     MACHINE-CHECKED      NOT THE CLAIM',
      'C4     MACHINE-CHECKED      DERIVES'], 'MODEL',
     'BORDERLINE -- it unfolds a kernel terminal, and grades the record`s own sentences by it'),
    ('b456', 'the errata entry, the live note, and the routed annotations completed',
     ['COMPONENT 1 -- ERRATA E-2026-09-14-1, APPENDED',
      'COMPONENT 3 -- THE PROFILE AT THE DEPOSITED TAG: ABSENT.'], 'RECORD', ''),
    ('b457', 'the profiles printed at the tag, and the sentence gate priced',
     ['structural_exhaustiveness_proved         STANDARD THREE',
      'SpectralCannonFull.spectral_cannon       STANDARD THREE',
      'ConservationBridge.riemann_hypothesis    STANDARD THREE',
      'S 45 items naming a declared theorem with a proof word'], 'MODEL', ''),
    ('b458', 'rulings (R65) through (R68) entered as records',
     # ### **THE REHEARSAL CAUGHT THIS ONE:** the first string was `RULINGS WITH FULLER TEXT IN
     # ### THE BANKED SCOPE : 4 OF 4.`, which lives in b458_components.txt and NOT in its closing.
     # ### ### **A FOLD MAY ONLY CARRY WHAT THE ACT`S OWN CLOSING SAYS**, so the closing`s own
     # ### wording is used instead. ### Both strings are on the record.
     ['ALL FOUR HAVE FULLER TEXT. `NO FULLER TEXT EXISTS IN THE RECORD` WAS NEVER PRINTED.',
      'THE FACE`S BLOCK RULE WAS DEFECTIVE AND THE DEFECT IS THE COMPONENT`S MAIN FINDING.'], 'RECORD', ''),
    ('b459', 'the six sites set against three candidate index sets',
     ['ALL THREE CANDIDATE INDEX SETS ARE `NOT THE INDEX SET`. ### 2 OF 18 CELLS EMBED.',
      'WHAT THIS DOES NOT SAY: that no index set exists.'], 'RECORD',
     'BORDERLINE -- G1`s range is read off an instrument`s own function'),
    ('b460', 'the b452 test given a positive control, and the TECHNE push',
     ['VERDICT : OBJECT-SIDE. ### THE CONTROL FIRES.',
      'A SECOND ROUTE TO THE SAME EDGE, SHARING NO ARGUMENT WITH THE FIRST:',
      'COMMITS NOW ON THE REMOTE THAT WERE LOCAL-ONLY BEFORE THIS ACT : 24'], 'MODEL',
     'BORDERLINE -- the cell is banked and the push is record-keeping'),
    ('b461', 'the suite given controls, and the arms that cannot have them retired',
     ['SIXTY-FOUR ARMS, AND NOT ONE OF THEM WAS EVER RUN AGAINST AN INPUT IT HAD TO FAIL ON.',
      'CARRYING BOTH CONTROLS EXERCISED TODAY      0',
      'RETIRED 3 ### given controls 61'], 'RECORD', ''),
    ('b462', 'the terminal-less census of the deposited surfaces',
     ['NAMES A TERMINAL 37 ### NAMES A CARRIER 82 ### NAMES NOTHING 300.',
      'AND 8 SAY `machine-checked` WHILE NAMING NO TERMINAL',
      'THE BIN IS NOT A DEFECT COUNT'], 'RECORD', ''),
]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def norm(s):
    """### **FOLD BOTH SIDES, NEVER ONE** -- the trap b436-b439 hit five times. ### Curly quotes,
    ### em dashes and runs of whitespace are levelled on the needle AND on the haystack alike."""
    s = (s.replace(chr(0x2019), "'").replace(chr(0x2018), "'")
         .replace(chr(0x201c), '"').replace(chr(0x201d), '"')
         .replace(chr(0x2014), '--').replace(chr(0x2013), '-').replace('`', "'"))
    return re.sub(r'\s+', ' ', s).strip()


def find(path, needle, label, show=150):
    ls = read(path).split(NL)
    hit = [(i + 1, l.strip()) for i, l in enumerate(ls) if needle in l]
    if not hit:
        MISSES.append((label, os.path.basename(path), needle))
        rec('      ### MISS : %s -- %r' % (label, needle))
        return None
    rec('      %s:%d | %s' % (os.path.basename(path), hit[0][0], hit[0][1][:show]))
    return hit[0][0]


def main():
    rec('=' * 104)
    rec('b463 -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).')
    rec('=' * 104)
    rec('')

    rec('(P1) THE FOLD`S STANDING FORM, READ OFF THE LAST FOLD RATHER THAN RECALLED.')
    find(OT, '### b453 — the fold at span eight — filed 2026-09-14', 'P1 the last fold`s heading')
    find(OT, 'One section appended to `FINDINGS.md` under a heading the span tool reads',
         'P1 what a fold writes', 190)
    rec('      ### **SO A FOLD WRITES EXACTLY TWO THINGS** -- one section appended to FINDINGS.md under a')
    rec('      ### heading the span tool reads, and one block appended to the (R31) digest -- plus its own')
    rec('      ### trail record. ### **AND NOTHING ELSE IS EDITED.**')
    rec('      digest : phase2/method/THE_FINDINGS_AS_THEY_STAND.md, present : %s' % os.path.exists(DIGEST))
    rec('')

    rec('(R70) THE REHEARSAL -- THE VERDICT-STRING MATCHER, RUN ON ALL NINE CLOSING BANKS.')
    rec('      ### every string a row will carry, searched in THAT ACT`S OWN closing, count printed.')
    rec('      ### **BOTH SIDES NORMALISED**: curly quotes, dashes, backticks and whitespace levelled.')
    tot, bad = 0, 0
    for act, subj, strings, col, note in ROWS:
        bank = os.path.join(D, '%s_closing.txt' % act)
        hay = norm(read(bank))
        rec('      %s  [%s]  %s' % (act, col, subj[:70]))
        for s in strings:
            c = hay.count(norm(s))
            tot += 1
            if c < 1:
                bad += 1
                MISSES.append(('R70 verdict string', '%s_closing.txt' % act, s))
            rec('          count %d  %s %s' % (c, '###MISS' if c < 1 else '   ok  ', s[:88]))
    rec('      ### ### **STRINGS CHECKED : %d. ### MATCHING NOWHERE : %d.**' % (tot, bad))
    rec('')

    rec('(P2) THE COLUMNS, AND THE ONE THAT STAYS EMPTY.')
    cols = {}
    for _a, _s, _st, c, _n in ROWS:
        cols[c] = cols.get(c, 0) + 1
    rec('      ' + ' ; '.join('%s %d' % (k, cols[k]) for k in sorted(cols)))
    rec('      ### ### **OBJECT : 0.** ### Nine acts, and not one of them made a statement about the')
    rec('      ### object -- about xi, about the Epstein object, or about any zero. ### That is a')
    rec('      ### PROPERTY OF THE SPAN and is carried as one, not offered as an achievement.')
    rec('')

    rec('(P3) THE CARRIED ARM FAILURES, LOCATED IN THEIR OWN BANKS.')
    find(os.path.join(D, 'b461_closing.txt'), 'b461_components.py     ### **A GENUINE BREACH**',
         'P3 b461 breach one', 120)
    find(os.path.join(D, 'b461_closing.txt'), 'b461_exercise.json     ### **A GENUINE BREACH**',
         'P3 b461 breach two', 120)
    find(os.path.join(D, 'b462_closing.txt'), 'IT IS NOT A BREACH. ### THE FACE DOES NAME IT',
         'P3 b462 the version-naming mismatch', 140)
    rec('      ### **AND (R73), THE AUTHOR`S, CLOSES THE MISMATCH BY MOVING THE CONVENTION:** a face')
    rec('      ### names every file by its full name, versions included. ### **THE ARM DOES NOT MOVE.**')
    rec('')

    rec('(P4) THE SPAN, BY THE TOOL, READ-ONLY.')
    out = subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '463'],
                         capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    for l in out.splitlines():
        if re.search(r'THE CURRENT SPAN|next span STARTS AT|runs through|last fold', l):
            rec('      ' + l.strip())
    rec('      ### **THE FOLD`S OWN SPAN IS THE FILING ACT EXCLUDED: b454-b462 IS NINE ACTS.**')
    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES[:3] or ''))
    rec('=' * 104)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0 if not MISSES else 2


if __name__ == '__main__':
    sys.exit(main())
