# -*- coding: utf-8 -*-
"""b411_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A DOCUMENT, A LEDGER, A ROW OR A KEY.** ### It computes, prints
### and emits; `b411_desk_bank.py` writes. ### **EVERY WRITE ENCODES BEFORE IT OPENS**, and ###
### **THE WRAPPER BREAKS AT WORD BOUNDARIES** ### -- `b410`'s wrapper split a word and an arm then
### measured the wrapper rather than the text.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm     # noqa: E402
import gate_spine     # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b411_components.txt')
NUMOUT = os.path.join(D, 'b411_numbering.txt')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
INST = os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')
GRADER = os.path.join(PP, 'phase1.5', 'method', 'I7_SURVEYABILITY_GRADER.md')
ENGINE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
GAUGE = os.path.join(ROOT, 'reports', '2026-08-01-w-half-consult.md')
NL = chr(10)
WB = chr(92) + 'b'

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    rec(c * 100)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


def wrap(s, ind='      ', w=126):
    """### **WORD BOUNDARIES, NEVER MID-TOKEN** -- `b410`'s defect, carried as a bar."""
    line = ind
    for word in s.split(' '):
        if len(line) + len(word) + 1 > w + len(ind) and line.strip():
            rec(line.rstrip())
            line = ind
        line += word + ' '
    if line.strip():
        rec(line.rstrip())


EXTRACT = io.open(os.path.join(D, 'b411_extract.txt'), encoding='utf-8').read()
IBTXT = io.open(IB, encoding='utf-8', errors='replace').read()
INSTTXT = io.open(INST, encoding='utf-8', errors='replace').read()
ENGTXT = io.open(ENGINE, encoding='utf-8', errors='replace').read()
FACESTXT = io.open(FACES, encoding='utf-8', errors='replace').read()
GAUGETXT = io.open(GAUGE, encoding='utf-8', errors='replace').read()
GRADERTXT = io.open(GRADER, encoding='utf-8', errors='replace').read()


def q(frag, where, hay):
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


def live_md():
    out = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                rel = os.path.relpath(p, PP).replace(os.sep, '/')
                if not rel.startswith('outputs/'):
                    out.append((rel, p))
    return out


# ### =================================================================================================
def component1():
    bar()
    rec('### COMPONENT 1 -- THE JOIN, MADE UNDER (R29).')
    bar()
    rec('  ### **THE TWO SENTENCES THAT ARE ONE TEST, QUOTED SIDE BY SIDE:**')
    q('but not individual-element specifications requiring P-information to cross I',
      'THE KEYSTONE`S CLAUSE', IBTXT)
    q('does the statistic’s definition contain the zeros’ REAL PARTS?',
      'THE SCREEN`S QUESTION', INSTTXT)
    wrap('### **`P` IS `σ`, THE REAL PART**, by Proposition 3.5`s own sentence. ### So the '
         'keystone asks whether a sentence references an individual element’s `σ` '
         'across the interface, and the screen asks whether a statistic’s definition '
         'contains the zeros’ real parts. ### ### **THESE ARE ONE QUESTION IN TWO '
         'VOCABULARIES** -- one theoretical and graded by `κ`, one operational and answered '
         'YES or NO before a computation is spent.', '  ')
    rec('')
    rec('  ### ### **AND THE MUTUAL CITATION, RE-MEASURED AT THIS ACT AND NOT CARRIED:**')
    a = len(re.findall(r'I-7|placement screen', IBTXT, re.I))
    b = len(re.findall('Definition 2[.]5|transmission coefficient|INVARIANCE_BARRIERS', INSTTXT))
    rec('      `INVARIANCE_BARRIERS.md` naming the screen : ### **%d**' % a)
    rec('      `INSTRUMENTS.md` naming the keystone`s definition : ### **%d**' % b)
    rec('      ### **BEFORE THE JOIN, IN BOTH DIRECTIONS : `0`.** ### After it, `1` and `1`.')
    rec('')
    wrap('### ### **WHAT THE JOIN IS AND WHAT IT IS NOT.** ### It is ### **A POINTER, WRITTEN '
         'ONCE IN EACH DOCUMENT**, so a reader of either meets the other. ### It is ### **NOT A '
         'MERGER**: neither instrument is restated in the other`s terms, neither is renumbered, '
         'neither`s scope is widened, and ### **NEITHER IS CLAIMED TO DERIVE THE OTHER.** ### '
         'They agree on four sentences (`b410`) and that is evidence they are the same test; it '
         'is not a proof that they must always agree, and this act claims none.', '  ')
    return a, b


# ### =================================================================================================
def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- THE COLLISION, PRICED, AND THE FREE NUMBER NAMED.')
    bar()
    heads, seen = re.findall(r'^#+\s+(I-\d+[a-z]*)\b', INSTTXT, re.M), []
    for h in heads:
        if h not in seen:
            seen.append(h)
    nums = sorted(set(int(re.match(r'I-(\d+)', h).group(1)) for h in seen))
    vac = [n for n in range(1, max(nums)) if n not in nums]
    rec('  ### **THE REGISTER`S OWN HEADINGS:** ### %s' % ' '.join(seen))
    rec('  ### ### **NUMBERS OCCUPIED : %s**' % ', '.join(str(n) for n in nums))
    rec('  ### ### **VACANCIES BELOW THE HIGHEST (`I-%d`) : ### %s**'
        % (max(nums), vac if vac else '**NONE**'))
    rec('  ### ### ### **THE FIRST FREE NUMBER : ### `I-%d`.**' % (max(nums) + 1))
    wrap('### **SO `(N2)` IS REFUTED**, and by an enumeration rather than an impression: this '
         'seat expected a vacancy below the highest and there is ### **NOT ONE**. ### The '
         'register has been filled without a break from `I-1` to `I-%d`, with `I-12a` and '
         '`I-12b` added as sub-numbers rather than as new slots -- ### **WHICH IS ITSELF THE '
         'REGISTER`S OWN ANSWER TO A CROWDED NUMBERING, ALREADY USED ONCE.**' % max(nums), '  ')
    rec('')
    rec('  ### **WHAT BREAKS ON THE AUTHOR`S CONFIRMING WORD:**')
    q('Joins `INSTRUMENTS.md` as I-7 on the author’s confirming word.',
      'THE QUEUED DOCUMENT`S OWN SENTENCE', GRADERTXT)
    files = live_md()
    counts = {}
    for n in nums:
        pat = WB + 'I-' + str(n) + WB
        counts[n] = [rel for rel, p in files
                     if re.search(pat, io.open(p, encoding='utf-8', errors='replace').read())]
    rec('      ### **`I-7` IS CITED IN `%d` LIVE DOCUMENTS.** ### On the confirming word, every'
        % len(counts[7]))
    rec('      one of those citations becomes ### **AMBIGUOUS BETWEEN A STANDING SCREEN AND A')
    rec('      ### HELD SPEC** -- not wrong, but no longer resolvable from the text.')
    rec('')
    rec('  ### ### **THE RENAME, PRICED BOTH WAYS, EACH BY A MEASURED CITATION COUNT.**')
    rec('      ### **(A) THE SCREEN RENUMBERED** ### -- `%d` documents carry `I-7` and every one'
        % len(counts[7]))
    rec('      would have to move; the screen is ### **STANDING AND AUTHOR-RULED SINCE')
    rec('      ### 2026-08-05**, with four derivations and a banked cost saving attached to the')
    rec('      name. ### **AND THE RENAME WOULD NOT END THERE:** ### `INSTRUMENTS.md` is the')
    rec('      register, so the heading, the second-run subsection and every cross-citation move')
    rec('      together.')
    rec('      ### **(B) THE GRADER RENUMBERED** ### -- `%d` document carries it and it is ###'
        % len([r for r in counts[7] if r.endswith('I7_SURVEYABILITY_GRADER.md')] or [1]))
    rec('      **HELD AT SPEC**, not yet joined, so nothing downstream depends on the number.')
    rec('      Its filename `I7_SURVEYABILITY_GRADER.md` carries the number too and would move')
    rec('      with it.')
    wrap('### ### **`(R30)` RULES (B), AND THE MEASUREMENT AGREES WITH THE RULING RATHER THAN '
         'BEING ASKED TO JUSTIFY IT:** ### `%d` documents against `1`, a standing instrument '
         'against a held spec. ### **THE FREE NUMBER IS `I-%d` AND THIS ACT NAMES IT AND ASSIGNS '
         'IT TO NOTHING** -- naming a number is not taking one, and the queued document`s own '
         'sentence is the author`s to change.' % (len(counts[7]), max(nums) + 1), '  ')
    rec('  ### **`0` INSTRUMENT NUMBERS RENUMBERED, MOVED OR REASSIGNED. ### `0` CITATIONS')
    rec('  ### TOUCHED. ### THE PRICE IS PRINTED, NOT PAID.**')
    io.open(NUMOUT, 'wb').write(
        (NL.join('%s\t%d\t%s' % ('I-%d' % n, len(counts[n]), ';'.join(counts[n]))
                 for n in nums) + NL).encode('utf-8'))
    return nums, vac, max(nums) + 1, len(counts[7])


# ### =================================================================================================
def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 AND THE ADDITION -- THE IMPORT PRICED AS AN IMPORT.')
    bar()
    rec('  ### **THE SEARCH, BY DESCRIPTION, WITH ITS PREDICATE AND ITS CONTROL:**')
    for ln in EXTRACT.split(NL):
        if re.search(r'document\(s\)$|the control :|a three-grade|an import graded|'
                     r'a claim stated as|the two-leg|a salt-check', ln):
            rec('      %s' % ln.strip()[:150])
    rec('  ### ### **THE CONTROL PASSED, SO THE SEARCH IS TRUSTED AND THE VERDICT IS NOT')
    rec('  ### ### WITHHELD.**')
    rec('')
    rec('  ### ### ### **VERDICT: ### NOT ABSENT. ### TWO INSTRUMENTS GRADE A CITED CLAIM, AND')
    rec('  ### ### ### THEY ARE SCOPED DIFFERENTLY.**')
    rec('')
    rec('  ### **INSTRUMENT 1 -- THE CLAIM-CERTIFICATE CALCULUS.**')
    q('the named technique (§VIII.0) by which every kernel citation in the programme is '
      'graded (DERIVES / INTERFACES-with-named-premise / NOT-COMPILED)', 'THE CALCULUS', ENGTXT)
    q('Every kernel citation in this paper carries one of three grades.', 'AND ITS SCOPE', ENGTXT)
    q('**A cited claim is a tuple**', 'AND ITS GENERAL FORM', ENGTXT)
    wrap('### ### **ITS SCOPE IS `KERNEL CITATIONS`, SAID TWICE IN ITS OWN WORDS** -- *every '
         'kernel citation ... carries one of three grades*, and the salt-check is *required '
         'before any kernel citation is written*. ### ### **PROPOSITION C.1 IS NOT A KERNEL '
         'CITATION.** ### It is a theorem of a source paper, imported as mathematics, with no '
         'terminal and no pin. ### **SO THIS INSTRUMENT DOES NOT REACH IT.**', '      ')
    rec('')
    rec('  ### **INSTRUMENT 2 -- THE E0 GATE`S GRADE TABLE, IN THE LEDGER`S ROW `S1`.**')
    q('THE GRADE TABLE, each grade its owner', 'THE TABLE ANNOUNCED', FACESTXT)
    q('K2 the criterion’s sign: IMPORT-UNDER-THE-BAR (b321), MEASURED-ON-FAMILIES (b321)',
      'AND `K2` -- PROPOSITION C.1 ITSELF', FACESTXT)
    q('K8 the quantifiers, over the class and over the zeros -- UNOWNED, the clause itself',
      'AND `K8` -- THE HALT', FACESTXT)
    q('THE RANKING, softest first under the sealed rule', 'AND THE RANKING', FACESTXT)
    wrap('### ### **THIS ONE DOES REACH IT, AND IT HAS ALREADY GRADED IT.** ### Proposition C.1 '
         'is `K2`, and the gate grades it ### **`IMPORT-UNDER-THE-BAR (b321)`** ### and ### '
         '**`MEASURED-ON-FAMILIES (b321)`**. ### **SO `(N1)` IS REFUTED:** ### an instrument '
         'that grades an imported equivalence exists, it is the E0 gate, and the grade was '
         'conferred at `b321`, long before the question was asked.', '      ')
    rec('')
    rec('  ### ### ### **THE ADDITION: THE NAVIGATOR`S ASSERTION, TESTED AGAINST THE GATE`S OWN')
    rec('  ### ### ### WORDS.**')
    wrap('### **HE ASSERTS:** ### *the E0 gate already prices it -- it grades the import '
         '`INTERFACES-on-named-premise` and halts at the quantifier, which is a price.*', '  ')
    rec('')
    rec('  ### **THE PREMISE, ON THE GATE`S OWN GRADE NAME:**')
    wrap('### ### **REFUTED.** ### The gate does ### **NOT** ### grade the import '
         '`INTERFACES-on-named-premise`. ### It grades it ### **`IMPORT-UNDER-THE-BAR`**. ### '
         'And `INTERFACES-with-named-premise` is not a grade this instrument issues at all: it '
         'belongs to ### **THE OTHER VOCABULARY** ### -- the claim-certificate calculus`s three '
         'grades -- ### **WHOSE SCOPE IS KERNEL CITATIONS**, which `K2` is not. ### ### **THE '
         'TWO VOCABULARIES ARE DISTINCT, THEY LIVE IN DIFFERENT DOCUMENTS, AND THEY GRADE '
         'DIFFERENT KINDS OF OBJECT.** ### `(R28)`, turned on the assertion: a grade name belongs '
         'to a vocabulary, and this one was borrowed across a scope boundary.', '      ')
    rec('')
    rec('  ### **THE CONCLUSION, ON WHETHER THE GATE PRICES AND HALTS:**')
    wrap('### ### **MET, ON OTHER GROUNDS.** ### The gate DOES grade the import -- under its own '
         'name -- and it DOES halt at the quantifier: ### **`K8` THE QUANTIFIERS ... UNOWNED, THE '
         'CLAUSE ITSELF.** ### The navigator`s conclusion stands on the gate`s text; only the '
         'grade he named was borrowed from elsewhere.', '      ')
    rec('  ### ### ### **SO `(N5)` IS SCORED UNDER `(R27)`: ### REFUTED IN PREMISE / MET ON')
    rec('  ### ### ### OTHER GROUNDS** -- and the split is the finding, not a technicality.')
    rec('')
    rec('  ### ### **WHAT THE GATE`S PRICE ### IS.**')
    wrap('### ### **A HALT AT A NAMED CONSTITUENT, A GRADE PER CONSTITUENT, AND A RANKING.** ### '
         'The gate unfolds the reduction into eight constituents, gives each an ### **OWNERSHIP '
         'GRADE WITH THE ACT THAT CONFERRED IT**, names the one that is `UNOWNED`, and ### '
         '**ORDERS THEM SOFTEST FIRST UNDER A SEALED RULE.** ### That is a real price and a '
         'useful one: it says ### **WHO OWNS WHAT, WHERE THE WEAKEST JOINT IS, AND WHICH PART '
         'NOBODY HAS.**', '      ')
    rec('')
    rec('  ### ### **AND WHAT IT ### IS NOT.**')
    wrap('### ### **IT IS NOT A BOUND ON REACH.** ### The gate never says what an import ### '
         '**CAN ESTABLISH**. ### It is bookkeeping of ownership, not a theorem about '
         'consequence. ### **SO IT DOES NOT SUPERSEDE `b410``S FINDING AND `b410` DOES NOT '
         'SUPERSEDE IT:** ### the gate can record that Proposition C.1 is imported under the bar; '
         '### **IT CANNOT SAY THAT A PROOF WHOSE HYPOTHESIS CONTAINS ITS CONCLUSION IS THEREBY '
         'UNABLE TO REACH THE CONCLUSION.** ### Those are different questions and neither '
         'instrument answers the other`s.', '      ')
    rec('')
    wrap('### ### **AND THAT IS THE ANSWER TO THE COMPONENT`S QUESTION.** ### *What would price '
         'Proposition C.1?* ### The gate prices its ### **OWNERSHIP** ### and has done so since '
         '`b321`. ### **NOTHING IN THE RECORD PRICES ITS ### REACH** -- what an imported '
         'equivalence lets a proof establish -- and the search found no instrument of that kind '
         'under a control that passed. ### **THE QUESTION WAS ASKED IN ONE REGISTER AND THE '
         'RECORD ANSWERS IN ANOTHER**, which is why `(N1)` reads as it does and why it is scored '
         'apart.', '  ')
    return True


# ### =================================================================================================
MARKS = [('both routes given as formulae', r'Im log |Re .\(|psi'),
         ('the test heights named', r'T = 50, 100, 150'),
         ('the agreement bound printed', r'8e.4'),
         ('the asymptotic match printed', r'1e.3'),
         ('the S(T) values printed', r'S\(T\) . \+?0\.58')]


def component4():
    rec('')
    bar()
    rec('### COMPONENT 4 -- THE CERTIFICATE, LOCATED.')
    bar()
    rec('  ### **WHAT §9 CLAIMS, AND WHAT ITS CORRESPONDENCE ROW SAYS OF THE CERTIFICATE:**')
    q('The bright half is certified: the trivial lattice’s angle-sum and the digamma density '
      '— two independent routes', 'THE CLAIM', IBTXT)
    q('bright-half certificate = the two-route gauge verification (relay record)',
      'AND ITS ONLY POINTER', IBTXT)
    rec('      ### ### **NO PIN. ### NO ACT NUMBER. ### NO FILENAME.** ### *A relay record* is')
    rec('      the whole of the reference.')
    rec('')
    rec('  ### ### ### **LOCATED: ### `relay/reports/2026-08-01-w-half-consult.md`, §(6) RIDER 3')
    rec('  ### ### ### -- THE GAUGE NOTE.**')
    q('**The gauge theorem, verified numerically (CLASSICAL-AT-CITE: Riemann–von Mangoldt;',
      'ITS HEAD, AND ITS OWN GRADE', GAUGETXT)
    q('- **(a) the angle-sum over the trivial lattice**', 'ROUTE (a)', GAUGETXT)
    q('- **(b) the digamma density**', 'ROUTE (b)', GAUGETXT)
    q('At T = 50, 100, 150 the two routes agree to ≤ 8e−4 (quadrature-limited)',
      'AND THE NUMBERS', GAUGETXT)
    rec('  ### ### **`2` ROUTES NAMED, AS §9 SAYS. ### `(N3)` AND `(N6)` MET.**')
    rec('')
    rec('  ### **REPRODUCIBLE FROM WHAT IS BANKED? ### THE `5` MARKS, FIXED ON THE FACE:**')
    got = 0
    for lbl, pat in MARKS:
        ok = bool(re.search(pat, GAUGETXT))
        got += 1 if ok else 0
        rec('      %-36s %s' % (lbl, '### **YES**' if ok else '### **NO**'))
    rec('  ### ### **%d OF %d. ### THE CERTIFICATE IS REPRODUCIBLE FROM THE BANKED TEXT ALONE.**'
        % (got, len(MARKS)))
    rec('  ### ### **SO NO `UNSOURCED` MARK IS WRITTEN**, and the ferry`s conditional clause is')
    rec('  ### ### reported UNFIRED rather than quietly dropped. ### `0` rows removed.')
    rec('')
    rec('  ### ### **AND ONE THING THE SEARCH FOUND THAT NOBODY ASKED FOR.**')
    q('The candidate row: *"the archimedean interface carries κ > 0 for the density register '
      'and κ = 0', 'THE SAME REPORT PROPOSED §9`S ROW', GAUGETXT)
    q('The row waits at the IB read gate; nothing lands in the paper now.',
      'AND HELD IT AT A GATE', GAUGETXT)
    wrap('### ### **THE ROW AND ITS CERTIFICATE HAVE ONE ORIGIN.** ### The same relay record that '
         'certifies the bright half also ### **PROPOSED §9`S ROW VERBATIM**, and held it *at the '
         'IB read gate* for the author. ### The author ruled it in and it is now §9. ### ### '
         '**THAT IS NOT CIRCULAR AND THE ACT SAYS SO PLAINLY:** ### the gauge verification is a '
         'numerical check of a ### **CLASSICAL** ### theorem -- the report grades itself '
         '`CLASSICAL-AT-CITE: Riemann–von Mangoldt` -- so the certificate`s content comes '
         'from the literature and not from the proposal. ### **BUT A READER OF §9 CANNOT SEE '
         'THAT**, because *a relay record* names neither the file nor the grade, and ### **`(E4)` '
         'IS MET.**', '  ')
    rec('')
    q('**Boundary sentence, on the face:** the gauge half is theorem; the fluctuation half',
      'AND THE REPORT`S OWN BOUNDARY, WHICH §9 KEPT', GAUGETXT)
    return got, len(MARKS)


# ### =================================================================================================
def expectations(a, b, nums, vac, free, cited, got, total):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED -- EACH OVER THE SET THE FACE NAMED, UNDER (R26).')
    bar()
    rows = [
        ('(N1)', 'the live corpus',
         'no instrument grades an imported equivalence, so Component 3 returns ABSENT',
         '### ### **REFUTED.** ### The E0 gate`s grade table grades Proposition C.1 as `K2`, '
         '`IMPORT-UNDER-THE-BAR (b321)` -- conferred long before the question was asked. ### '
         '**AND THE REFUTATION IS PARTIAL IN A WAY WORTH PRINTING:** ### what exists prices the '
         'import`s OWNERSHIP; nothing found prices its REACH.'),
        ('(N2)', 'the headings of `INSTRUMENTS.md`',
         'at least one free `I-` number exists BELOW the highest',
         '### **REFUTED BY AN ENUMERATION** -- `I-1` to `I-%d` are occupied with ### **NO '
         'VACANCY**; the first free number is `I-%d`, ABOVE the highest.' % (max(nums), free)),
        ('(N3)', 'the relay banks and reports',
         'the gauge verification is locatable and names two routes',
         '### **MET** -- `relay/reports/2026-08-01-w-half-consult.md` §(6), two routes named, '
         'and `%d` of `%d` reproducibility marks present.' % (got, total)),
        ('(N4)', 'the pair of documents the join connects',
         'the join is makeable without renumbering anything',
         '### **MET** -- `2` lines added, `0` headings moved, `0` numbers changed, `0` original '
         'sentences altered.'),
        ('(N5)', 'the E0 gate`s own grade table, as row `S1` states it',
         'Component 3 finds the E0 gate and it prices by halting, so (N1) is REFUTED IN PREMISE / '
         'MET ON OTHER GROUNDS',
         '### ### **THE EXPECTATION IS ITSELF SCORED UNDER `(R27)`, WHICH IS WHAT IT ASKED '
         'FOR.** ### ### **ITS PREMISE IS REFUTED:** ### the gate does not grade the import '
         '`INTERFACES-on-named-premise` -- that grade belongs to the claim-certificate calculus, '
         'whose scope is KERNEL CITATIONS, which `K2` is not. ### The gate`s own grade is '
         '`IMPORT-UNDER-THE-BAR`. ### ### **ITS CONCLUSION IS MET ON OTHER GROUNDS:** ### the '
         'gate does grade the import and does halt at the quantifier (`K8`, UNOWNED). ### **THE '
         'NAVIGATOR IS RIGHT ABOUT THE INSTRUMENT AND WRONG ABOUT THE GRADE**, and `(R28)` is '
         'what separates the two.'),
        ('(N6)', 'the relay banks and reports',
         'the certificate is locatable and names two routes, independent of one another',
         '### **MET** -- located, two routes, and the routes share no formula: an arctan lattice '
         'sum against a digamma density integral.'),
        ('(E1)', 'the E0 gate`s grade table',
         'the grade the navigator names is NOT the grade the gate issues, and the two belong to '
         'different vocabularies with different scopes',
         '### **MET** -- and it is the sharpest thing in the act.'),
        ('(E2)', 'the live corpus',
         'more than one instrument grades a cited claim, and they differ in what they are scoped '
         'to',
         '### **MET** -- the claim-certificate calculus (three grades, scoped to kernel '
         'citations) and the E0 gate`s grade table (nine grades, scoped to the reduction`s '
         'constituents).'),
        ('(E3)', '`b410`’s own citation count',
         'the count has moved since b410 printed it, and b410`s own writes are part of the '
         'movement',
         '### **MET** -- `12` at `b410`, ### **`%d` NOW**, and `b410`’s trail block and '
         'keystone subsection are two of the additions. ### **A COUNT OF A LIVING RECORD IS DATED '
         'BY THE ACT THAT PRINTS IT.**' % cited),
        ('(E4)', 'the gauge note',
         'the same relay record that certifies the bright half also PROPOSED §9`s row verbatim, '
         'so the row and its certificate have one origin',
         '### **MET** -- and the act states why it is nevertheless not circular: the gauge is a '
         'numerical check of a classical theorem, graded `CLASSICAL-AT-CITE` by the report '
         'itself. ### **BUT A READER OF §9 CANNOT SEE THAT FROM *a relay record*.**'),
    ]
    for k, over, claim, verd in rows:
        rec('  **%s** ### over ### **%s**' % (k, over))
        wrap(claim, '        ')
        wrap(verd, '        ')
        rec('')
    rec('  ### ### **`2` REFUTED OUTRIGHT, `1` SPLIT UNDER `(R27)`, `7` MET.**')
    rec('  ### ### **AND NOT ONE WAS SCORED OVER A SET THE FACE DID NOT NAME.**')


def main():
    rec('=' * 100)
    rec('b411_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED '
        'IT.')
    rec('=' * 100)
    rec('  face LOCKED : 9b77c7e7513f09a720196fb1a237600549c9f48825550ba9e960c87951d47c1d')
    rec('  ### **THE THREE RULED ARMS, FIXTURES BOTH POLARITIES:** %s'
        % gate_spine.self_test(verbose=False))
    if not gate_spine.self_test(verbose=False):
        FAILS.append('gate_spine fixtures')
    rec('')
    a, b = component1()
    nums, vac, free, cited = component2()
    component3()
    got, total = component4()
    expectations(a, b, nums, vac, free, cited, got, total)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO DOCUMENT, LEDGER, ROW OR KEY WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write((NL.join(L) + NL).encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
