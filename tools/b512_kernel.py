# -*- coding: utf-8 -*-
"""b512_kernel.py -- COMPONENTS 0 AND 1 IN SIDE-explicit-formula. ### `python tools/b512_kernel.py compile | statement | profile | axiomcheck`

### `compile`    -- `lake env lean -o <olean> SIDEExplicitFormula/Registers.lean`; every run banked by `run_clock`.
### `statement`  -- `h2_sign`, `h2_sign_aim` and `classK` printed from their declaration lines to their `:=`.
### `profile`    -- `#print axioms` on `h2_sign_imp_cell`, MATCHED ON THE WHOLE STRING, with `h2_sign_imp_aim` beside it.
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
MOD = os.path.join('SIDEExplicitFormula', 'Registers.lean')
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'Registers.olean')
PRINT = os.path.join(D, 'b512_printaxioms.lean')
NAME = 'SIDEExplicitFormula.B321.h2_sign_imp_cell'
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
    lake(['-o', OLEAN, MOD], 'b512_compile_log')
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
    io.open(os.path.join(D, 'b512_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(heads) + NL)
    io.open(os.path.join(D, 'b512_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(whole) + NL)
    print('%d declarations banked' % len(whole))
    return 0


def profile():
    io.open(PRINT, 'w', encoding='utf-8', newline=NL).write(
        'import SIDEExplicitFormula.Registers\n\n#print axioms %s\n#print axioms SIDEExplicitFormula.B321.h2_sign_imp_aim\n' % NAME)
    r = lake([PRINT], 'b512_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    new = [l for l in lines if l.startswith("'%s'" % NAME)]
    ctl = [l for l in lines if l.startswith("'SIDEExplicitFormula.B321.h2_sign_imp_aim'")]
    res = dict(new=new, control=ctl, new_std3=(new == [STD3 % NAME]),
               control_std3=(ctl == [STD3 % 'SIDEExplicitFormula.B321.h2_sign_imp_aim']),
               sorry=('sorryAx' in r.stdout), exit=r.returncode)
    io.open(os.path.join(D, 'b512_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### the theorem, whole string : %s ; the control : %s' % (res['new_std3'], res['control_std3']))
    return 0


def axiomcheck():
    r = lake(['AxiomCheck.lean'], 'b512_axiomcheck_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    io.open(os.path.join(D, 'b512_axiomcheck.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout)), indent=1) + NL)
    return 0


if __name__ == '__main__':
    sys.exit({'compile': compile_, 'statement': statement, 'profile': profile, 'axiomcheck': axiomcheck}[sys.argv[1]]())
