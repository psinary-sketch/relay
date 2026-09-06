# -*- coding: utf-8 -*-
"""b335_checks.py -- THE GATE SUITE FOR THE STANDING CLAUSES, FILED.

### ### **THE ARMS (registration (F), F1-F7):** `G-STANDING`, `G-PROVENANCE`, `G-SCAN`, `G-DIFF`, `G-RULE6`, `G-ROW`,
### `G-KEY` / `G-BINDS-NOTHING`, `G-NOMATH` (must-fail), `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`,
### `G-ONCE`, `G-NOEDIT`, `G-APPENDONLY`, the hedge audit, the stem sweep, the must-fail fixtures; re-run after the push.
"""
import hashlib
import io
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
import b335_standing as STG  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
RULES = os.path.join(PP, 'protocols', 'EXECUTOR_RULES.md')
STANDING = os.path.join(ROOT, 'tools', 'FERRY_STANDING.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b335_the_standing_clauses.txt')
REG = d('b335_registration_2026-09-06.txt')
EXTRACT = d('b335_extract_notes.txt')
SRUN = d('b335_standing_run.txt')
SELFT, SCAN_AFTER, CITE_CUR, CITE_STALE = d('b335_scan_selftest.txt'), d('b335_ferry_scan_after.txt'), d('b335_scan_cite_current.txt'), d('b335_scan_cite_stale.txt')
R6, R6R = d('b335_rule6_run.txt'), d('b335_rule6_rerun.txt')
CORR, CORRR = d('b335_corr_run.txt'), d('b335_corr_rerun.txt')
IDX, IDXR = d('b335_index_run.txt'), d('b335_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b335_ferry_scan.txt'), d('b335_reg_termscan.txt'), d('b335_reg_gate.txt')
CENSUS, FCEN = d('b335_census.txt'), d('b335_faces_census.txt')
REGSPEC, SATIS = d('b335_regspec_run.txt'), d('audit_b335_reg_satisfiable.txt')
PINS, INDEXQ = d('b335_pins_stepzero.txt'), d('audit_b335_index_query.txt')
HOOKS, MIRROR = d('b335_hooks.txt'), d('b335_mirror.txt')
SEAL = '5d29122ae27380f1ee5df5f7092b22d17ddcb5ac658a4fc5c886be26cf8a4ff1'
MARK6 = '## Rule 6 \u2014 The STOP format'

OWNED = [BANK, REG, SRUN, SELFT, SCAN_AFTER, CITE_CUR, CITE_STALE, R6, R6R, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b335_satisfiable.json'), STANDING, t('b335_extract.py'), t('b335_regspec.py'), t('b335_standing.py'), t('b335_rule6.py'),
         t('b335_correspondence.py'), t('b335_index_append.py')]

CARRIERS = [
    (t('b335_checks.py'), 'its own fixtures'),
    (d('b335_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
    (t('ferry_scan.py'), 'the scanner carries the struck clauses as patterns and fixtures'),
]

F334 = d('b334_ferry_2026-09-06.txt')
OWNER_NEEDLES = [
    ('b334 -- concurrency and the read rule', F334, 'CONCURRENCY: SOLO (research seat; every read through the'),
    ('### the registration sealed, no counts predicted', F334, 'in the path; registration sealed before any instrument runs,'),
    ('### step zero', F334, 'STEP ZERO: the ferry scan; both censuses; push anything ahead'),
    ('### the shadow', F334, 'ordered. THE SHADOW: expected nothing; say so.'),
    ('### execution', F334, 'EXECUTION: ferry scan first; registration sealed before any'),
    ('### the mirror, STOP', F334, 'touched; mirror if it moves. STOP.'),
    ('### the foot', F334, 'deposit left it; locks last.'),
    ('b320 -- step zero', d('b320_ferry_2026-09-04.txt'), 'STEP ZERO: the ferry scan; the ledger census with its scope;'),
    ('b327 -- execution', d('b327_ferry_2026-09-05.txt'), 'EXECUTION: ferry scan first; registration sealed before any'),
    ('the sortie -- leg 0', d('b335_ferry_2026-09-06.txt'), 'LEG 0 (b335) \u2014 THE STANDING CLAUSES, FILED: extract the scope,'),
    ('### the scan checks the citation', d('b335_ferry_2026-09-06.txt'), 'scan checking that a ferry citing it cites the current'),
    ('### DRAFT -- NAVIGATOR EDITS', d('b335_ferry_2026-09-06.txt'), 'next ferry, marked DRAFT \u2014 NAVIGATOR EDITS. Filings only.'),
    ("the executor's rules -- Rule 5", RULES, '## Rule 5 \u2014 The two verification legs'),
    ('ferry_scan -- the record it reads', t('ferry_scan.py'), "RECORD = os.path.join(ROOT, 'data', 'STRUCK_CLAUSES.md')"),
]

SELF_NEEDLES = [
    ('bank states the filings first', BANK, 'THE FILINGS, FIRST.'),
    ('### (1) the file exists and is measured', BANK, '`relay/tools/FERRY_STANDING.md`, VERSION 1, EXISTS AND IS MEASURED.'),
    ('### binds nothing', BANK, 'IT BINDS NOTHING BY ITSELF** -- a ferry that cites it carries its clauses by reference.'),
    ('### (2) the scan checks the citation', BANK, "THE FERRY SCAN CHECKS THE CITATION, BY THE ORDER'S WORDS."),
    ('### (3) rule 6', BANK, "RULE 6, THE STOP FORMAT, APPENDED TO THE EXECUTOR'S RULES."),
    ('### the draft binds nothing', BANK, 'THE DRAFT BINDS NOTHING.'),
    ('### no grade no claim', BANK, 'NO GRADE. NO CLAIM. NO ROW OF THE FACES LEDGER. NO FINDINGS SECTION. NOTHING DEPOSITS.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives filing 1', BANK, 'FILING 1 -- THE STANDING FILE.'),
    ('bank gives filing 2', BANK, 'FILING 2 -- THE SCANNER\'S EDIT, BY ORDER.'),
    ('### not additions only', BANK, 'NOT "ADDITIONS ONLY"'),
    ('bank gives filing 3', BANK, 'FILING 3 -- RULE 6.'),
    ('bank gives the row and the key', BANK, 'THE ROW AND THE KEY.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1', BANK, "E1 -- THE SCANNER'S EDIT IS NOT ADDITIONS ONLY."),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE SORTIE: LEG 1, b336, THE COST CENSUS.'),
    ('registration -- filings only', REG, '**FILINGS ONLY.**'),
    ('registration -- a majority', REG, 'A CLAUSE IS STANDING WHEN A MAJORITY OF THE FIFTEEN CARRY IT'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the standing file -- version', STANDING, 'VERSION: 1'),
    ('### binds nothing', STANDING, 'THIS FILE BINDS NOTHING BY ITSELF'),
    ('the rules -- rule 6', RULES, '## Rule 6 \u2014 The STOP format (filed 2026-09-06, author-ruled at the b335 sortie, leg 0)'),
    ('### the draft binds nothing', RULES, '**The draft binds nothing.**'),
]

MUST_FAIL = [
    ('the bank never states a grade', BANK, '### ### **A GRADE IS CONFERRED.**'),
    ('the bank never states a measurement of the mathematics', BANK, '### ### **THE MARGIN IS MEASURED HERE.**'),
    ('the bank never says the draft binds', BANK, '### ### **THE DRAFT BINDS.**'),
    ('the bank never says the file is a new rule', BANK, '### ### **THE STANDING FILE IS A NEW RULE.**'),
    ('the bank never says K8 is owned', BANK, '### ### **K8 IS OWNED.**'),
]

TOOLNUM = [
    ('37 / 33 / 4 clauses, the counts, 85 lines, 8772 bytes', 'tools/b335_standing.py'),
    ('9 of 9, 12 of 12, NONE, CURRENT, STALE, exit 1', 'tools/ferry_scan.py'),
    ('+18 lines, 129 -> 147', 'tools/b335_rule6.py'),
    ('62 insertions, 4 deletions', 'tools/b335_checks.py'),
    ('row 182', 'tools/b335_correspondence.py'),
    ('the key', 'tools/b335_index_append.py'),
    ('24 clauses', 'tools/b335_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('11407 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b335_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
]
NEW_THIS_ACT = {'tools/b335_standing.py', 'tools/b335_rule6.py', 'tools/b335_correspondence.py', 'tools/b335_index_append.py', 'tools/b335_regspec.py',
                'tools/b335_extract.py', 'tools/b335_checks.py'}


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
    print('b335 -- GATE SUITE (THE STANDING CLAUSES, FILED: FILINGS ONLY)')
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
    srun = io.open(SRUN, encoding='utf-8').read()
    standing = io.open(STANDING, encoding='utf-8').read()
    rules = io.open(RULES, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + '  G-STANDING (F1: the file, VERSION 1, every STANDING count a majority, the counts re-measured live):')
    rows = STG.measure()
    bad, ver = STG.check(rows)
    st_rows = [r for r in rows if r['count'] >= STG.MAJORITY]
    m = re.search(r'clauses measured (\d+) ; STANDING \(>= (\d+) of (\d+)\) (\d+) ; FREQUENT, NOT STANDING (\d+)', srun)
    gs = (ver == 1 and not bad and all(('**%s**' % r['id']) in standing for r in rows) and len(st_rows) == int(m.group(4)) and len(rows) == int(m.group(1))
          and 'CITE AS: `FERRY_STANDING v1`' in standing)
    print('    VERSION %s ; counts disagreeing %d ; standing %d of %d measured : %s' % (ver, len(bad), len(st_rows), len(rows), gs))
    if not gs:
        fails.append('G-STANDING')

    print(chr(10) + "  G-PROVENANCE (F2: every clause's source ferry line is located in the extract file or is the clause's own key found in its carriers):")
    # ### every clause names a source ferry; the extract file carries b334's, b320's and b327's lines; every clause's key is present in every carrier it names
    texts = {act: STG.flat(os.path.join(D, fn)) for act, fn in STG.FERRIES}
    gp = all(all(any(re.sub(r'\s+', ' ', k.lower()) in texts[a] for k in r['keys']) for a in r['carriers']) for r in rows) and all(r['source'].startswith(('b334', 'b320')) for r in rows)
    print('    %s' % gp)
    if not gp:
        fails.append('G-PROVENANCE')

    print(chr(10) + '  G-SCAN (F3: the self-test with the citation arms; NONE on the sortie ferry; CURRENT quiet, STALE a hit):')
    ok_self, _o = ferry_scan.self_test(verbose=False)
    st_none = ferry_scan.citation_check(io.open(d('b335_ferry_2026-09-06.txt'), encoding='utf-8').read())[0]
    cur = ferry_scan.standing_version()
    gsc = (ok_self and cur == 1 and st_none == 'NONE' and 'FIXTURES AGREEING : 12 of 12' in io.open(SELFT, encoding='utf-8').read()
           and 'CITATION : CURRENT' in io.open(CITE_CUR, encoding='utf-8').read() and '0 HIT(S) REPORTED' in io.open(CITE_CUR, encoding='utf-8').read()
           and 'CITATION : STALE' in io.open(CITE_STALE, encoding='utf-8').read() and '1 HIT(S) REPORTED' in io.open(CITE_STALE, encoding='utf-8').read()
           and 'CITATION : NONE' in io.open(SCAN_AFTER, encoding='utf-8').read())
    print('    self-test %s ; version %s ; sortie %s ; records current/stale/after present : %s' % (ok_self, cur, st_none, gsc))
    if not gsc:
        fails.append('G-SCAN')

    print(chr(10) + '  G-DIFF (F4: the scanner against its blob -- the changed lines named; the struck and stem arms byte-identical):')
    blob_scan = blob_of(ROOT, 'tools/ferry_scan.py') or ''
    cur_scan = io.open(t('ferry_scan.py'), encoding='utf-8').read()
    diff = subprocess.run(['git', '-C', ROOT, 'diff', 'HEAD', '--stat', '--', 'tools/ferry_scan.py'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout
    committed_scan = 'standing_version' in blob_scan
    removed = [ln[1:] for ln in subprocess.run(['git', '-C', ROOT, 'diff', 'HEAD', '--', 'tools/ferry_scan.py'], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.splitlines()
               if ln.startswith('-') and not ln.startswith('---')]
    arms_same = all(seg in cur_scan for seg in ('def parse_record(path=None):', 'def scan_text(text, struck=None, stem_list=None):', "e1 = struck[0]", 's0 = banned_terms.STEMS[0]'))
    if committed_scan:
        print('    the edited scanner is committed ; arms present %s : %s' % (arms_same, arms_same))
        gd = arms_same
    else:
        allowed = all(('FIXTURES AGREEING' in r or 'VERDICT' in r or 'return 1 if' in r or r.strip() == 'rec()' or r.strip() == 'print()' or 'len(cases) + len(stem_cases)' in r or 'len(ch) + len(sh)' in r) for r in removed)
        gd = arms_same and allowed and '62 insertions' in diff and '4 deletions' in diff
        print('    diff %s ; removed lines all in the tally / verdict / exit places %s ; arms present %s : %s' % (diff.strip().splitlines()[-1] if diff.strip() else '-', allowed, arms_same, gd))
    if not gd:
        fails.append('G-DIFF')

    print(chr(10) + '  G-RULE6 (F5: the rules file a true prefix of its blob plus Rule 6; Rules 1-5 byte-identical; the DRAFT header in the rule):')
    rb = blob_of(PP, 'protocols/EXECUTOR_RULES.md') or ''
    committed_r6 = MARK6 in rb
    pre_ok = norm(rules).startswith(norm(rb).rstrip(chr(10)))
    r6 = rules[rules.index(MARK6):] if MARK6 in rules else ''
    gr = rules.count(MARK6) == 1 and pre_ok and 'DRAFT \u2014 NAVIGATOR EDITS' in r6 and '**The draft binds nothing.**' in r6 and all(('## Rule %d' % k) in rules for k in range(1, 6))
    print('    mark once %s ; prefix of blob %s (Rule 6 committed: %s) ; DRAFT header %s : %s' % (rules.count(MARK6) == 1, pre_ok, committed_r6, 'DRAFT \u2014 NAVIGATOR EDITS' in r6, gr))
    if not gr:
        fails.append('G-RULE6')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row 182: NO TERMINAL with the reason, a filing act, M-2; the table a true prefix of its blob):')
    r182 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 182 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r182) == 1 and 'NO TERMINAL, AND THE REASON' in r182[0] and 'A FILING ACT' in r182[0] and 'M-2' in r182[0] and norm(tbl).startswith(norm(head).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-BINDS-NOTHING (one row; the must-not-hit queries NO KEY; the answer says the file and the draft bind nothing):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('ferry-standing')
    gk = o.count('act      :') == 1 and 'THE FILE BINDS NOTHING BY ITSELF' in o and 'THE DRAFT BINDS NOTHING' in o
    for s in ('the draft binds', 'a new rule', 'the cost census'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-BINDS-NOTHING')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner files beyond the ordered scanner edit, sealed files, the deposit, TECHNE, HANDOFF, the struck record: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/banned_terms.py', 'HANDOFF.md', 'data/STRUCK_CLAUSES.md',
              'data/b334_ferry_2026-09-06.txt', 'data/b320_ferry_2026-09-04.txt', 'data/b327_ferry_2026-09-05.txt', 'data/b334_the_aim_map.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('EXECUTOR_RULES.md')]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the rules) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the generator, the file, the scanner, the rule, the row and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b335_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b335_standing.py'), STANDING, t('ferry_scan.py'), t('b335_rule6.py'), RULES, SRUN, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b335_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b335_checks_run.txt')) else ''
        after = 'the generator, the file, the scanner, the rule, the row and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the generator, the file, the scanner, the rule, the row and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed_r6:
        print('    the rule committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    the rule not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    checks.append(('37 measured, 33 standing, 4 frequent', m.group(1) == '37' and m.group(4) == '33' and m.group(5) == '4' and 'measured 37 clauses: 33 STANDING' in bank and '4 FREQUENT, NOT STANDING' in bank))
    nl = len(standing.rstrip(chr(10)).split(chr(10)))
    nb = len(norm(standing).encode('utf-8'))   # ### LF-normalised: autocrlf rewrites the working file after a commit (b309)
    checks.append(('%d lines, %d bytes' % (nl, nb), ('%d lines, %d bytes' % (nl, nb)) in bank))
    for cid, cnt in (('C4', 2), ('C5', 6), ('C6', 1), ('C14', 5)):
        r = [x for x in rows if x['id'] == cid][0]
        checks.append(('%s count %d' % (cid, r['count']), r['count'] == cnt and ('%d of' % cnt) in bank))
    checks.append(('9 of 9 then 12 of 12', 'FIXTURES AGREEING : 12 of 12' in io.open(SELFT, encoding='utf-8').read() and '9 of 9 before' in bank and '12 of 12 after' in bank))
    r6run = io.open(R6, encoding='utf-8').read()
    add = re.search(r'WRITTEN \+(\d+) lines', r6run).group(1)
    nr = len(norm(rules).rstrip(chr(10)).split(chr(10)))
    nrb = len(norm(rb).rstrip(chr(10)).split(chr(10))) if not committed_r6 else nr - int(add)
    checks.append(('+%s lines, %d -> %d' % (add, nrb, nr), ('gains %s lines' % add) in bank and ('`%d -> %d`' % (nrb, nr)) in bank))
    checks.append(('62 insertions, 4 deletions', ('62 insertions, 4 deletions' in bank) and (committed_scan or ('62 insertions' in diff and '4 deletions' in diff))))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [SRUN, SELFT, SCAN_AFTER, CITE_CUR, CITE_STALE, R6, R6R, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b335_rule6_run2.txt'))
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

    print(chr(10) + '  G-STEM-APPENDED (the rule, row 182, the index row, swept):')
    ib = idx[idx.index('# ### THE STANDING CLAUSES, FILED (b335'):idx.index('# ### THE AIM-MAP (b334).')] if '# ### THE STANDING CLAUSES, FILED (b335' in idx else ''
    for lbl, blk2 in (('rule 6', r6), ('row 182', r182[0] if r182 else ''), ('index row', ib)):
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the rule, the row and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b335_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('rule 6', r6), ('row 182', r182[0] if r182 else ''), ('the index row', ib)):
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
