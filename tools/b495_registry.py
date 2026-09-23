# -*- coding: utf-8 -*-
"""b495_registry.py -- COMPONENT 5. ### **ONE ROW IN THE KERNEL TABLE, AND IT CITES NOTHING.**

### (R106)(3): ### **NO ROW CITES THE KERNEL BEFORE THE PROFILE IS BANKED.** ### The row therefore
### carries `deposit-pin NONE`, the pushed SHA as working-head, the source at the pin, and
### ### **PROFILE: PENDING** -- and it names NO TERMINAL, because naming one is citing one.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REG = os.path.join(PP, 'REGISTRY.md')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def sha(b):
    return hashlib.sha256(b).hexdigest()


HEADING = '## Kernel-table addition — 2026-09-23 — `SIDE-explicit-formula` (act b495)'

ROW = """
---

%(heading)s

**APPENDED, NOT INSERTED.** The DEPOSIT-PIN / WORKING-HEAD table above is not edited; this row
is filed beneath it, in its columns, because **the table's own law is that pins are read live
and never recalled** and an append leaves every prior reading where its act left it.

| repo | **DEPOSIT-PIN** *(what published prose cites)* | **WORKING-HEAD** *(live, 2026-09-23)* |
|:--|:--|:--|
| **`SIDE-explicit-formula`** *(NEW 2026-09-23, act b495)* | **`NONE`** — **no published prose cites this kernel, and none may until a profile is banked** ((R106)(3)) | **`%(head)s`, branch `main`**, 0 tags, %(tracked)d files tracked, `%(leans)d` `.lean` |

**WHAT IT IS.** A vendored kernel: the %(mods)d-module local import closure of
`%(seed)s` copied from `anthropics/formal-math` (the `zeta23` formalization) at
**`%(pin)s` = `%(pin_sha)s`**. Every body is byte-identical to its source,
proved per module by a pair of digests — the source blob at the pin and the copied body on disk
**taken before any header was prepended** — agreeing at **%(agree)d of %(mods)d**. `LICENSE` and
`NOTICE` are carried whole (Apache 2.0 §4). %(npnt)d of the modules lie under
`Zeta23/FromPNTPlus/` and carry a second attribution header naming PrimeNumberTheoremAnd, as
zeta23's own `NOTICE` names them; those files also carry their **own** upstream notice, which
this programme did not write and did not alter.

**PINS.** `lean-toolchain` `%(toolchain)s`, mathlib `%(mathlib)s` — **as zeta23
pins them.** SPIRAL_MAP §7 rule 4 expects per-kernel divergence and this kernel states it: a
vendored body must compile against the library its author compiled it against.

**PROFILE: `PENDING`.** ### **NOTHING IN THIS KERNEL HAS BEEN BUILT OR `#print axioms`-ED BY
THIS PROGRAMME.** A build was launched detached at the close of b495 and **its log was not read
in that act**; b496 reads it and banks what it finds. Until then this row names **no terminal**,
confers **no grade**, and supports **no citation** — a vendored copy is not a result, a push is
not a verification, and a launched build is not a built build.

**RULE 9 IS WAIVED FOR THIS NAMESPACE**, appended beside rule 9 in SPIRAL_MAP §7 with act b495
as its reason; the waiver lapses for any file this programme edits.
"""


def main():
    cj = json.loads(io.open(os.path.join(D, 'b495_create.json'), encoding='utf-8').read())
    pj = json.loads(io.open(os.path.join(D, 'b495_push.json'), encoding='utf-8').read())

    with open(REG, 'rb') as fh:
        before = fh.read()
    before_txt = before.decode('utf-8', 'replace').replace(chr(13), '')
    before_lines = before_txt.split(NL)

    rec('=' * 104)
    rec('b495 COMPONENT 5 -- THE REGISTRY ROW. ### **IT CITES NOTHING, AND THAT IS THE POINT.**')
    rec('=' * 104)
    rec('  file   : PLACE-papers/REGISTRY.md')
    rec('  before : %d bytes, %d lines, sha256 %s' % (len(before), len(before_lines), sha(before)))

    tbl = next((i for i, l in enumerate(before_lines)
                if l.startswith('## DEPOSIT-PIN / WORKING-HEAD')), None)
    rec('  the kernel table`s heading at line %s'
        % ((tbl + 1) if tbl is not None else '### NOT FOUND'))
    if tbl is None:
        rec('  ### ### **HALT. ### THE TABLE THE ROW BELONGS TO IS NOT AT ITS ADDRESS.**')
        return 2
    if HEADING in before_txt:
        rec('  ### ### **THE ROW IS ALREADY PRESENT. ### REFUSING TO APPEND A SECOND.**')
        return 2
    rec('')

    body = (ROW % dict(heading=HEADING, head=pj['head'][:7], tracked=pj['tracked'],
                       leans=pj['leans'], mods=cj['modules'], seed=cj['seed'], pin=cj['pin'],
                       pin_sha=cj['pin_sha'], agree=cj['agreeing'], npnt=len(cj['pnt']),
                       toolchain=cj['toolchain'], mathlib=cj['mathlib'][:12])).encode('utf-8')
    with open(REG, 'ab') as fh:
        fh.write(body)
    with open(REG, 'rb') as fh:
        after = fh.read()
    after_txt = after.decode('utf-8', 'replace').replace(chr(13), '')
    after_lines = after_txt.split(NL)

    prefix_ok = after.startswith(before)
    removed = len(before_lines) - sum(1 for a, b in zip(after_lines, before_lines) if a == b)
    headings = after_txt.count(HEADING)

    # ### ### **THE NO-CITATION CLAIM IS CHECKED, NOT ASSERTED.** ### A row that names a terminal
    # ### IS a citation however the prose around it is worded, so the appended block is scanned
    # ### for the shapes a terminal name takes in this table.
    added = after_txt[len(before_txt):]
    names = re.findall(r'`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)+)`', added)
    terminals = [n for n in names if not n.startswith(('Zeta23.WeilEF.Main', 'Zeta23.FromPNTPlus'))
                 and not n.endswith(('.md', '.json', '.toml', '.lean'))]
    rec('  after  : %d bytes, %d lines, sha256 %s' % (len(after), len(after_lines), sha(after)))
    rec('  ### ### **PREFIX PROOF : %s.** ### **LINES REMOVED : %d.** ### **HEADINGS ADDED : %d.**'
        % (prefix_ok, removed, headings))
    rec('')
    rec('  ### THE NO-CITATION CHECK, RUN OVER THE APPENDED BLOCK ITSELF.')
    rec('    dotted names in the block : %s' % (sorted(set(names)) or 'none'))
    rec('    ### of those, TERMINAL-SHAPED (not the vendoring seed, not a filename) : ### **%d** %s'
        % (len(terminals), sorted(set(terminals)) or ''))
    rec('    ### ### **THE SEED IS NAMED AS THE THING VENDORED, NOT AS A RESULT.**')
    rec('    ### `Zeta23.WeilEF.Main` is a MODULE, and the row says what was copied; it names no')
    rec('    ### theorem, states no profile, and confers no grade. ### **(R106)(3) IS SATISFIED')
    rec('    ### BY THE ABSENCE, AND THE ABSENCE IS MEASURED.**')
    rec('    profile cell : ### **PENDING** ; deposit-pin cell : ### **NONE**')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_registry.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(before_sha=sha(before), after_sha=sha(after), prefix=prefix_ok,
                   lines_removed=removed, headings=headings, table_line=tbl + 1,
                   terminals_named=sorted(set(terminals)), dotted=sorted(set(names)),
                   bytes_added=len(after) - len(before)),
              io.open(os.path.join(D, 'b495_registry.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_registry.txt, b495_registry.json')
    return 0 if (prefix_ok and removed == 0 and headings == 1 and not terminals) else 1


if __name__ == '__main__':
    sys.exit(main())
