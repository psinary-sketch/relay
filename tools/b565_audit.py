# -*- coding: utf-8 -*-
"""b565_audit.py -- COMPONENT 3: THE AUDIT DRIVER, UNDER (R175)(2).
### `python tools/b565_audit.py clone <name> <url> | info <name> | sorry <name> <root module path>...`.
### Writes D:/audit-b565/<name> (the clone; its builds are the seat's commands) and relay data/b565_audit_<name>_*.txt|json.
### A clone goes into a directory verified absent first; nothing is deleted here.
"""
import io, json, os, re, subprocess, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
AUD = os.path.join('D:' + os.sep, 'audit-b565')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def now():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')


def put(name, L):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


def clone(name, url):
    dst = os.path.join(AUD, name)
    if os.path.exists(dst):
        sys.exit('### %s EXISTS -- REFUSING TO CLONE OVER IT' % dst)
    os.makedirs(AUD, exist_ok=True)
    t0 = now()
    r = subprocess.run(['git', 'clone', '--quiet', url, dst], capture_output=True, text=True, encoding='utf-8', errors='replace')
    head = git(dst, 'rev-parse', 'HEAD').stdout.strip()
    L = ['b565 -- COMPONENT 3: THE CLONE OF %s' % name, '',
         '### url %s' % url, '### into %s (verified absent before the clone)' % dst,
         '### started %s ; exit %d ; stderr %s' % (t0, r.returncode, r.stderr.strip()[:300] or 'NONE'),
         '### ### **HEAD (THE PIN FOR THIS ACT) : %s**' % head,
         '### HEAD`s commit: %s' % git(dst, 'log', '-1', '--format=%H %cI %s').stdout.strip()[:300]]
    put('b565_audit_%s_clone.txt' % name, L)
    json.dump(dict(url=url, dir=dst, head=head, exit=r.returncode, at=t0),
              io.open(os.path.join(D, 'b565_audit_%s_clone.json' % name), 'w', encoding='utf-8', newline=NL), indent=1)


def info(name, sub=''):
    root = os.path.join(AUD, name, *[x for x in sub.split('/') if x])
    L = ['b565 -- COMPONENT 3: %s -- THE PROJECT AT %s' % (name, root), '']
    for f in ('lean-toolchain', 'lakefile.lean', 'lakefile.toml', 'lake-manifest.json'):
        p = os.path.join(root, f)
        if os.path.exists(p):
            t = io.open(p, encoding='utf-8', errors='replace').read()
            L.append('### %s (%d bytes)' % (f, len(t)))
            if f == 'lake-manifest.json':
                j = json.loads(t)
                for pk in j.get('packages', []):
                    L.append('    package %-22s rev %s  %s' % (pk.get('name'), pk.get('rev'), pk.get('url') or pk.get('dir') or ''))
            else:
                L += ['    | ' + x for x in t.split(NL)[:60] if x.strip()]
        else:
            L.append('### %s ABSENT' % f)
    put('b565_audit_%s_info%s.txt' % (name, ('_' + sub.replace('/', '_')) if sub else ''), L)


def strip_comments(t):
    """### Lean block comments NEST (b565 defect (m): a docstring holding `/- ... -/` ended early under a non-greedy regex
    ### and exposed its example`s `axiom` lines). Block comments are removed by depth; newlines inside them are kept."""
    out, i, depth, n = [], 0, 0, len(t)
    while i < n:
        two = t[i:i + 2]
        if two == '/-':
            depth += 1
            i += 2
        elif two == '-/' and depth:
            depth -= 1
            i += 2
        else:
            if not depth or t[i] == NL:
                out.append(t[i])
            i += 1
    return NL.join(l.split('--')[0] for l in ''.join(out).split(NL))


def sorry(name, root_rel, *mods):
    """### the transitive closure of the named modules WITHIN the project (imports resolved to files under root_rel), and the
    ### lexical count of `sorry`, `admit` and `axiom ` declarations in their comment-stripped code."""
    root = os.path.join(AUD, name, *[x for x in root_rel.split('/') if x])
    tag = None
    if mods and mods[0].startswith('tag='):  # an explicit bank tag (b565: the Zeta23 scan is banked as `_sorry_zeta23`)
        tag, mods = mods[0][4:], mods[1:]
    seen, todo = {}, list(mods)
    while todo:
        m = todo.pop()
        if m in seen:
            continue
        p = os.path.join(root, *m.split('.')) + '.lean'
        if not os.path.exists(p):
            seen[m] = None
            continue
        code = strip_comments(io.open(p, encoding='utf-8', errors='replace').read())
        imps = re.findall(r'^\s*(?:public\s+)?import\s+(\S+)', code, re.M)
        seen[m] = dict(file=os.path.relpath(p, os.path.join(AUD, name)).replace(os.sep, '/'),
                       sorry=len(re.findall(r'\bsorry\b', code)), admit=len(re.findall(r'\badmit\b', code)),
                       axioms=re.findall(r'^\s*(?:private\s+|protected\s+)?axiom\s+(\S+)', code, re.M),
                       imports=[i for i in imps if not i.startswith(('Mathlib', 'Lean', 'Std', 'Batteries', 'Aesop', 'Qq', 'Init'))])
        todo += seen[m]['imports']
    local = {k: v for k, v in seen.items() if v}
    L = ['b565 -- COMPONENT 3: %s -- THE TRANSITIVE CLOSURE OF %s WITHIN THE PROJECT, READ FOR sorry, admit AND axiom' % (name, list(mods)), '',
         '### modules in the closure (files found under %s): %d ; imports not found there: %s' % (
             root_rel or '.', len(local), sorted(k for k, v in seen.items() if v is None) or 'NONE')]
    for k in sorted(local):
        v = local[k]
        if v['sorry'] or v['admit'] or v['axioms']:
            L.append('    %-60s sorry %d admit %d axioms %s' % (v['file'], v['sorry'], v['admit'], v['axioms']))
    tot = dict(sorry=sum(v['sorry'] for v in local.values()), admit=sum(v['admit'] for v in local.values()),
               axioms=sorted(a for v in local.values() for a in v['axioms']))
    L.append('### ### **CLOSURE TOTALS : sorry %d ; admit %d ; axiom declarations %s**' % (tot['sorry'], tot['admit'], tot['axioms'] or 'NONE'))
    tag = tag or '_'.join(x.split('.')[-1] for x in mods)[:60]
    put('b565_audit_%s_sorry_%s.txt' % (name, tag), L)
    json.dump(dict(mods=list(mods), closure=local, missing=sorted(k for k, v in seen.items() if v is None), totals=tot),
              io.open(os.path.join(D, 'b565_audit_%s_sorry_%s.json' % (name, tag)), 'w', encoding='utf-8', newline=NL), indent=1)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a and a[0] == 'clone':
        clone(a[1], a[2])
    elif a and a[0] == 'info':
        info(a[1], a[2] if len(a) > 2 else '')
    elif a and a[0] == 'sorry':
        sorry(a[1], a[2], *a[3:])
    else:
        sys.exit(__doc__)
