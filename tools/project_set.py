# -*- coding: utf-8 -*-
"""tools/project_set.py -- b765, (R375)(7): THE PROJECT'S MIRROR REPOSITORY, THE BUILDER'S STEP.

Written at b765 by the Write tool and committed before its run, under tools/ and outside tools/standing/ ((R375)(11)); every route refuses
where this file differs from its blob at the relay's HEAD. No identifier of the author is read into any string here: the account the
repository stands under is read from the relay's own remote at run time and printed as <account>, a path under a user's profile is printed
as <profile>, and no line of any file of the set is printed -- each file is read by its name, its bytes and its md5 alone.

THE SET ((R375)(7)): the files tools/standing/roster.py's project route lists from tools/mirror_project_set.json at the export's source head,
each by the flat name the export gives it -- FINDINGS.md whole left out, its cut standing in its place (rule (16) of data/b754_rules.txt), and
MANIFEST taken as the export's own MANIFEST.md -- with FINDINGS_CUT.md and OPEN_TRAILS_CUT.md as tools/standing/cuts.py wrote them beside the
archive, and HANDOFF.md, the export's second source. The repository holds the set and nothing else; edited by no hand. Its bytes are
committed as the export holds them: the clone's core.autocrlf is false, read before the add.

THE COMPARISON, each file of the set against its want: an archive file and HANDOFF.md by md5 and bytes against the export MANIFEST's row; a cut
by its bytes against the MANIFEST's project row (which carries no md5) and by its md5 against the cut rebuilt by tools/standing/cuts.py at the
export's source head for the act that built it; MANIFEST.md by md5 and bytes against the export's own member. A file absent reads MISSING,
one that differs DIFFERS, a file of no row EXTRA.

  python -X utf8 -u tools/project_set.py control [<zip>]     the comparator's controls on the last export the worklist names (or <zip>),
                                                             nothing remote: the set written into a new temporary folder and read EQUAL, a
                                                             planted byte in one copy read as a difference; data/<act>_project_set_control.txt
  python -X utf8 -u tools/project_set.py create              the repository made private under the account where it is absent, read back
  python -X utf8 -u tools/project_set.py clone               the empty repository cloned to CLONE, outside every repository, its HEAD the
                                                             act's branch push-<act>-set, its core.autocrlf false
  python -X utf8 -u tools/project_set.py mirror <tag>        tools/mirror_build.ps1 -DateTag <tag>, unedited, refused unless PLACE-papers'
                                                             HEAD is its remote's main
  python -X utf8 -u tools/project_set.py verify <tag>        tools/mirror_verify.py over that export, run from PLACE-papers (clause 2's cwd)
  python -X utf8 -u tools/project_set.py write <tag>         the set from the export read CLEAN written into the empty clone, compared, a
                                                             planted byte read in a copy, then staged (one git write)
  python -X utf8 -u tools/project_set.py commit <tag>        the clone's commit, its message naming the two source commits (one git write)
  python -X utf8 -u tools/project_set.py readback <tag>      after `bash tools/push_gated.sh <clone> push-<act>-set`: the remote's main read
                                                             against the commit, each blob of its tree against the set, the repository read
                                                             private; data/<act>_project_set_build.txt rendered
The routes create and clone write data/<act>_project_set_repo.json; mirror, verify, write, commit and readback write
data/<act>_project_set_build.json; verify banks the verifier's print as data/<act>_project_set_verify.txt.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
import zipfile

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
for _p in (S, T):
    if _p not in sys.path:
        sys.path.insert(0, _p)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A        # noqa: E402
import roster as SR    # noqa: E402

PP = 'D:/MY-DOwnloads/PLACE-papers'
EXPORTS = 'D:/MY-DOwnloads'
NAME = 'PLACE-project-set'
CLONE = 'D:/PLACE-project-set'
NL = '\n'
NOREPLY = '@users.noreply.github.com'
CLEAN = 'VERDICT: CLEAN ON ALL THREE CLAUSES'
ROW = re.compile(r'^\|\s*([^|]+?)\s*\|\s*([\d,]+)\s*\|\s*`?([0-9a-fA-F]{32})`?\s*\|', re.M)   # tools/mirror_verify.py :44, the md5 rows
CUTROW = re.compile(r'^\|\s*(FINDINGS_CUT\.md|OPEN_TRAILS_CUT\.md)\s*\|\s*(\d+)\s*\|', re.M)   # roster.py project_lines :263-:264, bytes alone
HEAD = re.compile(r'@\s*`?([0-9a-f]{7,40})`?')   # tools/mirror_verify.py :45, the declared source head
SECOND = re.compile(r'^Second source: the relay at commit ([0-9a-f]{7,40}) \(its HEAD\)', re.M)   # roster.py SECOND_LINE
PROFILE = re.compile(r'[A-Za-z]:[\\/]+Users[\\/]+[^\\/\s\'"]+', re.I)
CUT_NAMES = ('FINDINGS_CUT.md', 'OPEN_TRAILS_CUT.md')
LEFT_OUT = ('FINDINGS.md',)   # rule (16): the cut in its place
BUILD_ROUTES = ('mirror', 'verify', 'write', 'commit', 'readback')


def act():
    return A.current()['act']


def branch():
    return 'push-%s-set' % act()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def md5(b):
    return hashlib.md5(b).hexdigest().lower()


def run(cmd, cwd=None, env=None):
    r = subprocess.run(cmd, cwd=cwd, env=env, capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout or '', r.stderr or ''


def git(repo, *a):
    return run(['git', '-C', repo] + list(a))


def parse_owner(url):
    m = re.match(r'^(?:https://(?:[^@/]+@)?github\.com/|git@github\.com:)([A-Za-z0-9-]+)/[^/]+?/?$', (url or '').strip())
    return m.group(1) if m else None


def owner():
    rc, out, _e = git(RELAY, 'remote', 'get-url', 'origin')
    o = parse_owner(out) if rc == 0 else None
    if not o:
        raise SystemExit('### THE ACCOUNT NOT READ FROM THE RELAY`S REMOTE -- NOTHING DONE')
    return o


def mask(s, o=None):
    s = PROFILE.sub('<profile>', s or '')
    return s.replace(o, '<account>') if o else s


def committed():
    here = open(os.path.abspath(__file__), 'rb').read().replace(b'\r', b'')
    b = A.blob('HEAD', 'tools/project_set.py')
    if b is None or b.replace(b'\r', b'') != here:
        raise SystemExit('### tools/project_set.py DIFFERS FROM ITS BLOB AT THE RELAY`S HEAD, OR IS NOT COMMITTED -- NOTHING RUN')


def put(name, obj=None, text=None):
    p = os.path.join(D, name)
    s = (json.dumps(obj, indent=1, ensure_ascii=False) + NL) if obj is not None else (NL.join(text) + NL)
    with open(p + '.tmp', 'w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    os.replace(p + '.tmp', p)
    return p


def jl(name):
    p = os.path.join(D, name)
    if not os.path.isfile(p):
        return {}
    with open(p, encoding='utf-8') as f:
        return json.load(f)


def repo_bank():
    return '%s_project_set_repo.json' % act()


def build_bank():
    return '%s_project_set_build.json' % act()


def zip_of(tag):
    return '%s/mirror-refresh-%s.zip' % (EXPORTS, tag)


def cuts_of(zpath):
    return zpath[:-4] + '-cuts'


def in_repository(p):
    """True where `p`, or the nearest folder of it that stands, lies inside a git work tree."""
    q = os.path.abspath(p)
    while not os.path.isdir(q) and os.path.dirname(q) != q:
        q = os.path.dirname(q)
    rc, out, _e = git(q, 'rev-parse', '--show-toplevel')
    return rc == 0 and bool(out.strip())


# ================================================================================ the set and its comparison

def plan(zpath, built_by):
    """the set read from an export: (items, meta). Each item: flat, path, src ('zip' with member | 'cuts' with file), md5, bytes, against.
    Refuses where any file of the project route's list is not found in the export by its flat name and its bytes, where a member is not its
    MANIFEST row, or where a cut beside the archive is not the cut rebuilt at the source head."""
    import cuts as CU
    z = zipfile.ZipFile(zpath)
    byname = dict((n.split('/')[-1], n) for n in z.namelist())
    if 'MANIFEST.md' not in byname:
        raise SystemExit('### THE EXPORT HOLDS NO MANIFEST.md -- NOTHING DONE')
    man_b = z.read(byname['MANIFEST.md'])
    man = man_b.decode('utf-8-sig', 'replace').replace('\r', '')
    hm, sm = HEAD.search(man), SECOND.search(man)
    if not hm:
        raise SystemExit('### THE MANIFEST DECLARES NO SOURCE HEAD -- NOTHING DONE')
    full = A.gs('pp', 'rev-parse', '--verify', '--quiet', hm.group(1) + '^{commit}')
    if not full:
        raise SystemExit('### THE DECLARED SOURCE HEAD %s IS NOT A COMMIT OF PLACE-papers -- NOTHING DONE' % hm.group(1))
    rows = dict((nm.strip('` ').split('/')[-1], (int(sz.replace(',', '')), h.lower())) for nm, sz, h in ROW.findall(man))
    crow = dict((n, int(b)) for n, b in CUTROW.findall(man))
    prow = SR.project(full, built_by, with_cuts=False)[0]
    items, left, bad = [], [], []
    for q, _b, note in prow:
        if q == 'MANIFEST':
            continue
        if q in LEFT_OUT:
            left.append(q)
            continue
        if note.startswith('###'):
            bad.append('%s: %s' % (q, note))
            continue
        leaf = q.split('/')[-1]
        cands = [leaf] + (['%s__%s' % (q.split('/')[-2], leaf)] if '/' in q else [])
        if q in SR.SECOND:
            src = A.blob(sm.group(1), q) if sm else None
        else:
            src = A.blob(full, q, 'pp')
        if src is None:
            bad.append('%s: not read at its source commit' % q)
            continue
        hit = [c for c in cands if c in rows and c in byname and z.read(byname[c]).replace(b'\r', b'') == src.replace(b'\r', b'')]
        if len(hit) != 1:
            bad.append('%s: %d flat names of the export match its bytes (%s)' % (q, len(hit), ', '.join(cands)))
            continue
        f = hit[0]
        mb = z.read(byname[f])
        if md5(mb) != rows[f][1] or len(mb) != rows[f][0]:
            bad.append('%s: the export`s member %s is not its MANIFEST row' % (q, f))
            continue
        items.append(dict(flat=f, path=q, src='zip', member=byname[f], md5=rows[f][1], bytes=rows[f][0],
                          against='the MANIFEST`s row, md5 and bytes'))
    cdir = cuts_of(zpath)
    rebuilt = CU.build(full, built_by)[0]
    for n in CUT_NAMES:
        p = os.path.join(cdir, n)
        want = (NL.join(rebuilt[n]) + NL).encode('utf-8')
        if not os.path.isfile(p):
            bad.append('%s: not beside the export' % n)
            continue
        with open(p, 'rb') as fh:
            b = fh.read()
        if n not in crow or len(b) != crow[n] or md5(b) != md5(want):
            bad.append('%s: beside the export %d bytes, the MANIFEST`s project row %s, the rebuilt cut %d bytes -- not equal' % (
                n, len(b), crow.get(n), len(want)))
            continue
        items.append(dict(flat=n, path=n, src='cuts', file=p, md5=md5(want), bytes=crow[n],
                          against='the MANIFEST`s project row by bytes, the cut rebuilt at the source head by md5'))
    items.append(dict(flat='MANIFEST.md', path='MANIFEST', src='zip', member=byname['MANIFEST.md'], md5=md5(man_b), bytes=len(man_b),
                      against='the export`s own MANIFEST.md, md5 and bytes'))
    if bad:
        raise SystemExit('### THE SET NOT READ FROM THE EXPORT -- NOTHING WRITTEN:\n  ' + '\n  '.join(bad))
    flats = [it['flat'] for it in items]
    if len(set(flats)) != len(flats):
        raise SystemExit('### A FLAT NAME TWICE IN THE SET -- NOTHING WRITTEN')
    with open(zpath, 'rb') as fh:
        zsha = hashlib.sha256(fh.read()).hexdigest()
    meta = dict(export=os.path.basename(zpath), export_sha256=zsha, pp=full, relay=(sm.group(1) if sm else None), left_out=left,
                built_by=built_by, files=len(items), by_manifest_row=sum(1 for it in items if it['src'] == 'zip' and it['flat'] != 'MANIFEST.md'),
                cuts=sum(1 for it in items if it['src'] == 'cuts'))
    return items, meta


def read_src(it, z):
    if it['src'] == 'zip':
        return z.read(it['member'])
    with open(it['file'], 'rb') as fh:
        return fh.read()


def write_set(dest, items, zpath):
    z = zipfile.ZipFile(zpath)
    for it in items:
        with open(os.path.join(dest, it['flat']), 'wb') as f:
            f.write(read_src(it, z))


def compare(dest, items):
    out = []
    for it in items:
        p = os.path.join(dest, it['flat'])
        if not os.path.isfile(p):
            out.append((it['flat'], 'MISSING'))
            continue
        with open(p, 'rb') as fh:
            b = fh.read()
        out.append((it['flat'], 'EQUAL' if (md5(b) == it['md5'] and len(b) == it['bytes']) else 'DIFFERS'))
    for e in sorted(set(os.listdir(dest)) - set(it['flat'] for it in items) - {'.git'}):
        out.append((e, 'EXTRA'))
    return out


def tally(cmp_):
    t = {}
    for _f, s in cmp_:
        t[s] = t.get(s, 0) + 1
    return t


def planted(dest, items):
    """the set's copies taken into a new temporary folder, one byte of one copy changed with its size kept: wanted that copy alone DIFFERS."""
    tmp = tempfile.mkdtemp(prefix='project-set-planted-')
    try:
        for it in items:
            shutil.copyfile(os.path.join(dest, it['flat']), os.path.join(tmp, it['flat']))
        victim = items[0]['flat']
        p = os.path.join(tmp, victim)
        with open(p, 'rb') as fh:
            b = bytearray(fh.read())
        b[len(b) // 2] ^= 0x01
        with open(p, 'wb') as fh:
            fh.write(bytes(b))
        c = compare(tmp, items)
        ok = [s for f, s in c if f == victim] == ['DIFFERS'] and all(s == 'EQUAL' for f, s in c if f != victim)
        return victim, tally(c), ok
    finally:
        if os.path.basename(tmp).startswith('project-set-planted-'):
            shutil.rmtree(tmp, ignore_errors=True)


def item_lines(items, states=None):
    st = dict(states or ())
    return ['    %s | %d bytes | md5 %s | against %s%s' % (it['flat'], it['bytes'], it['md5'], it['against'],
                                                        (' | %s' % st[it['flat']]) if it['flat'] in st else '') for it in items]


# ================================================================================ the routes

def control(*a):
    committed()
    o = owner()
    W = __import__('%s_worklist' % act())
    zpath = (a[0] if a else W.MIRROR_ZIP).replace('\\', '/')
    m = re.search(r'-(b\d+)\.zip$', zpath)
    built_by = m.group(1) if m else act()
    items, meta = plan(zpath, built_by)
    cases = []

    def case(name, got, want):
        cases.append((name, got, want, got == want))

    tmp = tempfile.mkdtemp(prefix='project-set-control-')
    try:
        write_set(tmp, items, zpath)
        case('THE SET FROM THE EXPORT WRITTEN INTO AN EMPTY FOLDER: every file EQUAL to its want, none MISSING, DIFFERS or EXTRA',
             tally(compare(tmp, items)), {'EQUAL': len(items)})
        victim, pt, pok = planted(tmp, items)
        case('A PLANTED BYTE: one byte of the copy of %s changed, its size kept: that copy alone DIFFERS (%s)' % (victim, pt), pok, True)
        gone = items[-2]['flat']
        os.remove(os.path.join(tmp, gone))
        case('A COPY REMOVED (%s): it alone reads MISSING' % gone, [s for _f, s in compare(tmp, items) if s != 'EQUAL'], ['MISSING'])
        with open(os.path.join(tmp, 'EXTRA.md'), 'wb') as fh:
            fh.write(b'x\n')
        case('A FILE OF NO ROW ADDED: it reads EXTRA beside the MISSING copy', sorted(s for _f, s in compare(tmp, items) if s != 'EQUAL'),
             ['EXTRA', 'MISSING'])
    finally:
        if os.path.basename(tmp).startswith('project-set-control-'):
            shutil.rmtree(tmp, ignore_errors=True)
    case('THE ACCOUNT READ FROM AN https REMOTE (constructed)', parse_owner('https://github.com/some-one/relay.git'), 'some-one')
    case('THE ACCOUNT READ FROM AN ssh REMOTE (constructed)', parse_owner('git@github.com:some-one/relay'), 'some-one')
    case('A REMOTE OF ANOTHER HOST NOT READ (constructed)', parse_owner('https://example.org/some-one/relay.git'), None)
    case('THE ACCOUNT MASKED IN A PRINTED ADDRESS (constructed)', mask('https://github.com/some-one/x.git', 'some-one'),
         'https://github.com/<account>/x.git')
    case('A PROFILE PATH MASKED (constructed)', mask('C:\\Users\\someone\\AppData\\x'), '<profile>\\AppData\\x')
    case('THE RELAY`S OWN REMOTE READ FOR ITS ACCOUNT', bool(o), True)
    case('A FOLDER INSIDE THE RELAY READ INSIDE A REPOSITORY', in_repository(os.path.join(RELAY, 'data')), True)
    case('THE CLONE`S FOLDER (%s) READ OUTSIDE EVERY REPOSITORY' % os.path.dirname(CLONE), in_repository(os.path.dirname(CLONE)), False)
    n_ok = sum(1 for c in cases if c[3])
    L = ['%s -- THE PROJECT SET`S BUILDER, ITS CONTROLS BEFORE ITS FIRST BUILD ((R375)(7)), by tools/project_set.py control (%s)' % (act(), utc()),
         '',
         '### the export read: %s, sha256 %s, built by %s from PLACE-papers %s and the relay %s' % (
             meta['export'], meta['export_sha256'][:16], built_by, meta['pp'][:8], (meta['relay'] or '-')[:8]),
         '### the set: %d files (%d by the MANIFEST`s rows, %d cuts, the MANIFEST); left out by rule (16): %s' % (
             meta['files'], meta['by_manifest_row'], meta['cuts'], ', '.join(meta['left_out']) or 'none'),
         '### each file by its name, bytes and md5 alone; no line of any file read into this bank'] + item_lines(items) + ['', '### THE CASES:']
    L += ['    %s: got %r, wanted %r -- %s' % (n, g, w, 'AS WANTED' if ok else '### NOT AS WANTED') for n, g, w, ok in cases]
    L += ['', '### ### **THE CONTROLS: %d OF %d AS WANTED**' % (n_ok, len(cases))]
    p = put('%s_project_set_control.txt' % act(), text=L)
    for line in L[2:5] + L[-len(cases) - 2:]:
        print(line)
    print('written', os.path.relpath(p, RELAY).replace('\\', '/'))
    return 0 if n_ok == len(cases) else 1


def create(*a):
    committed()
    o = owner()
    full = '%s/%s' % (o, NAME)
    R = jl(repo_bank())
    rc, out, err = run(['gh', 'repo', 'view', full, '--json', 'name,visibility'])
    if rc == 0:
        R['create'] = dict(at=utc(), absent_before=False, view=mask(out, o).strip())
        put(repo_bank(), R)
        print('### THE REPOSITORY STANDS ALREADY -- NOT CREATED: %s' % mask(out, o).strip())
        return 1
    absent = mask(err, o).strip()
    rc2, out2, err2 = run(['gh', 'repo', 'create', full, '--private'])
    rc3, out3, err3 = run(['gh', 'repo', 'view', full, '--json', 'name,visibility,isPrivate'])
    v = json.loads(out3) if rc3 == 0 and out3.strip() else {}
    ok = rc2 == 0 and v.get('isPrivate') is True and v.get('name') == NAME
    R['create'] = dict(at=utc(), absent_before=True, absent_read=absent, create_rc=rc2, create_print=mask(out2 + err2, o).strip(),
                       view=v, view_rc=rc3, as_wanted=ok, repository='<account>/%s' % NAME)
    put(repo_bank(), R)
    print('  read before: absent (%s)' % absent[:160])
    print('  create: exit %d ; %s' % (rc2, mask(out2 + err2, o).strip()[:200]))
    print('  read back: %s ; %s' % (v, 'PRIVATE AS WANTED' if ok else '### NOT AS WANTED'))
    print('written', 'data/%s' % repo_bank())
    return 0 if ok else 1


def clone(*a):
    committed()
    o = owner()
    if os.path.exists(CLONE):
        raise SystemExit('### %s STANDS ALREADY -- NOT CLONED' % CLONE)
    if in_repository(os.path.dirname(CLONE)):
        raise SystemExit('### THE FOLDER OF %s LIES INSIDE A REPOSITORY -- NOT CLONED' % CLONE)
    R = jl(repo_bank())
    if not (R.get('create') or {}).get('as_wanted'):
        raise SystemExit('### THE REPOSITORY NOT READ CREATED AND PRIVATE BY THE create ROUTE -- NOT CLONED')
    url = 'https://github.com/%s/%s.git' % (o, NAME)
    rc, out, err = run(['git', 'clone', url, CLONE])
    rc2 = rc4 = None
    if rc == 0:
        rc2 = git(CLONE, 'symbolic-ref', 'HEAD', 'refs/heads/%s' % branch())[0]
        rc4 = git(CLONE, 'config', 'core.autocrlf', 'false')[0]
    head = git(CLONE, 'symbolic-ref', '--short', 'HEAD')[1].strip() if rc == 0 else ''
    unborn = git(CLONE, 'rev-parse', '--verify', '--quiet', 'HEAD')[0] != 0 if rc == 0 else None
    crlf = git(CLONE, 'config', 'core.autocrlf')[1].strip() if rc == 0 else ''
    files = sorted(set(os.listdir(CLONE)) - {'.git'}) if os.path.isdir(CLONE) else None
    ok = rc == 0 and rc2 == 0 and rc4 == 0 and head == branch() and unborn is True and crlf == 'false' and files == []
    R['clone'] = dict(at=utc(), place=CLONE, remote=mask(url, o), clone_rc=rc, clone_print=mask(out + err, o).strip(), head=head, unborn=unborn,
                      autocrlf=crlf, files=files, as_wanted=ok)
    put(repo_bank(), R)
    print('  clone: exit %s ; %s' % (rc, mask(out + err, o).strip()[:200]))
    print('  HEAD %s ; unborn %s ; core.autocrlf %s ; files beside .git %s ; %s' % (head, unborn, crlf, files, 'AS WANTED' if ok else '### NOT AS WANTED'))
    print('written', 'data/%s' % repo_bank())
    return 0 if ok else 1


def mirror(tag):
    committed()
    zpath = zip_of(tag)
    stage = os.path.join(os.environ.get('TEMP', ''), 'mirror-build-%s' % tag)
    if os.path.exists(zpath) or os.path.exists(cuts_of(zpath)) or os.path.exists(stage):
        raise SystemExit('### THE EXPORT, ITS CUTS OR ITS STAGE STANDS FOR THE TAG %s -- NOT BUILT' % tag)
    loc = A.gs('pp', 'rev-parse', 'HEAD') or ''
    rc0, out0, _e0 = git(PP, 'ls-remote', 'origin', 'refs/heads/main')
    rem = (out0.split() or [''])[0]
    if not loc or loc != rem:
        raise SystemExit('### PLACE-papers HEAD %s IS NOT ITS REMOTE`S MAIN %s -- NOT BUILT (clause 2 would read the export stale)' % (loc[:8], rem[:8]))
    t0 = time.time()
    rc, out, err = run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(T, 'mirror_build.ps1'), '-DateTag', tag])
    B = jl(build_bank())
    B['mirror'] = dict(at=utc(), tag=tag, rc=rc, seconds=int(time.time() - t0), pp_head=loc, export=os.path.basename(zpath),
                       out=mask(out).replace('\r', '').split(NL), err=mask(err).replace('\r', '').split(NL))
    put(build_bank(), B)
    for line in mask(out).replace('\r', '').split(NL)[-8:]:
        print('  ' + line)
    print('  exit %d ; %d s ; PLACE-papers %s, its remote main equal' % (rc, B['mirror']['seconds'], loc[:8]))
    print('written', 'data/%s' % build_bank())
    return 0 if rc == 0 and os.path.isfile(zpath) else 1


def verify(tag):
    committed()
    zpath = zip_of(tag)
    if not os.path.isfile(zpath):
        raise SystemExit('### NO EXPORT FOR THE TAG %s -- NOTHING VERIFIED' % tag)
    env = dict(os.environ, PYTHONIOENCODING='utf-8')
    rc, out, err = run([sys.executable, os.path.join(T, 'mirror_verify.py'), zpath, 'origin', 'main'], cwd=PP, env=env)
    clean = CLEAN in out
    L = ['%s -- THE EXPORT FOR THE PROJECT`S REPOSITORY VERIFIED BY tools/mirror_verify.py, run from PLACE-papers, its print verbatim (%s)' % (act(), utc()),
         '### the export: %s' % os.path.basename(zpath), ''] + mask(out + err).replace('\r', '').split(NL) + ['### exit %d' % rc]
    put('%s_project_set_verify.txt' % act(), text=L)
    B = jl(build_bank())
    B['verify'] = dict(at=utc(), rc=rc, export=os.path.basename(zpath), clean=clean)
    put(build_bank(), B)
    print('  %s ; exit %d' % (CLEAN if clean else '### NOT CLEAN', rc))
    print('written', 'data/%s_project_set_verify.txt' % act(), 'and', 'data/%s' % build_bank())
    return 0 if clean else 1


def write(tag):
    committed()
    zpath = zip_of(tag)
    B = jl(build_bank())
    v = B.get('verify') or {}
    if not (v.get('clean') and v.get('export') == os.path.basename(zpath)):
        raise SystemExit('### THE EXPORT %s IS NOT READ CLEAN BY THE verify ROUTE -- NOTHING WRITTEN' % os.path.basename(zpath))
    if B.get('write'):
        raise SystemExit('### THE SET IS WRITTEN ALREADY (the bank`s write) -- NOTHING WRITTEN')
    if not os.path.isdir(os.path.join(CLONE, '.git')):
        raise SystemExit('### NO CLONE AT %s -- NOTHING WRITTEN' % CLONE)
    head = git(CLONE, 'symbolic-ref', '--short', 'HEAD')[1].strip()
    crlf = git(CLONE, 'config', 'core.autocrlf')[1].strip()
    held = sorted(set(os.listdir(CLONE)) - {'.git'})
    if head != branch() or crlf != 'false' or held:
        raise SystemExit('### THE CLONE IS NOT AS THE clone ROUTE LEFT IT (HEAD %s, core.autocrlf %s, files %d) -- NOTHING WRITTEN' % (head, crlf, len(held)))
    items, meta = plan(zpath, act())
    write_set(CLONE, items, zpath)
    c = compare(CLONE, items)
    t = tally(c)
    victim, pt, pok = planted(CLONE, items)
    ok = t == {'EQUAL': len(items)} and pok
    rec = dict(at=utc(), meta=meta, items=[dict((k, it[k]) for k in ('flat', 'path', 'bytes', 'md5', 'against')) for it in items],
               states=c, tally=t, planted=dict(victim=victim, tally=pt, as_wanted=pok))
    if not ok:
        B['write_refused'] = rec
        put(build_bank(), B)
        raise SystemExit('### THE SET AS WRITTEN IS NOT AS WANTED (%s ; the planted byte %s) -- NOTHING STAGED; the files stand in the clone, unstaged' % (t, pok))
    rc, out, err = git(CLONE, 'add', '-A')
    staged = sorted(x for x in git(CLONE, 'diff', '--cached', '--name-only')[1].replace('\r', '').split(NL) if x)
    rec.update(add_rc=rc, staged=staged, staged_equal=(staged == sorted(it['flat'] for it in items)))
    B['write'] = rec
    put(build_bank(), B)
    print('  the export %s (sha256 %s) from PLACE-papers %s and the relay %s' % (meta['export'], meta['export_sha256'][:16], meta['pp'][:8], (meta['relay'] or '-')[:8]))
    print('  the set: %d files ; compared %s ; the planted byte in the copy of %s %s' % (len(items), t, victim, 'DIFFERS, AS WANTED' if pok else '### NOT AS WANTED'))
    print('  staged %d ; equal to the set %s ; add exit %d' % (len(staged), rec['staged_equal'], rc))
    print('written', 'data/%s' % build_bank())
    return 0 if rc == 0 and rec['staged_equal'] else 1


def commit(tag):
    committed()
    B = jl(build_bank())
    w = B.get('write') or {}
    if not w.get('staged_equal'):
        raise SystemExit('### THE SET IS NOT READ STAGED BY THE write ROUTE -- NOT COMMITTED')
    if B.get('commit'):
        raise SystemExit('### THE CLONE`S COMMIT IS MADE ALREADY (the bank`s commit) -- NOT COMMITTED')
    staged = sorted(x for x in git(CLONE, 'diff', '--cached', '--name-only')[1].replace('\r', '').split(NL) if x)
    if staged != sorted(it['flat'] for it in w['items']):
        raise SystemExit('### THE STAGED SET IS NOT THE SET -- NOT COMMITTED')
    em = git(CLONE, 'config', 'user.email')[1].strip()
    if not em.endswith(NOREPLY):
        raise SystemExit('### THE COMMIT IDENTITY IS NOT A NOREPLY ADDRESS -- NOT COMMITTED')
    meta = w['meta']
    msg = '%s the Project set from PLACE-papers %s and the relay %s, written by relay tools/project_set.py from the export %s, edited by no hand' % (
        act(), meta['pp'][:8], (meta['relay'] or '-')[:8], meta['export'])
    rc, out, err = git(CLONE, 'commit', '-q', '-m', msg)
    sha = git(CLONE, 'rev-parse', 'HEAD')[1].strip()
    subj = git(CLONE, 'log', '-1', '--format=%s')[1].strip()
    B['commit'] = dict(at=utc(), rc=rc, sha=sha, subject=subj, subject_equal=(subj == msg), noreply=True, branch=branch())
    put(build_bank(), B)
    print('  commit %s on %s ; exit %d ; the identity a noreply address' % (sha[:8], branch(), rc))
    print('  subject   : %s' % subj)
    print('  read back : %s' % ('EQUAL' if subj == msg else '### NOT EQUAL'))
    print('written', 'data/%s' % build_bank())
    return 0 if rc == 0 and subj == msg else 1


def readback(tag):
    committed()
    o = owner()
    B = jl(build_bank())
    c = B.get('commit') or {}
    w = B.get('write') or {}
    if not c.get('sha'):
        raise SystemExit('### NO COMMIT IN THE BANK -- NOTHING READ')
    rc, out, _e = git(CLONE, 'ls-remote', 'origin', 'refs/heads/main')
    remote = (out.split() or [''])[0]
    rcv, ov, _ev = run(['gh', 'repo', 'view', '%s/%s' % (o, NAME), '--json', 'name,visibility,isPrivate'])
    v = json.loads(ov) if rcv == 0 and ov.strip() else {}
    blobs = []
    for it in w['items']:
        r = subprocess.run(['git', '-C', CLONE, 'show', '%s:%s' % (c['sha'], it['flat'])], capture_output=True)
        b = r.stdout if r.returncode == 0 else None
        blobs.append((it['flat'], 'MISSING' if b is None else ('EQUAL' if (md5(b) == it['md5'] and len(b) == it['bytes']) else 'DIFFERS')))
    names = sorted(x for x in git(CLONE, 'ls-tree', '-r', '--name-only', c['sha'])[1].replace('\r', '').split(NL) if x)
    extra = sorted(set(names) - set(it['flat'] for it in w['items']))
    ok = remote == c['sha'] and v.get('isPrivate') is True and all(s == 'EQUAL' for _f, s in blobs) and not extra
    B['readback'] = dict(at=utc(), remote_main=remote, equal=(remote == c['sha']), visibility=v.get('visibility'), private=v.get('isPrivate'),
                         tree_files=len(names), blobs=tally(blobs), extra=extra, as_wanted=ok)
    put(build_bank(), B)
    meta = w['meta']
    st = dict(blobs)
    L = ['%s -- THE PROJECT`S MIRROR REPOSITORY BUILT ((R375)(7)), by tools/project_set.py, each route`s record in data/%s (%s)' % (act(), build_bank(), utc()),
         '',
         '### THE REPOSITORY: <account>/%s, %s (read by the host`s tool) ; its clone %s, outside every repository of the record' % (NAME, v.get('visibility'), CLONE),
         '### THE EXPORT: %s, sha256 %s, built under the tag %s (exit %s) and verified %s' % (
             meta['export'], meta['export_sha256'][:16], (B.get('mirror') or {}).get('tag'), (B.get('mirror') or {}).get('rc'),
             'CLEAN ON ALL THREE CLAUSES' if (B.get('verify') or {}).get('clean') else '### NOT CLEAN'),
         '### THE SOURCES: PLACE-papers %s ; the relay %s (the export`s second source, its HEAD at the build)' % (meta['pp'][:8], (meta['relay'] or '-')[:8]),
         '### THE SET: %d files -- by the MANIFEST`s rows %d, md5 and bytes ; the cuts %d, by bytes to the MANIFEST`s project rows and by md5 to the cut '
         'rebuilt at the source head ; the MANIFEST 1, the export`s own ; left out by rule (16): %s' % (
             meta['files'], meta['by_manifest_row'], meta['cuts'], ', '.join(meta['left_out']) or 'none'),
         '### THE WRITE: compared %s ; the planted byte in the copy of %s %s ; staged %d, equal to the set %s' % (
             w['tally'], w['planted']['victim'], 'read as a difference, AS WANTED' if w['planted']['as_wanted'] else '### NOT AS WANTED',
             len(w['staged']), w['staged_equal']),
         '### THE COMMIT: %s on %s, its subject read back %s: %s' % (c['sha'][:8], c['branch'], 'EQUAL' if c['subject_equal'] else '### NOT EQUAL', c['subject']),
         '### THE READ-BACK: the remote`s main %s, equal to the commit %s ; the commit`s tree %d files, each blob against the set %s, EXTRA %s ; private %s' % (
             remote[:8], remote == c['sha'], len(names), tally(blobs), extra or 'none', v.get('isPrivate')),
         '### ### **THE BUILD %s**' % ('AS WANTED' if ok else '### NOT AS WANTED'),
         '', '### THE FILES, each by its name, bytes and md5 alone, its blob at the commit read against its want:'] + [
        '    %s | %d bytes | md5 %s | against %s | %s' % (it['flat'], it['bytes'], it['md5'], it['against'], st.get(it['flat'])) for it in w['items']]
    put('%s_project_set_build.txt' % act(), text=L)
    for line in L[2:11]:
        print(line)
    print('written', 'data/%s_project_set_build.txt' % act(), 'and', 'data/%s' % build_bank())
    return 0 if ok else 1


ROUTES = dict(control=control, create=create, clone=clone, mirror=mirror, verify=verify, write=write, commit=commit, readback=readback)


def main(argv):
    if not argv or argv[0] not in ROUTES:
        sys.exit(__doc__)
    if argv[0] in BUILD_ROUTES and len(argv) != 2:
        sys.exit('### THE ROUTE %s TAKES ONE TAG' % argv[0])
    return ROUTES[argv[0]](*argv[1:]) or 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
