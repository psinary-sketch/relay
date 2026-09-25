# -*- coding: utf-8 -*-
"""b529_kernel.py -- COMPONENTS 1-4 IN SIDE-explicit-formula. ### `python tools/b529_kernel.py install | compile | statement | read | profile`

### `install`   -- the sealed draft (scratchpad) copied into the kernel as the NEW files SIDEExplicitFormula/PairTerm.lean and
###                AxiomCheckPair.lean (no prior bytes); the draft`s sha256 printed and banked. Run ONCE, after the seal.
### `compile`   -- `lake env lean -o <olean> SIDEExplicitFormula/PairTerm.lean`; EVERY RUN IS AN ATTEMPT (READING (4)),
###                numbered, its source banked beside its log by `run_clock`.
### `statement` -- every declaration from its line to its `:=`, and whole.
### `read`      -- line counts; the vendored references resolved to their declaration keywords; the LEMMAS against b524`s (N3).
### `profile`   -- `lake env lean AxiomCheckPair.lean`: each theorem MATCHED ON THE WHOLE STRING; the `#check` and `#print`.
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
SCR = os.environ.get('B529_DRAFT', '')
MOD = os.path.join('SIDEExplicitFormula', 'PairTerm.lean')
CHK = 'AxiomCheckPair.lean'
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'PairTerm.olean')
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
NS = 'SIDEExplicitFormula.B321.'
THMS = ['pairTwo_factored', 'pairTwo_near_far', 'nearInt_ge', 'realizedGrowth_eq', 'realizedGrowth_ge_one', 'nearPair_eq',
        'pair_near_sign', 'pair_bound', 'pair_algebra', 'windowSlope_bound', 'kWin_FT', 'cosWinC_FT', 'cosWinC_FT_near_far',
        'phiC_FT_imag', 'phiC_FT_neg', 'farFT_conj', 'paperFT_ofReal_conj', 'gammaOf_rhoZero', 'gammaOf_reflect_rhoZero']
# ### (N3)`s reference set: the vendored LEMMAS b524`s module cited, read from `b524_read.json` at run time (not typed here).
B524_READ = 'b524_read.json'
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def install():
    """### the sealed draft copied into the kernel as two NEW files; `prior_sha` is None when no file stood there (it must be)."""
    out = {}
    for name, dst in (('PairTerm.lean', MOD), (CHK, CHK)):
        src = os.path.join(SCR, name)
        p = os.path.join(KER, dst)
        prior = sha(p) if os.path.exists(p) else None
        shutil.copyfile(src, p)
        out[name] = dict(prior_sha=prior, draft_sha=sha(src), installed_sha=sha(p))
    io.open(os.path.join(D, 'b529_install.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
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
    att = os.path.join(D, 'b529_attempts.json')
    hist = json.loads(io.open(att, encoding='utf-8').read()) if os.path.exists(att) else []
    n = len(hist) + 1
    srcp = os.path.join(D, 'b529_attempt%d.lean' % n)
    shutil.copyfile(os.path.join(KER, MOD), srcp)
    r, secs = lake(['-o', OLEAN, MOD], 'b529_compile_log')
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
    io.open(os.path.join(D, 'b529_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['head'] for x in d) + NL)
    io.open(os.path.join(D, 'b529_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['whole'] for x in d) + NL)
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
               refs=[dict(name=r, resolved=resolve(r)) for r in refs])
    b524 = json.loads(io.open(os.path.join(D, B524_READ), encoding='utf-8').read())['lemma_refs']
    res['b524_lemma_refs'] = b524
    res['lemma_refs'] = [r['name'] for r in res['refs'] if any(h['keyword'] in ('theorem', 'lemma') for h in r['resolved'])]
    res['def_refs'] = [r['name'] for r in res['refs'] if r['resolved'] and all(h['keyword'] == 'def' for h in r['resolved'])]
    res['lemmas_beyond_b524'] = [r for r in res['lemma_refs'] if r not in b524]
    res['module_lines'] = len(s.split(NL))
    io.open(os.path.join(D, 'b529_read.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    for x in res['decls']:
        print('  %-26s %3d lines : %s' % (x['name'], x['lines'], x['head'].replace(NL, ' ')[:140]))
    for r in res['refs']:
        print('  ref %-36s -> %s' % (r['name'], ['%(keyword)s in %(file)s' % h for h in r['resolved']]))
    print('  ### vendored lemmas referenced : %s ; b524`s : %s ; BEYOND b524`s : %s'
          % (res['lemma_refs'] or 'NONE', b524, res['lemmas_beyond_b524'] or 'NONE'))
    return 0


def profile():
    r, _ = lake([CHK], 'b529_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    res = dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout),
               std3={NS + n: ([l for l in lines if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)]) for n in THMS})
    out = r.stdout
    i = out.find('SIDEExplicitFormula.B321.farSmall :')
    res['check_prop'] = out[i:out.find(NL, i)].strip() if i >= 0 else None
    res['prints'] = {}
    for nm in ('pairConst', 'pairEps', 'farSmall', 'nearInt', 'farFT', 'nearPair', 'pairTwo', 'rhoZero'):
        j = out.find('def SIDEExplicitFormula.B321.%s ' % nm)
        if j < 0:
            j = out.find('def SIDEExplicitFormula.B321.%s' % nm + NL)
        k = out.find(NL + 'def ', j + 1) if j >= 0 else -1
        k2 = out.find(NL + "'", j + 1) if j >= 0 else -1
        ends = [e for e in (k, k2) if e > 0]
        res['prints'][nm] = out[j:min(ends) if ends else len(out)].strip() if j >= 0 else None
    io.open(os.path.join(D, 'b529_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print('### whole-string standard three : %d of %d' % (sum(res['std3'].values()), len(res['std3'])))
    for k, v in res['std3'].items():
        print('    %-60s %s' % (k, v))
    print('### #check : %s' % res['check_prop'])
    for k, v in res['prints'].items():
        print('### #print %s : %s' % (k, (v or 'NONE').replace(NL, ' ')[:300]))
    return 0


if __name__ == '__main__':
    sys.exit({'install': install, 'compile': compile_, 'statement': statement, 'read': read, 'profile': profile}[sys.argv[1]]())
