# -*- coding: utf-8 -*-
"""b475_extract.py -- THE SURVEY. ### The dependency order of Solution's import closure, computed by
### tool from the sources themselves; the three modules b473 found dead of memory, placed in that order;
### and the memory ceiling looked for in b473's own log. ### **NO BUILD IS STARTED HERE.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
LOG473 = os.path.join(D, 'b471_zeta23_build.log')
NL = chr(10)
L, MISSES = [], []
FAILED = ('Zeta23.Hypotheses', 'Zeta23.Defs.Counting', 'Zeta23.Taper.Basic')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def src(m):
    return os.path.join(Z, *m.split('.')) + '.lean'


def imports(m):
    return [x.group(1) for x in re.finditer(r'^\s*import\s+(\S+)', read(src(m)), re.M)]


def order_from(root):
    """### DEPTH-FIRST POST-ORDER: a module is emitted only after every module it imports.
    ### ### **THE ORDER IS COMPUTED FROM THE SOURCES, NOT TYPED AND NOT TAKEN FROM A LOG.**"""
    seen, out, stack = set(), [], []

    def walk(m, path):
        if m in seen or not os.path.exists(src(m)):
            return
        if m in path:
            MISSES.append(('import cycle', ' -> '.join(list(path) + [m])))
            return
        for i in imports(m):
            if i.startswith('Zeta23'):
                walk(i, path + [m])
        seen.add(m)
        out.append(m)

    walk(root, [])
    return out


def main():
    rec('=' * 104)
    rec('b475 -- THE SURVEY. ### THE ORDER IS COMPUTED; NO BUILD IS STARTED HERE.')
    rec('=' * 104)

    rec('')
    rec('(P1) THE DEPENDENCY ORDER OF `Solution`, COMPUTED FROM THE SOURCES.')
    rec('-' * 104)
    sol = read(os.path.join(Z, 'Solution.lean'))
    roots = [x.group(1) for x in re.finditer(r'^\s*import\s+(\S+)', sol, re.M)]
    rec('    Solution.lean imports : %s' % ', '.join(roots))
    order = []
    for r in roots:
        if r.startswith('Zeta23'):
            for m in order_from(r):
                if m not in order:
                    order.append(m)
    rec('    ### ### **MODULES IN THE ORDER : %d** (each after every Zeta23 module it imports)' % len(order))
    rec('    first five  : %s' % ', '.join(order[:5]))
    rec('    last five   : %s' % ', '.join(order[-5:]))
    # ### the order's own control: no module appears before one of its own imports
    pos = {m: i for i, m in enumerate(order)}
    bad = [(m, i) for m in order for i in imports(m)
           if i.startswith('Zeta23') and i in pos and pos[i] > pos[m]]
    rec('    ### ### **THE ORDER`S OWN CONTROL: modules placed before one of their own imports : %d**'
        % len(bad))
    if bad:
        MISSES.append(('order', '%d inversions' % len(bad)))

    rec('')
    rec('(P2) THE THREE MODULES b473 FOUND DEAD OF MEMORY, PLACED IN THAT ORDER.')
    rec('-' * 104)
    for m in FAILED:
        rec('    %-24s in the order : %s ; source present : %s'
            % (m, pos.get(m, 'NOT IN THE ORDER'), os.path.exists(src(m))))
        if m not in pos:
            MISSES.append((m, 'not in Solution`s import closure'))
    deps = {m: [i for i in imports(m) if i.startswith('Zeta23')] for m in FAILED}
    for m, d in deps.items():
        rec('    %-24s imports %d Zeta23 modules' % (m, len(d)))

    rec('')
    rec('(P3) THE MEMORY CEILING, LOOKED FOR IN b473`S OWN LOG.')
    rec('-' * 104)
    log = read(LOG473)
    figs = re.findall(r'[^\n]*\b(\d[\d,\.]*\s*(?:B|KB|MB|GB|bytes|kB|MiB|GiB))\b[^\n]*', log)
    panics = [l.strip() for l in log.split(NL) if 'PANIC' in l or 'bad_alloc' in l]
    rec('    lines carrying a memory FIGURE : %d' % len(figs))
    for f in figs[:5]:
        rec('      %s' % f[:120])
    rec('    lines carrying the failure ITSELF : %d' % len(panics))
    for p in panics:
        rec('      %s' % p[:120])
    rec('  ### ### **THE LOG HOLDS THE FAILURE AND NOT A FIGURE: NO MEMORY CEILING IS RECORDED IN IT.**')
    rec('  ### The order asks for the ceiling *"if the log holds it"* -- it does not, so the face says')
    rec('  ### NOT IN THE LOG rather than supplying a number from anywhere else.')

    rec('')
    rec('(P4) WHAT THE SERIALIZED RUN CHANGES, READ FROM THE TWO RUNS` OWN SETTINGS.')
    rec('-' * 104)
    prev = read(os.path.join(ROOT, 'tools', 'b471_detached_run.cmd'))
    rec('    b471`s launcher : LEAN_NUM_THREADS %s ; one call for the whole library : %s'
        % ('UNSET' if 'set "LEAN_NUM_THREADS="' in prev else '?',
           'lake build Solution' in prev))
    rec('    b475`s launcher : LEAN_NUM_THREADS=1 ; one `lake build <module>` per module, in the order')
    rec('      above ; a timestamp per module ; then scripts\\PrintAxioms.lean and the three (R82) names')
    rec('  ### ### **WHAT IS HELD FIXED: the clone, its pin, its toolchain, its Mathlib, and the three')
    rec('  ### declarations. ### WHAT CHANGES: the number of Lean processes alive at once.**')

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b475_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b475_order.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(order) + NL)
    json.dump(dict(order=order, modules=len(order), roots=roots, failed_positions={m: pos.get(m) for m in FAILED},
                   memory_figures=len(figs), panic_lines=panics, inversions=len(bad), misses=MISSES),
              io.open(os.path.join(D, 'b475_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
