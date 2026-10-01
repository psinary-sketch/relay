# -*- coding: utf-8 -*-
"""b575_record.py -- THE ACT'S RECORD TOOL, UNDER (R185). ### ONE SUBCOMMAND PER BANK.

### ### b575: LANE THREE, ACT THREE -- CP-5, THE RECONCILING EDITS AS RULED. Subcommands write only `data/b575_*` unless the
### docstring names a ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then
### `os.replace`). The one Zenodo write of the act is `tools/b575_zenodo.py`'s; this tool's only platform call is the
### anonymous GET of record 21539068 (`lv`).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '0018869'
MIRROR = 'outputs/DEPOSITED-v1.1.2/'
REG = os.path.join(PP, 'REGISTRY.md')
SPM = os.path.join(PP, 'SPIRAL_MAP.md')
ERR = os.path.join(PP, 'ERRATA.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def gb(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if r.returncode == 0 else None


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


def md5(b):
    return 'md5:' + hashlib.md5(b).hexdigest() if b is not None else None


DEFECTS = [
    '(a) STEP ZERO: A TRANSCRIPT SEARCH OF THE SEAT`S OWN (a grep with a long bounded repeat over the session file) ran past the '
    'foreground limit and was moved to the background; TaskStop left its four pipeline children running, which the listing found '
    'and which were stopped by PID with their command lines (data/b575_procs_stepzero.txt). The searches after it carried a '
    'timeout.',
    '(b) COMPONENT 2`S CITATION MATCHER v1 READ EVERY v1.0-v1.7 ON A LINE AS A KERNEL TAG, and so took document versions '
    '(SIMPLICITY_OF_RIEMANN_ZEROS v1.0, A_METHODOLOGY v1.2) for SIDE-kernel pins: 9 lines differing, two of them artefacts. Matcher '
    'v2 counts only `SIDE-kernel v1.x` or a tag; both yields are printed and every line either hit is hand-read.',
    '(c) THE FILES-UNCHANGED PREDICATE CARRIED FROM b535 INTO b575_zenodo.py READ FALSE ON IDENTICAL FILES: it compares the deposition '
    'API`s bare checksums (before) with the records API`s md5:-prefixed ones (fetch-back), prefixing only the second side. The '
    'files are read again like for like -- the fetch-back`s (key, checksum, size) against b574`s fetch from the same records API '
    '(data/b575_files_same.txt): equal on both records. The tool is not edited after its run; the c2 bank`s line stands as printed.',
    '(d) A PATCH SCRIPT OF THE SEAT`S TRUNCATED tools/b575_record.py TO ZERO BYTES: it opened the tool for writing with an illegal '
    'newline argument, which raised after the open had truncated the file. The tool (untracked) was restored from the session '
    'transcript`s copy of its first write and the two patches re-applied in their order; its banks were untouched. The patch '
    'scripts after it write bytes to a temporary file and replace.',
    '(e) THE SUITE`S FIRST RUN FAILED G-NODEPOSIT LIVE ON ITS OWN TEXT: its needle for a file-upload path was written as a literal '
    'the suite itself contains -- b574`s defect (e) again, an arm that catches its author. The needle is now built by concatenation.',
]


def defects():
    put_txt('b575_defects.txt', ['### b575 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + ['    ' + d for d in DEFECTS])


def _Q():
    import b566_record as R6
    return R6.Q


# ================================================================================ READING (1)
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay b574`s fetch bank (the two request lines)', RELAY, 'HEAD', 'data/b574_zenodo_fetch.txt', 'REQUEST : '),
    ('relay b574`s pins bank (the CRLF-restored rows)', RELAY, 'HEAD', 'data/b574_pins.txt', 'as deposited, CRLF'),
    ('relay b574`s ledgers bank (the v2 hits)', RELAY, 'HEAD', 'data/b574_ledgers.txt', 'SILENT SPIRAL_MAP'),
    ('relay b574`s draft (the three sentences` rulings)', RELAY, 'HEAD', 'data/b574_description_draft.txt', '###   (R'),
    ('PLACE-papers REGISTRY (the ceiling lines)', PP, PRE_PP, 'REGISTRY.md', [956, 958, 960]),
    ('PLACE-papers REGISTRY (lines naming SIDE-kernel)', PP, PRE_PP, 'REGISTRY.md', 'SIDE-kernel'),
    ('PLACE-papers SPIRAL_MAP (the three lines and the annotation)', PP, PRE_PP, 'SPIRAL_MAP.md', [41, 43, 140, 533]),
    ('PLACE-papers SPIRAL_MAP (lines naming SIDE-kernel)', PP, PRE_PP, 'SPIRAL_MAP.md', 'SIDE-kernel'),
    ('PLACE-papers README (lines naming SIDE-kernel)', PP, PRE_PP, 'README.md', 'SIDE-kernel'),
    ('PLACE-papers ERRATA (the index; E-2026-09-25-1`s heading; E-2026-09-25-3`s heading)', PP, PRE_PP, 'ERRATA.md',
     [280, 281, 282, 283, 284, 285, 286, 483, 543]),
    ('relay b535`s route (the token; the write; the fetch-back)', RELAY, 'HEAD', 'tools/b535_zenodo.py', [49, 50, 210, 223, 228, 240, 248, 266]),
    ('relay b540`s ferry ((R150)(1))', RELAY, 'HEAD', 'data/b540_ferry.txt', [12, 13, 14]),
]


def reads():
    L = ['b575 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        lines = sel if isinstance(sel, list) else [i for i, l in enumerate(sl, 1) if sel in l]
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(lines)))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    er = g(PP, 'show', PRE_PP + ':ERRATA.md').split(NL)
    st = [i for i, l in enumerate(er, 1) if l.startswith('**Status.**') and 543 < i < 600]
    L.append('### ERRATA E-2026-09-25-3`s Status at :%s : %s' % (st, er[st[0] - 1][:300] if st else '### NOT FOUND'))
    put_txt('b575_reads.txt', L)


# ================================================================================ COMPONENT 1: THE LINES AND THE MIRROR
def weight():
    """### PLACE-papers FINDINGS.md (two appended lines): (R185)(1) -- b574 at its weight; the H26a letter as the navigator's."""
    Q = _Q()
    e = Q.line_of(Q.FIND, '## CP-5, act one: the deposit read against REGISTRY')
    h1 = '*Appended 2026-10-01 by b575 to b574’s entry (:%s), under `(R185)`(1) -- b574 AT ITS WEIGHT:*' % e
    h2 = '*Appended 2026-10-01 by b575 to b574’s entry (:%s), under `(R185)`(2)(i) -- THE H26a LETTER, THE NAVIGATOR’S:*' % e
    Q.guard_absent(Q.FIND, h1)
    a1 = ('\n%s two fetches with no write, records 21539167 (the deposit, v1.1.2) and 21520474 (SIDE-kernel v1.5), responses '
          'banked whole; descriptions and last-modified stamps unchanged since b535 -- the deposit is immutable and the b535 edits '
          'are the last. All 11 files match the fetch by content; Anomaly 1 is the single pin difference; README matches REGISTRY’s '
          'seven ceiling sentences word for word; SPIRAL_MAP differs at three lines REGISTRY does not state, none contradicting it; '
          'E-2026-09-25-1 is in both descriptions as ruled. The suite read 65 of 65.\n' % h1)
    a2 = ('\n%s H26a was refuted in letter and held in content: the navigator’s clause compared committed blobs, and git held the '
          'deposit’s two CRLF files LF-normalized, so blobs hid the line endings. The sealed b574 face is not edited; from b575 the '
          'mirror holds the deposited bytes and the bank prints both md5s per file.\n' % h2)
    r = [Q.append_to(Q.FIND, a1), Q.append_to(Q.FIND, a2)]
    put_json('b575_weight.json', dict(entry=e, lines=[Q.line_of(Q.FIND, h1), Q.line_of(Q.FIND, h2)], appends=r))
    print(jl('b575_weight.json'))


def _record_md5s():
    return jl('b574_zenodo_fetch.json')['21539167']['files']


def _mirror_files(rev):
    return sorted(x for x in g(PP, 'ls-tree', '--name-only', rev, MIRROR).split(NL) if x.strip())


def mirror_pre():
    """### Before the re-commit: each mirror file's working-tree md5, committed-blob md5 and the record's md5."""
    rec = _record_md5s()
    L = ['b575 -- COMPONENT 1, BEFORE THE RE-COMMIT: THE MIRROR`S WORKING TREE AND BLOBS AGAINST THE RECORD`S md5s', '',
         '    %-30s %-38s %-38s %-38s %s' % ('file', 'the record (b574 fetch)', 'working tree', 'blob at HEAD', 'tree = record')]
    ok = True
    for p in _mirror_files('HEAD'):
        k = os.path.basename(p)
        wt = md5(open(os.path.join(PP, p), 'rb').read())
        bl = md5(gb(PP, 'show', 'HEAD:' + p))
        good = wt == rec.get(k)
        ok = ok and good
        L.append('    %-30s %-38s %-38s %-38s %s' % (k, rec.get(k), wt, bl, 'YES' if good else '### NO'))
    L += ['', '### ### **EVERY WORKING-TREE FILE EQUALS THE RECORD: %s.** ### attributes: %s' % (
        ok, g(PP, 'check-attr', 'text', 'eol', '--', MIRROR + 'ERRATA.md').strip().replace(NL, ' ; '))]
    put_txt('b575_mirror_pre.txt', L)
    print('working tree = record:', ok)
    return 0 if ok else 2


def mirror(rev='HEAD'):
    """### After the re-commit: every committed blob's md5 at `rev` beside the record's, both columns; and each blob with CRLF
    ### folded to LF against the pre-act blob folded the same way (the content unchanged)."""
    rec = _record_md5s()
    rv = g(PP, 'rev-parse', '--short=8', rev).strip()
    L = ['b575 -- COMPONENT 1, THE FRESH COMPARISON AFTER THE COMMIT: EVERY MIRROR BLOB AT PLACE-papers %s AGAINST THE RECORD' % rv,
         '### record md5s: record 21539167 as b574 fetched it (data/b574_zenodo_fetch.json; immutable at its version). Content: the '
         'blob and the pre-act blob (%s), each with CRLF folded to LF.' % PRE_PP, '',
         '    %-30s %-38s %-38s %-8s %s' % ('file', 'the record', 'the blob at ' + rv, 'equal', 'content = pre-act')]
    rows = []
    for p in _mirror_files(rev):
        k = os.path.basename(p)
        b = gb(PP, 'show', '%s:%s' % (rev, p))
        pre = gb(PP, 'show', '%s:%s' % (PRE_PP, p))
        same = b is not None and pre is not None and b.replace(b'\r\n', b'\n') == pre.replace(b'\r\n', b'\n')
        rows.append(dict(file=k, record=rec.get(k), blob=md5(b), equal=md5(b) == rec.get(k), content_same=same))
        L.append('    %-30s %-38s %-38s %-8s %s' % (k, rec.get(k), md5(b), md5(b) == rec.get(k), same))
    n = sum(r['equal'] for r in rows)
    L += ['', '### ### **BLOBS EQUAL TO THE RECORD: %d OF %d ; CONTENT UNCHANGED: %d OF %d.**' % (
        n, len(rows), sum(r['content_same'] for r in rows), len(rows)),
          '### attributes now: %s' % g(PP, 'check-attr', 'text', 'eol', '--', MIRROR + 'ERRATA.md').strip().replace(NL, ' ; ')]
    put_txt('b575_mirror.txt', L)
    put_json('b575_mirror.json', dict(rev=g(PP, 'rev-parse', rev).strip(), rows=rows, equal=n, files=len(rows)))
    print('equal', n, 'of', len(rows))


# ================================================================================ COMPONENT 2
KVER = re.compile(r'\bv1\.([0-7])\b(?!\.\d)')
SHA_NEAR = re.compile(r'^[^.;|]{0,12}?(?:=|\()\s*\**`?([0-9a-f]{7,40})`?')
KREC = ('21520474', '19674312', '19937590', '21417776')


KVER2 = re.compile(r'(?:SIDE-kernel\s+\**`?|\btag\s+`)(v1\.[0-7])\b(?!\.\d)')


def _classify(line, matcher='v1'):
    """### v1: every v1.0-v1.7 on the line; v2: only `SIDE-kernel v1.x` or ``tag `v1.x` `` -- v1 read document
    ### versions (SIMPLICITY_OF_RIEMANN_ZEROS v1.0, A_METHODOLOGY v1.2) as kernel tags (defect (b))."""
    cites = []
    dep_ctx = bool(re.search(r'zenodo|deposit|DOI', line, re.I))
    for m in (KVER.finditer(line) if matcher == 'v1' else KVER2.finditer(line)):
        v = ('v1.' + m.group(1)) if matcher == 'v1' else m.group(1)
        sm = SHA_NEAR.search(line[m.end():m.end() + 40])
        cites.append(dict(version=v, sha=sm.group(1) if sm else None))
    recs = [r for r in KREC if r in line]
    verdict = []
    for c in cites:
        if c['version'] == 'v1.5':
            verdict.append('%s %s: OBEYS (the deposit`s pin)' % (c['version'], c['sha'] or ''))
        elif c['sha']:
            verdict.append('%s = %s: OBEYS (a tag cited by its SHA)' % (c['version'], c['sha']))
        else:
            verdict.append('%s: ### DIFFERS (a tag cited without its SHA%s)' % (c['version'], '; a deposit context' if dep_ctx else ''))
    if '19937590' in line:
        verdict.append('record 19937590 (the v1.1 deposit): ### DIFFERS IN LETTER (a deposit citation not at v1.5)')
    return cites, recs, verdict


HAND = {
    ('README.md', 15): 'the kernel line: deposit v1.5 = 0e5233f cited by named terminal -- obeys.',
    ('SPIRAL_MAP.md', 18): 'v0.6`s changelog entry (July 2026): "SIDE-kernel v1.4" as the pin of that pass, a dated historical line; '
                           'it cites neither the deposit nor the current kernel -- differs in letter only.',
    ('SPIRAL_MAP.md', 41): 'the frozen v1.1 deposit row, historical and retained verbatim (annotation :43) -- differs in letter only.',
    ('SPIRAL_MAP.md', 43): 'the annotation: v1.1 = e7ab5a2 (tag object) and v1.2 = b1407b2, both by SHA -- obeys.',
    ('SPIRAL_MAP.md', 49): 'the deposit-wave row: v1.5 (0e5233f), record 21520474 -- obeys.',
    ('SPIRAL_MAP.md', 257): 'the Foundations row`s note: "de-vacuified at SIDE-kernel v1.4 / W-6-EXT", the version at which a '
                            'past event happened -- neither the deposit nor the current kernel; differs in letter only.',
    ('SPIRAL_MAP.md', 268): 'the same note in the live table`s Foundations row -- differs in letter only.',
    ('SPIRAL_MAP.md', 443): 'the barrier table: "InvarianceBarrier.invariance_barrier (SIDE-kernel v1.6, axiom-free)", a terminal '
                            'cited at the tag where it landed, without its SHA -- not the deposit; differs from the rule as written.',
    ('SPIRAL_MAP.md', 236): 'v1 artefact: "SIMPLICITY_OF_RIEMANN_ZEROS v1.0" is the document`s version; the line names SIDE-kernel '
                            'with no pin -- rule not engaged.',
    ('SPIRAL_MAP.md', 256): 'v1 artefact: "A_METHODOLOGY v1.2" is the document`s version; no kernel pin -- rule not engaged.',
    ('SPIRAL_MAP.md', 54): 'the live-kernel reconciliation of 2026-07-19: v1.4 = f374174 and v1.2 = b1407b2 by SHA, the deposit v1.5 -- obeys.',
}


def kernel_lines():
    """### README's and SPIRAL_MAP's lines naming SIDE-kernel, each with what it cites and its verdict against the rule as
    ### written, by both matchers (both yields printed); then the seat's hand-read of every line either matcher hit. Nothing is
    ### edited."""
    L = ['b575 -- COMPONENT 2: README`S AND SPIRAL_MAP`S LINES NAMING SIDE-kernel AGAINST THE CITATION RULE OF (R185)(2)(ii)',
         '### the rule: a sentence citing SIDE-kernel for the deposit cites v1.5; one citing the current kernel cites the tag by its SHA.',
         '### matcher v1: each v1.0-v1.7 on the line (v1.1.2 and longer excluded); matcher v2: only `SIDE-kernel v1.x` or a '
         '``tag `v1.x` `` (defect (b)); a SHA within 40 characters after the version read as its pin; a SIDE-kernel record id '
         '(21520474, 19674312, 19937590, 21417776) noted. Read at PLACE-papers %s.' % PRE_PP, '']
    res = {}
    for mv in ('v1', 'v2'):
        out = []
        for f in ('README.md', 'SPIRAL_MAP.md'):
            sl = g(PP, 'show', '%s:%s' % (PRE_PP, f)).split(NL)
            for i, l in enumerate(sl, 1):
                if 'SIDE-kernel' not in l:
                    continue
                cites, recs, verdict = _classify(l, mv)
                out.append(dict(file=f, line=i, cites=cites, records=recs, verdict=verdict,
                                differs=any('DIFFERS' in v for v in verdict), hand=HAND.get((f, i))))
        res[mv] = out
        d = [o for o in out if o['differs']]
        L.append('### matcher %s : lines naming SIDE-kernel %d ; citing a pin %d ; differing %d %s' % (
            mv, len(out), sum(1 for o in out if o['cites'] or o['records']), len(d), ['%s :%d' % (o['file'], o['line']) for o in d]))
    L.append('')
    L.append('### MATCHER v2, EVERY LINE, WITH THE HAND-READ OF EVERY LINE EITHER MATCHER HIT:')
    hit = set((o['file'], o['line']) for mv in res for o in res[mv] if o['differs'] or o['cites'] or o['records'])
    for o in res['v2']:
        L.append('    %s :%-4d cites %s ; records %s ; %s' % (o['file'], o['line'], [(c['version'], c['sha']) for c in o['cites']] or 'NO PIN',
                                                         o['records'] or '-', '; '.join(o['verdict']) or 'RULE NOT ENGAGED (no pin cited)'))
        if (o['file'], o['line']) in hit:
            L.append('              hand-read: %s' % (o['hand'] or '### NOT HAND-READ'))
    d2 = [o for o in res['v2'] if o['differs']]
    L += ['', '### ### **DIFFERING FROM THE RULE AS WRITTEN (matcher v2): %d -- %s.**' % (
        len(d2), ['%s :%d' % (o['file'], o['line']) for o in d2] or 'NONE'),
          '### ### hand-read: %s' % ('every differing line is a dated or frozen historical line, or a terminal cited at the tag '
                                      'where it landed; none cites another version as the deposit or as the current kernel. Nothing '
                                      'edited.' if all(o['hand'] for o in d2) else '### A DIFFERING LINE IS NOT HAND-READ.')]
    put_txt('b575_kernel_lines.txt', L)
    put_json('b575_kernel_lines.json', dict(v1=res['v1'], v2=res['v2'], differing=['%s:%d' % (o['file'], o['line']) for o in d2],
                                            v1_differing=['%s:%d' % (o['file'], o['line']) for o in res['v1'] if o['differs']]))
    print('v1 differing', sum(o['differs'] for o in res['v1']), '; v2 differing', [(o['file'], o['line']) for o in d2])


REMOTES = [('SIDE-kernel', 'https://github.com/psinary-sketch/SIDE-kernel.git', ['v1.1', 'v1.5', 'v1.7']),
           ('SIDE-t7-topology-cmb', None, ['v0.3']), ('SIDE-silence-principle', None, ['v0.2.0'])]


def facts():
    """### The two tags and SIDE-kernel's v1.1, v1.5, v1.7 peeled at the remote by ls-remote; the fresh count at v1.1."""
    L = ['b575 -- COMPONENT 2: THE PINS AT THE REMOTES AND THE FRESH COUNT, (R185)(2)(ii)-(iii)', '### read at (UTC) %s' % utc(), '']
    peeled = {}
    for repo, url, tags in REMOTES:
        url = url or g('D:/' + repo, 'remote', 'get-url', 'origin').strip()
        out = g('D:/' + repo, 'ls-remote', url, *(['refs/tags/%s' % t for t in tags] + ['refs/tags/%s^{}' % t for t in tags]))
        refs = dict((l.split('\t')[1], l.split('\t')[0]) for l in out.split(NL) if '\t' in l)
        for t in tags:
            rem = refs.get('refs/tags/%s^{}' % t) or refs.get('refs/tags/%s' % t)
            obj = refs.get('refs/tags/%s' % t)
            loc = g('D:/' + repo, 'rev-parse', '%s^{commit}' % t).strip()
            peeled['%s %s' % (repo, t)] = dict(remote=rem, tag_object=obj if obj != rem else None, local=loc, agree=rem == loc)
            L.append('    %-24s %-7s remote peeled %s ; tag object %s ; local %s ; %s' % (repo, t, rem, obj if obj != rem else '-', loc,
                                                                                         'AGREE' if rem == loc else '### DIFFER'))
    sm = g(PP, 'show', PRE_PP + ':SPIRAL_MAP.md').split(NL)
    L += ['', '### SPIRAL_MAP`s tags: :140 %s ; :533 %s' % (re.findall(r'v0\.3\S* \(`([0-9a-f]+)`\)', sm[139]),
                                                           re.findall(r'`v0\.2\.0`\*\* = `([0-9a-f]+)`', sm[532]))]
    sp = {'SIDE-t7-topology-cmb v0.3': (re.findall(r'v0\.3\S* \(`([0-9a-f]+)`\)', sm[139]) or [''])[0],
          'SIDE-silence-principle v0.2.0': (re.findall(r'`v0\.2\.0`\*\* = `([0-9a-f]+)`', sm[532]) or [''])[0]}
    agree_sp = {k: bool(v) and (peeled[k]['remote'] or '').startswith(v) for k, v in sp.items()}
    L.append('### ### **SPIRAL_MAP`S TWO TAGS AGAINST THE REMOTE: %s**' % agree_sp)
    pin = peeled['SIDE-kernel v1.1']['remote']
    files = [x for x in g('D:/SIDE-kernel', 'ls-tree', '-r', '--name-only', pin).split(NL) if x.strip()]
    lean = [x for x in files if x.endswith('.lean')]
    k = sum(1 for x in lean if x.startswith('Kernel/'))
    b = sum(1 for x in lean if x.startswith('Bridge/'))
    mk = sum(1 for x in lean if x == 'MetaKernel.lean')
    count = dict(kernel=k, bridge=b, metakernel=mk, kernel_bridge=k + b, with_metakernel=k + b + mk, lean_whole=len(lean), files=len(files))
    L += ['', '### THE FRESH COUNT at SIDE-kernel v1.1 = %s (E-2026-07-13-1`s method: git ls-tree -r --name-only, `.lean` by directory):' % pin[:7],
          '    Kernel/ %d ; Bridge/ %d ; MetaKernel.lean %d ; Kernel/+Bridge/ %d ; +MetaKernel %d ; every .lean %d ; every file %d'
          % (k, b, mk, k + b, k + b + mk, len(lean), len(files)),
          '### ### **THE SCOPES YIELDING 83: %s.**' % ([n for n, v in count.items() if v == 83] or 'NONE')]
    put_txt('b575_facts.txt', L)
    put_json('b575_facts.json', dict(peeled=peeled, spiral=sp, spiral_agree=agree_sp, count=count, pin=pin))
    print({k2: v['remote'] for k2, v in peeled.items()}, count)


def _registry_lines():
    F = jl('b575_facts.json')
    p = F['peeled']
    c = F['count']
    v17 = p['SIDE-kernel v1.7']['remote']
    v11 = p['SIDE-kernel v1.1']
    scopes = [n for n, v in c.items() if v == 83]
    pair = ("*(Appended under the author's ruling `(R185)`(2)(ii), 2026-10-01, b575: Anomaly 1 stated as a pair of pins, with no "
            "deposit.)* **SIDE-kernel, the deposited pin and the current tag.** Deposited at **v1.5** = `0e5233f` (record 21520474, "
            "DOI 10.5281/zenodo.21520474; immutable at its version). Current tag **v1.7** = `%s` (the peeled SHA read at the remote by "
            "ls-remote, 2026-10-01, relay `data/b575_facts.txt`; a tag is not a deposit; no deposit carries v1.6 or v1.7). **The "
            "citation rule:** a sentence citing SIDE-kernel for the deposit cites v1.5; a sentence citing the current kernel cites the "
            "tag by its SHA. A new SIDE-kernel deposit waits on the author's posture ruling." % v17)
    f1 = ("*(Appended under the author's ruling `(R185)`(2)(iii), 2026-10-01, b575, verified before writing.)* **SIDE-kernel v1.1, "
          "record 19937590 (DOI 10.5281/zenodo.19937590), the count its description states:** \"83 files\" is the count of `.lean` "
          "files under `Kernel/` (%d) and `Bridge/` (%d) at tag `v1.1` (tag object `%s`, peeled `%s`, read at the remote); the other "
          "scopes count %d with `MetaKernel.lean` and %d over every `.lean` path -- re-counted 2026-10-01 by E-2026-07-13-1's method "
          "(relay `data/b575_facts.txt`), as that erratum found. (SPIRAL_MAP :41)"
          % (c['kernel'], c['bridge'], (v11['tag_object'] or '')[:7], v11['remote'][:7], c['with_metakernel'], c['lean_whole']))
    if scopes != ['kernel_bridge']:
        f1 = f1.replace('as that erratum found', '### THE SCOPES YIELDING 83 ARE %s' % scopes)
    t7 = p['SIDE-t7-topology-cmb v0.3']['remote']
    sp = p['SIDE-silence-principle v0.2.0']['remote']
    f2 = ("*(Appended under the author's ruling `(R185)`(2)(iii), 2026-10-01, b575, verified before writing.)* "
          "**SIDE-t7-topology-cmb v0.3** = `%s` (the peeled SHA read at the remote by ls-remote, 2026-10-01; a tag is not a "
          "deposit). (SPIRAL_MAP :140)" % t7)
    f3 = ("*(Appended under the author's ruling `(R185)`(2)(iii), 2026-10-01, b575, verified before writing.)* "
          "**SIDE-silence-principle v0.2.0** = `%s` (the peeled SHA read at the remote by ls-remote, 2026-10-01; a tag is not a "
          "deposit). (SPIRAL_MAP :533)" % sp)
    return [pair, f1, f2, f3]


def registry_lines():
    """### PLACE-papers REGISTRY.md (four lines appended at its end): the pair line, then the three facts."""
    Q = _Q()
    F = jl('b575_facts.json')
    if not all(v['agree'] for v in F['peeled'].values()):
        sys.exit('### A TAG DIFFERS BETWEEN LOCAL AND REMOTE -- NO LINE WRITTEN.')
    ls = _registry_lines()
    Q.guard_absent(REG, ls[0][:120])
    r = [Q.append_to(REG, '\n' + l + '\n') for l in ls]
    text = io.open(REG, encoding='utf-8').read().split(NL)
    nums = [[i for i, x in enumerate(text, 1) if x == l][0] for l in ls]
    put_json('b575_registry_lines.json', dict(lines=nums, text=ls, appends=r))
    print('REGISTRY lines', nums)


def spiral_pointers():
    """### PLACE-papers SPIRAL_MAP.md: ' (REGISTRY :N)' appended to :140 and :533 at the line's end, and to :41 inside its last
    ### cell before the closing bar. No other byte changes."""
    R = jl('b575_registry_lines.json')['lines']
    raw = open(SPM, 'rb').read()
    lines = raw.split(b'\n')
    pre = gb(PP, 'show', PRE_PP + ':SPIRAL_MAP.md')
    if raw.replace(b'\r\n', b'\n') != (pre or b'').replace(b'\r\n', b'\n'):
        sys.exit('### SPIRAL_MAP DIFFERS FROM ITS PRE-ACT BLOB -- NO POINTER WRITTEN.')
    plan = [(41, R[1]), (140, R[2]), (533, R[3])]
    for n, rn in plan:
        l = lines[n - 1]
        cr = l.endswith(b'\r')
        body = l[:-1] if cr else l
        ptr = (' (REGISTRY :%d)' % rn).encode('utf-8')
        if ptr in body:
            sys.exit('### POINTER ALREADY PRESENT AT :%d' % n)
        if n == 41:
            if not body.rstrip().endswith(b'|'):
                sys.exit('### :41 IS NOT A TABLE ROW')
            k = body.rstrip().rfind(b'|')
            core = body[:k].rstrip()
            body = core + ptr + b' ' + body[k:]
        else:
            body = body + ptr
        lines[n - 1] = body + (b'\r' if cr else b'')
    new = b'\n'.join(lines)
    open(SPM + '.tmp', 'wb').write(new)
    os.replace(SPM + '.tmp', SPM)
    after = open(SPM, 'rb').read().split(b'\n')
    put_json('b575_spiral.json', dict(plan=plan, lines={str(n): after[n - 1].decode('utf-8')[-160:] for n, _ in plan}))
    for n, _ in plan:
        print(':%d ...%s' % (n, after[n - 1].decode('utf-8')[-90:]))


def files_same():
    """### Like for like: each fetch-back's files (key, checksum, size) against b574's anonymous fetch from the same records API."""
    L = ['b575 -- COMPONENT 3: THE RECORDS` FILES AFTER THE WRITE, LIKE FOR LIKE (defect (c))', '']
    out = {}
    for r in ('21520474', '21539167'):
        fb, old = jl('b575_fetchback_%s.json' % r), jl('b574_fetch_%s.json' % r)
        f1 = sorted((f['key'], f['checksum'], f['size']) for f in fb['files'])
        f0 = sorted((f['key'], f['checksum'], f['size']) for f in old['files'])
        out[r] = dict(same=f1 == f0, files=len(f1), version=fb['metadata'].get('version'), id=fb.get('id'),
                      modified=[old.get('modified'), fb.get('modified')])
        L.append('    %s : files %d ; (key, checksum, size) equal to b574`s fetch : %s ; version %s ; id %s ; modified %s -> %s'
                 % (r, len(f1), f1 == f0, out[r]['version'], out[r]['id'], old.get('modified'), fb.get('modified')))
    L += ['', '### ### **FILES UNCHANGED ON BOTH RECORDS: %s.**' % all(v['same'] for v in out.values())]
    put_txt('b575_files_same.txt', L)
    put_json('b575_files_same.json', out)


# ================================================================================ COMPONENT 3: THE ERRATUM (on MATCH only)
def erratum():
    """### PLACE-papers ERRATA.md: E-2026-10-01-1's index line inserted after E-2026-09-25-6's in the DEPOSIT-FACING list, and
    ### its entry appended at the end. Refuses unless b575_zenodo.py's c2 recorded MATCH on both records."""
    Q = _Q()
    R = jl('b575_zenodo_results.json')
    c2 = R.get('c2') or {}
    if c2.get('all_match') is not True:
        sys.exit('### c2 DID NOT RECORD MATCH ON BOTH RECORDS -- NO ERRATUM WRITTEN.')
    recs = c2['records']
    stamps = {rid: recs[rid].get('fetchback_at') for rid in recs}
    I = jl('b575_intended_meta.json')
    head = ('## E-2026-10-01-1 — The descriptions of the deposit and of SIDE-kernel v1.5 now carry the compiled ceiling at the '
            'successor sentence (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5)')
    Q.guard_absent(ERR, head)
    idx = ("- `E-2026-10-01-1` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5* (appended to this list by "
           "b575 under `(R185)`(2)(iv))")
    raw = open(ERR, 'rb').read()
    lines = raw.split(b'\n')
    anchor = [i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-25-6` — '.encode('utf-8'))]
    if len(anchor) != 1:
        sys.exit('### THE INDEX ANCHOR IS NOT FOUND ONCE: %s' % anchor)
    lines.insert(anchor[0] + 1, idx.encode('utf-8'))
    open(ERR + '.tmp', 'wb').write(b'\n'.join(lines))
    os.replace(ERR + '.tmp', ERR)
    s1, s3 = I['sentences']
    body = [
        '', head, '',
        '**Filed 2026-10-01 by b575, on the author’s ruling `(R185)`(2)(iv), at the write it records. The records are immutable at '
        'their versions; their files are unchanged; only the description field of each was edited, by the `(R110)` route.**', '',
        '**Affected deposits.** *A Place to Stand*, Zenodo v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) '
        '— the record description; SIDE-kernel v1.5, tag `v1.5` = commit `0e5233f` '
        '([10.5281/zenodo.21520474](https://doi.org/10.5281/zenodo.21520474)) — the record description.', '',
        '**What was written.** Two sentences of REGISTRY, quoted whole in the author’s words, in this order: the Weil sentence of '
        '`(R177)`(2) (REGISTRY :956) and the successor sentence of `(R183)`(3) (REGISTRY :960). In record 21520474 they follow the '
        'first paragraph’s sentence carrying the standing reduction; in record 21539167 they follow paragraph four’s sentence naming '
        'the clause at Section 27.3. The sentence of `(R182)`(2) (REGISTRY :958), superseded by the successor, is not on the records; '
        'it stays in FINDINGS’ lineage.', '',
        '> ' + s1, '', '> ' + s3, '',
        '**The route and the fetch-back.** relay `tools/b575_zenodo.py`, carried from b535: edit, PUT with every other key carried, '
        'publish, then an anonymous fetch-back compared byte for byte with the intended description -- MATCH on both records. '
        'Fetch-back of 21520474 at %s; of 21539167 at %s (relay `data/b575_zenodo_c2.txt`, `data/b575_fetchback_21520474.json`, '
        '`data/b575_fetchback_21539167.json`).' % (stamps.get('21520474'), stamps.get('21539167')), '',
        '**What is not corrected.** No sentence already on either record is changed; the deposited files are not touched; '
        'E-2026-09-25-1 stands in both descriptions as b535 wrote it. Nothing here is a statement about RH, GRH or any zero beyond '
        'the compiled statements’ own words.', '',
        '**Status.** FILED. Retained at monograph v1.1.2 and SIDE-kernel v1.5.', '']
    r = Q.append_to(ERR, NL.join(body))
    text = io.open(ERR, encoding='utf-8').read().split(NL)
    put_json('b575_erratum.json', dict(index_line=[i for i, x in enumerate(text, 1) if x == idx][0],
                                       heading_line=[i for i, x in enumerate(text, 1) if x == head][0], stamps=stamps, append=r))
    L = ['b575 -- COMPONENT 3: E-2026-10-01-1 WRITTEN TO ERRATA (on MATCH)', '', '### index line :%s ; heading :%s' % (
        jl('b575_erratum.json')['index_line'], jl('b575_erratum.json')['heading_line'])] + ['    ' + x for x in [idx] + body]
    put_txt('b575_erratum.txt', L)


# ================================================================================ COMPONENT 4: THE THIRD RECORD (GET only)
LV = '21539068'
LV_NEEDLES = ['E-2026-09-25-3', 'Rather than leaving that clause as prose', 'The one deliberately open obligation is the clause itself',
              'states a goal state around it', 'which is false as stated at every s with re s ≤ 1']


def lv():
    """### Record 21539068 by one anonymous GET (no Authorization header, the token variable never read); banked whole."""
    import urllib.request
    url = 'https://zenodo.org/api/records/' + LV
    req = urllib.request.Request(url, method='GET', headers={'Accept': 'application/json', 'User-Agent': 'relay-b575-read'})
    t0 = utc()
    with urllib.request.urlopen(req, timeout=60) as r:
        status, body = r.status, r.read()
    p = os.path.join(D, 'b575_fetch_%s.json' % LV)
    open(p + '.tmp', 'wb').write(body)
    os.replace(p + '.tmp', p)
    d = json.loads(body.decode('utf-8'))
    m = d.get('metadata', {})
    desc = m.get('description') or ''
    rel = (m.get('relations') or {}).get('version') or [{}]
    hits = {n: desc.count(n) for n in LV_NEEDLES}
    L = ['b575 -- COMPONENT 4: THE THIRD RECORD, (R185)(2)(v) -- READ ONLY: anonymous GET, no Authorization header, no token read', '',
         '### REQUEST : GET %s ; Authorization header sent : %s ; at (UTC) %s ; HTTP %s ; %d bytes ; banked whole as data/b575_fetch_%s.json'
         % (url, req.has_header('Authorization'), t0, status, len(body), LV),
         '    id %s ; doi %s ; title %s ; version %s ; modified %s ; is_last %s' % (d.get('id'), d.get('doi'), m.get('title'),
                                                                                m.get('version'), d.get('modified'), rel[0].get('is_last')),
         '    description, verbatim:', '      ' + desc.replace(NL, NL + '      '), '',
         '### the needles in the description: %s' % hits,
         '### positive control: the drafted RESTS sentence the erratum quotes from the b499 fetch-back, "Rather than leaving that '
         'clause as prose", is %s' % ('FOUND' if hits['Rather than leaving that clause as prose'] else '### NOT FOUND'),
         '### ### **E-2026-09-25-3 IN THE DESCRIPTION: %s** -- governed by (R150)(1), relay data/b540_ferry.txt :12-:14: "Whether '
         'lv-conservation`s Zenodo description is edited under (R110) is a separate ruling, not taken here"; no later ruling '
         '(every ferry from b540 searched); NO RULING ORDERED IT INTO THE DESCRIPTION -- RECORDED, NOT APPENDED.'
         % ('PRESENT' if hits['E-2026-09-25-3'] else 'ABSENT')]
    put_txt('b575_zenodo_lv.txt', L)
    put_json('b575_lv.json', dict(at=t0, status=status, auth=req.has_header('Authorization'), id=d.get('id'), version=m.get('version'),
                                  modified=d.get('modified'), hits=hits, present=bool(hits['E-2026-09-25-3'])))
    print(jl('b575_lv.json'))


# ================================================================================ COMPONENT 5 AND THE SCORING
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3')
EF = 'D:/SIDE-explicit-formula'
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-t7-topology-cmb': None}
PP_ALLOWED = {'.gitattributes', MIRROR + 'A_Place_to_Stand.md', MIRROR + 'ERRATA.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'ERRATA.md',
              'FINDINGS.md', 'OPEN_TRAILS.md'}


def _pp_changed():
    a = set(x for x in g(PP, 'diff', '--name-only', PRE_PP).split(NL) if x.strip())
    return sorted(a)


def scores():
    M, K, F, Z, E, LV, FS = (jl('b575_mirror.json'), jl('b575_kernel_lines.json'), jl('b575_facts.json'), jl('b575_zenodo_results.json'),
                             jl('b575_erratum.json'), jl('b575_lv.json'), jl('b575_files_same.json'))
    c2 = Z.get('c2') or {}
    d2 = K['differing']
    ch = _pp_changed()
    kmain = g(EF, 'rev-parse', 'main').strip()
    heads = {r: g('D:/' + r, 'rev-parse', 'main').strip() for r in PRE_HEADS}
    heads_ok = all(h is None or heads[r].startswith(h) for r, h in PRE_HEADS.items())
    faces = [x for x in g(ROOT, 'diff', '--name-only', 'HEAD', '--', 'data/b56*_registration_*.txt', 'data/b57[0-4]_registration_*.txt').split(NL) if x.strip()]
    nodep = all(v['same'] for v in FS.values()) and FS['21520474']['version'] == 'v1.5' and FS['21539167']['version'] == 'v1.1.2'
    S = dict(
        N1=('HELD' if M['equal'] == M['files'] == 11 else 'REFUTED',
            'after the re-commit (PLACE-papers %s) %d of %d blob md5s equal record 21539167`s, the content of each unchanged from the '
            'pre-act blob with line endings folded (relay data/b575_mirror.txt)' % (M['rev'][:7], M['equal'], M['files'])),
        N2=('HELD' if not d2 else 'REFUTED',
            'README :15 obeys; SPIRAL_MAP differs from the rule as written at %d lines -- %s -- each hand-read as a dated or frozen '
            'historical line or a terminal cited at the tag where it landed; none cites another version as the deposit or as the '
            'current kernel; nothing edited (relay data/b575_kernel_lines.txt; matcher v1 read 9, two of them document versions)'
            % (len(d2), ', '.join(d2))),
        N3=('HELD' if all(F['spiral_agree'].values()) else 'REFUTED',
            'SIDE-t7-topology-cmb v0.3 peels to %s and SIDE-silence-principle v0.2.0 to %s at the remotes, equal to SPIRAL_MAP :140 and '
            ':533 (relay data/b575_facts.txt)' % (F['peeled']['SIDE-t7-topology-cmb v0.3']['remote'][:7],
                                                F['peeled']['SIDE-silence-principle v0.2.0']['remote'][:7])),
        N4=('HELD' if c2.get('all_match') and E.get('heading_line') else 'REFUTED',
            'both fetch-backs MATCH on the first try (21520474 at %s, 21539167 at %s); E-2026-10-01-1 written, ERRATA :%s (index) and '
            ':%s (entry)' % (E['stamps'].get('21520474'), E['stamps'].get('21539167'), E['index_line'], E['heading_line'])),
        N5=('HELD' if LV['present'] else 'REFUTED',
            'E-2026-09-25-3 is absent from record 21539068`s description (read %s, modified %s): b535 edited two other records, and '
            '(R150)(1) left the lv description to a separate ruling not taken; its two RESTS sentences stand on the record as b499 '
            'fetched them (relay data/b575_zenodo_lv.txt)' % (LV['at'], LV['modified'])),
        N6=('HELD' if nodep and kmain == V015 and heads_ok and set(ch) <= PP_ALLOWED and not faces else 'REFUTED',
            'nothing deposits: both records keep their id, version and files (relay data/b575_files_same.txt); SIDE-explicit-formula '
            'main %s and every other kernel`s main unmoved; PLACE-papers changed at %s only; the sealed faces of b566-b574 unedited'
            % (kmain[:7], ch)),
        S1=('HELD' if 'SPIRAL_MAP.md:18' in d2 and 'SPIRAL_MAP.md:41' in d2 and not [x for x in d2 if x.startswith('README')] else 'REFUTED',
            '(N2) refuted in letter at :18 and :41 and README :15 obeys, as registered -- but the list was not complete: :257, :268 '
            'and :443 differ in letter too'),
        S2=('HELD' if not LV['present'] else 'REFUTED', 'E-2026-09-25-3 is absent from the lv description'),
        S3=('HELD' if F['count']['kernel_bridge'] == 83 and [n for n, v in F['count'].items() if v == 83] == ['kernel_bridge'] else 'REFUTED',
            'the fresh count at e0a8ba0 yields 83 only in the Kernel/ + Bridge/ scope (70 + 13); SPIRAL_MAP :43`s "no partition of the '
            'tree yields 83" cites E-2026-07-13-1, whose no-partition finding is for 65 -- printed, not edited'),
        cp5='CLOSED' if (M['equal'] == 11 and c2.get('all_match') and E.get('heading_line') and jl('b575_registry_lines.json').get('lines')
                         and jl('b575_spiral.json').get('plan')) else 'OPEN',
        counts=dict(mirror=M['equal'], differing=d2, registry=jl('b575_registry_lines.json')['lines'], erratum=[E['index_line'], E['heading_line']],
                    lv_present=LV['present'], pp_changed=ch),
    )
    put_json('b575_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))
    print('  CP-5', S['cp5'])


TITLE = ('## CP-5, act two: the deposit mirror at the deposited bytes, Anomaly 1 as a stated pair of pins, the three facts in REGISTRY, '
         'the description at the successor sentence with fetch-back, the lv record read')


def findings():
    Q = _Q()
    S = jl('b575_scores.json')
    c = S['counts']
    Z = jl('b575_zenodo_results.json')['c2']['records']
    F = jl('b575_facts.json')
    Q.guard_absent(Q.FIND, TITLE)
    e = ['', TITLE, '',
         '*Filed at b575 on the author’s ruling `(R185)`. Banks: relay `data/b575_mirror.txt`, `data/b575_facts.txt`, '
         '`data/b575_kernel_lines.txt`, `data/b575_zenodo_draft.txt`, `data/b575_zenodo_c1.txt`, `data/b575_zenodo_c2.txt`, '
         '`data/b575_files_same.txt`, `data/b575_erratum.txt`, `data/b575_zenodo_lv.txt`. Nothing deposits.*', '',
         '**The mirror** (`(R185)`(2)(i)). `outputs/DEPOSITED-v1.1.2/** -text` committed alone in `.gitattributes`; the two files '
         're-committed at their CRLF bytes. All %d blob md5s now equal the record’s, the content unchanged.' % c['mirror'], '',
         '**Anomaly 1 as a pair** (`(R185)`(2)(ii)), REGISTRY :%d: SIDE-kernel deposited at v1.5 = `0e5233f`, current tag v1.7 = `%s` '
         'read at the remote, with the citation rule beside it. README’s kernel line obeys the rule; SPIRAL_MAP differs from it in '
         'letter at %d lines (%s), each a dated or frozen historical line or a terminal cited at the tag where it landed -- printed, '
         'not edited.' % (c['registry'][0], F['peeled']['SIDE-kernel v1.7']['remote'][:7], len(c['differing']),
                          ', '.join(x.replace('SPIRAL_MAP.md', '') for x in c['differing'])), '',
         '**The three facts** (`(R185)`(2)(iii)), REGISTRY :%d, :%d, :%d, each verified before it was written: SIDE-kernel v1.1’s '
         '“83 files” is the `.lean` count of `Kernel/` (70) and `Bridge/` (13) at `e0a8ba0`, re-counted; SIDE-t7-topology-cmb v0.3 '
         'and SIDE-silence-principle v0.2.0 peel at the remotes to the SHAs SPIRAL_MAP states. SPIRAL_MAP :41, :140 and :533 carry '
         'their pointers. SPIRAL_MAP :43’s annotation says no partition of the tree yields 83; E-2026-07-13-1, which it cites, says '
         'that of 65 -- printed, not edited.' % tuple(c['registry'][1:]), '',
         '**The description** (`(R185)`(2)(iv)). The sentences of REGISTRY :956 and :960, byte-exact from the bank, written into the '
         'descriptions of records 21520474 and 21539167 by the `(R110)` route; both fetch-backs MATCH, byte for byte, on the first try '
         '(%s, %s); ids, versions and files unchanged. The sentence of :958, superseded by :960’s, stays in this ledger’s lineage and '
         'is not on the records. Recorded as E-2026-10-01-1 (ERRATA :%d, :%d).' % (Z['21520474'].get('fetchback_at'),
                                                                                 Z['21539167'].get('fetchback_at'), c['erratum'][0], c['erratum'][1]), '',
         '**The lv record** (`(R185)`(2)(v)). Record 21539068 read without a write: E-2026-09-25-3 is absent from its description, '
         'and the two sentences that erratum reads as resting on the false clause stand there as b499 fetched them. `(R150)`(1) left '
         'that description to a separate ruling, not taken since; recorded, not appended.', '',
         '**CP-5 is %s.**' % S['cp5'], '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; the seat’s (S1) %s, (S2) %s, (S3) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R185)`(4): CP-7 act one, the observation document’s purpose statement drafted from the ledgers in the '
         'author’s own sentences and printed for ruling; and at the same boundary the memory and mirror refresh per `(R157)`(6).', '',
         '*Nothing deposits; no kernel touched; README, FACES_LEDGER and the pages unedited; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b575_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE), append=r, title=TITLE))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE))


THEAD = ('### b575 — lane three, act three under (R185): CP-5 -- the mirror at the deposited bytes, Anomaly 1 as a pair of pins, the '
         'three facts in REGISTRY, the description by the (R110) route with fetch-back, the lv record read')


def trail():
    Q = _Q()
    S = jl('b575_scores.json')
    c = S['counts']
    fj, wt = jl('b575_findings.json'), jl('b575_weight.json')
    Q.guard_absent(Q.OT, THEAD)
    rows = ['', THEAD, '',
            '**(R185) ratified.** (1) b574 at its weight. (2) The five items: (i) the mirror, (ii) Anomaly 1, (iii) the three facts, '
            '(iv) the description, (v) the lv record. (3) CP-5 closes when all five land. (4) The act after.', '',
            '**Entered:** FINDINGS.md:%s and :%s (b574’s weight; the H26a letter, the navigator’s), :%s (the entry); REGISTRY.md:%s; '
            'SPIRAL_MAP.md :41, :140, :533 (the pointers); ERRATA.md:%s and :%s (E-2026-10-01-1); `.gitattributes` and the mirror’s two '
            'files; this record. Zenodo: the descriptions of records 21520474 and 21539167. No kernel, README, FACES_LEDGER or '
            'CORRESPONDENCE line.' % (wt['lines'][0], wt['lines'][1], fj['entry_line'], ', :'.join(str(x) for x in c['registry']),
                                      c['erratum'][0], c['erratum'][1]), '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**CP-5 %s** -- (i)-(v) of `(R185)`(2) landed with their prints.' % S['cp5'], '',
            '**For the author:** the lv description still carries the two sentences E-2026-09-25-3 reads as resting on the false '
            'clause (`(R150)`(1)’s separate ruling, untaken); SPIRAL_MAP :43 cites E-2026-07-13-1 for “no partition yields 83”, which '
            'that erratum says of 65; SPIRAL_MAP :18, :41, :257, :268, :443 differ from the citation rule in letter.', '',
            '**Next:** per `(R185)`(4), CP-7 act one -- the observation document’s purpose statement drafted from the ledgers in the '
            'author’s own sentences (the register sentence, the ceiling’s seven sentences, the three layers of `(R153)`) and printed '
            'for ruling, no edition written; and, at the same boundary, the memory and mirror refresh per `(R157)`(6), carrying v0.2 '
            'through v0.15 and the two pages.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; README, FACES_LEDGER and the pages untouched; row U1 '
            'unedited; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r = Q.append_to(Q.OT, NL.join(rows))
    put_json('b575_trail.json', dict(line=Q.line_of(Q.OT, THEAD), head=THEAD, append=r))
    print(jl('b575_trail.json')['line'])


def desk():
    S = jl('b575_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')
    L = ['=' * 104, 'b575 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in NK if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.** ### CP-5 %s.'
          % (nh, 6 - nh, sh, 3 - sh, S['cp5']), '']
    L += rd('b575_defects.txt').rstrip(NL).split(NL)
    put_txt('b575_desk_notes.txt', L)


def components():
    S = jl('b575_scores.json')
    c = S['counts']
    fj, tj, wt = jl('b575_findings.json'), jl('b575_trail.json'), jl('b575_weight.json')
    L = ['b575 -- THE COMPONENTS, BANKED UNDER (R185).', '',
         '### COMPONENT 0 : the process listing (four children of the seat`s stopped task stopped by PID) ; b574`s closing push-out '
         'relay c8052113 ; push-b574* branches deleted by name (data/b575_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b574`s weight FINDINGS :%s, the navigator`s line :%s ; .gitattributes rule alone ; the mirror re-committed ; '
         '%d of 11 blob md5s equal the record`s (data/b575_mirror.txt) ; N1 %s' % (wt['lines'][0], wt['lines'][1], c['mirror'], S['N1'][0]),
         '### COMPONENT 2 : the pins at the remotes and the count (data/b575_facts.txt) ; REGISTRY :%s ; SPIRAL_MAP pointers :41, :140, '
         ':533 ; the kernel lines (data/b575_kernel_lines.txt), differing %s ; N2 %s, N3 %s' % (
             ', :'.join(str(x) for x in c['registry']), c['differing'], S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the text against REGISTRY (data/b575_zenodo_draft.txt) ; the dry plan (c1) ; the writes and fetch-backs '
         '(c2) MATCH on both ; files unchanged (data/b575_files_same.txt) ; E-2026-10-01-1 ERRATA :%d, :%d ; N4 %s' % (
             c['erratum'][0], c['erratum'][1], S['N4'][0]),
         '### COMPONENT 4 : record 21539068 read (data/b575_zenodo_lv.txt) ; E-2026-09-25-3 %s ; recorded under (R150)(1) ; N5 %s' % (
             'PRESENT' if c['lv_present'] else 'ABSENT', S['N5'][0]),
         '### COMPONENT 5 : FINDINGS :%s ; OPEN_TRAILS :%s (the record) ; CP-5 %s ; next: CP-7 act one and the refresh'
         % (fj['entry_line'], tj['line'], S['cp5'])]
    put_txt('b575_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b575_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
