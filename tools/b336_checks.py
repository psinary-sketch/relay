# -*- coding: utf-8 -*-
"""b336_checks.py -- THE GATE SUITE FOR THE COST CENSUS.

### ### **THE ARMS (registration (E), F1-F7):** `G-COST`, `G-NOGRADE`, `G-L2`, `G-ADDENDUM`, `G-PRICES`, `G-ROW`, `G-KEY` /
### `G-NOTAGRADE`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOEDIT`, `G-APPENDONLY`, the
### hedge audit, the stem sweep at extended scope, the must-fail fixtures; re-run after the push.
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
import b336_cost as CT   # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b336_the_cost_census.txt')
REG = d('b336_registration_2026-09-06.txt')
EXTRACT = d('b336_extract_notes.txt')
CRUN, CRUN2, CRER, CRER2, SORTED = d('b336_cost_run.txt'), d('b336_cost_run2.txt'), d('b336_cost_rerun.txt'), d('b336_cost_rerun2.txt'), d('b336_cost_sorted.txt')
CORR, CORRR = d('b336_corr_run.txt'), d('b336_corr_rerun.txt')
IDX, IDXR = d('b336_index_run.txt'), d('b336_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b336_ferry_scan.txt'), d('b336_reg_termscan.txt'), d('b336_reg_gate.txt')
CENSUS, FCEN = d('b336_census.txt'), d('b336_faces_census.txt')
REGSPEC, SATIS = d('b336_regspec_run.txt'), d('audit_b336_reg_satisfiable.txt')
PINS, INDEXQ = d('b336_pins_stepzero.txt'), d('audit_b336_index_query.txt')
HOOKS, MIRROR = d('b336_hooks.txt'), d('b336_mirror.txt')
SEAL = '2297b0d9910085dba16bd6d4c7014184a26a5d826bf3e3b9c457a696b4253642'
MARK_C, MARK_A = CT.MARK_C, CT.MARK_A

OWNED = [BANK, REG, CRUN, CRUN2, CRER, CRER2, SORTED, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b336_satisfiable.json'), t('b336_extract.py'), t('b336_regspec.py'), t('b336_cost.py'), t('b336_correspondence.py'), t('b336_index_append.py')]

CARRIERS = [
    (t('b336_checks.py'), 'its own fixtures'),
    (d('b336_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
]

OWNER_NEEDLES = [
    ('ledger -- the column law', LEDGER, '**THE COLUMN LAW.** `id`'),
    ('### row S1', LEDGER, '| S1 | S1 -- '),
    ('### row L1', LEDGER, '| L1 | L1 -- '),
    ("### b328's update block", LEDGER, '<!-- b328 update -->'),
    ("b322 -- the unit's domain factor", d('b322_the_membership.txt'), '### ### **`3.104e+02`.** ### **THAT IS AN EXTRAPOLATION OF A FITTED SLOPE AND IT IS LABELLED AS'),
    ("b321 -- the exponent's ratio", d('b321_the_window_opened.txt'), 'than either lies to the equality: they are apart by between one twenty-fourth and one fifth of'),
    ("b321_run -- the instrument's acts, imported", t('b321_run.py'), 'import b316_instrument as INS'),
    ('### b321', t('b321_run.py'), 'import b321_window as WI'),
    ('b328 -- the crossing widths', d('b328_family_run.txt'), "**VERDICT : SEES IT** at [('E', 40.0), ('E', 81.0), ('E', 160.0), ('O', 20.0), ('O', 40.0), ('O', 81.0), ('O', 160.0)]"),
    ('b334 -- the crossing region', d('b334_the_aim_map.txt'), 'THE EPSTEIN CROSSING REGION -- THE NEGATIVE CONTROL CHARTED -- IS THREE AIMS:'),
    ('b327 -- the pole-at-zero constant', d('b327_the_faces_ledger.txt'), 'the archimedean place PLUS the pole-at-zero constant -- *"log s"* in the keystone\'s own split,'),
    ('### the fold: one distribution, the pole constant 1', FINDINGS, 'The deposit\u2019s archimedean channel is the archimedean distribution on the Li family plus the pole constant `1`; the two margins are two'),
    ('### row L1 carries the derivation', LEDGER, 'gives \u03bb_A(n) = S\u221e(n) + 1 for every n \u2265 1 -- the gamma factor is exactly the source\'s archimedean term and `log s` is exactly the source\'s pole constant.'),
    ('b334 bank -- the threshold rule is not the sign condition', d('b334_the_aim_map.txt'), 'THE SEALED THRESHOLD RULE IS NOT THE SIGN CONDITION, AND THE MAP SAYS SO.'),
    ("b334 chart -- the sign column", d('b334_chart_run.txt'), "(* = the phase exceeds 45 deg at that beta: REACHED ; the trailing sign is the quadruple's term S_4 = 4 |G|^2 cos 2 phi, negative only between 45 and 135 degrees)"),
    ('b328 bank -- the rule as b328 stated it', d('b328_the_discriminating_family.txt'), 'NEGATIVE EXACTLY PAST FORTY-FIVE DEGREES OF PHASE**;'),
    ('the writer -- write_row', t('b327_faces_row.py'), 'def write_row(row):'),
    ('### append_block', t('b327_faces_row.py'), 'def append_block(mark, body_lines):'),
    ('the sortie -- leg 1', d('b336_ferry_2026-09-06.txt'), 'LEG 1 (b336) \u2014 THE COST CENSUS: a typed cost column on the'),
    ('### no grade moved', d('b336_ferry_2026-09-06.txt'), "chart's sign column cited). No grade moved."),
]

SELF_NEEDLES = [
    ('bank states the census first', BANK, 'THE CENSUS, FIRST.'),
    ('### (1) fifteen rows typed', BANK, 'FIFTEEN ROWS TYPED, THROUGH THE WRITER, AND NO GRADE MOVED.'),
    ('### no read or import as the next step', BANK, 'NO ROW HOLDS A READ OR AN IMPORT AS ITS NEXT'),
    ('### (2) the four prices', BANK, 'THE FOUR PRICES, AT THEIR EMITTERS.'),
    ('### (3) row L2', BANK, 'ROW L2, THE POLE-CONSTANT RELATION, STATED, COST ZERO.'),
    ('### (4) the phase rule', BANK, "THE PHASE RULE REFINED, AS AN ADDENDUM TO b328's BLOCK."),
    ('### no grade moved', BANK, 'NO GRADE MOVED. ### A COST IS NOT A GRADE, NOT A PLAN, NOT A PREDICTION. ### NOTHING DEPOSITS.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the tool and its runs', BANK, 'THE CENSUS TOOL AND ITS RUNS.'),
    ('bank gives the row and the key', BANK, 'THE ROW AND THE KEY.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1', BANK, "E1 -- ONE SENTENCE ATTRIBUTED TO FINDINGS IS b331's BANK'S."),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, "NEXT, BY THE SORTIE: LEG 2, b337, THE WAVE'S HOUSEKEEPING."),
    ('registration -- no grade moved', REG, '**NO GRADE MOVED.**'),
    ('registration -- the placement', REG, 'THE PLACEMENT, AND WHY IT IS A BLOCK.'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('the ledger -- the cost block', LEDGER, MARK_C),
    ('### the addendum', LEDGER, MARK_A),
    ('### row L2', LEDGER, '| L2 | L2 -- the pole-constant relation between the Li and positivity faces:'),
    ('the sorted view -- no grade moved', SORTED, '### NO GRADE MOVED. ### A cost is not a grade, not a plan, not a prediction.'),
]

MUST_FAIL = [
    ('the bank never says a grade moved', BANK, '### ### **A GRADE MOVED.**'),
    ('the bank never says a price predicts', BANK, '### ### **THE PRICE PREDICTS THE ACT.**'),
    ('the bank never says L2 is new mathematics', BANK, '### ### **L2 IS NEW MATHEMATICS.**'),
    ('the bank never says K8 is owned', BANK, '### ### **K8 IS OWNED.**'),
    ('the bank never says the clause moved', BANK, '### ### **THE CLAUSE HAS MOVED.**'),
]

TOOLNUM = [
    ('15 rows typed, the types, the priced rows, the sorted view', 'tools/b336_cost.py'),
    ('row 183', 'tools/b336_correspondence.py'),
    ('the key', 'tools/b336_index_append.py'),
    ('23 clauses', 'tools/b336_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('13879 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b336_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the ledger writer, 6 quotations verified', 'tools/b327_faces_row.py'),
    ('3.104e+02 (b322)', 'tools/b322_ladder.py'),
    ('the twenty-fourth and the fifth (b321)', 'tools/b321_run.py'),
    ('SEES IT at seven cells (b328)', 'tools/b328_family.py'),
    ('270 / 170 / 100 (b334)', 'tools/b334_aimmap.py'),
]
NEW_THIS_ACT = {'tools/b336_cost.py', 'tools/b336_correspondence.py', 'tools/b336_index_append.py', 'tools/b336_regspec.py', 'tools/b336_extract.py', 'tools/b336_checks.py'}


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
    print('b336 -- GATE SUITE (THE COST CENSUS: TYPED, THROUGH THE WRITER, NO GRADE MOVED)')
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
    led = io.open(LEDGER, encoding='utf-8', errors='replace').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    srt = io.open(SORTED, encoding='utf-8').read()
    lb = blob_of(PP, 'FACES_LEDGER.md') or ''
    committed = MARK_C in lb

    print(chr(10) + '  G-COST (F1: the block names every row id once with a type from the five and a price cell; the sorted view in the type order):')
    blk = led[led.index(MARK_C):led.index(MARK_A)] if (MARK_C in led and MARK_A in led) else ''
    table_ids = [m.group(1) for m in re.finditer(r'^\| ([A-Z]\d+) \| ', led, re.M)]
    ids_in_block = re.findall(r'^\| \*\*([A-Z]\d+)\*\* \|', blk, re.M)
    types_ok = all(r[2] in CT.TYPE_ORDER or r[0] == 'L2' for r in CT.COST)
    price_ok = all((r[4] == CT.NO_PRICE) or r[4].startswith("the certificate's") or r[4] == 'cost zero' or any(k in r[4] for k in ('3.104e+02', 'twenty-fourth', 'six acts', 'SEES IT', 'priced at one act')) for r in CT.COST)
    order = [ln.split()[1] for ln in srt.splitlines() if re.match(r'\s+[A-Z]\d+\s+', ln)]
    ranks = [CT.TYPE_ORDER.index(x) if x in CT.TYPE_ORDER else -1 for x in order]
    gc = (sorted(ids_in_block) == sorted(set(table_ids)) and len(ids_in_block) == len(set(ids_in_block)) and types_ok and price_ok and ranks == sorted(ranks) and len(order) == len(CT.COST))
    print('    ids in the block %d = table rows %d ; types ok %s ; prices ok %s ; sorted view in type order %s : %s' % (len(ids_in_block), len(set(table_ids)), types_ok, price_ok, ranks == sorted(ranks), gc))
    if not gc:
        fails.append('G-COST')

    print(chr(10) + '  G-NOGRADE (F2: every existing row byte-identical, the fourth cell of every row unchanged):')
    rows_w = {m.group(1): m.group(0) for m in re.finditer(r'^\| ([A-Z]\d+) \| .*$', norm(led), re.M)}
    rows_b = {m.group(1): m.group(0) for m in re.finditer(r'^\| ([A-Z]\d+) \| .*$', norm(lb), re.M)}
    same = all(rows_w.get(k) == v for k, v in rows_b.items())
    extra = set(rows_w) - set(rows_b)
    gn = same and (extra <= {'L2'})
    print('    existing rows identical %s ; rows added %s : %s' % (same, sorted(extra), gn))
    if not gn:
        fails.append('G-NOGRADE')

    print(chr(10) + '  G-L2 (F3: row L2 present once, through the writer, quotations verified, STATED and cost zero, the writer append-only):')
    l2 = [ln for ln in norm(led).split(chr(10)) if ln.startswith('| L2 | ')]
    run2 = io.open(CRUN2, encoding='utf-8').read() if os.path.exists(CRUN2) else ''
    gl = len(l2) == 1 and 'STATED' in l2[0] and 'COST ZERO' in l2[0] and 'quotations verified 6' in run2 and 'append-only working=True blob=True' in run2 and 'row L2        WRITTEN' in run2
    print('    %s' % gl)
    if not gl:
        fails.append('G-L2')

    print(chr(10) + "  G-ADDENDUM (F4: the block names b328's update, cites b334's chart sign column, carries 45 and 135; b328's block byte-identical):")
    add = led[led.index(MARK_A):] if MARK_A in led else ''
    b328_w = norm(led)[norm(led).index('<!-- b328 update -->'):norm(led).index('<!-- b329 update -->')]
    b328_b = norm(lb)[norm(lb).index('<!-- b328 update -->'):norm(lb).index('<!-- b329 update -->')]
    ga = led.count(MARK_A) == 1 and "b328's update" in add and 'b334_chart_run.txt' in add and '45' in add and '135' in add and b328_w == b328_b
    print('    mark once %s ; names b328 %s ; cites the chart %s ; b328 block identical %s : %s' % (led.count(MARK_A) == 1, "b328's update" in add, 'b334_chart_run.txt' in add, b328_w == b328_b, ga))
    if not ga:
        fails.append('G-ADDENDUM')

    print(chr(10) + '  G-PRICES (F5: each of the four prices a quotation located in the extract file at its emitter):')
    gp = all(k in extract for k in ('3.104e+02', 'one twenty-fourth and one fifth', 'import b316_instrument as INS', "SEES IT** at [('E', 40.0)", 'IS THREE AIMS'))
    print('    %s' % gp)
    if not gp:
        fails.append('G-PRICES')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row 183: NO TERMINAL with the reason, a census act, NO GRADE MOVED, M-2; the table a true prefix of its blob):')
    r183 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 183 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = len(r183) == 1 and 'NO TERMINAL, AND THE REASON' in r183[0] and 'A CENSUS ACT' in r183[0] and 'NO GRADE MOVED' in r183[0] and 'M-2' in r183[0] and norm(tbl).startswith(norm(head).rstrip(chr(10)))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTAGRADE (one row; the must-not-hit queries NO KEY; the answer says no grade moved):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('cost-census')
    gk = o.count('act      :') == 1 and 'NO GRADE MOVED' in o and 'A COST IS NOT A GRADE, NOT A PLAN, NOT A PREDICTION' in o
    for s in ('a grade moved', 'the price predicts', 'the housekeeping'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NOTAGRADE')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner files, sealed files, the deposit, TECHNE, HANDOFF, the banks quoted: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/b327_faces_rows.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md', 'HANDOFF.md', 'data/STRUCK_CLAUSES.md',
              'data/b322_the_membership.txt', 'data/b321_the_window_opened.txt', 'data/b327_the_faces_ledger.txt', 'data/b328_the_discriminating_family.txt', 'data/b331_the_fold.txt',
              'data/b334_the_aim_map.txt', 'data/b334_chart_run.txt', 'data/b328_family_run.txt']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('FACES_LEDGER.md')]
    st_t = git(TC, 'status', '--porcelain').strip().replace('?? modules/2026-08/', '').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    fnd_same = git(PP, 'status', '--porcelain', 'FINDINGS.md').strip() == ''
    gn2 = not st_r and not st_s and not st_p and not st_t and not dep and fnd_same
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond the ledger) %s ; TECHNE %r ; deposit %r ; FINDINGS untouched %s : %s' % (st_r, st_s, st_p, st_t, dep, fnd_same, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the tool, the runs, the ledger, the row and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b336_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b336_cost.py'), CRUN, CRUN2, SORTED, LEDGER, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b336_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b336_checks_run.txt')) else ''
        after = 'the tool, the runs, the ledger, the row and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the tool, the runs, the ledger, the row and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-HOOK / G-MIRROR (read from their records when they exist; owed after the push):')
    hk = os.path.exists(HOOKS) and 'REPOS FAILING : 0' in io.open(HOOKS, encoding='utf-8', errors='replace').read()
    mr = os.path.exists(MIRROR) and all(('CLAUSE %d : CLEAN' % k) in io.open(MIRROR, encoding='utf-8', errors='replace').read() for k in (1, 2, 3))
    if committed:
        print('    the ledger committed ; hook record %s ; mirror CLEAN on three clauses %s : %s' % (hk, mr, hk and mr))
        if not (hk and mr):
            fails.append('G-HOOK/G-MIRROR')
    else:
        print('    the ledger not yet committed ; the hook and the mirror are owed after the commit (records present: %s / %s)' % (os.path.exists(HOOKS), os.path.exists(MIRROR)))

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    run1 = io.open(CRUN, encoding='utf-8').read()
    n = re.search(r'rows typed (\d+)', run1).group(1)
    checks.append(('%s rows typed' % n, n == '15' and 'FIFTEEN ROWS TYPED' in bank))
    by = {}
    for rid, _h, typ, _w, _p in CT.COST:
        by.setdefault(typ, []).append(rid)
    checks.append(('CONSTRUCTION rows', by['CONSTRUCTION'] == ['R1', 'R2', 'R3', 'R5', 'F4', 'F6'] and 'CONSTRUCTION for R1, R2, R3, R5, F4, F6' in bank))
    checks.append(('DERIVATION rows', by['DERIVATION'] == ['R4', 'F3', 'F5', 'L1'] and 'DERIVATION for R4, F3,' in bank))
    checks.append(('MEASUREMENT rows', by['MEASUREMENT'] == ['F1', 'F2', 'F7', 'S1'] and 'MEASUREMENT for F1, F2, F7, S1' in bank))
    pr = re.search(r"rows the record prices : \[(.*?)\]", run1).group(1).replace("'", '')
    checks.append(('priced rows %s' % pr, pr == 'F1, F2, F7, S1' and 'record prices the step: F1, F2, F7, S1' in bank))
    checks.append(('quotations verified 6', 'quotations verified 6' in run2 and '6 quotations verified' in bank))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    checks.append(('the domain factor', '3.104e+02' in io.open(d('b322_the_membership.txt'), encoding='utf-8').read() and '`3.104e+02`' in bank))
    checks.append(('270 / 170 / 100', all(x in io.open(d('b334_chart_run.txt'), encoding='utf-8').read() for x in ('rule 270', 'discriminating) 170', 'deg) 100')) and '270 aims' in bank and '170 with' in bank and '100 with' in bank))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded; the numbered runs as the bank tells them):')
    once_ok = all(os.path.exists(p) for p in [CRUN, CRUN2, CRER, CRER2, SORTED, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b336_cost_run3.txt'))
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

    print(chr(10) + '  G-STEM-APPENDED (extended scope: the cost block, row L2, the addendum, row 183, the index row, swept):')
    ib = idx[idx.index('# ### THE COST CENSUS (b336'):idx.index('# ### THE STANDING CLAUSES, FILED (b335')] if '# ### THE COST CENSUS (b336' in idx else ''
    for lbl, blk2 in (('the cost block', blk), ('row L2', l2[0] if l2 else ''), ('the addendum', add), ('row 183', r183[0] if r183 else ''), ('index row', ib)):
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
    extra2 = got - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra2), 'PASS' if not extra2 else '### FAIL ###'))
    if extra2:
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the cost block, row L2, the addendum, the row and the index row included):')
    tmpdir = tempfile.mkdtemp(prefix='b336_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('the cost block', blk), ('row L2', l2[0] if l2 else ''), ('the addendum', add), ('row 183', r183[0] if r183 else ''), ('the index row', ib)):
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
