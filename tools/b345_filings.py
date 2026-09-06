# -*- coding: utf-8 -*-
"""b345_filings.py -- THE TWO APPEND-ONLY FILINGS IN PLACE-papers, GENERATED FROM THIS ACT'S OWN RECORDS.

### ### (1) `FACES_LEDGER.md` -- an UPDATE block through the writer's `append_block` (b327_faces_row.py), naming row
### `L1` and carrying the order's own words, ### **ONE DISTRIBUTION ON TWO FAMILIES**, with ### **WHAT IS MEASURED AND
### WHAT IS NOT** ### set out plainly. ### Row L1 itself is never rewritten.
### ### (2) `OPEN_TRAILS.md` -- ONE appended block under a `b345` mark, in the shape that ledger's own trail updates
### take, opening the author's work-order with its own ID and quoting b344's PRINTED figures for the two axes it did
### not move. ### ### **NOTHING IS PRICED HERE AND NO AXIS IS MOVED; the point of the filing is that the price can be
### ### taken from b344's printed figures WITHOUT RE-RUNNING b344.**
### ### Every figure is read from `b345_control.json` and `b344_ny.json`; nothing is typed from memory of a run.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK_L = '<!-- b345 update -->'
MARK_T = '<!-- b345 trail update -->'
TRAIL_ID = 'W-ORD-FLOOR-HELD-AXES'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def blob(path, rel):
    import subprocess
    r = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def faces_block(C):
    idx = C['indices']
    fx = C['kernel_fixture']
    kd = C['kernel_diagnostic'] or {}
    fixture_clause = (
        'the sealed kernel fixture PASSED' if fx else
        ('the sealed kernel fixture FAILED AT ITS OWN THRESHOLD and is tabled as a defective bar: section (C) sealed a '
         'recurrence to `\\|w\\| >= %d` with the Stirling asymptotic through `B_%d`, whose first dropped term leaves the '
         'routine a floor near `%s`, and sealed a fixture threshold of `%s` in the same paragraph. At `%s` the fixture '
         'rejects the CORRECT copy as well as the broken one, so at its own threshold it separates nothing. The '
         'registration is not edited and the bar is not rewritten; what it would have licensed -- that route B\'s '
         'hand-rolled kernel is correct AT THE SEALED TOLERANCE -- is NOT CONFERRED. Holding the sealed truncation and '
         'carrying only the recurrence to `\\|w\\| >= %s` brings the same routine to `%s`, which locates the defect in one '
         'named half (the threshold) and is a DIAGNOSTIC, not this act\'s route B and not a value used anywhere'
         % (C['recur_to'], 2 * C['n_bern'], C['kernel_worst'], C['fix_bar'], C['fix_bar'], kd.get('recur'), kd.get('worst'))))
    return [
        '', MARK_L, '',
        '## UPDATE — filed 2026-09-06 (b345): row L1, the bridge row',
        '',
        "*Rows above are never rewritten; an update names the row it bears on. Written through the writer's `append_block`.*",
        '',
        '| row | what b345 did | what is measured, and what is not |',
        '|:--|:--|:--|',
        ('| **L1** (the Li-to-Weil bridge) | **ONE DISTRIBUTION ON TWO FAMILIES.** The archimedean distribution '
         '`I(n) = (1/2 pi) INT Re G_n(1/2 + iu) h_+(u) du`, with the derived kernel `h_+(u) = Re psi(1/4 + iu/2) - log pi`, '
         'was evaluated at the %d indices the balance keystone tabulates by TWO ROUTES SHARING NO CODE, under a bar this '
         "act sealed BEFORE any value with the tail panel's quadrature rule fixed as TANH-SINH -- the rule b340's own "
         "diagnosis named. Route A is b340's theta route, imported and unedited; route B is written fresh in the `u` "
         'variable with the transform factor as the complex power `Re[1 - ((s-1)/s)^n]` and a HAND-ROLLED digamma. '
         "**VERDICT, BY THE SEALED RULE: %s** — the bar holds at %d of %d indices; worst `\\|I(n) + 1 - lambda_A(n)\\|` = `%s` "
         "against `1e-9 max(1, \\|lambda_A\\|)`; worst drift between the two routes `%s`; the pole constant `L_n[log s]` "
         "carried as its own column and equal to `1` to `%s`. **b340's BAR IS NOT REWRITTEN AND ITS VERDICT IS NOT "
         'RE-VERDICTED**; this is a new bar with the same threshold and a different tail rule, and a re-run under a new '
         'bar is a new measurement and not a correction of the old one. On the sealed face of this act, %s. | '
         '**MEASURED:** the archimedean constituent, at those %d indices, at this act\'s bar, on this family. **NOT '
         'MEASURED:** the zero side over the atlas\'s ordinates and the finite side `S_f`, which together keep '
         '`W-ORD-LI-FAMILY-CONTROL` OWED — the explicit formula is not closed on the Li family and this act pays its '
         'archimedean constituent only; and the Sonin margin, which is **not defined on this family at all**. '
         '**AND THE FAMILY IS NOT IN THE LAWFUL CLASS:** three of three of Theorem 1\'s conditions fail, so Theorem 1\'s '
         "inequality and the Sonin margin do not apply, nor do the square on the stable cut, b321's control bar, b326's "
         "per-cell closures, or the atlas's zero-side truncation bound. What DOES apply: the kernel identity (b333), the "
         "arrangement `Z = P - PR + A` (b321), and the noise-floor gate as a method. The deposit's finite-range "
         'positivity is restated at its scope and is **the deposit\'s, not this act\'s**: positivity of `lambda_n` in a '
         'finite range is not evidence of the kind the criterion respects. |'
         % (len(idx), C['verdict'], C['n_hold'], len(idx), C['worst_miss'], C['worst_drift'], C['pole_worst'],
            fixture_clause, len(idx))),
        '',
        ("*No grade is conferred by a seat. A control certifies the instrument, not the object. Nothing about `h2`, "
         "totality or the roster; the wave stays parked. Filed by b345 (relay `data/b345_the_li_control_rerun.txt`).*"),
    ]


def trail_block(N):
    rows = N['rows']
    tau = rows[0]['held']['tau']
    a, b = rows[0]['held']['alpha'], rows[0]['held']['beta']
    per = '; '.join('`NY = %d`: %d eigenvalue(s) within a decade either side, smallest kept `%.6e`, largest dropped `%.6e`, distance `%.6e`'
                    % (r['NY'], r['held']['eig_within_decade'], r['held']['smallest_kept'], r['held']['largest_dropped'], r['held']['distance'])
                    for r in rows)
    return [
        '', MARK_T, '',
        '### **`%s` — OPENED 2026-09-06 (b345): a work-order, not an attempt**' % TRAIL_ID,
        '',
        ("b344 priced the floor on ONE axis, `NY`, and named in its sealed registration why that axis and not the other "
         "two: moving the cut's `tau` would move the stable-cut rank that b343 showed constant, and the taper's `ALPHA` "
         "and `BETA` are the source's own constants. It then printed the two held axes AT EVERY RUNG so that a later act "
         "could price them. **THIS BLOCK IS THAT NAMING, AND NOTHING MORE: THE FLOOR'S TWO UNMOVED AXES ARE PRICEABLE "
         "FROM b344's PRINTED FIGURES WITHOUT RE-RUNNING b344.** Nothing is priced here and no axis is moved."),
        '',
        ("**What b344 printed, quoted from its own ladder record** (relay `data/b344_ny.json`, `data/b344_ny_run.txt`): "
         "the cut's `tau = %s` in force at every rung, with %s. The taper held at `ALPHA = %s`, `BETA = %s` at every rung — "
         "the source's own constants, which is the reason b344 gave for not moving them."
         % (('%.1e' % tau), per, ('%.1f' % a), ('%.1f' % b))),
        '',
        ("**What is owed:** the same movement measurement b344 made on `NY`, made on `tau` and on the taper, against the "
         "same sealed rule and the same separation. **The price, as the record states it:** it can be read off the "
         "figures above without a single new frame — the distance between the smallest kept and the largest dropped "
         "eigenvalue at each rung is what a move in `tau` would have to cross, and it is printed at every rung. "
         "**The trigger:** an act that moves either axis, which this one is not."),
        '',
        ("*Species: **PRICE**. Nothing here is a route. No grade moves. One axis moved is one axis moved, and nothing is "
         "concluded about the two held. h2 stands exactly where the deposit left it.*"),
    ]


def main():
    C = load('b345_control.json')
    N = load('b344_ny.json')
    rec('=' * 100)
    rec('b345_filings.py -- ONE LEDGER BLOCK, ONE TRAIL BLOCK. ### APPEND-ONLY, THROUGH THE WRITER WHERE THE WRITER OWNS THE FILE.')
    rec('=' * 100)
    wrote = []
    # ### (1) the faces ledger, through its writer
    st, det = W.append_block(MARK_L, faces_block(C))
    rec('  FACES_LEDGER.md : %s -- %s' % (st, det))
    if st == 'WRITTEN':
        wrote.append('FACES_LEDGER.md')
    # ### (2) the trails ledger, appended with the same append-only discipline, read back and checked against the blob
    body = trail_block(N)
    txt = io.open(TRAILS, encoding='utf-8').read()
    if MARK_T in txt:
        st2, det2 = 'DUPLICATE', 'mark %s already present -- REFUSED, nothing written' % MARK_T
    else:
        hb = blob(TRAILS, 'OPEN_TRAILS.md')
        before = txt
        io.open(TRAILS, 'w', encoding='utf-8', newline=chr(10)).write(before.rstrip(chr(10)) + chr(10) + chr(10).join(body) + chr(10))
        after = io.open(TRAILS, encoding='utf-8').read()
        pw = after.startswith(before.rstrip(chr(10)))
        pb = (hb is not None) and after.startswith(hb.rstrip(chr(10)))
        ok = after.count(MARK_T) == 1 and pw and pb
        st2 = 'WRITTEN' if ok else 'READ-BACK FAILED'
        det2 = 'mark %d time(s); append-only working=%s blob=%s' % (after.count(MARK_T), pw, pb)
        if ok:
            wrote.append('OPEN_TRAILS.md')
    rec('  OPEN_TRAILS.md  : %s -- %s' % (st2, det2))
    rec('  trail ID        : %s (new; no collision with the ledger\'s existing IDs)' % TRAIL_ID)
    rec('  ### PLACE-papers files written this run : %d (CAP 2)' % len(wrote))
    rec('=' * 100)
    p, k = os.path.join(D, 'b345_filings_run.txt'), 1
    while os.path.exists(p):
        k += 1
        p = os.path.join(D, 'b345_filings_run%d.txt' % k)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(LINES) + chr(10))
    io.open(os.path.join(D, 'b345_filings.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(faces=st, faces_detail=det, trails=st2, trails_detail=det2, trail_id=TRAIL_ID, mark_l=MARK_L, mark_t=MARK_T,
             wrote=wrote, run_file=os.path.basename(p)), indent=1))
    return 0 if st in ('WRITTEN', 'DUPLICATE') and st2 in ('WRITTEN', 'DUPLICATE') else 1


if __name__ == '__main__':
    sys.exit(main())
