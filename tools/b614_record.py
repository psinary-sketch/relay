# -*- coding: utf-8 -*-
"""b614_record.py -- THE ACT'S RECORD TOOL, UNDER (R224). ### ONE SUBCOMMAND PER BANK.

### ### b614: LANE THREE, ACT FORTY-ONE -- THE SYNTHESIS FOR CLUSTER 2D: ONE DOCUMENT FROM THE CLUSTER'S EIGHT PAPERS READ AT ADDRESS,
### EVERY CLAIM GRADED, THE ROUTES READ; THE 2B PAPERS' FINDINGS ENTERED; THE MIRROR REFRESHED AFTER THE ACT'S LAST PLACE-papers PUSH.
### Subcommands write only `data/b614_*` unless the docstring names another file; `dry` on the command line routes every b614 bank and the
### document to the seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are written by
### encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. TECHNE-Core's module documents are read locally for
### the no-disclosure needles and never printed. The mirror subcommands (`roster`, `build`, `see`, `mverify`, `mbank`) run after the act's
### last PLACE-papers push and write nothing to PLACE-papers. No platform call. No Lean call. The template is tools/b613_record.py.
"""
import difflib
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b614_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = 'cafd5bdf'
STEPZERO = 'ba67435e'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/e914e49e-352a-4a49-8f97-a4d19c0f47eb/scratchpad'
SESSION_ID = 'e914e49e-352a-4a49-8f97-a4d19c0f47eb'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS.md'
B613_DOC = 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
METHOD_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
BANK = 'b614_claims_2D.txt'
TAG = '2026-10-04'
ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % TAG
PREV_ZIP = 'D:/MY-DOwnloads/mirror-refresh-2026-10-01.zip'
STAGE = os.path.join(os.environ.get('TEMP', SP), 'mirror-build-%s' % TAG)
ROSTER = os.path.join(ROOT, 'tools', 'mirror_roster.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b614_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b614_') else '', name, len(b)))
    return b


def put_json(name, obj):
    put_txt(name, [json.dumps(obj, indent=1, ensure_ascii=False)])


def jl(name):
    return json.load(io.open(_p(name), encoding='utf-8'))


def rd(name):
    p = _p(name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def _segs(l):
    return R4._segs(l)


def _cell(s):
    return s.replace('|', '¦')


DEFECTS = [
    '(a) THE SEAT`S, BEFORE THE SEAL, IN WRITING THIS ACT`S OWN SPEC: the clause block of tools/b614_regspec.py (carried from b613`s by name '
    'substitution into a file confirmed absent first) was replaced by a guarded Python splice run through a bash heredoc -- the new block read '
    'from a scratchpad file written through the Write tool, the old block`s span asserted before the write -- where the standing line orders '
    'edits to an unsealed tool through the Edit tool alone. The splice wrote what was intended (the spec`s run prints its clauses); the '
    'remaining edits to the act`s tools went through the Edit tool.',
]
DEFECT_SHORT = ['(a) the seat’s: the regspec’s clause block spliced by a guarded Python script through a heredoc, not the Edit tool -- the '
                'content as intended, the rest through the Edit tool']


def defects(*a):
    L = ['b614 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b614_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the 2D row and the no-keystone section', PP, PRE_PP, CEN3, ('GREP', r'^\| R14 \||^## §2|^- \*\*R14 '), 900),
    ('REGISTRY.md: the 2D heading and rows p2-8, p2-9, p2-10, p2-15, p2-25, p2-30, p2-31, p2-26', PP, PRE_PP, 'REGISTRY.md',
     [265, 269, 270, 271, 272, 273, 274, 275, 276], 900),
] + [('%s whole (%s)' % (v[0].split('/')[-1], v[1]), PP, PRE_PP, v[0], 'ALL', 300) for v in K.PAPERS.values()] + [
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the five tests, RH-60, and the Matter / cosmology cluster`s one row', PP, PRE_PP, K.SIEVE, [24, 26, 28, 29, 30, 31, 32, 44, 122, 578, 582], 700),
    ('OPEN_TRAILS: the form, the precedence order, the sequence`s form, the form`s clauses, b613`s record lines and record, the second reader`s work-order',
     PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12212, 12228, 12566, 12601, 12645, 12647, 12649, 12651], 1500),
    ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md v0.1, the form`s latest instance: tier line, head line, version, body, back matter',
     PP, PRE_PP, B613_DOC, [1, 3, 5, 7, 24, 140, 160], 500),
    ('FINDINGS: b613`s entry', PP, PRE_PP, 'FINDINGS.md', [7278, 7280], 600),
    ('the 2B fact items` lines: COGNITION :155-:180', PP, PRE_PP, 'phase2/philosophy/COGNITION.md', list(range(155, 169)) + [172, 178, 179, 180], 300),
    ('the 2B fact items` lines: IDENTITY_SUBSPACE :53, :65, :129, :135, :171', PP, PRE_PP, 'phase2/method/IDENTITY_SUBSPACE.md', [53, 65, 129, 135, 171], 400),
    ('the 2B fact items` lines: INTERFACE_DARKNESS :25, :245, :249, :250, :327', PP, PRE_PP,
     'phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', [25, 245, 249, 250, 327], 400),
    ('SIDE-silence-principle v0.1.0: the silence predicate and the two instances` κ fields, (R224)(2)(v)', 'D:/SIDE-silence-principle', 'v0.1.0',
     'SIDESilencePrinciple/Basic.lean', [52, 60, 64, 131, 135, 139, 143, 146], 220),
    ('SIDE-kernel v1.0 and v1.7: silence_universal, (R224)(2)(iv)', 'D:/SIDE-kernel', 'v1.0', 'Kernel/SilenceTheorem.lean', [74], 220),
    ('SIDE-kernel v1.7', 'D:/SIDE-kernel', 'v1.7', 'Kernel/SilenceTheorem.lean', [74], 220),
    ('the mirror builder (never edited, (R96)): the roster source, the version column, the roster-change line', RELAY, PRE_RELAY,
     'tools/mirror_build.ps1', [20, 23, 59, 65, 101, 102, 113, 115, 120, 124], 220),
    ('relay data/b613_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b613_closing_push_out.txt', 'ALL', 260),
    ('relay data/b613_scores.json (whole)', RELAY, STEPZERO, 'data/b613_scores.json', 'ALL', 300),
] + [('%s at %s: %s' % (K.PINS[v[0]][0], K.PINS[v[0]][1], k), 'D:/' + K.PINS[v[0]][0], K.PINS[v[0]][1], v[1], [v[2]], 260) for k, v in K.KREADS.items()]


def reads(*a):
    L = ['b614 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel, width in READS:
        t = R4._show(repo, rev, path)
        at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        if t is None:
            L.append('### %s -- %s @ %s ### NO SUCH LINE (the blob does not exist)' % (label, path, at))
            continue
        sl = t.split(NL)
        if sl and sl[-1] == '':
            sl = sl[:-1]
        if sel == 'ALL':
            nums = [i + 1 for i, l in enumerate(sl) if l.strip()]
        elif isinstance(sel, tuple):
            nums = [i + 1 for i, l in enumerate(sl) if re.search(sel[1], l)]
        else:
            nums = [n for n in sel if not (0 < n <= len(sl)) or sl[n - 1].strip()]
        L.append('### %s -- %s @ %s (%d lines cited, of %d)' % (label, path, at, len(nums), len(sl)))
        for n in nums:
            line = sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE'
            L.append('    :%-6d %s' % (n, line[:width]))
    z = zipfile.ZipFile(PREV_ZIP)
    man = z.read('MANIFEST.md')
    L += ['', '### THE 2026-10-01 MIRROR, %s: MANIFEST md5 %s ; %d entries ; its head:' % (PREV_ZIP, hashlib.md5(man).hexdigest(), len(z.namelist()))]
    L += ['    ' + l for l in man.decode('utf-8-sig').replace(chr(13), '').split(NL)[:8]]
    L += ['### PLACE-papers since its source 192077f, the files added (the roster`s candidates):']
    L += ['    ' + l for l in g(PP, 'diff', '--name-status', '--diff-filter=A', '192077f', PRE_PP).split(NL) if l.strip()]
    L += ['', '### THE PINS THE PAPERS NAME WITH A TERMINAL, EACH AS CITED, RESOLVED IN ITS CLONE AND AT ITS REMOTE:']
    for k in K.PINS:
        st = K.pin_state(k)
        L.append('    %-9s %s %s -> %s ; at the remote: %s -- named at %s' % (k, st[1], st[2], st[3] or '### DOES NOT RESOLVE', st[4] or '### NONE', K.PINS[k][3]))
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('    %-24s named without a pin (%s); read for the record at %s %s = %s, %s :%d: %s' % (k, st[7], st[1], st[2], st[6], st[3], st[4],
                                                                                                    'stands' if st[5] else '### ABSENT'))
    L.append('### SIDE-silence-principle tags by ls-remote: %s' % ' ; '.join(l.strip() for l in g('D:/SIDE-silence-principle', 'ls-remote', '--tags', 'origin').split(NL) if l.strip()))
    nd = nd_sets()
    L += ['### THE NO-DISCLOSURE NEEDLE SETS, read locally at TECHNE-Core %s and never printed: the method document %s, %d sentences of 40 '
          'characters or more (b591`s form); the tree %s, %d (b595`s form); every module document, %d sentences of 60 characters or more '
          '(b611`s form)' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), METHOD_REL, len(nd['method']), TREE_REL, len(nd['tree']), len(nd['modules'])),
          '### TECHNE mentions in the eight papers: %s' % {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()},
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b614_reads.txt', L)


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
    L = ['### b614 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-04), banked verbatim with the options and the '
         'recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for k, q in enumerate(inp.get('questions', []), 1):
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        r = results.get(cid, (None, '### NO RESULT'))
        L += ['RESULT (transcript line %s): %s' % (r[0], r[1]), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act.')
    put_txt('b614_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo',
         'SIDE-trivium', 'SIDE-residual-bridge', 'SIDE-effects', 'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b614_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b614_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ THE NO-DISCLOSURE NEEDLE SETS (b613's, carried)
SECTION_RE = re.compile(r'^## \((i|ii|iii|iv|v|vi|vii|viii)\) ', re.M)


def _sections(text):
    ms = list(SECTION_RE.finditer(text))
    out = []
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        out.append((m.group(1), text[m.start():end]))
    return out


def _prose40(text):
    body = ''.join(s for k, s in _sections(text) if k != 'viii')
    out = []
    for para in re.split(r'\n\s*\n', body):
        if para.lstrip().startswith(('|', '#', '```')):
            continue
        flat = ' '.join(re.sub(r'[*_`]', '', para).split())
        for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(])', flat):
            if len(s) >= 40:
                out.append(s)
    return out


def _te_read(rel):
    try:
        return io.open(os.path.join(TE, *rel.split('/')), encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except OSError:
        return ''


def nd_sets():
    method = [' '.join(x.split()) for x in _prose40(_te_read(METHOD_REL))]
    tree = [' '.join(x.split()) for x in _prose40(_te_read(TREE_REL))]
    mods = set()
    for f in [x for x in g(TE, 'ls-files', 'modules').split(NL) if x.endswith('.md')]:
        for s in re.split(r'(?<=[.!?])\s+', _te_read(f)):
            s = ' '.join(s.split())
            if len(s) >= 60 and not s.startswith('|') and not s.startswith('#'):
                mods.add(s)
    return dict(method=method, tree=tree, modules=sorted(mods))


def nd_hits(text, sets=None):
    sets = sets or nd_sets()
    flat = ' '.join(text.split())
    return {k: sum(1 for s in v if s and s in flat) for k, v in sets.items()}, {k: len(v) for k, v in sets.items()}


# ================================================================================ COMPONENT 1: THE ARITHMETIC, THE RECORD LINES, THE ADDENDUM
def arith(*a):
    """### data/b614_arith.txt: COGNITION`s table re-read (R224)(2)(i)-(ii), and IDENTITY_SUBSPACE :129`s Frobenius bound -- each computed
    ### here, its range printed."""
    import statistics as st
    rows = [(2, .39), (2.5, .47), (4, .61), (4.5, .49), (4, .65), (4, .55), (4, .48), (5, .73), (1.5, .15), (4.5, .58), (4, .36)]
    r = st.correlation([x for x, _ in rows], [y for _, y in rows])
    n2 = (29, 104, 62, 12, 8, 1, 1)
    gs_ = sorted(((a_ * b_ - a_ - b_), a_, b_) for a_ in range(2, 60) for b_ in range(a_ + 1, 60) if __import__('math').gcd(a_, b_) == 1)
    other = [x for x in gs_ if (x[1], x[2]) != (2, 3)]
    sm = [n for n in range(0, 4) if n > 0 and all(p in (2, 3) for p in _pf(n))]
    L = ['b614 -- COMPONENT 1: THE ARITHMETIC OF (R224)(2), computed %s (Python %s)' % (utc(), sys.version.split()[0]), '',
         '### (i) COGNITION`S TABLE (phase2/philosophy/COGNITION.md :155-:168, :172): the twelve rows, the Feeling-of-Learning row excluded.',
         '    the coding: each Bloom range at its midpoint -- 1-3 -> 2, 1-4 -> 2.5, 3-5 -> 4, 3-6 -> 4.5, 4-6 -> 5, 1-2 -> 1.5, 4-5 -> 4.5',
         '    the rows: %s' % rows,
         '    rows after the exclusion: %d (:172 says n = 12) ; Pearson r over them: %.4f (:172 says 0.762; the coding the paper used is not stated)' % (len(rows), r),
         '    THE COMPUTATION OF RECORD: n = 11 after the exclusion; r ≈ %.3f at midpoint coding, against the stated 0.762.' % r,
         '', '### (ii) COGNITION :179: the n₂ rows` study counts %s (Freeman concept inventories, Kozanitis and Nenciovici, Hake, Knight, Steif and '
         'Dollár, Ruiz-Primo conceptual, Deslauriers actual) sum to %d ; :179 says 261 ; the n₁ rows` 158 + 225 + 1 = %d (:178 says 384)' % (
             list(n2), sum(n2), 158 + 225 + 1),
         '    THE SUM OF RECORD: 217 against the stated 261.',
         '', '### (iii) IDENTITY_SUBSPACE :129: the Frobenius number g(a, b) = ab − a − b over the coprime pairs 2 ≤ a < b < 60: g(2, 3) = %d ; the '
         'least over every other pair %d, at %s ; pairs other than {2, 3} with g ≤ 1: %d' % (
             2 * 3 - 5, other[0][0], other[0][1:], sum(1 for x in other if x[0] <= 1)),
         '    THE BOUND OF RECORD: every other coprime pair has g ≥ 3, so :129`s "g(a, b) ≥ 1" holds of every pair and does not single out {2, 3}; '
         'g ≥ 2 does (the bound SIDE-frobenius v0.1.0 compiles as g_two_three_minimal).',
         '', '### (iii) IDENTITY_SUBSPACE :171: the {2,3}-smooth integers from 0 to 3 are %s ; 0 is not {2,3}-smooth (it has no factorization into '
         'primes), so the listed set {0, 1, 2, 3} carries one element that is not smooth.' % sm]
    put_txt('b614_arith.txt', L)
    put_json('b614_arith.json', dict(at=utc(), cg_rows=len(rows), cg_r=r, cg_n2=sum(n2), cg_n1=158 + 225 + 1, frob_other_min=other[0][0],
                                     frob_le1=sum(1 for x in other if x[0] <= 1), smooth_0_3=sm))
    for l in L:
        print(l[:220])


def _pf(n):
    out, d = [], 2
    while d * d <= n:
        while n % d == 0:
            out.append(d)
            n //= d
        d += 1
    if n > 1:
        out.append(n)
    return out


B613_ENTRY = '## The 2B synthesis: the Silence Principle and interface darkness at v0.1'
B613_TRAIL = '### b613 — lane three, act forty under (R223): the synthesis for 2B'
SECOND_READER = '*Appended 2026-10-02 by b593 beside b592’s record (:12196), under the author’s ruling `(R203)`(3) -- W-ORD-SECOND-READER'
W_HEAD = ('*Appended 2026-10-04 by b614 to b613’s entry (:%d), under `(R224)`(1) -- b613 AT ITS WEIGHT; THE CITED PIN, THE POINTER, THE '
          'CORPUS-FACING TAG AND THE TWO ROUTE VERDICTS CONFIRMED:*')
F_HEAD = ('*Appended 2026-10-04 by b614 to b613’s record (:%d), under `(R224)`(2)(i)-(iv) -- THE 2B PAPERS’ FINDINGS, FACT ITEMS FOR THEIR NEXT '
          'EDITIONS, THE SYNTHESIS’S ROWS STANDING AS GRADED:*')
S_HEAD = ('*Appended 2026-10-04 by b614 to W-ORD-SECOND-READER (:%d), under `(R224)`(2)(v) -- A READING FOR THE RECORD: THE SILENCE-PRINCIPLE '
          'KERNEL’S INSTANCES SILENT BY DEFINITION; THE SECOND READER’S ADDENDUM EXTENDED:*')


def _b613():
    S = json.loads(R4._show(RELAY, STEPZERO, 'data/b613_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, trail, sr, dry=False):
    s = _b613()
    allh = lambda ks, w: w if all(s[k] == w for k in ks) else [s[k] for k in ks]   # noqa: E731
    A = json.load(io.open(os.path.join(SP if dry else D, 'b614_arith.json'), encoding='utf-8'))
    AD = json.load(io.open(os.path.join(SP if dry else D, 'b614_addendum.json'), encoding='utf-8'))
    t1 = ('\n%s THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md v0.1 (PLACE-papers 36d13a7), in the 2B papers’ folder: p2-2, p2-24, p2-14, p2-21, '
          'p2-22 and p2-28 read whole at a4f16fe and unedited; 83 claims -- 0 kernel-verified, 4 theorem-supported, 18 argument-supported, 9 '
          'computationally-verified, 19 synthesis-suggested, 33 statement-grade; tier C, the one cited kernel pin, SIDE-silence-principle v0.1, '
          'resolving neither in the clone nor at the remote (which holds v0.1.0 and v0.2.0), silence_universal named without a pin, the '
          'Correspondence in the back matter; two routes -- the enumeration claims of DARK_INTERFACE DARK by test 2 (RH-60), the identification '
          'paths of IDENTITY_SUBSPACE NOT A ROUTE by its own correction; DARK_INTERFACE :125 the one TECHNE citation, by pointer (the sha256 of '
          'TECHNE-Core’s file manifest); the no-disclosure check at 0 hits over 56 + 61 + 1,052 needles; neither page changed. The verdicts, as '
          'relay data/b613_scores.json prints them: H47a-H47d %s; N1 %s, N2-N5 %s; S1-S5 %s. The author confirms the cited pin read as written '
          '(tier C), the pointer form, the corpus-facing tag on E-2026-10-04-2 (the seat’s search governing), and the two route verdicts. FINDINGS '
          ':7278, :7280; OPEN_TRAILS :12645, :12647, :12649, :12651; ERRATA 35fedf7; PLACE-papers e7b444e; relay 5d54f24b, cafd5bdf. The suite 86 '
          'of 86 before and after the push; defect (a) the seat’s; two network failures kept as _attempt1 banks. Nothing deposited; no kernel '
          'touched; TECHNE-Core untouched.\n' % (
              W_HEAD % entry, allh(('H47a', 'H47b', 'H47c', 'H47d'), 'HOLDS'), s['N1'], allh(('N2', 'N3', 'N4', 'N5'), 'HELD'),
              allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD')))
    t2 = ('\n%s (i) phase2/philosophy/COGNITION.md :172 gives n = 12 after excluding one of its table’s twelve rows, leaving %d, and the '
          'coefficient r = 0.762 with its coding unstated; at midpoint coding of the Bloom ranges the %d rows give r ≈ %.3f (relay '
          'data/b614_arith.txt) -- a fact item, the coding to be stated or the coefficient corrected. (ii) COGNITION.md :179 gives the n₂ stage '
          '261 studies where the rows its table lists sum to %d -- a fact item. (iii) phase2/method/IDENTITY_SUBSPACE.md :129 bounds every other '
          'coprime pair by g(a, b) ≥ 1, which holds of every pair and does not single out {2, 3}; every other pair has g ≥ %d, so g ≥ 2 does '
          '(SIDE-frobenius v0.1.0’s g_two_three_minimal) -- a fact item; :171 lists 0 among the {2,3}-smooth integers, which 0 is not -- a fact '
          'item; :65 keeps its sentence of logically independent derivations beneath its own :53 correction that three share the involution -- '
          'a fact item. (iv) phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md :25, :245, :249 and :327 cite '
          'SIDE-silence-principle v0.1, which resolves nowhere: the pin is corrected to the tag the remote holds whose text the papers match '
          '(v0.1.0 or v0.2.0), read by the seat at the next act that touches those papers; and silence_universal, named at :250 and :329 without '
          'a pin, takes one -- it stands at SIDE-kernel Kernel/SilenceTheorem.lean :74 at every tag from v1.0 = 078b3c5 to v1.7 = 2957e7d. The '
          'synthesis’s rows stand as graded.\n' % (F_HEAD % trail, A['cg_rows'], A['cg_rows'], A['cg_r'], A['cg_n2'], A['frob_other_min']))
    t3 = ('\n%s at SIDE-silence-principle v0.1.0 (90e540fd, a remote tag) an interface is silent when its κ field is 0 (`isSilent`, '
          'SIDESilencePrinciple/Basic.lean :64), and each load-bearing instance sets that field to 0 in its own definition -- the product formula '
          '(:131-:135) and the distributive law (:139-:143) -- so the kernel’s instances carry silence by definition and not by derivation. Every '
          'sentence citing them as a verified silence takes the ceiling at the 1.5h and 2B editions. The second reader’s addendum is extended '
          'beside b610’s, which is not edited: relay data/b614_second_reader_addendum.txt, %d lines of three matchers over the current 1.5h and '
          '2B documents, read by hand -- %d kin, %d not kin.\n' % (S_HEAD % sr, AD['lines'], AD['kin'], AD['not_kin']))
    return [(W_HEAD % entry, t1), (F_HEAD % trail, t2), (S_HEAD % sr, t3)]


def ledger_check(*texts):
    import terminal_table as TT
    bad = []
    for t in texts:
        for ln in t.split(NL):
            if TT.GRADE_RE.search(ln) and TT._names_on(ln):
                bad.append((ln[:120], TT._names_on(ln)))
    return bad


def _addr():
    Q = R2._Q()
    return Q, Q.line_of(Q.FIND, B613_ENTRY), Q.line_of(Q.OT, B613_TRAIL), Q.line_of(Q.OT, SECOND_READER)


def record_lines(*a):
    """### FINDINGS: b613's weight, addressed to b613's entry; OPEN_TRAILS: the 2B fact items (addressed to b613's record) and the
    ### silence-principle reading (addressed to W-ORD-SECOND-READER) -- each appended at the end. Needs the arithmetic and the addendum."""
    Q, entry, trail, sr = _addr()
    if (entry, trail, sr) != (7280, 12651, 12212):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, trail, sr))
    dry = 'dry' in a
    for f in ('b614_arith.json', 'b614_addendum.json'):
        if not os.path.exists(os.path.join(SP if dry else D, f)):
            sys.exit('### %s IS NOT BANKED -- NOTHING WRITTEN' % f)
    parts = _texts(entry, trail, sr, dry)
    bad = ledger_check(*[t for _h, t in parts])
    nd, _n = nd_hits(NL.join(t for _h, t in parts))
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits in the lines: %s' % (bad or 'NONE', nd))
    if dry:
        for _h, t in parts:
            print(t)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    plan = [(Q.FIND, parts[0])] + [(Q.OT, p) for p in parts[1:]]
    for p, (h, _t) in plan:
        Q.guard_absent(p, h)
    out = []
    for p, (h, t) in plan:
        r = Q.append_to(p, t)
        out.append(dict(file=os.path.basename(p), head=h, line=Q.line_of(p, h), append=r))
    put_json('b614_record_lines.json', dict(entry=entry, trail=trail, second_reader=sr, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


# ### the second reader's addendum, (R224)(2)(v): three matchers over the current 1.5h and 2B documents, every hit read by hand
ADD_DOCS = ['phase1.5/method/SIDE_EXCLUSION.md', 'phase1.5/method/SIDE_DOOR.md', 'phase1.5/method/ENUMERA_v1_6.md', 'phase1.5/method/A_METHODOLOGY.md',
            'phase1.5/method/SIEVE_TO_SIDE.md', 'phase1.5/method/EXCLUSION_ENGINE.md', 'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md',
            'phase1.5/method/TECHNE_TOOLKIT_v8_3.md', 'phase2/philosophy/SILENCE_EMERGENCE.md', 'phase2/philosophy/DARK_INTERFACE.md',
            'phase2/philosophy/COGNITION.md', 'phase2/philosophy/UNIFIED_COGNITIVE.md', 'phase2/method/IDENTITY_SUBSPACE.md',
            'phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', B613_DOC]
ADD_M = [('A1', 'the line names the kernel (SIDE-silence-principle, its module, or silence_principle)',
          lambda l: re.search(r'SIDE-silence-principle|SIDESilencePrinciple|silence_principle\b', l)),
         ('A2', 'the line names the Silence Principle with kernel, verified, compiled, Lean, machine or formal',
          lambda l: re.search(r'Silence Principle', l, re.I) and re.search(r'kernel|verified|compiled|Lean|machine|formali', l, re.I)),
         ('A3', 'the line names the product formula or the distributive law with Lean, kernel, formally, compiled or verified',
          lambda l: re.search(r'product formula|distributive law', l, re.I) and re.search(r'Lean|kernel|formally|compiled|verified', l, re.I))]
KIN = {('A_METHODOLOGY.md', 37): 'the kernel “certifies” κ = 0 by the chain', ('A_METHODOLOGY.md', 78): '“kernel-verified in SIDE-silence-principle”',
       ('A_METHODOLOGY.md', 110): 'the kernel “verifies” the chain; the instances at κ = 0', ('A_METHODOLOGY.md', 423): 'the chain “makes this structural rather than empirical”',
       ('A_METHODOLOGY.md', 447): 'the kernel listed as carrying the chain', ('A_METHODOLOGY.md', 568): '“Kernel verification of the Silence Principle”',
       ('INVARIANCE_BARRIERS_v1_4.md', 433): 'the deposited principle taken as the verified leg', ('SILENCE_EMERGENCE.md', 25): 'the product formula’s instance as formally checked',
       ('SILENCE_EMERGENCE.md', 275): '“the mathematical instance” as formally checked', ('ENUMERA_v1_6.md', 186): 'the distributive law at rank 0, “Verified”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 17): '“theorem-supported (... kernel-verified)”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 25): '“kernel-verified in SIDE-silence-principle v0.1”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 245): '“kernel-verified in SIDE-silence-principle v0.1”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 249): 'the kernel as “the formal core”, instances at κ = 0',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 277): '“theorem-supported and kernel-verified”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 287): '“Clauses A–F (kernel-verified)”',
       ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 327): 'the kernel as “formal core”, instances at κ = 0'}
NOT_KIN = {('A_METHODOLOGY.md', 21): 'the federation in general; no silence instance', ('A_METHODOLOGY.md', 92): 'the principle’s empirical pattern, no kernel',
           ('A_METHODOLOGY.md', 535): 'the kernel named as compiling, no silence claimed', ('A_METHODOLOGY.md', 539): 'the methodology’s verification in general',
           ('INVARIANCE_BARRIERS_v1_4.md', 23): 'the RH reduction; no silence instance', ('INVARIANCE_BARRIERS_v1_4.md', 53): 'the principle cited to a paper',
           ('INVARIANCE_BARRIERS_v1_4.md', 71): 'the principle assumed, cited to a paper', ('INVARIANCE_BARRIERS_v1_4.md', 522): 'a dependency cited to a paper',
           ('DARK_INTERFACE.md', 10): 'natural language as a silent interface, no kernel', ('DARK_INTERFACE.md', 189): 'formalization in general',
           ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 329): 'SIDE-kernel’s silence_universal, outside the reading’s kernel',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 3): 'the tier line: the pin read as unresolved',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 26): 'a body sentence reporting ID’s citation at its grade',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 38): 'a body sentence on natural language',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 77): 'a Correspondence row at argument-supported, no pin',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 147): 'a Correspondence row at statement-grade',
           ('THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md', 171): 'the pin table: does not resolve'}


def addendum(*a):
    """### data/b614_second_reader_addendum.txt and its json: the second reader's addendum extended beside b610's (not edited)."""
    hits, yields = [], {}
    for d in ADD_DOCS:
        ls = K.lines_of(K.show(d))
        for i, l in enumerate(ls, 1):
            ms = [m[0] for m in ADD_M if m[2](l)]
            for m in ms:
                yields[m] = yields.get(m, 0) + 1
            if ms:
                key = (d.split('/')[-1], i)
                mark = 'KIN' if key in KIN else 'NOT KIN' if key in NOT_KIN else 'UNMARKED'
                hits.append((d, i, ms, mark, KIN.get(key) or NOT_KIN.get(key) or '', l))
    kin = sum(1 for h in hits if h[3] == 'KIN')
    nk = sum(1 for h in hits if h[3] == 'NOT KIN')
    un = sum(1 for h in hits if h[3] == 'UNMARKED')
    L = ['b614 -- THE SECOND READER`S ADDENDUM, EXTENDED, (R224)(2)(v): every 1.5h and 2B sentence citing the SIDE-silence-principle kernel`s '
         'instances as a verified silence, banked %s' % utc(),
         '### ADDRESSED to b610`s addendum, relay data/b610_residue_addendum.txt (OPEN_TRAILS :12212`s work-order); that bank is a prior bank and is '
         'not edited -- this addendum is banked beside it',
         '### THE READING IT ANSWERS TO, (R224)(2)(v): at SIDE-silence-principle v0.1.0 an interface is silent when its κ field is 0 (`isSilent`, '
         'SIDESilencePrinciple/Basic.lean :64), and each load-bearing instance sets the field to 0 in its own definition (:135, :143), so the '
         'instances carry silence by definition and not by derivation; a sentence citing them as a verified silence takes the ceiling at the 1.5h '
         'and 2B editions',
         '### THE DOCUMENTS READ, each at its current version at PLACE-papers %s: %s' % (PRE_PP, ', '.join(d.split('/')[-1] for d in ADD_DOCS)),
         '### THE MARKS: KIN -- the line cites the kernel, its chain or its instances as a verified, certified, formal or kernel-checked silence; '
         'NOT KIN -- the line names the principle or a kernel without that claim, or reports such a citation at its grade', '']
    for m, desc, _f in ADD_M:
        L.append('### MATCHER %s (%s): %d lines' % (m, desc, yields.get(m, 0)))
    L += ['### the union, read by hand: %d lines' % len(hits), '']
    for d, i, ms, mark, why, l in hits:
        L.append('  %s :%-4d %-8s %s -- %s' % (d, i, mark, '+'.join(ms), why))
        L.append('          “%s”' % ' '.join(l.split())[:400])
    L += ['', '### ### **THE ADDENDUM: %d lines read -- KIN %d ; NOT KIN %d ; unmarked %d.**' % (len(hits), kin, nk, un)]
    put_txt('b614_second_reader_addendum.txt', L)
    put_json('b614_addendum.json', dict(at=utc(), lines=len(hits), kin=kin, not_kin=nk, unmarked=un, yields=yields,
                                        hits=[dict(doc=d, line=i, matchers=ms, mark=mark) for d, i, ms, mark, _w, _l in hits]))
    print(L[-1])


# ================================================================================ COMPONENT 2: THE CLAIM BANK
def _route_rows():
    rs = {}
    for c in K.C:
        if c[8]:
            rs.setdefault(c[8][0], []).append(c)
    return rs


def route_score(sieve):
    rs = _route_rows()
    reached = [r for r, cs in rs.items() if cs[0][8][1] in ('DARK', 'BRIGHT', 'NOT A ROUTE')]
    matched, listed = [], []
    for r, cs in sorted(rs.items()):
        row = cs[0][8][5]
        mine = cs[0][8][1] + ('' if cs[0][8][2] is None else ', test %d' % cs[0][8][2])
        if row and row in sieve:
            v, t = sieve[row]
            theirs = v + ('' if t.strip() == '—' else ', test %s' % t.split()[0])
            matched.append((r, row, mine, theirs, mine == theirs))
        elif not row and cs[0][8][1] != 'NOT A ROUTE':
            listed.append((r, mine))
    return reached, matched, listed


def _kv():
    return [c for c in K.claims() if c[5] == 'kernel-verified']


def claims(*a):
    """### data/b614_claims_2D.txt and data/b614_claims.json: each paper's path, version and head; every claim with its line, grade and reason;
    ### the routes through the five tests; the pins and the kernel reads; the cluster's arithmetic; H48a's trace table -- banked before any
    ### writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    kr = K.resolve_kernel()
    sieve = K.sieve_rows()
    CC = K.claims()
    if not all(ok for ok, _l in rc.values()) or not all(ok for _k, ok, _l in kr):
        sys.exit('### A NEEDLE FAILS -- NOTHING WRITTEN')
    bad = [c[0] for c in K.C if not K.grade_ok(c)]
    if bad:
        sys.exit('### GRADES OUT OF RULE %s -- NOTHING WRITTEN' % bad)
    L = ['b614 -- COMPONENT 2: THE CLAIM BANK OF CLUSTER 2D, (R224)(4), banked %s before any writing' % utc(),
         '### the papers at PLACE-papers %s; the sieve v0.4 at %s' % (PRE_PP, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'A ROUTE is' in x or 'RESOLVES' in x] + ['']
    L += ['### PART A -- THE PAPERS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        reg = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        ver = next((l.strip() for l in ls[:20] if re.search(r'v\d+\.\d|April 2026|May 2026|March 2026|January 2026', l)), '')
        L.append('  %s = `%s` -- REGISTRY %s (:%d), its version %s, its status %s -- %d lines -- head :1 “%s” -- the paper`s own version/date line “%s” '
                 '-- last commit %s' % (k, path, rid, rline, reg[3], reg[5].replace('*', '')[:40], len(ls), ls[0][:120], ver[:120],
                                       g(PP, 'log', '-1', '--format=%h %ad', '--date=short', PRE_PP, '--', path).strip()))
    L += ['  lines in all: %d' % sum(len(v) for v in P.values())]
    L += ['', '### PART B -- THE CLAIMS, EACH WITH ITS LINE, NEEDLE, GRADE AND REASON (%d):' % len(CC)]
    for c in CC:
        cid, pk, n, needle, text, grade, support, reason, route = c
        L.append('  %-6s %s :%-4d %-25s support %-11s -- %s' % (cid, pk, n, grade, support, text))
        L.append('         needle “%s” on the line: %s ; reason: %s%s' % (needle[:90], rc[cid][0], reason,
                                                                     (' ; route %s %s%s' % (route[0], route[1], '' if route[2] is None else ' test %d' % route[2])) if route else ''))
    L += ['', '### PART C -- THE ROUTES, EACH THROUGH THE FIVE TESTS IN ORDER, WITH ITS VERDICT AND INSTRUMENT:']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        passed = ('tests 1-%d passed; ' % (t - 1)) if t and t > 1 else ''
        L.append('  %s -- claims %s -- %s%s -- %s, %s -- %s -- the sieve`s row %s' % (
            r, ', '.join(x[0] for x in cs), passed, 'fails test %d' % t if t else 'not asked (not a route)', v, inst, why,
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', ''))))) if row else 'none'))
    L += ['', '### PART D -- THE PINS THE PAPERS NAME WITH A TERMINAL, THE STATEMENTS READ THERE, AND THE NAMES CITED WITHOUT A PIN:']
    for k in K.PINS:
        st = K.pin_state(k)
        L.append('  %-9s %s %s -> commit %s ; at the remote: %s ; named at %s' % (k, st[1], st[2], st[3] or 'DOES NOT RESOLVE', st[4] or 'NONE', K.PINS[k][3]))
    for k, ok, l in kr:
        v = K.KREADS[k]
        L.append('  read %-11s %s :%d at %s -- needle on the line: %s -- %s' % (k, v[1], v[2], K.PINS[v[0]][1], ok, v[4]))
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('  %-24s named without a pin (%s); stands at %s %s = %s, %s :%d -- no row certifies from it' % (k, st[7], st[1], st[2], st[6], st[3], st[4]))
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '[]')
    TT = T.get('rows') if isinstance(T, dict) else T
    for nm in ('omega_b_equals_4_over_81', 'xi_total', 'formation_count', 'mechanism_class_card_derived', 'three_weight1_eq_14', 'mass_gap',
               'yang_mills_total_eight'):
        r = [x for x in TT if str(x.get('name', '')).split('.')[-1] == nm]
        L.append('  the terminal table on %s: %s' % (nm, ['%s %s %s %s' % (x.get('repo'), x.get('name'), x.get('pin'), x.get('grade')) for x in r] or 'no row'))
    zl = K.lines_of(io.open(os.path.join(D, NODES['zeta']), encoding='utf-8').read())
    xl = K.lines_of(io.open(os.path.join(D, NODES['chi']), encoding='utf-8').read())
    L += ['  the pages: ζ list %d lines, χ list %d lines; no node of either is a name the eight papers cite with a pin' % (len(zl), len(xl))]
    L += ['', '### PART E -- THE CLUSTER`S ARITHMETIC, RECOMPUTED (mpmath %s):' % __import__('mpmath').__version__]
    AR = K.arith2d()
    for lab, val, paper, ok in AR:
        L.append('  %s -- computed %s ; the paper %s ; %s' % (lab, val, paper, 'AGREES' if ok else '### DIFFERS'))
    trace = sorted(set((c[1], c[2]) for c in CC))
    L += ['', '### PART F -- H48a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    reached, matched, listed = route_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in CC)
    kvpins = sorted(set(K.PINS[c[7]][0] + ' ' + K.PINS[c[7]][1] for c in K.C if c[5] == 'kernel-verified') | {'SIDE-effects a27415d'})
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### THE CERTIFYING PINS: %d (%s), in %d kernels' % (len(kvpins), ', '.join(kvpins), len(set(x.split()[0] for x in kvpins))),
          '### H48d -- THE ROUTES: %d (%s); against the sieve: %s; with no row, listed for its next version: %s' % (
              len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                  for r, row, m, t, ok in matched) or 'none', listed or 'none')]
    put_txt(BANK, L)
    put_json('b614_claims.json', dict(at=utc(), n=len(CC), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, matched=matched, listed=listed,
                                      kvpins=kvpins, arith=[dict(label=x[0], value=x[1], paper=x[2], agrees=x[3]) for x in AR],
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in CC]))
    print(L[-3])
    print(L[-2])
    print(L[-1])


# ================================================================================ COMPONENT 3: THE DOCUMENT
TITLE = ('# The Baryon Fraction, the Dark Sector and the Constants: the Lithium Plateaux, the Størmer Wall, the Fano Split, Hodge Conservation and the '
         'Yang-Mills Exclusion Form')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional|[Uu]nique|[Ee]xact)\b')
HEADLINE = '*This document synthesises the eight papers it names and certifies nothing they do not.*'
VERSION = '*v0.1, 2026-10-04 -- written at b614 under `(R224)`(4), the synthesis for 2D that THE_KEYSTONE_CENSUS v0.3 names (its row R14).*'
BM_TAG = '<!-- b614 (R224) THE v0.1 BACK MATTER, 2026-10-04 -->'
BODY1 = '## 1. The papers and their status'

BODY = [
    (BODY1, [
        'PO states that the dimensionless constants of physics are arithmetic expressions in two and three (PO :11), and that whether their simplicity is forced or merely available is open (PO :83).',
        'ST lists the cosmos as a determined system over ℤ as an assumption, not derived (ST :143).',
        'CS re-graded its headline claims on 2026-07-19 without changing its mathematics (CS :8), and YM states on its face that the physical Yang-Mills mass gap is open (YM :15).',
        'UF states that the forces are unified arithmetically in the prime structure of their constants (UF :24), and REGISTRY files it DEFUNCT.']),
    ('## 2. The lithium plateaux', [
        'CS reports the BBN prediction A(⁷Li) = 2.69 dex against the Spite plateau’s 2.20 dex, a factor of 3.1 (CS :22), and assigns BBN the formation (2, 3, 2, 0) = 7 (CS :34).',
        'CS gives κ < 0.65 for the composite observational interface (CS :62), and states that a universal dark interface keeps a plateau flat while offsetting its value (CS :96).',
        'CS reads the second lithium plateau in early red giants as the controlled experiment (CS :121), cites stellar models reproducing both plateaux (CS :154), and states the problem substantially accounted for, a residual of 0.1-0.15 dex carried as a candidate for new physics (CS :184).',
        'CS classifies the problem TYPE II on observational registration (CS :146), and draws the lesson that universality is not brightness (CS :188).']),
    ('## 3. Density and placement', [
        'CS states that sieve methods give density results for the zeros on the critical line and not the placement of every zero, citing Selberg (1942) and Conrey (1989) (CS :72), whose theorems give a positive proportion and more than two fifths.',
        'CS grades as conjecture the reading that no sieve method can bridge density to placement (CS :72), states that the Euler product’s interface has κ = 0 for zero placement (CS :74), and scopes its sieve-ceiling theorem to the Sieve Ceiling Lemma, the kernel terminals W-6 shells (CS :174).']),
    ('## 4. The baryon fraction 4/81 and the Størmer wall', [
        'MA defines Ω = n₁^{n₃}/n₂^{n₁+n₃} for each formation class (MA :53), and states that the baryon density selects the Arithmetic class, Ω = 4/81, at 0.13σ against Planck 2018 while excluding the other classes at 18.6σ to 351σ (MA :14).',
        'MA grounds n₂ = 3, n₃ = 2 and n₄ = 0 in named theorems, Chevalley–Steinberg, Hadamard with Cartan’s Theorem B, and Schur’s lemma, the counts cited to programme results (MA :30, MA :32, MA :34), and states that the second component of classes B and D is stipulated (MA :28).',
        'ST reaches the same 4/81 through Størmer’s theorem, whose consecutive {2, 3}-smooth pairs end at (8, 9) (ST :22), the seven smooth numbers up to the wall (ST :23) and the identity wall² = n₂^(n₁+n₃) when n₁ = n₃ (ST :66).',
        'ST writes the dark sector as 77 = 7 × 11 (ST :78), and reports that dark = formation count × first unreachable prime holds for {2, 3} alone among prime pairs up to 13 (ST :93), which the claim bank recomputes.',
        'ST states that the remaining open step is the structural justification of total = n₂^(n₁+n₃) (ST :145), which it also argues from Independence and Silence (ST :175).',
        'At SIDE-omega-b 9c80279, omega_b_equals_4_over_81 states that the Ω of a tuple defined as (2, 3, 2, 0) is 4/81 (ST :257, MA :181), and at SIDE-cosmo c5cba30 the xi_* cluster counts 81 total and 4 visible slots for a tuple so defined (MA :183).',
        'At SIDE-kernel 5e668b4, formation_count sums n₁ to n₄, each defined as a numeral, to 7 (ST :223), and at SIDE-trivium 1aac3a9 the seven classes are counted through an injective image of seven integers (ST :228).',
        'MA reads Ω_b × 81/4 = 1 as cosmic flatness (MA :89), and states that ℚ has exactly three places by Ostrowski’s theorem (MA :99), where that theorem gives the archimedean place and one p-adic place for each prime.']),
    ('## 5. The dark sector and Λ', [
        'FA derives Ω_Λ = 14Ω_b = 56/81 = 0.6914, 0.82σ from Planck (FA :19), from three weight-1 elements of (ℤ/2)³ each contributing 14/3 Ω_b, the sum compiled as three_weight1_eq_14 at SIDE-residual-bridge v0.1 (FA :113).',
        'FA states that the partition (3, 3, 1) is a Hamming-weight grading and not a GL(3, 𝔽₂) orbit decomposition (FA :25), against MA’s reading of it as such a decomposition (MA :111); the claim bank finds the diagonal’s stabilizer of order 24 and transitive on the six other elements.',
        'FA assigns w = −1 to the weight-1 elements and w = 0 to the weight-2 elements (FA :95), an assignment it calls a structural choice (FA :244).',
        'MA and FA state that the split decomposition gives Ω_total = 244/243, a flatness deviation of Ω_b/12 ≈ 0.41% (MA :123, FA :131), which FA offers as a falsifiable prediction (FA :141).',
        'FA gives Ω_DM = 64/243 at 0.49σ (FA :155), and Ω_Λ = 169/243 at 1.38σ when the diagonal joins the dark-energy sector (FA :145).',
        'MA reads the 1/12 as echoing ζ(−1) = −1/12 (MA :127), a link FA states at magnitude alone (FA :248).']),
    ('## 6. The constants in two and three', [
        'PO gives the leading term 11α/12¹¹² = 1.087 × 10⁻¹²² for Λ (PO :67) and series coefficients built from two, three and eleven (PO :75), and states that its residual measures the closure of a six-coefficient fit, not agreement to fourteen places (PO :81).',
        'FA records a heritage formula carrying 12^{11/2} where PO carries 12¹¹² (FA :193), as UF does (UF :644); the claim bank computes 11α/12^{11/2} ≈ 9.3 × 10⁻⁸.',
        'PO states that 2^a + 3^b yields the primes from 5 to 41 and then 137 and 337 (PO :17); the claim bank finds 43, 59, 67, 73, 83, 89, 97, 113 and 131 of that form between 41 and 137.',
        'PO states that 23 and 53 lie outside the sum form (PO :19), that their Sophie Germain children 47 and 107 are prime (PO :27), and that {2, 3} alone among coprime pairs leaves only 1 unreachable (PO :29).',
        'PO gives the Weinberg angle as 3/13 + α/16 − α²/10 and the strong coupling as 2/17 + α/29 + α²/50 (PO :89), and names three Lean files for the arithmetic without a kernel or pin (PO :107).']),
    ('## 7. Hodge conservation', [
        'HC states that every structure present at codimension p ≥ 2 and absent at p = 1 acts on the kernel of the cycle class map and not its cokernel (HC :24), and concludes the Hodge Conjecture in five steps, the last the Mechanism Theorem (HC :104).',
        'HC states that the exhaustiveness of its five structures rests on evidence and search, not a classification theorem (HC :125), and defines the Griffiths group with an Abel-Jacobi quotient the standard definition does not carry (HC :48).']),
    ('## 8. The Yang-Mills exclusion form', [
        'YM states that what compiles is the exclusion form and the four-sector enumeration (YM :14), and that the physical Yang-Mills mass gap is open, per-sector positivity entering by definition (YM :15).',
        'At SIDE-effects c66f3c5, YangMills.mass_gap concludes ¬Massless from `gapped` defined True on each sector, retired at a27415d (YM :405), and at SIDE-yang-mills-formation 73e9e2c the count (3, 3, 2, 0) = 8 compiles over entries defined as numerals (YM :405).',
        'YM states that the four-sector classification is complete by Bott periodicity (YM :49), which computes the stable homotopy groups (YM :118), and classes the vortex sector by π₁ of the center Z(SU(N)) (YM :103).',
        'YM states code parameters [[8, 1, 5]] and [[8, 1, 3]] (YM :207), graded by its era annotation as subcode derivations (YM :442).',
        'YM’s reaches say the structural argument establishes the Yang-Mills mass gap (YM :341), beside its own note that the physical mass gap is open (YM :15).']),
    ('## 9. The routes the papers offer', [
        'HC states that for RH the E condition was closed by Conservation of Spectra (HC :16), credits that exhaustiveness to Tate’s thesis (HC :127), and names the Mechanism Theorem as the commitment it shares with the RH argument (HC :133).',
        'YM states that its architecture of a verified surround and a manuscript criterion is that of the RH argument, the manuscript’s Ostrowski the criterion (YM :323).']),
    ('## 10. The heritage paper', [
        'UF places four constants between the 46th and 47th ordinates of ζ’s zeros (UF :36), writes α⁻¹ and G as interpolations through ordinates of ζ’s zeros (UF :60, UF :157), and reads the interval as a unification hub (UF :88).',
        'UF reports 122 constants tested without failure (UF :719).']),
]
TRACE_RE = re.compile(r'\b(CS|MA|ST|HC|PO|FA|YM|UF) :(\d+)')


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    return ('KC' if cert else 'C'), len(cert)


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | paper | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(P[k][0].lstrip('# ').strip()), _cell(st[5]).replace('*', '')[:40]))
    kvp = jl('b614_claims.json')['kvpins']
    return [TITLE, '',
            '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-04 (b614), under `(R224)`(4): '
            'the tier the rows earn, decided after they were graded -- %d rows read kernel-verified at %d pins in %d kernels, each pin resolving in its '
            'clone and at its remote; the certifying statements are arithmetic over tuples their own files define, a placeholder form and a '
            'derived count, and they certify nothing about the physics; each other row is cited at its stated grade, the Correspondence after the '
            'front matter (`(R221)`(3)).*' % (tier, cert_rows, len(kvp), len(set(x.split()[0] for x in kvp))), '',
            HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for cluster 2D (THE_KEYSTONE_CENSUS v0.3, its row R14 and §2): the eight papers REGISTRY '
            'files as p2-8, p2-9, p2-10, p2-15, p2-25, p2-30, p2-31 and p2-26, each claim listed with the grade its own text supports; for a reader who '
            'meets those papers and needs what each states and what backs it.*', '',
            '**The papers, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** UNIFICATION_OF_FORCES (UF) sits in heritage/ and REGISTRY files it DEFUNCT; it is synthesised here because the '
            'census row lists it, each claim at its grade and none cited as current. The grades are `(R19)`’s vocabulary as `(R220)`(5) lists it; a '
            'row reads kernel-verified only where its paper names the terminal at a pin, and the statement there is quoted in the row; cite the '
            'synthesis for orientation and each row at its stated grade.', '']


def _corr(CC):
    S = ['## Correspondence', '',
         '*Every claim of the eight papers this document carries, with the grade the paper’s own text supports. A route is read through the sieve’s '
         'five tests in order; the routes and their instruments are in the back matter.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in CC:
        cid, pk, n, _needle, text, grade, _support, reason, route = c
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(reason), rcell))
    return S + ['']


def _back(CC, tier):
    sieve = K.sieve_rows()
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-04 by b614 under the author’s ruling `(R224)`(4), by the synthesis form of `(R220)`(5) and `(R221)`(3)', '',
         '### The grading rule, confirmed by `(R222)`(1)', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A pin resolves when its commit is in the clone and at the remote (`(R223)`(1)).',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.', '']
    if tier != 'KC':
        B += _corr(CC)
    B += ['### The routes through the five tests', '',
          '| route | claims | verdict | test, instrument at pin | reason | the sieve’s row |', '|:--|:--|:--|:--|:--|:--|']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        B.append('| %s | %s | %s | %s | %s | %s |' % (r, ', '.join(x[0] for x in cs), v, ('%d (%s)' % (t, inst)) if t else '—', _cell(why),
                                                   ('%s, %s' % (row, ' '.join(sieve.get(row, ('?', ''))).replace(' —', ''))) if row else 'none'))
    B += ['', '### The pins the papers name', '', '| as cited | its resolution | where the paper names it |', '|:--|:--|:--|']
    for k in K.PINS:
        st = K.pin_state(k)
        B.append('| %s %s | commit `%s`, %s | %s |' % (st[1], st[2], st[3], st[4] or 'NOT AT THE REMOTE', K.PINS[k][3]))
    B += ['', '| statement read | at | what it states |', '|:--|:--|:--|']
    for k, v in K.KREADS.items():
        B.append('| `%s` :%d | %s %s | %s |' % (v[1], v[2], K.PINS[v[0]][0], K.PINS[v[0]][1], _cell(v[4])))
    B += ['', '### Names cited without a pin', '', '| name | where the paper names it | where it stands |', '|:--|:--|:--|']
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        B.append('| %s | %s | %s %s = %s, `%s` :%d |' % (k, st[7], st[1], st[2], st[6], st[3], st[4]))
    B += ['', '### The arithmetic the rows cite, recomputed in the claim bank', '', '| what | computed | the paper | agrees |', '|:--|:--|:--|:--|']
    for x in jl('b614_claims.json')['arith']:
        B.append('| %s | %s | %s | %s |' % (_cell(x['label']), _cell(x['value'][:400]), _cell(x['paper']), 'yes' if x['agrees'] else 'no'))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b614 |' % DOC]
    for k, (path, rid, _rl) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R14 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/%s` | banked before this document |' % BANK, '',
          '### Version history', '',
          '- **v0.1, 2026-10-04 (b614, `(R224)`(4))**: the synthesis of p2-8, p2-9, p2-10, p2-15, p2-25, p2-30, p2-31 and p2-26, %d claims graded, the '
          'routes read through the five tests.' % len(CC), '']
    return B


def doc(*a):
    """### PLACE-papers phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS.md (created) and data/b614_doc.json; `dry`: the
    ### scratchpad. Needs the claim bank first."""
    if not os.path.exists(_p('b614_claims.json')):
        sys.exit('### THE CLAIM BANK IS NOT BANKED -- NOTHING WRITTEN')
    CC = K.claims()
    tier, ncert = _tier()
    front = _front(tier, ncert)
    body = []
    for h, ss in BODY:
        body += [h, ''] + [' '.join(ss), '']
    lines = (front + _corr(CC)) if tier == 'KC' else front
    body_at = len(lines) + 1
    lines = lines + body
    body_end = len(lines)
    lines = lines + _back(CC, tier)
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b614_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b614_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(CC)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b614_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b614_doc_termscan.txt', t.rstrip(NL).split(NL))


def h48a(ls, J):
    trace = set((p, n) for p, n in jl('b614_claims.json')['trace'])
    body = [l for l in ls[J['body_at'] - 1:J['body_end']] if l.strip() and not l.startswith('#')]
    sents = [s for l in body for s in _segs(l)]
    bad = []
    for s in sents:
        tr = [(m.group(1), int(m.group(2))) for m in TRACE_RE.finditer(s)]
        if not tr or any(x not in trace for x in tr):
            bad.append(s[:120])
    return not bad, len(sents), bad


def h48c_check(tier_line):
    """### C or KC, the line agreeing with the rows, and every certifying row's pin resolving with its statements standing"""
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    pins_ok = all(K.grade_ok(c) for c in kv)
    return ((not kv and 'TIER C**' in tier_line) or (bool(kv) and 'TIER KC**' in tier_line)) and pins_ok


def doc_bank(*a):
    """### data/b614_doc_bank.txt and data/b614_h48.json: the title's property words, H48a-H48c, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b614_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b614_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h48a(ls, J)
    rows = [l for l in ls if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h48b = 'HOLDS' if len(rows) >= 20 and not over and len(rows) == len(K.C) else 'REFUTED'
    hits, sizes = nd_hits(NL.join(ls))
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    h48c = 'HOLDS' if h48c_check(tier_line) else 'REFUTED'
    CJ = jl('b614_claims.json')
    h48d = 'HOLDS' if CJ['matched'] and all(x[4] for x in CJ['matched']) else 'REFUTED'
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    L = ['b614 -- COMPONENT 3: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified; the line: %s' % (J['tier'], J['cert_rows'], tier_line[:700]),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'in the back matter, after the body (C)' if placed and J['tier'] == 'C'
                                                                                          else 'after the front matter (KC)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s ; THE VERSION LINE: %s' % (HEADLINE in ls[:12], VERSION in ls[:12]),
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM over this document, the needles read locally and never printed: the method document %d needles, %d hits ; the '
         'tree %d, %d ; every module document %d, %d' % (sizes['method'], hits['method'], sizes['tree'], hits['tree'], sizes['modules'], hits['modules']),
         '### H48a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H48a %s** -- every body sentence traces by path and line to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H48b %s** -- the Correspondence carries %d rows (at least twenty), none graded above its paper`s named backing (%s)' % (h48b, len(rows), over or 'none'),
         '### ### **H48c %s** -- the tier line reads %s, %d rows certifying, every certifying pin resolving with its statements standing' % (h48c, J['tier'], J['cert_rows']),
         '### ### **H48d %s** -- every route claim`s verdict against the sieve`s row: %s' % (h48d, CJ['matched']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and not any(hits.values()) and placed else '### ### **HELD.**']
    put_txt('b614_doc_bank.txt', L)
    put_json('b614_h48.json', dict(H48a='HOLDS' if a_ok else 'REFUTED', H48b=h48b, H48c=h48c, H48d=h48d, sentences=n_sent, untraced=a_bad, rows=len(rows),
                                   over=over, clean=clean, ceiling=len(ceiling), title_props=title_props, nd_hits=hits, nd_sizes=sizes, placed=placed,
                                   tier=J['tier']))
    for l in L[-6:]:
        print(l)


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b614_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b614_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b614_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b614 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b614_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b614_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE MIRROR, AFTER THE LAST PLACE-papers PUSH
EDITIONS = ['SPIRAL_MAP_v0_7.md', 'day1/A_Place_to_Stand_v5_17.md', 'phase1.5/method/ENUMERA_v1_6.md', 'phase1.5/method/EXHAUSTIVENESS_LICENSE_v0_2.md',
            'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md', 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md',
            'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH_v1_2.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md',
            'phase1.5/rcurve/R_CURVE_CRITERION_v0_2_2.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md',
            'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md', 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md', 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY_v0_2_4.md',
            'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE_v0_2.md',
            'phase2/method/REPARAMETERIZATION_BARRIERS_v0_2.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md',
            'phase2/quantum/SILENCE_STAGES_DEALIGNMENT_v1_3.md']
SYNTHESES = ['phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
             B613_DOC, DOC]
ROSTER_HISTORY = (' ### b614: THE CURRENT EDITIONS SINCE 192077f AND THE FOUR SYNTHESES ADDED BY THE AUTHOR’S ANSWERS TO b614’s PROMPT (all 22 '
                  'documents’ current editions, the diff governing over (R224)(3)’s named ten; the build after the act’s last PLACE-papers push, so '
                  'the 2D synthesis is carried). APPENDED AT THE END SO NO EXISTING ROW CHANGES ITS SLOT.')


def _roster_new():
    return [p.replace('/', '\\') for p in EDITIONS + SYNTHESES]


def roster(*a):
    """### relay tools/mirror_roster.json: the 26 rows appended at the end, lastChanged 2026-10-04, one _history sentence -- committed alone.
    ### `dry` prints the diff and writes nothing."""
    raw = open(ROSTER, 'rb').read()
    doc_ = json.loads(raw.decode('utf-8-sig'))
    redump = json.dumps(doc_, indent=2, ensure_ascii=False)
    print('  the roster re-dumps byte-equal: %s' % (redump.encode('utf-8') == raw.rstrip(b'\n').rstrip(b'\r') or redump.encode('utf-8') + b'\n' == raw))
    new = _roster_new()
    have = set(doc_['files'])
    if any(x in have for x in new):
        sys.exit('### A ROW IS ALREADY IN THE ROSTER -- NOTHING WRITTEN')
    for p in EDITIONS + SYNTHESES:
        if not os.path.exists(os.path.join(PP, *p.split('/'))):
            sys.exit('### %s IS NOT ON DISK -- NOTHING WRITTEN' % p)
    leaves = [x.split('\\')[-1] for x in doc_['files'] + new]
    dup = sorted(set(x for x in leaves if leaves.count(x) > 1) - {'README.md'})
    print('  rows %d -> %d ; leaf collisions beyond the known README pair: %s' % (len(doc_['files']), len(doc_['files']) + len(new), dup or 'none'))
    if dup:
        sys.exit('### A LEAF WOULD COLLIDE -- NOTHING WRITTEN')
    doc_['_history'] = doc_['_history'] + ROSTER_HISTORY
    doc_['lastChanged'] = TAG
    doc_['files'] = doc_['files'] + new
    out = json.dumps(doc_, indent=2, ensure_ascii=False) + ('\n' if raw.endswith(b'\n') else '')
    if 'dry' in a:
        for x in new:
            print('    + ' + x)
        return
    open(ROSTER + '.tmp', 'wb').write(out.encode('utf-8'))
    os.replace(ROSTER + '.tmp', ROSTER)
    put_json('b614_roster.json', dict(at=utc(), added=new, rows=len(doc_['files']), sha256=sha(out.encode('utf-8'))))


def build(*a):
    """### the builder, carried unedited (R96), run with -DateTag 2026-10-04 after the last PLACE-papers push; it writes the zip in
    ### D:/MY-DOwnloads, its stage folder in %TEMP%, and relay tools/mirror_prevbuild.json (its state). Refuses if the zip or stage exists."""
    if os.path.exists(ZIP) or os.path.exists(STAGE):
        sys.exit('### THE ZIP OR ITS STAGE EXISTS -- NOT STARTED (the builder deletes a same-named one)')
    loc, rem = g(PP, 'rev-parse', 'HEAD').strip(), (g(PP, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    if loc != rem:
        sys.exit('### PLACE-papers HEAD %s IS NOT THE REMOTE MAIN %s -- NOT STARTED' % (loc[:12], rem[:12]))
    t0 = time.time()
    r = subprocess.run(['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', os.path.join(ROOT, 'tools', 'mirror_build.ps1'), '-DateTag', TAG],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    put_json('b614_mirror_build.json', dict(at=utc(), rc=r.returncode, out=r.stdout, err=r.stderr, seconds=int(time.time() - t0), pp_head=loc))
    print(r.stdout[-2000:], r.stderr[-1000:], 'exit', r.returncode)


def _base_of(leaf, leaves):
    m = re.match(r'^(.+?)_v\d+(?:_\d+)*\.md$', leaf)
    return (m.group(1) + '.md') if m and (m.group(1) + '.md') in leaves else None


def see(*a):
    """### the author's addition: each base row whose numbered current edition is in the roster carries that edition's version in its version
    ### column with "(see <edition file>)" -- written into the staged MANIFEST and the zip's one entry updated in place. No file removed."""
    man_p = os.path.join(STAGE, 'MANIFEST.md')
    raw = open(man_p, 'rb').read()
    if b'(see ' in raw:
        sys.exit('### THE SEE NOTES ARE ALREADY IN THE STAGED MANIFEST -- REFUSING TO WRITE THEM TWICE')
    bom = raw.startswith(b'\xef\xbb\xbf')
    text = raw.decode('utf-8-sig')
    body, tail = (text[:-2], '\r\n') if text.endswith('\r\n') else (text, '')
    lines = body.split(NL)
    rows = {}
    for i, l in enumerate(lines):
        m = re.match(r'^\| ([^|]+?) \| (\d+) \| `([0-9a-f]{32})` \| ([^|]*?) \| ([^|]*?) \|$', l)
        if m:
            rows[m.group(1)] = (i, m.group(4))
    pairs = []
    for leaf in rows:
        b = _base_of(leaf, rows)
        if b:
            pairs.append((b, leaf))
    pairs.sort()
    bases = [b for b, _e in pairs]
    if len(bases) != len(set(bases)):
        sys.exit('### A BASE HAS TWO EDITIONS IN THE ROSTER -- REFUSING')
    for b, e in pairs:
        i, ver = rows[b]
        ever = rows[e][1]
        old = lines[i]
        lines[i] = old.replace(' | %s | ' % ver, ' | %s (see %s) | ' % (ever, e), 1)
        assert lines[i] != old and lines[i].count(' | ') == old.count(' | ')
    out = NL.join(lines) + tail
    before = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    open(man_p, 'wb').write((b'\xef\xbb\xbf' if bom else b'') + out.encode('utf-8'))
    ps = subprocess.run(['powershell', '-NoProfile', '-Command', "Compress-Archive -Path '%s' -DestinationPath '%s' -Update" % (man_p, ZIP)],
                        capture_output=True, text=True)
    after = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    put_json('b614_mirror_see.json', dict(at=utc(), pairs=pairs, bom=bom, crlf_tail=bool(tail), zip_sha_before=before, zip_sha_after=after,
                                          update_rc=ps.returncode, update_err=ps.stderr.strip()))
    print('  see notes : %d base rows ; update rc %d ; zip sha256 %s -> %s' % (len(pairs), ps.returncode, before[:16], after[:16]))
    for b, e in pairs:
        print('    %s -> %s' % (b, e))


def mverify(*a):
    """### relay tools/mirror_verify.py on the zip, all three clauses, run from PLACE-papers (clause 2's ls-remote is cwd-dependent)"""
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'mirror_verify.py'), ZIP, 'origin', 'main'], cwd=PP,
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt('b614_mirror_verify.txt', (r.stdout + r.stderr + '### exit %d' % r.returncode).replace(chr(13), '').split(NL))
    print(r.stdout[-1500:])


def mbank(*a):
    """### data/b614_mirror.txt and its json: the zip's sha256, the MANIFEST's md5, its roster-change line, its rows, the see notes, the verdict"""
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    text = man.decode('utf-8-sig').replace(chr(13), '')
    ls = text.split(NL)
    rows = [l for l in ls if re.match(r'^\| [^|:]', l) and not l.startswith('| flat file')]
    rline = [l for l in ls if l.startswith('ROSTER')]
    added = next((l for l in ls if l.strip().startswith('ADDED:')), '')
    removed = next((l for l in ls if l.strip().startswith('REMOVED:')), '')
    see_rows = [l for l in rows if '(see ' in l]
    ver = rd('b614_mirror_verify.txt')
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in ver
    zsha = hashlib.sha256(open(ZIP, 'rb').read()).hexdigest()
    head = next((l for l in ls if l.startswith('Source: PLACE-papers @')), '')
    adds = [x.strip() for x in added.split(':', 1)[1].split(',')] if added else []
    synth = [x for x in adds if x in [s.split('/')[-1] for s in SYNTHESES]]
    L = ['b614 -- THE MIRROR, BUILT AFTER THE ACT`S LAST PLACE-papers PUSH (the author`s answer to b614`s prompt), banked %s' % utc(),
         '### THE ZIP : %s ; %d bytes ; sha256 %s' % (ZIP, os.path.getsize(ZIP), zsha),
         '### THE MANIFEST : md5 %s ; %d bytes ; %d rows ; entries in the zip %d (files %d + MANIFEST)' % (hashlib.md5(man).hexdigest(), len(man), len(rows),
                                                                                                     len(names), len([n for n in names if n != 'MANIFEST.md'])),
         '### THE SOURCE LINE : %s' % head,
         '### THE ROSTER-CHANGE LINE : %s' % (rline[0] if rline else '### NONE'),
         '###   %s' % added.strip(), '###   %s' % (removed.strip() or 'REMOVED: none'),
         '### the files the line names as added: %d ; the syntheses among them: %d (%s)' % (len(adds), len(synth), ', '.join(synth)),
         '### THE SEE NOTES (the author`s addition): %d base rows carry their current edition`s version:' % len(see_rows)]
    L += ['    ' + r for r in see_rows]
    L += ['### THE VERIFICATION (relay data/b614_mirror_verify.txt): %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
          '### THE PREVIOUS BUILD : %s, MANIFEST md5 %s' % (PREV_ZIP, hashlib.md5(zipfile.ZipFile(PREV_ZIP).read('MANIFEST.md')).hexdigest()),
          '### THE MANIFEST, WHOLE:'] + ['    ' + l for l in ls]
    put_txt('b614_mirror.txt', L)
    put_json('b614_mirror.json', dict(at=utc(), zip=ZIP, zip_sha256=zsha, manifest_md5=hashlib.md5(man).hexdigest(), rows=len(rows), entries=len(names),
                                      source=head, roster_line=rline[0] if rline else '', added=adds, removed=removed.strip(), syntheses_added=synth,
                                      see_rows=len(see_rows), clean=clean))
    for l in L[:12]:
        print(l[:300])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H48a', 'H48b', 'H48c', 'H48d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + (CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md', B613_DOC,
                                                     'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', K.SIEVE, 'phase2/philosophy/COGNITION.md',
                                                     'phase2/method/IDENTITY_SUBSPACE.md',
                                                     'phase2/philosophy/INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md', 'ERRATA.md')
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the seat's expectation, registered on the face


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _n1():
    if not os.path.exists(_p('b614_mirror.json')):
        return ('NOT SCORABLE', 'the build sits after the act’s last PLACE-papers push (the author’s answer), so the MANIFEST does not exist when the '
                                'record is written; scored in relay after the build')
    M = jl('b614_mirror.json')
    floor = len(M['added']) >= 12
    two = len(M['syntheses_added'])
    return ('HELD' if floor and two == 2 else 'REFUTED',
            'the roster-change line names %d added files (the floor twelve: %s) and %d syntheses (%s) -- three written since 192077f before this act '
            'and this act`s own; the navigator`s count is two, so the expectation holds on its floor and fails in letter on its count' % (
                len(M['added']), floor, two, ', '.join(M['syntheses_added'])))


def scores(*a):
    H, CJ, J = jl('b614_h48.json'), jl('b614_claims.json'), jl('b614_doc.json')
    Z, X = jl('b614_page_zeta.json'), jl('b614_page_chi.json')
    face = jl('b614_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    mirror_files = ('tools/mirror_roster.json', 'tools/mirror_prevbuild.json')
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b614_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b613_closing_push_out.txt' and x not in mirror_files))
    rc = K.resolve_claims()
    kr = K.resolve_kernel()
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    pins = {k: K.pin_state(k) for k in K.PINS}
    arms2 = rd('b614_page_arms_c2.txt')
    nroutes = len(CJ['routes'])
    S = {
        'H48a': (H['H48a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H48b': (H['H48b'], 'Correspondence rows %d (the floor 20), graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H48c': (H['H48c'], 'the tier line reads %s with %d certifying rows; every certifying pin resolves in its clone and at its remote: %s' % (
            H['tier'], J['cert_rows'], all(bool(pins[c[7]][3]) and bool(pins[c[7]][4]) for c in kv))),
        'H48d': (H['H48d'], 'routes %d (%s); against the sieve: %s' % (nroutes, ', '.join(CJ['routes']), CJ['matched'])),
        'N1': _n1(),
        'N2': ('HELD' if CJ['n'] >= 70 else 'REFUTED', '%d claims (the floor 70)' % CJ['n']),
        'N3': ('HELD' if all(K.grade_ok(c) for c in kv) else 'REFUTED', '%d rows kernel-verified, each at a terminal whose pin resolves in its clone '
                                                                         'and at its remote, the statement read there standing: %s' % (
                                                                             len(kv), all(K.grade_ok(c) for c in kv))),
        'N4': ('HELD' if H['H48a'] == 'HOLDS' and H['clean'] and H['ceiling'] == 0 else 'REFUTED',
               'every body sentence traced %s ; the scanner %s ; the ceiling pattern %d' % (H['H48a'], 'CLEAN' if H['clean'] else 'NOT CLEAN', H['ceiling'])),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the papers, the census, REGISTRY, SPIRAL_MAP, b613`s document, the taxonomy, the '
               'sieve, the 2B papers and ERRATA unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools, the table and the '
               'mirror`s roster rows and builder state %s' % (kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if all(p[3] and p[4] for p in pins.values()) and all(ok for _k, ok, _l in kr) and len(kv) == 8 else 'REFUTED',
               'the cited pins resolving %d of %d ; the kernel reads standing %d of %d ; rows kernel-verified %d' % (
                   sum(1 for p in pins.values() if p[3] and p[4]), len(pins), sum(ok for _k, ok, _l in kr), len(kr), len(kv))),
        'S3': ('HELD' if H['placed'] else 'REFUTED', 'the Correspondence placed by (R221)(3) for tier %s: %s' % (H['tier'], H['placed'])),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b614_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _title():
    J, CJ = jl('b614_doc.json'), jl('b614_claims.json')
    return ('## The 2D synthesis: the baryon fraction, the dark sector and the constants at v0.1 from p2-8, p2-9, p2-10, p2-15, p2-25, p2-30, p2-31 and '
            'p2-26, %d claims graded, %d routes read, tier %s; the 2B papers’ fact items; the mirror built after the last push' % (
                J['rows'], len(CJ['routes']), J['tier']))


TRAIL_HEAD = ('### b614 — lane three, act forty-one under (R224): the synthesis for 2D -- one document from the cluster’s eight papers read at address, '
              'every claim graded, the routes read; the 2B papers’ findings entered; the mirror after the last push')
FOR_AUTHOR = (
    '(1) the 2D papers’ findings, for their next editions: COSMOLOGICAL_SIEVE_CEILING :72 gives Selberg 40%%, Conrey 41.6%% and a record near '
    '100%%, where Selberg’s theorem gives a positive proportion and Conrey’s more than two fifths; MATTER_AS_ARITHMETIC :99 gives ℚ exactly three '
    'places by Ostrowski’s theorem, which gives the archimedean place and one p-adic place for each prime; MATTER_AS_ARITHMETIC :111 reads the '
    'partition (3, 3, 1) as a GL(3, 𝔽₂) orbit decomposition, which FANO_DERIVATION_OF_LAMBDA :25 refutes and the claim bank confirms (the '
    'diagonal’s stabilizer of order 24, transitive on the six); PRIME_ORDER :17 says 2^a + 3^b yields no prime between 41 and 137, where 43, 59, 67, '
    '73, 83, 89, 97, 113 and 131 are of that form, and :27 and :54 call 47 and 107 the first primes outside the set, where 37 and 43 are; '
    'FANO_DERIVATION_OF_LAMBDA :193 and heritage/UNIFICATION_OF_FORCES.md :644 carry 12^{11/2}, which gives 11α/12^{11/2} ≈ 9.3 × 10⁻⁸, where '
    'PRIME_ORDER :65 carries 12¹¹²; HODGE_CONSERVATION :48 defines the Griffiths group with an Abel-Jacobi quotient the standard definition does '
    'not carry; YANG_MILLS_MONOGRAPH :103 gives π₁ of the center Z(SU(N)), which is trivial, for the vortex classifier π₁(SU(N)/ℤ_N), and :118 '
    'says Bott periodicity computes every homotopy group of SU(N), where it computes the stable ones; YANG_MILLS_MONOGRAPH :341 says the '
    'structural argument establishes the Yang-Mills result its own :15 claim-status note calls open; STORMER :145 calls the structural justification of total '
    '= n₂^(n₁+n₃) open where its :142 marks it done; FANO_DERIVATION_OF_LAMBDA :143 names ten theorems in SIDE-residual-bridge without a pin, six '
    'standing at the tag v0.1 its :113 cites; STORMER :228 calls the CardDerived route an image of (ℤ/2)³ where SIDE-trivium 1aac3a9 routes it '
    'through the seven discriminant integers; (2) the roster: (R224)(3)’s ten editions were the navigator’s, the diff since 192077f naming 22 '
    'documents’ current editions, all appended on the author’s answer, with the four syntheses -- the 2D synthesis carried because the build '
    'follows the last push; (3) the mirror’s MANIFEST md5 and the zip’s sha256 are banked in relay data/b614_mirror.txt after the build, '
    'OWED to the next act that touches OPEN_TRAILS, since nothing is written to PLACE-papers after the build (STANDING b537); (4) (N1) is scored '
    'in relay after the build; its count of two syntheses meets three added since 192077f')


def _finding_text():
    S, J, CJ = jl('b614_scores.json'), jl('b614_doc.json'), jl('b614_claims.json')
    rl = jl('b614_record_lines.json')
    w, fa, sr = [x['line'] for x in rl['lines']]
    dc = _pp_commit('b614 (R224)(4): ' + DOC)
    t = _title()
    gr = CJ['grades']
    e = ['', t, '',
         '*Filed at b614 on the author’s ruling `(R224)`. Banks: relay `data/b614_reads.txt`, `data/%s`, `data/b614_arith.txt`, '
         '`data/b614_second_reader_addendum.txt`, `data/b614_doc_bank.txt`, `data/b614_page_arms_c2.txt`. Nothing deposits.*' % BANK, '',
         '**The document** (`(R224)`(4)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the eight papers REGISTRY files as p2-8, p2-9, '
         'p2-10, p2-15, p2-25, p2-30, p2-31 and p2-26 read whole at %s, %d claims each restated in one sentence and graded by its paper’s own text -- '
         'kernel-verified %d, theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d. '
         'Tier %s: the kernel-verified rows sit at %d pins in %d kernels, each resolving in its clone and at its remote -- the 4/81 arithmetic over a '
         'tuple defined as (2, 3, 2, 0) at SIDE-omega-b 9c80279 and SIDE-cosmo c5cba30, formation_count at SIDE-kernel 5e668b4, a derived count of '
         'seven at SIDE-trivium 1aac3a9, three weight-1 contributions summing to 14 at SIDE-residual-bridge v0.1, the mass_gap placeholder at '
         'SIDE-effects c66f3c5 (retired at a27415d) and the count eight at SIDE-yang-mills-formation 73e9e2c -- and they certify nothing about the '
         'physics; the Correspondence after the front matter (`(R221)`(3)). The cluster’s arithmetic is recomputed in the claim bank, its '
         'disagreements listed for the author.' % (
             DOC, dc, PRE_PP, CJ['n'], gr.get('kernel-verified', 0), gr.get('theorem-supported', 0), gr.get('argument-supported', 0),
             gr.get('computationally-verified', 0), gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), J['tier'], len(CJ['kvpins']),
             len(set(x.split()[0] for x in CJ['kvpins']))), '',
         '**The routes** (the five tests). %d routes: HODGE_CONSERVATION’s credit of the RH-side exhaustiveness to Conservation of Spectra, Tate’s thesis '
         'and the Mechanism Theorem, and YANG_MILLS_MONOGRAPH’s reading of the RH argument as a verified surround with an Ostrowski criterion -- '
         'each DARK by test 2, matching the sieve’s RH-60. The cluster’s other claims are about cosmology, the constants, Hodge theory and '
         'Yang-Mills, and offer no argument toward RH.' % len(CJ['routes']), '',
         '**The record lines.** b613’s weight, with the four confirmations, at FINDINGS :%d; the 2B papers’ fact items at OPEN_TRAILS :%d, the '
         'COGNITION computation at relay data/b614_arith.txt; the silence-principle reading at :%d, the second reader’s addendum extended at relay '
         'data/b614_second_reader_addendum.txt.' % (w, fa, sr), '',
         '**The mirror.** Built after this act’s last PLACE-papers push (the author’s answer, STANDING b537), the roster taking the 22 documents’ '
         'current editions since 192077f and the four syntheses; its MANIFEST md5 and the zip’s sha256 are banked in relay data/b614_mirror.txt and '
         'are owed to the next act that touches OPEN_TRAILS.', '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R14 (FINDINGS :7212, b610’s §2) and follows the form of '
         'b611’s, b612’s and b613’s syntheses (:7240, :7260, :7280); its two routes meet b609’s sieve row RH-60 (:7186) again, as b611’s, b612’s and '
         'b613’s did; its 4/81 rows read the kernel anchors the cosmology sitting graded (the era annotations it carries); its (ℤ/2)³ rows meet '
         'b612’s Trivium synthesis (:7260). It strengthens the programme’s offering of the arithmetic-substrate cosmology: eight papers, one '
         'DEFUNCT, now have one place where each claim stands at its own grade, the kernel anchors are read at their pins and the arithmetic is '
         'recomputed.', '',
         '**Next.** Per `(R224)`(5): b615, the synthesis for 2F. The author rules on the closing.', '',
         '*Nothing deposits; no paper of either cluster edited; README, REGISTRY and the census unwritten; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    nd, _n = nd_hits(e)
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s' % (bad or 'NONE', nd))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b614_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b614_scores.json'), jl('b614_findings.json'), jl('b614_record_lines.json')
    w, fa, sr = [x['line'] for x in rl['lines']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R224) ratified.** (1) b613 at its weight, its four strike items confirmed. (2) The 2B papers’ findings entered as fact items, the '
             'silence-principle reading for the record. (3) The mirror refreshed. (4) The synthesis for 2D; H48a-H48d. (5) The act after: b615.', '',
             '**Entered:** FINDINGS.md:%d (b613’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the 2B fact items, addressed '
             'to b613’s record :12651), :%d (the silence-principle reading, addressed to W-ORD-SECOND-READER :12212); this record; PLACE-papers `%s`; '
             'relay data/%s, data/b614_arith.txt, data/b614_second_reader_addendum.txt.' % (w, fj['entry_line'], fa, sr, DOC, BANK), '',
             '**Resolved by the seat, for the author’s strike:** the pins the papers name read as cited, eight resolving, so eight rows certify and the '
             'tier reads KC; a terminal named without a pin certifies nothing; the era annotations’ and dated rulings’ pins read as the papers’ own '
             'text; the two routes and their verdicts; UNIFICATION_OF_FORCES synthesised as the census row lists it, its DEFUNCT status on the face. '
             'Two prompts were put and answered before the seal (relay data/b614_author_answers.txt): the roster takes all 22 current editions and '
             'the build follows the last push.', '',
             '**For the author:** %s.' % FOR_AUTHOR, '',
             '**b615 priced** (the sequence’s form: each act prices the next): the census row R16, 2F, three papers, 838 lines -- '
             'phase2/empirical/ZERO_SIMPLICITY.md, BSD_TRANSFER.md and BSD_VIA_FORMATION_TRANSFER.md -- read whole at address; one act, no Lean call; '
             'the tier read from the rows; BSD_TRANSFER names TECHNE once, carried by pointer.', '',
             '**Defects** (relay data/b614_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**A transient network failure, kept:** the first scores run read every cited pin’s remote as absent; tested directly, all eight '
             'resolve by ls-remote, and the scorer was re-run alone (relay data/b614_scores_attempt1.json beside data/b614_scores.json).', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R224)`(5), b615, the synthesis for 2F; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left '
             'it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = nd_hits(e)
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s' % (bad or 'NONE', nd))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b614_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b614_trail.json')['line'])


def desk(*a):
    S = jl('b614_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b614 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H48a-H48d, (R224)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H48 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b614_defects.txt').rstrip(NL).split(NL)
    put_txt('b614_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b614_scores.json'), jl('b614_findings.json'), jl('b614_trail.json'), jl('b614_record_lines.json')
    Z, X = jl('b614_page_zeta.json'), jl('b614_page_chi.json')
    M = jl('b614_mirror.json') if os.path.exists(_p('b614_mirror.json')) else {}
    L = ['b614 -- THE COMPONENTS, BANKED UNDER (R224).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b613`s closing push-out relay %s ; push-b613* branches deleted by name '
         '(data/b614_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b614_arms_prerun.txt) ; the mirror moved '
         'after the last PLACE-papers push by the author`s answer' % STEPZERO,
         '### COMPONENT 1 : b613`s weight FINDINGS :%d ; the 2B fact items OPEN_TRAILS :%d ; the silence-principle reading :%d ; the arithmetic '
         'data/b614_arith.txt ; the addendum data/b614_second_reader_addendum.txt' % tuple(x['line'] for x in rl['lines']),
         '### COMPONENT 2 : the claim bank data/%s ; routes %s' % (BANK, ', '.join(jl('b614_claims.json')['routes'])),
         '### COMPONENT 3 : the document %s ; data/b614_doc_bank.txt ; H48a %s, H48b %s, H48c %s, H48d %s' % (DOC, S['H48a'][0], S['H48b'][0], S['H48c'][0], S['H48d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b614_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b615 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0]),
         '### THE MIRROR : %s ; zip sha256 %s ; MANIFEST md5 %s ; %s' % (M.get('zip', 'NOT BUILT'), M.get('zip_sha256', '-'), M.get('manifest_md5', '-'),
                                                                     'CLEAN ON ALL THREE CLAUSES' if M.get('clean') else 'NOT CLEAN OR NOT BUILT')]
    put_txt('b614_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b614_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
