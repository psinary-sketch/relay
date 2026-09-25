# -*- coding: utf-8 -*-
"""b536_kernel.py -- THE KERNEL COMPONENT IN SIDE-explicit-formula. ### `python tools/b536_kernel.py install | compile | statement | profile`

### `install`   -- the sealed draft (scratchpad) copied into the kernel as the NEW files SIDEExplicitFormula/Seam.lean and
###                AxiomCheckSeam.lean (no prior bytes); the draft`s sha256 printed and banked.
### `compile`   -- `lake env lean -o <olean> SIDEExplicitFormula/Seam.lean`; EVERY RUN IS AN ATTEMPT, numbered, its source
###                banked beside its log by `run_clock`, the declarations its errors fall in recorded (`failed_decls`).
### `statement` -- every declaration from its line to its first `:=` OR its first equation line (`  |`), and whole
###                (b533`s defect (c) cured here: an equation-compiler head no longer runs on).
### `profile`   -- `lake env lean AxiomCheckLimit.lean`: each theorem MATCHED ON THE WHOLE STRING; the `#check` lines, multi-line.
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
SCR = os.environ.get('B536_DRAFT', '')
MOD = os.path.join('SIDEExplicitFormula', 'Seam.lean')
PW = os.path.join('SIDEExplicitFormula', 'PowerWindow.lean')
CHK = 'AxiomCheckSeam.lean'
OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'Seam.olean')
PW_OLEAN = os.path.join('.lake', 'build', 'lib', 'lean', 'SIDEExplicitFormula', 'PowerWindow.olean')
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
NS = 'SIDEExplicitFormula.B321.'
THMS = ['zeta_zero_re_nonpos', 'rh_strip_imp_rh_holds', 'h2_sign_imp_rh_holds', 'h2_sign_iff_rh', 'h2_sign_imp_ch_holds', 'ch_iff_h2_sign']
CHECKS = ['zeta_zero_re_nonpos', 'rh_strip_imp_rh_holds', 'h2_sign_iff_rh', 'ch_iff_h2_sign', 'h2_sign_imp_rh_holds', 'h2_sign_imp_ch_holds']
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def code_lines(text):
    return [l for l in text.replace(chr(13), '').split(NL) if not l.lstrip().startswith('--')]


def install():
    """### the sealed draft copied into the kernel as the NEW files Seam.lean and AxiomCheckSeam.lean (no prior bytes)."""
    out = {}
    for name, dst in (('Seam.lean', MOD), (CHK, CHK)):
        src = os.path.join(SCR, name)
        p = os.path.join(KER, dst)
        prior = sha(p) if os.path.exists(p) else None
        shutil.copyfile(src, p)
        out[name] = dict(prior_sha=prior, draft_sha=sha(src), installed_sha=sha(p))
    io.open(os.path.join(D, 'b536_install.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    print(json.dumps(out, indent=1))
    return 0


def lake(args, stem):
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean'] + args, cwd=KER, capture_output=True, text=True, encoding='utf-8', errors='replace')
    body = ['$ lake env lean ' + ' '.join(args), 'exit %d ; %.1f s' % (r.returncode, time.time() - t0), '--- stdout ---',
            r.stdout.rstrip(NL), '--- stderr ---', r.stderr.rstrip(NL)]
    p = run_clock.write(D, stem, body)
    print(NL.join(body)[-8000:])
    print('### banked : %s' % p)
    return r, time.time() - t0


def compile_():
    os.makedirs(os.path.join(KER, os.path.dirname(OLEAN)), exist_ok=True)
    att = os.path.join(D, 'b536_attempts.json')
    hist = json.loads(io.open(att, encoding='utf-8').read()) if os.path.exists(att) else []
    n = len(hist) + 1
    srcp = os.path.join(D, 'b536_attempt%d.lean' % n)
    shutil.copyfile(os.path.join(KER, MOD), srcp)
    r, secs = lake(['-o', OLEAN, MOD], 'b536_compile_log')
    errs = [l for l in r.stdout.split(NL) if ': error' in l]
    srctext = io.open(srcp, encoding='utf-8').read().split(NL)
    starts = [(i + 1, re.match(r'^(?:theorem|def|structure) (\S+)', l).group(1)) for i, l in enumerate(srctext)
              if re.match(r'^(?:theorem|def|structure) \S+', l)]
    failed = set()
    for e in errs:
        m = re.search(r'Seam\.lean:(\d+):', e)
        if m:
            ln = int(m.group(1))
            owner = [nm for st, nm in starts if st <= ln]
            if owner:
                failed.add(owner[-1])
    hist.append(dict(attempt=n, exit=r.returncode, seconds=round(secs, 1), errors=len(errs), first_errors=errs[:12],
                     sorry=bool(re.search(r'\bsorry\b', r.stdout)), source_sha=sha(srcp), failed_decls=sorted(failed)))
    io.open(att, 'w', encoding='utf-8', newline=NL).write(json.dumps(hist, indent=1) + NL)
    print('### ATTEMPT %d : exit %d, %d error lines, %.1f s ; failing %s' % (n, r.returncode, len(errs), secs, sorted(failed)))
    return 0


def src():
    return io.open(os.path.join(KER, MOD), encoding='utf-8').read()


def decls(s):
    out = []
    ms = list(re.finditer(r'^(?:def|theorem|structure) (\S+)', s, re.M))
    for k, m in enumerate(ms):
        i = m.start()
        nxt = re.search(r'^(?:theorem|def|structure|open |/-|end |variable|example|--)', s[m.end():], re.M)
        whole = s[i:m.end() + (nxt.start() if nxt else len(s) - m.end())].rstrip()
        cuts = [x for x in (whole.find(':='), whole.find(NL + '  |'), whole.find(' where')) if x >= 0]
        head = whole[:min(cuts)].rstrip() if cuts else whole
        out.append(dict(name=m.group(1), head=head, whole=whole, lines=len(whole.split(NL))))
    return out


def statement():
    d = decls(src())
    io.open(os.path.join(D, 'b536_statement.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['head'] for x in d) + NL)
    io.open(os.path.join(D, 'b536_definitions.txt'), 'w', encoding='utf-8', newline=NL).write((NL + NL).join(x['whole'] for x in d) + NL)
    print('%d declarations banked' % len(d))
    return 0


def profile():
    r, _ = lake([CHK], 'b536_profile_log')
    lines = [l.strip() for l in r.stdout.split(NL) if 'depends on axioms' in l or 'does not depend' in l]
    res = dict(lines=lines, exit=r.returncode, sorry=('sorryAx' in r.stdout),
               std3={NS + n: ([l for l in lines if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)]) for n in THMS})
    out = r.stdout
    res['checks'] = {}
    for nm in CHECKS:
        i = out.find(NS + nm + ' :')
        if i < 0:
            res['checks'][nm] = None
            continue
        rest = out[i + 1:]
        nxt = [x for x in (rest.find(NL + NS), rest.find(NL + "'")) if x >= 0]
        res['checks'][nm] = out[i:i + 1 + min(nxt)].strip() if nxt else out[i:].strip()
    io.open(os.path.join(D, 'b536_profile.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1, ensure_ascii=False) + NL)
    print('### whole-string standard three : %d of %d' % (sum(res['std3'].values()), len(res['std3'])))
    for k, v in res['std3'].items():
        if not v:
            print('    NOT STD3 : %s' % k)
    for k, v in res['checks'].items():
        print('### #check %s : %s' % (k, ' '.join((v or 'NONE').split())))
    return 0


if __name__ == '__main__':
    sys.exit({'install': install, 'compile': compile_, 'statement': statement, 'profile': profile}[sys.argv[1]]())
