# -*- coding: utf-8 -*-
"""b371_filing.py -- THE TRAILS LEDGER, UPDATED FOR EACH ITEM THAT CLOSED.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### `b157`'s entry and the `b367`, `b368` and
### `b369` blocks all stand exactly as written; this one NAMES them and edits none.
### ### ### **AND IT CLOSES `SCAFFOLD-TERMINALS`, WHICH HAS BEEN OPEN SINCE `b157`.** ### Under `(R7)`,
### with the file and date that killed it named -- ### **NOT ON THE ORDER'S SAY-SO.**
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b371 the desk closes: scaffold-terminals, the anchored arms, the hook -->'
PRIOR = ['<!-- b367 scaffold terminals not located -->',
         '<!-- b368 front document reconciled by an appended currency block -->',
         '<!-- b371 the list repaired in place, the original preserved -->'.replace('371', '369')]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def block(Q, S, H, INV):
    closed = Q['closed_items']
    return [
        '', MARK, '',
        ('### **`SCAFFOLD-TERMINALS` — CLOSED 2026-09-08 (b371), UNDER RULING (R7), WITH THE FILE AND '
         'DATE THAT KILLED IT NAMED**'),
        '',
        ('*No block above is edited. b157\'s entry and the b367, b368 and b369 blocks stand exactly as '
         'they were written, and this one names them.*'),
        '',
        ('**Ruling (R7), the author\'s, 2026-09-08:** *an item whose occasion is gone closes, with the '
         'file and date that killed it named. A desk that only accumulates is a list.* **This reverses '
         'the disposition b368, b369 and b370 were each given** — all three were ordered to produce '
         '*marks, not verdicts*, and all three said so on their faces. **None of them is re-verdicted: '
         'each obeyed the rule it was given, and the author changed the rule.**'),
        '',
        '### What closed, and what killed it',
        '',
        '| item | killing file | dated |', '|---|---|---|',
    ] + [
        '| %s | `%s` | %s |' % (c['item'], c['file'], c['date']) for c in closed
    ] + [
        '',
        ('**`SCAFFOLD-TERMINALS` is the one this entry is filed against.** Its occasion was the *repair* '
         'of two scaffold terminals. b367 found them **retired and gone at the kernel, with the kernel\'s '
         'own retirement ledger recording it**; b368 re-derived the same finding independently; b369 '
         're-derived it a third time and corrected b368\'s split of the ledger while confirming its '
         'count. **There is nothing to repair, and the kernel says so.** The item is closed — not '
         'because the ferry said so, but because the file that killed it exists, is named above, and '
         'carries the sentence claimed for it.'),
        '',
        ('**The other two closures are desk items rather than trail entries**, and are recorded here so '
         'the closures live in one place: the *anchored gate arms as available mechanical work, '
         'unscheduled and not built* — built at b363 and swept across the whole record at b366; and the '
         '*hook\'s non-durability*, named as owed by b370 and killed by this act.'),
        '',
        ('**And that last closure is flagged, because its killing file is this act\'s own.** That is '
         'allowed — this act did the killing — and it is **not** a confirmation drawn from the record. '
         'b368 made that mistake with a sweep that read its own paperwork; it is not repeated here by '
         'accident.'),
        '',
        '### What this act did to the guard, and exactly how far it goes',
        '',
        ('The pre-push guard now lives at **`%s/pre-push` in each of the %d rostered repositories, '
         'tracked by git**, byte-identical to the one source, with `core.hooksPath` set to read it. It '
         'was exercised in **both polarities in every repository, with %d failing**.'
         % (H['tracked_dir'], len(H['repos']), len(H['failing']))),
        '',
        ('**A clone is still not guarded, and this entry says so rather than letting `made durable` be '
         'read as `done`.** `core.hooksPath` lives in `.git/config`, which is not tracked. What changed '
         'is *which half is missing*: before, a clone had neither the guard nor the wiring and the guard '
         'existed only on one machine; now the clone carries **the guard** and lacks **one command** — '
         '`%s`. That is a smaller hole and it is not no hole.' % H['residual_step']),
        '',
        ('**The old location is left in place and inert.** With the path set, `.git/hooks/pre-push` does '
         'not run; if the config is ever unset it becomes live again. **A safety net and a trap** — two '
         'copies that can drift — and the byte-identity arm against the one tracked source is what '
         'catches the drift.'),
        '',
        '### The one confirmed live claim, settled',
        '',
        ('The construction kernel\'s public description named a `Core` figure of **%d**. That figure was '
         '**exact at tag `%s`**, where the printed profile carried **%d** — and the repository is **%s '
         'commits past that tag**, its profile now carrying **%d**. **The two count the same thing at '
         'different refs, not different things**, so the verdict is **STALE** and not scope-dependent. '
         'The description is repaired; the original is preserved in this act\'s bank, because **a '
         'description has no history and nothing else will remember it.**'
         % (S['figure'], S['tag'], S['prints_at_tag'], S['head_ahead_of_tag'], S['prints_at_head'])),
        '',
        ('**And the repair removes the count rather than updating it.** Replacing one number with '
         'another buys one act\'s correctness and re-arms the same trap; the description now states the '
         'property the repository asserts everywhere else and names the artifact that carries the '
         'number. **That is this seat\'s judgement, flagged as one**, and the dated-number alternative '
         'is banked beside it.'),
        '',
        ('**The durability is stated with the finding:** a repository description is **account metadata, '
         'not a tracked file**. The correction survives a clone and survives nothing else, and **no '
         'tracked artifact would fail if it drifted again.**'),
        '',
        '### What is still owed, and it grew',
        '',
        ('**The kernel\'s own `README.md` — a tracked file, unlike the description — disagrees with '
         'itself and with the profile it ships.** Its headline says **%s** terminals; its own '
         'parenthetical breakdown sums to **%s**; its assembly ratio says **%s/%s**; and the profile in '
         'the same repository carries **%d**. **This is outside the target this act was given** and is '
         'recorded and routed, not repaired — and it is the sharper half, because the README travels '
         'with a clone and the description does not.'
         % (S['readme_headline'], S['readme_breakdown_sum'], S['readme_ratio'][0],
            S['readme_ratio'][1], S['prints_at_head'])),
        '',
        ('**And the row inventory found the surface (R6) sent it to.** Of %d table rows across %d '
         'tracked markdown files in this repository, **%d name a kernel and a terminal**; **%d of those '
         'name a pin and %d name none**. A row without a pin **cannot be checked the way (R6) '
         'specifies**, which checks a row *at the kernel and pin the row itself names*. **%d rows name a '
         'declaration this record has already classified absent** — a cross-reference against a banked '
         'finding, **not a check**, and a row so flagged is not thereby wrong.'
         % (INV['table_rows_scanned'], INV['files'], INV['rows'], INV['with_pin'],
            INV['without_pin'], INV['flagged_count'])),
        '',
        ('*Species: **CLOSURE UNDER A NEW RULE**. SCAFFOLD-TERMINALS is CLOSED after b157, b367, b368 '
         'and b369; two desk items close with it. **No row was checked and no kernel was opened for any '
         'row. No repository was audited beyond the single settled claim. No `.lean` file was written, '
         'no build was run, no axiom profile recomputed. No act is re-verdicted.** Trigger: the first '
         'batch of row checks under (R6), or any act that would repair the README\'s figures. Nothing '
         'here is a route, no coordinate is closed, and `h2` stands exactly where the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b371 -- THE TRAILS LEDGER: THE CLOSURES, FILED.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures : %s' % AF.self_test(False))
    Q = json.load(io.open(os.path.join(D, 'b371_desk.json'), encoding='utf-8'))
    S = json.load(io.open(os.path.join(D, 'b371_settle.json'), encoding='utf-8'))
    H = json.load(io.open(os.path.join(D, 'b371_hookpath.json'), encoding='utf-8'))
    INV = json.load(io.open(os.path.join(D, 'b371_inventory.json'), encoding='utf-8'))
    rec('  ### the closures, read from the sweep and not typed : %d' % Q['closed'])
    for c in Q['closed_items']:
        rec('      %-58s <- `%s` (%s)' % (c['item'][:58], c['file'], c['date']))
    if Q['closed'] == 0:
        rec('  ### ### **NOTHING CLOSED. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b371_filing_notes', LINES)
        return 0

    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    rec('')
    rec('  ### the blocks this one names and does not edit:')
    for m in PRIOR:
        rec('    %-70s present : %s' % (m[:70], m in before))
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED.**')
        run_clock.write(D, 'b371_filing_notes', LINES)
        return 0
    body = chr(10).join(block(Q, S, H, INV)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    grew = len(after) - len(before)
    ph = re.findall(r'%[sd]', body)
    rec('')
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### ### **UNFORMATTED PLACEHOLDERS LEFT IN THE BLOCK : %d** %s' % (len(ph), ph[:3]))
    rec('  ### ### **AND `SCAFFOLD-TERMINALS` IS CLOSED, AFTER `b157`, `b367`, `b368` AND `b369`.**')
    rec('=' * 100)
    ok = prefix_file and prefix_blob and not ph
    p = run_clock.write(D, 'b371_filing_notes', LINES)
    io.open(os.path.join(D, 'b371_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='SCAFFOLD-TERMINALS', status='CLOSED', mark=MARK, file='OPEN_TRAILS.md',
             closed=Q['closed'], closed_items=Q['closed_items'],
             names_prior=[m in before for m in PRIOR],
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             placeholders=len(ph),
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
