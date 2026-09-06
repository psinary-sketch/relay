# -*- coding: utf-8 -*-
"""b337_checks.py -- THE GATE SUITE FOR THE WAVE'S HOUSEKEEPING.

### ### **THE ARMS (registration (G), F1-F7):** `G-FETCH`, `G-LEDGERS`, `G-PARTITION`, `G-TECHNE`, `G-RECEIPTS`, `G-NODEPOSIT`
### (must-fail), `G-ROW`, `G-KEY`, `G-ORDER`, `G-HOOK` / `G-MIRROR`, `G-NUMBERS`, `G-TOOLNUM`, `G-ONCE`, `G-NOEDIT`, `G-APPENDONLY`,
### the hedge audit, the stem sweep at extended scope; re-run after the push.
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
import b337_errata as ER  # noqa: E402

D = os.path.join(ROOT, 'data')
SIDE = r'D:\SIDE-global-section'
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
TC2 = r'D:\MY-DOwnloads\TECHNE_Core'
PAT = r'D:\MY-DOwnloads\patent-package-BACKUP-2026-08-29'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(ROOT, 'tools', 'banked_index.py')
ERRATA = os.path.join(PP, 'ERRATA.md')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b337_the_housekeeping.txt')
REG = d('b337_registration_2026-09-06.txt')
EXTRACT = d('b337_extract_notes.txt')
FRUN, FJ, RECJ = d('b337_fetch_run.txt'), d('b337_fetch.json'), d('b337_record.json')
ERUN, ERER = d('b337_errata_run.txt'), d('b337_errata_rerun.txt')
TRUN, TRER, TMSG = d('b337_techne_run.txt'), d('b337_techne_rerun.txt'), d('b337_techne_commit_msg.txt')
RRUN = d('b337_receipts_run.txt')
CORR, CORRR = d('b337_corr_run.txt'), d('b337_corr_rerun.txt')
IDX, IDXR = d('b337_index_run.txt'), d('b337_index_rerun.txt')
SCAN, TERMSCAN, GATE = d('b337_ferry_scan.txt'), d('b337_reg_termscan.txt'), d('b337_reg_gate.txt')
CENSUS, FCEN = d('b337_census.txt'), d('b337_faces_census.txt')
REGSPEC, SATIS = d('b337_regspec_run.txt'), d('audit_b337_reg_satisfiable.txt')
PINS, INDEXQ = d('b337_pins_stepzero.txt'), d('audit_b337_index_query.txt')
HOOKS, MIRROR = d('b337_hooks.txt'), d('b337_mirror.txt')
SEAL = 'b557da51fea385d1c56d05e29de2dc7454043174cc892ba6193e77b136ac06ca'
MARK = ER.MARK

OWNED = [BANK, REG, FRUN, FJ, ERUN, ERER, TRUN, TRER, TMSG, RRUN, CORR, CORRR, IDX, IDXR, CENSUS, FCEN, REGSPEC, SATIS, PINS, INDEXQ, GATE,
         d('b337_satisfiable.json'), t('b337_extract.py'), t('b337_regspec.py'), t('b337_fetch.py'), t('b337_errata.py'), t('b337_techne.py'),
         t('b337_receipts.py'), t('b337_correspondence.py'), t('b337_index_append.py')]

CARRIERS = [
    (t('b337_checks.py'), 'its own fixtures'),
    (d('b337_ferry_2026-09-06.txt'), "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "the scan's own log"), (TERMSCAN, "the term scan's own log"),
    (EXTRACT, "the extract file carries the emitters' own words"),
    (RECJ, "the public record's JSON, as fetched"),
]

OWNER_NEEDLES = [
    ("REGISTRY -- the d1-1 row", os.path.join(PP, 'REGISTRY.md'), '| d1-1 | A Place to Stand (monograph) | `day1/A_Place_to_Stand.md` | v5.13 |'),
    ("ERRATA -- its head names v1.1.1 as current", ERRATA, 'publication. The current deposit is the monograph at manuscript **v5.8** /'),
    ('### entries never restated', ERRATA, 'Entries are retained across deposits and are never restated to the current'),
    ("the loom -- the gate-1 pin", os.path.join(PP, 'VERIFICATION_LOOM.md'), '21539167` returns **v1.1.2 \u00b7 2026-07-24 \u00b7 DOI 10.5281/zenodo.21539167 \u00b7 concept 19675355 \u00b7 11'),
    ("the trails -- the deposit-voice pin", os.path.join(PP, 'OPEN_TRAILS.md'), '**Deposit-voice is pinned** by the read-only fetch of 2026-08-28: Zenodo **v1.1.2**, DOI'),
    ('E-2026-07-23-1', ERRATA, '## E-2026-07-23-1 \u2014 \u00a718.2 on-line constraint mislabeled Im(\u03be) (should be Re(\u03be))'),
    ('### no deposited artifact affected', ERRATA, '### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY.**'),
    ('### no deposit action, nothing written at Zenodo', ERRATA, '### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.'),
    ('E-2026-09-03-1', ERRATA, "## E-2026-09-03-1 \u2014 The archimedean remainder's normalization convention is the corpus's own, not the source's (INTERNAL RECORD"),
    ('b236 -- the record URL', t('b236_deposit_fetch.py'), "REC = 'https://zenodo.org/api/records/21539167'"),
    ("the counsel list -- item 3", os.path.join(PAT, 'COUNSEL_ITEMS.md'), '| **3** | **NEW-6 / NEW-8 receipts** | standing |'),
    ('the deadline board -- enumerate the volumes', os.path.join(PAT, 'OFFICE_DEADLINES_2026-08-30.md'), 'volumes before concluding a file does not exist.**'),
    ('the sortie -- leg 2', d('b337_ferry_2026-09-06.txt'), "LEG 2 (b337) \u2014 THE WAVE'S HOUSEKEEPING: the three ledgers"),
    ('### the ERRATA ruling', d('b337_ferry_2026-09-06.txt'), 'by this paste and strikeable: "ERRATA is partitioned into a'),
    ('### the TECHNE ruling', d('b337_ferry_2026-09-06.txt'), 'TECHNE module files are committed to the canonical local clone,'),
]

SELF_NEEDLES = [
    ('bank states the four items first', BANK, 'THE FOUR ITEMS, FIRST.'),
    ('### (1) the fetch agrees', BANK, 'THE FETCH AGREES WITH REGISTRY ON EVERY FIELD; TWO LEDGERS CURRENT, ONE DRIFT, REPAIRED BY'),
    ('### nothing routed', BANK, 'Nothing was ROUTED: the fetch confirmed or refuted every statement located.'),
    ('### (2) the partition', BANK, 'THE PARTITION, EXECUTED AS RULED: ONE APPENDED BLOCK, ENTRIES UNMOVED.'),
    ('### (3) TECHNE', BANK, 'THE NINE AUGUST TECHNE FILES COMMITTED LOCALLY AT `4c0a6af`, NOT PUSHED.'),
    ('### (4) the receipts', BANK, 'THE PATENT RECEIPTS: ABSENT ON THE MOUNTED VOLUMES, AND F: IS NOT MOUNTED.'),
    ('### nothing concluded about the reply', BANK, 'NOTHING IS CONCLUDED ABOUT WHETHER A REPLY'),
    ('### no deposit action', BANK, 'NO DEPOSIT ACTION; NOTHING WAS WRITTEN AT ZENODO. NO ENTRY MOVED. NO GRADE. NO CLAIM. NOTHING DEPOSITS.'),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('bank gives the tools', BANK, 'THE TOOLS AND THEIR RUNS.'),
    ('bank gives the row and the key', BANK, 'THE ROW AND THE KEY.'),
    ("### the seat's defects", BANK, "THE SEAT'S OWN DEFECTS, DECLARED."),
    ('### E1', BANK, "E1 -- ONE LINE OF THE TECHNE RUN FILE MISREPORTS A FILE'S STATE."),
    ('bank gives the standing rows', BANK, 'THE STANDING ROWS.'),
    ('### the shadow none', BANK, 'THE SHADOW: NONE.'),
    ('### next', BANK, 'NEXT, BY THE SORTIE: LEG 3, b338, THE FOLD b331-b334.'),
    ('registration -- no deposit action', REG, 'HOUSEKEEPING, FOUR ITEMS, EACH A FILING OR A CHECK; NO CLAIM, NO GRADE, NO DEPOSIT ACTION.'),
    ('registration -- F: not mounted', REG, 'wrappers on 2026-08-30, IS NOT MOUNTED THIS SESSION.'),
    ('registration -- expected nothing', REG, '**EXPECTED: NOTHING.**'),
    ('ERRATA -- the partition block', ERRATA, MARK),
    ('### the ruling as the header line', ERRATA, '**This block is that header line.**'),
    ('### the currency note', ERRATA, "**THE CURRENCY NOTE, AGAINST THE HEAD'S SENTENCE"),
    ('the fetch run -- every field agrees', FRUN, 'REGISTRY d1-1 AGREES WITH THE RECORD ON EVERY FIELD'),
    ('the techne run -- unchanged, not pushed', TRUN, 'UNCHANGED True ; NOT PUSHED : the clone is 2 commits ahead of the remote'),
    ('the receipts run -- F: not mounted', RRUN, 'IS NOT MOUNTED THIS SESSION'),
]

MUST_FAIL = [
    ('the bank never says a deposit action was taken', BANK, '### ### **A DEPOSIT ACTION WAS TAKEN.**'),
    ('the bank never says a Zenodo write was made', BANK, '### ### **A ZENODO WRITE WAS MADE.**'),
    ('the bank never says TECHNE was pushed', BANK, '### ### **TECHNE WAS PUSHED.**'),
    ('the bank never says the reply was filed', BANK, '### ### **THE REPLY WAS FILED.**'),
    ('the bank never says an entry moved', BANK, '### ### **AN ENTRY WAS MOVED.**'),
    ('the bank never says K8 is owned', BANK, '### ### **K8 IS OWNED.**'),
]

TOOLNUM = [
    ('v1.1.2, 2026-07-24, the DOIs, 11 files, 11 of 11, CURRENT/DRIFT', 'tools/b337_fetch.py'),
    ('+26 lines, 265 -> 291, the two lists', 'tools/b337_errata.py'),
    ('4c0a6af, 9 files, 621 insertions, 2 ahead, 22739c9, 6e8638a', 'tools/b337_techne.py'),
    ('C and D, F: absent, ABSENT per application, the notices', 'tools/b337_receipts.py'),
    ('row 184', 'tools/b337_correspondence.py'),
    ('the key', 'tools/b337_index_append.py'),
    ('25 clauses', 'tools/b337_regspec.py'),
    ('the satisfiability verdict', 'tools/reg_satisfiable.py'),
    ('0/0 on the scans', 'tools/ferry_scan.py'),
    ('TOTAL MISSING 0 (HANDOFF)', 'tools/b307_handoff_census.py'),
    ('TOTAL MISSING 0 (FACES)', 'tools/b327_faces_census.py'),
    ('the pins', 'tools/b303_pins.py'),
    ('15347 bytes sealed', 'tools/reg_seal.py'),
    ('the extract zeros', 'tools/b337_extract.py'),
    ('the hook', 'tools/b304_hooks.py'),
    ('the mirror', 'tools/mirror_verify.py'),
    ('the record URL, the MD5 rule', 'tools/b236_deposit_fetch.py'),
]
NEW_THIS_ACT = {'tools/b337_fetch.py', 'tools/b337_errata.py', 'tools/b337_techne.py', 'tools/b337_receipts.py', 'tools/b337_correspondence.py',
                'tools/b337_index_append.py', 'tools/b337_regspec.py', 'tools/b337_extract.py', 'tools/b337_checks.py'}


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
    print("b337 -- GATE SUITE (THE WAVE'S HOUSEKEEPING: FILINGS AND CHECKS; NO DEPOSIT ACTION)")
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
    fj = json.load(io.open(FJ, encoding='utf-8'))
    err = io.open(ERRATA, encoding='utf-8', errors='replace').read()
    eb = blob_of(PP, 'ERRATA.md') or ''
    committed = MARK in eb
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(INDEX, encoding='utf-8').read()
    trun = io.open(TRUN, encoding='utf-8').read()
    rrun = io.open(RRUN, encoding='utf-8').read()

    print(chr(10) + '  G-FETCH (F1: the record fields; REGISTRY agreeing on every field; the local MD5s):')
    gf = all(fj['agree'].values()) and fj['local_match'] == fj['local_total'] == 11 and not fj['missing'] and not fj['mismatching'] and os.path.exists(RECJ)
    print('    agree %s ; local %d of %d ; record kept %s : %s' % (fj['agree'], fj['local_match'], fj['local_total'], os.path.exists(RECJ), gf))
    if not gf:
        fails.append('G-FETCH')

    print(chr(10) + '  G-LEDGERS (F2: the three ledgers scored CURRENT / DRIFT / ROUTED from the located lines):')
    L = fj['ledgers']
    gl = (L['VERIFICATION_LOOM.md']['status'] == 'CURRENT' and L['OPEN_TRAILS.md']['status'] == 'CURRENT' and L['ERRATA.md']['status'].startswith('DRIFT')
          and all(v['located'] for v in L.values()))
    print('    %s : %s' % ({k: v['status'].split(' (')[0] for k, v in L.items()}, gl))
    if not gl:
        fails.append('G-LEDGERS')

    print(chr(10) + '  G-PARTITION (F3: the block once; every entry in exactly one list; entries byte-identical; the file a true prefix of its blob plus the block):')
    ids_w = ER.entry_ids(err)
    ids_b = ER.entry_ids(eb)
    listed = [e for e, _w in ER.DEPOSIT_FACING] + [e for e, _w in ER.INTERNAL_RECORD]
    body_w = norm(err)[:norm(err).index(MARK)] if MARK in err else norm(err)
    body_b = norm(eb)[:norm(eb).index(MARK)] if MARK in eb else norm(eb)
    entries_same = body_w.rstrip(chr(10)) == body_b.rstrip(chr(10))
    prefix = norm(err).startswith(norm(eb).rstrip(chr(10)))
    gp = err.count(MARK) == 1 and sorted(ids_w) == sorted(listed) and ids_w == ids_b and entries_same and prefix and len(ER.DEPOSIT_FACING) == 5 and len(ER.INTERNAL_RECORD) == 5
    print('    mark once %s ; ids covered %s ; entries identical %s ; prefix %s : %s' % (err.count(MARK) == 1, sorted(ids_w) == sorted(listed), entries_same, prefix, gp))
    if not gp:
        fails.append('G-PARTITION')

    print(chr(10) + '  G-TECHNE (F4: the nine tracked; the remote unchanged; two ahead; the second clone untouched; the commit exactly the nine):')
    remote = git(TC, 'ls-remote', 'origin', 'main').split()
    remote_sha = remote[0] if remote else ''
    ahead = git(TC, 'rev-list', '--count', '%s..HEAD' % remote_sha).strip() if remote_sha else '?'
    tracked = [x for x in git(TC, 'ls-files', '--', 'modules/2026-08').splitlines()]
    shown = [ln.split('|')[0].strip() for ln in git(TC, 'show', '--stat', '--format=', 'HEAD').splitlines() if 'modules/2026-08/' in ln]
    c2 = git(TC2, 'rev-parse', 'HEAD').strip()
    gt = (len(tracked) == 9 and remote_sha.startswith('22739c9') and ahead == '2' and len(shown) == 9 and c2.startswith('6e8638a') and 'committed : True' in trun and git(TC, 'rev-parse', 'HEAD').strip().startswith('4c0a6af'))
    print('    tracked %d ; remote %s ; ahead %s ; commit files %d ; second clone %s : %s' % (len(tracked), remote_sha[:7], ahead, len(shown), c2[:7], gt))
    if not gt:
        fails.append('G-TECHNE')

    print(chr(10) + '  G-RECEIPTS (F5: the volumes named, F: absent, ABSENT per application, the search paths listed, the repo of record without a remote):')
    gr = ("volumes mounted (Get-PSDrive, filesystem) : ['C', 'D'] ; F: mounted : False" in rrun and rrun.count('ABSENT ON THE MOUNTED VOLUMES (C, D)') == 2
          and 'remotes 0 (NONE, as required)' in rrun and 'search roots :' in rrun and git(PAT, 'remote').strip() == '')
    print('    %s' % gr)
    if not gr:
        fails.append('G-RECEIPTS')

    print(chr(10) + '  G-ROW / G-ANCESTOR (row 184: NO TERMINAL with the reason, not pushed, nothing concluded, M-2; the table a true prefix of its blob):')
    r184 = [ln for ln in tbl.split(chr(10)) if ln.startswith('| 184 |')]
    head = blob_of(SIDE, 'CORRESPONDENCE.md') or ''
    grw = (len(r184) == 1 and 'NO TERMINAL, AND THE REASON' in r184[0] and 'NOT PUSHED' in r184[0] and 'NOTHING IS CONCLUDED ABOUT WHETHER A REPLY WAS FILED' in r184[0]
           and 'M-2' in r184[0] and norm(tbl).startswith(norm(head).rstrip(chr(10))))
    print('    %s' % grw)
    if not grw:
        fails.append('G-ROW/G-ANCESTOR')

    print(chr(10) + '  G-KEY / G-NODEPOSIT (one row; the must-not-hit queries NO KEY; the answer says no deposit action, not pushed, nothing concluded):')

    def qq(s):
        r = subprocess.run([sys.executable, INDEX, '--query', s], capture_output=True, text=True, encoding='utf-8', errors='replace')
        return r.stdout or ''
    o = qq('housekeeping')
    gk = o.count('act      :') == 1 and 'NO DEPOSIT ACTION; NOTHING WAS WRITTEN AT ZENODO' in o and 'TECHNE NOT PUSHED' in o and 'NOTHING IS CONCLUDED ABOUT WHETHER' in o
    for s in ('the deposit moved', 'TECHNE pushed', 'the reply filed'):
        gk = gk and any(ln.strip().startswith('### NO KEY') for ln in qq(s).splitlines())
    print('    %s' % gk)
    if not gk:
        fails.append('G-KEY/G-NODEPOSIT')

    print(chr(10) + '  G-APPENDONLY (banked_index.py: every line of the blob still present, in order):')
    b = blob_of(ROOT, 'tools/banked_index.py')
    sq = subsequence(norm(b).split(chr(10)), norm(idx).split(chr(10))) if b is not None else False
    print('    %s' % sq)
    if not sq:
        fails.append('G-APPENDONLY')

    print(chr(10) + "  G-NOEDIT (owner files, sealed files, the deposit, HANDOFF, the patent repo, the other ledgers: no tracked change beyond the act's files):")
    owners = ['tools/b302_kernel.py', 'tools/b302_correspondence.py', 'tools/b303_correspondence.py', 'tools/b327_faces_row.py', 'tools/reg_seal.py',
              'tools/b300_regspec.py', 'tools/mirror_roster.json', 'tools/lore_rules.py', 'tools/ferry_scan.py', 'tools/FERRY_STANDING.md', 'tools/b236_deposit_fetch.py',
              'HANDOFF.md', 'data/STRUCK_CLAUSES.md']
    st_r = git(ROOT, 'status', '--porcelain', '--', *owners).strip()
    st_s = [x for x in git(SIDE, 'status', '--porcelain').splitlines() if x.strip() and not x.strip().endswith('CORRESPONDENCE.md')]
    st_p = [x for x in git(PP, 'status', '--porcelain').splitlines() if x.strip() and 'BLOB_SENSITIVITY' not in x and not x.strip().endswith('ERRATA.md')]
    st_pat = git(PAT, 'status', '--porcelain').strip()
    dep = git(PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2').strip()
    others = git(PP, 'status', '--porcelain', 'REGISTRY.md', 'VERIFICATION_LOOM.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md', 'FINDINGS.md').strip()
    gn2 = not st_r and not st_s and not st_p and not st_pat and not dep and not others
    print('    relay %r ; SIDE (beyond the table) %s ; PLACE-papers (beyond ERRATA) %s ; patent repo %r ; deposit %r ; the other ledgers %r : %s' % (st_r, st_s, st_p, st_pat, dep, others, gn2))
    if not gn2:
        fails.append('G-NOEDIT')

    print(chr(10) + '  G-ORDER (the seal verifies; the tools, the runs, the ledger, the row and the bank after the seal):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG], capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    raw = open(REG, 'rb').read()
    committed_reg = blob_of(ROOT, 'data/b337_registration_2026-09-06.txt') is not None
    body = raw if not committed_reg else raw.replace(b'\r\n', b'\n')
    i = body.find(b'=' * 100 + b'\n### THE REGISTRATION SEAL')
    rawhash = hashlib.sha256(body[:i]).hexdigest() if i > 0 else ''
    if not committed_reg:
        seal_m = os.path.getmtime(REG)
        after = all(seal_m < os.path.getmtime(p) for p in [t('b337_fetch.py'), t('b337_errata.py'), t('b337_techne.py'), t('b337_receipts.py'), FRUN, ERUN, TRUN, RRUN, ERRATA, CORR, IDX, BANK])
        how = 'file times (pre-commit)'
    else:
        pre = io.open(d('b337_checks_run.txt'), encoding='utf-8', errors='replace').read() if os.path.exists(d('b337_checks_run.txt')) else ''
        after = 'the tools, the runs, the ledger, the row and the bank after the seal True' in pre
        how = 'the pre-commit suite record'
    go = intact and rawhash == SEAL and after
    print('    seal verifies %s ; hash equals the literal %s ; the tools, the runs, the ledger, the row and the bank after the seal %s [%s] : %s' % (intact, rawhash == SEAL, after, how, go))
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

    print(chr(10) + '  G-NUMBERS (every number the bank quotes, read back from its producing file):')
    checks = []
    got = fj['got']
    checks.append(('the record fields', all(x in bank for x in ('`v1.1.2`', '`2026-07-24`', '`10.5281/zenodo.21539167`', '`10.5281/zenodo.19675355`')) and got['nfiles'] == 11 and '11 files' in bank))
    checks.append(('11 of 11', fj['local_match'] == 11 and '11 of 11' in bank))
    add = re.search(r'WRITTEN \+(\d+) lines', io.open(ERUN, encoding='utf-8').read()).group(1)
    nb = len(norm(eb).rstrip(chr(10)).split(chr(10)))
    na = len(norm(err).rstrip(chr(10)).split(chr(10)))
    nb = nb if not committed else na - int(add)
    checks.append(('+%s lines, %d -> %d' % (add, nb, na), ('+%s lines' % add) in bank and ('`%d -> %d`' % (nb, na)) in bank))
    checks.append(('4c0a6af, 621 insertions, 2 ahead', '4c0a6af' in trun and '621 insertions' in git(TC, 'show', '--stat', '--format=', 'HEAD') and '621 insertions' in bank and 'is 2 commits ahead' in bank))
    checks.append(('22739c9, 6e8638a', '22739c9' in trun and '6e8638a' in trun and '`22739c9`' in bank and '`6e8638a`' in bank))
    rn = re.search(r'last row number is (\d+)', io.open(CORR, encoding='utf-8').read()).group(1)
    checks.append(('row %s' % rn, ('row %s' % rn) in bank))
    sm = re.search(r'bytes sealed : (\d+)', raw.decode('utf-8', 'replace')).group(1)
    checks.append(('%s bytes sealed' % sm, ('%s bytes' % sm) in bank))
    cl = re.search(r'clauses\s*:\s*(\d+)', io.open(SATIS, encoding='utf-8').read()).group(1)
    checks.append(('%s clauses' % cl, ('%s CLAUSES' % cl) in bank))
    checks.append(('five and five', len(ER.DEPOSIT_FACING) == 5 and len(ER.INTERNAL_RECORD) == 5 and all(e in bank for e, _w in ER.DEPOSIT_FACING + ER.INTERNAL_RECORD)))
    for what, ok in checks:
        print('    %-44s %s' % (what, 'PASS' if ok else '### FAIL ###'))
    if not all(ok for _w, ok in checks):
        fails.append('G-NUMBERS')

    print(chr(10) + '  G-ONCE (run files written once per path; the re-runs recorded):')
    once_ok = all(os.path.exists(p) for p in [FRUN, FJ, RECJ, ERUN, ERER, TRUN, TRER, RRUN, CORR, CORRR, IDX, IDXR]) and not os.path.exists(d('b337_errata_run2.txt')) and not os.path.exists(d('b337_techne_run2.txt'))
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

    print(chr(10) + '  G-STEM-APPENDED (extended scope: the ERRATA block, row 184, the index row, the TECHNE commit message, swept):')
    blk = err[err.index(MARK):] if MARK in err else ''
    ib = idx[idx.index("# ### THE WAVE'S HOUSEKEEPING (b337"):idx.index('# ### THE COST CENSUS (b336')] if "# ### THE WAVE'S HOUSEKEEPING (b337" in idx else ''
    cmsg = git(TC, 'log', '-1', '--format=%B')
    for lbl, blk2 in (('the ERRATA block', blk), ('row 184', r184[0] if r184 else ''), ('index row', ib), ('the TECHNE message', cmsg)):
        ch, _ = ferry_scan.scan_text(blk2, struck, stem_list)
        _c, sh = ferry_scan.scan_text(blk2, [], stem_list)
        print('    %-20s struck : %d   stem : %d   (%d chars)' % (lbl, len(ch), len(sh), len(blk2)))
        if ch or sh or not blk2:
            fails.append('G-STEM-APPENDED ' + lbl)

    print(chr(10) + '  G-SHARED:')
    got2 = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got2.add((name, label))
    extra = got2 - {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got2), len(extra), 'PASS' if not extra else '### FAIL ###'))
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

    print(chr(10) + '  HEDGE AUDIT (over every file this act wrote, the ERRATA block, the row, the index row and the TECHNE message included):')
    tmpdir = tempfile.mkdtemp(prefix='b337_hedge_')
    targets = [(os.path.basename(p), p) for p in OWNED if os.path.exists(p) and not p.endswith('.json')]
    for lbl, text in (('the ERRATA block', blk), ('row 184', r184[0] if r184 else ''), ('the index row', ib), ('the TECHNE message', cmsg)):
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
