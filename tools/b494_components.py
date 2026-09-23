# -*- coding: utf-8 -*-
"""b494_components.py -- THE COMPONENTS. ### TWO TABLES, FILED TO FINDINGS AS ONE SECTION.

### ### **TABLE 1 (R104):** ### the July census's twenty and the current desk's six, each disposed
### TAKEN UP BY (R104) / TRIPPED BY (R104) / UNTOUCHED with the sequence act named in the cell.
### ### **TABLE 2 (R105):** ### nine findings, each with its address, its grade AS THE RECORD
### HOLDS IT, and the ceiling sentence it must not exceed. ### **A ROW WITH NO ADDRESS READS
### `NAMES NOTHING` AND IS NOT RESTATED.**
### ### **THIS ACT CONFERS NO GRADE.** ### It reports what the record holds.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FND = os.path.join(PP, 'FINDINGS.md')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SEQ = {
    1: 'b493 (closed)',
    2: 'the SIDE-explicit-formula creation under (R103)',
    3: "b321's identity derived from the vendored explicit formula",
    4: 'h2 stated as one Prop, the sign of A - PR with K8 as binder',
    5: 'the W-ORD-QUADRATURE-BOUND repair',
    6: 'the ladder extended past sqrt 32, the asymptote of m(a) read',
    7: 'the register-equivalence read at the compiled Prop',
}

U = 'UNTOUCHED'

# ### the July census, read at its archive address. ### (grade, item, disposition, cell)
CENSUS = [
    (1, 'DIRECT', 'Barrier extension -- fuller mollifier-class statement; search for an '
     'un-excluded class', U,
     'acts 5 and 6 repair and extend the INSTRUMENT that prices the Li detection exponent; '
     'NEITHER searches for an un-excluded class, which is this item`s own work'),
    (2, 'DIRECT', 'W-SIGN-5 -- construct the ZeroActingPairing witness (realization wall)', U,
     'act 4 STATES h2 as a Prop; it constructs no pairing and forecloses no route to one'),
    (3, 'DIRECT', 'W-SIGN-1 -- the prime-ledger-coherence statement', 'TAKEN UP BY (R104)',
     'act 4 -- h2 as the SIGN OF `A - PR` with K8 as binder IS a prime-ledger-coherence '
     'statement, on the object the kernel constructs'),
    (4, 'DIRECT', 'W-PRIME-PHYSICAL -- a physical system whose spectrum realizes the ordinates',
     U, 'no act of the sequence is an outside-math attack'),
    (5, 'DIRECT', 'C5-DIST-A -- the ordinate form of the C5 input/output distance', U,
     'act 7 reads equivalence BETWEEN registers; this item asks for one register`s own '
     'internal distance in ordinate form -- adjacent, not the same work'),
    (6, 'INFORMING', 'Multiplicity map extension -- DH/Epstein double-zero to more RH-false '
     'zeros', U, 'the sequence reads the Epstein CONTROL, not the multiplicity map'),
    (7, 'INFORMING', 'C-invariant Selberg extension', U, ''),
    (8, 'INFORMING', 'W-ORBIT -- orbit invariants, the class-number diagonal', U, ''),
    (9, 'INFORMING', 'W-6-EXT-A -- constructive Lean formalization of a DH/Epstein off-line zero',
     U, 'act 2 vendors an EXPLICIT FORMULA, not a countermodel construction'),
    (10, 'INFORMING', 'gamma-bound `n_one_binding_instance` (BALANCE section E)', U,
     'already landed at pin; no act of the sequence touches it'),
    (11, 'INFORMING', 'W-DISCHARGE-DAY -- the corpus-wide pointer conversion, closure-gated', U,
     'it opens on a sign/derivative CLOSURE; act 4 states the clause, it does not close it'),
    (12, 'INFORMING', 'W-LADDER complexity consult', U,
     'the `ladder` of act 6 is the SUPPORT ladder, a different object entirely'),
    (13, 'INDEPENDENT', 'W-METHOD-EXPORT -- Steane-in-methodology, patent-day content', U, ''),
    (14, 'INDEPENDENT', 'Trivium NumberField v0.2 lift', U, ''),
    (15, 'INDEPENDENT', 'T7 residues -- the topology/CMB pipeline', U, ''),
    (16, 'INDEPENDENT', 'Cosmology remainder', U, ''),
    (17, 'INDEPENDENT', 'TECHNE.Core reconciliation -- two divergent timelines', U,
     'blocked on a clone, and no act of the sequence unblocks it'),
    (18, 'INDEPENDENT', 'Permitted-layer positive definition', U, ''),
    (19, 'INDEPENDENT', 'STRUCTURAL_FRACTION / CONSTANCE / theory-space cluster', U, ''),
    (20, 'INDEPENDENT', '1.5c-12 / 1.5c-14 cross-domain cluster', U, ''),
]

DESK = [
    (1, "File E's arrangement", U, 'provisionally ruled; the operator governs'),
    (2, 'the Day-1 `W_inf` citation-hazard repair', U, ''),
    (3, "b209's rows 46/47 -- six rulings, the author's", U, ''),
    (4, "the fold rulings -- FINDINGS.md's document home", U,
     '### **SETTLED, BUT NOT BY (R104):** ### (R98) ruled a fold`s home is FINDINGS at b488, and '
     '(R105) files this act`s tables there too. ### The cell reads UNTOUCHED because the order '
     'asks what (R104) does, and (R104) does not reach it'),
    (5, 'posture', U, "b213's ruling stands"),
    (6, '`SIGN_ARRANGEMENT`’s proposed repair', U,
     'a CONVENTION reading in a document -- Day-1`s "positive (provable)" row against CC`s '
     'convention -- not the h2 sign clause act 4 states'),
]

CEIL_RED = ('Supportable: RH reduced to a single located clause, reduction machine-verified; '
            'not supportable: RH proved.')

# ### the nine, each with the address LOOKED UP and the grade AS THE RECORD HOLDS IT.
FRAME = [
    ('The four-channel identity `Z = P - PR + A` holds at content, the residual vanishing to the '
     'arithmetic`s own precision.',
     '`relay tools/b321_window.py` `channels()` returns `residual = Z - (P - PR + A)`; banked at '
     '`relay data/b321_rows.json` and re-run at all 35 cells in `b492_cells.json`',
     'MEASURED (bank). ### Floor: the two-side residual, worst `1.07e-05` RELATIVE to the margin '
     'it prices (b490), against b477`s halt floor `1.49e-08` on `W` itself.',
     'A numerical identity holding at every tested cell is a measurement over those cells. ### It '
     'is not a proof of the explicit formula and not a reduction of anything. ### ' + CEIL_RED),
    ('The prime channel switches on at the class boundary `a = sqrt 2`, the first prime power '
     'entering the window exactly there.',
     '`relay data/b492_cells.json` -- the first three rungs bank `pr = 0`; b486`s digest clause '
     '(2) cites this boundary from ### **b110**, outside that fold`s own span',
     'MEASURED (bank). ### Exact: at `a = sqrt 2`, `a^2 = 2` and `2 <= 2` by integer arithmetic, '
     'so no tolerance decides it.',
     'A boundary in an instrument`s support is a fact about the instrument. ### ' + CEIL_RED),
    ('The margin `m(a) = A - PR` is positive at all 35 ladder cells.',
     '`relay data/b477_entries.jsonl`, `kind == "diagonal"`, re-run cell for cell at b492 with '
     '### **all 35 reproducing bit for bit**',
     'MEASURED (bank). ### Floor: b477`s own halt threshold `1.49e-08`; the minimum margin is '
     '`0.024337988` at `a = 4.061553`, six orders above it.',
     'Positivity on a finite chart of 35 widths is a measurement on that chart. ### b489 showed '
     'a least-squares fit of it is a centre line and not a bound. ### ' + CEIL_RED),
    ('A prime power entering the window contributes nothing at its own rung: an entry is a '
     'bookkeeping boundary, not an event.',
     '`relay data/b492_cells.json` and `b492_results.json` -- at all seven boundary cells that '
     'admit their own `n0` the term reads `0.000e+00`, and at 15 of 16 entry steps the entering '
     'terms carry at most `1.6e-03` of `d(pr)`',
     'MEASURED (bank). ### The split `d(pr) = new + drift` is an IDENTITY and closes to `8.5e-17`.',
     'It describes the prime channel only; ### **the archimedean half of `d(m)` is not '
     'decomposed and is not attributed.** ### ' + CEIL_RED),
    ('The Epstein control isolates `Lambda(n) >= 0` as the ingredient specific to `xi`.',
     '### **NAMES NOTHING.**',
     '### **NO GRADE.** ### The record holds no row, terminal or bank asserting this.',
     '### **NOT RESTATED**, as (R105) directs.'),
    ('Per-class exclusion does not compose to joint exclusion: the general commutation fails, as '
     'a theorem.',
     '`SIDE-lv-conservation` at tag `v0.10.0` = `93c27ec`, '
     '`SIDELvConservation/T3_StepNineBridge.lean`, theorem '
     '### **`T3.T3doubleprime_general_commutation_fails`** ### -- and it IS profiled: '
     '`AxiomCheck.lean` line 40 carries `#print axioms` for it among its 32.',
     'A COMPILED AND PROFILED TERMINAL at a pinned tag. ### The record grades the lv terminals '
     '`{propext, Classical.choice, Quot.sound}`; ### **this act confers no grade above DERIVES.**',
     'A countermodel shows a composition FAILS. ### It establishes no positive claim about zeta '
     'and reduces nothing. ### ' + CEIL_RED),
    ('The C7 finite-type hypothesis is false.',
     '`SIDE-lv-conservation` at `v0.10.0`, `SIDELvConservation/C7FiniteTypeFalse.lean`, theorem '
     '### **`C7_finite_type_false`** ### -- ### **COMPILED BUT NOT PROFILED:** ### `AxiomCheck.lean` '
     'at that tag profiles 32 terminals and this is not among them. ### And `OPEN_TRAILS.md` '
     'line 102 still carries it as a ### *"future trail item (optional)"*, a July line the '
     'repository overtook.',
     'A COMPILED terminal at a pinned tag, ### **WITH NO BANKED AXIOM PROFILE.** ### No grade '
     'above DERIVES, and the record supplies no axiom base for this one.',
     'A refuted hypothesis is a negative result about one class. ### ' + CEIL_RED),
    ('K8 and row U1`s sites (i) and (ii) are the SAME OBJECT.',
     '`relay data/b478_components.txt` -- the survey`s own rule fixed before any cell was read, '
     'and ### **exactly two cells read `SAME OBJECT`: (i) x K8 and (ii) x K8**',
     'MEASURED (bank), and b478`s own `(N1)` HELD on it.',
     'An identification between a site and a constituent is a reading of two statements. ### '
     + CEIL_RED),
    ('zeta23`s `EF_lit_zetaZeroConfig` contains b321`s identity.',
     '`relay data/b470_components.txt` and `b470_closing.txt` -- '
     '### **HELD ON CONTAINS, REFUTED ON EVEN**: the containment holds, the evenness clause of '
     'the expectation does not.',
     'b486`s digest clause (3) holds it ### **DERIVES, CONDITIONAL on a profile that had not '
     'run.** ### **THAT PROFILE HAS NOW RUN:** ### b491 read the b475 log and '
     '`EF_lit_zetaZeroConfig` reports `[propext, Classical.choice, Quot.sound]`. ### The grade `'
     'the record holds` is therefore DERIVES with its condition ### **DISCHARGED BY b491**, and '
     'no higher.',
     'Containment of an identity inside another kernel`s explicit formula is a statement about '
     'two formalisations. ### ' + CEIL_RED),
]


def rec(s=''):
    L.append(s)
    print(s)


def main():
    rec('=' * 120)
    rec('b494 -- THE COMPONENTS. ### TWO TABLES, ONE SECTION.')
    rec('=' * 120)

    # ============================================================ TABLE 1
    rec('')
    rec('### TABLE 1 -- THE SEQUENCE AGAINST THE RECORD. ### **(R104).**')
    rec('-' * 120)
    rec('    ### the July census, read at '
        '`archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-...md:2471`')
    rec('')
    rec('    %-4s %-13s %-62s %s' % ('#', 'h2 grade', 'item', 'disposition'))
    rec('    ' + '-' * 112)
    for n, g, item, d, why in CENSUS:
        rec('    %-4d %-13s %-62s %s' % (n, g, item[:62], d))
        if why:
            for chunk in [why[i:i + 100] for i in range(0, len(why), 100)]:
                rec('         %s' % chunk)
    rec('')
    rec('    ### the desk, read at `OPEN_TRAILS.md:3420` (filed 2026-08-28, b234) -- SIX rows')
    rec('')
    for n, item, d, why in DESK:
        rec('    D%-3d %-13s %-62s %s' % (n, '(desk)', item[:62], d))
        if why:
            for chunk in [why[i:i + 100] for i in range(0, len(why), 100)]:
                rec('         %s' % chunk)
    tu = [c for c in CENSUS if c[3] != U] + [d for d in DESK if d[2] != U]
    direct = [c for c in CENSUS if c[1] == 'DIRECT']
    dtu = [c for c in direct if c[3] != U]
    rec('')
    rec('    ### ### **TAKEN UP BY (R104) : %d. ### TRIPPED BY (R104) : 0. ### UNTOUCHED : %d.**'
        % (len(tu), 26 - len(tu)))
    rec('    ### of the ### **%d DIRECT** ### items, ### **%d** ### read TAKEN UP.'
        % (len(direct), len(dtu)))
    rec('    ### ### **AND THAT IS THE TABLE`S OWN FINDING.** ### The (R104) sequence is an')
    rec('    ### EXPLICIT-FORMULA AND h2-STATEMENT sequence; the July DIRECT bench is a')
    rec('    ### REALIZATION-WALL ATTACK bench. ### **THEY MEET AT ONE ITEM.** ### The sequence')
    rec('    ### does not discharge the July census and this act does not pretend it does.')
    rec('    ### ### **AND NOTHING IS TRIPPED.** ### No act of the sequence forecloses a route')
    rec('    ### any item of either register was taking.')

    # ============================================================ TABLE 2
    rec('')
    rec('### TABLE 2 -- THE FRAME CHECK. ### **(R105).**')
    rec('-' * 120)
    for i, (f, addr, grade, ceil) in enumerate(FRAME, 1):
        rec('')
        rec('    ### **%d. %s**' % (i, f))
        rec('       ADDRESS : %s' % addr)
        rec('       GRADE   : %s' % grade)
        rec('       CEILING : %s' % ceil)
    nn = sum(1 for f in FRAME if 'NAMES NOTHING' in f[1])
    rec('')
    rec('    ### ### **ROWS : 9. ### WITH AN ADDRESS : %d. ### `NAMES NOTHING` : %d.**'
        % (9 - nn, nn))
    rec('    ### ### **NO ROW CARRIES A GRADE ABOVE `DERIVES` FOR A TERMINAL OR ABOVE `MEASURED`')
    rec('    ### FOR A BANK**, and every row carries the ceiling sentence it must not exceed.')
    rec('    ### ### **THIS ACT CONFERS NO GRADE.** ### Each grade cell reports what the record')
    rec('    ### holds; where the record holds none, the cell says so.')

    # ============================================================ the section
    rec('')
    rec('### THE SECTION, FILED TO FINDINGS.')
    rec('-' * 120)
    sec = []
    sec.append('')
    sec.append('## THE RECONCILIATION AND THE FRAME CHECK, b494 — TWO TABLES')
    sec.append('')
    sec.append('*Filed at b494 on rulings `(R104)` and `(R105)`. **Two tables, one section; no '
               'other document is created.** Table 1 reconciles the fixed forward sequence with '
               'the living record; Table 2 checks the frame. **No grade is conferred here** '
               '— every grade cell reports what the record holds.*')
    sec.append('')
    sec.append('### Table 1 — the sequence against the record')
    sec.append('')
    sec.append('**Sources.** The 2026-07-26 pending-work census is **not in the live loom** '
               '— the twenty-fifth seam’s split moved it to '
               '`archive/2026-08-24-ledger-split/VERIFICATION_LOOM-archive-1-dated-log-through-'
               'nineteenth-seam.md`, line 2471, where it stands as a twenty-item table graded '
               '`DIRECT` / `INFORMING` / `INDEPENDENT`. The desk is `OPEN_TRAILS.md:3420`, filed '
               '2026-08-28 at b234, and carries **six** rows.')
    sec.append('')
    sec.append('| # | h2 grade | item | disposition |')
    sec.append('|--:|:--|:--|:--|')
    for n, g, item, d, why in CENSUS:
        sec.append('| %d | %s | %s | %s |' % (n, g, item, ('**%s**' % d) if d != U else d))
    for n, item, d, why in DESK:
        sec.append('| D%d | *(desk)* | %s | %s |' % (n, item, d))
    sec.append('')
    sec.append('**TAKEN UP BY (R104): %d. TRIPPED BY (R104): 0. UNTOUCHED: %d.** Of the five '
               '`DIRECT` items, **%d** reads TAKEN UP — item 3, `W-SIGN-1`, because act 4 '
               'states h2 as *the sign of `A - PR` with K8 as binder*, which is a '
               'prime-ledger-coherence statement.' % (len(tu), 26 - len(tu), len(dtu)))
    sec.append('')
    sec.append('**And that is the table’s own finding.** The `(R104)` sequence is an '
               'explicit-formula and h2-statement sequence; the July `DIRECT` bench is a '
               'realization-wall attack bench. **They meet at one item.** The sequence does not '
               'discharge the July census, and **nothing is tripped**: no act of the sequence '
               'forecloses a route either register was taking.')
    sec.append('')
    sec.append('### Table 2 — the frame check')
    sec.append('')
    sec.append('*Each finding in one sentence; the address that carries it; its grade as the '
               'record holds it; the ceiling sentence it must not exceed. **A row with no address '
               'reads NAMES NOTHING and is not restated.***')
    sec.append('')
    for i, (f, addr, grade, ceil) in enumerate(FRAME, 1):
        sec.append('**%d. %s**' % (i, f))
        sec.append('')
        sec.append('- **Address** — %s' % addr)
        sec.append('- **Grade** — %s' % grade)
        sec.append('- **Ceiling** — %s' % ceil)
        sec.append('')
    sec.append('**Rows: 9. With an address: %d. NAMES NOTHING: %d.** No row carries a grade above '
               '`DERIVES` for a terminal or above `MEASURED` for a bank.' % (9 - nn, nn))
    sec.append('')
    sec.append('**Two readings this table produced that the record did not already hold.** '
               '`C7_finite_type_false` is **compiled but not profiled** — `AxiomCheck.lean` '
               'at `v0.10.0` lists 32 terminals and this is not among them, while '
               '`OPEN_TRAILS.md:102` still carries it as a *“future trail item '
               '(optional)”*. And row 9’s condition, which b486 recorded as *conditional '
               'on a profile that has not run*, **was discharged at b491**: that profile ran and '
               'reported the standard three.')
    sec.append('')
    sec.append('*Filed by b494 on `(R104)` and `(R105)`. Nothing above this section was edited; '
               'no grade is conferred by a seat; nothing about RH follows from either table.*')
    sec.append('')
    body = NL.join(sec)

    head = '## THE RECONCILIATION AND THE FRAME CHECK, b494 — TWO TABLES'
    raw = io.open(FND, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    eol = chr(13) + NL if (chr(13) + NL).encode() in raw else NL
    old = raw.decode('utf-8-sig', 'replace').replace(chr(13), '')
    if head in old:
        rec('    ### ### **THE SECTION IS ALREADY IN `FINDINGS.md`. ### NOT APPENDING AGAIN.**')
        rec('    ### occurrences : %d' % old.count(head))
        after = raw
    else:
        add = (eol + eol.join(body.split(NL))).encode('utf-8')
        io.open(FND, 'ab').write(add)
        after = io.open(FND, 'rb').read()
        rec('    bytes before / appended / after : %d / %d / %d' % (len(raw), len(add), len(after)))
    new = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    missing = [x for x in old.split(NL) if x not in set(new.split(NL))]
    rec('    PRIOR BYTES A TRUE PREFIX : ### **%s** ### ; BOM preserved : ### **%s**'
        % (after.startswith(raw) or head in old,
           after.startswith(b'\xef\xbb\xbf') == bom))
    rec('    ### ### **LINES OF THE OLD FILE ABSENT FROM THE NEW : %d.**' % len(missing))
    rec('    headings named b494 : ### **%d** ### (must be 1)' % new.count(head))
    rec('    ### ### **ONE SECTION, BOTH TABLES, AND NO OTHER DOCUMENT CREATED.**')

    rec('')
    rec('=' * 120)
    io.open(os.path.join(D, 'b494_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(census=[dict(n=c[0], grade=c[1], item=c[2], disposition=c[3]) for c in CENSUS],
                   desk=[dict(n=d[0], item=d[1], disposition=d[2]) for d in DESK],
                   frame=[dict(finding=f[0], address=f[1], grade=f[2], ceiling=f[3])
                          for f in FRAME],
                   taken_up=len(tu), tripped=0, untouched=26 - len(tu),
                   direct=len(direct), direct_taken=len(dtu), names_nothing=nn,
                   headings=new.count(head), lines_removed=len(missing)),
              io.open(os.path.join(D, 'b494_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b494_components.txt, b494_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
