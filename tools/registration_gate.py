# -*- coding: utf-8 -*-
"""registration_gate.py -- THE INDEX-QUERY GATE, IN THE PATH (built b185).

### WHY THIS EXISTS. b160 built the banked-result index and a convention with it:
### ### "BEFORE AN OBJECT IS MARKED OPEN, NAVIGATOR-ASSERTED, OR REQUIRING A
### ### CONSTRUCTION, THE INDEX IS QUERIED AND THE QUERY'S RESULT REPORTED."
### It built that index because ### "TWO ACTS DID NOT READ A RESULT THE RECORD
### ALREADY HELD."
### At b182 this seat marked THREE ROUTES "NAVIGATOR-ASSERTED. UNREAD" and
### "REQUIRING A CONSTRUCTION", and ### QUERIED NOTHING. The answer was one query
### away: `boundary-license` -> b151 -> "no license derives". ### A WHOLE PROGRAM
### WAS DRAFTED FOR WORK THAT WAS ALREADY FINISHED.
###
### ### THE INDEX DID NOT FAIL. IT WAS NOT ASKED.
### That is why this is a GATE and not a reminder:
### ### **AN INSTRUMENT THAT MUST BE REMEMBERED IS NOT AN INSTRUMENT.**

### WHAT IT DOES. Given a registration file, it looks for the marks the b160
### convention names. If any is present, the registration MUST also carry a
### recorded index-query result. No result -> HARD FAILURE, and the registration
### is not bankable.

# ### THE LIMITS, IN THE HEADER SO THE GATE IS NOT TRUSTED BEYOND THEM:
# ### (1) IT MATCHES TEXT. It cannot tell a real query from the WORDS of one, and
# ###     an act that types "NO KEY" without running anything passes. ### IT RAISES
# ###     THE COST OF SKIPPING THE QUERY; IT DOES NOT MAKE SKIPPING IMPOSSIBLE.
# ### (2) It knows the marks it is given. A mark phrased in words it does not know
# ###     is invisible -- the same false-miss class b164 named for the index's own
# ###     keys: ### KEYS CLOSE FALSE HITS, NOT FALSE MISSES.
# ### (3) ### IT CHECKS THAT A QUERY WAS RECORDED, NOT THAT IT WAS THE RIGHT QUERY.
# ###     b182 would have been caught by this gate only if it had queried at all;
# ###     an act that queries the wrong keys still passes. ### NO INSTRUMENT HERE
# ###     CHECKS THAT AN OBJECT WAS QUERIED UNDER THE NAME IT ACTUALLY HAS.

#
# ### AND A BUILD NOTE KEPT BECAUSE IT IS THE SECOND TIME: this file's first run
# ### died on an UNCLOSED MODULE DOCSTRING, exactly as b179's pre-commit hook did.
# ### THE SAME SLIP, IN THE SAME SHAPE, SIX ACTS APART. Both were caught at once by
# ### the interpreter, so neither shipped -- ### BUT A DEFECT THAT REPEATS IS NOT AN
# ### ACCIDENT, IT IS A HABIT, and naming it is cheaper than pretending the first
# ### one taught me something.
"""

import io
import os
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE MARKS, TAKEN FROM b160's CONVENTION WORD FOR WORD.
MARKS = [
    (re.compile(r'\bNAVIGATOR-ASSERTED\b', re.I), 'NAVIGATOR-ASSERTED'),
    (re.compile(r'\bREQUIRING A CONSTRUCTION\b|\bNEEDS A CONSTRUCTION\b', re.I),
     'REQUIRING A CONSTRUCTION'),
    (re.compile(r'\bMARKED OPEN\b|\bIS OPEN\b|\bSTILL OPEN\b|\bLEFT OPEN\b', re.I), 'OPEN'),
    (re.compile(r'\bUNREAD\b', re.I), 'UNREAD'),
]

# ### EVIDENCE THAT THE QUERY RAN AND ITS RESULT WAS RECORDED.
QUERY = re.compile(
    r'NO KEY|banked_index|banked-result index|HIT\s*->|index quer(?:y|ies|ied)', re.I)


# ### ==============================================================================================
# ### ### **THE BAR-FLOOR ARMS, ADDED b347 BY THE AUTHOR'S ORDER.** ### They sit BESIDE the index-query
# ### arm above and replace nothing in it.
# ###
# ### ### **THE RULE THEY MECHANIZE, MINTED AT b347 FROM TWO BANKED INCIDENTS:**
# ### ### **A NUMERICAL BAR IS STATED WITH THE FLOOR OF THE OBJECT IT TESTS; A BAR BELOW THAT FLOOR IS
# ### ### UNINFORMATIVE RATHER THAN STRICT. ### AND A BAR WITH SEVERAL ARMS IS STATED WITH WHAT MAKES THE
# ### ### ARMS INDEPENDENT; ARMS THAT ARE ALGEBRAICALLY ONE ARM ARE ONE ARM.**
# ###   ### b345 sealed a fixture demanding `1e-25` of a routine whose sealed truncation left it a floor
# ###     near `4.4e-18`. ### At its own threshold it rejected the CORRECT copy as well as the broken one
# ###     and separated nothing.
# ###   ### b346 sealed an uncertainty bar with three arms of which two could not contribute: a two-point
# ###     drift-zero is algebraically the local slope of those two points, so the second estimator
# ###     collapsed onto the first and the arm keyed to the window's bottom was structurally zero.
# ###
# ### ### **THE LIMITS, IN THE HEADER SO THESE ARMS ARE NOT TRUSTED BEYOND THEM, IN THE VOICE THIS FILE
# ### ### ALREADY USES:**
# ### ### **(1) THEY MATCH TEXT.** ### They cannot tell a floor from the WORDS of one. ### A registration
# ###     that writes `UNPRICED` beside every threshold PASSES and has priced nothing. ### **THEY RAISE
# ###     THE COST OF AN UNPRICED BAR FROM ZERO TO A DELIBERATE WORD.**
# ### ### **(2) THEY SEE THE SHAPES THEY ARE GIVEN.** ### A threshold phrased in words they do not know is
# ###     invisible -- the same false-miss class b164 named for the index's keys. ### **KEYS CLOSE FALSE
# ###     HITS, NOT FALSE MISSES.**
# ### ### **(3) THE WINDOW IS THE PARAGRAPH.** ### A floor stated three paragraphs away from its bar does
# ###     not satisfy the arm, and that is deliberate: a reader who must hunt for the floor is a reader who
# ###     will not find it.
# ### ### **(4) THEY BIND REGISTRATIONS WRITTEN AFTER THEM.** ### b347 ran them over every registration in
# ###     the record as a CENSUS and re-verdicted nothing.
# ### ==============================================================================================

# ### a numeric literal in the notation the corpus's bars are written in.
_NUM = r'\d+(?:\.\d+)?[eE][-+]?\d+'
THRESHOLD = re.compile(
    r'(?:\bbar\b|\bthreshold\b|\btolerance\b|\bagree(?:s|d)?\s+to\b|\bwithin\b|<=|≤)'
    r'[^\n]{0,80}?`?' + _NUM, re.I)
FLOOR_WORD = re.compile(r'\bfloor\b|\bUNPRICED\b', re.I)
MULTIARM = re.compile(
    r'\bthe largest of\b|\bthe weaker of\b|\((?:u|a|b)\d\)|\bby two routes\b|\btwo estimators\b'
    r'|\btwo routes\b|\bboth routes\b|\bthree arms\b|\btwo arms\b', re.I)
ARMWORD = re.compile(r'\bindependen\w*\b|\bshar(?:e|es|ing)\s+no\b|\bdisjoint\b|\bSINGLE-ARM\b', re.I)


def _paragraphs(txt):
    """### THE WINDOW. ### A paragraph is a run of lines with no blank line in it; the registrations are
    ### written that way and every section is separated by a rule line."""
    out, cur, start = [], [], 1
    for i, ln in enumerate(txt.split('\n'), 1):
        if ln.strip() == '' or set(ln.strip()) in ({'-'}, {'='}):
            if cur:
                out.append((start, '\n'.join(cur)))
                cur = []
            start = i + 1
        else:
            if not cur:
                start = i
            cur.append(ln)
    if cur:
        out.append((start, '\n'.join(cur)))
    return out


def bar_floor_check(txt):
    """### RETURN `(floor_misses, arm_misses, n_threshold_paras, n_multiarm_paras)`. ### A MISS is a paragraph
    ### that states a threshold (or declares several arms) and carries neither the word the rule requires nor
    ### the token that says it is deliberately unpriced."""
    fmiss, amiss, nth, nma = [], [], 0, 0
    for start, para in _paragraphs(txt):
        if THRESHOLD.search(para):
            nth += 1
            if not FLOOR_WORD.search(para):
                fmiss.append((start, para.strip().split('\n')[0][:88]))
        if MULTIARM.search(para):
            nma += 1
            if not ARMWORD.search(para):
                amiss.append((start, para.strip().split('\n')[0][:88]))
    return fmiss, amiss, nth, nma


def bar_floor_self_test(verbose=True):
    """### FIXTURES, BOTH POLARITIES, ON SYNTHETIC TEXT WRITTEN HERE AND DRAWN FROM NO BANK.
    ### ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM, AND ONE THAT CANNOT PASS IS NOT ONE EITHER.**"""
    def say(s):
        if verbose:
            print(s)

    bad_floor = '### THE BAR: the routine must agree to `1e-25` at every point.'
    good_floor = ('### THE BAR: the routine must agree to `1e-25` at every point, against a floor of\n'
                  '### `4.4e-18` imposed by its own truncation.')
    good_unpriced = '### THE BAR: the routine must agree to `1e-25` at every point. ### UNPRICED.'
    bad_arms = '### THE UNCERTAINTY is the largest of (u1), (u2) and (u3), each printed beside the verdict.'
    good_arms = ('### THE UNCERTAINTY is the largest of (u1), (u2) and (u3); the estimators share no code and\n'
                 '### are independent at the top of the window.')
    good_single = '### THE UNCERTAINTY is the largest of (u1) and (u2). ### SINGLE-ARM.'
    r = []
    f1, _a1, _n, _m = bar_floor_check(bad_floor)
    r.append(('the floor arm FIRES on a bare threshold', bool(f1)))
    f2, _a, _n, _m = bar_floor_check(good_floor)
    r.append(('and is QUIET when the floor is beside it', not f2))
    f3, _a, _n, _m = bar_floor_check(good_unpriced)
    r.append(('and is QUIET on a deliberate UNPRICED', not f3))
    _f, a2, _n, _m = bar_floor_check(bad_arms)
    r.append(('the arms arm FIRES on an unqualified multi-arm bar', bool(a2)))
    _f, a3, _n, _m = bar_floor_check(good_arms)
    r.append(('and is QUIET when independence is named', not a3))
    _f, a4, _n, _m = bar_floor_check(good_single)
    r.append(('and is QUIET on a deliberate SINGLE-ARM', not a4))
    for what, ok in r:
        say('    %-52s %s  %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


# ======================================================================================================
# ### ### **THE STRADDLING-GATE RULE (minted b352). ### APPENDED, NOTHING ABOVE IS EDITED.**
# ### ### **A GATE THAT STRADDLES AN EVENT HAS TWO READINGS, AND THE ACT NAMES THE ONE IT RELIES ON.**
# ###
# ### THREE INCIDENTS, EACH QUOTED AT ITS OWN EMITTING FILE:
# ###   (i)   `tools/mirror_verify.py` -- *"A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A
# ###         CORRECT ONE."* ### The mirror must be rebuilt AFTER the commit; run before, it passes on a stale
# ###         archive and the pass looks identical.
# ###   (ii)  `data/b350_checks_run_prepush.txt` -- *"the hook and the mirror records are NOT YET WRITTEN (they
# ###         are written at the push)."* ### The arm CANNOT pass before the push, and its whole content is the
# ###         after-reading.
# ###   (iii) the ancestry arm's *true prefix of its blob*: a strong check BEFORE a commit and a near-vacuous
# ###         one after it, because the blob then IS the file (`data/b351_checks_run_prepush.txt`, and named in
# ###         b351's own closing).
# ###
# ### ### **THE MECHANIZABLE HALF, WHICH IS WHAT THIS CODE IS:** a registration that names a gate arm reading
# ### a REPOSITORY state must say whether that arm is read BEFORE or AFTER the push, or mark it
# ### `SIDE-INVARIANT`.
# ### ### **THE JUDGEMENT HALF, WHICH THIS CODE CANNOT CARRY AND WHICH IS FILED AS JUDGEMENT:** ### WHICH ARMS
# ### STRADDLE CANNOT BE DECIDED BY A STRING. ### An arm straddles when its VERDICT would change across the
# ### event, and no scanner computes that from the arm's text. ### **THIS FORCES A DECLARATION; IT DOES NOT
# ### AND CANNOT CHECK THAT THE DECLARATION IS RIGHT.**
# ======================================================================================================

REPO_STATE = re.compile(
    r'\bblob\b|\bls-remote\b|\bworking tree\b|\bcommitted\b|\bthe push\b|\bpushed\b|\bHEAD\b'
    r'|\bthe mirror\b|\bthe hook\b|\btrue prefix\b|\bancestry\b|\bgit\b', re.I)
SIDE_WORD = re.compile(
    r'\bBEFORE THE PUSH\b|\bAFTER THE PUSH\b|\bbefore the commit\b|\bafter the commit\b'
    r'|\bpre-push\b|\bpost-push\b|\bSIDE-INVARIANT\b|\bOWED\b', re.I)
ARMNAME = re.compile(r'`G-[A-Z0-9-]+`|\bG-[A-Z0-9-]{3,}\b')


def _flatpara(para):
    """### ### **THE WRAP CURE, AND IT WAS FOUND BY THIS ARM'S OWN FIXTURE FAILING.** ### A registration wraps,
    ### and `AFTER THE PUSH` can land with a line break and a marker inside it. ### An arm that searched the raw
    ### paragraph would raise a FALSE ALARM on a registration that HAD declared its side -- which is the
    ### needle-wrapping species the record has banked six times. ### Markers and newlines are collapsed here so
    ### the search sees the sentence rather than the layout."""
    return re.sub(r'\s+', ' ', re.sub(r'#{2,}', ' ', para)).strip()


def straddle_check(txt):
    """### RETURN `(misses, n_repo_paras)`. ### A MISS is a paragraph that names a gate arm AND touches a
    ### repository state, and says on neither side of the event it is read."""
    miss, nrepo = [], 0
    for start, para in _paragraphs(txt):
        flat = _flatpara(para)
        if ARMNAME.search(flat) and REPO_STATE.search(flat):
            nrepo += 1
            if not SIDE_WORD.search(flat):
                miss.append((start, para.strip().split(chr(10))[0][:88]))
    return miss, nrepo


def straddle_self_test(verbose=True):
    """### FIXTURES, BOTH POLARITIES, ON SYNTHETIC TEXT WRITTEN HERE AND DRAWN FROM NO BANK."""
    def say(s):
        if verbose:
            print(s)

    bad = '### `G-ROW` -- the row present once, and the table a true prefix of its blob.'
    good_after = ('### `G-ROW` -- the row present once, and the table a true prefix of its blob, read AFTER THE\n'
                  '### PUSH, which is the reading this act relies on.')
    good_before = '### `G-TRAIL` -- a true prefix of its committed blob, pre-push. ### That is the arm that carries.'
    good_inv = '### `G-STATE` -- every state one of the sealed three, read off the blob. ### SIDE-INVARIANT.'
    quiet = '### `G-NUMBERS` -- every figure in the bank recomputes from the act own record.'
    also_quiet = '### the working tree is clean and the mirror was rebuilt, with no arm named in this sentence.'
    r = []
    m1, _n = straddle_check(bad)
    r.append(('the straddle arm FIRES on an arm reading a blob with no side named', bool(m1)))
    m2, _n = straddle_check(good_after)
    r.append(('and is QUIET when the arm says AFTER THE PUSH', not m2))
    m3, _n = straddle_check(good_before)
    r.append(('and is QUIET when the arm says pre-push', not m3))
    m4, _n = straddle_check(good_inv)
    r.append(('and is QUIET on a deliberate SIDE-INVARIANT', not m4))
    m5, n5 = straddle_check(quiet)
    r.append(('and does NOT fire on an arm that touches no repository state', not m5 and n5 == 0))
    m6, n6 = straddle_check(also_quiet)
    r.append(('and does NOT fire on repository prose that names no arm', not m6 and n6 == 0))
    for what, ok in r:
        say('    %-62s %s  %s' % (what, ok, 'PASS' if ok else '### FAIL ###'))
    return all(ok for _w, ok in r)


def check(path):
    if not os.path.exists(path):
        return 2, ["### HARD FAILURE -- registration not found: %s" % path]
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    if not txt.strip():
        # ### THE ZERO CASE. b167 added an empty-scope hard failure to
        # ### banned_terms.py; b179's hook cleared an EMPTY staged set; b183's
        # ### clause 3 refuses an empty roster. ### IN THIS RECORD EMPTINESS READS
        # ### AS SUCCESS UNLESS A LINE IS WRITTEN AGAINST IT.
        return 2, ["### HARD FAILURE -- THE REGISTRATION IS EMPTY.",
                   "### An empty file trivially carries no unbacked mark.",
                   "### THAT IS NOT A PASS. A verdict over an empty scope is not a verdict."]

    found = []
    for rx, name in MARKS:
        for m in rx.finditer(txt):
            line = txt.count('\n', 0, m.start()) + 1
            found.append((name, line, txt.split('\n')[line - 1].strip()[:90]))

    out = ["  registration : %s" % os.path.basename(path),
           "  marks found  : %d" % len(found)]
    for n, ln, s in found[:8]:
        out.append("      %-26s line %-5d %s" % (n, ln, s))
    if len(found) > 8:
        out.append("      ... and %d more" % (len(found) - 8))

    if not found:
        out.append("  VERDICT      : PASS -- no mark requires a query")
        out.append("  ### and that means ONE thing only: none of the known marks")
        out.append("  ### appears. ### IT IS NOT A REVIEW OF THE REGISTRATION.")
        return 0, out

    q = QUERY.search(txt)
    if q:
        line = txt.count('\n', 0, q.start()) + 1
        out.append("  query result : RECORDED at line %d" % line)
        out.append("  VERDICT      : PASS -- marks present and a query result is recorded")
        out.append("  ### THE GATE CHECKS THAT A QUERY WAS RECORDED, NOT THAT IT WAS THE")
        out.append("  ### RIGHT QUERY. An act that queries the wrong keys still passes.")
        return 0, out

    out.append("  query result : ### ABSENT")
    out.append("  ### VERDICT   : HARD FAILURE -- NOT BANKABLE.")
    out.append("  ### This registration marks an object OPEN / NAVIGATOR-ASSERTED /")
    out.append("  ### UNREAD / REQUIRING A CONSTRUCTION and records no index query.")
    out.append("  ### b160's convention: the index is queried and the query's result")
    out.append("  ### REPORTED before such a mark is made.")
    out.append("  ### THIS IS THE b182 FAILURE: three routes marked, nothing queried,")
    out.append("  ### and the answer one query away.")
    out.append("  ### To satisfy: python relay/tools/banked_index.py --query <object>")
    return 1, out


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    rc = 0
    for p in argv:
        print("--- INDEX-QUERY GATE (b185) ---")
        code, lines = check(p)
        for l in lines:
            print(l)
        print()
        rc = max(rc, code)
    return rc


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
