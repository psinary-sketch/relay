# -*- coding: utf-8 -*-
"""b402_fold.py -- THE FOLD, b385 THROUGH b401. ### **PURELY ADDITIVE.**

### ### ### **`F-NOGRADE` IS THE POINT OF THIS FILE.** ### Every headline below must be located
### ### **BY THE ANCHOR TOOL IN THE BANK OF THE ACT IT IS ATTRIBUTED TO** -- or the section is not
### written at all. ### **THE NO-GRADE-MOVED CLAIM IS MECHANICAL, NOT A PROMISE** (`b348`).
### ### **AND THE ATTRIBUTION IS THE HARD HALF.** ### Each act is quoted from its own bank only
### (`b360`'s rule: never from a later act's summary of it).
### ### **THE SPAN IS READ FROM THIS ACT'S OWN SPAN JSON AND THE FOLD REFUSES IF IT DISAGREES.**
### ### **THE THRESHOLD IS READ FROM `(R1)` AND NOT FROM THE COUNTER**, whose own line on the
### threshold is stale -- and saying which is which is `G-THRESHOLD`.
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
TITLE = 'THE ARTEFACT ARC, b385–b401 — THE FOLD'
THRESHOLD = 9

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **(act, its own bank, the headline hint, the one-line gloss this seat writes).**
ACTS = [
    (385, 'b385_the_six_on_the_trails.txt',
     '### ### ### **THE RULE `b383` REPORTED ABSENT IS IN THE REGISTRY, AND THE ABSENCE',
     'found the rule a prior act called absent, sitting under a heading nobody had searched'),
    (386, 'b386_the_guard_single_sourced.txt',
     '### ### ### **THE AUTHOR RULED `(R15)`: ONE GUARD, ONE SOURCE -- AND THE DEFECT WAS',
     'single-sourced the guard and found nine copies where two were reported'),
    (387, 'b387_what_the_tables_carry.txt',
     '### ### ### **A READ AND A COUNT. ### NO RULING, NO REPAIR, NO ROW EDITED, NO GRADE',
     'counted what the keystone tables actually carry, and repaired nothing'),
    (388, 'b388_the_map_refreshed.txt',
     '### ### ### **THE AUTHOR RULED `(R17)`: THE FEDERATION MAP IS REFRESHED IN FULL.**',
     'refreshed the map from quoted moves only, and drew the line at a mention'),
    (389, 'b389_the_look_see.txt',
     '### ### ### **THE AUTHOR RULED `(R18)`: TWO MAPS, TWO KEYS.**',
     'kept two maps apart, proved a halt at the platform, and withdrew its own prior finding'),
    (390, 'b390_the_proofreading_pass.txt',
     '### ### ### **THE CORPUS HAD RUN CURRENCY PASSES AND CLASSIFICATION PASSES AND NO',
     'read one document whole and found a version that has never existed, cited across eleven'),
    (391, 'b391_the_phantom_repaired.txt',
     '### ### ### **THE METHODOLOGY PAPER WAS CITED AT A VERSION IT HAS NEVER HAD, AND THE',
     'traced the phantom version to a bundle label that never propagated, and repaired 24 of 32'),
    (392, 'b392_the_two_rulings.txt',
     '### ### ### **TWO THINGS THE CORPUS HAD BEEN DOING WITHOUT A NAME OR A RULE',
     'gave two standing practices their rules, and its own census refuted one of them'),
    (393, 'b393_the_clusters_surfaced.txt',
     '### ### ### **TWO ACTS FOUND THE FIVE CLUSTERS AND NEITHER PUT THEM IN FRONT',
     'surfaced the clusters and found four different answers to one question, not added'),
    (394, 'b394_the_reconciliation_batched.txt',
     '### ### ### **THREE KEYSTONES READ IN ONE ACT, AND THE BATCH FOUND A DEFECT',
     'batched three reads and found a defect between two of them that neither would have shown'),
    (395, 'b395_the_ceiling_answered.txt',
     '### ### ### **THE CEILING WAS AN ARTEFACT OF A MATCHER, AND THE MATCHER WAS THIS',
     'showed a banked ceiling was its own matcher`s shape, and priced four routes past it'),
    (396, 'b396_the_backtick_swept.txt',
     '### ### ### **THE QUESTION HAS NO ANSWER AT INSTRUMENT GRANULARITY, AND THE THREE',
     'swept the narrow-matcher shape across every instrument and threw out three vacuous filters'),
    (397, 'b397_the_unlanded_work.txt',
     '### ### ### **EIGHT OF THE NINE HELD BRANCHES WERE ALREADY LANDED. ### WHAT IS',
     'found the held work already landed and the prose about it the thing that was stale'),
    (398, 'b398_the_li_weil_bridge.txt',
     '### ### ### **UNDECIDABLE FROM THE RECORD. ### BOTH HALVES OF THE READING ARE',
     'tested the bridge reading from banked results and named the one missing identity'),
    (399, 'b399_the_sign_and_the_refutation.txt',
     '### ### ### **(M) IS REFUTED. ### IT SURVIVES THE SIGN TEST VACUOUSLY AND THEN FAILS BY A',
     'refuted that identity by a printed value, after a sign test that passed vacuously'),
    (400, 'b400_the_bridge_restated.txt',
     '### ### ### **(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW.)**',
     'declared the pair two objects and restated the bridge as one question, typed and not opened'),
    (401, 'b401_the_absent_element_searched.txt',
     '### ### ### **COMPONENT 1 : ### PRESENT BUT NOT APPLICABLE.**',
     'searched for that question`s missing piece and found the piece absent and its kind present'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    span = json.load(io.open(os.path.join(D, 'b402_span.json'), encoding='utf-8'))
    lo, hi = span['span_starts_at'], span['this_act'] - 1
    rec('=' * 100)
    rec('b402 -- THE FOLD, b%d THROUGH b%d. ### PURELY ADDITIVE.' % (lo, hi))
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
    rec('')
    rec('  ### (1b) THE THRESHOLD, READ FROM THE RULING AND NOT FROM THE COUNTER.')
    rec('  ' + '-' * 96)
    rec('    ### **`(R1)`, THE AUTHOR`S RULING AT `b366`: THE FOLD THRESHOLD IS NINE ACTS.**')
    rec('    ### **AND THE COUNTER`S OWN LINE ON IT IS STALE:** ### its JSON carries')
    rec('    ### `threshold_declared : %s`, and it prints *THERE IS NO DECLARED THRESHOLD IN THE'
        % json.dumps(span.get('threshold_declared')))
    rec('    ### RECORD*. ### That was true when `b363` wrote it and has been false since `b366`.')
    rec('    ### ### **A DATED ARM (`b364`s species), PRINTED AND ROUTED, NOT REPAIRED HERE.**')
    rec('    ### ### **%d >= %d, SO THE FOLD IS DUE.**' % (hi - lo + 1, THRESHOLD))
    rec('')
    rec('  ### (1c) THE NAVIGATOR`S COUNT, PRINTED BESIDE THE TOOL`S AND SCORED.')
    rec('  ' + '-' * 96)
    rec('    the navigator`s claim : ### **SIXTEEN**')
    rec('    the tool`s count      : ### **%d** ### (`b%d` through `b%d` inclusive)'
        % (hi - lo + 1, lo, hi))
    rec('    ### ### **THE CLAIM IS REFUTED BY ONE SUBTRACTION. ### `(N4)`S FIRST HALF -- THAT THE')
    rec('    ### ### FOLD IS DUE -- IS MET; ITS SECOND -- THE NUMBER -- IS NOT.**')
    covered = [a for a, _b, _h, _g in ACTS]
    agree = (covered == list(range(lo, hi + 1)))
    rec('    ### **THE ACTS THIS FILE WRITES AGREE WITH THE COUNTER : %s**' % agree)
    if not agree:
        rec('    ### ### **REFUSING: the span JSON and this file disagree.**')
        run_clock.write(D, 'b402_fold_notes', LINES)
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
        run_clock.write(D, 'b402_fold_notes', LINES)
        return 1

    # ------------------------------------------------------------------------------ THE SECTION
    S = []
    S.append('')
    S.append('---')
    S.append('')
    S.append('## %s' % TITLE)
    S.append('')
    S.append('*Filed by b402, 2026-09-10. Span decided by `tools/b363_span.py`, not by the seat: '
             'the last fold covered b%d–b%d and was filed by b%d, so this span starts at b%d and '
             'runs through b%d — **%d acts against a fold threshold of nine, ruled by the author '
             'at b366 as (R1)**. The threshold is read from the ruling and not from the counter, '
             'whose own line on it — *there is no declared threshold in the record* — was true '
             'when b363 wrote it and has been false since b366. The folding act is not in its own '
             'fold. **The navigator’s count for this span was sixteen; the tool’s is '
             '%d, and the tool governs.** Purely additive: nothing above this line was edited.*'
             % (span['last_fold']['lo'], span['last_fold']['hi'], span['filed_by'], lo, hi,
                hi - lo + 1, hi - lo + 1))
    S.append('')
    S.append('### The arc’s one statement')
    S.append('')
    S.append('**In nine of these seventeen acts the finding was that a limit, a count, an absence '
             'or a version already on the record was an artefact of how it had been measured — and '
             'in the four mathematical acts that close the span the limit was real, and the work '
             'became stating it exactly.** b385 found a rule a prior act had reported absent '
             'sitting in the registry under a heading nobody had searched. b386 found **nine** '
             'copies of a guard where two were reported. b391 traced a version cited across eleven '
             'live documents to a **bundle label that never propagated** — a phantom, not a '
             'regression. b393 found that one question had been given **four different answers, '
             'and that they are not added**. b394 found a survey had **silently added a condition** '
             'to a rule it quoted, cutting its own eligible set. b395 showed a banked ceiling of '
             '*eleven unreachable keystones* was **its own matcher’s shape**, ten of the eleven '
             'being readable without a clone. b396 swept that shape across all **856** instruments '
             'and threw out **three vacuous filters with their yields printed**. b397 found eight '
             'of nine *held* branches already landed, so **the prose about them was the stale '
             'thing**. And b389 withdrew one of its own predecessor’s findings as simply wrong.',)
    S.append('')
    S.append('**The other half of the span is four acts on one owed bridge, and every step is a '
             'subtraction.** b398 read the Li-to-Weil decomposition from banked results and '
             'returned **UNDECIDABLE FROM THE RECORD**, naming the one missing identity `(M)` and '
             'typing it. b399 tested `(M)` by sign — it **survived vacuously**, every in-class '
             'prime sum being an empty sum — and then **refuted it by a printed value**, '
             '`−8.622324442` against `0` exactly, under either sign convention. b400 assembled the '
             'constraint set and reached **(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE '
             'WINDOW)**: on the source’s lawful class the finite-place sum is **identically zero by '
             'the definition of the class**, so a relation to the Li family’s live finite channel '
             'would have to supply the arithmetic from outside itself. And b401 searched for that '
             'question’s one missing piece across **4536** files and both pinned sources and found '
             'it **absent — while finding that its *kind* is not absent at all**: Lagarias Theorem '
             '6.1 bounds a finite-place contribution unconditionally, on the other family, against '
             'the zeros, and b358 already owned it. **Four acts, and the owed bridge went from a '
             'debt with no shape to a question with a named missing piece. Nothing was proved.**')
    S.append('')
    S.append('**And the two halves are the same lesson at two scales.** The instrument half kept '
             'finding that *a limit reported by an instrument is a property of the instrument until '
             'a second shape has been tried*. The mathematical half tried a second shape — five '
             'matcher shapes, both sources at content — and **the limit held**. That is the only '
             'way the record can tell the two apart, and this span did it in both directions.')
    S.append('')
    S.append('*Scope:* **This is a statement about what this span put on the board, not about what '
             'is true of the object.** No coordinate is closed; the clause has not moved; `(Q400)` '
             'is not opened; nothing here bears on `h2`, totality or the roster. The four open '
             'lists stay OPEN. Every grade in the span is its own act’s.')
    S.append('')
    S.append('### The span, act by act, each at its own grade')
    S.append('')
    S.append('| act | what it put on the board |')
    S.append('|:--|:--|')
    for r in located:
        flat = r['text'].replace('###', '').replace('**', '').replace('|', '\\|').strip()
        S.append('| **b%d** | %s — *%s* |' % (r['act'], r['gloss'], flat))
    S.append('')
    S.append('### The corrections this span made — to its own readings, and to each other’s')
    S.append('')
    S.append('**A correction is not a re-verdict.** Each row is a measurement replaced by a better '
             'measurement, made by the act that made it.')
    S.append('')
    S.append('| what was corrected | by whom | what it was, and what it became |')
    S.append('|---|---|---|')
    S.append('| a rule reported absent from the record | b385, against b383 | b383 searched for the '
             'navigator’s *name* for the rule and the rule uses none of those words. **The rule is '
             'in `REGISTRY.md` under a SESSION PROTOCOL heading. Absent-from-a-search is not '
             'absent-from-the-record.** |')
    S.append('| the number of copies of a tracked guard | b386, against b385’s own report | **two** '
             'reported; **nine** found. The extra seven were not a new defect but the same defect '
             'measured properly. |')
    S.append('| one layer’s missing ledger entry | b369→b385 lineage, carried forward | already '
             'corrected before this span; restated here only because b385’s trail rows depend on '
             'it. |')
    S.append('| a version citation across eleven documents | b391, against b390 | b390 measured the '
             'phantom at **28 citations across 11 documents**; b391 re-measured at **32 across 13** '
             'and found the origin — **a registry bundle label reconciled on 2026-07-16 that never '
             'propagated**. 24 repaired, 8 excluded with reasons. |')
    S.append('| a survey’s own eligible set | b394, against itself | the survey **silently added a '
             'condition** to the rule it quoted and cut the eligible set from 4 to 3. **An added '
             'condition is invisible in the result.** |')
    S.append('| a banked ceiling of unreachable keystones | b395, against b394 | *eleven '
             'unreachable* was **an artefact of b394’s own backtick matcher**; **ten of the eleven '
             'are readable without a clone**. |')
    S.append('| a finding about an interface split | b389, against b388 | **WITHDRAWN as wrong** by '
             'the act that inherited it, with the withdrawal recorded rather than the finding '
             'quietly dropped. |')
    S.append('| the shape of the owed bridge | b399, against b398 | b398 named `(M)` as the missing '
             'identity and typed it a RESULT. b399 **refuted it by value**. The row was not paid '
             'and **was no longer owed in the same way: the statement it was waiting for is '
             'false**. |')
    S.append('| where the absent element’s absence came from | b401, against b400 | b400 called it '
             'absent **from a constraint set**; b401 called it absent **from a search** — five '
             'matcher shapes, 4536 files, both sources at content — and found the *kind* of '
             'statement present in a pinned source the record already owned. |')
    S.append('')
    S.append('### The defective bars this span declared')
    S.append('')
    S.append('| act | the bar, and why it was defective |')
    S.append('|---|---|')
    S.append('| **b394** | a survey arm gated a rule it had itself improved — the eligible count '
             'was measured against a condition the rule does not carry. |')
    S.append('| **b396** | **three filters that kept nine tenths of what they were given**, thrown '
             'out with their yields printed rather than tightened. A filter that keeps nine tenths '
             'is not a filter. |')
    S.append('| **b397** | an arm took its population **from a name prefix** rather than from '
             'content, and a direction count was read the wrong way round — `--left-right` puts the '
             'main-only count first. |')
    S.append('| **b400** | `G-ONEQ` grepped raw prose for a claim the act refuses to make and '
             '**fired on the act’s own sentence saying it was not made** — b317/b348’s species in a '
             'prose haystack, where stripping strings cannot help. Rebuilt as an assertion-level '
             'predicate with both controls. |')
    S.append('| **b401** | `G-PRESERVE` was declared on the **wrong side of the push**: it compares '
             'a file against its committed blob, and after the push the blob *is* the file, so a '
             'correct write reads as a failure. Repaired in the arm — the reference is the pre-act '
             'commit on both sides — and **not on the locked face**. |')
    S.append('')
    S.append('### The seats’ own defects, declared by the acts that made them')
    S.append('')
    S.append('**This table is not a confession and it is not a boast.** It is here because the '
             'arc’s claimed product is a record checkable by a reader who trusts none of it, and a '
             'record whose defects are declared only when convenient is not that.')
    S.append('')
    S.append('| act | what it declared against itself |')
    S.append('|---|---|')
    S.append('| **b386** | ran an installer mid-act that **writes when run**, leaving backups it '
             'then had to account for. |')
    S.append('| **b387** | found two of its own claims living **only in an index hook** — one trim '
             'from gone, under no version control. |')
    S.append('| **b389** | its own predecessor’s finding was wrong and it said so; and its halt at '
             'the platform had to be **proved route by route** rather than asserted. |')
    S.append('| **b390** | routed a defect in eleven documents rather than repairing one and '
             'calling it done. |')
    S.append('| **b394** | **added a condition to a rule it was quoting**, and its own survey is '
             'where that showed. |')
    S.append('| **b396** | three of its own filters were vacuous, and it printed their yields '
             'rather than deleting them. |')
    S.append('| **b399** | its locked face named **five** new tool files and the act wrote **six**; '
             'both numbers printed, the face not edited. |')
    S.append('| **b400** | its write list, built by walking the ritual forward from the lock — the '
             'repair of b399’s species — **was still incomplete**: 8 of 38 files unnamed, 6 of them '
             'extra numbered runs of named kinds and 2 kinds never named. **Two arms of its own '
             'suite failed and were not weakened.** |')
    S.append('| **b401** | its face declared a preservation arm on the wrong side of the push, and '
             'the arm failed post-push because of it: **36 of 37 at the first post-push run**. Both '
             'readings printed; the locked face not edited. |')
    S.append('')
    S.append('*A fold is a summary of its acts at their own grades. It proves nothing, discharges '
             'nothing, and moves no grade. Every headline above was located by the anchor tool in '
             'the bank of the act it is attributed to — %d of %d, none missing — and no act is '
             'quoted from a later act’s summary of it.*' % (len(located), len(ACTS)))
    S.append('')

    # ---------------------------------------------------------------------------- THE APPEND
    rec('')
    rec('  ### (3) THE APPEND. ### **PURELY ADDITIVE.**')
    rec('  ' + '-' * 96)
    before = io.open(FINDINGS, encoding='utf-8', newline='').read()
    if TITLE in before:
        rec('    ### ALREADY FILED -- the title is present. ### NOTHING APPENDED.')
        after, appended = before, False
        prefix_ok = True
    else:
        io.open(FINDINGS, 'a', encoding='utf-8', newline=chr(10)).write(chr(10).join(S) + chr(10))
        after = io.open(FINDINGS, encoding='utf-8', newline='').read()
        appended = after.startswith(before)
        r = subprocess.run(['git', 'show', 'HEAD:FINDINGS.md'], cwd=PP, capture_output=True)
        committed = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
        prefix_ok = after.startswith(committed.rstrip(chr(10))) or after.startswith(committed)
        rec('    bytes %d -> %d ; lines %d -> %d'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')),
               len(before.split(chr(10))), len(after.split(chr(10)))))
        rec('    ### the pre-act FILE is a true prefix of the post-act file      : %s' % appended)
        rec('    ### the pre-act COMMITTED BLOB is a true prefix of it too       : %s' % prefix_ok)
        if not (appended and prefix_ok):
            rec('    ### ### **HARD FAILURE -- the write was not purely additive.**')
            run_clock.write(D, 'b402_fold_notes', LINES)
            return 1
    seg = after.split('## ' + TITLE, 1)[-1]
    low = ' '.join(seg.lower().split())
    says = {
        'the arc statement': 'artefact of how it had been measured' in low,
        'the scope beside it': '*scope:*' in low,
        'the act-by-act table': '| **b385** |' in low and '| **b401** |' in low,
        'the corrections table': 'a correction is not a re-verdict' in low,
        'the defective-bars table': 'the defective bars this span declared' in low,
        'the seat-defects table': 'declared by the acts that made them' in low,
        'the last two acts are in the defect table': '| **b400** |' in low and '| **b401** |' in low,
        'the fold proves nothing': 'it proves nothing, discharges nothing, and moves no grade'
                                   in low,
        'the navigator count is scored': 'sixteen' in low,
        'the threshold source is named': '(r1)' in low,
    }
    rec('')
    rec('  ### (4) WHAT THE SECTION SAYS, CHECKED RATHER THAN PROMISED.')
    rec('  ' + '-' * 96)
    for k, v in says.items():
        rec('    %-46s %s' % (k, v))
    if not all(says.values()):
        rec('    ### ### **HARD FAILURE -- the section does not carry what this file claims: %s**'
            % [k for k, v in says.items() if not v])
        run_clock.write(D, 'b402_fold_notes', LINES)
        return 1
    subprocess.run(['git', '-C', PP, 'add', '--', 'FINDINGS.md'], capture_output=True)
    rec('')
    rec('  ### ### **THE FOLD IS WRITTEN. ### %d ACTS, %d HEADLINES LOCATED, %d MISSING.**'
        % (hi - lo + 1, len(located), len(missing)))
    io.open(os.path.join(D, 'b402_fold.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(title=TITLE, lo=lo, hi=hi, acts=hi - lo + 1, threshold=THRESHOLD,
                        navigator_claim=16, located=len(located), missing=len(missing),
                        appended=appended, says=says), indent=1, ensure_ascii=False) + chr(10))
    run_clock.write(D, 'b402_fold_notes', LINES)
    return 0


if __name__ == '__main__':
    sys.exit(main())
