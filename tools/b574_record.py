# -*- coding: utf-8 -*-
"""b574_record.py -- THE ACT'S RECORD TOOL, UNDER (R184). ### ONE SUBCOMMAND PER BANK.

### ### b574: LANE THREE, ACT TWO -- CP-5, THE DEPOSIT RECONCILIATION. NOTHING AT ZENODO IS WRITTEN. Subcommands write only `data/b574_*` unless the docstring names a
### ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then `os.replace`).
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import e0_rule as E0   # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
EF = 'D:/SIDE-explicit-formula'
PP = 'D:/MY-DOwnloads/PLACE-papers'
V014 = '4dce7b97eb29733b823919bd80b08d01c82c6d8f'
STD3 = ['propext', 'Classical.choice', 'Quot.sound']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


DEFECTS = [
    '(a) THE FACE`S READING (v) TOOK EACH DEPOSITED FILE`S md5 FROM ITS COMMITTED BLOB: git stores outputs/DEPOSITED-v1.1.2 '
    'LF-normalized (core.autocrlf), the deposit carries the bytes as written with CRLF; two files (A_Place_to_Stand.md, ERRATA.md) '
    'read DIFFER by line endings alone on the first run -- the standing BOM/autocrlf trap. The bank prints the blob`s md5 as declared '
    'and the CRLF-restored md5 beside it; the verdict reads the latter, which equals the working tree and the fetch.',
    '(b) THE FACE`S READING (vi) EXTRACTOR GAVE EACH RECORD ID ITS LINE`S FIRST VERSION: on lines naming several records (README :154, '
    'SPIRAL_MAP :54) every id took one version, and an id named twice counted twice -- matcher v1 hit 16, 13 of them artefacts. '
    'Matcher v2 takes the nearest version before each distinct id; both yields are printed and every hit line hand-read.',
    '(c) THE LOCK GATE REFUSED THE FACE ONCE: paragraph (A) named G-CHAIN-PAGE with HEAD and blob but no side word; "the suite reads it '
    'pre-push and post-push, the pages` blobs unchanged by the push" added before the seal (data/b574_lockgate_notes.txt refused, '
    '_notes2.txt permitted).',
    '(d) THE SCORING`S PAGE PREDICATE READ A NEEDLE THE BANK DOES NOT PRINT ("PASS 2 of 2"; the bank prints two "G-CHAIN-PAGE : '
    'PASS" lines) and scored N1 and S3 REFUTED on its first run; the predicate now counts the lines and prints its yield.',
    '(e) THE SUITE`S FIRST RUN FAILED G-NO-ZENODO-CALL AND G-DELETE-FREE LIVE ON ITS OWN TEXT: the positive controls` mutation '
    'literals (a PUT method, a remove call) were written out in the suite, one of the tools the arms read -- an arm that catches '
    'its author. The literals are now built by concatenation; the GET clause reads the record tool by name.',
]


def defects():
    put_txt('b574_defects.txt', ['### b574 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def _Q():
    import b566_record as R6
    return R6.Q


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay chain_page.py (the Correspondence selection; the variant constants)', RELAY, '69c2ae5a', 'tools/chain_page.py', [None]),
    ('PLACE-papers REGISTRY (the deposit rows; the kernel note; the DEPOSIT-PIN table)', PP, 'HEAD', 'REGISTRY.md', [94, 98, 414, 418, 419, 698]),
    ('PLACE-papers REGISTRY (the ceiling lines)', PP, 'HEAD', 'REGISTRY.md', [950, 952, 954, 956, 958, 960]),
    ('PLACE-papers README (the ceiling lines)', PP, 'HEAD', 'README.md', [113, 115, 117, 119, 121, 123, 125]),
    ('PLACE-papers SPIRAL_MAP (the deposit table)', PP, 'HEAD', 'SPIRAL_MAP.md', [40, 41, 49, 50, 52, 86, 327]),
    ('PLACE-papers ERRATA (the index)', PP, 'HEAD', 'ERRATA.md', [280, 281, 282, 283, 284, 285, 286]),
    ('relay b535`s route (the anonymous fetch-back)', RELAY, 'HEAD', 'tools/b535_zenodo.py', [240]),
    ('PLACE-papers OPEN_TRAILS (Anomaly 1 routed to CP-5)', PP, 'HEAD', 'OPEN_TRAILS.md', [11354]),
]


def reads():
    L = ['b574 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, lines in READS:
        src = g(repo, 'show', '%s:%s' % (rev, path))
        sl = src.split(NL)
        if lines == [None]:
            lines = [i for i, l in enumerate(sl, 1) if l.startswith('def corr_select') or l.startswith('DIR_PAGE_NAME')
                     or 'not n.startswith(SCHEMA_PREFIX)' in l]
        L.append('### %s -- %s @ %s' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip()))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8').read().split(NL)
    wg = [i for i, l in enumerate(ot, 1) if l.startswith('### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')]
    L.append('### PLACE-papers OPEN_TRAILS -- the W-ORD-GRH-WEIL heading at :%s' % wg)
    for e in ERRATA_IDS:
        er = io.open(os.path.join(PP, 'ERRATA.md'), encoding='utf-8').read().split(NL)
        L.append('### ERRATA %s : %s' % (e, [i for i, l in enumerate(er, 1) if e in l]))
    put_txt('b574_reads.txt', L)


ERRATA_IDS = ['E-2026-09-25-1', 'E-2026-09-25-2', 'E-2026-09-25-3', 'E-2026-09-25-4', 'E-2026-09-25-5', 'E-2026-09-25-6',
              'E-2026-09-27-1']


# ================================================================================ COMPONENT 2: THE FETCH (GET ONLY)
API = 'https://zenodo.org/api/records/'
RECORDS = [('21539167', 'the deposit: A Place To Stand v1.1.2'), ('21520474', 'SIDE-kernel v1.5 (Anomaly 1)')]


def fetch():
    """### Component 2: two anonymous GETs (no Authorization header; the token variable is never read); each response banked
    ### whole as data/b574_fetch_<id>.json; the file list, md5s and description printed verbatim into data/b574_zenodo_fetch.txt."""
    import urllib.request
    L = ['b574 -- COMPONENT 2: THE ZENODO FETCH, (R184)(4)(a) -- READ ONLY: anonymous GET, no Authorization header, no token read', '']
    out = {}
    for rid, what in RECORDS:
        url = API + rid
        req = urllib.request.Request(url, method='GET', headers={'Accept': 'application/json', 'User-Agent': 'relay-b574-read'})
        t0 = utc()
        with urllib.request.urlopen(req, timeout=60) as r:
            status, body = r.status, r.read()
        sent_auth = req.has_header('Authorization')
        open(os.path.join(D, 'b574_fetch_%s.json.tmp' % rid), 'wb').write(body)
        os.replace(os.path.join(D, 'b574_fetch_%s.json.tmp' % rid), os.path.join(D, 'b574_fetch_%s.json' % rid))
        d = json.loads(body.decode('utf-8'))
        m = d.get('metadata', {})
        rel = (m.get('relations') or {}).get('version') or [{}]
        L += ['### REQUEST : GET %s ; Authorization header sent : %s ; at (UTC) %s ; HTTP %s ; %d bytes ; banked whole as data/b574_fetch_%s.json'
              % (url, sent_auth, t0, status, len(body), rid),
              '### %s' % what,
              '    id %s ; doi %s ; conceptdoi %s ; title %s' % (d.get('id'), d.get('doi'), d.get('conceptdoi'), m.get('title')),
              '    version %s ; publication_date %s ; modified %s ; is_last %s ; versions index %s of %s'
              % (m.get('version'), m.get('publication_date'), d.get('modified'), rel[0].get('is_last'), rel[0].get('index'),
                 rel[0].get('count')),
              '    files (%d), key / size / checksum as the record states them:' % len(d.get('files') or [])]
        for f in sorted(d.get('files') or [], key=lambda f: f.get('key')):
            L.append('      %-40s %10s  %s' % (f.get('key'), f.get('size'), f.get('checksum')))
        L += ['    description, verbatim:', '      ' + (m.get('description') or '').replace(NL, NL + '      '), '']
        out[rid] = dict(url=url, at=t0, status=status, auth=sent_auth, version=m.get('version'), doi=d.get('doi'),
                        conceptdoi=d.get('conceptdoi'), pubdate=m.get('publication_date'), is_last=rel[0].get('is_last'),
                        files={f.get('key'): f.get('checksum') for f in (d.get('files') or [])}, description=m.get('description') or '',
                        title=m.get('title'))
    put_txt('b574_zenodo_fetch.txt', L)
    put_json('b574_zenodo_fetch.json', out)
    print({k: (v['version'], len(v['files']), v['is_last']) for k, v in out.items()})


# ================================================================================ COMPONENT 1: the lines
def weight():
    """### PLACE-papers FINDINGS.md (two appended lines): (R184)(1) -- b573 at its weight; the lemma-walk instrument."""
    Q = _Q()
    e = Q.line_of(Q.FIND, '## GRH-Weil, act eight: the criterion over a configuration')
    h1 = '*Appended 2026-10-01 by b574 to b573’s entry (:%s), under `(R184)`(1) -- b573 AT ITS WEIGHT:*' % e
    h2 = '*Appended 2026-10-01 by b574 to b573’s entry (:%s), under `(R184)`(1) -- AN INSTRUMENT OF THE METHOD CANON, THE LEMMA WALK:*' % e
    Q.guard_absent(Q.FIND, h1)
    a1 = ('\n%s SIDE-explicit-formula v0.15 = `21c8c52`, tagged by the push script and read back: over a configuration with an explicit '
          'formula, a local count and a target, Weil positivity on classK is equivalent to the target, 22 declarations at the standard '
          'three, no sorryAx on main; ζ and every primitive χ ≠ 1 compiled as instances, each checked by the definition to carry exactly '
          'the statement of its existing equivalence. Equivalences between open statements; nothing proved. H25a, H25c held; H25b refuted '
          'by one proof, the assembly’s explicit-formula step shortened from four lines to one rewrite by the field -- a finding about '
          'the instance’s plumbing, not the schema. The page at the Dirichlet instance, 18 nodes, byte-identical on two runs, its last '
          'line the successor sentence byte for byte; the suite 76 of 76.\n' % h1)
    a2 = ('\n%s a constant walk from a terminal through every kernel declaration it consumes, each classified by whether its statement '
          'or its proof names the instance (relay `data/b572_crit_probe.lean.txt`, `data/b572_lemmas.txt`); it priced the schema exactly '
          '(relay `data/b572_schema.json`, `data/b573_fields.txt`).\n' % h2)
    r = [Q.append_to(Q.FIND, a1), Q.append_to(Q.FIND, a2)]
    put_json('b574_weight.json', dict(entry=e, lines=[Q.line_of(Q.FIND, h1), Q.line_of(Q.FIND, h2)], appends=r))
    print(jl('b574_weight.json'))


REMAINDERS = [
    ('THE χ-LI CONVERSE AT χ', '(V1)-(V4) at χ, with the pairing across (χ, χ⁻¹) in (V1)'),
    ('THE FAMILY FORM OVER ALL χ MODULO q', 'the sum of the χ-forms, orthogonality turning the prime side into primes in residue classes, '
                                            'the conductor terms adding'),
    ('THE IMPRIMITIVE AND PRINCIPAL CHARACTERS', 'the instances the primitive hypothesis excludes'),
    ('THE SELBERG-CLASS INSTANCES BEYOND DIRICHLET', 'each waiting on an explicit formula the rev does not hold'),
]


def word_close():
    """### PLACE-papers OPEN_TRAILS.md (five appended lines): (R184)(3) -- W-ORD-GRH-WEIL closed at its landing; its four remainders."""
    Q = _Q()
    wg = Q.line_of(Q.OT, '### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC')
    h = '*Appended 2026-10-01 by b574, under the author’s ruling `(R184)`(3), to the W-ORD-GRH-WEIL entry (:%s)' % wg
    Q.guard_absent(Q.OT, h + ' -- CLOSED')
    a = ('\n%s -- CLOSED AT ITS LANDING:* eight acts from the 31 items of b555: the explicit formula for primitive χ (v0.13), the '
         'criterion for χ (v0.14), the schema with ζ and χ as instances (v0.15). Its remainders are named below as priced items, each '
         'NOT STARTED, each with its trigger the author’s word.\n' % h)
    r = [Q.append_to(Q.OT, a)]
    for i, (name, what) in enumerate(REMAINDERS, 1):
        r.append(Q.append_to(Q.OT, '\n%s -- REMAINDER %d, A PRICED ITEM, NOT STARTED, %s:* %s. Trigger: the author’s word.\n' % (h, i, name, what)))
    lines = [i for i, l in enumerate(Q.rd(Q.OT).split(NL), 1) if l.startswith(h)]
    put_json('b574_word.json', dict(wg=wg, lines=lines, appends=r))
    print(jl('b574_word.json'))


# ================================================================================ COMPONENT 3: THE PINS
def _blob(repo, spec):
    r = subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def pins():
    """### Component 3: the deposit's files (the corpus's deposited copy and b535's fetch-back) against the fetch, md5 by file;
    ### REGISTRY's statements about the two records against the fetch; Anomaly 1 from the fetch. Banks data/b574_pins.txt (.json)."""
    import hashlib
    F = jl('b574_zenodo_fetch.json')
    dep = F['21539167']
    ls = g(PP, 'ls-tree', '--name-only', 'HEAD', 'outputs/DEPOSITED-v1.1.2/').split(NL)
    local, local_crlf = {}, {}
    for p in [x for x in ls if x.strip()]:
        b = _blob(PP, 'HEAD:' + p)
        local[os.path.basename(p)] = 'md5:' + hashlib.md5(b).hexdigest() if b is not None else None
        # ### defect (a): git stores these files LF-normalized (core.autocrlf); the deposit carries the bytes as written, CRLF.
        # ### The blob's md5 is printed as the face declared it; the verdict reads the blob with its CRLF restored.
        local_crlf[os.path.basename(p)] = ('md5:' + hashlib.md5(b.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')).hexdigest()
                                           if b is not None else None)
    prior = {f['key']: f['checksum'] for f in jl('b535_fetchback_21539167.json').get('files', [])}
    keys = sorted(set(dep['files']) | set(local) | set(prior))
    lfonly = []
    L = ['b574 -- COMPONENT 3: THE PIN COMPARISON, (R184)(4)(b) -- THE FETCH (data/b574_zenodo_fetch.txt) AGAINST THE DEPOSIT`S FILE LIST',
         '### AS THE CORPUS HOLDS IT (PLACE-papers HEAD outputs/DEPOSITED-v1.1.2/, md5 of each committed blob) AND b535`S FETCH-BACK',
         '### (data/b535_fetchback_21539167.json); no file named MANIFEST exists for the deposit (reading (v)).', '',
         '### the corpus copy is printed twice: its committed blob`s md5 (LF, as git stores it) and with CRLF restored (the bytes as',
         '### deposited, which the working tree carries); the verdict reads the CRLF-restored copy (defect (a)).', '',
         '    %-30s %-38s %-38s %-38s %-38s %s' % ('file', 'the fetch', 'the corpus copy (blob, LF)', 'the corpus copy (CRLF restored)',
                                                 'b535`s fetch-back', 'verdict')]
    mism = []
    for k in keys:
        a, b, bc, c = dep['files'].get(k), local.get(k), local_crlf.get(k), prior.get(k)
        ok = a is not None and a == c and a in (b, bc)
        if not ok:
            mism.append(dict(file=k, fetch=a, copy=b, copy_crlf=bc, prior=c))
        if ok and a != b:
            lfonly.append(k)
        L.append('    %-30s %-38s %-38s %-38s %-38s %s' % (k, a, b, bc, c, ('AGREE' + (' (as deposited, CRLF)' if a != b else '')) if ok else '### DIFFER'))
    L += ['', '### ### **FILES: %d ; DIFFERING: %d.** ### files agreeing only with CRLF restored (the committed blob`s md5 differs by line '
          'endings alone): %s' % (len(keys), len(mism), lfonly or 'NONE'), '']
    reg = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8').read().split(NL)
    kern = F['21520474']
    facts = []
    # ### REGISTRY's statements about the two records, each read off its own line and compared with the fetch
    for i, l in enumerate(reg, 1):
        if '21539167' in l and 'CURRENT IMMUTABLE ZENODO STATE' in l:
            for kind, rx, fv in (('version', r'\*\*(v1\.1\.2)\*\*', dep['version']), ('doi', r'DOI \*\*(10\.5281/zenodo\.\d+)\*\*', dep['doi']),
                                 ('concept', r'concept (10\.5281/zenodo\.\d+)', dep['conceptdoi']),
                                 ('date', r'\*\*(20\d\d-\d\d-\d\d)\*\*', dep['pubdate'])):
                m = re.search(rx, l)
                facts.append(dict(line=i, record='21539167', kind=kind, registry=m.group(1) if m else None, fetch=fv))
        if '`v1.5` = `0e5233f`' in l and '21520474' in l:
            for kind, rx, fv in (('version', r'`(v1\.5)` = `0e5233f`', kern['version']),
                                 ('version doi', r'version DOI `(10\.5281/zenodo\.\d+)`', kern['doi']),
                                 ('concept', r'concept DOI `(10\.5281/zenodo\.\d+)`', kern['conceptdoi'])):
                m = re.search(rx, l)
                facts.append(dict(line=i, record='21520474', kind=kind, registry=m.group(1) if m else None, fetch=fv))
            m = re.search(r'\*\*`(v\d+\.\d+)`, HEAD `([0-9a-f]+)`', l)
            facts.append(dict(line=i, record='21520474', kind='WORKING-HEAD (REGISTRY`s dated reading) against the record`s version',
                              registry=('%s, HEAD %s' % m.groups()) if m else None, fetch='%s (is_last %s)' % (kern['version'], kern['is_last'])))
    L += ['### REGISTRY`S STATEMENTS ABOUT THE TWO RECORDS, AGAINST THE FETCH:']
    pdiff = []
    for f in facts:
        same = (f['registry'] == f['fetch']) or (f['registry'] and f['fetch'] and f['registry'] in str(f['fetch']))
        f['agree'] = bool(same)
        if not same:
            pdiff.append(f)
        L.append('    REGISTRY :%-5d %-9s %-60s registry %-28s fetch %-28s %s' % (f['line'], f['record'], f['kind'][:60], f['registry'],
                                                                                 f['fetch'], 'AGREE' if same else '### DIFFER'))
    live = g('D:/SIDE-kernel', 'tag', '--sort=-creatordate').split(NL)[0].strip()
    livesha = g('D:/SIDE-kernel', 'rev-parse', '--short=7', live + '^{commit}').strip()
    L += ['', '### ANOMALY 1, FROM THE FETCH: the SIDE-kernel record 21520474 states version %s (is_last %s among its versions); the '
          'kernel`s latest tag is %s = %s (git, read now); REGISTRY`s DEPOSIT-PIN is v1.5 = 0e5233f and its dated WORKING-HEAD reading '
          'v1.7. The deposited kernel is v1.5; the kernel has moved past it by tags no deposit carries.' % (kern['version'], kern['is_last'],
                                                                                                            live, livesha),
          '### ### **PIN DIFFERENCES BETWEEN REGISTRY AND THE FETCH: %d** -- %s' % (len(pdiff), [(d['line'], d['kind']) for d in pdiff])]
    put_txt('b574_pins.txt', L)
    put_json('b574_pins.json', dict(files=keys, mismatch=mism, lf_only=lfonly, facts=facts, pin_differences=pdiff, kernel_latest=[live, livesha],
                                    kernel_record=kern['version'], kernel_is_last=kern['is_last']))
    print('files', len(keys), 'differing', len(mism), '; pin differences', len(pdiff))

# ================================================================================ COMPONENT 4: README AND SPIRAL_MAP AGAINST REGISTRY
PIN_RX = re.compile(r'(SIDE-[A-Za-z0-9-]+)[^|\n]{0,60}?\b(v\d+(?:\.\d+)+)\b`?\**\s*(?:=|\(|·)\s*\**`?([0-9a-f]{7})')
ZEN_RX = re.compile(r'zenodo\.(\d{7,8})')
VER_RX = re.compile(r'\bv(\d+(?:\.\d+)+)\b')
CNT_RX = re.compile(r'\b(\d+) files\b')
CEIL_RX = re.compile(r"(?:Appended|Reworded) under the author's ruling `\((R\d+)\)`\((\d+)\)|THE CEILING LINE, `\((R\d+)\)`\((\d+)\)")


def _ceiling_sentence(line):
    for opener in ("Supportable, the author's sentence: *", 'Supportable, the author’s sentence: *', 'Supportable: *', ':** *'):
        a = line.find(opener)
        if a >= 0:
            b = line.find('*', a + len(opener))
            return line[a + len(opener):b] if b > 0 else line[a + len(opener):]
    return None


def facts_of(text, matcher='v1'):
    """### v1: each record id on a line takes the line's first version (reading (vi) as written). v2: each distinct record id
    ### takes the nearest version token ending within 60 characters before it, or none -- v1 handed the line's first version
    ### to every id on a line naming several records (README :154, SPIRAL_MAP :54), and counted a twice-named id twice."""
    out = []
    for i, l in enumerate(text.split(NL), 1):
        for m in PIN_RX.finditer(l):
            out.append(dict(kind='pin', key=(m.group(1), m.group(2)), value=m.group(3), line=i))
        if matcher == 'v2':
            seen = set()
            for m in ZEN_RX.finditer(l):
                z = m.group(1)
                if z in seen:
                    continue
                seen.add(z)
                pre = [v for v in VER_RX.finditer(l[:m.start()]) if m.start() - v.end() <= 60]
                if pre:
                    out.append(dict(kind='record-version', key=(z,), value='v' + pre[-1].group(1), line=i))
            cs = CNT_RX.findall(l)
            if cs and len(set(ZEN_RX.findall(l))) == 1:
                out.append(dict(kind='record-files', key=(ZEN_RX.findall(l)[0],), value=cs[0], line=i))
        zs = ZEN_RX.findall(l) if matcher == 'v1' else []
        if zs:
            vs = VER_RX.findall(l)
            cs = CNT_RX.findall(l)
            for z in zs:
                if vs:
                    out.append(dict(kind='record-version', key=(z,), value='v' + vs[0], line=i))
                if cs and len(zs) == 1:
                    out.append(dict(kind='record-files', key=(z,), value=cs[0], line=i))
        m = CEIL_RX.search(l)
        if m:
            rid = (m.group(1) or m.group(3)) + '(' + (m.group(2) or m.group(4)) + ')'
            s = _ceiling_sentence(l)
            if s is not None:
                out.append(dict(kind='ceiling', key=(rid,), value=' '.join(s.split()), line=i))
    return out


def ledgers():
    """### Component 4: README and SPIRAL_MAP against REGISTRY at every pin, record version, file count and ceiling sentence the
    ### extractors find; every difference printed with both readings and line numbers. Both matcher versions' yields printed; the
    ### verdict reads v2, its residue hand-read (HAND_READ). Banks data/b574_ledgers.txt (.json). No edit."""
    texts = {f: io.open(os.path.join(PP, f), encoding='utf-8').read().replace(chr(13), '') for f in ('REGISTRY.md', 'README.md', 'SPIRAL_MAP.md')}
    L = ['b574 -- COMPONENT 4: README AND SPIRAL_MAP AGAINST REGISTRY, (R184)(4)(c) -- THE EXTRACTORS OF READING (vi), NO EDIT', '',
         '### extractors: pin %s ; record id %s with a version %s ; count %s beside a single record id ; ceiling lines %s '
         '(the supportable sentence compared)' % (PIN_RX.pattern, ZEN_RX.pattern, VER_RX.pattern, CNT_RX.pattern, CEIL_RX.pattern),
         '### matcher v1: an id takes its line`s first version (as reading (vi) was written); matcher v2: each distinct id takes the '
         'nearest version ending within 60 characters before it, or none (defect (b)).', '']
    res = {}
    for mv in ('v1', 'v2'):
        reg = facts_of(texts['REGISTRY.md'], mv)
        regmap = {}
        for f in reg:
            regmap.setdefault((f['kind'],) + f['key'], []).append(f)
        diffs, yields = [], {'REGISTRY.md': len(reg)}
        for name in ('README.md', 'SPIRAL_MAP.md'):
            fs = facts_of(texts[name], mv)
            yields[name] = len(fs)
            for f in fs:
                key = (f['kind'],) + f['key']
                rv = regmap.get(key, [])
                if not rv:
                    d = dict(file=name, line=f['line'], kind=f['kind'], key=list(f['key']), value=f['value'], registry=None,
                             reg_lines=[], why='SILENT')
                elif f['value'] not in [x['value'] for x in rv]:
                    d = dict(file=name, line=f['line'], kind=f['kind'], key=list(f['key']), value=f['value'],
                             registry=sorted(set(x['value'] for x in rv)), reg_lines=[x['line'] for x in rv], why='CONTRADICTS')
                else:
                    continue
                diffs.append(d)
        res[mv] = dict(diffs=diffs, yields=yields)
        L.append('### matcher %s : facts found %s ; hits %d (contradicting %d, REGISTRY silent %d)'
                 % (mv, yields, len(diffs), sum(d['why'] == 'CONTRADICTS' for d in diffs), sum(d['why'] == 'SILENT' for d in diffs)))
    L.append('')
    for mv in ('v1', 'v2'):
        L.append('### THE HITS OF MATCHER %s, each with both readings:' % mv)
        for d in res[mv]['diffs']:
            L.append('    %s %s :%-5d %-15s %-30s %s reads %r ; REGISTRY %s' % (d['why'], d['file'], d['line'], d['kind'], ' '.join(d['key'])[:30],
                     d['file'], d['value'][:120], ('reads %r at :%s' % (d['registry'], d['reg_lines']))[:200] if d['registry'] else 'does not state it'))
        L.append('')
    L.append('### THE HAND-READ OF EVERY LINE EITHER MATCHER HIT (the line read whole by the seat):')
    hit_lines = sorted(set((d['file'], d['line']) for mv in res for d in res[mv]['diffs']))
    for fl in hit_lines:
        L.append('    %s :%-5d %s' % (fl[0], fl[1], HAND_READ.get(fl, '### NOT HAND-READ')))
    d2 = res['v2']['diffs']
    con = [d for d in d2 if d['why'] == 'CONTRADICTS']
    sil = [d for d in d2 if d['why'] == 'SILENT']
    by = {}
    for d in d2:
        by['%s/%s' % (d['file'], d['kind'])] = by.get('%s/%s' % (d['file'], d['kind']), 0) + 1
    big = max(by.items(), key=lambda x: x[1]) if by else None
    ceil = {n: sum(1 for f in facts_of(texts[n], 'v2') if f['kind'] == 'ceiling') for n in texts}
    L += ['', '### ceiling sentences found per file: %s ; ceiling differences: %d' % (ceil, sum(1 for d in d2 if d['kind'] == 'ceiling')),
          '### clusters (file/kind), matcher v2: %s ; the largest: %s' % (by, ('%s (%d)' % big) if big else 'NONE'),
          '### ### **DIFFERENCES IN TOTAL (matcher v2): %d -- %d WHERE REGISTRY STATES IT OTHERWISE, %d WHERE REGISTRY DOES NOT STATE IT.**'
          % (len(d2), len(con), len(sil)),
          '### ### matcher v1 (reading (vi) as written) hit %d; its excess over v2 is the defect (b) artefact, every hit line hand-read above.'
          % len(res['v1']['diffs'])]
    # ### the positive control: two mutations of README in memory (the deposit's Zenodo version at :154; one word of the first
    # ### ceiling sentence); matcher v2 must report each as REGISTRY stating it otherwise, and the unmutated text nothing.
    def _contra(x):
        regv2 = facts_of(texts['REGISTRY.md'], 'v2')
        out = []
        for f in facts_of(x, 'v2'):
            vals = [g['value'] for g in regv2 if (g['kind'],) + g['key'] == (f['kind'],) + f['key']]
            if vals and f['value'] not in vals:
                out.append((f['line'], f['kind']))
        return out
    t0 = texts['README.md']
    m1 = t0.replace('Zenodo **v1.1.2** ([10.5281', 'Zenodo **v1.1.3** ([10.5281', 1)
    w = [f for f in facts_of(t0, 'v2') if f['kind'] == 'ceiling'][0]['value'].split()[3]
    m2 = m1.replace(w, 'XXXX', 1)
    ctrl = dict(unmutated=_contra(t0), mutated=_contra(m2), mutations=['v1.1.2 -> v1.1.3 at the first "Zenodo **v1.1.2** ([10.5281"',
                                                                      '%r -> XXXX at its first occurrence' % w])
    ctrl['fires'] = (ctrl['unmutated'] == [] and ('record-version' in [k for _, k in ctrl['mutated']])
                     and ('ceiling' in [k for _, k in ctrl['mutated']]))
    L += ['', '### POSITIVE CONTROL (matcher v2, README mutated in memory, nothing written): mutations %s ; unmutated hits %s ; mutated hits %s ; '
          'FIRES: %s' % (ctrl['mutations'], ctrl['unmutated'], ctrl['mutated'], ctrl['fires'])]
    put_txt('b574_ledgers.txt', L)
    put_json('b574_ledgers.json', dict(control=ctrl, v1=res['v1'], v2=res['v2'], contradicting=len(con), silent=len(sil), total=len(d2),
                                       clusters=by, largest=big[0] if big else None, ceiling=ceil))
    print('v1', len(res['v1']['diffs']), '; v2', len(d2), 'contradicting', len(con), 'silent', len(sil), by, ceil)


HAND_READ = {
    ('README.md', 154): 'the deposit note: monograph manuscript v5.10.2 / Zenodo v1.1.2 at 21539167 (concept 19675355), lv v0.10.0 = 93c27ec at '
                        '21539068 (concept 21433177), the T7 record 21436282 (concept 21436281), live monograph v5.13 -- every figure '
                        'REGISTRY states, it states alike (:77, :83, :102, :419); the T7 record REGISTRY does not name. NOT A DIFFERENCE '
                        'AGAINST REGISTRY: v1 gave all six ids the line`s first version, v5.10.2.',
    ('SPIRAL_MAP.md', 41): 'the frozen v1.1 deposit row: SIDE-kernel v1.1, 19937590, "83 files, 0 sorry, 0 axioms" -- REGISTRY does not state '
                           'the v1.1 record or its count. REGISTRY SILENT.',
    ('SPIRAL_MAP.md', 54): 'the live-kernel reconciliation: "against tag v1.4 = f374174 ... the current published deposit is v1.5 (0e5233f, '
                           'DOI 10.5281/zenodo.21520474)" -- v1.5 at 21520474 agrees with REGISTRY :700. NOT A DIFFERENCE: v1 gave the '
                           'id the line`s first version, the reconciliation tag v1.4.',
    ('SPIRAL_MAP.md', 140): 'SIDE-t7-topology-cmb v0.3 (8eb0d5a), the T7 kernel note -- REGISTRY carries no pin for this kernel. REGISTRY SILENT.',
    ('SPIRAL_MAP.md', 533): 'SIDE-silence-principle v0.2.0 = 667c254, appended by b558 under (R168)(2)(a) to the Foundations row -- REGISTRY '
                            'carries no pin for this kernel. REGISTRY SILENT.',
}


# ================================================================================ COMPONENT 5: THE ERRATA AND THE DRAFT
RULED_INTO = {'E-2026-09-25-1': '(R145)(4) at b535: the three (R110) description edits name it (relay data/b535_ferry.txt :43-:51)'}
DRAFT_RULINGS = ['(R177)(2)', '(R182)(2)', '(R183)(3)']


def errata():
    """### Component 5(d): each erratum located in ERRATA (heading, index line, its own label) and in the two fetched descriptions."""
    F = jl('b574_zenodo_fetch.json')
    er = io.open(os.path.join(PP, 'ERRATA.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    L = ['b574 -- COMPONENT 5(d): THE SEVEN ERRATA, (R184)(4)(d) -- LOCATED IN ERRATA AND IN THE FETCHED DESCRIPTIONS', '']
    rows = []
    for e in ERRATA_IDS:
        hits = [i for i, l in enumerate(er, 1) if e in l]
        head = [i for i in hits if er[i - 1].startswith('## ' + e) or er[i - 1].startswith('**`' + e)]
        idx = [i for i in hits if er[i - 1].startswith('- `' + e)]
        lab = re.findall(r'\(([A-Z][A-Z \-;,.0-9v]+(?:FACING|RETAINED)[^)]*)\)', er[head[0] - 1]) if head else []
        if not lab and head and 'DESCRIPTION EDITS' in er[head[0] - 1]:
            lab = ['THE RECORD OF b535`S PLATFORM EDITS']
        indesc = {rid: (e in F[rid]['description']) for rid in F}
        ruled = RULED_INTO.get(e)
        rows.append(dict(id=e, heading=head, index=idx, label=lab, in_description=indesc, ruled=ruled))
        L.append('    %-15s heading :%s ; index :%s ; label %s ; ruled into a description: %s ; in the fetched descriptions %s'
                 % (e, head, idx or '-', lab or '-', ruled or 'NO', indesc))
    ruled = [r for r in rows if r['ruled']]
    present = [r for r in ruled if any(r['in_description'].values())]
    L += ['', '### ### **ERRATA A RULING PLACED IN A DESCRIPTION: %d ; PRESENT IN THE FETCH: %d ; ABSENT: %s.**'
          % (len(ruled), len(present), [r['id'] for r in ruled if r not in present] or 'NONE')]
    put_txt('b574_errata.txt', L)
    put_json('b574_errata.json', dict(rows=rows, ruled=[r['id'] for r in ruled], present=[r['id'] for r in present]))
    print([(r['id'], r['ruled'] is not None, r['in_description']) for r in rows])


def draft():
    """### Component 5(e): the description edit drafted from the three ceiling sentences the description does not yet carry, in the
    ### author's words read from REGISTRY; banked as data/b574_description_draft.txt and written nowhere else."""
    F = jl('b574_zenodo_fetch.json')
    reg = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    picked = []
    for rid in DRAFT_RULINGS:
        r, n = rid[1:].split(')(')
        mk = "Appended under the author's ruling `(%s)`(%s)" % (r, n.rstrip(')'))
        ls = [(i, l) for i, l in enumerate(reg, 1) if mk in l]
        s = _ceiling_sentence(ls[0][1]) if ls else None
        picked.append(dict(ruling=rid, line=ls[0][0] if ls else None, sentence=' '.join(s.split()) if s else None,
                           in_description=bool(s) and any(' '.join(s.split())[:60] in ' '.join(F[x]['description'].split()) for x in F)))
    L = ['b574 -- COMPONENT 5(e): THE (R110) DESCRIPTION EDIT, DRAFTED, (R184)(4)(e) -- PRINTED FOR RULING, WRITTEN NOWHERE BUT THIS BANK',
         '', '### written at (UTC) %s' % utc(),
         '### the three supportable ceiling sentences the deposit`s description does not yet carry, quoted whole from REGISTRY in the '
         'author`s words, in the order of their rulings:']
    for p in picked:
        L.append('###   %s, REGISTRY :%s ; in a fetched description already: %s' % (p['ruling'], p['line'], p['in_description']))
    L += ['', '### THE DRAFT (the sentences the description of record 21539167 would carry after the ceiling`s successor):', '']
    L += [p['sentence'] or '### NOT FOUND' for p in picked]
    L += ['', '### NOTE FOR THE RULING: the second sentence ((R182)(2)) ends "The criterion for χ is not yet composed"; the third '
          '((R183)(3)) states it composed. Carried together, the description would state both; the author rules which it carries.',
          '', '### NOTHING HERE IS WRITTEN AT ZENODO; THE AUTHOR RULES THE EDIT AT THE CLOSING.']
    put_txt('b574_description_draft.txt', L)
    put_json('b574_description_draft.json', dict(picked=picked))
    print([(p['ruling'], p['line'], bool(p['sentence']), p['in_description']) for p in picked])

# ================================================================================ COMPONENT 6 AND THE SCORING
SCORE_KEYS = ('H26a', 'H26b', 'H26c', 'H26d', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')
GEN = '69c2ae5a'
PUSHOUT = 'ea7b1f28'
V015 = '21c8c52'
ZPAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
CPAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
MANIFEST_SEARCH = ('git ls-files in PLACE-papers and relay, case-insensitive "manifest": PLACE-papers phase1.5/method/'
                   'METHODOLOGY_DAY_MANIFEST.md (a method-day list), relay data/zenodo-manifests/record_19675356.json and '
                   'record_21432399.json (other records), reports/2026-07-11-keystone-manifest.md -- none the deposit`s; the same query '
                   'finds REGISTRY.md (the control)')


def scores():
    P, Lg, E, F = jl('b574_pins.json'), jl('b574_ledgers.json'), jl('b574_errata.json'), jl('b574_zenodo_fetch.json')
    pr = rd('b574_page_runs.txt')
    # ### the yield, printed: four BYTE-IDENTICAL verdicts (two pages, run2 and HEAD) and two G-CHAIN-PAGE PASS lines
    nbi, npass = pr.count('BYTE-IDENTICAL'), len(re.findall(r'^G-CHAIN-PAGE : PASS ', pr, re.M))
    print('  page runs: BYTE-IDENTICAL %d ; G-CHAIN-PAGE PASS lines %d' % (nbi, npass))
    pages_ok = nbi == 4 and npass == 2
    lf = P.get('lf_only', [])
    letter = len(P['mismatch']) + len(lf)
    pd = P['pin_differences']
    anomaly = len(pd) == 1 and 'WORKING-HEAD' in pd[0]['kind']
    con, sil, tot = Lg['contradicting'], Lg['silent'], Lg['total']
    v1 = len(Lg['v1']['diffs'])
    ruled, present = E['ruled'], E['present']
    in_desc = {r['id']: any(r['in_description'].values()) for r in E['rows']}
    kmain = g(EF, 'rev-parse', '--short=7', 'main').strip()
    auth = any(v['auth'] for v in F.values())
    zpage_same = (subprocess.run(['git', '-C', PP, 'diff', '--quiet', 'HEAD', '--', ZPAGE, CPAGE]).returncode == 0)
    pp_changed = [x for x in g(PP, 'diff', '--name-only', 'HEAD').split(NL) if x.strip()]
    S = dict(
        H26a=('HELD' if letter == 0 else 'REFUTED',
              'against the deposit`s file list as reading (v) declared it (PLACE-papers HEAD outputs/DEPOSITED-v1.1.2/, the md5 of '
              'each committed blob): %d of %d files differ -- %s -- and by line endings alone: git holds them LF-normalized, the '
              'deposit holds the bytes as written, CRLF; with CRLF restored each equals the fetch, the working tree and b535`s '
              'fetch-back, and the other %d agree as committed (relay data/b574_pins.txt). No file named MANIFEST is the deposit`s (%s)'
              % (letter, len(P['files']), lf + [m['file'] for m in P['mismatch']], len(P['files']) - letter, MANIFEST_SEARCH)),
        H26b=('HELD' if anomaly else 'REFUTED',
              'REGISTRY`s statements about the two records against the fetch: %d differences, %s -- Anomaly 1: REGISTRY`s dated '
              'WORKING-HEAD reading v1.7 against the record`s v1.5 (is_last %s); the kernel`s latest tag %s; every pin, DOI, concept '
              'DOI and date agrees (relay data/b574_pins.txt)' % (len(pd), [(d['line'], d['registry'], d['fetch']) for d in pd],
                                                                 P['kernel_is_last'], P['kernel_latest'])),
        H26c=('HELD' if tot <= 12 else 'REFUTED',
              '%d differences in total under reading (vi) -- %d where REGISTRY states it otherwise, %d where REGISTRY does not state '
              'it (SPIRAL_MAP :41 the v1.1 record`s count, :140 and :533 two kernel pins); the ceiling sentences %s per file, none '
              'differing; matcher v1 as first written hit %d, its 13 extra hits artefacts of assigning a line`s first version to every '
              'record on it, each hit line hand-read; the positive control fires (relay data/b574_ledgers.txt)'
              % (tot, con, sil, Lg['ceiling'], v1)),
        H26d=('HELD' if ruled and set(ruled) == set(present) else 'REFUTED',
              'the errata a ruling ordered into a description: %s; present in the fetched descriptions: %s; every other erratum`s '
              'presence printed beside its label (relay data/b574_errata.txt)' % (ruled, present)),
        N1=('HELD' if pages_ok else 'REFUTED', 'both pages generated twice, each byte-identical to its committed copy at HEAD; '
                                                 'G-CHAIN-PAGE PASS 2 of 2 (relay data/b574_page_runs.txt)'),
        N2=('HELD' if letter == 0 else 'REFUTED', 'H26a %s: %d files differ as committed blobs, by line endings alone'
            % ('HELD' if letter == 0 else 'REFUTED', letter)),
        N3=('HELD' if anomaly else 'REFUTED', 'H26b: the single pin difference is Anomaly 1'),
        N4=('REFUTED' if tot <= 12 and Lg['ceiling'].get('README.md') and not any(d['kind'] == 'ceiling' for d in Lg['v2']['diffs'])
            else ('HELD' if tot <= 12 else 'REFUTED'),
            'H26c holds at %d, but the README`s ceiling block is not the largest cluster: its 7 ceiling sentences all equal REGISTRY`s '
            'and README carries no difference; the largest cluster is %s' % (tot, Lg['largest'])),
        N5=('HELD' if in_desc.get('E-2026-09-25-2') and in_desc.get('E-2026-09-25-1') else 'REFUTED',
            'E-2026-09-25-1 is in both fetched descriptions; E-2026-09-25-2 in neither -- it is the record of b535`s platform edits '
            '(ERRATA :528), never ordered into a description; the other five absent, none ordered into one'),
        N6=('HELD' if not auth and kmain == V015 and zpage_same and set(pp_changed) <= {'FINDINGS.md', 'OPEN_TRAILS.md'} else 'REFUTED',
            'two GETs, no Authorization header; nothing deposits; SIDE-explicit-formula main %s (v0.15, unmoved); PLACE-papers '
            'changed only at %s, by appended record lines; both pages unchanged' % (kmain, pp_changed)),
        S1=('HELD' if not in_desc.get('E-2026-09-25-2') and [k for k, v in in_desc.items() if v] == ['E-2026-09-25-1'] else 'REFUTED',
            'only E-2026-09-25-1 is in the fetched descriptions'),
        S2=('HELD' if letter == 0 else 'REFUTED',
            'refuted in letter with H26a: as committed blobs 2 files differ, by line endings alone; the deposit`s 11 files equal '
            'b535`s fetch-back at every md5, and both descriptions and `modified` stamps equal b535`s read -- the deposit immutable, '
            'its description last moved by b535`s edits'),
        S3=('HELD' if pages_ok else 'REFUTED', 'the ζ page regenerates to its committed blob byte for byte; no node changed'),
        counts=dict(files=len(P['files']), letter=letter, lf_only=lf, pin_diffs=len(pd), ledger=tot, contradicting=con, silent=sil,
                    v1=v1, ruled=ruled, present=present),
    )
    put_json('b574_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


def findings():
    Q = _Q()
    S = jl('b574_scores.json')
    c = S['counts']
    title = ('## CP-5, act one: the deposit read against REGISTRY, the corpus`s deposited copy, README and SPIRAL_MAP; Anomaly 1 from '
             'the fetch; the errata located; the description edit drafted').replace('`', '’')
    Q.guard_absent(Q.FIND, title)
    e = ['', title, '',
         '*Filed at b574 on the author’s ruling `(R184)`. Banks: relay `data/b574_zenodo_fetch.txt` (with the two responses whole), '
         '`data/b574_pins.txt`, `data/b574_ledgers.txt`, `data/b574_errata.txt`, `data/b574_description_draft.txt`, '
         '`data/b574_page_runs.txt`. Nothing at Zenodo was written; nothing deposits; no ledger line was reconciled.*', '',
         '**The fetch** (`(R184)`(4)(a)): records 21539167 (the deposit, v1.1.2) and 21520474 (SIDE-kernel v1.5) read by two anonymous '
         'GETs, each response banked whole; both descriptions and `modified` stamps equal b535’s fetch-back.', '',
         '**The files** (`(R184)`(4)(b)). The deposit has no MANIFEST file; its file list is held in the corpus at '
         '`outputs/DEPOSITED-v1.1.2/`. Of %d files, %d agree with the fetch as committed; %d (%s) differ as committed and agree once '
         'their CRLF line endings are restored -- git holds them LF-normalized, the deposit holds the bytes as written. H26a is refuted '
         'in that letter; the content is the deposit’s.' % (c['files'], c['files'] - c['letter'], c['letter'], ', '.join(c['lf_only'])), '',
         '**Anomaly 1, from the fetch.** REGISTRY’s pins, DOIs, concept DOIs and dates for both records agree with the fetch. The single '
         'difference is the kernel: the record carries v1.5 = `0e5233f`, the latest version on Zenodo, while the kernel’s tags have moved '
         'to v1.7 and REGISTRY’s dated working-head reading says so. No deposit carries v1.6 or v1.7.', '',
         '**README and SPIRAL_MAP against REGISTRY** (`(R184)`(4)(c)): %d differences -- none where REGISTRY states a fact otherwise; '
         '%d facts REGISTRY does not state (SPIRAL_MAP :41, the frozen v1.1 record’s file count; :140 and :533, the pins of '
         'SIDE-t7-topology-cmb and SIDE-silence-principle). README’s seven ceiling sentences equal REGISTRY’s. The extractor as first '
         'written hit %d; its excess was its own defect, each line hand-read.' % (c['ledger'], c['silent'], c['v1']), '',
         '**The errata** (`(R184)`(4)(d)): each of the seven located by heading and label; the one a ruling ordered into a description, '
         'E-2026-09-25-1, is in both fetched descriptions; E-2026-09-25-2 is the record of b535’s platform edits; -3 faces the '
         'SIDE-lv-conservation record (not fetched); -4, -5, -6 are drafts not filed; E-2026-09-27-1 faces the keystone.', '',
         '**The description edit, drafted** (`(R184)`(4)(e)): the three ceiling sentences of `(R177)`(2), `(R182)`(2) and `(R183)`(3), '
         'quoted whole from REGISTRY, banked as relay `data/b574_description_draft.txt` and written nowhere else. The second ends “The '
         'criterion for χ is not yet composed”, which the third supersedes; the author rules which the edit carries.', '',
         '**The ζ page’s generator** (`(R184)`(2)): the Correspondence selection factored by variant (relay `%s`); both pages regenerate '
         'byte for byte to their committed copies.' % GEN, '',
         '**The scores.** H26a %s; H26b %s; H26c %s; H26d %s. (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, '
         '(S2) %s, (S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R184)`(6), the lists are not empty: the reconciling edits and the description edit, as the author rules them.', '',
         '*Nothing deposits; nothing at Zenodo written; no kernel touched; README, REGISTRY, SPIRAL_MAP and ERRATA unedited; nothing here '
         'is a statement about RH, GRH or any zero.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b574_findings.json', dict(entry_line=Q.line_of(Q.FIND, title), append=r, title=title))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, title))


def trail():
    Q = _Q()
    S = jl('b574_scores.json')
    fj, wt, wj = jl('b574_findings.json'), jl('b574_weight.json'), jl('b574_word.json')
    head = ('### b574 — lane three, act two under (R184): CP-5 -- the deposit read with no write at Zenodo; the difference lists; '
            'Anomaly 1 from the fetch; the errata located; the description edit drafted; the ζ page’s generator repaired; W-ORD-GRH-WEIL '
            'closed at its landing')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R184) ratified.** (1) b573 at its weight. (2) The ζ page’s generator. (3) W-ORD-GRH-WEIL closed, its four remainders priced. '
            '(4) CP-5: the fetch, the pins, README and SPIRAL_MAP, the errata, the draft. (5) H26a-H26d. (6) The next act.', '',
            '**Entered:** FINDINGS.md:%s and :%s (b573’s weight; the lemma walk), :%s (the entry); OPEN_TRAILS.md:%s (the closing) and '
            ':%s (the four remainders), this record. Relay instrument commit: the generator `%s`. No kernel, README, REGISTRY, SPIRAL_MAP, '
            'ERRATA or CORRESPONDENCE line.' % (wt['lines'][0], wt['lines'][1], fj['entry_line'], wj['lines'][0],
                                                '-:'.join(str(x) for x in (wj['lines'][1], wj['lines'][-1])), GEN), '',
            '**H26a %s · H26b %s · H26c %s · H26d %s. (N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, '
            '(S2) %s, (S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**The lists, for ruling:** the two deposited files LF-normalized in git (relay data/b574_pins.txt); Anomaly 1, the kernel at '
            'v1.7 against the record’s v1.5; three facts REGISTRY does not state (relay data/b574_ledgers.txt); the draft of three '
            'sentences, the second superseded by the third (relay data/b574_description_draft.txt).', '',
            '**Next:** per `(R184)`(6), the reconciling edits and the description edit as the author rules them.', '',
            '**No `sorry` on any `main`.** Nothing deposits; nothing at Zenodo written; no kernel touched; ERRATA, README, REGISTRY, '
            'SPIRAL_MAP and FACES_LEDGER untouched; row U1 unedited; the four lists stay OPEN; nothing here is a statement about RH, GRH '
            'or any zero.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b574_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r))
    print(jl('b574_trail.json')['line'])


def desk():
    S = jl('b574_scores.json')
    L = ['=' * 104, 'b574 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H26a-H26d ((R184)(5)).', '-' * 104]
    L += ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H26a', 'H26b', 'H26c', 'H26d')]
    NK = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')
    L += ['', '### THE NAVIGATOR`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in NK if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (nh, 6 - nh, sh, 3 - sh), '']
    L += rd('b574_defects.txt').rstrip(NL).split(NL)
    put_txt('b574_desk_notes.txt', L)


def components():
    S = jl('b574_scores.json')
    fj, tj, wj, wt = jl('b574_findings.json'), jl('b574_trail.json'), jl('b574_word.json'), jl('b574_weight.json')
    c = S['counts']
    L = ['b574 -- THE COMPONENTS, BANKED UNDER (R184).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b573`s push-out banks relay %s ; push-b573* branches deleted by name '
         '(data/b574_branches.txt) ; the kept branches untouched' % PUSHOUT,
         '### COMPONENT 1 : the generator relay %s (test 31 of 31) ; both pages twice byte-identical, G-CHAIN-PAGE 2 of 2 '
         '(data/b574_page_runs.txt) ; b573`s weight FINDINGS :%s, :%s ; W-ORD-GRH-WEIL closed OPEN_TRAILS :%s, remainders :%s'
         % (GEN, wt['lines'][0], wt['lines'][1], wj['lines'][0], wj['lines'][1:]),
         '### COMPONENT 2 : the fetch, two anonymous GETs, responses banked whole (data/b574_zenodo_fetch.txt)',
         '### COMPONENT 3 : the pins (data/b574_pins.txt) : %d files, %d differ as committed blobs by line endings ; %d pin difference '
         '(Anomaly 1) ; H26a %s, H26b %s' % (c['files'], c['letter'], c['pin_diffs'], S['H26a'][0], S['H26b'][0]),
         '### COMPONENT 4 : README and SPIRAL_MAP (data/b574_ledgers.txt) : %d differences (%d contradicting, %d REGISTRY silent) ; '
         'H26c %s ; no edit' % (c['ledger'], c['contradicting'], c['silent'], S['H26c'][0]),
         '### COMPONENT 5 : the errata (data/b574_errata.txt), ruled %s present %s ; the draft (data/b574_description_draft.txt) ; '
         'H26d %s' % (c['ruled'], c['present'], S['H26d'][0]),
         '### COMPONENT 6 : FINDINGS :%s ; OPEN_TRAILS :%s (the record) ; no correspondence row ; next: the reconciling edits and the '
         'description edit as ruled' % (fj['entry_line'], tj['line'])]
    put_txt('b574_components.txt', L)



if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b574_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
