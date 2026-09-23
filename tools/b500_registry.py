# -*- coding: utf-8 -*-
"""b500_registry.py -- COMPONENT 3: THE ROW, AND THE TABLE. ### **ONLY IF (R82) HOLDS.**

### ONE note APPENDED at the end of REGISTRY.md, where the `SIDE-explicit-formula` block ends; the
### PENDING paragraph is not edited. ### Then `tools/terminal_table.py` (CARRIED, UNEDITED) is re-run and
### its diff printed.
"""
import hashlib
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
REG = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers', 'REGISTRY.md')
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def main():
    R = json.loads(io.open(os.path.join(D, 'b500_results.json'), encoding='utf-8').read())
    rec('=' * 104)
    rec('COMPONENT 3 -- THE ROW, AND THE TABLE.')
    rec('=' * 104)
    if R.get('r82') != 'HOLDS':
        rec('    ### ### **(R82) DOES NOT HOLD -- COMPONENT 3 WRITES NOTHING.**')
        return 2
    # ### the tree the build compiled: the launch was at 21:14 UTC against HEAD 52d8cf9; b499 later
    # ### committed c29c2eb, which touches the guard only. ### Checked, not assumed:
    lean_diff = subprocess.run(['git', '-C', KERNEL, 'diff', '--name-only', '52d8cf9', 'HEAD'],
                               capture_output=True, text=True).stdout.split()
    rec('    kernel files changed between the build`s tree 52d8cf9 and HEAD : %s' % (lean_diff or 'NONE'))
    if any(x.endswith('.lean') or x.startswith(('lake', 'lean-toolchain')) for x in lean_diff):
        rec('    ### ### **A BUILD INPUT CHANGED SINCE THE BUILD -- STOP.**')
        return 2
    p = R['profiles']
    note = (NL + '**PROFILE, BANKED BY `b500`, 2026-09-23 — the `PENDING` cell above, restated by '
            'appended note; that paragraph is not edited.** Read from `#print axioms` in the corpus’s own '
            'clone, at `SIDE-explicit-formula` `52d8cf9` (the build’s tree; `c29c2eb` since changes only '
            'the guard), toolchain `v4.33.0-rc2`, mathlib `51e6992e`, the log committed unchanged at '
            '`relay/data/b498_ef_build.log` sha256 `%s`: `Zeta23.WeilEF.EF_lit_zetaZeroConfig` — `[%s]`; '
            '`Zeta23.EF.EF_lit` — `[%s]`; `Zeta23.WeilEF.EF_lit_zeta` — `[%s]`. **All three the standard '
            'three, matched on the whole axiom string; `(R82)` HOLDS at this run.** The build exited 0 with '
            '57 `Zeta23.*` modules built and none failed. **No grade is conferred and no keystone cites '
            'the kernel in this act.**' % (R['sha256'], p['EF_lit_zetaZeroConfig']['axioms'],
                                          p['EF_lit']['axioms'], p['EF_lit_zeta']['axioms'])) + NL
    before = open(REG, 'rb').read()
    crlf = b'\r\n' in before
    add = (note.replace(NL, '\r\n') if crlf else note).encode('utf-8')
    if not before.endswith(b'\n'):
        add = (b'\r\n' if crlf else b'\n') + add
    with open(REG, 'ab') as fh:
        fh.write(add)
    after = open(REG, 'rb').read()
    ok = after.startswith(before)
    rec('    REGISTRY.md : %d bytes appended ; prior bytes a TRUE PREFIX : %s' % (len(after) - len(before), ok))
    # ------------------------------------------------ the table
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True,
                       text=True, encoding='utf-8', errors='replace')
    diff = json.loads(io.open(os.path.join(D, 'terminal_table_diff.json'), encoding='utf-8').read() or '{}')
    rec('    terminal_table.py : exit %d' % r.returncode)
    rec('    ### the diff : rows added %d ; rows gone %d ; grade-or-profile changed %d'
        % (len(diff.get('added') or []), len(diff.get('gone') or []), len(diff.get('changed') or [])))
    for c in (diff.get('changed') or [])[:12]:
        rec('      %s' % json.dumps(c, ensure_ascii=False)[:200])
    ef = [x for x in (diff.get('added') or []) + (diff.get('changed') or []) if 'EF_lit' in json.dumps(x)]
    rec('    ### entries of the diff naming EF_lit : %d' % len(ef))
    rec('    ### ### **THE TABLE IS AN INSTRUMENT OUTPUT; WHAT IT READS IS ITS OWN.** ### Whether it picks the')
    rec('    ### profile up from the appended note is printed above, not assumed.')
    rec('=' * 104)
    R['c3'] = dict(appended=len(after) - len(before), prefix=ok, table_exit=r.returncode,
                   table_changed=len(diff.get('changed') or []), table_added=len(diff.get('added') or []),
                   table_ef_entries=len(ef), kernel_changed=lean_diff,
                   reg_before=hashlib.sha256(before).hexdigest(), reg_after=hashlib.sha256(after).hexdigest())
    io.open(os.path.join(D, 'b500_results.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(R, indent=1, ensure_ascii=False) + NL)
    io.open(os.path.join(D, 'b500_components_c3.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print('  written: b500_components_c3.txt')
    return 0 if ok and r.returncode == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
