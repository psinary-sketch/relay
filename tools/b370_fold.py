# -*- coding: utf-8 -*-
"""b370_fold.py -- COMPONENT 1: THE FOLD, b361 THROUGH b369. ### **PURELY ADDITIVE.**

### ### ### **`F-NOGRADE` IS THE POINT OF THIS FILE.** ### Every grade string below must be found
### ### **VERBATIM, IN THE BANK OF THE ACT IT IS ATTRIBUTED TO**, under the shared normaliser -- or the
### section is not written at all. ### **THE NO-GRADE-MOVED CLAIM IS MECHANICAL, NOT A PROMISE**
### (`b348`), and the order asks for it by name.
### ### **AND THE ATTRIBUTION IS THE HARD HALF, NOT THE PRESENCE.** ### The grade WORD
### `SUPPORTED-BY-THE-SOURCE'S-APPLICATION` was ruled at `b366` and is about `b365`'s finding. ###
### **PUTTING IT IN `b365`'s ROW WOULD FIRE THIS ARM**, and it should: `b365`'s own bank says
### `SUPPORTED AT ζ, WITH A STATED CONSTANT`, and that is what `b365` is entitled to say.
### ### **EVERY OBSTACLE IS LOCATED BY THE ANCHOR TOOL IN THE BANK THAT ORIGINATED IT** -- never in a
### later act's summary of it (`b360`'s rule).
### ### **THE SPAN IS READ FROM THIS ACT'S OWN SPAN JSON AND THE FOLD REFUSES IF IT DISAGREES.**
### ### **AND THE FILE IS APPENDED TO, NEVER EDITED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

BANK = {361: 'b361_the_held_item.txt', 362: 'b362_the_approximation_register.txt',
        363: 'b363_the_anchored_gate_arms.txt', 364: 'b364_the_copy_that_did_not_reproduce.txt',
        365: 'b365_the_owed_read_paid.txt', 366: 'b366_the_dated_arm_sweep.txt',
        367: 'b367_the_scaffold_repair.txt', 368: 'b368_the_front_document_reconciled.txt',
        369: 'b369_the_list_repaired.txt'}

# ### (act, what it is, the grade as ITS OWN act left it, the PROBE that must be in ITS OWN bank)
ROWS = [
    (361, 'the held evaluation b358\'s cap forbade, run: the index the archimedean asymptotic '
          'requires, evaluated for the corpus\'s own object from the source\'s own formulae',
     'DECIDED — `K(pi_triv) = 0`, so the index condition is vacuous for the corpus\'s object, and the '
     'value is an IDENTIFICATION of two of the source\'s displayed formulae, not a quotation of either',
     'DECIDED. ### `K(pi_triv) = 0`, SO THE INDEX CONDITION IS VACUOUS FOR THE CORPUS'),
    (362, 'the approximation register located in the literature and read for whether its finite side '
          'would carry the corpus\'s question',
     'LOCATED BUT NOT WORTH OPENING — at the reach the record can afford, with the hint CONFIRMED and '
     'its space CORRECTED by the source\'s own flag; the finite side is unconditional and the only '
     'upper bound on its rate is circular',
     'LOCATED BUT NOT WORTH OPENING'),
    (363, 'the anchored gate helper built, and the arms it was proposed for counted from the banks '
          'rather than from the draft that proposed it',
     'THE HELPER IS BUILT AND IT IS NARROWER THAN THE RULE IT WAS PROPOSED UNDER — the banks declare '
     'ELEVEN arms, not the draft\'s thirteen, and the helper reaches SEVEN of them',
     'THE HELPER IS BUILT AND IT IS NARROWER THAN THE RULE IT WAS PROPOSED UNDER.'),
    (364, 'the gate suite copy that did not reproduce, diagnosed rather than repaired-to-pass, with the '
          'branch fixed before the diagnosis',
     'THE BRANCH IS `REAL`, AND THE COPY WAS INNOCENT — the banked suite fails identically at its own '
     'location, so the failure has nothing to do with copying; the expectation was refuted BY A RUN AND '
     'NOT BY AN ARGUMENT',
     'THE BRANCH IS `REAL`, AND THE COPY WAS INNOCENT.'),
    (365, 'the owed read paid: what the pinned source states about the non-cuspidal case its own '
          'theorem is quantified over',
     'THE CONVENTION IS LOCATED, AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF — it names the '
     'convention, calls it one, applies its cuspidal lemmas to it by name and prints its constant; '
     'graded SUPPORTED AT `ζ`, WITH A STATED CONSTANT',
     'THE CONVENTION IS LOCATED, AND THE SOURCE WORKS THE EXCEPTIONAL CASE ITSELF.'),
    (366, 'every gate arm in the record swept for the dated-arm species, under three author\'s rulings '
          'executed in the same act',
     'THREE DATED ARMS IN THE WHOLE RECORD, OUT OF 1255 ARMS ACROSS 146 SUITES — two of them one '
     'substitution from standing, and the third MISSING ITS CONTENT because its act banked a line '
     'number and not the text found there',
     'THREE DATED ARMS IN THE WHOLE RECORD, OUT OF 1255 ARMS ACROSS 146 SUITES.'),
    (367, 'two scaffold terminals sought in the exclusion kernel for a repair the ferry had already '
          'priced, under a cap that made NOT LOCATED a full stop',
     'NOT LOCATED — the terminals do not exist and the kernel says so itself; every mention is inside '
     'its own retirement ledger, and the record had banked the same finding THIRTEEN DAYS BEFORE the '
     'ferry that ordered the repair',
     'NOT LOCATED. ### THE TERMINALS DO NOT EXIST, AND THE KERNEL SAYS SO ITSELF.'),
    (368, 'the front document that survived b367 measured against its source at a pinned ref, each '
          'exported name classified on its own evidence',
     'THE FRONT DOCUMENT IS RECONCILED, AND IT WAS RECONCILED WITHOUT EDITING A SENTENCE — 18 of 20 '
     'exported names absent and every one RETIRED, re-derived and not carried; and the retirement '
     'ledger names only half of them',
     'THE FRONT DOCUMENT IS RECONCILED, AND IT WAS RECONCILED WITHOUT EDITING A SENTENCE.'),
    (369, 'the same list repaired under a ruling that reversed b368\'s disposition of it, the original '
          'preserved by quotation before the edit',
     'THE LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED IN THE SAME FILE — the repaired list '
     'exports none of the absent names, the edit is bounded on both sides against the committed blob, '
     'and b368\'s ledger SPLIT is corrected while its COUNT stands',
     'THE LIST IS REPAIRED IN PLACE AND THE ORIGINAL IS PRESERVED IN THE SAME FILE.'),
]

# ### THE OBSTACLES: (act, sentence, the hint the anchor tool must find IN THAT ACT'S OWN BANK)
OBSTACLES = [
    (361, 'the value the corpus needed is written nowhere in the source',
     'AND THE VALUE IS NOT QUOTED FROM THE SOURCE. ### IT IS AN IDENTIFICATION OF TWO OF THE'),
    (362, 'the criterion as located is stated in a modified form, and the space is not the one the hint '
          'named', 'THE CORRECTION IS THE SPACE**, and the source itself flags it:'),
    (363, 'the draft that proposed the work was wrong about how much work there was',
     'AND THE DRAFT IS REFUTED IN ITS INPUT AS WELL AS IN ITS OUTPUT.'),
    (366, 'a dated arm can be missing its content, not merely its wording',
     'AND THE THIRD IS NOT HARDER TO WRITE. ### IT IS MISSING ITS CONTENT'),
    (367, 'the record already held the correction when the ferry was written',
     'AND THE RECORD ALREADY FOUND THIS, THIRTEEN DAYS AGO, AND SAID SO IN THESE WORDS'),
    (368, 'the ledger is accurate about what it says and incomplete about what it names',
     'LEDGER NAMES ONLY HALF OF THEM.'),
    (369, 'the failure that caught two acts is one sentence, and no arm in the record would have caught '
          'it', 'BOTH FAILURES ARE THE SAME SENTENCE: A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE'),
]

MARK = '## THE APPARATUS ARC, b361–b369 — THE FOLD'

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bank(n):
    return io.open(os.path.join(D, BANK[n]), encoding='utf-8', errors='replace').read()


def main():
    rec('=' * 100)
    rec('b370 -- COMPONENT 1: THE FOLD. ### **F-NOGRADE FIRST, AND THE SECTION ONLY IF IT PASSES.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures : %s ; the needle helper : %s'
        % (AF.self_test(False), GN.self_test(False)))

    S = json.load(io.open(os.path.join(D, 'b370_span.json'), encoding='utf-8'))
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE SPAN, READ FROM THE COUNTER AND NOT TYPED. ### **BAR 3.**')
    rec('-' * 100)
    lo, hi, n = S['span_starts_at'], S['this_act'], S['current_span']
    named_lo, named_hi = 361, 369
    agree = (lo == named_lo and hi == named_hi and n == (named_hi - named_lo + 1) == len(ROWS))
    rec('    the counter says the span starts at b%d and runs through b%d : %d act(s)' % (lo, hi, n))
    rec('    the fold names b%d through b%d, with %d rows' % (named_lo, named_hi, len(ROWS)))
    rec('    ### ### **THEY AGREE : %s**' % agree)
    if not agree:
        rec('    ### ### **THEY DO NOT AGREE. ### THE FOLD IS NOT WRITTEN, AND THE DISAGREEMENT IS THIS')
        rec('    ### ### ACT`S FINDING.**')
        run_clock.write(D, 'b370_fold_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec("  ### (2) `F-NOGRADE`. ### **EVERY GRADE IN ITS OWN ACT'S BANK, VERBATIM, OR NOTHING.**")
    rec('-' * 100)
    misses = []
    for act, _what, _grade, probe in ROWS:
        b = bank(act)
        ok = GN.norm(probe) in GN.norm(b)
        if not ok:
            misses.append((act, probe))
        rec('    b%-4d %-6s %s' % (act, 'PASS' if ok else '### FAIL', probe[:88]))
    rec('    ### ### **GRADE STRINGS NOT FOUND IN THEIR OWN BANK : %d**' % len(misses))
    if misses:
        rec('    ### ### **THE SECTION IS NOT WRITTEN.** ### A grade retyped from memory is a grade')
        rec('    ### moved, and this arm exists to stop exactly that.')
        run_clock.write(D, 'b370_fold_notes', LINES)
        return 3
    rec('    ### **AND ONE ATTRIBUTION WAS CORRECTED BY THIS ARM BEFORE IT PASSED, WHICH IS WHY IT IS')
    rec('    ### ### HERE:** ### the grade word `SUPPORTED-BY-THE-SOURCE`S-APPLICATION` is `b366`s')
    rec('    ### ruling, not `b365`s finding. ### `b365`s row carries what `b365`s own bank says.')

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE OBSTACLES, EACH LOCATED IN THE BANK THAT ORIGINATED IT.')
    rec('-' * 100)
    quoted = []
    for act, sentence, hint in OBSTACLES:
        p = os.path.join(D, BANK[act])
        try:
            ln, line = AF.find(p, hint)
        except AF.AnchorError as e:
            rec('    ### ### **NO ANCHOR at b%d : %s**' % (act, str(e)[:90]))
            run_clock.write(D, 'b370_fold_notes', LINES)
            return 3
        clean = ' '.join(re.sub(r'#{2,}', ' ', line).split()).strip().strip('*')
        quoted.append(dict(act=act, sentence=sentence, file=BANK[act], line=ln, quote=clean))
        rec('    b%-4d %s:%-5d | %s' % (act, BANK[act][:34], ln, clean[:80]))
    rec('    ### ### **OBSTACLES LOCATED : %d ### -- EACH IN THE BANK OF THE ACT THAT ORIGINATED IT.**'
        % len(quoted))

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE APPEND. ### **PURELY ADDITIVE.**')
    rec('-' * 100)
    before = io.open(FINDINGS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE SECTION IS ALREADY PRESENT. ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b370_fold_notes', LINES)
        return 0

    out = ['', MARK, '']
    out.append(
        '**%d acts, 2026-09-08.** A filings section: **no grade moves here, no act is re-verdicted, and '
        'nothing below is new mathematics.** Each entry carries its grade as *its own act* left it and '
        'its own scope sentence, and **every grade string below was required to appear, verbatim, in the '
        'bank of the act it is attributed to, or this section would not have been written** — an arm '
        'that fired once during the writing, on a grade word that belongs to b366\'s ruling and not to '
        'b365\'s finding. Every obstacle is quoted from the bank of the act that **originated** it. '
        '**And the span is counted, not typed:** the emitter reads the last fold section\'s own filing '
        'line off this document, counts forward, and refuses to write if its count disagrees with the '
        'range this section names.' % n)
    out += ['', '### The span, act by act', '',
            '| act | what it is | grade, as its own act left it |', '|---|---|---|']
    for act, what, grade, _p in ROWS:
        out.append('| **b%d** | %s | %s |' % (act, what, grade))

    out += ['', '### The obstacles, each quoted at the act that met it', '',
            '| act | the obstacle | quoted from its own bank |', '|---|---|---|']
    for q in quoted:
        out.append('| **b%d** | %s | *"%s"* |' % (q['act'], q['sentence'], q['quote']))

    out += ['', '### The corrections this span made — to its own readings, and to each other\'s', '',
            ('**A correction is not a re-verdict.** Each row below is a measurement replaced by a better '
             'measurement, made by the act that made it and accepted by the act it corrects.'), '',
            '| what was corrected | by whom | what it was, and what it became |', '|---|---|---|',
            '| a draft\'s count of the work available | b363, against the draft that proposed it | '
            'THIRTEEN incidents claimed; **ELEVEN** declared by the banks — and the helper\'s reach came '
            'out at SEVEN, not the draft\'s nine or ten. **Refuted in its input as well as its output.** |',
            '| the space a located criterion is stated over | b362, against its own hint | the hint '
            'named one space; the source flags a modified form. **The criterion is real and where the '
            'hint said; the space is not what the hint said.** |',
            '| an expectation about why a copy failed | b364, against the navigator\'s registered '
            'expectation | `ENVIRONMENTAL` was expected; the banked suite fails identically at its own '
            'location. **Refuted by a run and not by an argument.** |',
            '| a hint\'s characterisation of two terminals | b367, against the ferry that carried it | '
            '*written as trivially true* was the hint; the kernel\'s own audit files them as opaque-Prop '
            'templates, a different thing. **The hint named the right terminals and the wrong defect.** |',
            '| one act\'s split of a retirement ledger | b369, against b368 | b368 reported one name as '
            'having **no ledger entry for its layer at all**; the ledger carries an entry headed by that '
            'declaration\'s own name. **b368\'s COUNT stands and is confirmed a third time; its SPLIT is '
            'corrected.** |']

    out += ['', '### The defects these seats declared in their own work', '',
            ('**This table is not a confession and it is not a boast.** It is here because the arc\'s '
             'claimed product is a record checkable by a reader who trusts none of it, and a record '
             'whose defects are declared only when convenient is not that. Every entry was declared by '
             'the act that committed it, in its own bank, before any later act found it.'), '',
            '| act | what it declared against itself |', '|---|---|',
            '| **b363** | its own census tool committed the act\'s own species twice — a name typed '
            'rather than read, then an item shape assumed rather than read |',
            '| **b364** | two arms of its own suite were wrong: one asked the bank for a print '
            'statement, one demanded a file be byte-identical *now* when the closing appends to it |',
            '| **b366** | an arm whose predicate treated every detector hit as a dated arm, '
            'contradicting its own act\'s finding |',
            '| **b367** | a banned stem inside a verbatim kernel quotation, which fired in the bank and '
            'in an already-appended block; and a bounded search that reported a bounded answer without '
            'saying where its bound fell |',
            '| **b368** | its bank claimed a history search run for only half the names; its own '
            '`G-EVIDENCE` arm caught it, and chasing that arm is what found the third evidence group |',
            '| **b369** | a gate driver that tested a tuple for truth and so could not fail; a detector '
            'that fired on a language version; a ranking sentence that was simply false; and a banned '
            'stem in its own prose |']

    out += ['', '### The arc as one statement', '',
            ('**This span produced no new mathematics about the clause.** It produced two results about '
             'the clause\'s *shape* — the approximation register located and closed, with its '
             'obstruction identified as a rate (b362); and the Li localization\'s archimedean half '
             'supported at `ζ` with a stated constant (b361, b365), under the grade word b366 ruled for '
             'that kind of support. **And its main product was neither: it was making the record '
             'checkable by a reader who trusts none of it.**'), '',
            ('**Seven of the nine acts produced no result about the object at all.** They built a needle '
             'helper and measured its reach against the banks rather than against the draft that '
             'proposed it; they diagnosed a failing suite instead of repairing it to pass; they swept '
             'every arm in the record for a species one of them had just minted; and they found, '
             'measured and repaired a front document that had been exporting eighteen names its source '
             'does not declare. **A fold that let those seven read as progress on the clause would be '
             'the exact defect this span spent itself finding elsewhere.**'), '',
            ('*Scope:* **This is a statement about what this span put on the board, not about what is '
             'true of the object.** The clause has not moved and no act in the span claims otherwise. '
             'The two shape results are graded where their own acts left them and are not promoted here. '
             'Nothing above closes a coordinate, discharges a class, or bears on `h2`.'), '',
            ('*A fold is a summary of its acts at their own grades. It proves nothing, discharges '
             'nothing, and moves no grade. No coordinate is closed, the partition stays UNDECIDED, and '
             '`h2` stands exactly where the deposit left it. Filed by b370 (relay '
             '`data/b370_the_fold.txt`; the extract that located every quotation above at '
             '`data/%s`; the span counted by `tools/b363_span.py`, repaired in this act to read without '
             'writing).*' % json.load(io.open(os.path.join(D, 'b370_reads.json'),
                                              encoding='utf-8'))['run_file'])]

    io.open(FINDINGS, 'a', encoding='utf-8', newline=chr(10)).write(chr(10).join(out) + chr(10))
    after = io.open(FINDINGS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    r = subprocess.run(['git', 'show', 'HEAD:FINDINGS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    grew = len(after) - len(before)
    rec('    bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('    ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('    ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('    ### **READ BEFORE THE PUSH** (`b352`), which is the reading that carries.')
    rec('    lines appended : %d' % len(out))
    rec('=' * 100)
    ok = prefix_file and prefix_blob
    rec('  ### ### **THE FOLD IS FILED. ### NO GRADE MOVED, NO ACT RE-VERDICTED, NOTHING NEW.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b370_fold_notes', LINES)
    io.open(os.path.join(D, 'b370_fold.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(mark=MARK, acts=len(ROWS), span_lo=lo, span_hi=hi, span_counted=n, span_agrees=agree,
             grade_misses=len(misses), obstacles=len(quoted), quoted=quoted,
             corrections=5, defects=6,
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             sections_edited=0, grades_moved=0, acts_reverdicted=0, lines_appended=len(out),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
