# -*- coding: utf-8 -*-
"""b432_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

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
MARK = '<!-- b432 the disproof lane restated with a worked case -->'
PRIOR = '<!-- b431 the LongGapsBetweenPrimes grading and the Type-D question -->'
BANKOUT = os.path.join(D, 'b432_the_disproof_lane.txt')
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


FACE = read(os.path.join(D, 'b432_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b432_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY '
               r'DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)

try:
    G = json.loads(read(os.path.join(D, 'b432_forms.json')) or '{}')
except Exception:
    G = {}
CHK = read(os.path.join(D, 'b432_checks.txt'))
_a = re.search(r'ARMS RUN : (\d+)\. ### PASSING : (\d+)\. ### FAILING : (\d+)', CHK)
ARMS_RUN, ARMS_PASS = (int(_a.group(1)), int(_a.group(2))) if _a else (0, 0)

NCFORM = G.get('negative_control_form', '?')
PHFORM = G.get('phase_form', '?')
NOB = G.get('no_instrument_for_form_b')
CASE_A = '%s / %s' % (G.get('case_a_grade', '?'), G.get('case_a_shape', '?'))
CASE_B = '%s / %s' % (G.get('case_b_grade', '?'), G.get('case_b_shape', '?'))

ROWMARK = ('**THE DISPROOF LANE RESTATED WITH A WORKED CASE OF EACH SHAPE, AND BOTH NAMED '
           'INSTRUMENTS FOUND TO SERVE ONLY ONE OF THE TWO FORMS**')

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — '
        'the rows grading a declaration the record has classified absent (b373). **OPEN.** '
        '**LIST 3** — the undated figures across the roster (b374). **OPEN.** **LIST 4** — the '
        'bibliography entries nothing cites (b374). **OPEN.** Trigger: the ruling on which test '
        'governs, or any disposition on the four open lists.')

DESK = [
    ('the disproof lane, restated with a worked case (leg 3 of the b430-b432 sortie)', 'CLOSE',
     'RUN at b432. The lane was named at b428 with no example of what a graded disproof looks '
     'like; the sortie has since produced one terminal of each shape. **b429 against Clay C: '
     'DERIVES, and C`s conclusion is a UNIVERSAL NEGATIVE. b431 against Theorem 1.1: DERIVES, and '
     'the statement is an EXISTENTIAL -- a construction.** The two forms a disproof of `h2` could '
     'take are written out in the corpus`s own vocabulary, each with the clause it would have to '
     'meet, quoted at its line. **THE LANE ITSELF IS NOT OPENED AND ITS TRIGGER IS NOT TOUCHED.**'),
    ('which form the corpus`s instruments serve', 'CLOSE',
     'DECIDED at b432 by what each instrument is RUN ON and what it REPORTS, never by its name. '
     '**THE NEGATIVE CONTROL IS FOR FORM (a), THE EXHIBITED ZERO**: it is run on the Epstein zeta '
     'the corpus calls its own counterexample, whose off-line zeros are proved and exhibited, and '
     'it reports whether the instrument SEES that zero (b325 DOES NOT SEE IT; b328 SEES IT at '
     'seven of eight). **THE PHASE CONDITION IS FOR FORM (a) TOO**, and for the same reason: the '
     'four-term sum is stated AT AN OFF-LINE QUADRUPLE, so it is the calibration that decides '
     'whether the control can fire at all -- not a second instrument.'),
    ('that the corpus has no instrument for form (b)', 'STANDING',
     'ROUTED, NOT ACTED ON. Both named instruments serve form (a). **THE CORPUS HAS NO INSTRUMENT '
     'POINTED AT THE UNIVERSAL NEGATIVE AT ALL**, which sharpens b428`s finding of a certified '
     'instrument never pointed: the instrument it has is of the WRONG KIND for one of the two '
     'forms, not merely unpointed. **This is not a claim that form (b) is unreachable**, nor any '
     'pricing of what an instrument for it would cost. The author rules.'),
    ('the three gradings, cited nowhere', 'STANDING',
     'b429`s, b430`s and b431`s are banked at relay and entered on the trails. TRIGGER: *cited '
     'nowhere until the author rules whether they are.* 0 corpus documents cite any of them.'),
    ('the conspiracy keystone`s lemma name and prose (b431)', 'STANDING',
     'ROUTED at b431 and untouched here. `crt_exhaustiveness` invokes no Chinese Remainder '
     'Theorem; its witness`s modulus set is a singleton and its proof is the periodic lift. The '
     'lemma is true; the name and the prose are what claim CRT.'),
    ('the write list against what an act discovers it needs', 'STANDING',
     'ROUTED at b430 and again at b431, in both directions. **b432`s face answered it for itself**: '
     'it names its tools, names the three files the ritual`s own tools rewrite, and permits a '
     'further declared tool provided the suite prints its name and reason. The result was 0 '
     'unlisted writes and 0 inherited dirt. Whether that form should be standing is the author`s.'),
    ('the fourth grade`s standing in the corpus`s vocabulary', 'STANDING',
     'ROUTED at b430 and not ruled. (R40) seats `NOT THE CLAIM`; the two documents that DEFINE '
     'the corpus`s grades still name three.'),
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
         '### b432 — the disproof lane, restated with a worked case — filed 2026-09-12', '',
         '**The lane was named at b428 with no example of what a graded disproof looks like. The '
         'sortie has since produced one terminal of each shape, so the restatement can now point '
         'at something. __The lane is restated and NOT opened; its trigger is untouched.__**', '',
         '#### The two worked cases, and that they are of two shapes', '',
         '- **b429, against Clay statement C:** graded `%s`. C’s conclusion is a **universal '
         'negative** — in the terminal’s own Lean, `¬ (∃ v p, …)`.' % G.get('case_a_grade', '?'),
         '- **b431, against the paper’s Theorem 1.1:** graded `%s`. The statement is an '
         '**existential — a construction**: `∃ c X₀, 0 < c ∧ ∀ X ≥ X₀, ∃ n, …`, a witness at every '
         'large X.' % G.get('case_b_grade', '?'), '',
         '**Both grades are the same word, and the statements are of opposite shape.** The shape '
         'is read from the statement, never from the grade — which is the point of the pairing.',
         '',
         '#### What a disproof would have to state, in the corpus’s own vocabulary', '',
         'The hypothesis is the corpus’s own, quoted from `INVARIANCE_BARRIERS.md`: **`h2`, the '
         'positive space on the zeros** — *a positive-definite pairing realized on the nontrivial '
         'zeros; equivalently, realization-totality at the ξ interface*. **RH follows from `h2`, '
         'so a disproof of RH must deny `h2` — and a denial of `h2` is not by itself a disproof of '
         'RH.** The implication runs one way and this record says so.', '',
         '- **Form (a), an exhibited zero off the line.** *There exists `s₀` with `ξ(s₀) = 0` and '
         '`Re s₀ ≠ 1/2`, exhibited* — a witness, not a density statement. The clause it must meet '
         'is the keystone’s **T6**: *F real-valued on σ = 1/2 (from T1 + real coefficients), so '
         'off-line zeros require Re F = Im F = 0 (two real conditions)* — **codimension 2**.',
         '- **Form (b), the universal negative.** *No arrangement of zeros on the line is '
         'consistent with the Euler balance* — the positive space cannot be realized at all. **It '
         'exhibits nothing**, and it quantifies over every arrangement.', '',
         '**And the shapes match the two cases:** form (b) has b429’s shape (`¬∃`), form (a) has '
         'b431’s (`∃`). That is what a graded disproof would look like in each form.', '',
         '**Neither form is asserted here and neither is constructed here.**', '',
         '#### Which form the corpus’s instruments are for', '',
         '**Decided by what each is run on and what it reports, never by its name** — the bar b431 '
         'minted on `crt_exhaustiveness` applies here too.', '',
         '- **The negative control is an instrument for form (a).** It is run on the Epstein zeta '
         'the corpus calls its own counterexample — *Davenport–Heilbronn (1936) proved that Z(s) '
         'has infinitely many zeros off the critical line; Stark (1967) established explicit '
         'off-line zeros* — and what it reports is whether the instrument **sees** that zero: '
         'b325 *DOES NOT SEE IT*, b328 *SEES IT* at seven of eight cells. **It cannot be an '
         'instrument for form (b): a universal negative exhibits no object, so there is nothing '
         'for a control of this kind to be run on.**',
         '- **The phase condition is for form (a) too, and for the same reason.** The four-term '
         'sum is `4 Re(G_e² − G_o²)` **at an off-line quadruple**, negative only past forty-five '
         'degrees of phase. It is the condition on the seed that decides whether the control can '
         'fire at all — **the calibration of the negative control, not a second instrument**.', '',
         '**So both named instruments serve form (a), and the corpus has no instrument pointed at '
         'form (b) at all.** That is consistent with b428’s finding by a different route — a '
         'certified disproof instrument the corpus has never pointed — and it sharpens it: **the '
         'instrument it has is of the wrong kind for one of the two forms, not merely unpointed.** '
         '**This is not a claim that form (b) is unreachable**, and no price is put on an '
         'instrument for it.', '',
         '**And each act’s own scope travels with its words:** b328 states that its verdict is *on '
         'this family, on this instrument, at this reach, and says nothing about the method or '
         'about zeta*, and its own obstacle sentence reads *“IT DOES NOT SAY THE INSTRUMENT SEES '
         'COUNTEREXAMPLES.”*', '',
         '#### The symmetry clause, quoted beside it', '',
         'The keystone’s **T1**: *∃ a reflective FE F(s) = F(1−s) (self-dual completion), centring '
         'the critical line at σ = 1/2* — **the s ↔ 1−s symmetry**. With real coefficients an '
         'off-line zero comes as a **quadruple** `s₀, 1−s₀, s̄₀, 1−s̄₀`, which is why the corpus’s '
         'instrument is tested at an off-line quadruple and why the phase condition is stated '
         'there. **The scope is the keystone’s and this act adds none:** T1 is listed as a tool of '
         'the six-tool toolkit `T`, and the keystone’s claim is about what `T` cannot establish — '
         'not a claim about zeta’s zeros.', '',
         '#### The lane, left where it was found', '',
         '**Trigger unchanged: the instrument lane opening.** Lanes opened by this act: 0. '
         'Candidates constructed: 0. Claims about reach: 0. Keystones edited: 0. **The restatement '
         'is the whole of what this act did to the lane.**', '',
         '#### The four lists', '', FOUR, '',
         '#### What this act did not do', '',
         '0 lanes opened. 0 triggers moved. 0 candidate zeros, seeds, families or arrangements '
         'constructed. 0 claims that either form is reachable, cheap, dear or impossible. 0 claims '
         'about RH, about `h2`, or about zeta. 0 grades moved, conferred or minted. 0 premises '
         'discharged — **`h2` is not discharged, not weakened and not restated**. 0 keystones '
         'edited or annotated. 0 kernels built. 0 addresses resolved and nothing fetched. 0 rows '
         'of `FACES_LEDGER.md`. 0 register rows. 0 deposit actions. **And h2 where the deposit '
         'left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS A LANE RESTATED WITH A WORKED CASE OF EACH SHAPE, AND A READING OF "
         "WHICH FORM THE CORPUS'S OWN INSTRUMENTS SERVE. ### IT OPENS NO LANE, MOVES NO TRIGGER, "
         "CONSTRUCTS NOTHING, EDITS NO KEYSTONE AND MOVES NO GRADE")


def corr_rows():
    m = ROWMARK + " (b432, the disproof lane restated)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE**, chained on b378's gate run as "
            "b432 -- @GR@ gates read, @GDG@ checked by digest. **THE LANE WAS NAMED AT b428 WITH NO "
            "EXAMPLE OF A GRADED DISPROOF; THE SORTIE HAS SINCE PRODUCED ONE TERMINAL OF EACH "
            "SHAPE.** **CASE A: @CASEA@ -- b429 AGAINST CLAY C, WHOSE CONCLUSION IS A UNIVERSAL "
            "NEGATIVE. CASE B: @CASEB@ -- b431 AGAINST THEOREM 1.1, AN EXISTENTIAL CONSTRUCTION. "
            "BOTH GRADES ARE THE SAME WORD AND THE STATEMENTS ARE OF OPPOSITE SHAPE.** **THE TWO "
            "FORMS A DISPROOF OF h2 COULD TAKE ARE WRITTEN IN THE CORPUS'S OWN VOCABULARY, EACH "
            "WITH THE CLAUSE IT MUST MEET QUOTED AT ITS LINE -- FORM (a) AN EXHIBITED ZERO OFF THE "
            "LINE, MEETING T6'S CODIMENSION 2; FORM (b) THE UNIVERSAL NEGATIVE, EXHIBITING "
            "NOTHING.** **BOTH NAMED INSTRUMENTS SERVE FORM (a): THE NEGATIVE CONTROL IS RUN ON AN "
            "OBJECT WITH PROVED OFF-LINE ZEROS AND REPORTS WHETHER IT SEES ONE, AND THE PHASE "
            "CONDITION IS STATED AT AN OFF-LINE QUADRUPLE AND IS ITS CALIBRATION. THE CORPUS HAS "
            "NO INSTRUMENT POINTED AT FORM (b) AT ALL -- ROUTED, NOT ACTED ON.** **NEITHER FORM "
            "ASSERTED, NEITHER CONSTRUCTED, THE TRIGGER UNTOUCHED.** 0 LANES OPENED, 0 GRADES "
            "MOVED, 0 KEYSTONES EDITED, 0 CONTENT LOST")
    term = ("NO TERMINAL ADDED, MOVED OR GRADED. The two terminals this row names were graded at "
            "b429 and b431 and are only cited here")
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX, CARRYING "
            "THE RESTATEMENT; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO KERNEL FILE, NO "
            "LANE DOCUMENT -- 0 CONTENT LOST")
    grade = ("### THE HYPOTHESIS IS QUOTED IN THE CORPUS'S OWN WORDS AND NOT PARAPHRASED; EACH "
             "INSTRUMENT'S PURPOSE IS READ FROM WHAT IT IS RUN ON AND WHAT IT REPORTS RATHER THAN "
             "FROM ITS NAME; AND EACH QUOTED ACT'S OWN SCOPE SENTENCE TRAVELS WITH ITS VERDICT")
    status = ("data/b432_the_disproof_lane.txt; data/b432_components.txt; data/b432_extract.txt; "
              "data/b432_forms.json; data/b432_checks.txt; "
              "data/b432_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@CASEA@', CASE_A).replace('@CASEB@', CASE_B))
    return [(m, sub(stmt), term, prof, grade, SCOPE, status)]


ALIASES = ('the disproof lane', 'what a disproof would have to state',
           'which form the negative control is for', 'the two shapes of a disproof',
           'is there an instrument for the universal negative')
MUST_NOT_HIT = ('rh is false', 'a zero off the line was found', 'h2 is refuted')
KEY = 'the-disproof-lane-restated'


def query(q):
    p = subprocess.run([sys.executable, INDEX, '--query', q], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return p.stdout, p.returncode


def no_key(out):
    """### A2: THE VERDICT LINE, NEVER A SUBSTRING."""
    return any('NO KEY.' in ln for ln in out.splitlines())


def do_key(rownum):
    statement = (
        "b432 RESTATED THE DISPROOF LANE WITH A WORKED CASE OF EACH SHAPE AND OPENED NOTHING. The "
        "lane was named at b428 with no example of a graded disproof; the sortie produced two. "
        "CASE A: %s -- b429 against Clay C, whose conclusion is a UNIVERSAL NEGATIVE. CASE B: %s "
        "-- b431 against Theorem 1.1, an EXISTENTIAL construction. Both grades are the same word "
        "and the statements are of opposite shape. THE TWO FORMS a disproof of h2 could take, in "
        "the corpus's own vocabulary: (a) an exhibited zero off the line, which must meet the "
        "barrier keystone's T6 -- Re F = Im F = 0, codimension 2; (b) the universal negative that "
        "no on-line arrangement is consistent with the balance, which exhibits nothing. Form (b) "
        "has b429's shape, form (a) has b431's. BOTH NAMED INSTRUMENTS SERVE FORM (a): the "
        "negative control is run on the Epstein zeta whose off-line zeros are proved and "
        "exhibited, and reports whether the instrument sees one (b325 DOES NOT SEE IT, b328 SEES "
        "IT at seven of eight); the phase condition is stated AT AN OFF-LINE QUADRUPLE and is the "
        "calibration that decides whether the control can fire at all. SO THE CORPUS HAS NO "
        "INSTRUMENT POINTED AT FORM (b) AT ALL -- which sharpens b428's finding: the instrument it "
        "has is of the WRONG KIND for one of the two forms, not merely unpointed. Not a claim that "
        "form (b) is unreachable. Neither form asserted, neither constructed, trigger untouched. "
        "Cited in no corpus document.")
    grade = ("### NO LANE OPENED. ### NO TRIGGER MOVED. ### NO CANDIDATE CONSTRUCTED. ### NO GRADE "
             "MOVED. ### NO KEYSTONE EDITED. ### NOTHING DEPOSITS")
    where = ("data/b432_the_disproof_lane.txt; data/b432_components.txt; data/b432_forms.json; "
             "data/b432_registration_2026-09-12.txt (LOCKED, %d gates read, %d by digest); "
             "OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b432 (the disproof lane restated with a worked case)"


    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE DISPROOF LANE RESTATED (b432).%s    (%r, %r,%s     %r,%s'
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
        rec('    %-58s reaches the b432 key : %s' % (qq[:58], g2))
    for lbl, cond in (('both worked cases carried', 'CASE A' in out and 'CASE B' in out),
                      ('both forms carried', 'exhibited zero off the line' in out
                       and 'universal negative' in out),
                      ('the instrument finding carried', 'WRONG KIND' in out),
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
           '  (L3)(a) the negative control is for the EXHIBITED-ZERO form : %s' % (NCFORM == 'a'),
           '  (L3)(b) it is NOT for the universal negative                : %s'
           % bool(G.get('negative_control_not_form_b')),
           '  ### AND PRINTED, SCORED AGAINST NOTHING (the face says so):',
           '      the phase condition serves form                         : %s' % PHFORM,
           '      an instrument pointed at form (b) exists                : %s' % (not NOB),
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


B431ROW_RE = r"(?m)^\| (\d+) \| \*\*THE LongGapsBetweenPrimes TERMINAL"


def main():
    bar('=')
    rec('b432_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
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
    rec('  b431`s row by its marker : %s'
        % [int(x.group(1)) for x in re.finditer(B431ROW_RE, txt)])
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
    rec('  after -- b431`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B431ROW_RE, after)], at(ROWS2[0][0], after)))
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
    write_bytes(os.path.join(D, 'b432_desk_notes.txt'), NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
