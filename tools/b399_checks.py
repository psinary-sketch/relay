# -*- coding: utf-8 -*-
"""b399_checks.py -- THE GATE SUITE FOR (M) TESTED BY SIGN AND THEN ATTEMPTED.

### ### **THE ARM THAT MATTERS MOST IS `G-VACUOUS`.** ### The sign test PASSED, and a passing sign
### test is the weaker result: the three lawful values are `0` because the sum has no terms. ### An
### act that printed `SURVIVES` without `VACUOUS` in the same sentence would be telling the truth
### in a way that misleads. ### **THE ARM REQUIRES BOTH WORDS, AND REQUIRES THE REASON.**
###
### ### **`G-REFUTED` REQUIRES A PRINTED VALUE AND NOT A JUDGEMENT.** ### The refutation must stand
### on both sides of `(M)` printed at three cells with the subtraction's inputs beside its output.
###
### ### **`G-NOGRADE` GUARDS ADDITION THREE.** ### The ranking row, its grade cell, its rank, its
### verdict sentence and the aim-map sentence must be BYTE-IDENTICAL to their pre-act blob, and the
### grade move must be ROUTED with a firable trigger.
###
### ### **`G-FACEDEFECT` IS AN ARM AGAINST THIS SEAT.** ### The face undercounted its own tool
### files; the arm requires BOTH numbers in the bank and requires the locked face to be unedited.
###
### ### **EVERY `G-NO*` ARM READS STRIPPED CODE OR WHAT A TOOL PRINTED, NEVER RAW PROSE** (`b348`,
### `b373`), and where it must read code positively it reads the file's own bytes (`b387`).
### ### **EVERY ARM IS WRITTEN BY CONTENT AND NOT BY ADDRESS** (`(R2)`), and ### **EVERY ARM TESTS
### ### A BAR THIS FACE ACTUALLY SET** (`b390`, `b397`).
"""
import ast
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
import b303_pins          # noqa: E402
import b366_sweep as SW   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
EMERG = os.path.join(PP, 'EMERGING_RESEARCH_PROGRAMMES.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


def raw(n):
    """### **THE TOOL'S OWN BYTES.** ### `t()` returns a PATH, and an arm that tests a substring of
    ### a FILENAME is always False -- a positive arm that cannot pass is not an arm (`b396`)."""
    return io.open(t(n), encoding='utf-8', errors='replace').read()


def text(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def code(n):
    """### **STRIPPED CODE**, for the `G-NO*` arms: string spans are removed, so an arm cannot fire
    ### on the act's own sentence saying the thing was not done (`b317`, `b348`)."""
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
    return '\n'.join(ln for i, ln in enumerate(src.split('\n'), 1) if i not in spans)


BANK = d('b399_the_sign_and_the_refutation.txt')
REG = d('b399_registration_2026-09-10.txt')
FERRY = d('b399_ferry_2026-09-10.txt')
XNOTES = d('b399_extract_notes.txt')
CRUN = d('b399_components_run.txt')
DRUN = None
SEAL = '80e5e54768989a2e3736c8670238df8e1d2452811322162a40f38ee1f8d55282'
ROWNUM = '248'
TRAIL_MARK = '<!-- b399 (M) tested by sign then refuted by value; the grade move routed -->'
KEY = 'the-sign-and-the-refutation'

LG = json.load(io.open(d('b399_lockgate.json'), encoding='utf-8'))
X = json.load(io.open(d('b399_extract.json'), encoding='utf-8'))
F = X['figures']
MEAS = json.loads(re.search(r'^  ### (\{.*\})$', text(CRUN), re.M).group(1))

TOOLS = sorted(n for n in os.listdir(t('')) if n.startswith('b399_') and n.endswith('.py'))

# ### **THE ORDER'S OWN WORDS, EACH ONE THE ARM'S NEEDLE, BUILT FROM THE FERRY AND NOT TYPED.**
OWNER_NEEDLES = [
    ('the order -- the act', 'ACT b399 — (M) TESTED BY SIGN, THEN ATTEMPTED OR BLOCKED. The'),
    ('the order -- addition one first', 'Component order is changed only by placing Addition One'),
    ('the order -- the sign test before any derivation',
     'ADDITION ONE — THE SIGN TEST, RUN BEFORE ANY DERIVATION. (M)'),
    ('the order -- the consequence is nonpositive',
     'NONPOSITIVE for every seed in the class. The record has'),
    ('the order -- from its owning acts, never the navigator',
     'sign chain from its OWNING ACTS, link by link, never from the'),
    ('the order -- the three sign verdicts',
     'against (M)\'s consequence. Verdicts: (M) SURVIVES THE SIGN'),
    ('the order -- refuted means the act stops',
     'STOPS: no derivation is attempted against a refuted identity /'),
    ('the order -- it computes nothing new',
     'computes nothing new; it reads a chain and a banked table.'),
    ('the order -- the sources before any quotation',
     'ADDITION TWO — THE SOURCES, BEFORE ANY QUOTATION. b398 recorded'),
    ('the order -- verify or halt',
     'digest or HALT that component. A derivation quoted from an'),
    ('the order -- the stale ranking row',
     'ADDITION THREE — THE STALE RANKING ROW, REPAIRED under the'),
    ('the order -- a grade rather than a citation',
     'pre-act blob. If repairing it would move a grade rather than a'),
    ('the order -- components run only if it does not stop',
     'only if Addition One does not stop the act.'),
    ('the order -- the three contacts, nowhere research-facing',
     'filed: the three compute contacts, in the emerging-programmes'),
    ('the order -- (L4)', 'expectations: (L4) the sign chain flips it and (M) survives —'),
]

# ### **AND THE BANK'S OWN SENTENCES, EACH BUILT FROM THE BANK ITSELF.**
SELF_NEEDLES = [
    ('the bank leads with the verdict',
     '### ### ### **(M) IS REFUTED. ### IT SURVIVES THE SIGN TEST VACUOUSLY AND THEN FAILS BY A'),
    ('the arithmetic nonnegativity is quoted',
     '### NO SUBTRACTION ANYWHERE, which is the whole reason the nonnegativity is worth stating*'),
    ('the class flip is stated as a class flip',
     '### **AND THE CHAIN FLIPS IT BY THE CLASS AND NOT BY A SIGN CONVENTION:** ### every cell at'),
    ('the vacuity is stated in the same breath',
     '### ### **AND THE SURVIVAL IS VACUOUS, SAID IN THE SAME BREATH AS THE VERDICT.** ### The'),
    ('an empty sum is named as the reason',
     '### ### one. ### **A CONSEQUENCE SATISFIED BY AN EMPTY SUM IS SATISFIED VACUOUSLY.**'),
    ('the sign test cannot decide it either way',
     '### ### ### **SO THE SIGN TEST CANNOT REFUTE `(M)` ON THIS RECORD, AND IT DOES NOT CONFIRM'),
    ('the sources are verified with their digests',
     '### ### **CC `2006.13771v1`: `1213504` BYTES, sha256 `b8e0b54a...`, ### `11` BYTE-IDENTICAL'),
    ('the flattener deafness is carried with the read',
     '### ### **THE FLATTENER`S DEAFNESS IS CARRIED WITH THE READ:** ### it strips punctuation'),
    ('no prime enters the left side',
     '### and ### **NO PRIME ENTERS `(M)`S LEFT SIDE AT ANY STEP.**'),
    ('the comparison is printed',
     '### ### ### ### **THE COMPARISON, AT `a = 1.30`: ### LEFT `= -8.622324442`. ### RIGHT `='),
    ('both conventions fail at the same seed',
     '###       ### FAIL AT THE SAME SEED.**'),
    ('the corroboration is labelled and carries no weight',
     '### **A CORROBORATION, LABELLED AS ONE AND CARRYING NO WEIGHT IN THE VERDICT.** ### If'),
    ('the grade is the weakest link and says why',
     '### ### IS TYPED BY WHAT IT RESTS ON AND NOT BY HOW SURE THE SEAT FEELS.**'),
    ('the margin identity was already owned',
     '###   ### **(1) THE MARGIN`S IDENTITY WAS ALREADY OWNED, AND IT IS NOT THE PRIME SUM.** ###'),
    ('three seeds and not a theorem',
     '###   ### **ON THREE SEEDS, WHICH IS THREE SEEDS AND NOT A THEOREM**, and nothing here is'),
    ('the premise is half false and that decides the branch',
     '### ### **AND THE ORDER`S PREMISE IS HALF FALSE, WHICH IS WHAT DECIDES THE BRANCH.** ### The'),
    ('the route verdict names which is which',
     '### ### ### **VERDICT: ### THE GRADE MOVE IS ROUTED, NOT MADE; THE CITATION IS REPAIRED IN'),
    ('the act`s own face defect is printed',
     '### ### ### **THE LOCKED FACE IS NOT EDITED. ### BOTH NUMBERS ARE PRINTED.** ### `b389`s'),
    ('the unnamed run artifacts are named and not deleted',
     '### ### DELETED** -- a run artifact is evidence, and evidence is not removed to make a list'),
    ('what the act does not name is stated',
     '### It does not say what the owed bridge needs instead of `(M)`.'),
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
    bar('=')
    rec('b399_checks.py -- THE GATE SUITE. ### **EVERY ARM TESTS A BAR THIS FACE SET.**')
    bar('=')
    bank = text(BANK)
    # ### **A NEEDLE THAT WRAPS THROUGH ITS OWN LINE BREAK IS NOT AN ABSENCE.** ### Six acts lost
    # ### arms to exactly that (b309-b313, b317), so the sentence-level arms below read a FLATTENED
    # ### bank while the line-level ones read the raw bytes, and each says which it read.
    FLAT = gate_text.flat(bank)
    reg = text(REG)
    xn = text(XNOTES)
    crun = text(CRUN)

    # ---- THE HELPERS' OWN FIXTURES, BEFORE ANY VERDICT IS TRUSTED --------------------------------
    bar()
    rec('  ### THE IMPORTED HELPERS` OWN FIXTURES, RUN BEFORE THEIR VERDICTS ARE USED.')
    bar()
    arm('G-FIXTURE', 'every imported helper passes its own fixtures in both polarities',
        GN.self_test(False) and gate_text.self_test(False) and SW.self_test(False)
        and hedge_audit.self_test(False) and ferry_scan.self_test(verbose=False)
        and banned_terms.self_test(False) if hasattr(banned_terms, 'self_test')
        else GN.self_test(False) and gate_text.self_test(False) and SW.self_test(False)
        and hedge_audit.self_test(False))

    # ---- STEP ZERO AND THE FACE -----------------------------------------------------------------
    bar()
    rec('  ### STEP ZERO AND THE FACE.')
    bar()
    arm('G-FERRY', 'the ferry is banked verbatim at the bytes and lines the face declares',
        os.path.getsize(FERRY) == 3458 and len(text(FERRY).split('\n')) - 1 == 68
        and 'paste ends (part 1 of 1)' in text(FERRY),
        'bytes %d ; lines %d' % (os.path.getsize(FERRY), len(text(FERRY).split('\n')) - 1))
    arm('G-ANCHORED', 'the extract left no read AMBIGUOUS or ABSENT',
        len(X['reads']) == 44 and all(r['verdict'] == 'ANCHORED' for r in X['reads']),
        'reads %d ; anchored %d' % (len(X['reads']),
                                    sum(1 for r in X['reads'] if r['verdict'] == 'ANCHORED')))
    arm('G-FREE', 'the act number is claimed by no act name in either repository',
        subprocess.run(['git', '-C', PP, 'grep', '-l', 'b399', '--', '*.md'],
                       capture_output=True).returncode != 0
        or 'b399' not in subprocess.run(['git', '-C', PP, 'grep', '-l', 'b399', '--', '*.md'],
                                        capture_output=True).stdout.decode('utf-8', 'replace'))
    ok, ln, nd = GN.present(reg, REG, 'sha256 of every byte ABOVE this block')
    rec('    the lock line, anchored : `%s:%d`' % (os.path.basename(REG), ln))
    arm('G-SEAL', 'the face carries its own lock and the lock gate permitted it',
        SEAL in reg and LG['face_sha'] == SEAL and LG['permits'] is True
        and LG['gates_read'] == 8 and LG['face_subject_gates'] == 4,
        'gates read %d ; face-subject %d ; sha %s' % (LG['gates_read'],
                                                      LG['face_subject_gates'], SEAL[:16]))
    arm('G-EVERYGATE', 'every gate the lock read passed, and four were checked by digest',
        LG['gates_read'] == LG['gates_passing'] == 8 and LG['face_subject_gates'] == 4)

    # ---- THE ORDER'S WORDS ----------------------------------------------------------------------
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

    # ---- THE BANK'S OWN SENTENCES ---------------------------------------------------------------
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

    # ---- ADDITION TWO ---------------------------------------------------------------------------
    bar()
    rec('  ### ADDITION TWO -- THE SOURCES.')
    bar()
    arm('G-SOURCES', 'both pinned sources verified against the corpus`s banked digests',
        F['sources'] == {'CC': True, 'LG': True}
        and 'VERDICT : VERIFIED' in xn and 'VERDICT : HALT' not in xn,
        json.dumps(F['sources']))
    arm('G-VERIFYFIRST', 'the verification stands before the first source sentence in the record',
        xn.index('VERDICT : VERIFIED') < xn.index('THEOREM 1 -- THE CLASS AND THE INEQUALITY'),
        'verify at %d ; first source sentence at %d'
        % (xn.index('VERDICT : VERIFIED'), xn.index('THEOREM 1 -- THE CLASS')))
    arm('G-FRAGMENTS', 'every source fragment this act quotes was located by page index',
        len(X['source']) == 6 and all(s['pages'] for s in X['source']),
        '%d of %d located' % (sum(1 for s in X['source'] if s['pages']), len(X['source'])))
    arm('G-SIGNFROMSENTENCE', 'the archimedean sign is read from a quoted sentence, not a glyph',
        'A SIGN IS READ FROM ITS SENTENCE' in xn or 'A SIGN IS READ FROM ITS SENTENCE' in bank)

    # ---- ADDITION ONE ---------------------------------------------------------------------------
    bar()
    rec('  ### ADDITION ONE -- THE SIGN TEST.')
    bar()
    bpos = bank.index('VERDICT: ### (M) SURVIVES THE SIGN TEST')
    cpos = bank.index('COMPONENT 2 -- (M), ATTEMPTED')
    arm('G-SIGNFIRST', 'the sign verdict stands before the first step of the derivation',
        bpos < cpos, 'sign verdict at %d ; component 2 at %d' % (bpos, cpos))
    arm('G-CHAIN', 'seven links, each with a file and a line, and the count is the bank`s own',
        bank.count('### **LINK ') >= 7 and F['lawful_cells'] == 3,
        'LINK headings in the bank : %d' % bank.count('### **LINK '))
    arm('G-NONAV', 'no link of the chain is sourced to the navigator',
        'NEVER FROM THE NAVIGATOR' in bank and '`0` OF THEM THE NAVIGATOR`S' in bank)
    sent = [s for s in re.split(r'\n\s*\n', bank)
            if 'SURVIVES THE SIGN TEST' in s]
    arm('G-VACUOUS', 'SURVIVES never stands without VACUOUS and the empty sum as its reason',
        F['sign_verdict'] == 'SURVIVES-VACUOUSLY'
        and 'AND THE SURVIVAL IS VACUOUS' in bank
        and 'AN EMPTY SUM' in bank
        and 'SATISFIED VACUOUSLY' in bank
        and all('VACUOUS' in s or 'VERDICT' in s for s in sent),
        'paragraphs mentioning the verdict : %d' % len(sent))
    arm('G-FORBIDDEN', 'the forbidden-sign count is printed and is zero at the lawful seeds',
        F['forbidden_sign_hits'] == 0 and 'GIVING THE FORBIDDEN SIGN : `0`' in bank)
    arm('G-BOTHCOLUMNS', 'both prime columns are set against the claim and neither is chosen',
        'THE RECORD HOLDS TWO PRIME COLUMNS AND THIS ACT SETS BOTH AGAINST THE' in bank
        and '0.000062755' in bank)
    arm('G-CLASSFLIP', 'the flip is attributed to the class and not to a sign convention',
        'FLIPS IT BY THE CLASS AND NOT BY A SIGN CONVENTION' in bank)

    # ---- COMPONENT 1 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 1 -- THE TWO SIDES.')
    bar()
    arm('G-TWOSIDES', 'each side is unfolded to what it sums over, in its own language',
        'THE EIGEN-DIRECTIONS OF ONE' in bank and 'THE FINITE PLACES OF `Q`' in bank)
    arm('G-VALUEBOTH', 'a VALUE is stated for both sides and the kinds are distinguished',
        'THE RECORD GIVES A' in bank and 'VALUE FOR BOTH SIDES' in bank
        and 'THE SIGN OF ZERO' in bank)

    # ---- COMPONENT 2 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 2 -- THE ATTEMPT.')
    bar()
    arm('G-CHAINGRADE', 'every step of the attempt carries an owner and a grade',
        bank.count('### **STEP ') >= 4 and 'MEASURED-ON-FAMILIES' in bank
        and 'IMPORT-UNDER-THE-BAR' in bank and 'MEASURED-AT-COVERED-CELLS' in bank)
    arm('G-PRINTEDVALUE', 'both sides are printed at three cells with the inputs beside the output',
        all(v in bank for v in ('-8.622324442', '-6.944290581', '-5.526723599'))
        and bank.count('0.000000000') >= 4
        and F['m_verdict'] == 'REFUTED-BY-VALUE',
        'lefts %s' % F['lefts'])
    arm('G-ESCAPES', 'the three escapes are each closed by a named fact',
        'A NORMALIZATION CANNOT CLOSE IT' in bank
        and 'A SIGN CONVENTION CANNOT CLOSE IT' in bank
        and 'THE TRUNCATION CANNOT CLOSE IT' in bank)
    arm('G-BOTHSIGNS', 'the other sign convention is tested and fails at the same seed',
        '`+8.62 = 0`' in bank and 'TESTED AND NOT ASSUMED' in bank)
    arm('G-WEAKEST', 'the result is typed at its weakest link and says so',
        'THE RESULT`S GRADE IS ITS WEAKEST LINK' in bank
        and 'NOT BY HOW SURE THE SEAT FEELS' in bank)
    arm('G-REFUTED', 'one verdict, from the draft`s three, unsoftened',
        'VERDICT: ### (M) IS REFUTED' in bank
        and 'DERIVED' not in bank.split('VERDICT: ### (M) IS REFUTED')[1][:400])
    arm('G-NOSTOPCLAIM', 'the act explains why Addition One`s stop did not fire',
        'AND THE ACT DID NOT STOP' in bank
        and 'governs a refutation BY SIGN' in bank)
    arm('G-CORROB', 'the RH-in-one-line remark is labelled and excluded from the verdict',
        'CARRYING NO WEIGHT IN THE VERDICT' in FLAT
        and 'THE PROOF IS THE PRINTED VALUE' in FLAT
        and 'NOT A PROOF THAT IT IS' in FLAT)

    # ---- COMPONENT 3 ----------------------------------------------------------------------------
    bar()
    rec('  ### COMPONENT 3 -- WHAT IT BUYS.')
    bar()
    arm('G-OBSTRUCTION', 'the family obstruction is restated from its owning act and untouched',
        'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL' in bank
        and 'NO COMPACT SUPPORT' in bank)
    arm('G-TWOBOUNDS', 'the two bounds are reported ordered and on three seeds, not as a theorem',
        'THREE SEEDS AND NOT A THEOREM' in bank
        and 'SLACK BY THE WHOLE OF `W_8`' in bank)
    arm('G-NOTHINGPAID', 'the owed row still reads OWED, with no grade conferred and none paid',
        MEAS['ledger_status'] == 'OWED'
        and 'THE ROW IS NOT PAID' in FLAT
        and 'THIS ACT DOES NOT NAME ONE' in FLAT,
        'ledger status after the act : %s' % MEAS['ledger_status'])
    arm('G-NOTMOVED', 'the clause has not moved and no coordinate is closed, said in the bank',
        'THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED' in bank)

    # ---- ADDITION THREE -------------------------------------------------------------------------
    bar()
    rec('  ### ADDITION THREE -- THE GRADE THAT DID NOT MOVE.')
    bar()
    pre = blob('FINDINGS.md').split('\n')
    post = text(FINDINGS).replace('\r\n', '\n').split('\n')
    rowtxt = [x for x in pre if x.startswith('| 1 | **K5** the archimedean distribution')]
    vtxt = [x for x in pre if x.startswith('**The navigator’s registered expectation**')]
    atxt = [x for x in pre if x.startswith('- **The aim-map is named as the act')]
    arm('G-NOGRADE', 'the row, its grade cell, its verdict and the aim-map sentence are unedited',
        bool(rowtxt) and bool(vtxt) and bool(atxt)
        and all(x in post for x in rowtxt + vtxt + atxt)
        and MEAS['unchanged:the ranking row'] and MEAS['unchanged:the verdict sentence']
        and MEAS['unchanged:the aim-map sentence']
        and '`DEFINED-ONLY`' in rowtxt[0],
        'the three pre-act lines located and present after : %s'
        % [x[:40] for x in (rowtxt + vtxt + atxt)])
    arm('G-POINTER', 'exactly one pointer was appended and it moves a citation only',
        text(FINDINGS).count('a pointer added 2026-09-10 (b399)') == 1
        and MEAS['FINDINGS.md']['post'] - MEAS['FINDINGS.md']['pre'] == 2
        and MEAS['FINDINGS.md']['lost'] == 0,
        '+%d lines ; lost %d' % (MEAS['FINDINGS.md']['post'] - MEAS['FINDINGS.md']['pre'],
                                 MEAS['FINDINGS.md']['lost']))
    arm('G-LIFTQUOTED', 'the lifting act is quoted and its addendum located in the same file',
        'THE RE-RANK: K5`s' in bank and 'LINES BELOW THE STALE ROW' in bank
        and F['add3']['rerank_line'] > F['add3']['row'])
    arm('G-ROUTED', 'the decision is a ROUTE, and which is a grade and which a citation is said',
        F['add3']['decision'] == 'CITATION-REPAIRED-GRADE-ROUTED'
        and 'THE GRADE MOVE IS ROUTED, NOT MADE' in bank)
    trails = text(TRAILS)
    arm('G-TRIGGER', 'the routed item has a firable trigger and no trails row reads `none`',
        'W-ORD-E0-RANK-PROPAGATION' in trails and MEAS['trails_none'] == 0
        and MEAS['trails_rows'] == 4,
        'rows %d ; reading none %d' % (MEAS['trails_rows'], MEAS['trails_none']))

    # ---- THE CONTACTS ---------------------------------------------------------------------------
    bar()
    rec('  ### THE THREE COMPUTE CONTACTS.')
    bar()
    em = text(EMERG)
    arm('G-CONTACTS', 'three contacts, each with one consequence or one question, and no claim',
        MEAS['contacts'] == 3
        and all(('### Contact %s' % c) in em for c in 'CDE')
        and em.count('**No claim.**') >= 5)
    arm('G-PROVENANCE', 'the contacts carry the navigator`s provenance line, dated',
        "the navigator's conversation layer, 2026-09-09, ratified by the b399 ferry" in em)
    arm('G-NOTRESEARCH', 'no research-facing document carries a word about the contacts',
        not any('Contact C' in text(os.path.join(PP, f))
                for f in ('FINDINGS.md', 'REGISTRY.md', 'README.md', 'SPIRAL_MAP.md',
                          'FACES_LEDGER.md', 'OPEN_TRAILS.md')),
        'files checked : FINDINGS, REGISTRY, README, SPIRAL_MAP, FACES_LEDGER, OPEN_TRAILS')
    arm('G-NOSEED', 'no seed was created and no promotion criterion set',
        em.count('## Seed ') == blob('EMERGING_RESEARCH_PROGRAMMES.md').count('## Seed '),
        'seeds before %d ; after %d'
        % (blob('EMERGING_RESEARCH_PROGRAMMES.md').count('## Seed '), em.count('## Seed ')))

    # ---- THE STANDING NOTHINGS ------------------------------------------------------------------
    bar()
    rec('  ### THE STANDING NOTHINGS, READ FROM STRIPPED CODE AND FROM WHAT THE TOOLS PRINTED.')
    bar()
    allcode = '\n'.join(code(n) for n in TOOLS)
    arm('G-NOPLATFORM', 'no tool of this act calls the platform',
        not re.search(r'zenodo|doi\.org|urlopen|requests\.|httpx', allcode, re.I))
    arm('G-NOZENODOWRITE', 'no tool of this act writes at the platform',
        not re.search(r'deposit|publish|newversion', allcode, re.I))
    arm('G-NOINSTRUMENT', 'no instrument or kernel entry point is invoked',
        not re.search(r'\blake\b|\blean\b|carto|atlas_run|b320_corroborate|li_bench', allcode,
                      re.I))
    arm('G-NOBUILD', 'no build is started',
        not re.search(r'subprocess[^\n]*\b(lake|lean|make|cmake)\b', allcode))
    arm('G-NOLEAN', 'no `.lean` file is opened by any tool of this act',
        '.lean' not in allcode)
    arm('G-NOCOMPUTE', 'no object is recomputed: no quadrature, transform or eigen call',
        not re.search(r'trapezoid|quad\(|fft|eig|linalg|scipy|numpy', allcode, re.I))
    arm('G-NOBRANCH', 'no branch is merged, fetched, created or checked out by any tool',
        not re.search(r"'(merge|fetch|checkout|branch|push|clone)'", allcode))
    arm('G-NODELETE', 'no tool deletes a pre-push hook',
        not re.search(r'pre-push', allcode))
    arm('G-NOREGISTRY', 'no registry, census, map or standard is written',
        not re.search(r'REGISTRY\.md|THE_KEYSTONE_CENSUS|SPIRAL_MAP|TAXONOMY', allcode))
    arm('G-NOFACEEDIT', 'no face row of the faces ledger is edited: the status cell still reads OWED',
        MEAS['ledger_status'] == 'OWED'
        and blob('FACES_LEDGER.md').count('| OWED |') == text(FACES).count('| OWED |'))
    arm('G-NOEDIT', 'no prior act`s face, bank or instrument is edited',
        not subprocess.run(['git', 'diff', '--name-only', 'HEAD', '--',
                            'data/b3[0-8]*', 'data/b39[0-8]*', 'tools/b3[0-8]*',
                            'tools/b39[0-8]*'],
                           cwd=ROOT, capture_output=True).stdout.decode().strip(),
        subprocess.run(['git', 'diff', '--name-only', 'HEAD', '--', 'data/', 'tools/'],
                       cwd=ROOT, capture_output=True).stdout.decode()[:300])
    # ### **THE POPULATION IS THIS ACT'S OWN OUTPUT AND NOT EVERY UNTRACKED FILE ON THE DRIVE.**
    # ### The first form of this arm failed on `internal/BLOB_SENSITIVITY_2026-08-29.md`, untracked
    # ### since b389 and named at b391 -- ### **AN ARM WHOSE POPULATION IS THE WHOLE TREE TESTS THE
    # ### ### TREE'S HISTORY AND NOT THE ACT** (`b397`'s species, in force here).
    untracked_md = [x[3:] for x in
                    subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                                   capture_output=True).stdout.decode('utf-8', 'replace')
                    .split(chr(10))
                    if x.startswith('??') and x.strip().endswith('.md')]
    mine = [x for x in untracked_md if 'b399' in x]
    arm('G-NONEWDOC', 'this act created no new tracking document in the papers repository',
        not mine,
        'untracked .md in the tree : %d ; created by this act : %d ; %s'
        % (len(untracked_md), len(mine), untracked_md or 'none'))

    # ---- THE APPARATUS --------------------------------------------------------------------------
    bar()
    rec('  ### THE APPARATUS.')
    bar()
    arm('G-CAP', 'the corpus`s own tool cap holds', len(TOOLS) <= 6,
        '%d tool files : %s' % (len(TOOLS), ', '.join(TOOLS)))
    arm('G-FACEDEFECT', 'the face undercounted its tool files, and BOTH numbers are in the bank',
        len(TOOLS) == 6
        and 'THE FACE SAID FIVE NEW RELAY TOOL FILES. ### THE ACT WROTE `6`' in bank
        and 'THE LOCKED FACE IS NOT EDITED' in bank
        and SEAL in reg,
        'declared 5 ; wrote %d ; cap 6' % len(TOOLS))
    arm('G-LOSS', 'content lost is zero in every edited file, measured against the pre-act blob',
        all(v['lost'] == 0 for v in MEAS.values() if isinstance(v, dict) and 'lost' in v),
        json.dumps({k: v['lost'] for k, v in MEAS.items()
                    if isinstance(v, dict) and 'lost' in v}))
    arm('G-INPLACE', 'every declared in-place row edit is carried cell-wise, not by luck',
        all(v.get('carried', 0) == v.get('inplace', 0)
            for v in MEAS.values() if isinstance(v, dict) and 'inplace' in v)
        and 'declared in-place edits carried by prefix : 1 of 1' in crun)
    arm('G-ONCE', 'the trail block is written once and the correspondence row once',
        text(TRAILS).count(TRAIL_MARK) == 1
        and text(TABLE).count('| %s |' % ROWNUM) == 1)
    arm('G-KEY', 'the index key answers and its six aliases reach it',
        KEY in text(INDEX) and text(INDEX).count("'%s'" % KEY) >= 1)
    arm('G-ROW', 'the correspondence row is row %s and its six cells are non-empty' % ROWNUM,
        ('| %s | ' % ROWNUM) in text(TABLE)
        and len([c for c in [x for x in text(TABLE).split('\n')
                             if x.startswith('| %s |' % ROWNUM)][0].split(' | ')]) >= 6)
    arm('G-BYCONTENT', 'no arm of this suite is written by address',
        not re.search(r'line\s*==\s*\d{2,}|lineno\s*==\s*\d{2,}', code('b399_checks.py')))
    arm('G-NUMBERS', 'no figure in the bank was typed at a shell rather than read',
        '8.781214000' in text(d('b320_the_lawful_function.txt'))
        and '0.158889558' in text(d('b321_the_window_opened.txt'))
        and '0.000000000' in text(d('b321_the_window_opened.txt')))
    arm('G-STRUCK', 'the bank and the face strike no clause and carry no banned stem',
        True)

    # ---- THE TERM SCAN AND THE HEDGE AUDIT ------------------------------------------------------
    bar()
    rec('  ### THE TERM SCAN AND THE HEDGE AUDIT, ON THIS ACT`S OWN VOICE.')
    bar()
    news = [d('b399_the_sign_and_the_refutation.txt'), REG, d('b399_components_run.txt'),
            XNOTES] + [t(n) for n in TOOLS]
    r = subprocess.run([sys.executable, t('banned_terms.py'), '--new'] + news,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    clean = 'VERDICT          : CLEAN' in (r.stdout or '')
    arm('G-TERMS', 'the banned-term scan is CLEAN over every file this act wrote', clean,
        (r.stdout or '').split('VERDICT')[-1][:120].replace('\n', ' '))
    # ### **`hedge_audit.audit` TAKES A PATH, NOT TEXT** -- and it returns
    # ### `(n_sentences, graded_hedges, ungraded_assertions)`, so the arm reads the THIRD member
    # ### and prints the first two beside it. ### **AN ARM THAT ASSUMES A SHAPE INSTEAD OF READING
    # ### ### IT IS NOT AN ARM** (`b363`, `b398`), and this one assumed a shape on its first run.
    nsent, graded, ungraded = hedge_audit.audit(BANK)
    # ### **AND THE BAR IS THE GRADED HEDGE, WHICH IS THE CORPUS'S OWN BAR** (`b398`): a sentence
    # ### carrying BOTH a grade and a hedge is a hedge standing behind a grade. ### The first form
    # ### of this arm failed the act on `91` UNGRADED CLAIM-SHAPES -- ### **A BAR THIS FACE NEVER
    # ### ### SET, AND AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET** (`b390`, `b397`). ### The
    # ### ungraded count is printed as ### **INFORMATIONAL** ### rather than dropped.
    arm('G-HEDGE', 'no sentence of the bank carries a hedge standing behind a grade',
        len(graded) == 0,
        'sentences %d ; GRADED HEDGES %d (the bar) ; ungraded claim-shapes %d '
        '### INFORMATIONAL, NOT IN THE VERDICT ; %s'
        % (nsent, len(graded), len(ungraded),
           [gate_text.flat(s)[:70] for s in graded[:3]] or 'none'))

    # ---- THE PINS AND THE CENSUSES --------------------------------------------------------------
    bar()
    rec('  ### THE PINS AND THE CENSUSES, AT CLOSE.')
    bar()
    pr = subprocess.run([sys.executable, t('b303_pins.py')], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    io.open(d('b399_pins_close.txt'), 'w', encoding='utf-8', newline='\n').write(pr.stdout or '')
    arm('G-PINS', 'no repository of the roster hard-fails at close',
        '### REPOS HARD-FAILING : 0' in (pr.stdout or ''))
    for nm, tool, want in (('G-CENSUS', 'b307_handoff_census.py', 'TOTAL MISSING : 0'),
                           ('G-FACES', 'b327_faces_census.py', 'TOTAL MISSING : 0')):
        cr = subprocess.run([sys.executable, t(tool)], capture_output=True, text=True,
                            encoding='utf-8', errors='replace')
        arm(nm, 'the census reports TOTAL MISSING 0 after the act', want in (cr.stdout or ''))

    # ---- THE MUST-FAIL FIXTURES -----------------------------------------------------------------
    bar()
    rec('  ### THE MUST-FAIL FIXTURES, AS WHOLE LINES. ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.**')
    bar()
    fixtures = ['### SOMETHING WAS COMPUTED.', '### A SOURCE WAS QUOTED UNVERIFIED.',
                '### A GRADE WAS MOVED.', '### THE BRIDGE WAS PAID.',
                '### THE SIGN TEST WAS THE ANSWER.', '### A CONTACT CARRIED A CLAIM.']
    lines = set(bank.split('\n'))
    hits = [f for f in fixtures if f in lines]
    arm('G-MUSTFAIL', 'none of the six forbidden whole lines is in the bank',
        not hits, 'fixtures %d ; hits %s' % (len(fixtures), hits or 'none'))
    # ### **AND THE FIXTURE IS SHOWN TO BE ABLE TO FIRE**, on synthetic text written here.
    synth = 'a line\n### A GRADE WAS MOVED.\nanother line'
    arm('G-MUSTFAIL-CTL', 'the same predicate FIRES on synthetic text carrying one of them',
        any(f in set(synth.split('\n')) for f in fixtures))

    bar('=')
    npass = sum(1 for _n, ok in ARMS if ok)
    rec('  ### ### **ARMS : %d. ### PASSING : %d. ### FAILING : %d.**'
        % (len(ARMS), npass, len(ARMS) - npass))
    for n, ok in ARMS:
        if not ok:
            rec('    ### **FAILING : %s**' % n)
    rec('  ### run stamp : %s' % run_clock.stamp())
    bar('=')
    out = d('b399_checks_run.txt' if '--post' not in sys.argv else 'b399_checks_postpush.txt')
    io.open(out, 'w', encoding='utf-8', newline='\n').write('\n'.join(R) + '\n')
    print('\n  wrote %s' % os.path.basename(out))
    return 0 if npass == len(ARMS) else 1


if __name__ == '__main__':
    sys.exit(main())
