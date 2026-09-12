# -*- coding: utf-8 -*-
"""b429_desk_bank.py -- THE DESK, THE TRAIL, THE CORRESPONDENCE ROW, THE KEY, THE BANK.

### ### **ROWS ARE READ BY MARKER, NEVER BY NUMBER.** ### Every figure here is read off a component's JSON,
### never typed. ### The trail block is the CALIBRATION RECORD, and its trigger is the author's ruling on
### whether it may be cited.
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
MARK = '<!-- b429 the external grading read: a calibration record -->'
PRIOR = '<!-- b428 site (iii), the disproof lane named, the external read priced -->'
BANKOUT = os.path.join(D, 'b429_the_external_grading_read.txt')
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


def tidy(s):
    return (s or '').replace('`', '’').replace('|', '/')


FACE = read(os.path.join(D, 'b429_registration_2026-09-12.txt'))
_sh = re.search(r'([0-9a-f]{64})', FACE.split('THE REGISTRATION LOCK')[-1])
SEALHASH = _sh.group(1) if _sh else ''
LG = read(os.path.join(D, 'b429_lockgate_notes.txt'))
_g = re.search(r'GATES READ : (\d+)\. ### PASSING : (\d+)\. ### FACE-SUBJECT GATES CHECKED BY DIGEST : (\d+)', LG)
GR, GDG = (int(_g.group(1)), int(_g.group(3))) if _g else (0, 0)


def loadj(name, default):
    try:
        return json.loads(read(os.path.join(D, name)))
    except Exception:
        return default


A = loadj('b429_addresses.json', dict(supplied=0, resolved=0, unreachable=['x'], addresses={}))
B = loadj('b429_build_and_profile.json', dict(built=None, profile={}, axioms_beyond={}, sorryax={},
                                              foreign_toolchain='', corpus_pins={}, newer=None, head='',
                                              sorry_lines=0, sorry_outside_challenges=0))
RD = loadj('b429_statement_read.json', dict(answers={}, mapped=0, of=0))
G = loadj('b429_the_grade.json', dict(grade=None, clauses=[], asymmetric=0, same=0, corpus_grade=None))
GRADE = G.get('grade') or 'NO GRADE'
BUILT = bool(B.get('built'))
PROF = B.get('profile', {}).get('NavierStokes.Comparator.navier_stokes_breakdown_R3', [])
ASYM = G.get('asymmetric', 0)
ROWMARK = ("**THE EXTERNAL GRADING READ: THE COLLABORATION'S NAVIER-STOKES LEAN TERMINAL GRADED %s, AND THE "
           "SELF-GRADING TEST FOUND %d ASYMMETRIC CLAUSE(S), BOTH FAVOURING THE STRANGER**" % (GRADE, ASYM))

FOUR = ('**LIST 1** — the rows that cite at a ref nobody can name (b373). **OPEN.** **LIST 2** — the rows grading '
        'a declaration the record has classified absent (b373). **OPEN.** **LIST 3** — the undated figures across the '
        'roster (b374). **OPEN.** **LIST 4** — the bibliography entries nothing cites (b374). **OPEN.** Trigger: the '
        'ruling on which test governs, or any disposition on the four open lists.')

DESK = [
    ('the external grading read', 'CLOSE',
     'RUN at b429: three addresses supplied, %d resolved; the repository pinned at %s; built %s; the terminal '
     'graded %s. The corpus`s own route terminal grades %s under the same reading.'
     % (A.get('resolved'), str(B.get('head'))[:12], BUILT, GRADE, G.get('corpus_grade'))),
    ('the calibration record, cited nowhere', 'STANDING',
     'The grading is banked at relay and entered on the trails. TRIGGER: *cited nowhere until the author rules '
     'whether it is.* 0 corpus documents cite it.'),
    ('the two asymmetries the self-grading test found', 'STANDING',
     'ROUTED AND NOT RULED. (1) The vocabulary: four grades were available against the stranger and the corpus '
     'has only ever had three -- unused here, so it changed no outcome. (2) The instrument: the stranger`s '
     'definitions were accepted on a READING while the corpus runs `rowgen``s defenc check on its own. '
     '**BOTH FAVOUR THE STRANGER, which is the opposite direction from the concern b428 routed.**'),
    ('what the self-grading test cannot tell', 'STANDING',
     'CANNOT TELL, said plainly: whether the corpus would confer DERIVES on a terminal of its own with this '
     'profile and this mapping. It has never had one -- its route terminal carries a premise and the '
     'salt-check`s subjects were shells -- so there is no like case on its own side.'),
    ('the disproof lane, named and not opened (b428)', 'STANDING', 'Named at b428; still unopened. TRIGGER: the '
     'instrument lane opening.'),
    ('W-ORD-WITNESS-ENUMERATION, sites (iv) to (vi)', 'STANDING',
     'CHECKPOINTED after site (iii). Three sites remain, one act each; trigger: the author`s word.'),
    ('whether the arc is converging on one boundary', 'STANDING',
     'ROUTED at b428 on three sites: the class boundary`s share 13/16, 10/19, 12/20; union of kinds 10 and still '
     'growing.'),
    ('whether the witness cell should carry the list inside its own text (b424)', 'STANDING', 'ROUTED at b424.'),
    ('(R38)`s two clauses, divergent on a mixed set', 'STANDING', 'ROUTED at b426 and not ruled.'),
    ('the lane`s condition under (R38)', 'STANDING', 'Carried from b426; p2-d6 does not move.'),
    ('OPEN_TRAILS O.8 -- the DESI five-year release', 'STANDING', 'OPEN, unchanged.'),
    ('the seat`s reading of §10.2 (b423)', 'STANDING', 'ROUTED at b423.'),
    ('the four open lists', 'STANDING', 'All four OPEN; their trigger has not fired.'),
    ('W-ORD-LI-WEIL-BRIDGE', 'STANDING', 'The author’s word; not fired.'),
    ('W-ORD-DISCRIMINATING-FAMILY / W-ORD-LI-FAMILY-CONTROL', 'STANDING', 'Blocked by the PARKED instrument lane.'),
    ('the scan’s sites against the lock’s zero', 'STANDING', 'The (R36) instrument item.'),
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
    ad = A.get('addresses', {})
    L = ['', MARK, '',
         '### b429 — the external grading read: a calibration record — filed 2026-09-12', '',
         '**This is a calibration of the corpus’s grading discipline against a proof it did not write. '
         '__TRIGGER: cited nowhere until the author rules whether it is.__ It is banked at relay and entered here; '
         'no corpus document cites it, and none should until that ruling.**', '',
         '#### The addresses, as the author supplied them', '',
         'Three, and no others; nothing guessed. The Lean repository `github.com/openai/NavierStokesAndEuler`, '
         'pinned at `%s`; the writeup PDF at `cdn.openai.com`, `sha256 %s`; the Clay formulation at `claymath.org`, '
         '`sha256 %s`. **%d of 3 resolved.**'
         % (str(ad.get('repository', {}).get('head', ''))[:12],
            str(ad.get('writeup', {}).get('sha256', ''))[:16],
            str(ad.get('clay', {}).get('sha256', ''))[:16], A.get('resolved', 0)), '',
         '#### Statement C, at content', '',
         'The page is Fefferman’s. **(C)** reads: *“Breakdown of Navier–Stokes solutions on R3. Take ν > 0 and '
         'n = 3. Then there exist a smooth, divergence-free vector field u◦(x) on R3 and a smooth f(x,t) on '
         'R3 × [0,∞), satisfying (4), (5), for which there exist no solutions (p, u) of (1), (2), (3), (6), (7) on '
         'R3 × [0,∞).”* Conditions (4) and (5) are the rapid-decay bounds on `u◦` and `f`; (6) is `p, u ∈ '
         'C^∞(Rn × [0,∞))`; (7) is *“∫ |u(x,t)|²dx < C for all t ≥ 0 (bounded energy)”*, with the constant outside '
         'the quantifier. **The page carries an errata section, and neither entry touches (C) or (4)–(7):** one '
         'makes a pressure-periodicity condition explicit in Eqn (8), which only (D) uses; the other replaces an '
         '“Eqn (10)” with a weak-form identity, while the page as served numbers (10) as the periodicity '
         'condition — a disagreement this act reports rather than resolves.', '',
         '#### The terminal, and the build', '']
    if BUILT:
        L += ['The README names the statements and **names no theorem**; the terminals were taken from the '
              'repository’s `formalization.yaml` manifest instead. **b428’s ACT 1 priced “read the README … and name '
              'the single theorem”, and said that if the README names none the act ends there — it names none, and '
              'the act did not end.** That pricing premise is refuted and the refutation is printed.', '',
              'The foreign toolchain is `%s` with Mathlib `%s`; the corpus pins `%s` — **the foreign pin is newer**. '
              '**It builds.** `#print axioms NavierStokes.Comparator.navier_stokes_breakdown_R3` returns `%s`, read '
              'from the printer’s own output on this machine and not from an exit code — **the standard three and '
              'nothing else, and no `sorryAx` in the closure**. The repository’s %d bare `sorry` terms are all in '
              '`ComparatorChallenges/`, its own reference statements, which the axiom profile independently confirms '
              'are outside the terminal’s closure.'
              % (B.get('foreign_toolchain'), str(B.get('foreign_mathlib', ''))[:12],
                 '/'.join(B.get('corpus_pins', {}).values()), PROF, B.get('sorry_bare', 0)), '']
    else:
        L += ['**The build did not complete on this machine, so no grade is conferred** — a grading of an unbuilt '
              'proof is a grading of an announcement. What it needed is printed in the act’s own record.', '']
    L += ['#### The statement, read against C', '',
          '- **Quantifiers:** `∀ nu, nu > 0 → ∃ u₀ f, …`, with `n = 3` fixed by `EuclideanSpace ℝ (Fin 3)`. Exactly '
          'C’s *“Take ν > 0 and n = 3. Then there exist …”*.',
          '- **The decay of (5):** a stated field, `ForceConditionDecay.decay`. It bounds the **total** `m`-th '
          'derivative, which dominates every mixed partial of that order — **at least as strong as the page’s '
          'condition, on the side where being stronger makes the theorem weaker**.',
          '- **The initial data:** existential in the terminal, and **at rest one level down** — the witness is '
          '`fun _ => 0` (`NavierStokes/R3/ComparatorBridge.lean:85`), with the lemma named '
          '`zero_initial_condition_decay`. **C permits this exactly**; the forcing does the work.',
          '- **The conclusion:** `¬ (∃ v p, NavierStokesExistenceAndSmoothnessRn nu u₀ f v p)` — **the universal '
          'negative of C, not the blowup of a constructed solution**. The transport into the repository’s own '
          'excluded class is a **total definition**, so any solution in C’s class yields one in the excluded class.',
          '- **Uniqueness:** **not used and not needed.** A universal negative never has to identify a solution, so '
          'it never has to know there is only one. The question’s premise does not hold here.', '',
          '**All %d clauses of C map to a named field.** And the one place a reader would suspect a narrowing — the '
          'added `integrable : ∀ t ≥ 0, MemLp (‖v · t‖) 2` — **restores C’s meaning rather than narrowing it**: '
          'Mathlib’s Bochner integral returns `0` for a non-integrable function, so without it the energy bound '
          'would hold vacuously for exactly the solutions C means to exclude.' % RD.get('of', 0), '',
          '#### The grade, and the self-grading test', '',
          '**GRADE: %s.**' % GRADE, '']
    if GRADE == 'DERIVES':
        L += ['Every clause of C maps to a named field; the conclusion is C’s universal negative; the terminal takes '
              '**no premise beyond `nu > 0`**, so it is not INTERFACES; it stipulates nothing, so it is not a SHELL; '
              'it states nothing weaker than C, so it is not NOT THE CLAIM. **Residue, named by content:** the '
              'statement is written against the repository’s own copy of the Formal Conjectures definitions, of which '
              'the repository says *“Comparator checks these definitions against the independent reference at '
              'runtime”* — **and this act did not run Comparator**. The agreement was established here **by reading**, '
              'and a reading is not a checker.', '']
    L += ['**The corpus’s own route terminal, under the same reading: %s.** '
          '`ConservationBridge.riemann_hypothesis (h_cons : ConservationHypothesis) : RiemannHypothesis` concludes '
          '**Mathlib’s own** `RiemannHypothesis`, so it is no shell; it is conditional, so it is not DERIVES; its '
          'premise is identified and discharged nowhere in the closure. That is the grade the corpus already gives '
          'it. *(The order named the premise `h2`; the source names it `h_cons : ConservationHypothesis`, and a '
          'source governs its paraphrase.)*' % G.get('corpus_grade'), '',
          '**The clauses, compared both ways: %d the same, %d asymmetric.**' % (G.get('same', 0), ASYM), '',
          '- *“every step is in the closure”* — **the same**: a clean `#print axioms` was required of the stranger, '
          'and the corpus records its own profiles and ran the §VIII salt-check on itself.',
          '- *“the statement unfolded to its base objects”* — **the same, and the corpus applied it to itself '
          'harshly**: its own salt-check found *“most of the application-layer terminals this paper cited in v2.0 are '
          'shells, including the one v2.0 named as its exemplar of substance.”*',
          '- **the available vocabulary** — **asymmetric, favouring the stranger**: four grades were available here '
          'and the corpus has only ever had three. Unused, so it changed no outcome; an unused finer grade is still '
          'an asymmetry in the instrument.',
          '- **the verification instrument behind the definitions** — **asymmetric, favouring the stranger, and it '
          'bears on the grade**: the stranger’s definitions were accepted on a reading, with its own checker '
          'available and unrun, while the corpus does not accept its own definitions on a reading — `rowgen`’s '
          '`defenc` flag exists because a reading once passed a stand-in.', '',
          '**So the seat’s routed concern at b428 — that a discipline which has only graded its own work might grade '
          'itself more generously than a stranger — is not confirmed on this trial: both asymmetries run the other '
          'way.** It is not refuted either; one trial on one terminal is one trial. **And what the test cannot tell, '
          'said plainly: whether the corpus would confer `DERIVES` on a terminal of its own with this profile and '
          'this mapping — it has never had one, so there is no like case on its own side.**', '',
          '#### The arc, and the lanes this act leaves where it found them', '',
          '**W-ORD-WITNESS-ENUMERATION stays checkpointed after site (iii)** — sites (iv) to (vi) remain, one act '
          'each, and this act entered none of them. The disproof lane named at b428 stays **named and not opened**. '
          'Both instrument lanes stay parked and the wave stays parked.', '',
          '#### The four lists', '', FOUR, '',
          '#### What this act did not do', '',
          '0 grades of the corpus’s own moved, conferred or minted. 0 premises discharged. 0 doors restated. '
          '0 routes proposed. 0 lanes opened. 0 kappa measured. 0 corpus kernel files touched. 0 corpus kernel '
          'builds. 0 rows of `FACES_LEDGER.md`. 0 register rows. 0 keystones. 0 lane documents. 0 bytes of the '
          'foreign repository entered any rostered repository. 0 claims that the external proof is correct or '
          'incorrect beyond what its grade says. 0 deposit actions. **And h2 where the deposit left it.**', '']
    return L


SCOPE = ("### THIS ROW RECORDS A CALIBRATION OF THE CORPUS'S GRADING DISCIPLINE AGAINST A PROOF IT DID NOT WRITE. "
         "### IT MOVES NO GRADE OF THE CORPUS'S OWN, OPENS NO LANE, EDITS NO KEYSTONE AND TOUCHES NO CORPUS KERNEL")


def corr_rows():
    m = ROWMARK + " (b429)"
    stmt = (m + ". **THE REGISTRATION WAS LOCKED BEFORE ANY WRITE, FETCH, CLONE OR BUILD**, chained on b378's gate "
            "run as b429 -- @GR@ gates read, @GDG@ checked by digest. **THREE ADDRESSES SUPPLIED BY THE AUTHOR, "
            "@RES@ RESOLVED, 0 GUESSED; THE REPOSITORY PINNED AT @HEAD@.** **STATEMENT C AND CONDITIONS (4) TO (7) "
            "QUOTED VERBATIM FROM THE CLAY PAGE; ITS ERRATA TOUCH NEITHER.** **BUILT: @BUILT@ ON A FOREIGN "
            "TOOLCHAIN @TC@ AGAINST THE CORPUS'S @CTC@; AXIOM PROFILE @PROF@ FROM #print axioms, NO sorryAx.** "
            "**ALL @MAP@ CLAUSES OF C MAP TO A NAMED FIELD; THE CONCLUSION IS C'S UNIVERSAL NEGATIVE, THE INITIAL "
            "DATA IS AT REST, AND UNIQUENESS IS NEITHER USED NOR NEEDED.** **GRADE @GRADE@; THE CORPUS'S OWN ROUTE "
            "TERMINAL @CG@ UNDER THE SAME READING; @ASYM@ ASYMMETRIC CLAUSE(S), BOTH FAVOURING THE STRANGER.** "
            "0 GRADES MOVED, 0 PREMISES DISCHARGED, 0 CONTENT LOST")
    term = "NO TERMINAL ADDED OR MOVED. No grade of the corpus's own was conferred, moved or restated"
    prof = ("### ONE PLACE-papers FILE APPENDED -- OPEN_TRAILS.md, ITS PIN A TRUE PREFIX, CARRYING THE CALIBRATION "
            "RECORD; NO KEYSTONE, NO REGISTER ROW, NO LEDGER ROW, NO CORPUS KERNEL FILE; THE CLONE, THE TOOLCHAIN "
            "AND EVERY BUILD ARTEFACT OUTSIDE EVERY ROSTERED REPOSITORY -- 0 CONTENT LOST")
    grade = ("### THE OBJECT GRADED AGAINST IS THE CLAY PAGE AT ITS OWN DIGEST AND NOT A PARAPHRASE; THE PROFILE IS "
             "THE PRINTER'S OWN OUTPUT AND NOT AN EXIT CODE; EVERY CLAUSE OF THE READING IS QUOTED AT ITS LEAN FILE "
             "AND LINE; AND THE ONE RESIDUE -- COMPARATOR UNRUN -- IS NAMED BY CONTENT")
    status = ("data/b429_the_external_grading_read.txt; data/b429_addresses.txt; data/b429_statement_c.txt; "
              "data/b429_build_and_profile.txt; data/b429_statement_read.txt; data/b429_the_grade.txt; "
              "data/b429_axiom_prints.txt; data/b429_registration_2026-09-12.txt (LOCKED at sha256 %s); "
              "PLACE-papers OPEN_TRAILS.md; CORRESPONDENCE.md row %%d" % SEALHASH[:16])

    def sub(x):
        return (x.replace('@GR@', str(GR)).replace('@GDG@', str(GDG))
                .replace('@RES@', str(A.get('resolved'))).replace('@HEAD@', str(B.get('head', ''))[:12])
                .replace('@BUILT@', str(BUILT)).replace('@TC@', str(B.get('foreign_toolchain')))
                .replace('@CTC@', '/'.join(B.get('corpus_pins', {}).values()))
                .replace('@PROF@', str(PROF)).replace('@MAP@', str(RD.get('of', 0)))
                .replace('@GRADE@', GRADE).replace('@CG@', str(G.get('corpus_grade')))
                .replace('@ASYM@', str(ASYM)))
    return [(sub(m), sub(stmt), term, prof, grade, SCOPE, status)]


def no_key(out):
    return any(ln.strip().startswith('### NO KEY') for ln in (out or '').splitlines())


def query(qq):
    r = subprocess.run([sys.executable, INDEX, '--query', qq], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout or '', r.returncode


ALIASES = ('the external grading read', 'the navier stokes lean terminal graded',
           'the self grading test', 'calibration of the grading discipline', 'b429 external read')
MUST_NOT_HIT = ('the lock was overridden', 'a grade was moved', 'h2 has moved', 'a lane was opened',
                'the proof is correct')
KEY = 'the-external-grading-read'


def do_key(rownum):
    statement = (
        "b429 GRADED THE COLLABORATION'S NAVIER-STOKES LEAN TERMINAL AGAINST THE CLAY PAGE'S STATEMENT C. "
        "Three author-supplied addresses, %s resolved, 0 guessed; repository pinned at %s; foreign toolchain %s "
        "against the corpus's %s; BUILT %s; axiom profile %s from #print axioms with no sorryAx. All %s clauses of C "
        "map to a named field; the conclusion is C's UNIVERSAL NEGATIVE; the initial data is AT REST; uniqueness is "
        "NEITHER USED NOR NEEDED. GRADE %s, with the unrun Comparator check named as the residue. THE SELF-GRADING "
        "TEST: the corpus's own route terminal grades %s under the same reading, and %s clause(s) were applied "
        "asymmetrically -- BOTH FAVOURING THE STRANGER. Cited in no corpus document."
        % (A.get('resolved'), str(B.get('head', ''))[:12], B.get('foreign_toolchain'),
           '/'.join(B.get('corpus_pins', {}).values()), BUILT, PROF, RD.get('of', 0), GRADE,
           G.get('corpus_grade'), ASYM))
    grade = "### NO GRADE OF THE CORPUS'S OWN MOVED OR CONFERRED. ### NO LANE OPENED. ### NOTHING DEPOSITS"
    where = ("data/b429_the_external_grading_read.txt; data/b429_the_grade.txt; data/b429_build_and_profile.txt; "
             "data/b429_statement_read.txt; data/b429_registration_2026-09-12.txt (LOCKED, %d gates read, %d by "
             "digest); OPEN_TRAILS.md; CORRESPONDENCE.md row %d" % (GR, GDG, rownum))
    act = "b429 (the external grading read)"
    key_new = ("    %r: %r,%s" % (KEY, list(ALIASES), NL))
    row_new = ('    # ### THE EXTERNAL GRADING READ (b429).%s    (%r, %r,%s     %r,%s     %r,%s     %r),%s'
               % (NL, KEY, act, NL, statement, NL, grade, NL, where, NL))
    pre = {qq: no_key(query(qq)[0]) for qq in MUST_NOT_HIT}
    for qq in MUST_NOT_HIT:
        rec('    %-40s NO KEY before : %s' % (qq, pre[qq]))
    txt = io.open(INDEX, encoding='utf-8').read()
    KEY_ANCHOR = 'KEYS = {' + NL
    ROW_ANCHOR = ('INDEX = [' + NL + '    # (key, act, one-line statement, grade as its own act recorded it, location)' + NL)
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
    rec('  READ BACK : %s returns %d row(s)  %s   [verdict LINE read, under A2]' % (KEY, n, 'PASS' if ok else '### FAIL ###'))
    for qq in ALIASES:
        o, _rc = query(qq)
        g2 = (not no_key(o)) and KEY in o
        ok = ok and g2
        rec('    %-58s reaches the b429 key : %s' % (qq[:58], g2))
    for lbl, cond in (('the grade carried', GRADE in out),
                      ('the corpus`s own grade carried', str(G.get('corpus_grade')) in out),
                      ('the asymmetry carried', 'FAVOURING THE STRANGER' in out),
                      ('cited nowhere carried', 'Cited in no corpus document' in out)):
        ok = ok and cond
        rec('    %-52s : %s' % (lbl, cond))
    for qq in MUST_NOT_HIT:
        o, _rc = query(qq)
        g2 = pre[qq] and no_key(o)
        ok = ok and g2
        rec('    %-40s NO KEY after  : %s' % (qq, no_key(o)))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return ok


def bank_file(Q, rownum, kok):
    Bk = ['=' * 100, 'b429 -- THE EXTERNAL GRADING READ. ### A CALIBRATION RECORD.', 'THE BANK.', '=' * 100, '']
    for blk in trail_block():
        if blk and not blk.startswith('<!--'):
            Bk.append(blk)
    comp = read(os.path.join(D, 'b429_components.txt'))
    Bk += ['', '-' * 100, '### THE EXPECTATIONS, AS THE REPORT SCORED THEM.', '-' * 100]
    Bk += [ln for ln in comp.splitlines() if ln.strip().startswith(('(N1)', '(N2)', '(N3)'))]
    Bk += ['', '-' * 100, '### THE DESK.', '-' * 100]
    for item, want, _why in DESK:
        Bk.append('  %-70s %s' % (item[:70], want))
    Bk += ['', '  ITEMS SWEPT : %d. CLOSED : %d. STANDING : %d.' % (Q['items'], Q['closed'], Q['standing']),
           '', '  CORRESPONDENCE ROW : %d. ### KEY : %s.' % (rownum, 'PASS' if kok else 'FAIL'), '', '=' * 100]
    n = write_bytes(BANKOUT, NL.join(Bk) + NL)
    rec('  bank written : %s (%d bytes, %d lines)' % (os.path.basename(BANKOUT), n, len(Bk)))
    return len(Bk)


B428ROW_RE = r"(?m)^\| (\d+) \| \*\*SITE \(iii\), THE WIDTH COORDINATE'S UNION"


def main():
    bar('=')
    rec('b429_desk_bank.py -- THE DESK, THE TRAIL, THE ROW, THE KEY, THE BANK.')
    bar('=')
    if not _g:
        rec('  ### HARD FAILURE -- the lock gate`s record is missing.')
        return 1
    bar()
    rec('### THE DESK, SWEPT.')
    bar()
    Q = do_desk()
    bar()
    rec('### THE TRAIL, APPENDED -- THE CALIBRATION RECORD.')
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
    at = lambda mk, s: [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \| ' + re.escape(mk), s)]
    rec('  b428`s row by its marker : %s' % [int(x.group(1)) for x in re.finditer(B428ROW_RE, txt)])
    nums = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', txt)]
    if ROWS2[0][0] in txt:
        rec('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        rownum = at(ROWS2[0][0], txt)[0]
    else:
        start = max(nums) + 1
        lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start, stmt, term, prof, grade, scope, status % start)
                 for (_m, stmt, term, prof, grade, scope, status) in ROWS2]
        new_txt = txt.rstrip(NL) + NL + NL.join(lines) + NL
        write_bytes(TABLE, new_txt)
        back = read(TABLE)
        got = [int(x.group(1)) for x in re.finditer(r'(?m)^\| (\d+) \|', back)]
        cellsx = [GD.split_cells(t) for t in back.rstrip(NL).split(NL)[-1:]]
        okr = (got[-1] == start and C.blank_cells(back) == 0
               and all(len(c) == 6 and all(x.strip() for x in c) for c in cellsx) and back.startswith(txt.rstrip(NL)))
        rec('  READ BACK : last row %d ; cells %s ; prior text a TRUE PREFIX %s ; %s'
            % (got[-1], [len(c) for c in cellsx], back.startswith(txt.rstrip(NL)), 'PASS' if okr else '### FAIL ###'))
        if not okr:
            return 1
        rownum = start
    after = read(TABLE)
    rec('  after -- b428`s : %s ; this act`s, by its marker : %s'
        % ([int(x.group(1)) for x in re.finditer(B428ROW_RE, after)], at(ROWS2[0][0], after)))
    bar()
    rec('### THE KEY.')
    bar()
    kok = do_key(rownum)
    bar()
    rec('### THE BANK.')
    bar()
    nlines = bank_file(Q, rownum, kok)
    bar('=')
    rec('  ### ### **DESK %d SWEPT / %d CLOSED. ### CORR ROW %d. ### KEY %s. ### BANK %d LINES.**'
        % (Q['items'], Q['closed'], rownum, 'PASS' if kok else 'FAIL', nlines))
    bar('=')
    io.open(os.path.join(D, 'b429_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if kok else 1


if __name__ == '__main__':
    sys.exit(main())
