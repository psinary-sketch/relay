# -*- coding: utf-8 -*-
"""b329_axiom_probe.py -- WHICH TACTICS AND WHICH CORE LEMMAS CARRY AXIOMS, MEASURED.

### ### **THE FINDING THIS FILE EXISTS TO RECORD:** ### the core library's lemmas about `∣`, `%`, `/`
### and `Nat.Coprime` -- and `Nat.mul_assoc` -- carry `propext` (and often `Quot.sound`), as do
### `omega`, `simp`, `ac_rfl` and `by_cases` on divisibility. ### The audit bar is zero axioms, so the
### module's general theorems are stated as equations with witnesses and proved from the axiom-free
### part of core plus helpers proved by induction. ### **THE PROBE FILE IS `data/b329_axiom_probe.lean`
### AND ITS STDOUT IS WRITTEN HERE VERBATIM**, then counted: the elaboration runs from the kernel's
### checkout with its `LEAN_PATH`, through b302's `elaborate`, never a shell redirection.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_kernel as K  # noqa: E402

PROBE = os.path.join(ROOT, 'data', 'b329_axiom_probe.lean')
OUT = os.path.join(ROOT, 'data', 'b329_axiom_probe.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def main():
    raw, rc, err = K.elaborate(PROBE)
    txt = raw.decode('utf-8', 'replace').replace('\r\n', '\n')
    lines = [ln for ln in txt.split('\n') if ln.strip()]
    clean = [ln for ln in lines if ln.rstrip().endswith('does not depend on any axioms')]
    dirty = [ln for ln in lines if 'depends on axioms' in ln]
    out = []
    out.append('=' * 100)
    out.append('b329 -- THE AXIOM PROBE. ### WHICH TACTICS AND WHICH CORE LEMMAS CARRY AXIOMS, MEASURED.')
    out.append('=' * 100)
    out.append('  probe file        : %s' % os.path.basename(PROBE))
    out.append('  exit code / stderr bytes : %d / %d' % (rc, len(err.strip())))
    out.append('  prints            : %d  (axiom-free %d ; carrying axioms %d)' % (len(clean) + len(dirty), len(clean), len(dirty)))
    out.append('')
    out.append('  ### THE PRINTS, VERBATIM:')
    for ln in lines:
        out.append('      %s' % ln)
    if err.strip():
        out.append('')
        out.append('  ### STDERR:')
        for ln in err.decode('utf-8', 'replace').splitlines():
            out.append('      %s' % ln)
    out.append('')
    tac = [ln for ln in dirty if re.match(r"'t_", ln)]
    out.append('  ### TACTICS CARRYING AXIOMS : %d  -- %s' % (len(tac), ', '.join(re.findall(r"'(t_\w+)'", ' '.join(tac)))))
    core = [ln for ln in dirty if not re.match(r"'t_", ln)]
    out.append('  ### CORE LEMMAS CARRYING AXIOMS : %d' % len(core))
    out.append('  ### THE CONSEQUENCE: the general theorems of FiniteSideSeal.lean are stated as equations with')
    out.append('  ### witnesses and proved from the axiom-free names in section (3) plus helpers proved by induction.')
    out.append('=' * 100)
    io.open(OUT, 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
    print('\n'.join(out[:6] + out[-6:]))
    return 0 if rc == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
