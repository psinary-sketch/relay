# -*- coding: utf-8 -*-
"""act_root.py -- THE ACT ROOT, W-ORD-ACT-ROOT (OPEN_TRAILS :12210), written at b624 under the author's ruling (R234)(3).

### ### **WHAT IT IS.** An act root is the sha256 over one sorted line per item --
###   "<repository> <head SHA>"        for relay, PLACE-papers, SIDE-global-section and every kernel the census names;
###   "<kernel> <tag> <peeled SHA>"    for every tag the REGISTRY cites (a kernel the census names, a tag its clone carries);
###   "<bank path> <sha256>"           for every data/ bank the act wrote and names --
### followed by the previous act's root, so the roots chain; the chain starts at b624 with the previous root printed as the
### empty string's sha256, so the form is uniform from its start. The payload hashed is the sorted item lines and then the
### previous root, each line ended by a line feed.
### ### `compute <act> <bank> ...` prints the item lines and the root; with `--write` it appends "<act> <root> <previous>" to
### data/act_roots.txt and banks data/<act>_act_root.json (the items, the reads) and data/<act>_act_root.txt (the lines).
### The repository heads are read from the clones (main) and confirmed by one `git ls-remote origin` per repository; a
### head the remote does not hold refuses the root. The cited tags' peeled SHAs are read in the clone and back at the remote.
### ### `verify` recomputes every act of data/act_roots.txt from its banked json and the reads now, one ls-remote per
### repository: the chain (each previous root the line before's root), the root over the banked items, every bank's sha256
### now, every tag's peel at its remote now, every head an ancestor of (or equal to) the remote's main now; it prints AGREE
### or DISAGREE per act. It writes nothing. The deposit description carrying the root is a separate (R110) item.
### ### **(R235)(3), b625: THE REPOSITORY LIST WIDENED.** From b625 the repositories are relay, PLACE-papers and the union of the
### census's kernel column, REGISTRY's kernel rows (a table row whose first or second cell is a kernel's name alone) and every kernel
### a page pins (the kernel each generated page's pin sentence names). The chain takes appends and no edits: b624's line stands as
### written; an act whose repositories gain on the previous act's carries "list widened: +<kernel> ..." after its three fields, one
### name per kernel gained, sorted. `verify` reads the three fields of every line and checks a note against the heads the two acts'
### banks name.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'   # ### b634, (R244)(4): the census at v0.5 (b633), its §1 kernel column in the same place
ROOTS = os.path.join(D, 'act_roots.txt')
EMPTY = hashlib.sha256(b'').hexdigest()

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


_REMOTE = {}
LSR = {}


def ls_remote(path):
    """### one `git ls-remote origin` per repository per process, retried once alone when it fails: {ref: sha}"""
    if path not in _REMOTE:
        LSR[path] = LSR.get(path, 0) + 1
        out = g(path, 'ls-remote', 'origin')
        if 'refs/heads/' not in out:
            LSR[path] += 1
            out = g(path, 'ls-remote', 'origin')
        _REMOTE[path] = dict((l.split('\t')[1].strip(), l.split('\t')[0].strip()) for l in out.split(NL) if '\t' in l)
    return _REMOTE[path]


def path_of(repo):
    return {'relay': ROOT.replace('\\', '/'), 'PLACE-papers': PP}.get(repo, 'D:/' + repo)


def census_kernels(rev='HEAD'):
    """### the kernels the census names in its kernel column (the body table, rows R01 on), read at PLACE-papers `rev`."""
    t = g(PP, 'show', '%s:%s' % (rev, CENSUS))
    out, seen_table = set(), False
    for l in t.split(NL):
        if re.match(r'^\| R\d\d \|', l):
            seen_table = True
            cells = [c.strip() for c in l.split('|')]
            if len(cells) > 7 and not re.match(r'^:\d+$', cells[2]):
                out |= set(re.findall(r'\bSIDE-[a-z0-9]+(?:-[a-z0-9]+)*', cells[7]))
        elif seen_table and not l.strip():
            break
    return sorted(out)


KERNEL = r'SIDE-[a-z0-9]+(?:-[a-z0-9]+)*'
PAGES = ('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md')


def registry_kernels(rev='HEAD'):
    """### REGISTRY's kernel rows: every table row whose first or second cell is a kernel's name alone (backticks and bold stripped)."""
    t = g(PP, 'show', '%s:REGISTRY.md' % rev)
    out = set()
    for l in t.split(NL):
        if l.startswith('|'):
            cells = [c.strip().strip('`*').strip() for c in l.split('|')]
            out |= set(c for c in cells[1:3] if re.fullmatch(KERNEL, c))
    return sorted(out)


def page_kernels(rev='HEAD'):
    """### every kernel a page pins: the kernel each generated page's pin sentence ("It is generated at <kernel> ...") names."""
    out = set()
    for p in PAGES:
        out |= set(re.findall(r'It is generated at (%s)\b' % KERNEL, g(PP, 'show', '%s:%s' % (rev, p))))
    return sorted(out)


def repositories(rev='HEAD'):
    """### (R235)(3), from b625: relay, PLACE-papers and the union of the census's kernel column, REGISTRY's kernel rows and every
    ### kernel a page pins."""
    return ['relay', 'PLACE-papers'] + sorted(set(census_kernels(rev)) | set(registry_kernels(rev)) | set(page_kernels(rev)))


def widened(heads, prev_act):
    """### the note an act's line carries when its repositories gain on the previous act's banked heads: 'list widened: +a +b', or ''."""
    if not prev_act:
        return ''
    jp = os.path.join(D, '%s_act_root.json' % prev_act)
    prev = set(json.load(io.open(jp, encoding='utf-8'))['reads']['heads']) if os.path.exists(jp) else set()
    gained = sorted(set(heads) - prev)
    return ('list widened: ' + ' '.join('+' + k for k in gained)) if gained else ''


VER = r'v\d+(?:\.\d+)*'


def registry_tags(kernels, rev='HEAD'):
    """### every tag the REGISTRY cites: a kernel's name then a version within 40 characters on one line with no table pipe
    ### between (b611's matcher), or a version cell beside the kernel's own cell; kept when the clone carries the tag."""
    t = g(PP, 'show', '%s:REGISTRY.md' % rev)
    got = set()
    for l in t.split(NL):
        for k in kernels:
            name = k[len('SIDE-'):]
            for m in re.finditer(r'(?:SIDE-)?%s\b' % re.escape(name), l):
                for v in re.finditer(r'\b(%s)(?![.\d])' % VER, l[m.end():m.end() + 40].split('|')[0]):
                    got.add((k, v.group(1)))
            if l.startswith('|'):
                cells = [c.strip().strip('`*').strip() for c in l.split('|')]
                for i in range(len(cells) - 1):
                    if cells[i] == k and re.fullmatch(VER, cells[i + 1]):
                        got.add((k, cells[i + 1]))
    return sorted((k, v) for k, v in got if g(path_of(k), 'rev-parse', '-q', '--verify', 'refs/tags/' + v).strip())


def sha256_file(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def root_of(items, previous):
    payload = ''.join(x + NL for x in sorted(items)) + previous + NL
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()


def last_root():
    if not os.path.exists(ROOTS):
        return EMPTY, None
    ls = [l.split()[:3] for l in io.open(ROOTS, encoding='utf-8').read().split(NL) if l.strip()]
    return (ls[-1][1], ls[-1][0]) if ls else (EMPTY, None)


def gather(banks, remote=ls_remote, rev='HEAD'):
    """### the item lines and the reads behind them; refuses (raises) on a head its remote does not hold."""
    repos = repositories(rev)
    items, reads = [], dict(heads={}, tags={}, banks={})
    for r in repos:
        p = path_of(r)
        loc = g(p, 'rev-parse', 'main').strip()
        rem = remote(p).get('refs/heads/main', '')
        if not loc or loc != rem:
            raise SystemExit('### %s: main %s, the remote %s -- NO ROOT' % (r, loc[:12], rem[:12]))
        items.append('%s %s' % (r, loc))
        reads['heads'][r] = loc
    for k, t in registry_tags([r for r in repos if r.startswith('SIDE-')], rev):
        p = path_of(k)
        loc = g(p, 'rev-parse', t + '^{commit}').strip()
        refs = remote(p)
        rp = refs.get('refs/tags/%s^{}' % t) or refs.get('refs/tags/%s' % t)
        items.append('%s %s %s' % (k, t, loc))
        reads['tags']['%s %s' % (k, t)] = dict(peel=loc, remote=rp, equal=rp == loc)
    for b in banks:
        rel = b.replace('\\', '/')
        rel = rel[rel.index('data/'):] if 'data/' in rel else 'data/' + os.path.basename(rel)
        h = sha256_file(os.path.join(ROOT, *rel.split('/')))
        items.append('%s %s' % (rel, h))
        reads['banks'][rel] = h
    return items, reads


def compute(act, banks, write=False):
    prev, prev_act = last_root()
    items, reads = gather(banks)
    root = root_of(items, prev)
    lines = sorted(items)
    for l in lines:
        print('  ' + l)
    note = widened(reads['heads'], prev_act)
    print('### previous root (%s): %s' % (prev_act or 'the empty string', prev))
    print('### ### **ACT ROOT %s : %s** (repositories %d ; tags %d ; banks %d)%s' % (act, root, len(reads['heads']), len(reads['tags']),
                                                                                    len(reads['banks']), (' ; ' + note) if note else ''))
    if write:
        if os.path.exists(ROOTS) and re.search(r'^%s ' % re.escape(act), io.open(ROOTS, encoding='utf-8').read(), re.M):
            raise SystemExit('### %s ALREADY IN data/act_roots.txt -- NOTHING WRITTEN' % act)
        j = dict(act=act, root=root, previous=prev, previous_act=prev_act, items=lines, reads=reads, lsr=LSR)
        for name, body in (('%s_act_root.json' % act, json.dumps(j, indent=1, ensure_ascii=False) + NL),
                           ('%s_act_root.txt' % act, NL.join(['%s -- THE ACT ROOT (tools/act_root.py)' % act, ''] + ['  ' + l for l in lines] +
                                                           ['', 'previous %s' % prev, 'root %s' % root]) + NL)):
            p = os.path.join(D, name)
            open(p + '.tmp', 'wb').write(body.encode('utf-8'))
            os.replace(p + '.tmp', p)
        with open(ROOTS, 'ab') as f:
            f.write(('%s %s %s%s' % (act, root, prev, (' ' + note) if note else '') + NL).encode('utf-8'))
        print('  written: data/act_roots.txt (+1 line), data/%s_act_root.json, data/%s_act_root.txt' % (act, act))
    return root, items, prev


def verify(remote=ls_remote):
    """### every act of data/act_roots.txt recomputed: [(act, verdict, reasons)]"""
    out = []
    if not os.path.exists(ROOTS):
        return out
    rows = [l.split(None, 3) for l in io.open(ROOTS, encoding='utf-8').read().split(NL) if l.strip()]
    prev_expect, prev_heads = EMPTY, None
    for row in rows:
        act, root, prev = row[:3]
        note = row[3].strip() if len(row) > 3 else ''
        why = []
        jp = os.path.join(D, '%s_act_root.json' % act)
        if not os.path.exists(jp):
            out.append((act, 'DISAGREE', ['no bank data/%s_act_root.json' % act]))
            prev_expect = root
            continue
        j = json.load(io.open(jp, encoding='utf-8'))
        if prev != prev_expect:
            why.append('the chain: previous %s, the line before %s' % (prev[:12], prev_expect[:12]))
        if j.get('root') != root or j.get('previous') != prev or root_of(j['items'], prev) != root:
            why.append('the root over the banked items does not recompute')
        heads = set(((j.get('reads') or {}).get('heads') or {}))
        if note or prev_heads is not None:
            gained = sorted(heads - prev_heads) if prev_heads is not None else []
            want = ('list widened: ' + ' '.join('+' + k for k in gained)) if gained else ''
            if note != want:
                why.append('the line`s note %r, the heads gained %r' % (note, want))
        prev_heads = heads
        for it in j['items']:
            parts = it.split()
            if parts[0].startswith('data/'):
                p = os.path.join(ROOT, *parts[0].split('/'))
                if not os.path.exists(p) or sha256_file(p) != parts[1]:
                    why.append('bank %s changed' % parts[0])
            elif len(parts) == 3:
                refs = remote(path_of(parts[0]))
                rp = refs.get('refs/tags/%s^{}' % parts[1]) or refs.get('refs/tags/%s' % parts[1])
                if rp != parts[2]:
                    why.append('tag %s %s at the remote %s' % (parts[0], parts[1], (rp or 'ABSENT')[:12]))
            else:
                p = path_of(parts[0])
                rm = remote(p).get('refs/heads/main', '')
                if not rm or (rm != parts[1] and subprocess.run(['git', '-C', p, 'merge-base', '--is-ancestor', parts[1], rm],
                                                                capture_output=True).returncode != 0):
                    why.append('head %s %s not on the remote main %s' % (parts[0], parts[1][:12], rm[:12]))
        out.append((act, 'AGREE' if not why else 'DISAGREE', why))
        prev_expect = root
    return out


def main(argv):
    if len(argv) >= 2 and argv[0] == 'compute':
        compute(argv[1], [a for a in argv[2:] if a != '--write'], write='--write' in argv)
        return 0
    if argv[:1] == ['verify']:
        res = verify()
        for act, v, why in res:
            print('  %s %s %s' % (act, v, '; '.join(why)))
        print('### ### **ACTS %d ; AGREE %d ; DISAGREE %d.**' % (len(res), sum(v == 'AGREE' for _a, v, _w in res), sum(v != 'AGREE' for _a, v, _w in res)))
        return 0 if res and all(v == 'AGREE' for _a, v, _w in res) else 1
    print('usage: act_root.py compute <act> <bank> ... [--write] | verify')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
