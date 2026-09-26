# -*- coding: utf-8 -*-
"""b544_probe_part.py -- THE ENUMERATION AND THE AXIOM PROBES OF b544, UNDER (R154)(4). Imported by b544_record.py.
### `python tools/b544_probe_part.py decls | probe <repo> | probe-all`
### Reads the federation through `git show` at b542`s pins; the probes run `lake env lean` on a scratch file in the scratchpad
### (no repository is written). TECHNE-Core`s names and statements never leave memory. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b542_record as Q
NL = chr(10)
SCR = os.environ.get('B544_SCRATCH', '')
PRIV = Q.PRIV
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ZETA = [('riemannZeta', r'(?<![A-Za-z0-9_])riemannZeta(?![A-Za-z0-9_₀])'),
        ('completedRiemannZeta', r'(?<![A-Za-z0-9_])completedRiemannZeta(?![A-Za-z0-9_₀])'),
        ('completedRiemannZeta₀', r'(?<![A-Za-z0-9_])completedRiemannZeta₀'), ('jacobiTheta', r'(?<![A-Za-z0-9_])jacobiTheta'),
        ('evenKernel', r'(?<![A-Za-z0-9_])evenKernel'), ('ζ (Zeta23 notation)', r'(?<![A-Za-z_])ζ(?![A-Za-z_₀])'),
        ('zetaZeroConfig', r'(?<![A-Za-z0-9_])zetaZeroConfig(?![A-Za-z0-9_])'),
        ('IsNontrivialZero', r'(?<![A-Za-z0-9_])IsNontrivialZero(?![A-Za-z0-9_])'),
        ('paperFT', r'(?<![A-Za-z0-9_])paperFT(?![A-Za-z0-9_])'), ('weilTest', r'(?<![A-Za-z0-9_])weilTest(?![A-Za-z0-9_])'),
        ('mellin Phi', r'mellin\s+\(?Phi\b')]
BODYKW = ('def', 'abbrev', 'structure', 'class', 'inductive', 'opaque', 'instance')
TERMKW = ('theorem', 'lemma')


def namespaces(raw):
    """line index -> the namespace path open at that line"""
    Lc = Q.blank_all_comments(raw.replace(chr(13), '')).split(NL)
    stack, out = [], []
    for l in Lc:
        s = l.strip()
        m = re.match(r'^namespace\s+([A-Za-z0-9_.₀]+)', s)
        if m:
            stack.append(m.group(1))
        m2 = re.match(r'^end\s+([A-Za-z0-9_.₀]+)\s*$', s)
        if m2 and stack and stack[-1] == m2.group(1):
            stack.pop()
        out.append('.'.join(stack))
    return out


def enumerate_all():
    decls = []
    for r, cited, _ in Q.REPOS:
        pin = cited or 'HEAD'
        files = sorted(f for f in Q.g(r, 'ls-tree', '-r', '--name-only', pin).split(NL) if f.endswith('.lean'))
        for f in files:
            raw = Q.g(r, 'show', '%s:%s' % (pin, f))
            ns = namespaces(raw)
            for x in Q.scan_file(raw, [], set()):
                x.update(repo=r, pin=pin, file=f, namespace=ns[x['line'] - 1] if x['line'] - 1 < len(ns) else '',
                         private=bool(re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:\w+\s+)*private\s', x['statement'])))
                decls.append(x)
    return decls


def classify(decls):
    fed = {}
    for x in decls:
        if x['kw'] in BODYKW and x['name'] != '(anonymous)':
            fed.setdefault(x['name'].split('.')[-1], set()).add(x['repo'])
    fednames = {n for n in fed if len(n) > 2}
    for x in decls:
        code = Q.blank_all_comments(x['statement'])
        zs = [n for n, p in ZETA if re.search(p, code)]
        toks = set(t.split('.')[-1] for t in re.findall(r'[A-Za-z_][A-Za-z0-9_₀′\'.]*', code))
        own = x['name'].split('.')[-1]
        prog = sorted(t for t in toks if t in fednames and t != own)
        x['zeta'] = zs
        x['prog'] = prog
        x['subject'] = 'ZETA' if zs else ('PROGRAMME-TYPE' if prog else 'ARITHMETIC-OR-LOGIC')
        nm = x['name'] if not x['namespace'] or x['name'].startswith(x['namespace'] + '.') else x['namespace'] + '.' + x['name']
        x['full'] = nm
    return decls, fednames


def decls():
    t0 = time.time()
    ds, fednames = classify(enumerate_all())
    pub = []
    for x in ds:
        if x['repo'] == PRIV:
            pub.append(dict(repo=PRIV, pin='HEAD', file=x['file'], line=x['line'], kw=x['kw'], subject=x['subject'], private_repo=True))
        else:
            pub.append({k: x[k] for k in ('repo', 'pin', 'file', 'line', 'end_line', 'kw', 'name', 'full', 'namespace', 'private', 'statement', 'zeta', 'prog', 'subject')})
    from collections import Counter
    per = {}
    for x in ds:
        per.setdefault(x['repo'], Counter())[x['subject']] += 1
    res = dict(count=len(ds), b542_count=5293, equal=(len(ds) == 5293), federation_names=len(fednames),
               needles=[n for n, _ in ZETA], subjects=dict(Counter(x['subject'] for x in ds)),
               per_repo={r: dict(c) for r, c in per.items()}, zeta_yields=dict(Counter(n for x in ds for n in x['zeta'])),
               seconds=round(time.time() - t0, 1), decls=pub)
    io.open(os.path.join(D, 'b544_decls.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, ensure_ascii=False) + NL)
    print('  declarations %d (b542: 5293, equal %s) ; subjects %s ; %.0f s' % (len(ds), res['equal'], res['subjects'], res['seconds']))
    print('  ZETA yields %s' % res['zeta_yields'])
    for r in sorted(per, key=lambda k: -per[k]['ZETA']):
        if per[r]['ZETA']:
            print('    %-34s %s' % (r, dict(per[r])))


def module_of(f):
    return f[:-5].replace('/', '.')


def imports_at(repo, pin, f):
    raw = Q.g(repo, 'show', '%s:%s' % (pin, f))
    return [m.group(1) for m in re.finditer(r'^import\s+([A-Za-z0-9_.₀]+)', raw, re.M)]


def closure(repo, pin, mod, files):
    seen, todo = set(), [mod]
    while todo:
        m = todo.pop()
        if m in seen:
            continue
        seen.add(m)
        f = m.replace('.', '/') + '.lean'
        if f in files:
            todo += imports_at(repo, pin, f)
    return seen


PRINT_OUT = re.compile(r"'([^']+)'[ \t]+(does not depend on any axioms|depends on axioms: \[[^\]]*\])")


def probe(repo):
    dj = json.loads(io.open(os.path.join(D, 'b544_decls.json'), encoding='utf-8').read())
    rows = [x for x in dj['decls'] if x['repo'] == repo and x['subject'] == 'ZETA' and x['kw'] in ('theorem', 'lemma')]
    pin = rows[0]['pin'] if rows else 'HEAD'
    out = dict(repo=repo, pin=pin, rows=len(rows), probed_at='HEAD', skipped=[], profiles={}, errors=[])
    if repo == PRIV:
        print('  TECHNE-Core : its ZETA rows are private and are not probed by name here')
        return
    target = rows
    if repo == 'SIDE-kernel':
        changed = set(f for f in Q.g(repo, 'diff', '--name-only', '--diff-filter=MDR', pin, 'HEAD', '--', '*.lean').split(NL) if f)
        cmods = set(module_of(f) for f in changed)
        files = set(Q.g(repo, 'ls-tree', '-r', '--name-only', pin).split(NL))
        target = []
        for x in rows:
            if x['file'].startswith('legacy/'):
                out['skipped'].append(dict(full=x['full'], file=x['file'], line=x['line'], changed=['legacy/ is outside the build: no library target']))
                continue
            cl = closure(repo, pin, module_of(x['file']), files)
            hit = sorted(cl & cmods)
            if hit:
                out['skipped'].append(dict(full=x['full'], file=x['file'], line=x['line'], changed=hit))
            else:
                target.append(x)
        out['changed_modules'] = sorted(cmods)
    target = [x for x in target if not x['private']]
    out['private_skipped'] = [x['full'] for x in rows if x['private']]
    mods = sorted(set(module_of(x['file']) for x in target))
    src = ['import ' + m for m in mods] + [''] + ['#print axioms ' + x['full'] for x in target]
    p = os.path.join(SCR, 'b544_probe_%s.lean' % repo)
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(src) + NL)
    t0 = time.time()
    r = subprocess.run(['lake', 'env', 'lean', p], cwd=os.path.join('D:', os.sep, repo), capture_output=True, text=True, encoding='utf-8', errors='replace')
    out['seconds'] = round(time.time() - t0, 1)
    out['exit'] = r.returncode
    txt = re.sub(r'\n\s+', ' ', (r.stdout + NL + r.stderr).replace(chr(13), ''))
    for m in PRINT_OUT.finditer(txt):
        out['profiles'][m.group(1)] = m.group(2)
    out['errors'] = [l[:300] for l in (r.stdout + NL + r.stderr).split(NL) if 'error' in l.lower()][:40]
    out['head'] = Q.g(repo, 'rev-parse', 'HEAD').strip()
    io.open(os.path.join(D, 'b544_probe_%s.json' % repo), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, ensure_ascii=False, indent=1) + NL)
    io.open(os.path.join(D, 'b544_probe_%s.txt' % repo), 'w', encoding='utf-8', newline=NL).write(
        'b544 -- THE AXIOM PROBE of %s at HEAD %s (pin %s) ; exit %d ; %.1f s\n%s\n---\n%s' % (repo, out['head'], pin, r.returncode, out['seconds'], NL.join(src), r.stdout + r.stderr))
    print('  %s : %d ZETA terminals ; probed %d ; printed %d ; skipped (closure) %d ; private %d ; exit %d ; %.0f s'
          % (repo, len(rows), len(target), len(out['profiles']), len(out['skipped']), len(out['private_skipped']), r.returncode, out['seconds']))


if __name__ == '__main__':
    if sys.argv[1] == 'decls':
        decls()
    elif sys.argv[1] == 'probe':
        probe(sys.argv[2])
