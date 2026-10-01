# -*- coding: utf-8 -*-
"""b576_record.py -- THE ACT'S RECORD TOOL, UNDER (R186). ### ONE SUBCOMMAND PER BANK.

### ### b576: LANE THREE, ACT FOUR -- CP-7 ACT ONE. Subcommands write only `data/b576_*` unless the
### docstring names a ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then
### `os.replace`). The one Zenodo write of the act is `tools/b576_zenodo.py`'s; this tool makes no platform call.
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
PRE_PP = 'b95e5c0'
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
    '(a) b576_zenodo.py WAS CARRIED FROM b575`s WITH b575`s DEFECT (c) UNREPAIRED, knowingly: its files-unchanged predicate compares '
    'the deposition API`s bare checksums with the records API`s md5:-prefixed ones and printed False again on identical files. A new '
    'tool of this act could have carried the repair; it carried the defect. The files are read like for like '
    '(data/b576_files_same.txt).',
    '(b) THE ERRATA BANK`S FIRST RUN PRINTED E-2026-10-01-2`S HEADING LINE EMPTY: the lv entry banked its heading at :790, and the '
    'corpus entry`s index line, inserted afterwards at :297, moved every line below it by one. The bank now locates each line by '
    'its text when it is written.',
    '(c) THE MEMORY REWRITE`S FIRST PASS MOVED 16 OF THE 17 b559-b575 PROJECT HOOKS: it matched file names ending _bNNN.md, and '
    'project_audit_b565_paused.md ends otherwise. Counted against the files (17) and moved by name; the archive pointer reads 17.',
    '(d) THE SEALED FACE`S WRITE LIST OMITS A WRITE OF THE MIRROR BUILDER: tools/mirror_build.ps1 also rewrites relay '
    'tools/mirror_prevbuild.json (the staged names it diffs the next build against), which b537`s face named and this face did '
    'not -- a write list omits the late ritual. G-WRITELIST-KINDS fails live on it, rightly; the face is not edited, the file is '
    'committed with the act, and the suite reads 68 of 69 with this arm failing for this cause.',
]


def defects():
    put_txt('b576_defects.txt', ['### b576 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


def _Q():
    import b566_record as R6
    return R6.Q


RELAY = ROOT.replace('\\', '/')
FERRY = {'R153': 'data/b543_ferry.txt', 'R157': 'data/b547_ferry.txt', 'R166': 'data/b556_ferry.txt', 'R186': 'data/b576_ferry.txt',
         'R150': 'data/b540_ferry.txt'}


# ================================================================================ READING (1)
READS = [
    ('(R153)(4), the checkpoints and CP-7', RELAY, 'HEAD', FERRY['R153'], list(range(34, 68))),
    ('(R157)(1), the three layers', RELAY, 'HEAD', FERRY['R157'], list(range(8, 22))),
    ('(R166)(1), the principle', RELAY, 'HEAD', FERRY['R166'], 'THE PRINCIPLE'),
    ('PLACE-papers REGISTRY, the seven ceiling lines', PP, PRE_PP, 'REGISTRY.md', [948, 950, 952, 954, 956, 958, 960]),
    ('PLACE-papers README, the register sentence', PP, PRE_PP, 'README.md', [106, 107, 113]),
    ('PLACE-papers ERRATA (E-2026-07-13-1; the partition; E-2026-09-25-3`s lv rows)', PP, PRE_PP, 'ERRATA.md',
     [66, 81, 85, 273, 287, 289, 294, 543, 562, 564, 565, 567]),
    ('PLACE-papers SPIRAL_MAP :43', PP, PRE_PP, 'SPIRAL_MAP.md', [43]),
    ('relay b575`s route bank (c2)', RELAY, 'HEAD', 'data/b575_zenodo_c2.txt', 'MATCH'),
    ('relay b575`s lv bank', RELAY, 'HEAD', 'data/b575_zenodo_lv.txt', '### '),
    ('relay b558`s refresh record', RELAY, 'HEAD', 'data/b558_refresh.txt', '    '),
]


def reads():
    L = ['b576 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        if isinstance(sel, list):
            lines = sel
        elif sel == 'THE PRINCIPLE':
            a = [i for i, l in enumerate(sl, 1) if l.startswith('(1) THE PRINCIPLE')][0]
            lines = list(range(a, a + 9))
        else:
            lines = [i for i, l in enumerate(sl, 1) if sel in l][:40]
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(lines)))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### relay data/b558_editions/ : %s' % sorted(os.listdir(os.path.join(D, 'b558_editions'))))
    put_txt('b576_reads.txt', L)


# ================================================================================ COMPONENT 1
def weight():
    """### PLACE-papers FINDINGS.md (one appended line): (R186)(1) -- b575 at its weight."""
    Q = _Q()
    e = Q.line_of(Q.FIND, '## CP-5, act two: the deposit mirror at the deposited bytes')
    h = '*Appended 2026-10-01 by b576 to b575’s entry (:%s), under `(R186)`(1) -- b575 AT ITS WEIGHT, CP-5 CLOSED:*' % e
    Q.guard_absent(Q.FIND, h)
    a = ('\n%s the deposit mirror holds the deposited bytes, all 11 blob md5s equal to the record’s; Anomaly 1 is a stated pair at '
         'REGISTRY :962, with the citation rule beside it; the three facts at :964, :966 and :968, each verified before it was written; '
         'REGISTRY :956 and :960 stand byte-exact in the descriptions of records 21520474 and 21539167, fetch-back MATCH, recorded as '
         'E-2026-10-01-1; record 21539068 was read with no write. SPIRAL_MAP’s five SIDE-kernel lines differ from the rule in letter as '
         'dated or frozen lines, printed and not edited. (N2) and (N5) refuted as scored; the suite read 69 of 69.\n' % h)
    r = Q.append_to(Q.FIND, a)
    put_json('b576_weight.json', dict(entry=e, line=Q.line_of(Q.FIND, h), append=r))
    print(jl('b576_weight.json'))


def files_same():
    """### Like for like: the fetch-back's files (key, checksum, size) against b575's anonymous fetch from the same records API."""
    fb, old = jl('b576_fetchback_21539068.json'), jl('b575_fetch_21539068.json')
    f1 = sorted((f['key'], f['checksum'], f['size']) for f in fb['files'])
    f0 = sorted((f['key'], f['checksum'], f['size']) for f in old['files'])
    out = dict(same=f1 == f0, files=len(f1), version=fb['metadata'].get('version'), id=fb.get('id'),
               modified=[old.get('modified'), fb.get('modified')])
    put_txt('b576_files_same.txt', ['b576 -- COMPONENT 1: RECORD 21539068`S FILES AFTER THE WRITE, LIKE FOR LIKE', '',
                                    '    files %d ; (key, checksum, size) equal to b575`s fetch : %s ; version %s ; id %s ; modified %s -> %s'
                                    % (len(f1), f1 == f0, out['version'], out['id'], old.get('modified'), fb.get('modified'))])
    put_json('b576_files_same.json', out)


def lv_erratum():
    """### PLACE-papers ERRATA.md: E-2026-10-01-2's index line inserted after E-2026-10-01-1's in the DEPOSIT-FACING list, and its
    ### entry appended at the end. Refuses unless b576_zenodo.py's c2 recorded MATCH."""
    Q = _Q()
    c2 = jl('b576_zenodo_results.json').get('c2') or {}
    if c2.get('all_match') is not True:
        sys.exit('### c2 DID NOT RECORD MATCH -- NO ERRATUM WRITTEN.')
    cell = c2['records']['21539068']
    I = jl('b576_intended_meta.json')
    sa, sb = I['sentences']
    head = ('## E-2026-10-01-2 — The description of SIDE-lv-conservation v0.10.0 now carries E-2026-09-25-3’s two replacement '
            'sentences, appended beneath the two it reads as resting on the false clause (DEPOSIT-FACING; RETAINED AT SIDE-lv-conservation v0.10.0)')
    Q.guard_absent(ERR, head)
    idx = ("- `E-2026-10-01-2` — *DEPOSIT-FACING; RETAINED AT SIDE-lv-conservation v0.10.0* (appended to this list by b576 under "
           "`(R186)`(2))")
    lines = open(ERR, 'rb').read().split(b'\n')
    anchor = [i for i, l in enumerate(lines) if l.startswith('- `E-2026-10-01-1` — '.encode('utf-8'))]
    if len(anchor) != 1:
        sys.exit('### THE INDEX ANCHOR IS NOT FOUND ONCE: %s' % anchor)
    lines.insert(anchor[0] + 1, idx.encode('utf-8'))
    open(ERR + '.tmp', 'wb').write(b'\n'.join(lines))
    os.replace(ERR + '.tmp', ERR)
    fb_old = jl('b575_zenodo_lv.txt'.replace('.txt', '.json')) if os.path.exists(os.path.join(D, 'b575_zenodo_lv.json')) else jl('b575_lv.json')
    body = [
        '', head, '',
        '**Filed 2026-10-01 by b576, on the author’s ruling `(R186)`(2), `(R150)`(1) taken at that ruling, at the write it records. The '
        'record is immutable at its version; its files are unchanged; only its description field was edited, by the `(R110)` route.**', '',
        '**Affected deposit.** SIDE-lv-conservation v0.10.0, tag `v0.10.0` = commit `93c27ec` '
        '([10.5281/zenodo.21539068](https://doi.org/10.5281/zenodo.21539068)) — the record description.', '',
        '**What was written.** One paragraph appended at the description’s end, carrying E-2026-09-25-3’s two replacement sentences for '
        'this description, in the erratum’s order: ERRATA :564’s and :567’s. The two sentences they answer, “Rather than leaving that '
        'clause as prose …” and “The one deliberately open obligation …”, stay on the record as written; descriptions grow by append. '
        'The ruling’s word “sentence” was read, on the author’s answer before the seal, as the erratum’s two sentences.', '',
        '> ' + sa, '', '> ' + sb, '',
        '**The route and the fetch-back.** relay `tools/b576_zenodo.py`, carried from b575’s: edit, PUT with every other key carried, '
        'publish, then an anonymous fetch-back compared byte for byte with the intended description -- MATCH. The record read with no '
        'write at %s (relay `data/b575_zenodo_lv.txt`); fetch-back at %s (relay `data/b576_zenodo_c2.txt`, '
        '`data/b576_fetchback_21539068.json`).' % (fb_old.get('at'), cell.get('fetchback_at')), '',
        '**What is not corrected.** The record’s title and its other sentences; the deposited files. Nothing here is a statement about '
        'RH or any zero beyond the compiled statements’ own words.', '',
        '**Status.** FILED. Retained at SIDE-lv-conservation v0.10.0.', '']
    r = Q.append_to(ERR, NL.join(body))
    text = io.open(ERR, encoding='utf-8').read().split(NL)
    put_json('b576_lv_erratum.json', dict(index_line=[i for i, x in enumerate(text, 1) if x == idx][0],
                                          heading_line=[i for i, x in enumerate(text, 1) if x == head][0],
                                          stamps=[fb_old.get('at'), cell.get('fetchback_at')], append=r))
    print(jl('b576_lv_erratum.json'))


def spiral():
    """### PLACE-papers SPIRAL_MAP.md: one line inserted directly beneath :43, inside its blockquote."""
    raw = open(SPM, 'rb').read()
    lines = raw.split(b'\n')
    pre = gb(PP, 'show', PRE_PP + ':SPIRAL_MAP.md')
    if raw.replace(b'\r\n', b'\n') != (pre or b'').replace(b'\r\n', b'\n'):
        sys.exit('### SPIRAL_MAP DIFFERS FROM ITS PRE-ACT BLOB -- NO LINE WRITTEN.')
    if not lines[42].startswith('> **[†] Annotation (2026-08-08'.encode('utf-8')):
        sys.exit('### :43 IS NOT THE ANNOTATION')
    line = ("> *(Appended beneath :43 by b576 under the author’s ruling `(R186)`(3), 2026-10-01; :43 stands as written.)* "
            "**Correction:** E-2026-07-13-1 does not say that no partition of the tree yields 83. It says the tag annotation’s "
            "“across 65 files” reproduces under no scope (ERRATA :85), and that 83 is exact for the v1.1 `Kernel/` + `Bridge/` scope, "
            "70 + 13 (ERRATA :81) -- re-counted at `e0a8ba0` by b575 (REGISTRY :964). Errata: `E-2026-10-01-3`.")
    lines.insert(43, line.encode('utf-8'))
    open(SPM + '.tmp', 'wb').write(b'\n'.join(lines))
    os.replace(SPM + '.tmp', SPM)
    after = io.open(SPM, encoding='utf-8').read().split(NL)
    put_txt('b576_spiral.txt', ['b576 -- COMPONENT 1: SPIRAL_MAP :43 CORRECTED BENEATH, (R186)(3)', '',
                                '    :43 %s' % after[42][:200], '    :44 %s' % after[43], '    :45 %s' % after[44][:120]])
    put_json('b576_spiral.json', dict(line=44, text=line))


def corpus_erratum():
    """### PLACE-papers ERRATA.md: E-2026-10-01-3, corpus-facing -- an index line after the INTERNAL-RECORD list's last line, and
    ### its entry appended at the end."""
    Q = _Q()
    head = ('## E-2026-10-01-3 — SPIRAL_MAP :43’s annotation cites E-2026-07-13-1 for a finding it does not make (CORPUS-FACING; NO '
            'DEPOSITED ARTIFACT IS AFFECTED)')
    Q.guard_absent(ERR, head)
    idx = ("- `E-2026-10-01-3` — *CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED* (appended to this list by b576 under "
           "`(R186)`(3))")
    lines = open(ERR, 'rb').read().split(b'\n')
    anchor = [i for i, l in enumerate(lines) if l.startswith('- `E-2026-09-03-1` — '.encode('utf-8'))]
    if len(anchor) != 1:
        sys.exit('### THE INTERNAL-RECORD ANCHOR IS NOT FOUND ONCE: %s' % anchor)
    lines.insert(anchor[0] + 1, idx.encode('utf-8'))
    open(ERR + '.tmp', 'wb').write(b'\n'.join(lines))
    os.replace(ERR + '.tmp', ERR)
    body = [
        '', head, '',
        '**Filed 2026-10-01 by b576, on the author’s ruling `(R186)`(3). Corpus-facing: no deposited artifact is affected.**', '',
        '**What was wrong.** SPIRAL_MAP :43, the annotation of 2026-08-08 to the frozen SIDE-kernel v1.1 row, says “no partition of '
        'the tree yields 83”, citing E-2026-07-13-1. That erratum says the opposite of 83: the count is exact for the v1.1 `Kernel/` + '
        '`Bridge/` scope, 70 + 13 (ERRATA :81); its no-partition finding is for the tag annotation’s “across 65 files” (ERRATA :85).', '',
        '**The correction.** One line directly beneath SPIRAL_MAP :43 states it; :43 stands as written. b575 re-counted the scope at '
        '`e0a8ba0` by the erratum’s method (REGISTRY :964; relay `data/b575_facts.txt`).', '',
        '**Status.** FILED.', '']
    r = Q.append_to(ERR, NL.join(body))
    text = io.open(ERR, encoding='utf-8').read().split(NL)
    put_json('b576_corpus_erratum.json', dict(index_line=[i for i, x in enumerate(text, 1) if x == idx][0],
                                              heading_line=[i for i, x in enumerate(text, 1) if x == head][0], append=r))
    print(jl('b576_corpus_erratum.json'))


def errata_bank():
    a, b, s = jl('b576_lv_erratum.json'), jl('b576_corpus_erratum.json'), jl('b576_spiral.json')
    t = io.open(ERR, encoding='utf-8').read().split(NL)
    # ### the lines as they stand now, located by their text: the corpus entry's index line, inserted after the lv entry was
    # ### written, moved every line below :297 by one (defect (b)).
    for j, eid, name in ((a, 'E-2026-10-01-2', 'b576_lv_erratum.json'), (b, 'E-2026-10-01-3', 'b576_corpus_erratum.json')):
        j['index_line'] = [i for i, x in enumerate(t, 1) if x.startswith('- `%s` — ' % eid)][0]
        j['heading_line'] = [i for i, x in enumerate(t, 1) if x.startswith('## %s — ' % eid)][0]
        put_json(name, j)
    L = ['b576 -- COMPONENT 1: THE ERRATA WRITTEN, (R186)(2)-(3)', '',
         '### E-2026-10-01-2 (deposit-facing) : index :%d ; heading :%d' % (a['index_line'], a['heading_line']),
         '    %s' % t[a['index_line'] - 1], '    %s' % t[a['heading_line'] - 1],
         '### E-2026-10-01-3 (corpus-facing) : index :%d ; heading :%d' % (b['index_line'], b['heading_line']),
         '    %s' % t[b['index_line'] - 1], '    %s' % t[b['heading_line'] - 1],
         '### SPIRAL_MAP :%d -- %s' % (s['line'], s['text'][:200])]
    put_txt('b576_errata.txt', L)


# ================================================================================ COMPONENT 2: THE PURPOSE STATEMENT
SRC = {
    'R186(4)': ('relay data/b576_ferry.txt', 'R186'),
    'R157(1)': ('relay data/b547_ferry.txt', 'R157'),
    'R153(4)': ('relay data/b543_ferry.txt', 'R153'),
    'R166(1)': ('relay data/b556_ferry.txt', 'R166'),
    'README': ('PLACE-papers README.md', None),
    'REGISTRY': ('PLACE-papers REGISTRY.md', None),
}
# ### each draft: a list of (kind, text, source); kind S = the author's words (verbatim), C = the seat's connective (bracketed)
DRAFT_A = [
    ('C', 'This document observes', None),
    ('S', "the kernel's declarations at pins, the bench's banked numbers, the field at its pins", 'R186(4)'),
    ('C', ':', None),
    ('S', 'the record of what was done and measured', 'R157(1)'),
    ('C', '. It writes to the', None),
    ('S', 'observational layer', 'R157(1)'),
    ('C', ',', None),
    ('S', 'append-only, dated', 'R157(1)'),
    ('C', '. Its readers are', None),
    ('S', 'the editions and the monograph, which cite it and do not restate it', 'R186(4)'),
    ('C', '. It is not a claim:', None),
    ('S', 'RH reduced to a single located clause, reduction machine-verified', 'README'),
    ('C', '; not', None),
    ('S', 'RH proved', 'README'),
    ('C', '. It is written', None),
    ('S', 'without narrative', 'R153(4)'),
    ('C', '. It is not a tracking document:', None),
    ('S', 'The cascade is the audit', 'R166(1)'),
    ('C', '.', None),
    ('S', 'The work-orders it has generated are the research', 'R166(1)'),
    ('C', ';', None),
    ('S', 'the editions wait for the work-orders', 'R166(1)'),
    ('C', '.', None),
]
DRAFT_B = [
    ('C', 'Its object:', None),
    ('S', "the kernel's declarations at pins, the bench's banked numbers, the field at its pins", 'R186(4)'),
    ('C', '. Its layer, the observational:', None),
    ('S', 'relay banks, the four ledgers, the terminal table, the censuses — append-only, dated, the record of what was done and measured', 'R157(1)'),
    ('C', '. Its readers:', None),
    ('S', 'the editions and the monograph, which cite it and do not restate it', 'R186(4)'),
    ('C', ',', None),
    ('S', 'written from the observational layer at checkpoints', 'R157(1)'),
    ('C', '. It is not a claim:', None),
    ('S', 'neither is proved', 'REGISTRY'),
    ('C', '; it is written', None),
    ('S', 'without narrative', 'R153(4)'),
    ('C', '; it is not a tracking document:', None),
    ('S', "an audit of a conclusion's standing is not its documentation", 'R166(1)'),
    ('C', '.', None),
]


def _norm(t):
    return ' '.join(t.replace(chr(13), '').split())


def _source_text(key):
    if key in ('README', 'REGISTRY'):
        return g(PP, 'show', '%s:%s.md' % (PRE_PP, key))
    return io.open(os.path.join(ROOT, FERRY[SRC[key][1]]), encoding='utf-8').read()


def _locate(key, frag):
    """### the fragment in its source, whitespace-normalized (the ferries are hard-wrapped); the line where it starts."""
    t = _source_text(key)
    nt = _norm(t)
    if frag not in nt:
        return None
    k = nt.index(frag)
    # ### map the normalized offset back to a line: count the words before it
    words_before = len(nt[:k].split())
    seen = 0
    for i, l in enumerate(t.split(NL), 1):
        seen += len(l.split())
        if seen > words_before:
            return i
    return None


def _render(draft):
    out = ''
    for kind, text, _ in draft:
        if not out:
            out = text
        elif text[:1] in '.,;:' or text.startswith('--') and False:
            out += text
        else:
            out += ' ' + text
    return out


def drafts():
    """### Component 2: the document named; the sources printed; the two drafts with every fragment located; the work-lists."""
    L = ['b576 -- COMPONENT 2: THE PURPOSE STATEMENT, DRAFTED FOR RULING, (R186)(4) -- WRITTEN INTO NO DOCUMENT', '']
    sl = io.open(os.path.join(D, 'b543_ferry.txt'), encoding='utf-8').read().split(NL)
    L += ['### THE OBSERVATION DOCUMENT. (R153)(4)`s CP-7, relay data/b543_ferry.txt :63-:67, names none:']
    L += ['    :%-4d %s' % (n, sl[n - 1]) for n in range(63, 68)]
    files = g(PP, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
    hits = [f for f in files if 'observ' in f.lower()]
    L += ['### PLACE-papers HEAD %s : files whose path names observation: %s ; control, the same search for "REGISTRY.md": %s'
          % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), hits or 'NONE', [f for f in files if f == 'REGISTRY.md']),
          '### ### **NO OBSERVATION DOCUMENT EXISTS AND (R153) NAMES NONE: ITS WORKING NAME IS THE AUTHOR`S. IT HAS NO HEAD.**', '']
    L += ['### THE SOURCES, by path and line:']
    srcs = []
    for draft in (DRAFT_A, DRAFT_B):
        for kind, text, key in draft:
            if kind == 'S' and (key, text) not in srcs:
                srcs.append((key, text))
    allfound = True
    for key, text in srcs:
        ln = _locate(key, text)
        allfound = allfound and ln is not None
        L.append('    %-9s %-28s :%-6s %s' % (key, SRC[key][0], ln if ln else '### NOT FOUND', text))
    L += ['', '### THE NOTES THE SOURCES CARRY, FOR THE RULING:',
          '    (a) "the three layers of (R153)": they are named in (R157)(1), relay data/b547_ferry.txt :8-:21; (R153) does not name them.',
          '    (b) the register sentence is README :106 with :107 beside it; REGISTRY carries no copy of it. README :113 ((R145)(2)) says',
          '        that sentence is supportable only with the clause named as h2_sign and the two lines below beside it -- draft A quotes it',
          '        bare and would need that beside it; draft B uses REGISTRY :960`s "neither is proved" instead.',
          '    (c) (R153)(4) makes the observation document Tier K with a Correspondence table; (R157)(1) places the four ledgers and the',
          '        relay banks in the observational layer and the keystones` editions in the clarified layer; (R186)(4) says the document',
          '        writes at the observational layer. Which of these the document`s Correspondence table answers to is the author`s.',
          '    (d) "a tracking document" is (R186)(4)`s own word; no earlier ruling or ledger sentence uses it.', '']
    out = {}
    for name, draft in (('A', DRAFT_A), ('B', DRAFT_B)):
        text = _render(draft)
        nw = len(text.replace('--', ' ').split())
        conn = sum(len(t.split()) for k, t, _ in draft if k == 'C' and t.strip(' .,;:-'))
        out[name] = dict(text=text, words=nw, connective_words=conn)
        L += ['### DRAFT %s -- %d words (at most 120: %s) ; the seat`s connective words %d ; every author fragment located : %s'
              % (name, nw, nw <= 120, conn, all(_locate(k, t) for kk, t, k in draft if kk == 'S')),
              '', '    ' + text, '', '    its fragments, in order (S the author`s words with source and line; C the seat`s connective):']
        for kind, t, key in draft:
            L.append('      %s %-60s %s' % (kind, t[:60], ('%s :%s' % (SRC[key][0], _locate(key, t))) if kind == 'S' else '[connective]'))
        L.append('')
    L += ['### DRAFT A carries the register sentence and (R166)(1)`s three clauses; DRAFT B carries the ceiling`s last clause and',
          '### (R166)(1)`s audit sentence. Both state the four things in the ruled order. NOTHING IS WRITTEN INTO ANY DOCUMENT.', '']
    W = []
    for f in sorted(os.listdir(os.path.join(D, 'b558_editions'))):
        n = len(io.open(os.path.join(D, 'b558_editions', f), encoding='utf-8', errors='replace').read().split(NL))
        W.append((f[:-4], n))
    L += ['### THE EDITION WORK-LISTS (relay data/b558_editions/), BY KEYSTONE, FOR THE ORDER OF CP-7 ACT TWO: %d' % len(W)]
    L += ['    %-40s %5d lines' % w for w in W]
    put_txt('b576_purpose_drafts.txt', L)
    put_json('b576_purpose_drafts.json', dict(drafts=out, sources_found=allfound, worklists=W, doc_hits=hits))
    print({k: (v['words'], v['connective_words']) for k, v in out.items()}, 'sources found', allfound, 'worklists', len(W))


# ================================================================================ THE SCORING, THE RECORD, THE REFRESH
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
EF = 'D:/SIDE-explicit-formula'
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}
PP_ALLOWED = {'ERRATA.md', 'SPIRAL_MAP.md', 'FINDINGS.md', 'OPEN_TRAILS.md'}
ZIP = r'D:\MY-DOwnloads\mirror-refresh-2026-10-01.zip'
PAGES = ('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md')
MEMDIR = r'C:\Users\echo chamber\.claude\projects\D--\memory'


def scores():
    Z = jl('b576_zenodo_results.json').get('c2') or {}
    cell = (Z.get('records') or {}).get('21539068', {})
    E2 = jl('b576_lv_erratum.json')
    P = jl('b576_purpose_drafts.json')
    FS = jl('b576_files_same.json')
    M = jl('b576_mirror.json') if os.path.exists(os.path.join(D, 'b576_mirror.json')) else {}
    ch = sorted(set(x for x in g(PP, 'diff', '--name-only', PRE_PP).split(NL) if x.strip()))
    kmain = g(EF, 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    roster = [x for x in g(ROOT, 'diff', '--name-only', 'HEAD', '--', 'tools/mirror_roster.json').split(NL) if x.strip()] or \
        [x for x in g(ROOT, 'log', '--name-only', '--pretty=format:', '3aff82e8..HEAD', '--', 'tools/mirror_roster.json').split(NL) if x.strip()]
    tries = cell.get('tries') or []
    words = {k: v['words'] for k, v in P['drafts'].items()}
    conn = {k: v['connective_words'] for k, v in P['drafts'].items()}
    S = dict(
        N1=('HELD' if Z.get('all_match') and len(tries) == 1 and E2.get('heading_line') else 'REFUTED',
            'the single write`s fetch-back MATCHES on its first try (%s), byte for byte; E-2026-10-01-2 written, ERRATA :%s (index) and '
            ':%s (entry); the record`s id, version and files unchanged (relay data/b576_files_same.txt)'
            % (cell.get('fetchback_at'), E2.get('index_line'), E2.get('heading_line'))),
        N2=('HELD' if 'FINDINGS.md' in P.get('doc_hits', []) else 'REFUTED',
            '(R153)(4)`s CP-7 (relay data/b543_ferry.txt :63-:67) names no document: its working name is the author`s; it is Tier K '
            'with a Correspondence table; no file in PLACE-papers is it (search for observation: %s; control REGISTRY.md found). '
            'FINDINGS.md is one of the four ledgers of the observational layer ((R157)(1))' % (P.get('doc_hits') or 'NONE')),
        N3=('HELD' if P['sources_found'] and not any(conn.values()) else 'REFUTED',
            'every author fragment is found verbatim at its line, but not only in REGISTRY, (R153) or (R166): the three layers are '
            '(R157)(1)`s, the register sentence README :106-:107`s, the readers clause and "a tracking document" (R186)(4)`s own; '
            'and each draft needs connective words of the seat`s -- A %d, B %d' % (conn.get('A'), conn.get('B'))),
        N4=('PENDING', 'scored on the mirror bank, built after the last PLACE-papers push') if not M else (
            'HELD' if all(M['manifest_has'].get(p) for p in PAGES) and M['manifest_has'].get('ERRATA.md') and M.get('errata_carries') else 'REFUTED',
            'the MANIFEST (md5 %s) lists both pages and ERRATA.md (last-commit %s); MANIFEST rows are files, not entries -- the zipped '
            'ERRATA.md carries E-2026-10-01-2 and E-2026-10-01-3: %s (relay data/b576_mirror.txt)'
            % (M.get('manifest_md5'), M.get('errata_commit'), M.get('errata_carries'))),
        N5=('PENDING', 'scored after the refresh') if not M else (
            'HELD' if (FS.get('same') and kmain == V015 and heads_ok and set(ch) <= PP_ALLOWED and not roster) else 'REFUTED',
            'nothing deposits (record 21539068 keeps id, version v0.10.0 and its file); every kernel`s main unmoved; PLACE-papers changed '
            'at %s only -- but one relay instrument file was edited, the mirror roster (two page paths appended, as (R186)(5) orders '
            'and the face declared), which the expectation`s list does not name' % ch),
        S1=('HELD' if 'FINDINGS.md' not in P.get('doc_hits', []) and not P.get('doc_hits') else 'REFUTED',
            '(R153) names no document and none exists'),
        S2=('HELD' if any(conn.values()) else 'REFUTED',
            'the three layers are (R157)(1)`s, the register sentence README`s; connective words A %d, B %d' % (conn.get('A'), conn.get('B'))),
        S3=('PENDING', 'scored on the mirror bank') if not M else (
            'HELD' if all(M['manifest_has'].get(p) for p in PAGES) and M.get('errata_carries') and roster else 'REFUTED',
            'the roster`s append (a relay instrument file) refutes (N5) in letter; with it the MANIFEST lists both pages, and the zipped '
            'ERRATA.md carries E-2026-10-01-2'),
        counts=dict(words=words, connective=conn, worklists=len(P['worklists']), pp_changed=ch, mirror=bool(M)),
    )
    put_json('b576_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


TITLE = ('## CP-7, act one: the observation document’s purpose statement drafted from the author’s sentences, two drafts for ruling; '
         'the lv description answered by append; SPIRAL_MAP :43 corrected beneath; the refresh')


def records_pp():
    """### PLACE-papers: OPEN_TRAILS (CP-5`s closing line at :11417; the trail record) and FINDINGS (the entry). N4, N5 and S3 are
    ### scored on the mirror bank after the push (reading (vi))."""
    Q = _Q()
    S = jl('b576_scores.json')
    E2, E3, P = jl('b576_lv_erratum.json'), jl('b576_corpus_erratum.json'), jl('b576_purpose_drafts.json')
    wt = jl('b576_weight.json')
    lane = Q.line_of(Q.OT, "> LANE THREE — THE CLARIFIED LAYER, after lane two's (a) and (b) at least")
    h0 = '*Appended 2026-10-01 by b576, under the author’s ruling `(R186)`(1), to the critical path’s lane three (:%s) -- CP-5 CLOSED:*' % lane
    Q.guard_absent(Q.OT, h0)
    Q.append_to(Q.OT, '\n%s at b575 (OPEN_TRAILS :11818), its five items landed with their prints: the deposit mirror at the deposited '
                      'bytes, Anomaly 1 as a pair of pins, the three facts in REGISTRY, the descriptions at the successor sentence with '
                      'fetch-back MATCH, the lv record read; the lv description answered by append at b576 (E-2026-10-01-2). CP-4 and '
                      'CP-5 are closed; CP-7 is open at its purpose statement.\n' % h0)
    Q.guard_absent(Q.FIND, TITLE)
    pend = 'scored on the mirror bank after this entry’s push (relay `data/b576_scores.json`)'
    e = ['', TITLE, '',
         '*Filed at b576 on the author’s ruling `(R186)`. Banks: relay `data/b576_zenodo_c2.txt`, `data/b576_errata.txt`, '
         '`data/b576_spiral.txt`, `data/b576_purpose_drafts.txt`, `data/b576_mirror.txt`, `data/b576_refresh.txt`. Nothing deposits.*', '',
         '**The lv description** (`(R186)`(2), `(R150)`(1) taken). E-2026-09-25-3’s two replacement sentences, ERRATA :564’s and :567’s, '
         'appended as one paragraph to record 21539068’s description by the `(R110)` route; the two sentences they answer stand as '
         'written. Fetch-back MATCH, byte for byte, on the first try; id, version and file unchanged. Recorded as E-2026-10-01-2 '
         '(ERRATA :%s, :%s). The ruling’s word “sentence” was read, on the author’s answer before the seal, as the erratum’s two '
         'sentences -- the navigator’s wording, recorded as such.' % (E2['index_line'], E2['heading_line']), '',
         '**SPIRAL_MAP :43** (`(R186)`(3)) stands as written; the line beneath it, :44, states what E-2026-07-13-1 says -- 65 reproduces '
         'under no scope (ERRATA :85), 83 is exact for `Kernel/` + `Bridge/` (ERRATA :81). Corpus-facing: E-2026-10-01-3 (ERRATA :%s, '
         ':%s).' % (E3['index_line'], E3['heading_line']), '',
         '**The purpose statement** (`(R186)`(4)), drafted and written into no document. `(R153)` names no observation document: CP-7’s '
         'working name is the author’s, Tier K with a Correspondence table, and none exists. Two drafts, %d and %d words, each stating '
         'the four things in the ruled order from the author’s sentences located at their lines -- `(R157)`(1)’s layers, README :106’s '
         'register sentence (draft A) or REGISTRY :960’s “neither is proved” (draft B), `(R153)`(4)’s “without narrative”, `(R166)`(1), '
         'and `(R186)`(4)’s own words -- with the seat’s connective words bracketed and counted (relay `data/b576_purpose_drafts.txt`). '
         'The 17 work-lists of b558 listed by keystone beneath them.' % (P['drafts']['A']['words'], P['drafts']['B']['words']), '',
         '**The refresh** (`(R186)`(5)) is taken after this entry’s push, as the standing rule of b537 requires: the mirror roster gains '
         'the two pages; the zip `mirror-refresh-2026-10-01.zip`; the seat’s memory rewritten in b558’s form.', '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s; (N4) and (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s.'
         % (S['N1'][0], S['N2'][0], S['N3'][0], pend, S['S1'][0], S['S2'][0], 'likewise'), '',
         '**Next.** Per `(R186)`(6): CP-7 act two on the author’s ruling of the purpose statement -- the editions in the order the author '
         'gives, each written from its tier table and its CP-1b work-list, the page as its spine.', '',
         '*Nothing deposits; no kernel touched; README, REGISTRY, FACES_LEDGER and the pages unedited; no document of the clarified layer '
         'written; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    head = ('### b576 — lane three, act four under (R186): CP-7 act one -- the purpose statement drafted for ruling; the lv description '
            'answered by append; SPIRAL_MAP :43 corrected beneath; the refresh')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R186) ratified.** (1) b575 at its weight, CP-5 closed. (2) The lv description, `(R150)`(1) taken. (3) SPIRAL_MAP :43. (4) '
            'CP-7 act one, the purpose statement drafted. (5) The refresh. (6) The act after.', '',
            '**Entered:** FINDINGS.md:%s (b575’s weight), :%s (the entry); OPEN_TRAILS.md:%s (CP-5 closed, at lane three); ERRATA.md:%s '
            'and :%s (E-2026-10-01-2), :%s and :%s (E-2026-10-01-3); SPIRAL_MAP.md :44; this record. Zenodo: the description of record '
            '21539068. Relay: the mirror roster, by append, after this push. No kernel, README, REGISTRY, FACES_LEDGER or CORRESPONDENCE '
            'line.' % (wt['line'], Q.line_of(Q.FIND, TITLE), Q.line_of(Q.OT, h0), E2['index_line'], E2['heading_line'],
                       E3['index_line'], E3['heading_line']), '',
            '**The navigator’s wording, recorded:** `(R186)`(2)’s “the erratum’s correction sentence” was read, on the author’s answer '
            'before the seal, as E-2026-09-25-3’s two replacement sentences for that description, ERRATA :564’s then :567’s.', '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) and (N5) scored on the mirror bank after this push.** The seat’s own: (S1) %s, (S2) %s, '
            '(S3) likewise.' % (S['N1'][0], S['N2'][0], S['N3'][0], S['S1'][0], S['S2'][0]), '',
            '**For the author:** two drafts of the purpose statement (relay `data/b576_purpose_drafts.txt`), with four notes -- the layers '
            'are `(R157)`(1)’s; README :113 qualifies the register sentence draft A quotes; `(R153)`(4)’s Tier K with a Correspondence '
            'table against `(R186)`(4)’s observational layer; “a tracking document” is `(R186)`(4)’s own word.', '',
            '**Next:** per `(R186)`(6), CP-7 act two on the author’s ruling of the purpose statement: the editions in the order the author '
            'gives, each from its tier table and its CP-1b work-list, the page as its spine.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b576_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE), title=TITLE, append=r))
    put_json('b576_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, cp5_line=Q.line_of(Q.OT, h0), lane=lane, append=r2))
    print(jl('b576_findings.json')['entry_line'], jl('b576_trail.json'))


def mirror_bank():
    """### After the build and the verify: the zip read back -- its entries, the MANIFEST md5 and rows, the pages and ERRATA."""
    import zipfile
    zf = zipfile.ZipFile(ZIP)
    names = zf.namelist()
    man = [n for n in names if n.endswith('MANIFEST.md')]
    mb = zf.read(man[0]) if man else b''
    mt = mb.decode('utf-8', 'replace')
    rows = [l for l in mt.split(NL) if l.startswith('|') and not l.startswith('|--') and not l.startswith('| file')]
    has = {p: any(p in l for l in rows) for p in PAGES + ('ERRATA.md',)}
    er = [n for n in names if n.endswith('ERRATA.md') and 'DEPOSITED' not in n]
    ert = zf.read(er[0]).decode('utf-8', 'replace') if er else ''
    carries = '## E-2026-10-01-2 — ' in ert and '## E-2026-10-01-3 — ' in ert
    erow = [l for l in rows if 'ERRATA.md' in l]
    ecommit = re.findall(r'\b([0-9a-f]{7})\b', erow[0]) if erow else []
    vt = rd('b576_mirror_verify.txt')
    import datetime
    zt = datetime.datetime.fromtimestamp(os.path.getmtime(ZIP), datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    pp_push = re.search(r'capture on -> \S+ \((\S+)\)', rd('b576_push_out.txt'))
    L = ['b576 -- COMPONENT 3: THE MIRROR, (R186)(5) -- BUILT AFTER THE LAST PLACE-papers PUSH', '',
         '    zip : %s ; %d entries ; %d bytes ; written (UTC) %s' % (ZIP, len(names), os.path.getsize(ZIP), zt),
         '    PLACE-papers last push of this act began (UTC) %s (relay data/b576_push_out.txt) ; HEAD %s ; ls-remote main %s'
         % (pp_push.group(1) if pp_push else None, g(PP, 'rev-parse', '--short=7', 'HEAD').strip(),
            g(PP, 'ls-remote', 'origin', 'refs/heads/main').split('\t')[0][:7]),
         '    MANIFEST.md md5 : %s (%d bytes) ; rows %d' % (hashlib.md5(mb).hexdigest(), len(mb), len(rows)),
         '    the two pages and ERRATA.md in the MANIFEST : %s' % has,
         '    ERRATA.md`s MANIFEST row : %s' % (erow[0][:200] if erow else '### NONE'),
         '    the zipped ERRATA.md carries E-2026-10-01-2 and E-2026-10-01-3 : %s' % carries,
         '    the verify (relay data/b576_mirror_verify.txt) : %s' % ([l.strip() for l in vt.split(NL) if 'VERDICT' in l or 'CLAUSE' in l][:4]),
         '    the previous mirror : mirror-refresh-2026-09-29-b558.zip, MANIFEST.md md5 09cc39604fa935b1e81c4e940a789823',
         '', '### ### **THE ZIP, FOR THE AUTHOR: %s**' % ZIP]
    put_txt('b576_mirror.txt', L)
    put_json('b576_mirror.json', dict(zip=ZIP, entries=len(names), manifest_md5=hashlib.md5(mb).hexdigest(), rows=len(rows), manifest_has=has,
                                      errata_carries=carries, errata_commit=ecommit[:1], written=zt,
                                      verify_clean='CLEAN ON ALL THREE CLAUSES' in vt))
    print(jl('b576_mirror.json'))


def refresh_bank(before_lines, before_entries):
    """### The memory record rewritten in b558's form, counted before and after; every linked file exists."""
    mp = os.path.join(MEMDIR, 'MEMORY.md')
    t = io.open(mp, encoding='utf-8').read().split(NL)
    ents = [l for l in t if l.startswith('- [')]
    links = re.findall(r'\]\(([^)]+\.md)\)', NL.join(t))
    missing = [x for x in links if not os.path.exists(os.path.join(MEMDIR, x))]
    kinds = {}
    for x in links:
        k = x.split('_')[0]
        kinds[k] = kinds.get(k, 0) + 1
    L = ['b576 -- COMPONENT 3: THE REFRESH, (R186)(5) -- THE SEAT`S MEMORY, IN b558`S FORM', '',
         '### THE SEAT`S MEMORY (%s)' % mp,
         '    before : %s lines ; %s index entries' % (before_lines, before_entries),
         '    after  : %d lines ; %d index entries -- %s' % (len(t), len(ents), kinds),
         '    added  : reference_index_archive_b559_b575.md (the project hooks of b559-b575, every linked file kept);',
         '             project_state_cp4_cp5_b559_b576.md (the state from the four ledgers: SIDE-explicit-formula v0.2-v0.15, the two',
         '             pages, CP-4 and CP-5 closed, CP-7 open, the instruments since b558); feedback_standing_rules_b559_b576.md',
         '    every file MEMORY.md links exists : %s %s' % (not missing, missing or ''),
         '### the four ledgers and the relay banks remain the continuity.']
    put_txt('b576_refresh.txt', L)
    put_json('b576_refresh.json', dict(before=[before_lines, before_entries], after=[len(t), len(ents)], kinds=kinds, missing=missing))


def desk():
    S = jl('b576_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    L = ['=' * 104, 'b576 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    nh = sum(1 for k in NK if S[k][0] == 'HELD')
    sh = sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'HELD')
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        nh, sum(1 for k in NK if S[k][0] == 'REFUTED'), sh, sum(1 for k in ('S1', 'S2', 'S3') if S[k][0] == 'REFUTED')), '']
    L += rd('b576_defects.txt').rstrip(NL).split(NL)
    put_txt('b576_desk_notes.txt', L)


def components():
    S = jl('b576_scores.json')
    fj, tj, wt, E2, E3, M = (jl('b576_findings.json'), jl('b576_trail.json'), jl('b576_weight.json'), jl('b576_lv_erratum.json'),
                             jl('b576_corpus_erratum.json'), jl('b576_mirror.json'))
    L = ['b576 -- THE COMPONENTS, BANKED UNDER (R186).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b575`s closing push-out relay 3aff82e8 ; push-b575* branches deleted by '
         'name (data/b576_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b575`s weight FINDINGS :%s ; the two sentences from ERRATA :564, :567 ; the write and fetch-back MATCH '
         '(data/b576_zenodo_c2.txt) ; files unchanged ; E-2026-10-01-2 ERRATA :%s, :%s ; SPIRAL_MAP :44 ; E-2026-10-01-3 ERRATA :%s, '
         ':%s ; N1 %s' % (wt['line'], E2['index_line'], E2['heading_line'], E3['index_line'], E3['heading_line'], S['N1'][0]),
         '### COMPONENT 2 : the purpose statement, two drafts (data/b576_purpose_drafts.txt), %s words ; the 17 work-lists ; N2 %s, '
         'N3 %s' % (S['counts']['words'], S['N2'][0], S['N3'][0]),
         '### COMPONENT 4 : CP-5 closed OPEN_TRAILS :%s ; FINDINGS :%s ; OPEN_TRAILS :%s (the record) ; next: CP-7 act two'
         % (tj['cp5_line'], fj['entry_line'], tj['line']),
         '### COMPONENT 3 : after the last PLACE-papers push -- the roster`s append ; %s (%d entries, MANIFEST md5 %s) ; the memory '
         'rewritten (data/b576_refresh.txt) ; N4 %s, N5 %s' % (M.get('zip'), M.get('entries', 0), M.get('manifest_md5'), S['N4'][0], S['N5'][0])]
    put_txt('b576_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b576_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
