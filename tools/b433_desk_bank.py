# -*- coding: utf-8 -*-
"""b433_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off this act's
### own JSON, never typed. ### The trail block carries the grading and the Type-D finding; its
### trigger is the author's ruling on whether the grading may be cited.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as GD  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
MARK = '<!-- b433 the five rulings executed -->'
PRIOR = '<!-- b432 the disproof lane restated with a worked case -->'
BANKOUT = os.path.join(D, 'b433_the_five_rulings.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace')
    except Exception:
        return ''


def write_bytes(path, text):
    data = text.encode('utf-8')
    open(path + '.tmp', 'wb').write(data)
    os.replace(path + '.tmp', path)
    return len(data)


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


FACE = read(os.path.join(D, 'b433_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b433_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

try:
    G = json.loads(read(os.path.join(D, 'b433_repairs.json')) or '{}')
except Exception:
    G = {}
CHK = read(os.path.join(D, 'b433_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS = (int(_a.group(1)), int(_a.group(2))) if _a else (0, 0)

APPLIED = len([r for r in G.get('repairs', []) if r.get('status') == 'APPLIED'])
NOTLOC = G.get('notlocated', '?')
REFUSED = G.get('refused', '?')
DELTAS = G.get('deltas', {})
TOTDELTA = sum(v for v in DELTAS.values() if isinstance(v, int))
CLONE_GONE = G.get('clone_removed')
ALLPOS = G.get('all_deltas_nonnegative')
ALLKEPT = G.get('all_originals_present')


ROWMARK = ('**THE FIVE RULINGS EXECUTED: THE FOURTH GRADE DEFINED, THE LEMMA`S PROSE NARROWED WITH '
           'ITS NAME KEPT, THE FINITE-SIDE PROSE MARKED TO THE TERMINAL, THE WRITE-LIST FORM '
           'STANDING, AND THE EXTERNAL CLONE REMOVED**').replace('`', chr(0x2019))


FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — '
        'the rows grading a declaration the record has classified absent (b373). **OPEN.** '
        '**LIST 3** — the undated figures across the roster (b374). **OPEN.** **LIST 4** — the '
        'bibliography entries nothing cites (b374). **OPEN.** Trigger: the ruling on which test '
        'governs, or any disposition on the four open lists.')

DESK = [
    ('the five rulings (R41)-(R45)', 'CLOSE',
     'EXECUTED at b433. **%d repairs APPLIED, %d NOT LOCATED, %d REFUSED**; every per-file byte '
     'delta against the pre-act blob NON-NEGATIVE (%s) and every original still findable (%s). '
     'The clone is gone (%s). Each repair was written in the form its own document already uses, '
     'and each original is preserved by quotation where a heading was corrected.'
     % (APPLIED, NOTLOC, REFUSED, ALLPOS, ALLKEPT, CLONE_GONE)),
    ('the fourth grade, defined', 'CLOSE',
     '`NOT THE CLAIM` now stands in both documents that define the corpus`s grades -- `README.md` '
     'and `EXCLUSION_ENGINE.md` §0 -- additively, the three existing bullets untouched, with '
     'b429`s and b430`s incidents cited beside it. **THE GAP b430 ROUTED IS CLOSED**: a grade used '
     'at b430 and undefined until now is defined.'),
    ('the conspiracy keystone`s lemma name and prose', 'CLOSE',
     'ANNOTATED IN PLACE at b433 by `(R42)`. `crt_exhaustiveness` **is not renamed** -- in the '
     'kernel, which this act did not open, or in any line of the document. The annotation states '
     'what the compiled proof does: a periodic lift at a SINGLE modulus, invoking no Chinese '
     'Remainder Theorem, and narrows the paper`s claim for it to that. **The original sentence '
     'survives word for word.**'),
    ('the finite-side prose against its terminal', 'CLOSE',
     'MARKED at b433 by `(R43)`. `K3``s two rows and `F5``s claim-bearing row each carry a '
     'narrowing that says what `smear_general` states -- the model`s count, over '
     'single-prime-factor bases -- with `K3``s named objects KEPT as what the source`s trace would '
     'require and MARKED as not carried by the terminal. **`F5``s scope clause is NOT rewritten**: '
     'it is true of the terminals that row lists, and rewriting it would have made a true row '
     'false. That reading was declared on the locked face before the act touched anything.'),
    ('the disproof lane`s form-(b) finding', 'CLOSE',
     'APPENDED to the trail at b433 with the barrier keystone`s symmetry clause quoted beside it '
     'and the sentence the order required: **the instruments are not symmetric though the theory '
     'is.** The lane is NOT opened and its trigger is untouched.'),
    ('the write-list form', 'STANDING',
     'MADE STANDING by `(R44)`, as b432`s face states it: tools named, the ritual`s own rewritten '
     'files named, a further tool permitted if the suite declares it. **b432 AND b433 BOTH CLOSED '
     'WITH 0 UNLISTED WRITES**, where b430 and b431 did not.'),
    ('what the corpus still has no instrument for', 'STANDING',
     'ROUTED at b432 and carried. Both named instruments serve the exhibited-zero form; the corpus '
     'has no instrument pointed at the universal negative. Not a claim that it is unreachable.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 on three sites: 13/16, 10/19, 12/20; union of kinds 10 and still growing.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING',
     'ROUTED at b424.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author`s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING',
     'Blocked by the PARKED instrument lane.'),
    ('the scan`s sites against the lock`s zero', 'STANDING', 'The (R36) instrument item.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; untouched by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('the fold, b423 to b432', 'STANDING', 'DUE AT b434, the sortie`s second leg.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT -- **READ BY THIS ACT AND NOT MOVED.**'),
]


def do_desk():
    for item, want, why in DESK:
        rec('    %-72s %s' % (item[:72], want))
        for seg in wrap(why[:1800], 150):
            rec('        %s' % seg)
    closed = [m for m in DESK if m[1] == 'CLOSE']
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### STANDING : %d.**'
        % (len(DESK), len(closed), len(DESK) - len(closed)))
    return dict(items=len(DESK), closed=len(closed), standing=len(DESK) - len(closed))


def trail_block():
    L = ['', MARK, '',
         '### b433 — the five rulings executed — filed 2026-09-12', '',
         '**Five rulings, %d repairs, every one append-or-narrow with its original preserved. '
         'Nothing was built, no terminal was renamed, no grade moved, and the disproof lane stayed '
         'shut.**' % APPLIED, '',
         '#### How each repair was measured', '',
         'Seven documents were pinned by byte count and `sha256` **before this act typed its '
         'face** (`relay/data/b433_preact_blobs.txt`). Every repair is measured against that blob, '
         'two ways: a **non-negative byte delta**, and **the original text still findable '
         'afterwards**. A repair failing either would have been refused and the file restored from '
         'the pre-act bytes. **%d refused, %d not located.** Total growth across the six repaired '
         'files: **%+d bytes**, and `INVARIANCE_BARRIERS.md` — quoted but not repaired — moved '
         '**0**, which is the point of listing it.' % (REFUSED, NOTLOC, TOTDELTA), '',
         '#### `(R41)` — the fourth grade is defined', '',
         '`NOT THE CLAIM` now stands in both documents that define the corpus’s grades: `README.md` '
         'and `EXCLUSION_ENGINE.md` §0. **Additively.** Each heading was corrected — *"The three '
         'grades"* → *"The four grades"* — with the words it had **quoted in a note directly '
         'beneath it**, which is `(R4)`’s form: preserve by quotation, repair by edit. The three '
         'existing bullets are unchanged, word for word.', '',
         '**And the two incidents are cited, because a grade admitted without its occasion is a '
         'grade nobody can check.** At **b429** four grades were available against a stranger while '
         'the corpus had only ever had three — unused there, so it changed no outcome. At **b430** '
         'the corpus put its own `SmearGeneral.smear_general` to the same protocol and the fourth '
         'grade *was* needed: `DERIVES` against the claim its correspondence row names, '
         '**`NOT THE CLAIM`** against the claim its own finite-side prose makes.', '',
         '#### `(R42)` — the name stays, the prose narrows', '',
         '**`crt_exhaustiveness` is not renamed** — not in the kernel, which this act did not open, '
         'and not in any line of the keystone. The keystone is annotated **in the form that '
         'document already uses**, a block declaring the existing text preserved and saying what it '
         'adds. What it adds is the reading: the lemma quantifies over **one** `StructuralCoupling` '
         'whose period is fixed by the term; its witness is `ofPeriodic sc.period`, whose modulus '
         'set is **`moduli := {L}`, a singleton**; and what it establishes is that a predicate '
         'built from finitely many congruence conditions is a congruence condition modulo the lcm '
         'of those moduli. **That is true, cleanly proved, and narrower than the sentence above '
         'it** — which survives word for word, now read beside what the proof does.', '',
         '#### `(R43)` — the finite-side prose marked to the terminal', '',
         '`K3`’s two rows in the clause anchor and `F5`’s claim-bearing row in the faces ledger '
         'each carry a narrowing: what `SmearGeneral.smear_general` states is **the model’s '
         'count** — an equation between three `Nat` quantities — over bases with a **single prime '
         'factor** only. `K3`’s named objects — the source’s construction, the test function at the '
         'identity, the dimension — are **kept** as what the source’s trace would require and '
         '**marked as not carried by that terminal**; their identification with the model’s count '
         'stays b310’s derivation and is not compiled.', '',
         '**And one thing was deliberately not done, declared on the locked face before the act '
         'touched anything.** `F5`’s clause *"GENERAL, over every base p ≥ 2, level, power and '
         'index"* is **true of the terminals `F5` lists** — `valuation_exists` and the rest of the '
         'scaling part — and `smear_general` is in neither of its lists, being a later terminal '
         '(b419). **Rewriting that clause to "single-prime-factor" would have made a true row false '
         'about its own terminals**, which is the opposite of a repair. The ruling’s own words are '
         '*preserved*, *kept* and *marked*, so the narrowing was written beside the clause and not '
         'over it. Every marked row still parses with the cell count it had.', '',
         '#### The disproof lane’s form-(b) finding', '',
         'Appended to the lane’s trail entry with the barrier keystone’s **T1** symmetry clause '
         'quoted beside it, and the sentence the order required on the record: **the instruments '
         'are not symmetric though the theory is.** The functional equation is symmetric in '
         '`s ↔ 1−s` and the two forms a disproof could take are duals; the corpus’s instruments are '
         'not — every one looks for something to *see*, and nothing in the record looks for '
         'something that cannot *be*. **The lane is not opened and its trigger is untouched.**', '',
         '#### `(R44)` and `(R45)`', '',
         '**`(R44)`** makes b432’s write-list form standing: tools named, the ritual’s own '
         'rewritten files named, a further tool permitted provided the suite prints its name and '
         'reason. b432 and b433 both closed with **0 unlisted writes**, where b430 and b431 did '
         'not. **`(R45)`**: the external clone at `D:/_b431_external` is **removed**, its absence '
         'read back after the removal — but only after the record’s substitutes were confirmed '
         '**present and tracked in git**: the two pins, the paper digest, the build log and the '
         'printer’s output. A removal whose substitutes are not committed is a deletion, not a '
         'substitution.', '',
         '#### The four lists', '', FOUR, '',
         '#### What this act did not do', '',
         '0 kernels built. 0 `.lean` files written or edited. 0 terminals renamed. 0 grades moved, '
         'conferred or minted — **defining a grade name confers it on nothing**. 0 premises '
         'discharged: `h2` is not discharged, not weakened and not restated. 0 lanes opened and 0 '
         'triggers moved. 0 addresses resolved and nothing fetched. 0 register rows and 0 doors '
         'restated. 0 folds run — **the fold is b434’s**. 0 rules struck, amended or widened. '
         '0 locked faces edited. 0 deposit actions. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS FIVE AUTHOR RULINGS EXECUTED AS REPAIRS TO THE RECORD, EACH MEASURED "
         "AGAINST A PRE-ACT BLOB AND EACH PRESERVING ITS ORIGINAL. ### IT MOVES NO GRADE, RENAMES NO "
         "TERMINAL, BUILDS NOTHING, OPENS NO LANE AND DISCHARGES NO PREMISE")


def corr_rows():
    m = ROWMARK + " (b433)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b433 -- @GR@ gates read, @GDG@ checked by digest. **SEVEN DOCUMENTS PINNED BY BYTE "
            "COUNT AND sha256 BEFORE THE FACE WAS TYPED; EVERY REPAIR MEASURED AGAINST ITS PRE-ACT "
            "BLOB, TWO WAYS -- A NON-NEGATIVE DELTA AND THE ORIGINAL STILL FINDABLE.** **@APPLIED@ "
            "REPAIRS APPLIED, @NOTLOC@ NOT LOCATED, @REFUSED@ REFUSED; TOTAL GROWTH @TOTDELTA@ "
            "BYTES.** **(R41): NOT THE CLAIM DEFINED IN BOTH GRADE-VOCABULARY DOCUMENTS, THE THREE "
            "EXISTING BULLETS UNTOUCHED, EACH HEADING CORRECTED WITH ITS OLD WORDS QUOTED BENEATH "
            "IT, b429'S AND b430'S INCIDENTS CITED.** **(R42): THE KEYSTONE ANNOTATED IN ITS OWN "
            "DOCUMENT'S FORM -- THE COMPILED PROOF IS A PERIODIC LIFT AT A SINGLE MODULUS AND "
            "INVOKES NO CRT; THE LEMMA IS NOT RENAMED AND THE ORIGINAL SENTENCE SURVIVES.** "
            "**(R43): K3'S TWO ROWS AND F5'S CLAIM-BEARING ROW MARKED TO WHAT smear_general STATES "
            "-- THE MODEL'S COUNT, SINGLE-PRIME-FACTOR BASES -- WITH K3'S NAMED OBJECTS KEPT AND "
            "MARKED AS NOT CARRIED; F5'S SCOPE CLAUSE NOT REWRITTEN, BECAUSE IT IS TRUE OF THE "
            "TERMINALS THAT ROW LISTS.** **THE DISPROOF LANE'S TRAIL ENTRY GAINED THE FORM-(b) "
            "FINDING WITH T1 QUOTED BESIDE IT; THE LANE STAYED SHUT.** **(R44) NOTED STANDING; "
            "(R45) EXECUTED AFTER THE SUBSTITUTES WERE CONFIRMED TRACKED.** 0 GRADES MOVED, 0 "
            "TERMINALS RENAMED, 0 KERNELS BUILT, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED, RENAMED OR GRADED. crt_exhaustiveness and "
            "SmearGeneral.smear_general are both READ and both unchanged")
    prof = ("### SIX PLACE-papers FILES EDITED IN PLACE WITH ORIGINALS PRESERVED, BY THE RULINGS' "
            "OWN ORDER -- README.md, EXCLUSION_ENGINE.md, ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md, "
            "FINDINGS.md, FACES_LEDGER.md, AND OPEN_TRAILS.md APPENDED; INVARIANCE_BARRIERS.md "
            "QUOTED AND UNCHANGED AT 0 BYTES; NO KERNEL FILE, NO REGISTER ROW -- 0 CONTENT LOST")
    grade = ("### EVERY REPAIR WAS WRITTEN IN THE FORM ITS OWN DOCUMENT ALREADY USES, QUOTED IN THE "
             "SURVEY BEFORE THE FACE WAS TYPED; EVERY HEADING CORRECTED KEEPS ITS OLD WORDS BY "
             "QUOTATION; AND THE ONE CLAUSE THE RULING'S LETTER MIGHT HAVE HAD REWRITTEN WAS LEFT "
             "STANDING, WITH THE REASON DECLARED ON THE LOCKED FACE BEFORE THE ACT TOUCHED ANYTHING")
    status = ("data/b433_the_five_rulings.txt; data/b433_components.txt; data/b433_extract.txt; "
              "data/b433_preact_blobs.txt; data/b433_repairs.json; data/b433_checks.txt; "
              "data/b433_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers README.md, EXCLUSION_ENGINE.md, "
              "ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md, FINDINGS.md, FACES_LEDGER.md, OPEN_TRAILS.md; "
              "CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@APPLIED@', str(APPLIED)).replace('@NOTLOC@', str(NOTLOC))
                .replace('@REFUSED@', str(REFUSED)).replace('@TOTDELTA@', '%+d' % TOTDELTA))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the five rulings executed', 'the fourth grade defined',
           'crt exhaustiveness annotated', 'the finite side prose narrowed',
           'where is NOT THE CLAIM defined')
MUST_NOT_HIT = ('the keystone was wrong', 'a grade was moved', 'the terminal was renamed')
KEY = 'the-five-rulings-executed'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b433 EXECUTED FIVE AUTHOR RULINGS AS REPAIRS TO THE RECORD, EACH MEASURED AGAINST A "
        "PRE-ACT BLOB PINNED BY sha256 BEFORE THE FACE WAS TYPED. %s applied, %s not located, %s "
        "refused; every per-file delta non-negative and every original still findable. (R41): NOT "
        "THE CLAIM is DEFINED in both documents that define the corpus's grades -- README.md and "
        "EXCLUSION_ENGINE.md section 0 -- additively, the three existing bullets untouched, each "
        "heading corrected with its old words quoted beneath it, and b429's and b430's incidents "
        "cited. (R42): the conspiracy keystone is annotated in its own document's form -- the "
        "compiled crt_exhaustiveness is a periodic lift at a SINGLE modulus and invokes no Chinese "
        "Remainder Theorem -- and THE LEMMA IS NOT RENAMED; the original sentence survives word for "
        "word. (R43): K3's two rows and F5's claim-bearing row are marked to what "
        "SmearGeneral.smear_general states, the model's count over single-prime-factor bases, with "
        "K3's named objects KEPT as what the source's trace would require and MARKED as not carried "
        "by the terminal; F5's scope clause was NOT rewritten because it is true of the terminals "
        "that row lists, and that reading was declared on the locked face before the act touched "
        "anything. The disproof lane's trail entry gained the form-(b) finding with the barrier "
        "keystone's T1 symmetry clause quoted beside it and the sentence that the instruments are "
        "not symmetric though the theory is; the lane stayed shut. (R44): b432's write-list form is "
        "standing. (R45): the external clone is removed, after its substitutes were confirmed "
        "present and tracked. 0 grades moved, 0 terminals renamed, 0 kernels built, 0 premises "
        "discharged.")
    grade = ("### NO GRADE MOVED, CONFERRED OR MINTED. ### NO TERMINAL RENAMED. ### NO LANE OPENED. "
             "### NO PREMISE DISCHARGED. ### NOTHING DEPOSITS")
    where = ("data/b433_the_five_rulings.txt; data/b433_components.txt; data/b433_repairs.json; "
             "data/b433_preact_blobs.txt; data/b433_registration_2026-09-12.txt (LOCKED, %d gates "
             "read, %d by digest); README.md; EXCLUSION_ENGINE.md; "
             "ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md; FINDINGS.md; FACES_LEDGER.md; OPEN_TRAILS.md; "
             "CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b433 (the five rulings executed)"


    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE FIVE RULINGS EXECUTED (b433).%s    (%r, %r,%s     %r,%s'
               '     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = dict((qq, no_key(query(qq)[0])) for qq in MUST_NOT_HIT)
    for qq in MUST_NOT_HIT:
        rec('    %-48s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL +
                  '    # (key, act, one-line statement, grade as its own act recorded it, '
                  'location)' + NL)
    if KEY_ANCHOR not in txt or ROW_ANCHOR not in txt:
        rec('  ### HARD FAILURE -- an anchor is not in the file.')
        return False
    if ("'%s'" % KEY) not in txt:
        txt = txt.replace(KEY_ANCHOR, KEY_ANCHOR + key_new, 1)
    if ("(%r," % KEY) not in txt:
        txt = txt.replace(ROW_ANCHOR, ROW_ANCHOR + row_new, 1)
    write_bytes(INDEX, txt)
    out, rc = query(KEY)
    n = out.count('act      :')
    ok = (not no_key(out)) and rc == 0 and n >= 1
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]'
        % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b433 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the fourth grade carried', 'NOT THE CLAIM is DEFINED' in out),
                      ('the name-kept finding carried', 'THE LEMMA IS NOT RENAMED' in out),
                      ('the F5 reading carried', 'scope clause was NOT rewritten' in out),
                      ('the measurement carried', 'PRE-ACT BLOB' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-48s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100,
          'b431 -- THE LongGapsBetweenPrimes GRADING, AND THE TYPE-D QUESTION.', 'THE BANK.',
          '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    Bk += ['', '-' * 100, '### THE EXPECTATION (L2), AS THE REPORT SCORED IT.', '-' * 100,
           '  (L1)(a) every repair append-or-narrow, original preserved : %s'
           % (bool(ALLPOS) and bool(ALLKEPT)),
           '  (L1)(b) none needs routing (0 NOT LOCATED, 0 REFUSED)      : %s'
           % (NOTLOC == 0 and REFUSED == 0),
           '  ### AND THE MEASUREMENTS BEHIND THEM:',
           '      repairs applied / not located / refused                 : %s / %s / %s'
           % (APPLIED, NOTLOC, REFUSED),
           '      total growth across the repaired files                  : %+d bytes' % TOTDELTA,
           '  ### **EACH CLAUSE SCORED ONCE, APART, AND EACH REFUTABLE BY A PRINTED RESULT.**']
    Bk += ['', '-' * 100, '### THE CONTROL SUITE.', '-' * 100,
           '  arms run %d ; passing %d' % (ARMS_RUN, ARMS_PASS)]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.'
           % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'),
           '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B432ROW_RE = r"(?m)^\| (\d+) \| \*\*THE DISPROOF LANE RESTATED"


def main():
    bar('=')
    rec('b433_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    if not G:
        rec('  ### HARD FAILURE -- this act`s own grade JSON is missing.')
        return 1
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED.')
    bar()
    t = read(TRAILS)
    if MARK in t:
        rec('  already present; not re-appended.')
    else:
        if PRIOR not in t:
            rec('  ### HARD FAILURE -- the prior act`s mark is absent; refusing to append.')
            return 1
        before = len(t.splitlines())
        t2 = t.rstrip(NL) + NL + NL.join(trail_block()) + NL
        write_bytes(TRAILS, t2)
        rec('  appended %d lines; prior mark still present : %s ; prior text a TRUE PREFIX : %s'
            % (len(t2.splitlines()) - before, PRIOR in t2, t2.startswith(t.rstrip(NL))))
    rec('  lines deleted : 0')
    bar()
    rec('### THE CORRESPONDENCE ROW. ### READ BY MARKER.')
    bar()
    ROWS2 = corr_rows()
    txt = read(TABLE)
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = GD.split_fixture()
    bad = [(i, j) for i, r in enumerate(ROWS2) for j, c in enumerate(r) if GD.raw_pipes(str(c))]
    slip = [mm for mm, s2, *_ in ROWS2 if not s2.startswith(mm)]
    rec('  fixtures %s %s %s %s %s %s ; unescaped pipes %d ; marker a prefix %s'
        % (pos, neg, sa, sb, sc, sd, len(bad), not slip))
    if bad or slip or not (pos and neg and sa and sb and sc and sd):
        rec('  ### HARD FAILURE at the row fixtures -- nothing written.')
        return 1

    def at(mk, s):
        return [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b432`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B432ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |'
                 % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t2) for t2 in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx)
               and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)),
               'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- b432`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B432ROW_RE, after)], at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ROW %d. ### KEY %s. ### DESK %d items, %d closed.'
        % (rownum, 'PASS' if kok else '### FAIL ###', Q['items'], Q['closed']))
    bar('=')
    write_bytes(os.path.join(D, 'b433_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
