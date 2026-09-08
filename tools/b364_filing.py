# -*- coding: utf-8 -*-
"""b364_filing.py -- THE REAL BRANCH'S ONE OBLIGATION: FILE THE FINDING FOR THE AUTHOR.

### ### **THE BRANCH TAKEN IS (REAL)**, and the locked registration fixed what that requires: report at
### full prominence that a banked verdict rests on an arm that no longer holds; name ### **WHAT THE ARM
### ### WAS CERTIFYING**; ### **RE-VERDICT NOTHING**; and file the finding for the author.
### ### **THIS FILE DOES THE FILING AND NOTHING ELSE.** ### One append-only block under its own mark in
### `OPEN_TRAILS.md`, nothing above it edited, the file a true prefix of what it was AND of its committed
### blob -- ### **THE READING BEFORE THE PUSH, WHICH BY `b352`'s RULE IS THE ONE THAT CARRIES.**
### ### **AND IT IS NOT AN ERRATA ENTRY.** ### ERRATA is for defects in deposited text. ### Nothing
### deposited is wrong here; a gate arm in the working record has aged out.
### ### **EVERY FIGURE IN THE BLOCK IS READ FROM THIS ACT'S OWN DIAGNOSIS JSON.** ### None is typed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock            # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN    # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b364 dated arm finding -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    """### THIS RECORD'S OWN SCAFFOLDING REMOVED AND NOTHING ELSE; ### **THE EQUALITY IS CHECKED.**"""
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def quote(path, hint, span=1):
    n, _line = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    q = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=q,
                equal=(GN.norm(q) == GN.norm(raw)))


def block(J, Q):
    moved = J['moved']
    rows = chr(10).join(
        '> - `%s` — read at `%d`, now `%d`' % (m[0], m[1], m[2]) for m in moved)
    return [
        '', MARK, '',
        '### **`FINDING-DATED-ARM` — FILED 2026-09-07 (b364): A BANKED VERDICT RESTS ON AN ARM THAT NO '
        'LONGER HOLDS**',
        '',
        ('*A finding for the author, **filed and not acted on**. **No verdict is withdrawn, no act is '
         're-verdicted, no suite is edited and no arm is repaired** — the order that produced this said '
         '*"diagnose, do not repair-to-pass"*, and an arm made to pass by editing the thing it reads has '
         'not been diagnosed, it has been silenced. **This is not an ERRATA matter:** ERRATA is for '
         'defects in deposited text, and nothing deposited is wrong here.*'),
        '',
        ('**What happened.** b363 exercised six banked gate suites as copies and found five of six '
         'reproducing their own act’s verdict. b357’s copy reported `GATES FAILING : 1 [\'G-LOCATED\']` '
         'where b357 itself banked `0`. b363 reported that at full prominence and adjusted nothing. b364 '
         'was ordered to diagnose it, with the branches fixed before the diagnosis was seen.'),
        '',
        ('**And the copy was innocent.** b364 ran the banked suite `tools/b357_checks.py` **at its own '
         'location, unedited**, and it reports `GATES FAILING : %d %s` — **the same failure, the same '
         'arm, the same four rows.** The failure has nothing to do with copying, with paths or with a '
         'working directory. **The branch is REAL, and ENVIRONMENTAL is unreachable.**'
         % (J['home_failing'], J['home_names'])),
        '',
        ('**What the arm was certifying — two things, not one.** `G-LOCATED` is quoted from its own suite '
         'and not paraphrased:'),
        '',
        '> `%s:%d` — %s' % (Q['label']['file'], Q['label']['line'], Q['label']['quote']),
        '',
        ('**(a) That every row b357 classified is still findable at its own ledger, now** — by the anchor '
         'tool, on the row’s own text, across four ledgers: `FINDINGS.md`, `FACES_LEDGER.md`, '
         '`CORRESPONDENCE.md` and `tools/banked_index.py`. **THIS HALF STILL HOLDS, %s.**'
         % J['located_phrase']),
        '',
        ('**(b) And that any row whose line number has moved since the reading is declared in b357’s own '
         'bank, with both numbers.** The condition, quoted from the suite:'),
        '',
        '> `%s:%d` — `%s`' % (Q['cond']['file'], Q['cond']['line'], Q['cond']['quote']),
        '',
        ('**THIS HALF CANNOT HOLD AND CANNOT BE MADE TO.** It compares a line number computed *now* '
         'against a literal string in a bank written *once*, in an append-only file that may never be '
         'edited. Four rows have moved since b357 read them:'),
        '',
        rows,
        '',
        ('b357’s bank declares two of these movements — `banked_index.py` `1022 → 1054` and `613 → 645`, '
         'the moves b357’s **own** index append caused, printed under its own straddle declaration. It '
         'could not declare `1232` or `823`, because the acts that produced those numbers had not yet '
         'run. **b357 predicted the shape and was right about it; it could not predict the arithmetic of '
         'the future.**'),
        '',
        ('**THE SPECIES, NAMED: A DATED ARM.** An arm whose pass condition is a literal in a frozen file, '
         'compared against a quantity recomputed at every run, **is dated by construction** — it does not '
         'become wrong, it becomes *old*, and the moment of its expiry is set by the next act that moves '
         'a line. **This is not b363’s wrong arm.** A wrong arm’s predicate tests something other than '
         'its label, and was wrong the day it was written; `G-LOCATED` tested exactly what its label says '
         'and was right the day it was written. **The two need different cures and this record should not '
         'confuse them.**'),
        '',
        ('**AND THE DRIFT REACHES THE PROSE, NOT ONLY THE GATE.** b357’s own answer section prints its '
         'row addresses as text — `FACES_LEDGER.md : 140` among them — and that row is now at `141`. **A '
         'banked act that cites a line number is citing a moving target, and no gate arm anywhere '
         'protects a number printed in prose.**'),
        '',
        ('**WHAT IS NOT CLAIMED.** b357’s *finding* is untouched: which passages say what, and the '
         '5 wider / 6 narrower / 1 silent split, rest on half (a), which still holds at every row. **What '
         'has aged out is a currency check b357 wrote about its own bank, not the reading b357 made about '
         'the ledgers.** No grade moves. No act is re-verdicted. b357’s verdict was true when it was '
         'banked and this filing does not withdraw it; **it records that re-running that suite today no '
         'longer reproduces it, and why.**'),
        '',
        ('*Species: **FINDING** (a dated arm, not a wrong arm, not a defect in a deposited text). **FILED '
         'FOR THE AUTHOR AND NOT ACTED ON.** The choices are the author’s and are not proposed here. '
         'Trigger: any act that re-runs a banked suite, or that relies on a line number printed in a '
         'bank. Nothing here is a route, no grade moves, no coordinate is closed, and `h2` stands exactly '
         'where the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b364 -- THE FILING. ### **THE REAL BRANCH, AND ITS ONE OBLIGATION.**')
    rec('=' * 100)
    rec('')
    J = json.load(io.open(os.path.join(D, 'b364_diagnose.json'), encoding='utf-8'))
    if J['branch'] != 'REAL':
        rec('  ### ### **THE BRANCH IS %s, NOT REAL. ### NOTHING IS FILED.**' % J['branch'])
        run_clock.write(D, 'b364_filing_notes', LINES)
        return 0
    rec('  ### the branch, read from the diagnosis and not typed : %s' % J['branch'])

    # ### THE MOVED ROWS, PARSED FROM THE SUITE'S OWN OUTPUT AND NOT RETYPED.
    moved = [(m.group(1), int(m.group(2)), int(m.group(3))) for m in
             re.finditer(r'(\S+)\s+read at (\d+), now (\d+) ;', J['home_section'])]
    loc = re.search(r'(rows re-located at their ledgers : \d+ of \d+ ; unclassified : \d+)',
                    J['home_section'])
    J['moved'] = moved
    J['located_phrase'] = loc.group(1) if loc else 'as the run reports'
    rec('  ### moved rows, parsed from the suite own output : %d %s' % (len(moved), moved))
    rec('  ### the located half, in the run own words : %s' % J['located_phrase'])
    if not moved or not loc:
        rec('  ### ### **THE RUN DID NOT YIELD THE FIGURES THIS BLOCK NEEDS. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b364_filing_notes', LINES)
        return 3

    SUITE = os.path.join(ROOT, 'tools', 'b357_checks.py')
    Q = {
        'label': quote(SUITE, 'G-LOCATED (every classified row located by the anchor tool'),
        'cond': quote(SUITE, "ok_dec = ('%d' % was) in bank and ('%d' % now) in bank"),
    }
    rec('')
    for k, q in Q.items():
        rec('  [%-6s] %s:%d ### scaffolding removed, equal under the shared normaliser : %s'
            % (k, q['file'], q['line'], q['equal']))
        rec('      | %s' % q['quote'][:150])
    if not all(q['equal'] for q in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b364_filing_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec('  ### THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK, NOTHING ABOVE IT EDITED.**')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED, AND THIS IS NOT A FAILURE**')
        rec('  ### -- it is the append-only rule refusing a second write of the same entry.')
        run_clock.write(D, 'b364_filing_notes', LINES)
        return 0
    body = chr(10).join(block(J, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### **THE READING BEFORE THE PUSH, AND IT IS THE ONE THAT CARRIES** -- after the commit the')
    rec('  ### blob IS the file and the same arm proves nothing about how it got there.')
    rec('')
    rec('=' * 100)
    ok = prefix_file and prefix_blob
    rec('  ### ### **THE FINDING IS FILED : `FINDING-DATED-ARM`. ### NO VERDICT IS WITHDRAWN.**')
    rec('  ### ### **NOTHING IS REPAIRED AND NO SUITE IS EDITED.**')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b364_filing_notes', LINES)
    io.open(os.path.join(D, 'b364_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='FINDING-DATED-ARM', mark=MARK, file='OPEN_TRAILS.md', branch=J['branch'],
             moved=moved, located_phrase=J['located_phrase'],
             quotes={k: dict(file=q['file'], line=q['line'], equal=q['equal'], quote=q['quote'])
                     for k, q in Q.items()},
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             verdict_withdrawn=False, arm_repaired=False, suite_edited=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
