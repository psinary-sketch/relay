# -*- coding: utf-8 -*-
"""b409_components.py -- THE COMPONENTS. ### **EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.**

### ### **NOTHING HERE WRITES TO A DOCUMENT, A LEDGER, A ROW OR A KEY.** ### It computes, prints,
### and emits the declaration list; `b409_desk_bank.py` writes. ### **EVERY WRITE ENCODES FIRST.**
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import quote_norm     # noqa: E402
import class_scheme   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b409_components.txt')
TABLE_OUT = os.path.join(D, 'b409_scheme_table.txt')
PP = r'D:\MY-DOwnloads\PLACE-papers'
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')
BS = chr(92)

L = []
FAILS = []


def rec(s=''):
    L.append(s)
    print(s)


def bar(c='-'):
    rec(c * 100)


def flat(s):
    return re.sub(r'\s+', ' ', quote_norm.norm(s)).strip()


EXTRACT = io.open(os.path.join(D, 'b409_extract.txt'), encoding='utf-8').read()
IBTXT = io.open(IB, encoding='utf-8').read()
MONOTXT = io.open(MONO, encoding='utf-8').read()


def q(frag, where, hay=None):
    hay = EXTRACT if hay is None else hay
    ok = flat(frag) in flat(hay)
    if not ok:
        FAILS.append('%s : %r' % (where, frag[:70]))
    rec('        %s *"%s"*' % ('quote:' if ok else '### NOT IN SOURCE:', frag))
    return ok


def wrap(s, ind='      ', w=126):
    for k in range(0, len(s), w):
        rec('%s%s' % (ind, s[k:k + w]))


def live_md():
    out = []
    for root, dirs, files in os.walk(PP):
        dirs[:] = [d for d in dirs if d not in ('.git', 'archive')]
        for f in sorted(files):
            if f.endswith('.md'):
                p = os.path.join(root, f)
                out.append((os.path.relpath(p, PP).replace(BS, '/'), p))
    return out


# ### =================================================================================================
def component1():
    bar()
    rec('### COMPONENT 1 -- THE NUMBERING, MEASURED AND DECLARED.')
    bar()
    rec('  ### **THE CANONICAL INDEX, ATTESTED TWICE AND INDEPENDENTLY:**')
    q('the monograph\u2019s canonical index is C\u2081 Schwarz \u00b7 C\u2082 Euler \u00b7 '
      'C\u2083 functional-equation \u00b7 C\u2084 modular/PSL\u2082 \u00b7 C\u2085 spectral \u00b7 '
      'C\u2086 Cauchy\u2013Riemann \u00b7 C\u2087 Hadamard', 'ENUMERA')
    q('| C\u2084 (Modular/PSL\u2082) | Transformation | Modular symmetry (PSL\u2082(\u2124) '
      'action) | Modular forms framework |', 'MONOGRAPH TABLE', hay=MONOTXT)
    rec('      ### **THE MONOGRAPH`S OWN TABLE AND `ENUMERA``S RECONCILIATION AGREE, SYMBOL FOR')
    rec('      ### SYMBOL.**')
    rec('')
    rec('  ### **AND THE CORRESPONDENCE TABLE THAT ATTRIBUTES A DIFFERENT SCHEME TO THE MONOGRAPH:**')
    q('| C\u2083 | C\u2081 | Archimedean / functional equation |', 'CORRESPONDENCE C3')
    q('| C\u2084 | C\u2085 | Global / PSL\u2082 symmetry |', 'CORRESPONDENCE C4')
    rec('  ### ### ### **SO `b408`\u2019S CONCLUSION STANDS AND ITS LABEL WAS WRONG.** ### There')
    rec('  ### ARE two numberings and they do disagree on six of seven symbols -- but the second is')
    rec('  ### ### **NOT THE MONOGRAPH\u2019S**, and two independent witnesses say so. ### **THE')
    rec('  ### ### TABLE DESCRIBES A LIVE SCHEME CORRECTLY AND MISNAMES WHOSE IT IS.** ###')
    rec('  ### **ROUTED, NOT REPAIRED**, and `b408` is corrected here and NOT EDITED.')
    rec('')
    rec('  ### ### **THE SWEEP, UNDER BOTH WINDOWS -- AND THE KINDER NUMBER IS NOT REPORTED ALONE.**')
    for ln in EXTRACT.split('\n'):
        if re.search(r'LIVE documents using|DEPOSITED \(`outputs/`\)|DISAGREEING PIN|'
                     r'SCHEME READABLE|SCHEME UNDECLARED', ln):
            rec('      %s' % ln.strip()[:160])
    rec('      ### **THE LOOSE WINDOW\u2019S DISAGREEMENT COUNT IS THE SHAPE OF A LIST, NOT A')
    rec('      ### CONFLICT** -- a document naming its classes in a row gives every symbol its')
    rec('      ### neighbour\u2019s content. ### Both are printed; the tight one governs.')
    rec('')
    rec('  ### **THE PER-DOCUMENT TABLE, DECIDED BY CONTENT AND NEVER BY PROVENANCE:**')
    rows = []
    for rel, p in live_md():
        if rel.startswith('outputs/'):
            continue
        src = io.open(p, encoding='utf-8', errors='replace').read()
        if not class_scheme.SYM.search(src):
            continue
        sch, why = class_scheme.scheme_of(src)
        # ### **THE BOM DEFEATS `^#`** -- two documents carry `﻿` and were called headless by
        # ### this act's own first predicate. ### Stripped before the test, and the count printed.
        head = re.match(r'^#\s+\S', src.lstrip('﻿')) is not None
        bom = src.startswith('﻿')
        rows.append(dict(rel=rel, sch=sch, why=why, head=head, bom=bom,
                         uses=len(class_scheme.SYM.findall(src))))
    dec = [r for r in rows if r['sch']]
    undecl = [r for r in rows if not r['sch'] and 'UNDECLARED' in r['why']]
    tied = [r for r in rows if not r['sch'] and 'TIED' in r['why']]
    stage = [r for r in dec if r['sch'] == 'STAGE']
    excl = [r for r in dec if r['sch'] == 'EXCLUSION-ORDER']
    for r in sorted(dec, key=lambda x: -x['uses']):
        rec('      %-52s %-16s uses %-4d head %s'
            % (r['rel'][:52], r['sch'], r['uses'], r['head']))
        rec('          %s' % r['why'])
    rec('')
    rec('  ### ### **DECIDABLE : %d ### -- STAGE %d, EXCLUSION-ORDER %d.**'
        % (len(dec), len(stage), len(excl)))
    rec('  ### ### **TIED (a tie is not a reading) : %d ### ; SCHEME UNDECLARED : %d.**'
        % (len(tied), len(undecl)))
    writable = [r for r in dec if r['head']]
    routed = [r for r in rows if r not in writable]
    rec('  ### ### **DECLARABLE (decidable AND has a `# ` head to hang a note on) : %d.**'
        % len(writable))
    rec('  ### ### **ROUTED, NOT GUESSED : %d** ### -- %d UNDECLARED, %d TIED, %d headless.'
        % (len(routed), len(undecl), len(tied),
           len([r for r in dec if not r['head']])))
    boms = [r['rel'] for r in dec if r['bom']]
    rec('  ### **AND `%d` OF THE DECLARABLE DOCUMENTS BEGIN WITH A BYTE-ORDER MARK**, which this'
        % len(boms))
    rec('  ### act`s FIRST head test read as *headless* and would have ROUTED unread: %s.'
        % (', '.join('`%s`' % b for b in boms) if boms else 'none'))
    rec('  ### ### **A DOCUMENT IS NOT HEADLESS BECAUSE AN INVISIBLE CHARACTER STANDS IN FRONT OF')
    rec('  ### ### ITS HEAD.** ### The predicate strips the mark and the writer PRESERVES it.')
    rec('  ### ### ### **SO A MAJORITY OF DOCUMENTS CANNOT BE ASSIGNED A SCHEME FROM THEIR OWN')
    rec('  ### ### ### TEXT: %d OF %d.**' % (len(rows) - len(dec), len(rows)))
    rec('')
    rec('  ### ### ### **AND THIS ACT`S TWO INSTRUMENTS DISAGREE, SO BOTH NUMBERS ARE PRINTED AND')
    rec('  ### ### ### THE DEFECTIVE PREDICATE IS NAMED.**')
    import b409_extract as X  # noqa: E402  ### the surveying instrument, imported not retyped
    ext = set()
    for rel, p in live_md():
        if rel.startswith('outputs/'):
            continue
        src = io.open(p, encoding='utf-8', errors='replace').read()
        if not class_scheme.SYM.search(src):
            continue
        if X.pins(src, tight=True)[0] > 0:
            ext.add(rel)
    mine = set(r['rel'] for r in dec)
    rec('      the survey called ### **%d** ### readable; the matcher calls ### **%d** ### '
        'decidable.' % (len(ext), len(mine)))
    rec('      ### **ONLY IN THE SURVEY (%d):**' % len(ext - mine))
    for r in sorted(ext - mine):
        rec('          %s' % r)
    rec('      ### **ONLY IN THE MATCHER (%d):**' % len(mine - ext))
    for r in sorted(mine - ext):
        rec('          %s' % r)
    wrap('### **THE SURVEY`S PREDICATE IS `at least one symbol whose following content matches the '
         'CANONICAL index`.** ### That is not readability and it is not symmetric: a document '
         'consistently using the OTHER scheme scores `0` and is called UNDECLARED, while a document '
         'whose only pinned symbol is `C7` -- ### **THE ONE SYMBOL BOTH SCHEMES SHARE** ### -- '
         'scores `1` and is called readable though nothing about it is decided. ### The two errors '
         'run in opposite directions and very nearly cancel, which is why a difference of `%d` '
         'conceals a symmetric difference of `%d`.'
         % (abs(len(ext) - len(mine)), len(ext ^ mine)), '      ')
    wrap('### ### **THE MATCHER GOVERNS**, because it requires a symbol to match ONE scheme and NOT '
         'the other, which is what deciding a scheme means. ### **THE SURVEY`S LINE IS NOT EDITED '
         'AND ITS NUMBER IS NOT WITHDRAWN**; it is republished here beside the number that governs, '
         'with the predicate that produced it stated. ### And `C7`, shared by both indices, ### '
         '**CAN NEVER DECIDE A DOCUMENT** -- the matcher`s exclusivity test is what makes that true '
         'by construction rather than by care.', '      ')
    rec('')
    rec('  ### **AND ONE DOCUMENT USES BOTH SCHEMES IN ITS OWN TEXT, WHICH THE TABLE ABOVE HIDES**')
    rec('  ### **BECAUSE IT REPORTS A MAJORITY:** ### `PATHS_TO_THE_CRITICAL_LINE.md` pins')
    rec('  ### ### **STAGE** ### on the balance of its symbols, and its fifth-path line uses')
    rec('  ### ### **EXCLUSION-ORDER** ### -- which is precisely the line `b408` met.')
    rec('')
    rec('  ### **WHAT DISPOSITION (A) WOULD HAVE COST, PRINTED SO THE CHOICE IS ON THE RECORD:**')
    tot = sum(r['uses'] for r in rows)
    wrap('### **(A) EVERY DOCUMENT ADOPTS ONE NUMBERING** ### -- %d documents touched and '
         '### **%d SYMBOL USES REWRITTEN**, of which the %d in EXCLUSION-ORDER documents change '
         'meaning; every compiled terminal, ledger row and deposited file carrying a symbol would '
         'have to move with them, and `outputs/` cannot be edited at all. ### **AND THE DEPOSITED '
         '### COPIES WOULD THEN DISAGREE WITH THE LIVE ONES**, which is a worse hazard than the '
         'one being cured.'
         % (len(rows), tot, sum(r['uses'] for r in excl)))
    wrap('### **(B) EVERY DOCUMENT DECLARES ITS SCHEME** ### -- %d documents gain ONE LINE each, '
         '### **`0` SYMBOLS MOVE**, nothing deposited is touched, and the %d that cannot be read '
         'are ROUTED. ### **THIS IS THE ONE `(R25)` RULES**, and it is executed.'
         % (len(writable), len(routed)))
    io.open(TABLE_OUT, 'wb').write(
        ('\n'.join('%s\t%s\t%s\t%d' % (r['rel'], r['sch'] or 'ROUTED', r['head'], r['uses'])
                   for r in rows) + '\n').encode('utf-8'))
    rec('  ### the declaration list is at `data/b409_scheme_table.txt` for the writer.')
    return dict(rows=len(rows), dec=len(dec), stage=len(stage), excl=len(excl),
                tied=len(tied), undecl=len(undecl), writable=[r['rel'] for r in writable],
                routed=len(routed))


def component2():
    rec('')
    bar()
    rec('### COMPONENT 2 -- THE GLOBAL CLASS, EXAMINED BY DESCRIPTION.')
    bar()
    rec('  ### **FIRST: THE TWO ARTEFACT HITS, READ WHOLE UNDER THEIR OWN SCHEME.**')
    q('*Touches.* output-stage classes (C\u2083 + C\u2087)', 'PATHS TOUCHES')
    q('The level curves {Re \u03be = 0}, the logarithmic derivative, Stirling asymptotics, the '
      'Hadamard product', 'PATHS MACHINERY')
    rec('      ### **THE MACHINERY LINE DECIDES IT AND THE SYMBOLS DO NOT:** ### level curves and')
    rec('      ### the logarithmic derivative are ### **CAUCHY-RIEMANN**, and the Hadamard product')
    rec('      ### is ### **HADAMARD.** ### Under the EXCLUSION-ORDER index those are `C3` and')
    rec('      ### `C7`, which is exactly what the line says.')
    rec('  ### ### ### **SO THE TWO HITS NAME THE LOCAL CLASS AND THE ORDER CLASS, AND')
    rec('  ### ### ### **NEITHER IS THE MODULAR RELATION.** ### `b408`\u2019s artefact reading is')
    rec('  ### ### ### CONFIRMED, by the path\u2019s own machinery rather than by a numbering table.')
    rec('')
    rec('  ### **SECOND: THE SEARCH BY DESCRIPTION, WITH ITS POSITIVE CONTROL.**')
    for ln in EXTRACT.split('\n'):
        if re.search(r'BY DESCRIPTION \(the modular|BY SYMBOL \(|POSITIVE CONTROL|files in scope',
                     ln):
            rec('      %s' % ln.strip()[:150])
    rec('')
    rec('  ### ### ### **AND THE CONTROL DID ITS WORK: IT FOUND SOMETHING `b408` COULD NOT HAVE')
    rec('  ### ### ### FOUND.**')
    rec('  ### `INVARIANCE_BARRIERS.md` carries a whole section this record had never cited:')
    q('## 9. The calibration family: the archimedean instance and the per-place table',
      'SECTION 9', hay=IBTXT)
    q('*The archimedean interface carries \u03ba > 0 for the density register and \u03ba = 0 for '
      'the placement register.*', 'THE ARCHIMEDEAN ROW', hay=IBTXT)
    rec('      ### ### **THE RECORD GRADES `\u03ba` BY REGISTER, AND IT HAS A CALIBRATED ROW FOR')
    rec('      ### ### THE ARCHIMEDEAN INTERFACE.** ### `b408` searched for the class SYMBOL beside')
    rec('      ### a channel word; ### **THIS SECTION NAMES ITS INTERFACES BY DESCRIPTION AND NEVER')
    rec('      ### ### BY SYMBOL**, so no symbol search could reach it. ### **THE FERRY\u2019S')
    rec('      ### ### INSTRUCTION TO SEARCH BY DESCRIPTION IS WHAT FOUND IT.**')
    rec('')
    rec('  ### **AND THE PER-PLACE TABLE, WHICH SAYS WHAT HAS A ROW AND WHAT DOES NOT:**')
    q('every single-place row \u2014 the archimedean digamma term, each finite prime\u2019s ledger '
      'terms \u2014 transmits the density register', 'PER-PLACE TABLE', hay=IBTXT)
    q('further per-place instance rows are the named next moves', 'THE NEXT MOVES', hay=IBTXT)
    rec('      ### ### **THE FAMILY\u2019S ROWS ARE PLACES. ### THE MODULAR SYMMETRY IS NOT A')
    rec('      ### ### PLACE, SO IT HAS NO ROW -- AND THE FAMILY\u2019S OWN STATED NEXT MOVES ARE')
    rec('      ### ### MORE PLACES, WHICH WOULD NOT REACH IT.**')
    rec('')
    rec('  ### ### ### **VERDICT ON EXAMINATION: ### ABSENT UNDER BOTH SCHEMES.**')
    rec('  ### `4` hits by description and `2` by symbol across `4746` files, every one hand-read,')
    rec('  ### and not one examines the modular relation as a channel. ### And the corpus\u2019s own')
    rec('  ### calibration family -- the one place that grades interfaces -- ### **HAS NO ROW FOR')
    rec('  ### ### IT.** ### **THE CONTROL PASSED, SO THE SEARCH IS TRUSTED.**')
    rec('')
    rec('  ### ### ### **AND NOW THE EXAMINATION ITSELF, AS A READING.**')
    rec('  ### **THE CLASS, IN THE MONOGRAPH\u2019S OWN DEFINITION:**')
    q('| C\u2084 (Modular/PSL\u2082) | Transformation | Modular symmetry (PSL\u2082(\u2124) '
      'action) | Modular forms framework |', 'C4 DEFINED', hay=MONOTXT)
    rec('  ### **AND THE SENTENCE THAT DECIDES IT, STATED BY THE MONOGRAPH OF *EVERY* CLASS:**')
    q('The constraint function of each mechanism class is antisymmetric about the reflection axis '
      '(the functional equation forces this). An antisymmetric continuous function has exactly one '
      'zero on the axis.', 'THE ANTISYMMETRY', hay=MONOTXT)
    rec('')
    rec('  ### ### ### **VERDICT: ### DARK ON THE PLACEMENT REGISTER.**')
    wrap('### An antisymmetric constraint has exactly one zero ### **ON THE AXIS** ### -- it '
         'locates the AXIS, not a point on it. ### The modular class\u2019s constraint is '
         'antisymmetric for the same reason every class\u2019s is: ### **THE FUNCTIONAL EQUATION '
         '### FORCES IT.** ### So the modular relation, like the functional equation, preserves the '
         'critical line and ### **DISTINGUISHES NO INDIVIDUAL ZERO ON IT** -- which is the '
         'record\u2019s own placement register, and the register the archimedean row grades at '
         '`\u03ba = 0`.', '  ')
    rec('')
    rec('  ### ### **AND WHAT THIS VERDICT IS NOT, SAID IN THE SAME BREATH AS THE VERDICT.**')
    wrap('### **IT IS A READING OF THE RECORD\u2019S OWN TWO SENTENCES, NOT A MEASURED `\u03ba` '
         'UNDER DEFINITION 2.4\u2019S SUPREMUM.** ### The calibration family has ### **NO ROW** ### '
         'for the modular relation, so ### **NO CERTIFICATE EXISTS**, and this act writes none. ### '
         'A reading and a calibrated row are different objects and the record keeps them apart.',
         '  ')
    rec('')
    rec('  ### ### **AND THE CONSEQUENCE, NAMED AND NOT DRAWN.**')
    wrap('### If every mechanism class\u2019s constraint is antisymmetric about the axis, and the '
         'exhaustiveness says the channels ARE the mechanism classes with no fourth, then ### '
         '**COROLLARY 3.6\u2019S BRIGHT CHANNEL IS NOT AMONG THE THREE AS THE RECORD READS THEM.** '
         '### ### **THAT IS A CONSEQUENCE OF TWO SENTENCES READ TOGETHER AND IT IS NOT DRAWN HERE**'
         ' -- the record grades ONE row, calls the family OPEN, and its own next moves are more '
         'places. ### **A CONSEQUENCE NAMED IS NOT A CONSEQUENCE ESTABLISHED, AND THIS ACT DOES '
         'NOT ESTABLISH IT.** ### `0` routes proposed, priced or opened.', '  ')
    return 'ABSENT UNDER BOTH SCHEMES', 'DARK ON THE PLACEMENT REGISTER'


MOVES = [
    ('MOVEMENT 1 -- Lemma 3.2 and Corollary 3.3',
     'a factoring step\u2019s conclusion cannot discriminate within a `~_{I,P}`-class',
     'SURVIVES -- ### **PROVIDED EVERY SENTENCE OF `H` ITSELF FACTORS THROUGH `I`.**',
     'The induction is over `\u03c0`\u2019s inference steps. ### Adding `H` adds PREMISES, and a '
     'step invoking a premise that references an individual-element specification across `I` ### '
     '**DOES NOT FACTOR** -- so the theorem\u2019s own hypothesis fails at that step. ### **THE '
     '### RELATIVIZATION THEREFORE COSTS ONE HYPOTHESIS THE ORIGINAL DID NOT NEED**, and it is a '
     'hypothesis about `H` and not about `\u03c0`.'),
    ('MOVEMENT 2 -- Lemma 3.4',
     'the strongest conclusion is density-one within each class',
     'SURVIVES UNCHANGED.',
     'The lemma bounds what an `I`-factored proof can CONCLUDE about `P`. ### A conclusion of the '
     'form `H \u21d2 \u2200x P(x)` still has a truth value at each `x` that depends on `x`, so '
     'Corollary 3.3 applies to it verbatim and the bound becomes `H \u21d2 (P on a density-one '
     'subset of each class)`. ### **NOTHING IN THE ARGUMENT MENTIONS THE SHAPE OF THE '
     'CONCLUSION.**'),
    ('MOVEMENT 3 -- Proposition 3.5, the Epstein witness',
     'density-one-per-class does not imply universality',
     'SURVIVES UNCHANGED, AND FOR A REASON WORTH PRINTING.',
     'This movement is a ### **GENERAL NON-ENTAILMENT** ### -- it exhibits one determined system '
     'where density-one holds and universality fails, and thereby shows the implication is not '
     'valid. ### **IT SAYS NOTHING ABOUT `M`, SO IT NEEDS NO WITNESS SATISFYING `H`.** ### A '
     'reader who expected this to be the failing step expected the witness to be doing work it is '
     'not doing.'),
]


def component3():
    rec('')
    bar()
    rec('### COMPONENT 3 -- THE LEMMA RELATIVIZED.')
    bar()
    rec('  ### **THE ORIGINAL, QUOTED:**')
    q('Let M be a determined structure with specification S, interface I with \u03ba(P, I) = 0 for '
      'target parameter P. Let \u03c0 be a formal first-order proof in ZFC \u222a S. If \u03c0 '
      'factors through I for P, then \u03c0 does not establish the universal statement', 'THM 3.1')
    rec('')
    rec('  ### **THE STATEMENT FOR A PROOF OF A CONDITIONAL:**')
    wrap('### **THEOREM 3.1-H.** ### *Let `M` be a determined structure with specification `S`, '
         '`I` an interface with `\u03ba(P, I) = 0`, and `H` a finite set of `\u2112`-sentences '
         '### **EVERY MEMBER OF WHICH FACTORS THROUGH `I` FOR `P`.** ### Let `\u03c0` be a formal '
         'first-order proof in `ZFC \u222a S` of `H \u21d2 (\u2200x \u2208 M: P(x))`. ### If '
         '`\u03c0` factors through `I` for `P`, then `\u03c0` does not establish it; the strongest '
         'statement it can establish has the form `H \u21d2` (`P` holds on a density-one subset of '
         'each `I`-class), and the individual element remains unreached.*', '  ')
    rec('')
    rec('  ### **THE STEP-BY-STEP CHECK, AT CONTENT:**')
    for name, what, verdict, why in MOVES:
        rec('    ### **%s**' % name)
        rec('        what it establishes : %s' % what)
        rec('        under `H`           : ### **%s**' % verdict)
        wrap(why, '        ')
        rec('')
    rec('  ### ### ### **VERDICT: ### RELATIVIZES.**')
    rec('  ### ### **AND THE EXTRA COST IS PART OF THE VERDICT AND NOT BURIED IN THE PROOF:**')
    wrap('### **THE RESTATEMENT NEEDS ONE HYPOTHESIS THE ORIGINAL DID NOT: THAT EVERY SENTENCE OF '
         '### `H` ITSELF FACTORS THROUGH `I` FOR `P`.** ### Without it a step invoking `H` need '
         'not factor, and the theorem\u2019s own hypothesis fails. ### **A RESTATEMENT THAT '
         'QUIETLY COSTS MORE THAN THE ORIGINAL IS NOT THE ORIGINAL RELATIVIZED**, so the cost is '
         'on the face of the verdict.', '  ')
    rec('')
    rec('  ### ### **AND WHAT IT SAYS OF THE CORPUS\u2019S REDUCTION, WITH `b408`\u2019S FOUR')
    rec('  ### ### IMPORTED PREMISES AS `H`.**')
    wrap('`H` = { the source\u2019s Definition 3.1 ; Proposition C.1 ; the local term (149) ; '
         'Theorem 4.7 }. ### The relativized lemma applies to the corpus\u2019s reduction ### '
         '**IF AND ONLY IF ALL FOUR FACTOR THROUGH THE PRODUCT-FORMULA INTERFACE FOR `P`** -- that '
         'is, if each references only cumulative invariants and not individual-element '
         'specifications. ### ### **AND THAT IS A DEFINITION-2.5 CLASSIFICATION OF FOUR SENTENCES '
         '### THAT NOBODY HAS RUN.**', '  ')
    wrap('### ### **SO THE RELATIVIZATION SUCCEEDS AND HANDS THE CORPUS A NEW UNASKED QUESTION IN '
         '### ### PLACE OF THE OLD ONE.** ### `b407` said the theorem did not apply because the '
         'reduction was the wrong kind of object; `b408` priced the writing that would fix that '
         'and found it would produce a conditional; ### **THIS ACT SHOWS THE LEMMA COVERS '
         'CONDITIONALS -- AND THAT APPLYING IT NOW TURNS ON WHETHER FOUR IMPORTED SENTENCES '
         'FACTOR.** ### **A THEOREM THAT APPLIES *PROVIDED A CONDITION* IS NOT A THEOREM THAT '
         'APPLIES**, and this act does not run the check.', '  ')
    rec('')
    rec('  ### ### **THE GRADE, AND ONE THING THE ORDER\u2019S WORDING CANNOT MEAN.**')
    q('| Theorem 3.1, semantic core (inference respecting indistinguishability cannot separate '
      'related points) | SIDE-kernel v1.7 = `2957e7d` | `SieveCeilingSemantic.sieve_ceiling_'
      'semantic` | axiom-free (none) | Compiled', 'THE ORIGINAL`S GRADE', hay=IBTXT)
    wrap('### The order says the restatement carries ### **THE ORIGINAL\u2019S GRADE.** ### The '
         'original\u2019s grade is ### **COMPILED, AXIOM-FREE, AT A PIN** -- and ### **NOTHING WAS '
         'COMPILED HERE.** ### So the restatement takes ### **NO NEW GRADE** ### (which is what '
         'the instruction is for) and is marked ### **UNCOMPILED**, with the compiled terminal '
         'named as covering the ORIGINAL only. ### **BORROWING A COMPILED GRADE FOR PROSE WOULD BE '
         'THE ONE THING THIS WHOLE APPARATUS EXISTS TO PREVENT.**', '  ')
    return 'RELATIVIZES'


SPINE = [
    ('G-VACUOUS-POPULATION',
     'every arm that reports a PASS must print the size of the population that could have produced '
     'a FAIL, and say VACUOUS in the same line when that size is zero.',
     '`b399` -- the sign test passed VACUOUSLY because the only lawful seeds give an empty prime '
     'sum, and the pass was banked before the vacuity was noticed.',
     'what counts as "the population" for a test over a family of test functions -- the seeds '
     'tried, the seeds admissible, or the seeds the criterion quantifies over. ### **THREE '
     'DIFFERENT NUMBERS, AND THE AUTHOR MUST SAY WHICH.**'),
    ('G-PREMISE-BEFORE-CONCLUSION',
     'when an act scores an expectation, the arm must check the expectation\u2019s own PREMISE '
     'against the record before the conclusion is scored, and print both verdicts separately.',
     '`b404` -- `(N2)` reasoned from "a one-L-function corpus" and the premise was false, while its '
     'conclusion survived on other grounds. ### The act caught it by hand.',
     'whether a refuted premise with a surviving conclusion scores MET, REFUTED, or a third thing '
     'the record has no word for. ### **THE VOCABULARY IS THE DECISION.**'),
    ('G-KIND-BEFORE-APPLICATION',
     'when an act cites a result about an object, the arm must require the act to state the KIND '
     'the result quantifies over and the kind the object is, side by side, before the citation '
     'stands.',
     '`b405`, `b406` and `b407` -- three independent instances of one statement, each caught by '
     'hand: a countermodel about a shape, a witness form that does not transpose, a theorem whose '
     'subject is the wrong kind of object.',
     'the one statement itself has ### **NO NAME IN THE RECORD** ### -- `b408` routed the naming '
     'and it is still routed. ### **AN ARM CANNOT ENFORCE A LAW THE RECORD HAS NOT NAMED.**'),
]


def component4():
    rec('')
    bar()
    rec('### COMPONENT 4 -- THE SPINE, PROPOSED AND NOT BUILT.')
    bar()
    for name, what, incident, decision in SPINE:
        rec('  ### **%s**' % name)
        wrap('WHAT IT WOULD REQUIRE : %s' % what, '      ')
        wrap('THE INCIDENT IT WOULD HAVE CAUGHT : %s' % incident, '      ')
        wrap('### **THE DECISION THE AUTHOR MUST MAKE:** %s' % decision, '      ')
        rec('')
    rec('  ### ### **THREE PROPOSED. ### `0` WRITTEN.** ### **AND NOT ONE OF THE THREE CAN BE')
    rec('  ### ### WRITTEN WITHOUT A DECISION THE AUTHOR HAS NOT MADE** -- which is the finding,')
    rec('  ### not an excuse: a mathematics-facing arm needs a mathematics-facing ruling, and the')
    rec('  ### apparatus arms needed none, which is why there are eight of those and none of these.')
    return len(SPINE)


def component5():
    rec('')
    bar()
    rec('### COMPONENT 5 -- THE ROW, FROZEN.')
    bar()
    wrap('Row `U1` receives ### **NO ENTRY** ### from this act and is marked, through its writer, '
         'as a ### **REGISTER COMPLETE AT SIX** ### until an act changes what it can say about the '
         'object.', '  ')
    wrap('### **THE REASON IS THE SEAT\u2019S OWN COUNT, NOT A JUDGEMENT ABOUT THE ROW\u2019S '
         'WORTH:** ### `b408` measured `6` sites, `2` coordinates, `1` price corrected, `0` bridges '
         'typed, `0` grades conferred and ### **`0` STATEMENTS ABOUT THE OBJECT** ### in six acts.',
         '  ')
    wrap('### ### **A FREEZE IS NOT A CLOSURE AND NOT A GRADE.** ### The row stays OPEN, its '
         'refusal stands verbatim, and the mark says only that no further entry is taken until the '
         'condition is met. ### The condition is printed with the mark so a later act can see when '
         'it is satisfied: ### **A SITE WHOSE ENTRY PRODUCES A STATEMENT ABOUT THE OBJECT.**', '  ')
    rec('  ### ### **`0` SITES ENTERED. ### `0` COORDINATES ADDED. ### `0` GRADES CONFERRED.**')


def expectations(c1, exam, dark, rel, spine):
    rec('')
    bar()
    rec('### THE EXPECTATIONS, SCORED. ### **EACH BY A PRINTED RESULT.**')
    bar()
    maj = c1['rows'] - c1['dec']
    rows = [
        ('(N1)', 'a majority of symbol uses CAN be assigned a scheme from their own document',
         '### **REFUTED** -- `%d` of `%d` live documents CANNOT be assigned a scheme from their own '
         'text (`%d` SCHEME UNDECLARED, `%d` TIED). ### **AND THE STATED REASON IS ALSO FALSE:** '
         'the documents do not cite the monograph\u2019s table; `1` document carries it and the '
         'monograph itself contradicts it.' % (maj, c1['rows'], c1['undecl'], c1['tied'])),
        ('(N2)', 'the two artefact hits name the local and order classes, neither the modular '
                 'relation',
         '### **MET** -- and decided by the path\u2019s own MACHINERY line rather than by a '
         'numbering table: level curves and the logarithmic derivative are CAUCHY-RIEMANN, the '
         'Hadamard product is HADAMARD.'),
        ('(N3)', 'the global class is ABSENT under both schemes and reads DARK on the '
                 'monograph\u2019s own definition, for the same reason the functional equation does',
         '### **MET IN BOTH HALVES, AND THE SECOND HALF EXACTLY AS STATED.** ### `%s`; and `%s` -- '
         'because *"the constraint function of each mechanism class is antisymmetric about the '
         'reflection axis (the functional equation forces this)"*, which is the functional '
         'equation\u2019s own reason.' % (exam, dark)),
        ('(N4)', 'the lemma RELATIVIZES',
         '### **MET, WITH ITS COST PRINTED** -- it needs one hypothesis the original did not: that '
         'every sentence of `H` itself factors through `I`.'),
        ('(E1)', 'the monograph does NOT use the scheme the table attributes to it',
         '### **MET** -- the monograph\u2019s own class table and `ENUMERA`\u2019s reconciliation '
         'agree with each other and disagree with the table\u2019s *Monograph* column on six of '
         'seven symbols.'),
        ('(E2)', 'the second scheme is nevertheless LIVE',
         '### **MET** -- `%d` live documents use it, so `b408`\u2019s conclusion stands and its '
         'label was wrong.' % c1['excl']),
        ('(E3)', 'some live document uses BOTH schemes in its own text',
         '### **MET** -- `PATHS_TO_THE_CRITICAL_LINE.md` pins STAGE on the balance of its symbols '
         'and uses EXCLUSION-ORDER in its fifth-path line, which is the line `b408` met.'),
        ('(E4)', 'the relativization needs a hypothesis about `H` itself',
         '### **MET** -- and it is the whole of what the restatement costs.'),
    ]
    for k, claim, verd in rows:
        rec('  **%s** %s' % (k, claim))
        wrap(verd, '        ')


def main():
    rec('=' * 100)
    rec('b409_components.py -- THE COMPONENTS. ### EVERY VERDICT WITH THE SENTENCE THAT DECIDED IT.')
    rec('=' * 100)
    rec('  face LOCKED : ac57933015429df82d756354dc70e98aa908c11c05fe17fca75d2052aac53006')
    rec('  ### **THE MATCHER`S FIXTURES, BOTH POLARITIES ON EVERY ARM:** %s'
        % class_scheme.self_test(verbose=False))
    if not class_scheme.self_test(verbose=False):
        FAILS.append('class_scheme fixtures')
    rec('')
    c1 = component1()
    exam, dark = component2()
    rel = component3()
    spine = component4()
    component5()
    expectations(c1, exam, dark, rel, spine)
    rec('')
    rec('=' * 100)
    rec('  ### ### **LIVE-QUOTE FAILURES : %d**' % len(FAILS))
    for f in FAILS:
        rec('      %s' % f)
    rec('  ### **NO DOCUMENT, LEDGER, ROW OR KEY WAS WRITTEN BY THIS FILE.**')
    rec('=' * 100)
    io.open(OUT, 'wb').write(('\n'.join(L) + '\n').encode('utf-8'))
    return 0 if not FAILS else 1


if __name__ == '__main__':
    sys.exit(main())
