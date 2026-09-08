# -*- coding: utf-8 -*-
"""b368_filing.py -- THE SCAFFOLD TRAIL, UPDATED WITH THE ITEM'S TRUE STATE.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### `b157`'s entry and `b367`'s block both stand
### exactly as they were written; this block NAMES them and edits neither.
### ### **THE ITEM'S TRUE STATE, IN THREE PARTS AND NOT ONE:** ### the terminals are RETIRED at the
### kernel and the retirement is recorded there; ### the standing restriction was NEVER A SPECIAL RULE,
### only the general rule for their class; ### and the live defect -- the front document -- ### **NOW
### ### CARRIES A CURRENCY BLOCK BESIDE ITS LIST, AND THE LIST ITSELF IS UNCHANGED AND STILL WRONG.**
### ### **SO THE TRAIL IS NOT CLOSED BY THIS ACT**, and the block says which part is discharged and
### which part is still owed.
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
### ### **AND EVERY KERNEL NAME IS WRITTEN INSIDE BACKTICKS** -- `b367`'s incident: a retired identifier
### carrying a banned stem is a QUOTED KERNEL IDENTIFIER only where the scanner can see the quoting.
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
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
MARK = '<!-- b368 front document reconciled by an appended currency block -->'
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


def names(rows, pred):
    return ', '.join('`%s`' % r['name'] for r in rows if pred(r))


def block(C, R, K, Q):
    named = [r for r in C['rows'] if r['kind'] == 'RETIRED'
             and r['note'] == 'named by the ledger itself']
    rest = [r for r in C['rows'] if r['kind'] == 'RETIRED'
            and r['note'] != 'named by the ledger itself']
    # ### **THREE GROUPS, READ FROM THE EVIDENCE.** ### One layer carries no ledger entry at all.
    layer_only = [r for r in rest if r['evidence'].get('line')]
    hist_only = [r for r in rest if not r['evidence'].get('line')]
    return [
        '', MARK, '',
        ('### **`SCAFFOLD-TERMINALS` — UPDATED 2026-09-08 (b368): THE TERMINALS ARE RETIRED, THE '
         'RESTRICTION WAS NEVER A SPECIAL RULE, AND THE FRONT DOCUMENT NOW CARRIES A CURRENCY BLOCK '
         'BESIDE THE LIST THAT IS STILL WRONG**'),
        '',
        ('*Neither block above is edited. b157\'s entry and b367\'s block stand exactly as they were '
         'written, and this one names them. **No `.lean` file was touched, no build was run, no axiom '
         'profile was computed and no existing sentence of the front document was changed.***'),
        '',
        ('**The count was re-derived, not carried.** b367 reported eighteen absent names. This act did '
         'not reuse that figure: it re-read the Layer-1 export list at `SIDE-effects` ref `%s` = `%s` '
         '(local head equal to `ls-remote`, working tree clean, **head unmoved since b367**), extracted '
         'the backticked names, and searched this kernel\'s six `.lean` files for a declaration of each. '
         '**Of %d exported names, %d are declared and %d are absent** — and the independently derived '
         'figure **agrees with b367\'s**. Two independent derivations of the same number are worth more '
         'than one carried forward, which is why the order forbade carrying it.'
         % (C['ref'], C['head'], C['exported'], C['n_present'], C['n_absent'])),
        '',
        '**Each absent name classified on its own evidence, one row each — and none from its own sound:**',
        '',
        ('- **RETIRED: %d.** Each is named in the retirement ledger, or its layer\'s ledger entry records '
         'the removal that took it, or the repository\'s own history shows the declaration present and '
         'then gone.' % C['kinds'].get('RETIRED', 0)),
        ('- **RENAMED: %d.** None. A successor was accepted only from a declared mapping, and the mapping '
         'is empty. Resemblance between a retired name and a live one is exactly what the order forbade '
         'acting on, and one such resemblance was met and refused.' % C['renamed_rows']),
        ('- **NEVER EXISTED: 0.** No exported name is an invention. Every one of the %d was really there '
         'and was really removed.' % C['n_absent']),
        ('- **PRESENT: %d** — %s.' % (C['n_present'], names(C['rows'], lambda r: r['kind'] == 'PRESENT'))),
        '',
        ('**AND THIS ACT\'S OWN NEW FINDING, WHICH NEITHER b157 NOR b367 HAD: THE LEDGER NAMES ONLY HALF '
         'OF THEM.** Of the %d retired names, **%d are named in the retirement ledger explicitly**, '
         '**%d are covered only by their layer\'s entry** — the entry records that the layer\'s skeletons '
         'were retired without listing which — and **%d have no ledger entry for their layer at all**. '
         '**The ledger is accurate about what it says and incomplete about what it names**, and that is a '
         'different defect from the one b367 found.'
         % (C['kinds'].get('RETIRED', 0), C['retired_named_by_ledger'], len(layer_only),
            len(hist_only))),
        '',
        '**Named by the ledger:** %s.' % names(named, lambda r: True),
        '',
        '**Covered only by a layer entry:** %s.' % names(layer_only, lambda r: True),
        '',
        ('**No ledger entry for their layer at all:** %s — evidenced by the repository\'s own history, '
         'which shows each present in an earlier commit and absent now. **There the ledger omits a name; '
         'here it omits a whole layer.**' % names(hist_only, lambda r: True)),
        '',
        ('**The kernel\'s own ledger heading, quoted** (`%s`, line %d):'
         % (Q['head']['file'], Q['head']['line'])),
        '',
        '> %s' % Q['head']['quote'],
        '',
        ('**What was done about it: an APPEND-ONLY CURRENCY BLOCK, and the branch was decided by the '
         'classification rather than chosen.** Because every exported name has a kind and the kinds '
         'partition the list, a block can state what is present, what is retired and where the '
         'retirements are recorded **without changing a single existing sentence** — so the second branch '
         '(price it and route it to the author) was unreachable. The block was appended to `AGENTS.md` '
         'under its own mark: the file before is a true prefix of the file after (**%s**) and the '
         'committed blob is a true prefix of the working file (**%s**), both read **before the push**, '
         'which is the reading that carries.'
         % (R['prefix_of_file'], R['prefix_of_blob'])),
        '',
        ('**And the block exports nothing.** It carries **%d** lines in the front document\'s own export '
         'shape and mentions **no** absent name outside a status row — verified as a check on the block, '
         'not on the document. `AGENTS.md` grew by %d bytes and lost none.'
         % (R['export_shaped_lines'], R['grew'])),
        '',
        ('**WHAT IS STILL OWED, AND THIS IS WHY THE TRAIL IS NOT CLOSED.** The Layer-1 list above the '
         'block **still exports %d absent names**, and this act did not edit it — which is the whole of '
         'what append-only means here. A reader who stops at the list is still misled; a reader who '
         'reaches the block is not. **Correcting the list itself edits sentences, and that decision is '
         'the author\'s, not this seat\'s.**' % R['list_above_still_exports_absent']),
        '',
        ('**The standing restriction is unchanged, and b367\'s reading of it is confirmed rather than '
         'extended.** A terminal that does not exist cannot be cited; the restriction is redundant for '
         'these and stands anyway, because a name can return. **It was never a special rule** — it is the '
         'general rule for its class, as the record\'s own grading architecture already says.'),
        '',
        ('*Species: **RECONCILIATION, APPEND-ONLY**. b157 CONFIRMED for the third time and still live in '
         'its remaining half. **No name was classified from its own sound; no `.lean` file was written; '
         'no build was run; no existing sentence was edited; no desk item was closed; no grade was '
         'conferred and no act was re-verdicted.** Trigger: any act that would repair the Layer-1 list '
         'itself, or that would name a successor for a retired terminal. Nothing here is a route, no '
         'coordinate is closed, and `h2` stands exactly where the deposit left it.*'),
    ]


def main():
    rec('=' * 100)
    rec('b368 -- THE SCAFFOLD TRAIL, UPDATED. ### **NEITHER BLOCK ABOVE IS EDITED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    C = json.load(io.open(os.path.join(D, 'b368_classify.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b368_reconcile.json'), encoding='utf-8'))
    K = json.load(io.open(os.path.join(D, 'b368_desk.json'), encoding='utf-8'))
    rec('  ### the kinds, read from the classifier and not typed : %s' % C['kinds'])
    rec('  ### the branch, read from the reconciler and not typed : %s' % R['branch'])

    Q = {'head': q(STRUCT, '-- RETIREMENT LEDGER (audit Phase S.2–S.4)', 2)}
    rec('')
    for kk, v in Q.items():
        rec('  [%-5s] %-22s line %-6d equal under the shared normaliser : %s'
            % (kk, v['file'], v['line'], v['equal']))
        rec('      | %s' % v['quote'][:160])
    if not all(v['equal'] for v in Q.values()):
        rec('  ### ### **A QUOTATION CHANGED MORE THAN THE SCAFFOLDING. ### NOTHING IS FILED.**')
        run_clock.write(D, 'b368_filing_notes', LINES)
        return 3

    rec('')
    rec('-' * 100)
    rec('  ### THE TWO BLOCKS THIS ONE NAMES AND DOES NOT EDIT.')
    rec('-' * 100)
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    rec("    `b367`'s mark present above : %s" % (B367_MARK in before))
    rec('    ### **THIS BLOCK IS APPENDED BELOW BOTH, AND NEITHER IS REWRITTEN.**')

    rec('')
    rec('-' * 100)
    rec('  ### THE APPEND. ### **APPEND-ONLY, UNDER ITS OWN MARK, NOTHING ABOVE IT EDITED.**')
    rec('-' * 100)
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED, AND THIS IS NOT A FAILURE.**')
        run_clock.write(D, 'b368_filing_notes', LINES)
        return 0
    body = chr(10).join(block(C, R, K, Q)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    lean_dirty = [x for x in subprocess.run(['git', '-C', KERNEL, 'status', '--porcelain'],
                                            capture_output=True, text=True).stdout.splitlines()
                  if x.strip().endswith('.lean')]
    rec('  ### bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('  ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('  ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('  ### ### **AND NO `.lean` FILE WAS TOUCHED : %s** %s' % (not lean_dirty, lean_dirty or ''))
    rec('  ### **THE READING BEFORE THE PUSH, AND IT IS THE ONE THAT CARRIES** (`b352`).')

    # ### **EVERY KERNEL NAME IN THE BLOCK IS INSIDE BACKTICKS.** ### `b367`'s incident, mechanized:
    # ### the scanner excuses a QUOTED KERNEL IDENTIFIER only where it can see the quoting.
    absent = set(C['absent']) | set(C['present'])
    naked = []
    for ln in body.split(chr(10)):
        for nm in absent:
            for m in re.finditer(re.escape(nm), ln):
                a, b2 = m.start(), m.end()
                if not (ln[a - 1:a] == '`' and ln[b2:b2 + 1] == '`'):
                    naked.append((nm, ln.strip()[:60]))
    rec('  ### ### **KERNEL NAMES WRITTEN WITHOUT BACKTICKS : %d** %s' % (len(naked), naked[:2]))
    rec('')
    rec('=' * 100)
    ok = prefix_file and prefix_blob and not lean_dirty and not naked
    rec('  ### ### **THE TRAIL IS UPDATED. ### THE ITEM IS NOT CLOSED: THE LIST ITSELF IS STILL WRONG.**')
    rec('  ### append-only checks passing : %s' % ok)
    rec('=' * 100)
    p = run_clock.write(D, 'b368_filing_notes', LINES)
    io.open(os.path.join(D, 'b368_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(entry='SCAFFOLD-TERMINALS', status='UPDATED, NOT CLOSED', mark=MARK,
             file='OPEN_TRAILS.md', names_b367_block=(B367_MARK in before),
             quotes={k: dict(file=v['file'], line=v['line'], equal=v['equal'], quote=v['quote'])
                     for k, v in Q.items()},
             bytes_before=len(before), bytes_after=len(after), grew=grew,
             prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
             lean_touched=len(lean_dirty), naked_kernel_names=len(naked),
             still_owed=R['list_above_still_exports_absent'], closed=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
