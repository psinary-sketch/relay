# -*- coding: utf-8 -*-
"""b396_desk_bank.py -- THE DESK, THE LEDGER WRITES, AND THE BANK.

### ### **THE ONLY CORPUS WRITE THIS ACT MAKES IS `(R21)`'S, AND `b396_components.py` MADE IT.**
### This file writes the ledgers and the bank, and closes what `(R7)` permits.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b396 how many findings rest on a backtick: 82 figures at risk -->'
PRIOR = '<!-- b395 the ceiling answered: the eleven were readable all along -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


SEALTXT = io.open(os.path.join(D, 'b396_registration_2026-09-10.txt'),
                  encoding='utf-8').read()
SEALHASH = re.search(r'sha256 of every byte ABOVE this block : ([0-9a-f]{64})', SEALTXT).group(1)
SEALSTAMP = re.search(r'locked at \(UTC\) : (\S+)', SEALTXT).group(1)

AC = J('b396_components')
LG = J('b396_lockgate')
E = J('b396_reads')
C1, C2, C3, A3 = AC['c1'], AC['c2'], AC['c3'], AC['a3']
S0, S1, S4 = E['s0'], E['s1'], E['s4']
BANKOUT = os.path.join(D, 'b396_the_backtick_swept.txt')


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


DESK = [
    ('M-2, under b310 cap', 'STAND', 'the aggregation is still SPECIFIED-NOT-STATED'),
    ("the object's conditions", 'STAND', "the conditions are the object's and none discharged"),
    ('the uniformity row U1', 'STAND', "the row's own refusal stands"),
    ('the instrument lane, PARKED under ruling R4', 'STAND', "PARKED by the author's ruling"),
    ('the wave, and the wave candidate list', 'STAND', "PARKED by the author's ruling"),
    ('the routed items, each with its owner', 'STAND', 'each still carries its owner'),
    ('the patent receipts, absent on the mounted volumes', 'STAND', "the patent seat owns it"),
    ('the count claim above the repaired Layer-1 list', 'STAND', 'no act sent to it since b369'),
    ("the retirement ledger's own lacunae", 'STAND', 'FILED, NOT INVENTED, AND NOT REPAIRED'),
    ('where the keystone census should live, ROUTED at b375', 'STAND', 'ROUTED to the author'),
    ("the census's definition-versus-operation drift", 'STAND', 'FILED at b377, NOT REPAIRED'),
    ('LIST 1 -- the rows that cite at a ref nobody can name', 'STAND', 'OPEN'),
    ('LIST 2 -- the rows grading a declaration the record has classified absent', 'STAND',
     'OPEN. ### This act moves no grade'),
    ('LIST 3 -- the undated figures across the roster', 'STAND', 'OPEN. ### This act dates none'),
    ('LIST 4 -- the bibliography entries nothing cites', 'STAND', 'OPEN'),
    ('the three amendments b383 drafted that are still routed', 'STAND', 'ROUTED AND UNAPPLIED'),
    ('the download-layer book`s registry drift', 'STAND', "OPEN AND THE AUTHOR`S"),
    ('the six subject clusters with no keystone', 'STAND', '`NOT-YET-SYNTHESIZED` since b385'),
    ('column (d) is a FLOOR and the wider question is named', 'STAND', 'NOT RE-MEASURED'),
    ('the ten untracked run records of earlier acts', 'STAND', 'NAMED at b382, STILL UNTRACKED'),
    ('the legacy `.git/hooks/pre-push` copies', 'STAND', '### **RULED BY `(R16)`: THEY STAY**'),
    ('the untracked `.b304-backup` artifacts', 'STAND', 'NAMED at b386, still untracked'),
    ('the five keystones the union names that carry no correspondence table', 'STAND',
     'CONFIRMED BY READING at b394 and NOT REPAIRED. ### **STILL THE AUTHOR`S**'),
    ('the 23 unreadable correspondence rows', 'STAND', 'NAMED at b388 by cause, and ROUTED'),
    ('the seat`s memory is under no version control', 'STAND', 'NAMED at b387, routed'),
    ('the keystone-class documents b388 marked UNASSIGNED', 'STAND',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT**'),
    ('the deposited layer, unread since b389', 'STAND',
     'STILL BLOCKED; this act did not ask the platform'),
    ('the eight-versus-six cluster-synthesis disagreement', 'STAND', 'ROUTED at b389'),
    ('the practice that let the phantom drift run', 'STAND',
     'TWO INSTANCES in four acts. ### **NOTHING IN THE CORPUS CHECKS A CITED VERSION AGAINST '
     'ITS TARGET.** ### **STILL OPEN**'),
    ('the `66` superseded version citations', 'STAND', 'REPORTED at b391 and LEFT'),
    ('`CONSTANCE.md` carries no version in its own bytes', 'STAND', 'ROUTED at b391'),
    ('placement into `Tier KC`', 'STAND', 'PRICED at b393 and STILL EMPTY'),
    ('whether `SIDE-kernel` has a current citable record', 'STAND', 'ROUTED at b392'),
    ('the two deposited records` remediation', 'STAND',
     'DRAFTED at b395 and WRITTEN NOWHERE; the smallest recovering read for `19675356` is '
     'named and ### **THIS SEAT CANNOT PERFORM IT.** ### **STILL THE AUTHOR`S**'),
    ('the anchor question, unanswerable for three of five', 'STAND', 'ROUTED at b393'),
    ('the `34` federation names the drive does not hold', 'STAND', 'FILED at b395, not repaired'),
    ('`theory-space` shares nothing between its two members', 'STAND', 'ROUTED at b395'),
    ('`cross-domain` has something for a synthesis to be about', 'STAND', 'ROUTED at b395'),
    ('`ENUMERA` names no terminal at all', 'STAND',
     'ROUTED at b395. ### **AND THIS ACT`S PRICE CONFIRMS IT IS NOT A READING PROBLEM:** ### '
     'reading the other ten reaches `%d` of `%d` and leaves `ENUMERA` untouched -- ### **WHAT '
     'IT NEEDS IS AN AUTHOR NAMING ITS TERMINAL**' % (C3['after'], C3['of'])),
    ('the fifteen keystones not read', 'STAND',
     '### **AND THIS ACT PRICES IT FOR THE FIRST TIME:** ### `%s` minutes at `b394``s own '
     'measured rate takes the census from `%d` of `%d` to ### **`%d` OF `%d`.** ### **THE '
     'FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR**, and the rate came from the easy end. '
     '### **STILL AVAILABLE AND NOT DONE**'
     % (C3['minutes'], C3['reconciled'], C3['of'], C3['after'], C3['of'])),

    # ---- WHAT THIS ACT CLOSES AND ADDS -----------------------------------------------------------
    ('the predicate that produced `b394``s ceiling', 'CLOSE',
     '### **CLOSED BY `(R7)`: THE OCCASION IS GONE, BECAUSE THIS ACT IS THE MEASUREMENT.** ### '
     '`b395` opened this item saying ### *how many other findings rest on a backtick is '
     'UNMEASURED.* ### It is now measured: `%d` instruments carry a narrow test, `%d` carry an '
     'at-risk figure, and the at-risk figures number `%d` across `%d` acts. ### **THE ITEM '
     'ASKED FOR A MEASUREMENT AND HAS ONE**'
     % (C1['narrow'], C1['files'], C1['figures'], C1['acts'])),
    ('the `82` at-risk figures, unrepaired', 'STAND',
     '### **NEW at `b396`, AND IT IS THE ITEM THE CLOSED ONE BECAME.** ### `%d` figures across '
     '`%d` instruments rest on a matcher that requires a backtick, a case, or a leading marker, '
     'under a report that states an absence. ### **THIS ACT REPAIRS NONE OF THEM** -- naming a '
     'body of work is not doing it -- and `%d` were re-run with all `%d` CONFIRMED. ### **A '
     'CONFIRMATION IS THE WEAKER RESULT** and `%d` are untested. ### **OPEN**'
     % (C1['figures'], C1['files'], C2['runs'], C2['runs'], C1['figures'] - C2['runs'])),
    ('the self-reading / corpus-reading distinction, unmeasurable at module granularity', 'STAND',
     '### **NEW at `b396`.** ### A narrow matcher against text the act WROTE fails its own gate '
     'loudly; one against the CORPUS shrinks a finding in silence, which is `b394``s species. '
     '### **THAT IS WHERE THE RISK LIVES AND THE MODULE-LEVEL TEST KEPT `79` OF `82`** -- '
     'nearly every instrument names a corpus path somewhere. ### **A TRUE DISTINCTION A TOOL '
     'CANNOT DRAW IS FILED, NOT APPLIED.** ### **OPEN**'),
    ('the five deafnesses of this sweep', 'STAND',
     '### **NEW at `b396`, AND STATED IN THE INSTRUMENT ITSELF.** ### A narrowness assembled '
     'from a variable at run time; one living in the DATA a tool reads; a matcher passed in '
     'from another module; a shape restriction with no string and no case method; and ### '
     '**WHETHER A NARROW MATCHER IS WRONG.** ### **EVERY `CONFIRMED` IN THIS ACT STANDS IN '
     'FRONT OF THESE FIVE.** ### **OPEN**'),
    ('the judgement half of the preservation rule', 'STAND',
     '### **NEW at `b396`.** ### `>` is ### **SUFFICIENT AND NOT NECESSARY** ### for a '
     'preserved block, so the mechanized arm is ### **A FLOOR ON THE HAZARD AND NOT A GUARD '
     'AGAINST IT.** ### Whether a passage carrying no `>` is preserved is judgement and ### '
     '**IS NOT CLAIMED AS MECHANIZED.** ### **OPEN**'),
]


def do_desk():
    rec('    ### ### **THIS ACT CLOSES ONE ITEM BY MEASURING IT, AND THE MEASUREMENT OPENS FOUR.**')
    rec('    ### `b395` left an item reading ### *how many other findings rest on a backtick is')
    rec('    ### UNMEASURED.* ### **THAT IS NOW MEASURED**, so `(R7)` closes it -- and what the')
    rec('    ### measurement found is four new items, three of which are limits rather than')
    rec('    ### defects. ### **A MEASUREMENT THAT OPENS MORE THAN IT CLOSES IS STILL A')
    rec('    ### ### MEASUREMENT.**')
    rec('')
    marks = []
    for item, want, why in DESK:
        marks.append(dict(item=item, disposition=want, why=why))
        rec('    %-74s %s' % (item[:74], want))
        for k in range(0, min(len(why), 900), 150):
            rec('        %s' % why[k:k + 150])
    closed = [m for m in marks if m['disposition'] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(marks), len(closed), len(marks) - len(closed)))
    rec('    ### ### **FOUR ITEMS ARE ADDED AND ALL FOUR STAND** -- because ### **A FINDING')
    rec('    ### ### RECORDED IS NOT A FINDING DISCHARGED**, and three of the four are ### **LIMITS')
    rec('    ### ### OF THIS ACT`S OWN INSTRUMENT**, filed so a later act does not inherit them')
    rec('    ### ### unstated.')
    return dict(items=len(marks), closed=len(closed), standing=len(marks) - len(closed),
                lists_closed=0, marks=marks)


SCOPE = (
    "**SCOPE: HOW MANY FINDINGS REST ON A BACKTICK -- AND THE QUESTION HAS NO ANSWER AT INSTRUMENT "
    "GRANULARITY.** **THE ORDER'S FIRST INSTRUCTION WAS DISCHARGED BEFORE ANYTHING WAS SWEPT**: the "
    "detector was run against a fixture carrying ONE NARROW MATCHER WRITTEN THREE WAYS -- a "
    "raw-string regex, a double-quoted escaped regex, and A FORM WITH NO REGEX AT ALL -- and ALL "
    "THREE WERE FOUND, with a WIDE fixture run beside them coming back CLEAN, because without a "
    "negative control a fixture shows a detector FIRES and not that it DISCRIMINATES. **WHAT THE "
    "SWEEP IS DEAF TO IS STATED IN THE INSTRUMENT ITSELF AND NOT ONLY IN THE BANK**, and it is five "
    "things. A RAW grep IS NOT THE INSTRUMENT: 826 of 858 files in tools/ carry a backtick "
    "somewhere and almost every one is PROSE, so the sweep reads by ast and keeps a literal only "
    "where it is USED AS A TEST. **THE FUNNEL: 856 parsed, 407 carrying a narrow test, 64 carrying "
    "an at-risk figure, and 82 AT-RISK FIGURES across 51 acts.** **THREE FILTERS WERE TRIED AND "
    "DISCARDED BEFORE THE LOCK AND ALL THREE ARE REPORTED WITH THEIR YIELDS** -- printed-absence "
    "kept 374 of 407, act-name-in-a-ledger kept 350 of 380, and reads-corpus-text kept 79 of 82 -- "
    "because A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER and A TIGHTENING MADE IN "
    "SILENCE IS ONE NOBODY CAN AUDIT. **THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT: THE "
    "NARROW SHAPE IS PERVASIVE.** The third is a TRUE DISTINCTION THIS TOOL CANNOT DRAW -- a narrow "
    "matcher against text the act WROTE fails its own gate loudly while one against the CORPUS "
    "shrinks a finding in silence, which is b394's species, and that is where the risk lives -- so "
    "it is FILED AS A LIMIT AND NOT APPLIED AS A FILTER. **THE CHEAPEST THREE AND THE MOST EXPOSED "
    "THREE SHARE NO MEMBER**, exposure being counted OUTSIDE the act's own artifacts, and **ALL SIX "
    "WERE RUN** because every one is a local read and a choice not worth making is not made. **THE "
    "UNIT IS THE FIGURE AND NOT THE MATCH COUNT**: an earlier form of the component read the act's "
    "data records instead of the text the matcher actually read and compared counts where the "
    "figure is a BOOLEAN, and it called two of the six MOVED -- BOTH WERE ARTEFACTS OF THE HARNESS "
    "and were repaired before the bank. **ALL SIX RE-RUNS CONFIRMED; 0 FIGURES MOVED; 1 NARROWNESS "
    "WITHOUT CONSEQUENCE** (b318 matches once narrow and twice wide and the figure is True either "
    "way). **(L2) IS THEREFORE REFUTED AND THIS SEAT REGISTERED THAT BEFORE THE LOCK**; (L1) IS MET "
    "AT 64 AND 82; **(L3) IS MET BY b395 AND NOT BY THIS ACT** -- b394 reported no kernel "
    "repository on the drive for 8 keystones and the drive holds one for every one. **A "
    "CONFIRMATION IS THE WEAKER RESULT**: it proves a figure is not an artefact of THE SHAPE THAT "
    "WAS WIDENED, and 76 figures are untested. THE TEN NOW-REACHABLE KEYSTONES ARE **PRICED AND NOT "
    "READ** at b394's own measured rate, 2.8 x 10 = 28.0 MINUTES, taking the census from 4 of 16 to "
    "14 of 16 and leaving ENUMERA, which needs an author; **THE FIGURE IS A FLOOR BECAUSE ITS INPUT "
    "IS A FLOOR** and the rate came from the easy end. THE PRESERVATION HAZARD IS FILED WITH b395's "
    "near miss as its incident and **MECHANIZED IN PART**: anchor_from_file.py gains an OPT-IN, "
    "DEFAULT-OFF editing mode excluding blockquoted lines and REFUSING an anchor that resolves only "
    "inside one, proved by 12 fixture arms with 0 failing, and **144 CALLERS WITH 0 MOVED**; the "
    "JUDGEMENT HALF -- whether a passage with no > is preserved -- IS LISTED APART AND NOT CLAIMED "
    "AS MECHANIZED, so the arm is A FLOOR ON THE HAZARD AND NOT A GUARD AGAINST IT. One TECHNE "
    "module written, LOCAL AND NOT PUSHED. **NO INSTRUMENT OF ANY PRIOR ACT IS REPAIRED OR EDITED "
    "AND NO CORPUS DOCUMENT IS EDITED AT ALL.** NO GRADE MOVED, NO CLAIM WITHDRAWN, NO "
    "CORRESPONDENCE TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED "
    "OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NEITHER MAP TOUCHED, NO "
    "CLUSTER RESHAPED, NO LIST CLOSED, NO PRIOR ACT'S FACE OR BANK EDITED. NOTHING DEPOSITS; **THE "
    "PLATFORM WAS NOT CALLED AT ALL**; 0 REPOSITORIES CLONED, 0 BRANCHES FETCHED MERGED PUSHED OR "
    "CREATED, NO BUILD RUN AND NO AXIOM PROFILE RECOMPUTED. **THE FOUR OPEN LISTS ARE RESTATED OPEN "
    "BY NAME.** NO NEW TRACKING DOCUMENT WAS CREATED. NO ARCHIVE OR outputs FILE TOUCHED, THE "
    "MIRROR ROSTER NOT EDITED, NO .git/hooks/pre-push DELETED. NO .lean FILE TOUCHED. NOTHING IS "
    "CLAIMED ABOUT THE MATHEMATICS OF ANY NAMED SUBJECT. NOTHING WAS COMPUTED ABOUT THE OBJECT. "
    "Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE "
    "HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS "
    "STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, "
    "still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
    "record. THE INSTRUMENT LANE STAYS PARKED. THE WAVE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. "
    "h2 stands exactly where the deposit left it and this act makes no claim about it in either "
    "direction.")


def trail_block(Q):
    return [
        '', MARK, '',
        '### **b396 — HOW MANY FINDINGS REST ON A BACKTICK (2026-09-10)**',
        '',
        ('*No block above is edited. The b395 block (`%s`) and every block before it stand exactly '
         'as they were written.*' % PRIOR),
        '',
        ('**THE ORDER\u2019S FIRST INSTRUCTION, DISCHARGED BEFORE ANYTHING WAS SWEPT.** b395 found '
         'that the prior order had not tested its own premise, so this one required that the sweep '
         'be shown capable of finding a narrow matcher written in a form it did not anticipate. '
         'The fixture carries **one narrow matcher written three ways** — a raw-string regex, a '
         'double-quoted escaped regex, and **a form with no regex at all** (`startswith` + `in` + '
         '`islower()`) — and **all three are found**. A **wide** fixture runs beside them and comes '
         'back **clean**, because without a negative control a fixture shows only that a detector '
         '*fires*, not that it **discriminates**. **What the sweep is deaf to is stated in the '
         'instrument itself**, and it is five things: a narrowness assembled from a variable at run '
         'time; one living in the data a tool reads; a matcher passed in from another module; a '
         'shape restriction with no string and no case method; and **whether a narrow matcher is '
         'wrong** — the shape is measured, never the verdict.'),
        '',
        ('**A RAW `grep` IS NOT THE INSTRUMENT, AND THE NUMBERS SAY SO.** **`%d` of `%d`** files in '
         '`tools/` carry a backtick somewhere, and almost every one is prose. **A backtick in a '
         'sentence is not a backtick in a matcher**, so the sweep reads by `ast` and keeps a '
         'literal only where it is *used as a test*.'
         % (S0['raw_backtick'], S0['tools'])),
        '',
        ('**THE FUNNEL, EVERY STAGE PRINTED.** `%d` instruments parsed, `0` unparseable; **`%d` '
         'carry at least one narrow test**; **`%d` carry at least one at-risk figure**; and the '
         '**at-risk figures number `%d`**, across `%d` acts. A figure is at risk when a narrow '
         'literal\u2019s yield is bound to a name and a report naming that same name carries an '
         'absence **in its own literal** — the absence and the measurement in the same sentence, or '
         'it is prose that happens to contain the word *no*.'
         % (C1['parsed'], C1['narrow'], C1['files'], C1['figures'], C1['acts'])),
        '',
        ('**THREE FILTERS WERE TRIED AND DISCARDED BEFORE THE LOCK, AND ALL THREE ARE REPORTED WITH '
         'THEIR YIELDS.** *The module prints an absence somewhere* kept **374 of 407**. *The '
         'act\u2019s name appears in a ledger* kept **350 of 380** — every act names itself in its '
         'own row, so it measured nothing. *The instrument reads corpus text rather than its own '
         'artifacts* kept **79 of 82**. **A filter that keeps nine tenths of its input is not a '
         'filter**, and a tightening made in silence is one nobody can audit. **Three vacuous '
         'filters in one act is itself the result: the narrow shape is pervasive**, so the '
         'order\u2019s question has **no answer at instrument granularity** — it has one at figure '
         'granularity, and that is the list. The third is a **true distinction this tool cannot '
         'draw**: a narrow matcher against text the act *wrote* fails its own gate loudly, while '
         'one against the *corpus* shrinks a finding in silence — which is b394\u2019s species and '
         'is where the risk actually lives. **It is filed as a limit, not applied as a filter.**'),
        '',
        ('**SIX RE-RUNS, AND THE TWO CRITERIA PICK DIFFERENT SETS.** The cheapest three are '
         '`b307 b318 b323`; the most exposed three are `b392 b326 b332`; **they share `%d` '
         'members**. **All six were run**, because every one is a local read and the paragraph '
         'justifying a choice would cost more than the choice saves. **The unit is the figure and '
         'not the match count**: an earlier form of this component read each act\u2019s `data/` '
         'records instead of the text its matcher actually read, and compared counts where the '
         'figure is a boolean — it called two of the six MOVED, **and both were artefacts of the '
         'harness**, repaired before this bank. **Result: `%d` CONFIRMED, `%d` MOVED, and `%d` '
         'narrowness without consequence** — `b318`\u2019s literal matches once narrow and twice '
         'wide while its figure is `True` either way. **`(L2)` is therefore REFUTED**, which this '
         'seat registered as `(E2)` before the lock: **a confirmation is the weaker result**, and '
         'the arc\u2019s one known move was found by reading a document, not by widening a regex. '
         '**`(L3)` is met by b395 and not by this act** — b394 reported *no kernel repository it '
         'names is on the drive* for `8` keystones and the drive holds one for every one of them.'
         % (C2['shared'], C2['verdicts'].get('CONFIRMED', 0), C2['moved'], C2['nwc'])),
        '',
        ('**THE TEN NOW-REACHABLE KEYSTONES: PRICED, NOT READ.** At b394\u2019s own measured rate '
         'of **`%s` per keystone**, reading the ten costs **`%s` minutes** and takes the census '
         'from **`%d` of `%d`** to **`%d` of `%d`**, leaving **`%d`** — `ENUMERA`, which names no '
         'terminal and needs an author rather than a reader. **The figure is a floor because its '
         'input is a floor**: b394 declared both of its figures floors, and **a rate taken from '
         'the easy end prices the hard end too cheaply**. The item stays on the desk as '
         '**available and not done**.'
         % (C3['per_keystone'], C3['minutes'], C3['reconciled'], C3['of'], C3['after'],
            C3['of'], C3['remaining'])),
        '',
        ('**THE PRESERVATION HAZARD, FILED AND MECHANIZED IN PART.** b395\u2019s needle for the '
         'live cluster row matched b388\u2019s **preserved quotation** of the superseded table and '
         '**resolved to it silently**, having met it first; an act editing by that anchor would '
         'have edited a quotation the corpus preserved so that it would not change. **The rule: an '
         'editing anchor excludes preserved blocks by construction, and an anchor resolving inside '
         'one is refused rather than disambiguated** — a caller told *ambiguous* picks one, and '
         'picking is how the quotation gets edited. The paper tree carries **`%d` blockquoted '
         'blocks across `%d` documents** plus `%d` explicit preservation banners, so the '
         'mechanized half is real: `anchor_from_file.py` gains an **opt-in, default-off** '
         '`editing=True`, proved by **`%d` fixture arms with `%d` failing** and by **`%d` callers '
         'of which `%d` moved**. The default is off on purpose — **the hazard is editing by an '
         'anchor, not reading by one**. And the **judgement half is listed apart and not claimed '
         'as mechanized**: `>` is sufficient and not necessary, so the arm is **a floor on the '
         'hazard and not a guard against it** — this act\u2019s own subject turned on its own '
         'remedy. One TECHNE module, **local and not pushed**. **The four lists stay OPEN by '
         'name.** **Nothing deposits and the platform was not called at all.**'
         % (A3['blocks'], A3['files'], A3['banners'], A3['arms'], A3['failing'],
            A3['callers'], A3['moved'])),
        '',
    ]


def corr_rows(Q):
    m = ("**THE BACKTICK SWEPT: 82 AT-RISK FIGURES ACROSS 64 INSTRUMENTS, SIX RE-RUN AND ALL SIX "
         "CONFIRMED, AND THREE FILTERS DISCARDED BEFORE THE LOCK** (b396, how many findings rest "
         "on a backtick)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, CHAINED ON A LOCK GATE THAT "
            "CHECKS WHAT EACH GATE READ** -- b378's gate run as b396, %d gates read and %d checked "
            "by digest. **THE ORDER'S FIRST INSTRUCTION WAS DISCHARGED BEFORE ANYTHING WAS SWEPT**: "
            "the detector was run against a fixture carrying ONE NARROW MATCHER WRITTEN THREE WAYS, "
            "INCLUDING ONE WITH NO REGEX AT ALL, and ALL THREE WERE FOUND, with a WIDE fixture "
            "beside them coming back CLEAN. A RAW grep IS NOT THE INSTRUMENT: %d of %d files in "
            "tools/ carry a backtick and almost every one is PROSE, so the sweep reads by ast and "
            "keeps a literal only where it is USED AS A TEST. THE FUNNEL: %d parsed, %d carrying a "
            "narrow test, %d carrying an at-risk figure, and %d AT-RISK FIGURES across %d acts. "
            "**THREE FILTERS WERE TRIED AND DISCARDED BEFORE THE LOCK WITH THEIR YIELDS PRINTED** "
            "-- 374 of 407, 350 of 380, 79 of 82 -- because A FILTER THAT KEEPS NINE TENTHS OF ITS "
            "INPUT IS NOT A FILTER, and THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT: THE "
            "NARROW SHAPE IS PERVASIVE and the question HAS NO ANSWER AT INSTRUMENT GRANULARITY. "
            "THE CHEAPEST THREE AND THE MOST EXPOSED THREE SHARE %d MEMBERS AND ALL SIX WERE RUN. "
            "**THE UNIT IS THE FIGURE AND NOT THE MATCH COUNT**: an earlier form read the wrong "
            "input and compared counts where the figure is a BOOLEAN, calling two MOVED, and BOTH "
            "WERE ARTEFACTS OF THE HARNESS, repaired before the bank. %d CONFIRMED, %d MOVED, %d "
            "NARROWNESS WITHOUT CONSEQUENCE, so (L2) IS REFUTED as this seat registered before the "
            "lock. THE TEN NOW-REACHABLE KEYSTONES ARE PRICED AND NOT READ at %s minutes, taking "
            "the census from %d of %d to %d of %d, AND THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A "
            "FLOOR. THE PRESERVATION HAZARD IS FILED AND MECHANIZED IN PART: an OPT-IN DEFAULT-OFF "
            "editing mode in anchor_from_file.py, %d fixture arms %d failing, %d callers %d moved, "
            "with the JUDGEMENT HALF LISTED APART AND NOT CLAIMED AS MECHANIZED"
            % (LG['gates_read'], LG['face_subject_gates'], S0['raw_backtick'], S0['tools'],
               C1['parsed'], C1['narrow'], C1['files'], C1['figures'], C1['acts'],
               C2['shared'], C2['verdicts'].get('CONFIRMED', 0), C2['moved'], C2['nwc'],
               C3['minutes'], C3['reconciled'], C3['of'], C3['after'], C3['of'],
               A3['arms'], A3['failing'], A3['callers'], A3['moved']))
    term = ("### NO TERMINAL IS CLAIMED BY THIS ACT AS ITS OWN. ### 856 of the record's own "
            "instruments were parsed and read by ast; NO KERNEL WAS OPENED, NO STATEMENT PROVED, "
            "NO BUILD RUN, NO REPOSITORY CLONED AND NO BRANCH FETCHED MERGED PUSHED OR CREATED. "
            "### READING AN INSTRUMENT IS NOT VERIFYING WHAT IT MEASURED")
    prof = ("### NO AXIOM PROFILE. ### NO .lean FILE WAS TOUCHED AND NOTHING WAS COMPUTED ABOUT "
            "THE OBJECT. ### NO INSTRUMENT OF ANY PRIOR ACT WAS REPAIRED OR EDITED AND NO CORPUS "
            "DOCUMENT WAS EDITED AT ALL. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CORRESPONDENCE "
            "TABLE WRITTEN EXTENDED OR RE-GRADED, NO CLASS RULED, NO DOCUMENT RECLASSIFIED OR "
            "PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO CLUSTER RESHAPED, "
            "NO LIST CLOSED. ### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL")
    grade = ("### THE SWEEP'S OWN PREMISE WAS TESTED BEFORE THE SWEEP RAN, ON THREE FORMS AND A "
             "WIDE CONTROL. ### THE FIGURE FILTER WAS TESTED ON BOTH AXES. ### EVERY STAGE OF THE "
             "FUNNEL IS PRINTED AND EVERY DISCARDED FILTER CARRIES ITS YIELD. ### EVERY WIDENING "
             "WAS WRITTEN IN THE TOOL BEFORE IT RAN. ### THE HARNESS DEFECT THAT PRODUCED TWO FALSE "
             "MOVES WAS FOUND AND REPAIRED BEFORE THE BANK, AND IS REPORTED. ### THE FIVE "
             "DEAFNESSES STAND IN FRONT OF EVERY CONFIRMED. ### THE ADDED ANCHOR MODE IS OPT-IN AND "
             "0 CALLERS MOVED")
    status = ("data/b396_the_backtick_swept.txt; data/%s; data/%s; "
              "data/b396_registration_2026-09-10.txt (LOCKED before any write, chained on "
              "tools/b378_lockgate.py run as b396); tools/b396_narrow.py; tools/b396_figures.py; "
              "tools/b396_extract.py; tools/b396_regspec.py; tools/b396_reg_gate.py; "
              "tools/b396_components.py; tools/b396_desk_bank.py; tools/b396_checks.py; "
              "tools/anchor_from_file.py (one added opt-in mode and its fixtures); "
              "PLACE-papers OPEN_TRAILS.md (an append-only block); "
              "CORRESPONDENCE.md row %%d" % (AC['run_file'], E['run_file']))
    return [(m, stmt, term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('how many findings rest on a backtick', 'was the sweep itself narrow',
           'what is a figure at risk', 'did any figure move when the predicate was widened',
           'what does it cost to read the ten reachable keystones',
           'can an anchor edit a preserved block')
MUST_NOT_HIT = ('the sweep was not tested', 'a filter was discarded in silence',
                'an instrument was repaired', 'the platform was called')


def do_key(rownum):
    KEY = 'the-backtick-swept'
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), chr(10)))
    statement = (
        "b396 MEASURED WHAT b395 LEFT UNMEASURED. THE ORDER'S FIRST INSTRUCTION WAS DISCHARGED "
        "BEFORE ANYTHING WAS SWEPT: the detector was run against a fixture carrying ONE NARROW "
        "MATCHER WRITTEN THREE WAYS, INCLUDING ONE WITH NO REGEX AT ALL, and ALL THREE WERE FOUND, "
        "with a WIDE fixture coming back CLEAN so the fixture shows DISCRIMINATION and not merely "
        "firing. A RAW grep IS NOT THE INSTRUMENT: %d OF %d FILES IN tools/ CARRY A BACKTICK AND "
        "ALMOST EVERY ONE IS PROSE, so the sweep reads by ast and keeps a literal only where it is "
        "USED AS A TEST. THE FUNNEL: %d PARSED, %d CARRYING A NARROW TEST, %d CARRYING AN AT-RISK "
        "FIGURE, AND %d AT-RISK FIGURES ACROSS %d ACTS. THREE FILTERS WERE TRIED AND DISCARDED "
        "BEFORE THE LOCK WITH THEIR YIELDS PRINTED -- 374 OF 407, 350 OF 380, 79 OF 82 -- AND "
        "THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT: THE NARROW SHAPE IS PERVASIVE AND "
        "THE QUESTION HAS NO ANSWER AT INSTRUMENT GRANULARITY, ONLY AT FIGURE GRANULARITY. THE "
        "CHEAPEST THREE AND THE MOST EXPOSED THREE SHARE %d MEMBERS AND ALL SIX WERE RUN. THE UNIT "
        "IS THE FIGURE AND NOT THE MATCH COUNT: AN EARLIER FORM READ THE WRONG INPUT AND COMPARED "
        "COUNTS WHERE THE FIGURE IS A BOOLEAN, CALLING TWO MOVED, AND BOTH WERE ARTEFACTS OF THE "
        "HARNESS. %d CONFIRMED, %d MOVED, %d NARROWNESS WITHOUT CONSEQUENCE, SO (L2) IS REFUTED AS "
        "THIS SEAT REGISTERED BEFORE THE LOCK, AND (L3) IS MET BY b395 RATHER THAN BY THIS ACT. A "
        "CONFIRMATION IS THE WEAKER RESULT AND %d FIGURES ARE UNTESTED. THE TEN NOW-REACHABLE "
        "KEYSTONES ARE PRICED AND NOT READ AT %s MINUTES, TAKING THE CENSUS FROM %d OF %d TO %d OF "
        "%d, AND THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR. THE PRESERVATION HAZARD IS "
        "FILED WITH b395'S NEAR MISS AS ITS INCIDENT AND MECHANIZED IN PART: AN OPT-IN DEFAULT-OFF "
        "EDITING MODE THAT EXCLUDES BLOCKQUOTED LINES AND REFUSES AN ANCHOR RESOLVING ONLY INSIDE "
        "ONE, %d FIXTURE ARMS %d FAILING, %d CALLERS %d MOVED, WITH THE JUDGEMENT HALF LISTED APART "
        "AND NOT CLAIMED AS MECHANIZED."
        % (S0['raw_backtick'], S0['tools'], C1['parsed'], C1['narrow'], C1['files'],
           C1['figures'], C1['acts'], C2['shared'], C2['verdicts'].get('CONFIRMED', 0),
           C2['moved'], C2['nwc'], C1['figures'] - C2['runs'], C3['minutes'],
           C3['reconciled'], C3['of'], C3['after'], C3['of'],
           A3['arms'], A3['failing'], A3['callers'], A3['moved']))
    grade = (
        "### NO INSTRUMENT OF ANY PRIOR ACT WAS REPAIRED OR EDITED AND NO CORPUS DOCUMENT WAS "
        "EDITED AT ALL. ### NO GRADE MOVED, NO CLAIM WITHDRAWN, NO CLASS RULED, NO DOCUMENT "
        "RECLASSIFIED OR PLACED IN Tier KC, NO REGISTRY ROW EDITED, THE CENSUS NOT EDITED, NO "
        "CLUSTER RESHAPED, NO LIST CLOSED, NO PRIOR FACE OR BANK EDITED. ### THE ONLY relay EDIT "
        "OUTSIDE THIS ACT'S OWN FILES IS ONE INDEX KEY AND ONE ADDED OPT-IN MODE IN "
        "anchor_from_file.py, WITH 0 CALLERS MOVED. ### THE SWEEP'S OWN PREMISE WAS TESTED FIRST. "
        "### EVERY DISCARDED FILTER CARRIES ITS YIELD. ### EVERY WIDENING WAS STATED BEFORE IT RAN. "
        "### NOTHING DEPOSITS AND THE PLATFORM WAS NOT CALLED AT ALL. ### THE FOUR OPEN LISTS ARE "
        "RESTATED OPEN BY NAME. ### M-2 UNCHANGED")
    where = (
        "data/b396_the_backtick_swept.txt; data/%s; data/%s; "
        "data/b396_registration_2026-09-10.txt (LOCKED before any write, chained on "
        "tools/b378_lockgate.py run as b396 -- %d gates read, %d checked by digest); "
        "tools/b396_narrow.py; tools/b396_figures.py; tools/b396_extract.py; "
        "tools/b396_regspec.py; tools/b396_reg_gate.py; tools/b396_components.py; "
        "tools/b396_desk_bank.py; tools/b396_checks.py; tools/anchor_from_file.py; "
        "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %d"
        % (AC['run_file'], E['run_file'], LG['gates_read'], LG['face_subject_gates'], rownum))
    act = ('b396 (the backtick swept: 82 at-risk figures across 64 instruments, six re-run and '
           'all six confirmed, and three filters discarded before the lock)')
    row_new = ('    # ### THE BACKTICK SWEPT (b396).%s'
               '    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (chr(10), KEY, act, chr(10), statement, chr(10), grade, chr(10), where,
                  chr(10)))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-44s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + chr(10)
    ROW_ANCHOR = ('INDEX = [' + chr(10)
                  + '    # (key, act, one-line statement, grade as its own act recorded it, '
                    'location)' + chr(10))
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ('"%s"' % KEY) not in txt and ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    open(INDEX + '.tmp', 'wb').write(txt.encode('utf-8'))
    os.replace(INDEX + '.tmp', INDEX)
    ok = True
    out, rc = query(KEY)
    n = out.count('act      :')
    good = (not no_key(out)) and rc == 0 and n >= 1
    ok = ok and good
    rec('  READ BACK : %s returns %d row(s)  %s' % (KEY, n, 'PASS' if good else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g = (not no_key(o)) and KEY in o
        ok = ok and g
        rec('    %-52s reaches the b396 key : %s' % (qq, g))
    for lbl, cond in (('the premise was tested before the sweep',
                       'DISCHARGED BEFORE ANYTHING WAS SWEPT' in out),
                      ('three forms including one with no regex',
                       'INCLUDING ONE WITH NO REGEX AT ALL' in out),
                      ('the wide control discriminates', 'DISCRIMINATION' in out),
                      ('a grep is not the instrument', 'ALMOST EVERY ONE IS PROSE' in out),
                      ('the funnel is stated', 'AT-RISK FIGURES ACROSS' in out),
                      ('the discards carry their yields', '374 OF 407' in out),
                      ('the shape is called pervasive', 'THE NARROW SHAPE IS PERVASIVE' in out),
                      ('the figure is the unit',
                       'THE UNIT IS THE FIGURE AND NOT THE MATCH COUNT' in out),
                      ('the harness defect is owned',
                       'ARTEFACTS OF THE HARNESS' in out),
                      ('a confirmation is the weaker result',
                       'A CONFIRMATION IS THE WEAKER RESULT' in out),
                      ('the price is a floor',
                       'A FLOOR BECAUSE ITS INPUT IS A FLOOR' in out),
                      ('the anchor mode is opt-in and moved nobody',
                       'OPT-IN DEFAULT-OFF' in out),
                      ('the judgement half is not claimed as mechanized',
                       'NOT CLAIMED AS MECHANIZED' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g = pre[qq] and no_key(o)
        ok = ok and g
        rec('    %-44s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def main():
    bar('=')
    rec('b396 -- THE DESK, THE LEDGER WRITES, AND THE BANK.')
    bar('=')
    bar()
    rec('  ### THE DESK UNDER (R7).')
    bar()
    Q = do_desk()

    rec()
    bar()
    rec('  ### THE TRAIL BLOCK, APPEND-ONLY.')
    bar()
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        after = before
        tr = dict(appended_only=True, committed_prefix_intact=True, prior_present=True)
    else:
        rec('  ### the b394 block is present and is not edited : %s' % (PRIOR in before))
        io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(trail_block(Q)) + chr(10))
        after = io.open(TRAILS, encoding='utf-8', newline='').read()
        committed = blob('OPEN_TRAILS.md')
        ao = after.startswith(before)
        pi = committed in after.replace(chr(13) + chr(10), chr(10))
        rec('  ### bytes %d -> %d ; append-only %s ; committed still a substring %s'
            % (len(before.encode('utf-8')), len(after.encode('utf-8')), ao, pi))
        subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
        tr = dict(appended_only=ao, committed_prefix_intact=pi, prior_present=(PRIOR in before))
    seg = after.split(MARK, 1)[-1]
    tr['says_premise_first'] = 'DISCHARGED BEFORE ANYTHING WAS SWEPT' in seg
    tr['says_three_forms'] = 'no regex at all' in seg
    tr['says_wide_control'] = 'discriminates' in seg
    tr['says_grep_not_instrument'] = 'not a backtick in a matcher' in seg
    tr['says_funnel'] = 'THE FUNNEL, EVERY STAGE PRINTED' in seg
    tr['says_discards'] = '374 of 407' in seg
    tr['says_pervasive'] = 'the narrow shape is pervasive' in seg
    # ### **AND THIS CHECK WAS ITSELF CASE-NARROW ON ITS FIRST RUN** -- it looked for a
    # ### lowercase phrase the block states in title case, and reported the block silent
    # ### about a claim the block makes. ### **THE ACT'S OWN SUBJECT, IN ITS OWN WRITER.**
    tr['says_figure_is_unit'] = 'unit is the figure' in seg.lower()
    tr['says_harness_owned'] = 'artefacts of the' in seg
    tr['says_floor'] = 'floor because its input is a floor' in seg
    tr['says_optin'] = 'opt-in, default-off' in seg
    tr['says_judgement_apart'] = 'not claimed as mechanized' in seg
    tr['says_lists_open'] = 'four lists stay OPEN by name' in seg
    rec('  ### ### **EVERY CLAIM THE WRITER RECORDS ABOUT ITS OWN BLOCK:** ### %s'
        % {k: v for k, v in tr.items() if k.startswith('says_')})

    rec()
    bar()
    rec('  ### THE CORRESPONDENCE ROW.')
    bar()
    ROWS = corr_rows(Q)
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302): %s %s ; SPLITTER (b303): %s %s %s %s'
        % (pos, neg, sa, sb, sc, sd))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    rec('  cells carrying an UNESCAPED pipe : %d' % len(bad))
    if bad or not (pos and neg and sa and sb and sc and sd):
        run_clock.write(D, 'b396_desk_notes', LINES)
        return 1
    slip = [mm for mm, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(mm)]
    rec('  marker is a literal prefix of its statement : %s' % (not slip))
    if slip:
        run_clock.write(D, 'b396_desk_notes', LINES)
        return 1
    nums = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    present = [mm for mm, _s, _t, _p, _g, _sc, _st in ROWS if mm in txt]
    if present:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = max(nums)
    else:
        start = max(nums) + 1
        rec('  last existing row : %d ; row to append : %d' % (max(nums), start))
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start + k, stmt, term, prof, grade, scope,
                    (status % (start + k)) if '%d' in status else status)
                 for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
        new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
        open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
        os.replace(TABLE + '.tmp', TABLE)
        back = io.open(TABLE, encoding='utf-8').read()
        got = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', back, re.M)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(chr(10))))
        rec('  READ BACK : last row %d ; cells %s ; true prefix %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(chr(10))),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            run_clock.write(D, 'b396_desk_notes', LINES)
            return 1
        rownum = start

    rec()
    bar()
    rec('  ### THE INDEX KEY.')
    bar()
    kok = do_key(rownum)

    rec()
    bar()
    rec('  ### THE BANK.')
    bar()
    B = []
    BAR, SUB = '=' * 100, '-' * 100
    B.append(BAR)
    B.append('b396 -- HOW MANY FINDINGS REST ON A BACKTICK. ### THE BANK.')
    B.append(BAR)
    B.append('')
    B.append('### ### ### **THE QUESTION HAS NO ANSWER AT INSTRUMENT GRANULARITY, AND THE THREE')
    B.append('### ### ### VACUOUS FILTERS THAT PROVE IT ARE THE RESULT.**')
    B.append('')
    B.append(SUB)
    B.append('### THE ORDER`S FIRST INSTRUCTION, DISCHARGED BEFORE ANYTHING WAS SWEPT.')
    B.append(SUB)
    B.append('### **ONE NARROW MATCHER, WRITTEN THREE WAYS:**')
    B.append('###   form 1  a raw-string regex, backtick-delimited        FOUND : %s'
             % S0['forms'][0])
    B.append('###   form 2  a double-quoted escaped regex                 FOUND : %s'
             % S0['forms'][1])
    B.append('###   form 3  ### **NO REGEX AT ALL** -- `startswith` + `in` + `islower()`')
    B.append('###                                                        FOUND : %s'
             % S0['forms'][2])
    B.append('### ### **ALL THREE FOUND : %s.**' % S0['all_three'])
    B.append('### ### **AND THE WIDE FIXTURE IS CLEAN : %s** ### -- without a negative control'
             % S0['wide_clean'])
    B.append('### ### the fixture shows the detector ### **FIRES** ### and not that it ###')
    B.append('### ### **DISCRIMINATES.**')
    B.append('### ### **A SWEEP FOR NARROW MATCHERS THAT WAS ITSELF NARROW WOULD BE THE SPECIES')
    B.append('### ### INSIDE THE ACT THAT MEASURES IT, FOR THE THIRD TIME IN FOUR ACTS.**')
    B.append('')
    B.append('### **WHAT THIS SWEEP IS DEAF TO, STATED IN THE INSTRUMENT AND NOT ONLY HERE:**')
    B.append('###   -- a narrowness assembled from a VARIABLE at run time')
    B.append('###   -- a narrowness living in the DATA an instrument reads')
    B.append('###   -- a matcher passed in from ANOTHER module')
    B.append('###   -- a shape restriction with no string and no case method')
    B.append('###   -- ### **WHETHER A NARROW MATCHER IS WRONG** -- the shape is measured, never')
    B.append('###      the verdict')
    B.append('')
    B.append(SUB)
    B.append('### THE FUNNEL. ### **EVERY STAGE PRINTED.**')
    B.append(SUB)
    B.append('###   `tools/b*.py` parsed                          ### **`%d`** (unparseable `0`)'
             % C1['parsed'])
    B.append('###   carrying a backtick ANYWHERE (a raw `grep`)   ### **`%d`** of `%d`'
             % (S0['raw_backtick'], S0['tools']))
    B.append('###   carrying at least one NARROW TEST             ### **`%d`**' % C1['narrow'])
    B.append('###   ### **CARRYING AT LEAST ONE AT-RISK FIGURE**  ### **`%d`**' % C1['files'])
    B.append('###   ### **AT-RISK FIGURES**                       ### **`%d`** across `%d` acts'
             % (C1['figures'], C1['acts']))
    B.append('### ### **`%d` OF `%d` IS WHY A RAW `grep` IS NOT THE INSTRUMENT.** ### Almost'
             % (S0['raw_backtick'], S0['tools']))
    B.append('### ### every one of those backticks is PROSE. ### **A BACKTICK IN A SENTENCE IS')
    B.append('### ### NOT A BACKTICK IN A MATCHER**, so the sweep reads by `ast` and keeps a')
    B.append('### ### literal only where it is ### **USED AS A TEST.**')
    B.append('')
    B.append(SUB)
    B.append('### THREE FILTERS TRIED AND DISCARDED BEFORE THE LOCK, WITH THEIR YIELDS.')
    B.append(SUB)
    B.append('###   (i)   `the module prints an absence somewhere`   kept ### **`374` of `407`**')
    B.append('###   (ii)  `the act`s name appears in a ledger`       kept ### **`350` of `380`**')
    B.append('###   (iii) `the instrument reads corpus text`         kept ### **`79` of `82`**')
    B.append('### ### **A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER**, and ###')
    B.append('### ### **A TIGHTENING MADE IN SILENCE IS ONE NOBODY CAN AUDIT** (`b381`).')
    B.append('### ### **(ii) MEASURED NOTHING BECAUSE EVERY ACT NAMES ITSELF IN ITS OWN ROW.**')
    B.append('### ### **(iii) IS A TRUE DISTINCTION THIS TOOL CANNOT DRAW:** ### a narrow matcher')
    B.append('### ### against text the act WROTE fails its own gate loudly; one against the')
    B.append('### ### CORPUS shrinks a finding in silence, which is `b394``s species. ### **THAT')
    B.append('### ### IS WHERE THE RISK LIVES AND THIS ACT CANNOT SEPARATE IT** -- filed as a')
    B.append('### ### limit, not applied as a filter.')
    B.append('### ### ### **AND THREE VACUOUS FILTERS IN ONE ACT IS ITSELF THE RESULT:** ### the')
    B.append('### ### ### narrow shape is ### **PERVASIVE**, so ### *how many findings rest on a')
    B.append('### ### ### backtick* ### **HAS NO ANSWER AT INSTRUMENT GRANULARITY.** ### It has')
    B.append('### ### ### one at FIGURE granularity, and that is the list.')
    B.append('')
    B.append(SUB)
    B.append('### WHAT MAKES A FIGURE AT RISK, AND THAT FILTER IS TESTED TOO.')
    B.append(SUB)
    B.append('### A narrow literal whose yield is bound to a name, and a report naming that same')
    B.append('### name whose ### **OWN LITERAL** ### carries an absence.')
    B.append('### ### **THE ABSENCE AND THE MEASUREMENT MUST SIT IN THE SAME LITERAL**, or it is')
    B.append('### ### prose that happens to contain the word `no`.')
    B.append('### ### **TESTED ON BOTH AXES : narrow+absence FIRES `%s` ; narrow+ordinary QUIET'
             % S1['filter_fixture'][0])
    B.append('### ### `%s` ; wide+absence QUIET `%s`.**'
             % (S1['filter_fixture'][1], S1['filter_fixture'][2]))
    B.append('### ### **AND NARROW IS NOT A DEFECT:** ### `%d` instruments carry a narrow test'
             % C1['not_at_risk'])
    B.append('### ### with no negative finding standing on it, and ### **THEY ARE NOT COUNTED AS')
    B.append('### ### AT RISK.**')
    B.append('')
    B.append(SUB)
    B.append('### THE SIX RE-RUNS. ### **THE UNIT IS THE FIGURE, NOT THE MATCH COUNT.**')
    B.append(SUB)
    B.append('### **THE TWO CRITERIA PICK DIFFERENT SETS AND THE ACT SAYS SO:**')
    B.append('###   the CHEAPEST three     : %s' % ', '.join('`%s`' % x for x in C2['cheapest']))
    B.append('###   the MOST EXPOSED three : %s' % ', '.join('`%s`' % x for x in C2['exposed']))
    B.append('### ### **THEY SHARE `%d` MEMBERS. ### ALL SIX WERE RUN**, because every one is a'
             % C2['shared'])
    B.append('### ### local read and ### **A CHOICE NOT WORTH MAKING IS NOT MADE.**')
    B.append('')
    B.append('### ### **AN EARLIER FORM OF THIS COMPONENT CALLED TWO OF THE SIX `MOVED`, AND')
    B.append('### ### BOTH WERE ARTEFACTS OF THE HARNESS:** ### it read the act`s `data/` records')
    B.append('### ### instead of ### **THE TEXT THE MATCHER ACTUALLY READ**, and it compared')
    B.append('### ### match counts where the figure is a ### **BOOLEAN.** ### **A FIGURE THAT')
    B.append('### ### DOES NOT MOVE HAS NOT MOVED, WHATEVER THE COUNT DID.** ### Repaired before')
    B.append('### ### this bank, and reported rather than quietly corrected.')
    B.append('')
    for o in C2['rows']:
        B.append('###   **%s** `%s` [%s] %s' % (o['act'], o['inst'], o['set'], o['kind']))
        B.append('###       input  : `%s`' % o['input'])
        B.append('###       narrow : %s' % (' | '.join(o['narrow'])[:88]))
        B.append('###       wide   : %s' % o['wide'][:88])
        B.append('###       matches narrow `%d` wide `%d` ; ### **FIGURE narrow `%s` wide `%s`'
                 % (o['narrow_hits'], o['wide_hits'], o['narrow_figure'], o['wide_figure']))
        B.append('###       --> %s**' % o['verdict'])
        if o['narrowness_without_consequence']:
            B.append('###       ### **NARROWNESS WITHOUT CONSEQUENCE** -- the count moved, the')
            B.append('###       ### figure did not.')
    B.append('')
    B.append('### ### **THE SIX VERDICTS : %s. ### FIGURES MOVED : `%d`. ### NARROW WITHOUT'
             % (C2['verdicts'], C2['moved']))
    B.append('### ### CONSEQUENCE : `%d`.**' % C2['nwc'])
    B.append('### ### **`(L2)` ASKED WHETHER ONE RE-RUN MOVES A BANKED FIGURE. ### ON THESE SIX')
    B.append('### ### THE ANSWER IS %s**, and this seat registered `(E2)` before the lock: ###'
             % ('MET' if C2['moved'] else 'REFUTED'))
    B.append('### ### *the re-runs will mostly confirm, and confirming is the weaker result.*')
    B.append('### ### **A REFUTED `(L2)` IS A REAL ANSWER AND NOT A DISAPPOINTMENT** -- the')
    B.append('### ### arc`s one known move was found by ### **READING A DOCUMENT, NOT BY WIDENING')
    B.append('### ### A REGEX.**')
    B.append('### ### **AND A CONFIRMATION IS THE WEAKER RESULT.** ### It proves a figure is not')
    B.append('### ### an artefact of ### **THE SHAPE THAT WAS WIDENED**, and nothing more. ###')
    B.append('### ### **`%d` OF THE `%d` FIGURES ARE UNTESTED**, and the five deafnesses stand in'
             % (C1['figures'] - C2['runs'], C1['figures']))
    B.append('### ### front of every `CONFIRMED` above.')
    B.append('### ### **`(L3)` IS MET BY `b395` AND NOT BY THIS ACT:** ### `b394` reported ###')
    B.append('### ### *no kernel repository it names is on the drive* ### for `8` keystones and')
    B.append('### ### the drive holds one for every one of them. ### **THE ACT NAMES IT RATHER')
    B.append('### ### THAN RE-DISCOVERING IT.**')
    B.append('')
    B.append(SUB)
    B.append('### THE TEN NOW REACHABLE. ### **PRICED. ### NOT READ.**')
    B.append(SUB)
    B.append('### **THE RATE, READ FROM `b394``S OWN COMPONENT JSON:** ### **`%s` PER KEYSTONE**'
             % C3['per_keystone'])
    B.append('### against `b390``s `24` for one.')
    B.append('### ### **THE PRICE : `%s` x `%d` = `%s` MINUTES.**'
             % (C3['per_keystone'], C3['ten'], C3['minutes']))
    B.append('### **WHAT IT BUYS:** ### `%d` of the census`s `%d` are reconciled today; reading'
             % (C3['reconciled'], C3['of']))
    B.append('### the ten takes that to ### **`%d` OF `%d`**, leaving ### **`%d`** ### --'
             % (C3['after'], C3['of'], C3['remaining']))
    B.append('### `ENUMERA`, which names no terminal and needs an author rather than a reader.')
    B.append('### ### **THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR.** ### `b394` declared')
    B.append('### ### both of its figures floors, and ### **A RATE TAKEN FROM THE EASY END PRICES')
    B.append('### ### THE HARD END TOO CHEAPLY** -- `b394` read ### *the reachable ones.*')
    B.append('### ### **THE TEN ARE NOT READ. ### THE ITEM STAYS AVAILABLE AND NOT DONE.**')
    B.append('')
    B.append(SUB)
    B.append('### THE PRESERVATION HAZARD. ### **FILED, AND MECHANIZED IN PART.**')
    B.append(SUB)
    B.append('### **THE INCIDENT:** ### `b395``s needle for the live cluster row matched `b388``s')
    B.append('### ### **PRESERVED QUOTATION** ### of the superseded table and ### **RESOLVED TO')
    B.append('### ### IT SILENTLY**, having met it first.')
    B.append('### **THE RULE:** ### an anchor used to EDIT ### **EXCLUDES PRESERVED BLOCKS BY')
    B.append('### ### CONSTRUCTION**, and an anchor resolving inside one is ### **REFUSED RATHER')
    B.append('### ### THAN DISAMBIGUATED** -- a caller told `AMBIGUOUS` picks one, and picking is')
    B.append('### how the quotation gets edited.')
    B.append('### **THE SURVEY THAT MAKES IT MECHANIZABLE:** ### `%d` contiguous blockquoted'
             % A3['blocks'])
    B.append('### blocks across `%d` documents, plus `%d` explicit preservation banners.'
             % (A3['files'], A3['banners']))
    B.append('### **THE MECHANIZED HALF:** ### `tools/anchor_from_file.py` gains an ### **OPT-IN,')
    B.append('### ### DEFAULT-OFF** ### `editing=True`. ### **ITS OWN FIXTURES: `%d` ARMS, `%d`'
             % (A3['arms'], A3['failing']))
    B.append('### ### FAILING.** ### **CALLERS `%d` ; CALLERS MOVED `%d`.**'
             % (A3['callers'], A3['moved']))
    B.append('### ### **THE DEFAULT IS OFF ON PURPOSE:** ### an anchor used to QUOTE a preserved')
    B.append('### ### block is CORRECT. ### **THE HAZARD IS EDITING BY AN ANCHOR, NOT READING BY')
    B.append('### ### ONE.**')
    B.append('### **THE JUDGEMENT HALF, LISTED APART AND NOT CLAIMED AS MECHANIZED:** ### whether')
    B.append('### a passage carrying no `>` is preserved. ### `>` is ### **SUFFICIENT AND NOT')
    B.append('### ### NECESSARY**, so the arm is ### **A FLOOR ON THE HAZARD AND NOT A GUARD')
    B.append('### ### AGAINST IT** -- this act`s own subject turned on its own remedy.')
    B.append('### **THE MODULE:** ### `%s`, `%d` bytes, stating its two halves apart : %s.'
             % (A3['module'], A3['bytes'], A3['halves']))
    B.append('### ### **LOCAL ONLY, UNTRACKED AND NOT PUSHED.**')
    B.append('')
    B.append(SUB)
    B.append('### THE DESK.')
    B.append(SUB)
    B.append('### ### **ITEMS SWEPT `%d` ; CLOSED `%d` ; STANDING `%d`.**'
             % (Q['items'], Q['closed'], Q['standing']))
    B.append('### ### **ONE ITEM IS CLOSED BY BEING MEASURED** -- `b395` left ### *how many other')
    B.append('### ### findings rest on a backtick is UNMEASURED* ### and it is now measured.')
    B.append('### ### **AND THE MEASUREMENT OPENS FOUR**, three of which are ### **LIMITS OF THIS')
    B.append('### ### ACT`S OWN INSTRUMENT**, filed so a later act does not inherit them unstated.')
    B.append('### ### **THE FOUR OPEN LISTS ARE RESTATED OPEN BY NAME AND THIS ACT CLOSES NONE.**')
    B.append('')
    B.append(SUB)
    B.append('### WHAT THIS BANK WAS MADE FROM. ### **NAMED, SO A READER CAN RE-RUN IT.**')
    B.append(SUB)
    B.append('### ### **THE FACE, LOCKED BEFORE ANY WRITE:**')
    B.append('###   `data/b396_registration_2026-09-10.txt`')
    B.append('###   sha256 `%s`' % SEALHASH)
    B.append('###   locked at `%s` (UTC)' % SEALSTAMP)
    B.append('### ### **THE LOCK GATE:** ### `tools/b378_lockgate.py` run as `b396` -- ###')
    B.append('### **`%d` GATES READ, `%d` PASSING, `%d` CHECKED BY DIGEST.**'
             % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
    B.append('### ### **THE RUN RECORDS, EACH RESOLVED BY ITS OWN RECORDED CLOCK** (`b358`):')
    B.append('###   the extract and its six surveys    `data/%s`  `%s`'
             % (E['run_file'], E['run_clock']))
    B.append('###   the components and the module      `data/%s`  `%s`'
             % (AC['run_file'], AC['run_clock']))
    B.append('### ### **AND THE LEDGER WRITES:** ### `CORRESPONDENCE.md` row `%d`; the'
             % rownum)
    B.append('### ### `OPEN_TRAILS.md` block marked `%s`; the index key' % MARK)
    B.append('### ### `the-backtick-swept`.')
    B.append('')
    B.append(SCOPE)
    B.append('')
    B.append(BAR)
    io.open(BANKOUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(B) + chr(10))
    bbad = [i + 1 for i, x in enumerate(B) if '%s' in x or '%d' in x]
    rec('  written: %s  (%d lines, %d bytes)'
        % (os.path.basename(BANKOUT), len(B), len(chr(10).join(B).encode('utf-8'))))
    rec('  ### UNFILLED PLACEHOLDERS IN THE BANK : %s' % (bbad or 'none'))
    MUSTFAIL = ('### THE SWEEP WAS NOT TESTED.', '### A FILTER WAS DISCARDED IN SILENCE.',
                '### A COUNT WAS REPORTED AS A LIST.', '### A RE-RUN WAS TUNED.',
                '### A CALLER WAS MOVED.', '### AN INSTRUMENT WAS REPAIRED.',
                '### A CORPUS DOCUMENT WAS EDITED.', '### THE PLATFORM WAS CALLED.')
    bhit = [x for x in MUSTFAIL if x in B]
    rec('  ### MUST-FAIL WHOLE LINES PRESENT : %s' % (bhit or 'none'))
    rec()
    bar('=')
    rec('  ### desk %d ; closed %d ; trail %s ; row %s ; key %s'
        % (Q['items'], Q['closed'], tr['appended_only'], rownum, kok))
    bar('=')
    p = run_clock.write(D, 'b396_desk_notes', LINES)
    Q.update(trail=tr, mark=MARK, row=rownum, key_ok=kok,
             bank='b396_the_backtick_swept.txt', bank_lines=len(B),
             bank_placeholders=len(bbad), bank_mustfail=len(bhit),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b396_desk.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(Q, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (kok and not bbad and not bhit) else 1


if __name__ == '__main__':
    sys.exit(main())
