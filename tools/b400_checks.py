# -*- coding: utf-8 -*-
"""b400_checks.py -- THE GATE SUITE FOR THE BRIDGE RESTATED.

### ### **THE ARM THAT MATTERS MOST IS `G-SCOPE`.** ### This act reaches an IMPOSSIBILITY, and an
### impossibility claimed wider than its argument is a false claim. ### The arm requires the
### scoping word AND the sentence naming what the derivation does not show, ### **IN THE SAME
### ### DOCUMENT AND EACH AS A LIVE LINE.**
###
### ### **`G-ORDERQ` IS AN ARM AGAINST THIS SEAT'S GOOD MANNERS.** ### The order asserted something
### the source contradicts. ### The arm requires the order's own phrase to be QUOTED and the
### correction PRINTED beside it -- ### **AN ORDER IMPROVED IN SILENCE PASSES NO ARM.**
###
### ### **`G-ONEQ` IS A NEGATIVE ARM ON A PERMISSION.** ### The ferry permits one claim only if the
### record's words carry it. ### They do not, so the arm requires the claim to be ABSENT and
### requires the act to say it searched.
###
### ### **`G-PRESERVE` READS THE COMMITTED BLOB, AFTER THE PUSH.** ### Three ledger rows were
### appended to; the arm requires every prior byte of each to be a true prefix of the new cell, and
### requires the preserved `>` quotation of one of those rows to be UNTOUCHED.
###
### ### **EVERY `G-NO*` ARM READS STRIPPED CODE OR WHAT A TOOL PRINTED, NEVER RAW PROSE** (`b348`,
### `b373`); ### **EVERY ARM IS WRITTEN BY CONTENT AND NOT BY ADDRESS** (`(R2)`); ### **EVERY ARM
### ### TESTS A BAR THIS FACE ACTUALLY SET** (`b390`, `b397`); and ### **NO ARM TAKES ITS
### ### POPULATION FROM A NAME PREFIX** (`b397`).
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import banned_terms       # noqa: E402
import ferry_scan         # noqa: E402
import gate_needle as GN  # noqa: E402
import gate_text          # noqa: E402
import hedge_audit        # noqa: E402
import run_clock          # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def raw(n):
    """### **THE TOOL'S OWN BYTES**, because `t()` returns a PATH and an arm testing a substring of
    ### a FILENAME can never pass (`b396`)."""
    return io.open(t(n), encoding='utf-8', errors='replace').read()


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def code(n):
    """### **STRIPPED CODE** for the `G-NO*` arms: string spans removed, so an arm cannot fire on
    ### the act's own sentence saying the thing was not done (`b317`, `b348`)."""
    src = raw(n)
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return src
    spans = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            for k in range(getattr(node, 'lineno', 1), getattr(node, 'end_lineno', 1) + 1):
                spans.add(k)
    return chr(10).join(ln for i, ln in enumerate(src.split(chr(10)), 1) if i not in spans)


FERRY = d('b400_ferry_2026-09-10.txt')
REG = d('b400_registration_2026-09-10.txt')
BANK = d('b400_the_bridge_restated.txt')
XNOTES = d('b400_extract_notes3.txt')
CRUN = d('b400_components_run2.txt')
X = json.load(io.open(d('b400_extract.json'), encoding='utf-8'))
CF = json.load(io.open(d('b400_components.json'), encoding='utf-8'))
LG = json.load(io.open(d('b400_lockgate.json'), encoding='utf-8'))
F = X['fig']
SEAL = LG['face_sha']

# ### **THE ORDER'S OWN CLAUSES.** ### Every needle is built FROM THE FERRY by `b363`'s helper, so
# ### a clause that has drifted cannot be tested against a remembered wording.
OWNER_NEEDLES = [
    ('the fourth verdict is admitted', 'A FOURTH VERDICT ADMITTED'),
    ('the class is prime-free by design', 'THE CLASS IS PRIME-FREE BY DESIGN'),
    ('the source chose its support', 'the source chose its support so no prime'),
    ('the open window', 'THE OPEN WINDOW'),
    ('the window is outside the class',
     'a support wide enough that primes enter, which is outside the'),
    ('no claim unless the record says it', 'unless the record'),
    ('the owed pair rows updated through the writer', 'owed pair-rows are updated through the'),
    ('the deposit`s refusal quoted beside them', 'refusal quoted beside them'),
    ('no equivalence compiled', 'no equivalence compiled'),
    ('(N4) the constraint set forces IMPOSSIBLE', '(N4) the constraint set'),
    ('(N5) no banked lawful seed admits a prime power', 'no banked lawful seed admits a prime'),
    ('nothing deposits', 'nothing deposits'),
]

# ### **THE BANK'S OWN SENTENCES**, each needle built FROM THE BANK.
SELF_NEEDLES = [
    ('the verdict', '(TWO OBJECTS ON THEIR FAMILIES, ONE QUESTION AT THE WINDOW.)'),
    ('the identically-zero constraint', 'SUM_p W_p(f) = 0 IDENTICALLY'),
    ('the obstruction as a new statement', 'NEW STATEMENT ABOUT THE PRIMES'),
    ('the limit of the obstruction', 'it does NOT show that no formula'),
    ('a chosen correspondence is compiled', 'COMPILED, NOT DERIVED'),
    ('the question is not opened', 'NOT OPENED'),
    ('the order`s phrase corrected at source', 'PROPOSITION C.1 CARRIES NONE'),
    ('the window caution keeps its distinction', 'CONSTITUENT SUM_p W_p'),
    ('the lawful census', '0 OF 3 LAWFUL SEEDS ADMIT A PRIME POWER'),
    ('the prior face is not edited', 'THE PRIOR FACE IS NOT EDITED'),
    ('the step-zero incident', 'WRITES WHEN RUN'),
    ('nothing deposits', 'NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED'),
]

R = []


def rec(s=''):
    R.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


ARMS = []


def arm(name, why, ok, detail=''):
    ARMS.append((name, bool(ok)))
    rec('  %-16s %-64s %s' % (name, why[:64], 'PASS' if ok else '### FAIL ###'))
    if detail:
        for k in range(0, min(len(detail), 900), 150):
            rec('      %s' % detail[k:k + 150])
    return bool(ok)


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def main():
    post = '--post' in sys.argv
    bar('=')
    rec('b400_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    rec('### side of the push : %s' % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar('=')
    bank = text(BANK)
    FLAT = gate_text.flat(bank)
    reg = text(REG)
    xn = text(XNOTES)
    crun = text(CRUN)
    RFLAT = gate_text.flat(reg)

    # ---- THE HELPERS' OWN FIXTURES ---------------------------------------------------------------
    bar()
    rec('  ### THE IMPORTED HELPERS` OWN FIXTURES, RUN BEFORE THEIR VERDICTS ARE USED.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and hedge_audit.self_test(False)
        and ferry_scan.self_test(verbose=False))

    # ---- STEP ZERO AND THE FACE ------------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO AND THE FACE.')
    bar()
    arm('G-FERRY', 'the ferry is banked at the bytes and lines the face declares',
        os.path.getsize(FERRY) == 2867 and len(text(FERRY).split(chr(10))) - 1 == 59
        and 'paste ends (part 1 of 1)' in text(FERRY),
        'bytes %d ; lines %d' % (os.path.getsize(FERRY),
                                 len(text(FERRY).split(chr(10))) - 1))
    arm('G-DRAFT', 'the adopted draft is readable at a banked file with its provenance',
        os.path.exists(d('b400_draft_adopted.txt'))
        and 'ACT b400' in text(d('b400_draft_adopted.txt'))
        and 'VERBATIM' in text(d('b400_draft_adopted.txt')))
    arm('G-ANCHOR', 'the extract left no read AMBIGUOUS or ABSENT',
        len(X['reads']) == 23 and all(r['verdict'].startswith('ANCHORED') for r in X['reads']),
        'reads %d ; anchored %d' % (len(X['reads']),
                                    sum(1 for r in X['reads']
                                        if r['verdict'].startswith('ANCHORED'))))
    ok, ln, nd = GN.present(reg, REG, 'sha256 of every byte ABOVE this block')
    rec('    the lock line, anchored : `%s:%d`' % (os.path.basename(REG), ln))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['permits'] is True and LG['gates_read'] == 8
        and LG['face_subject_gates'] == 4,
        'gates read %d ; face-subject %d ; sha %s'
        % (LG['gates_read'], LG['face_subject_gates'], SEAL[:16]))
    arm('G-EVERYGATE', 'every gate the lock read passed, and four were checked by digest',
        LG['gates_read'] == LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)
    sealed_now = hashlib.sha256(reg.split('=' * 100 + chr(10)
                                          + '### THE REGISTRATION LOCK')[0]
                                .encode('utf-8')).hexdigest()
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify',
                         os.path.relpath(REG, ROOT).replace(os.sep, '/')],
                        cwd=ROOT, capture_output=True, text=True, encoding='utf-8',
                        errors='replace')
    arm('G-SEALINTACT', 'the sealed body is byte-for-byte what was sealed, read by the seal tool',
        'SEAL INTACT' in (vr.stdout or ''), (vr.stdout or '').strip().split(chr(10))[-1][:120])

    # ---- THE ORDER'S WORDS -----------------------------------------------------------------------
    bar()
    rec('  ### THE ORDER`S OWN WORDS, EACH NEEDLE BUILT FROM THE FERRY (b363`s helper).')
    bar()
    miss = []
    for lbl, hint in OWNER_NEEDLES:
        try:
            n, line = GN.build(FERRY, hint)
            rec('    %-58s ### `%s:%d`' % (lbl, os.path.basename(FERRY), n))
        except Exception as e:
            miss.append((lbl, str(e)[:80]))
            rec('    %-58s ### **NEEDLE WILL NOT BUILD** %s' % (lbl, str(e)[:60]))
    arm('G-QUOTED', 'every clause of the order resolves in the ferry as a live line',
        not miss, '%d of %d built' % (len(OWNER_NEEDLES) - len(miss), len(OWNER_NEEDLES)))

    # ---- THE BANK'S OWN SENTENCES ----------------------------------------------------------------
    bar()
    rec('  ### THE BANK`S OWN SENTENCES, EACH NEEDLE BUILT FROM THE BANK.')
    bar()
    smiss = []
    for lbl, hint in SELF_NEEDLES:
        try:
            n, line = GN.build(BANK, hint)
            rec('    %-58s ### `bank:%d`' % (lbl, n))
        except Exception as e:
            smiss.append((lbl, str(e)[:80]))
            rec('    %-58s ### **NOT IN THE BANK** %s' % (lbl, str(e)[:60]))
    arm('G-BANKSAYS', 'every sentence this suite tests for is in the bank as a live line',
        not smiss, '%d of %d' % (len(SELF_NEEDLES) - len(smiss), len(SELF_NEEDLES)))

    # ---- BAR 1 : THE SOURCES ---------------------------------------------------------------------
    bar()
    rec('  ### BAR 1 -- THE SOURCES, VERIFIED BEFORE A WORD WAS READ.')
    bar()
    arm('G-SRC', 'both pinned sources verified against the corpus`s banked digests',
        F['sources'] == {'CC': True, 'LG': True}
        and 'VERDICT : VERIFIED' in xn and 'VERDICT : HALT' not in xn)
    arm('G-SRCLOC', 'every source fragment the act quotes was located by page index',
        len(X['srcreads']) == 8 and all(s['pages'] for s in X['srcreads']),
        'fragments %d ; located %d' % (len(X['srcreads']),
                                       sum(1 for s in X['srcreads'] if s['pages'])))
    arm('G-SRCORDER', 'the extract verifies the artefacts BEFORE it reads any fragment',
        xn.index('VERDICT : VERIFIED') < xn.index('THE SOURCE FRAGMENTS'))

    # ---- BAR 2 / BAR 3 : THE CONSTRAINT SET ------------------------------------------------------
    bar()
    rec('  ### BARS 2 AND 3 -- THE CONSTRAINT SET, ANCHORED AND NOT THE NAVIGATOR`S.')
    bar()
    keys = re.findall(r'\*\*(C-[IVX]+)\.', crun)
    arm('G-CONSTRAINTS', 'the constraint set carries the eight constraints the face declares',
        len(set(keys)) == 8 and CF['constraints'] == 8, 'keys %s' % sorted(set(keys)))
    grades = len(re.findall(r'### GRADE : \*\*', crun))
    cites = len(re.findall(r'### AT    : `', crun))
    arm('G-CGRADE', 'every constraint carries a grade and a file-and-line citation',
        grades == 8 and cites == 8, 'grades %d ; citations %d' % (grades, cites))
    arm('G-DERIVES', 'the act names which constraints the record holds at DERIVES',
        CF['constraints_at_derives'] == 2
        and 'THE RECORD HOLDS AT `DERIVES` : `2`' in crun)
    arm('G-NAV', 'no constraint is quoted from the navigator, and the act says so',
        '0` FROM THE NAVIGATOR' in crun.replace('`0` FROM THE NAVIGATOR', '0` FROM THE NAVIGATOR')
        or '0 FROM THE NAVIGATOR' in gate_text.flat(crun))

    # ---- BAR 4 : THE SCOPE OF THE IMPOSSIBILITY --------------------------------------------------
    bar()
    rec('  ### BAR 4 -- `G-SCOPE`. ### **AN IMPOSSIBILITY CLAIMED WIDER THAN ITS ARGUMENT IS A')
    rec('  ### FALSE CLAIM**, so the arm requires the scoping word AND the sentence naming what the')
    rec('  ### derivation does not show, each as a live line of the same document.')
    bar()
    try:
        n1, _l1 = GN.build(CRUN, 'IMPOSSIBLE -- AND THE WORD `LAWFUL` IS PART OF THE CLAIM')
        s1 = True
    except Exception:
        n1, s1 = 0, False
    try:
        n2, _l2 = GN.build(CRUN, 'IT DOES NOT SHOW THAT NO FORMULA RELATING THE TWO INDEXED')
        s2 = True
    except Exception:
        n2, s2 = 0, False
    arm('G-SCOPE', 'the impossibility carries its scope AND the sentence naming its limit',
        s1 and s2, 'scope line %d ; limit line %d' % (n1, n2))
    # ### **AND THE ARM IS SHOWN TO BE ABLE TO FAIL**, on synthetic text written here.
    arm('G-SCOPE-CTL', 'the same predicate FAILS on synthetic text carrying only the claim',
        not GN.contains('the relation is IMPOSSIBLE and that is the end of it',
                        'IT DOES NOT SHOW THAT NO FORMULA RELATING THE TWO INDEXED')
        if hasattr(GN, 'contains') else
        'IT DOES NOT SHOW THAT NO FORMULA RELATING THE TWO INDEXED'
        not in 'the relation is IMPOSSIBLE and that is the end of it')

    # ---- BAR 5 : THE ORDER'S OWN PHRASE ----------------------------------------------------------
    bar()
    rec('  ### BAR 5 -- `G-ORDERQ`. ### **AN ORDER IMPROVED IN SILENCE PASSES NO ARM.**')
    bar()
    quoted = 'neither Theorem 1 nor' in crun
    corrected = 'PROPOSITION C.1 CARRIES NONE' in crun
    at_source = 'page index `51`' in crun and 'page index `3`' in crun
    arm('G-ORDERQ', 'the order`s phrase is quoted, corrected, and the correction is at source',
        quoted and corrected and at_source,
        'quoted %s ; corrected %s ; at source %s' % (quoted, corrected, at_source))
    arm('G-ORDERQ-FACE', 'the face declared the correction in advance, before the components ran',
        'HALF FALSE' in reg and 'PROPOSITION C.1 CARRIES NONE' in reg)

    # ---- BAR 6 : THE CLAIM THE FERRY FORBIDS -----------------------------------------------------
    bar()
    rec('  ### BAR 6 -- `G-ONEQ`. ### A NEGATIVE ARM ON A PERMISSION.')
    bar()
    claim_words = ('the bridge and the clause are one question',
                   'the bridge and the clause are the same question',
                   'the bridge IS the clause')
    # ### **A RAW GREP HERE IS THE `b317`/`b348` SPECIES AND IT FIRED ON THIS ACT`S FIRST RUN:**
    # ### the bank's sentence *It does not say that the bridge and the clause are one question*
    # ### contains the claim as a substring, so the arm reported a claim the act refuses to make.
    # ### **THE PREDICATE IS THEREFORE ASSERTION-LEVEL, NOT STRING-LEVEL:** ### the flattened bank
    # ### is cut into sentences and a hit counts only in a sentence carrying no negator.
    NEG = ('does not', 'do not', 'is not', 'are not', 'no claim', 'not made', 'unless',
           'none is about', 'never')

    def asserted(hay, words):
        out = []
        for s in re.split(r'(?<=[.!?])\s+', hay):
            low = s.lower()
            if any(gate_text.flat(w) in gate_text.flat(s) for w in words) \
                    and not any(g in low for g in NEG):
                out.append(s.strip()[:120])
        return out
    made = asserted(bank, claim_words)
    raw_hits = [w for w in claim_words if gate_text.flat(w) in FLAT]
    arm('G-ONEQ', 'the act ASSERTS nowhere that the bridge and the clause are one question',
        not made, 'asserting sentences %d %s ; raw substring hits %d (the negated sentence is one '
        'of them, and that is the point)' % (len(made), made or '', len(raw_hits)))
    arm('G-ONEQ-NEGCTL', 'the assertion-level predicate is QUIET on the act`s own negated sentence',
        not asserted('It does not say that the bridge and the clause are one question.',
                     claim_words))
    arm('G-ONEQ-SAID', 'and the act says it searched, and how many hits it hand-read',
        'NONE IS ABOUT THE BRIDGE AND THE CLAUSE' in crun and 'HITS, ALL HAND-READ' in crun)
    arm('G-ONEQ-CTL', 'the same predicate FIRES on synthetic text ASSERTING the claim',
        bool(asserted('This act holds that the bridge and the clause are one question.',
                      claim_words)))

    # ---- BAR 7 : NO GRADE MOVED ------------------------------------------------------------------
    bar()
    rec('  ### BAR 7 -- `G-NOGRADE`, READ OFF WHAT THE WRITER PRINTED AND OFF THE BLOB.')
    bar()
    fb, ft = blob('FACES_LEDGER.md'), text(FACES)
    tb, tt = blob('OPEN_TRAILS.md'), text(TRAILS)
    grade_words = ('DEFINED-ONLY', 'DERIVES-ON-IMPORTS', 'MEASURED-ON-FAMILIES',
                   'PROVED-GENERAL', 'DERIVED-ON-CONTENT', 'UNDER-RESOLVED-AT-BENCH',
                   'IMPORT-UNDER-THE-BAR', 'PROVED-PER-CELL', 'MEASURED-AT-COVERED-CELLS')
    moved = [w for w in grade_words if fb.count(w) != ft.count(w)]
    arm('G-NOGRADE', 'no grade token`s count changed in the faces ledger across this act',
        not moved, 'tokens checked %d ; changed %s' % (len(grade_words), moved or 'none'))
    arm('G-NOGRADE-CTL', 'the same predicate FIRES on a synthetic blob with a grade removed',
        [w for w in ('DEFINED-ONLY',)
         if ft.replace('DEFINED-ONLY', 'X', 1).count(w) != ft.count(w)])

    # ---- BAR 8 : PRESERVATION --------------------------------------------------------------------
    bar()
    rec('  ### BAR 8 -- `G-PRESERVE`, READ %s. ### The three OWED pair rows were APPENDED TO.'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar()
    pairs = ('F2–F3', 'F2–L1', 'F3–L1')
    prefix_ok, seg_ok = [], []
    for p in pairs:
        old = [x for x in fb.split(chr(10)) if x.startswith('| %s | OWED |' % p)]
        new = [x for x in ft.split(chr(10)) if x.startswith('| %s | OWED |' % p)]
        if not old or not new:
            prefix_ok.append(False)
            continue
        stem = old[0].rstrip()[:-1].rstrip()
        prefix_ok.append(new[0].startswith(stem))
        seg_ok.append('RESTATED 2026-09-10 (b400)' in new[0])
    arm('G-PRESERVE', 'every prior byte of each OWED cell is a true prefix of the new cell',
        len(prefix_ok) == 3 and all(prefix_ok) and len(seg_ok) == 3 and all(seg_ok),
        'true prefixes %s ; segments present %s' % (prefix_ok, seg_ok))
    pres_old = [x for x in tb.split(chr(10)) if x.startswith('> | F2–F3 | OWED |')]
    pres_new = [x for x in tt.split(chr(10)) if x.startswith('> | F2–F3 | OWED |')]
    pres_fold = [x for x in fb.split(chr(10)) if x.startswith('> | F2–F3 | OWED |')]
    pres_fnew = [x for x in ft.split(chr(10)) if x.startswith('> | F2–F3 | OWED |')]
    arm('G-PRESERVED-BLOCK', 'the preserved `>` quotation of an OWED row is UNTOUCHED',
        pres_old == pres_new and pres_fold == pres_fnew,
        'quoted blocks in trails %d ; in faces %d' % (len(pres_new), len(pres_fnew)))
    arm('G-APPENDONLY', 'the trail block is append-only: the pre-act bytes are a true prefix',
        tt.startswith(tb), 'bytes %d -> %d' % (len(tb.encode('utf-8')),
                                               len(tt.encode('utf-8'))))
    arm('G-NOLOST', 'no line was lost from either ledger',
        len(ft.split(chr(10))) == len(fb.split(chr(10)))
        and len(tt.split(chr(10))) >= len(tb.split(chr(10))))
    arm('G-STILLOWED', 'the three pair rows still read OWED after the act',
        all(any(x.startswith('| %s | OWED |' % p) for x in ft.split(chr(10))) for p in pairs))

    # ---- BAR 9 : THE TOOL CAP --------------------------------------------------------------------
    bar()
    rec('  ### BAR 9 -- `G-CAP`. ### The cap counts FILES (`b382`).')
    bar()
    tools = [n for n in sorted(os.listdir(t(''))) if n.startswith('b400_') and n.endswith('.py')]
    arm('G-CAP', 'new relay tool files at most the six the face declares',
        len(tools) == 6, 'wrote %d : %s' % (len(tools), tools))
    arm('G-CAPFACE', 'and the face declared six, which is the repair of b399`s own defect',
        'NEW RELAY TOOL FILES : `6`' in reg)

    # ---- BAR 10 : THE WRITE LIST -----------------------------------------------------------------
    bar()
    rec('  ### BAR 10 -- `G-WRITELIST`, WALKED FORWARD FROM THE LOCK. ### **A FILE WRITTEN AND NOT')
    rec('  ### NAMED IS A DEFECT AND THE ARM REPORTS IT RATHER THAN EXCUSING IT.**')
    bar()
    written = sorted(n for n in os.listdir(D) if n.startswith('b400_')
                     or n.startswith('audit_b400_'))
    unnamed = [n for n in written if n not in reg]
    arm('G-WRITELIST', 'every relay data file this act wrote is named on the locked face',
        not unnamed, 'files %d ; NOT NAMED %d : %s' % (len(written), len(unnamed),
                                                       unnamed or 'none'))

    # ### **AND THE COMPANION ARM PRINTS THE SHAPE OF THAT FAILURE RATHER THAN REPLACING IT.**
    # ### `b389`'s rule: when a later instrument disproves a figure already on a locked face, print
    # ### BOTH and name the defective predicate. ### The strict arm above is the bar the face set
    # ### and it is left to fail; this one measures the WEAKER true statement, which is what a
    # ### reader needs in order to know whether the defect is a missing KIND of file or an extra
    # ### numbered RUN of a kind already named.
    def stem(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        return (m.group(1) + m.group(3)) if m else n
    unnamed_kind = [n for n in unnamed if stem(n) not in reg
                    and stem(n).replace('.json', '.txt') not in reg]
    arm('G-WRITELIST-KIND', 'no file of a KIND the face does not name was written',
        not unnamed_kind,
        'unnamed files %d ; of an unnamed KIND %d : %s ; the rest are additional numbered runs '
        'of kinds the face names' % (len(unnamed), len(unnamed_kind), unnamed_kind or 'none'))

    # ---- BAR 11 : NO INSTRUMENT ------------------------------------------------------------------
    bar()
    rec('  ### BAR 11 -- `G-NOINSTRUMENT`, READ OFF STRIPPED CODE AND OFF THE REPOSITORIES.')
    bar()
    allcode = chr(10).join(code(n) for n in tools)
    forbidden = ('lakefile', 'subprocess.run([\'lake', 'zenodo', 'requests.post', 'urllib.request')
    hits = [w for w in forbidden if w in allcode]
    arm('G-NOINSTRUMENT', 'no tool of this act builds a kernel, calls a platform or fetches',
        not hits, 'stripped-code hits %s' % (hits or 'none'))
    lean = subprocess.run(['git', '-C', PP, 'status', '--porcelain', '--', '*.lean'],
                          capture_output=True, text=True)
    arm('G-NOLEAN', 'no `.lean` file is touched in the papers repository',
        not (lean.stdout or '').strip())
    arm('G-NOTRACE', 'the act states that it ran no instrument and recomputed no object',
        'NO INSTRUMENT WAS RUN' in gate_text.flat(text(INDEX)))

    # ---- BAR 12 / 13 : THE CENSUSES AND THE PINS -------------------------------------------------
    bar()
    rec('  ### BARS 12 AND 13 -- THE CENSUSES AND THE PINS, READ %s.'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'))
    bar()
    for nm, tool in (('G-CENSUS', 'b307_handoff_census.py'), ('G-FACES', 'b327_faces_census.py')):
        cr = subprocess.run([sys.executable, t(tool)], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        arm(nm, 'the census reports TOTAL MISSING 0 after the act',
            'TOTAL MISSING : 0' in (cr.stdout or ''))
    if post:
        pr = subprocess.run([sys.executable, t('b303_pins.py')], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        arm('G-PINS', 'all four repositories equal by ls-remote, read AFTER THE PUSH',
            '### REPOS HARD-FAILING : 0' in (pr.stdout or ''))
    else:
        rec('  G-PINS           read AFTER THE PUSH only; it cannot pass before it   ### DEFERRED')

    # ---- BAR 15 : THE INCIDENT -------------------------------------------------------------------
    bar()
    rec('  ### BAR 15 -- `G-INCIDENT`. ### The step-zero overwrite, declared and restored.')
    bar()
    pj = 'data/b373_pins.json'
    r = subprocess.run(['git', 'show', 'HEAD:' + pj], cwd=ROOT, capture_output=True)
    restored = hashlib.sha256(open(os.path.join(ROOT, pj), 'rb').read()).hexdigest()
    banked = hashlib.sha256(r.stdout).hexdigest()
    arm('G-INCIDENT', 'the overwritten prior record is byte-identical to its committed blob',
        restored == banked, 'restored %s ; banked %s' % (restored[:16], banked[:16]))
    arm('G-INCIDENT-FACE', 'and the incident is declared on the locked face, before the components',
        'b373_pins.json' in reg and 'IT WRITES WHEN RUN' in reg)

    # ---- THE ROW, THE KEY, THE HEDGES ------------------------------------------------------------
    bar()
    rec('  ### THE ROW, THE KEY AND THE HEDGE AUDIT.')
    bar()
    tb2 = text(TABLE)
    rows = [int(x.group(1)) for x in re.finditer(r'^\| (\d+) \|', tb2, re.M)]
    arm('G-ROW', 'the correspondence row is present once and its number is the last, read %s'
        % ('AFTER THE PUSH' if post else 'BEFORE THE PUSH'),
        rows[-1] == 249 and tb2.count('THE BRIDGE IS RESTATED AND THE PAIR DECLARED TWO OBJECTS')
        == 1, 'last row %d' % rows[-1])
    kq = subprocess.run([sys.executable, INDEX, '--query', 'the-bridge-restated'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    arm('G-KEY', 'the index key resolves and returns exactly one row',
        (kq.stdout or '').count('act      :') == 1)
    try:
        ha = hedge_audit.audit(BANK)
        haok = True
    except Exception as e:
        ha, haok = str(e)[:100], False
    arm('G-HEDGE', 'the hedge audit runs on the bank FILE and its own fixtures pass',
        hedge_audit.self_test(False) and haok, 'audit result : %s' % str(ha)[:120])

    # ---- THE MUST-FAIL FIXTURES ------------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES, AS WHOLE LINES. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.**')
    bar()
    fixtures = ['### THE BRIDGE WAS PAID.', '### AN EQUIVALENCE WAS COMPILED.',
                '### A GRADE WAS MOVED.', '### THE WINDOW WAS OPENED.',
                '### SOMETHING WAS COMPUTED.', '### THE CLAUSE AND THE BRIDGE ARE ONE QUESTION.']
    lines = set(bank.split(chr(10)))
    hits2 = [f for f in fixtures if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
        not hits2, 'fixtures %d ; hits %s' % (len(fixtures), hits2 or 'none'))
    synth = 'a line' + chr(10) + '### A GRADE WAS MOVED.' + chr(10) + 'another line'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one of them',
        any(f in set(synth.split(chr(10))) for f in fixtures))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b400_checks_postpush.txt' if post else 'b400_checks_run.txt')
    io.open(out, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(R) + chr(10))
    print(chr(10) + '  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main())
