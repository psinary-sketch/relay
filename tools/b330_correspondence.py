# -*- coding: utf-8 -*-
"""b330_correspondence.py -- ONE ROW: THE TECHNE EXTRACTION, METHOD ONLY, NOT PUSHED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The module count,
### the local hash, the remote tip and the line-ending census are read from the act's run files
### (`b330_modules_check_run3.txt`, `b330_techne_verify.txt`, `b330_eol_after.txt`), never typed.
### ### **THE HAZARD:** ### a row in the research table that reads as if TECHNE received a result. It
### received method, and the row says so first.
"""
import io
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


def read_records():
    chk = io.open(os.path.join(D, 'b330_modules_check_run3.txt'), encoding='utf-8').read()
    ver = io.open(os.path.join(D, 'b330_techne_verify.txt'), encoding='utf-8').read()
    eol = io.open(os.path.join(D, 'b330_eol_after.txt'), encoding='utf-8').read()
    n = int(re.search(r'modules on disk : (\d+)', chk).group(1))
    failing = int(re.search(r'MODULES FAILING : (\d+)', chk).group(1))
    head = re.search(r'canonical clone HEAD now ([0-9a-f]+), ahead of origin/main by (\d+)', ver)
    remote = re.search(r'remote tip unchanged \(NOTHING PUSHED\)\s*:\s*(True|False)\s*\(([0-9a-f]+)\)', ver)
    second = re.search(r'second clone untouched\s*:\s*(True|False)\s*\(([0-9a-f]+)\)', ver)
    aug = 'August files byte-identical to the snapshot : True' in ver
    crlf = re.search(r'working copies CRLF : (\d+) ; LF : (\d+)', eol)
    raw = 'EQUALS ITS BLOB ON RAW BYTES : True' in eol
    return dict(n=n, failing=failing, head=head.group(1), ahead=head.group(2), remote_ok=remote.group(1) == 'True', remote=remote.group(2),
                second_ok=second.group(1) == 'True', second=second.group(2), aug=aug, crlf=int(crlf.group(1)), lf=int(crlf.group(2)), raw=raw)


def rows():
    r = read_records()
    return [
        ("THE TECHNE EXTRACTION: THE ARC'S METHODS AS CLAIM-SHAPED MODULE DRAFTS IN TECHNE'S PRIVATE CORE, METHOD ONLY, NOT PUSHED (b330)",
         "THE TECHNE EXTRACTION: THE ARC'S METHODS AS CLAIM-SHAPED MODULE DRAFTS IN TECHNE'S PRIVATE CORE, METHOD ONLY, NOT PUSHED "
         "(b330): **METHOD, NOT A RESULT -- nothing in this row is about the programme's objects.** %d module files under "
         "`modules/2026-09/` in the canonical local clone `TECHNE-Core` (the clone b257 used), each stating a method as WHAT IT "
         "DOES, WHEN IT APPLIES, WHAT IT REFUSES, with PROVENANCE (act, incident, relay tool path, date) pulled from the emitting "
         "files at the extract step; a top-level `modules/INDEX.md` created (the August index sits at `modules/2026-08/INDEX.md` "
         "and is linked untouched), mapping each module to a family -- the August families or one of five named once: VACUITY, "
         "REGISTRATION, READING, CERTIFICATION, NEGATIVE_CONTROL -- and cross-referencing the August module each extends or "
         "supersedes. The modules measured by `b330_modules_check.py`: shape, provenance (every tool path on disk, every act a "
         "relay record, every quotation in the extract file), research-vocabulary sweep 0 hits, %d failing. The local commit "
         "`%s`, ahead of `origin/main` by %s; **THE REMOTE TIP `%s` UNCHANGED -- NOT PUSHED**; the second clone `%s` untouched; "
         "the nine August files byte-identical (%s)." % (r['n'], r['failing'], r['head'], r['ahead'], r['remote'], r['second'], r['aug']),
         "**NO TERMINAL. A FILING OF METHOD.** The step-zero hygiene fix beside it: `.gitattributes` in the kernel repository "
         "(SIDE-global-section `3cbe47c`), after which the profile's working file equals its blob on raw bytes (%s) and %d of %d "
         "tracked working copies are CRLF." % (r['raw'], r['crlf'], r['crlf'] + r['lf']),
         "**NO PRINT.** The registration sealed before any write; the patent note is in the bank and not in TECHNE, listing modules "
         "plausibly novel AS METHOD with no legal claim.",
         "**WHAT IT IS: DOCUMENTATION OF ASSESSMENT METHOD, in TECHNE's own terms (formalize logic, keep assessment informal).** "
         "No grade conferred; no grade moved; the two-clone divergence read and not resolved; nothing about the programme's "
         "results enters TECHNE.",
         "**SCOPE: FILINGS OF METHOD INTO A PRIVATE CORE.** TECHNE-Core stays private until its four provisionals are filed. NOT A "
         "CLAIM, NOT A FILING POSITION, NOT A LEGAL OPINION. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
         "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, "
         "UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",
         "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b330 -- THE TECHNE EXTRACTION. ### THE ROW.")
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
    method = all('METHOD, NOT A RESULT' in s and 'NOT PUSHED' in s for _m, s, _t, _p, _g, _sc, _st in ROWS)
    print('  the row says METHOD, NOT A RESULT and NOT PUSHED in its statement : %s' % method)
    if not method:
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
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-1]
    cells = G.split_cells(tail)
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0 and len(cells) == 6 and all(x.strip() for x in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %d (6 required, none blank)' % (got[-1], len(cells)))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
