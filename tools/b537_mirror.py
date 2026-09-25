# -*- coding: utf-8 -*-
"""b537_mirror.py -- COMPONENT 1: THE HEAD BLOCK, THE VERIFICATION, THE BANK. ### `head | verify | bank`

### READING (1): the builder (`mirror_build.ps1`, CARRIED, UNEDITED) has already built this act's zip. `head` writes the
### head block into the staged MANIFEST directly under its title line and updates that ONE entry of this act's zip in
### place. The block carries no "@ `" and no line opening with "|", so mirror_verify's HEAD and ROW parses read the
### builder's own lines. ### This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys, zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
TAG = '2026-09-25-b537'
STAGE = os.path.join(os.environ['TEMP'], 'mirror-build-' + TAG)
ZIP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-%s.zip' % TAG)
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
REPOS = [('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section')),
         ('SIDE-explicit-formula', os.path.join('D:', os.sep, 'SIDE-explicit-formula')), ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel'))]
KER = REPOS[3][1]
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ceiling():
    f = ' '.join(io.open(os.path.join(D, 'b536_ferry.txt'), encoding='utf-8').read().split())
    i = f.index('reads, supportable: "') + len('reads, supportable: "')
    return f[i:f.index('" Not supportable', i)]


def dump(name, obj):
    io.open(os.path.join(D, name), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def head():
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'THE CEILING, (R146)(2)' in raw:
        print('### THE HEAD BLOCK IS ALREADY IN THE STAGED MANIFEST -- REFUSING TO WRITE IT TWICE.')
        return 2
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    eol = '\r\n' if '\r\n' in text else NL
    lines = text.split(eol)
    assert lines[0].startswith('# MANIFEST - mirror-refresh-' + TAG), lines[0]
    repos = []
    for n, p in REPOS:
        loc = git(p, 'rev-parse', 'HEAD')
        rem = (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
        repos.append(dict(repo=n, local=loc, remote=rem, agree=(loc == rem)))
    tags = {}
    for l in git(KER, 'ls-remote', '--tags', 'origin').split(NL):
        m = re.match(r'^([0-9a-f]{40})\s+refs/tags/(v0\.[12])\^\{\}$', l.strip())
        if m:
            tags[m.group(2)] = m.group(1)
    c = ceiling()
    blk = ['', '**THE CEILING, (R146)(2)** (the author`s ruling, 2026-09-25; quoted once): *%s*' % c, '',
           '**THE LAST COMMIT OF EACH REPOSITORY**, read at build time -- local HEAD and the remote`s main, both full:', '']
    for r in repos:
        extra = ''
        if r['repo'] == 'SIDE-explicit-formula':
            extra = ' ; tags v0.1 = %s , v0.2 = %s' % (tags.get('v0.1', 'ABSENT'), tags.get('v0.2', 'ABSENT'))
        blk.append('- %s : local %s ; remote %s ; %s%s' % (r['repo'], r['local'], r['remote'], 'AGREE' if r['agree'] else 'DISAGREE', extra))
    blk += ['', 'The block above is written by relay `tools/b537_mirror.py` under (R147)(2); the lines below are the builder`s own.']
    assert not any(l.lstrip().startswith('|') or '@ `' in l or '@`' in l for l in blk)
    out = eol.join([lines[0]] + blk + lines[1:])
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    ps = subprocess.run(['powershell', '-NoProfile', '-Command',
                         "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)], capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    dump('b537_head.json', dict(ceiling=c, repos=repos, tags=tags, block=blk, bom=bom, eol=repr(eol), zip_sha_before=before,
                                zip_sha_after=after, update_rc=ps.returncode, update_err=ps.stderr.strip()))
    print('  head block : %d lines inserted under the title ; update rc %d ; zip sha256 %s -> %s' % (len(blk), ps.returncode, before[:16], after[:16]))
    for l in blk:
        print('    ' + l)
    return ps.returncode


def verify():
    r = subprocess.run([sys.executable, os.path.join(T, 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    io.open(os.path.join(D, 'b537_mirror_verify.txt'), 'w', encoding='utf-8', newline=NL).write(r.stdout + r.stderr + '### exit %d%s' % (r.returncode, NL))
    print(r.stdout)
    return r.returncode


def bank():
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md').decode('utf-8-sig').replace('\r', '')
    rows = {m.group(1): m.group(2) for m in re.finditer(r'^\|\s*([^|]+?)\s*\|\s*[\d,]+\s*\|\s*`?([0-9a-f]{32})`?\s*\|', man, re.M)}
    loc, rem = git(PP, 'rev-parse', 'HEAD'), (git(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    n1 = {}
    for f in ('FINDINGS.md', 'REGISTRY.md', 'ERRATA.md', 'README.md'):
        h = hashlib.md5(git_bytes(PP, 'show', 'HEAD:' + f)).hexdigest()
        n1[f] = dict(manifest=rows.get(f), at_head=h, equal=(rows.get(f) == h))
    adds = [l for l in git(PP, 'diff', '--name-status', '--diff-filter=A', '3b5532a', 'HEAD').split(NL) if l.strip()]
    roster_line = next((l for l in man.split(NL) if l.startswith('ROSTER')), '')
    prev_status = git(ROOT, 'status', '--porcelain', '--', 'tools/mirror_prevbuild.json')
    res = dict(zip=ZIP, zip_sha256=hashlib.sha256(open(ZIP, 'rb').read()).hexdigest(), entries=len(names),
               files_excl_manifest=len([n for n in names if n != 'MANIFEST.md']), manifest_rows=len(rows),
               manifest_head=man.split(NL)[:22], pp_local=loc, pp_remote=rem, pp_agree=(loc == rem), n1=n1,
               additions_since_3b5532a=adds, roster_line=roster_line, prevbuild_git_status=prev_status,
               ceiling_count=man.count(ceiling()))
    dump('b537_mirror.json', res)
    print('  zip : %s' % ZIP)
    print('  ### entries %d (files %d + MANIFEST) ; MANIFEST rows %d' % (res['entries'], res['files_excl_manifest'], res['manifest_rows']))
    print('  ### zip sha256 : %s' % res['zip_sha256'])
    print('  additions since 3b5532a : %s' % (adds or 'NONE'))
    print('  roster line : %s' % roster_line)
    print('  PLACE-papers HEAD %s ; remote %s ; %s' % (loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
    for f, v in n1.items():
        print('  (N1) %-12s manifest %s ; at HEAD %s ; %s' % (f, v['manifest'], v['at_head'], 'EQUAL' if v['equal'] else 'DIFFER'))
    print('  ceiling occurrences in MANIFEST : %d' % res['ceiling_count'])
    print('  mirror_prevbuild.json git status : %r' % prev_status)
    print('  ### THE MANIFEST HEAD:')
    for l in res['manifest_head']:
        print('    ' + l)
    return 0


def rehead():
    """### DEFECT (b)'s REPAIR. `head` split the builder's text on CRLF because Out-File ends it with one, while the
    ### builder joins its own lines with LF -- so the whole MANIFEST was one "line" and the block went to its END. The
    ### builder's exact text is everything before the first CRLF, plus that CRLF; the block is re-inserted under the
    ### title with LF, and the one entry of this act's zip is updated in place again."""
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    hb = json.loads(io.open(os.path.join(D, 'b537_head.json'), encoding='utf-8').read())
    orig = text.split('\r\n')[0] + '\r\n'
    tail = text[len(orig):]
    if tail != '\r\n'.join(hb['block']) + '\r\n':
        print('### THE STAGED MANIFEST IS NOT THE DEFECTIVE WRITE THIS REPAIR KNOWS -- REFUSING.')
        return 2
    rows_before = re.findall(r'^\|.*$', orig, re.M)
    first, rest = orig.split(NL, 1)
    fixed = first + NL + NL.join(hb['block']) + NL + rest
    assert re.findall(r'^\|.*$', fixed, re.M) == rows_before and fixed.count(hb['ceiling']) == 1
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + fixed.encode('utf-8'))
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    ps = subprocess.run(['powershell', '-NoProfile', '-Command',
                         "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)], capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    dump('b537_rehead.json', dict(builder_text_md5=hashlib.md5(orig.encode('utf-8')).hexdigest(), rows=len(rows_before),
                                  zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode, update_err=ps.stderr.strip()))
    print('  rehead : builder text recovered (%d table lines) ; block under the title ; update rc %d ; zip %s -> %s'
          % (len(rows_before), ps.returncode, before[:16], after[:16]))
    return ps.returncode


if __name__ == '__main__':
    sys.exit(dict(head=head, rehead=rehead, verify=verify, bank=bank)[sys.argv[1]]())
