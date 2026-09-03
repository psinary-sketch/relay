# -*- coding: utf-8 -*-
"""b307_fold.py -- THE FOLD, b297-b306. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED** -- the arc keystone exists (b299) and is
### CROSS-REFERENCED, NOT DUPLICATED. ### Every bar was fixed in
### `data/b307_registration_2026-09-03.txt`, SEALED `ae6353ea...` before this ran.

### ### **THE DESIGN POINT, CARRIED FROM b266, b282 AND b297:**
### ### **THE RESULT TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER ### EMITS ### THE
### ### MARKDOWN THE FOLD APPENDS.** ### A quotation that fails `F-QUOTE` never reaches
### `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE;
### ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**

### ### **AND THE EMITTER DISCIPLINE, WHICH IS b283's SCAR:** ### every quotation is checked
### against ### THE ACT THAT ORIGINATED IT ### , never against an act that quoted it.
### ### **A QUOTATION OF A QUOTATION IS NOT A SOURCE.**
### ### **THE MECHANICAL CHECK IS `in the originating file`; THE JUDGEMENT -- that the sentence is
### that act's OWN VOICE and not material it was itself quoting -- IS THE SEAT'S, AND IS DECLARED
### AS THE SEAT'S IN THE BANK.** ### A tool cannot tell an act's voice from its quotations, and
### pretending otherwise would be the same false assurance this discipline exists against.
"""
import io
import json
import os
import subprocess
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
FINDINGS = os.path.join(PP, 'FINDINGS.md')
EMIT = os.path.join(D, 'b307_fold_emitted.md')
ROWS = os.path.join(D, 'b307_rows.json')

ARC = ['b297', 'b298', 'b299', 'b300', 'b301',
       'b302', 'b303', 'b304', 'b305', 'b306']

SRC = {
    'b297': 'b297_the_fold.txt',
    'b298': 'b298_the_boundary_terminal.txt',
    'b299': 'b299_the_arc_keystone.txt',
    'b300': 'b300_the_archimedean_leg.txt',
    'b301': 'b301_the_object_completed.txt',
    'b302': 'b302_the_unit_requirement.txt',
    'b303': 'b303_the_uniform_family.txt',
    'b304': 'b304_the_demands_shape.txt',
    'b305': 'b305_the_arithmetics_entry.txt',
    'b306': 'b306_the_difference.txt',
}

SECTION = 'THE ADELIC ARC, b297\u2013b306 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT)
RESULTS = [
    ('b297', 'the prior fold, filed',
     'the pairing vanishes identically on',
     'FILED \u2014 a filings act; no grade moved'),
    ('b298', 'the boundary terminal, both sides at one cell',
     'THE KERNEL NOW CARRIES BOTH SIDES OF THE BOUNDARY AT ONE CELL.',
     'BUILT \u2014 zero-axiom, and the statement carries its scope in its own conjuncts'),
    ('b299', 'the arc keystone written, and the strike that reached the command path',
     'A GENERATOR RAN TO COMPLETION, PASSED EVERY ONE OF ITS OWN FALSIFIERS, AND EMITTED',
     'WRITTEN \u2014 and the strike-reader built as a consequence'),
    ('b300', 'the archimedean leg: the space conditionally, the unit in it',
     'THE SPACE: ### (CONSTRUCTED, CONDITIONALLY).',
     '(CONSTRUCTED, CONDITIONALLY) \u2014 eight constituents supplied, one open'),
    ('b301', 'the object completed conditionally',
     'THE OBJECT IS CONSTRUCTED CONDITIONALLY, AND THE CONDITIONS ARE FOUR, EACH TYPED:',
     'CONSTRUCTED CONDITIONALLY \u2014 four conditions, each typed'),
    ('b302', 'the unit requirement: a ruling executed against quoted text',
     'IT NARROWS THE ORIGINAL WORDING RATHER',
     'EXECUTED \u2014 and what it does is narrow the wording, not fulfil it'),
    ('b303', 'the definition read at the page image, and the uniform family',
     'ONE SENTENCE, TWO OBJECTS',
     'CONFIRMS at source; the family UNIFORM AS FORM, LOCAL AS OBJECT'),
    ('b304', "the demand's shape: per-index because one-level primes have one index",
     'IT DOES NOT DISSOLVE, AND CANNOT',
     'DERIVED from the specification\u2019s own text; the compact-part smear zero and derived'),
    ('b305', 'where the arithmetic enters',
     'THESE ARE THE SAME EXPRESSION',
     'READ at content; the prime summand the source\u2019s local term, factor for factor'),
    ('b306', 'the difference: is the corpus\u2019s imbalance the source\u2019s object?',
     'A DIFFERENCE OF TWO THINGS IS THE SAME OBJECT ONLY IF BOTH ARE',
     'DIFFERENT \u2014 decided by definitions, constituent by constituent'),
]

# ### (act, THE OBSTACLE, QUOTED). ### **EVERY ONE VERIFIED AGAINST THE ACT THAT ORIGINATED IT.**
OBSTACLES = [
    ('b297', 'W-ORD-FIBER-GENERAL'),
    ('b298', 'AND THE FOUR REFUSED CANDIDATES STAY REFUSED.'),
    ('b299', 'THE STRIKE ARRIVED IN THE FERRY AND NOTHING IN THE COMMAND PATH READ THE'),
    ('b300', 'the construction is stated conditionally'),
    ('b301', 'THIS ACT NAMES AND DOES NOT PERFORM'),
    ('b302', 'IF DEFINITION 3.3.1'),
    ('b303', 'A LATER ACT MAY QUOTE THE FORM AND MAY NOT QUANTIFY OVER THE OBJECTS'),
    ('b304', 'THE REFUSED PART IS THE PART WITH AN ARCHIMEDEAN'),
    ('b305', 'HAVING THE OBJECT IS NOT DOING WITH IT WHAT THE SOURCE'),
    ('b306', 'THE FIRST DIFFERING CONSTITUENT IS THE'),
]

# ### THE ARC'S CORRECTIONS TO ITS OWN READINGS. ### (act, what was corrected, WHAT DID NOT MOVE)
CORRECTIONS = [
    ('b302', 'b300 and b301 each restated a debt b268 had already paid, pulling it from the act '
             'that INCURRED it and never asking whether a later act had PAID it.',
     'Neither act is re-verdicted. Their verdicts were about other questions and stand as banked; '
     'what was corrected is a row each of them carried.'),
    ('b303', 'b302\u2019s sentence said the object\u2019s conditions were \u201cnow three\u201d '
             'while its own list carried four. The list was right.',
     'No verdict moved and no condition was added or removed \u2014 only the count. The root was '
     'b301\u2019s headline, which counted one of its own three typed results.'),
    ('b305', 'the author\u2019s registered falsifier \u2014 that the arithmetic enters through the '
             'test function \u2014 was refuted in its first half by eq. (149).',
     'Nothing of the corpus moved. A falsifier refuted is a falsifier doing its work.'),
    ('b306', 'b305 renamed a work-order and reworded its bank and tools, but the index row had '
             'already been written: the fix touched the generator and not the generated artefact.',
     'b305\u2019s verdicts stand. The repair brought one artefact into line with its own act\u2019s '
     'bank, and two ancestors\u2019 rows carrying the same stem were FILED, not rewritten.'),
]


def fquote(text_by_act, rec):
    """### **F-QUOTE, WITH ITS DISCRIMINATION ARM.** ### A matcher that never misses is not
    matching, so an ALTERED quotation is fed to the same matcher and must come back unfindable."""
    bad = []
    for act, _what, quote, _grade in RESULTS:
        if quote not in text_by_act[act]:
            bad.append((act, 'RESULT', quote))
    for act, quote in OBSTACLES:
        if quote not in text_by_act[act]:
            bad.append((act, 'OBSTACLE', quote))
    n = len(RESULTS) + len(OBSTACLES)
    rec('  F-QUOTE  : %d quotations, %d unfindable' % (n, len(bad)))
    for act, kind, quote in bad:
        rec('      ### UNFINDABLE  %s %s -- %r' % (act, kind, quote[:74]))
    act0, _w, q0, _g = RESULTS[0]
    altered = q0.replace('pairing', 'pairingg')
    disc = altered not in text_by_act[act0]
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fcount(rec):
    covered = sorted({a for a, _w, _q, _g in RESULTS}, key=lambda s: int(s[1:]))
    obs = sorted({a for a, _q in OBSTACLES}, key=lambda s: int(s[1:]))
    ok = (covered == ARC) and (obs == ARC)
    rec('  F-COUNT  : results cover %d, obstacles cover %d, arc %d, exact match : %s'
        % (len(covered), len(obs), len(ARC), ok))
    if not ok:
        rec('      ### results missing  : %s' % [a for a in ARC if a not in covered])
        rec('      ### obstacles missing: %s' % [a for a in ARC if a not in obs])
    return ok


def emit_markdown():
    L = []

    def A(s=''):
        L.append(s)

    A('## %s' % SECTION)
    A('')
    A('**Ten acts, 2026-09-02 to 2026-09-03.** A filings section: **no grade moves here, no act '
      'is re-verdicted, and nothing below is new mathematics.** Each entry carries its grade as '
      '*its own act* left it, and every quotation was checked verbatim against the act that '
      '**originated** it before this section was emitted.')
    A('')
    A('**The arc keystone for the preceding campaign exists** — '
      '`phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md` (b299) — and is '
      '**cross-referenced here, not duplicated.**')
    A('')
    A('### The ten')
    A('')
    A('| act | what it is | grade, as its own act left it |')
    A('|---|---|---|')
    for act, what, _q, grade in RESULTS:
        A('| **%s** | %s | %s |' % (act, what, grade))
    A('')
    A('### Each with its own sentence, and its obstacle')
    A('')
    obs = dict(OBSTACLES)
    for act, what, quote, grade in RESULTS:
        A('- **%s — %s.** *Grade:* %s.' % (act, what, grade))
        A('  - Its own words: “…%s…”' % quote)
        A('  - **Obstacle, quoted:** “…%s…”' % obs[act])
    A('')
    A('### The arc\u2019s corrections to its own readings')
    A('')
    A('| act | what was corrected | **what did not move** |')
    A('|---|---|---|')
    for act, what, notmoved in CORRECTIONS:
        A('| **%s** | %s | %s |' % (act, what, notmoved))
    A('')
    A('### The arc as one statement')
    A('')
    A('At the grade these ten acts support, and no higher: **the object\u2019s two halves now '
      'share a form and a dilation** — one sentence defines a two-radius family at every place, '
      'and the finite dilation is the archimedean dilation at `1/p` under the corpus\u2019s own '
      'chart. **The finite side\u2019s first-level mass is annihilated exactly when either radius '
      'clears its threshold.** **The archimedean instruments compute with vectors that lie outside '
      'the object\u2019s own space.** And **the corpus works at the open end of a single window '
      'parameter whose closed end is the source\u2019s forced positivity** — the source chooses its '
      'window so that no prime enters; the corpus chooses its window so that every prime up to '
      '`a²` does.')
    A('')
    A('**Scope, printed beside it.** This is a summary of ten acts at their own grades. **Nothing '
      'about the identity, `h2`, or the complete roster follows from it.** One half of the '
      'one-signed residual is derived and the other is at bench; the family is a definition and '
      'not a route; the window sentence is a statement about two choices of a parameter and not '
      'about what either choice proves. **`M-2` is owed and no aggregation is stated.**')
    A('')
    A('### What this arc leaves open')
    A('')
    A('- **`M-2`** — `(SPECIFIED-NOT-STATED)`, unchanged across all ten acts.')
    A('- **The object stands on three conditions**, each typed: a premise (the level limit, b198), '
      'a ruling (`W-ORD-ARCH-NORM-READING`), a construction (C9 / `N-OPEN-B`). '
      '**A condition discharged is not the object constructed.**')
    A('- **`W-ORD-INSTRUMENT-Q-P`** — the instrument that would see the scaling direction, priced '
      'and not built.')
    A('- **`W-ORD-SOURCE-METHOD-APPLICABILITY`** — what would have to hold for the source\u2019s '
      'argument to reach the corpus\u2019s difference.')
    A('- **The seam\u2019s debt item 1** — **still unpaid.** Restated, not discharged, not '
      'renegotiated.')
    A('- **The patent lane** — carried on the patent seat\u2019s report, **unconfirmed on this '
      'seat\u2019s record.**')
    A('')
    A('### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**')
    A('')
    return '\n'.join(L)


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b307 -- THE FOLD, b297-b306. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)

    text_by_act = {}
    for act in ARC:
        text_by_act[act] = io.open(os.path.join(D, SRC[act]), encoding='utf-8').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)'
        % len(text_by_act))

    ok_q = fquote(text_by_act, rec)
    ok_c = fcount(rec)

    lean = subprocess.run(['git', '-C', ROOT, 'status', '--short', '--', '*.lean'],
                          capture_output=True, text=True).stdout.strip()
    lean2 = subprocess.run(['git', '-C', r'D:\SIDE-global-section', 'status', '--short',
                            '--', '*.lean'], capture_output=True, text=True).stdout.strip()
    ok_s = (lean == '' and lean2 == '')
    rec('  F-NOSHADOW: `.lean` files touched in either repo : %s' % ('0' if ok_s else 'SOME'))

    if not (ok_q and ok_c):
        rec('')
        rec('  ### ### **NOTHING EMITTED. ### A GATE FIRED AND THE DOCUMENT IS NOT WRITTEN.**')
        rec('=' * 100)
        with io.open(os.path.join(D, 'b307_fold_run.txt'), 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out) + '\n')
        return 1

    md = emit_markdown()
    io.open(EMIT, 'w', encoding='utf-8', newline='\n').write(md)
    rec('  emitted markdown : %s  (%d lines)' % (os.path.basename(EMIT), len(md.splitlines())))

    cur = io.open(FINDINGS, encoding='utf-8').read()
    if SECTION in cur:
        rec('  ### SECTION ALREADY PRESENT -- FINDINGS.md NOT WRITTEN (idempotence guard).')
    else:
        io.open(FINDINGS, 'w', encoding='utf-8', newline='\n').write(
            cur.rstrip('\n') + '\n\n' + md)
        rec('  FINDINGS.md : section appended')

    p = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', 'FINDINGS.md'],
                       capture_output=True, text=True)
    added = removed = 0
    if p.stdout.strip():
        parts = p.stdout.split()
        added, removed = int(parts[0]), int(parts[1])
    ok_g = (removed == 0 and added > 0)
    rec('  FINDINGS.md vs HEAD : ### **+%d / -%d**' % (added, removed))
    rec('  ### ### **F-NOGRADE %s**'
        % ('DID NOT FIRE -- no line deleted; the change is PURELY ADDITIVE.'
           if ok_g else 'FIRED. ### A LINE WAS DELETED, OR NOTHING WAS ADDED.'))

    ks = subprocess.run(['git', '-C', PP, 'status', '--short'],
                        capture_output=True, text=True).stdout.strip().splitlines()
    kpaths = [l for l in ks if 'keystone' in l.lower() or '/method/' in l.replace('\\', '/')]
    ok_k = (len(kpaths) == 0)
    rec('  F-NOKEYSTONE: files touched under a keystone path : %d  %s'
        % (len(kpaths), 'PASS' if ok_k else '### FAIL ### %s' % kpaths))

    rec('')
    rec('=' * 100)
    rec('  F-QUOTE      (every quotation verbatim in its ORIGINATING act) : ### **%s**'
        % ('DID NOT FIRE' if ok_q else 'FIRED'))
    rec('  F-COUNT      (results and obstacles both cover the arc)        : ### **%s**'
        % ('DID NOT FIRE' if ok_c else 'FIRED'))
    rec('  F-NOGRADE    (purely additive, measured by numstat)            : ### **%s**'
        % ('DID NOT FIRE' if ok_g else 'FIRED'))
    rec('  F-NOKEYSTONE (no keystone written or edited)                   : ### **%s**'
        % ('DID NOT FIRE' if ok_k else 'FIRED'))
    rec('  F-NOSHADOW   (nothing built)                                   : ### **%s**'
        % ('DID NOT FIRE' if ok_s else 'FIRED'))
    rec('=' * 100)

    json.dump(dict(arc=ARC, results=len(RESULTS), obstacles=len(OBSTACLES),
                   corrections=len(CORRECTIONS), findings_added=added,
                   findings_removed=removed, f_quote=ok_q, f_count=ok_c,
                   f_nograde=ok_g, f_nokeystone=ok_k, f_noshadow=ok_s),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    with io.open(os.path.join(D, 'b307_fold_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if (ok_q and ok_c and ok_g and ok_k and ok_s) else 1


if __name__ == '__main__':
    sys.exit(main())
