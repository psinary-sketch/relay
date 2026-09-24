# -*- coding: utf-8 -*-
"""b513_kernel.py -- COMPONENTS 0 AND 1 IN SIDE-explicit-formula. ### `python tools/b513_kernel.py compile | statement | profile | axiomcheck`

### `compile`    -- `lake env lean -o <olean> SIDEExplicitFormula/RHChain.lean`; every run banked by `run_clock`.
### `statement`  -- every declaration of RHChain.lean printed from its declaration line to its `:=`, and whole.
### `profile`    -- `lake env lean AxiomCheckChain.lean` in the kernel: the three links, EACH MATCHED ON THE WHOLE STRING.
### `axiomcheck` -- `lake env lean AxiomCheck.lean` in the kernel`s own tree, the output banked verbatim.
### ### Lean`s exit code is printed and is NOT the verdict: a failed declaration elaborates with `sorryAx`.
"""
import io
import json
import os
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import run_clock  # noqa: E402
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MOD = os.path.join('SIDEExplicitFormula', 'RHChain.lean')
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'RHChain.olean')
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def lake(args, stem):
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean'] + args, cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    body = ['$ lake env lean ' + ' '.join(args), 'exit %d ; %.1f s' % (r.returncode, time.time() - t0), '--- stdout ---',
            r.stdout.rstrip(NL), '--- stderr ---', r.stderr.rstrip(NL)]
    p = run_clock.write(D, stem, body)
    print(NL.join(body))
    print('### banked : %s' % p)
    return r


def compile_():
    os.makedirs(os.path.join(KER, os.path.dirname(OLEAN)), exist_ok=True)
    lake(['-o', OLEAN, MOD], 'b513_compile_log')
    return 0


def statement():
    """### every declaration of the module: its line to its `:=` (b510_statement form), and WHOLE (a def`s content is after it)."""
    import re
    src = io.open(os.path.join(KER, MOD), encoding='utf-8').read()
    heads, whole = [], []
    for m in re.finditer(r'^(?:def|theorem) \S+', src, re.M):
        i = m.start()
        j = src.index(':=', i)
        heads.append(src[i:j + 2])
        k = src.find(NL + NL, i)
        whole.append(src[i:k if k >= 0 else len(src)].rstrip())
    io.open(os.path.join(D, 'b513_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(heads) + NL)
    io.open(os.path.join(D, 'b513_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(whole) + NL)
    print('%d declarations banked' % len(whole))
    return 0


LINKS = ['SIDEExplicitFormula.B321.rh_imp_h2_sign', 'SIDEExplicitFormula.B321.h2_sign_imp_cell',
         'SIDEExplicitFormula.B321.rh_imp_cell_form']


def profile():
    """### the kernel`s own `AxiomCheckChain.lean` IS the print file (READING (5)); every link matched on the WHOLE string."""
    r = lake(['AxiomCheckChain.lean'], 'b513_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    res = dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout),
               std3={n: ([l for l in lines if l.startswith("'%s'" % n)] == [STD3 % n]) for n in LINKS})
    res['new'] = [l for l in lines if l.startswith("'%s'" % LINKS[0])]
    res['new_std3'] = res['std3'][LINKS[0]]
    io.open(os.path.join(D, 'b513_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### whole-string standard three : %s' % res['std3'])
    return 0


def axiomcheck():
    r = lake(['AxiomCheck.lean'], 'b513_axiomcheck_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    io.open(os.path.join(D, 'b513_axiomcheck.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout)), indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit({'compile': compile_, 'statement': statement, 'profile': profile, 'axiomcheck': axiomcheck}[sys.argv[1]]())
