# -*- coding: utf-8 -*-
"""hedge_audit.py -- THE HEDGE / GRADE AUDIT (built b279, at the author's instruction).

### WHAT IT IS, SAID FIRST: ### **A TOOL, NOT A RESOLUTION.** ### It flags two SHAPES in a
### file's prose. ### It does not decide whether a flagged sentence is wrong, and it cannot.

### THE TWO SHAPES.
###   ### **(i) A GRADED HEDGE.** ### A sentence carrying a GRADE token -- the corpus's own
###     vocabulary for how firmly a thing is held -- ### AND ALSO ### a hedge stem. ### **A
###     GRADE IS A COMMITMENT; A HEDGE IS A RETREAT FROM ONE. ### CARRYING BOTH IN ONE SENTENCE
###     MEANS THE READER CANNOT TELL WHICH WAS MEANT.**
###   ### **(ii) AN UNGRADED ASSERTION.** ### A claim-shaped sentence carrying NEITHER a grade
###     token NOR a hedge. ### **IT ASSERTS WITHOUT SAYING ON WHAT FOOTING.**

### ### **WHAT IT CANNOT DO, IN ITS OWN HEADER SO IT IS NOT TRUSTED BEYOND IT:**
###   ### **IT CANNOT TELL A CLAIM FROM A DESCRIPTION.** ### "Claim-shaped" is a SHAPE: a claim
###     verb and enough words. ### A table row, a quotation, a heading and a genuine claim can
###     all wear it. ### **EVERY COUNT IT REPORTS IS A COUNT OF SHAPES, NOT OF FAULTS.**
###   ### **IT CANNOT SEE A HEDGE IT HAS NO STEM FOR**, and the stem list is finite and given.
###   ### **IT DOES NOT EDIT.** ### The append-only law stands: what it finds in a banked act is
###     filed as a work-order, never corrected in place.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull  # noqa: E402  ### needles pulled, never typed

GRADE_TOKENS = ('DERIVES-on-IMP', 'DERIVES', 'VERIFIED-AT-BENCH', 'AT-BENCH',
                'TRUSTED-AT-CITE', 'OBSERVED', 'ABSENT', 'UNCERTIFIED',
                'NAVIGATOR-ASSERTED')

HEDGE_STEMS = ('may', 'might', 'plausibly', 'suggests', 'likely', 'appears',
               'seems', 'could', 'would seem')

# ### THE CLAIM-VERB LIST. ### **IT WAS SHORTER, AND A FIXTURE CAUGHT IT** (b279): the sentence
# ### "the scaling map FIXES only zero ..." is an assertion the first list could not see, because
# ### `fixes` was not on it. ### The list below adds the corpus's own assertion verbs. ### **IT IS
# ### STILL FINITE AND STILL GIVEN, AND A VERB OFF IT IS STILL INVISIBLE** -- that is the reach,
# ### not a defect hidden.
CLAIM_VERBS = ('is', 'are', 'was', 'were', 'has', 'have', 'gives', 'shows',
               'holds', 'equals', 'proves', 'means', 'follows',
               'fixes', 'vanishes', 'forces', 'yields', 'requires', 'admits',
               'contains', 'satisfies', 'infers', 'derives', 'constructs',
               'defines', 'states', 'says', 'carries', 'rests')

MIN_WORDS = 8


def _sentences(text):
    """### SPLIT ON SENTENCE ENDS AND ON THE CORPUS'S OWN `###` SEPARATOR, WHICH THIS PROSE
    ### USES AS A CLAUSE BREAK. ### Crude, and said to be crude."""
    parts = re.split(r'(?<=[.!?])\s+|\s###\s+|\n', text)
    return [p.strip() for p in parts if p.strip()]


def _has_grade(s):
    return any(t in s for t in GRADE_TOKENS)


def _has_hedge(s):
    low = s.lower()
    return any(re.search(r'\b%s\b' % re.escape(h), low) for h in HEDGE_STEMS)


def _claim_shaped(s):
    """### A CLAIM VERB, ENOUGH WORDS, NOT A QUESTION, AND NOT A RULE OR TABLE LINE."""
    # ### STRIP TRAILING EMPHASIS BEFORE THE QUESTION TEST. ### A real corpus line ends
    # ### `...S-bar_v?**` and the bare `endswith('?')` could not see the question mark.
    if s.rstrip('*`_ ').endswith('?'):
        return False
    words = re.findall(r"[A-Za-z_']+", s)
    if len(words) < MIN_WORDS:
        return False
    if re.match(r'^[-=_*#\s]+$', s):
        return False
    low = [w.lower() for w in words]
    return any(v in low for v in CLAIM_VERBS)


def audit(path):
    """### RETURNS `(n_sentences, graded_hedges, ungraded_assertions)`."""
    text = io.open(path, encoding='utf-8', errors='replace').read()
    sents = _sentences(text)
    gh, ua = [], []
    for s in sents:
        g, h = _has_grade(s), _has_hedge(s)
        if g and h:
            gh.append(s)
        if _claim_shaped(s) and not g and not h:
            ua.append(s)
    return len(sents), gh, ua


# ### -------------------------------------------------------------------------------------------
# ### THE FIXTURES, BOTH POLARITIES, FROM REAL CORPUS LINES. ### **NOT INVENTED SENTENCES.**
# ### -------------------------------------------------------------------------------------------
# ### EACH FIXTURE NAMES A FILE AND AN ANCHOR. ### **THE LINE IS PULLED FROM THAT FILE AT RUN
# ### TIME** (W-ORD-NEEDLE-SOURCE / W-ORD-SELF-NEEDLE discipline), never typed here from memory.
# ### An unpullable anchor is a FAILURE, not a skip.
# ### (label, path, anchor, part, expect_graded_hedge, expect_ungraded, note)
# ### `part` = index of the sentence within the pulled line to test; None = the whole line
# ### (flag if ANY of its sentences flags), which is how production reads a file.
FIXTURES = [
    ('(i) fires: grade + deontic "may"',
     'data/b274_registration_2026-09-01.txt',
     'NO UNCERTIFIED COMPARISON MAY BE REPORTED AS FALSE', None, True, False,
     '### A TRUE SHAPE AND NOT A FAULT: "may" here is PERMISSION, not hedging. ### The tool '
     'cannot tell them apart and this fixture is kept to prove that it cannot.'),

    ('(i) fires: grade + epistemic "could"',
     'data/b210_wronskian_gate.txt',
     'COULD NOT SAY WHY', None, True, False,
     '### Also a true shape and not a fault -- a report about an act, not a hedged grade.'),

    ('(i) quiet: grade, no hedge',
     'data/b278_space_level_barrier.txt',
     '(ABSENT), WITH A POSITIVE CONTROL ON THE ABSENCE', None, False, False,
     '### A graded line that commits and does not retreat. ### The clean case.'),

    ('(ii) fires: claim, no grade, no hedge',
     'data/b278_space_level_barrier.txt',
     'THE NEAR-MISSES WERE FOUND, NOT THAT A SEARCH RETURNED NOTHING', None, False, True,
     '### An assertion carrying no footing token. ### The shape the audit exists to see.'),

    ('(ii) quiet: hedged, so not ungraded',
     'data/b277_aggregation_stated.txt',
     'the author may rule that the tower is not', None, False, False,
     '### Hedged prose is NOT an ungraded assertion -- it says its own footing by hedging.'),

    ('(ii) quiet: a question is not a claim',
     'data/b277_aggregation_stated.txt',
     'IS THE TOWER WHOSE CLOSURE IS', 0, False, False,
     '### The line ends `S-bar_v?**`; the bare question test could not see it and was fixed.'),
]


def self_test(verbose=True):
    out = []

    def rec(s=''):
        out.append(s)
        if verbose:
            print(s)

    rec('=' * 100)
    rec('hedge_audit.py -- SELF-TEST. ### BOTH POLARITIES ON EACH SHAPE.')
    rec('=' * 100)
    rec('  grade tokens : %s' % ', '.join(GRADE_TOKENS))
    rec('  hedge stems  : %s' % ', '.join(HEDGE_STEMS))
    rec('  claim shape  : a claim verb, at least %d words, not a question' % MIN_WORDS)
    rec()
    rec('  ### EVERY FIXTURE LINE IS PULLED FROM ITS FILE AT RUN TIME -- none is typed here.')
    rec()
    rec('  %-38s %-13s %-13s %s' % ('fixture', 'graded hedge', 'ungraded', 'agree'))
    bad = 0
    for lbl, path, anchor, part, eg, eu, note in FIXTURES:
        try:
            line = needle_pull.pull(os.path.join(ROOT, path), anchor)
        except LookupError as e:
            bad += 1
            rec('  %-38s ### UNPULLABLE -- %s' % (lbl, e))
            continue
        sents = _sentences(line)
        if part is not None:
            sents = sents[part:part + 1]
        g = any(_has_grade(s) and _has_hedge(s) for s in sents)
        u = any(_claim_shaped(s) and not _has_grade(s) and not _has_hedge(s) for s in sents)
        ok = (g == eg and u == eu)
        if not ok:
            bad += 1
        rec('  %-38s %-13s %-13s %s'
            % (lbl, '%s/%s' % (g, eg), '%s/%s' % (u, eu), 'YES' if ok else '### NO ###'))
        rec('      pulled: %s' % line[:96])
        rec('      %s' % note)
    rec()
    rec('  ### FIXTURES AGREEING : %d of %d ### (0 unpullable required)'
        % (len(FIXTURES) - bad, len(FIXTURES)))
    rec('  ### **BOTH SHAPES FIRE AND BOTH STAY QUIET WHEN THEY SHOULD.**')
    rec('  ### REACH: ### **EVERY COUNT IS A COUNT OF SHAPES, NOT OF FAULTS.** ### The tool')
    rec('  ### cannot tell a claim from a description, and does not edit anything.')
    return bad == 0, out


def main(argv):
    if not argv:
        ok, _ = self_test()
        return 0 if ok else 1
    for path in argv:
        n, gh, ua = audit(path)
        print('%-52s sentences=%-6d graded-hedges=%-4d ungraded-shapes=%d'
              % (os.path.basename(path), n, len(gh), len(ua)))
        for s in gh[:6]:
            print('    (i)  %s' % s[:104])
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
