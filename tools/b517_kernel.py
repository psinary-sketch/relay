# -*- coding: utf-8 -*-
"""b517_kernel.py -- COMPONENTS 1 AND 2 IN SIDE-explicit-formula. ### `python tools/b517_kernel.py compile | statement | read | profile`

### `compile`   -- `lake env lean -o <olean> SIDEExplicitFormula/GrowthBound.lean`; every run banked by `run_clock` (READING (3)).
### `statement` -- every declaration of the module from its line to its `:=`, and whole.
### `read`      -- READING (4)'s line counts, and READING (5)'s vendored references resolved to their declaration keywords.
### `profile`   -- `lake env lean AxiomCheckGrowth.lean` in the kernel: both theorems, EACH MATCHED ON THE WHOLE STRING.
### ### Lean's exit code is printed and is NOT the verdict: a failed declaration elaborates with `sorryAx`.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import run_clock  # noqa: E402
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MOD = os.path.join('SIDEExplicitFormula', 'GrowthBound.lean')
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'GrowthBound.olean')
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
LINKS = ['SIDEExplicitFormula.B321.paperFT_growth', 'SIDEExplicitFormula.B321.paperFT_growth_at']
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
    lake(['-o', OLEAN, MOD], 'b517_compile_log')
    return 0


def src():
    return io.open(os.path.join(KER, MOD), encoding='utf-8').read()


def decls(s):
    out = []
    for m in re.finditer(r'^(?:def|theorem) (\S+)', s, re.M):
        i = m.start()
        j = s.index(':=', i)
        k = s.find(NL + NL, i)
        whole = s[i:k if k >= 0 else len(s)].rstrip()
        out.append(dict(name=m.group(1), head=s[i:j + 2], whole=whole, lines=len(whole.split(NL))))
    return out


def statement():
    d = decls(src())
    io.open(os.path.join(D, 'b517_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['head'] for x in d) + NL)
    io.open(os.path.join(D, 'b517_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['whole'] for x in d) + NL)
    print('%d declarations banked' % len(d))
    return 0


def resolve(name):
    """### a vendored name's declaration keyword, read from the kernel's own vendored tree."""
    last = name.split('.')[-1]
    pat = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:noncomputable\s+)?(theorem|lemma|def|abbrev|structure|instance)\s+%s\b' % re.escape(last), re.M)
    hits = []
    for dp, _d, fs in os.walk(os.path.join(KER, 'Zeta23')):
        for f in fs:
            if f.endswith('.lean'):
                t = io.open(os.path.join(dp, f), encoding='utf-8').read()
                for m in pat.finditer(t):
                    hits.append(dict(file=os.path.relpath(os.path.join(dp, f), KER).replace(os.sep, '/'), keyword=m.group(1)))
    return hits


def read():
    s = src()
    d = decls(s)
    body = s[s.index('import'):]
    code = re.sub(r'/-[\s\S]*?-/', ' ', body)
    code = NL.join(l for l in code.split(NL) if not l.startswith('import '))   # ### a module import is not a declaration (b517`s first read)
    refs = sorted(set(re.findall(r'\bZeta23\.[A-Za-z_][A-Za-z0-9_.]*', code)))
    res = dict(decls=[dict(name=x['name'], head=x['head'], lines=x['lines']) for x in d],
               refs=[dict(name=r, resolved=resolve(r)) for r in refs])
    res['lemma_refs'] = [r['name'] for r in res['refs'] if any(h['keyword'] in ('theorem', 'lemma') for h in r['resolved'])]
    res['def_refs'] = [r['name'] for r in res['refs'] if r['resolved'] and all(h['keyword'] == 'def' for h in r['resolved'])]
    io.open(os.path.join(D, 'b517_read.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    for x in res['decls']:
        print('  %-22s %3d lines : %s' % (x['name'], x['lines'], x['head'].replace(NL, ' ')[:150]))
    for r in res['refs']:
        print('  ref %-24s -> %s' % (r['name'], ['%(keyword)s in %(file)s' % h for h in r['resolved']]))
    print('  ### vendored lemmas referenced : %s ; vendored definitions : %s' % (res['lemma_refs'] or 'NONE', res['def_refs']))
    return 0


def profile():
    r = lake(['AxiomCheckGrowth.lean'], 'b517_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    res = dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout),
               std3={n: ([l for l in lines if l.startswith("'%s'" % n)] == [STD3 % n]) for n in LINKS})
    res['new'] = [l for l in lines if l.startswith("'%s'" % LINKS[0])]
    res['new_std3'] = res['std3'][LINKS[0]]
    io.open(os.path.join(D, 'b517_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### whole-string standard three : %s' % res['std3'])
    return 0


if __name__ == '__main__':
    sys.exit({'compile': compile_, 'statement': statement, 'read': read, 'profile': profile}[sys.argv[1]]())
