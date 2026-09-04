# -*- coding: utf-8 -*-
"""b322_checks.py -- THE GATE SUITE FOR A LADDER, AN UNFOLDING, AND A PRICED QUESTION.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NOADOPT`** ### -- ### **THE ONE THE ACT'S OWN NAME MOST TEMPTS IT TO BREACH.** ###
###     THE MEMBERSHIP is the act that would like to come out of itself holding a unit. ### The
###     order forbids it in terms and the registration caps it at zero.
###   ### ### **`G-NOTSETTLED`** ### -- the residual falls and its exponent matches a prediction, and
###     ### **THAT IS NOT THE MEMBERSHIP SETTLED.** ### The arms disagree; the noise gate refuses
###     every step. ### This arm requires the bank, the run AND the index row to say so.
###   ### ### **`G-DEFECTS`** ### -- ### **THE ARM THIS RECORD NEEDS MOST AND HAS THE LEAST PRACTICE
###     ### AT.** ### Two of this act's own sealed bars turned out defective. ### A record whose
###     registrations are only ever reported as having worked is a record that has stopped reading
###     them. ### Both defects must be in the bank AND in the correspondence row, and the
###     registration must be UNEDITED.
###   ### **`G-NOLIMIT`** ### -- a falling course at five frames is a falling course at five frames.
###   ### **`G-ORDER`** ### -- the reading was taken from the ladder BEFORE any definition was
###     unfolded. ### Component 1 precedes Component 2 in the run file, and the bank says why.
###   ### **`G-REPRO`** ### -- the ladder reproduces b319's banked residuals on BOTH cuts before it
###     extends them. ### **A LADDER THAT COULD NOT REPRODUCE THE ROW IT EXTENDS WOULD BE A
###     ### DIFFERENT MEASUREMENT WEARING ITS NAME.**
###   ### **`G-EMITTER`** ### -- b283's law. ### CM Lemma 3.1 is pulled from `b202`, the file that
###     read it, and NOT from `b300`, which quotes it.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402  ### the stripper and git helper, IMPORTED not copied

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

OWNERS = ['tools/e16/carto_atlas.py', 'tools/e16/qeps_layer.py', 'tools/e16/b205_prolate.py',
          'tools/e16/prolate_layer.py', 'tools/e16/b313f_qeps_layer.py',
          'tools/e16/b313r_qeps_layer.py', 'tools/b316_instrument.py', 'tools/b317_smear.py',
          'tools/b318_square.py', 'tools/b319_stable.py', 'tools/b320_weil.py',
          'tools/b321_window.py', 'tools/noise_floor.py', 'tools/b305_source.py',
          'tools/b317_extract.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b322_the_membership.txt')
REG = d('b322_registration_2026-09-04.txt')
RUN = d('b322_components_run.txt')
SCAN = d('b322_ferry_scan.txt')
FERRY = d('b322_ferry_2026-09-04.txt')
CENSUS = d('b322_census.txt')
EXTRACT = d('b322_extract_notes.txt')

OWNED = [RUN, CENSUS, EXTRACT, d('b322_index_query.txt'), d('b322_index_run.txt'),
         d('b322_pins_stepzero.txt'), d('b322_regspec_run.txt'), d('b322_reg_termscan.txt'),
         d('b322_satisfiable.json'), d('b322_satisfiable_run.txt'), d('b322_rows.json'),
         t('b322_regspec.py'), t('b322_correspondence.py'), t('b322_run.py'),
         t('b322_ladder.py'), t('b322_extract.py')]

CARRIERS = [
    (t('b322_checks.py'), 'its own fixtures'),
    (t('b322_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    # ### **THE LIGATURE TRAP, MET AGAIN AND AVOIDED.** ### The PDF sets `fi` as U+FB01, so
    # ### `'Definition 4.4'` does not match the extract's own bytes. ### b317 lost four fragments to
    # ### exactly this; the anchor is chosen to start after the ligature.
    ("Definition 4.4 -- the space and its two conditions", EXTRACT, 'nition 4.4 For'),
    ("(16) -- the inner product and its normalization", EXTRACT, 'as follows'),
    ("(24) -- the transform on even functions", EXTRACT, 'nes the unitary in L2'),
    ("### CM Lemma 3.1, AT b202 -- the file that READ it, not b300 which quotes it",
     EXTRACT, 'zero on [-1,1]'),
    ("### and the closing line of its proof", EXTRACT, 'F_eR phi_mu = xi_mu'),
    ("b211's (C3) -- the eigenrelation condition two rests on", EXTRACT, 'F phi_mu = c phi_mu'),
    ("### b203's fence -- the derivation would be circular without it", EXTRACT, 'IS NOT'),
    ("b300's verdict (b) and its grade", EXTRACT, 'DERIVES-on-IMPORTS'),
    ("b319's residual table, both cuts", EXTRACT, 'residual stable'),
    ("b321's instrument ladder, the rate this act compares against", EXTRACT,
     'THE IDENTITY CONTROL HOLDS'),
    ("the instrument realization -- sonin_unit, whole", EXTRACT, 'def sonin_unit'),
    ("### and condition one IMPOSED by array construction", EXTRACT, 'out = np.zeros(fr.N)'),
    ("the edge diagnostic, with b316's own meaning attached", EXTRACT, 'def taper'),
    ("the two conditions as index sets", EXTRACT, 'def masks'),
    ("the space as the stable-rank scheme selects it", EXTRACT, 'def stable_subspace'),
    ("the unit, at its emitting file", t('b316_instrument.py'), 'def sonin_unit'),
    ("the cut, at its emitting file", t('b319_stable.py'), 'def stable_subspace'),
    ("b300 -- the derivation under test", d('b300_the_archimedean_leg.txt'), 'VERDICT (b)'),
    ("b319 -- the course this act fits", d('b319_the_stable_rank.txt'), 'residual stable'),
    ("b321 -- the incident that bought the rule", d('b321_the_window_opened.txt'),
     'AN INSTRUMENT CANNOT DISCRIMINATE'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('bank gives the ladder verdict', BANK, 'THE RESIDUAL FALLS, AT EVERY STEP OF THE DOMAIN'),
    ('### and the reading that follows from it', BANK, 'THE RESIDUAL IS THE TRUNCATION'),
    ('### bank reports the refuted rate half', BANK, 'RATE HALF IS REFUTED'),
    ('### and the band it fell outside', BANK, 'NOT COMPARABLE'),
    ('bank reports the second route agreeing', BANK, 'THE SECOND ROUTE AGREES WITH THE FIRST'),
    ('### and prints all three exponents', BANK, 'ALL THREE NUMBERS ARE PRINTED RATHER THAN'),
    ('### bank states the arms disagree', BANK, 'THE ARMS DISAGREE, AND THAT IS THE'),
    ('bank gives the verdict and its price', BANK, 'UNDER-RESOLVED`, AND IT CARRIES ITS PRICE'),
    ('### bank states no unit is adopted', BANK, 'NO UNIT IS ADOPTED AND NONE IS REPLACED'),
    ('### bank gives the defects their own section', BANK, 'TWO DEFECTS IN THIS ACT'),
    ('### and names the first', BANK, 'IS NOT A PARTITION, AND THE ACT IMPORTED IT WITHOUT'),
    ('### with the reason it is not a partition', BANK, 'IT DOES NOT RESTORE THE MASS BEYOND'),
    ('### and names the second', BANK, 'BRANCHES ARE NOT MUTUALLY EXCLUSIVE'),
    ('### and says which branch the act took', BANK, 'THE ACT TAKES THE WEAKER OF THE TWO'),
    ('### and that the registration is unedited', BANK, 'NEITHER IS EDITED'),
    ('bank refuses the limit claim', BANK, 'IT DOES NOT SAY THE RESIDUAL REACHES ZERO'),
    ('### bank reports the noise gate refusing', BANK, 'REFUSES 4 OF 4'),
    ('bank carries the open L2 order', BANK, 'W-ORD-PHI-MU-L2'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER ITS CAP'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank states the rule the lore gains', BANK, 'THE RESOLVING-POWER RULE'),
    ('### and what the rule is for', BANK, 'AN OPEN QUESTION INVITES ANOTHER OPINION'),
    ('bank states the reproduction law', BANK, 'A LADDER THAT COULD NOT REPRODUCE'),
    ('### and that FLAT was reachable', BANK, 'FLAT` WAS REACHABLE'),
    ('### bank says the two differing rows are not independent', BANK,
     'THE TWO ARE NOT INDEPENDENT'),
    ('bank names the emitter law it followed', BANK, 'b283'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### and names the fold with its count', BANK,
     'THE FOLD, FROM b314 ONWARD -- EIGHT ACTS -- IS NAMED NEXT'),
    ('### and the keystone after it', BANK, 'THE KEYSTONE IS RE-READ AFTER THE FOLD'),
    ('registration names the act', REG, 'THE MEMBERSHIP'),
    ('the run reports zero checks failing', RUN, '### CHECKS FAILING : 0'),
    ('the run gives the direction', RUN, '(B1a) DIRECTION : FALLS'),
    ('the run gives the rate band', RUN, '(B1b) BAND'),
    ('the run gives the taper verdict', RUN, '(B2) : THE VECTOR'),
    ('the run names the first differing constituent', RUN, 'FIRST DIFFERING CONSTITUENT'),
    ('### the run prints the branch its own chain reached', RUN, 'BRANCH REACHED'),
    ('the run reports the noise gate refusing', RUN, 'REFUSED -- 4 of 4'),
    ('the run computes the price', RUN, 'THE PRICE, COMPUTED AS b321 PRICED THE EXPONENT'),
    ('the extract reports nothing missing at the source', EXTRACT,
     'SOURCE FRAGMENTS NOT FOUND : 0'),
    ('### and nothing missing at the owners', EXTRACT, 'CORPUS FRAGMENTS NOT PRESENT : 0'),
]

MUST_FAIL = [
    # ### **`G-NOADOPT` -- the sentences THE MEMBERSHIP would be tempted to write.**
    ('no unit is adopted', BANK, 'THE UNIT IS ADOPTED.'),
    ('no unit is replaced', BANK, 'THE UNIT IS REPLACED.'),
    ('membership is not decided', BANK, 'THE MEMBERSHIP IS DECIDED.'),
    ('the unit is not placed in the space', BANK, 'THE UNIT IS IN THE SPACE.'),
    ('the derivation is not called confirmed', BANK, 'THE DERIVATION IS CONFIRMED.'),
    # ### **`G-NOLIMIT`.**
    ('the residual is not called zero', BANK, 'THE RESIDUAL IS ZERO.'),
    ('the residual is not called converged', BANK, 'THE RESIDUAL HAS CONVERGED.'),
    ('the limit is not claimed', BANK, 'THE RESIDUAL REACHES ZERO.'),
    ('the price is not read as a prediction', BANK, 'THE RESIDUAL WILL REACH 0.01.'),
    # ### **`G-DEFECTS` -- and the sentences that would have hidden them.**
    ('the bars are not called sound', BANK, 'THE BARS HELD.'),
    ('the registration is not re-sealed', BANK, 'THE REGISTRATION IS RE-SEALED.'),
    ('the branch is not called unambiguous', BANK, 'THE BRANCH WAS UNAMBIGUOUS.'),
    # ### **THE STANDING CAPS.**
    ('b300 is not re-verdicted', BANK, 'b300 IS RE-VERDICTED.'),
    ('b319 is not re-verdicted', BANK, 'b319 IS RE-VERDICTED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the L2 question is not closed', BANK, 'W-ORD-PHI-MU-L2 IS DISCHARGED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('nothing about the identity', BANK, "THE IDENTITY'S TRUTH IS DECIDED."),
    ('nothing about the roster', BANK, 'THE ROSTER IS COMPLETE.'),
]

TOOLNUM = [
    ("the residual, the ladder and the two fits", 'tools/b322_ladder.py'),
    ("the three components", 'tools/b322_run.py'),
    ("the source, owner and code fragments", 'tools/b322_extract.py'),
    ("### the finder those fragments were located with", 'tools/b317_extract.py'),
    ("the unit, the frame, the taper and the decay bound", 'tools/b316_instrument.py'),
    ("the cut both residuals are taken against", 'tools/b319_stable.py'),
    ("the domain and grid ladders", 'tools/b317_smear.py'),
    ("the radial solver the unit bottoms out in", 'tools/e16/b205_prolate.py'),
    ("the floor/drift verdicts", 'tools/noise_floor.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b322_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b322_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b322_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b322_index_append.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b322' in x)

# ### **THE DECLARED LITERALS IN THE DECIDING RUNNER, AND WHERE EACH COMES FROM.**
# ### `0.5` and `2.0` are (B1b)'s band; `0.1` and `0.5` (B2)'s two thresholds; `-0.5` (B3)'s
# ### predicted exponent and `0.2` its agreement bar; `0.01` the figure (B5) prices to; `1.0` a
# ### comparison point and `1e-300` a divide guard. ### **EVERY ONE IS A SEALED BAR OR A GUARD.**
# ### ### **AND THE FIVE THAT ARE NOT THIS ACT'S AT ALL:** ### `0.896557, 0.306328, 0.112555,
# ### 0.047182, 0.023224` are ### **b321's INSTRUMENT-RESIDUAL LADDER AT `a = 1.3`**, quoted from
# ### that act's own bank so that `q` can be fitted by the same fitter on the same domains. ### They
# ### are an owner's banked numbers carried verbatim; ### **CHANGING ONE WOULD BE FALSIFYING b321's
# ### ### MEASUREMENT, WHICH IS WHY THEY ARE DECLARED HERE RATHER THAN HIDDEN IN A HELPER.**
FLOAT_OK = {'0.5', '2.0', '0.1', '-0.5', '0.2', '0.01', '1.0', '1e-300', '0.0',
            '0.896557', '0.306328', '0.112555', '0.047182', '0.023224'}

# ### **THE SEALED HASH, WRITTEN HERE BEFORE THE LADDER WAS RUN.**
SEAL = '332a3a836352719346ea84bc69661c0906360c35a58053dc88a9046f67f55fc4'


def main():
    fails = []
    print('=' * 100)
    print('b322 -- GATE SUITE (A LADDER, AN UNFOLDING, AND A PRICED QUESTION)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (each pulled from the file that EMITTED the sentence -- b283):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    run = io.open(RUN, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    src = io.open(t('b322_run.py'), encoding='utf-8').read()
    lad = io.open(t('b322_ladder.py'), encoding='utf-8').read()
    code = K7.strip_text(src) + K7.strip_text(lad)

    print('\n  G-NOADOPT (no unit is adopted or replaced -- the cap this act is named for):')
    na = ('NO UNIT IS ADOPTED AND NONE IS REPLACED' in bank
          and 'NO UNIT IS ADOPTED AND NONE IS REPLACED' in run
          and 'NO UNIT IS ADOPTED' in tbl)
    print('    the bank, the run and the correspondence row all say so : %s' % na)
    if not na:
        fails.append('G-NOADOPT')

    print('\n  G-NOTSETTLED (a falling course is not the membership settled):')
    ns = ('THE ARMS DISAGREE, AND THAT IS THE' in bank
          and 'UNDER-RESOLVED' in run
          and 'DID NOT SETTLE THE MEMBERSHIP' in idx
          and 'W-ORD-ARCH-MEMBERSHIP` IS NOT CLOSED' in bank)
    print('    the bank, the run and the INDEX ROW all carry it : %s' % ns)
    print('    ### **THE INDEX ROW IS WHERE A LATER READER ARRIVES FIRST**, and a row that answered')
    print('    ### *is the unit in the space* with a falling course and stopped would be a true')
    print('    ### sentence assembled to give a false impression.')
    if not ns:
        fails.append('G-NOTSETTLED')

    print('\n  G-DEFECTS (two of this act\'s own sealed bars, declared and NOT edited):')
    r = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (r.stdout or '')
    same = SEAL in reg
    d1 = 'IS NOT A PARTITION' in bank and 'IT DOES NOT RESTORE THE MASS BEYOND' in bank
    d2 = 'BRANCHES ARE NOT MUTUALLY EXCLUSIVE' in bank and 'THE ACT TAKES THE WEAKER OF THE TWO' in bank
    inrow = 'IS NOT A PARTITION' in tbl and 'NOT MUTUALLY EXCLUSIVE' in tbl
    print('    the seal verifies : %s ; hash is the one written BEFORE the ladder : %s'
          % (intact, same))
    print('    defect 1 stated with its reason : %s ; defect 2 with the branch taken : %s' % (d1, d2))
    print('    ### and both are in the correspondence row, not only the bank : %s' % inrow)
    print('    ### **A RECORD WHOSE REGISTRATIONS ARE ONLY EVER REPORTED AS HAVING WORKED IS A')
    print('    ### ### RECORD THAT HAS STOPPED READING THEM.**')
    if not (intact and same and d1 and d2 and inrow):
        fails.append('G-DEFECTS')

    print('\n  G-NOLIMIT (a falling course at five frames is a falling course at five frames):')
    nl = ('IT DOES NOT SAY THE RESIDUAL REACHES ZERO' in bank
          and 'REFUSES 4 OF 4' in bank
          and 'A PRICE IS NOT A PREDICTION' in bank)
    print('    the bank refuses the limit, reports the refusal, and labels the price : %s' % nl)
    if not nl:
        fails.append('G-NOLIMIT')

    print('\n  G-ORDER (the reading was taken BEFORE any definition was unfolded):')
    i1 = run.find('COMPONENT 1 -- THE LADDER')
    i2 = run.find('COMPONENT 2 -- THE TWO REALIZATIONS')
    i3 = run.find('(B1a) DIRECTION :')
    ordered = 0 <= i1 < i3 < i2
    said = 'BEFORE ANY DEFINITION IS' in run and 'WOULD HAVE KNOWN WHICH ANSWER IT WANTED' in bank
    print('    the direction is printed before Component 2 begins : %s' % ordered)
    print('    ### and the bank says why that ordering mattered : %s' % said)
    if not (ordered and said):
        fails.append('G-ORDER')

    print('\n  G-REPRO (the ladder reproduces b319 on BOTH cuts before it extends it):')
    rp = ('reproduced' in run and '0.7973' in run and '0.9963' in run
          and 'the arm can miss' in run)
    print('    fixture (i) reproduces and fixture (ii) shows the arm can miss : %s' % rp)
    if not rp:
        fails.append('G-REPRO')

    print('\n  G-EMITTER (b283\'s law: pulled from the file that emitted the sentence):')
    em = ("b202_sum_test.txt" in io.open(EXTRACT, encoding='utf-8').read()
          and 'NOT FROM b300' in io.open(t('b322_extract.py'), encoding='utf-8').read())
    print('    CM Lemma 3.1 comes from b202, and the extract says why not from b300 : %s' % em)
    if not em:
        fails.append('G-EMITTER')

    print('\n  G-ARMS (every arm shown ABLE to fire, or reported unable):')
    arms = [('the residual, able to miss against the wrong cut', 'the arm can miss' in run),
            ('the fitter, recovering a planted -0.5', 'planted exponent -0.5 recovered' in run),
            ('### and a different planted -1.25', 'planted exponent -1.25 recovered' in run),
            ('### and FLAT reachable on a flat course', 'FLAT is reachable' in run),
            ('the taper, actually moving the vector', 'the taper moves the vector' in run),
            ('the noise-floor gate -- REPORTED REFUSING', 'REFUSED -- 4 of 4' in run)]
    for lbl, ok_ in arms:
        print('    %-56s %s' % (lbl, 'PASS' if ok_ else '### FAIL ###'))
    if not all(x for _l, x in arms):
        fails.append('G-ARMS')

    print('\n  G-NOFLOAT (no undeclared float literal in the deciding runner):')
    rcode = K7.strip_text(src)
    lits = set()
    for m in re.finditer(r'(?<![\w.])(\d+\.\d*(?:[eE][-+]?\d+)?|\d+[eE][-+]?\d+)(?![\w.])', rcode):
        lits.add(m.group(1))
    extra = sorted(x for x in lits if x not in FLOAT_OK)
    print('    float literals in b322_run.py : %d ; UNDECLARED : %d %s'
          % (len(lits), len(extra), extra if extra else ''))
    if extra:
        fails.append('G-NOFLOAT')

    print('\n  G-NOEDIT (the owner instruments byte-identical to git HEAD, checked AFTER the run):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS,
                           capture_output=True, text=True).stdout.strip()
    print('    git status over those paths : %r' % dirty)
    print('    ### **b316 IS IN THIS LIST AND IT IS THE ACT\'S CENTRAL IMPORT.** ### The unit, the')
    print('    ### taper and the decay bound are all b316\'s, and an act that edited them while')
    print('    ### measuring with them would be measuring itself.')
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-NOPAPERS / G-ANCESTOR:')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'],
                        capture_output=True, text=True).stdout
    tracked = [x for x in pp.splitlines() if x.strip() and not x.startswith('??')]
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'],
                          capture_output=True).stdout.decode('utf-8', 'replace')
    pfx = tbl.startswith(head.rstrip('\n'))
    print('    PLACE-papers tracked changes : %d ; table is a TRUE PREFIX : %s'
          % (len(tracked), pfx))
    if tracked:
        fails.append('G-NOPAPERS')
    if not pfx:
        fails.append('G-ANCESTOR')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s'
              % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an '
                              'achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0],
                                     [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s'
          % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-SHARED (the stem sweep at extended scope):')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s ; UNEXPECTED : %d  %s'
          % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-36s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s'
          % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the run', RUN)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d'
              % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d' % unpullable)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
