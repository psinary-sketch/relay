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
### ### **(R251)(3), b641: W-ORD-ROOT-ORDER.** The act root is the last step of an act, after the last declared seal re-run, and no bank
### the root names is written after it; an edit after the root is the next act's. `compute --write` refuses a root that leaves out the
### act's own seal bank (data/<act>_seal_hashes.json) when that bank exists, and banks the root's time (`at`, `at_epoch`); `verify` reads
### a bank the root names whose file was written after that time as DISAGREE -- "written after the root" -- even when its bytes are
### unchanged. A root banked before b641 carries no time and is read as before: b640's root is not recomputed.
### ### **(R254)(2), b644: W-ORD-CHAIN-AT-COMMIT.** `verify` reads every bank a root names at the commit that root recorded, by git, not
### from the working tree. From b644 `compute` banks `commit` -- the relay commit and the PLACE-papers commit it hashed at (each clone's
### HEAD at the computation); a root banked before b644 carries no `commit` and its recorded relay commit is the relay head it read
### (`reads.heads.relay`). A named path is read at that commit when the commit carries it; a bank the act wrote after that commit (the act's
### own banks, hashed in the working tree and committed in the act's commit) is read at the first commit on relay main's first-parent line
### after the recorded commit that carries the path. Each read is compared twice and the agreeing form counted apart: the blob's bytes, and
### the blob's CRLF form (`crlf_form`) -- relay's `* text=auto eol=lf` normalises every commit to LF, so a bank written with CRLF (the
### step-zero banks a shell redirect writes) was hashed in a form no commit holds byte for byte. A later edit to a named shared file
### (data/glossary.txt) is not read; a bank re-written before its first commit still is. The author's answer at b644: the CRLF reads of
### b624-b643 (82 banks) agree, counted apart per act, none recomputed -- "a property of how the banks were written, not of what they say";
### and from b644 every bank is written LF before it is hashed: `compute --write` refuses a named bank holding a CR LF, and `verify` reads a
### CRLF read on any act after b643 (CRLF_LAST) as DISAGREE.
### `verify --worktree` (and a stand-in relay that is not a git clone, as the tests' temporary directories are) reads the working tree as
### before, with the (R251)(3) time rule; READS_AT holds each act's commit and the count of reads per form.
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
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'   # ### b638, (R248)(5): the census at v0.6 (b638), its §1 kernel column in the same place (b634: v0.5)
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


ORDER_SLACK = 2.0   # ### seconds: a bank's mtime this far past the root's time still reads as written before it (filesystem rounding)


CRLF_LAST = 643   # ### (R254)(2), the author's answer at b644: a CRLF read is lawful on b624-b643 alone


def _rel(b):
    b = b.replace('\\', '/')
    return b[b.index('data/'):] if 'data/' in b else 'data/' + os.path.basename(b)


def seal_bank_unnamed(act, banks):
    """### (R251)(3): the act's own seal bank, when it exists, must be among the banks the root names -- the root follows the last seal re-run."""
    sb = 'data/%s_seal_hashes.json' % act
    named = set(b.replace('\\', '/')[b.replace('\\', '/').index('data/'):] if 'data/' in b.replace('\\', '/') else 'data/' + os.path.basename(b)
                for b in banks)
    return os.path.exists(os.path.join(ROOT, *sb.split('/'))) and sb not in named


def compute(act, banks, write=False):
    import time
    if write and seal_bank_unnamed(act, banks):
        raise SystemExit('### data/%s_seal_hashes.json EXISTS AND THE ROOT DOES NOT NAME IT -- W-ORD-ROOT-ORDER: NO ROOT' % act)
    crlf = [b for b in banks if os.path.exists(os.path.join(ROOT, *_rel(b).split('/'))) and
            b'\r\n' in open(os.path.join(ROOT, *_rel(b).split('/')), 'rb').read()]
    if write and crlf:
        raise SystemExit('### %s HOLD CR LF -- (R254)(2), the author`s answer at b644: every bank is written LF before it is hashed: NO ROOT'
                         % ', '.join(_rel(b) for b in crlf))
    prev, prev_act = last_root()
    at_epoch = time.time()
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
        j = dict(act=act, root=root, previous=prev, previous_act=prev_act, items=lines, reads=reads, lsr=LSR,
                 at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(at_epoch)), at_epoch=at_epoch,
                 commit={'relay': g(ROOT, 'rev-parse', 'HEAD').strip(), 'PLACE-papers': g(PP, 'rev-parse', 'HEAD').strip()})
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


READS_AT = {}


def is_clone():
    """### (R254)(2): True when ROOT is a git clone's top (relay); a stand-in directory is read from its working tree."""
    return os.path.exists(os.path.join(ROOT, '.git'))


def crlf_form(b):
    """### the blob's bytes with every line feed written CR LF, for a blob holding no CR: the form a bank written with CRLF was hashed in,
    ### which relay's `* text=auto eol=lf` (.gitattributes, b372) normalises to LF in every commit; None when the blob holds a CR."""
    return None if b is None or b'\r' in b else b.replace(b'\n', b'\r\n')


def _batch(specs):
    """### one `git cat-file --batch` over '<commit>:<path>' specs: {spec: bytes or None}."""
    if not specs:
        return {}
    a = ['git', '-C', ROOT, 'cat-file', '--batch']
    raw = subprocess.run(a, input=''.join(s + NL for s in specs).encode('utf-8'), capture_output=True).stdout
    out, i = {}, 0
    for s in specs:
        j = raw.index(b'\n', i)
        head = raw[i:j].split()
        if len(head) == 3 and head[1] == b'blob':
            n = int(head[2])
            out[s] = raw[j + 1:j + 1 + n]
            i = j + 1 + n + 1
        else:
            out[s] = None
            i = j + 1
    return out


def at_commit(commit, paths):
    """### (R254)(2): {path: (the commit read, blob bytes, the blob's CRLF form)} -- each path at `commit` when it carries it, else at the
    ### first commit on relay main's first-parent line after it that carries the path; (None, None, None) when none does."""
    have = set(x for x in g(ROOT, 'ls-tree', '-r', '--name-only', '--full-tree', commit, '--', 'data').split(NL) if x)
    where = dict((p, commit) for p in paths if p in have)
    rest = [p for p in paths if p not in have]
    if rest:
        cur = None
        for l in g(ROOT, 'log', '--first-parent', '--reverse', '--format=#%H', '--name-only', '%s..main' % commit, '--', *rest).split(NL):
            if l.startswith('#'):
                cur = l[1:].strip()
            elif l.strip() in rest and l.strip() not in where and cur:
                where[l.strip()] = cur
    specs = ['%s:%s' % (where[p], p) for p in paths if p in where]
    blob = _batch(specs)
    return dict((p, (where[p], blob.get('%s:%s' % (where[p], p)), crlf_form(blob.get('%s:%s' % (where[p], p))))
                 if p in where else (None, None, None)) for p in paths)


def verify(remote=ls_remote, worktree=None):
    """### every act of data/act_roots.txt recomputed: [(act, verdict, reasons)]; (R254)(2): the banks read at each root's recorded commit
    ### (worktree=None reads at commit in a clone and the working tree in a stand-in; worktree=True reads the working tree)."""
    out = []
    if worktree is None:
        worktree = not is_clone()
    READS_AT.clear()
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
        at_epoch = j.get('at_epoch')
        named = [it.split()[0] for it in j['items'] if it.split()[0].startswith('data/')]
        if not worktree:
            commit = (j.get('commit') or {}).get('relay') or ((j.get('reads') or {}).get('heads') or {}).get('relay', '')
            reads_at = at_commit(commit, named) if commit else dict((p, (None, None, None)) for p in named)
            READS_AT[act] = dict(commit=commit, blob=0, crlf=0, later=0, unread=0)
        for it in j['items']:
            parts = it.split()
            if parts[0].startswith('data/') and not worktree:
                c, b, co = reads_at[parts[0]]
                hb = hashlib.sha256(b).hexdigest() if b is not None else None
                hc = hashlib.sha256(co).hexdigest() if co is not None else None
                if c is None:
                    READS_AT[act]['unread'] += 1
                    why.append('bank %s carried by no commit from %s on' % (parts[0], commit[:12]))
                elif parts[1] not in (hb, hc):
                    why.append('bank %s changed (read at %s)' % (parts[0], c[:12]))
                else:
                    READS_AT[act]['blob' if parts[1] == hb else 'crlf'] += 1
                    READS_AT[act]['later'] += c != commit
                    if parts[1] != hb and int(re.sub(r'\D', '', act) or 0) > CRLF_LAST:
                        why.append('bank %s agrees in its CRLF form alone, on an act after b%d (every bank written LF from b644)' % (
                            parts[0], CRLF_LAST))
            elif parts[0].startswith('data/'):
                p = os.path.join(ROOT, *parts[0].split('/'))
                if not os.path.exists(p) or sha256_file(p) != parts[1]:
                    why.append('bank %s changed' % parts[0])
                elif at_epoch is not None and os.path.getmtime(p) > at_epoch + ORDER_SLACK:
                    why.append('bank %s written after the root (W-ORD-ROOT-ORDER: an edit after the root is the next act`s)' % parts[0])
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
        res = verify(worktree=True if '--worktree' in argv else None)
        for act, v, why in res:
            ra = READS_AT.get(act)
            at = (' [at %s: blob %d, crlf %d, of them at a later commit %d]' % (ra['commit'][:12], ra['blob'], ra['crlf'], ra['later'])
                  if ra else ' [the working tree]')
            print('  %s %s%s %s' % (act, v, at, '; '.join(why)))
        print('### ### **ACTS %d ; AGREE %d ; DISAGREE %d.**' % (len(res), sum(v == 'AGREE' for _a, v, _w in res), sum(v != 'AGREE' for _a, v, _w in res)))
        return 0 if res and all(v == 'AGREE' for _a, v, _w in res) else 1
    print('usage: act_root.py compute <act> <bank> ... [--write] | verify [--worktree]')
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
