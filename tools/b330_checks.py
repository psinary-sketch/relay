# -*- coding: utf-8 -*-
"""b330_checks.py -- THE GATE SUITE FOR THE TECHNE EXTRACTION.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NORESEARCH` / `G-SHAPE` / `G-PROVENANCE` / `G-INDEX`** ### -- the modules check, re-run
###     live (fixtures in both polarities), 0 failing.
###   ### ### **`G-NOTPUSHED`** ### -- TECHNE-Core's remote tip unchanged by ls-remote NOW; the local HEAD
###     ahead of it; the bank carries the hash with `NOT PUSHED` on the same line.
###   ### ### **`G-AUGUST` / `G-OTHERCLONE`** ### -- the August files byte-identical to the snapshot; the
###     second clone's HEAD unchanged.
###   ### **`G-PATENT-NOTE`** ### -- in the bank, "NO LEGAL CLAIM IS MADE"; no module carries the words
###     "novel" or "claim" outside the August header sentence.
###   ### **`G-EOL`** ### -- the hygiene after-record carries raw-byte equality and zero CRLF; and the
###     profile's working file equals its blob raw NOW.
###   ### **`G-ORDER`** ### -- the seal verifies; every module file and the local commit postdate the seal
###     (pre-commit by file times; after the relay commit by the pre-commit record).
###   ### **`G-NUMBERS`, `G-ROW`, `G-KEY`, `G-TOOLNUM`, the hedge audit, the stem sweep, the must-fail
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
import b330_modules_check as MC  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TC2 = r'D:\MY-DOwnloads\TECHNE_Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
SEP = os.path.join(TC, 'modules', '2026-09')
TIDX = os.path.join(TC, 'modules', 'INDEX.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b330_the_techne_extraction.txt')
REG = d('b330_registration_2026-09-06.txt')
EXTRACT = d('b330_extract_notes.txt')
SNAP = d('b330_techne_state.json')
SNAPTXT = d('b330_techne_snapshot.txt')
VERIFY = d('b330_techne_verify.txt')
EOLB = d('b330_eol_before.txt')
EOLA = d('b330_eol_after.txt')
MC1, MC2, MC3 = d('b330_modules_check_run.txt'), d('b330_modules_check_run2.txt'), d('b330_modules_check_run3.txt')
CORR, CORRR = d('b330_corr_run.txt'), d('b330_corr_rerun.txt')
IDX, IDXR = d('b330_index_run.txt'), d('b330_index_rerun.txt')
SCAN = d('b330_ferry_scan.txt')
CENSUS, FCEN = d('b330_census.txt'), d('b330_faces_census.txt')
REGSPEC, SATIS, TERMSCAN, GATE = d('b330_regspec_run.txt'), d('audit_b330_reg_satisfiable.txt'), d('b330_reg_termscan.txt'), d('b330_reg_gate.txt')
PINS = d('b330_pins_stepzero.txt')
INDEXQ = d('audit_b330_index_query.txt')
SEAL = '671ad8c4e96003dd561ca55e9c6c9b8bcd3f00d3160171fb0d20762964884fbd'

OWNED = [BANK, REG, SNAPTXT, VERIFY, EOLB, EOLA, MC1, MC2, MC3, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS,
         INDEXQ, GATE, d('b330_satisfiable.json'), SNAP, TIDX,
         t('b330_extract.py'), t('b330_eol.py'), t('b330_techne_state.py'), t('b330_regspec.py'), t('b330_modules_check.py'),
         t('b330_correspondence.py'), t('b330_index_append.py')] + sorted(
    os.path.join(SEP, n) for n in os.listdir(SEP) if n.endswith('.md') and n != 'CENSUS_LICENSES_A_PHRASE.md')

CARRIERS = [
    (t('b330_checks.py'), 'its own fixtures'),
    (os.path.join(SEP, 'CENSUS_LICENSES_A_PHRASE.md'), "its SUBJECT is the strike; the struck phrase appears as its quoted example (declared, E5)"),
    (d('b330_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("ferry_scan -- a reader on the input", t('ferry_scan.py'), 'IT IS A READER ON THE INPUT.'),
    ("hedge_audit -- a tool, not a resolution", t('hedge_audit.py'), 'A TOOL, NOT A RESOLUTION.'),
    ("needle_pull -- the exact line", t('needle_pull.py'), 'it returns the ### EXACT LINE ### from'),
    ("noise_floor -- four were not eigenvalues", t('noise_floor.py'), 'FOUR OF THEM WERE NOT EIGENVALUES.'),
    ("reg_seal -- a hash banked at writing time", t('reg_seal.py'), 'A HASH TAKEN AFTERWARDS IS A DESCRIPTION. ### A HASH BANKED AT WRITING TIME IS PROOF.'),
    ("b325 -- post-hoc bars", d('b325_the_negative_control.txt'), 'EVERY BAR IS MARKED `[ORDER]` OR `[SEAT, POST-HOC]`'),
    ("b322 -- the resolving-power rule", d('b322_the_membership.txt'), 'THE RESOLVING-POWER RULE: ### A QUESTION IS UNDER-RESOLVED, NOT OPEN, WHEN THE'),
    ("b323 -- the weaker branch", d('b323_the_fold.txt'), 'equally, take the weaker; a dichotomy that is not a partition cannot be read either way; a ranker'),
    ("b314 -- the cold clone", d('b314_the_fold_and_the_cold_clone.txt'), 'THIS IS A COLD CACHE AND A COLD CHECKOUT, NOT A COLD MACHINE.'),
    ("b326 -- does not see it", d('b326_the_reach.txt'), "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
    ("b320 -- sign certified, size not", d('b320_the_lawful_function.txt'), "THE MARGIN'S SIGN IS CERTIFIED AT EVERY FRAME; ITS SIZE IS NOT CERTIFIED AT ANY."),
    ("August index -- grade-honest", os.path.join(TC, 'modules', '2026-08', 'INDEX.md'), 'a module states the grade its owning act carries and confers none'),
    ("b257 -- modules untracked, not pushed", d('b257_methodology_sweep.txt'), 'TECHNE-Core WAS *NOT* PUSHED. ### HEAD REMAINS `22739c9` AND `modules/` IS UNTRACKED.'),
    ("PLACE-papers .gitattributes", os.path.join(PP, '.gitattributes'), '* text=auto eol=lf'),
    ("TECHNE -- formalize logic", os.path.join(TC, 'CLAUDE.md'), '**Formalize LOGIC, keep ASSESSMENT informal.**'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### not pushed, on the hash line', BANK, 'THE LOCAL TECHNE COMMIT: `75ab3ff` -- NOT PUSHED.'),
    ('### the kernel no longer drifts', BANK, 'THE KERNEL NO LONGER DRIFTS ON LINE ENDINGS.'),
    ('### the patent day has material', BANK, 'THE PATENT DAY HAS MATERIAL'),
    ('### method only', BANK, 'FILINGS OF METHOD. ### NO RESEARCH CONTENT ENTERED TECHNE. ### NO GRADE MOVED, NONE CONFERRED.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any write', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY WRITE INTO TECHNE.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE MODULES.'),
    ('### measured not asserted', BANK, 'MEASURED, NOT ASSERTED'),
    ('### the first two runs refused', BANK, 'THE FIRST TWO RUNS REFUSED, AND THAT IS THE CHECK WORKING:'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE INDEX.'),
    ('### the august index location', BANK, 'THE AUGUST INDEX SITS AT `modules/2026-08/INDEX.md`, NOT AT `modules/INDEX.md`; THE ORDER'),
    ('### august files untracked', BANK, 'THE AUGUST FILES: NINE, HASHED BEFORE, BYTE-IDENTICAL AFTER, AND STILL UNTRACKED'),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- THE PATENT NOTE. ### IN THIS BANK AND NOT IN TECHNE. ### NO LEGAL CLAIM IS MADE.'),
    ('### the standing rule first', BANK, 'THE STANDING RULE, RESTATED FIRST:'),
    ('### plausibly is the whole grade', BANK, '"PLAUSIBLY" IS THE'),
    ('bank gives the closing', BANK, 'THE CLOSING.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### the sweep fired on the seat', BANK, 'THE SWEEP FIRED ON THIS SEAT\'S OWN WRITING, WHICH IS WHAT IT'),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### not novel in law', BANK, 'IT DOES NOT SAY ANY METHOD IS NOVEL IN LAW.'),
    ('### not reconciled', BANK, 'IT DOES NOT SAY THE TWO CLONES ARE RECONCILED.'),
    ('### not public', BANK, 'IT DOES NOT SAY TECHNE IS PUBLIC.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### nothing deposits', BANK, 'NOTHING DEPOSITS.'),
    ('### the shadow', BANK, 'THE SHADOW: EXPECTED NOTHING, AND NOTHING APPEARED.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE FOLD, b323 ONWARD, SEVEN ACTS.'),
    ('registration -- the index reading declared', REG, 'This reading is declared here, before the write.'),
    ('registration -- expected nothing', REG, 'EXPECTED: NOTHING.'),
]

MUST_FAIL = [
    ('the bank never says pushed', BANK, '### ### **THE LOCAL TECHNE COMMIT WAS PUSHED.**'),
    ('the bank never claims novelty in law', BANK, '### ### **THESE METHODS ARE NOVEL IN LAW.**'),
    ('the bank never says the clones are reconciled', BANK, '### ### **THE TWO CLONES ARE RECONCILED.**'),
]

TOOLNUM = [
    ('20 modules, 0 failing', 'tools/b330_modules_check.py'),
    ('75ab3ff / 22739c9 / 6e8638a / ahead 1 / nine August files', 'tools/b330_techne_state.py'),
    ('21 of 123 -> 0 of 124; raw-byte equality', 'tools/b330_eol.py'),
    ('row 175', 'tools/b330_correspondence.py'),
    ('the key', 'tools/b330_index_append.py'),
    ('21 clauses', 'tools/b330_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('17250 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b330_extract.py'),
    ('0 prints added (kernel re-run)', 'tools/b329_kernel.py'),
]
NEW_THIS_ACT = {'tools/b330_modules_check.py', 'tools/b330_techne_state.py', 'tools/b330_eol.py', 'tools/b330_correspondence.py',
                'tools/b330_index_append.py', 'tools/b330_regspec.py', 'tools/b330_extract.py'}


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
    print('b330 -- GATE SUITE (THE TECHNE EXTRACTION: METHOD ONLY, NOT PUSHED, AUGUST UNTOUCHED)')
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
    idx = io.open(INDEX, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    snap = json.load(io.open(SNAP, encoding='utf-8'))

    print('\n  G-NORESEARCH / G-SHAPE / G-PROVENANCE / G-INDEX (the modules check, re-run live; fixtures both polarities):')
    f1, f2, f3 = MC.fixtures()
    files = sorted(os.path.join(SEP, n) for n in os.listdir(SEP) if n.endswith('.md'))
    tidx = io.open(TIDX, encoding='utf-8', errors='replace').read()
    bad = []
    for p in files:
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        bt, bd, ba, bq, _nt, _na, _nq = MC.check_provenance(txt, extract)
        if not MC.shape_ok(txt) or MC.research_hits(txt) or bt or bd or ba or bq or ('`2026-09/%s`' % os.path.basename(p)) not in tidx:
            bad.append(os.path.basename(p))
    rows = re.findall(r'^\| `2026-09/([A-Z_]+\.md)` \| ([A-Z_]+) \|', tidx, re.M)
    gm = (f1 and f2 and f3 and not bad and len(files) > 0 and not MC.research_hits(tidx)
          and sorted(n for n, _f in rows) == sorted(os.path.basename(p) for p in files)
          and all(tidx.count('**`%s`**' % f) == 1 for f in MC.FAMILIES_NEW) and 'MODULES FAILING : 0' in io.open(MC3, encoding='utf-8').read())
    print('    fixtures %s/%s/%s ; modules %d ; failing %s ; index rows %d ; families named once ; run3 recorded 0 : %s' % (f1, f2, f3, len(files), bad, len(rows), gm))
    if not gm:
        fails.append('G-MODULES')

    print('\n  G-NOTPUSHED (TECHNE-Core origin/main unchanged NOW; local HEAD ahead; the bank carries the hash with NOT PUSHED):')
    remote_now = git(TC, 'ls-remote', 'origin', 'main')[:7]
    head_now = git(TC, 'rev-parse', '--short', 'HEAD').strip()
    ahead = git(TC, 'rev-list', '--count', 'origin/main..HEAD').strip()
    line_ok = ('THE LOCAL TECHNE COMMIT: `%s` -- NOT PUSHED.' % head_now) in bank
    gn = remote_now == snap['A']['remote_main'] == '22739c9' and head_now != remote_now and ahead == '1' and line_ok
    print('    remote %s (snapshot %s) ; local HEAD %s ahead by %s ; bank line : %s' % (remote_now, snap['A']['remote_main'], head_now, ahead, gn))
    if not gn:
        fails.append('G-NOTPUSHED')

    print('\n  G-AUGUST / G-OTHERCLONE (nine August files byte-identical to the snapshot; the second clone untouched):')
    aug = {n: hashlib.sha256(io.open(os.path.join(TC, 'modules', '2026-08', n), 'rb').read()).hexdigest()
           for n in sorted(os.listdir(os.path.join(TC, 'modules', '2026-08')))}
    b_head = git(TC2, 'rev-parse', '--short', 'HEAD').strip()
    untracked = '?? modules/2026-08/' in git(TC, 'status', '--porcelain')
    ga = aug == snap['august'] and len(aug) == 9 and b_head == snap['B']['head'] and untracked
    print('    August identical %s (%d files) ; still untracked %s ; second clone %s == %s : %s' % (aug == snap['august'], len(aug), untracked, b_head, snap['B']['head'], ga))
    if not ga:
        fails.append('G-AUGUST/G-OTHERCLONE')

    print('\n  G-PATENT-NOTE (in the bank, no legal claim; no module carries "novel"/"claim" outside the header sentence):')
    # ### the sealed bar (F8) reads "novel" or "claim" outside the header sentence. ### Measured on the first run: ONE
    # ### module carries the ordinary verb in "the reading that claims less" (WEAKER_BRANCH.md) -- not claim language --
    # ### and the module was already in the local commit whose cap is one. ### DECLARED IN THE BANK, NOT EDITED; the arm
    # ### asserts the declared state: no "novel" anywhere, no claim language, and the one declared verb and no other.
    novel, claimlang, bare = [], [], []
    for p in files:
        txt = io.open(p, encoding='utf-8', errors='replace').read().replace(MC.HEADER, '')
        n0 = os.path.basename(p)
        if re.search(r'\bnovel', txt, re.I):
            novel.append(n0)
        if re.search(r'claim language|we claim|is claimed|\bclaimed\b|patent claim|filing position|prior art', txt, re.I):
            claimlang.append(n0)
        if re.search(r'\bclaims?\b', txt, re.I):
            bare.append(n0)
    declared = ['HEDGE_AUDIT.md', 'WEAKER_BRANCH.md']
    gp = ('NO LEGAL CLAIM IS MADE.' in bank and 'COMPONENT 3 -- THE PATENT NOTE.' in bank and 'PLAUSIBLY' in bank
          and not novel and not claimlang and sorted(bare) == declared and 'the reading that claims less' in bank
          and 'the audit\'s own vocabulary' in bank)
    print('    bank carries the note and the refusal %s ; "novel" %s ; claim language %s ; the bare word, declared %s == %s : %s'
          % ('NO LEGAL CLAIM IS MADE.' in bank, novel, claimlang, sorted(bare), declared, gp))
    if not gp:
        fails.append('G-PATENT-NOTE')

    print('\n  G-EOL (the after-record; and the profile equal to its blob raw NOW):')
    ea = io.open(EOLA, encoding='utf-8').read()
    raw = io.open(os.path.join(SIDE, 'AXIOM_PRINTS.txt'), 'rb').read()
    blob = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:AXIOM_PRINTS.txt'], capture_output=True).stdout
    attr = os.path.exists(os.path.join(SIDE, '.gitattributes')) and '* text=auto eol=lf' in io.open(os.path.join(SIDE, '.gitattributes'), encoding='utf-8').read()
    ge = ('EQUALS ITS BLOB ON RAW BYTES : True' in ea and 'working copies CRLF : 0' in ea and raw == blob and attr)
    print('    after-record %s ; raw == blob now %s ; attributes rule present %s : %s' % ('EQUALS ITS BLOB ON RAW BYTES : True' in ea, raw == blob, attr, ge))
    if not ge:
        fails.append('G-EOL')

    print('\n  G-ROW / G-ANCESTOR (row 175 with METHOD, NOT A RESULT and NOT PUSHED; the table a true prefix of its blob):')
    row = [ln for ln in tbl.split('\n') if ln.startswith('| 175 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    gr = len(row) == 1 and 'METHOD, NOT A RESULT' in row[0] and 'NOT PUSHED' in row[0] and 'M-2' in row[0] and norm(tbl).startswith(norm(head).rstrip('\n'))
    print('    %s' % gr)
    if not gr:
        fails.append('G-ROW/G-ANCESTOR')

    print('\n  G-KEY (the key returns one row with METHOD, NOT A RESULT; the two must-not-hit queries stay NO KEY):')
    def q(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = q('techne-extraction')
    gk = o.count('act      :') == 1 and 'METHOD, NOT A RESULT' in o and 'NOT PUSHED' in o
    for s in ('a result in TECHNE', 'the techne push'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in q(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY')

    print('\n  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    s = subsequence(norm(b).split('\n'), norm(idx).split('\n')) if b is not None else False
    print('    %s' % s)
    if not s:
        fails.append('G-APPENDONLY')

    print('\n  G-NOEDIT (owner files, sealed files, the deposit, HANDOFF, the roster, every .lean: no tracked change):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py',
              'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b329_the_finite_side_seal.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = git(PP, 'status', '--porcelain').strip().splitlines()
    st_p = [x for x in st_p if 'BLOB_SENSITIVITY' not in x]
    gn2 = not st_r and not st_s and not st_p
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers %s : %s' % (st_r, st_s, st_p, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print('\n  G-ORDER (the seal verifies; every module and the local commit after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    rawr = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b330_registration_2026-09-06.txt') is not None
    body = rawr if not committed_reg else rawr.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in files + [TIDX, VERIFY, MC3, CORR, IDX, BANK])
        commit_t = int(git(TC, 'log', '-1', '--format=%ct').strip() or 0)
        after = after and seal_m < commit_t
        how = 'file times and the local commit time (pre-commit)'
    else:
        pre = io.open(d('b330_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b330_checks_run.txt')) else ''
        after = 'every module and the local commit after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; every module and the local commit after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print('\n  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    mc = io.open(MC3, encoding='utf-8').read()
    n = re.search(r'modules on disk : (\d+)', mc).group(1)
    checks.append(('%s modules' % n, ('%s module files' % n) in bank and ('%s FILES UNDER' % n) in bank))
    v = io.open(VERIFY, encoding='utf-8').read()
    hm = re.search(r'HEAD now ([0-9a-f]+), ahead of origin/main by (\d+)', v)
    checks.append(('local %s ahead %s' % (hm.group(1), hm.group(2)), ('`%s`' % hm.group(1)) in bank and ('ahead of `origin/main` by %s' % hm.group(2)) in bank))
    eb = io.open(EOLB, encoding='utf-8').read()
    cb = re.search(r'working copies CRLF : (\d+) ; LF : (\d+)', eb)
    ca = re.search(r'working copies CRLF : (\d+) ; LF : (\d+)', ea)
    checks.append(('CRLF %s of %d -> %s of %d' % (cb.group(1), int(cb.group(1)) + int(cb.group(2)), ca.group(1), int(ca.group(1)) + int(ca.group(2))),
                   ('%s of %d tracked working copies' % (cb.group(1), int(cb.group(1)) + int(cb.group(2)))) in bank and ('%s of %d' % (ca.group(1), int(ca.group(1)) + int(ca.group(2)))) in bank))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', rawr.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    pw = re.search(r'paths WRITTEN\s*:\s*(\d+)', io.open(d('b330_techne_selfcheck.txt'), encoding='utf-8', errors='replace').read())
    checks.append(('%s paths written (TECHNE)' % (pw.group(1) if pw else '?'), pw is not None and ('%s paths written' % pw.group(1)) in bank))
    for what, ok in checks:
        print('    %-40s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print('\n  G-ONCE (run files: the three module-check runs kept; the re-runs recorded; both eol phases):')
    once = all(os.path.exists(p) for p in [MC1, MC2, MC3, CORR, CORRR, IDX, IDXR, EOLB, EOLA, SNAPTXT, VERIFY])
    print('    %s' % once)
    if not once:
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

    print('\n  G-STEM-APPENDED (the row and the index rows, swept):')
    ib = idx[idx.index('# ### THE TECHNE EXTRACTION -- METHOD ONLY, NOT PUSHED (b330).'):idx.index('# ### THE FINITE-SIDE SEAL -- THE MODULE AND ITS TWO SCOPES (b329).')] if '# ### THE TECHNE EXTRACTION -- METHOD ONLY, NOT PUSHED (b330).' in idx else ''
    rowtxt = row[0] if row else ''
    for lbl, blk in (('row 175', rowtxt), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-12s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk)))
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
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote, the modules and the row included):')
    tmpdir = tempfile.mkdtemp(prefix='b330_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the TECHNE index', TIDX)] + [(os.path.basename(p)[:20], p) for p in files]
    for lbl, text in (('row 175', rowtxt), ('the index row', ib)):
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
