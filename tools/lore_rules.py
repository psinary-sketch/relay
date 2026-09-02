# -*- coding: utf-8 -*-
"""lore_rules.py -- THE HARNESS LORE, CONSOLIDATED (built b282).

### ### **THE DIVISION THIS FILE EXISTS TO ENFORCE:**
### ### **A JUDGEMENT RULE LISTED BESIDE A MECHANIZED ONE READS AS THOUGH SOMETHING CHECKS IT.
### ### NOTHING CHECKS IT. ### SO THEY ARE IN TWO LISTS, NOT ONE, AND THE SECOND LIST SAYS SO
### ### IN ITS OWN HEADING.**

### Every rule carries ### **ITS INCIDENT** ### -- the act that bore it.
### ### *"A rule without its incident is a preference."*
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull    # noqa: E402
import noise_floor    # noqa: E402
import hedge_audit    # noqa: E402


# ### ==========================================================================================
# ### LIST ONE -- MECHANIZED. ### **EACH NAMES THE TOOL THAT ENFORCES IT AND IS EXERCISED IN
# ### BOTH POLARITIES BELOW. ### A RULE HERE IS A GATE THAT CAN FIRE.**
# ### ==========================================================================================
MECHANIZED = [
    dict(rule='A must-fail fixture must not be a substring of the correct text.',
         incident='b277 -- a fixture fired on the CORRECT sentence, because its string was a '
                  'substring of "IT IS NOT PROVED THAT...". Invisible to reachability checks.',
         tool='needle_pull.absent_exact -- WHOLE-LINE equality, plus a suite-level count of '
              'substring-based must-fail fixtures that must be 0.',
         discharged='b278'),
    dict(rule='A fixture built from a rounded printout is not the measurement.',
         incident='b272 -- four of b264\'s printed modes were false at the floor; mode 7 sits at '
                  '2.178e-8, ABOVE sqrt(eps). A magnitude test alone would have passed all four.',
         tool='noise_floor.classify -- the DRIFT arm, not the magnitude arm, is the tool; '
              'fixtures carry b264\'s own printed DRIFT column.',
         discharged='b272'),
    dict(rule='A graded claim must not also hedge, and an assertion must say its footing.',
         incident='b279 -- the author\'s instruction; the tool then caught its own author twice '
                  '("fixes" absent from the claim-verb list; a line ending "S-bar_v?**" defeating '
                  'the question test).',
         tool='hedge_audit.audit -- two shapes, both polarities, fixtures PULLED from real files.',
         discharged='b279'),
    dict(rule='A needle is pulled from the emitting file, never typed from memory -- '
              'including a needle into the act\'s OWN files.',
         incident='b274/b275 -- mis-typed gate needles (W-ORD-NEEDLE-SOURCE); b277 -- three '
                  'needles into the act\'s own files typed from memory (W-ORD-SELF-NEEDLE); '
                  'b280 -- "THIS ACT DOES NOT WRITE IT" typed from memory, and the sentence '
                  'WRAPS A LINE.',
         tool='needle_pull.pull / pull_self -- an unpullable anchor is a FAIL, never a skip.',
         discharged='b276 (owner), b278 (self)'),
    dict(rule='A control arm that cannot exist reports UNAVAILABLE -- never a pass.',
         incident='b280 -- the not-dead witness searched k = 1..n and so tested k = n as its own '
                  'witness at level 1, WHICH WOULD HAVE REPORTED THE DEAD VALUE AS THE LIVE ONE.',
         tool='the exhaustive-arm convention (W-ORD-PREDICATE-ARM): arm B returns None, and None '
              'is counted as neither pass nor fail.',
         discharged='b280, re-used b281'),
    dict(rule='A quotation that cannot be verified verbatim is not emitted.',
         incident='b266 -- the fold\'s generator pattern. A check that runs AFTER the writing can '
                  'only report a paraphrase; one that GENERATES the writing cannot emit one.',
         tool='the constructive quotation gate (F-QUOTE) with a DISCRIMINATION control -- an '
              'altered quotation must be reported unfindable.',
         discharged='b266, re-used b282'),
    dict(rule='Compiled is not certified. A terminal outside the certification file is a file '
              'on disk.',
         incident='b289 -- `BallAbsorptionShadow` (b270) and `AbsorptionFunctionalShadow` (b271) '
                  'were built and printed by their own acts and were NEVER imported by '
                  '`AllPrints.lean`, so `AXIOM_PRINTS.txt` never carried them and their `.olean` '
                  'files were not even in the build cache. THE INDEX CORE OF EVERY BARRIER '
                  'STATEMENT IN THE ARC SAT OUTSIDE THE FILE THAT CERTIFIES THE KERNEL.',
         tool='the coverage check: a set difference of `Core/*.lean` against the `import` lines '
              'of `AllPrints.lean`. ### **ITS REACH, PRINTED WITH IT: it compares FILENAMES, so '
              'it CANNOT see a terminal in a module that IS imported but has no `#print axioms` '
              'line. That is a second species and is NOT covered.**',
         discharged='b289 (two modules); 25 remain -- `W-ORD-PRINT-COVERAGE`, filed b290'),
]

# ### ==========================================================================================
# ### LIST TWO -- ### **JUDGEMENT. ### NOT MECHANIZED, AND NOT LISTED BESIDE THE GATES ABOVE.**
# ### ### **NOTHING IN THE COMMAND PATH ENFORCES ANY OF THESE. ### THEY ARE HERE TO BE READ BY A
# ### ### SEAT BEFORE IT ACTS, AND THAT IS THEIR ONLY ENFORCEMENT.**
# ### ==========================================================================================
JUDGEMENT = [
    dict(rule='A definition can be invisible to a search for the defined term.',
         incident='b278 searched the act stream for `S-bar` definition-shapes and found the tower '
                  'ABSENT -- 191 mentions, 13 definition-shaped, none defining. b279 found the '
                  'definition in a SOURCE document under the phrase "the local Sonin closures", '
                  'a sentence that never says `S-bar_v` is being defined; it just defines it.',
         why_not_mechanized='The fix is to search for the OBJECT\'S DESCRIPTION, not its name -- '
                            'and no tool can guess which description an author used.'),
    dict(rule='When both seats agree, the falsifier is the only adversary left.',
         incident='b279 -- both seats registered (UNDERDETERMINED) and BOTH WERE WRONG. Falsifier '
                  'F1 ("a naming found only in an act does not construct") forced the search out '
                  'of the act stream and into the sources, which is where the definition was.',
         why_not_mechanized='A tool cannot know what two seats expect. The countermeasure is to '
                            'WRITE the falsifier to be able to kill the expected answer, and to '
                            'say at registration that the seats agree.'),
    dict(rule='A scope refinement is not a refutation.',
         incident='b281 -- the runner printed "FIBER LEMMA FAILS HERE" before b276\'s domain had '
                  'been read. b276\'s lemma is about ball-vanishing E_1 vectors; the runner '
                  'computed over ALL of Son. Every counterexample lay OUTSIDE E_1.',
         why_not_mechanized='Deciding whether a computation falls inside a lemma\'s domain '
                            'requires reading the lemma. The countermeasure is a registered '
                            'falsifier forbidding the word "refuted" until the domain is read.'),
    dict(rule='A print width is not a datum -- and neither is an arithmetic done in the head.',
         incident='b274 -- a pre-seal probe printed only red[:4] and INFERRED rationality, '
                  'computing fictitious values 2/7, 1/6, 1/5, 4/15. The conclusion survived; the '
                  'numbers did not. b281 -- an ordered-pair count written as 5,254 in three '
                  'places, and it is 5,746.',
         why_not_mechanized='A truncated print is well-formed output. The countermeasure is to '
                            'recompute any summed or sampled figure before the seal.'),
]


def _fixture_needle_wholeline():
    """### BOTH POLARITIES ON THE WHOLE-LINE RULE, against this file itself."""
    me = os.path.abspath(__file__)
    real = 'MECHANIZED = ['
    # ### POSITIVE: the real line is PRESENT as a whole line -> absent_exact must say False.
    pos = not needle_pull.absent_exact(me, real)
    # ### NEGATIVE: a SUBSTRING of a real line is NOT itself a whole line -> absent_exact must
    # ### say True. ### **THAT IS THE b277 SPECIES, AND THIS IS THE ARM THAT CLOSES IT.**
    neg = needle_pull.absent_exact(me, 'MECHANIZED')
    return pos, neg


def _fixture_noise_floor():
    """### BOTH POLARITIES: the exact channel, and a drifting value."""
    exact, _ = noise_floor.classify(0, exact=True)
    drift, _ = noise_floor.classify(1e-4, refined=1e-4 * 1.5)
    return exact == noise_floor.EXACT, drift == noise_floor.DRIFTING


def _fixture_hedge():
    """### BOTH POLARITIES: a graded hedge fires, a clean graded line does not."""
    fires = hedge_audit._has_grade('VERDICT: ABSENT -- it may be so.') and \
        hedge_audit._has_hedge('VERDICT: ABSENT -- it may be so.')
    quiet = not (hedge_audit._has_grade('VERDICT: ABSENT -- and nothing else.') and
                 hedge_audit._has_hedge('VERDICT: ABSENT -- and nothing else.'))
    return fires, quiet


def self_test(verbose=True):
    out = []

    def rec(s=''):
        out.append(s)
        if verbose:
            print(s)

    rec('=' * 100)
    rec('lore_rules.py -- THE CONSOLIDATED LORE. ### TWO LISTS, AND THEY ARE NOT ONE LIST.')
    rec('=' * 100)
    bad = 0

    rec('')
    rec('### LIST ONE -- MECHANIZED (%d rules). ### **EACH NAMES ITS TOOL AND ITS SCAR.**'
        % len(MECHANIZED))
    for r in MECHANIZED:
        rec('  - %s' % r['rule'])
        rec('      incident   : %s' % r['incident'])
        rec('      tool       : %s' % r['tool'])
        rec('      discharged : %s' % r['discharged'])

    rec('')
    rec('### THE FIXTURES, BOTH POLARITIES ON EACH MECHANIZED RULE THAT HAS A CALLABLE GATE:')
    for name, fn in [('whole-line must-fail (b277/b278)', _fixture_needle_wholeline),
                     ('noise floor, drift arm (b272)', _fixture_noise_floor),
                     ('hedge audit, both shapes (b279)', _fixture_hedge)]:
        a, b = fn()
        ok = a and b
        if not ok:
            bad += 1
        rec('  %-36s fires: %-5s  stays quiet: %-5s  %s'
            % (name, a, b, 'PASS' if ok else '### FAIL ###'))

    rec('')
    rec('### LIST TWO -- ### **JUDGEMENT (%d rules). ### NOTHING IN THE COMMAND PATH ENFORCES**'
        % len(JUDGEMENT))
    rec('### ### **ANY OF THESE, AND THEY ARE DELIBERATELY NOT LISTED BESIDE THE GATES ABOVE.**')
    for r in JUDGEMENT:
        rec('  - %s' % r['rule'])
        rec('      incident          : %s' % r['incident'])
        rec('      why not mechanized: %s' % r['why_not_mechanized'])

    rec('')
    rec('### F-INCIDENT: every rule in BOTH lists names an act.')
    missing = [r['rule'] for r in MECHANIZED + JUDGEMENT if 'b' not in r['incident']]
    rec('  rules missing an incident : ### **%d**' % len(missing))
    if missing:
        bad += 1
    rec('')
    rec('### THE STANDING CAUTION, REPEATED BECAUSE IT IS THE ONE THAT DOES NOT STAY LEARNED:')
    rec('### ### **A GATE THAT HAS NEVER FIRED IS NOT A GATE THAT PASSED. ### IT IS A GATE**')
    rec('### ### **NOBODY HAS SHOWN CAN FIRE.**')
    rec('=' * 100)
    return bad == 0, out


if __name__ == '__main__':
    ok, _ = self_test()
    sys.exit(0 if ok else 1)
