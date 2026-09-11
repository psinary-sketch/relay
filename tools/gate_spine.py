# -*- coding: utf-8 -*-
"""gate_spine.py -- THE THREE MATHEMATICS-FACING ARMS, BUILT AT b410 UNDER (R26)-(R28).

### ### **WHY THIS EXISTS.** ### `b409` proposed three arms and built none, because not one could
### be written without a ruling the author had not made. ### The rulings came: `(R26)` names the
### population, `(R27)` splits the score, `(R28)` names the kind check. ### **A MATHEMATICS-FACING
### ### ARM NEEDS A MATHEMATICS-FACING RULING, AND WITH THE RULING IT IS ORDINARY WORK.**
###
### ### **THE THREE ARE INDEPENDENT OF ONE ANOTHER**: three rulings, three predicates, three
### different acts' banks. ### They share no code path here beyond the reporting helper.
###
### ### ### **AND EACH IS RUN RETROACTIVELY AGAINST THE BANK OF THE INCIDENT IT WOULD HAVE
### ### ### CAUGHT.** ### `b410`'s order is exact: ### **AN ARM THAT WOULD NOT HAVE CAUGHT ITS
### ### ### OWN INCIDENT IS NOT BUILT.** ### An arm asserted to work is an arm untested; these
### report the retroactive run and let the reader see it fire.
###
### ### **EVERY ARM CARRIES FIXTURES IN BOTH POLARITIES**, on synthetic text written here and
### drawn from no bank -- because a fixture drawn from the thing it tests is not a fixture.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import gate_text                  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


RULE = re.compile('[-=]{8,}')


def fold(s):
    """### **MARKUP FOLDED AWAY BEFORE ANY MATCH** -- markers, backticks, emphasis, line breaks.

    ### ### **AND THE HORIZONTAL RULES ARE CUT TO A FULL STOP, NOT TO A SPACE.** ### A run of
    ### dashes between two sections is a SENTENCE BOUNDARY in a banked record; folding it to a
    ### space glues the end of one section to the heading of the next, and the first version of
    ### this file reported a match on exactly such a splice. ### **A FALSE POSITIVE FROM A JOIN
    ### ### THE WRITER NEVER MADE IS NOT A CATCH.**
    """
    s = RULE.sub('. ', (s or ''))
    return re.sub(r'\s+', ' ', s.replace('###', ' ').replace('`', '').replace('*', ''))


def sentences(text):
    """### Split folded text into sentences. ### **ONE PLACE, SO EVERY ARM SPLITS ALIKE.**"""
    return [x for x in re.split(r'(?<=[.!?])\s+', fold(text)) if x.strip()]


def bank(act):
    """### The named act's bank, read from `data/`. ### **BY CONTENT, NOT BY A TYPED PATH.**"""
    cands = [f for f in sorted(os.listdir(D))
             if f.startswith(act + '_') and f.endswith('.txt')
             and not re.search(r'_(checks|census|pins|ferry|reg|lockgate|satisfiable|'
                               r'desk_notes|extract|components|closing|mirror|audit|'
                               r'index_query|span|scheme_table)', f)]
    if not cands:
        return None, None
    p = os.path.join(D, cands[0])
    return cands[0], io.open(p, encoding='utf-8', errors='replace').read()


# ### =================================================================================================
# ### (1) G-VACUOUS-POPULATION -- under (R26), THE POPULATION.
# ### =================================================================================================
# ### **THE INFLECTIONS ARE IN THE PATTERN.** ### The first version matched `PASS` with a trailing
# ### word boundary and was therefore blind to `PASSES`, `PASSED` and `SURVIVED`. ### **ITS OWN
# ### FIXTURE CAUGHT THAT**, which is the whole reason the fixture is written before the arm is
# ### trusted -- an arm whose vocabulary is narrower than its subject's reports a clean absence.
PASSWORD = re.compile(r'\b(PASS|PASSES|PASSED|PASSING|MET|SURVIVE|SURVIVES|SURVIVED|HOLD|HOLDS|'
                      r'SATISFIED|CONFIRMED|CERTIFIED)\b', re.I)
VACUOUS = re.compile(r'\bvacuous(?:ly)?\b', re.I)
# ### **THE EMPTINESS MUST BE THE POPULATION'S, NOT ANY ZERO IN THE SENTENCE.** ### A pattern that
# ### accepted a bare `0 of` matched fixture tallies and census rows, which is how this arm first
# ### reported nine hits on an act with one incident.
EMPTYPOP = re.compile(r'\bempty (?:\w+ ){0,2}(?:sum|set|class|family|population)\b'
                      r'|\bno (?:lawful )?(?:seeds?|primes?|prime powers?|terms?|elements?)\b'
                      r'|\bholds no prime\b|\bnothing to range over\b'
                      r'|\bcould not have (?:failed|produced)\b'
                      r'|\bpopulation .{0,30}\b(?:zero|empty)\b', re.I)
# ### A fixture row, a census tally or an arm-name list -- never a verdict about the object.
TABLEROW = re.compile(r'got/expected|got/exp|fixture|True/True|False/False|YES\b.*YES\b'
                      r'|\bG-[A-Z][A-Z0-9-]+\b.*\bG-[A-Z][A-Z0-9-]+\b', re.I)


def vacuous_population(text):
    """### **(R26): A PASS MUST PRINT THE SIZE OF THE POPULATION THAT COULD HAVE PRODUCED A FAIL,
    ### and say VACUOUS in the SAME SENTENCE when that size is zero.**

    ### Returns `(fires, offenders, examined)`. ### **IT FIRES ON A PASS WHOSE OWN SENTENCE SAYS
    ### THE POPULATION WAS EMPTY AND DOES NOT SAY `VACUOUS` THERE** -- the exact shape of `b399`,
    ### where the only lawful seeds give an empty prime sum and the pass was banked before anyone
    ### noticed the test could not have failed.
    """
    offenders, examined = [], 0
    for s in sentences(text):
        # ### **A FIXTURE TABLE IS NOT A VERDICT.** ### The first version counted rows of
        # ### `got/expected agree ... YES` as passes and fired on nine of `b399`'s files, none
        # ### of them the incident. ### **A FILTER THAT KEEPS THE NOISE HAS NOT FOUND THE
        # ### ### SIGNAL**, so table rows and arm-name lists are excluded before anything counts.
        if TABLEROW.search(s) or not PASSWORD.search(s):
            continue
        examined += 1
        if EMPTYPOP.search(s) and not VACUOUS.search(s):
            offenders.append(s[:150])
    return bool(offenders), offenders, examined


def vacuous_population_fixtures(verbose=False):
    """### **BOTH POLARITIES.** ### A pass over an empty population WITHOUT the word must FIRE;
    ### the same sentence WITH the word must not; and an ordinary pass must not."""
    bad = 'The sign test PASSES: the only lawful seeds give an empty prime sum.'
    good = ('The sign test PASSES vacuously: the only lawful seeds give an empty prime sum, '
            'so the population that could have failed is of size zero.')
    plain = 'The identity HOLDS at all seven cells, against 128 candidates that could have failed.'
    r = (vacuous_population(bad)[0], not vacuous_population(good)[0],
         not vacuous_population(plain)[0])
    if verbose:
        print('    (1a) a pass over an empty population, unmarked -> FIRES   %s' % r[0])
        print('    (1b) the same sentence saying VACUOUS          -> quiet   %s' % r[1])
        print('    (1c) an ordinary pass with its population      -> quiet   %s' % r[2])
    return all(r)


# ### =================================================================================================
# ### (2) G-PREMISE-BEFORE-CONCLUSION -- under (R27), THE SPLIT SCORE.
# ### =================================================================================================
# ### **THE COMPLIANT FORM IS WRITTEN SEVERAL WAYS AND THE ARM MUST KNOW THEM ALL.** ### `(R27)`
# ### names one wording; `b404` reached the same disposition in its own words -- *PREMISE REFUTED,
# ### CONCLUSION SURVIVING ON OTHER GROUNDS* -- and an arm that knew only the ruling's phrasing
# ### would have fired on the one act that got it right.
SPLIT = re.compile(r'REFUTED IN PREMISE|MET ON OTHER GROUNDS|PREMISE REFUTED'
                   r'|CONCLUSION SURVIV\w+|survives on other grounds', re.I)
FALSEPREM = re.compile(r'\bpremise\b[^.]{0,80}\b(is|was|are|were)\b[^.]{0,20}'
                       r'\b(false|refuted|wrong)\b', re.I)
# ### **AND THE HIT MUST SIT IN A SCORING CONTEXT.** ### *A conclusion shown to rest on a false
# ### premise is not thereby shown false* is a statement OF the rule, not a score under it; the
# ### first version fired on that very sentence in four files.
SCORED = re.compile(r'\((?:N|E|L|F)\d+\)|\bMET\b|\bREFUTED\b|\bSCORED\b|\bexpectation', re.I)


def premise_before_conclusion(text):
    """### **(R27): A REFUTED PREMISE WITH A SURVIVING CONCLUSION IS SCORED APART, NEVER AVERAGED.**

    ### Returns `(fires, offenders, examined)`. ### **IT FIRES WHERE A PASSAGE SAYS A PREMISE IS
    ### FALSE AND THEN GIVES THE ITEM ### ONE ### WORD** -- the shape of `b404`, whose `(N2)`
    ### reasoned from a false premise while its conclusion survived on other grounds, and which
    ### the act caught by hand because no arm could.
    """
    offenders, examined = [], 0
    flat = fold(text)
    for m in FALSEPREM.finditer(flat):
        window = flat[max(0, m.start() - 200):m.start() + 700]
        if not SCORED.search(window):
            continue
        examined += 1
        if not SPLIT.search(window):
            offenders.append(window[200:350] if m.start() > 200 else window[:150])
    return bool(offenders), offenders, examined


def premise_before_conclusion_fixtures(verbose=False):
    """### **BOTH POLARITIES.** ### A false premise scored in one word must FIRE; the same scored
    ### apart must not; and a passage with no premise claim must not."""
    bad = ('(N2) is MET. The premise the draft reasoned from is false, the corpus is not a '
           'one-L-function corpus, and the conclusion stands.')
    good = ('(N2) is REFUTED IN PREMISE / MET ON OTHER GROUNDS. The premise the draft reasoned '
            'from is false -- the corpus is not a one-L-function corpus -- and the conclusion '
            'survives because Theorem 6.1 ranges over a class the second object is not in.')
    plain = 'The identity holds at all seven cells and the margin is negative at every frame.'
    r = (premise_before_conclusion(bad)[0], not premise_before_conclusion(good)[0],
         not premise_before_conclusion(plain)[0])
    if verbose:
        print('    (2a) a false premise scored in ONE word       -> FIRES   %s' % r[0])
        print('    (2b) the same scored apart under (R27)        -> quiet   %s' % r[1])
        print('    (2c) a passage making no premise claim        -> quiet   %s' % r[2])
    return all(r)


# ### =================================================================================================
# ### (3) G-KIND-BEFORE-APPLICATION -- under (R28), THE KIND CHECK.
# ### =================================================================================================
APPLIES = re.compile(r'\b(applies|apply|applied|instance of|covered by|governed by)\b', re.I)
# ### **THE RECORD NAMES ITS RESULTS IN PROSE AS OFTEN AS BY NUMBER**, and the first version of
# ### this arm -- which saw only `Theorem 3.1` and its siblings -- examined ### **ZERO** ###
# ### sentences across three banks that discuss almost nothing else. ### **AN ARM THAT EXAMINES
# ### ### NOTHING REPORTS A CLEAN ABSENCE, WHICH IS THE WORST THING AN ARM CAN DO.**
RESULT = re.compile(r'\b(?:Theorem|Lemma|Corollary|Proposition|Definition)\s+[0-9C][.0-9A-Za-z-]*'
                    r'|\b(?:barrier|ceiling|sieve[- ]ceiling|exclusion) theorem\b'
                    r'|\bthe (?:countermodel|criterion|witness form|shared-witness form)\b',
                    re.I)
KINDWORD = re.compile(r'\bkind\b|\bquantifies over\b|\branges over\b|\bis of the (?:same )?kind\b'
                      r'|\bthe object is a\b|\bnot an? \w+ at all\b', re.I)


def kind_before_application(text):
    """### **(R28): A RESULT APPLIES TO AN OBJECT ONLY IF THE OBJECT IS OF THE KIND THE RESULT
    ### QUANTIFIES OVER**, and the act must say both kinds side by side before the citation stands.

    ### Returns `(fires, offenders, examined)`. ### **IT FIRES ON A SENTENCE APPLYING A NAMED
    ### RESULT TO AN OBJECT WITHOUT NAMING EITHER KIND** -- the shape `b405`, `b406` and `b407`
    ### each met independently, and which `b408` found was one statement wearing four dresses.
    """
    offenders, examined = [], 0
    ss = sentences(text)
    for i, s in enumerate(ss):
        if not (APPLIES.search(s) and RESULT.search(s)):
            continue
        examined += 1
        # ### **THE KIND MAY BE NAMED IN THE VERY NEXT SENTENCE AND THAT IS COMPLIANT.** ### An
        # ### arm confined to one sentence fired on `b407`'s *VERDICT: NOT AN INSTANCE OF THEOREM
        # ### 3.1*, an act that named both kinds in the sentence beside it. ### **AN ARM THAT
        # ### ### CANNOT SEE A NEIGHBOURING SENTENCE CONVICTS THE CAREFUL ALONG WITH THE CARELESS.**
        near = ' '.join(ss[i:i + 2])
        if not KINDWORD.search(near):
            offenders.append(s[:150])
    return bool(offenders), offenders, examined


def kind_before_application_fixtures(verbose=False):
    """### **BOTH POLARITIES.** ### A citation with no kind stated must FIRE; the same citation
    ### naming both kinds must not; and a sentence citing no result must not."""
    bad = 'Theorem 3.1 applies to the corpus reduction, so the halt at K8 is an instance of it.'
    good = ('Theorem 3.1 quantifies over formal first-order proofs and the reduction is a gate '
            'of eight constituents, so the object is not of the kind the result ranges over and '
            'Theorem 3.1 does not apply to it.')
    plain = 'The margin is negative at every frame and the sign is certified at all seven cells.'
    r = (kind_before_application(bad)[0], not kind_before_application(good)[0],
         not kind_before_application(plain)[0])
    if verbose:
        print('    (3a) a result applied with NO kind stated     -> FIRES   %s' % r[0])
        print('    (3b) the same citation naming both kinds      -> quiet   %s' % r[1])
        print('    (3c) a sentence citing no result at all       -> quiet   %s' % r[2])
    return all(r)


# ### =================================================================================================
ARMS = (
    ('G-VACUOUS-POPULATION', '(R26)', vacuous_population, vacuous_population_fixtures,
     ('b399',), 'the sign test passed VACUOUSLY and was banked before the vacuity was noticed'),
    ('G-PREMISE-BEFORE-CONCLUSION', '(R27)', premise_before_conclusion,
     premise_before_conclusion_fixtures, ('b404',),
     'an expectation reasoned from a false premise while its conclusion survived'),
    ('G-KIND-BEFORE-APPLICATION', '(R28)', kind_before_application,
     kind_before_application_fixtures, ('b405', 'b406', 'b407'),
     'a result cited about an object of the wrong kind, three times independently'),
)


def self_test(verbose=False):
    """### **ALL THREE ARMS, BOTH POLARITIES.** ### An arm that cannot fail is not an arm."""
    return all(fx(verbose) for _n, _r, _f, fx, _b, _w in ARMS)


def retroactive(verbose=False):
    """### **THE RUN THAT DECIDES WHETHER THE ARM IS BUILT AT ALL.**

    ### Each arm is run against the bank of the incident it was written for. ### Returns a list of
    ### `(arm, ruling, act, bankfile, fired, n_offenders, n_examined)`. ### **AN ARM THAT DOES NOT
    ### FIRE ON ITS OWN INCIDENT IS REPORTED NOT BUILT**, and this function never hides that.
    """
    out = []
    for name, ruling, fn, _fx, acts, _why in ARMS:
        for act in acts:
            files = sorted(f for f in os.listdir(D)
                           if f.startswith(act + '_') and f.endswith(('.txt', '.json')))
            hits, examined, offenders, head = [], 0, [], None
            for f in files:
                txt = io.open(os.path.join(D, f), encoding='utf-8', errors='replace').read()
                fires, off, ex = fn(txt)
                examined += ex
                if fires:
                    hits.append((f, len(off)))
                    offenders.extend(off[:1])
                if f == bank(act)[0]:
                    head = fires
            out.append((name, ruling, act, hits, bool(hits), len(offenders), examined, head))
            if verbose:
                print('    %-28s on %-6s : %s -- %d of %d file(s) fire, %d sentence(s) examined'
                      % (name, act, 'FIRES' if hits else 'QUIET', len(hits), len(files), examined))
                print('        headline bank alone : %s'
                      % ('FIRES' if head else 'quiet -- the bank records the REPAIR, not the '
                                             'defect, because the act caught it by hand'))
                for f, n in hits[:3]:
                    print('        | %-46s %d offending' % (f, n))
                for o in offenders[:1]:
                    print('        | %s' % o[:140])
    return out


if __name__ == '__main__':
    print('gate_spine.py -- the three ruled arms.')
    print('  fixtures, both polarities on every arm:')
    ok = all(fx(True) for _n, _r, _f, fx, _b, _w in ARMS)
    print('  ### FIXTURES : %s' % ok)
    print()
    print('  the retroactive runs, against the banks of the incidents themselves:')
    rows = retroactive(True)
    fired = {}
    for row in rows:
        name, f2 = row[0], row[4]
        fired[name] = fired.get(name, False) or f2
    print()
    for name, _r, _f, _fx, _b, why in ARMS:
        print('  ### %-30s fires on its own incident : %s   (%s)'
              % (name, fired.get(name), why))
    built = all(fired.values())
    print('  ### ### **ARMS BUILT : %d of %d.**' % (sum(1 for v in fired.values() if v), len(ARMS)))
    sys.exit(0 if (ok and built) else 1)
