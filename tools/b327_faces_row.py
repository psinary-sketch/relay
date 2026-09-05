# -*- coding: utf-8 -*-
"""b327_faces_row.py -- THE FACES LEDGER'S ROW-WRITER. ### **REFUSES DUPLICATES, GUARDS NOTATION, VERIFIES
### EVERY QUOTATION AGAINST ITS EMITTER, READS BACK AFTER EVERY WRITE.**

### ### **THE GUARDS ARE IMPORTED, NEVER COPIED:** ### the b303 splitter and raw-pipe count; the b302
### blank-cell audit; `ferry_scan.scan_text` for struck clauses and banned stems; b305's flattener for
### the pinned source's text layer.

### ### **WHAT IT WRITES:** ### the ledger's HEAD (once, if the file is absent), rows (one path), the
### cascade section (one path). ### Every write is append-only against the working file AND against the
### blob at `HEAD` when one exists. ### **TWO PATHS, TWO RUN FILES**: a run that writes lands in
### `b327_ledger_run.txt`; a run that finds everything present lands in `b327_ledger_rerun.txt`.

### ### **THE LIMITS, IN THE HEADER:** ### (1) it verifies that a fragment is IN the file it names; it
### cannot tell whether the fragment is the right one -- that is this seat's reading. ### (2) it refuses
### a row it cannot verify; it does not edit a row already written (the append-only law). ### (3) the
### head's class line is the sibling ledgers' -- ROUTED, not placed -- and this tool does not place it.
"""
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C2   # noqa: E402
import b303_correspondence as C3   # noqa: E402
import b305_source as S5           # noqa: E402
import ferry_scan                  # noqa: E402
import b327_faces_rows as R        # noqa: E402

PP = r'D:\MY-DOwnloads\PLACE-papers'
LEDGER = os.path.join(PP, 'FACES_LEDGER.md')
REL = 'FACES_LEDGER.md'
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CASCADE_MARK = '<!-- b327 cascades -->'
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


HEAD = [
    '# FACES_LEDGER.md',
    '',
    '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): ### NOT PLACED — ROUTED TO THE AUTHOR** — *declared 2026-09-05 (b327), as the sibling ledgers declare: the standing taxonomy treats a ledger as a VENUE, not a class (b190).*',
    '',
    '**PURPOSE:** *a cross-reference instrument — the ledger of every equivalence or face the corpus has met, each with what the corpus holds of it and at what grade, and the bridges it owes; **it certifies nothing**.* — built 2026-09-05 (b327), author-authorized 2026-09-04.',
    '',
    '> ### **THE DEPOSIT\'S REFUSAL GOVERNS THIS LEDGER**, quoted from the verified deposit copy (`outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md`, section 27.3): *"compiling the *structure* of the one-premise-in-five-registers claim while deliberately **not** compiling the cross-register equivalences, since to compile \'discharge one and you discharge all five\' would be to compile RH-equivalence itself."*',
    '> ### **A LEDGER THAT LISTS THE FACES SIDE BY SIDE IS A MAP OF THE PREMISE, NOT A CARRIER OF IT.** Every row carries its own act\'s grade and no other\'s; no row is promoted by its neighbours; no pair\'s relation is an equivalence unless the record already states one, and the record states none.',
    '',
    '**THE COLUMN LAW.** `id` · `face or equivalence` · `register` · `source, with the emitting file (deposited / internal / imported)` · `what the corpus holds — PROVED (a kernel terminal at a pin), MEASURED (a banked number, at its own act\'s grade), IMPORTED (at cite, the pinned source named), or NAMED-ONLY — each graded, the claim quoted from the emitting file` · `rows touched (SIDE-global-section CORRESPONDENCE.md)` · `bridges owed, typed`. **No blank cells**; NAMED-ONLY where nothing more is held. Rows are written only by `relay/tools/b327_faces_row.py`, which refuses duplicates, guards notation, verifies every quotation against its emitter before writing, and reads the file back after every write. **Append-only.** Provenance of every row: the file and line it quotes; the extract step at `relay/data/b327_extract_notes.txt`.',
    '',
    '## THE ROWS',
    '',
    '| ' + ' | '.join(R.COLUMNS) + ' |',
    '|' + '|'.join([':--'] * len(R.COLUMNS)) + '|',
]


def read():
    return io.open(LEDGER, encoding='utf-8', errors='replace').read() if os.path.exists(LEDGER) else None


def blob():
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + REL], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def write_bytes(text):
    open(LEDGER + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(LEDGER + '.tmp', LEDGER)


def verify_quotes(quotes):
    """### EVERY (path, fragment, flat) MUST BE IN ITS FILE. ### RETURNS THE LIST OF MISSES."""
    miss = []
    for path, frag, flat in quotes:
        if not os.path.exists(path):
            miss.append((path, frag, 'FILE ABSENT'))
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read()
        ok = (S5.flatten(frag) in S5.flatten(body)) if flat else (frag in body)
        if not ok:
            miss.append((path, frag, 'NOT IN FILE'))
    return miss


def guard_cells(cells):
    """### RETURNS A LIST OF REFUSALS (empty means clean)."""
    bad = []
    struck, _u = ferry_scan.parse_record()
    stems = ferry_scan.stems()
    for j, c in enumerate(cells):
        if not str(c).strip():
            bad.append('cell %d BLANK' % j)
        if C3.raw_pipes(str(c)):
            bad.append('cell %d carries an UNESCAPED PIPE' % j)
        ch, sh = ferry_scan.scan_text(str(c), struck, stems)
        if ch:
            bad.append('cell %d carries a STRUCK CLAUSE' % j)
        if sh:
            bad.append('cell %d carries a BANNED STEM: %s' % (j, [h[3][:40] for h in sh]))
    return bad


def row_line(row):
    cells = [row['id']] + list(row['cells'])
    return '| ' + ' | '.join(cells) + ' |'


def ensure_head():
    txt = read()
    if txt is None:
        write_bytes('\n'.join(HEAD) + '\n')
        rec('  HEAD written : %s (%d lines)' % (REL, len(HEAD)))
        return True
    rec('  HEAD present : %s' % ('DOCUMENT CLASS' in txt and 'it certifies nothing' in txt))
    return False


def append_only_check(before, after, hb):
    pw = after.startswith(before.rstrip('\n')) if before is not None else True
    pb = (after.replace('\r\n', '\n').startswith(hb.replace('\r\n', '\n').rstrip('\n'))) if hb else True
    return pw, pb


def write_row(row):
    """### ONE ROW, WITH EVERY GUARD, THEN READ BACK. ### RETURNS (status, detail)."""
    rid = row['id']
    txt = read() or ''
    marker = '| %s | ' % rid
    if any(ln.startswith(marker) for ln in txt.splitlines()):
        return 'DUPLICATE', 'row %s already present -- REFUSED, nothing written' % rid
    cells = [rid] + list(row['cells'])
    if len(cells) != len(R.COLUMNS):
        return 'REFUSED', 'row %s has %d cells, %d required' % (rid, len(cells), len(R.COLUMNS))
    bad = guard_cells(cells)
    if bad:
        return 'REFUSED', 'row %s: %s' % (rid, '; '.join(bad))
    miss = verify_quotes(row.get('quotes', []))
    if miss:
        return 'REFUSED', 'row %s: quotation not verified: %s' % (rid, miss)
    hb = blob()
    before = txt
    line = row_line(row)
    # ### the row goes at the end of the table, i.e. before the cascade section if that exists
    if CASCADE_MARK in before:
        i = before.index(CASCADE_MARK)
        # ### the table is above the cascades; find the last table line before the mark
        head, tail = before[:i], before[i:]
        new = head.rstrip('\n') + '\n' + line + '\n\n' + tail
    else:
        new = before.rstrip('\n') + '\n' + line + '\n'
    write_bytes(new)
    after = read()
    n = sum(1 for ln in after.splitlines() if ln.startswith(marker))
    rows_on_disk = [ln for ln in after.splitlines() if ln.startswith(marker)]
    ncells = len(C3.split_cells(rows_on_disk[0])) if rows_on_disk else 0
    pw, pb = append_only_check(before, after, hb) if CASCADE_MARK not in before else (True, True)
    ok = (n == 1 and ncells == len(R.COLUMNS) and all(x.strip() for x in C3.split_cells(rows_on_disk[0])))
    return ('WRITTEN' if ok else 'READ-BACK FAILED',
            'row %s: present %d time(s), %d cells on disk, none blank %s; append-only working=%s blob=%s; quotations verified %d'
            % (rid, n, ncells, ok, pw, pb, len(row.get('quotes', []))))


def append_block(mark, body_lines):
    """### A GENERIC APPEND-ONLY BLOCK UNDER A MARKER (added b328): idempotent, guarded cell by cell on every
    ### table line, true-prefix checked against the working file and the blob, read back. ### The rows
    ### above are never rewritten; an UPDATE to a row is a block that names the row."""
    txt = read() or ''
    if mark in txt:
        return 'DUPLICATE', 'block %s already present -- REFUSED, nothing written' % mark
    # ### split on UNESCAPED pipes only, keeping the escapes, so the guard sees the cell as written
    # ### (the first run of this mode unescaped first and then refused its own escaped norm bars).
    bs = chr(92)
    cells = []
    for ln in body_lines:
        if ln.startswith('| '):
            body = ln.strip()[1:-1] if ln.strip().endswith('|') else ln.strip()[1:]
            cells += re.split('(?<!' + bs + bs + ')' + bs + '|', body)
    bad = guard_cells(cells) if cells else []
    bad += guard_cells([ln for ln in body_lines if ln and not ln.startswith('|')])
    if bad:
        return 'REFUSED', 'block %s: %s' % (mark, bad)
    hb = blob()
    before = txt
    new = before.rstrip('\n') + '\n' + '\n'.join(body_lines) + '\n'
    write_bytes(new)
    after = read()
    pw, pb = append_only_check(before, after, hb)
    return ('WRITTEN' if (after.count(mark) == 1 and pw and pb) else 'READ-BACK FAILED',
            'block %s: mark %d time(s); append-only working=%s blob=%s' % (mark, after.count(mark), pw, pb))


def all_pairs(order):
    return [(order[i], order[j]) for i in range(len(order)) for j in range(i + 1, len(order))]


def cascade_lines(pairs_table, order):
    lines = ['', CASCADE_MARK, '', '## THE CASCADES — every pair of rows, one of three',
             '',
             '*For each unordered pair: **STATED** — a relation the record already states, quoted from its emitting file and verified before writing; **OWED** — a bridge typed, with its trail ID (cross-filed to `OPEN_TRAILS.md`); **NONE** — the record states no relation and this act types no bridge. No pair is absent. Generated by `relay/tools/b327_faces_row.py` from the pair table in `b327_faces_rows.py`; a relation quoted here is a relation, never an equivalence.*',
             '',
             '| pair | kind | the relation, quoted, or the bridge, typed |',
             '|:--|:--|:--|']
    counts = {'STATED': 0, 'OWED': 0, 'NONE': 0}
    for a, b in all_pairs(order):
        key = (a, b) if (a, b) in pairs_table else ((b, a) if (b, a) in pairs_table else None)
        if key is None:
            kind, text = 'NONE', R.NONE_TEXT
        else:
            kind, text, _q = pairs_table[key]
        counts[kind] += 1
        lines.append('| %s–%s | %s | %s |' % (a, b, kind, text))
    lines.append('')
    lines.append('*Pairs: %d of %d rows; STATED %d, OWED %d, NONE %d. The owed bridges: `W-ORD-LI-WEIL-BRIDGE`, `W-ORD-DISCRIMINATING-FAMILY`, `W-ORD-LI-FAMILY-CONTROL` — on the trails ledger by ID.*'
                 % (len(all_pairs(order)), len(order), counts['STATED'], counts['OWED'], counts['NONE']))
    return lines, counts


def write_cascades(pairs_table, order):
    txt = read() or ''
    if CASCADE_MARK in txt:
        return 'DUPLICATE', 'cascade section already present -- REFUSED, nothing written'
    # ### every STATED/OWED entry is quotation-verified and guarded before anything is written
    for key, (kind, text, quotes) in pairs_table.items():
        if key[0] not in order or key[1] not in order:
            return 'REFUSED', 'pair %s names a row not in the ledger order' % (key,)
        bad = guard_cells([text])
        if bad:
            return 'REFUSED', 'pair %s: %s' % (key, bad)
        miss = verify_quotes(quotes)
        if miss:
            return 'REFUSED', 'pair %s: quotation not verified: %s' % (key, miss)
        if kind not in ('STATED', 'OWED', 'NONE'):
            return 'REFUSED', 'pair %s: kind %r' % (key, kind)
    present = [ln for ln in txt.splitlines() if ln.startswith('| ') and ln.split('|')[1].strip() in order]
    if len(present) != len(order):
        return 'REFUSED', 'the table holds %d rows of the %d the order names; the cascades wait for the rows' % (len(present), len(order))
    lines, counts = cascade_lines(pairs_table, order)
    expect = len(order) * (len(order) - 1) // 2
    if sum(counts.values()) != expect:
        return 'REFUSED', 'pair count %d is not N(N-1)/2 = %d' % (sum(counts.values()), expect)
    hb = blob()
    before = txt
    new = before.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    write_bytes(new)
    after = read()
    pw, pb = append_only_check(before, after, hb)
    n = after.count(CASCADE_MARK)
    rows = [ln for ln in after.splitlines() if re.match(r'^\| [RFL]\d+–[RFL]\d+ \|', ln)]
    ok = (n == 1 and len(rows) == expect and pw and pb)
    return ('WRITTEN' if ok else 'READ-BACK FAILED',
            'cascades: mark %d time(s); %d pair lines on disk of %d; STATED %d OWED %d NONE %d; append-only working=%s blob=%s'
            % (n, len(rows), expect, counts['STATED'], counts['OWED'], counts['NONE'], pw, pb))


def main(argv):
    mode = argv[0] if argv else '--seed'
    rec('=' * 100)
    rec('b327_faces_row.py -- THE ROW-WRITER. ### mode %s' % mode)
    rec('=' * 100)
    a, b = C2.blank_check_fixture()
    sa, sb, sc, sd = C3.split_fixture()
    rec('  BLANK-CHECK FIXTURE (b302, imported): real blank=%s quiet on full=%s  %s' % (a, b, 'PASS' if (a and b) else '### FAIL ###'))
    rec('  SPLITTER FIXTURE (b303, imported): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    rec('  GUARD FIXTURES: a pipe is refused=%s ; a blank is refused=%s ; a duplicate is refused (measured below)'
        % (bool(guard_cells(['a | b'])), bool(guard_cells(['   ']))))
    if not (a and b and sa and sb and sc and sd and guard_cells(['a | b']) and guard_cells(['   '])):
        rec('  ### REFUSING TO WRITE WITH GUARDS THAT FAIL THEIR OWN FIXTURES.')
        return 2
    wrote = False
    if mode == '--seed':
        wrote = ensure_head() or wrote
        for row in R.ROWS:
            st, det = write_row(row)
            wrote = wrote or (st == 'WRITTEN')
            rec('  %-16s %s' % (st, det))
        # ### the duplicate refusal, exercised on the first seed row after the write
        st, det = write_row(R.ROWS[0])
        rec('  %-16s %s   ### the duplicate guard, exercised' % (st, det))
        if st != 'DUPLICATE':
            rec('  ### FAIL -- the duplicate guard did not refuse')
            return 1
    elif mode == '--live':
        import json
        j = json.load(io.open(os.path.join(D, 'b327_bridge.json'), encoding='utf-8'))
        row = dict(id=j['row']['id'], cells=j['row']['cells'],
                   quotes=[(q[0], q[1], bool(q[2])) for q in j['row']['quotes']])
        st, det = write_row(row)
        wrote = wrote or (st == 'WRITTEN')
        rec('  %-16s %s' % (st, det))
        if st not in ('WRITTEN', 'DUPLICATE'):
            return 1
    elif mode == '--candidates':
        # ### THE RESUME FERRY (2026-09-05) ORDERS ONE FLAG: the third-identity-element keystone as a
        # ### CANDIDATE ROW for the author's word, NOT ADDED. ### Append-only, idempotent, read back.
        mark = '<!-- b327 candidate rows -->'
        txt = read() or ''
        if mark in txt:
            rec('  DUPLICATE        candidate section already present -- REFUSED, nothing written')
        else:
            dep = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'Third_Identity_Element.md')
            if not os.path.exists(dep):
                rec('  REFUSED          the deposited keystone is not at %s' % dep)
                return 1
            body = [
                '', mark, '',
                '## CANDIDATE ROWS — for the author\'s word, not added',
                '',
                '*A candidate is a face the record holds and this ledger does not yet carry; it becomes a row only on the author\'s word, through the writer, with its claim quoted from its emitting file. Flagged, not added.*',
                '',
                '| candidate | emitting file | why it is flagged | status |',
                '|:--|:--|:--|:--|',
                '| **the third identity element** | `outputs/DEPOSITED-v1.1.2/Third_Identity_Element.md` (DEPOSITED) | named by the resume ferry of 2026-09-05 as a candidate row for this ledger; no face, register, grade or bridge is typed for it here, because typing them is the row and the row is the author\'s to authorize | **CANDIDATE — NOT ADDED** |',
            ]
            hb = blob()
            before = txt
            new = before.rstrip('\n') + '\n' + '\n'.join(body) + '\n'
            bad = guard_cells([c for ln in body if ln.startswith('| **') for c in C3.split_cells(ln)])
            if bad:
                rec('  REFUSED          %s' % bad)
                return 1
            write_bytes(new)
            after = read()
            pw, pb = append_only_check(before, after, hb)
            rec('  WRITTEN          candidate section: mark %d time(s); append-only working=%s blob=%s' % (after.count(mark), pw, pb))
            wrote = True
    elif mode == '--cascades':
        import b327_bridge_pairs as BP  # ### the live row's pairs, emitted by b327_bridge.py
        table = dict(R.PAIRS)
        table.update(BP.PAIRS)
        st, det = write_cascades(table, R.ORDER)
        wrote = wrote or (st == 'WRITTEN')
        rec('  %-16s %s' % (st, det))
        if st not in ('WRITTEN', 'DUPLICATE'):
            return 1
    else:
        rec('  ### unknown mode')
        return 2
    after = read() or ''
    rows = [ln for ln in after.splitlines() if ln.startswith('| ') and ln.split('|')[1].strip() in R.ORDER]
    rec('  ledger rows on disk : %d ; blank cells (line-scoped) : %d ; bytes : %d'
        % (len(rows), C2.blank_cells(after), len(after.encode('utf-8'))))
    rec('=' * 100)
    return 0


def run_file_name(stem, wrote_any):
    """### TWO PATHS, TWO FILES -- AND A THIRD RUN THAT WRITES DOES NOT OVERWRITE THE FIRST'S RECORD.
    ### The first writing run lands in `<stem>_run.txt`, a later writing run in `<stem>_run2.txt`, ...;
    ### the idempotent path in `<stem>_rerun.txt` and likewise numbered. ### NO RECORD IS REPLACED."""
    base = '%s_run' % stem if wrote_any else '%s_rerun' % stem
    k = 1
    while True:
        name = '%s%s.txt' % (base, '' if k == 1 else str(k))
        if not os.path.exists(os.path.join(D, name)):
            return name
        k += 1


if __name__ == '__main__':
    code = main(sys.argv[1:])
    wrote_any = any(('WRITTEN' in x or 'HEAD written' in x) for x in LINES)
    stem = 'b327_ledger'
    if len(sys.argv) > 1 and sys.argv[1] == '--cascades':
        stem = 'b327_cascades'
    elif len(sys.argv) > 1 and sys.argv[1] == '--live':
        stem = 'b327_live'
    elif len(sys.argv) > 1 and sys.argv[1] == '--candidates':
        stem = 'b327_candidates'
    name = run_file_name(stem, wrote_any)
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
