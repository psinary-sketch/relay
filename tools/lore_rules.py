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
    dict(rule='A constant is scope-bound and its scope is written down. A tuple that was '
              'ample where it was born is a tuple, not a law.',
         incident='b325 -- `b321_window.PRIMES = (2, ..., 31)`, copied from the atlas\'s own '
                  'prime loop and ample at the arc\'s cells (support below 9), was carried to '
                  'a = 32 (support 1024) where it misses almost every prime in range: zeta\'s '
                  'places sum came out +0.003489041, a value b321\'s own theorem forbids. The '
                  'positive control fired; with every prime the value is -0.000389214.',
         tool='b321_window.primes_to(reach) -- the set is GENERATED to the reach of the test '
              'function\'s support and the scope is in the header (edited b326 by order); the '
              'lore self-test carries both polarities below.',
         discharged='b326'),
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
    dict(rule='Search in words as well as symbols. A symbolic-only search is half a search.',
         incident='b278->b279 -- the tower definition was recorded ABSENT after a search of the '
                  'act stream for the defined term; it sat in a source document under the phrase '
                  '"the local Sonin closures", a sentence that never names what it defines. '
                  'b286->b287 -- the bridging statements were recorded missing after an '
                  "Introduction-only read; they sit in section 4 (ADJACENT species: the DEPTH "
                  'of the search, not its FORM, labelled adjacent not counted the same). '
                  'b290->b291 -- the involutivity was recorded used-not-stated after a search for '
                  'symbolic forms and the stem "involut"; the source says it in plain English.',
         why_not_mechanized='A tool cannot guess which words an author chose for a fact it states '
                            'without symbols. The countermeasure is a habit -- run both forms, '
                            'with controls -- and b292 ran both and recorded that the symbolic '
                            'arm sufficed, which is an observation only because the other arm '
                            'was also run.'),
    dict(rule='An orbit is a confounded variable. Vary the factors independently or attribute '
              'nothing.',
         incident='b294 -- the first run tested the dilation orbit `a + b = 0` alone and returned '
                  'ZERO EVERYWHERE, which was ABOUT TO BE BANKED as "the barrier extends to the '
                  'whole orbit". The orbit couples a WEAKENED function side to a STRENGTHENED '
                  'transform side, so its zeroes could not say which side caused them. The grid '
                  '(-1,0), (0,-1), (-1,-1) separated them and the reading was wrong.',
         why_not_mechanized='A tool cannot know which of an act\'s parameters move together, '
                            'because that is a fact about what the parameters MEAN. The '
                            'countermeasure is to name, at registration, which factor each swept '
                            'coordinate is supposed to isolate -- and to refuse a one-parameter '
                            'sweep whose coordinate moves two of them.'),
    dict(rule='A true statement is not compiled when the medium cannot carry its scope.',
         incident='b294 -- the nonzero first-level value IS finite-decidable and WAS refused. A '
                  'terminal reading "the first-level value is -1" would sit in the kernel beside '
                  'the barrier\'s terminals with no room to carry the sentence that the vector is '
                  'NOT a `Son` vector. b293 refused on the neighbouring ground: a compiled '
                  'terminal would have certified the truncation and carried the family\'s name.',
         why_not_mechanized='Whether a name and a statement carry the scope that a surrounding '
                            'paragraph carries is a judgement about reading, not a property a '
                            'checker can measure. The countermeasure is the question asked '
                            'aloud before the build: what would a reader who saw ONLY this '
                            'terminal believe, and is that true?'),
    dict(rule='A property checked on the members of a spanning set is not a property of the span. '
              'THE SPECIES HAS BEEN MET TWICE -- once as a spanning family, once as a diagonal.',
         incident='b271/b272 (spanning families) -- b271 read a property off `g_0`, ONE member of '
                  'an `N`-member spanning family; b272 had to sweep all sixteen and reported '
                  '"MEMBERS OF THE SPANNING FAMILY SATISFYING (SPEC-2): 0 of 16", which is a '
                  'statement about members and not about the span. '
                  'b294/b295 (diagonals) -- b294 answered "does this member give zero?" by '
                  'computing `<A v, v>` on each vector of ONE basis and reporting ZERO on 10 of '
                  '10; `Son(2,2; -1,0)` contains `v_1 + v_6` with value 4/3. Ten such members '
                  'across six cells. b296 then found the same shape a third time in the '
                  'opposite direction: the whole FORM, not the diagonal, is what the criterion '
                  'is about, and the two are different questions with the same answer here only '
                  'because a single vector `h` realizes both.',
         why_not_mechanized='Nothing distinguishes a per-member loop that MEANS "for each member" '
                            'from one that MEANS "for the span"; the intent lives in the sentence '
                            'the act writes afterwards. The countermeasure is to carry the form\'s '
                            'TYPE next to every verdict read from it, and to compute the whole '
                            'matrix whenever the type is not symmetric.'),
    dict(rule='A symmetric expectation about two conditions is a HYPOTHESIS, not a default. '
              'Two conditions on one object are not owed the same treatment by the operator '
              'that reads them.',
         incident='THE NAVIGATOR\'S, TWICE, BOTH IN b295\'s FERRY. (i) It ordered "the '
                  'transform-side analogue of the barrier\'s function-side argument, written out '
                  'with its own hypotheses" -- the word ANALOGUE presupposing one exists. (ii) It '
                  'proposed as the joint statement that the pairing "vanishes on any member '
                  'satisfying EITHER of the object\'s two conditions, so a nonzero value requires '
                  'both to be broken". BOTH ARE FALSE: the function-side threshold is the '
                  'object\'s own radius at every level, the transform-side threshold is `n-1` and '
                  'moves with the level, and above level 1 the object\'s second condition '
                  'contributes nothing to this pairing at all.',
         why_not_mechanized='A presupposed symmetry lives in a noun ("the analogue") or a '
                            'connective ("either"), not in a checkable claim, and no scanner can '
                            'tell a symmetry that was derived from one that was assumed. The '
                            'countermeasure is a registration clause with a cap of zero: name the '
                            'symmetric default, retire it by name, and require every comparison '
                            'between the two sides to cite the operator\'s two reading scales.'),
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


def _fixture_scope_bound():
    """### BOTH POLARITIES: the frozen tuple is insufficient at reach 100 (the gate FIRES on it);
    ### the generated set reaches the prime the tuple does not (the gate stays QUIET on it)."""
    sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
    import b321_window
    gen = b321_window.primes_to(100)
    fires = (37 not in b321_window.PRIMES_ATLAS) and (max(b321_window.PRIMES_ATLAS) < 100)
    quiet = (37 in gen) and (gen[-1] == 97) and (len(gen) == 25)
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
                     ('hedge audit, both shapes (b279)', _fixture_hedge),
                     ('scope-bound constant (b325/b326)', _fixture_scope_bound)]:
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
