# -*- coding: utf-8 -*-
"""b299_keystone.py -- THE ARC KEYSTONE. ### THE GENERATOR.

### **A WRITING ACT. ### NO NEW MATHEMATICS. ### NO GRADE MOVES. ### NO ACT RE-VERDICTED.
### NO DEPOSITED TEXT TOUCHED.** ### Every bar was fixed in
### `data/b299_registration_2026-09-02.txt`, SEALED `78d45c6f...`, term-scanned and
### satisfiability-checked BEFORE the seal.

### ### **THE DESIGN POINT, CARRIED FROM b266 THROUGH b282, b297:**
### ### **THE CLAIM TABLE BELOW IS THE SINGLE SOURCE OF TRUTH AND THIS RUNNER ### EMITS ### THE
### ### DOCUMENT.** ### A claim whose quotation cannot be verified verbatim against the act that
### ### ORIGINATED it never reaches the document at all.

### ### **AND THIS TOOL EXISTS FOR A SECOND REASON, WHICH IS THE ACT'S OWN CONSTRAINT:**
### ### **`W-ORD-ADHOC-CHECK-FIXTURES` (b298) FORBIDS THIS ACT FROM REPORTING ANY NUMBER TYPED AT
### ### A SHELL.** ### So every count the bank quotes is printed here, by a committed tool that
### carries fixtures -- including the additive diff, the deposited-path guard, and the title check.

### ### ==========================================================================================
### ### **THE REGENERATION (b299, second pass). ### THE AUTHOR STRUCK A CLAUSE THIS TOOL APPLIED.**
### ### ==========================================================================================
### ### **STRUCK, BY THE AUTHOR, BY PASTE:** ### the title law's PROPERTY half. ### **ONLY THE
### ### NUMERAL HALF STANDS** -- a numeral appears in a title when the numeral is itself the
### ### finding. ### The record is `data/STRUCK_CLAUSES.md`, entry ### **S-1**.
### ### **WHAT THE FIRST PASS DID WITH IT, AT THREE SITES, ALL THREE NOW GONE:**
###   ### (1) ### **IN `q_title`** -- a `banned` word list that REJECTED a property-claiming
###       title. ### **THE ARM IS REMOVED, NOT WIDENED.** ### The numeral arm and its fixture stay.
###   ### (2) ### **IN THE TITLE** -- the subtitle *"the arc's objects, with their grades and
###       their scopes"* was the clause's own words carried into the title to demonstrate
###       compliance with it. ### **REMOVED.**
###   ### (3) ### **IN THE DOCUMENT** -- a claim row quoting `FINDINGS.md`'s `F.2026-07-29` and a
###       scope sentence asserting the title *"claims no achieved property"*. ### **REMOVED**, and
###       `FINDINGS.md` is no longer opened, because no claim quotes it any more.
### ### **AND A GATE REPLACES THE CLAUSE RATHER THAN INHERITING IT: ### `Q-STRUCK` SCANS THE
### ### TITLE, THE DOCUMENT AND BOTH POINTERS AGAINST THE STRUCK RECORD, WITH A DISCRIMINATION
### ### ARM.** ### A gate that can only ever return zero is not a gate.
### ### **THE SEAL IS NOT EDITED.** ### `data/b299_registration_2026-09-02.txt` fixed the struck
### ### clause as `Q-TITLE` before the author struck it, and it stays sealed exactly as it is.
### ### **THE DOCUMENT FOLLOWS THE AUTHOR'S RULING OVER THE REGISTRATION'S WORDING**, and the
### ### bank declares the conflict rather than quietly resolving it.
"""
import io
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ferry_scan  # noqa: E402  ### the struck record is READ, never restated here

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROOT = r'D:\relay'
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
METHOD = os.path.join(PP, 'phase2', 'method')
DOCNAME = 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'
DOC = os.path.join(METHOD, DOCNAME)
GLOBAL = os.path.join(METHOD, 'THE_GLOBAL_SECTION.md')
CHAIN = os.path.join(METHOD, 'THE_IDENTITY_CHAIN.md')
README = os.path.join(PP, 'README.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
SIGNARR = os.path.join(METHOD, 'SIGN_ARRANGEMENT_RECONCILIATION.md')
ROWS = os.path.join(D, 'b299_rows.json')
RUNLOG = os.path.join(D, 'b299_keystone_run.txt')

# ### **THE TITLE, REGENERATED.** ### The first pass appended *"-- the arc's objects, with their
# ### grades and their scopes"*, which is the STRUCK clause's own wording carried into the title
# ### to demonstrate compliance with it. ### **THE APPENDAGE IS GONE AND NOTHING REPLACES IT.**
# ### ### **WHAT STILL GOVERNS: THE NUMERAL HALF ONLY.** ### `two-radius` is the arc's own name
# ### for the object (b293's *"finite two-radius family"*), not a count this act found; and it
# ### carries no numeral in the sense the surviving law means, which `q_title` measures.
TITLE = 'The two-radius family and the annihilation boundary'

SRC = {
    'b284': 'b284_the_scalings_domain.txt',
    'b285': 'b285_archimedean_opening.txt',
    'b286': 'b286_the_cc_condition.txt',
    'b288': 'b288_the_family_and_the_complement.txt',
    'b291': 'b291_the_involution.txt',
    'b292': 'b292_the_identification.txt',
    'b293': 'b293_the_finite_family.txt',
    'b294': 'b294_the_family_value.txt',
    'b295': 'b295_the_second_mechanism.txt',
    'b296': 'b296_the_asymmetry.txt',
    'b297': 'b297_the_fold.txt',
    'b298': 'b298_the_boundary_terminal.txt',
}
# ### FILES OUTSIDE relay/data THAT ARE THEMSELVES EMITTERS OF A SENTENCE THIS DOCUMENT QUOTES.
# ### ### **`FINDINGS.md` WAS HERE AND IS NOT ANY MORE.** ### It was opened for exactly one claim
# ### -- the title law's struck half -- and that claim is gone. ### **A SOURCE OPENED FOR NO
# ### CLAIM IS A SOURCE THE RUN LOG COUNTS AND THE DOCUMENT DOES NOT USE**, which reads as
# ### breadth the act does not have.
EXT = {
    'README': README,
    'SIGNARR': SIGNARR,
}

# ### (group, act, quotation, grade-as-its-act-left-it, scope sentence)
# ### ### **EVERY QUOTATION IS CHECKED VERBATIM AGAINST ITS OWN EMITTER BEFORE EMISSION.**
CLAIMS = [
    # --- (i) THE FINITE TWO-RADIUS FAMILY ---
    ('i', 'b293', 'THE FAMILY IS CONSTRUCTED.',
     '**CONSTRUCTED**',
     'In the corpus\u2019s own `p`-adic terms and at its own level indexing.'),
    ('i', 'b293', 'DIMENSION `(p^n - p^a)(p^n - p^b)`, DERIVED AND VERIFIED WITH ZERO MISMATCHES.',
     '**DERIVED**',
     'Claimed only where it was tested: `a + b >= 0` with both exponents non-negative. '
     'At `a = b = 0` it is the keystone\u2019s own `(p^n-1)^2`.'),
    ('i', 'b293', 'CHECKED VECTOR BY VECTOR',
     '**VERIFIED**, not asserted',
     'The corpus\u2019s existing space is the diagonal member `(0,0)` \u2014 checked in BOTH '
     'directions, with a negative control that rejects an off-ball spike.'),
    ('i', 'b293', 'set equality, not containment',
     '**SET EQUALITY**',
     'The two directions together; a containment in one direction would not have been the '
     'identification.'),
    ('i', 'b293', 'THE SUM `a+b` IS INVARIANT',
     '**DERIVED**',
     'From the corpus\u2019s own conditions and its own valuation. The archimedean analogue is '
     'named as an analogue and is never used as a reason.'),
    ('i', 'b293', 'THE FAMILY EXISTS.',
     'the act\u2019s own standing sentence',
     '**A family existing is not a route existing.**'),

    # --- (ii) THE ARCHIMEDEAN FAMILY, READ AT ITS SOURCE ---
    ('ii', 'b286', 'THE SPACE IS `L^2(R)_ev`.',
     '**(SUPPLIED BY SOURCE)** \u2014 an import, graded as one',
     'Two conditions, cutoff `[-1,1]` at `Lambda = 1`. Nothing adopted, nothing constructed.'),
    ('ii', 'b288', 'COMPONENT 1 -- VERDICT: THE PRODUCT IS INVARIANT.',
     '**INVARIANT**',
     'The dilation is a flow on the product\u2019s level sets.'),
    ('ii', 'b288', 'STABILIZER IS TRIVIAL',
     'a **stabilizer** statement',
     'Non-preservation of one member is not the absence of an action.'),
    ('ii', 'b291', '`F_eR : S(lambda,mu) -> S(mu,lambda)`',
     '**DERIVES-on-IMPORT**',
     'The import being the source\u2019s own sentence that the transform is its own inverse on '
     'the even space \u2014 stated in plain English, where an earlier symbolic search did not '
     'reach it.'),
    ('ii', 'b291', "(ii) THE CORPUS'S ARCHIMEDEAN MEMBER IS SELF-DUAL.",
     'immediate from the reflection',
     'At `lambda = mu = 1`: the corpus\u2019s member is the self-dual point of its own orbit.'),
    ('ii', 'b285', 'NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`.',
     '**the arc\u2019s standing boundary**',
     'Carried by every act after it. The archimedean space is **(NAMED-NOT-CONSTRUCTED)** in the '
     'corpus\u2019s own register.'),

    # --- (iii) THE ANNIHILATION CRITERION ---
    ('iii', 'b295', '`a >= 0`  ###  OR  ###  `b >= n - 1`',
     '**DERIVED** (sufficiency)',
     'Vanishing as a **form**, in both slots, at every finite place and every level. '
     'A statement about one pairing of one shape.'),
    ('iii', 'b296', 'THE THRESHOLD FALLS OUT',
     '**DERIVED, not fitted**',
     'The reading scale was measured with no reference to `b`, both polarities firing, at six '
     'cells. What remains measured and not derived is that the derivation and the measurement '
     'agree outside those cells.'),
    ('iii', 'b296', 'EACH THRESHOLD IS THE DISTANCE FROM',
     '**ONE RULE, TWO NUMBERS**',
     'Distance `0` on the function side, level-free; `n-1` on the transform side, level-carrying. '
     'The asymmetry is between the two ways the operator reads its two slots, not between the '
     'object\u2019s two conditions.'),
    ('iii', 'b296', 'IF AND ONLY IF',
     '**EQUIVALENCE** \u2014 necessity derived, not measured',
     'Necessity witnessed by one vector per cell, each hypothesis used exactly once in the '
     'construction.'),
    ('iii', 'b296', 'THE ANNIHILATION IS ONE-SIDED',
     '**MEASURED**, on two spaces built outside the family\u2019s index range',
     'On the object\u2019s own space the function-side condition does the work at every level; '
     'above level 1 the object\u2019s second condition contributes nothing **to this pairing**, '
     'and this arc tested no other purpose.'),
    ('iii', 'b294', "THE BARRIER'S ZERO IS A PROPERTY OF A SUB-FAMILY",
     'its twenty measurements **stand**',
     '**Its member-level reading of them was corrected at b295 \u2014 a correction to a fact, not '
     'a re-verdict.** The form is neither Hermitian nor symmetric, so a diagonal on one basis does '
     'not decide a span.'),

    # --- (iv) THE PLACEMENT OF THE ARCHIMEDEAN INSTRUMENTS ---
    ('iv', 'b292', 'VERDICT: (SAME OBJECT), UP TO A NONZERO SCALAR',
     '**(SAME OBJECT)**',
     'Derived from two defining equations that are one equation in two notations. The resemblance '
     'between the two constructions was named and refused first, and appears nowhere in the '
     'derivation.'),
    ('iv', 'b292', '`zeta_n` IS NOT IN `S(1,1)`',
     'the refutation reaches the corpus\u2019s own instruments',
     'The corpus\u2019s archimedean instrument vectors lie **outside** the object\u2019s space.'),
    ('iv', 'b292', 'AND NO MEASUREMENT IS DISTURBED.',
     '**no measurement disturbed**',
     'Every banked number stands. Nothing about the identity, `h2`, or the complete roster '
     'follows.'),

    # --- WHAT IS MACHINE-CHECKED, AND WHAT IS NOT ---
    ('v', 'b298', 'boundary_value_at_cell_2_2_on_member_radii_neg1_0',
     '**MACHINE-CHECKED**, zero axioms',
     'One cell. The terminal names the cell and the radii in its own statement, and decides that '
     'the object\u2019s own space rejects the witness. **The pair with the function-side terminal '
     'certifies sharpness at that cell, not the equivalence in general.**'),
    ('v', 'b298', 'STILL REFUSED',
     'the refusal list, restated',
     'One candidate passing does not open the others.'),
    ('v', 'b297', 'EVERYTHING ANALYSIS-BOUND',
     '**NOT machine-verified**',
     'The closure step is standard analysis and remains the chain\u2019s one uncompiled link.'),
    ('v', 'b284', 'ESCAPED MASS FOLDED BACK IN',
     'a standing hazard',
     'Everything exposed to the model\u2019s escaped-mass artifact is refused: a compiled terminal '
     'over the truncated model would certify the truncation and carry the object\u2019s name.'),

    # --- WHAT NONE OF IT SAYS ---
    ('vi', 'b296', 'M-2 REMAINS (SPECIFIED-NOT-STATED)',
     '**UNCHANGED**',
     'Untouched by every act of this arc.'),
    ('vi', 'README', 'Not supportable: *RH proved.*',
     'the deposit\u2019s ceiling, quoted from its own file',
     'Nothing in this document reaches it, approaches it, or is evidence toward it.'),
    # ### **A ROW STOOD HERE QUOTING `FINDINGS.md`'s TITLE LAW `F.2026-07-29`, WITH A SCOPE
    # ### SENTENCE ASSERTING THAT THIS DOCUMENT'S TITLE "CLAIMS NO ACHIEVED PROPERTY".**
    # ### ### **THE AUTHOR STRUCK THAT CLAUSE. ### THE ROW IS REMOVED AND NOTHING REPLACES IT**
    # ### -- see `data/STRUCK_CLAUSES.md` S-1. ### The corpus's own `F.2026-07-29` line is left
    # ### exactly as it stands: the append-only law governs, and reconciling the ledger to the
    # ### strike is the author's, not this act's.
    ('vi', 'SIGNARR', 'frozen, errata-only',
     'the voices ruling',
     '**DEPOSIT-VOICE** texts move only by errata and a new version. **This document is '
     'SUPPORT-VOICE, at working HEAD, and amends no deposited text.**'),
]

GROUP_TITLES = {
    'i': 'The finite two-radius family',
    'ii': 'The archimedean family, read at its source',
    'iii': 'The annihilation criterion',
    'iv': 'The placement of the archimedean instruments',
    'v': 'What is machine-checked, and what is not',
    'vi': 'What none of it says',
}


# ### ==========================================================================================
# ### THE GATES. ### **EACH CARRIES A FIXTURE, BECAUSE THIS ACT MAY NOT REPORT A NUMBER A
# ### SHELL ONE-LINER PRODUCED.**
# ### ==========================================================================================
def load_sources():
    t = {}
    for act, fn in SRC.items():
        t[act] = io.open(os.path.join(D, fn), encoding='utf-8').read()
    for key, path in EXT.items():
        t[key] = io.open(path, encoding='utf-8').read()
    return t


def q_quote(texts, rec):
    bad = []
    for grp, act, quote, _g, _s in CLAIMS:
        if quote not in texts[act]:
            bad.append((grp, act, quote))
    rec('  Q-QUOTE : %d claims, %d unfindable' % (len(CLAIMS), len(bad)))
    for grp, act, quote in bad:
        rec('      ### UNFINDABLE  (%s) %s -- %s' % (grp, act, quote[:66]))
    _g0, act0, q0, _g, _s = CLAIMS[0]
    altered = q0.replace('FAMILY', 'FAMILLY')
    disc = altered not in texts[act0]
    rec('  ### DISCRIMINATION ARM: an altered quotation is reported unfindable : %s' % disc)
    return (not bad) and disc


def q_title(title, rec):
    """### **THE TITLE LAW -- ITS SURVIVING HALF ONLY, WITH BOTH POLARITIES.**

    ### ### **THE NUMERAL HALF, WHICH STANDS:** ### a numeral appears in a title only when the
    ### numeral is itself the finding. ### In this arc none is -- the finding is that a threshold
    ### MOVES WITH THE LEVEL, ### **which is a shape and not a number** -- so the title carries no
    ### numeral and this check is reachable and can fire.

    ### ### **THE PROPERTY HALF IS STRUCK (S-1) AND ITS ARM IS REMOVED FROM THIS FUNCTION.**
    ### The first pass carried a `banned` word list rejecting a property-claiming title.
    ### ### **IT IS NOT WIDENED, NOT SOFTENED AND NOT MOVED SOMEWHERE QUIETER. ### IT IS GONE**,
    ### and `Q-STRUCK` below checks that it did not reappear in the prose instead.
    """
    has_numeral = bool(re.search(r'\d', title))
    ok = not has_numeral
    # ### FIXTURE, BOTH POLARITIES. ### A check that only ever passes is not a check.
    catches = bool(re.search(r'\d', 'The 4/3 value'))
    passes = not bool(re.search(r'\d', 'The annihilation boundary'))
    rec('  Q-TITLE : numeral %-5s  -> %s   ### the numeral half only; the property half is STRUCK'
        % (has_numeral, 'PASS' if ok else '### FAIL ###'))
    rec('      fixture: a numeral title is caught: %-5s   a clean title is passed: %s'
        % (catches, passes))
    return ok and catches and passes


def q_struck(title, doc, pointers, rec):
    """### ### **Q-STRUCK -- THE GATE THAT REPLACES THE CLAUSE INSTEAD OF INHERITING IT.**

    ### Every text this act WRITES is scanned against `data/STRUCK_CLAUSES.md` through
    ### `ferry_scan.scan_text`. ### The record is READ, never restated here, so a clause struck
    ### later moves this gate without an edit.
    ### ### **AND THE DISCRIMINATION ARM: ### A SYNTHETIC TEXT CARRYING THE CLAUSE MUST COME BACK
    ### WITH HITS.** ### A scanner that reports zero on everything reports zero on the document
    ### too, and the two zeroes look identical.
    """
    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    targets = [('the title', title), ('the document', doc)]
    targets += [('pointer: %s' % k, v) for k, v in pointers]
    total = 0
    rec('  Q-STRUCK : record %s -- %d struck entr%s, %d UNCONFIRMED not loaded'
        % (os.path.basename(ferry_scan.RECORD), len(struck),
           'y' if len(struck) == 1 else 'ies', unconf))
    for label, text in targets:
        ch, _sh = ferry_scan.scan_text(text, struck, stem_list)
        total += len(ch)
        rec('      %-28s struck-clause hits : %d  %s'
            % (label, len(ch), 'PASS' if not ch else '### FAIL ###'))
        for lbl, i, c, line in ch:
            rec('          line %d col %d  %s' % (i, c, lbl))
            rec('              %s' % line[:96])
    synth = 'a title must name its objects and conditions, not claim an achieved property'
    disc = bool(ferry_scan.scan_text(synth, struck, stem_list)[0])
    rec('      ### DISCRIMINATION ARM: a text carrying the struck clause comes back hit : %s'
        % disc)
    return (total == 0) and disc and bool(struck)


def numstat(repo, path):
    p = subprocess.run(['git', '-C', repo, 'diff', '--numstat', 'HEAD', '--', path],
                       capture_output=True, text=True)
    if not p.stdout.strip():
        return 0, 0
    parts = p.stdout.split()
    return int(parts[0]), int(parts[1])


def q_nodeposit(rec):
    """### **ZERO FILES TOUCHED UNDER A DEPOSITED PATH.** ### The deposited records live under
    `outputs/DEPOSITED-*`; the two keystones and the new document are working-HEAD support layer."""
    p = subprocess.run(['git', '-C', PP, 'status', '--short'], capture_output=True, text=True)
    touched = [l[3:].strip() for l in p.stdout.splitlines() if l.strip()]
    dep = [t for t in touched if 'DEPOSITED' in t.upper() or '/outputs/' in ('/' + t)]
    rec('  Q-NODEPOSIT : files touched %d, of which under a deposited path : %d  %s'
        % (len(touched), len(dep), 'PASS' if not dep else '### FAIL ### %s' % dep))
    return not dep


def emit_document(texts):
    ceiling = 'Not supportable: *RH proved.*'
    L = []
    A = L.append
    A('# %s' % TITLE)
    A('')
    A('**DOCUMENT CLASS \u2014 THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): '
      '### TIER C** \u2014 *declared 2026-09-02 (b299); basis: it states results whose terminals '
      'and grades are their owning acts\u2019, and confers none of its own.* '
      '### **PRIVATE.** ### **SUPPORT-VOICE** \u2014 the support layer at working HEAD. '
      '### **ARC KEYSTONE \u2014 not a synthesis.**')
    A('')
    A('---')
    A('')
    A('## \u00a71 \u2014 Its place in the corpus')
    A('')
    A('### **THIS DOCUMENT AMENDS NOTHING AND CLAIMS NOTHING.** It states what one arc built, at '
      'the grades its own acts left, with each result\u2019s scope printed beside it. Every '
      'sentence of substance below is a **quotation**, verified verbatim against the act that '
      '**originated** it by the runner that **generated this document** \u2014 '
      '`relay/tools/b299_keystone.py`. A check that runs after the writing can only report a '
      'paraphrase; one that generates the writing cannot emit one.')
    A('')
    A('### **IT STANDS UNDER THE REGISTER SENTENCE, AND UNDER THE DEPOSIT\u2019S CEILING, WHICH '
      'IS QUOTED HERE RATHER THAN SUMMARISED** (`README.md`, its own file):')
    A('')
    A('> *"%s"* The open clause is a premise of the multiplicative structure, undischarged, and '
      'the corpus names it openly at every site that depends on it.' % ceiling)
    A('')
    A('### **NOTHING BELOW REACHES THAT CEILING, APPROACHES IT, OR IS EVIDENCE TOWARD IT.** '
      'Nothing below is a route. Nothing below states an aggregation. **M-2 is owed.**')
    A('')
    A('### **AND ON ITS OWN STATUS:** the voices ruling governs \u2014 **DEPOSIT-VOICE** texts are '
      '*"frozen, errata-only"* and **move only by errata and a new version**. '
      '**This document is SUPPORT-VOICE, at working HEAD. It touches no deposited text, and it is '
      'not one.**')
    A('')
    A('**The acts it draws on:** `b284`, `b285`, `b286`, `b288`, `b291`, `b292`, `b293`, `b294`, '
      '`b295`, `b296`, `b297`, `b298` \u2014 the arc `b283\u2013b296` and the two filing acts that '
      'followed it. Their banks are in `relay/data/`, and the arc is folded as one section of '
      '`FINDINGS.md`.')
    A('')
    for g in ['i', 'ii', 'iii', 'iv']:
        rows = [c for c in CLAIMS if c[0] == g]
        A('---')
        A('')
        A('## \u00a7%d \u2014 %s' % (['i', 'ii', 'iii', 'iv'].index(g) + 2, GROUP_TITLES[g]))
        A('')
        A('| result, quoted from its owning act | grade as its act left it | its scope |')
        A('|:--|:--|:--|')
        for _g, act, quote, grade, scope in rows:
            A('| **%s** \u2014 *"%s"* | %s | %s |'
              % (act, quote.replace('|', '\\|'), grade, scope.replace('|', '\\|')))
        A('')
    A('---')
    A('')
    A('## \u00a76 \u2014 %s' % GROUP_TITLES['v'])
    A('')
    A('| result, quoted from its owning act | grade as its act left it | its scope |')
    A('|:--|:--|:--|')
    for _g, act, quote, grade, scope in [c for c in CLAIMS if c[0] == 'v']:
        A('| **%s** \u2014 *"%s"* | %s | %s |'
          % (act, quote.replace('|', '\\|'), grade, scope.replace('|', '\\|')))
    A('')
    A('### **THE REFUSAL LIST, AND ITS REASON, WHICH IS ONE REASON AND NOT FOUR:**')
    A('')
    A('- The family\u2019s **definition and dimension law**, and the **diagonal identification** '
      'as set equality \u2014 both finite-decidable at a cell, both **REFUSED**: a terminal '
      'certifying either at one cell reads as the general law.')
    A('- The **transform-side fiber-sum collapse** at the reading scale \u2014 **REFUSED** on the '
      'same ground.')
    A('- Everything **analysis-bound**, and everything exposed to the **escaped-mass artifact**.')
    A('')
    A('### ### **THE SENTENCE THAT GOVERNS ALL OF THEM: MOST OF THIS ARC\u2019S CONTENT IS '
      'SCOPED, AND IS THEREFORE UNCOMPILABLE WITHOUT LOSING ITS SCOPE.** A terminal carries its '
      'statement and nothing else. Where a result quantifies over all levels and all places \u2014 '
      'which the criterion and the equivalence both do \u2014 a terminal at one cell would sit in '
      'the kernel **looking like the general statement**. The one candidate that was built is the '
      'one whose terminal **names its member in its own statement**, so the scope travels with it.')
    A('')
    A('---')
    A('')
    A('## \u00a77 \u2014 %s' % GROUP_TITLES['vi'])
    A('')
    A('| result, quoted from its owning act | grade as its act left it | its scope |')
    A('|:--|:--|:--|')
    for _g, act, quote, grade, scope in [c for c in CLAIMS if c[0] == 'vi']:
        A('| **%s** \u2014 *"%s"* | %s | %s |'
          % (act, quote.replace('|', '\\|'), grade, scope.replace('|', '\\|')))
    A('')
    A('### **NOTHING ABOUT THE IDENTITY. NOTHING ABOUT `h2`** beyond the register sentence exact. '
      '**NOTHING ABOUT THE COMPLETE ROSTER.** **NO ROUTE IS CLAIMED**, and the members carrying a '
      'nonzero value are reached by **relaxing the object\u2019s own first condition**, not by any '
      'map the corpus states \u2014 every witness has mass **on the ball**, which that condition '
      'forbids outright.')
    A('')
    A('---')
    A('')
    A('## \u00a78 \u2014 Placement')
    A('')
    A('**Path:** `phase2/method/%s`. **Class:** TIER C, PRIVATE, SUPPORT-VOICE, arc keystone. '
      '**Voice:** support, at working HEAD.' % DOCNAME)
    A('')
    A('**Cross-references, appended and not rewritten:** `THE_GLOBAL_SECTION.md` and '
      '`THE_IDENTITY_CHAIN.md` each carry a pointer line to this document. '
      '**No existing sentence in either was edited and no grade in either was moved.**')
    A('')
    A('**Correspondence:** the arc\u2019s terminals and refusals are rowed in '
      '`SIDE-global-section/CORRESPONDENCE.md`; the boundary pair is rows 112\u2013113.')
    A('')
    A('*The results above are their owning acts\u2019. This document states grades and confers '
      'none.*')
    A('')
    return '\n'.join(L)


POINTER_GLOBAL = (
    '\n> ### **ARC KEYSTONE, APPENDED 2026-09-02 (b299) \u2014 pointer only; nothing above is '
    'edited and no grade is moved.** The arc `b283\u2013b296` built a **finite two-radius family** '
    '`Son(p,n; a,b)` of which **this document\u2019s `Son(p,n)` is the diagonal member `(0,0)`**, '
    'verified by set equality in both directions (b293); and it derived that the first-level '
    'pairing vanishes on a member **if and only if** `a >= 0` or `b >= n-1` \u2014 so **this '
    'space\u2019s two defining conditions are not read the same way by that operator** (b295, '
    'b296). Stated with grades and scopes in '
    '`phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md`.\n')

POINTER_CHAIN = (
    '\n> ### **ARC KEYSTONE, APPENDED 2026-09-02 (b299) \u2014 pointer only; nothing above is '
    'edited and no grade is moved.** The barrier terminals this document cites now have a **second '
    'side in the kernel at one cell**: `B270.absorb_2_2` (function side) and '
    '`B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0` (the relaxed member), both printing '
    'at zero axioms. **The pair certifies sharpness at that cell, not the equivalence in '
    'general.** Stated with grades and scopes in '
    '`phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md`.\n')


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b299 -- THE ARC KEYSTONE. ### THE GENERATOR, NOT A REVIEW.')
    rec('=' * 100)

    texts = load_sources()
    rec('  source files opened : %d  (%d banks + %d corpus emitters)'
        % (len(texts), len(SRC), len(EXT)))

    ok_q = q_quote(texts, rec)
    ok_t = q_title(TITLE, rec)

    md = emit_document(texts)
    ok_s = q_struck(TITLE, md,
                    [('THE_GLOBAL_SECTION.md', POINTER_GLOBAL),
                     ('THE_IDENTITY_CHAIN.md', POINTER_CHAIN)], rec)

    if not (ok_q and ok_t and ok_s):
        rec('')
        rec('  ### ### **NOTHING EMITTED. ### A GATE FIRED AND THE DOCUMENT IS NOT WRITTEN.**')
        rec('=' * 100)
        with io.open(RUNLOG, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(out) + '\n')
        return 1

    # ### **THE IDEMPOTENCE GUARD, REBUILT AT THE REGENERATION.** ### The first pass guarded on
    # ### EXISTENCE ALONE: `if os.path.exists(DOC): NOT REWRITTEN`. ### **UNDER AN ORDER TO
    # ### REGENERATE, THAT GUARD SILENTLY KEEPS THE OLD DOCUMENT AND REPORTS A CLEAN RUN** -- the
    # ### one file the act exists to change is the one it would refuse to touch, and every gate
    # ### below would then be measuring the PREVIOUS emission. ### **IT NOW COMPARES BYTES AND
    # ### SAYS WHICH OF THE THREE CASES IT IS.**
    prev = io.open(DOC, encoding='utf-8').read() if os.path.exists(DOC) else None
    if prev is None:
        io.open(DOC, 'w', encoding='utf-8', newline='\n').write(md)
        rec('  document write : CREATED')
    elif prev == md:
        rec('  document write : IDENTICAL to what is on disk -- not rewritten')
    else:
        io.open(DOC, 'w', encoding='utf-8', newline='\n').write(md)
        rec('  document write : ### REGENERATED -- the bytes on disk differed and were replaced')
    rec('  document : %s' % DOCNAME)
    rec('  document lines : %d   bytes : %d' % (len(md.splitlines()), len(md.encode('utf-8'))))

    # ### THE POINTERS -- APPEND-ONLY, EACH WITH ITS OWN IDEMPOTENCE GUARD.
    for path, ptr, label in [(GLOBAL, POINTER_GLOBAL, 'THE_GLOBAL_SECTION.md'),
                             (CHAIN, POINTER_CHAIN, 'THE_IDENTITY_CHAIN.md')]:
        cur = io.open(path, encoding='utf-8').read()
        if 'ARC KEYSTONE, APPENDED 2026-09-02 (b299)' in cur:
            rec('  pointer in %-28s : ALREADY PRESENT, nothing written' % label)
        else:
            io.open(path, 'a', encoding='utf-8', newline='\n').write(ptr)
            rec('  pointer in %-28s : appended' % label)

    # ### Q-NOGRADE -- PURELY ADDITIVE, MEASURED.
    rec('')
    tot_add, tot_del = 0, 0
    for path, label in [(GLOBAL, 'THE_GLOBAL_SECTION.md'), (CHAIN, 'THE_IDENTITY_CHAIN.md')]:
        a, d = numstat(PP, os.path.relpath(path, PP).replace('\\', '/'))
        tot_add += a
        tot_del += d
        rec('  Q-NOGRADE %-28s : +%d / -%d' % (label, a, d))
    rec('  Q-NOGRADE TOTAL across existing files : +%d / -%d   %s'
        % (tot_add, tot_del,
           'DID NOT FIRE -- purely additive' if tot_del == 0 else '### FIRED ###'))
    ok_g = (tot_del == 0)

    ok_d = q_nodeposit(rec)

    # ### Q-VOICE -- the class line first, and the ceiling quoted.
    body = io.open(DOC, encoding='utf-8').read()
    first_nonblank = [l for l in body.splitlines() if l.strip()][:2]
    voice_ok = ('SUPPORT-VOICE' in first_nonblank[1] and 'ARC KEYSTONE' in first_nonblank[1]
                and 'PRIVATE' in first_nonblank[1] and 'TIER' in first_nonblank[1])
    ceiling_ok = 'Not supportable: *RH proved.*' in body
    errata_ok = 'move only by errata and a new version' in body
    rec('  Q-VOICE : class line is the first line after the title : %-5s' % voice_ok)
    rec('            deposit ceiling quoted verbatim : %-5s   errata sentence present : %s'
        % (ceiling_ok, errata_ok))

    rec('')
    rec('=' * 100)
    rec('  Q-QUOTE      : ### **%s**' % ('DID NOT FIRE' if ok_q else 'FIRED'))
    rec('  Q-TITLE      : ### **%s**' % ('DID NOT FIRE' if ok_t else 'FIRED'))
    rec('  Q-STRUCK     : ### **%s**' % ('DID NOT FIRE' if ok_s else 'FIRED'))
    rec('  Q-NOGRADE    : ### **%s**' % ('DID NOT FIRE' if ok_g else 'FIRED'))
    rec('  Q-NODEPOSIT  : ### **%s**' % ('DID NOT FIRE' if ok_d else 'FIRED'))
    rec('  Q-VOICE      : ### **%s**'
        % ('DID NOT FIRE' if (voice_ok and ceiling_ok and errata_ok) else 'FIRED'))
    rec('  claims by group : ' + ', '.join(
        '%s=%d' % (g, len([c for c in CLAIMS if c[0] == g]))
        for g in ['i', 'ii', 'iii', 'iv', 'v', 'vi']))
    rec('=' * 100)

    json.dump(dict(claims=len(CLAIMS), unfindable=0, doc_lines=len(md.splitlines()),
                   doc_bytes=len(md.encode('utf-8')), sources_opened=len(texts),
                   keystone_added=tot_add, keystone_deleted=tot_del,
                   q_quote=ok_q, q_title=ok_t, q_struck=ok_s, q_nograde=ok_g, q_nodeposit=ok_d,
                   q_voice=bool(voice_ok and ceiling_ok and errata_ok)),
              io.open(ROWS, 'w', encoding='utf-8'), indent=1)
    with io.open(RUNLOG, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if (ok_q and ok_t and ok_s and ok_g and ok_d
                 and voice_ok and ceiling_ok and errata_ok) else 1


if __name__ == '__main__':
    sys.exit(main())
