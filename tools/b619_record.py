# -*- coding: utf-8 -*-
"""b619_record.py -- THE ACT'S RECORD TOOL, UNDER (R229). ### ONE SUBCOMMAND PER BANK.

### ### b619: LANE THREE, ACT FORTY-SIX -- THE_KEYSTONE_CENSUS AT v0.4: THE SIX SYNTHESES NAMED IN THEIR ROWS WITH TIERS, THE EDITION,
### KERNEL-TAG AND SIEVE COLUMNS REFRESHED; THE N5 SCORER'S STANDING REPAIR.
### Subcommands write only `data/b619_*` unless the docstring names another file; `dry` on the command line routes every b619 bank and the
### edition to the seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are written by
### encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. The census's data and resolvers are
### tools/b619_census.py's (b610's imported and pointed at this act's pins). The edition is built from v0.3's blob by line transforms --
### each v0.3 line carried, rewritten or removed, every one mapped -- and written once, refused if the file exists. No platform call. No
### Lean call: both pages are re-emitted from their banked probes. The templates are tools/b618_record.py and tools/b610_record.py.
"""
import difflib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b619_census as K  # noqa: E402

C = K.C
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = 'fda4e81b'
STEPZERO = K.STEPZERO
DATE = '2026-10-04'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a7f90da7-bccd-48d0-914d-84e76892ff54/scratchpad'
SESSION_ID = 'a7f90da7-bccd-48d0-914d-84e76892ff54'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
CEN3, CEN4 = K.CEN3, K.CEN4

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b619_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b619_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def lines_of(t):
    t = (t or '').replace(chr(13), '')
    ls = t.split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def _segs(l):
    return R4._segs(l)


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


DEFECTS = []
DEFECT_SHORT = []


def defects(*a):
    L = ['b619 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b619_defects.txt', L)


# ================================================================================ READING (1): THE READS
SYN_FILES = ['phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
             'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md',
             'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md',
             'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md']
OT_LINES = [11864, 12212, 12228, 12356, 12566, 12595, 12597, 12777, 12779, 12781, 12783, 12785, 12787, 12789, 12791, 12793, 12795, 12797]
READS = [
    ('THE_KEYSTONE_CENSUS v0.3, whole', PP, PRE_PP, CEN3, 'ALL', 500),
] + [('the synthesis`s head and tier line', PP, PRE_PP, f, list(range(1, 10)), 420) for f in SYN_FILES] + [
    ('the sieve v0.5: its rows by cluster (the cluster headings)', PP, PRE_PP, K.SIEVE5, ('GREP', r'^## .* — \d+ rows?'), 300),
    ('REGISTRY at a939198: the row update`s Version cells and the row additions', PP, 'a939198', 'REGISTRY.md', ('GREPRANGE', r'^\| (d1|1\.5|p2|m5)', 970, 1070), 300),
    ('relay data/b610_census.txt: the v0.3 mapping`s head, Part D and its verdict lines', RELAY, PRE_RELAY, 'data/b610_census.txt',
     ('GREP', r'^(b610 --|### PART|  R\d\d |### ### \*\*H44|  \(F1\))'), 600),
    ('relay data/b617_currency.txt: its lines naming the census', RELAY, PRE_RELAY, 'data/b617_currency.txt', ('GREP', r'KEYSTONE_CENSUS|census'), 400),
    ('the record tool`s N5 scorer, relay tools/b618_record.py', RELAY, PRE_RELAY, 'tools/b618_record.py', list(range(1273, 1283)) + list(range(1310, 1315)), 300),
    ('OPEN_TRAILS: the form, the precedence order, the build clause, the synthesis form, the ANNEX struck, W-ORD-TAG-REMOTES, '
     'W-ORD-SECOND-READER, b618`s record and correction', PP, PRE_PP, 'OPEN_TRAILS.md', OT_LINES, 1400),
    ('FINDINGS: b618`s weight and entry', PP, PRE_PP, 'FINDINGS.md', [7384, 7386], 600),
    ('relay data/b618_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b618_closing_push_out.txt', ('GREP', r'push_gated: (as-of|DONE|main read)'), 200),
]


def reads(*a):
    L = ['b619 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = _show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = lines_of(t)
        if sel == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        elif isinstance(sel, tuple) and sel[0] == 'GREP':
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        elif isinstance(sel, tuple) and sel[0] == 'GREPRANGE':
            nums = [i + 1 for i, l in enumerate(sl) if sel[2] <= i + 1 <= sel[3] and re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### THE KERNELS` TAGS ARE READ BY ls-remote ONCE PER REPOSITORY IN THE MAPPING (data/b619_census.txt, Part C), not here.',
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b619_reads.txt', L)


def answers(*a):
    calls, results = [], {}
    if os.path.exists(SESSION):
        for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
            try:
                o = json.loads(raw)
            except Exception:
                continue
            m = o.get('message') or {}
            for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b619 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (%s), banked verbatim with the options and the '
         'recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % (n, DATE), '']
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'),
                                                     op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act; the precedence order and the standing lines reached every reading.')
    put_txt('b619_author_answers.txt', L)


KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-spinor': '520abe7'}


def kern_list():
    """### every kernel this act reads: the five the record names and every kernel a census row names (b610`s R-6)"""
    ks = set(KERN_PIN)
    try:
        for row in jl('b619_census.json')['rows']:
            ks |= set(row['kernel_src'])
    except Exception:
        B = K.build(read_remotes=False)
        for row in B['J']:
            ks |= set(row['kernel_src'])
    return sorted(k for k in ks if os.path.isdir('D:/' + k))


def kern_state(ks=None):
    out = {}
    for k in (ks or kern_list()):
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b619_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b619_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ COMPONENT 1: THE RECORD LINES
B618_ENTRY = ('## The living documents’ currency: eight documents fed in their own forms — the loom’s 81-row table, INSTRUMENTS I-16 to '
              'I-39, the faces at v0.17–v0.21')
W_HEAD = '*Appended 2026-10-04 by b619 to b618’s entry (:%d), under `(R229)`(1) -- b618 AT ITS WEIGHT:*'
N5_HEAD = '*Appended 2026-10-04 by b619 beneath the build clause (:12356), under the author’s ruling `(R229)`(2) -- THE N5 SCORER, STANDING:*'


def _count_bank(text):
    m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', text or '')
    return (int(m.group(2)), int(m.group(1))) if m else None


def _b618():
    j = lambda p: json.loads(_show(RELAY, PRE_RELAY, 'data/' + p))   # noqa: E731
    S, RC, RL, FJ, TJ, CJ, HJ = (j('b618_scores.json'), j('b618_regcheck.json'), j('b618_record_lines.json'), j('b618_findings.json'),
                                 j('b618_trail.json'), j('b618_correction.json'), j('b618_h52.json'))
    chk = {n: _count_bank(_show(RELAY, PRE_RELAY, 'data/' + n)) for n in ('b618_checks.txt', 'b618_checks_postpush.txt')}
    return dict(S={k: v[0] for k, v in S.items()}, RC=RC, RL=RL, FJ=FJ, TJ=TJ, CJ=CJ, HJ=HJ, chk=chk)


def _weight(entry):
    W = _b618()
    S, chk, HJ = W['S'], W['chk'], W['HJ']
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    items = HJ['items']
    ins = HJ['instruments']
    return ('\n%s eight appends, each read back as its committed version plus its banked draft byte for byte and committed alone in '
            'PLACE-papers: VERIFICATION_LOOM 5f74760 (one table, 81 rows, b537–b617), INSTRUMENTS 7bc3f33 (I-16 to I-39), THE_METHOD_CANON '
            'a5d1944 (its XXI, the two forms by trail line, the located-clause method by file name and sha256), THE_METHOD_AS_IT_STANDS 1364177 '
            '(the same as an addendum), FACES_LEDGER bff682d (the six faces of v0.17–v0.21, through its own writer), THE_LOAD_BEARING_MAP '
            'f54aa9e (76 nodes by pointer, 77 rows), GAUGE_AND_INVARIANT 81a3a74 (nothing missed, dated), REGISTRY a939198 (17 Version cells, '
            '11 row additions, the SPIRAL_MAP pointer, the two disagreements, SIDE-spinor read at v0.1.0 = b235bc6). H52a-H52d %s (%d of %d '
            'currency items, %d of %d version cells, %d of %d trail lines, the scanner clean on all eight); N1-N5 %s; S1-S5 %s. The χ page '
            'gained one Placement row naming the map (ed43c2f), the ζ page unchanged, the page arms and the frozen control 2 of 2. FINDINGS '
            ':%d, :%d; OPEN_TRAILS :%d, :%d. Relay fda4e81b; PLACE-papers 9dbac4b. The suite %d of %d before the push and %d of %d after it, '
            'G-TABLE-GRADES-DECLARED failing on the sealed face’s own prediction -- two T2-INTERFACES rows adding grade cells the table’s '
            'reader does not add: a prediction refuted, no grade moved, and the dated correction at :%d the proper repair. Accepted by the '
            'author: INSTRUMENTS’ ids I-16 to I-39, the document already holding I-8 to I-15; REGISTRY’s row-update form, fold into the '
            'table at next hand edit; and the generator’s channels at OPEN_TRAILS :12280 as b596’s answer, which now stand in INSTRUMENTS '
            'as an instrument (I-39). Defects (a)-(e), the seat’s. Nothing deposited; no kernel touched.\n' % (
                W_HEAD % entry, 'HOLD' if all(S[k] == 'HOLDS' for k in ('H52a', 'H52b', 'H52c', 'H52d')) else [S[k] for k in ('H52a', 'H52b', 'H52c', 'H52d')],
                sum(x['ok'] for x in items), len(items), W['RC']['ok'], W['RC']['n'], sum(x['ok'] for x in ins), len(ins),
                allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'),
                W['RL']['lines'][0]['line'], W['FJ']['entry_line'], W['TJ']['line'], W['CJ']['line'],
                chk['b618_checks.txt'][0], chk['b618_checks.txt'][1], chk['b618_checks_postpush.txt'][0], chk['b618_checks_postpush.txt'][1],
                W['CJ']['line']))


N5_TEXT = ('\n%s the record tool’s N5 scorer takes the trail record’s expected line on OPEN_TRAILS as a parameter, from b619 on, so the '
           'write list is scored against the files the face names and not against the ledger’s state mid-act: the trail record is read at '
           'that line once it is written, and as pending while OPEN_TRAILS stops short of the line and no record stands; a test runs the '
           'scorer before and after the trail write and expects the same verdict. The defect it closes recurred at b598, b601, b603 and b618 '
           '(b618’s defect (c)); the repair is one edit of the act’s own record tool after its seal, committed alone in relay with its test.\n'
           % N5_HEAD)


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _scan_text(text, name):
    p = os.path.join(SP if DRY else D, 'b619_scanfile_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', p], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout, re.search(r'^\s*VERDICT\s*: CLEAN\s*$', r.stdout, re.M) is not None


def record_lines(*a):
    """### FINDINGS: b618's weight, addressed to b618's entry; OPEN_TRAILS: the N5 scorer's standing line, addressed to :12356; both
    ### appended at the end."""
    Q = R2._Q()
    entry = Q.line_of(Q.FIND, B618_ENTRY)
    if entry != 7386:
        sys.exit('### THE ADDRESSED LINE MOVED (%s) -- NOTHING WRITTEN' % entry)
    wt, st = _weight(entry), N5_TEXT
    for t, nm in ((wt, 'weight'), (st, 'standing')):
        bad = ledger_check(t)
        nd, _n = _nd(t)
        sc, clean = _scan_text(t, nm)
        print('  %s: grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (
            nm, bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
        if 'dry' in a:
            print(t)
        elif bad or any(nd.values()) or not clean:
            sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    if 'dry' in a:
        return
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    Q.guard_absent(Q.OT, N5_HEAD)
    r1 = Q.append_to(Q.FIND, wt)
    r2 = Q.append_to(Q.OT, st)
    out = [dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r1),
           dict(file='OPEN_TRAILS.md', head=N5_HEAD, line=Q.line_of(Q.OT, N5_HEAD), append=r2)]
    put_json('b619_record_lines.json', dict(entry=entry, lines=out))
    print('  FINDINGS.md :%s ; OPEN_TRAILS.md :%s' % (out[0]['line'], out[1]['line']))


# ================================================================================ COMPONENT 2: THE MAPPING
def _h53_bank(B, J):
    """### H53a-H53c scored on the mapping before any writing"""
    sf = K.syn_facts()
    byn = {r['key']: r for r in J}
    a = []
    for i, f in sf.items():
        row = byn[f['key']]
        want = '%s: ' % f['tier']
        cellv = [x for x in row['keystones'] if x.startswith(want)]
        needle = '%s (`%s` %s)' % (i, f['path'], f['version'])
        a.append(dict(id=i, row=row['n'], tier=f['tier'], path=f['path'], version=f['version'], vline=f['vline'],
                      ok=bool(cellv) and needle in cellv[0] and f['tier'] in ('K', 'KC', 'C')))
    kl = [r['n'] for r in J if not r['has_keystone']]
    rem = B['remotes']
    c = []
    for k, rt in sorted(rem.items()):
        lo = rt.get('local_only') or []
        ok = rt.get('ok') and (not rt.get('current') or (rt.get('local_peel') == rt.get('remote_peel')))
        c.append(dict(kernel=k, current=rt.get('current'), remote=(rt.get('remote_peel') or '')[:7], local_only=lo, ok=bool(ok)))
    unp = sorted(x['kernel'] for x in c if x['local_only'])
    return dict(H53a='HOLDS' if a and all(x['ok'] for x in a) and len(a) == 6 else 'REFUTED', a=a,
                H53b='HOLDS' if kl == ['R22'] else 'REFUTED', kl=kl,
                H53c='HOLDS' if c and all(x['ok'] for x in c) else 'REFUTED', c=c, unpushed=unp,
                unpushed_in_nine=all(k in K.TAG_REMOTES for k in unp), n_tags=sum(len(x['local_only']) for x in c))


def census(*a):
    """### data/b619_census.txt and data/b619_census.json: every census row read with its current cells, each cell that changes printed
    ### old -> new with its source, the kernels read by ls-remote once per repository -- banked BEFORE any edition is written; H53a-H53c
    ### scored on it."""
    B = K.build(read_remotes=True)
    J = B['J']
    old = K.v03_cells()
    H = _h53_bank(B, J)
    SRC = {'documents': 'REGISTRY.md at %s (its blob a939198`s), the population and placement rules' % PRE_PP,
           'keystones': 'each document`s own class line at its newest version (§0`s order), the syntheses` heads',
           'editions': 'the editions by the form beside each file at %s and the trails` lines naming them; the dated appends since f374bba' % PRE_PP,
           'sieve': 'THE_FINDINGS_AS_THEY_STAND_v0_5.md`s cluster headings at %s, through SPIRAL_MAP §4A`s members' % PRE_PP,
           'kernels': 'git ls-remote --tags, once per repository, read back against the clone`s peel; the clone`s tags the remote lacks',
           'deposit': 'the Day-1 record`s files at %s and the mirror roster at relay %s' % (PRE_PP, STEPZERO)}
    L = ['b619 -- COMPONENT 2: THE MAPPING, (R229)(3) -- every census row read with its current cells, banked %s, before any edition is '
         'written' % utc(),
         '### the pins: PLACE-papers %s (REGISTRY.md = a939198`s blob, the documents, SPIRAL_MAP.md, the sieve v0.5, OPEN_TRAILS.md); relay %s '
         '(the mirror roster); census v0.3 read at %s; the remotes read by `git ls-remote --tags` at this bank`s time' % (PRE_PP, STEPZERO, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if x.strip().startswith('###') and re.search(r'R-\d+', x)]
    L += ['', '### PART A -- THE REGISTRY ROWS, EACH READ AND PLACED (%d rows; %d title-layer references and %d row-update cell references apart, '
          'Part E):' % (len(B['rows']), len(B['refs']), len(B['refs_update']))]
    for r in B['rows']:
        L.append('  :%-4d %-8s %-62s -> %-4s %s' % (r['line'], r['id'] or '—', r['path'] or '(no file)', r['census'], r['why']))
        L.append('        tier %s -- %s ; edition %s %s ; deposit %s %s%s' % (
            r['tier'] or 'NONE', r['tier_src'], r['edition'][0], r['edition'][1], r['deposit'][0], r['deposit'][1],
            (' ; appended %s' % r['appended']) if r.get('appended') else ''))
    L += ['', '### PART B -- THE CENSUS ROWS, EACH CELL THAT CHANGES PRINTED v0.3 -> v0.4 WITH ITS SOURCE:']
    changes = []
    for row in J:
        o = old.get(row['n'], {})
        cc = []
        for col in K.COLS:
            new = row[col] if isinstance(row[col], str) else ' ; '.join(row[col])
            if new != o.get(col):
                cc.append(col)
                changes.append(dict(row=row['n'], col=col, old=o.get(col), new=new, source=SRC[col]))
        row['changed'] = cc
        L.append('  ### %s %s (REGISTRY :%s) -- %d rows ; keystone %s ; changed %s' % (row['n'], row['label'], row['heading'], len(row['rows']),
                                                                                    'yes' if row['has_keystone'] else 'none', cc or 'none'))
        for col in cc:
            x = [c for c in changes if c['row'] == row['n'] and c['col'] == col][0]
            L += ['      %-9s v0.3: %s' % (col, x['old']), '      %-9s v0.4: %s' % ('', x['new']), '      %-9s source: %s' % ('', x['source'])]
    L += ['', '### PART C -- THE KERNELS, READ BY ls-remote (one call per repository):']
    for k, rt in sorted(B['remotes'].items()):
        L.append('  %-36s %s ; via %s ; current %s ; remote peel %s ; clone peel %s ; read back %s ; unpushed by name %s%s' % (
            k, 'READ' if rt['ok'] else 'NOT READ (%s)' % rt['err'], rt['via'], rt.get('current'), (rt.get('remote_peel') or '—')[:12],
            (rt.get('local_peel') or '—')[:12], (rt.get('local_peel') == rt.get('remote_peel')) if rt.get('current') else 'no tag',
            rt.get('local_only') or 'none', '' if k not in K.TAG_REMOTES else ' ; one of W-ORD-TAG-REMOTES` nine (OPEN_TRAILS :12597)'))
    L += ['', '### PART D -- THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE AFTER v0.4: %s' % (
        ', '.join('%s %s' % (r['n'], r['label']) for r in J if not r['has_keystone']) or 'none')]
    L += ['### PART D2 -- THE SIX SYNTHESES, EACH READ AT ITS OWN HEAD:']
    for x in H['a']:
        L.append('  %s %-7s tier %-3s `%s` %s (its version line :%d) -- in the census cell: %s' % (x['row'], x['id'], x['tier'], x['path'], x['version'],
                                                                                              x['vline'], x['ok']))
    L += ['', '### PART E -- THE REFERENCE LAYERS, NOT COUNTED: the ratified titles %s ; the row update`s Version cells %s' % (
        ', '.join('%s (:%d)' % (r['id'], r['line']) for r in B['refs']), ', '.join('%s (:%d -> %s)' % (r['id'], r['line'], r['points']) for r in B['refs_update']))]
    L += ['', '### PART F -- WHAT THE READING FOUND, STATED AND NOT REPAIRED:',
          '  (F1) %d kernels carry %d tags their remotes do not: %s' % (len(H['unpushed']), H['n_tags'], '; '.join(
              '%s %s' % (x['kernel'], ', '.join('%s=%s' % t for t in x['local_only'])) for x in H['c'] if x['local_only'])),
          '  (F2) the navigator`s list "the monograph v5.17 ... SPIRAL_MAP v0.7" names two editions written at b609 and b610, before v0.3`s read; '
          'R01`s cell reads v5.17 at v0.3 already, and SPIRAL_MAP has no REGISTRY row (its v0.7 stands in v0.3`s Placement): no cell changes for them',
          '  (F3) of the eight living documents b618 fed, one is a REGISTRY row (m5-1 THE_METHOD_CANON, R23); the other seven stand outside the '
          'census`s population']
    nch = len(changes)
    L += ['', '### ### **CELLS CHANGED : %d, in %d rows** (%s)' % (nch, len(set(c['row'] for c in changes)), ', '.join(sorted(set(c['row'] for c in changes)))),
          '### ### **H53a %s** -- %d of 6 synthesis cells carry the path, version and tier the document`s own head gives' % (
              H['H53a'], sum(x['ok'] for x in H['a'])),
          '### ### **H53b %s** -- the rows with documents and no keystone after v0.4: %s' % (H['H53b'], H['kl']),
          '### ### **H53c %s** -- %d kernels read, each current tag read back at the clone; %d kernels carry %d tags unpushed, each named in its '
          'cell; all among W-ORD-TAG-REMOTES` nine: %s' % (H['H53c'], len(H['c']), len(H['unpushed']), H['n_tags'], H['unpushed_in_nine'])]
    put_txt('b619_census.txt', L)
    put_json('b619_census.json', dict(at=utc(), pre_pp=PRE_PP, rows=J, changes=changes, h53=H, remotes=B['remotes'],
                                      registry_rows=[dict((x, r[x]) for x in ('line', 'id', 'path', 'census', 'why', 'tier', 'tier_src', 'edition', 'deposit'))
                                                     for r in B['rows']], refs=B['refs'], refs_update=B['refs_update'], sieve_counts=B['sc']))
    for l in L[-4:]:
        print(l)


# ================================================================================ COMPONENT 3: THE EDITION AT v0.4
BM_TAG4 = '<!-- b619 (R229) THE v0.4 EDITION’S BACK MATTER, 2026-10-04 -->'
VERSION4 = ('*v0.4, 2026-10-04 -- the census read again at its rows: the six syntheses of b611-b616 named in their rows with path, version and '
            'tier; the edition-state, kernel-tag and sieve columns refreshed; the no-keystone section at the ANNEX alone; v0.3 stands beside it, '
            'unedited.*')
V3 = dict(version=10, h1=35, intro=37, header=39, rows=(41, 63), nk_intro=67, nk_rm=(69, 74), annex=75, count=77, tags=81, internal=82,
          p12=83, titles=84, close=86, bm=88)
REWRITES = [   # ### (v0.3 line, old span, new span, clause, the object named)
    (35, '*(read 2026-10-03, b610; relay `data/b610_census.txt`)*', '*(read 2026-10-04, b619; relay `data/b619_census.txt`)*', 'fact',
     'the read and its bank'),
    (37, 'the sieve rows the cluster holds at v0.4 through', 'the sieve rows the cluster holds at v0.5 through', 'fact', 'the sieve`s version read'),
    (37, 'the kernels anchoring it with their current tags read by ls-remote, and the deposit state',
     'the kernels anchoring it with their current tags read by ls-remote and the tags their clones carry unpushed named beside them, and the '
     'deposit state', 'ruled', 'the kernel-tag column, `(R229)`(3)'),
    (37, 'Each cell is read at PLACE-papers 7055f04 or at the remote', 'Each cell is read at PLACE-papers 9dbac4b or at the remote', 'fact',
     'the pin read'),
    (39, '| sieve rows at v0.4 |', '| sieve rows at v0.5 |', 'fact', 'the sieve`s version read'),
    (77, '7 of the census’s 23 rows hold documents and no keystone; the other 16 hold',
     '1 of the census’s 23 rows holds documents and no keystone; the other 22 hold', 'fact', 'the count read at v0.4'),
    (81, '9 kernels carry tags their remotes do not (relay `data/b610_census.txt`, Part C and (F1));',
     '{TAGS} (relay `data/b619_census.txt`, Part C and (F1)) -- W-ORD-TAG-REMOTES’ nine (OPEN_TRAILS :12597), each such tag named unpushed in '
     'its kernel’s cell in §1;', 'fact', 'the tags read by ls-remote'),
    (83, '1.5a-1 to 1.5a-4 sit in the 1.5A table and land in Phase 1.2 by the phase attribute (REGISTRY :780).',
     '1.5a-1 to 1.5a-4 sit in the 1.5A table and land in Phase 1.2 by the phase attribute (REGISTRY :780); 1.5a-9 and 1.5a-10, entered in '
     'the 1.5A row addition of 2026-10-04 (REGISTRY :1004-:1005), land there by their own provenance cells.', 'fact', 'the rows placed in Phase 1.2'),
    (84, 'its entries are references and are not counted.',
     'its entries are references and are not counted; the row update of 2026-10-04 (REGISTRY :978-:994), a layer of Version cells over '
     'seventeen rows, is read the same way.', 'fact', 'the population at a939198'),
]
ANNEX4 = ('- **R22 ANNEX: the download layer** (REGISTRY :360): `A_WOUND_UP_ENOUGH_CRANK_v0_5.md` -- REGISTRY files the download layer '
          'non-keystone and outside the repository tree (:360), and `(R221)`(2)(i) struck its synthesis act (OPEN_TRAILS :12595): no '
          'keystone is written from a file the tree does not hold, and this row stands as the ANNEX’s record.')
NK_LINE4 = ('*Six rows v0.3 listed here -- R02, R07, R12, R14, R16 and R17 -- now name in §1 the synthesis the form wrote for each (OPEN_TRAILS '
            ':12566), b611 to b616, with its path, version and tier; they leave this list, the removals recorded in the back matter.*')
LIVING4 = ('- **The living documents.** b618 fed eight living documents one dated append each in its own form (`(R228)`(2)): VERIFICATION_LOOM '
           '`5f74760`, INSTRUMENTS `7bc3f33`, THE_METHOD_CANON `a5d1944` (m5-1, its edition-state cell in R23), THE_METHOD_AS_IT_STANDS '
           '`1364177`, FACES_LEDGER `bff682d`, THE_LOAD_BEARING_MAP `f54aa9e`, GAUGE_AND_INVARIANT `81a3a74` and REGISTRY `a939198`; the '
           'other seven are no REGISTRY row and stand outside this census’s population.')


def _tags_phrase(H):
    return '%d kernels carry %d tags their remotes do not' % (len(H['unpushed']), H['n_tags'])


def _edition(CJ):
    cur = lines_of(_show(PP, PRE_PP, CEN3))
    J, H = CJ['rows'], CJ['h53']
    anchors = [(V3['version'], '*v0.3, 2026-10-03 -- the phase-state reading'), (V3['h1'], '## §1 — THE PHASES AND CLUSTERS'),
               (V3['header'], '| row | phase and cluster |'), (V3['rows'][0], '| R01 |'), (V3['rows'][1], '| R23 |'),
               (V3['nk_rm'][0], '- **R02 '), (V3['nk_rm'][1], '- **R17 '), (V3['annex'], '- **R22 ANNEX'), (V3['count'], '7 of the census’s 23 rows'),
               (V3['tags'], '- **Local tags the remotes do not carry.**'), (V3['p12'], '- **Phase 1.2.**'), (V3['titles'], '- **The title layer.**'),
               (V3['bm'], '<!-- b610 (R220) THE v0.3 EDITION')]
    for n, a in anchors:
        if not cur[n - 1].startswith(a):
            sys.exit('### v0.3`S ANCHOR :%d MOVED (%r) -- NOTHING WRITTEN' % (n, cur[n - 1][:60]))
    for n, old, _new, _c, _o in REWRITES:
        if cur[n - 1].count(old) != 1:
            sys.exit('### v0.3 :%d DOES NOT CARRY ITS OLD WORDING ONCE -- NOTHING WRITTEN (%r)' % (n, old[:60]))
    byn = {r['n']: r for r in J}
    out, where, kinds = [], {}, {}
    for i, l in enumerate(cur, 1):
        if i == V3['version']:
            out += [VERSION4, '']
        if V3['nk_rm'][0] <= i <= V3['nk_rm'][1]:
            where[i] = None
            kinds[i] = 'removed'
            continue
        nl = l
        if V3['rows'][0] <= i <= V3['rows'][1]:
            n = re.match(r'^\| (R\d\d) \| ', l).group(1)
            if byn[n]['changed']:
                nl = byn[n]['table_line']
                kinds[i] = 'row rewritten'
            else:
                if l != byn[n]['table_line']:
                    sys.exit('### %s UNCHANGED BY THE MAPPING BUT ITS LINE DIFFERS -- NOTHING WRITTEN' % n)
                kinds[i] = 'carried'
        elif i == V3['annex']:
            nl = ANNEX4
            kinds[i] = 'rewritten (ruled)'
        else:
            fx = [f for f in REWRITES if f[0] == i]
            for _n, old, new, _c, _o in fx:
                nl = nl.replace(old, new.replace('{TAGS}', _tags_phrase(H)))
            kinds[i] = 'rewritten' if fx else 'carried'
        out.append(nl)
        where[i] = len(out)
        if i == V3['annex']:
            out += ['', NK_LINE4]
        if i == V3['titles']:
            out.append(LIVING4)
    return cur, out, where, kinds


def _backmatter(CJ, cur, where):
    J, H = CJ['rows'], CJ['h53']
    ch = CJ['changes']
    bm = [BM_TAG4, '',
          '## Back matter of the v0.4 edition — written 2026-10-04 by b619 under the author’s ruling `(R229)`(3), by the form of `(R187)`(5), its '
          'clauses and the precedence order', '',
          '### The readings v0.4 adds, each the seat’s and strikeable', '',
          '- **R-1, widened.** A dated row update’s table of Version cells -- its second cell a `REGISTRY.md:n` pointer, b618’s of 2026-10-04 at '
          'REGISTRY :978-:994 -- is a layer of cells over the rows it points to, as the ratified-titles table is a layer of titles: printed in the '
          'bank, not counted.',
          '- **R-2, by its letter.** A dated row addition lands in the cluster its heading names: a heading naming Phase 2B to 2G places its rows '
          'there, as one naming Phase 1.5A to 1.5H always did; a row whose own provenance names Phase 1.2 as its cluster (1.5a-9, 1.5a-10) lands '
          'in Phase 1.2 beside 1.5a-1 to 1.5a-4, as `(R229)`(3) names Phase 1.2’s synthesis in its row.',
          '- **R-6, the unpushed mark.** A kernel’s cell names, beside the remote’s current tag, every tag its clone carries and its remote does '
          'not, by name and peeled commit, marked unpushed (W-ORD-TAG-REMOTES, OPEN_TRAILS :12597).',
          '- **R-9, a dated append.** A registry row’s file, held at v0.3’s commit, that gained a dated append in its own form since is named in its '
          'edition-state cell by the commit that appended it; an append is not an edition by the form.',
          '- **R-10, the syntheses.** The six syntheses’ rows name, in their keystones cell, the file read and its version as the document’s own '
          'version line gives it, at the tier its own class line gives; 2D is read at its v0.2.',
          '- **R-11, v0.3’s back matter.** v0.3’s back matter is carried whole beneath v0.3’s body as the dated record of that edition, and its own '
          '`:n` cite v0.3, which stands beside this edition unedited; they are not re-pinned. This back matter’s `:n` cite this edition.',
          '- **R-12, the navigator’s list.** The monograph’s v5.17 and SPIRAL_MAP’s v0.7 were written at b609 and b610, before v0.3’s read: R01’s '
          'cell carries v5.17 at v0.3 already, and SPIRAL_MAP has no REGISTRY row (v0.3’s Placement names its v0.7), so no cell changes for them.',
          '', '### The cells changed, by row and column (both wordings in relay `data/b619_census.txt`, Part B)', '',
          '| row | this edition’s line | v0.3 line | columns changed | source |', '|:--|:--|:--|:--|:--|']
    srcs = {'documents': 'REGISTRY @ a939198, R-1 and R-2', 'keystones': 'the class lines; R-10', 'editions': 'the editions and the trails; R-9',
            'sieve': 'the sieve v0.5’s headings', 'kernels': 'ls-remote, once per repository; R-6', 'deposit': 'the mirror roster at relay db0aaa5b'}
    for row in J:
        if row['changed']:
            v3 = V3['rows'][0] + int(row['n'][1:]) - 1
            bm.append('| %s | {E:%s} | :%d | %s | %s |' % (row['n'], row['n'], v3, ', '.join(row['changed']), '; '.join(srcs[c] for c in row['changed'])))
    bm += ['', '*%d cells changed in %d rows.*' % (len(ch), len(set(c['row'] for c in ch))), '',
           '### Rewrites under the clauses', '', '| line | v0.3 line | was | now | clause | the object named |', '|:--|:--|:--|:--|:--|:--|']
    for n, old, new, c, o in REWRITES:
        bm.append('| {E:L%d} | :%d | “%s” | “%s” | %s | %s |' % (n, n, old.replace('|', '¦'), new.replace('{TAGS}', _tags_phrase(H)).replace('|', '¦'), c,
                                                              o.replace('`', '’')))
    bm += ['| {E:L%d} | :%d | the ANNEX’s row, its documents | the same, with its reason | ruled, `(R229)`(3) | the ANNEX row standing with its '
           'reason |' % (V3['annex'], V3['annex']), '',
           '### Removals', '', '| v0.3 line | text | destination | sentences |', '|:--|:--|:--|:--|']
    for i in range(V3['nk_rm'][0], V3['nk_rm'][1] + 1):
        rn = re.match(r'^- \*\*(R\d\d) ', cur[i - 1]).group(1)
        bm.append('| :%d | §2’s entry for %s | its §1 row, which names its synthesis (`(R229)`(3)) | %d |' % (i, rn, len(_segs(cur[i - 1]))))
    bm += ['', '### Insertions ordered by the ruling', '', '| line | what | Status |', '|:--|:--|:--|',
           '| {E:ver} | the version line, above v0.3’s | inserted |',
           '| {E:nk} | §2’s line on the six rows that leave it | inserted |',
           '| {E:living} | §3’s line on the living documents’ appends, by commit | inserted |', '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.4 | `%s` | written at b619 |' % CEN4,
           '| v0.3 | `%s` | unedited |' % CEN3,
           '| the current version (v0.1 with its v0.2 section) | `phase2/method/THE_KEYSTONE_CENSUS.md` | unedited |',
           '| the mapping | relay `data/b619_census.txt` | banked before this edition |',
           '| the registry read | `REGISTRY.md` @ a939198 (read at PLACE-papers 9dbac4b) | read, unedited |',
           '| the sieve read | `%s` | read, unedited |' % K.SIEVE5]
    for f in SYN_FILES:
        bm.append('| a synthesis named in its row | `%s` | read, unedited |' % f)
    bm += ['', '### Correspondence', '', '| row | this edition’s line | phase and cluster | REGISTRY rows (lines) | keystone | Status |',
           '|:--|:--|:--|:--|:--|:--|']
    for row in J:
        bm.append('| %s | {E:%s} | %s | %s | %s | %s |' % (row['n'], row['n'], K.cell(row['label']), ', '.join(':%d' % x['line'] for x in row['rows']),
                                                       'yes' if row['has_keystone'] else 'none', 'read again' if row['changed'] else 'read, unchanged'))
    bm += ['', '### Version history', '',
           '- **v0.4, 2026-10-04 (b619, `(R229)`(3))**: the census read again at its rows -- %d cells changed in %d rows; the six syntheses named in '
           'their rows with path, version and tier; the edition-state, kernel-tag and sieve columns refreshed; the no-keystone section at the ANNEX '
           'alone. v0.3 stands beside it, unedited.' % (len(ch), len(set(c['row'] for c in ch))),
           '- **v0.3, 2026-10-03 (b610)**, **v0.2, 2026-09-28 (b553)** and **v0.1, 2026-08-12**: carried above.', '']
    return bm


def edition(*a):
    """### PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_4.md beside v0.3 (unedited), and data/b619_edition.json. `dry`: the scratchpad.
    ### The re-pin step is last: the {E:n} tokens resolved against the final file."""
    CJ = jl('b619_census.json')
    cur, out, where, kinds = _edition(CJ)
    bm = _backmatter(CJ, cur, where)
    lines = out + [''] + bm
    pos = {}
    for i, l in enumerate(lines, 1):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if m and i <= len(out):
            pos[m.group(1)] = i
    pos['ver'] = lines.index(VERSION4) + 1
    pos['nk'] = lines.index(NK_LINE4) + 1
    pos['living'] = lines.index(LIVING4) + 1
    for n in set([f[0] for f in REWRITES] + [V3['annex']]):
        pos['L%d' % n] = where[n]
    lines = [re.sub(r'\{E:(\w+)\}', lambda m: ':%d' % pos[m.group(1)], l) for l in lines]
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b619_census_dry.md') if DRY else os.path.join(PP, *CEN4.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### v0.4 EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    v3bm = where[V3['bm']]
    bm_at = lines.index(BM_TAG4) + 1
    removed = [cur[i - 1] for i in range(V3['nk_rm'][0], V3['nk_rm'][1] + 1)]
    seg_d = []
    for i, k in kinds.items():
        if k.startswith('rewritten') or k == 'row rewritten':
            seg_d.append(dict(line=i, at=where[i], d=len(_segs(lines[where[i] - 1])) - len(_segs(cur[i - 1])), kind=k))
    J2 = dict(at=utc(), path=CEN4, sha256=sha(b), bytes=len(b), lines=len(lines), body_end=v3bm - 1, v3bm=v3bm, bm=bm_at, pos=pos,
              where={str(k): v for k, v in where.items()}, kinds={str(k): v for k, v in kinds.items()}, version_lines=1, history_lines=0,
              removals=_count(removed), removed_lines=list(range(V3['nk_rm'][0], V3['nk_rm'][1] + 1)), ruled=_count([NK_LINE4, LIVING4]),
              seg_d=seg_d, n_body=_count(lines[:v3bm - 1]), n_cur_body=_count(cur[:V3['bm'] - 1]), n_backmatter=_count(lines[v3bm - 1:]),
              n_backmatter4=_count(lines[bm_at - 1:]), dry=DRY)
    print('  %s : %d lines, %d bytes, sha256 %s ; body %d sentences (v0.3 %d) ; removals %d ; ruled %d ; version 1 ; rewrites` segment change %s ; '
          'back matter %d (v0.4`s own %d)' % ('DRY ' + dest if DRY else CEN4, len(lines), len(b), J2['sha256'][:16], J2['n_body'], J2['n_cur_body'],
                                              J2['removals'], J2['ruled'], [x['d'] for x in seg_d if x['d']], J2['n_backmatter'], J2['n_backmatter4']))
    put_json('b619_edition.json', J2)


def _edpath():
    return os.path.join(SP, 'b619_census_dry.md') if DRY else os.path.join(PP, *CEN4.split('/'))


def _ed():
    return lines_of(open(_edpath(), encoding='utf-8').read().replace(chr(13), ''))


def termscan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _edpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b619_census_termscan.txt', t.rstrip(NL).split(NL))


def keystone_hits(text):
    """### the generator's own keystone pattern (chain_page) applied to a text: which page nodes it names, per page"""
    import chain_page as CP
    out = {}
    for k in ('zeta', 'chi'):
        names = [x['name'] for x in CP.read_nodes(os.path.join(D, NODES[k]))[0] if x['source'] == 'kernel']
        short = sorted(set(n.split('.')[-1] for n in names))
        plain = sorted(s for s in short if re.fullmatch(r'[a-z]+', s))
        rest = sorted(s for s in short if s not in plain)
        alts = [r'\b(' + '|'.join(re.escape(s) for s in rest) + r')\b'] if rest else []
        alts += [r'(`' + re.escape(s) + r'`|[A-Za-z0-9_]\.' + re.escape(s) + r'\b)' for s in plain]
        out[k] = sorted(set(m.group(0).strip('`').split('.')[-1] for m in re.finditer('|'.join(alts), text)))
    return out


def _carried(cur, ed, E):
    """### every non-blank v0.3 line found verbatim in v0.4 at its mapped line, or as its recorded rewrite, or recorded as removed"""
    ok, bad = 0, []
    for i, l in enumerate(cur, 1):
        if not l.strip():
            continue
        k = E['kinds'].get(str(i))
        w = E['where'].get(str(i))
        if k == 'removed':
            ok += i in E['removed_lines']
            if i not in E['removed_lines']:
                bad.append(i)
            continue
        if not w:
            bad.append(i)
            continue
        new = ed[w - 1]
        if k == 'carried':
            good = new == l
        elif k == 'row rewritten':
            good = new.startswith(l.split(' | ')[0] + ' | ') and new != l
        elif k == 'rewritten (ruled)':
            good = new == ANNEX4
        else:
            want = l
            for n, old, nw, _c, _o in REWRITES:
                if n == i:
                    want = want.replace(old, nw.replace('{TAGS}', _tags_phrase(jl('b619_census.json')['h53'])))
            good = new == want
        ok += good
        if not good:
            bad.append(i)
    return ok, bad


def bank(*a):
    """### data/b619_edition_CENSUS.txt (the diff bank, the offset head once) and data/b619_h28.json: H28a-H28c and H53d scored."""
    E = jl('b619_edition.json')
    ed = _ed()
    cur = lines_of(_show(PP, PRE_PP, CEN3))
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### v0.4 ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b619_census_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    live = re.search(r'live uses\s*: (\d+)', scan)
    body = ed[:E['body_end']]
    beyond = [(i + 1, m.group(0)) for i, l in enumerate(body) for m in CEILING.finditer(l)]
    beyond0 = [(i + 1, m.group(0)) for i, l in enumerate(cur[:V3['bm'] - 1]) for m in CEILING.finditer(l)]
    cok, cbad = _carried(cur, ed, E)
    segc = sum(abs(x['d']) for x in E['seg_d'])
    allowed = E['removals'] + E['ruled'] + E['history_lines'] + E['version_lines'] + segc
    dn = E['n_body'] - E['n_cur_body']
    h28a = 'HOLDS'
    h28b = 'HOLDS' if abs(dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and len(beyond) <= len(beyond0) else 'REFUTED'
    kh = keystone_hits(NL.join(ed))
    L = ['### OFFSET FROM v0.3 (R190)(3): v0.3 :1-:9 unmoved; +2 from :10 (the version line and its blank); §2`s six entries (v0.3 :69-:74) removed, '
         '-6 from :75; +2 after :75 (a blank and the line on the six rows); +1 after :84 (the living documents` line); v0.3`s back matter from its '
         ':88 at :%d; this edition`s back matter at :%d' % (E['v3bm'], E['bm']),
         'b619 -- COMPONENT 3: THE DIFF BANK OF THE_KEYSTONE_CENSUS v0.4 against v0.3 at %s; the final file sha256 %s (%d lines, %d bytes)' % (
             PRE_PP, E['sha256'], E['lines'], E['bytes']), '',
         '### THE COUNTS, SEPARATELY: the body v0.3 %d sentences, v0.4 %d (%+d); the removals %d; the ruled insertions %d; the version line 1; the '
         'rewrites` segment change %d; the history lines 0; the back matter %d (v0.3`s carried and v0.4`s own; v0.4`s own %d)' % (
             E['n_cur_body'], E['n_body'], dn, E['removals'], E['ruled'], segc, E['n_backmatter'], E['n_backmatter4']), '',
         '### EVERY v0.3 LINE, MAPPED (carried / rewritten / removed), BOTH WORDINGS FOR EACH LINE THAT MOVED IN MEANING:']
    for i, l in enumerate(cur, 1):
        k = E['kinds'].get(str(i), 'carried')
        w = E['where'].get(str(i))
        if k == 'carried':
            continue
        L.append('  v0.3 :%d -> %s %s' % (i, (':%d' % w) if w else '(removed)', k))
        L.append('      was: %s' % l[:2000])
        if w:
            L.append('      now: %s' % ed[w - 1][:2400])
    L.append('  ### carried verbatim: %d lines (every other line of v0.3, each at its mapped line)' % sum(1 for k in E['kinds'].values() if k == 'carried'))
    L += ['### THE INSERTIONS: the version line :%d ; §2`s line :%d ; §3`s living-documents line :%d' % (E['pos']['ver'], E['pos']['nk'], E['pos']['living']),
          '### CARRIED: %d of %d non-blank v0.3 lines found at their mapped line, verbatim or as their recorded rewrite, or recorded as removed '
          '(failing %s)' % (cok, sum(1 for l in cur if l.strip()), cbad or 'none'),
          '### THE SCANNER: %s, live %s ; the ceiling pattern in the body: %d hits (v0.3`s body %d)' % (
              'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(beyond), len(beyond0)),
          '### THE PAGE NODES THE EDITION NAMES (the generator`s keystone pattern): %s' % kh, '',
          '### ### **H28a %s** -- VACUOUS on its letter: the census has no work-list (b558 none), so no MOVED-IN-MEANING sentence; beside it, every '
          'changed cell names its source (the mapping`s Part B) and every rewrite its clause (the back matter)' % h28a,
          '### ### **H28b %s** -- the body %+d against at most %d (removals %d + ruled %d + version 1 + the rewrites` segment change %d)' % (
              h28b, dn, allowed, E['removals'], E['ruled'], segc),
          '### ### **H28c %s** -- the scanner %s, %s live stems by its count; the ceiling pattern in the body %d against v0.3`s %d' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', live.group(1) if live else '?', len(beyond), len(beyond0)),
          '### ### **H53d %s** -- H28a-H28c %s' % ('HOLDS' if (h28a, h28b, h28c) == ('HOLDS',) * 3 else 'REFUTED', [h28a, h28b, h28c]),
          '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' if not cbad else '### ### **HELD AT %s.**' % cbad]
    put_txt('b619_edition_CENSUS.txt', L)
    put_json('b619_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H53d='HOLDS' if (h28a, h28b, h28c) == ('HOLDS',) * 3 else 'REFUTED', body_dn=dn,
                                   allowed=allowed, clean=clean, live=int(live.group(1)) if live else None, beyond=len(beyond), beyond0=len(beyond0),
                                   carried_ok=cok, carried_bad=cbad, vacuous_a=True, keystone_hits=kh))
    for l in L[-6:]:
        print(l)


def repin(*a):
    E = jl('b619_edition.json')
    ed = _ed()
    pos = E['pos']
    L = ['b619 -- THE RE-PIN STEP (R190)(3), THE FORM`S LAST: THE_KEYSTONE_CENSUS v0.4`s own cited lines read against its final file (sha256 %s)' % E['sha256'][:16]]
    ok = n = 0
    for k, v in sorted(pos.items(), key=lambda kv: kv[1]):
        n += 1
        l = ed[v - 1] if 0 < v <= len(ed) else ''
        if re.fullmatch(r'R\d\d', k):
            good = l.startswith('| %s | ' % k)
        elif k == 'ver':
            good = l == VERSION4
        elif k == 'nk':
            good = l == NK_LINE4
        elif k == 'living':
            good = l == LIVING4
        elif k.startswith('L'):
            vn = int(k[1:])
            good = vn == V3['annex'] and l == ANNEX4 or any(f[0] == vn and f[2].replace('{TAGS}', '')[:30] in l.replace(
                _tags_phrase(jl('b619_census.json')['h53']), '') for f in REWRITES)
        else:
            good = bool(l.strip())
        ok += good
        L.append('  {E:%s} -> :%d %s %s' % (k, v, 'HOLDS' if good else '### FAILS', l[:120]))
    bm = NL.join(ed[E['bm'] - 1:])
    unres = re.findall(r'\{E:\w+\}', bm)
    L += ['### unresolved tokens in the back matter: %s' % (unres or 'none'),
          '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (ok, n)]
    put_txt('b619_repin.txt', L)
    print(L[-1])


# ================================================================================ H53, READ BACK FROM THE EDITION
def _v4_rows(text):
    out = {}
    for l in lines_of(text):
        m = re.match(r'^\| (R\d\d) \| ', l)
        if m and l.endswith(' |'):
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            if len(c) == 8 and m.group(1) not in out:
                out[m.group(1)] = dict(zip(('n', 'label', 'documents', 'keystones', 'editions', 'sieve', 'kernels', 'deposit'), c))
    return out


def _v4_section2(text):
    ls = lines_of(text)
    i = next((k for k, l in enumerate(ls) if l.startswith('## §2 — THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE')), None)
    if i is None:
        return []
    out = []
    for l in ls[i + 1:]:
        if l.startswith('## '):
            break
        m = re.match(r'^- \*\*(R\d\d) ', l)
        if m:
            out.append(m.group(1))
    return out


KER_ENTRY = re.compile(r'(SIDE-[a-z0-9-]+) (\S+) = ([0-9a-f]{7})(?: \(unpushed by name: ([^)]*)\))?')
KER_NOTAG = re.compile(r'(SIDE-[a-z0-9-]+): no tag(?: \(unpushed by name: ([^)]*)\))?')


def kernel_entries(text):
    """### every kernel entry of the edition's §1 cells: [(row, kernel, tag or None, sha or None, [(tag, sha) unpushed])]"""
    out = []
    for n, row in _v4_rows(text).items():
        for part in row['kernels'].split(' ; '):
            m = KER_ENTRY.match(part)
            if m:
                un = [tuple(x.split(' = ')) for x in m.group(4).split(', ')] if m.group(4) else []
                out.append((n, m.group(1), m.group(2), m.group(3), un))
                continue
            m = KER_NOTAG.match(part)
            if m:
                un = [tuple(x.split(' = ')) for x in m.group(2).split(', ')] if m.group(2) else []
                out.append((n, m.group(1), None, None, un))
    return out


def h53_readback(text, remotes, facts):
    rows = _v4_rows(text)
    a = []
    for i, f in facts.items():
        row = rows.get({r: k for r, k in (('P12', 'R02'), ('15E', 'R07'), ('2B', 'R12'), ('2D', 'R14'), ('2F', 'R16'), ('2G', 'R17'))}[f['key']], {})
        cellv = row.get('keystones', '')
        needle = '%s: %s (`%s` %s)' % (f['tier'], i, f['path'], f['version'])
        a.append(dict(id=i, needle=needle, ok=needle in cellv or ('%s (`%s` %s)' % (i, f['path'], f['version']) in cellv and
                                                                  re.search(r'(^|; )%s: [^;]*%s \(' % (f['tier'], re.escape(i)), cellv) is not None)))
    s2 = _v4_section2(text)
    ke = kernel_entries(text)
    c = []
    for n, k, tag, s, un in ke:
        rt = remotes.get(k) or {}
        okt = (tag is None and not rt.get('current')) or (tag == rt.get('current') and (rt.get('remote_peel') or '').startswith(s or 'x'))
        want_un = sorted(tuple(x) for x in (rt.get('local_only') or []))
        oku = sorted(un) == want_un and all(t not in (rt.get('tags') or {}) for t, _s in un)
        c.append(dict(row=n, kernel=k, tag=tag, sha=s, unpushed=un, ok=bool(okt and oku)))
    unp = sorted(set(x['kernel'] for x in c if x['unpushed']))
    return dict(a=a, s2=s2, c=c, unpushed=unp, H53a='HOLDS' if len(a) == 6 and all(x['ok'] for x in a) else 'REFUTED',
                H53b='HOLDS' if s2 == ['R22'] else 'REFUTED', H53c='HOLDS' if c and all(x['ok'] for x in c) else 'REFUTED')


def h53(*a):
    """### data/b619_h53.json: H53a-H53c read back from the edition on disk, against the syntheses' heads and the remotes read at the mapping"""
    text = NL.join(_ed())
    CJ = jl('b619_census.json')
    R = h53_readback(text, CJ['remotes'], K.syn_facts())
    put_json('b619_h53.json', dict(at=utc(), **R))
    print('  H53a %s (%d of 6) ; H53b %s (%s) ; H53c %s (%d of %d entries ; unpushed kernels %s)' % (
        R['H53a'], sum(x['ok'] for x in R['a']), R['H53b'], R['s2'], R['H53c'], sum(x['ok'] for x in R['c']), len(R['c']), R['unpushed']))


# ================================================================================ COMPONENT 5: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b619_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b619_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b619_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b619 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b619_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b619_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE SCORES AND THE RECORD
HKEYS = ('H53a', 'H53b', 'H53c', 'H53d')
NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5', 'S6')
SCORE_KEYS = HKEYS + NK + SK
EDITION_PREFIX = 'b619 (R229)(3): ' + CEN4
CURRENTS = ('README.md', 'ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS.md', CEN3, K.SIEVE5,
            'phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md', 'day1/A_Place_to_Stand_v5_17.md') + tuple(SYN_FILES)
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the edition names no page node (the keystone pattern on the dry edition): both pages unchanged


def _pp_commits():
    return [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in g(PP, 'log', '--reverse', '--format=%h %s', PRE_PP + '..HEAD').split(NL)
            if l.strip()]


def _files(h, repo=PP):
    return sorted(x for x in g(repo, 'show', '--name-only', '--pretty=format:', h).split(NL) if x.strip())


def R2_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def n5(*a):
    """### N5, scored by its letter: nothing deposits; no kernel touched; no current version edited; no file written beyond the edition file,
    ### the mapping bank, the diff bank, the scorer edit and its test, the re-emitted pages, the record lines and the trails."""
    Z, X = (jl('b619_page_%s.json' % k) if os.path.exists(_p('b619_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    face = jl('b619_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state(list(face)).items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    trail_pending = not os.path.exists(_p('b619_trail.json'))   # ### b618's form, carried: OPEN_TRAILS wanted once the trail record is banked
    want_pp = sorted([CEN4, 'FINDINGS.md'] + ([] if trail_pending else ['OPEN_TRAILS.md']) + [p['page'] for p in (Z, X) if p.get('changed')])
    created = sorted(x for x in g(PP, 'diff', '--name-only', '--diff-filter=ADR', PRE_PP, 'HEAD').split(NL) if x.strip())
    cur_ok = all((_show(PP, PRE_PP, p) or '') == (_show(PP, 'HEAD', p) or '') and (_show(PP, PRE_PP, p) or '') == R2.cr0(
        open(os.path.join(PP, *p.split('/')), 'rb').read()).decode('utf-8', 'replace') for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b619_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b618_closing_push_out.txt'))
    ok = kern_same and created in ([], [CEN4]) and cur_ok and pp_ch == want_pp and relay_beyond == []
    return ('HELD' if ok else 'REFUTED',
            'nothing deposits; kernels unmoved since the face %s; created %s (the edition alone allowed); current versions unedited %s; '
            'PLACE-papers %s (wanted %s%s); relay beyond the act`s banks, tools and the table %s' % (
                kern_same, created or 'none', cur_ok, pp_ch, want_pp, ', the trail record pending' if trail_pending else '', relay_beyond))


def scores(*a):
    CJ = jl('b619_census.json')
    E = jl('b619_edition.json') if os.path.exists(_p('b619_edition.json')) else {}
    H28 = jl('b619_h28.json') if os.path.exists(_p('b619_h28.json')) else {}
    H = jl('b619_h53.json') if os.path.exists(_p('b619_h53.json')) else {}
    Z, X = (jl('b619_page_%s.json' % k) if os.path.exists(_p('b619_page_%s.json' % k)) else {} for k in ('zeta', 'chi'))
    T5 = jl('b619_test_n5.json') if os.path.exists(_p('b619_test_n5.json')) else {}
    commits = _pp_commits()
    ed_c = [h for h, s in commits if CEN4 in _files(h)]
    ed_alone = len(ed_c) == 1 and _files(ed_c[0]) == [CEN4] and dict(commits)[ed_c[0]].startswith(EDITION_PREFIX)
    rc = [l.split(' ', 1) for l in g(RELAY, 'log', '--format=%h %s', PRE_RELAY + '..HEAD', '--', 'tools/b619_record.py').split(NL) if l.strip()]
    sc_edit = [h for h, s in rc if s.startswith('b619 (R229)(2): the N5 scorer')]
    sc_alone = len(sc_edit) == 1 and set(_files(sc_edit[0], RELAY)) <= {'tools/b619_record.py', 'tools/b619_test_n5.py', 'data/b619_test_n5.txt',
                                                                         'data/b619_test_n5.json'}
    ed_t = [int(g(PP, 'log', '-1', '--format=%ct', h).strip()) for h in ed_c]
    map_t = R2_epoch(CJ.get('at'))
    ed_at = R2_epoch(E.get('at', ''))
    cur3 = lines_of(_show(PP, PRE_PP, CEN3))
    v3_same = (_show(PP, PRE_PP, CEN3) or '') == (_show(PP, 'HEAD', CEN3) or '')
    arms2 = rd('b619_page_arms_c2.txt')
    unp = H.get('unpushed') or []
    n5v = n5()
    S = {
        'H53a': (H.get('H53a', 'REFUTED'), 'read back from v0.4 on disk: %s of 6 synthesis cells carry the path, version and tier their own head gives %s' % (
            sum(x['ok'] for x in H.get('a') or []), [x['needle'] for x in H.get('a') or [] if not x['ok']] or '')),
        'H53b': (H.get('H53b', 'REFUTED'), 'the no-keystone section after v0.4 names %s' % H.get('s2')),
        'H53c': (H.get('H53c', 'REFUTED'), '%s of %s kernel entries read back at their remotes or marked unpushed by name; unpushed kernels %s' % (
            sum(x['ok'] for x in H.get('c') or []), len(H.get('c') or []), unp)),
        'H53d': (H28.get('H53d', 'REFUTED'), 'H28a %s, H28b %s, H28c %s (relay data/b619_edition_CENSUS.txt)' % (H28.get('H28a'), H28.get('H28b'), H28.get('H28c'))),
        'N1': (('HELD' if H.get('H53a') == 'HOLDS' else 'REFUTED'), 'every synthesis cell reads back equal to its document`s head and tier line: %s of 6' % (
            sum(x['ok'] for x in H.get('a') or []))),
        'N2': (('HELD' if H.get('s2') == ['R22'] else 'REFUTED'), 'the no-keystone section names %s' % H.get('s2')),
        'N3': (('HELD' if len(unp) <= 9 and all(k in K.TAG_REMOTES for k in unp) else 'REFUTED'), '%d kernels read unpushed in their cells, each one of '
               'W-ORD-TAG-REMOTES` nine: %s ; %d kernel entries carry the mark across the rows' % (len(unp), all(k in K.TAG_REMOTES for k in unp),
                                                                                                    sum(1 for x in H.get('c') or [] if x['unpushed']))),
        'N4': (('HELD' if (H28.get('H28a'), H28.get('H28b'), H28.get('H28c')) == ('HOLDS',) * 3 and H28.get('carried_bad') == [] else 'REFUTED'),
               'H28a-H28c %s ; sentences held %s' % ([H28.get('H28a'), H28.get('H28b'), H28.get('H28c')], H28.get('carried_bad'))),
        'N5': n5v,
        'S1': (('HELD' if map_t and ed_at and map_t < ed_at and (not ed_t or map_t < min(ed_t)) else 'REFUTED'),
               'the mapping banked at %s, the edition written at %s and committed at %s' % (CJ.get('at'), E.get('at'), ed_t)),
        'S2': (('HELD' if v3_same and H28.get('carried_bad') == [] and H28.get('carried_ok') == sum(1 for l in cur3 if l.strip()) else 'REFUTED'),
               'v0.3 unedited at HEAD %s; %s of %d non-blank v0.3 lines mapped (carried, rewritten as recorded, or removed as recorded)' % (
                   v3_same, H28.get('carried_ok'), sum(1 for l in cur3 if l.strip()))),
        'S3': (('HELD' if ed_alone and sc_alone else 'REFUTED'), 'the edition committed alone in PLACE-papers %s %s; the scorer edit committed alone in relay %s %s' % (
            ed_alone, ed_c, sc_alone, sc_edit)),
        'S4': (('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] and Z.get('rc') == 0 and X.get('rc') == 0 else 'REFUTED'),
               'the ζ page changed %s, the χ page changed %s (expected %s)' % (Z.get('changed'), X.get('changed'), S4_EXPECT)),
        'S5': (('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED'),
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
        'S6': (('HELD' if T5.get('same') is True and T5.get('runs', 0) >= 2 else 'REFUTED'), 'the N5 test: %s' % (T5.get('summary') or 'not run')),
    }
    put_json('b619_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:300]))


def _title_entry():
    n = len(jl('b619_census.json')['changes'])
    return ('## THE_KEYSTONE_CENSUS at v0.4: the six syntheses in their rows with tiers, %d cells refreshed, the no-keystone section at the ANNEX '
            'alone; the N5 scorer’s standing repair' % n)


TRAIL_HEAD = ('### b619 — lane three, act forty-six under (R229): THE_KEYSTONE_CENSUS at v0.4 -- the six syntheses named in their rows with '
              'tiers, the edition, kernel-tag and sieve columns refreshed; the N5 scorer’s standing repair')


def _finding_text():
    S, rl = jl('b619_scores.json'), jl('b619_record_lines.json')
    CJ = jl('b619_census.json')
    ch = CJ['changes']
    t = _title_entry()
    ed = next((h for h, s in _pp_commits() if s.startswith(EDITION_PREFIX)), '?')
    sc = [l.split(' ', 1)[0] for l in g(RELAY, 'log', '--format=%h %s', PRE_RELAY + '..HEAD', '--', 'tools/b619_record.py').split(NL)
          if 'the N5 scorer' in l]
    H = CJ['h53']
    e = ['', t, '',
         '*Filed at b619 on the author’s ruling `(R229)`. Banks: relay `data/b619_reads.txt`, `data/b619_census.txt`, `data/b619_edition_CENSUS.txt`, '
         '`data/b619_h53.json`, `data/b619_repin.txt`, `data/b619_test_n5.txt`, `data/b619_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R229)`(3)). `%s` beside v0.3, unedited, committed alone (%s): v0.3’s lines carried, rewritten or removed, every one '
         'mapped; %d cells changed in %d rows, each printed old to new with its source in the mapping banked before the edition was written; the '
         'six syntheses named in their rows with path, version and tier -- Phase 1.2 at KC, 1.5E at KC, 2B, 2D (at its v0.2), 2F and 2G at C, '
         'each as its own class line reads; the 2C row gaining the four documents b618 entered in REGISTRY; the sieve column at v0.5 (the '
         'Simplicity / RH cascade at 70 rows); the kernel-tag column read by ls-remote once per repository, %d kernels carrying %d tags '
         'unpushed, each tag named in its kernel’s cell, the nine of W-ORD-TAG-REMOTES; the no-keystone section at the ANNEX alone, with its '
         'reason.' % (CEN4, ed, len(ch), len(set(c['row'] for c in ch)), len(H['unpushed']), H['n_tags']), '',
         '**The record lines.** b618’s weight at FINDINGS :%d, the three acceptances and the refuted prediction’s repair; the N5 scorer’s standing '
         'line at OPEN_TRAILS :%d, beneath the build clause (:12356). **The repair** (`(R229)`(2)), after the seal: the record tool’s N5 scorer '
         'takes the trail record’s expected line as a parameter, committed alone in relay (%s) with its test, which ran the scorer before and '
         'after a trail write and read the same verdict.' % (rl['lines'][0]['line'], rl['lines'][1]['line'], ', '.join(sc) or '?'), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the census v0.3 (b610, FINDINGS :7212) named seven rows without a keystone and the '
         'synthesis sequence wrote one for six of them (b611 to b616, :7240 to :7346); b618 entered them in REGISTRY (:7386), and this edition '
         'reads them back into the rows that wanted them, at the tiers the load-bearing clause left (:7322); the ANNEX stands as `(R221)`(2)(i) '
         'struck it (OPEN_TRAILS :12595); the unpushed tags are W-ORD-TAG-REMOTES’ (:12597), now named in their rows. It strengthens the '
         'programme’s offering of a census a reader can enter at any phase or cluster and find its keystone, its tier and its kernels read at '
         'their remotes.', '',
         '**Next.** Per `(R229)`(4): b620, W-ORD-SECOND-READER’s batch by its form (OPEN_TRAILS :12212). The author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; no current version edited; nothing here is a statement about RH, GRH or any zero beyond the compiled '
         'statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'entry')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b619_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = (
    '(1) R-1 widened: b618’s row update of Version cells (REGISTRY :978-:994) is read as a layer of cells over the rows it points to, not as rows; '
    '(2) R-2 by its letter: a Phase 2B-2G heading places its rows in that cluster, and 1.5a-9 and 1.5a-10, filed under the 1.5A row addition, land '
    'in Phase 1.2 by their own provenance, as the ruling names 1.2’s synthesis in its row; (3) the 2C row gains the four documents b618 entered '
    '(p2-39 to p2-42), the census among them at C by its own class line; (4) the navigator’s “monograph v5.17 ... SPIRAL_MAP v0.7” were v0.3’s '
    'state already, and of the eight living documents only THE_METHOD_CANON (m5-1) is a REGISTRY row; (5) v0.3’s back matter carried whole as '
    'its dated record, its own `:n` citing v0.3, not re-pinned')


def _trail_text():
    S, fj, rl = jl('b619_scores.json'), jl('b619_findings.json'), jl('b619_record_lines.json')
    rows_ = ['', TRAIL_HEAD, '',
             '**(R229) ratified.** (1) b618 at its weight. (2) The N5 scorer’s standing repair. (3) THE_KEYSTONE_CENSUS v0.4; H53a-H53d. (4) The act '
             'after: b620, W-ORD-SECOND-READER’s batch.', '',
             '**Entered:** FINDINGS.md:%d (b618’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS.md:%d (the N5 scorer’s standing '
             'line, beneath :12356); this record; the edition, committed alone in PLACE-papers; the scorer’s repair and its test, committed alone in '
             'relay; relay data/b619_census.txt, data/b619_edition_CENSUS.txt, data/b619_test_n5.txt.' % (
                 rl['lines'][0]['line'], fj['entry_line'], rl['lines'][1]['line']), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % FOR_AUTHOR, '',
             '**b620 priced** (`(R229)`(4)): W-ORD-SECOND-READER’s batch by its form (:12212) over the monograph’s three acts (v5.14-v5.16), the '
             'sieve’s editions (v0.2-v0.5) and the six syntheses, with the residue seed (relay data/b609_residue_seed.txt), the two addenda (relay '
             'data/b610_residue_addendum.txt, data/b614_second_reader_addendum.txt) and the enumeration needle as inputs; a fresh seat session from '
             'the ledgers alone as the reader, the agreement rate banked.', '',
             '**Defects** (relay data/b619_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R229)`(4), b620, W-ORD-SECOND-READER’s batch; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; row U1 unedited; `h2` where the deposit left it; the four lists '
             'stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    sc, clean = _scan_text(e, 'trail')
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s ; scanner %s' % (bad or 'NONE', nd, 'CLEAN' if clean else 'NOT CLEAN'))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()) or not clean:
        sys.exit('### A LINE WOULD GRADE A TABLE NAME, CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b619_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b619_trail.json')['line'])


def desk(*a):
    S = jl('b619_scores.json')
    L = ['=' * 104, 'b619 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H53a-H53d, (R229)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H53 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b619_defects.txt').rstrip(NL).split(NL)
    put_txt('b619_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b619_scores.json'), jl('b619_findings.json'), jl('b619_trail.json'), jl('b619_record_lines.json')
    Z, X = jl('b619_page_zeta.json'), jl('b619_page_chi.json')
    ed = next((h for h, s in _pp_commits() if s.startswith(EDITION_PREFIX)), '?')
    L = ['b619 -- THE COMPONENTS, BANKED UNDER (R229).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b618`s closing push-out relay %s ; push-b618* branches deleted by name '
         '(data/b619_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b619_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b618`s weight FINDINGS :%d ; the N5 scorer`s standing line OPEN_TRAILS :%d' % (rl['lines'][0]['line'], rl['lines'][1]['line']),
         '### COMPONENT 2 : the mapping data/b619_census.txt ; %d cells changed ; H53a-H53c on the bank %s' % (
             len(jl('b619_census.json')['changes']), [jl('b619_census.json')['h53'][k] for k in ('H53a', 'H53b', 'H53c')]),
         '### COMPONENT 3 : the edition %s, committed alone %s ; H28a %s, H28b %s, H28c %s ; H53a %s, H53b %s, H53c %s, H53d %s' % (
             CEN4, ed, jl('b619_h28.json')['H28a'], jl('b619_h28.json')['H28b'], jl('b619_h28.json')['H28c'], S['H53a'][0], S['H53b'][0], S['H53c'][0],
             S['H53d'][0]),
         '### COMPONENT 4 : the N5 scorer`s repair and its test (data/b619_test_n5.txt) ; S6 %s' % S['S6'][0],
         '### COMPONENT 5 : the ζ page changed %s, the χ page changed %s ; page arms data/b619_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b620 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b619_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b619_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
