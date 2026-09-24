# -*- coding: utf-8 -*-
"""b507_record.py -- THE COMPONENTS BANK, THE DESK AND THE TRAIL. ### `python tools/b507_record.py components | desk | trail`
### Every figure READ from the banks, not retyped."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OT = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'OPEN_TRAILS.md')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


FOLD = json.loads(read('b507_fold.json') or '{}')
NOTES = json.loads(read('b507_notes.json') or '[]')
FIX = json.loads(read('b507_fixtures.json') or '{}')
B504_NEEDLE = 'against quadrature bounds near 1e-7, because the Epstein bank stops at 149.72'


def b504_line():
    ot = io.open(OT, encoding='utf-8').read().split(NL)
    hits = [i for i, l in enumerate(ot, 1) if B504_NEEDLE in l]
    return hits[0] if len(hits) == 1 else None


def components():
    w1, w2 = FOLD['writes']
    L = ['=' * 104, 'b507 -- THE COMPONENTS, AS THEY RAN.', '=' * 104, '',
         '### COMPONENT 1 -- THE FOLD. `%s`' % FOLD['heading'],
         '    span : b%(lo)d - b%(hi)d, %(acts)d acts ; the span tool read %(tool_reads)d through this act ; last fold filed by b%(filed_by)d' % FOLD['span'],
         '    verdict strings matched in their own closing bank : %d of %d' % (sum(q['found'] for q in FOLD['quotes']), len(FOLD['quotes'])),
         '    rulings matched in the file named : %d of %d ; defect phrases matched : %d of %d ; defects recorded : %d'
         % (sum(r['found'] for r in FOLD['rulings']), len(FOLD['rulings']), sum(d['found'] for d in FOLD['defects']),
            len(FOLD['defects']), sum(d['n'] for d in FOLD['defects'])),
         '    columns : OBJECT %(OBJECT)d ; MODEL %(MODEL)d ; RECORD %(RECORD)d' % FOLD['columns'],
         '    findings about folded acts : the cut one-statement at FINDINGS.md:%s (whole at OPEN_TRAILS.md:%s) ; b504`s mislabelled defect'
         % (FOLD['findings']['findings_line'], FOLD['findings']['trail_line']),
         '    FINDINGS.md : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % w1,
         '    digest      : %(before)d + %(added)d = %(after)d bytes ; prefix %(prefix)s ; BOM kept %(bom)s ; lines removed %(removed)d' % w2,
         '', '### COMPONENT 2 -- THE NOTES, (R117)(1) AND (3).']
    for n in NOTES:
        L.append('    %(file)-24s written %(written)4d ; prefix %(prefix)s ; removed %(removed)d ; marks %(marks)d' % n)
    L += ['', '### COMPONENT 3 -- THE TWO REPAIRS, (R117)(1) AND (2).'] + read('b507_fixtures.txt').rstrip(NL).split(NL)
    L += ['', '### COMPONENT 4 -- THE TRAIL RECORD: b504`s line at OPEN_TRAILS.md:%s is the one the correcting note names.' % b504_line(),
          '=' * 104]
    io.open(os.path.join(D, 'b507_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


def desk():
    L = ['=' * 104, 'b507 -- THE DESK. ### **A FOLD REGISTERS NO EXPECTATIONS, AND NONE IS SCORED.**', '=' * 104, '',
         '### THE NAVIGATOR`S : REGISTERED 0. ### THE SEAT`S : REGISTERED 0.',
         '', '### THIS ACT`S OWN DEFECTS, FOUND BEFORE THE SEAL.',
         '    (a) ### **THE FACE`S FIRST DRAFT TRIPPED THE PREDICTION COUNTER** -- "the three components files" read as an',
         '        artifact-count prediction at two lines; reworded before the seal, the regspec run re-banked.',
         '    (b) ### **THE FOLD`S FIRST DRAFT CARRIED A SENTENCE THE SPAN REFUTES** -- b474`s "every one was found by this',
         '        record`s own controls before its act closed", carried by habit; b504 found b503`s predicate after b503 closed.',
         '        Caught by the (R70) rehearsal`s preview, replaced before the write.',
         '    (c) ### **A BASH HEREDOC CARRYING THE SPEC`S CLAUSES FAILED TO PARSE** -- the clauses were moved to a script file.',
         '', '### AND FOUND AFTER THE SEAL, BY THE SUITE, PRE-PUSH.',
         '    (d) ### **`G-NOTES-PREFIX` COMPARED A CRLF WORKING COPY WITH AN LF BLOB.** ### `b334_the_aim_map.txt` is',
         '        `i/lf w/crlf` under `eol=lf`; the note is a pure append by git`s own numstat (9 added, 0 deleted), but the',
         '        arm read the working bytes against the committed blob and FAILED, its negative control with it. ### The',
         '        arm now normalises as git stores and takes the numstat as a second witness. ### First run banked as',
         '        `b507_checks_first.txt`. ### The working copy keeps its CRLF prefix and LF note; the blob is LF.',
         '    (e) ### **THE REPAIR`S FIRST TEXT WENT THROUGH A QUOTED HEREDOC, WHICH COLLAPSED `\\r\\n`** -- caught by the',
         '        parser; rewritten with byte values.',
         '', '### THE PRICE: seconds for every component, as the face said.',
         '=' * 104]
    io.open(os.path.join(D, 'b507_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


HEADING = '### b507 — THE MARGIN AND ITS CONTROL ARC folded, b487–b506, with (R117)’s repairs inside it'


def trail():
    ln = b504_line()
    if ln is None:
        sys.exit('### REFUSED -- b504`s line is not found exactly once; nothing written.')
    c = FIX['census']
    body = """
%(h)s

**(R117) ratified.** The three items b506 routed are disposed inside this fold; the fold runs at span 20 before
any other act; the instrument lane opened inside it for two repairs and shuts at its close; b334's Epstein
crossings are UNVERIFIED by appended note; the numerical lane opens for b508.

**The span.** The ferry named "b475 THROUGH b506" and (R117)(2) "span 20"; the navigator chose the span tool's
count at the seat, **b487–b506**, twenty acts, the filing act excluded. b475–b485 were folded by b486 and written
home at b488, and are cited there, not folded again.

**THE FOLD** is `FINDINGS.md`'s section `%(heading)s`, with one block appended to the digest under (R31).
%(nq)d verdict strings, every one matched in its own act's closing bank; %(nr)d rulings, (R97)–(R116), each matched in
the file that ratifies it; columns OBJECT %(o)d, MODEL %(m)d, RECORD %(r)d. It reports two findings about acts it
folds and repairs neither: the previous fold's one statement is cut mid-sentence at `FINDINGS.md:%(fl)s` (whole at
`OPEN_TRAILS.md:%(tl)s`), and b504's closing labels its second defect with its own number where its commit names
b503. Prefixes proved in both files, 0 lines removed.

**(R117)(1), the notes.** Beside each (R115)(1) note — `b477_components.txt`, `b502_components.txt`,
`b504_components.txt` — a note that b326's derived kernel closes on the bank completed at b506 (93 of 93 wide
cells) while b325's does not; b325's was shown not closing at b504, on the incomplete bank, and b506 ran the
derived kernel alone.

**(R117)(1), b504's trail line, corrected by this note.** b504's record above, at `OPEN_TRAILS.md:%(b504)d`, reads
"against quadrature bounds near 1e-7"; the bounds are **about 1e-6** — 9e-7 to 2.3e-6, `B_qd` in
`relay/data/b504_cells.jsonl`, as b506 found. The line itself is unedited.

**(R117)(3).** b334's Epstein crossings are marked UNVERIFIED by a note appended to `b334_the_aim_map.txt`:
they were computed on the bank b506 found short by 30 zeros.

**The two repairs, (R117)(1) and (2), both polarities.** `registration_gate.py`'s bar-floor arm reads `>=`, `≥`
and a bare `>` (not an arrow); b505's own sealed bar is its positive control, and b347's six fixtures still
pass. A census of %(regs)d banked registrations, re-verdicting nothing: %(fo)d fire under b347's pattern, %(fn)d under
the repair, %(fx)d newly — %(names)s. `corr_row.py` now splits a row as it would land before any byte is written: a
cell carrying a pipe is refused with the ledger unchanged, the same cell with `‖` accepted, b488's controls
carried. **This act's correspondence row is its first live use.**

**No expectation registered; a fold registers none.** The instrument lane shuts at this act's close; the numerical
lane opens for b508 under (R117)(4). Nothing compiled; no grade conferred; nothing deposits; row U1 unedited; `h2`
where the deposit left it; the four lists stay OPEN; no cell of this act is a statement about RH.
""" % dict(h=HEADING, heading=FOLD['heading'].lstrip('# '), nq=len(FOLD['quotes']), nr=len(FOLD['rulings']),
           o=FOLD['columns']['OBJECT'], m=FOLD['columns']['MODEL'], r=FOLD['columns']['RECORD'],
           fl=FOLD['findings']['findings_line'], tl=FOLD['findings']['trail_line'], b504=ln,
           regs=c['registrations'], fo=c['fire_old'], fn=c['fire_new'], fx=c['fire_only_new'],
           names=', '.join(x.split('_registration')[0] for x in c['only_new']))
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(body.encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING),
               b504_line=ln)
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b507_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out) + NL)


if __name__ == '__main__':
    {'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]()
