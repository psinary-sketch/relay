# -*- coding: utf-8 -*-
"""b300_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### WHY THIS FILE EXISTS RATHER THAN A HAND-WRITTEN JSON. ### `W-ORD-ADHOC-CHECK-FIXTURES`
### (b298) is the standing work-order and ruling (3) of the b300 ferry confirms it stands:
### ### **EVERY NUMBER AN ACT REPORTS COMES FROM A COMMITTED TOOL THAT CARRIES FIXTURES.**
### A satisfiability spec whose `demand` cells were typed at the shell would be exactly the
### shape that work-order was filed against -- ### **a number that looks measured and was
### asserted.**

### WHAT IT DOES. ### It measures ONE demand off the registration's own text -- ruling (1)'s
### ### **ARTIFACT-COUNT PREDICTIONS** ### -- and emits the spec with the four planned-zero
### demands beside it, each naming the closing gate that RE-MEASURES it after the act runs.

# ### THE LIMITS, IN THE HEADER SO THE TOOL IS NOT TRUSTED BEYOND THEM:
# ### (1) ### **A CAP IS NOT A PREDICTION.** ### `CAP 0` and `cap of zero` are ceilings the act
# ###     binds itself to, not counts of things it expects to build. ### They are EXCLUDED, and
# ###     that exclusion is a JUDGEMENT this tool makes on the act's behalf -- ### **A REGISTRATION
# ###     COULD SMUGGLE A PREDICTION IN AS A CEILING AND THIS TOOL WOULD NOT SEE IT.**
# ### (2) ### **IT MATCHES A NUMERAL BESIDE AN ARTIFACT NOUN.** ### A prediction phrased without
# ###     either -- "the usual suite", "one per component" -- is invisible to it. ### The noun list
# ###     is this tool's whole reach and it is printed with the result.
# ### (3) ### **THE FOUR PLANNED-ZERO DEMANDS ARE THE ACT'S CLAIMS ABOUT ITS OWN FUTURE**, which
# ###     no tool can measure before the act runs. ### They are re-measured in `b300_checks.py`
# ###     against the files that actually landed, and THAT is where they become evidence.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REG = os.path.join(ROOT, 'data', 'b300_registration_2026-09-02.txt')
SPEC = os.path.join(ROOT, 'data', 'b300_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE ARTIFACT NOUNS. ### **PRINTED WITH THE RESULT, BECAUSE THE LIST IS THE REACH.**
NOUNS = ('gates?|tools?|needles?|fixtures?|terminals?|artifacts?|documents?|checks?|modules?'
         r'|\.lean files?|banks?|components?')
NUMERAL = r'(?:\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)'
PRED = re.compile(r'\b%s\s+(?:%s)\b' % (NUMERAL, NOUNS), re.IGNORECASE)
# ### A CEILING IS NOT A PREDICTION -- see limit (1).
CAP = re.compile(r'\bcap\s+(?:of\s+)?%s\b' % NUMERAL, re.IGNORECASE)


def count_predictions(text):
    """### RETURN `(n, hits)`. ### A hit is `(line_no, matched_text)`.

    ### **A NUMERAL-PLUS-NOUN INSIDE A `CAP ...` PHRASE IS NOT COUNTED**, and the whole line is
    ### tested for the ceiling form so that `CAP 0` followed by a noun clause is not read as a
    ### prediction of zero objects.
    """
    hits = []
    for i, line in enumerate(text.splitlines(), 1):
        if CAP.search(line):
            continue
        for m in PRED.finditer(line):
            hits.append((i, m.group(0)))
    return len(hits), hits


def self_test(verbose=True):
    """### **BOTH POLARITIES, AND THE NEAR-MISS IS THE CEILING.**"""
    cases = [
        ('fires: a plain artifact-count prediction',
         'This act will produce 12 terminals and a bank.', 1),
        ('fires: a spelled numeral',
         'The suite registers three gates before the run.', 1),
        ('quiet: a ceiling, which is a prohibition and not a prediction',
         'ad-hoc shell-typed numbers: CAP 0 -- vs the demand, every number reported.', 0),
        ('quiet: a numeral governing a non-artifact noun',
         "Definition 4.4's TWO CONDITIONS are tested separately.", 0),
        ('quiet: an act name carrying digits',
         'b298 filed the work-order and b299 was the first act bound by it.', 0),
        ('quiet: a numeral with no noun beside it',
         'The scan returned 0 and the control returned 14.', 0),
    ]
    ok = True
    if verbose:
        print('  %-58s %-9s %s' % ('fixture', 'got/exp', 'agree'))
    for lbl, text, exp in cases:
        got, _ = count_predictions(text)
        agree = (got == exp)
        ok = ok and agree
        if verbose:
            print('  %-58s %-9s %s' % (lbl, '%d/%d' % (got, exp), 'YES' if agree else '### NO ###'))
    return ok


CLAUSES = [
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / W-ORD-ADHOC-CHECK-FIXTURES (b298). ### PLANNED ZERO; RE-MEASURED IN THE CLOSING"
     " BY `b300_checks.py`'s G-TOOLNUM, which lists the committed tool behind each reported number."),
    ("files written under a deposited path", 0, 0, "files",
     "THE SCOPE CLAUSE: nothing deposits. ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY"
     " `b300_checks.py`'s G-NODEPOSIT against `git status` over the deposited trees."),
    ("`.lean` files moved", 0, 0, "files",
     "THE SHADOW'S OWN EXPECTATION (T8). ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY"
     " `b300_checks.py`'s G-SHADOW against the kernel repo's working tree."),
    ("PLACE-papers files written", 0, 0, "files",
     "THE SCOPE CLAUSE: PLACE-papers is READ ONLY this act, so no hook and no place_add."
     " ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY `b300_checks.py`'s G-NOPAPERS."),
]


def main(argv):
    print('=' * 100)
    print('b300_regspec.py -- THE SATISFIABILITY SPEC, COMPUTED FROM THE REGISTRATION.')
    print('=' * 100)
    print('  SELF-TEST (both polarities; the near-miss is the ceiling form):')
    if not self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()
    print('  artifact nouns this counter can see : %s' % NOUNS.replace('|', ', '))
    print('  ### **THAT LIST IS THE WHOLE OF THE REACH.**')

    text = io.open(REG, encoding='utf-8').read()
    n, hits = count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))

    clauses = [{"clause": c, "cap": cap, "demand": dem, "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    clauses.append({
        "clause": "artifact counts predicted in this registration",
        "cap": 0, "demand": n, "units": "predictions",
        "from": "RULING (1), U-1 CONFIRMED STRUCK. ### MEASURED off the registration's own text by"
                " `tools/b300_regspec.py`, whose counter carries fixtures in both polarities and"
                " whose near-miss fixture is the ceiling form (`CAP 0`), since **A CEILING IS A"
                " PROHIBITION AND NOT A PREDICTION.**"})

    spec = {"registration": "data/b300_registration_2026-09-02.txt -- b300, THE ARCHIMEDEAN LEG",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)

    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and back['clauses'][-1]['demand'] == n
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
