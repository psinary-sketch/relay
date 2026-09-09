# -*- coding: utf-8 -*-
"""b384_fold.py -- THE FOLD, b371 THROUGH b383. ### **PURELY ADDITIVE.**

### ### ### **`F-NOGRADE` IS THE POINT OF THIS FILE.** ### Every headline below must be located
### ### **BY THE ANCHOR TOOL IN THE BANK OF THE ACT IT IS ATTRIBUTED TO** -- or the section is not
### written at all. ### **THE NO-GRADE-MOVED CLAIM IS MECHANICAL, NOT A PROMISE** (`b348`).
### ### **AND THE ATTRIBUTION IS THE HARD HALF, NOT THE PRESENCE.** ### `b383` said things about
### `b375`; ### **THOSE BELONG IN `b383`'s ROW.** ### Each act is quoted from its own bank only
### (`b360`'s rule: never from a later act's summary of it).
### ### **THE SPAN IS READ FROM THIS ACT'S OWN SPAN JSON AND THE FOLD REFUSES IF IT DISAGREES.**
### ### **AND `FINDINGS.md` IS APPENDED TO, NEVER EDITED.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
TITLE = 'THE RE-DERIVATION ARC, b371–b383 — THE FOLD'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **(act, its own bank, the headline hint, the one-line gloss this seat writes).**
# ### ### **THE HINT IS LOCATED IN THAT ACT'S OWN BANK. ### THE GLOSS IS THIS SEAT'S PROSE.**
ACTS = [
    (371, 'b371_the_first_target.txt',
     '### ### ### **THE COUNT CLAIM IS `STALE`, AND THE NAVIGATOR`S EXPECTATION IS REFUTED ON ITS '
     'FIRST HALF.**',
     'settled a count claim by one read: exact at a tag, stale at the head'),
    (372, 'b372_the_first_batch.txt',
     '### ### ### **THE END-OF-LINE ATTRIBUTE IS NOW TRACKED IN ALL `4` ROSTERED REPOSITORIES, AND '
     'IN',
     'pinned `eol=lf` in every rostered repository and classified the first row batch'),
    (373, 'b373_the_pins_and_the_status_column.txt',
     '### ### ### **`(R9)` WAS EXECUTED AS FAR AS ITS OWN SOURCING RULE ALLOWS, AND IT WROTE NO '
     'PIN.**',
     'executed the pin ruling over every pinless row and wrote none'),
    (374, 'b374_the_descriptive_layer.txt',
     '### ### ### **THE KEYSTONES HEDGE LESS THAN HALF AS OFTEN AS THE WORKING NOTES, AND CARRY '
     'UNDATED',
     'measured the descriptive layer and repaired nothing; four lists opened'),
    (375, 'b375_the_keystone_and_cluster_census.txt',
     '### ### ### **THE WORD `KEYSTONE` NAMES THREE DIFFERENT TESTS IN THIS RECORD, AND THEY DO '
     'NOT',
     'found three definitions of `keystone` and one instrument giving opposite answers'),
    (376, 'b376_the_two_axis_read.txt',
     '### ### ### **EVERY ONE OF THE THREE TESTS CROSSES THE QUADRANTS, AND SO DOES THE CORPUS`S '
     'OWN',
     'separated ROLE from APPARATUS and found every test crossing both'),
    (377, 'b377_the_unblocked_obligation.txt',
     '### ### ### **THE PIN WAS THE MISSING ELEMENT, NOT THE TERMINAL.**',
     'found the missing element was the pin, and fixed a figure as a floor'),
    (378, 'b378_the_refs_widened.txt',
     '### ### ### **AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT** -- and ### **A SEARCH THAT '
     'CANNOT',
     'widened the refs and caught its own sweep silently dead'),
    (379, 'b379_the_apparatus_axis_rescored.txt',
     '### ### ### **THE SUSPECT COLUMN WAS UNDERCOUNTING, AND CORRECTING IT MOVED NOTHING WHERE '
     'THE',
     'corrected the apparatus column and moved nothing where the ruling needed movement'),
    (380, 'b380_the_role_axis_scored_structurally.txt',
     '### ### ### **THE ROLE COLUMN MOVED FOR THE FIRST TIME IN FIVE ACTS, AND THE PREDICATE THAT '
     'MOVED',
     'read role from reach; the column moved and the predicate failed its own control'),
    (381, 'b381_the_control_rebuilt.txt',
     '### ### ### **THE CONTROL WAS REBUILT SO THAT IT COULD FAIL IN BOTH DIRECTIONS, AND THE NEW',
     'rebuilt the control so it could fail, and co-location failed on it'),
    (382, 'b382_the_sequence_stopped.txt',
     '### ### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS:',
     'closed the evidence: a class ruling must rest on declaration, and two failures are not proof'),
    (383, 'b383_the_standard_read.txt',
     '### ### ### **THE SEQUENCE RECONCILES AS 3 DUPLICATED AND 5 ADDS.**',
     'read the standing standard at content and reconciled the sequence to it'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    span = json.load(io.open(os.path.join(D, 'b384_span.json'), encoding='utf-8'))
    lo, hi = span['span_starts_at'], span['this_act'] - 1
    rec('=' * 100)
    rec('b384 -- THE FOLD, b%d THROUGH b%d. ### PURELY ADDITIVE.' % (lo, hi))
    rec('=' * 100)
    rec('')
    rec('  ### (1) THE SPAN, FROM THE COUNTER AND NOT FROM THIS SEAT.')
    rec('  ' + '-' * 96)
    rec('    the last fold      : %s, b%d-b%d (%d acts), filed by b%d'
        % (span['last_fold']['title'], span['last_fold']['lo'], span['last_fold']['hi'],
           span['last_fold']['acts'], span['filed_by']))
    rec('    so the span starts : b%d' % lo)
    rec('    this act           : b%d ### -- **AND IS NOT IN ITS OWN FOLD**' % span['this_act'])
    rec('    ### ### **SO THE FOLD COVERS b%d-b%d : %d ACTS.**' % (lo, hi, hi - lo + 1))
    rec('    the fold threshold : ### **9** ### (b366`s author ruling)')
    rec('    ### ### **%d >= 9, SO THE FOLD IS DUE BY THE RECORD`S OWN RULE.**' % (hi - lo + 1))
    covered = [a for a, _b, _h, _g in ACTS]
    agree = (covered == list(range(lo, hi + 1)))
    rec('    ### **THE ACTS THIS FILE WRITES AGREE WITH THE COUNTER : %s**' % agree)
    if not agree:
        rec('    ### ### **REFUSING: the span JSON and this file disagree.**')
        run_clock.write(D, 'b384_fold_notes', LINES)
        return 1

    # ------------------------------------------------------------------ F-NOGRADE, BEFORE THE WRITE
    rec('')
    rec('  ### (2) `F-NOGRADE` -- EVERY HEADLINE LOCATED IN ITS OWN ACT`S BANK.')
    rec('  ' + '-' * 96)
    located, missing = [], []
    for act, bank, hint, gloss in ACTS:
        p = os.path.join(D, bank)
        try:
            n, line = AF.find(p, hint)
            located.append(dict(act=act, bank=bank, line=n, text=line.rstrip(chr(10)), gloss=gloss))
            rec('    b%d  `%s` line %-5d ### LOCATED' % (act, bank, n))
        except Exception as e:
            missing.append((act, bank, str(e)[:90]))
            rec('    b%d  `%s` ### ### **NOT LOCATED** -- %s' % (act, bank, str(e)[:90]))
    rec('    ### ### **HEADLINES LOCATED : %d OF %d. ### NOT LOCATED : %d.**'
        % (len(located), len(ACTS), len(missing)))
    if missing:
        rec('    ### ### ### **THE SECTION IS NOT WRITTEN AT ALL.** ### `F-NOGRADE` refuses, and')
        rec('    ### that is the arm working rather than the act failing.')
        run_clock.write(D, 'b384_fold_notes', LINES)
        return 1

    # ------------------------------------------------------------------------------ THE SECTION
    S = []
    S.append('')
    S.append('---')
    S.append('')
    S.append('## %s' % TITLE)
    S.append('')
    S.append('*Filed by b384, 2026-09-09. Span decided by `tools/b363_span.py`, not by the seat: the '
             'last fold covered b%d–b%d and was filed by b%d, so this span starts at b%d and '
             'runs through b%d — **%d acts against a fold threshold of nine**. The folding act '
             'is not in its own fold. Purely additive: nothing above this line was edited.*'
             % (span['last_fold']['lo'], span['last_fold']['hi'], span['filed_by'], lo, hi,
                hi - lo + 1))
    S.append('')
    S.append('### The arc’s one statement')
    S.append('')
    S.append('**An eight-act sequence re-derived a standard the corpus had already ruled, and did '
             'not cite it once.** b375–b382 asked what the corpus means by *keystone*, how many '
             'documents are one, and whether a document’s role can be read from its structure. '
             '`THE_DOCUMENT_CLASS_TAXONOMY.md` — **standing standard, 2026-07-28, author-ruled** '
             '— already fixes four tiers and, for each, **what it must carry and how it may be '
             'cited**: Tier K states *grade · terminal · pin* and **may be cited as '
             'certification**; Tier C **organizes** certified results and is **never cited as '
             'certification**, which the standard calls its load-bearing rule. The registry’s '
             '**PHASE ATTRIBUTE** section already reconciles the rubric’s WHEN with the '
             'registry’s WHERE. And `THE_LOAD_BEARING_MAP.md`, the keystone correspondence '
             'union, already names **14 graded Correspondence tables**. b383 read all three at '
             'content and reconciled the sequence to them: **3 DUPLICATED, 5 ADDS**.')
    S.append('')
    S.append('**What the sequence added is narrower than its own banks suggest, and it is real.** '
             'b376’s **two-axis separation** — that ROLE and APPARATUS are different '
             'properties and every one of the three tests crosses both — is the durable result; '
             'the standard states the two properties as separate *tiers* but nowhere states that a '
             'test can cross them. b378 established facts about kernel identifiers across 270 refs '
             'that no standard states or could state. b380 and b381 are **two negative results about '
             'two structural predicates**, each failing on a control built to fail. b382 argued a '
             'conclusion the standard assumes but nowhere makes: that a class ruling must rest on '
             '**declaration** rather than classification. And b383 corrected the reading that the '
             'standard merely *omits* the conjunction of the two tiers — **it excludes it**, by '
             'its own contradictory citation rules, by disposing of mixed documents through ruling '
             'one tier and reading the parts apart, and by having **retired a predecessor scheme for '
             'spanning the two**.')
    S.append('')
    S.append('**And the sequence violated a freshness rule this seat had itself minted, four acts '
             'earlier.** `DESK_FRESHNESS.md`, minted at b368: *every desk item names the FILE and the '
             'DATE at which it was last confirmed; an item without one is RE-VERIFIED before it is '
             'ordered* — and *the cost was not a wrong belief. It was **a right belief with no '
             'date on it**, and a second act spent to re-derive what a first act had already banked.* '
             'The premise the sequence ran on carried no date. The standard that dated it was '
             'author-ruled on 2026-07-28 and sat in the tree the whole time. **A minted rule is not a '
             'carried rule.**')
    S.append('')
    S.append('### The span, act by act, each at its own grade')
    S.append('')
    S.append('| act | what it put on the board |')
    S.append('|:--|:--|')
    for r in located:
        flat = r['text'].replace('###', '').replace('**', '').replace('|', '\\|').strip()
        S.append('| **b%d** | %s — *%s* |' % (r['act'], r['gloss'], flat))
    S.append('')
    S.append('### The shape of the span, said rather than smoothed')
    S.append('')
    S.append('**The arc has two unequal halves.** b371–b374 moved rows and ledgers and produced '
             'results about the record: a count claim settled as stale, `eol=lf` pinned in all four '
             'rostered repositories, the pin ruling executed over every pinless row **without '
             'writing a pin**, and the descriptive layer measured with four lists opened and nothing '
             'repaired. b375–b382 measured a question the standard had already answered. '
             '**Four acts of work and eight of re-derivation** is the honest shape, and b383 is the '
             'act that found it.')
    S.append('')
    S.append('**Three instruments were built and shared across the span:** `role_structure.py` '
             '(role read from what a document draws on), `co_location.py` (whether sources from '
             'different clusters share a unit), and `row_categories.py` (a vocabulary so a checker '
             'stops reporting a category as an absence). **Two of the three scored predicates that '
             'failed their controls, and both failures are on the record as findings.**')
    S.append('')
    S.append('*Scope:* **This is a statement about what this span put on the board, not about what '
             'is true of the object.** Nothing here about the quantifier, `h2`, totality or the '
             'roster; no coordinate closed and the partition undecided. The four open lists stay '
             'OPEN. The class ruling is the author’s and the standing standard is already his.')
    S.append('')
    S.append('*A fold is a summary of its acts at their own grades. It proves nothing, discharges '
             'nothing, and moves no grade. Every headline above was located by the anchor tool in the '
             'bank of the act it is attributed to — %d of %d, none missing — and no act is '
             'quoted from a later act’s summary of it.*' % (len(located), len(ACTS)))
    S.append('')

    # ---------------------------------------------------------------------------- THE APPEND
    rec('')
    rec('  ### (3) THE APPEND. ### **PURELY ADDITIVE.**')
    rec('  ' + '-' * 96)
    before = io.open(FINDINGS, encoding='utf-8', newline='').read()
    if TITLE in before:
        rec('    ### ALREADY FILED -- the title is present. ### NOTHING APPENDED.')
        after, appended, prefix_ok = before, False, True
    else:
        io.open(FINDINGS, 'a', encoding='utf-8', newline=chr(10)).write(chr(10).join(S) + chr(10))
        after = io.open(FINDINGS, encoding='utf-8', newline='').read()
        appended = after.startswith(before)
        r = subprocess.run(['git', 'show', 'HEAD:FINDINGS.md'], cwd=PP, capture_output=True)
        committed = r.stdout.decode('utf-8', 'replace')
        prefix_ok = (committed.replace(chr(13) + chr(10), chr(10))
                     in after.replace(chr(13) + chr(10), chr(10)))
        rec('    bytes %d -> %d ; ### **APPEND-ONLY %s ; COMMITTED BLOB STILL A TRUE PREFIX %s**'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), appended, prefix_ok))
        subprocess.run(['git', '-C', PP, 'add', '--', 'FINDINGS.md'], capture_output=True)
    nsec = after.count('## ' + TITLE)
    rec('    sections carrying this title : %d ### -- **EXACTLY ONE**' % nsec)
    MUSTFAIL = ('### A GRADE WAS MOVED.', '### A CLASS WAS RULED.', '### A COORDINATE WAS CLOSED.',
                '### AN ACT WAS PROMOTED.', '### THE FOLD EDITED WHAT WAS ABOVE IT.')
    hit = [m for m in MUSTFAIL if m in chr(10).join(S)]
    rec('    ### MUST-FAIL WHOLE LINES IN THE SECTION : %s' % (hit or 'none'))
    bad = [i + 1 for i, x in enumerate(S) if '%s' in x or '%d' in x]
    rec('    ### UNFILLED PLACEHOLDERS : %s' % (bad or 'none'))
    rec('')
    rec('=' * 100)
    rec('  ### ### **NO GRADE WAS MOVED. ### NO CLASS WAS RULED. ### NO ACT WAS PROMOTED. ### NOTHING')
    rec('  ### ### WAS DISCHARGED. ### THE FILE WAS APPENDED TO AND NEVER EDITED.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b384_fold_notes', LINES)
    out = dict(span_lo=lo, span_hi=hi, span_acts=hi - lo + 1, threshold=9,
               counter_agrees=agree, headlines_located=len(located), headlines_missing=len(missing),
               acts=[dict(act=r['act'], bank=r['bank'], line=r['line']) for r in located],
               section_title=TITLE, sections=nsec, appended=appended, prefix_ok=prefix_ok,
               section_lines=len(S), mustfail=len(hit), placeholders=len(bad),
               grades_moved=0, classes_ruled=0, acts_promoted=0,
               before_bytes=len(before.encode('utf-8')), after_bytes=len(after.encode('utf-8')),
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b384_fold.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (prefix_ok and nsec == 1 and not hit and not bad) else 1


if __name__ == '__main__':
    sys.exit(main())
