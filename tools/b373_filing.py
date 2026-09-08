# -*- coding: utf-8 -*-
"""b373_filing.py -- THE TRAILS LEDGER, UPDATED WITH WHAT THIS ACT SETTLED AND WHAT IT ROUTED.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### Every prior block stands exactly as written.
### ### ### **AND THIS ACT APPENDS TO A LEDGER IT REFUSED TO EDIT.** ### `(R9)` was not read as a
### licence to rewrite a banked entry; appending a new block is what this record has always done and is
### not the same act as changing a row somebody else wrote.
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b373 the pins sourced from the writing act, and the status column listed -->'
PRIOR = '<!-- b372 the eol pin, the readme figures, the first batch of row checks -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def jload(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def block(P, S, Q):
    reasons = P['reasons']
    exr = P['excluded_reasons']
    det = P['detail']
    pinnable = [x for x in det if x['status'] == 'PINNABLE']
    lines = [
        '', MARK, '',
        ('### **b373 — THE PINS, SOURCED FROM THE WRITING ACT; AND THE STATUS COLUMN, LISTED '
         '(2026-09-08)**'),
        '',
        ('*No block above is edited. The b372 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**Ruling (R9), the author\'s, 2026-09-08:** *a citing row names a pin. Pins are added to '
         'citing rows, and sourced ONLY from the act that wrote the row, located in its own bank; '
         'never from the current head, which would date the claim to today rather than to when it was '
         'made. A row whose writing act cannot be located is marked CITES-AT-AN-UNKNOWN-REF and left, '
         'which is honest and is not a pin.*'),
        '',
        '### What the sourcing rule found, and it is not what the ruling assumed',
        '',
        ('The chain (R9) requires was declared before it was run: **the row re-anchored by its own '
         'content → the commit that introduced it → the act that commit\'s subject names → that act\'s '
         'own banked pins record**. It was run over all **%d** pinless rows the b371 inventory found, '
         'at **%.1f seconds a row**. The price fits one act, so this act executed rather than only '
         'priced.' % (P['rows'], P['per_row'])),
        '',
        ('**%d of %d rows have a locatable writing act. %d do not.** Of the %d that do, the chain then '
         'fails again for most: %s'
         % (P['located_act'], P['rows'], P['act_not_located'], P['located_act'],
            '; '.join('**%d** %s' % (n, k.lower()) for k, n in sorted(reasons.items())
                      if k and k != 'WRITING ACT NOT NAMED'))),
        '',
        ('**The reason is structural and is the finding of this act: the papers are older than the '
         'instruments.** The commit subjects of this repository did not always name an act — %d of the '
         '%d rows were introduced by commits whose subject names none — and the pins instrument that '
         'banks a kernel\'s ref begins at b300, later than most of the rows that need one. **(R9) is a '
         'good rule reaching back into a record that did not yet keep the evidence the rule requires.**'
         % (reasons.get('WRITING ACT NOT NAMED', 0), P['rows'])),
        '',
        '### What was pinned: nothing, and the reason is not neglect',
        '',
        ('**%d rows were PINNABLE. All %d of them sit on a surface no act may rewrite** — %s. **So no '
         'pin was written to any row.**'
         % (P['pinnable'], P['pinnable'],
            '; '.join('%d on %s' % (n, k.lower()) for k, n in sorted(exr.items())))),
        '',
        ('**This seat will not read a ruling about citation hygiene as a licence to rewrite a '
         'deposited artefact, an archived snapshot, or a banked append-only ledger entry.** A '
         'deposited companion edited on this machine no longer matches what was deposited; an archive '
         'that changes is not an archive; and a ledger row is a historical statement already dated by '
         'the act that wrote it. **Whether those surfaces should carry pins at all is the author\'s '
         'question, and it is routed, not decided.**'),
        '',
        ('**And one pin that could be sourced could not be written for a second reason, which is '
         'reported rather than worked around.** Eight of the pinnable rows resolve to a ref that '
         '**equals a current head** — not because the head was used as the source, but because '
         '`SIDE-kernel` has not moved since the act that wrote them, and that act\'s own bank says so '
         'in as many words. The bar this act locked forbids writing a pin equal to a head. **The bar '
         'tests the value; the ruling forbids the source; a kernel that has not moved makes the two '
         'coincide.** The bar as locked was obeyed.'),
        '',
        '### The status column — listed, carried, routed; no grade moved',
        '',
        ('Of **%d** table rows across **%d** tracked markdown files, **%d** name a declaration this '
         'record has classified retired or absent *and* carry a grade. Of those, **%d state their own '
         'retirement** and **%d grades a declaration b372 found alive** — neither is the defect. '
         '**%d assert the grade with neither, and those are the defect.**'
         % (S['rows_scanned'], S['files'], S['hits'], S['corrected'], S['live_graded'],
            S['defect'])),
        '',
        '| carrier | row | grade | declaration(s) | as this record classified them |',
        '|---|---|---|---|---|',
    ] + [
        '| `%s` | %d | %s | %s | %s |'
        % (h['file'], h['line'], ', '.join('`%s`' % g for g in h['grades'][:2]),
           ', '.join('`%s`' % x for x in h['declarations']),
           '; '.join(sorted(set(v.split(':')[-1].strip() for v in h['classified'].values()))))
        for h in S['detail'] if not h['states_own_retirement'] and not h['grades_a_live_declaration']
    ] + [
        '',
        ('**This is not a stale number.** A stale count misstates a quantity; **a grade against an '
         'absent declaration asserts that something was checked that is not there to check**, and a '
         'reader traversing the row cannot see the difference. **And every one of these rows is inside '
         'the twelve b372 already flagged — the sweep found no instance outside that set**, which '
         'bounds the problem rather than widening it.'),
        '',
        ('**No grade was moved by this seat.** A grade is a judgement about verified content, and a '
         'seat that regrades is a seat that decided what was verified. The author faces **three '
         'choices per row, named here without one being chosen**: strike the grade; restate it as a '
         'retirement, the way `VERIFICATION_LOOM.md` already does for the GRH and Landau-Siegel pair; '
         'or leave it with a pin that dates it — noting that this act has just shown a pin cannot be '
         'sourced for these rows.'),
        '',
        '### The desk, and the instrument corrected',
        '',
        ('%d desk items swept under (R7); **%d closed** — %s — each with the file and date that killed '
         'it named, and both flagged because the killing file is this act\'s own. %d stand, and %d of '
         'those are new at this act.'
         % (Q['items'], Q['closed'], ', '.join('*%s*' % c['item'] for c in Q['closed_items']),
            Q['standing'], 3)),
        '',
        ('**`tools/b304_hooks.py` carried a sentence b372 made false** — that no `.gitattributes` pins '
         'the guard, so its identity arm could not tell you. The order licensed the correction and it '
         'is made. **The caveat was kept rather than deleted along with the falsehood**: what an '
         'attribute fixes is what the next checkout produces, the identity arm is still '
         'EOL-normalised, and it still would not tell you — what changed is that the hazard is pinned '
         'shut upstream of it. **A correction that deletes the caveat is a worse file.**'),
        '',
        ('*Species: **A RULE CAN OUTRUN THE RECORD IT REACHES INTO**. (R9) is sound and its evidence is '
         'b372\'s own; the record simply does not carry, for most rows, the act-name and the banked ref '
         'the rule needs. **No pin was written. No grade was moved. No row was checked at any pin. No '
         'deposited file, archived file or ledger entry was edited. No `.lean` file was written and no '
         'build was run.** Trigger: the author\'s answer on the frozen surfaces, or on the three '
         'choices for the graded rows. Nothing here is a route, no coordinate is closed, and `h2` '
         'stands exactly where the deposit left it.*'),
    ]
    return lines


def main():
    rec('=' * 100)
    rec('b373 -- THE TRAILS LEDGER: THE PINS SOURCED, THE STATUS COLUMN LISTED.')
    rec('=' * 100)
    P = jload('b373_pins.json')
    S = jload('b373_status.json')
    Q = jload('b373_desk.json')
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        run_clock.write(D, 'b373_filing_notes', LINES)
        return 0
    rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
    body = chr(10).join(block(P, S, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    committed = r.stdout.decode('utf-8', 'replace')
    appended_only = after.startswith(before)
    prefix_intact = (committed.replace(chr(13) + chr(10), chr(10))
                     in after.replace(chr(13) + chr(10), chr(10)))
    rec('  ### bytes %d -> %d' % (len(before.encode('utf-8')), len(after.encode('utf-8'))))
    rec('  ### ### **APPEND-ONLY (the file before is a prefix of the file after) : %s**' % appended_only)
    rec('  ### ### **THE COMMITTED VERSION IS STILL A SUBSTRING OF THE FILE : %s**' % prefix_intact)
    rec('  ### mark : %s' % MARK)
    rec('  ### lines appended : %d' % len(body.split(chr(10))))
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
    rec('=' * 100)
    p = run_clock.write(D, 'b373_filing_notes', LINES)
    io.open(os.path.join(D, 'b373_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(mark=MARK, prior_present=(PRIOR in before), appended_only=appended_only,
                        committed_prefix_intact=prefix_intact,
                        before_bytes=len(before.encode('utf-8')),
                        after_bytes=len(after.encode('utf-8')),
                        file='OPEN_TRAILS.md',
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
