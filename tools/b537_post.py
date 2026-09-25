# -*- coding: utf-8 -*-
"""b537_post.py -- THE AUTHOR`S WORD ON DEFECT (c): THE -post BUILD`S HEAD BLOCK, VERIFICATION AND BANK. ### `head | verify | bank`

### The builder (`mirror_build.ps1`, unedited) built `mirror-refresh-2026-09-25-b537-post.zip` from PLACE-papers after the act`s
### last PLACE-papers push. `head` inserts the head block under the MANIFEST`s title the way `b537_mirror.py rehead` repaired it:
### the builder joins its lines with LF and Out-File ends the file with one CRLF, so the text is split on LF only, the trailing
### CRLF kept, and every builder line is kept byte for byte. The pre-push zip and its stage folder are not touched.
### This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import b537_mirror as M   # ### ceiling(), REPOS, KER, git -- imported, not copied

ROOT, D, T, PP = M.ROOT, M.D, M.T, M.PP
TAG = '2026-09-25-b537-post'
STAGE = os.path.join(os.environ['TEMP'], 'mirror-build-' + TAG)
ZIP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-%s.zip' % TAG)
OLD_ZIP = M.ZIP
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


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
    first, rest = text.split(NL, 1)
    assert first == '# MANIFEST - mirror-refresh-' + TAG, first
    repos = []
    for n, p in M.REPOS:
        loc = M.git(p, 'rev-parse', 'HEAD')
        rem = (M.git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
        repos.append(dict(repo=n, local=loc, remote=rem, agree=(loc == rem)))
    tags = {}
    for l in M.git(M.KER, 'ls-remote', '--tags', 'origin').split(NL):
        m = re.match(r'^([0-9a-f]{40})\s+refs/tags/(v0\.[12])\^\{\}$', l.strip())
        if m:
            tags[m.group(2)] = m.group(1)
    c = M.ceiling()
    blk = ['', '**THE CEILING, (R146)(2)** (the author`s ruling, 2026-09-25; quoted once): *%s*' % c, '',
           '**THE LAST COMMIT OF EACH REPOSITORY**, read at build time -- local HEAD and the remote`s main, both full:', '']
    for r in repos:
        extra = ''
        if r['repo'] == 'SIDE-explicit-formula':
            extra = ' ; tags v0.1 = %s , v0.2 = %s' % (tags.get('v0.1', 'ABSENT'), tags.get('v0.2', 'ABSENT'))
        blk.append('- %s : local %s ; remote %s ; %s%s' % (r['repo'], r['local'], r['remote'], 'AGREE' if r['agree'] else 'DISAGREE', extra))
    blk += ['', 'The block above is written by relay `tools/b537_post.py` under (R147)(2) and the author`s word on b537 defect (c); '
                'the lines below are the builder`s own. This build supersedes mirror-refresh-2026-09-25-b537.zip, which is kept.']
    assert not any(l.lstrip().startswith('|') or '@ `' in l or '@`' in l for l in blk)
    fixed = first + NL + NL.join(blk) + NL + rest
    assert re.findall(r'^\|.*$', fixed, re.M) == re.findall(r'^\|.*$', text, re.M) and fixed.count(c) == 1
    assert fixed.replace(NL.join(blk) + NL, '', 1) == text
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + fixed.encode('utf-8'))
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    ps = subprocess.run(['powershell', '-NoProfile', '-Command',
                         "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)], capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    dump('b537_post_head.json', dict(ceiling=c, repos=repos, tags=tags, block=blk, bom=bom, builder_text_md5=hashlib.md5(text.encode('utf-8')).hexdigest(),
                                     zip_sha_before=before, zip_sha_after=after, update_rc=ps.returncode, update_err=ps.stderr.strip()))
    print('  head block : %d lines under the title ; update rc %d ; zip %s -> %s' % (len(blk), ps.returncode, before[:16], after[:16]))
    return ps.returncode


def verify():
    r = subprocess.run([sys.executable, os.path.join(T, 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    io.open(os.path.join(D, 'b537_post_verify.txt'), 'w', encoding='utf-8', newline=NL).write(r.stdout + r.stderr + '### exit %d%s' % (r.returncode, NL))
    print(r.stdout)
    return r.returncode


def bank():
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md').decode('utf-8-sig').replace('\r', '')
    rows = {m.group(1): m.group(2) for m in re.finditer(r'^\|\s*([^|]+?)\s*\|\s*[\d,]+\s*\|\s*`?([0-9a-f]{32})`?\s*\|', man, re.M)}
    loc, rem = M.git(PP, 'rev-parse', 'HEAD'), (M.git(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    n1 = {f: dict(manifest=rows.get(f), at_head=hashlib.md5(M.git_bytes(PP, 'show', 'HEAD:' + f)).hexdigest()) for f in
          ('FINDINGS.md', 'REGISTRY.md', 'ERRATA.md', 'README.md', 'OPEN_TRAILS.md')}
    ot = z.read('OPEN_TRAILS.md').decode('utf-8', 'replace')
    res = dict(zip=ZIP, zip_sha256=hashlib.sha256(open(ZIP, 'rb').read()).hexdigest(), entries=len(names),
               files_excl_manifest=len([n for n in names if n != 'MANIFEST.md']), manifest_rows=len(rows), manifest_head=man.split(NL)[:22],
               pp_local=loc, pp_remote=rem, n1={f: dict(v, equal=v['manifest'] == v['at_head']) for f, v in n1.items()},
               ot_counts={w: ot.count(w) for w in ('W-ORD-SEAM-UPSTREAM', 'W-ORD-REGISTER-DEPTH')},
               old_zip_sha256=hashlib.sha256(open(OLD_ZIP, 'rb').read()).hexdigest(), old_stage_present=os.path.isdir(M.STAGE),
               ceiling_count=man.count(M.ceiling()), roster_line=next((l for l in man.split(NL) if l.startswith('ROSTER')), ''))
    dump('b537_post.json', res)
    print('  zip : %s' % ZIP)
    print('  ### entries %d (files %d + MANIFEST) ; rows %d ; sha256 %s' % (res['entries'], res['files_excl_manifest'], res['manifest_rows'], res['zip_sha256']))
    print('  PLACE-papers HEAD %s ; remote %s' % (loc, rem))
    for f, v in res['n1'].items():
        print('  md5 %-15s manifest %s ; at HEAD %s ; %s' % (f, v['manifest'], v['at_head'], 'EQUAL' if v['equal'] else 'DIFFER'))
    print('  ceiling occurrences %d ; %s' % (res['ceiling_count'], res['roster_line']))
    print('  the superseded zip : sha256 %s (unchanged: %s) ; its stage folder present : %s'
          % (res['old_zip_sha256'], res['old_zip_sha256'] == json.loads(io.open(os.path.join(D, 'b537_mirror.json'), encoding='utf-8').read())['zip_sha256'],
             res['old_stage_present']))
    print('  ### THE MANIFEST HEAD:')
    for l in res['manifest_head']:
        print('    ' + l)
    return 0


if __name__ == '__main__':
    sys.exit(dict(head=head, verify=verify, bank=bank)[sys.argv[1]]())
