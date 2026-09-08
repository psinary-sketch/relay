# -*- coding: utf-8 -*-
"""b368_reconcile.py -- ADDITION THREE: THE APPEND-ONLY CURRENCY BLOCK.

### ### **THE BRANCH IS DECIDED BY THE CLASSIFICATION, NOT BY PREFERENCE.** ### Every absent name is
### `RETIRED` and every present name has a declaration, so a block naming what is present, what is retired
### and where the retirements are recorded says everything the reconciliation needs -- ### **AND NO
### ### EXISTING SENTENCE HAS TO CHANGE.**
### ### **THE APPEND-ONLY TEST IS MECHANICAL:** ### the file before is a true prefix of the file after AND
### of its committed blob, read ### **BEFORE THE PUSH.** ### An edit anywhere above the block fails it.
### ### **AND THE VERIFICATION THE ORDER ASKS FOR IS A CHECK ON THE BLOCK, NOT ON THE DOCUMENT**, and this
### tool says which: ### **THE BLOCK EXPORTS NOTHING.** ### Every name it mentions is mentioned under a
### status, and it carries no line in the front document's own export shape.
### ### **NO `.lean` FILE IS TOUCHED.**
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
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
AGENTS = os.path.join(KERNEL, 'AGENTS.md')
STRUCT = os.path.join(KERNEL, 'SIDEEffects', 'Structural.lean')
MARK = '<!-- b368 currency block: layer-1 export list vs source -->'
LAYER_SHAPE = re.compile(r'^- \*\*[^*]+\*\*:.*`')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def block(J):
    rows = J['rows']
    present = [r for r in rows if r['kind'] == 'PRESENT']
    named = [r for r in rows if r['kind'] == 'RETIRED' and r['note'] == 'named by the ledger itself']
    rest = [r for r in rows if r['kind'] == 'RETIRED' and r['note'] != 'named by the ledger itself']
    # ### **THE SPLIT IS THREE-WAY AND IS READ FROM THE EVIDENCE, NOT FROM THE NOTE.** ### One layer has
    # ### no ledger entry at all, and a block that filed its declaration under *covered by its layer's
    # ### entry* would be describing evidence the row does not carry.
    layer_only = [r for r in rest if r['evidence'].get('line')]
    hist_only = [r for r in rest if not r['evidence'].get('line')]
    out = [
        '', MARK, '',
        '## Currency of the Layer-1 export list — checked %s against `%s`'
        % ('2026-09-08', J['head'][:7]),
        '',
        ('*Appended, not edited. Nothing above this line has been changed. This block records the state '
         'of the "Theorems exported" list above as measured against the source at ref `%s` = `%s`, so a '
         'reader meets the measurement at the same time as the claim.*' % (J['ref'], J['head'])),
        '',
        ('**Of the %d names the Layer-1 list above exports, %d are declared in this kernel\'s own `.lean` '
         'files and %d are not.** The %d that are not were **retired** — each existed and was removed; '
         'none was invented, and none has a successor under another name in this kernel.'
         % (J['exported'], J['n_present'], J['n_absent'], J['n_absent'])),
        '',
        '### Present in the source',
        '',
    ]
    for r in present:
        out.append('- `%s` — declared at `%s:%d`. Axiom profile: **%s** (this kernel carries no printed '
                   'profile file; none was computed here).' % (r['name'], r['evidence']['file'],
                                                               r['evidence']['line'], r['profile']))
    out += [
        '',
        '### Retired, and named as retired by the retirement ledger',
        '',
        ('The ledger is the comment block headed `RETIREMENT LEDGER (audit Phase S.2–S.4)` in '
         '`SIDEEffects/Structural.lean`. These names appear in it explicitly:'),
        '',
    ]
    for r in named:
        out.append('- `%s`' % r['name'])
    out += [
        '',
        '### Retired, but **not named** by the ledger — covered only by their layer\'s entry',
        '',
        ('These were removed too — the kernel\'s own `.lean` history shows each was present and is not '
         'now — but the ledger\'s entry for their layer does not list them by name. **The ledger is '
         'accurate about what it says and incomplete about what it names.**'),
        '',
    ]
    for r in layer_only:
        out.append('- `%s` — the ledger\'s entry for the %s does not name it' % (r['name'], r['layer']))
    if hist_only:
        out += [
            '',
            '### Retired, with **no ledger entry for their layer at all**',
            '',
            ('For %s the ledger has no entry. Neither these declarations nor their layer is recorded in '
             'it, and the repository\'s own `.lean` history — which shows each present in an earlier '
             'commit and absent now — is the whole of the evidence that they existed. **This is a '
             'sharper silence than the group above: there the ledger omits a name, here it omits a '
             'whole layer.**'
             % ', '.join(sorted(set('the %s' % r['layer'] for r in hist_only)))),
            '',
        ]
        for r in hist_only:
            out.append('- `%s` — %s; evidenced by the repository\'s own history'
                       % (r['name'], r['evidence'].get('text', 'no ledger entry')))
    out += [
        '',
        '### What this block does and does not do',
        '',
        ('**It does not export anything.** Every name above appears under a status, not as an available '
         'theorem. **The list above this block is left exactly as it was**; this block is the currency '
         'note beside it, on the append-only pattern the programme\'s papers repository uses for its own '
         'ledgers.'),
        '',
        ('**It does not retire, restore, rename or repair anything.** No `.lean` file was touched, no '
         'build was run, and no axiom profile was computed. **It does not claim the retirements were '
         'right** — only that they happened, and where they are recorded.'),
        '',
        ('*Measured and appended by the PLACE TO STAND research seat, act b368 (2026-09-08), from this '
         'repository\'s own files at ref `%s` = `%s`. The measurement is reproducible: read the Layer-1 '
         'list, extract its backticked names, and search this kernel\'s six `.lean` files for a '
         'declaration of each.*' % (J['ref'], J['head'])),
    ]
    return out


def main():
    rec('=' * 100)
    rec('b368 -- ADDITION THREE: THE APPEND-ONLY CURRENCY BLOCK.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    J = json.load(io.open(os.path.join(D, 'b368_classify.json'), encoding='utf-8'))
    rec('  ### the classification, read from the classifier and not typed : %s' % J['kinds'])

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE BRANCH, DECIDED BY THE CLASSIFICATION.')
    rec('-' * 100)
    unclassifiable = [r['name'] for r in J['rows'] if r['kind'] not in
                      ('PRESENT', 'RETIRED', 'RENAMED', 'NEVER EXISTED')]
    can_append = (not unclassifiable) and J['n_present'] + J['n_absent'] == J['exported']
    rec('    every exported name has a kind : %s ; the kinds partition the list : %s'
        % (not unclassifiable, J['n_present'] + J['n_absent'] == J['exported']))
    rec('    ### ### **SO A BLOCK CAN SAY WHAT IS PRESENT, WHAT IS RETIRED AND WHERE THE RETIREMENTS')
    rec('    ### ### ARE RECORDED, WITHOUT EDITING A SENTENCE : %s**' % can_append)
    if not can_append:
        rec('    ### ### **BRANCH: (PRICED AND ROUTED). ### NOTHING IS WRITTEN.**')
        run_clock.write(D, 'b368_reconcile_run', LINES)
        return 0
    rec('    ### ### ### **BRANCH TAKEN: (APPEND-ONLY RECONCILIATION).**')
    rec('    ### **(PRICED AND ROUTED) -- UNREACHABLE**, because reconciliation needs no existing')
    rec('    ### sentence changed, and the append-only test below decides that mechanically.')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE APPEND.')
    rec('-' * 100)
    before = io.open(AGENTS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ### **THE MARK IS ALREADY PRESENT. ### NOTHING IS APPENDED.**')
        run_clock.write(D, 'b368_reconcile_run', LINES)
        return 0
    body = chr(10).join(block(J)) + chr(10)
    io.open(AGENTS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(AGENTS, encoding='utf-8', newline='').read()
    prefix_file = after.startswith(before)
    grew = len(after) - len(before)
    r = subprocess.run(['git', '-C', KERNEL, 'show', 'HEAD:AGENTS.md'], capture_output=True)
    blob = r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))
    prefix_blob = after.replace(chr(13) + chr(10), chr(10)).startswith(blob)
    rec('    bytes before : %d ### after : %d ### grew by : %d' % (len(before), len(after), grew))
    rec('    ### ### **THE FILE BEFORE IS A TRUE PREFIX OF THE FILE AFTER : %s**' % prefix_file)
    rec('    ### ### **THE COMMITTED BLOB IS A TRUE PREFIX OF THE WORKING FILE : %s**' % prefix_blob)
    rec('    ### **READ BEFORE THE PUSH** (`b352`), which is the reading that carries.')

    rec('')
    rec('-' * 100)
    rec("  ### (3) THE VERIFICATION. ### **A CHECK ON THE BLOCK, NOT ON THE DOCUMENT.**")
    rec('-' * 100)
    blk = after.split(MARK)[-1]
    exports_shape = [ln for ln in blk.split(chr(10)) if LAYER_SHAPE.match(ln)]
    mentioned = sorted(set(re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', blk)))
    absent_names = set(J['absent'])
    unstatused = []
    for ln in blk.split(chr(10)):
        for nm in re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', ln):
            if nm in absent_names and not ln.strip().startswith('- `'):
                unstatused.append((nm, ln.strip()[:70]))
    ok_block = (not exports_shape) and (not unstatused)
    rec('    lines in the block carrying the export shape `- **X**: `name`` : %d' % len(exports_shape))
    rec('    absent names mentioned outside a status row : %d %s' % (len(unstatused), unstatused[:2]))
    rec('    ### ### **THE BLOCK EXPORTS NO ABSENT TERMINAL : %s**' % ok_block)
    rec('    ### **AND THE CHECK IS ON THE BLOCK.** ### The list ABOVE it still exports %d absent names,'
        % J['n_absent'])
    rec('    ### and this act did not edit it -- which is the whole of what append-only means here.')

    kernel_lean_dirty = [x for x in subprocess.run(
        ['git', '-C', KERNEL, 'status', '--porcelain'], capture_output=True, text=True).stdout.splitlines()
        if x.strip().endswith('.lean')]
    rec('')
    rec('    ### ### **AND NO `.lean` FILE WAS TOUCHED : %s** %s'
        % (not kernel_lean_dirty, kernel_lean_dirty or ''))
    rec('=' * 100)

    p = run_clock.write(D, 'b368_reconcile_run', LINES)
    io.open(os.path.join(D, 'b368_reconcile.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(branch='APPEND-ONLY RECONCILIATION', mark=MARK, file='AGENTS.md',
                        bytes_before=len(before), bytes_after=len(after), grew=grew,
                        prefix_of_file=prefix_file, prefix_of_blob=prefix_blob, side='BEFORE THE PUSH',
                        block_exports_nothing=bool(ok_block), export_shaped_lines=len(exports_shape),
                        unstatused=unstatused, lean_touched=len(kernel_lean_dirty),
                        list_above_still_exports_absent=J['n_absent'],
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0 if (prefix_file and prefix_blob and ok_block and not kernel_lean_dirty) else 1


if __name__ == '__main__':
    sys.exit(main())
