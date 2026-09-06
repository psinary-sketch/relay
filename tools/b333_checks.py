# -*- coding: utf-8 -*-
"""b333_checks.py -- THE GATE SUITE FOR THE ARCHIMEDEAN TERM DERIVED.

### ### **THE ARMS THAT CARRY THIS ACT (registration (G), F1-F11):**
###   `G-NORMALIZATIONS` -- the run file states (N1)-(N4) before any number.
###   `G-CHAIN` -- every link (L1)-(L5) a quotation in the extract file or an identity; the verdict word printed.
###   `G-VERDICT` -- the bank's verdict equals the tool's; not DERIVES-ON-IMPORT, so it is the bank's first sentence.
###   `G-ROUTE3` -- the sealed bar at every cell from the banked table; the failure reported FIRST in the run
###     file and in the bank; and the diagnosis: like for like inside the reading bar at every cell, from its record.
###   `G-CONVERGE` -- the third route's two precisions inside a tenth of the bar.
###   `G-RERANK` -- the ranking recomputed live under b332's sealed rule with K5's grades as conferred equals the
###     record; both seats' expectations scored in words; MEASURED-ON-FAMILIES not conferred.
###   `G-LEDGER` -- one block through the writer naming S1 and K5; row S1 byte-identical; the writer's append-only record.
###   `G-ADDENDUM` -- the addendum after the clause-stated section, the section byte-identical, the file a true prefix.
###   `G-NOQUANTIFIER` -- the bank says K8 stays unowned; the must-fail line absent.
###   `G-NOTCONFERRED`, `G-ROW`, `G-KEY`, `G-APPENDONLY`, `G-NOEDIT`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`,
###     `G-ONCE`, `G-TOOLNUM`, the hedge audit, the stem sweep, the must-fail fixtures -- standing.
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
import b333_rerank as RR  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b333_the_archimedean_term_derived.txt')
REG = d('b333_registration_2026-09-06.txt')
EXTRACT, EXTRACT2 = d('b333_extract_notes.txt'), d('b333_extract2_notes.txt')
DRUN, DJ = d('b333_derive_run.txt'), d('b333_derive.json')
GRUN, GJ = d('b333_diagnose_run.txt'), d('b333_diagnose.json')
RRUN, RJ = d('b333_rerank_run.txt'), d('b333_rerank.json')
FIL, FILR = d('b333_filings_run.txt'), d('b333_filings_rerun.txt')
CORR, CORRR = d('b333_corr_run.txt'), d('b333_corr_rerun.txt')
IDX, IDXR = d('b333_index_run.txt'), d('b333_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b333_ferry_scan.txt'), d('b333_reg_termscan.txt'), d('b333_reg_gate.txt')
CENSUS, FCEN = d('b333_census.txt'), d('b333_faces_census.txt')
REGSPEC, SATIS = d('b333_regspec_run.txt'), d('audit_b333_reg_satisfiable.txt')
PINS, INDEXQ, SRC = d('b333_pins_stepzero.txt'), d('audit_b333_index_query.txt'), d('b333_source.txt')
HOOKS, MIRROR = d('b333_hooks.txt'), d('b333_mirror.txt')
SEAL = 'a9bfe95aa345fbb8eb92fcf6346527851ef13487922a8f01b858f83d65bf05fa'
MARK_F = '<!-- b333 addendum: the archimedean term derived -->'
MARK_L = '<!-- b333 update -->'
ANCHOR = '<a id="clause-stated"></a>'

OWNED = [BANK, REG, DRUN, DJ, GRUN, GJ, RRUN, RJ, FIL, FILR, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, SRC,
         t('b333_source.py'), t('b333_extract.py'), t('b333_extract2.py'), t('b333_regspec.py'), t('b333_derive.py'), t('b333_diagnose.py'),
         t('b333_rerank.py'), t('b333_filings.py'), t('b333_correspondence.py'), t('b333_index_append.py')]

CARRIERS = [
    (t('b333_checks.py'), 'its own fixtures'),
    (d('b333_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"), (EXTRACT2, "the second extract file, likewise"),
]

OWNER_NEEDLES = [
    # ### the source, at its text layer
    ('source -- (150) the principal value', d('b328_source_text.txt'), 'WRpfq :\u201cp log 4\u03c0`\u03b3qfp1q`'),
    ('source -- (151) the Gamma form', d('b328_source_text.txt'), 'WRpfq\u201cp log\u03c0qfp1q\u00b4 1'),
    ('source -- (153) h_+', d('b328_source_text.txt'), 'h`p\u03c4q\u201c\u00b4 log\u03c0` \u211cp\u03bbp1{4`i\u03c4{2qq, \u03bb pzq\u201c \u03931pzq{\u0393pzq. (153)'),
    ('source -- W_R = -W_inf', d('b328_source_text.txt'), 'namely the equality for the local term ( WR\u201c\u00b4W8)'),
    ('source -- a principal value', d('b328_source_text.txt'), 'The distribution WR is then de\ufb01ned as a principal value.'),
    # ### the corpus's conventions and routes
    ('atlas -- the channel', t('e16/carto_atlas.py'), 'A = float(np.trapezoid(hhat(v, w, U) * kernel(U), U) / (2.0 * math.pi))'),
    ('atlas -- the sign', t('e16/carto_atlas.py'), 'sum_gamma hhat(gamma)  =  hhat(i/2) + hhat(-i/2)  -  PRIME  +  ARCH'),
    ('b318 -- f-hat', t('b318_square.py'), '`f-hat(t) = INT f(rho) rho^{-it} d*rho = INT w(v) e^{-itv} dv`'),
    ('b320 -- the table at a = 1.3', d('b320_the_lawful_function.txt'), '1.3    YES       8.781214000        8.781179663        3.434e-05'),
    ('b320 -- the worst difference', d('b320_the_lawful_function.txt'), 'WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS : 3.434e-05.'),
    ('b315 -- the term defined', d('b315_the_calibration_and_the_rate.txt'), 'THE CALIBRATION FIXES A SIGN ONLY, AND THE ARCHIMEDEAN TERM IS DEFINED'),
    ('b315 -- where A goes', d('b315_the_calibration_and_the_rate.txt'), 'IT DOES NOT SCALE `A`. ### IT DOES NOT SET `A`. ### IT CHOOSES WHERE `A` GOE'),
    ('b326 -- the derived Epstein kernel', t('b326_windows.py'), '`2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt23)`'),
    ('b332 -- the sealed rule', d('b332_registration_2026-09-06.txt'), "constituent's rank is its softest grade among its owners, ordered"),
    # ### the diagnosis's quotations (the second extract)
    ("b320_corroborate -- the function the table was made for", t('b320_corroborate.py'), 'g = SM.mean_zero_variant(a)'),
    ('### its autocorrelation', t('b320_corroborate.py'), 'f = SQ.autocorrelation(g)'),
    ('b320 bank -- the autocorrelation', d('b320_the_lawful_function.txt'), 'product is the autocorrelation `f(v) = INT g(u) g(u-v) du`'),
    ('b320 bank -- the sign certified, the size not', d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ("atlas bank -- the bump's channel at a = 1.3", d('carto_atlas.jsonl'), '"a": 1.3, "zero": 0.2065114708720861, "pole": 2.002722246159938, "arch": -1.7962126389496489'),
    ('registration (E) -- on the bump', REG, "precision, on the bump re-implemented from the atlas's definition"),
    ("registration (E) -- b320's table", REG, "banked values read from b320's table."),
    ('registration (E) -- 0.5 to 8.8', REG, 'magnitude at every cell (the values run from `0.5` to `8.8`).'),
    ('registration -- reported first', REG, 'A DISAGREEMENT IS REPORTED AT FULL PROMINENCE, FIRST.'),
    ('derive run -- the verdict as printed', DRUN, 'VERDICT : MISMATCH at (L3)'),
]

SELF_NEEDLES = [
    ('### the verdict first', BANK, "THE DERIVATION TOOL'S VERDICT, AS PRINTED, FIRST:"),
    ('### the differing constituent is the sealed bar', BANK, 'THE DIFFERING CONSTITUENT, QUOTED -- AND IT IS THIS ACT\'S OWN SEALED BAR, NOT THE RECORD.'),
    ('### the record untouched', BANK, "THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED."),
    ('### the sealed bar not met, not rewritten', BANK, 'THE SEALED BAR, AS SEALED, IS NOT MET AND IS NOT REWRITTEN.'),
    ('### families not conferred', BANK, '`MEASURED-ON-FAMILIES` IS NOT CONFERRED on K5 by this act.'),
    ('bank states the answers', BANK, 'THE ANSWERS.'),
    ('### the chain derives on import', BANK, 'THE CHAIN DERIVES ON IMPORT.'),
    ('### the hazard one identity', BANK, 'THE FACTOR-OF-TWO HAZARD IS ONE IDENTITY.'),
    ("### the bump's value", BANK, "THE THIRD ROUTE'S VALUE FOR THE BUMP IS THE CORPUS'S VALUE FOR THE BUMP."),
    ('### the re-rank', BANK, 'THE RE-RANK UNDER THE SEALED RULE, NOTHING ADJUSTED: K5 AND K6 TIE AT THE SOFTEST RANK.'),
    ("### the navigator's expectation not stated", BANK, "THE NAVIGATOR'S EXPECTATION FOR THE NEW SOFTEST: NOT STATED IN THE ORDER -- recorded, not scored."),
    ("### the seat's expectation met", BANK, "THIS SEAT'S REGISTERED EXPECTATION FOR THE NEW SOFTEST (K5 AND K6 TIED): MET."),
    ("### the seat's route expectation not met", BANK, "THIS SEAT'S REGISTERED EXPECTATION FOR THE THIRD ROUTE (INSIDE THE BAR AT EVERY CELL): NOT MET."),
    ('### the aim-map named', BANK, 'THE AIM-MAP IS NAMED AS NEXT, ITS TARGET THE NEW SOFTEST PAIR; NEITHER IT NOR THIS ACT IS THE DISCHARGE.'),
    ('### K8 unowned', BANK, 'K8 STAYS UNOWNED.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE CLASSICAL TERM, AS THE SOURCE STATES IT, UNDER THE CORPUS\'S CONVENTIONS.'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE THIRD ROUTE, THE SEALED BAR, AND THE DIAGNOSIS.'),
    ('### what agreement buys', BANK, 'WHAT THE AGREEMENT BUYS AND DOES NOT BUY.'),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- THE RE-RANK AND THE FILINGS.'),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- WHAT THIS ACT DOES AND DOES NOT SAY.'),
    ('### not the bar met', BANK, 'IT DOES NOT SAY THE SEALED BAR WAS MET.'),
    ('### not the size', BANK, 'IT DOES NOT SAY THE SIZE OF THE ARCHIMEDEAN TERM IS CERTIFIED.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1', BANK, 'E1 -- THE SEALED BAR PAIRED THE BUMP WITH A TABLE MADE FOR ANOTHER FUNCTION.'),
    ('### E2', BANK, "E2 -- THE DERIVATION TOOL'S RE-RANK CONFERRED A GRADE AHEAD OF ITS VERDICT."),
    ('### E3', BANK, "E3 -- THE DERIVATION TOOL'S (152) EVALUATION WAS UNDER-RESOLVED."),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE AIM-MAP, ITS TARGET THE PAIR K5 AND K6 -- AND IT IS NOT THE DISCHARGE.'),
    ('registration -- the bar', REG, "`|A_3 - A_digamma(b320)| <= 2e-4` and `|A_3 - W_inf,(38)(b320)| <= 2e-4`, the"),
    ('registration -- the seat expects the tie', REG, 'SO K5 AND K6 TIE AT THE SOFTEST RANK'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('diagnose run -- the finding', GRUN, 'THE CORPUS\'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED. THE SEALED BAR, AS WRITTEN, IS NOT MET AND IS NOT REWRITTEN.'),
    ('rerank run -- not conferred', RRUN, 'K5 GRADE NOT CONFERRED'),
]

MUST_FAIL = [
    ('the bank never says the sealed bar is met', BANK, '### ### **THE SEALED BAR IS MET.**'),
    ('the bank never says the size is certified', BANK, '### ### **THE SIZE OF THE ARCHIMEDEAN TERM IS CERTIFIED.**'),
    ('the bank never says the clause moved', BANK, '### ### **THE CLAUSE HAS MOVED.**'),
    ('the bank never says K8 is owned', BANK, '### ### **K8 IS OWNED.**'),
    ('the bank never confers the measurement grade', BANK, '### ### **MEASURED-ON-FAMILIES IS CONFERRED ON K5.**'),
    ('the bank never says the record is wrong', BANK, "### ### **THE RECORD'S ARCHIMEDEAN NUMBERS ARE WRONG.**"),
]

TOOLNUM = [
    ('the chain, 18 quotations, the identities, A_3 and W_R per cell, the sealed bar FAIL', 'tools/b333_derive.py'),
    ('the like-for-like worsts (A)-(E)', 'tools/b333_diagnose.py'),
    ('the ranking, the tie, the expectations', 'tools/b333_rerank.py'),
    ('+18 lines, 3098 -> 3116, the ledger block', 'tools/b333_filings.py'),
    ('row 179', 'tools/b333_correspondence.py'),
    ('the key', 'tools/b333_index_append.py'),
    ('21 clauses', 'tools/b333_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('16927 bytes sealed', 'tools/reg_seal.py'),
    ('five copies matched, the text layer pinned', 'tools/b333_source.py'),
    ('the extract zeros', 'tools/b333_extract.py'),
    ('the second extract zeros', 'tools/b333_extract2.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the ledger writer', 'tools/b327_faces_row.py'),
    ('3.434e-05, the table', 'tools/b320_corroborate.py'),
    ('the banked arch', 'tools/e16/carto_atlas.py'),
]
NEW_THIS_ACT = {'tools/b333_derive.py', 'tools/b333_diagnose.py', 'tools/b333_rerank.py', 'tools/b333_filings.py', 'tools/b333_correspondence.py',
                'tools/b333_index_append.py', 'tools/b333_regspec.py', 'tools/b333_source.py', 'tools/b333_extract.py', 'tools/b333_extract2.py'}


def git(repo, *args):
    return subprocess.run(['git', '-C', repo] + list(args), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def subsequence(old_lines, new_lines):
    i = 0
    for ln in new_lines:
        if i < len(old_lines) and ln == old_lines[i]:
            i += 1
    return i == len(old_lines)


def first_sentence(bank_text):
    """the first line of the bank after its header block (the second rule of '=')."""
    lines = bank_text.split(chr(10))
    rules = [i for i, ln in enumerate(lines) if ln.startswith('=' * 100)]
    for ln in lines[rules[1] + 1:]:
        if ln.strip():
            return ln
    return ''


def main():
    fails = []
    print('=' * 100)
    print('b333 -- GATE SUITE (THE ARCHIMEDEAN TERM DERIVED: A DERIVATION UNDER THE IMPORT BAR; THE SEALED BAR NOT MET, DIAGNOSED)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read() + io.open(EXTRACT2, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN AN EXTRACT FILE):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            inx = anchor in extract
            not_extracted += 0 if inx else 1
            print('    %s  %s%s' % ('PASS' if inx else '### FAIL', lbl, '' if inx else '  -- NOT IN THE EXTRACT FILES'))
            if not inx:
                fails.append('G-EXTRACT: ' + lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))
    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    drun = io.open(DRUN, encoding='utf-8').read()
    dj = json.load(io.open(DJ, encoding='utf-8'))
    gj = json.load(io.open(GJ, encoding='utf-8'))
    rj = json.load(io.open(RJ, encoding='utf-8'))
    fnd = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    fil = io.open(FIL, encoding='utf-8').read()
    dl = drun.split(chr(10))

    print(chr(10) + '  G-NORMALIZATIONS (F1: (N1)-(N4) stated in the run file before any number):')
    ni = [next((i for i, ln in enumerate(dl) if ln.strip().startswith('(N%d)' % k)), -1) for k in (1, 2, 3, 4)]
    first_num = next((i for i, ln in enumerate(dl) if re.match(r'\s+a = [\d.]+\s+W_R\(150\)', ln)), -1)
    gnorm = all(i >= 0 for i in ni) and first_num > max(ni)
    print('    (N1)-(N4) at lines %s ; first value at line %d : %s' % ([i + 1 for i in ni], first_num + 1, gnorm))
    if not gnorm:
        fails.append('G-NORMALIZATIONS')

    print(chr(10) + '  G-CHAIN (F2: every link a quotation in the extract file or an identity; the verdict word printed):')
    links = {}
    for k in (1, 2, 3, 4, 5):
        ln = next((x for x in dl if x.strip().startswith('(L%d)' % k) and 'quotations' in x), '')
        m = re.search(r'quotations (\d+)/(\d+) in the extract file', ln)
        links[k] = bool(m) and m.group(1) == m.group(2)
    gchain = all(links.values()) and 'VERDICT (chain) : DERIVES-ON-IMPORT' in drun and dj['chain'] is not None
    print('    links located %s ; chain verdict printed %s : %s' % (links, 'VERDICT (chain) : DERIVES-ON-IMPORT' in drun, gchain))
    if not gchain:
        fails.append('G-CHAIN')

    print(chr(10) + '  G-VERDICT (F3: the bank\'s verdict equals the tool\'s; not DERIVES-ON-IMPORT, so it is the first sentence):')
    fs = first_sentence(bank)
    gv = dj['verdict'] in fs and ('VERDICT : ' + dj['verdict']) in drun and dj['verdict'].startswith('MISMATCH')
    print('    tool verdict %r ; in the bank\'s first sentence %s : %s' % (dj['verdict'], dj['verdict'] in fs, gv))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-ROUTE3 (F4: the sealed bar from the banked table at every cell; the failure reported FIRST; the diagnosis like for like):')
    i_fail = next((i for i, ln in enumerate(dl) if 'REPORTED FIRST, AT FULL PROMINENCE' in ln), -1)
    i_verd = next((i for i, ln in enumerate(dl) if ln.strip().startswith('### VERDICT :')), -1)
    nfail = sum(1 for ln in dl if '### FAIL ###' in ln and re.match(r'\s+[\d.]+\s+-', ln))
    gr3 = (not dj['route_ok']) and nfail == 13 and 0 <= i_fail < i_verd and 'MISMATCH' in fs
    gdiag = gj['A_ok'] and gj['B_ok'] and len(gj['cells']) == 13 and gj['A_worst']['atlas'] <= gj['reading_bar'] and gj['B_worst']['w38'] <= gj['reading_bar']
    print('    sealed bar failed at %d cells ; the failure line %d before the verdict line %d ; bank first sentence carries it : %s' % (nfail, i_fail + 1, i_verd + 1, gr3))
    print('    diagnosis: A_ok %s B_ok %s ; worst atlas %.3e dig %.3e w38 %.3e ; b320 function %.3e / %.3e : %s'
          % (gj['A_ok'], gj['B_ok'], gj['A_worst']['atlas'], gj['A_worst']['dig'], gj['A_worst']['w38'], gj['B_worst']['dig'], gj['B_worst']['w38'], gdiag))
    if not (gr3 and gdiag):
        fails.append('G-ROUTE3')

    print(chr(10) + '  G-CONVERGE (F5: the two precisions inside a tenth of the bar):')
    gc = dj['worst']['conv'] <= 2e-5
    print('    worst |A_3(30) - A_3(50)| = %.3e : %s' % (dj['worst']['conv'], gc))
    if not gc:
        fails.append('G-CONVERGE')

    print(chr(10) + '  G-RERANK (F6: the ranking recomputed live under b332\'s rule with K5 as conferred equals the record; expectations scored; families not conferred):')
    conferred = [tuple(g) for g in rj['k5_grades'] if g[1] == 'b333']
    ranking, softest, k5 = RR.run_rule(conferred)
    same = [(r[1], r[3]) for r in ranking] == [(r[1], r[3]) for r in rj['ranking']] and softest == rj['softest']
    nofam = all(g[0] != 'MEASURED-ON-FAMILIES' for g in rj['k5_grades'])
    grr = (same and sorted(softest) == ['K5', 'K6'] and rj['seat_expectation'] == 'MET' and nofam and rj['ranking_with_families_identical']
           and 'NOT STATED IN THE ORDER' in bank and '(K5 AND K6 TIED): MET.' in bank)
    print('    recomputed == record %s ; softest %s ; seat %s ; families not conferred %s : %s' % (same, softest, rj['seat_expectation'], nofam, grr))
    if not grr:
        fails.append('G-RERANK')

    print(chr(10) + '  G-LEDGER (F7: one block through the writer naming S1 and K5; row S1 byte-identical; append-only per the writer):')
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    s1w = [ln for ln in norm(led).split(chr(10)) if ln.startswith('| S1 | ')]
    s1b = [ln for ln in norm(lb).split(chr(10)) if ln.startswith('| S1 | ')]
    blk = led[led.index(MARK_L):] if MARK_L in led else ''
    gl = (led.count(MARK_L) == 1 and s1w == s1b and len(s1w) == 1 and '**S1**, constituent **K5**' in blk and 'append-only working=True blob=True' in fil
          and 'MEASURED-ON-FAMILIES is NOT conferred' in blk)
    print('    mark once %s ; S1 identical %s ; block names S1/K5 %s ; writer append-only %s : %s' % (led.count(MARK_L) == 1, s1w == s1b, '**S1**, constituent **K5**' in blk, 'append-only working=True blob=True' in fil, gl))
    if not gl:
        fails.append('G-LEDGER')

    print(chr(10) + '  G-ADDENDUM (F8: after the clause-stated section, the section byte-identical, the file a true prefix of its blob):')
    fb = blob_of(PP, 'FINDINGS.md') or ''
    sec_b = norm(fb)[norm(fb).index(ANCHOR):].rstrip(chr(10)) if ANCHOR in fb else None
    sec_w = norm(fnd)[norm(fnd).index(ANCHOR):norm(fnd).index(MARK_F)].rstrip(chr(10)) if (ANCHOR in fnd and MARK_F in fnd) else None
    committed_add = MARK_F in fb
    pf = norm(fnd).startswith(norm(fb).rstrip(chr(10)))
    ga = fnd.count(MARK_F) == 1 and fnd.count(ANCHOR) == 1 and pf and (committed_add or sec_b == sec_w) and fnd.index(ANCHOR) < fnd.index(MARK_F)
    addm = fnd[fnd.index(MARK_F):] if MARK_F in fnd else ''
    ga = ga and dj['verdict'] in addm.split('**The derivation tool')[1][:400] if '**The derivation tool' in addm else False
    print('    mark once %s ; anchor once %s ; prefix of blob %s ; section identical %s (addendum committed: %s) ; verdict first in the addendum : %s' % (fnd.count(MARK_F) == 1, fnd.count(ANCHOR) == 1, pf, sec_b == sec_w, committed_add, ga))
    if not ga:
        fails.append('G-ADDENDUM')

    print(chr(10) + '  G-NOQUANTIFIER (F9):')
    gq = 'K8 STAYS UNOWNED.' in bank and needle_pull.absent_exact(BANK, '### ### **K8 IS OWNED.**') and 'K8, the quantifiers, stays unowned' in addm
    print('    %s' % gq)
    if not gq:
        fails.append('G-NOQUANTIFIER')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row 179 carries the verdict as printed first, NO TERMINAL with its reason, M-2; the table a true prefix of its blob):')
    r179 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 179 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = (len(r179) == 1 and 'NO TERMINAL, AND THE REASON' in r179[0] and 'VERDICT, AS PRINTED, FIRST' in r179[0] and dj['verdict'] in r179[0]
           and 'M-2' in r179[0] and 'MEASURED-ON-FAMILIES NOT' in r179[0] and norm(tbl).startswith(norm(head).rstrip(chr(10))))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCONFERRED (one row; the must-not-hit queries NO KEY; the answer confers no grade beyond the derivation\'s):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('archimedean-term-derived')
    gk = (o.count('act      :') == 1 and "NO GRADE CONFERRED BEYOND THE DERIVATION'S OWN" in o and 'ROUTES AGREEING CERTIFY THAT THE ROUTES AGREE' in o
          and 'VERDICT, AS PRINTED, FIRST' in o and 'NOT MET and not rewritten' in o)
    for s in ('the size certified', 'the clause moved', 'the sealed bar met'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTCONFERRED')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (owner files, sealed files, the deposit, TECHNE, every .lean, the derivation tool after its run: no tracked change beyond the act\'s files):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/b327_faces_rows.py',
              'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/b332_statement.py',
              'tools/b320_corroborate.py', 'tools/b320_weil.py', 'tools/b317_smear.py', 'tools/b318_square.py', 'tools/e16/carto_atlas.py', 'data/carto_atlas.jsonl',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b328_source_text.txt', 'data/b320_the_lawful_function.txt', 'data/b332_the_clause_stated.txt',
              'data/b332_registration_2026-09-06.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x
            and not any(x.strip().endswith(f) for f in ('FINDINGS.md', 'FACES_LEDGER.md'))]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    derive_committed = blob_of(ROOT, 'tools/b333_derive.py')
    derive_same = True if derive_committed is None else norm(derive_committed) == norm(io.open(t('b333_derive.py'), encoding='utf-8').read())
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep and derive_same
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the two) %s ; TECHNE %r ; deposit %r ; derive tool unedited %s : %s' % (st_r, st_s, st_p, st_t, dep, derive_same, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the tools, the runs, the filings and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b333_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b333_derive.py'), DRUN, DJ, GRUN, RRUN, FIL, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b333_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b333_checks_run.txt')) else ''
        after = 'the tools, the runs, the filings and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the tools, the runs, the filings and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed_add:
        print('    FINDINGS committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    FINDINGS not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    fm = re.search(r'FINDINGS\.md\s+WRITTEN \+(\d+) lines', fil)
    checks.append(('+%s lines' % fm.group(1), ('`+%s` lines' % fm.group(1)) in bank))
    nb, na = len(norm(fb).rstrip(chr(10)).split(chr(10))), len(norm(fnd).rstrip(chr(10)).split(chr(10)))
    if committed_add:
        nb = na - int(fm.group(1))
    checks.append(('%d -> %d' % (nb, na), ('`%d -> %d`' % (nb, na)) in bank))
    for lbl, v in (('A worst atlas', gj['A_worst']['atlas']), ('A worst dig', gj['A_worst']['dig']), ('A worst w38', gj['A_worst']['w38']),
                   ('B worst dig', gj['B_worst']['dig']), ('B worst w38', gj['B_worst']['w38']), ('C worst', gj['C_worst']),
                   ('D derive', gj['D_worst']['deriv']), ('D resolved', gj['D_worst']['resolved'])):
        checks.append((lbl + ' %.3e' % v, ('`%.3e`' % v) in bank))
    c13 = dj['cells']['1.3']
    checks.append(('A_3 at 1.3 %.9f' % c13['A3'], ('`%.9f`' % c13['A3']) in bank))
    checks.append(('A_3 at 3 %.9f' % dj['cells']['3.0']['A3'], ('`%.9f`' % dj['cells']['3.0']['A3']) in bank))
    checks.append(('d_dig at 1.3 %.3e' % abs(c13['A3'] - c13['A_dig_b320']), ('`d_dig %.3e`' % abs(c13['A3'] - c13['A_dig_b320'])) in bank))
    checks.append(('conv %.3e' % dj['worst']['conv'], ('`%.3e`' % dj['worst']['conv']) in bank))
    g13 = gj['cells']['1.3']
    checks.append(('the four routes at 1.3', all(('`%.9f`' % g13[k]) in bank for k in ('A3', 'atlas_arch', 'dig_on_bump', 'w38_on_bump'))))
    idw = max(float(x) for x in re.findall(r'h_\+\(tau\)\| = ([\d.e+-]+)', drun) + re.findall(r'kernel_b326\| = ([\d.e+-]+)', drun))
    checks.append(('identities worst %.3e' % idw, ('`%.3e`' % idw) in bank))
    nq = sum(int(m.group(1)) for m in re.finditer(r'quotations (\d+)/\d+ in the extract file', drun))
    checks.append(('%d quotations' % nq, nq == 18 and 'Eighteen quotations' in bank))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    cp = re.search(r'local copies matching the pin, re-hashed now : (\d+)', io.open(SRC, encoding='utf-8').read()).group(1)
    checks.append(('%s copies matched' % cp, cp == '5' and 'five local copies' in bank))
    nsec = len([x for x in fnd.splitlines() if x.startswith('## ')])
    checks.append(('%d sections' % nsec, nsec == 19 and 'still nineteen sections' in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded; the diagnostic\'s single record):')
    once_ok = all(os.path.exists(p) for p in [DRUN, DJ, GRUN, GJ, RRUN, RJ, FIL, FILR, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b333_diagnose_run2.txt'))
    print('    %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):' % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
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

    print(chr(10) + '  G-STEM-APPENDED (the addendum, the ledger block, row 179, the index row, swept):')
    ib = idx[idx.index('# ### THE ARCHIMEDEAN TERM DERIVED (b333).'):idx.index('# ### THE CLAUSE STATED (b332).')] if '# ### THE ARCHIMEDEAN TERM DERIVED (b333).' in idx else ''
    for lbl, blk2 in (('the addendum', addm), ('the ledger block', blk), ('row 179', r179[0] if r179 else ''), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    extra = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print(chr(10) + '  G-TOOLNUM:')
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the addendum, the ledger block, the row and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b333_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('the addendum', addm), ('the ledger block', blk), ('row 179', r179[0] if r179 else ''), ('the index row', ib)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, gh, ua = hedge_audit.audit(path)
        print('    %-36s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(gh), len(ua)))
        for s2 in gh:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d ; owner needles not in the extract files : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
