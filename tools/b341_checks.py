# -*- coding: utf-8 -*-
"""b341_checks.py -- THE GATE SUITE FOR THE TWO COEFFICIENTS (LEG 3 OF THE SORTIE b339-b343: A TRANSCRIPTION FILED).

### ### **THE ARMS (registration (F), F1-F8):** `G-EMITTERS` (both prior wordings through the extract; the owner files byte-identical
### to their blobs), `G-ROUTES` (the two routes recomputed live agree within the sealed bar), `G-LOCATE` (each source's status,
### bytes, sha256; the located string at its line in the banked text; no PDF in any repo), `G-DECIDE` (the verdict by the sealed
### rule from the record), `G-ERRATUM` (one block under the mark, the id, the prior wordings inside, the file a true prefix of
### its blob, the partition block byte-identical), `G-NOEDIT`, `G-ROW` / `G-ANCESTOR`, `G-KEY` / `G-NOTAMEASUREMENT`,
### `G-APPENDONLY`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, the struck-clause and stem sweeps,
### `G-SHARED`, the hedge audit, the must-fail fixtures; re-run after the push.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import tempfile

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402
import b341_coefficients as CO  # noqa: E402  ### route (B), re-run live

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
ERRATA = os.path.join(PP, 'ERRATA.md')
KEY = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
BENCH = os.path.join(PP, 'internal', 'bench', 'li_bench.py')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b341_the_two_coefficients.txt')
REG = d('b341_registration_2026-09-06.txt')
EXTRACT = d('b341_extract_notes.txt')
LRUNS = [d('b341_locate_run.txt'), d('b341_locate_run2.txt'), d('b341_locate_run3.txt')]
LJ = d('b341_locate.json')
CRUNS = [d('b341_coefficients_run.txt'), d('b341_coefficients_run2.txt')]
CJ = d('b341_coefficients.json')
ERUN, ERR2 = d('b341_errata_run.txt'), d('b341_errata_rerun.txt')
CORR, CORRR = d('b341_corr_run.txt'), d('b341_corr_rerun.txt')
IDX, IDXR = d('b341_index_run.txt'), d('b341_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b341_ferry_scan.txt'), d('b341_reg_termscan.txt'), d('b341_reg_gate.txt')
CENSUS, FCEN = d('b341_census.txt'), d('b341_faces_census.txt')
REGSPEC, SATIS = d('b341_regspec_run.txt'), d('audit_b341_reg_satisfiable.txt')
PINS, INDEXQ = d('b341_pins_stepzero.txt'), d('audit_b341_index_query.txt')
HOOKS, MIRROR = d('b341_hooks.txt'), d('b341_mirror.txt')
TEXTS = [d('b341_source_text_keiper1992.txt'), d('b341_source_text_maslanka0406312.txt'), d('b341_source_text_coffey0505052.txt')]
SEAL = '54e2391094a123830a4ce1e1893c575de012ba28c71cb1e94f79335fc22dd840'
MARK = '<!-- b341 -->'
EID = 'E-2026-09-06-1'
ROWNUM = '189'

OWNED = [BANK, REG] + LRUNS + [LJ] + CRUNS + [CJ, ERUN, ERR2, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b341_satisfiable.json'),
         t('b341_extract.py'), t('b341_regspec.py'), t('b341_locate.py'), t('b341_coefficients.py'), t('b341_errata.py'), t('b341_correspondence.py'), t('b341_index_append.py')]

CARRIERS = [
    (t('b341_checks.py'), 'its own fixtures'),
    (d('b341_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
] + [(p, "a source's extracted text, not this act's writing") for p in TEXTS]

OWNER_NEEDLES = [
    ("the bench -- the KEIPER dictionary", BENCH, "KEIPER = {1: '0.0230957089662', 2: '0.0923457352914', 3: '0.2077580993', 4: '0.3687904', 5: '0.5747345'}"),
    ('### the bench is an instrument', BENCH, 'BENCH INSTRUMENT (not an argument)'),
    ('the keystone -- n = 3', KEY, '| 3 | 0.20763892055432 | 0.20763892059268 | 3.8e-11 |'),
    ('### n = 5', KEY, '| 5 | 0.57554271446118 | 0.57554271443 | 3.1e-11 |'),
    ("### the residuals track the literature's digits", KEY, '(The residuals track the digits of the *literature* constants quoted, not the computation.)'),
    ("b327 -- the finding", d('b327_the_faces_ledger.txt'), '### ### **AND ONE INCIDENTAL FINDING, FILED NOT EDITED:** ### the bench\'s own `KEIPER` dict reads'),
    ('### a typed fixture, the owner not edited', d('b327_the_faces_ledger.txt'), "### keystone's column and not the dict. ### A typed fixture in an owner instrument; the owner is not"),
    ("the source -- Keiper's coefficients", d('b327_source_text.txt'), 'computations futher below. Keiper\u2019s coe\ufb03cients equal 1'),
    ('### reference [34]', d('b327_source_text.txt'), '[34] J. Keiper, Power series expansions of Riemann\u2019s \u03be-function, Math. Comp. 58 (1992),'),
    ('ERRATA -- the partition ruling', ERRATA, '**THE RULING, AS RATIFIED:** *"ERRATA is partitioned into a deposit-facing section and an internal-record section by an append-only header line, entries unmoved."* **This block is that header line.**'),
    ('### the convention entry\'s heading', ERRATA, '## E-2026-09-03-1 \u2014 The archimedean remainder\'s normalization convention is the corpus\'s own, not the source\'s (INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)'),
    ('### prior wordings retained in place', ERRATA, '### **Prior wordings are quoted above and retained in place at each site** \u2014 the record does not silently overwrite itself.'),
    ('the sortie -- leg 3', d('b341_ferry_2026-09-06.txt'), 'LEG 3 (b341) \u2014 THE TWO COEFFICIENTS: the Li bench\'s literature'),
    ('### owner files untouched', d('b341_ferry_2026-09-06.txt'), 'deposit-facing per the partition) with the owner files untouched.'),
    ('### the bench carries the defect', d('b341_ferry_2026-09-06.txt'), 'bench carries the defect. h2 where the deposit left it; nothing'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) the verdict', BANK, 'THE VERDICT BY THE SEALED RULE: THE BENCH CARRIES THE DEFECT at n = [3, 5].'),
    ('### (2) the literature', BANK, 'THE LITERATURE UNDER THE IMPORT BAR**'),
    ('### located and agrees', BANK, 'LOCATED, AND IT AGREES WITH THE'),
    ('### no located source agrees with the dictionary', BANK, 'NO LOCATED SOURCE AGREES WITH THE'),
    ('### (3) the erratum', BANK, 'THE ERRATUM, FILED PER THE PARTITION:'),
    ('### no owner file edited', BANK, 'NO OWNER FILE IS'),
    ('### (4) the name is not the provenance', BANK, "THE DICTIONARY'S NAME IS NOT ITS PROVENANCE."),
    ('### (5) L3 met', BANK, "THE NAVIGATOR'S (L3) -- *the bench carries the defect* --"),
    ('### no measurement changes', BANK, 'NO BENCH MEASUREMENT CHANGES. NO DEPOSITED ARTIFACT IS AFFECTED. NO GRADE MOVED. NO ACT RE-VERDICTED.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the instruments', BANK, 'THE INSTRUMENTS AND THEIR JUDGEMENT.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED:"),
    ('bank gives the row and the key', BANK, 'THE ROW AND THE KEY.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE SORTIE: LEG 4, b342, THE TWO RULES AS MODULES.'),
    ('registration -- sealed before any fetch', REG, 'SEALED BEFORE ANY SOURCE IS FETCHED, BEFORE ANY COEFFICIENT IS RECOMPUTED, AND BEFORE ANY LINE'),
    ('registration -- the rule', REG, '**THE RULE, FIXED HERE:**'),
    ('registration -- LOCATED defined', REG, '**LOCATED means:**'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the record run -- the verdict', CRUNS[-1], 'VERDICT BY THE SEALED RULE : THE BENCH CARRIES THE DEFECT at n = [3, 5].'),
    ('the record run -- no owner file edited', CRUNS[-1], 'NO OWNER FILE EDITED ; the dictionary enters no computation ; no grade moved.'),
    ('the locate record -- Keiper located', LRUNS[-1], "n = 3 : LOCATED at line 367 -- '6.92129735181082679304' agrees with the keystone's value under keiper"),
    ('the errata run -- written', ERUN, 'status WRITTEN ; mark on disk 1 time(s) ; append-only against the working file True ; against the blob True ; the partition block unchanged True'),
    ('the errata rerun -- duplicate', ERR2, 'status DUPLICATE ; mark on disk 1 time(s)'),
]

MUST_FAIL = [
    ('the bank never says a bench measurement changed', BANK, '### ### **A BENCH MEASUREMENT CHANGED.**'),
    ('the bank never says a deposited artifact is affected', BANK, '### ### **A DEPOSITED ARTIFACT IS AFFECTED.**'),
    ('the bank never says an owner file was edited', BANK, '### ### **AN OWNER FILE WAS EDITED.**'),
    ('the bank never says the keystone carries the defect', BANK, '### ### **THE KEYSTONE CARRIES THE DEFECT.**'),
    ('the bank never says the dictionary is Keiper', BANK, "### ### **THE DICTIONARY IS KEIPER'S TABLE.**"),
]

TOOLNUM = [
    ('the fetches, the hashes, the located strings and their lines', 'tools/b341_locate.py'),
    ('the two routes, the offsets, the verdict', 'tools/b341_coefficients.py'),
    ('the entry, its line counts', 'tools/b341_errata.py'),
    ('row 189', 'tools/b341_correspondence.py'),
    ('the key', 'tools/b341_index_append.py'),
    ('26 clauses', 'tools/b341_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('14186 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b341_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the bench loader', 'tools/b327_bridge.py'),
]
NEW_THIS_ACT = {'tools/b341_locate.py', 'tools/b341_coefficients.py', 'tools/b341_errata.py', 'tools/b341_correspondence.py', 'tools/b341_index_append.py',
                'tools/b341_regspec.py', 'tools/b341_extract.py', 'tools/b341_checks.py'}


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


def main():
    fails = []
    print('=' * 100)
    print('b341 -- GATE SUITE (THE TWO COEFFICIENTS: THE BENCH CARRIES THE DEFECT, FILED AS AN INTERNAL-RECORD ERRATUM, THE OWNER FILES UNTOUCHED)')
    print('=' * 100)
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    unpullable, not_extracted = 0, 0
    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
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
    C = json.load(io.open(CJ, encoding='utf-8'))
    L = json.load(io.open(LJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    err = io.open(ERRATA, encoding='utf-8', errors='replace').read()
    eb = blob_of(PP, 'ERRATA.md') or ''
    committed = MARK in eb

    print(chr(10) + '  G-EMITTERS (F1: both prior wordings in the extract file at their lines; the bench and the keystone byte-identical to their blobs):')
    kb = blob_of(PP, 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md') or ''
    bb = blob_of(PP, 'internal/bench/li_bench.py') or ''
    ge = ("3: '0.2077580993'" in extract and '| 3 | 0.20763892055432 | 0.20763892059268 |' in extract and norm(io.open(KEY, encoding='utf-8').read()) == norm(kb)
          and norm(io.open(BENCH, encoding='utf-8').read()) == norm(bb) and C['bench_line'] == 77 and C['keystone_rows']['3']['line'] == 291 and C['keystone_rows']['5']['line'] == 293)
    print('    %s (the dictionary at line %d; the keystone rows at lines %s, %s)' % (ge, C['bench_line'], C['keystone_rows']['3']['line'], C['keystone_rows']['5']['line']))
    if not ge:
        fails.append('G-EMITTERS')

    print(chr(10) + '  G-ROUTES (F2: route (B) re-run live against the record; the record\'s routes agree within 1e-12 at n = 1..5):')
    B = CO.route_b(5)
    with mp.workdps(40):
        live = max(abs(B[n] - mp.mpf(C['table'][str(n)]['B'])) for n in range(1, 6))
        gr = C['routes_ok'] and live < mp.mpf('1e-20') and all(mp.mpf(C['table'][str(n)]['dAB']) <= mp.mpf('1e-12') for n in range(1, 6))
    print('    route (B) live against the record : %s ; the record\'s |A - B| within 1e-12 at every n : %s : %s' % (mp.nstr(live, 3), C['routes_ok'], gr))
    if not gr:
        fails.append('G-ROUTES')

    print(chr(10) + '  G-LOCATE (F3: each source with status, bytes, sha256; the located string at its line in the banked text; no PDF in any repo):')
    ok_loc = True
    for sid, s in L['sources'].items():
        ok_loc = ok_loc and s.get('status') == 200 and isinstance(s.get('bytes'), int) and len(s.get('sha256', '')) == 64 and s.get('read') and os.path.exists(d(s['text_file']))
        for n in ('3', '5'):
            for h in s['hits'][n]:
                line = io.open(d(s['text_file']), encoding='utf-8').read().splitlines()[h['line'] - 1]
                ok_loc = ok_loc and h['string'] in line
    pdfs = [x for x in (git(ROOT, 'ls-files') + git(PP, 'ls-files') + git(SIDE, 'ls-files')).splitlines() if x.lower().endswith('.pdf') and 'b341' in x]
    gl = ok_loc and not pdfs and L['located']['3'] == [['S1', 'keystone']] and L['located']['5'] == []
    print('    sources read %d ; located n = 3 %s ; n = 5 %s ; b341 PDFs tracked %d : %s' % (sum(1 for s in L['sources'].values() if s.get('read')), L['located']['3'], L['located']['5'], len(pdfs), gl))
    if not gl:
        fails.append('G-LOCATE')

    print(chr(10) + '  G-DECIDE (F4: the verdict by the sealed rule, recomputed from the record):')
    with mp.workdps(40):
        bd = {n: mp.mpf(C['table'][n]['bench_off']) > mp.mpf('1e-9') for n in ('3', '5')}
        kd = {n: mp.mpf(C['table'][n]['keystone_off']) > mp.mpf('1e-9') for n in ('3', '5')}
    gd = C['routes_ok'] and bd['3'] and bd['5'] and not kd['3'] and not kd['5'] and C['verdict'] == 'THE BENCH CARRIES THE DEFECT at n = [3, 5]' and C['names_carrier'] \
        and C['lit_status']['3'] == 'LOCATED, AGREES' and C['lit_status']['5'] == 'NOT READ'
    print('    bench defect %s ; keystone defect %s ; verdict %r ; literature %s : %s' % (bd, kd, C['verdict'], C['lit_status'], gd))
    if not gd:
        fails.append('G-DECIDE')

    print(chr(10) + '  G-ERRATUM (F5: one block under the mark with the id; both prior wordings inside; the file a true prefix of its blob; the partition block byte-identical):')
    blk = err[err.index(MARK):] if MARK in err else ''
    part_pre = err[err.index('<!-- b337 partition -->'):err.index(MARK)] if MARK in err else ''
    pre_blob = blob_of(PP, 'ERRATA.md') or ''
    base = pre_blob if not committed else (pre_blob[:pre_blob.index(MARK)] if MARK in pre_blob else pre_blob)
    prefix_ok = norm(err).startswith(norm(base).rstrip(chr(10)))
    gerr = (err.count(MARK) == 1 and err.count('## %s' % EID) == 1 and "3: '0.2077580993'" in blk and '0.20763892059268' in blk and '(INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)' in blk
            and 'NO OWNER FILE IS EDITED' in blk and prefix_ok and part_pre.strip() in norm(pre_blob) and 'c822ec710fe0967e' in blk and C['verdict'] in blk)
    print('    mark once %s ; id once %s ; prior wordings inside %s ; class in the heading %s ; prefix of blob %s (committed %s) ; partition block unchanged %s : %s'
          % (err.count(MARK) == 1, err.count('## %s' % EID) == 1, "3: '0.2077580993'" in blk and '0.20763892059268' in blk, '(INTERNAL RECORD; NO DEPOSITED ARTIFACT IS AFFECTED)' in blk, prefix_ok, committed, part_pre.strip() in norm(pre_blob), gerr))
    if not gerr:
        fails.append('G-ERRATUM')

    print(chr(10) + "  G-NOEDIT (F6: the bench, the keystone, FINDINGS, the ledger, the owner tools: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md', 'tools/b327_bridge.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b327_the_faces_ledger.txt', 'data/b327_source_text.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('ERRATA.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond ERRATA) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    r189 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| %s |' % ROWNUM)]
    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s: NO TERMINAL with the reason; the table a true prefix of its blob):' % ROWNUM)
    headb = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r189) == 1 and 'NO TERMINAL, AND THE REASON: A TRANSCRIPTION FILED' in r189[0] and 'M-2' in r189[0] and 'THE BENCH CARRIES THE DEFECT' in r189[0] and norm(tbl).startswith(norm(headb).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTAMEASUREMENT (one row; the must-not-hit queries NO KEY; the answer says no measurement changes, no deposit affected, no owner file edited):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('two-coefficients')
    gk = o.count('act      :') == 1 and 'NO BENCH MEASUREMENT CHANGES' in o and 'NO DEPOSITED ARTIFACT IS AFFECTED' in o and 'NO OWNER FILE IS EDITED' in o
    for s in ("the bench's measurements wrong", 'the keystone wrong', 'the deposit affected'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTAMEASUREMENT')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-ORDER (the seal verifies; the locate, the coefficients, the entry, the row, the key and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b341_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b341_locate.py'), t('b341_coefficients.py'), t('b341_errata.py'), LRUNS[0], LJ, CRUNS[0], CJ, ERUN, ERRATA, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b341_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b341_checks_run.txt')) else ''
        after = 'the locate, the coefficients, the entry, the row, the key and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the locate, the coefficients, the entry, the row, the key and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed:
        print('    ERRATA committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    ERRATA not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing record):')
    checks = []
    for n in ('3', '5'):
        tt = C['table'][n]
        checks.append(('route values at n = %s' % n, ('`%s`' % tt['A']) in bank and ('`%s`' % tt['dAB']) in bank and ('`%s`' % tt['bench_off']) in bank and ('`%s`' % tt['keystone_off']) in bank and ('`%s`' % tt['bench']) in bank and ('`%s`' % tt['keystone']) in bank))
    checks.append(('the radii %s' % C['radii_worst'], ('`%s`' % C['radii_worst']) in bank))
    for sid, s in L['sources'].items():
        checks.append(('%s sha256' % sid, ('`%s`' % s['sha256']) in bank))
    checks.append(('S1 bytes %d' % L['sources']['S1']['bytes'], ('%d bytes' % L['sources']['S1']['bytes']) in bank))
    h3 = L['sources']['S1']['hits']['3'][0]
    checks.append(('the located string and line', ('`%s`' % h3['string']) in bank and ('line %d' % h3['line']) in bank))
    checks.append(('the bench line %d and the keystone table line %d' % (C['bench_line'], C['keystone_head_line']), ('line %d)' % C['bench_line']) in bank and ('table at line %d' % C['keystone_head_line']) in bank))
    el = io.open(ERUN, encoding='utf-8').read()
    lm = re.search(r'lines (\d+) -> (\d+)', el)
    checks.append(('ERRATA %s -> %s lines' % lm.groups(), ('%s -> %s lines' % lm.groups()) in bank and len(err.splitlines()) == int(lm.group(2))))
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, rn == ROWNUM and ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    for what, ok in checks:
        print('    %-52s %s' % (what[:52], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded and numbered; the record runs the last):')
    once_ok = all(os.path.exists(p) for p in LRUNS + CRUNS + [LJ, CJ, ERUN, ERR2, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b341_locate_run4.txt')) and not os.path.exists(d('b341_coefficients_run3.txt')) and C['run_file'] == 'b341_coefficients_run2.txt'
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
        print('    %-40s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                        ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                     if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib = idx[idx.index('# ### THE TWO COEFFICIENTS (b341'):idx.index('# ### THE LI FAMILY CONTROL (b340')] if '# ### THE TWO COEFFICIENTS (b341' in idx else ''
    print(chr(10) + '  G-STEM-APPENDED (row %s, the ERRATA entry, the index row, swept):' % ROWNUM)
    for lbl, blk2 in (('row %s' % ROWNUM, r189[0] if r189 else ''), ('the ERRATA entry', blk), ('index row', ib)):
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
        print('    %-64s %-34s exists=%s tracked=%s' % (what[:64], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the row, the entry and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b341_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, r189[0] if r189 else ''), ('the ERRATA entry', blk), ('the index row', ib)):
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
    print('  ### needles unpullable : %d ; owner needles not in the extract file : %d' % (unpullable, not_extracted))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
