# -*- coding: utf-8 -*-
"""no_sorry_main.py -- THE ARM G-NO-SORRY-MAIN, a standalone tool under (R259)(2)(a), an arm of every suite from b649.

### For every kernel of the corpus -- every SIDE-* repository with a clone on D:\\ (tools/terminal_table.py `kernels()`, the set b647's sorry
### census read) -- at its main as read by ls-remote and by the local clone's HEAD (both printed; equal required, an unequal or unread pair
### FAILS the kernel), every .lean file under every lean_lib of its lakefile is scanned for the token `sorry` outside comments and strings.
### A lean_lib's files: its roots (explicit `roots`, else its own name), every module its `globs` reach (`.submodules`, `.andSubmodules`,
### `X.+`, `X.*`, read as X and every module under it), under its `srcDir`, and every in-repository module those import. A kernel whose
### main carries no lakefile has no lean_lib: every tracked .lean file of its main is scanned, and the kernel is printed NO LAKEFILE. Files
### are read from the main commit's blobs, never the working tree. A quarantine branch is not main and is not scanned.
### Any hit FAILS the arm, printed with kernel, file and line.
###
### Usage:  python tools/no_sorry_main.py [--bank data/<name>.txt] [kernel ...]
### Library: kernels(), lean_code(text), sorry_hits(text), lib_files(read, names), scan_kernel(path, remote=None), run(kernels, remote=None)
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

IDC = r"[\w'!?]"
SORRY = re.compile(r"(?<![\w.'!?])sorry(?![\w'!?])")


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def kernels():
    """every SIDE-* repository with a clone on D:\\ -- tools/terminal_table.py's `kernels()`, the set b647's sorry census read."""
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import terminal_table as T
    return [n for n, _p in T.kernels()[1]]


def lean_code(text):
    """the text with every comment (line `--`, nested block `/- -/`, doc `/-- -/` and `/-! -/`) and every string and char literal blanked to
    spaces, newlines kept, so a position in the result is the same line and column in the source."""
    out = list(text)
    i, n, depth = 0, len(text), 0
    while i < n:
        c = text[i]
        if depth:
            if text.startswith('/-', i):
                depth += 1
                out[i] = out[i + 1] = ' '
                i += 2
                continue
            if text.startswith('-/', i):
                depth -= 1
                out[i] = out[i + 1] = ' '
                i += 2
                continue
            if c != NL:
                out[i] = ' '
            i += 1
            continue
        if text.startswith('/-', i):
            depth = 1
            out[i] = out[i + 1] = ' '
            i += 2
            continue
        if text.startswith('--', i):
            j = text.find(NL, i)
            j = n if j < 0 else j
            for k in range(i, j):
                out[k] = ' '
            i = j
            continue
        m = re.match(r'r(#*)"', text[i:]) if c == 'r' and (i == 0 or not re.match(IDC, text[i - 1])) else None
        if m:
            end = text.find('"' + m.group(1), i + len(m.group(0)))
            end = n if end < 0 else end + 1 + len(m.group(1))
            for k in range(i, end):
                if text[k] != NL:
                    out[k] = ' '
            i = end
            continue
        if c == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 2 if text[j] == '\\' else 1
            for k in range(i, min(j + 1, n)):
                if text[k] != NL:
                    out[k] = ' '
            i = j + 1
            continue
        if c == "'" and (i == 0 or not re.match(IDC, text[i - 1])):
            m = re.match(r"'(?:\\.[^']*|[^'\\])'", text[i:])
            if m:
                for k in range(i, i + len(m.group(0))):
                    out[k] = ' '
                i += len(m.group(0))
                continue
        i += 1
    return ''.join(out)


def sorry_hits(text):
    """[(line, the source line)] for every `sorry` token outside comments and strings."""
    code = lean_code(text)
    src = text.split(NL)
    out = []
    for i, l in enumerate(code.split(NL), 1):
        if SORRY.search(l):
            out.append((i, src[i - 1].strip()))
    return out


def _libs(lk):
    """[(name, roots, globs as module prefixes, srcDir)] from a lakefile's text, lakefile.lean or lakefile.toml."""
    libs = []
    for blk in re.split(r'(?=^\s*lean_lib\s+[«\w]|^\s*\[\[lean_lib\]\])', lk, flags=re.M)[1:]:
        m = re.match(r'\s*lean_lib\s+«?([\w.]+)»?', blk) or re.search(r'^\s*name\s*=\s*"([\w.]+)"', blk, re.M)
        if not m:
            continue
        name = m.group(1)
        rt = re.search(r'roots\s*:?=\s*#?\[([^\]]*)\]', blk)
        roots = [x.strip().lstrip('`').strip('"').strip() for x in rt.group(1).split(',') if x.strip()] if rt else [name]
        gl = []
        gm = re.search(r'globs\s*:?=\s*#?\[([^\]]*)\]', blk)
        if gm:
            for x in gm.group(1).split(','):
                x = x.strip()
                mm = re.match(r'\.(?:submodules|andSubmodules|one)\s+`?([\w.]+)', x) or re.match(r'"([\w.]+?)(?:\.\+|\.\*)?"', x)
                if mm:
                    gl.append(mm.group(1))
        sd = re.search(r'srcDir\s*:?=\s*"([^"]*)"', blk)
        libs.append((name, roots, gl, (sd.group(1).strip('./') if sd else '')))
    return libs


def lib_files(files, read, lk):
    """the .lean files of a main the lakefile's lean_libs build: [path]; `files` the tracked paths, `read(path)` a blob's text."""
    lean = [f for f in files if f.endswith('.lean') and not f.startswith('.lake/')]
    built = set()
    for name, roots, globs, sd in _libs(lk):
        pre = (sd + '/') if sd else ''
        mods = dict((f[len(pre):-5].replace('/', '.'), f) for f in lean if f.startswith(pre))
        todo = [mods[r] for r in roots if r in mods]
        todo += [f for m, f in mods.items() for gp in globs if m == gp or m.startswith(gp + '.')]
        while todo:
            f = todo.pop()
            if f in built:
                continue
            built.add(f)
            for imp in re.findall(r'^\s*import\s+([\w.]+)', read(f) or '', re.M):
                if imp in mods and mods[imp] not in built:
                    todo.append(mods[imp])
    return sorted(built)


def ls_remote(path):
    rc, out = git(path, 'ls-remote', 'origin', 'refs/heads/main')
    if 'refs/heads/main' not in out:
        rc, out = git(path, 'ls-remote', 'origin', 'refs/heads/main')
    return dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)


def scan_kernel(path, remote=None):
    """one kernel: dict(kernel, remote, head, equal, lakefile, files, hits=[(file, line, text)])."""
    refs = (remote or ls_remote)(path)
    rm = refs.get('refs/heads/main', '')
    head = git(path, 'rev-parse', 'HEAD')[1].strip()
    main = git(path, 'rev-parse', 'main')[1].strip()
    files = [x for x in git(path, 'ls-tree', '-r', '--name-only', main)[1].split(NL) if x.strip()] if main else []
    read = lambda f: (lambda r: r[1] if r[0] == 0 else None)(git(path, 'show', '%s:%s' % (main, f)))   # noqa: E731
    lk = (read('lakefile.lean') or '') + NL + (read('lakefile.toml') or '') if main else ''
    has_lk = bool(lk.strip())
    scan = lib_files(files, read, lk) if has_lk else sorted(f for f in files if f.endswith('.lean') and not f.startswith('.lake/'))
    hits = []
    for f in scan:
        for ln, t in sorry_hits(read(f) or ''):
            hits.append((f, ln, t[:200]))
    return dict(kernel=os.path.basename(path.rstrip('/\\')), remote=rm, head=head, main=main, equal=bool(rm) and rm == head == main,
                lakefile=has_lk, files=len(scan), hits=hits)


def run(names, remote=None):
    """[(row)] over the kernels named; the arm passes when every kernel's pair is equal and no hit is found."""
    return [scan_kernel('D:/' + k, remote) for k in names]


def report(rows):
    L = ['no_sorry_main.py -- THE ARM G-NO-SORRY-MAIN ((R259)(2)(a)): `sorry` outside comments and strings in every lean_lib of every '
         'kernel`s main (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### kernel | main at the remote | the clone`s HEAD | equal | lakefile | files scanned | hits']
    for r in rows:
        L.append('  %-34s %s %s %-5s %-11s %4d  %d' % (r['kernel'], (r['remote'] or 'UNREAD')[:12], (r['head'] or '?')[:12],
                                                      'EQUAL' if r['equal'] else '### UNEQUAL', 'lakefile' if r['lakefile'] else 'NO LAKEFILE',
                                                      r['files'], len(r['hits'])))
    hits = [(r['kernel'], f, ln, t) for r in rows for f, ln, t in r['hits']]
    L += ['', '### EVERY HIT, BY KERNEL, FILE AND LINE:'] + (['  %s %s:%d  %s' % h for h in hits] or ['  NONE'])
    bad = [r['kernel'] for r in rows if not r['equal']]
    ok = not hits and not bad
    L += ['', '### ### **KERNELS %d ; FILES SCANNED %d ; HITS %d ; PAIRS UNEQUAL OR UNREAD %d %s ; VERDICT : %s**' % (
        len(rows), sum(r['files'] for r in rows), len(hits), len(bad), bad or '', 'PASS' if ok else 'FAIL')]
    return ok, L


def main(argv):
    bank = argv[argv.index('--bank') + 1] if '--bank' in argv else None
    names = [a for a in argv if not a.startswith('--') and a != bank] or kernels()
    rows = run(names)
    ok, L = report(rows)
    if bank:
        for p, b in ((bank, (NL.join(L) + NL).encode('utf-8')),
                     (os.path.splitext(bank)[0] + '.json', (json.dumps(dict(ok=ok, rows=rows), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
            open(p + '.tmp', 'wb').write(b)
            os.replace(p + '.tmp', p)
    print(NL.join(L[-12:]))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
