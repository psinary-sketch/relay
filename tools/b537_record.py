# -*- coding: utf-8 -*-
"""b537_record.py -- THE ACT`S RECORD, UNDER (R147). ### `python tools/b537_record.py memory | workorders | components | desk | trail`

### The ceiling is READ from the banked b536 ferry, not typed; the memory entry is read back from the seat`s memory directory and
### banked byte for byte; OPEN_TRAILS takes ONE append (the two work-orders and this act`s record). This file deletes nothing.
"""
import hashlib, io, json, os, re, subprocess, sys, zipfile
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
ENTRY = 'project_criterion_b533_b536.md'
ZIP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-25-b537.zip')
V01 = 'baed4df861dac05224f01dad17453648d3d7fe0a'
V02 = '5c72cad24303f23d92256ebd466d3a3d32424a4b'
NOT_CLAIMED = "RH proved; h2_sign proved; the earliest Lean formalization of Weil's criterion."
HEADING = ('### b537 — the mirror export and the memory refresh under (R147); the ceiling of (R146)(2) at the MANIFEST`s head; '
           'W-ORD-SEAM-UPSTREAM and W-ORD-REGISTER-DEPTH named')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rd(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    io.open(os.path.join(D, n), 'w', encoding='utf-8', newline=NL).write(json.dumps(obj, indent=1, ensure_ascii=False) + NL)


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def ceiling():
    f = ' '.join(rd(os.path.join(D, 'b536_ferry.txt')).split())
    i = f.index('reads, supportable: "') + len('reads, supportable: "')
    return f[i:f.index('" Not supportable', i)]


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


# ------------------------------------------------------------------------------ COMPONENT 2
def memory():
    p = os.path.join(MEM, ENTRY)
    b = open(p, 'rb').read()
    open(os.path.join(D, 'b537_memory_entry.md'), 'wb').write(b)
    t = b.decode('utf-8')
    before = jl('b537_memory_before.json')['files']
    now = {f: sha(os.path.join(MEM, f)) for f in sorted(os.listdir(MEM)) if f.endswith('.md')}
    changed = sorted(f for f in before if f in now and now[f] != before[f])
    added = sorted(f for f in now if f not in before)
    gone = sorted(f for f in before if f not in now)
    idx = rd(os.path.join(MEM, 'MEMORY.md')).rstrip(NL).split(NL)
    res = dict(path=p, lines=len(t.rstrip(NL).split(NL)), sha256=hashlib.sha256(b).hexdigest(), frontmatter=t.startswith('---\nname: '),
               type_project='\n  type: project\n' in t, why='**Why:**' in t, how='**How to apply:**' in t,
               ceiling_verbatim=ceiling() in t, v01=V01 in t, v02=V02 in t, not_claimed=('Not claimed:' in t and NOT_CLAIMED in t),
               changed=changed, added=added, gone=gone, index_last=idx[-1], index_refs=sum(1 for l in idx if '(%s)' % ENTRY in l))
    put_json('b537_memory.json', res)
    print('  memory entry : %s' % p)
    print('  ### lines %d ; sha256 %s' % (res['lines'], res['sha256']))
    for k in ('frontmatter', 'type_project', 'why', 'how', 'ceiling_verbatim', 'v01', 'v02', 'not_claimed'):
        print('    %-17s %s' % (k, res[k]))
    print('  memory files changed since the pre-seal hashes : %s ; added : %s ; gone : %s' % (changed, added, gone or 'NONE'))
    print('  index : its last line points at the entry %s ; references %d' % ('(%s)' % ENTRY in idx[-1], res['index_refs']))


# ------------------------------------------------------------------------------ COMPONENT 3
def wo_lines():
    seam = rd(os.path.join(KER, 'SIDEExplicitFormula', 'Seam.lean')).split(NL)
    ln = next(i for i, l in enumerate(seam) if l.startswith('theorem zeta_zero_re_nonpos ')) + 1
    b512 = rd(os.path.join(D, 'b512_closing.txt')).split(NL)[4:7]
    f = ' '.join(re.sub(r'-\n(?=\S)', '-', rd(os.path.join(D, 'b537_ferry.txt'))).split())   # a hyphen at a hard wrap joins
    q = f[f.index('(4) Two work-orders are named, not started:'):f.index('RULING (R147) END')].strip()
    L = ['#### `W-ORD-SEAM-UPSTREAM` — OPEN, named not started, filed b537 on `(R147)`(4)', '',
         '**Trigger: the author`s word.** Starts from `SIDE-explicit-formula/SIDEExplicitFormula/Seam.lean:%d` at `v0.2` = `%s`:' % (ln, V02), '',
         '```', seam[ln - 1], '```', '',
         '`zeta_zero_re_nonpos` is a Mathlib-shaped lemma about zeta`s trivial zeros, priced for an upstream contribution in Mathlib`s form. '
         'Nothing is sent upstream by this entry.', '',
         '#### `W-ORD-REGISTER-DEPTH` — OPEN, named not started, filed b537 on `(R147)`(4)', '',
         '**Trigger: the act after b537, unless the author rules otherwise.** R1, R3, R5 of §27.3 read for statability in SIDE-explicit-formula '
         'and, where statable, the closure of their equivalence to RH, against b512`s table — relay `data/b512_closing.txt:5-7`:', '',
         '```'] + [l.strip() for l in b512] + ['```', '',
         '**The ruling`s words, verbatim** (relay `data/b537_ferry.txt`, hard wrap normalised): *"%s"*' % q]
    return L, ln


def workorders():
    L, ln = wo_lines()
    io.open(os.path.join(D, 'b537_workorders.md'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    print('  ### Seam.lean line %d ; banked b537_workorders.md (entered by `trail`, inside the ONE append)' % ln)


# ------------------------------------------------------------------------------ the desk
def token_count():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        return None
    return sum(open(os.path.join(d0, f), 'rb').read().count(t) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b537_'))


def scores():
    mj, mm = jl('b537_mirror.json'), jl('b537_memory.json')
    man = zipfile.ZipFile(ZIP).read('MANIFEST.md').decode('utf-8-sig').replace(chr(13), '')
    head = man.split('| flat file |')[0]
    needle = 'https://' + 'zenodo' + '.org'
    zen = [f for f in os.listdir(T) if f.startswith('b537_') and needle in rd(os.path.join(T, f))]
    tok = token_count()
    readme_has = ceiling() in ' '.join(rd(os.path.join(PP, 'README.md')).split())
    return dict(
        n1=mj.get('pp_agree') is True and len(mj.get('n1') or {}) == 4 and all(v['equal'] for v in mj['n1'].values()),
        n2=head.count(ceiling()) == 1 and man.count(ceiling()) == 1 and readme_has, readme_has=readme_has,
        n3=bool(mm.get('v01') and mm.get('v02') and mm.get('not_claimed')),
        n4=(git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == '' and not zen and tok == 0), token=tok, zenodo_tools=zen,
        s1=('unchanged since' in (mj.get('roster_line') or '')) and 'ADDED:' not in man and 'REMOVED:' not in man,
        s2='VERDICT: CLEAN ON ALL THREE CLAUSES' in rd(os.path.join(D, 'b537_mirror_verify.txt')),
        s3=mj.get('prevbuild_git_status') == '')


def w(v):
    return 'HELD' if v else 'REFUTED'


def components():
    mj, mm, hj = jl('b537_mirror.json'), jl('b537_memory.json'), jl('b537_head.json')
    L = ['=' * 132, 'b537 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### COMPONENT 1 -- THE EXPORT: %s' % mj.get('zip'),
         '  last export read : mirror-refresh-2026-09-25-b534.zip, built by b534 at PLACE-papers 3b5532a',
         '  build log : ' + ' ; '.join(l.strip() for l in rd(os.path.join(D, 'b537_build_log.txt')).split(NL) if l.strip()),
         '  entries %s (files %s + MANIFEST) ; rows %s ; zip sha256 %s' % (mj.get('entries'), mj.get('files_excl_manifest'), mj.get('manifest_rows'), mj.get('zip_sha256')),
         '  additions since the last export : %s' % (mj.get('additions_since_3b5532a') or 'NONE'),
         '  roster line : %s' % mj.get('roster_line'),
         '  verify : ' + ' ; '.join(l.strip() for l in rd(os.path.join(D, 'b537_mirror_verify.txt')).split(NL) if 'CLAUSE' in l and ':' in l and 'CLAUSE 1:' not in l
                                    and 'CLAUSE 2:' not in l and 'CLAUSE 3:' not in l),
         '  tags : v0.1 = %s ; v0.2 = %s' % ((hj.get('tags') or {}).get('v0.1'), (hj.get('tags') or {}).get('v0.2')),
         '  the MANIFEST head, read from inside the zip :'] + ['    ' + l for l in mj.get('manifest_head', [])] + [
         '', '### COMPONENT 2 -- THE MEMORY: %s ; lines %s ; sha256 %s' % (mm.get('path'), mm.get('lines'), mm.get('sha256')),
         '  ' + json.dumps({k: mm.get(k) for k in ('frontmatter', 'ceiling_verbatim', 'v01', 'v02', 'not_claimed', 'changed', 'added', 'gone', 'index_refs')}),
         '', '### COMPONENT 3 -- THE WORK-ORDERS: ' + ' ; '.join(l for l in rd(os.path.join(D, 'b537_workorders.md')).split(NL) if l.startswith('#### ')),
         '=' * 132]
    io.open(os.path.join(D, 'b537_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def desk():
    sc, mj, mm = scores(), jl('b537_mirror.json'), jl('b537_memory.json')
    n = ('n1', 'n2', 'n3', 'n4')
    s = ('s1', 's2', 's3')
    L = ['=' * 104, 'b537 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S FOUR.', '-' * 104,
         '  **(N1)** ### **%s.** -- PLACE-papers HEAD %s = remote %s ; ' % (w(sc['n1']), (mj.get('pp_local') or '')[:12], (mj.get('pp_remote') or '')[:12])
         + ' ; '.join('%s %s' % (f, 'EQUAL' if v['equal'] else 'DIFFER') for f, v in (mj.get('n1') or {}).items()) + '.',
         '  **(N2)** ### **%s.** -- the sentence once in the MANIFEST, above its table ; equal to README`s (R146)(2) sentence : %s.' % (w(sc['n2']), sc['readme_has']),
         '  **(N3)** ### **%s.** -- v0.1 full %s ; v0.2 full %s ; the not-claimed line %s.' % (w(sc['n3']), mm.get('v01'), mm.get('v02'), mm.get('not_claimed')),
         '  **(N4)** ### **%s.** -- deposit tree clean ; b537 tools naming the platform`s address %s ; token hits in b537 files %s.'
         % (w(sc['n4']), sc['zenodo_tools'] or 'NONE', sc['token']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- %s' % (w(sc['s1']), mj.get('roster_line')),
         '  **(S2)** ### **%s.** -- mirror_verify on the final zip, the head block in place.' % w(sc['s2']),
         '  **(S3)** ### **%s.** -- git status of tools/mirror_prevbuild.json after the build : %r.' % (w(sc['s3']), mj.get('prevbuild_git_status')),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in n].count(True), [sc[k] for k in n].count(False), [sc[k] for k in s].count(True), [sc[k] for k in s].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in rd(os.path.join(D, 'b537_defects.txt')).rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b537_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    put_json('b537_scores.json', sc)
    print(NL.join(L))


def trail():
    sc, mj, mm = scores(), jl('b537_mirror.json'), jl('b537_memory.json')
    wo, _ = wo_lines()
    body = [
        '', HEADING, '',
        '**(R147) ratified.** (1) The author`s word under (R145)(7) is given: the mirror export built and the seat`s memory refreshed, '
        'both carrying the standing after b536. (2) The export in (R69)`s form. (3) The seat`s memory entry for b533–b536. (4) Two '
        'work-orders named, not started.',
        '',
        '**The export.** `mirror-refresh-2026-09-25-b537.zip`, by the builder `tools/mirror_build.ps1` unedited, from PLACE-papers `%s`; '
        '%s entries (%s files and the MANIFEST); sha256 `%s`. The last export read was `mirror-refresh-2026-09-25-b534.zip`, built by '
        'b534 at `3b5532a`. Documents added since it: %s. The builder`s roster line: *%s* `mirror_verify.py` on the final zip: CLEAN on '
        'all three clauses. The MANIFEST`s head carries the ceiling of `(R146)`(2) once and the last commit of the five repositories, '
        'local and remote both full, with `v0.1` = `%s` and `v0.2` = `%s` beside SIDE-explicit-formula`s line. The navigator reads the '
        'mirror after the author uploads it; until then the ledgers on D: remain the currency authority.'
        % ((mj.get('pp_local') or '')[:7], mj.get('entries'), mj.get('files_excl_manifest'), mj.get('zip_sha256'),
           ', '.join(mj.get('additions_since_3b5532a') or []) or 'NONE', mj.get('roster_line'), V01, V02),
        '',
        '**The ceiling at the head, verbatim:** *%s*' % ceiling(),
        '',
        '**The memory.** One new entry in the seat`s memory, `%s` (%s lines), in its own form; one index line appended; no earlier entry '
        'edited (the pre-seal hashes: changed %s, added %s). It states the ceiling verbatim, both tags with their full SHAs, and: '
        '*Not claimed: %s*' % (ENTRY, mm.get('lines'), mm.get('changed'), mm.get('added'), NOT_CLAIMED),
        '',
        '**The work-orders**, named and not started:', ''] + wo + [
        '',
        '**Defects of this act**, in the desk: (a) a glob delete after an unchained `cd`, refused by the author before it ran, and the '
        'standing rule the author gave filed in the seat`s memory; (b) the head block first written at the MANIFEST`s end, repaired by '
        '`rehead` and re-verified.',
        '',
        '**(N1) %s · (N2) %s · (N3) %s · (N4) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
        % tuple(w(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
        '**No kernel lane opened at this act.** Nothing deposits; nothing at Zenodo written or read; no grade conferred or moved; row U1 '
        'unedited; `h2` where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH.',
        '']
    before = open(OT, 'rb').read()
    if HEADING.encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(HEADING))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b537_trail_notes.json', out)


if __name__ == '__main__':
    sys.exit({'memory': memory, 'workorders': workorders, 'components': components, 'desk': desk, 'trail': trail}[sys.argv[1]]())
