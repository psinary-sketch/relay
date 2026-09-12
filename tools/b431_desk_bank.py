# -*- coding: utf-8 -*-
"""b431_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b431 the LongGapsBetweenPrimes grading and the Type-D question -->'
PRIOR = "<!-- b430 the self-control: the corpus's own terminal graded twice -->"
BANKOUT = os.path.join(D, 'b431_the_long_gaps_grading.txt')
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


FACE = read(os.path.join(D, 'b431_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b431_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

try:
    G = json.loads(read(os.path.join(D, 'b431_the_grade.json')) or '{}')
except Exception:
    G = {}
CHK = read(os.path.join(D, 'b431_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS = (int(_a.group(1)), int(_a.group(2))) if _a else (0, 0)

GRADE = G.get('grade', 'NO GRADE')
TYPED = G.get('typed_verdict', 'NO VERDICT')
PIN = str(G.get('pin_post', ''))[:12]
PAPERSHA = str(G.get('paper_sha256', ''))[:16]
TC = G.get('toolchain', '')
PROFLINE = G.get('profile_line') or ''
MAPPED, OFN = G.get('clauses_mapped', 0), G.get('clauses_total', 0)

ROWMARK = ('**THE LongGapsBetweenPrimes TERMINAL GRADES %s AGAINST THE PAPER`S OWN THEOREM 1.1, '
           'AND THE TYPE-D QUESTION READS %s**' % (GRADE, TYPED)).replace('`', chr(0x2019))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — '
        'the rows grading a declaration the record has classified absent (b373). **OPEN.** '
        '**LIST 3** — the undated figures across the roster (b374). **OPEN.** **LIST 4** — the '
        'bibliography entries nothing cites (b374). **OPEN.** Trigger: the ruling on which test '
        'governs, or any disposition on the four open lists.')

DESK = [
    ('the LongGapsBetweenPrimes grading (leg 2 of the b430-b432 sortie)', 'CLOSE',
     'RUN at b431: repository pinned at %s, paper pinned at sha256 %s, foreign toolchain %s '
     'against the corpus`s v4.29.1; built one job at a time; profile from the printer`s own '
     'output. GRADE %s against the paper`s Theorem 1.1, %d of %d clauses mapped.'
     % (PIN, PAPERSHA, TC, GRADE, MAPPED, OFN)),
    ('the Type-D question', 'CLOSE',
     'DECIDED at b431 by unfolding and never by the word: **%s**. The paper chooses a residue '
     'class modulo every prime p <= x and assembles by CRT into one class mod Q(x); the '
     'keystone`s compiled lemma takes one syntactic coupling with a period FIXED BY THE TERM and '
     'exhibits a witness whose modulus set is a SINGLETON. They part at what is quantified.'
     % TYPED),
    ('the conspiracy keystone`s lemma name and prose', 'STANDING',
     'ROUTED AND NOT ACTED ON. `Module1.crt_exhaustiveness` invokes no Chinese Remainder Theorem: '
     'its witness is `ofPeriodic sc.period`, `moduli := {L}`, and its proof is the periodic lift. '
     'The keystone`s prose says the exclusion covers *"what the Chinese Remainder Theorem explains '
     'at every finite modulus"*. **THE LEMMA IS TRUE AND CLEANLY PROVED; IT IS THE NAME AND THE '
     'PROSE THAT CLAIM CRT.** No bridge typed, keystone unedited, grade unmoved. The author rules.'),
    ('the three gradings, cited nowhere', 'STANDING',
     'b429`s, b430`s and b431`s are banked at relay and entered on the trails. TRIGGER: *cited '
     'nowhere until the author rules whether they are.* 0 corpus documents cite any of them.'),
    ('the pre-lock network read at b431 step zero', 'STANDING',
     'DECLARED ON THE FACE, not absorbed. The repository address was resolved by `ls-remote` '
     'before the lock; both pins are printed and they agree. **A DECLARED BREACH THAT CHANGED '
     'NOTHING IS STILL A DECLARED BREACH**, and the author may strike the act for it.'),
    ('the fourth grade`s standing in the corpus`s vocabulary', 'STANDING',
     'ROUTED at b430 and not ruled. (R40) seats `NOT THE CLAIM`; the two documents that DEFINE '
     'the corpus`s grades still name three.'),
    ('the write list that omits the ritual`s own writes', 'STANDING',
     'ROUTED at b430, where two arms failed for it. **b431`s write list NAMES `banked_index.py` '
     'AND `b373_pins.json` explicitly**, so the same omission cannot recur at this act; whether '
     'the ritual`s own side-effect writes should be named on every face is the author`s.'),
    ('the disproof lane, named and not opened (b428)', 'STANDING',
     'Named at b428; leg 3 restates it with a worked case and does not open it. TRIGGER: the '
     'instrument lane opening.'),
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
    ('the scan`s sites against the lock`s zero', 'STANDING',
     'The (R36) instrument item. UNCHANGED by b430`s repair, which touched only which stems the '
     'scan reads.'),
    ('row U1', 'STANDING', 'FROZEN AT SIX; untouched by this act.'),
    ('M-2', 'STANDING', 'OWED and stays owed.'),
    ('h2', 'STANDING', 'WHERE THE DEPOSIT LEFT IT.'),
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
    prof = PROFLINE.split("' ")[-1] if PROFLINE else 'NOT READ'
    L = ['', MARK, '',
         '### b431 — the LongGapsBetweenPrimes grading, and the Type-D question — filed 2026-09-12',
         '',
         '**A second stranger graded by the same protocol, and a question about the corpus’s own '
         'keystone decided by unfolding. __TRIGGER: cited nowhere until the author rules whether '
         'it is.__ Banked at relay; no corpus document cites it.**', '',
         '#### A breach of order, declared', '',
         '**The repository address was resolved by `ls-remote` at step zero, before this act’s '
         'face was locked.** That is a network read ahead of the lock and the rule says the lock '
         'comes first. It is recorded at `data/b431_stepzero_lsremote.txt`; the post-lock pin is '
         'printed beside it and **the two agree at `%s`**. The breach changed nothing and is a '
         'breach regardless.' % PIN, '',
         '#### The addresses, and the terminal', '',
         'Two, and no others; nothing guessed. `github.com/openai/LongGapsBetweenPrimes` at '
         '`%s`; the paper at `cdn.openai.com`, `sha256 %s`. **The README names no theorem** — as '
         'at b429 — and the terminals come from `formalization.yaml`, which declares three main '
         'results and says the project formalizes *“Theorem 1.1 and Proposition 1.2”*. Of the '
         'three, the one whose **statement** is Theorem 1.1 is `LongGapsBetweenPrimes.'
         'long_prime_gaps`, chosen by reading the statements and not the names.' % (PIN, PAPERSHA),
         '',
         'Foreign toolchain `%s` against the corpus’s `v4.29.1` — **the foreign pin is newer**, '
         'again. The build ran one job at a time. The profile is `%s`, read from the printer’s own '
         'output.' % (TC, prof), '',
         '#### The grade', '',
         '**GRADE: `%s`, against the paper’s Theorem 1.1** — the claim named in the same sentence, '
         'under (R40). %d of %d clauses of Theorem 1.1 map to the terminal’s own text: an absolute '
         'constant `c > 0`; all sufficiently large `X`; a gap between **consecutive** primes '
         '(`Nat.nth Nat.Prime (n+1)` and `Nat.nth Nat.Prime n`); the gap below `X`; and the bound '
         '`log X (log₂X)² log₄X / (log₃X)²` term for term.' % (GRADE, MAPPED, OFN), '',
         '**The four clauses b429 compared were applied here too**, because b430 settled that they '
         'are the discipline’s and not one act’s: the profile from the printer with `sorryAx` '
         'sought by name; the statement unfolded to its base objects; the fourth grade available; '
         'and the definitions put to `rowgen`’s `defenc` with a control appended so that a `False` '
         'is a result.', '',
         '#### The Type-D question: **%s**' % TYPED, '',
         '**Decided by unfolding and never by the word.** One of these is *called* '
         '`crt_exhaustiveness`; the other *uses* the Chinese remainder theorem in its proof. '
         'Neither fact is evidence about what either states.', '',
         '- **The paper:** *“By the Chinese remainder theorem, choose 0 ≤ b < Q with b ≡ −a_p '
         '(mod p) for every prime p ≤ x”*, with `Q(x) = ∏_{p≤x} p`. **The number of moduli is '
         'π(x) and it grows without bound** — the theorem is about all sufficiently large `X`, '
         'with `x = (log X)/3`.',
         '- **The keystone’s lemma:** `crt_exhaustiveness (sc : StructuralCoupling) : ∃ m : '
         'ModularCoupling, ∀ n, sc.eval n ↔ m.eval n`. `StructuralCoupling` is a **syntactic** '
         'inductive over six constructors, each carrying an explicit finite modulus; its `period` '
         'is the lcm of its own moduli and is **fixed by the term**. The witness is `to_modular '
         'sc = ofPeriodic sc.period`, whose **`moduli := {L}` is a singleton**.', '',
         '**They part at what is quantified — a fixed period against all moduli.** And one '
         'refinement the measurement adds to that reading: the keystone’s lemma does not range '
         'over all moduli and then collapse them. **Its witness never leaves a single modulus at '
         'all.** No product over primes appears in the statement or in the proof, and no Chinese '
         'remainder theorem is invoked — the proof is the periodic lift, `ofPeriodic_eval`.', '',
         '**What the verdict does not say.** It does **not** say the keystone’s lemma is false: it '
         'is true and cleanly proved — a predicate built from finitely many congruence conditions '
         '*is* a congruence condition modulo the lcm of its moduli. It does **not** say the '
         'paper’s construction is an instance of it, or that it is not: the two statements do not '
         'quantify over the same thing, so neither contains the other and no bridge is available '
         'to be typed.', '',
         '**And one finding about the corpus’s own keystone, routed and not acted on.** The name '
         '`crt_exhaustiveness`, and the keystone’s prose about *“what the Chinese Remainder '
         'Theorem explains at every finite modulus”*, describe the intuition; the statement is the '
         'periodic lift. **No bridge typed, keystone unedited, grade unmoved.** The author rules '
         'whether the name and the prose should say what the lemma says.', '',
         '#### The arc, and the lanes this act leaves where it found them', '',
         '**W-ORD-WITNESS-ENUMERATION stays checkpointed after site (iii)**; this act entered no '
         'site. The disproof lane named at b428 stays **named and not opened**. Both instrument '
         'lanes stay parked and the wave stays parked.', '',
         '#### The four lists', '', FOUR, '',
         '#### What this act did not do', '',
         '0 grades of the corpus’s own moved, conferred or minted on the record. 0 bridges typed. '
         '0 keystones edited, annotated or re-graded. 0 premises discharged. 0 doors restated. '
         '0 routes proposed. 0 lanes opened. 0 kappa measured. 0 corpus `.lean` files touched and '
         '0 corpus kernel builds. 0 rows of `FACES_LEDGER.md`. 0 register rows. 0 bytes of the '
         'foreign repository entered any rostered repository. 0 claims about either conjecture’s '
         'truth. 0 deposit actions. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS A SECOND EXTERNAL GRADING AND A QUESTION ABOUT THE CORPUS'S OWN "
         "KEYSTONE DECIDED BY UNFOLDING. ### IT MOVES NO GRADE, TYPES NO BRIDGE, EDITS NO KEYSTONE "
         "AND TOUCHES NO CORPUS KERNEL")


def corr_rows():
    m = ROWMARK + " (b431)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY CLONE, FETCH OR BUILD**, chained on "
            "b378's gate run as b431 -- @GR@ gates read, @GDG@ checked by digest. **AND ONE BREACH "
            "DECLARED ON THE FACE: THE REPOSITORY ADDRESS WAS RESOLVED BY ls-remote BEFORE THE "
            "LOCK; BOTH PINS ARE PRINTED AND THEY AGREE AT @PIN@.** **TWO ADDRESSES SUPPLIED, TWO "
            "RESOLVED, 0 GUESSED; THE PAPER PINNED AT sha256 @SHA@.** **THE README NAMES NO "
            "THEOREM; THE TERMINAL COMES FROM formalization.yaml AND IS CHOSEN BY ITS STATEMENT.** "
            "**BUILT ON A FOREIGN TOOLCHAIN @TC@ AGAINST THE CORPUS'S v4.29.1, ONE JOB AT A TIME; "
            "PROFILE @PROF@ FROM THE PRINTER'S OWN OUTPUT.** **GRADE @GRADE@ AGAINST THE PAPER'S "
            "THEOREM 1.1, @MAPPED@ OF @OFN@ CLAUSES MAPPED; ALL FOUR OF b429'S CLAUSES APPLIED.** "
            "**TYPE-D: @TYPED@ -- THE PAPER CHOOSES A CLASS MODULO EVERY PRIME p <= x AND "
            "ASSEMBLES BY CRT; THE KEYSTONE'S LEMMA TAKES ONE COUPLING WITH A PERIOD FIXED BY THE "
            "TERM AND ITS WITNESS'S MODULUS SET IS A SINGLETON. THEY PART AT WHAT IS QUANTIFIED.** "
            "0 GRADES MOVED, 0 BRIDGES TYPED, 0 KEYSTONES EDITED, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED OR MOVED. A FOREIGN terminal was built and graded; "
            "Module1.crt_exhaustiveness was READ and is unchanged")
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX, CARRYING "
            "THE GRADING AND THE TYPE-D FINDING; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO "
            "CORPUS KERNEL FILE; THE CLONE, THE TOOLCHAIN AND EVERY BUILD ARTEFACT OUTSIDE EVERY "
            "ROSTERED REPOSITORY -- 0 CONTENT LOST")
    grade = ("### THE OBJECT GRADED AGAINST IS THE PAPER AT ITS OWN DIGEST AND NOT A PARAPHRASE; "
             "THE PROFILE IS THE PRINTER'S OWN OUTPUT; AND THE TYPE-D VERDICT RESTS ON WHAT EACH "
             "STATEMENT QUANTIFIES OVER RATHER THAN ON WHAT EITHER IS CALLED -- A LEMMA'S NAME IS "
             "EVIDENCE ABOUT ITS AUTHOR'S INTENT AND NO EVIDENCE AT ALL ABOUT ITS CONTENT")
    status = ("data/b431_the_long_gaps_grading.txt; data/b431_components.txt; "
              "data/b431_extract.txt; data/b431_the_grade.json; data/b431_paper_pin.txt; "
              "data/b431_stepzero_lsremote.txt; data/b431_build.log; data/b431_profile.txt; "
              "data/b431_checks.txt; "
              "data/b431_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@PIN@', PIN).replace('@SHA@', PAPERSHA).replace('@TC@', TC)
                .replace('@GRADE@', GRADE).replace('@TYPED@', TYPED)
                .replace('@MAPPED@', str(MAPPED)).replace('@OFN@', str(OFN))
                .replace('@PROF@', 'THE STANDARD THREE, NO sorryAx' if G.get('profile_clean')
                         else 'NOT READ CLEAN'))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the long gaps grading', 'long_prime_gaps graded', 'the type-d question',
           'is the covering construction the keystone`s lemma', 'crt exhaustiveness unfolded')
MUST_NOT_HIT = ('the keystone is wrong', 'twin primes proved', 'the conjecture is settled')
KEY = 'the-long-gaps-grading'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b431 GRADED openai/LongGapsBetweenPrimes' long_prime_gaps AGAINST THE PAPER'S OWN THEOREM "
        "1.1. Repository pinned at %s, paper at sha256 %s, foreign toolchain %s against the "
        "corpus's v4.29.1; built one job at a time; profile from #print axioms. GRADE %s, %s of %s "
        "clauses mapped, all four of b429's clauses applied. THE TYPE-D QUESTION: %s. The paper "
        "chooses a residue class modulo every prime p <= x and assembles by CRT into one class mod "
        "Q(x); the keystone's compiled crt_exhaustiveness takes ONE syntactic coupling whose "
        "period is fixed by the term, and its witness's modulus set is a SINGLETON -- no product "
        "over primes and no CRT in the proof, which is the periodic lift. They part at what is "
        "quantified. The lemma is true; it is the name and the keystone's prose that claim CRT, "
        "and that is ROUTED. No bridge typed, keystone unedited. Cited in no corpus document."
        % (PIN, PAPERSHA, TC, GRADE, MAPPED, OFN, TYPED))
    grade = ("### NO GRADE OF THE CORPUS'S OWN MOVED. ### NO BRIDGE TYPED. ### NO KEYSTONE EDITED. "
             "### NOTHING DEPOSITS")
    where = ("data/b431_the_long_gaps_grading.txt; data/b431_components.txt; "
             "data/b431_the_grade.json; data/b431_registration_2026-09-12.txt (LOCKED, %d gates "
             "read, %d by digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b431 (the LongGapsBetweenPrimes grading and the Type-D question)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE LongGapsBetweenPrimes GRADING (b431).%s    (%r, %r,%s     %r,%s'
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
        rec('    %-58s reaches the b431 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the grade carried', GRADE in out),
                      ('the Type-D verdict carried', TYPED in out),
                      ('the singleton finding carried', 'SINGLETON' in out),
                      ('cited nowhere carried', 'Cited in no corpus document' in out)):
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
           '  (L2)(a) the terminal grades DERIVES            : %s' % (GRADE == 'DERIVES'),
           '  (L2)(b) its profile is clean                   : %s' % bool(G.get('profile_clean')),
           '  (L2)(c) the Type-D verdict reads TWO THEOREMS  : %s'
           % (TYPED == 'TWO THEOREMS SHARING A NAME'),
           '  (L2)(c) and its REASON, scored apart -- parting at what is quantified : %s'
           % bool(G.get('witness_moduli_singleton')),
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


B430ROW_RE = r"(?m)^\| (\d+) \| \*\*THE SELF-CONTROL"


def main():
    bar('=')
    rec('b431_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('  b430`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B430ROW_RE, txt)])
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
    rec('  after -- b430`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B430ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b431_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
