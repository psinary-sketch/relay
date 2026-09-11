# -*- coding: utf-8 -*-
"""b420_components.py -- THE PROOF CITED, THE LOCK RULED, AND THE LEMMA AIMED AT THE RIGHT OBJECT.

### ### **EACH MODE WRITES ITS OWN RECORD, IN THE ORDER THE FACE GIVES:**
###   --c1-kernel   Component 1: the two annotations INSERTED in SinglePrimeFactor.lean (the rebuild is the
###                 shell's, recorded separately).
###   --c1-verify   Component 1: the words survive, the profile is byte-identical to the pin's.
###   --c1-record   Component 1: every target listed with what it says beside what is compiled.
###   --c2          Component 2: the step between the model and the source's trace, priced in two parts.
###   --c3          Component 3: b419's kernel-write clauses re-read against the build procedure.
###   --c4          Component 4: the barrier lemma put to positivity -- instance, hypotheses, verdict, (d).
###   (no flag)     the report.
### ### **EVERY QUOTATION IS PULLED FROM ITS FILE AT RUN TIME**, so a quote that is not in its source is a
### MISS and not a sentence.
"""
import hashlib
import io
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERN = os.path.join('D:', os.sep, 'SIDE-global-section')
PIN_SIDE = '9ea4d92'
SPF = os.path.join(KERN, 'Core', 'SinglePrimeFactor.lean')
SEAL = os.path.join(KERN, 'Core', 'FiniteSideSeal.lean')
SMG = os.path.join(KERN, 'Core', 'SmearGeneral.lean')
PROF = os.path.join(KERN, 'AXIOM_PRINTS.txt')
CORR = os.path.join(KERN, 'CORRESPONDENCE.md')
IB = os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')
FL = os.path.join(PP, 'FACES_LEDGER.md')
NL = chr(10)
MISS = []

ANCHOR1 = "occurrences of `sorry` and this module adds none."
ANN1 = ('\n\n  ANNOTATION, b420 -- APPENDED; EVERY WORD ABOVE IS KEPT AS THE RECORD OF WHAT\n'
        '  b414 KNEW. THE STATEMENT ABOVE IS NOW PROVED: `SmearGeneral.smear_general`\n'
        '  (`Core/SmearGeneral.lean`, b419) states it for every base with\n'
        '  `singlePrimeFactor p = true` and every level, and its printed profile reads\n'
        '  "does not depend on any axioms". It is a theorem about this model\'s counting\n'
        '  form; the identification with the source\'s trace is b310\'s and is still NOT\n'
        '  compiled (see `FiniteSideSeal`\'s WHAT IT DOES NOT CERTIFY).')
ANCHOR2 = "than competing with it — and this act does not prove it."
ANN2 = ('\n    ANNOTATION, b420: `SmearGeneral.cells_are_instances` (b419) now derives these\n'
        '    seven cells from the proved statement.')


def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def rb(p):
    with open(p, 'rb') as fh:
        return fh.read()


def read(p):
    try:
        return rb(p).decode('utf-8', 'replace')
    except Exception:
        return ''


def put(name, lines):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(lines) + NL)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def blob(repo, path, rev):
    return subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True).stdout


def wrap(text, width):
    out, line = [], ''
    for w in (text or '').split(' '):
        if line and len(line) + 1 + len(w) > width:
            out.append(line)
            line = w
        else:
            line = (line + ' ' + w) if line else w
    if line:
        out.append(line)
    return out


def q(path, start, end=None, cap=700):
    """### A QUOTATION PULLED FROM ITS FILE, WHITESPACE FOLDED; A MISS IS COUNTED, NEVER SMOOTHED."""
    src = read(path)
    i = src.find(start)
    if i < 0:
        MISS.append('%s : %r' % (os.path.basename(path), start[:48]))
        return '### MISS'
    j = src.find(end, i + len(start)) if end else -1
    return re.sub(r'\s+', ' ', src[i:j + len(end)] if j > i else src[i:i + cap]).strip()


def block(R, label, text, width=100, lead='      | '):
    R.append('  ' + label)
    R.extend(lead + s for s in wrap(text, width))


def prose(R, text, width=104):
    R.extend('  ' + s for s in wrap(text, width))


# =============================================================================================
# ### COMPONENT 1 -- THE PROOF CITED.
# =============================================================================================
def run_c1_kernel():
    R = ['=' * 100, 'b420 COMPONENT 1 -- THE ANNOTATIONS, INSERTED.', '=' * 100, '  at (UTC) : %s' % utc()]
    src = read(SPF)
    old = blob(KERN, 'Core/SinglePrimeFactor.lean', PIN_SIDE).decode('utf-8')
    if src != old:
        R.append('  ### REFUSED: the working file is not its blob at the pin -- nothing written.')
    elif src.count(ANCHOR1) != 1 or src.count(ANCHOR2) != 1:
        R.append('  ### REFUSED: an anchor does not occur exactly once (%d, %d).' % (src.count(ANCHOR1), src.count(ANCHOR2)))
    else:
        new = src.replace(ANCHOR1, ANCHOR1 + ANN1, 1).replace(ANCHOR2, ANCHOR2 + ANN2, 1)
        open(SPF, 'wb').write(new.encode('utf-8'))
        R += ['  written : Core/SinglePrimeFactor.lean ; sha %s -> %s ; lines %d -> %d'
              % (sha(src.encode())[:16], sha(new.encode())[:16], len(src.splitlines()), len(new.splitlines())),
              '  ### annotation 1, after the paragraph naming the statement OPEN :']
        R += ['      | %s' % x for x in ANN1.strip(NL).splitlines()]
        R.append('  ### annotation 2, inside the cells` docstring, after *this act does not prove it.* :')
        R += ['      | %s' % x for x in ANN2.strip(NL).splitlines()]
    R.append('=' * 100)
    put('b420_c1_kernel.txt', R)
    print(NL.join(R))
    return 0 if 'written :' in NL.join(R) else 2


def run_c1_verify():
    R = ['=' * 100, 'b420 COMPONENT 1 -- VERIFIED AFTER THE REBUILD.', '=' * 100, '  at (UTC) : %s' % utc()]
    fails = []
    old = blob(KERN, 'Core/SinglePrimeFactor.lean', PIN_SIDE)
    new = rb(SPF)
    back = new.decode('utf-8').replace(ANN1, '', 1).replace(ANN2, '', 1).encode('utf-8')
    to, tn = old.decode('utf-8').split(), new.decode('utf-8').split()
    ta1, ta2 = ANN1.split(), ANN2.split()
    k1 = next((i for i in range(len(to) + 1) if tn[:i] == to[:i] and tn[i:i + len(ta1)] == ta1), None)
    k2 = None
    if k1 is not None:
        rest_o, rest_n = to[k1:], tn[k1 + len(ta1):]
        k2 = next((i for i in range(len(rest_o) + 1) if rest_n[:i] == rest_o[:i] and rest_n[i:i + len(ta2)] == ta2
                   and rest_n[i + len(ta2):] == rest_o[i:]), None)
    R += ['### SinglePrimeFactor.lean.',
          '  removing exactly the two inserted texts returns the pin`s bytes : %s' % (back == old),
          '  ### ### **EVERY WORD AT THE PIN SURVIVES, IN ORDER, AND THE ONLY WORDS ADDED ARE THE TWO ANNOTATIONS : %s**'
          % (k1 is not None and k2 is not None),
          '  words : pin %d, now %d, added %d' % (len(to), len(tn), len(ta1) + len(ta2))]
    fails += [] if (back == old and k1 is not None and k2 is not None) else ['words']
    pold = blob(KERN, 'AXIOM_PRINTS.txt', PIN_SIDE)
    pnew = rb(PROF)
    same = pold == pnew
    R += ['', '### THE PROFILE.',
          '  pin blob %d bytes sha %s ; regenerated %d bytes sha %s' % (len(pold), sha(pold)[:16], len(pnew), sha(pnew)[:16]),
          '  ### ### **THE REGENERATED PROFILE IS BYTE-IDENTICAL TO THE PIN`S : %s** ### (so no terminal was added or moved)' % same]
    fails += [] if same else ['profile']
    R += ['', '### THE FILES THAT MUST NOT MOVE, BY GIT`S OWN VIEW AGAINST THE PIN.']
    for f in ('Core/FiniteSideSeal.lean', 'Core/SmearGeneral.lean', 'AllPrints.lean', 'AXIOM_PRINTS.txt'):
        ok = subprocess.run(['git', '-C', KERN, 'diff', '--quiet', PIN_SIDE, '--', f]).returncode == 0
        R.append('  %-28s unchanged : %s' % (f, ok))
        fails += [] if ok else [f]
    cl = sha(rb(os.path.join('D:', os.sep, 'SIDE-formation-arithmetic', 'SIDEFormationArithmetic', 'Classes.lean')))
    R.append('  %-28s sha %s ; the before-digest d4f931db1d50c01f : %s' % ('Classes.lean', cl[:16], cl.startswith('d4f931db1d50c01f')))
    fails += [] if cl.startswith('d4f931db1d50c01f') else ['Classes']
    code = re.sub(r'--[^\n]*', ' ', re.sub(r'/-.*?-/', ' ', new.decode('utf-8'), flags=re.S))
    R.append('  `sorry` as a term in SinglePrimeFactor.lean : %d' % len(re.findall(r'\bsorry\b', code)))
    R += ['', '### ### **VERIFY FAILURES : %d %s**' % (len(fails), fails), '=' * 100]
    put('b420_c1_verify.txt', R)
    print(NL.join(R))
    return 1 if fails else 0


def run_c1_record():
    R = ['=' * 100, 'b420 COMPONENT 1 -- THE RECORDS THE PROOF DATES, EACH BESIDE WHAT IS COMPILED.', '=' * 100]
    stmt = q(SMG, 'theorem smear_general', ':= by')
    R.append('### WHAT IS COMPILED, QUOTED FROM THE MODULE:')
    R.append('      | %s' % stmt)
    R.append('      | profile: %s' % next((x for x in read(PROF).splitlines() if x.startswith("'SmearGeneral.smear_general'")), '### MISS'))
    R += ['', '### TARGET 1 -- SinglePrimeFactor.lean. ### ANNOTATED BY INSERTION (b420_c1_kernel.txt).']
    block(R, 'what it says (at the pin) :', q(SPF, 'THIS IS NOT PROVED HERE AND NOTHING BELOW', 'PROVING IT.'))
    block(R, 'and :', q(SPF, 'IF ANYONE PROVES IT', 'this act does not prove it.'))
    prose(R, '### WHAT IS NOW TRUE: the statement it names is `smear_general`, compiled at zero axioms. ### Both sentences '
          'stay: *not proved here* is still true of this module, and *this act does not prove it* is true of b414.')
    corr = read(CORR)
    m = [(int(x.group(1)), x.start()) for x in re.finditer(r"(?m)^\| (\d+) \| \*\*THE KERNEL'S OWN HEADER NAMED THE MISSING", corr)]
    R += ['', '### TARGET 2 -- CORRESPONDENCE ROW 263 (b414), FOUND BY ITS MARKER : %s. ### NOT EDITED.' % [r for r, _ in m]]
    if m:
        row = corr[m[0][1]:corr.find(NL, m[0][1])]
        opn = re.search(r'[^.]{0,160}(NAMED OPEN STATEMENT|OPEN STATEMENT)[^.]{0,200}', row)
        block(R, 'what it says of the statement :', opn.group(0) if opn else '### MISS')
    prose(R, '### IT IS ANNOTATED BY THIS ACT`S APPENDED ROW, which names row 263 by its marker and records that the '
          'statement it carries OPEN is `SmearGeneral.smear_general`, PROVED at b419 (row 268). ### Row 263`s bytes '
          'are unchanged, under the table`s own append-only law.')
    R += ['', '### TARGET 3 -- THE EIGHT SENTENCES b419 RE-CLASSIFIED QUALIFIED BY THE PROOF. ### ANNOTATED HERE.',
          '  ### They live in banked ferries, and a banked ferry is never edited; so the annotation is this record. ###',
          '  ### The adopted draft called them *corpus sentences*; that was the executor`s misnomer, and none is in',
          '  ### PLACE-papers.']
    tw = read(os.path.join(D, 'b419_twentyeight.txt')).splitlines()
    b414 = read(os.path.join(D, 'b414_components.txt')).splitlines()
    rows = [x for x in tw if 'QUALIFIED BY THE PROOF   b414:' in x]
    for x in rows:
        n, f = x.split()[0], x.split()[1]
        k = next((i for i, y in enumerate(b414) if re.match(r'\s+%s\s+%s' % (re.escape(n), re.escape(f)), y)), None)
        sent = b414[k + 1].strip() if k is not None and k + 1 < len(b414) else '### MISS'
        R += ['  row %-3s %s (ferry banked: %s)' % (n, f, os.path.exists(os.path.join(D, f))),
              '      what it says  | %s' % sent[:150],
              '      now compiled  | QUALIFIED BY `SmearGeneral.smear_general`: true at every base with a single prime',
              '                    | factor and every level, for the model`s counting form; the identification with the',
              '                    | source`s trace is b310`s and uncompiled (Component 2).']
    R += ['', '  QUALIFIED sentences listed beside their terminal : %d' % len(rows), '=' * 100]
    put('b420_c1_record.txt', R)
    print(NL.join(R))
    return 0 if len(rows) == 8 and not MISS else 1


# =============================================================================================
# ### COMPONENT 2 -- THE PROOF'S REACH, PRICED IN THE RECORD'S OWN TWO PARTS.
# =============================================================================================
def run_c2():
    R = ['=' * 100, 'b420 COMPONENT 2 -- WHAT SEPARATES THE MODEL`S ARITHMETIC FROM THE SOURCE`S TRACE, PRICED.', '=' * 100]
    s310 = os.path.join(D, 'b310_the_smear_collapses.txt')
    block(R, 'WHAT IS COMPILED (the seal) :', q(SEAL, 'WHAT IT DOES NOT CERTIFY.', 'NOT COMPILED HERE.'))
    block(R, 'THE KERNEL`S CHARACTER (SinglePrimeFactor`s head) :', q(SPF, 'Lean 4 (v4.29.1, pinned)', 'never assumed.'))
    block(R, 'THE IDENTIFICATION, AS b310 REGISTERED IT :',
          q(os.path.join(D, 'b310_registration_2026-09-03.txt'), '`Tr(theta(t) Pi) = |t| * ( A_N(t) - (1/q) A_q(t) )`', '(t - 1) s = 0 mod M }`.**'))
    block(R, 'b310`s route :', q(s310, 'the assembly is `SUM_k w_k Tr(theta(p^k) Pi)`, and the frame algebra fixes', 'containing source and target;'))
    block(R, 'and the weight :', q(s310, 'The factor is the ### HAAR WEIGHT OF', None, cap=260))
    R += ['',
          '### ### **THE RECORD DRAWS THE STEP IN TWO PARTS, AND EACH IS PRICED BY WHAT ITS STATEMENT MUST MENTION.**',
          '',
          '  PART (i) -- ON THE FINITE AMBIENT: *Tr(theta(t) Pi) is a signed count of the off-ball points t fixes*.',
          '      must mention : functions on the grid Z/p^(2n); the scaling operator s -> t*s; the object`s projection Pi',
          '                     in finite form; and a trace, as the sum of the diagonal entries over the grid.',
          '      in the kernel today : the grid, the ball, both congruence counts and the signed count itself',
          '                     (`offBallFixed`, `signedTrace`, which already clears the 1/q by multiplying through by q).',
          '      what it lacks : a DEFINITION of the operator on grid functions and of its trace. ### Both are finite',
          '                     sums over `List.range (gridN p n)` with Int entries, the kind of definition this module',
          '                     family already writes by hand; nothing in them needs a real number, a limit or a choice.',
          '      ### ### **PRICE : ONE LEMMA, IN THE KERNEL`S PRESENT CHARACTER -- AFTER NEW DEFINITIONS OF THE FINITE',
          '      ### ### OPERATOR AND ITS TRACE.** ### Not attempted; no probe compiled.',
          '',
          '  PART (ii) -- THE SOURCE`S FRAME CARRIED TO THAT AMBIENT, WITH THE EMBEDDING`S HAAR WEIGHT.',
          '      must mention : the source`s space at the finite place and its scaling action; a projection on it; the',
          '                     Haar weight of the embedding (`p^{-max(k,0)}` in b310`s words); and the trace on an',
          '                     infinite-dimensional space that the frame algebra reduces to the finite one.',
          '      in the kernel today : none of these. ### The kernel`s character is `Nat`, `Int`, lists and hand-rolled',
          '                     lemmas; a measure, a completed space of functions and a trace on it are not definable',
          '                     there without real analysis.',
          '      ### ### **PRICE : A QUESTION THE KERNEL IN ITS PRESENT CHARACTER CANNOT STATE. ### THE CHEAPEST ROUTE TO',
          '      ### ### STATING IT IS A MATHLIB IMPORT, WHICH CHANGES THAT CHARACTER** (the library`s analysis carries',
          '      propext and Quot.sound at the least, per the seal`s axiom finding). ### Whether the pinned Mathlib',
          '      supplies every object this part mentions is NOT READ BY THIS ACT, ### **SO THE IMPORT IS A FLOOR ON THE',
          '      ### PRICE, NOT A QUOTE FOR IT.**',
          '',
          '### ### **THE DRAFT`S `(N1)`** -- *the identification in Component 2 prices as NOT STATABLE in the axiom-free',
          '### kernel without a new definition of the trace* -- ### **ITS CLAUSES SCORED APART (R27):**',
          '      as written, the identification is not statable without a new definition of the trace -- ### **MET**:',
          '          neither part is statable today, and part (i) needs exactly that definition (and the operator`s).',
          '      what it implies, that a new definition of the trace would make it statable -- ### **REFUTED AT PART (ii)**:',
          '          the frame`s carriage needs a measure and an infinite-dimensional space, which no definition in the',
          '          present character supplies.',
          '      ### ### **SO THE DRAFT PRICED ONE PART AND NAMED IT THE WHOLE.**',
          '=' * 100]
    put('b420_c2_priced.txt', R)
    print(NL.join(R))
    return 1 if MISS else 0


# =============================================================================================
# ### COMPONENT 3 -- b419'S KERNEL-WRITE CLAUSES, RE-READ.
# =============================================================================================
C3 = [
    (78, '(C)(ii) AllPrints BY APPEND ONLY: its import after the last existing import, its prints at the end',
     'NOT MEETABLE AS WRITTEN', 'its headline APPEND ONLY and its own placement disagree: an import after the last import is an '
     'insertion, since Lean admits `import` only before the first command. The placement was met; the headline was not.',
     'AllPrints.lean: ONE import line INSERTED after the last import; the prints APPENDED at the end; nothing else.'),
    (80, '(C)(iii) AXIOM_PRINTS regenerated as the stdout of `lean AllPrints.lean`, the blob at HEAD a true byte prefix',
     'MEETABLE AS WRITTEN', 'the profile is the driver`s stdout (b314: *lean AllPrints.lean exit 0*); prints appended at the end '
     'of the driver extend its output at the end, so the prior profile can be a prefix. Met at b419.', None),
    (170, 'BAR 3 -- the prior profile a true byte prefix of the new; AllPrints` prior bytes a true prefix of its new ones',
     'NOT MEETABLE AS WRITTEN (its second half)', 'the first half is meetable and was met; the second asks the driver itself '
     'to be append-only, which the import rule forbids. The one b419 found and printed.',
     'the PROFILE`s prior bytes a true prefix of the new; for AllPrints, the prior bytes with one import line inserted a true prefix.'),
    (199, 'KIND 3 -- a new module under Core/', 'MEETABLE AS WRITTEN', 'each module compiles standalone with sibling imports via '
     'LEAN_PATH (the README`s build section). Met at b419.', None),
    (200, 'KIND 4 -- AllPrints.lean, APPEND ONLY', 'NOT MEETABLE AS WRITTEN', 'the same import rule as (C)(ii): a new module`s '
     'import is an insertion, never an append.', 'AllPrints.lean: one import INSERTED after the last import, prints APPENDED.'),
    (201, 'KIND 5 -- AXIOM_PRINTS regenerated, the prior profile a true byte prefix', 'MEETABLE AS WRITTEN',
     'as (C)(iii). Met at b419.', None),
    (203, 'KIND 6 -- FiniteSideSeal.lean, b416`s annotation INSERTED and nothing else', 'MEETABLE AS WRITTEN',
     'an insertion inside a comment moves no declaration`s statement; measured at b419 by word sequence. Met.', None),
    (205, 'KIND 7 -- oleans under build/, ignored and never committed', 'MEETABLE AS WRITTEN',
     'the kernel`s .gitignore names build/ and *.olean. Met.', None),
]


def run_c3():
    R = ['=' * 100, 'b420 COMPONENT 3 -- b419`S KERNEL-WRITE CLAUSES, RE-READ AGAINST THE BUILD PROCEDURE.', '=' * 100]
    f419 = read(os.path.join(D, 'b419_registration_2026-09-11.txt')).splitlines()
    block(R, 'THE PROCEDURE, AS THE KERNEL README WRITES IT :', q(os.path.join(KERN, 'README.md'), 'Core: `lean` at the pinned toolchain', 're-runs every print.'))
    gi = read(os.path.join(KERN, '.gitignore'))
    R.append('  the kernel`s .gitignore names build/ : %s ; *.olean : %s' % ('build/' in gi, '*.olean' in gi))
    R.append('')
    bad = 0
    for ln, what, grade, why, fix in C3:
        text = f419[ln - 1].strip() if ln - 1 < len(f419) else '### MISS'
        R += ['  b419 face line %d | %s' % (ln, text[:120]),
              '      the clause : %s' % what,
              '      ### **%s**' % grade]
        R += ['      ' + s for s in wrap('why : ' + why, 104)]
        if fix:
            R += ['      ' + s for s in wrap('CORRECTED FORM : ' + fix, 104)]
            bad += 1
    R += ['', '  clauses re-read : %d ; NOT MEETABLE AS WRITTEN : %d ; MEETABLE : %d' % (len(C3), bad, len(C3) - bad),
          '  ### ### **b419 PRINTED ONE OF THE THREE.** ### Its closing named BAR 3; the same wording stood at (C)(ii)`s headline',
          '  ### and at KIND 4, and b419`s arm measured all three by the procedure`s form, which is why none failed there.',
          '  ### ### **THE CORRECTED FORMS ARE BANKED HERE FOR LATER FACES; NO STANDING CLAUSE IS ADDED**, and this act`s own',
          '  ### face (its KIND 5) asks the profile, not the driver, for sameness.',
          '=' * 100]
    put('b420_c3_clauses.txt', R)
    print(NL.join(R))
    return 1 if MISS else 0


# =============================================================================================
# ### COMPONENT 4 -- THE BARRIER LEMMA, APPLIED TO POSITIVITY.
# =============================================================================================
VERDICT_C4 = 'NOT AN INSTANCE'


def run_c4():
    R = ['=' * 100, 'b420 COMPONENT 4 -- THE BARRIER LEMMA, APPLIED TO POSITIVITY AND NOT TO THE REDUCTION.', '=' * 100]
    b400 = os.path.join(D, 'b400_components_run2.txt')
    s310 = os.path.join(D, 'b310_the_smear_collapses.txt')
    R += ['', '### (a) THE INSTANCE, EACH PART QUOTED FROM THE KEYSTONE AND MATCHED TO THE ARC`S OWN OBJECT.']
    block(R, 'the structure -- Definition 2.1 :', q(IB, '**Definition 2.1 (Determined system).**', 'up to isomorphism.'))
    block(R, '    the arc`s object (row S1) :', q(FL, 'S1 -- the clause stated:', "in the arc's vocabulary"))
    prose(R, '    matched by emitting act: the finite places` part is the prime sum `K4` (b306) and the finite places` '
          'contribution `K3` (b329, b310); the archimedean part is `K5` (b320, b315); the sum over places is the '
          'explicit formula`s, as row S1 states it.')
    block(R, 'the interface -- Definition 2.3`s own example :', q(IB, '- For M = ξ(s): I can be the product formula', 'Re(x) = 1/2."'))
    block(R, '    and the keystone`s places, sorted :', q(IB, '**The per-place table.**', 'transmits the density register;'))
    block(R, 'the elements and the target -- Definition 2.3 :', q(IB, '**Definition 2.3 (Target parameter).**', 'universal statement* for P on M.'))
    prose(R, '    the elements are the test functions `g` of the source`s class (`K1`, b328, Definition 3.1 with the '
          'vanishing conditions); the target is row S1`s own sign, `P(g) := SUM_v W_v(g conv g-bar^#) <= 0` (`K2`, b321), '
          '### **ONE `g` AT A TIME, SO UNARY AS DEFINITION 2.3 REQUIRES.** ### The ferry calls it *nonnegativity of the '
          'functional*; the record`s wording is the criterion`s sign `<= 0`, and the two are one condition under the '
          'source`s sign convention. The record`s wording governs (BAR 6).')
    R += ['', '### (b) THE HYPOTHESES, ONE BY ONE -- THE FIVE b407 ENUMERATED.']
    R += ['', '  HYPOTHESIS 1 -- M IS DETERMINED.']
    block(R, '    the keystone asserts it of :', q(IB, '- For M = ξ(s): I can be the product formula', 'Re(x) = 1/2."'))
    prose(R, '    ### **FOR THE STRUCTURE WHOSE ELEMENTS ARE THE CLASS`S TEST FUNCTIONS, THE RECORD HAS NO SENTENCE.** '
          '### Definition 2.1 needs a finite specification S with that structure as its unique model; the keystone`s '
          'examples and Proposition 3.5 name `xi`, whose elements are zeros, and no document writes S for the functional '
          'on the class. ### READING: NOT SUPPLIED BY THE RECORD -- the ferry asserts it; the keystone does not.')
    R += ['', '  HYPOTHESIS 2 -- THE INTERFACE IS THE PRODUCT FORMULA, THE PLACES.']
    prose(R, '    ### **MET AS THE KEYSTONE READS IT**: Definition 2.3 names the product formula for `xi`, and §9`s table '
          'sorts the explicit formula`s terms by the same places.')
    R += ['', '  HYPOTHESIS 3 -- THE TARGET IS A UNARY FORMULA.']
    prose(R, '    ### **MET**: `P(g)` is a property of one test function.')
    R += ['', '  HYPOTHESIS 4 -- EACH INTERFACE IS P-DARK (kappa = 0).']
    block(R, '    Definition 2.4 :', q(IB, 'κ = 0 indicates I is *P-dark*', 'without attenuation.'))
    R.append('    (i) THE FINITE PLACES.')
    block(R, '      the ferry`s description of b419`s clause :', q(os.path.join(D, 'b420_ferry.txt'), 'the general clause proved at b419, which returns', 'nothing about its sign;'))
    block(R, '      b419`s clause in its own words :', q(SMG, 'theorem smear_general', ':= by'))
    block(R, '      the words the ferry describes are b310`s, not b419`s :', q(s310, '### ### **THEREFORE `T(w) = w_0 * (p^n - 1)^2`.**', None, cap=60))
    block(R, '      and b310 locates the arithmetic elsewhere :', q(s310, 'The arithmetic is in the distribution, not in', 'as its prime sum.'))
    prose(R, '      ### **b419`S TERMINAL DOES NOT MENTION A TEST FUNCTION, THE IDENTITY, A DIMENSION OR A SIGN.** It states the '
          'compact part`s smear identity for the model`s counting form. *The weight at the identity times a dimension* is '
          'b310`s `T(w) = w_0 (p^n - 1)^2`, DERIVED-ON-CONTENT, and its identification with the source`s trace is the '
          'uncompiled step Component 2 prices. ### **AND THE FINITE PLACE`S TERM IN THE FUNCTIONAL IS NOT THE COMPRESSED '
          'TRACE AT ALL**: b310 itself says the arithmetic is in the distribution `W_p`, which reads the test function at '
          'the prime`s powers. ### So b419`s clause cannot certify the finite places` darkness for `P`, and does not. '
          '### What remains is the keystone`s own reading -- *every single-place row ... transmits the density register* '
          '-- ### **ASSERTED BY THE KEYSTONE, AT A READING`S GRADE, WITH NO CERTIFICATE FOR ANY FINITE ROW** (b410: of the '
          'single-place rows *exactly 1 is certified*, the archimedean bright half).')
    R.append('    (ii) THE ARCHIMEDEAN PLACE.')
    block(R, '      the calibration family`s row :', q(IB, '**The archimedean row.**', 'not a new theorem.'))
    prose(R, '      ### **ASSERTED, AT THE ROW`S OWN GRADE -- A MANUSCRIPT-RESIDENT STRUCTURAL READING**, its dark half`s '
          'certificate named as *the standing barrier corpus*. ### And the table puts `P` in that register by name: *the '
          'one placement cell in the table is the sign of the joint quadratic functional*.')
    block(R, '      printed and not decided -- a bound through this place on a sub-class :', q(b400, '### **THEOREM 1 CARRIES A SUPPORT HYPOTHESIS**', 'theta(g)*)."*'))
    prose(R, '      ### Theorem 1 is a BOUND on its support class, not the sign `P`; ### **WHETHER IT DECIDES `P` ON THAT '
          'SUB-CLASS IS NOT STATED BY THE RECORD**, and this act does not derive it. Were `P` held universally there by a '
          'proof, Corollary 3.6 would place a bright channel on that sub-class; the record says neither.')
    prose(R, '    ### HYPOTHESIS 4 IN ONE LINE: **MET AT THE KEYSTONE`S READING GRADE AT EVERY PLACE, CERTIFIED AT NONE FOR '
          'THE PLACEMENT REGISTER, AND NOT SUPPLIED BY b419`S TERMINAL**, which is about the counting form and not about '
          '`W_p`.')
    R += ['', '  HYPOTHESIS 5 -- THE PROOF`S FORM.']
    block(R, '    Theorem 3.1 quantifies over :', q(IB, '**Theorem 3.1 (Sieve Ceiling Lemma).**', '(∀x ∈ M: P(x)).*'))
    block(R, '    and a proof factors only if :', q(IB, '**Proof π factors through I for P** if every inference step', 'for P.'))
    block(R, '    the arc`s positivity argument, constituent by constituent (row S1) :',
          q(FL, 'THE GRADE TABLE, each grade its owner\'s:', 'UNOWNED, the clause itself.'))
    prose(R, '    ### **IT IS NOT A CHAIN THE LEMMA QUANTIFIES OVER. IT IS A TABLE OF CONSTITUENTS AT THEIR OWNERS` GRADES**: '
          'the sign itself (`K2`) and the class (`K1`) IMPORTED UNDER THE BAR and MEASURED ON FAMILIES; the archimedean '
          'distribution (`K5`) MEASURED AT COVERED CELLS; the decomposition (`K6`) imported and measured; the prime sum '
          '(`K4`) and one grade of `K3` DERIVED ON CONTENT; and ### **THE QUANTIFIER OVER THE CLASS (`K8`) UNOWNED -- *THE '
          'CLAUSE ITSELF***. ### b419 moved one grade inside `K3`, from per-cell to general, for the model`s counting '
          'form; ### **IT DID NOT TURN A MEASUREMENT INTO AN INFERENCE STEP, AND IT DID NOT SUPPLY `K8`.**')
    block(R, '    b407`s sentence, which governs here as it governed the reduction :',
          q(os.path.join(D, 'b407_the_barriers_own_instance.txt'), '### ### **AN IMPORT UNDER THE', 'HAS NOT DISCHARGED.**'))
    prose(R, '    ### **AND WHAT AIMING AT THE RIGHT-HAND SIDE DID BUY, SAID IN THE SAME PLACE**: b410`s obstacle is gone. '
          'Proposition C.1 is not imported by a proof of the sign alone, so the non-factoring sentence b410 named is not in '
          'this `H`. ### **THE OBSTACLE THAT REMAINS IS b407`S, NOT b410`S: WHAT A PROOF IS.**')
    R += ['', '### (c) THE VERDICT.',
          '  ### ### ### **%s -- THE FIFTH HYPOTHESIS FAILS, AND IT FAILS ON FORM.**' % VERDICT_C4]
    prose(R, '  ### The failing hypothesis, quoted: *Let π be a formal first-order proof in ZFC ∪ S ... If π factors through I '
          'for P* -- with *every inference step*. The arc`s positivity argument is measurements at cells and on families, '
          'imports under the bar, derivations on content, one compiled counting form, and an unowned quantifier; ### '
          '**NONE OF THOSE BUT THE COMPILED FORM IS AN INFERENCE STEP, AND THE STEP THE UNIVERSAL NEEDS IS THE ONE NO '
          'CONSTITUENT OWNS.** ### Two further readings are printed, not scored as the verdict: hypothesis 1 is NOT '
          'SUPPLIED by the record for this structure, and hypothesis 4 holds only at a reading`s grade and not by b419`s '
          'terminal.')
    prose(R, '  ### **AND THE LEMMA STILL SAYS SOMETHING, IN ITS OWN WORDS, THAT THIS ACT DOES NOT FILE AS AN INSTANCE**: of '
          'any FUTURE formal proof of the sign that factors through the places, Theorem 3.1 says it cannot certify every '
          'test function. That is the lemma`s statement, not a fact about the arc, and ### **0 ENTRIES ARE WRITTEN TO ROW '
          'U1** (BAR 8).')
    R += ['', '### (d) THE COMPARISON -- PRINTED, NOT CLAIMED.']
    lem = q(IB, '*That is: π can establish', 'individual elements.*')
    amap = q(os.path.join(D, 'b334_the_aim_map.txt'), '### ### **(1) FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN', 'NOTHING MORE.**')
    # ### REPAIRED AFTER RUN 1 (kept as b420_c4_barrier_run1.txt): the ferry file wraps between *every aim* and
    # ### *inside the margin*, so the anchor starts after the break and the quote is taken from the aim map's name on.
    fer = q(os.path.join(D, 'b420_ferry.txt'), 'the aim map measured — every aim', 'at any height.')
    R += ['  THE LEMMA`S PREDICTED REACH    | %s' % lem,
          '  WHAT THE AIM MAP MEASURED      | %s' % amap,
          '  (the ferry`s paraphrase of it) | %s' % fer]
    prose(R, '  ### **THE WORDING DIFFERS, AND THE SOURCE GOVERNS:** the map says *at every aim AT THIS REACH* and *nothing '
          'more* -- fourteen heights by seven abscissae and 28 lawful seeds per leg -- where the paraphrase says *at any '
          'height*.')
    prose(R, '  ### ### **DO THEY DESCRIBE ONE FACT? NO -- TWO FACTS OF TWO KINDS.** The lemma`s sentence bounds what a '
          'class of PROOFS can establish over an infinite class: density one in each class, never an individual element. '
          'The map`s sentence is a finite MEASUREMENT that certifies individual elements -- each of 28 seeds, by the '
          'noise-floor gate. A finite set has density zero in an infinite class, so the map neither instantiates nor tests '
          'the lemma`s reach; and the lemma quantifies over proofs, so it neither predicts nor explains a passed test. '
          '### **THEY ARE CONSISTENT, AND CONSISTENCY BETWEEN A BOUND ON PROOFS AND A FINITE MEASUREMENT IS NOT ONE FACT.**')
    R += ['', '### THE EXPECTATIONS, THEIR CLAUSES APART (R27).',
          '  (N2) premise, clause 1 -- *the finite-place chain is now a theorem* -- ### **REFUTED AS STATED**: b419 made the',
          '       model`s counting form general; `K3`s identification with the source (b310) is uncompiled, and the',
          '       finite place`s term in the functional is `W_p` (`K4`), derived on content and imported, not proved.',
          '  (N2) premise, clause 2 -- *only the archimedean step is measured* -- ### **REFUTED**: `K1`, `K2` and `K6` are',
          '       measured too, and `K8` is unowned.',
          '  (N2) conclusion -- *INSTANCE, the fifth met on form* -- ### **REFUTED**: NOT AN INSTANCE, the fifth failing on form.',
          '  (N3) -- *the two sentences in (d) describe one fact* -- ### **REFUTED**: two facts of two kinds, consistent.',
          '=' * 100]
    put('b420_c4_barrier.txt', R)
    print(NL.join(R))
    return 1 if MISS else 0


def main():
    L = []
    say = L.append
    recs = {nm: read(os.path.join(D, f)) for nm, f in (
        ('kernel', 'b420_c1_kernel.txt'), ('build', 'b420_kernel_build.txt'), ('verify', 'b420_c1_verify.txt'),
        ('record', 'b420_c1_record.txt'), ('c2', 'b420_c2_priced.txt'), ('c3', 'b420_c3_clauses.txt'),
        ('c4', 'b420_c4_barrier.txt'))}
    fails = [nm for nm, t in recs.items() if not t]
    say('=' * 100)
    say('b420_components.py -- THE PROOF CITED, THE LOCK RULED, AND THE LEMMA AIMED AT THE RIGHT OBJECT.')
    say('=' * 100)
    say('')
    say('### (R36) -- ROUTE (1), EXECUTED AS WRITTEN. ### No tool changed; the mismatch is an instrument item in the trail,')
    say('### its trigger *the author opens an instrument lane*; the lane is not opened.')
    say('')
    say('### COMPONENT 1 -- THE PROOF CITED.')
    for needle in ('removing exactly the two inserted texts returns the pin`s bytes : True',
                   'THE ONLY WORDS ADDED ARE THE TWO ANNOTATIONS : True',
                   'BYTE-IDENTICAL TO THE PIN`S : True', 'VERIFY FAILURES : 0',
                   'QUALIFIED sentences listed beside their terminal : 8'):
        ok = needle in recs['verify'] + recs['record']
        fails += [] if ok else ['c1:' + needle[:30]]
        say('  %-80s %s' % (needle[:80], ok))
    say('')
    say('### COMPONENT 2 -- PRICED. ### Part (i): ONE LEMMA after new definitions of the finite operator and its trace.')
    say('### Part (ii): NOT STATABLE IN THE PRESENT CHARACTER; a Mathlib import is the floor of its price, not a quote.')
    say('')
    say('### COMPONENT 3 -- %s' % next((x.strip() for x in recs['c3'].splitlines() if 'clauses re-read :' in x), '### MISS'))
    say('')
    say('### COMPONENT 4 -- ### **VERDICT : %s** -- the fifth hypothesis fails, on form.' % VERDICT_C4)
    for x in recs['c4'].splitlines():
        if x.startswith('  THE LEMMA') or x.startswith('  WHAT THE AIM') or x.startswith('  (the ferry') or x.startswith('  (N'):
            say(x)
    say('')
    say('### THE COMPONENTS` OWN TALLY : RECORD FAILURES %d %s' % (len(fails), fails))
    say('=' * 100)
    put('b420_components.txt', L)
    print(NL.join(L))
    return 1 if fails else 0


if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.exit(main())
    for flag, fn in (('--c1-kernel', run_c1_kernel), ('--c1-verify', run_c1_verify), ('--c1-record', run_c1_record),
                     ('--c2', run_c2), ('--c3', run_c3), ('--c4', run_c4)):
        if flag in sys.argv:
            sys.exit(fn())
