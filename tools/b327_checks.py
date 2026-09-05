# -*- coding: utf-8 -*-
"""b327_checks.py -- THE GATE SUITE FOR A LEDGER THAT CERTIFIES NOTHING AND A BRIDGE THAT STAYS OWED.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NOEQUIV`** ### -- ### **THE ONE THIS ACT WOULD MOST EASILY HAVE BREACHED.** ### A
###     ledger of every face side by side reads as a map of a route, and a bridge read reads as a bridge
###     closed. ### Bank, ledger head, index and rows must all refuse the carrier reading BY NAME, and no
###     cascade line may carry a kind other than STATED / OWED / NONE.
###   ### ### **`G-QUOTE`** ### -- every quotation the ledger's rows and pairs carry is IN the file it
###     names, re-verified here by the writer's own function; and ### **`G-EXTRACT`** -- every such
###     fragment is in the extract file, so the suite's needles come from the extract step.
###   ### ### **`G-ORDER`** ### -- the registration was sealed before any instrument of this act ran.
###   ### **`G-BRIDGE`** ### -- the corroboration holds, its SAME arm fires, and the verdict words are the
###     same in the JSON, the bank, the live row, the correspondence row and the index.
###   ### **`G-LEDGER`** ### -- thirteen rows, seven cells each, no blank, 78 pair lines, no pair absent,
###     the class line under the standing taxonomy's regex, the candidate section present once.
###   ### **`G-NOTES`** ### -- the count matched the order; the contacts carry no promotion criterion.
###   ### **`G-COMPUTE`** ### -- the cap of two computations, re-measured off the tools' imports.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import document_classes as DC  # noqa: E402
import b327_faces_rows as R    # noqa: E402
import b327_faces_row as W     # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
MONO = os.path.join(DEPOSIT, 'A_Place_to_Stand.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
BALANCE = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')

OWNERS_RELAY = ['tools/b307_handoff_census.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py',
                'tools/b305_source.py', 'tools/ferry_scan.py', 'tools/lore_rules.py', 'tools/mirror_roster.json',
                'tools/reg_seal.py', 'tools/reg_satisfiable.py', 'tools/b300_regspec.py', 'HANDOFF.md',
                'data/STRUCK_CLAUSES.md', 'data/read_pentagon.txt']
OWNERS_PP = ['internal/bench/li_bench.py', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md',
             'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'day1/A_Place_to_Stand.md']
PP_WRITTEN = ['EMERGING_RESEARCH_PROGRAMMES.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'FACES_LEDGER.md']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b327_the_faces_ledger.txt')
REG = d('b327_registration_2026-09-05.txt')
EXTRACT = d('b327_extract_notes.txt')
SRC = d('b327_source.txt')
BRUN = d('b327_bridge_run.txt')
NRUN = d('b327_notes_run.txt')
FIL = d('b327_filings_run.txt')
CORR = d('b327_corr_run.txt')
IDX = d('b327_index_run.txt')
CEN = d('b327_faces_census.txt')
SCAN = d('b327_ferry_scan.txt')
SCAN2 = d('b327_ferry_resume_scan.txt')
CENSUS = d('b327_census.txt')
REGSPEC = d('b327_regspec_run.txt')
SATIS = d('b327_satisfiable_run.txt')
LRUN = d('b327_ledger_run.txt')
LRUN2 = d('b327_ledger_run2.txt')
LIVE = d('b327_live_run.txt')
CASC = d('b327_cascades_run.txt')
CAND = d('b327_candidates_run.txt')

OWNED = [BANK, REG, EXTRACT, BRUN, NRUN, FIL, CORR, IDX, CEN, CENSUS, REGSPEC, SATIS, LRUN, LRUN2, LIVE, CASC, CAND,
         d('b327_satisfiable.json'), d('b327_bridge.json'), d('b327_notes.json'), d('b327_pins_stepzero.txt'),
         d('b327_reg_termscan.txt'), d('b327_reg_gate.txt'), d('audit_b327_index_query.txt'),
         t('b327_source.py'), t('b327_extract.py'), t('b327_regspec.py'), t('b327_faces_rows.py'), t('b327_faces_row.py'),
         t('b327_bridge.py'), t('b327_bridge_pairs.py'), t('b327_notes.py'), t('b327_filings.py'),
         t('b327_faces_census.py'), t('b327_correspondence.py'), t('b327_index_append.py'), LEDGER]

CARRIERS = [
    (t('b327_checks.py'), 'its own fixtures'),
    (d('b327_ferry_2026-09-05.txt'), "IT IS THE ORDER -- not this act's writing"),
    (d('b327_ferry_resume_2026-09-05.txt'), 'IT IS THE RESUME ORDER'),
    (SCAN, "the scan's own log"),
    (SCAN2, "the resume scan's own log"),
    (SRC, 'it names the pinned artefact and its fragments'),
    (d('b327_source_text.txt'), "THE PINNED SOURCE'S OWN TEXT LAYER -- not this act's writing"),
]

# ### owner needles: each at the file that EMITTED it, and EACH ALSO IN THE EXTRACT FILE (G-EXTRACT)
OWNER_NEEDLES = [
    ("the deposit's refusal, at the verified copy", MONO, 'deliberately **not** compiling the cross-register equivalences'),
    ("### the register sentence", MONO, 'A reader who discharges any one of them discharges all five'),
    ("### the finite-range certificate's scope", MONO, 'a certificate reaching exactly to where discrimination would begin, and no further'),
    ("the keystone's split, at the keystone", BALANCE, 'f_A(s) = log s + logΓ(s/2) − (s/2)log π and f_Z(s) = log((s−1)ζ(s))'),
    ("### and the bench that computes it", BENCH, 'return mp.log(s) + mp.loggamma(s / 2) - (s / 2) * mp.log(mp.pi)'),
    ("the wall, at the residue keystone", RESIDUE, 'The space is the wall'),
    ("b324 -- the square is not a zero channel", d('b324_the_keystones_reread.txt'), 'The square is not a zero channel'),
    ("### and the bridging statement typed", d('b324_the_keystones_reread.txt'), 'a formula carrying the archimedean margin'),
    ("b321 -- the balance is minus the zero side", d('b321_the_window_opened.txt'), 'SUM_v W_v(f) = - Z'),
    ("b326 -- the seed priced, not built", d('b326_the_reach.txt'), 'A seed that changes sign there is'),
    ("b288 -- the weights diverge at the object's space", d('b288_the_family_and_the_complement.txt'),
     "THE INSTRUMENTS' WEIGHTS DIVERGE PRECISELY AS ONE APPROACHES THE OBJECT'S SPACE"),
    ("the citation the corpus names, at the banked module", d('read_pentagon.txt'), 'Bombieri–Lagarias 1999, via the Guinand–Weil explicit formula'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### the ledger exists', BANK, 'THE LEDGER EXISTS: `PLACE-papers/FACES_LEDGER.md`, THIRTEEN ROWS, SEVENTY-EIGHT PAIRS,'),
    ('### a map, not a carrier', BANK, 'A MAP OF THE PREMISE, NOT A'),
    ('### the bridge read', BANK, 'THE BRIDGE, READ: DIFFERENT ON BOTH QUESTIONS, WITH THE MAP DERIVED AND THE BRIDGE'),
    ('### question one', BANK, 'DIFFERENT, constituent quoted: by the constant `1`'),
    ('### question two', BANK, 'quoted: at the second term.'),
    ('### one distribution', BANK, 'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE'),
    ('### the branch did not fire', BANK, "The order's *if SAME* branch did not fire."),
    ('### the source substituted', BANK, "THE SOURCE IS THE SAME AUTHOR'S RESTATEMENT, PINNED BY THIS ACT."),
    ('### the notes as contacts', BANK, 'THE TWO NOTES ARE FILED AS CONTACTS, NOT SEEDS'),
    ('### the count as stated', BANK, 'five Fano points and contains two of the seven lines, as the order stated.'),
    ('### the three trails', BANK, 'THE THREE OWED BRIDGES ARE ON THE TRAILS BY ID:'),
    ('### the two incidents', BANK, "TWO INCIDENTS OF THIS ACT'S OWN, DECLARED:"),
    ('### the R4 refusal', BANK, "the row-writer's quotation guard fired"),
    ('### the bench dict', BANK, "the bench's own literature dict disagrees with the balance keystone's literature column"),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### no two faces equivalent', BANK, 'IT DOES NOT SAY ANY TWO FACES ARE EQUIVALENT'),
    ('### not closed in the negative', BANK, 'IT DOES NOT SAY THE BRIDGE IS CLOSED IN THE NEGATIVE.'),
    ('### no theorem, no distribution, no control', BANK, 'IT PROVES NO THEOREM, EVALUATES NO WEIL DISTRIBUTION, AND RUNS NO CONTROL.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any run', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RAN.'),
    ('bank gives step zero', BANK, 'STEP ZERO.'),
    ('### the resume', BANK, 'THE RESUME.'),
    ('### the extract not re-run', BANK, 'so it was NOT re-run'),
    ('### the pin is this act\'s', BANK, "THE PIN IS THIS ACT'S"),
    ('### the different object in the index', BANK, '(`e1-even-bridge`, b35), reported as such and not taken as a hit.'),
    ('bank gives the ledger', BANK, 'COMPONENT 1 -- THE LEDGER.'),
    ('### the writer\'s guards', BANK, 'VERIFIED AGAINST ITS EMITTING FILE BEFORE WRITING'),
    ('### R4 after F7', BANK, 'AFTER F7 IN FILE ORDER'),
    ('### the census extended', BANK, 'THE CENSUS, EXTENDED TO THE NEW LEDGER:'),
    ('bank gives the bridge', BANK, 'COMPONENT 2 -- THE BRIDGE READ.'),
    ('### the derivation in four steps', BANK, 'THE DERIVATION (registration, section (3)), IN FOUR STEPS:'),
    ('### the map', BANK, '**`lambda_A(n) = S_inf(n) + 1`**'),
    ('### the bench definitions executed, not the run', BANK, 'the file has no main guard and its run section was not'),
    ('### the discrimination arm', BANK, 'THE DISCRIMINATION ARM FIRES:'),
    ('### the fourth control', BANK, 'THE FOURTH CONTROL, PRICED AND NOT RUN:'),
    ('### the bridge owed', BANK, 'THE BRIDGE STAYS OWED AND IS TYPED MORE SHARPLY'),
    ('bank gives the notes', BANK, 'COMPONENT 3 -- THE TWO NOTES.'),
    ('### contact A', BANK, 'CONTACT A -- THE CURIE READING OF THE EIGENVALUE-ONE BOUNDARY.'),
    ('### contact B', BANK, 'CONTACT B -- THE CUBIT READING OF THE 256 RULES.'),
    ('bank gives the cascades', BANK, 'COMPONENT 4 -- THE CASCADES.'),
    ('### every pair present', BANK, 'SEVENTY-EIGHT PAIRS, EVERY ONE PRESENT:'),
    ('### the candidate row', BANK, 'ONE CANDIDATE ROW, FLAGGED AND NOT ADDED'),
    ('### the author authorizes', BANK, "THE ROW IS THE AUTHOR'S TO AUTHORIZE."),
    ('bank gives the closing', BANK, 'THE CLOSING.'),
    ('### the roster unchanged', BANK, 'THE MIRROR ROSTER IS NOT CHANGED.'),
    ('### handoff not edited', BANK, '`HANDOFF.md` IS NOT EDITED.'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### the discriminating-family act next', BANK, 'THE DISCRIMINATING-FAMILY ACT IS NAMED NEXT BY THE ORDER'),
    ('### then the sealing module, then TECHNE', BANK, 'THEN THE FINITE-SIDE SEALING MODULE**, the kernel act; ### **THEN THE TECHNE EXTRACTION.'),
    ('### the fold accumulating', BANK, 'THE FOLD FROM b323 ONWARD IS ACCUMULATING'),
    ('### no recommendation', BANK, 'NO RECOMMENDATION AND NO RANKING'),
    ('registration names the act', REG, 'THE FACES LEDGER, THE BRIDGE, AND TWO NOTES. ### THE REGISTRATION.'),
    ('### sealed before any run', REG, 'THIS REGISTRATION IS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RUNS.'),
    ('### the derived map as a bar', REG, '**`λ_A(n) = S∞(n) + 1` FOR EVERY'),
    ('### the branches fixed', REG, 'THE BRANCHES, FIXED NOW:'),
    ('the bridge run holds', BRUN, 'HOLDS'),
    ('### the same arm fires', BRUN, 'FIRES (the SAME arm fails at every n)'),
    ('### question one in the run', BRUN, 'QUESTION ONE : DIFFERENT, constituent quoted'),
    ('### question two in the run', BRUN, 'QUESTION TWO : DIFFERENT, constituent quoted'),
    ('### the branch in the run', BRUN, 'THE "IF SAME" BRANCH OF THE ORDER : DOES NOT FIRE'),
    ('the notes run, as stated', NRUN, "THE ORDER'S NUMBERS (five points, two lines) : AS STATED"),
    ('the filing: deposit unchanged', FIL, 'THE DEPOSIT IS BYTE-UNCHANGED : True'),
    ('### four blocks written', FIL, 'FILING CHECKS FAILING : 0'),
    ('the rows read back', CORR, 'last 2 row number(s) are [166, 167]'),
    ('the index keys read back', IDX, 'faces-ledger             returns a row : True ; returns 2 row(s), 2 required  PASS'),
    ('### and the arm', IDX, 'the answer refuses the carrier reading BY NAME        : True'),
    ('the faces census', CEN, 'TOTAL MISSING : 0'),
    ('### 78 of 78', CEN, 'pair lines 78 of N(N-1)/2 = 78'),
    ('the handoff census', CENSUS, 'TOTAL MISSING : 0'),
    ('the satisfiability run passes', SATIS, 'JOINTLY SATISFIABLE'),
    ('the regspec found no predictions', REGSPEC, 'ARTIFACT-COUNT PREDICTIONS FOUND : 0'),
    ('the ferry scan was clean', SCAN, 'STRUCK-CLAUSE HITS : 0'),
    ('### on stems too', SCAN, 'BANNED/RETIRED-STEM HITS : 0'),
    ('the resume scan was clean', SCAN2, 'STRUCK-CLAUSE HITS : 0'),
    ('the seed run: R4 refused', LRUN, 'REFUSED          row R4: quotation not verified'),
    ('### the duplicate guard exercised', LRUN, 'the duplicate guard, exercised'),
    ('the second seed run: R4 written', LRUN2, 'WRITTEN          row R4'),
    ('the live row written', LIVE, 'WRITTEN          row L1'),
    ('the cascades written', CASC, 'STATED 25 OWED 5 NONE 48'),
    ('the candidate section written', CAND, 'WRITTEN          candidate section'),
    ('the extract file reports itself', EXTRACT, 'PATHS MISSING : 0 ; QUOTATIONS NOT FOUND : 0'),
    ('the source pin reports itself', SRC, 'FRAGMENTS NOT LOCATED : 0'),
]

MUST_FAIL = [
    ('no equivalence is stated', BANK, 'THE FACES ARE EQUIVALENT.'),
    ('### nor compiled', BANK, 'THE EQUIVALENCE IS COMPILED.'),
    ('the bridge is not closed', BANK, 'THE BRIDGE IS CLOSED.'),
    ('### nor proved impossible', BANK, 'NO BRIDGE EXISTS.'),
    ('the margins are not called one', BANK, 'THE TWO MARGINS ARE ONE FUNCTIONAL.'),
    ('the channel is not called SAME', BANK, 'QUESTION ONE: SAME.'),
    ('no face is promoted', BANK, 'A FACE IS PROMOTED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the candidate is not added', BANK, 'THE THIRD IDENTITY ELEMENT IS A ROW.'),
    ('no deposited text is edited', BANK, 'THE DEPOSIT IS EDITED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
    ('### either way', BANK, 'RH FAILS.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
]

TOOLNUM = [
    ("the source pin: bytes, hash, pages, fragments located", 'tools/b327_source.py'),
    ("the extract step's counts", 'tools/b327_extract.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b327_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
    ("the ledger's rows, cells, bytes, pair counts", 'tools/b327_faces_row.py'),
    ("the rows' quoted claims and the pair table", 'tools/b327_faces_rows.py'),
    ("the corroboration: the differences, the radii, the SAME arm", 'tools/b327_bridge.py'),
    ("the live row's pairs", 'tools/b327_bridge_pairs.py'),
    ("the Fano counts", 'tools/b327_notes.py'),
    ("the filings' line counts and prefix checks", 'tools/b327_filings.py'),
    ("what is missing from the new ledger, counted", 'tools/b327_faces_census.py'),
    ("what is missing from HANDOFF, counted", 'tools/b307_handoff_census.py'),
    ("the correspondence rows' numbers", 'tools/b327_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b327_index_append.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the pins by ls-remote", 'tools/b303_pins.py'),
    ("the gate, needle and hedge counts", 'tools/b327_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b327' in x)

SEAL = 'dca39c0036740953415e5242be9a6cced99ebeedbcdbb6e47ffa7a560ccfbffa'


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace('\r\n', '\n')


def main():
    fails = []
    print('=' * 100)
    print('b327 -- GATE SUITE (THE FACES LEDGER: A MAP OF THE PREMISE; THE BRIDGE: READ, AND STILL OWED)')
    print('=' * 100)

    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it; the deposit at its VERIFIED copy; each also IN THE EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILE'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
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
    reg = io.open(REG, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    bj = json.load(io.open(d('b327_bridge.json'), encoding='utf-8'))
    nj = json.load(io.open(d('b327_notes.json'), encoding='utf-8'))
    rows = [ln for ln in tbl.split('\n') if ln.startswith('| 166 |') or ln.startswith('| 167 |')]
    rowtxt = '\n'.join(rows)

    print('\n  G-NOEQUIV (a map of the premise, not a carrier; no equivalence compiled, stated or implied):')
    kinds = set(re.findall(r'^\| [RFL]\d+–[RFL]\d+ \| (\w+) \|', led, re.M))
    ne = ('IT DOES NOT SAY ANY TWO FACES ARE EQUIVALENT' in bank
          and 'deliberately **not** compiling the cross-register equivalences' in led
          and 'A MAP OF THE PREMISE, NOT A CARRIER OF IT' in led
          and 'A MAP OF THE PREMISE, NOT A CARRIER OF IT' in idx
          and 'NO EQUIVALENCE COMPILED' in rowtxt and 'NOT ONE FUNCTIONAL' in rowtxt and len(rows) == 2
          and kinds <= {'STATED', 'OWED', 'NONE'} and len(kinds) == 3
          and 'W-ORD-LI-WEIL-BRIDGE' in idx)
    print('    bank, ledger head, index, rows refuse the carrier reading; cascade kinds are exactly %s : %s' % (sorted(kinds), ne))
    if not ne:
        fails.append('G-NOEQUIV')

    print('\n  G-QUOTE / G-EXTRACT (every quotation the ledger carries is in its emitter, and in the extract file):')
    allq, miss_q, miss_x = [], [], []
    for row in R.ROWS:
        allq += list(row['quotes'])
    for _k, (_kind, _text, qs) in R.PAIRS.items():
        allq += list(qs)
    allq += [(q[0], q[1], bool(q[2])) for q in bj['row']['quotes']]
    for _k, (_kind, _text, qs) in bj['pairs'].items():
        allq += [(q[0], q[1], bool(q[2])) for q in qs]
    seen = set()
    src_txt = io.open(SRC, encoding='utf-8').read()
    for p, f, flat in allq:
        if (p, f) in seen:
            continue
        seen.add((p, f))
        if W.verify_quotes([(p, f, flat)]):
            miss_q.append((p, f))
        if flat:
            continue
        if ('fragment %r' % f) not in extract:
            miss_x.append((p, f))
    print('    distinct quotations %d ; not in their emitter %d ; not in the extract file %d ; source fragments located per the pin file : %s'
          % (len(seen), len(miss_q), len(miss_x), 'FRAGMENTS NOT LOCATED : 0' in src_txt))
    if miss_q or miss_x or 'FRAGMENTS NOT LOCATED : 0' not in src_txt:
        fails.append('G-QUOTE/G-EXTRACT')

    print('\n  G-ORDER (the registration was sealed before any instrument of this act ran):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    same = SEAL in reg
    seal_m = os.path.getmtime(REG)
    firsts = [os.path.getmtime(p) for p in (LRUN, LRUN2, LIVE, CASC, CAND, BRUN, NRUN, FIL, CORR, IDX, CEN, LEDGER, d('b327_bridge.json'), d('b327_notes.json')) if os.path.exists(p)]
    precedes = all(seal_m < m for m in firsts)
    print('    seal verifies : %s ; hash matches the literal in this gate : %s ; the sealed file predates every instrument record : %s' % (intact, same, precedes))
    print("    ### the bank's own sentence : %s" % ('THE REGISTRATION WAS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RAN' in bank))
    if not (intact and same and precedes):
        fails.append('G-ORDER')

    print('\n  G-BRIDGE (the corroboration holds, the SAME arm fires, the verdict words agree everywhere):')
    q1, q2 = bj['q1'], bj['q2']
    l1 = [ln for ln in led.splitlines() if ln.startswith('| L1 | ')]
    gb = (bj['holds'] and bj['fires'] and not bj['if_same_fires']
          and q1.startswith('DIFFERENT') and q2.startswith('DIFFERENT')
          and len(l1) == 1 and ('QUESTION ONE: %s' % q1) in l1[0] and ('QUESTION TWO: %s' % q2) in l1[0]
          and ('QUESTION ONE: %s. QUESTION TWO: %s.' % (q1, q2)) in rowtxt
          and q1 in idx and q2 in idx
          and 'DIFFERENT, constituent quoted: by the constant `1`' in bank
          and float(bj['worst_diff']) <= 1e-20 and float(bj['worst_radii']) <= 1e-20 and float(bj['same_arm_min']) > 1e-20)
    print('    holds %s ; fires %s ; if-SAME %s ; q1 %r ; q2 %r ; agree in ledger/rows/index/bank : %s'
          % (bj['holds'], bj['fires'], bj['if_same_fires'], q1, q2, gb))
    if not gb:
        fails.append('G-BRIDGE')

    print('\n  G-LEDGER (thirteen rows, seven cells, no blank, 78 pairs, no pair absent, the class line, the candidate once):')
    import b303_correspondence as C3
    import b302_correspondence as C2
    rws = [ln for ln in led.splitlines() if ln.startswith('| ') and ln.split('|')[1].strip() in R.ORDER]
    cells_ok = all(len(C3.split_cells(ln)) == len(R.COLUMNS) and all(x.strip() for x in C3.split_cells(ln)) for ln in rws)
    ids = [ln.split('|')[1].strip() for ln in rws]
    pairs_present = all(('| %s–%s |' % (a, b)) in led for a, b in W.all_pairs(R.ORDER))
    npairs = len(re.findall(r'^\| [RFL]\d+–[RFL]\d+ \|', led, re.M))
    tier = DC.TIER.search(led)
    routed = bool(tier and (tier.group(2) or '').upper() == 'ROUTED')
    gl = (len(rws) == 13 and sorted(ids) == sorted(R.ORDER) and cells_ok and C2.blank_cells(led) == 0
          and npairs == 78 and pairs_present and routed and led.count('<!-- b327 candidate rows -->') == 1
          and 'CANDIDATE — NOT ADDED' in led and 'it certifies nothing' in led)
    print('    rows %d (ids %s) ; cells ok %s ; blank cells %d ; pair lines %d ; every pair present %s ; class line ROUTED %s ; candidate once %s : %s'
          % (len(rws), ''.join(sorted(ids)) == ''.join(sorted(R.ORDER)), cells_ok, C2.blank_cells(led), npairs, pairs_present, routed, led.count('<!-- b327 candidate rows -->') == 1, gl))
    if not gl:
        fails.append('G-LEDGER')

    print('\n  G-NOTES (the count matched the order; the contacts carry no promotion criterion; filed nowhere research-facing):')
    em = io.open(os.path.join(PP, 'EMERGING_RESEARCH_PROGRAMMES.md'), encoding='utf-8', errors='replace').read()
    blk = em[em.index('<!-- b327 contacts -->'):] if '<!-- b327 contacts -->' in em else ''
    gn = (nj['as_stated'] and nj['fixtures_pass'] and nj['points'] == 5 and nj['lines'] == 2
          and 'not seeds' in blk and 'Promotes on' not in blk and 'Contact A' in blk and 'Contact B' in blk
          and 'No claim' in blk and 'not checked here' in blk and 'not answered here' in blk)
    others = [rel for rel in ('FINDINGS.md', 'OPEN_TRAILS.md', 'VERIFICATION_LOOM.md', 'FACES_LEDGER.md')
              if 'Curie' in (io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read().split('<!-- b327')[1:] and
                             ''.join(io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read().split('<!-- b327')[1:]) or '')]
    print('    points %d lines %d as stated %s ; block carries contacts, no promotion criterion, no claim : %s ; the Curie note in a research-facing b327 block : %s'
          % (nj['points'], nj['lines'], nj['as_stated'], gn, others))
    if not gn or others:
        fails.append('G-NOTES')

    print('\n  G-TRAILS / G-ANCHOR (three IDs on the trails; the anchor once in FINDINGS; each block once):')
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read()
    fd = io.open(os.path.join(PP, 'FINDINGS.md'), encoding='utf-8', errors='replace').read()
    lm = io.open(os.path.join(PP, 'VERIFICATION_LOOM.md'), encoding='utf-8', errors='replace').read()
    gt = (all(x in ot for x in ('W-ORD-LI-WEIL-BRIDGE', 'W-ORD-DISCRIMINATING-FAMILY', 'W-ORD-LI-FAMILY-CONTROL'))
          and ot.count('<!-- b327 owed bridges -->') == 1 and fd.count('<a id="faces-ledger"></a>') == 1
          and fd.count('<!-- b327 faces-ledger anchor -->') == 1 and lm.count('<!-- b327 loom entry -->') == 1
          and em.count('<!-- b327 contacts -->') == 1)
    print('    %s' % gt)
    if not gt:
        fails.append('G-TRAILS/G-ANCHOR')

    print('\n  G-APPEND (every PLACE-papers file this act wrote: the blob at HEAD is a TRUE PREFIX, or there is no blob yet):')
    for rel in PP_WRITTEN:
        now = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        hb = blob_of(PP, rel)
        ok = True if hb is None else norm(now).startswith(norm(hb).rstrip('\n'))
        print('    %-36s blob %s ; TRUE PREFIX : %s' % (rel, 'present' if hb is not None else 'none yet (untracked)', ok))
        if not ok:
            fails.append('G-APPEND ' + rel)

    print('\n  G-DEPOSIT (no file under outputs/DEPOSITED-v1.1.2/ is written):')
    st = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    print('    git status over the deposit path : %r' % st)
    if st:
        fails.append('G-DEPOSIT')

    print('\n  G-NOEDIT (owner instruments untouched):')
    dr = git(ROOT, 'status', '--porcelain', '--', *OWNERS_RELAY).strip()
    dp = git(PP, 'status', '--porcelain', '--', *OWNERS_PP).strip()
    print('    relay owners : %r ; papers owners : %r' % (dr, dp))
    if dr or dp:
        fails.append('G-NOEDIT')

    print('\n  G-PAPERS (only the five files this act writes are changed in PLACE-papers, or already committed):')
    pp = git(PP, 'status', '--porcelain')
    changed = sorted(x[3:].strip() for x in pp.splitlines() if x.strip() and not x.startswith('??'))
    untr = sorted(x[3:].strip() for x in pp.splitlines() if x.startswith('??'))
    only = set(changed) <= set(PP_WRITTEN) and set(untr) - {'internal/BLOB_SENSITIVITY_2026-08-29.md'} <= {'FACES_LEDGER.md'}
    print('    tracked changes : %s ; untracked : %s ; within this act\'s five : %s' % (changed, untr, only))
    if not only:
        fails.append('G-PAPERS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob):')
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    pfx2 = norm(tbl).startswith(norm(head).rstrip('\n'))
    print('    table is a TRUE PREFIX : %s' % pfx2)
    if not pfx2:
        fails.append('G-ANCESTOR')

    print('\n  G-COMPUTE (the cap of two computations, re-measured off the tools\' imports, over STRIPPED code):')
    q, loud = K7.strip_fixture()
    comp = []
    for name in sorted(os.listdir(os.path.join(ROOT, 'tools'))):
        if name.startswith('b327') and name.endswith('.py'):
            src = K7.strip_text(io.open(t(name), encoding='utf-8').read())
            if re.search(r'\bimport\s+(mpmath|numpy|scipy)\b', src):
                comp.append(name)
    print('    stripper fixture quiet/loud : %s/%s ; tools importing a numeric library : %s' % (q, loud, comp))
    if not (q and loud and comp == ['b327_bridge.py']):
        fails.append('G-COMPUTE')

    print('\n  G-ONCE (run files written once per path; the seed run\'s record kept beside the second\'s):')
    once_ok = (os.path.exists(LRUN) and os.path.exists(LRUN2) and os.path.exists(LIVE) and os.path.exists(CASC)
               and os.path.exists(CAND) and os.path.exists(FIL)
               and 'run_file_name' in io.open(t('b327_faces_row.py'), encoding='utf-8').read()
               and '_rerun.txt' in io.open(t('b327_filings.py'), encoding='utf-8').read())
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

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
            for h in (ch + sh)[:6]:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-34s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-STEM-APPENDED (the four appended blocks, swept):')
    for rel, mark in (('FINDINGS.md', '<!-- b327 faces-ledger anchor -->'), ('VERIFICATION_LOOM.md', '<!-- b327 loom entry -->'),
                      ('EMERGING_RESEARCH_PROGRAMMES.md', '<!-- b327 contacts -->'), ('OPEN_TRAILS.md', '<!-- b327 owed bridges -->')):
        txt = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        blk = txt[txt.index(mark):] if mark in txt else ''
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-36s struck : %d   stem : %d' % (rel, len(ch), len(sh)))
        if ch or sh:
            fails.append('G-STEM-APPENDED ' + rel)

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-58s %-34s exists=%s tracked=%s' % (what[:58], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote, the appended blocks and rows included):')
    tmpdir = tempfile.mkdtemp(prefix='b327_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the ledger', LEDGER), ('the bridge run', BRUN),
               ('the notes run', NRUN), ('the filing', FIL), ('the census', CEN)]
    for rel, mark in (('FINDINGS.md', '<!-- b327 faces-ledger anchor -->'), ('VERIFICATION_LOOM.md', '<!-- b327 loom entry -->'),
                      ('EMERGING_RESEARCH_PROGRAMMES.md', '<!-- b327 contacts -->'), ('OPEN_TRAILS.md', '<!-- b327 owed bridges -->')):
        txt = io.open(os.path.join(PP, rel), encoding='utf-8', errors='replace').read()
        blk = txt[txt.index(mark):] if mark in txt else ''
        p = os.path.join(tmpdir, rel + '.block.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(blk)
        targets.append(('the block in ' + rel, p))
    p = os.path.join(tmpdir, 'rows.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(rowtxt + '\n')
    targets.append(('rows 166-167', p))
    ib = idx[idx.index('# ### THE FACES LEDGER (b327).'):idx.index('# ### THE TWO NOTES, FILED AS CONTACTS (b327).')] if '# ### THE FACES LEDGER (b327).' in idx else ''
    p = os.path.join(tmpdir, 'index.txt')
    io.open(p, 'w', encoding='utf-8', newline='\n').write(ib)
    targets.append(('the index rows', p))
    for lbl, path in targets:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-36s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
