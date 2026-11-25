# -*- coding: utf-8 -*-
"""tools/b769_archives.py -- b769, (R379)(4)(d): THE CLUSTER'S SOURCE RECORD, TWO ARCHIVES COMMITTED AS BYTES WITH ONE MANIFEST.

The two archives the ruling names (data/b769_ferry.txt :21, read from the ferry bank at run time, its sha256 checked), handed by the author
at the act's one prompt of (4)(d) (data/b769_put_1.json; the answer: both stand on this host). Found by their names alone, one level under
the data volume's root, so that no folder of the author's own data is typed on a command line or written by the act; the folder is never
printed and never banked. Untrusted data: read by zipfile, nothing of them run or imported, the tool run with python -I from the relay.

  dry <scratch>     read each archive's list of members; where an archive carries its own list of digests (a member named as a digest
                    list, its lines or its JSON read for a sha256 beside a member's name), each listed member read against it; the members
                    unpacked to a new empty folder under <scratch> (names refused that climb out of it) for the address scan and nothing
                    else, the scan's four targets (tools/b769_address_scan.py: the previous address, the author's name, the previous
                    user.name, the ORCID), each held in memory and counted, never printed, over each member's name and bytes (read as
                    UTF-8, and as UTF-16 where its bytes carry NULs; a member that is itself an archive read one level in) -- the account
                    counted beside as a reading; the manifest composed in memory. Planted controls first: a digest list with one hash
                    altered reads one unequal; a text carrying each target once counts one each and a clean text none; a name climbing
                    out of the folder refused; the manifest read back equal to its rows. Printed: counts alone -- no member's name, no
                    line of a member, no folder.
  write <scratch>   the same, then, where each condition holds ([B1]'s: both found, each check clean, every target 0), the two archives
                    copied as bytes into the papers` repository under clusters/lean-archive-november-2026/ beside MANIFEST.txt (each
                    member's archive, name, size and sha256), each copy read back by sha256; banks data/b769_archives.txt and .json with
                    the manifest's path, its sha256 and the counts alone ((4)(d): nothing of the archives in the relay beyond those).
                    Where a condition fails nothing is copied and nothing written in the papers` repository; the bank names which, for
                    [B2].
No git write.
"""
import glob
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import zipfile

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'standing'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b769_worklist as K   # noqa: E402

ACT, NL = 'b769', '\n'
PP = K.PP
FERRY = os.path.join(D, 'b769_ferry.txt')
FERRY_SHA = '20ab92c5b57a9b5c'
FERRY_LINE = 21                       # ### (R379)(4)(d)
CLUSTER = 'clusters/lean-archive-november-2026'
MANIFEST = CLUSTER + '/MANIFEST.txt'
PPHEAD = 'd4808187'                   # ### the papers` repository's last commit of the act before this write ([X4] and [M5], step 25)
VOLUME = 'D:/'                        # ### the data volume; the archives found one level under its root by their names alone
GIT_FILE_LIMIT = 100 * 1024 * 1024    # ### the remote's refusal size for one file: an archive above it could not be pushed at the close
UNPACK_CAP = 4 * 1024 * 1024 * 1024   # ### the members' total size unpacked, at most
RATIO_CAP = 200                       # ### a member's size over its compressed size, at most
DIGEST_NAME = re.compile(r'(?i)(^|/)(sha256sums?|sha256|checksums?|manifest|digests?|hashes)([._-][^/]*)?$|\.sha256$')
HEX64 = re.compile(r'(?<![0-9a-fA-F])[0-9a-fA-F]{64}(?![0-9a-fA-F])')


def die(w):
    sys.exit('### %s -- NOTHING WRITTEN' % w)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def git(repo, *a):
    return subprocess.run(['git', '-C', repo, *a], capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def put(path, data):
    with open(path + '.tmp', 'wb') as f:
        f.write(data)
    os.replace(path + '.tmp', path)


# ================================================================================ THE NAMES AND THE TARGETS
def ruled():
    """the two archives' names, the cluster's folder and the writer's count of the bundle, from the ferry bank's :21."""
    with open(FERRY, 'rb') as f:
        b = f.read()
    if sha(b)[:16] != FERRY_SHA:
        die('THE FERRY BANK IS NOT ITS STEP-ZERO BYTES')
    line = b.decode('utf-8').split(NL)[FERRY_LINE - 1]
    names = re.findall(r'\b[A-Z0-9_]+\.zip\b', line)
    m = re.search(r'of (\d+) files by its writer`?\'?s count', line)
    if len(names) != 2 or CLUSTER + '/' not in line or not m:
        die('THE RULING`S NAMES NOT READ AT data/b769_ferry.txt :%d' % FERRY_LINE)
    return names, int(m.group(1))


def targets():
    """the address scan's four targets, held in memory, never printed; and the account, counted beside."""
    import b769_address_scan as SC
    prev = git(RELAY, 'log', '-1', '--format=%an', SC.USERNAME_REF).strip()   # ### as previous_username() reads it, with no call to the web
    if len(prev) < 2:
        die('THE PREVIOUS user.name NOT READ')
    import project_set as PS
    return dict(address=SC.previous_address(), name=SC.author_name(), previous_name=prev, orcid=SC.author_orcid()), PS.owner()


def tcount(text, needle):
    return text.lower().count(needle.lower()) if needle else 0


def texts_of(name, data):
    out = [name, data.decode('utf-8', 'replace')]
    if b'\x00' in data[:4096]:
        out.append(data.decode('utf-16-le', 'ignore'))
    return out


def scan(name, data, TG, acct):
    """{target: count} over a member's name and bytes; an inner archive read one level in (its names and members)."""
    c = dict((k, 0) for k in TG)
    c['account'] = 0
    inner = 0
    parts = texts_of(name, data)
    if data[:4] == b'PK\x03\x04':
        try:
            with zipfile.ZipFile(io.BytesIO(data)) as z:
                for i in z.infolist():
                    if not i.is_dir():
                        inner += 1
                        parts += texts_of(i.filename, z.read(i))
        except (zipfile.BadZipFile, RuntimeError, NotImplementedError):
            pass
    for t in parts:
        for k, v in TG.items():
            c[k] += tcount(t, v)
        c['account'] += tcount(t, acct)
    return c, inner


# ================================================================================ THE ARCHIVES
def find(names):
    """each archive's one path one level under the volume's root; refuses unless each stands once and both in one folder."""
    hits = [sorted(glob.glob(os.path.join(VOLUME, '*', n))) for n in names]
    if any(len(h) != 1 for h in hits):
        die('THE ARCHIVES NOT FOUND ONCE EACH (%s)' % ', '.join(str(len(h)) for h in hits))
    if len(set(os.path.dirname(h[0]) for h in hits)) != 1:
        die('THE TWO ARCHIVES NOT IN ONE FOLDER')
    return [h[0] for h in hits]


def safe_parts(name):
    """the member's path parts where it stays inside the folder; None where it climbs out (absolute, a drive, '..', empty parts)."""
    n = name.replace('\\', '/')
    parts = n.split('/')
    if n.startswith('/') or ':' in n or any(p in ('', '.', '..') for p in parts):
        return None
    return parts


def digest_lists(z, members):
    """{member path: listed sha256} read from every member named as a digest list; and the lists' count."""
    paths = [i.filename for i in members]
    lists = [i for i in members if DIGEST_NAME.search(i.filename)]
    out, n_lines = {}, 0

    def match(listed):
        listed = listed.strip().strip('*').replace('\\', '/').lstrip('./')
        hit = [p for p in paths if p == listed or p.endswith('/' + listed) or (listed.endswith('/' + p))]
        return hit[0] if len(hit) == 1 else None

    def walk(o):
        if isinstance(o, dict):
            hx = [v for v in o.values() if isinstance(v, str) and HEX64.fullmatch(v.strip())]
            nm = [v for v in o.values() if isinstance(v, str) and match(v)]
            if len(hx) == 1 and len(nm) == 1:
                out[match(nm[0])] = hx[0].strip().lower()
            for k, v in o.items():
                if isinstance(v, str) and HEX64.fullmatch(v.strip()) and match(k):
                    out[match(k)] = v.strip().lower()
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)

    for i in lists:
        raw = z.read(i).decode('utf-8', 'replace')
        try:
            walk(json.loads(raw))
            continue
        except ValueError:
            pass
        for l in raw.replace('\r', '').split(NL):
            h = HEX64.findall(l)
            if len(h) != 1:
                continue
            n_lines += 1
            rest = l.replace(h[0], ' ')
            cand = [p for p in paths if p in rest or p.split('/')[-1] in rest]
            best = sorted(cand, key=len, reverse=True)
            if best and (len(best) == 1 or len(best[0]) > len(best[1])):
                out[best[0]] = h[0].lower()
    return out, len(lists), n_lines


def read_archive(path, k, base, TG, acct):
    with open(path, 'rb') as f:
        whole = f.read()
    z = zipfile.ZipFile(io.BytesIO(whole))
    members = [i for i in z.infolist() if not i.is_dir()]
    unsafe = [i.filename for i in members if safe_parts(i.filename) is None]
    total = sum(i.file_size for i in members)
    ratio = max([i.file_size / max(1, i.compress_size) for i in members] or [0])
    rows, scanned, inner, binary = [], dict((x, 0) for x in list(TG) + ['account']), 0, 0
    dl, n_lists, n_lines = digest_lists(z, members)
    eq = neq = 0
    folder = os.path.join(base, 'a%d' % k)
    if not unsafe and total <= UNPACK_CAP and ratio <= RATIO_CAP:
        os.makedirs(folder)
        real = os.path.realpath(folder)
        for i in members:
            data = z.read(i)   # ### the CRC checked by zipfile
            dest = os.path.join(folder, *safe_parts(i.filename))
            if not os.path.realpath(dest).startswith(real + os.sep):
                die('A MEMBER`S PATH LEAVES ITS FOLDER')
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            with open(dest, 'wb') as f:
                f.write(data)
            rows.append((i.filename, i.file_size, sha(data)))
        for name, size, h in rows:   # ### the scan reads the unpacked bytes back from the scratch folder
            with open(os.path.join(folder, *safe_parts(name)), 'rb') as f:
                data = f.read()
            try:
                data.decode('utf-8')
            except UnicodeDecodeError:
                binary += 1
            c, n_in = scan(name, data, TG, acct)
            inner += n_in
            for x in c:
                scanned[x] += c[x]
            if name in dl:
                if dl[name] == h:
                    eq += 1
                else:
                    neq += 1
    listed_missing = sum(1 for p in dl if p not in [r[0] for r in rows]) if rows else len(dl)
    return dict(path=path, name=os.path.basename(path), size=len(whole), sha=sha(whole), members=len(members), rows=rows, unsafe=len(unsafe),
                total=total, ratio=ratio, lists=n_lists, list_lines=n_lines, listed=len(dl), equal=eq, unequal=neq, listed_missing=listed_missing,
                unlisted=sum(1 for r in rows if r[0] not in dl and not DIGEST_NAME.search(r[0])) if dl else None,
                scanned=scanned, inner=inner, binary=binary)


def manifest_text(A, date):
    L = ['# MANIFEST of %s/ (b769, (R379)(4)(d))' % CLUSTER,
         '# written by the relay`s tools/b769_archives.py on %s: the two archives beside this file, committed as bytes; one row a member,' % date,
         '# tab-separated: the archive, the member`s name, its size in bytes, its sha256. Workspace grade throughout: nothing of them compiled,',
         '# run or reproduced by the programme`s tools. Private.']
    for a in A:
        L.append('# the archive %s: %d bytes, sha256 %s, members %d' % (a['name'], a['size'], a['sha'], len(a['rows'])))
    L.append('archive\tmember\tsize\tsha256')
    for a in A:
        L += ['%s\t%s\t%d\t%s' % (a['name'], n, s, h) for n, s, h in a['rows']]
    return NL.join(L) + NL


def manifest_rows(text):
    out = []
    for l in text.split(NL):
        if l and not l.startswith('#') and l != 'archive\tmember\tsize\tsha256':
            a, n, s, h = l.split('\t')
            out.append((a, n, int(s), h))
    return out


# ================================================================================ THE PLANTED CONTROLS
def controls(TG, acct):
    out = []
    # ### a digest list with one hash altered reads one unequal, read in memory alone
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w') as z:
        z.writestr('w/a.txt', b'alpha\n')
        z.writestr('w/b.txt', b'beta\n')
        z.writestr('w/SHA256SUMS', ('%s  a.txt\n%s  b.txt\n' % (sha(b'alpha\n'), sha(b'BETA\n'))).encode())
    z = zipfile.ZipFile(io.BytesIO(buf.getvalue()))
    mem = [i for i in z.infolist() if not i.is_dir()]
    dl, nl_, _l = digest_lists(z, mem)
    got = [(p, dl.get(p) == sha(z.read(p))) for p in ('w/a.txt', 'w/b.txt')]
    out.append(('PLANTED: a digest list with one hash altered reads one equal and one unequal (%s)' % got,
                got == [('w/a.txt', True), ('w/b.txt', False)] and nl_ == 1))
    # ### each target planted alone in a text of its own counts at least one on its own kind (two targets may be one string, so each
    # ### planted apart), and a clean text counts none
    AL = dict(TG, account=acct)
    c = dict((k, scan('planted.txt', ('x ; %s ; y' % v).encode('utf-8'), TG, acct)[0][k]) for k, v in AL.items())
    c0, _n0 = scan('clean.txt', b'no identifier here', TG, acct)
    out.append(('PLANTED: each target alone in a text of its own counts on its kind %s; a clean text %s' % (
        ' '.join('%s %d' % (k, c[k]) for k in sorted(c)), ' '.join('%s %d' % (k, c0[k]) for k in sorted(c0))),
        all(v >= 1 for v in c.values()) and not any(c0.values())))
    # ### names climbing out of the folder refused
    bad = ['../x', '/x', 'C:/x', 'a/../b', 'a//b']
    out.append(('PLANTED: names climbing out of the folder refused (%d of %d), a plain name kept' % (
        sum(1 for b in bad if safe_parts(b) is None), len(bad)), all(safe_parts(b) is None for b in bad) and safe_parts('a/b.txt') == ['a', 'b.txt']))
    return out


# ================================================================================ THE RUN
def run(mode, scratch):
    names, writer_count = ruled()
    if not os.path.isdir(scratch):
        die('THE SCRATCH FOLDER DOES NOT STAND')
    base = os.path.join(scratch, 'b769_unpacked_%s' % time.strftime('%H%M%S', time.gmtime()))
    if os.path.exists(base):
        die('THE UNPACK FOLDER STANDS ALREADY')
    os.makedirs(base)
    TG, acct = targets()
    ctl = controls(TG, acct)
    paths = find(names)
    A = [read_archive(p, k, base, TG, acct) for k, p in enumerate(paths, 1)]
    date = time.strftime('%Y-%m-%d', time.gmtime())
    man = manifest_text(A, date)
    man_rows = manifest_rows(man)
    want_rows = [(a['name'], n, s, h) for a in A for n, s, h in a['rows']]
    ctl.append(('the manifest read back equal to its rows (%d rows)' % len(man_rows), man_rows == want_rows and len(man_rows) == sum(a['members'] for a in A)))
    pp_head = git(PP, 'rev-parse', 'HEAD').strip()
    tg_sum = dict((k, sum(a['scanned'][k] for a in A)) for k in list(TG) + ['account'])
    cond = [('the two archives the ruling names found once each, in one folder on this host (the folder not printed)', len(A) == 2),
            ('each archive under the remote`s size for one file, %d MB (its size not banked: (4)(d) keeps the relay to the manifest`s sha256 '
             'and counts)' % (GIT_FILE_LIMIT // 1048576), all(a['size'] < GIT_FILE_LIMIT for a in A)),
            ('no member`s name climbing out of its folder (%s), the members unpacked within %d GB and a ratio of %d' % (
                ', '.join(str(a['unsafe']) for a in A), UNPACK_CAP // 1073741824, RATIO_CAP),
             all(a['unsafe'] == 0 and a['total'] <= UNPACK_CAP and a['ratio'] <= RATIO_CAP for a in A)),
            ('each member unpacked and read: %s' % ', '.join('%d of %d' % (len(a['rows']), a['members']) for a in A),
             all(len(a['rows']) == a['members'] > 0 for a in A)),
            ('each listed member equal to its archive`s own list of digests where one is carried: %s' % ' ; '.join(
                '%s: lists %d, listed %d, equal %d, unequal %d, listed and absent %d' % (
                    'the bundle' if k == 0 else 'the supplement', a['lists'], a['listed'], a['equal'], a['unequal'], a['listed_missing'])
                for k, a in enumerate(A)),
             all(a['unequal'] == 0 and a['listed_missing'] == 0 for a in A)),
            ('the address scan over the members unpacked to scratch, 0 on each target: %s' % ' '.join(
                '%s %d' % (k, tg_sum[k]) for k in TG), not any(tg_sum[k] for k in TG)),
            ('the papers` repository`s HEAD the act`s last commit there before this write %s (%s), the cluster`s folder absent at HEAD and on disk' % (
                PPHEAD, pp_head[:8]),
             pp_head.startswith(PPHEAD) and not git(PP, 'ls-tree', 'HEAD', CLUSTER).strip() and not os.path.exists(os.path.join(PP, *CLUSTER.split('/'))))]
    ok = all(o for _w, o in ctl + cond)
    P = ['%s -- (R379)(4)(d): THE CLUSTER`S SOURCE RECORD, TWO ARCHIVES WITH ONE MANIFEST (%s)' % (ACT, utc()), '',
         '### tools/b769_archives.py %s; the names from data/b769_ferry.txt :%d (sha256 %s); the papers` repository at HEAD %s; nothing of the' % (
             mode, FERRY_LINE, FERRY_SHA, pp_head[:8]),
         '### archives run; no member`s name, no line of a member and no folder printed; the counts alone banked in the relay.', '',
         '## THE PLANTED CONTROLS']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in ctl]
    P += ['', '## THE CONDITIONS OF [B1]']
    P += ['  %-150s %s' % (w, 'AS WANTED' if o else 'NOT AS WANTED') for w, o in cond]
    P += ['', '## THE READINGS',
          '  members: the bundle %d (its writer`s count %d), the supplement %d ; together %d' % (A[0]['members'], writer_count, A[1]['members'],
                                                                                           A[0]['members'] + A[1]['members']),
          '  members not valid UTF-8 (the scan reads their bytes as UTF-8 and UTF-16, a compressed stream inside them unread): %s' % (
              ', '.join(str(a['binary']) for a in A)),
          '  members that are archives, read one level in: their members %s' % ', '.join(str(a['inner']) for a in A),
          '  members outside a carried list of digests: %s' % ', '.join('none carried' if a['unlisted'] is None else str(a['unlisted']) for a in A),
          '  the account counted beside, not a target of the scan: %d' % tg_sum['account'],
          '  the manifest: %s, %d rows, sha256 %s' % (MANIFEST, len(man_rows), sha(man.encode('utf-8'))[:16])]
    verdict = ('WRITTEN' if mode == 'write' else 'DRY, NOTHING WRITTEN') if ok else 'HELD'
    P += ['', '### ### **THE SOURCE RECORD: MEMBERS %d ; LISTED %d, EQUAL %d, UNEQUAL %d ; THE SCAN %d ON THE TARGETS ; CONTROLS %d OF %d AND CONDITIONS '
          '%d OF %d AS WANTED ; %s.**' % (len(man_rows), sum(a['listed'] for a in A), sum(a['equal'] for a in A), sum(a['unequal'] for a in A),
                                          sum(tg_sum[k] for k in TG), sum(1 for _w, o in ctl if o), len(ctl), sum(1 for _w, o in cond if o),
                                          len(cond), verdict)]
    print(NL.join(P))
    if mode == 'dry':
        return 0 if ok else 1
    lb, lj = os.path.join(D, 'b769_archives.txt'), os.path.join(D, 'b769_archives.json')
    if os.path.exists(lb) or os.path.exists(lj):
        die('THE BANK STANDS ALREADY')
    bank = dict(at=utc(), act=ACT, mode=mode, pp_head=pp_head, verdict=verdict,
                members=dict(bundle=A[0]['members'], supplement=A[1]['members'], together=len(man_rows), writer_count=writer_count),
                digests=[dict(lists=a['lists'], listed=a['listed'], equal=a['equal'], unequal=a['unequal'], listed_missing=a['listed_missing']) for a in A],
                scan=dict((k, tg_sum[k]) for k in TG), account_beside=tg_sum['account'], binary=[a['binary'] for a in A], inner=[a['inner'] for a in A],
                controls=[[w, o] for w, o in ctl], conditions=[[w, o] for w, o in cond])
    if ok:
        folder = os.path.join(PP, *CLUSTER.split('/'))
        os.makedirs(folder)
        for a in A:
            with open(a['path'], 'rb') as f:
                data = f.read()
            dest = os.path.join(folder, a['name'])
            put(dest, data)
            with open(dest, 'rb') as f:
                if sha(f.read()) != a['sha']:
                    die('A COPY IS NOT ITS ARCHIVE`S BYTES')
        put(os.path.join(PP, *MANIFEST.split('/')), man.encode('utf-8'))
        with open(os.path.join(PP, *MANIFEST.split('/')), 'rb') as f:
            if f.read() != man.encode('utf-8'):
                die('THE MANIFEST WRITTEN IS NOT ITS COMPOSITION')
        bank['manifest'] = dict(path=MANIFEST, rows=len(man_rows), sha256=sha(man.encode('utf-8'))[:16])
    put(lb, (NL.join(P) + NL).encode('utf-8'))
    put(lj, (json.dumps(bank, ensure_ascii=False, indent=1) + NL).encode('utf-8'))
    print('written %s ; data/b769_archives.txt and .json' % ('the two archives and %s in the papers` repository' % MANIFEST if ok else 'nothing in the papers` repository'))
    return 0 if ok else 1


def main(argv):
    if len(argv) != 2 or argv[0] not in ('dry', 'write'):
        sys.exit(__doc__)
    return run(argv[0], argv[1])


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
