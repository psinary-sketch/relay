# -*- coding: utf-8 -*-
"""b369_filing.py -- THE SCAFFOLD TRAIL, UPDATED WITH THE FRONT DOCUMENT'S STATE AFTER `(R4)`.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### `b157`'s entry, `b367`'s block and `b368`'s
### block all stand exactly as they were written; this one NAMES them and edits none.
### ### **AND IT REPORTS TWO THINGS THE TRAIL DID NOT HAVE:** ### that the list is now REPAIRED and the
### original PRESERVED in the same file; and that ### **`b368`'s SHARPER CLAIM WAS WRONG** -- the ledger
### does not omit a layer, and the predicate that said so knew only one shape.
### ### **THE PASS IS NAMED AS PRICED, NOT AS DONE.**
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
### ### **AND EVERY KERNEL NAME IS INSIDE BACKTICKS** (`b367`'s incident).
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
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
MARK = '<!-- b369 the list repaired in place, the original preserved -->'
B368_MARK = '<!-- b368 front document reconciled by an appended currency block -->'
B367_MARK = '<!-- b367 scaffold terminals not located -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def strip_markers(s):
    return ' '.join(re.sub(r'#{2,}', ' ', s).split()).strip()


def q(path, hint, span=1):
    n, _l = AF.find(path, hint)
    txt = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    raw = chr(10).join(txt[n - 1:n - 1 + span])
    s = strip_markers(raw)
    return dict(file=os.path.basename(path), line=n, span=span, quote=s,
                equal=(GN.norm(s) == GN.norm(raw)))


def nm(names):
    return ', '.join('`%s`' % n for n in names)


def block(R, P, K, Q):
    return [
        '', MARK, '',
        ('### **`SCAFFOLD-TERMINALS` — UPDATED 2026-09-08 (b369): THE LIST IS REPAIRED IN PLACE, THE '
         'ORIGINAL IS PRESERVED IN THE SAME FILE, AND b368\'s SHARPER CLAIM ABOUT THE LEDGER IS '
         'WITHDRAWN AS WRONG**'),
        '',
        ('*No block above is edited. b157\'s entry and b367\'s and b368\'s blocks stand exactly as they '
         'were written, and this one names them. **No `.lean` file was touched, no build was run and no '
         'axiom profile was computed.***'),
        '',
        ('**Ruling (R4), the author\'s, 2026-09-08:** *append-only is right for a ledger, where a reader '
         'reads the file; it is wrong for a list, where a reader reads the list. Preserve by quotation, '
         'repair by edit.* **This reverses b368\'s disposition of the same object, not its '
         'measurement** — and b368\'s measurement is confirmed for the third time below.'),
        '',
        ('**What was done.** At `SIDE-effects` ref `%s` = `%s` (local head equal to `ls-remote`, tree '
         'clean), the %d export rows were located, quoted **verbatim** into the currency note, the '
         'quotation was verified byte-for-byte against the located rows, and **only then** were the rows '
         'replaced. The repaired list carries **%d** of the names the classification calls absent, by a '
         'content predicate over the rows themselves — not by a count of edited lines.'
         % (R['ref'], R['head'], R['rows_replaced'], 0 if R['bar2_exports_none'] else -1)),
        '',
        ('**The classification was re-derived for the third time and agrees for the third time:** of %d '
         'names, **%d declared and %d absent**. b368\'s figure was held as a comparison only and was '
         'never an input to the count.'
         % (R['exported'], R['n_present'], R['n_absent'])),
        '',
        ('**The edit is bounded, and the bound is measured.** Every byte of the front document above the '
         'rows is its committed blob\'s (**%s**), and every byte below them up to the appended note is '
         'too (**%s**) — both read **before the push**. The original rows survive verbatim in the file '
         '(**%s**). *An edit is not an append, and this entry does not claim a prefix arm it cannot '
         'have.*' % (R['bar3_above'], R['bar3_below'], R['bar1_preserved'])),
        '',
        ('### b368\'s sharper claim is withdrawn — and the reason is a predicate, not a slip'),
        '',
        ('b368 reported the retirement ledger as naming 9 of the 18, covering 8 by a layer entry, and '
         '**leaving 1 with no entry for its layer at all** — and called that last the sharper half of '
         'its finding. **It is not true.** The ledger carries an entry *headed by that declaration\'s '
         'own name*. b368\'s predicate required a backtick or a slash before a name; the ledger names '
         'that one as a bare heading. **A predicate that knows one shape finds one shape.**'),
        '',
        'Re-derived here from the ledger\'s own entry headings, the split is:',
        '',
        '- **Named outright (%d):** %s.' % (len(R['ledger_named']), nm(R['ledger_named'])),
        ('- **Named only by the ledger\'s slash abbreviation (%d):** %s. **Reading an abbreviation as '
         'naming its expansions is a judgement, not a string match**, so these are kept apart rather '
         'than folded in.' % (len(R['ledger_by_abbreviation']), nm(R['ledger_by_abbreviation']))),
        '- **Covered only by their layer\'s entry (%d):** %s.'
        % (len(R['ledger_layer_only']), nm(R['ledger_layer_only'])),
        ('- **Not covered at all: %d.** **Every retired name is reached by the ledger** — by its own '
         'name, by its abbreviation, or through its layer\'s entry.'
         % len(R['ledger_silent'])),
        '',
        ('**Ruling (R5) governs what is said about them, and it binds this entry:** where the kernel\'s '
         'own record does not say *why* a name went, **this act says that it does not say**. No '
         'retirement reason is supplied anywhere in the repaired document or in this entry.'),
        '',
        ('**And the cost of (R4) is reported rather than left to be tripped over.** b368\'s block says '
         'nothing above it had been changed and that the list was left exactly as it was. **Both were '
         'true when written and neither is true now.** They are **not edited** — a past record is named '
         'and superseded, never rewritten — and the note appended to `AGENTS.md` says so in the same '
         'file a reader meets them in.'),
        '',
        '### The two hygiene items, closed',
        '',
        ('The exclusion kernel is now **in the pins roster** and carries the **pre-push hook**, '
         'byte-identical to the one tracked source, exercised in both polarities across all %d rostered '
         'repositories with **%d failing**. b368 had to pin it by hand; the record can now re-take that '
         'pin itself. **The roster mend is tracked and survives a clone; the hook install is not, '
         'because `.git/hooks/` is untracked.** The two repairs are not equal in durability.'
         % (len(K['rosters']['b303_pins.py']), K['repos_failing'])),
        '',
        '### The refinement pass — **priced, and not run**',
        '',
        ('The account was enumerated live: **%d repositories, %d of them programme material**. Their '
         'public surfaces are listed — %d descriptions, %d `README`s, %d front documents, and %d `.lean` '
         'files that could carry docstrings. **No surface was read for correctness, no claim was checked '
         'against any kernel, and no repository was graded.**'
         % (P['repos_on_account'], P['programme'], P['descriptions'], P['readmes'],
            P['front_documents'], P['lean_files'])),
        '',
        ('**The price splits, and the split is the part a price usually hides.** The mechanical half — '
         'does a surface exist, does it carry a count-shaped string, which identifiers does it name, do '
         'those identifiers have declarations — is **one act**, and b368\'s classifier already does all '
         'four. The read half — whether a count-shaped string is a *claim*, and whether the kernel still '
         'carries it — **does not scale and nothing in this pass makes it cheaper**; b367 and b368 spent '
         'two whole acts on one front document against one kernel.'),
        '',
        ('**Highest exposure by the order\'s own criterion** (age since last touch; counts rather than '
         'terminals; public): %s. **This is a ranking of exposure, not of error** — no repository on it '
         'has been shown to carry a stale claim, and this act did not look.'
         % nm(P['highest_risk'])),
        '',
        ('**And what the ranking cannot see is reported, because it is sharp:** `SIDE-effects` — the one '
         'repository this programme *knows* carried a stale claim — **is not on that list**, because its '
         'description carries no count shape and the claim lived in its front document. **A criterion is '
         'only as wide as the surface it reads.**'),
        '',
        ('**The hint, scored against what was found.** *(H1) the construction kernel\'s public '
         'description names a core terminal count* — **%s**: exactly one description on the account uses '
         'the word *construction*, and it carries the shape `%s`. *(H2) that count may predate its '
         'current profile* — **%s**: deciding it requires reading the profile, which is the audit the '
         'cap forbids. An age is not a staleness, and this act reports the age.'
         % (P['h1'].split(' --')[0], P['count_shape_of_construction'], P['h2'])),
        '',
        ('*Species: **REPAIR IN PLACE, UNDER A RULING**. The front document\'s Layer-1 list no longer '
         'exports a name its kernel does not carry; the original is preserved in the same file. **The '
         'trail is still not closed**: the paragraph above the list makes a count claim this act did not '
         'touch, because the order said the list is corrected and a count is not a name — and that '
         'paragraph is exactly the species the priced pass exists to sweep. No `.lean` file written, no '
         'build run, no retirement reason supplied, no successor named, no desk item closed, no grade '
         'conferred, no act re-verdicted. Trigger: the refinement pass, or any act that would repair a '
         'count claim. Nothing here is a route, no coordinate is closed, and `h2` stands exactly where '
         'the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b369 -- THE SCAFFOLD TRAIL, UPDATED. ### **NO BLOCK ABOVE IS EDITED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    R = json.load(io.open(os.path.join(D, 'b369_repair.json'), encoding='utf-8'))
    P = json.load(io.open(os.path.join(D, 'b369_pass.json'), encoding='utf-8'))
    K = json.load(io.open(os.path.join(D, 'b369_hygiene.json'), encoding='utf-8'))
    cs = next((x['count_shapes'][0] for x in P['rows']
               if x['name'] in P['construction_candidates'] and x['count_shapes']), '?')
    P['count_shape_of_construction'] = cs
    rec('  ### the split, read from the repair and not typed : %d / %d / %d / %d'
        % (R['n_named'], R['n_by_abbr'], R['n_layer_only'], R['n_silent']))
    rec('  ### the hint, read from the pass and not typed    : (H1) %s ; (H2) %s' % (P['h1'], P['h2']))

    Q = {'head': q(STRUCT, '-- RETIREMENT LEDGER (audit Phase S.2–S.4)', 2)}
    if not all(v['equal'] for v in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b369_filing_notes', LINES)
        return 3

    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    rec('')
    rec('  ### the three blocks this one names and does not edit:')
    for lbl, m in (('b367', B367_MARK), ('b368', B368_MARK)):
        rec('    %s mark present above : %s' % (lbl, m in before))
    rec("    b157's sentence present exactly once : %s"
        % (before.count("THE FERRY'S OWN SCAFFOLD PREMISE IS SUPERSEDED") == 1))

    rec('')
    rec('-' * 100)
    rec('  ### THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK.**')
    rec('-' * 100)
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED.**')
        run_clock.write(D, 'b369_filing_notes', LINES)
        return 0
    body = chr(10).join(block(R, P, K, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)

    allnames = set(R['absent']) | set(R['present'])
    naked = []
    for ln in body.split(chr(10)):
        for n2 in allnames:
            for m in re.finditer(re.escape(n2), ln):
                if not (ln[m.start() - 1:m.start()] == '`' and ln[m.end():m.end() + 1] == '`'):
                    naked.append((n2, ln.strip()[:60]))
    rec('  ### ### **KERNEL NAMES WRITTEN WITHOUT BACKTICKS : %d** %s' % (len(naked), naked[:2]))
    rec('=' * 100)
    ok = prefix_file and prefix_blob and not naked
    rec('  ### ### **THE TRAIL IS UPDATED. ### STILL NOT CLOSED: THE COUNT CLAIM ABOVE THE LIST STANDS.**')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b369_filing_notes', LINES)
    io.open(os.path.join(D, 'b369_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='SCAFFOLD-TERMINALS', status='REPAIRED IN PLACE, NOT CLOSED', mark=MARK,
             file='OPEN_TRAILS.md', names_b367=(B367_MARK in before), names_b368=(B368_MARK in before),
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             naked_kernel_names=len(naked), closed=False,
             b368_sharper_claim_withdrawn=True,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
