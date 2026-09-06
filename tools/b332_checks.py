# -*- coding: utf-8 -*-
"""b332_checks.py -- THE GATE SUITE FOR THE CLAUSE STATED.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`F-QUOTE` / `F-GRADES`, RE-RUN LIVE** ### -- the generator's own gates through its module.
###   ### ### **`G-STATEMENT`** ### -- the section carries (S) with both quantifiers, the class, the criterion,
###     the five registers, the refusal, the register sentence exact and the deposit's h2 words at its head.
###   ### ### **`G-E0`** ### -- the table names every constituent K1-K8 with its unfolding; the unowned one is
###     K8; the verdict says it halts there.
###   ### ### **`G-RANK`** ### -- the ranking re-computed from the sealed rule equals the emitted one; the
###     navigator's expectation scored in words, NOT MET as measured.
###   ### ### **`G-NOTDISCHARGED`** ### -- the section's own words: not discharge, not weaken, not replace;
###     must-fail fixtures on the opposite lines.
###   ### **`G-FACE`, `G-PLACEMENT`, `G-ADDITIVE`, `G-AIMMAP`, `G-ROW`, `G-KEY`, `G-ORDER`, `G-HOOK` / `G-MIRROR`,
###     `G-NUMBERS`, `G-TOOLNUM`, the hedge audit (the section included), the stem sweep, the must-fail
###     fixtures** -- standing.
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
import b332_statement as S  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
KEY = os.path.join(PP, 'phase2', 'method', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md')
KEYREL = 'phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b332_the_clause_stated.txt')
REG = d('b332_registration_2026-09-06.txt')
EXTRACT = d('b332_extract_notes.txt')
SRUN, SRUN2, SRUN3 = d('b332_statement_run.txt'), d('b332_statement_run2.txt'), d('b332_statement_run3.txt')
EMIT, ROWSJ = d('b332_statement_emitted.md'), d('b332_statement_rows.json')
FIL, FILR = d('b332_filings_run.txt'), d('b332_filings_rerun.txt')
CORR, CORRR = d('b332_corr_run.txt'), d('b332_corr_rerun.txt')
IDX, IDXR = d('b332_index_run.txt'), d('b332_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b332_ferry_scan.txt'), d('b332_reg_termscan.txt'), d('b332_reg_gate.txt')
CENSUS, FCEN = d('b332_census.txt'), d('b332_faces_census.txt')
REGSPEC, SATIS = d('b332_regspec_run.txt'), d('audit_b332_reg_satisfiable.txt')
PINS, INDEXQ = d('b332_pins_stepzero.txt'), d('audit_b332_index_query.txt')
HOOKS, MIRROR = d('b332_hooks.txt'), d('b332_mirror.txt')
SEAL = '0ac2de949bad57f7922b639081f01d628022cae11c758cbe1fe5fd0ffbaa9c76'

OWNED = [BANK, REG, SRUN, SRUN2, SRUN3, EMIT, ROWSJ, FIL, FILR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b332_satisfiable.json'), t('b332_extract.py'), t('b332_statement.py'), t('b332_regspec.py'), t('b332_filings.py'),
         t('b332_correspondence.py'), t('b332_index_append.py')]

CARRIERS = [
    (t('b332_checks.py'), 'its own fixtures'),
    (d('b332_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("deposit -- h2", S.DEP, 'and h2 \u2014 nonvanishing of the transform at the point in question.'),
    ("deposit -- the refusal", S.DEP, 'while deliberately **not** compiling the cross-register equivalences, since to compile "discharge one and you discharge all five" would be to compile RH-equivalence itself.'),
    ("deposit -- the fourth register", S.DEP, 'Fourth: the distance between *balance* and *positivity* at the multiplicative place.'),
    ("the register sentence", S.FACESK, 'THE REGISTER SENTENCE, UNTOUCHED BY EVERY WORD BELOW: `h2` IS THE SINGLE OPEN PREMISE.'),
    ("source -- Definition 3.1", S.SRC, 'positive de\ufb01nite when its Fourier transform is pointwise positive'),
    ("source -- Proposition C.1", S.SRC, 'Proposition C.1 Let Z \u0102 C be the set of non-trivial zeros of the Riemann zeta function and'),
    ("b321 -- the pole term vanishes", d('b321_the_window_opened.txt'), 'THE POLE TERM VANISHES IDENTICALLY FOR A LAWFUL'),
    ("b326 tool -- the convention", t('b326_windows.py'), 'places_z=PRz1 - Az1, places_q=PRq - Aq1'),
    ("b310 -- one term", d('b310_the_smear_collapses.txt'), 'THE TEST FUNCTION READ AT ONE POINT, TIMES A DIMENSION'),
    ("b329 -- compiled", d('b329_the_finite_side_seal.txt'), "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS"),
    ("b306 -- factor for factor", d('b306_the_difference.txt'), "`k`-th term of `W_p` under CC's own `\u2206`-normalization, factor for factor."),
    ("b320 -- the sign certified, the size not", d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ("b315 -- the term defined", d('b315_the_calibration_and_the_rate.txt'), 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    ("b321 -- Theorem 4.7 an equality", d('b321_the_window_opened.txt'), 'Theorem 4.7 / (83) is an ### **EQUALITY**, not'),
    ("b318 -- the square nonnegative", d('b318_the_forced_sign.txt'), 'THE SQUARE IS NONNEGATIVE AT EVERY CELL AND EVERY FRAME, AND THE SMEAR IS NOT.'),
    ("b300 -- derives on imports", d('b300_the_archimedean_leg.txt'), 'GRADE: ### **DERIVES-on-IMPORTS**'),
    ("b322 -- under-resolved", d('b322_the_membership.txt'), 'VERDICT: ### UNDER-RESOLVED, WITH ITS PRICE.'),
    ("the ledger's R4 row", LEDGER, '| R4 | R4 -- the distance between balance and positivity at the multiplicative place'),
    ("the keystone's placement", KEY, '**Cross-references, appended and not rewritten:**'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### stated, not discharged', BANK, 'THE CLAUSE IS STATED, WHOLE, IN THE ARC\'S VOCABULARY, AND IT IS NOT DISCHARGED.'),
    ('### the gate halts at K8', BANK, 'THE E0 GATE HALTS AT K8, THE QUANTIFIERS, AND AT NOTHING ELSE.'),
    ('### F-QUOTE 27', BANK, '`F-QUOTE` PASSES AT 27 OF 27, THE DISCRIMINATION ARM FIRES, AND `F-GRADES` PASSES:'),
    ('### the expectation not met', BANK, "SEAT'S, WHICH AGREED WITH IT.**"),
    ('### the reason is in the rule', BANK, 'THE REASON IS IN THE RULE AND NOT IN A JUDGEMENT:'),
    ('### both seats expected the remainder', BANK, 'BOTH SEATS EXPECTED THE REMAINDER; THE RULE BOTH SEATS SEALED SAYS OTHERWISE; THE RULE IS'),
    ('### the aim-map named', BANK, 'THE AIM-MAP IS NAMED AS NEXT, FOR THE SOFTEST CONSTITUENT UNDER THE RULE -- K5 -- AND'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any write', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY WRITE INTO THE PAPERS.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE STATEMENT, WRITTEN WHOLE.'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE GRADES AND THE RANKING.'),
    ('### scored not met', BANK, "THE NAVIGATOR'S REGISTERED EXPECTATION -- THE REMAINDER SOFTEST -- SCORED: NOT MET."),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- WHAT THE STATEMENT DOES AND DOES NOT DO.'),
    ('### does not discharge', BANK, 'IT DOES NOT DISCHARGE THE CLAUSE. IT DOES NOT WEAKEN IT. IT DOES NOT REPLACE IT.'),
    ('### one face', BANK, "IT IS ONE FACE OF THE OBLIGATION AND NOT THE OBLIGATION'S COMPILED EQUIVALENCE."),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- THE PLACEMENT.'),
    ('### no terminal and the reason', BANK, 'AND THE REASON: ANALYSIS, QUANTIFIED OVER AN INFINITE CLASS AND OVER THE ZEROS'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1 the first emission', BANK, 'THE FIRST EMISSION CARRIED A SENTENCE THE COMPUTED RANKING CONTRADICTED.'),
    ('### E4 the expectation wrong about its own rule', BANK, "THIS SEAT'S SEALED EXPECTATION WAS WRONG ABOUT ITS OWN SEALED RULE."),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### the ranking is not a verdict', BANK, 'IT DOES NOT SAY THE RANKING IS A VERDICT ON THE CLAUSE.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE AIM-MAP -- AND IT IS NOT THE DISCHARGE.'),
    # ### the sentence wraps in the sealed file; the anchor is the wrapped line's own text (a sealed file is not edited)
    ('registration -- the rule sealed', REG, "constituent's rank is its softest grade among its owners, ordered"),
    ('registration -- this seat expects the remainder', REG, 'THIS SEAT EXPECTS THE REMAINDER'),
    ('registration -- the shadow none', REG, '### ### **NONE.**'),
]

MUST_FAIL = [
    ('the bank never says discharged', BANK, '### ### **THE CLAUSE IS DISCHARGED.**'),
    ('the bank never says weakened', BANK, '### ### **THE CLAUSE IS WEAKENED.**'),
    ('the bank never says replaced', BANK, '### ### **THE CLAUSE IS REPLACED.**'),
    ('the section never says the faces are equivalent', EMIT, '**The five faces are equivalent.**'),
    ('the bank never says the expectation was met', BANK, "### ### **THE NAVIGATOR'S REGISTERED EXPECTATION IS MET.**"),
]

TOOLNUM = [
    ('+74 lines, 3024 -> 3098, 19 sections, F-QUOTE 27/0, the ranking', 'tools/b332_statement.py'),
    ('row S1 (7 cells, 4 quotations), the keystone +4 lines', 'tools/b332_filings.py'),
    ('row 178', 'tools/b332_correspondence.py'),
    ('the key', 'tools/b332_index_append.py'),
    ('22 clauses', 'tools/b332_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('15796 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b332_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the ledger writer', 'tools/b327_faces_row.py'),
]
NEW_THIS_ACT = {'tools/b332_statement.py', 'tools/b332_filings.py', 'tools/b332_correspondence.py', 'tools/b332_index_append.py',
                'tools/b332_regspec.py', 'tools/b332_extract.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace('\r\n', '\n')


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def main():
    fails = []
    print('=' * 100)
    print('b332 -- GATE SUITE (THE CLAUSE STATED: A STATEMENT, EVERY GRADE ITS OWNER\'S, NOT DISCHARGED)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
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
    emit = io.open(EMIT, encoding='utf-8').read()
    fnd = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    rows = json.load(io.open(ROWSJ, encoding='utf-8'))
    srun = io.open(SRUN2, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    key = io.open(KEY, encoding='utf-8', errors='replace').read()

    print('\n  F-QUOTE / F-GRADES (the generator\'s gates, re-run live):')
    logs = []
    q = S.fquote(logs.append)
    g = S.fgrades(logs.append)
    for ln in logs:
        print('   ' + ln)
    if not (q and g):
        fails.append('F-QUOTE/F-GRADES')

    print('\n  G-STATEMENT (the section: (S) with both quantifiers, the class, the criterion, the five registers, the refusal, the register sentence, the h2 words):')
    need = ['**(S)** For every `g` in the source\u2019s class', 'keeps the criterion\u2019s sign', '`\u03a3_v W_v(f) \u2264 0`',
            'positive de\ufb01nite when its Fourier transform is pointwise positive', 'Proposition C.1', 'one premise in five registers',
            'deliberately **not** compiling the cross-register equivalences', '`h2` IS THE SINGLE OPEN PREMISE', 'nonvanishing of the transform at the point in question',
            'over the class (infinite) and, through the explicit formula, over the zeros']
    miss = [x for x in need if x not in emit]
    gs = not miss and emit.strip() in fnd
    print('    missing %s ; the emitted section in the file verbatim %s : %s' % (miss, emit.strip() in fnd, gs))
    if not gs:
        fails.append('G-STATEMENT')

    print('\n  G-E0 (K1-K8 each with its unfolding; K8 unowned; the verdict halts there and at nothing else):')
    ge = all(('| **%s** ' % k) in emit for k in ['K%d' % i for i in range(1, 9)]) and 'UNOWNED' in emit and 'it halts at K8' in emit and 'HALTS at K8' in srun
    print('    %s' % ge)
    if not ge:
        fails.append('G-E0')

    print('\n  G-RANK (the ranking re-computed from the sealed rule equals the emitted one; the expectation scored NOT MET as measured):')
    rk = S.rank()
    same = [list(r) for r in rk] == rows['ranking']
    verdict, softest = S.score(rk)
    gr = same and verdict == rows['verdict'] == 'NOT MET' and softest == ['K5'] and ('scored against the ranking: %s' % verdict) in emit and 'SCORED: NOT MET.' in bank
    print('    recomputed == emitted %s ; verdict %s ; softest %s : %s' % (same, verdict, softest, gr))
    if not gr:
        fails.append('G-RANK')

    print('\n  G-NOTDISCHARGED / G-FACE / G-AIMMAP (the section\'s own words):')
    gn = ('**It does not discharge the clause. It does not weaken it. It does not replace it.**' in emit
          and 'one face of the obligation and not the obligation\u2019s compiled equivalence' in emit
          and 'neither that act nor this one is the discharge' in emit
          and 'positivity face\u2019s realized form' in emit)
    print('    %s' % gn)
    if not gn:
        fails.append('G-NOTDISCHARGED/G-FACE/G-AIMMAP')

    print('\n  G-PLACEMENT / G-ADDITIVE (the anchor once; row S1 once through the writer; the keystone line once; each file a true prefix of its blob):')
    fb = blob_of(PP, 'FINDINGS.md') or ''
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    kb = blob_of(PP, KEYREL) or ''
    once_a = fnd.count('<a id="clause-stated"></a>') == 1
    s1 = [ln for ln in norm(led).split('\n') if ln.startswith('| S1 | ')]
    once_k = key.count('<!-- b332 clause-stated cross-reference -->') == 1
    pf = norm(fnd).startswith(norm(fb).rstrip('\n'))
    pk = norm(key).startswith(norm(kb).rstrip('\n'))
    pl = norm(led).startswith(norm(lb).rstrip('\n')) or ('| S1 | ' in lb)
    # ### the ledger writer inserts a row before the cascade section, so the ledger is not a byte prefix of its blob;
    # ### the writer's own append-only check (working and blob) is read from its run file instead.
    fil = io.open(FIL, encoding='utf-8').read()
    wl = 'append-only working=True blob=True' in fil and 'quotations verified 4' in fil
    gp = once_a and len(s1) == 1 and 'STATED' in s1[0] and once_k and pf and pk and wl and rows['prefix_working'] and rows['prefix_blob']
    print('    anchor once %s ; S1 once %s ; keystone mark once %s ; FINDINGS prefix %s ; keystone prefix %s ; ledger writer append-only %s : %s'
          % (once_a, len(s1) == 1, once_k, pf, pk, wl, gp))
    if not gp:
        fails.append('G-PLACEMENT/G-ADDITIVE')

    print('\n  G-ROW / G-ANCESTOR (row 178 carries NO TERMINAL with its reason; the table a true prefix of its blob):')
    r178 = [ln for ln in tbl.split('\n') if ln.startswith('| 178 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r178) == 1 and 'NO TERMINAL, AND THE REASON' in r178[0] and 'HALTS AT K8' in r178[0] and 'M-2' in r178[0] and norm(tbl).startswith(norm(head).rstrip('\n'))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print('\n  G-KEY (one row; the must-not-hit queries NO KEY):')
    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('clause-stated')
    gk = o.count('act      :') == 1 and 'NOT DISCHARGED, NOT WEAKENED, NOT REPLACED' in o
    for s in ('the clause discharged', 'the clause weakened'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY')

    print('\n  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split('\n'), norm(idx).split('\n')) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print('\n  G-NOEDIT (owner files, sealed files, the deposit, TECHNE, every .lean, the keystone\'s body: no tracked change beyond the act\'s three files):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/b327_faces_rows.py',
              'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b328_source_text.txt'] + ['data/' + os.path.basename(S.bank(a)) for a in ('b300', 'b306', 'b310', 'b315', 'b318', 'b320', 'b321', 'b322', 'b326', 'b328', 'b329')]
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x
            and not any(x.strip().endswith(f) for f in ('FINDINGS.md', 'FACES_LEDGER.md', 'THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'))]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the three) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print('\n  G-ORDER (the seal verifies; the generator, the section, the row and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b332_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b332_statement.py'), SRUN, SRUN2, EMIT, FIL, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b332_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b332_checks_run.txt')) else ''
        after = 'the generator, the section, the row and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the generator, the section, the row and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print('\n  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    committed_f = '<a id="clause-stated"></a>' in fb
    if committed_f:
        print('    FINDINGS committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    FINDINGS not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print('\n  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    checks.append(('+%d lines, %d -> %d' % (rows['lines_added'], rows['lines_before'], rows['lines_after']),
                   ('`+%d` lines' % rows['lines_added']) in bank and ('`%d -> %d`' % (rows['lines_before'], rows['lines_after'])) in bank))
    fq = re.search(r'F-QUOTE\s*:\s*(\d+) quotations, (\d+) unfindable', srun)
    checks.append(('F-QUOTE %s/%s' % (fq.group(1), fq.group(2)), ('`F-QUOTE` PASSES AT %s OF %s' % (fq.group(1), fq.group(1))) in bank and fq.group(2) == '0'))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    km = re.search(r'keystone\s+WRITTEN \+(\d+) lines', fil)
    checks.append(('keystone +%s lines' % km.group(1), ('`+%s` lines' % km.group(1)) in bank))
    nsec = len([x for x in fnd.splitlines() if x.startswith('## ')])
    checks.append(('%d sections' % nsec, nsec == 19 and 'nineteenth section' in bank))
    cells = re.search(r'row S1: present 1 time\(s\), (\d+) cells on disk', fil)
    checks.append(('S1 %s cells' % cells.group(1), cells.group(1) == '7' and 'seven cells' in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print('\n  G-ONCE (run files written once per path; the first emission kept; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [SRUN, SRUN2, SRUN3, FIL, FILR, CORR, CORRR, IDX, IDXR, EMIT, ROWSJ])
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s' % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-36s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-STEM-APPENDED (the section, row S1, the keystone line, row 178, the index row, swept):')
    sec = fnd[fnd.index('<a id="clause-stated"></a>'):] if '<a id="clause-stated"></a>' in fnd else ''
    kl = key[key.index('<!-- b332 clause-stated cross-reference -->'):] if '<!-- b332 clause-stated cross-reference -->' in key else ''
    ib = idx[idx.index('# ### THE CLAUSE STATED (b332).'):idx.index('# ### THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD (b331).')] if '# ### THE CLAUSE STATED (b332).' in idx else ''
    for lbl, blk in (('the section', sec), ('row S1', s1[0] if s1 else ''), ('the keystone line', kl), ('row 178', r178[0] if r178 else ''), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk)))
        if ch or sh or not blk:
            fails.append('G-STEM-APPENDED ' + lbl)

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
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

    print('\n  HEDGE AUDIT (over every file this act wrote, the emitted section, the row, the keystone line and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b332_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the emitted section', EMIT), ('the generator', t('b332_statement.py'))]
    for lbl, text in (('row S1', s1[0] if s1 else ''), ('the keystone line', kl), ('row 178', r178[0] if r178 else ''), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline='\n').write(text + '\n')
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-22s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
