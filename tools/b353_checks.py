# -*- coding: utf-8 -*-
"""b353_checks.py -- THE GATE SUITE FOR THE WIDTH COORDINATE'S MISSING STATEMENT.

### ### **EVERY `G-NO*` ARM READS STRIPPED CODE** (b348), ### **EVERY PRESENCE ARM READS RAW SOURCE** (b349),
### and every quotation goes through `quote_norm`.
### ### **EVERY ARM BELOW THAT READS A REPOSITORY STATE DECLARES ITS SIDE OF THE PUSH** (b352's rule):
### `G-ROW`/`G-ANCESTOR` and `G-APPENDONLY` are read BEFORE THE PUSH and again after, and the pre-push reading
### is the one that carries; `G-NOEDIT` is `SIDE-INVARIANT`; and this act writes nothing to the papers repo, so
### `G-NOHOOK` checks that the hook and mirror are NOT OWED rather than assuming it.
"""
import ast
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
import gate_text         # noqa: E402
import quote_norm        # noqa: E402
import registration_gate as RG   # noqa: E402
import b353_extract as EX        # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b353_the_missing_statement.txt')
REG = d('b353_registration_2026-09-07.txt')
FERRY = d('b353_ferry_2026-09-07.txt')
EXTRACT = d('b353_extract_notes.txt')
RRUN, RJ = d('b353_read_run.txt'), d('b353_read.json')
SJ = d('b353_source.json')
CORR, IDX = d('b353_corr_run.txt'), d('b353_index_run.txt')
TERMSCAN, GATE = d('b353_reg_termscan.txt'), d('b353_reg_gate.txt')
CENSUS, FCEN = d('b353_census.txt'), d('b353_faces_census.txt')
REGSPEC, SATIS = d('b353_regspec_run.txt'), d('audit_b353_reg_satisfiable.txt')
SEAL = 'dbc62f54e2453ed65dcd63a18b2a6a7d34887d95ca8700d1640d306db38ac065'
ROWNUM = '201'
STATUSES = ('MET', 'MET TO A MEASURED TOLERANCE', 'REFUTABLE', 'UNDECIDABLE FROM THE RECORD')

OWNED = [BANK, REG, FERRY, RRUN, RJ, SJ, CORR, IDX, CENSUS, FCEN, REGSPEC, SATIS, GATE, TERMSCAN, EXTRACT,
         d('b353_satisfiable.json'), d('b353_ferry_scan.txt'), d('audit_b353_index_query.txt'),
         d('b353_pins_stepzero.txt'), d('b353_pins_stepzero2.txt'), d('b353_pins_stepzero3.txt'),
         t('b353_extract.py'), t('b353_regspec.py'), t('b353_read.py'),
         t('b353_correspondence.py'), t('b353_index_append.py')]

NEW_THIS_ACT = {'tools/b353_extract.py', 'tools/b353_regspec.py', 'tools/b353_read.py',
                'tools/b353_correspondence.py', 'tools/b353_index_append.py', 'tools/b353_checks.py'}

TOOLNUM = [
    ('the four hypotheses, graded twice, and the verdict', 'tools/b353_read.py'),
    ('the pin, the search and the reads', 'tools/b353_extract.py'),
    ("the sortie's shared normaliser", 'tools/quote_norm.py'),
    ("the run files' clocks", 'tools/run_clock.py'),
    ("the corpus's Definition 3.1 test, READ and not re-run", 'tools/b318_square.py'),
    ('the seeds, READ and not rebuilt', 'tools/b317_smear.py'),
    ('row 201', 'tools/b353_correspondence.py'),
    ('the key', 'tools/b353_index_append.py'),
    ('35 clauses', 'tools/b353_regspec.py'),
    ('15817 bytes sealed, and the seal clock', 'tools/reg_seal.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins, and the two that did not resolve', 'tools/b303_pins.py'),
]

SELF_NEEDLES = [
    ('the bank states the verdict first', BANK, '### ### ### **A STATEMENT EXISTS -- AND IT DOES NOT CLOSE THE WIDTH COORDINATE, AND CANNOT.**'),
    ('### the statement is the corpus own source', BANK, "### ### **THE STATEMENT IS IN THE CORPUS'S OWN SOURCE, NOT A NEW ONE.**"),
    ('### an equivalence, not a density statement', BANK, '### ### ### **IT IS AN EQUIVALENCE, WHICH IS STRONGER THAN THE DENSITY STATEMENT THE ORDER ASKED FOR.**'),
    ('### every conclusion at the same A', BANK, '### ### ### **AND EVERY CONCLUSION IT GIVES IS AT THE SAME `A` IT WAS GIVEN.**'),
    ('### the central sentence', BANK, '### ### ### **SO: AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS.**'),
    ('### graded twice, never merged', BANK, '### (2) THE HYPOTHESES, GRADED TWICE, AND THE TWO GRADINGS NEVER MERGED.'),
    ('### H1 refutable, in the record own words', BANK, '### ### IS NOT `C^infty`. ### IT IS NOT EVEN `C^1`.**'),
    ('### H3 undecidable, the tool says why', BANK, '### it cannot prove one IS beyond the interval scanned"*.'),
    ('### H4 to a tolerance, which is not MET', BANK, '### ### **(H4) THE VANISHING CONDITIONS. ### MET TO A MEASURED TOLERANCE, WHICH IS NOT `MET`.**'),
    ('### the branch picked by grading (i)', BANK, '### ### NONE.** ### All four are `MET` there, because the hypotheses ARE the source\'s class.'),
    ('### an absence of reading', BANK, '### ### ### **THAT IS AN ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE.**'),
    ('### the missing statement typed', BANK, '### ### **THE MISSING STATEMENT, TYPED:**'),
    ('### why the second half is not automatic', BANK, '### ### INSTRUMENT THAT DOES NOT REACH.**'),
    ('### unpriceable from banked figures', BANK, '### ### **THE CROSSING HALF IS UNPRICEABLE FROM BANKED FIGURES.**'),
    ('### the coverage class, not a failure class', BANK, "### ### **THE PHASE COORDINATE'S VANISHING-TRANSFORM CLASS IS A COVERAGE CLASS, NOT A FAILURE"),
    ('### the import bar discharged', BANK, '### ### **IS AN INTERNAL VERIFICATION TOOL-REACHABLE? ### NO, AND THE REASON IS NOT SHYNESS:**'),
    ('### the circular check named as not a verification', BANK, '### ### **THAT WOULD BE CIRCULAR HERE**'),
    ('### the thing no seat wrote down', BANK, "### ### ### **THE STATEMENT THE ORDER SENT THIS ACT LOOKING FOR IS ALREADY IN THE CORPUS'S OWN SOURCE, AND"),
    ('### the pins incident', BANK, '### ### **(E1) THE OPENING PINS FAILED TWICE AND RESOLVED ON THE THIRD ATTEMPT**'),
    ('### the pin/reading seam', BANK, '### ### **THE HASH PINS THE PDF WHILE'),
    ('### the shadow', BANK, '### ### **EXPECTED: NOTHING.** ### An act that reads a paper and grades four hypotheses has produced no'),
]

MUST_FAIL = [
    ('the bank never says the width is closed', BANK, '### THE WIDTH IS CLOSED.'),
    ('the bank never says the class is spanned', BANK, '### THE CLASS IS SPANNED.'),
    ('the bank never says the partition is decided', BANK, '### THE PARTITION IS DECIDED.'),
    ('the bank never says the literature carries no such statement', BANK, '### THE LITERATURE CARRIES NO SUCH STATEMENT.'),
]


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob_of(repo, rel):
    r = subprocess.run(['git', '-C', repo, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def norm(s):
    return s.replace(chr(13) + chr(10), chr(10))


def strip_prose(path):
    src2 = io.open(path, encoding='utf-8').read()
    tree = ast.parse(src2)
    spans = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and hasattr(n, 'lineno'):
            spans.append((n.lineno, n.end_lineno))
    keep = []
    for i, ln in enumerate(src2.split(chr(10)), 1):
        if any(a <= i <= b for a, b in spans):
            continue
        keep.append(ln.split('#')[0])
    return chr(10).join(keep)


def main():
    fails = []
    print('=' * 100)
    print('b353 -- GATE SUITE (A READ THAT COMPUTES NOTHING AND CLOSES NOTHING)')
    print('=' * 100)
    bank = io.open(BANK, encoding='utf-8').read()
    bf = gate_text.flat(bank)
    reg = io.open(REG, encoding='utf-8', errors='replace').read()
    extract = io.open(EXTRACT, encoding='utf-8', errors='replace').read()
    P = json.load(io.open(RJ, encoding='utf-8'))
    S = json.load(io.open(SJ, encoding='utf-8'))
    src = S['source']
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()

    print(chr(10) + "  G-PIN (the source's hash, bytes and URL present; the hash's floor stated):")
    p1 = src['sha256'] in bank and str(src['bytes']) in bank and src['arxiv'] in bank
    p2 = re.fullmatch(r'[0-9a-f]{64}', src['sha256']) is not None
    p3 = 'DOES NOT CERTIFY THAT THE FILE IS WHAT ARXIV SERVES TODAY' in gate_text.flat(reg)
    p4 = 'THE HASH PINS THE PDF WHILE' in bf
    gp = p1 and p2 and p3 and p4
    print('    hash, bytes and arXiv id all in the bank : %s ; the hash is 64 hex : %s' % (p1, p2))
    print("    the hash's floor stated in the registration : %s ; the seam stated in the bank : %s  %s"
          % (p3, p4, 'PASS' if gp else '### FAIL ###'))
    if not gp:
        fails.append('G-PIN')

    print(chr(10) + '  G-SEARCH (every query and fetch recorded, INCLUDING THE REFUSED ONE; and what was not found):')
    s1 = len(S['searches']) >= 5
    s2 = any('403' in w for _k, w in S['searches'])
    s3 = len(S['misses']) >= 3 and all(res.strip() for _w, res in S['misses'])
    s4 = 'ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE' in bf
    s5 = all(quote_norm.contains(extract, w[:60]) for _w, _r in [] ) or True
    gs = s1 and s2 and s3 and s4
    print('    searches recorded : %d ; the refused fetch recorded : %s' % (len(S['searches']), s2))
    print('    what was looked for and NOT found : %d entries ; the absence framed as reading : %s  %s'
          % (len(S['misses']), s4, 'PASS' if gs else '### FAIL ###'))
    if not gs:
        fails.append('G-SEARCH')

    print(chr(10) + '  G-HYPOTHESES (every hypothesis graded TWICE, each status one of the sealed four):')
    H = P['hypotheses']
    h1 = len(H) >= 4
    bad = [(h['id'], h['source'], h['corpus']) for h in H if h['source'] not in STATUSES or h['corpus'] not in STATUSES]
    h2 = not bad
    h3 = all(st in reg for st in STATUSES)
    h4 = all((h['id'] in bank and h['source'] in bank and h['corpus'] in bank) for h in H)
    gh = h1 and h2 and h3 and h4
    for h in H:
        print('      %-4s %-22s / %s' % (h['id'], h['source'], h['corpus']))
    print('    off-list statuses : %s ; all four sealed in the registration : %s ; all in the bank : %s  %s'
          % (bad or 'none', h3, h4, 'PASS' if gh else '### FAIL ###'))
    if not gh:
        fails.append('G-HYPOTHESES')

    print(chr(10) + '  G-TWOGRADINGS (the two gradings labelled and NOT merged; the branch picked by (i) alone):')
    t1 = 'grading (i)' in bank and 'grading (ii)' in bank
    t2 = 'THE TWO GRADINGS NEVER MERGED' in bf
    t3 = P['grading_i_all_met'] and not P['grading_i_failures']
    t4 = any(h['source'] != h['corpus'] for h in H)
    gt = t1 and t2 and t3 and t4
    print('    both gradings labelled in the bank : %s ; stated as never merged : %s' % (t1, t2))
    print('    grading (i) all MET, no failures : %s ; and the two gradings actually DIFFER somewhere : %s  %s'
          % (t3, t4, 'PASS' if gt else '### FAIL ###'))
    if not gt:
        fails.append('G-TWOGRADINGS')

    print(chr(10) + '  G-NOARGUMENT (STRIPPED code: the tool computes nothing and imports nothing that could):')
    code = strip_prose(t('b353_read.py'))
    forbidden = ('numpy', 'scipy', 'b316_instrument', 'b317_smear', 'b318_square', 'b319_stable',
                 'b326_windows', 'b328_family', 'b334_aimmap', 'b322_ladder', 'carto_atlas')
    hit = [x for x in forbidden if x in code]
    imports = sorted(set(re.findall(r'^import (\w+)', code, re.M)))
    n2 = set(imports) <= {'io', 'json', 'os', 'sys', 'needle_pull', 'quote_norm', 'run_clock'}
    gn = (not hit) and n2
    print('    forbidden imports in the CODE : %s' % (hit or 'none'))
    print('    what it does import : %s  %s' % (imports, 'PASS' if gn else '### FAIL ###'))
    if not gn:
        fails.append('G-NOARGUMENT')

    print(chr(10) + "  G-VERDICT (the branch by (D)'s rule; the branches not taken shown unreachable):")
    v1 = P['verdict'] == 'A STATEMENT EXISTS' and 'A STATEMENT EXISTS' in bf
    v2 = '(EXISTS BUT DOES NOT APPLY) -- UNREACHABLE' in bf
    v3 = '(NO SUCH STATEMENT LOCATED) -- UNREACHABLE' in bf
    gv = v1 and v2 and v3
    print('    the verdict and the bank agree : %s ; both other branches shown unreachable : %s / %s  %s'
          % (v1, v2, v3, 'PASS' if gv else '### FAIL ###'))
    if not gv:
        fails.append('G-VERDICT')

    print(chr(10) + '  G-NOTCLOSED (the act says at full prominence that the width is NOT closed):')
    c1 = 'THE WIDTH COORDINATE IS NOT CLOSED BY THIS ACT' in bf
    c2 = 'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS' in bf
    c3 = 'STAYS `UNDECIDED`' in bank or 'STAYS UNDECIDED' in bf
    c4 = 'THE CLAUSE HAS NOT MOVED' in bf
    gc = c1 and c2 and c3 and c4
    print('    not closed : %s ; the central sentence : %s ; UNDECIDED stands : %s ; clause unmoved : %s  %s'
          % (c1, c2, c3, c4, 'PASS' if gc else '### FAIL ###'))
    if not gc:
        fails.append('G-NOTCLOSED')

    print(chr(10) + '  G-PRICE (the missing statement typed; priced or its unpriceability stated; NOT attempted):')
    r1 = bool(P['missing']) and quote_norm.contains(bank, P['missing'][:70])
    r2 = 'UNPRICEABLE FROM BANKED FIGURES' in bf
    r3 = 'PRICING THE PRICING IS UNPRICEABLE TOO' in bf.upper()
    r4 = 'IT IS NOT ATTEMPTED' in bf.upper()
    r5 = 'A PROOF AND' in bf and 'NOT A RUN' in bf
    gr = r1 and r2 and r3 and r4 and r5
    print('    the missing statement typed and present in the bank : %s' % r1)
    print('    unpriceable stated : %s ; the pricing too : %s ; not attempted : %s ; a proof not a run : %s  %s'
          % (r2, r3, r4, r5, 'PASS' if gr else '### FAIL ###'))
    if not gr:
        fails.append('G-PRICE')

    print(chr(10) + "  G-COVERAGE (the vanishing-transform class filed as a COVERAGE class, with b349's words):")
    y1 = 'COVERAGE CLASS, NOT A FAILURE' in bf
    y2 = 'A COVERAGE CLASS IS A REGION THE INSTRUMENT DOES' in bf
    y3 = quote_norm.contains(bank, 'NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT')
    try:
        needle_pull.pull(d('b349_the_room_relative.txt'), '### ### NEVER DEGENERATES -- IT MEANS THESE THREE DID NOT.**')
        y4 = True
    except LookupError:
        y4 = False
    gy = y1 and y2 and y3 and y4
    print('    filed as coverage and not failure : %s ; the distinction stated : %s' % (y1, y2))
    print("    b349's words in the bank : %s ; and located at b349's own file : %s  %s"
          % (y3, y4, 'PASS' if gy else '### FAIL ###'))
    if not gy:
        fails.append('G-COVERAGE')

    print(chr(10) + "  G-IMPORT (the located statement graded under the bar; tool-reachability stated either way):")
    i1 = src['grade'] in ('VERIFIED-INTERNALLY', 'VERIFIED-AT-BENCH', 'TRUSTED-AT-CITE')
    i2 = src['grade'] in bank
    i3 = 'TOOL-REACHABLE' in bf.upper()
    i4 = 'NO WORK-ORDER IS OPENED' in bf
    i5 = quote_norm.contains(reg, 'VERIFIED-INTERNALLY / VERIFIED-AT-BENCH / TRUSTED-AT-CITE')
    gi = i1 and i2 and i3 and i4 and i5
    print("    the grade is one of the bar's three : %s ; in the bank : %s" % (i1, i2))
    print("    tool-reachability stated : %s ; no work-order, and said : %s ; the bar quoted : %s  %s"
          % (i3, i4, i5, 'PASS' if gi else '### FAIL ###'))
    if not gi:
        fails.append('G-IMPORT')

    print(chr(10) + '  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        ok = quote_norm.contains(bank, anchor)
        print('    %s  %s' % ('PASS' if ok else '### FAIL (NOT FOUND)', lbl))
        if not ok:
            fails.append('SELF: ' + lbl)

    print(chr(10) + '  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    print(chr(10) + '  OWNER NEEDLES (each at the file that EMITTED it, each also IN THE EXTRACT FILE):')
    nbad = 0
    for label, tag, path, anchor in EX.READS:
        try:
            needle_pull.pull(path, anchor)
            if not quote_norm.contains(extract, anchor):
                nbad += 1
                print('    ### FAIL (NOT IN THE EXTRACT FILE)  %s' % label)
        except LookupError:
            nbad += 1
            print('    ### FAIL (UNPULLABLE)  %s' % label)
    cited = len(re.findall(r'^ +\S+ : line \d+$', extract, re.M))
    print('    reads %d ; all located and in the extract : %s ; cited lines in the extract : %d'
          % (len(EX.READS), nbad == 0, cited))
    if nbad or cited != len(EX.READS):
        fails.append('G-EXTRACT')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row %s). ### **READ BEFORE THE PUSH AND AFTER IT; THE PRE-PUSH' % ROWNUM)
    print('  ### READING IS THE ONE THAT CARRIES**, because after the push the blob IS the file.')
    rows = [ln for ln in tbl.splitlines() if ln.startswith('| %s |' % ROWNUM)]
    tbb = blob_of(SIDE, 'CORRESPONDENCE.md')
    anc = (tbb is not None) and norm(tbl).startswith(norm(tbb).rstrip(chr(10)))
    grow = len(rows) == 1 and 'NO TERMINAL, AND THE REASON' in rows[0] and 'NOT A PROVED ONE' in rows[0] and anc
    print('    row %s present once : %s ; true prefix of its blob : %s ; %s'
          % (ROWNUM, len(rows) == 1, anc, 'PASS' if grow else '### FAIL ###'))
    if not grow:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NOTCLOSED (the index):')
    irun = io.open(IDX, encoding='utf-8').read()
    k1 = 'READ BACK : width-missing-statement returns 1 row(s)' in irun
    k2 = all(('%-44s NO KEY after  : True  PASS' % q) in irun for q in
             ('the width is closed', 'the class is spanned', 'the partition is decided',
              'the literature carries no such statement'))
    k3 = irun.rstrip().endswith('=' * 100) and '  ### PASS' in irun
    gk = k1 and k2 and k3
    print('    one key and one row : %s ; the four overreadings NO KEY after : %s ; the key run passed : %s ; %s'
          % (k1, k2, k3, 'PASS' if gk else '### FAIL ###'))
    if not gk:
        fails.append('G-KEY')

    print(chr(10) + '  G-APPENDONLY (banked_index.py). ### **READ BEFORE THE PUSH.**')
    ib = blob_of(ROOT, 'tools/banked_index.py')
    ap = True
    if ib is not None:
        old, new = norm(ib).split(chr(10)), norm(idx).split(chr(10))
        i = 0
        for ln in new:
            if i < len(old) and ln == old[i]:
                i += 1
        ap = (i == len(old))
    print('    every committed line still present, in order : %s' % ap)
    if not ap:
        fails.append('G-APPENDONLY')

    print(chr(10) + '  G-NOEDIT (no owner instrument edited; nothing outside relay/SIDE moved). ### SIDE-INVARIANT.')
    owner = ['tools/b318_square.py', 'tools/b317_smear.py', 'tools/b326_closure.py', 'tools/b334_aimmap.py',
             'tools/quote_norm.py', 'tools/run_clock.py', 'tools/gate_text.py', 'tools/registration_gate.py']
    touched = [p for p in owner if git(ROOT, 'diff', '--name-only', 'HEAD', '--', p).strip()]
    ppstat = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x]
    tcstat = [x for x in git(TC, 'status', '--porcelain').splitlines() if x.strip()]
    gne = not touched and not ppstat and not tcstat
    print('    owner instruments modified : %s ; papers dirty : %s ; TECHNE dirty : %s  %s'
          % (touched or 'none', ppstat or 'none', tcstat or 'none', 'PASS' if gne else '### FAIL ###'))
    if not gne:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-NOHOOK (nothing written to the papers repo, so hook and mirror are NOT owed -- CHECKED):')
    h_1 = not ppstat
    h_2 = git(PP, 'log', '-1', '--format=%H').strip() == git(PP, 'rev-parse', 'origin/main').strip()
    h_3 = 'Nothing written to PLACE-papers' in tbl or 'NOT OWED' in bank
    gho = h_1 and h_2 and h_3
    print('    papers tree clean : %s ; its HEAD equals its remote : %s ; the act says NOT OWED : %s  %s'
          % (h_1, h_2, h_3, 'PASS' if gho else '### FAIL ###'))
    if not gho:
        fails.append('G-NOHOOK')

    print(chr(10) + '  G-ORDER (the seal verifies; the ordering read from clocks):')
    vr = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    o1 = ('SEAL INTACT' in (vr.stdout or '')) and (SEAL in reg)
    o1 = o1 and hashlib.sha256(norm(reg).split('=' * 100 + chr(10) + '### THE REGISTRATION SEAL')[0].encode('utf-8')).hexdigest() == SEAL
    stampm = re.search(r'### sealed at \(UTC\) : (\S+)', reg)
    o2 = stampm is not None
    o3 = (stampm is not None) and S['run_clock'] < stampm.group(1) < P['run_clock']
    sat = io.open(SATIS, encoding='utf-8').read()
    o4 = 'JOINTLY SATISFIABLE' in sat
    go = o1 and o2 and o3 and o4
    print('    the seal recomputes : %s ; clock %s' % (o1, stampm.group(1) if stampm else 'none'))
    print('    extract %s < seal < read %s : %s ; JOINTLY SATISFIABLE : %s'
          % (S['run_clock'], P['run_clock'], o3, o4))
    print('    ### ### **THE SEAL SITS AFTER THE EVIDENCE AND BEFORE THE VERDICT.**')
    print('    %s' % ('PASS' if go else '### FAIL ###'))
    if not go:
        fails.append('G-ORDER')

    print(chr(10) + '  G-NUMBERS:')
    sm = re.search(r'### bytes sealed : (\d+)', reg).group(1)
    clc = re.search(r'clauses\s*:\s*(\d+)', sat).group(1)
    rn = re.search(r'row to append : (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks = [('the seal hash', SEAL in bank),
              ('%s bytes sealed' % sm, ('%s bytes' % sm) in bank),
              ('%s clauses' % clc, ('%s clauses' % clc) in bank),
              ('row %s' % rn, rn == ROWNUM),
              ("the source's hash", src['sha256'] in bank),
              ("the source's byte count", str(src['bytes']) in bank),
              ('the extract clock', S['run_clock'] in bank),
              ('the seal clock', (stampm.group(1) if stampm else 'x') in bank),
              ('the read clock', P['run_clock'] in bank)]
    for what, ok in checks:
        print('    %-56s %s' % (what[:56], 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (the extract ran once; the pins ran three times and all three are declared):')
    once = (not os.path.exists(d('b353_extract_notes2.txt'))
            and os.path.exists(d('b353_pins_stepzero3.txt'))
            and 'THE OPENING PINS FAILED TWICE AND RESOLVED ON THE THIRD ATTEMPT' in bf
            and 'THE EXTRACT RAN ONCE' in bf)
    print('    %s' % once)
    if not once:
        fails.append('G-ONCE')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print(chr(10) + '  G-STRUCK / G-STEM:')
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
            print('    ### %-44s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for hh in (ch + sh)[:4]:
                print('        line %d  |  %s' % (hh[1], hh[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    fired = sum(1 for _e, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                                   ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'), ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]
                if ferry_scan.scan_text(text, struck, stem_list)[0])
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired, ctrl))
    if total or stem_total or fired != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    ib2 = idx[idx.index("# ### THE WIDTH COORDINATE'S MISSING STATEMENT (b353)."):idx.index("# ### THE FLOOR'S FOURTH CANDIDATE (b352).")] \
        if "# ### THE WIDTH COORDINATE'S MISSING STATEMENT (b353)." in idx else ''
    print(chr(10) + '  G-STEM-APPENDED:')
    for lbl, blk2 in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
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
        tr2 = K7.git_tracked(ROOT, tool)
        if not (ex and (tr2 or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-52s %-34s exists=%s tracked=%s' % (what[:52], tool, ex, tr2))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print(chr(10) + '  HEDGE AUDIT:')
    tmpdir = tempfile.mkdtemp(prefix='b353_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('row %s' % ROWNUM, rows[0] if rows else ''), ('the index row', ib2)):
        p = os.path.join(tmpdir, lbl.replace(' ', '_') + '.txt')
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(text + chr(10))
        targets.append((lbl, p))
    for lbl, path in targets:
        n2, ghd, ua2 = hedge_audit.audit(path)
        print('    %-46s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n2, len(ghd), len(ua2)))
        for s2 in ghd:
            print('      ### GRADED HEDGE: %s' % s2[:110])
        if ghd:
            fails.append('HEDGE (%s)' % lbl)

    print(chr(10) + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
