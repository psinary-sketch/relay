# -*- coding: utf-8 -*-
"""b337_correspondence.py -- ONE ROW: THE WAVE'S HOUSEKEEPING. NO TERMINAL, AND THE REASON.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The fetch's fields, the ledgers'
### statuses, the TECHNE commit's state and the receipts' statement are read from the run records, never typed.
### ### **THE HAZARD:** a row that reads as if a deposit moved, an entry changed, or a reply were known to be filed.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE_TAIL = ("**SCOPE: HOUSEKEEPING -- FILINGS AND CHECKS, NO CLAIM, NO GRADE, NO DEPOSIT ACTION.** Nothing about the mathematics; no entry moved or "
              "edited; TECHNE local and not pushed; the receipts' absence scoped to the mounted volumes with F: recorded as not mounted. NO "
              "AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
              "lane carried on the patent seat's report, UNCONFIRMED on this seat's record, and this act's check does not confirm it. h2 stands "
              "exactly where the deposit left it. NOTHING DEPOSITS.")


def rows():
    f = json.load(io.open(os.path.join(D, 'b337_fetch.json'), encoding='utf-8'))
    got = f['got']
    led = '; '.join('%s %s' % (k, v['status'].split(' (')[0]) for k, v in f['ledgers'].items())
    tr = io.open(os.path.join(D, 'b337_techne_run.txt'), encoding='utf-8').read()
    m = re.search(r'HEAD now (\w+)', tr)
    head = m.group(1)
    rr = io.open(os.path.join(D, 'b337_receipts_run.txt'), encoding='utf-8').read()
    absent = [ln.strip() for ln in rr.splitlines() if 'ABSENT ON THE MOUNTED VOLUMES' in ln and ln.strip().startswith('64/')]
    er = io.open(os.path.join(D, 'b337_errata_run.txt'), encoding='utf-8').read()
    add = re.search(r'WRITTEN \+(\d+) lines', er).group(1)
    marker = "THE WAVE'S HOUSEKEEPING: THE THREE LEDGERS RECONCILED TO REGISTRY AGAINST A READ-ONLY DEPOSIT FETCH, THE ERRATA PARTITION BY ONE APPENDED HEADER LINE, THE NINE AUGUST TECHNE FILES COMMITTED LOCALLY AND NOT PUSHED, THE PATENT RECEIPTS CHECKED FOR ON DISK (b337, leg 2 of the sortie)"
    return [
        (marker,
         marker + ": one read-only fetch of the public record (version %s, published %s, DOI %s, concept %s, %d files) agrees with REGISTRY's governing "
         "d1-1 row on every field, and the local canonical copy matches the published MD5s at %d of %d; the three ledgers scored against it -- %s -- "
         "the one drift (ERRATA's head naming v1.1.1 as current) repaired by an APPENDED currency note, the head not edited, entries never restated. "
         "THE PARTITION, per the author's ruling ratified by the sortie paste: one block appended to ERRATA (+%s lines), five entries DEPOSIT-FACING "
         "and five INTERNAL-RECORD, each placed by its own words, every entry unmoved and byte-identical. THE TECHNE COMMIT, per the ruling: the "
         "nine August module files staged by explicit list and committed at %s in the canonical local clone, the remote read before and after and "
         "unchanged, the clone two commits ahead, NOT PUSHED; the second clone untouched. THE RECEIPTS: %s; F: (where the file wrappers were read on "
         "2026-08-30) not mounted this session; the four office notices and the 2026-08-30 response packages present; the repo of record has no "
         "remote and nothing newer than 2026-08-30. NOTHING IS CONCLUDED ABOUT WHETHER A REPLY WAS FILED."
         % (got['version'], got['date'], got['doi'], got['concept'], got['nfiles'], f['local_match'], f['local_total'], led, add, head, '; '.join(absent)),
         "**NO TERMINAL, AND THE REASON: A HOUSEKEEPING ACT** -- filings and checks; nothing is decided.",
         "**NO PRINT.** One appended block in ERRATA; a local commit in a private clone; two run files that state what is and is not on disk.",
         "**NO GRADE.** Nothing about the mathematics; no deposit action; no entry moved.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b337 -- THE WAVE'S HOUSEKEEPING. ### THE ROW.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = 'NO TERMINAL, AND THE REASON' in ROWS[0][2] and 'A HOUSEKEEPING ACT' in ROWS[0][2] and 'NOT PUSHED' in ROWS[0][1] and 'NOTHING IS CONCLUDED ABOUT WHETHER A REPLY WAS FILED' in ROWS[0][1]
    print('  the row says NO TERMINAL with its reason, not pushed, nothing concluded about the reply : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip(chr(10)).split(chr(10))[-1]
    cells = G.split_cells(tail)
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0 and len(cells) == 6 and all(x.strip() for x in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %d (6 required, none blank)' % (got[-1], len(cells)))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
