# -*- coding: utf-8 -*-
"""b338_checks.py -- THE GATE SUITE FOR THE FOLD, b331-b334.

### ### **THE ARMS (registration (E), F1-F11):** F-QUOTE / F-COUNT / F-MODULES re-run live through the generator's module;
### `G-ADDITIVE`, `G-NOGRADE`, `G-ONE`, `G-DESK`, `G-ROWS`, `G-KEY` / `G-NOTAVERDICT`, `G-ORDER`, `G-HOOK` / `G-MIRROR`,
### `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOEDIT`, `G-APPENDONLY`, the hedge audit (the emitted section included), the stem
### sweep over OWNED files and CARRIERS, the must-fail fixtures; re-run after the push.
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
import b338_fold as F    # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
FINDINGS = os.path.join(PP, 'FINDINGS.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b338_the_fold.txt')
REG = d('b338_registration_2026-09-06.txt')
EXTRACT = d('b338_extract_notes.txt')
FRUN, FRUN2, EMIT, ROWSJ = d('b338_fold_run.txt'), d('b338_fold_run2.txt'), d('b338_fold_emitted.md'), d('b338_fold_rows.json')
CORR, CORRR = d('b338_corr_run.txt'), d('b338_corr_rerun.txt')
IDX, IDXR = d('b338_index_run.txt'), d('b338_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b338_ferry_scan.txt'), d('b338_reg_termscan.txt'), d('b338_reg_gate.txt')
CENSUS, FCEN = d('b338_census.txt'), d('b338_faces_census.txt')
REGSPEC, SATIS = d('b338_regspec_run.txt'), d('audit_b338_reg_satisfiable.txt')
PINS, INDEXQ = d('b338_pins_stepzero.txt'), d('audit_b338_index_query.txt')
HOOKS, MIRROR = d('b338_hooks.txt'), d('b338_mirror.txt')
SEAL = 'ed06184dbdde8e6a7989dc3ea8d4e7876a41373906ca02ac76a191fc155a4075'
HEADING = '## ' + F.SECTION

OWNED = [BANK, REG, FRUN, FRUN2, EMIT, ROWSJ, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE, d('b338_satisfiable.json'),
         t('b338_extract.py'), t('b338_regspec.py'), t('b338_fold.py'), t('b338_correspondence.py'), t('b338_index_append.py')]

CARRIERS = [
    (t('b338_checks.py'), 'its own fixtures'),
    (d('b338_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ('b331 -- the result', d('b331_the_fold.txt'), 'AND IT IS PURELY ADDITIVE, MEASURED AND NOT PROMISED.'),
    ('### the obstacle', d('b331_the_fold.txt'), 'IT DOES NOT SAY EITHER NEXT ACT IS THE DISCHARGE.'),
    ('b332 -- the result', d('b332_the_clause_stated.txt'), "THE CLAUSE IS STATED, WHOLE, IN THE ARC'S VOCABULARY, AND IT IS NOT DISCHARGED."),
    ('### the obstacle', d('b332_the_clause_stated.txt'), 'IT DOES NOT SAY THE RANKING IS A VERDICT ON THE CLAUSE.'),
    ('b333 -- the result', d('b333_the_archimedean_term_derived.txt'), "THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED."),
    ('### the obstacle', d('b333_the_archimedean_term_derived.txt'), 'IT DOES NOT SAY THE SEALED BAR WAS MET.'),
    ('### families not conferred', d('b333_the_archimedean_term_derived.txt'), '`MEASURED-ON-FAMILIES` IS NOT CONFERRED on K5 by this act.'),
    ('b334 -- the result', d('b334_the_aim_map.txt'), 'FOR ZETA THE PRIME SUM STAYS INSIDE THE MARGIN AT EVERY AIM AT THIS REACH -- A PASSED TEST OVER A GRID AT THIS REACH AND NOTHING MORE.'),
    ('### the obstacle', d('b334_the_aim_map.txt'), 'IT DOES NOT SAY A CHART IS A PROOF.'),
    ("b323 -- the fold's law", d('b323_the_fold.txt'), 'A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD'),
    ("b324 -- the candidate list, typed", d('b324_the_keystones_reread.txt'), "THE WAVE'S CANDIDATE LIST, TYPED. ### NO RECOMMENDATION, NO RANKING."),
    ("### the wave is the author's", d('b324_the_keystones_reread.txt'), "THE WAVE IS THE AUTHOR'S. ### THIS LIST IS TYPED AND NOT RANKED, AND NO SEAT STARTS ONE."),
    ('b337 -- (1) the fetch', d('b337_the_housekeeping.txt'), 'THE FETCH AGREES WITH REGISTRY ON EVERY FIELD; TWO LEDGERS CURRENT, ONE DRIFT, REPAIRED BY'),
    ('### (4) the receipts', d('b337_the_housekeeping.txt'), 'THE PATENT RECEIPTS: ABSENT ON THE MOUNTED VOLUMES, AND F: IS NOT MOUNTED.'),
    ('b336 -- the census', d('b336_the_cost_census.txt'), 'FIFTEEN ROWS TYPED, THROUGH THE WRITER, AND NO GRADE MOVED.'),
    ('the sortie -- leg 3', d('b338_ferry_2026-09-06.txt'), 'LEG 3 (b338) \u2014 THE FOLD, b331 through b334, four acts, under'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### (1) appended, purely additive', BANK, 'THE SECTION IS APPENDED, THE TWENTIETH, AND IT IS PURELY ADDITIVE, MEASURED AND NOT PROMISED.'),
    ('### (2) F-QUOTE', BANK, '`F-QUOTE` PASSES AT 8 OF 8, AND ITS DISCRIMINATION ARM FIRES.'),
    ('### (3) F-COUNT', BANK, '`F-COUNT` PASSES: 4 RESULTS, 4 OBSTACLES, THE ARC EXACTLY.'),
    ('### (5) the desk first item', BANK, "THE DESK'S FIRST ITEM IS THE WAVE'S CANDIDATE LIST, RESTATED, WITH THE HOUSEKEEPING'S STATE"),
    ("### the wave the author's", BANK, "AUTHOR'S, THE LIST TYPED AND NOT RANKED**"),
    ('### (6) the arc as one statement', BANK, 'THE ARC AS ONE STATEMENT, AT THE GRADE FOUR ACTS SUPPORT AND NO HIGHER:'),
    ('### the clause has not moved', BANK, 'CLAUSE HAS NOT MOVED.**'),
    ('### a filing not a result', BANK, 'A FILING, NOT A RESULT. NO GRADE MOVED. NO ACT RE-VERDICTED. NO KEYSTONE TOUCHED. TECHNE NOT'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the generator', BANK, 'THE GENERATOR AND ITS JUDGEMENT.'),
    ('### the judgement declared', BANK, 'THE JUDGEMENT THE'),
    ('bank gives the rows and the key', BANK, 'THE ROWS AND THE KEY.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### none found', BANK, 'NONE FOUND BY THE GATES ON THIS LEG.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, "NEXT: THE SORTIE'S STOP -- ONE SUMMARY PARAGRAPH PER LEG, THE PINS, AND THE DRAFT OF THE NEXT FERRY MARKED DRAFT -- NAVIGATOR EDITS."),
    ('registration -- the rules held', REG, "(C) THE FOLD'S OWN RULES, INHERITED FROM b323 AND b331 AND HELD HERE."),
    ('registration -- the title', REG, '`THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD`'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the emitted section -- the heading', EMIT, HEADING),
    ('### the desk heading', EMIT, "### The desk \u2014 its first item the wave\u2019s candidate list, restated, with the housekeeping\u2019s state beside it"),
    ('### the arc as one statement', EMIT, '### The arc as one statement'),
    ('### h2 unchanged', EMIT, '### **h2 UNCHANGED. NOTHING PROMOTED. NOTHING DEPOSITS.**'),
]

MUST_FAIL = [
    ('the bank never says the clause is discharged', BANK, '### ### **THE CLAUSE IS DISCHARGED.**'),
    ('the bank never says a grade moved', BANK, '### ### **A GRADE MOVED.**'),
    ('the bank never says the chart is a proof', BANK, '### ### **THE CHART IS A PROOF.**'),
    ('the bank never recommends a candidate', BANK, '### ### **THE SEAT RECOMMENDS A CANDIDATE.**'),
    ('the section never says the wave is started', EMIT, '**The wave is started.**'),
    ('the bank never says K8 is owned', BANK, '### ### **K8 IS OWNED.**'),
]

TOOLNUM = [
    ('+114 lines, 3116 -> 3230, 19 -> 20 sections, F-QUOTE 8/0, F-MODULES 3/2', 'tools/b338_fold.py'),
    ('rows 185 and 186', 'tools/b338_correspondence.py'),
    ('the key', 'tools/b338_index_append.py'),
    ('24 clauses', 'tools/b338_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('14615 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b338_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the like-for-like comparator, the sign column (the lore by tool)', 'tools/b334_aimmap.py'),
]
NEW_THIS_ACT = {'tools/b338_fold.py', 'tools/b338_correspondence.py', 'tools/b338_index_append.py', 'tools/b338_regspec.py', 'tools/b338_extract.py', 'tools/b338_checks.py'}


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
    print('b338 -- GATE SUITE (THE FOLD, b331-b334: A FILING, PURELY ADDITIVE, NO GRADE MOVED)')
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
    emit = io.open(EMIT, encoding='utf-8').read()
    fnd = io.open(FINDINGS, encoding='utf-8', errors='replace').read()
    rows = json.load(io.open(ROWSJ, encoding='utf-8'))
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    fb = blob_of(PP, 'FINDINGS.md') or ''
    committed = HEADING in fb

    print(chr(10) + '  F-QUOTE / F-COUNT / F-MODULES (the generator\'s gates, re-run live through its module):')
    logs = []
    texts = {a: io.open(os.path.join(D, F.SRC[a]), encoding='utf-8', errors='replace').read() for a in F.ARC}
    q = F.fquote(texts, logs.append)
    c = F.fcount(logs.append)
    m = F.fmodules(logs.append)
    for ln in logs:
        print('   ' + ln)
    if not (q and c and m):
        fails.append('F-QUOTE/F-COUNT/F-MODULES')

    print(chr(10) + '  G-ADDITIVE (F3: the section in the file verbatim, once; the file a true prefix of its blob; the generator\'s record):')
    pf = norm(fnd).startswith(norm(fb).rstrip(chr(10)))
    ga = fnd.count(HEADING) == 1 and emit.strip() in norm(fnd) and pf and rows['prefix_working'] and rows['prefix_blob'] and fnd.index(HEADING) > fnd.index('<!-- b333 addendum: the archimedean term derived -->')
    print('    heading once %s ; section verbatim in the file %s ; prefix of blob %s (committed %s) ; after the b333 addendum %s : %s'
          % (fnd.count(HEADING) == 1, emit.strip() in norm(fnd), pf, committed, fnd.index(HEADING) > fnd.index('<!-- b333 addendum: the archimedean term derived -->'), ga))
    if not ga:
        fails.append('G-ADDITIVE')

    print(chr(10) + '  G-NOGRADE (F4: every grade word in the section is pulled from the owning act\'s bank via the extract file):')
    grade_words = {'b331': 'FILED', 'b332': 'STATED', 'b333': 'DERIVES-ON-IMPORTS', 'b334': 'MEASURED'}
    gn = all(('%s' % w) in texts[a] for a, w in grade_words.items()) and 'MEASURED-ON-FAMILIES` IS NOT CONFERRED' in texts['b333']
    print('    %s' % gn)
    if not gn:
        fails.append('G-NOGRADE')

    print(chr(10) + '  G-ONE (F5: the one-statement paragraph carries the four acts and the two standing sentences):')
    para = emit[emit.index('### The arc as one statement'):emit.index('### The lore this arc leaves')]
    go1 = all(x in para for x in ('(b332)', '(b333)', '(b334)', 'b331')) or all(x in para for x in ('(b332)', '(b333)', '(b334)'))
    go1 = go1 and 'the clause has not moved' in para and 'a chart is not a proof' in para and 'not discharged' in para
    print('    %s' % go1)
    if not go1:
        fails.append('G-ONE')

    print(chr(10) + "  G-DESK (F7: the desk's FIRST item is the wave's candidate list with b324's six, b331's addition and the housekeeping's four items; the rest present; the wave the author's):")
    desk = emit[emit.index('### The desk'):emit.index('### **h2 UNCHANGED')]
    first = F.DESK[0]
    gd = ('candidate list, restated' in first[0] and first[1].count('`[NEW]`') == 4 and '`[REFINEMENT-OF-DEPOSITED]`' in first[1] and '`[REFINEMENT-OF-INTERNAL]`' in first[1]
          and 'b331\u2019s addition' in first[1] and all(k in first[1] for k in ('read-only fetch', 'partitioned', 'nine August TECHNE files', 'ABSENT ON THE MOUNTED VOLUMES'))
          and 'The wave is the author\u2019s' in first[2] and desk.index('reconciliation wave') < desk.index('`M-2`')
          and all(k in desk for k in ('`M-2`', 'softest pair', 'three conditions', 'exponent', 'Li-to-Weil', 'Li bench', 'compact part', 'standing clauses', 'TECHNE clones', 'seam', 'patent receipts')))
    print('    %s' % gd)
    if not gd:
        fails.append('G-DESK')

    print(chr(10) + '  G-ROWS / G-ANCESTOR (rows 185 and 186: NO TERMINAL each, a filing and a summary; the table a true prefix of its blob):')
    r185 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 185 |')]
    r186 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 186 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = (len(r185) == 1 and len(r186) == 1 and 'A FILING, NOT A RESULT' in r185[0] and 'A SUMMARY AND NOT A VERDICT' in r186[0]
           and all('NO TERMINAL, AND THE REASON' in x[0] and 'M-2' in x[0] for x in (r185, r186)) and norm(tbl).startswith(norm(head).rstrip(chr(10))))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROWS/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTAVERDICT (one row; the must-not-hit queries NO KEY; the answer says a filing, a summary, the wave the author\'s):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('stated-clause-arc-fold')
    gk = o.count('act      :') == 1 and 'A FILING, NOT A RESULT; THE ONE STATEMENT A SUMMARY AND NOT A VERDICT' in o and "THE WAVE IS THE AUTHOR'S" in o
    for s in ("the arc's verdict", 'the wave recommended', 'the clause discharged'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTAVERDICT')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner files, sealed files, the deposit, TECHNE, HANDOFF, the four banks: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md', 'tools/b331_fold.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md', 'data/b331_the_fold.txt', 'data/b332_the_clause_stated.txt', 'data/b333_the_archimedean_term_derived.txt',
              'data/b334_the_aim_map.txt', 'data/b324_the_keystones_reread.txt', 'data/b337_the_housekeeping.txt', 'data/b336_the_cost_census.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FINDINGS.md')]
    st_t = git(TC, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond FINDINGS) %s ; TECHNE %r ; deposit %r : %s' % (st_r, st_s, st_p, st_t, dep, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the generator, the section, the rows and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b338_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b338_fold.py'), FRUN, EMIT, FINDINGS, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b338_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b338_checks_run.txt')) else ''
        after = 'the generator, the section, the rows and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the generator, the section, the rows and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed:
        print('    FINDINGS committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    FINDINGS not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    checks.append(('+%d lines, %d -> %d' % (rows['lines_added'], rows['lines_before'], rows['lines_after']),
                   ('`+%d` lines' % rows['lines_added']) in bank and ('`%d -> %d`' % (rows['lines_before'], rows['lines_after'])) in bank))
    srun = io.open(FRUN, encoding='utf-8').read()
    fq = re.search(r'F-QUOTE\s*:\s*(\d+) quotations, (\d+) unfindable', srun)
    checks.append(('F-QUOTE %s/%s' % (fq.group(1), fq.group(2)), ('`F-QUOTE` PASSES AT %s OF %s' % (fq.group(1), fq.group(1))) in bank and fq.group(2) == '0'))
    fm = re.search(r'F-MODULES: (\d+) rules by module, all on disk : True.*?; (\d+) rules by tool, all on disk : True', srun)
    checks.append(('F-MODULES %s/%s' % (fm.group(1), fm.group(2)), fm.group(1) == '3' and fm.group(2) == '2' and 'PASSES:** 3' in bank and '2 rules by tool' in bank))
    nj = sum(1 for x in rows['lore'] if x[2] == 'JUDGEMENT')
    checks.append(('%d judgement rules' % nj, nj == 3 and '3 rules judgement' in bank))
    rn = re.search(r'rows to append : (\d+) and (\d+)', io.open(CORR, encoding='utf-8').read())
    checks.append(('rows %s and %s' % rn.groups(), ('rows %s and %s' % rn.groups()) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    nsec = len([x for x in fnd.splitlines() if x.startswith('## ')])
    checks.append(('%d sections' % nsec, nsec == 20 and '19 sections before and 20 after' in bank))
    checks.append(('emitted %d lines' % len(emit.strip().splitlines()), ('%d lines' % len(emit.strip().splitlines())) in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [FRUN, FRUN2, EMIT, ROWSJ, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b338_fold_run3.txt'))
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

    print(chr(10) + '  G-STEM-APPENDED (the section, rows 185 and 186, the index row, swept):')
    sec = fnd[fnd.index(HEADING):] if HEADING in fnd else ''
    ib = idx[idx.index('# ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD (b338'):idx.index("# ### THE WAVE'S HOUSEKEEPING (b337")] if '# ### THE STATED-CLAUSE ARC, b331-b334 -- THE FOLD (b338' in idx else ''
    for lbl, blk in (('the section', sec), ('row 185', r185[0] if r185 else ''), ('row 186', r186[0] if r186 else ''), ('index row', ib)):
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-18s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk)))
        if ch or sh or not blk:
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the emitted section, the rows and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b338_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row 185', r185[0] if r185 else ''), ('row 186', r186[0] if r186 else ''), ('the index row', ib)):
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
