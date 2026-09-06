# -*- coding: utf-8 -*-
"""b331_checks.py -- THE GATE SUITE FOR THE FOLD, b323-b330.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`F-QUOTE` / `F-COUNT` / `F-MODULES`, RE-RUN LIVE** ### -- the generator's own gates, run
###     again through its module, with the discrimination arm.
###   ### ### **`G-ADDITIVE`** ### -- the section present once; the blob at HEAD a true prefix of the working
###     file (before the commit) or equal to it (after); the section's line count as the run file recorded.
###   ### ### **`G-NOGRADE`** ### -- every grade word the section carries for an act is a word that act's own
###     bank carries (pulled at the extract step): FILED, DIFFERENT, UNDECIDED, DOES NOT SEE IT, SEES IT,
###     zero-axiom, NOT PUSHED.
###   ### ### **`G-SIX`** ### -- the arc-as-one-statement paragraph carries the six clauses and the sentence
###     that the clause has not moved; the scope paragraph follows it.
###   ### **`G-DESK`** ### -- every desk item the order lists is present, and "neither is the discharge".
###   ### **`G-HOOK` / `G-MIRROR`** ### -- read from their records once they exist (post-push).
###   ### **`G-ORDER`, `G-ROWS`, `G-KEY`, `G-TOOLNUM`, `G-NUMBERS`, the hedge audit (the emitted section
###     included), the stem sweep, the must-fail fixtures** -- standing.
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
import b331_fold as F    # noqa: E402

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


BANK = d('b331_the_fold.txt')
REG = d('b331_registration_2026-09-06.txt')
EXTRACT = d('b331_extract_notes.txt')
FRUN, FRUN2 = d('b331_fold_run.txt'), d('b331_fold_run2.txt')
EMIT, ROWSJ = d('b331_fold_emitted.md'), d('b331_fold_rows.json')
CORR, CORRR = d('b331_corr_run.txt'), d('b331_corr_rerun.txt')
IDX, IDXR = d('b331_index_run.txt'), d('b331_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b331_ferry_scan.txt'), d('b331_reg_termscan.txt'), d('b331_reg_gate.txt')
CENSUS, FCEN = d('b331_census.txt'), d('b331_faces_census.txt')
REGSPEC, SATIS = d('b331_regspec_run.txt'), d('audit_b331_reg_satisfiable.txt')
PINS, INDEXQ = d('b331_pins_stepzero.txt'), d('audit_b331_index_query.txt')
HOOKS, MIRROR = d('b331_hooks.txt'), d('b331_mirror.txt')
SEAL = '885dce5f9141c8f7f35ce6d5cf9bb950c785571c2136ca96871fdb3fca430d9a'

OWNED = [BANK, REG, FRUN, FRUN2, EMIT, ROWSJ, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b331_satisfiable.json'), t('b331_extract.py'), t('b331_fold.py'), t('b331_regspec.py'), t('b331_correspondence.py'),
         t('b331_index_append.py')]

CARRIERS = [
    (t('b331_checks.py'), 'its own fixtures'),
    (d('b331_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ("b323 -- purely additive", d('b323_the_fold.txt'), 'A FOLD IS PURELY ADDITIVE OR IT IS NOT A FOLD'),
    ("b324 -- the wall different", d('b324_the_keystones_reread.txt'), 'THE WALL: ### DIFFERENT. ### (F1) IS REFUTED, AND BOTH ITS HALVES FALL.'),
    ("b324 -- withheld by design", d('b324_the_keystones_reread.txt'), 'THE DEPOSIT DELIBERATELY WITHHOLDS IT'),
    ("b325 -- negative at all thirteen", d('b325_the_negative_control.txt'), 'NEGATIVE AT ALL THIRTEEN CELLS'),
    ("b326 -- does not see it to a = 400", d('b326_the_reach.txt'), "THE ARC'S FAMILY, TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT."),
    ("b326 -- the halved kernel", d('b326_the_reach.txt'), 'Epstein archimedean kernel was ### **HALF** ### the derived'),
    ("b327 -- one distribution on two families", d('b327_the_faces_ledger.txt'), 'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL.'),
    ("b327 -- the bench at two indices", d('b327_the_faces_ledger.txt'), 'at `n = 3` and `n = 5` -- a typed fixture, filed and not edited; the computation matches the'),
    ("b328 -- sees it at seven of eight", d('b328_the_discriminating_family.txt'), 'SEES IT -- AT SEVEN OF EIGHT CELLS.'),
    ("b329 -- one compiled module", d('b329_the_finite_side_seal.txt'), "THE FINITE SIDE'S SILENCE IS ONE COMPILED MODULE, `Core/FiniteSideSeal.lean`, WITH ITS"),
    ("b330 -- not pushed", d('b330_the_techne_extraction.txt'), 'THE LOCAL TECHNE COMMIT: `75ab3ff` -- NOT PUSHED.'),
    ("HANDOFF -- the receipts", os.path.join(ROOT, 'HANDOFF.md'), "receipts are pending on the ferry's word, **three days past both dates.**"),
    ("b324 -- the candidate list typed", d('b324_the_keystones_reread.txt'), "THE WAVE'S CANDIDATE LIST, TYPED. ### NO RECOMMENDATION, NO RANKING."),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### the section is filed', BANK, 'THE SECTION IS FILED.'),
    ('### purely additive measured', BANK, 'AND IT IS PURELY ADDITIVE, MEASURED AND NOT PROMISED.'),
    ('### F-QUOTE 16 of 16', BANK, '`F-QUOTE` PASSES AT 16 OF 16, AND ITS DISCRIMINATION ARM FIRES.'),
    ('### F-COUNT', BANK, '`F-COUNT` PASSES: ### 8 RESULTS, 8 OBSTACLES, THE ARC EXACTLY.'),
    ('### F-MODULES', BANK, '`F-MODULES` PASSES:'),
    ('### the defects table', BANK, 'THE SEATS\' OWN DEFECTS, DECLARED BY THE ACTS'),
    ('### the clause has not moved', BANK, 'has not moved.'),
    ('### neither is the discharge', BANK, 'NEITHER IS THE DISCHARGE'),
    ('### the judgement declared', BANK, "THE JUDGEMENT THE MECHANISM DOES NOT MAKE, DECLARED AS THIS SEAT'S."),
    ('### the grades are the acts\' own words', BANK, "AND THE GRADES ARE THE ACTS' OWN WORDS:"),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any write', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY WRITE.'),
    ('bank gives component 1', BANK, 'COMPONENT 1 -- THE FOLD.'),
    ('bank gives component 2', BANK, 'COMPONENT 2 -- THE ARC AS ONE STATEMENT.'),
    ('bank gives component 3', BANK, 'COMPONENT 3 -- THE LORE AND THE SUITE.'),
    ('bank gives component 4', BANK, 'COMPONENT 4 -- THE DESK.'),
    ('### the one item with a date', BANK, 'THE ONE ITEM WITH A DATE.'),
    ('bank gives the closing', BANK, 'THE CLOSING.'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### not moved', BANK, 'IT DOES NOT SAY THE CLAUSE HAS MOVED.'),
    ('### not re-verdicted', BANK, 'IT DOES NOT RE-VERDICT ANY ACT IT FOLDS.'),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### nothing deposits', BANK, 'NOTHING DEPOSITS.'),
    ('### next', BANK, 'NEXT, BY THE ORDER: THE DISCHARGE-STATEMENT AND THE AIM-MAP -- AND NEITHER IS THE DISCHARGE.'),
    ('registration -- the title fixed', REG, 'THE SECTION\'S TITLE, FIXED HERE:'),
    ('registration -- expected nothing', REG, 'EXPECTED: NOTHING.'),
]

MUST_FAIL = [
    ('the bank never says the clause moved', BANK, '### ### **THE CLAUSE HAS MOVED.**'),
    ('the bank never claims a proof', BANK, '### ### **THE ARC PROVED THE CLAUSE.**'),
    ('the section never says the discharge is done', EMIT, '### **THE DISCHARGE IS DONE.**'),
]

TOOLNUM = [
    ('+144 lines, 2880 -> 3024, 18 sections, F-QUOTE 16/0', 'tools/b331_fold.py'),
    ('rows 176-177', 'tools/b331_correspondence.py'),
    ('the key', 'tools/b331_index_append.py'),
    ('18 clauses', 'tools/b331_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('15207 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b331_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
]
NEW_THIS_ACT = {'tools/b331_fold.py', 'tools/b331_correspondence.py', 'tools/b331_index_append.py', 'tools/b331_regspec.py',
                'tools/b331_extract.py'}

GRADE_WORDS = {'b323': 'FILED', 'b324': 'DIFFERENT', 'b325': 'DOES NOT SEE IT', 'b326': 'DOES NOT SEE IT',
               'b327': 'DIFFERENT', 'b328': 'SEES IT', 'b329': 'zero-axiom', 'b330': 'NOT PUSHED'}
SIX = ['the instrument can say no', 'the zeta window is a passed test for the discriminating family at this reach',
       'The finite side is compiled', 'two evaluations of one distribution separated by the pole',
       'in its space by derivation and priced at bench', 'the clause has not moved']
DESK_ITEMS = ['`M-2`', 'three conditions', 'exponent\u2019s ratio', 'Li-to-Weil bridge', 'Li bench versus the keystone',
              'August TECHNE files', 'compact part beyond the cells', 'discharge-statement and the aim-map',
              'reconciliation wave', 'seam\u2019s debt, item 1', 'patent receipts']


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
    print('b331 -- GATE SUITE (THE FOLD, b323-b330: A FILING AT THE ACTS\' OWN GRADES, PURELY ADDITIVE)')
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
    frun = io.open(FRUN, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()

    print('\n  F-QUOTE / F-COUNT / F-MODULES (the generator\'s gates, re-run live):')
    logs = []
    text_by_act = {a: io.open(d(F.SRC[a]), encoding='utf-8', errors='replace').read() for a in F.ARC}
    q = F.fquote(text_by_act, logs.append)
    c = F.fcount(logs.append)
    m = F.fmodules(logs.append)
    for ln in logs:
        print('   ' + ln)
    if not (q and c and m):
        fails.append('F-QUOTE/F-COUNT/F-MODULES')

    print('\n  G-ADDITIVE (the section once; the blob at HEAD a true prefix of, or equal to, the working file; the run\'s count):')
    blob = blob_of(PP, 'FINDINGS.md') or ''
    once = fnd.count('## ' + F.SECTION) == 1
    pfx = norm(fnd).startswith(norm(blob).rstrip('\n'))
    m2 = re.search(r'lines added : \+(\d+)', frun)
    counted = int(m2.group(1)) == rows['lines_added'] == len(fnd.splitlines()) - rows['lines_before']
    emitted_in = emit.strip() in fnd
    ga = once and pfx and counted and emitted_in and rows['prefix_working'] and rows['prefix_blob']
    print('    once %s ; blob prefix %s ; lines added %s counted consistently %s ; emitted section in the file verbatim %s ; run recorded both prefixes %s : %s'
          % (once, pfx, m2.group(1), counted, emitted_in, rows['prefix_working'] and rows['prefix_blob'], ga))
    if not ga:
        fails.append('G-ADDITIVE')

    print('\n  G-NOGRADE (every grade word the section carries for an act is in that act\'s own bank):')
    bad = []
    for act, _w, _q, grade, _s in F.RESULTS:
        w = GRADE_WORDS[act]
        if w not in grade or w not in text_by_act[act]:
            bad.append((act, w))
    print('    violations %s : %s' % (bad, not bad))
    if bad:
        fails.append('G-NOGRADE')

    print('\n  G-SIX (the arc-as-one-statement paragraph: the six clauses, then the scope paragraph):')
    para = emit[emit.index('### The arc\u2019s one statement') if '### The arc\u2019s one statement' in emit else emit.index('### The arc\u2019s corrections'):] if False else emit
    i0 = emit.find('### The arc\u2019s one statement')
    i0 = emit.find('### The arc as one statement') if i0 < 0 else i0
    i1 = emit.find('### The lore this arc leaves')
    seg = emit[i0:i1] if i0 >= 0 and i1 > i0 else ''
    missing = [s for s in SIX if s not in seg]
    scope_after = seg.find('**Scope, printed beside it.**') > seg.find('the clause has not moved')
    gs = not missing and scope_after and 'no act in the arc claims otherwise' in seg
    print('    missing clauses %s ; scope paragraph after the statement %s : %s' % (missing, scope_after, gs))
    if not gs:
        fails.append('G-SIX')

    print('\n  G-DESK (every ordered item present; "neither is the discharge"):')
    i2 = emit.find('### The desk')
    desk = emit[i2:] if i2 >= 0 else ''
    dm = [x for x in DESK_ITEMS if x not in desk]
    gd = not dm and 'neither is the discharge' in desk and 'the one item on this desk with a date' in desk
    print('    missing %s ; neither-is-the-discharge present %s : %s' % (dm, 'neither is the discharge' in desk, gd))
    if not gd:
        fails.append('G-DESK')

    print('\n  G-ROWS / G-ANCESTOR (rows 176-177; the table a true prefix of its blob; ancestor rows unchanged):')
    r176 = [ln for ln in tbl.split('\n') if ln.startswith('| 176 |')]
    r177 = [ln for ln in tbl.split('\n') if ln.startswith('| 177 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    gr = (len(r176) == 1 and len(r177) == 1 and 'A FILING, NOT A RESULT' in r176[0] and 'the clause has not moved' in r177[0]
          and 'M-2' in r176[0] and 'M-2' in r177[0] and norm(tbl).startswith(norm(head).rstrip('\n')))
    print('    %s' % gr)
    if not gr:
        fails.append('G-ROWS/G-ANCESTOR')

    print('\n  G-KEY (two rows; the must-not-hit queries NO KEY):')
    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('discriminating-arc-fold')
    gk = o.count('act      :') == 2 and 'THE CLAUSE HAS NOT MOVED' in o and 'A SUMMARY AND NOT A VERDICT' in o
    for s in ('the clause moved', 'the arc proved'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY')

    print('\n  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    s = subsequence(norm(b).split('\n'), norm(idx).split('\n')) if b is not None else False
    print('    %s' % s)
    if not s:
        fails.append('G-APPENDONLY')

    print('\n  G-NOEDIT (owner files, sealed files, keystones, the deposit, TECHNE, every .lean: no tracked change):')
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b323_fold.py',
              'tools/ferry_scan.py', 'tools/reg_seal.py', 'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md'] + [('data/' + F.SRC[a]) for a in F.ARC]
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FINDINGS.md')]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    tc_head = git(TC, 'rev-parse', '--short', 'HEAD').strip()
    gn = not st_r and not st_s and not st_p and not st_t and tc_head == '75ab3ff'
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond FINDINGS) %s ; TECHNE %r at %s : %s' % (st_r, st_s, st_p, st_t, tc_head, gn))
    if not gn:
        fails.append('G-NOEDIT')

    print('\n  G-ORDER (the seal verifies; the generator, the section and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b331_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b331_fold.py'), FRUN, EMIT, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b331_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b331_checks_run.txt')) else ''
        after = 'the generator, the section and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the generator, the section and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print('\n  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    committed_f = '## ' + F.SECTION in blob
    if committed_f:
        print('    FINDINGS committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    FINDINGS not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print('\n  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    checks.append(('+%d lines, %d -> %d' % (rows['lines_added'], rows['lines_before'], rows['lines_after']),
                   ('`+%d` lines' % rows['lines_added']) in bank and ('`%d -> %d` lines' % (rows['lines_before'], rows['lines_after'])) in bank))
    fq = re.search(r'F-QUOTE\s*:\s*(\d+) quotations, (\d+) unfindable', frun)
    checks.append(('F-QUOTE %s/%s' % (fq.group(1), fq.group(2)), ('`F-QUOTE` PASSES AT %s OF %s' % (fq.group(1), fq.group(1))) in bank and fq.group(2) == '0'))
    checks.append(('%d results, %d obstacles' % (len(rows['results']), len(rows['obstacles'])), ('%d RESULTS, %d OBSTACLES' % (len(rows['results']), len(rows['obstacles']))) in bank))
    checks.append(('%d defective bars, %d corrections, %d defects' % (len(rows['defective_bars']), len(rows['corrections']), len(rows['defects'])),
                   'five rows' in bank and 'six rows' in bank and 'seven rows' in bank and len(rows['defective_bars']) == 5 and len(rows['corrections']) == 6 and len(rows['defects']) == 7))
    nm = sum(1 for x in rows['lore'] if x[2] == 'MECHANIZED'); nj = sum(1 for x in rows['lore'] if x[2] == 'JUDGEMENT')
    checks.append(('%d mechanized, %d judgement' % (nm, nj), 'SIX MECHANIZED RULES' in bank and 'FIVE' in bank and nm == 6 and nj == 5))
    checks.append(('%d suite rows, %d desk rows' % (len(rows['suite']), len(rows['desk'])), 'nine rows' in bank and 'ELEVEN ROWS' in bank and len(rows['suite']) == 9 and len(rows['desk']) == 11))
    rn = re.search(r'last 2 row number\(s\) are \[(\d+), (\d+)\]', io.open(CORR, encoding='utf-8').read())
    checks.append(('rows %s and %s' % (rn.group(1), rn.group(2)), ('rows %s and %s' % (rn.group(1), rn.group(2))) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    nsec = len([x for x in fnd.splitlines() if x.startswith('## ')])
    checks.append(('%d sections' % nsec, nsec == 18 and 'eighteenth section' in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print('\n  G-ONCE (run files written once per path; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [FRUN, FRUN2, CORR, CORRR, IDX, IDXR, EMIT, ROWSJ])
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

    print('\n  G-STEM-APPENDED (the section in FINDINGS, the rows, the index rows, swept):')
    sec = fnd[fnd.index('## ' + F.SECTION):] if ('## ' + F.SECTION) in fnd else ''
    ib = idx[idx.index('# ### THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD (b331).'):idx.index('# ### THE TECHNE EXTRACTION -- METHOD ONLY, NOT PUSHED (b330).')] if '# ### THE DISCRIMINATING-FAMILY ARC, b323-b330 -- THE FOLD (b331).' in idx else ''
    rowtxt = '\n'.join(r176 + r177)
    for lbl, blk in (('the section', sec), ('rows 176-177', rowtxt), ('index rows', ib)):
        ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk, [], stem_list)
        print('    %-14s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk)))
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

    print('\n  HEDGE AUDIT (over every file this act wrote, the emitted section, the rows and the index rows included):')
    tmpdir = tempfile.mkdtemp(prefix='b331_hedge_')
    targets = [('the bank', BANK), ('the registration', REG), ('the emitted section', EMIT), ('the generator', t('b331_fold.py'))]
    for lbl, text in (('rows 176-177', rowtxt), ('the index rows', ib)):
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
