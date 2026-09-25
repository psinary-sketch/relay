# -*- coding: utf-8 -*-
"""b527_kernel.py -- COMPONENTS 1-3 IN SIDE-explicit-formula. ### `python tools/b527_kernel.py install | compile | statement | read | profile | diff`

### `install`   -- the sealed draft (scratchpad) copied into the kernel as SIDEExplicitFormula/TwoPropertyWindow.lean and
###                AxiomCheckWindow.lean; the draft`s sha256 printed and banked. Run ONCE, after the seal.
### `compile`   -- `lake env lean -o <olean> SIDEExplicitFormula/TwoPropertyWindow.lean`; EVERY RUN IS AN ATTEMPT (READING (4)),
###                numbered, its source banked beside its log by `run_clock`.
### `statement` -- every declaration from its line to its `:=`, and whole.
### `read`      -- line counts; the vendored references resolved to their declaration keywords; the set against b513`s.
### `profile`   -- `lake env lean AxiomCheckWindow.lean`: each theorem MATCHED ON THE WHOLE STRING; the `#check` and `#print`.
### ### Lean's exit code is printed and is NOT the verdict: a failed declaration elaborates with `sorryAx`.
"""
import hashlib
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import run_clock  # noqa: E402
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SCR = os.environ.get('B524_DRAFT', '')
MOD = os.path.join('SIDEExplicitFormula', 'TwoPropertyWindow.lean')
CHK = 'AxiomCheckWindow.lean'
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'TwoPropertyWindow.olean')
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
NS = 'SIDEExplicitFormula.B321.'
THMS = ['kWin_classK', 'paperFT_window_zero', 'paperFT_window', 'paperFT_second_order', 'ibp_step', 'weilTest_ofReal_even',
        'plateau_contDiff', 'plateau_even', 'plateau_hasCompactSupport', 'plateau_eq_one', 'plateau_apply_abs']
B513_REFS = ['Zeta23.EF.paperFT_weilTest', 'Zeta23.EF.weilTest', 'Zeta23.IsNontrivialZero', 'Zeta23.RH_implies_on_line',
             'Zeta23.gammaOf', 'Zeta23.paperFT', 'Zeta23.zetaZeroConfig.mult', 'Zeta23.zetaZeroConfig_carrier']
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def install():
    """### the sealed draft copied over the kernel`s module and AxiomCheck; the prior bytes` and the draft`s sha256 banked."""
    out = {}
    for name, dst in (('TwoPropertyWindow.lean', MOD), (CHK, CHK)):
        src = os.path.join(SCR, name)
        prior = sha(os.path.join(KER, dst))
        shutil.copyfile(src, os.path.join(KER, dst))
        out[name] = dict(prior_sha=prior, draft_sha=sha(src), installed_sha=sha(os.path.join(KER, dst)))
    io.open(os.path.join(D, 'b527_install.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    print(json.dumps(out, indent=1))
    return 0


def lake(args, stem):
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean'] + args, cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    body = ['$ lake env lean ' + ' '.join(args), 'exit %d ; %.1f s' % (r.returncode, time.time() - t0), '--- stdout ---',
            r.stdout.rstrip(NL), '--- stderr ---', r.stderr.rstrip(NL)]
    p = run_clock.write(D, stem, body)
    print(NL.join(body)[-6000:])
    print('### banked : %s' % p)
    return r, time.time() - t0


def compile_():
    os.makedirs(os.path.join(KER, os.path.dirname(OLEAN)), exist_ok=True)
    att = os.path.join(D, 'b527_attempts.json')
    hist = json.loads(io.open(att, encoding='utf-8').read()) if os.path.exists(att) else []
    n = len(hist) + 1
    srcp = os.path.join(D, 'b527_attempt%d.lean' % n)
    shutil.copyfile(os.path.join(KER, MOD), srcp)
    r, secs = lake(['-o', OLEAN, MOD], 'b527_compile_log')
    errs = [l for l in r.stdout.split(NL) if ': error' in l]
    hist.append(dict(attempt=n, exit=r.returncode, seconds=round(secs, 1), errors=len(errs), first_errors=errs[:8],
                     sorry=('sorry' in r.stdout), source_sha=sha(srcp)))
    io.open(att, 'w', encoding='utf-8', newline=NL).write(json.dumps(hist, indent=1) + NL)
    print('### ATTEMPT %d : exit %d, %d error lines, %.1f s' % (n, r.returncode, len(errs), secs))
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
    io.open(os.path.join(D, 'b527_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['head'] for x in d) + NL)
    io.open(os.path.join(D, 'b527_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['whole'] for x in d) + NL)
    print('%d declarations banked' % len(d))
    return 0


def resolve(name):
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
    code = NL.join(l for l in code.split(NL) if not l.startswith('import '))
    code = re.sub(r'--[^\n]*', ' ', code)
    refs = sorted(set(re.findall(r'\bZeta23\.[A-Za-z_][A-Za-z0-9_.]*', code)))
    res = dict(decls=[dict(name=x['name'], head=x['head'], lines=x['lines']) for x in d],
               refs=[dict(name=r, resolved=resolve(r)) for r in refs], b513_refs=B513_REFS)
    res['lemma_refs'] = [r['name'] for r in res['refs'] if any(h['keyword'] in ('theorem', 'lemma') for h in r['resolved'])]
    res['def_refs'] = [r['name'] for r in res['refs'] if r['resolved'] and all(h['keyword'] == 'def' for h in r['resolved'])]
    res['lemmas_beyond_b513'] = [r for r in res['lemma_refs'] if r not in B513_REFS]
    res['module_lines'] = len(s.split(NL))
    io.open(os.path.join(D, 'b527_read.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    for x in res['decls']:
        print('  %-26s %3d lines : %s' % (x['name'], x['lines'], x['head'].replace(NL, ' ')[:140]))
    for r in res['refs']:
        print('  ref %-36s -> %s' % (r['name'], ['%(keyword)s in %(file)s' % h for h in r['resolved']]))
    print('  ### vendored lemmas referenced : %s ; beyond b513`s : %s' % (res['lemma_refs'] or 'NONE', res['lemmas_beyond_b513'] or 'NONE'))
    return 0


def profile():
    r, _ = lake([CHK], 'b527_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    res = dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout),
               std3={NS + n: ([l for l in lines if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)]) for n in THMS})
    out = r.stdout
    i = out.find('SIDEExplicitFormula.B321.f_pair_hypothesis :')
    res['check_prop'] = out[i:out.find(NL + NL, i) if out.find(NL + NL, i) > 0 else len(out)].strip() if i >= 0 else None
    j = out.find('def SIDEExplicitFormula.B321.realizedGrowth')
    res['print_growth'] = out[j:out.find('def SIDEExplicitFormula.B321.plateau')].strip() if j >= 0 else None
    kk = out.find('def SIDEExplicitFormula.B321.plateau')
    res['print_plateau'] = out[kk:].strip() if kk >= 0 else None
    res['new'] = [l for l in lines if l.startswith("'%skWin_classK'" % NS)]
    res['new_std3'] = res['std3'][NS + 'kWin_classK']
    io.open(os.path.join(D, 'b527_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### whole-string standard three : %s' % res['std3'])
    print('### #check : %s' % res['check_prop'])
    print('### #print : %s' % res['print_growth'])
    return 0


def diff():
    """### Component 2: every theorem of b524 -- its statement from its line to its `:=` -- against the rebuilt module, byte for byte."""
    old = io.open(os.path.join(D, 'b524_statement.txt'), encoding='utf-8').read()
    new = src()
    oh = {m.group(1): old[m.start():old.index(':=', m.start()) + 2] for m in re.finditer(r'^theorem (\S+)', old, re.M)}
    nh = {x['name']: x['head'] for x in decls(new) if x['head'].startswith('theorem ')}
    rows = [dict(name=n, same=(nh.get(n) == h), present=n in nh) for n, h in oh.items()]
    res = dict(b524_theorems=len(oh), identical=sum(r['same'] for r in rows), changed=[r['name'] for r in rows if not r['same']],
               new_theorems=sorted(set(nh) - set(oh)), diff_lines=sum(0 if r['same'] else 1 for r in rows))
    io.open(os.path.join(D, 'b527_statement_diff.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### b524 theorems %d ; byte-identical %d ; changed %s ; new %s ; DIFF LINES %d'
          % (res['b524_theorems'], res['identical'], res['changed'] or 'NONE', res['new_theorems'], res['diff_lines']))
    return 0


if __name__ == '__main__':
    sys.exit({'install': install, 'compile': compile_, 'statement': statement, 'read': read, 'profile': profile, 'diff': diff}[sys.argv[1]]())
