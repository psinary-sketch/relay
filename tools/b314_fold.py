# -*- coding: utf-8 -*-
"""b314_fold.py -- THE FOLD, b307-b313. ### THE GENERATOR, NOT A REVIEW.

### **A FILINGS ACT. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NO NEW MATHEMATICS.
### ### NO KEYSTONE IS CREATED OR EDITED.**

### ### **THE DESIGN POINT, CARRIED FROM b266, b282, b297 AND b307:**
### ### **THE RESULT TABLE BELOW IS THE SINGLE SOURCE OF TRUTH, AND THIS RUNNER ### EMITS ### THE
### ### MARKDOWN THE FOLD APPENDS.** ### A quotation that fails `F-QUOTE` never reaches
### `FINDINGS.md` at all. ### **A CHECK THAT RUNS AFTER THE WRITING CAN ONLY REPORT A PARAPHRASE;
### ONE THAT GENERATES THE WRITING CANNOT EMIT ONE.**

### ### **AND THE EMITTER DISCIPLINE, WHICH IS b283's SCAR AND WHICH FIRED AGAIN AT b307:** ###
### every quotation is checked against ### THE ACT THAT ORIGINATED IT ### , never against an act
### that quoted it. ### **A QUOTATION OF A QUOTATION IS NOT A SOURCE.**
### ### **THE MECHANICAL CHECK IS `in the originating file`; THE JUDGEMENT -- that the sentence is
### that act's OWN VOICE and not material it was itself quoting -- IS THE SEAT'S, AND IS DECLARED
### AS THE SEAT'S IN THE BANK.**
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
EMIT = os.path.join(D, 'b314_fold_emitted.md')
ROWS = os.path.join(D, 'b314_fold_rows.json')

ARC = ['b307', 'b308', 'b309', 'b310', 'b311', 'b312', 'b313']

SRC = {
    'b307': 'b307_the_fold.txt',
    'b308': 'b308_the_local_field_instrument.txt',
    'b309': 'b309_the_scaling_trace.txt',
    'b310': 'b310_the_smear_collapses.txt',
    'b311': 'b311_the_identitys_neighbourhood.txt',
    'b312': 'b312_the_remainder.txt',
    'b313': 'b313_the_exponent.txt',
}

SECTION = 'THE INSTRUMENT ARC, b307\u2013b313 \u2014 THE FOLD'

# ### (act, what it is, THE QUOTATION, the grade AS ITS OWN ACT LEFT IT, THE SCOPE SENTENCE)
RESULTS = [
    ('b307', 'the prior fold filed, and a struck phrase licensed by a check that was built for it',
     'BEFORE: 26 MISSING -- TEN ACTS, FOURTEEN LIVE WORK-ORDERS',
     'FILED \u2014 a filings act; no grade moved',
     'The census counts NAMES in ONE ledger. It says nothing about `FINDINGS.md`, `REGISTRY.md`, '
     '`OPEN_TRAILS.md` or the desk, and a ledger naming every act in one line each passes it.'),
    ('b308', 'the local-field instrument: the two radii untied',
     'THE MODEL IS THE POINT `r = s = n`. ### THE INSTRUMENT IS THE PLANE.',
     'BUILT \u2014 an instrument and its reproduction controls; no first-level value computed on it',
     'The instrument reproduces every banked finite-side result and computes nothing new. The '
     'escaped-mass artifact is retired **for this instrument alone**.'),
    ('b309', 'the scaling trace, computed where the model could not reach',
     'THE VALUE IS EXACTLY ZERO, AT EVERY NONZERO POWER, AT EVERY BANKED CELL',
     'COMPUTED \u2014 exactly zero, 44 cell/power pairs, 0 disagreeing; three zero-axiom terminals',
     'One trace of one map against one projection, at the listed cells and powers, in the smallest '
     'ambient containing source and target. A different ambient is a different number.'),
    ('b310', "the source's construction assembled at a finite place",
     'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION',
     'COMPUTED AND DERIVED \u2014 one surviving term, `T(w) = w_0 (p^n \u2212 1)\u00b2`; '
     'two zero-axiom terminals',
     'This is what the construction returns AT A FINITE PLACE, on this object, in this '
     'compression. The archimedean contrast is named and not derived.'),
    ('b311', "the identity's neighbourhood: does the finite mechanism type at infinity?",
     'DOES NOT TYPE AT THE ARCHIMEDEAN PLACE',
     'DECIDED AT DEFINITIONS \u2014 a refusal, not a negative result',
     'A statement about TYPES \u2014 that a question answered on one side does not parse on the '
     'other. The corpus has done no mathematics at infinity here.'),
    ('b312', "the remainder: is the corpus's archimedean remainder the source's?",
     'NO. ### DIFFERENT.',
     'DIFFERENT \u2014 decided at definitions, constituent by constituent; eight of nine agree',
     'Two written definitions were compared and nothing was computed. No banked measurement is '
     'called wrong; what may change is what a banked number is a computation OF.'),
    ('b313', 'the exponent: the check b312 filed, run',
     'THE RESIDUE DOES NOT COLLAPSE',
     'MEASURED, AND NEGATIVE \u2014 the residue shrinks by 8% to 19% and keeps its order of '
     'magnitude',
     'The owner instrument was not edited; a copy carried the flip. No target was named and no fit '
     'was performed. The convention accounts for part of the residue and not for the rest.'),
]

# ### (act, THE OBSTACLE, QUOTED). ### **EVERY ONE VERIFIED AGAINST THE ACT THAT ORIGINATED IT.**
OBSTACLES = [
    ('b307', 'QUOTATION OF A QUOTATION IS NOT A SOURCE'),
    ('b308', 'IT IS NOT RETIRED FOR THE MODEL.'),
    ('b309', 'REGIME B: THE COMPRESSION IS ALIVE AND ITS TRACE IS ZERO'),
    ('b310', 'THIS ACT DERIVES NOTHING'),
    ('b311', 'CLAIMS NONE'),
    ('b312', 'CANNOT CHECK IT AND DOES NOT'),
    ('b313', 'IT DOES NOT ACCOUNT FOR THE REST'),
]

# ### THE ARC'S CORRECTIONS TO ITS OWN READINGS. ### (act, what was corrected, WHAT DID NOT MOVE)
CORRECTIONS = [
    ('b309', 'Its sealed prediction `(P4)` said, of the disjoint regime, that \u201c*the composed '
             'operator is IDENTICALLY ZERO*\u201d. It is the **compression** that vanishes \u2014 '
             'the image is orthogonal to the space rather than absent.',
     'The content survived; the wording did not. The seal is not edited and no value the act '
     'reports moved.'),
    ('b310', 'Its sealed prediction named the normalizing factor \u201c*the modulus of `t`*\u201d. '
             'The factor is the embedding\u2019s Haar weight, which agrees with the modulus at '
             'every unit and every positive power and differs at every negative one.',
     'The count is the content; the factor is what the prediction got wrong, and it changes no '
     'value the act reports.'),
    ('b311', 'Its sealed registration says the source artefact was not on this machine. **It was '
             '\u2014 in six byte-identical copies**, none of them in a location the corpus owns. '
             'The seat asserted a negative from a search that had not finished.',
     'The seal is not edited; the withdrawal is in the bank at full prominence. The re-acquisition '
     'and its hash check stand, and `W-ORD-ARTEFACT-PATHS` is strengthened rather than weakened.'),
    ('b313', 'Its own `G-ROUNDTRIP` control fired on the first run: the flip had been written as a '
             'code fragment whose inverse already occurs elsewhere in the same file. **And the '
             'first version of the tool wrote the copy anyway, reporting the failure beside it.**',
     'Both were repaired before any column was read \u2014 whole-line substitutions, and the write '
     'gated on the controls. A reported failure that changes nothing is a failure nobody has to '
     'act on.'),
]

# ### **THE THREE SEALED PREDICTIONS THAT FAILED AT A NORMALIZATION, AS ONE ROW.**
PREDICTIONS = [
    ('b309', 'the operator named', 'the composed map, where it is the compression that vanishes'),
    ('b310', 'the factor named', 'the modulus, where it is the embedding\u2019s Haar weight'),
    ('b312', 'the navigator\u2019s registered expectation',
     '\u201csame function up to the normalization \u2026 by a factor\u201d, where the factor is '
     '`\u03c1` and a function of the variable is not a scalar'),
]


def fquote(text_by_act, rec):
    """### **F-QUOTE, WITH ITS DISCRIMINATION ARM.** ### A matcher that never misses is not
    matching, so an ALTERED quotation is fed to the same matcher and must come back unfindable."""
    bad = []
    for act, _w, quote, _g, _s in RESULTS:
        if quote not in text_by_act[act]:
            bad.append((act, 'RESULT', quote))
    for act, quote in OBSTACLES:
        if quote not in text_by_act[act]:
            bad.append((act, 'OBSTACLE', quote))
    n = len(RESULTS) + len(OBSTACLES)
    rec('  F-QUOTE  : %d quotations, %d unfindable' % (n, len(bad)))
    for act, kind, quote in bad:
        rec('      ### UNFINDABLE  %s %s -- %r' % (act, kind, quote[:74]))
    act0, _w, q0, _g, _s = RESULTS[0]
    altered = q0.replace('MISSING', 'MISSINGG')
    disc = altered not in text_by_act[act0]
    rec('  ### DISCRIMINATION CONTROL: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def fcount(rec):
    covered = sorted({a for a, _w, _q, _g, _s in RESULTS}, key=lambda s: int(s[1:]))
    obs = sorted({a for a, _q in OBSTACLES}, key=lambda s: int(s[1:]))
    ok = (covered == ARC) and (obs == ARC)
    rec('  F-COUNT  : results cover %d, obstacles cover %d, arc %d, exact match : %s'
        % (len(covered), len(obs), len(ARC), ok))
    if not ok:
        rec('      ### results missing  : %s' % [a for a in ARC if a not in covered])
        rec('      ### obstacles missing: %s' % [a for a in ARC if a not in obs])
    return ok


def emit_markdown(cc):
    L = []

    def A(s=''):
        L.append(s)

    A('## %s' % SECTION)
    A('')
    A('**Seven acts, 2026-09-03.** A filings section: **no grade moves here, no act is '
      're-verdicted, and nothing below is new mathematics.** Each entry carries its grade as *its '
      'own act* left it and its own scope sentence, and every quotation was checked verbatim '
      'against the act that **originated** it before this section was emitted.')
    A('')
    A('### The seven')
    A('')
    A('| act | what it is | grade, as its own act left it |')
    A('|---|---|---|')
    for act, what, _q, grade, _s in RESULTS:
        A('| **%s** | %s | %s |' % (act, what, grade))
    A('')
    A('### Each with its own sentence, its scope, and its obstacle')
    A('')
    obs = dict(OBSTACLES)
    for act, what, quote, grade, scope in RESULTS:
        A('- **%s — %s.** *Grade:* %s.' % (act, what, grade))
        A('  - Its own words: “…%s…”' % quote)
        A('  - **Scope, as its own act set it:** %s' % scope)
        A('  - **Obstacle, quoted:** “…%s…”' % obs[act])
    A('')
    A('### The arc’s corrections to its own readings')
    A('')
    A('| act | what was corrected | **what did not move** |')
    A('|---|---|---|')
    for act, what, notmoved in CORRECTIONS:
        A('| **%s** | %s | %s |' % (act, what, notmoved))
    A('')
    A('### Three sealed predictions, and all three failed at a normalization')
    A('')
    A('**This is one row and not three, because the shape is the same each time.** Each act '
      'derived its answer on paper, sealed it before the runner existed, and **got the count or '
      'the object right and the normalizing factor wrong.**')
    A('')
    A('| act | what was predicted | how it failed |')
    A('|---|---|---|')
    for act, what, how in PREDICTIONS:
        A('| **%s** | %s | %s |' % (act, what, how))
    A('')
    A('**What follows from it, and what does not.** It is the reason b313’s order put the '
      'normalization check before every count, and the reason that check found something. **It is '
      'not evidence that any banked value is wrong** — in all three cases the value survived and '
      'the wording did not.')
    A('')
    A('### The kernel, certified from a clone that inherited nothing')
    A('')
    A('The kernel repository was cloned fresh from `origin` at its current pin onto a path outside '
      'the corpus, with **%d compiled artefacts present before the build** — `build/` is '
      '`.gitignore`d, so there is no cache to be stale. The toolchain `elan` resolved *inside the '
      'clone* was **`%s`**, against **`%s`** outside it: the pin is observable because the two '
      'differ. **%d modules were elaborated from source in dependency order**, and '
      '`AllPrints.lean` was re-run.'
      % (cc['pre_oleans'], cc['lean_in'].split(',')[0].replace('Lean (version ', ''),
         cc['lean_out'].split(',')[0].replace('Lean (version ', ''), cc['built']))
    A('')
    A('- **Regenerated profile vs the banked blob at `HEAD`: %s on normalised bytes, %d differing '
      'lines, length difference %+d.**'
      % ('IDENTICAL' if cc['norm_same'] else 'DIFFERENT', cc['diff_lines'], cc['length_delta']))
    A('- Prints: **%d total, %d zero-axiom, %d other** — the banked blob carries %d / %d / %d.'
      % (cc['prints'][0], cc['prints'][1], cc['prints'][2],
         cc['banked_prints'][0], cc['banked_prints'][1], cc['banked_prints'][2]))
    A('- Raw-byte hazards checked rather than normalised away: byte-order mark present in the '
      'regenerated stream **%s** and in the banked blob **%s**; CRLF pairs **%d** and **%d**.'
      % (cc['raw_bom'][0], cc['raw_bom'][1], cc['raw_crlf'][0], cc['raw_crlf'][1]))
    A('')
    A('**And the coverage question the record has carried has an answer, and the answer is '
      '*found*.** %d Core modules sit outside `AllPrints.lean`, and **%d `#print axioms` targets '
      'in them are not in the certification profile at all.** The `AxiomCheck*` wrappers are '
      'redundant — their targets are certified through the parent modules — but eight shadow '
      'modules are not: `AggregationSourceShadow`, `ArchimedeanTwinShadow`, `CeilingSweepShadow`, '
      '`E2EvenMonotoneShadow`, `GeneratorSupportShadow`, `JunctionLimitShadow`, '
      '`JunctionSignShadow`, `TopLevelSilenceShadow`, together with `M4EnvelopeShadow` through its '
      'own checker.'
      % (cc['outside'], cc['uncertified']))
    A('')
    A('**The reason is structural, not accidental.** `AllPrints.lean` is a hand-maintained import '
      'list. **Nothing in the build fails when a module is left out of it** — the profile simply '
      'does not mention the module, and a profile that does not mention a module looks exactly '
      'like a profile for a corpus that does not have one. **Nothing is repaired here; the finding '
      'is filed.**')
    A('')
    A('### The arc as one statement')
    A('')
    A('At the grade these seven acts support, and no higher: **at a finite place the source’s own '
      'construction, evaluated on the object’s space, returns the test function at one point times '
      'a dimension — and carries no arithmetic at all.** The primes enter the identity through the '
      'local distribution the trace is integrated *against*, not through this trace. **The '
      'mechanism that produces that silence does not type at the archimedean place**, and the step '
      'at which it parts is the dimension of the object’s space: finite-dimensional at a finite '
      'place, so the compression is finite rank and the trace is a count; infinite at infinity, so '
      'there is no count to take. **At infinity the source’s own theorem puts the trace side at a '
      'distribution plus a remainder function** — and the corpus’s remainder is **not** that '
      'function: it differs by a factor of `ρ`, from a scaling convention the corpus declared for '
      'itself, **and correcting it accounts for between 8% and 19% of the corpus’s residue and no '
      'more.**')
    A('')
    A('**Scope, printed beside it.** This is a summary of seven acts at their own grades. '
      '**Nothing about the identity, `h2`, or the complete roster follows from it.** The finite '
      'result is about one object in one compression; the archimedean statements are IMPORTS at '
      'the import bar and **no proof of the source’s was verified by this seat**; the residue’s '
      'remaining share is **owed**, and the hypothesis that the corpus’s archimedean instruments '
      'compute with vectors lying outside the object’s own space is **named here as a hypothesis '
      'and is not tested by any act in this arc.** **`M-2` is owed and no aggregation is stated.**')
    A('')
    A('### What this arc leaves open')
    A('')
    A('- **`M-2`** — `(SPECIFIED-NOT-STATED)`, unchanged across all seven acts.')
    A('- **The object stands on three conditions**, each typed: a premise (the level limit, b198), '
      'a ruling (`W-ORD-ARCH-NORM-READING`), a construction (C9 / `N-OPEN-B`). '
      '**A condition discharged is not the object constructed.**')
    A('- **The truncation nobody owns** — an archimedean instrument on the object’s own space '
      'needs one, and the only eigenvectors the corpus has there were derived *not* to be in the '
      'space. This is the central cost, priced at b311 and not paid.')
    A('- **The calibration read** — the archimedean term’s sign is fixed *by the E2 calibration* '
      'and the atlas disclaims any sign claim. Until a derived sign exists, `A + E2` cannot be '
      'told from its own calibration (`W-ORD-A-PLUS-E2`).')
    A('- **The rate re-derivation** — the even sector’s decay moves by one full power under the '
      'source’s convention while the leading constant does not move at all; what that does to the '
      'readings built on the banked rate is not decided here.')
    A('- **`W-ORD-CONVENTION-SWEEP`** — two of five convention sites already carried the source’s '
      'exponent; nobody has swept the instrument for others.')
    A('- **Kernel coverage** — the terminals above, compiled or compilable and never certified.')
    A('- **The seam’s debt item 1** — **still unpaid.** Restated, not discharged.')
    A('- **The patent lane** — carried on the patent seat’s report, **unconfirmed on this seat’s '
      'record.**')
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
    rec('b314 -- THE FOLD, b307-b313. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)

    text_by_act = {}
    for act in ARC:
        text_by_act[act] = io.open(os.path.join(D, SRC[act]), encoding='utf-8').read()
    rec('  source files opened : %d  (every quotation checked against the act that ORIGINATED it)'
        % len(text_by_act))

    ok_q = fquote(text_by_act, rec)
    ok_c = fcount(rec)

    ccpath = os.path.join(D, 'b314_coldclone_rows.json')
    if not os.path.exists(ccpath):
        rec('  ### THE COLD-CLONE RESULT IS NOT PRESENT -- REFUSING TO EMIT A SECTION THAT')
        rec('  ### DESCRIBES A CERTIFICATION THAT HAS NOT RUN.')
        return 1
    cc = json.load(io.open(ccpath, encoding='utf-8'))
    rec('  cold-clone rows read : %s  (norm_same=%s, uncertified=%s)'
        % (os.path.basename(ccpath), cc['norm_same'], cc['uncertified']))

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
        io.open(os.path.join(D, 'b314_fold_run.txt'), 'w', encoding='utf-8',
                newline='\n').write('\n'.join(out) + '\n')
        return 1

    md = emit_markdown(cc)
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
    kpaths = [x for x in ks if 'keystone' in x.lower() or '/method/' in x.replace('\\', '/')]
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
    rec('  F-NOSHADOW   (nothing built in either tracked repo)            : ### **%s**'
        % ('DID NOT FIRE' if ok_s else 'FIRED'))
    rec('=' * 100)

    json.dump(dict(arc=ARC, results=len(RESULTS), obstacles=len(OBSTACLES),
                   corrections=len(CORRECTIONS), predictions=len(PREDICTIONS),
                   findings_added=added, findings_removed=removed, f_quote=ok_q,
                   f_count=ok_c, f_nograde=ok_g, f_nokeystone=ok_k, f_noshadow=ok_s),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    io.open(os.path.join(D, 'b314_fold_run.txt'), 'w', encoding='utf-8',
            newline='\n').write('\n'.join(out) + '\n')
    return 0 if (ok_q and ok_c and ok_g and ok_k and ok_s) else 1


if __name__ == '__main__':
    sys.exit(main())
