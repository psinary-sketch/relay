# -*- coding: utf-8 -*-
"""b615_record.py -- THE ACT'S RECORD TOOL, UNDER (R225). ### ONE SUBCOMMAND PER BANK.

### ### b615: LANE THREE, ACT FORTY-TWO -- THE SYNTHESIS FOR CLUSTER 2F; THE KC TIER'S LOAD-BEARING CLAUSE AND THE RE-READ OF THE EARLIER
### TIER LINES; THE 2D PAPERS' FINDINGS AND TWO ERRATA; THE SUITE'S REMOTE READS ONE PER RUN.
### Subcommands write only `data/b615_*` unless the docstring names another file; `dry` on the command line routes every b615 bank, the
### edition and the document to the seat's scratchpad (for `findings`, `trail`, `record_lines` and `errata`, `dry` prints and appends
### nothing). Banks are written by encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`; ERRATA through
### tools/errata_append.py, which refuses a used id before it writes. TECHNE-Core's module documents are read locally for the no-disclosure
### needles and never printed; the act's public text carries TECHNE by pointer alone. No platform call. No Lean call. The template is
### tools/b614_record.py.
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

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b602_record as R2  # noqa: E402
import b604_record as R4  # noqa: E402
import b615_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = 'b89d88e8'
STEPZERO = '98fccb22'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f8294c02-be2c-4e3c-9aa7-3744e9ce9ce7/scratchpad'
SESSION_ID = 'f8294c02-be2c-4e3c-9aa7-3744e9ce9ce7'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md'
DOC2D = 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
METHOD_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
BANK = 'b615_claims_2F.txt'
ERR_IDS = ('E-2026-10-04-3', 'E-2026-10-04-4')
SYN = {
    '1.2': 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md',
    '1.5E': 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
    '2B': 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md',
    '2D': DOC2D,
}
EDITION = {k: v[:-3] + '_v0_2.md' for k, v in SYN.items()}
PAPERS_2D = {
    'CS': 'phase2/physics/COSMOLOGICAL_SIEVE_CEILING.md', 'MA': 'phase2/physics/MATTER_AS_ARITHMETIC.md', 'ST': 'phase2/physics/STORMER.md',
    'HC': 'phase2/physics/HODGE_CONSERVATION.md', 'PO': 'phase2/physics/PRIME_ORDER.md', 'FA': 'phase2/physics/FANO_DERIVATION_OF_LAMBDA.md',
    'YM': 'phase2/physics/YANG_MILLS_MONOGRAPH.md', 'UF': 'heritage/UNIFICATION_OF_FORCES.md'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines', 'errata')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b615_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b615_') else '', name, len(b)))
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
    '(a) THE SEAT`S, FOUND AFTER THE SEAL, AT THE SUITE`S RUN AFTER ITS EDIT (data/b615_checks_after_edit_attempt1.txt): two positive controls '
    'of the sealed suite passed -- G-DOC-TRACES deleted one trace from a sentence carrying two (ZS :64 and ZS :106), so the sentence still '
    'traced, the species of b613`s defect (a) repeated; G-WEIGHT-LINE mutated a phrase its predicate does not read. Both controls re-pointed '
    'through the Edit tool at a line the arm reads, each mutated text occurring once (a body sentence with one trace, at BV :213; the weight '
    'line`s head), and the suite re-run after the edit; the arms` LIVE verdicts and the sealed (G2) list unchanged.',
]
DEFECT_SHORT = ['(a) the seat’s: two positive controls of the sealed suite passed at the run after the edit -- G-DOC-TRACES deleted one of a '
                'sentence’s two traces, G-WEIGHT-LINE mutated a phrase its predicate does not read -- each re-pointed through the Edit tool and '
                'the suite re-run']


def defects(*a):
    L = ['b615 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b615_defects.txt', L)


# ================================================================================ READING (1): THE READS
_SYN_SEL = ('GREP', r'^# |^\*\*DOCUMENT CLASS|^\*This document synthesises|^\*v0\.1, |^## Correspondence|^## 1\. |^## Back matter|'
                    r'^### The routes through the five tests|\| kernel-verified \| ')
READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the 2F and 2G rows and the no-keystone section', PP, PRE_PP, CEN3,
     ('GREP', r'^\| R16 \||^\| R17 \||^## §2|^- \*\*R16 |^- \*\*R17 '), 900),
    ('REGISTRY.md: the 2F heading and rows p2-6, p2-11, p2-29', PP, PRE_PP, 'REGISTRY.md', [289, 293, 294, 295], 900),
] + [('%s whole (%s)' % (v[0].split('/')[-1], v[1]), PP, PRE_PP, v[0], 'ALL', 300) for v in K.PAPERS.values()] + [
    ('the four syntheses: title, tier line, head line, version line, the Correspondence and body heads, the kernel-verified rows (%s)' % k, PP,
     PRE_PP, p, _SYN_SEL, 600) for k, p in SYN.items()] + [
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the five tests, RH-58, RH-59, RH-60', PP, PRE_PP, K.SIEVE, [24, 26, 28, 29, 30, 31, 32, 120, 121, 122], 700),
    ('ERRATA.md: the head, the entry form and the latest entries', PP, PRE_PP, 'ERRATA.md', [1, 9, 11, 19, 841, 843, 845, 847, 849, 851, 853, 856],
     500),
    ('OPEN_TRAILS: the form, the arm-unrun standing line, the precedence order, the sequence`s form, (R19)`s clauses, b614`s record lines and record',
     PP, PRE_PP, 'OPEN_TRAILS.md', [11864, 12188, 12228, 12566, 12601, 12671, 12673, 12675], 1500),
    ('FINDINGS: b614`s weight line for b613 and b614`s entry', PP, PRE_PP, 'FINDINGS.md', [7298, 7300], 600),
] + [('the 2D fact items` lines: %s' % k, PP, PRE_PP, p, sel, 500) for k, p, sel in (
    ('CS', PAPERS_2D['CS'], [72]), ('MA', PAPERS_2D['MA'], [99, 111]), ('FA', PAPERS_2D['FA'], [25, 191, 193]),
    ('PO', PAPERS_2D['PO'], [17, 19, 27, 54, 65, 67]), ('HC', PAPERS_2D['HC'], [48]), ('YM', PAPERS_2D['YM'], [15, 103, 118, 341]),
    ('ST', PAPERS_2D['ST'], [142, 145]), ('UF', PAPERS_2D['UF'], [640, 641, 644]))] + [
    ('the suite`s ls-remote call sites at b614, by file and line: tools/b614_checks.py', RELAY, PRE_RELAY, 'tools/b614_checks.py', [277, 311], 260),
    ('tools/b614_claims.py', RELAY, PRE_RELAY, 'tools/b614_claims.py', [510, 519, 526, 564], 260),
    ('tools/b614_record.py', RELAY, PRE_RELAY, 'tools/b614_record.py', [175, 181, 1003], 260),
    ('tools/b614_closing.py', RELAY, PRE_RELAY, 'tools/b614_closing.py', [89, 94], 260),
    ('relay data/b614_mirror.txt (its figures)', RELAY, PRE_RELAY, 'data/b614_mirror.txt', list(range(1, 13)), 300),
    ('relay data/b614_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b614_closing_push_out.txt', 'ALL', 260),
    ('relay data/b614_scores.json (whole)', RELAY, STEPZERO, 'data/b614_scores.json', 'ALL', 300),
    ('SIDE-effects c66f3c5: its toolchain', 'D:/SIDE-effects', 'c66f3c5', 'lean-toolchain', [1], 200),
    ('SIDE-effects main: the retirement record', 'D:/SIDE-effects', 'main', 'SIDEEffects/Structural.lean', [98, 99, 100], 220),
] + [('%s at %s: %s' % (K.PINS[v[0]][0], K.PINS[v[0]][1], k), 'D:/' + K.PINS[v[0]][0], K.PINS[v[0]][1], v[1], [v[2]], 260) for k, v in K.KREADS.items()] + [
    ('%s at %s: %s' % (K.PINS_NT[v[0]][0], K.PINS_NT[v[0]][1], k), 'D:/' + K.PINS_NT[v[0]][0], K.PINS_NT[v[0]][1], v[1], [v[2]], 260)
    for k, v in K.NTREADS.items()]


def reads(*a):
    L = ['b615 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
            if 'TECHNE' in line and path.endswith('BSD_TRANSFER.md'):
                line = ' '.join(line.split()[:6]) + ' ### [TECHNE CONTENT: by pointer alone, TECHNE-Core manifest sha256 %s]' % K.techne_pointer()
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### THE PINS THE PAPERS NAME WITH A TERMINAL, EACH AS CITED, RESOLVED IN ITS CLONE AND AT ITS REMOTE:']
    for k in K.PINS:
        st = K.pin_state(k)
        L.append('    %-9s %s %s -> %s ; at the remote: %s -- named at %s' % (k, st[1], st[2], st[3] or '### DOES NOT RESOLVE', st[4] or '### NONE', K.PINS[k][3]))
    L += ['### THE PINS THE PAPERS NAME WITHOUT A TERMINAL:']
    for k in K.PINS_NT:
        st = K.pin_state(k)
        L.append('    %-9s %s %s -> %s ; at the remote: %s -- named at %s' % (k, st[1], st[2], st[3] or '### DOES NOT RESOLVE', st[4] or '### NONE', K.PINS_NT[k][3]))
    L += ['    the head commits` subjects: %s' % [K.commit_subject(k) for k in ('bft', 'bm')]]
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('    %-44s named without a pin (%s); read for the record at %s %s = %s, %s :%d: %s' % (k, st[7], st[1], st[2], st[6], st[3], st[4],
                                                                                                    'stands' if st[5] else '### ABSENT'))
    nd = nd_sets()
    L += ['### THE NO-DISCLOSURE NEEDLE SETS, read locally at TECHNE-Core %s and never printed: the method document %s, %d sentences of 40 '
          'characters or more (b591`s form); the tree %s, %d (b595`s form); every module document, %d sentences of 60 characters or more '
          '(b611`s form)' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), METHOD_REL, len(nd['method']), TREE_REL, len(nd['tree']), len(nd['modules'])),
          '### TECHNE mentions in the three papers: %s ; the pointer each takes: TECHNE-Core, its tracked-file manifest sha256 %s' % (
              {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()}, K.techne_pointer()),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b615_reads.txt', L)


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
    L = ['### b615 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-04), banked verbatim with the options and the '
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
        L.append('### NONE: no prompt was put to the author in this act; the precedence order reached every reading.')
    put_txt('b615_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-effects', 'SIDE-simplicity',
         'SIDE-bsd-formation-transfer', 'SIDE-bsd-multiplicity', 'SIDE-silence-principle', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-trivium',
         'SIDE-residual-bridge', 'SIDE-yang-mills-formation', 'SIDE-substrate-cluster', 'SIDE-constants')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b615_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b615_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


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


# ================================================================================ COMPONENT 1: THE ARITHMETIC, THE RECORD LINES, THE ERRATA
P15 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337)


def arith(*a):
    """### data/b615_arith.txt and its json: (R225)(3)'s PRIME_ORDER list and the 12^{11/2} value, each computed here, its range printed."""
    import mpmath
    mpmath.mp.dps = 30
    sums = sorted(set(2 ** x + 3 ** y for x in range(0, 10) for y in range(0, 7)))
    sp = [n for n in sums if K._is_prime(n) and n <= 337]
    b41 = [n for n in sp if 41 < n < 137]
    b137 = [n for n in sp if 137 < n < 337]
    outside = [n for n in range(2, 107) if K._is_prime(n) and n not in P15]
    al = mpmath.mpf('0.0072973525643')
    t12 = mpmath.mpf(12) ** mpmath.mpf(5.5)
    her = 11 * al / t12
    lam0 = 11 * al / mpmath.mpf(12) ** 112
    L = ['b615 -- COMPONENT 1: THE ARITHMETIC OF (R225)(3), computed %s (Python %s, mpmath %s)' % (utc(), sys.version.split()[0], mpmath.__version__), '',
         '### (i) PRIME_ORDER :17 (phase2/physics/PRIME_ORDER.md): the primes of the form 2^a + 3^b, a and b ≥ 0, every exponent with 2^a ≤ 512 and '
         '3^b ≤ 729 enumerated, so every sum up to 337 is reached.',
         '    the primes up to 337 of the form: %s (%d)' % (', '.join(map(str, sp)), len(sp)),
         '    between 41 and 137: %s (%d) ; between 137 and 337: %s (%d)' % (', '.join(map(str, b41)), len(b41), ', '.join(map(str, b137)), len(b137)),
         '    THE LIST OF RECORD: 43, 59, 67, 73, 83, 89, 97, 113 and 131 lie between 41 and 137, the seat`s list as (R225)(3) names it; 251, 257, 283 '
         'and 307 lie between 137 and 337, the stretch :17 also calls empty.',
         '', '### (ii) PRIME_ORDER :27 and :54: the primes below 107 outside the paper`s set {%s}: %s' % (', '.join(map(str, P15)), ', '.join(map(str, outside))),
         '    THE ORDER OF RECORD: 37 and 43 come before 47, so 47 and 107 are not the first primes outside the set.',
         '', '### (iii) FANO_DERIVATION_OF_LAMBDA :193 and heritage/UNIFICATION_OF_FORCES.md :644 against PRIME_ORDER :65-:67, α = 0.0072973525643 '
         '(CODATA 2018):',
         '    12^(11/2) = %s ; 11α/12^(11/2) = %s ; 11α/12^112 = %s' % (mpmath.nstr(t12, 8), mpmath.nstr(her, 4), mpmath.nstr(lam0, 4)),
         '    THE VALUE OF RECORD: 11α/12^(11/2) ≈ 9.3 × 10⁻⁸, against the order 10⁻¹²² the heritage formula is read as (UNIFICATION_OF_FORCES '
         ':640-:641); the exponent 112 of PRIME_ORDER :65 gives 1.087 × 10⁻¹²².']
    put_txt('b615_arith.txt', L)
    put_json('b615_arith.json', dict(at=utc(), sp=sp, b41=b41, b137=b137, outside=outside, t12=float(t12), her=float(her), lam0=mpmath.nstr(lam0, 6)))
    for l in L:
        print(l[:220])


B614_ENTRY = '## The 2D synthesis: the baryon fraction, the dark sector and the constants at v0.1'
B614_TRAIL = '### b614 — lane three, act forty-one under (R224): the synthesis for 2D'
FORM_CLAUSES = '*Appended 2026-10-03 by b611 to the synthesis sequence’s form (:12566), under `(R221)`(3) -- THREE CLAUSES OF THE SYNTHESIS FORM:*'
ARM_STANDING = '*Appended 2026-10-02 by b592 to b591’s record (:12172), under the author’s ruling `(R202)`(3) -- THE ARM-UNRUN STANDING LINE:*'
M_HEAD = '*Appended 2026-10-04 by b615 to b614’s record (:%d), under `(R225)`(1) -- THE MIRROR’S FIGURES, OWED BY b614’S RECORD AND ENTERED:*'
CL_HEAD = ('*Appended 2026-10-04 by b615 to the synthesis form’s clauses (:%d), under `(R225)`(2) -- THE FORM’S FOURTH CLAUSE, THE KC TIER’S '
           'LOAD-BEARING CLAUSE:*')
F_HEAD = ('*Appended 2026-10-04 by b615 to b614’s record (:%d), under `(R225)`(3) -- THE 2D PAPERS’ FINDINGS, FACT ITEMS FOR THEIR NEXT EDITIONS, '
          'TWO OF THEM ERRATA, THE SYNTHESIS’S ROWS STANDING AS GRADED:*')
S_HEAD = '*Appended 2026-10-04 by b615 to the arm-unrun standing line (:%d), under `(R225)`(4) -- THE SUITE’S REMOTE READS, STANDING:*'
W_HEAD = '*Appended 2026-10-04 by b615 to b614’s entry (:%d), under `(R225)`(1) -- b614 AT ITS WEIGHT:*'


def _b614():
    S = json.loads(R4._show(RELAY, STEPZERO, 'data/b614_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _mirror614():
    M = json.loads(R4._show(RELAY, STEPZERO, 'data/b614_mirror.json'))
    if M.get('zip_sha256') != '9abdc876bc98c8b8a50b5ce7c25ab94a6c3327e9e353fe04d13f7a05559f2e14' or M.get('manifest_md5') != '20ed9b0572787dc2a14984922153ff4c':
        sys.exit('### b614`S MIRROR BANK DOES NOT CARRY THE RULING`S FIGURES -- NOTHING WRITTEN')
    return M


def _texts(entry, trail, form, arm, dry=False):
    s = _b614()
    allh = lambda ks, w: w if all(s[k] == w for k in ks) else [s[k] for k in ks]   # noqa: E731
    M = _mirror614()
    A = json.load(io.open(os.path.join(SP if dry else D, 'b615_arith.json'), encoding='utf-8'))
    tm = ('\n%s the mirror built after b614’s last PLACE-papers push, at f22a13a: %s, %d files, CLEAN on all three clauses; the zip’s sha256 %s; '
          'the MANIFEST’s md5 %s; the roster’s 26 rows committed alone in relay (6fc380a6), %d base rows carrying their current edition’s version '
          'with a see note; banked at relay data/b614_mirror.txt. The item b614’s record names OWED is discharged by this line.\n' % (
              M_HEAD % trail, M['zip'], M['entries'] - 1, M['zip_sha256'], M['manifest_md5'], M['see_rows']))
    tc = ('\n%s (iv) `(R19)`’s KC obligation is that every load-bearing claim is carried by a row; a document’s tier line reads KC when at least one '
          'kernel-verified row is load-bearing for the cluster’s thesis as the document’s head states it, and reads C when the kernel-verified rows '
          'certify definitions, arithmetic over the papers’ own tuples, or placeholders that bear no claim the thesis makes -- the rows stay '
          'kernel-verified, the tier does not follow them. Applied first at b615 to the four earlier syntheses’ tier lines and to 2F’s (relay '
          'data/b615_reread.txt).\n' % (CL_HEAD % form))
    tf = ('\n%s (i) phase2/physics/COSMOLOGICAL_SIEVE_CEILING.md :72 gives Selberg 40 percent, Conrey 41.6 percent and a record near 100 percent; '
          'Selberg’s theorem gives a positive proportion of the zeros on the line and Conrey’s more than two fifths, and the record near 100 percent '
          'is unsupported -- a fact item, the literature read at its edition. (ii) phase2/physics/MATTER_AS_ARITHMETIC.md :99 gives ℚ exactly three '
          'places by Ostrowski’s theorem, which gives the archimedean place and one p-adic place for each prime -- a fact item. (iii) '
          'phase2/physics/PRIME_ORDER.md :17 says the sum 2^a + 3^b yields no prime between 41 and 137, where %s are of that form (and %s between 137 '
          'and 337), and :27 and :54 call 47 and 107 the first primes outside its set, where 37 and 43 are smaller -- ERRATA %s, the computation at '
          'relay data/b615_arith.txt. (iv) phase2/physics/FANO_DERIVATION_OF_LAMBDA.md :193 and heritage/UNIFICATION_OF_FORCES.md :644 carry '
          '12^{11/2} where PRIME_ORDER :65 carries 12¹¹²; 11α/12^{11/2} ≈ 9.3 × 10⁻⁸ against the claimed order 10⁻¹²² -- ERRATA %s, since the exponent '
          'carries the paper’s number. (v) MATTER_AS_ARITHMETIC :111 reads the partition (3, 3, 1) as a GL(3, 𝔽₂) orbit decomposition, which '
          'FANO_DERIVATION_OF_LAMBDA :25 refutes and relay data/b614_claims_2D.txt confirms (the diagonal’s stabilizer of order 24, transitive on the '
          'six) -- a fact item at MATTER. (vi) phase2/physics/HODGE_CONSERVATION.md :48 defines the Griffiths group with an Abel-Jacobi quotient the '
          'standard definition does not carry -- a fact item. (vii) phase2/physics/YANG_MILLS_MONOGRAPH.md :103 gives π₁ of the centre Z(SU(N)), '
          'which is trivial, where the vortex classifier is π₁(SU(N)/ℤ_N), and :118 says Bott periodicity computes the homotopy groups of SU(N), '
          'where it gives the stable groups alone -- fact items. (viii) The internal tensions, YANG_MILLS_MONOGRAPH :341 against its :15 and '
          'phase2/physics/STORMER.md :145 against its :142 -- restatement items, the later sentence taking the ceiling at the edition. The '
          'synthesis’s rows stand as graded. The cluster-level reading, for the record: the 2D papers carry 69 statement-grade rows of 143 and the '
          'errors above, so the cluster’s synthesis is the second reader’s instrument for Phase 2 as the editions were for Phase 1.5.\n' % (
              F_HEAD % trail, ', '.join(map(str, A['b41'][:-1])) + ' and %d' % A['b41'][-1], ', '.join(map(str, A['b137'][:-1])) + ' and %d' % A['b137'][-1],
              ERR_IDS[0], ERR_IDS[1]))
    ts = ('\n%s every suite resolves each remote pin once per run and reuses the read across arms, so a burst of ls-remote calls does not refute '
          'an arm; a failed read is retried once alone before the arm reads it as failed. The occasion is b614’s five bursts, each claim tested '
          'directly and the tool re-run alone (relay data/b614_checks_attempt1.txt and its siblings). Applied first at b615, whose suite takes the '
          'edit after its seal through the Edit tool, the edit committed alone in relay.\n' % (S_HEAD % arm))
    return [(M_HEAD % trail, tm), (CL_HEAD % form, tc), (F_HEAD % trail, tf), (S_HEAD % arm, ts)], s


def _weight(entry, mline, cline, s):
    allh = lambda ks, w: w if all(s[k] == w for k in ks) else [s[k] for k in ks]   # noqa: E731
    return ('\n%s THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS.md v0.1 (PLACE-papers 0672d78): eight papers read whole at e7b444e and '
            'unedited; 143 claims -- 8 kernel-verified, 7 theorem-supported, 17 argument-supported, 27 computationally-verified, 15 '
            'synthesis-suggested, 69 statement-grade; the eight kernel-verified rows at eight pins in seven kernels, each resolving in its clone and '
            'at its remote, certifying arithmetic over tuples their own files define (4/81, the count 7, the sum 14), the Yang-Mills placeholder '
            'form and the count of eight -- none of it says anything about the physics, the seat’s sentence, which the load-bearing clause carries '
            '(OPEN_TRAILS :%d); two routes DARK by test 2 matching RH-60 (HODGE_CONSERVATION :16, :127, :133; YANG_MILLS_MONOGRAPH :323); the '
            'scanner clean, the no-disclosure arm 0 hits, both pages unchanged. The verdicts, as relay data/b614_scores.json prints them: H48a-H48d '
            '%s; N1 %s in letter (four syntheses named, the navigator’s two), N2-N5 %s; S1-S5 %s. COGNITION’s r ≈ 0.782 over 11 rows and 217 '
            'against 261 banked (relay data/b614_arith.txt). The mirror at f22a13a under the author’s two answers: the roster’s 26 rows committed '
            'alone in relay, 16 base rows with see notes, mirror-refresh-2026-10-04.zip, 70 files, CLEAN on three clauses, its figures entered at '
            'OPEN_TRAILS :%d. FINDINGS :7298, :7300; OPEN_TRAILS :12671, :12673, :12675; PLACE-papers 0672d78, f22a13a; relay 1a237840, 6fc380a6, '
            'b89d88e8. The suite 88 of 88 before and after the push; defect (a) the seat’s (a heredoc splice before the seal, read back); the '
            'ls-remote bursts five times, each claim tested directly and the tool re-run alone. Nothing deposited; no kernel touched; TECHNE-Core '
            'untouched.\n' % (W_HEAD % entry, cline, allh(('H48a', 'H48b', 'H48c', 'H48d'), 'HOLDS'), s['N1'], allh(('N2', 'N3', 'N4', 'N5'), 'HELD'),
                              allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), mline))


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
    return Q, Q.line_of(Q.FIND, B614_ENTRY), Q.line_of(Q.OT, B614_TRAIL), Q.line_of(Q.OT, FORM_CLAUSES), Q.line_of(Q.OT, ARM_STANDING)


def record_lines(*a):
    """### OPEN_TRAILS: the mirror's figures and the 2D fact items (addressed to b614's record), the load-bearing clause (addressed to the form's
    ### clauses), the remote-reads standing line (addressed to the arm-unrun standing line); then FINDINGS: b614's weight, addressed to b614's
    ### entry -- each appended at the end. Needs the arithmetic."""
    Q, entry, trail, form, arm = _addr()
    if (entry, trail, form, arm) != (7300, 12675, 12601, 12188):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s, %s) -- NOTHING WRITTEN' % (entry, trail, form, arm))
    dry = 'dry' in a
    if not os.path.exists(os.path.join(SP if dry else D, 'b615_arith.json')):
        sys.exit('### b615_arith.json IS NOT BANKED -- NOTHING WRITTEN')
    parts, s = _texts(entry, trail, form, arm, dry)
    wt = _weight(entry, 0, 0, s)
    bad = ledger_check(*([t for _h, t in parts] + [wt]))
    nd, _n = nd_hits(NL.join([t for _h, t in parts] + [wt]))
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits in the lines: %s' % (bad or 'NONE', nd))
    if dry:
        for _h, t in parts:
            print(t)
        print(wt)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    for h, _t in parts:
        Q.guard_absent(Q.OT, h)
    Q.guard_absent(Q.FIND, W_HEAD % entry)
    out = []
    for h, t in parts:
        r = Q.append_to(Q.OT, t)
        out.append(dict(file='OPEN_TRAILS.md', head=h, line=Q.line_of(Q.OT, h), append=r))
    wt = _weight(entry, out[0]['line'], out[1]['line'], s)
    r = Q.append_to(Q.FIND, wt)
    out.append(dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r))
    put_json('b615_record_lines.json', dict(entry=entry, trail=trail, form=form, arm=arm, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


def _rl():
    """### the record lines by role: mirror, clause, fact, standing, weight"""
    ls = jl('b615_record_lines.json')['lines']
    return dict(zip(('mirror', 'clause', 'fact', 'standing', 'weight'), [x['line'] for x in ls]))


def _errata_blocks(dry=False):
    A = json.load(io.open(os.path.join(SP if dry else D, 'b615_arith.json'), encoding='utf-8'))
    fa = 0 if dry else _rl()['fact']
    lst = lambda xs: ', '.join(map(str, xs[:-1])) + ' and %d' % xs[-1]   # noqa: E731
    e3 = [
        '## %s — PRIME_ORDER :17 says the sum 2^a + 3^b yields no prime between 41 and 137 nor between 137 and 337, where nine primes of that form '
        'lie in the first stretch and four in the second, and :27 and :54 call 47 and 107 the first primes outside its set, where 37 and 43 are '
        'smaller (CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)' % ERR_IDS[0], '',
        '**Filed 2026-10-04 by b615, on the author’s ruling `(R225)`(3); found at b614 (relay `data/b614_claims_2D.txt`, Part E), computed at b615 '
        '(relay `data/b615_arith.txt`). Record affected: `phase2/physics/PRIME_ORDER.md` :17, :27, :54. ### NO DEPOSITED ARTIFACT IS AFFECTED BY '
        'THIS ENTRY: no file under `outputs/` carries these sentences (searched at PLACE-papers f22a13a).**', '',
        '**What the lines say.** :17: *“Eleven appear in sequence — 5, 7, 11, 13, 17, 19, 29, 31, 41 — and then, past a stretch where the sum '
        'produces no prime, two more arrive far out: 137 and 337.”*; :27: *“each has a child just outside the Core where the structure first spills '
        'over: 2·23+1 = 47 and 2·53+1 = 107”*; :54: *“the Sophie Germain pair whose children 47 = 2·23+1 and 107 = 2·53+1 are the first primes '
        'outside the Core.”*', '',
        '**What is true.** The primes of the form 2^a + 3^b with a, b ≥ 0 up to 337 are %s (%d of them, relay `data/b615_arith.txt`): between 41 '
        'and 137 lie %s, and between 137 and 337 lie %s. Below 107 the primes outside the paper’s fifteen-prime set are %s, so 37 and 43 come before '
        '47.' % (lst(A['sp']), len(A['sp']), lst(A['b41']), lst(A['b137']), lst(A['outside'])), '',
        '**The correction.** At :17 the sum does not stop at 41: nine primes of its form lie between 41 and 137 and four between 137 and 337, the '
        'list of record being the one above. At :27 and :54 the first primes outside the set are 37 and 43; 47 and 107 are the Sophie Germain '
        'children of 23 and 53, which stands. Which primes the set carries is the paper’s; this entry corrects the counting sentences alone, the '
        'stretch between 137 and 337 the seat’s computation beside the ruling’s named stretch.', '',
        '**Scope.** No line is edited: PRIME_ORDER takes the correction at its next edition as a fact item (OPEN_TRAILS :%d). No banked number, '
        'verdict or grade moves. Nothing here is a statement about RH or any zero.' % fa, '',
        '**Status.** FILED.', '']
    e4 = [
        '## %s — FANO_DERIVATION_OF_LAMBDA :193 and heritage UNIFICATION_OF_FORCES :644 give Λ’s leading term as 11α/12^{11/2}, about 9.3 × 10⁻⁸ '
        'and not of the order 10⁻¹²² the heritage formula is read as; PRIME_ORDER :65 carries the exponent 112 (CORPUS-FACING; NO DEPOSITED '
        'ARTIFACT IS AFFECTED)' % ERR_IDS[1], '',
        '**Filed 2026-10-04 by b615, on the author’s ruling `(R225)`(3); found at b614 (relay `data/b614_claims_2D.txt`, Part E), computed at b615 '
        '(relay `data/b615_arith.txt`). Records affected: `phase2/physics/FANO_DERIVATION_OF_LAMBDA.md` :193 and `heritage/UNIFICATION_OF_FORCES.md` '
        ':644. ### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY: no file under `outputs/` carries the formula (searched at PLACE-papers '
        'f22a13a).**', '',
        '**What the lines say.** FANO_DERIVATION_OF_LAMBDA :193 and UNIFICATION_OF_FORCES :644: *“Λ = 11α/12^{11/2} × [1 + …] − 337α⁶/27”*, the '
        'heritage formula, which UNIFICATION_OF_FORCES :640-:641 reads as carrying the factor 10⁻¹²²; PRIME_ORDER :65: *“Λ₀ = 11α/12¹¹²”*.', '',
        '**What is true.** With α = 0.0072973525643 (CODATA 2018), 12^{11/2} ≈ %s and 11α/12^{11/2} ≈ %.2f × 10⁻⁸; 11α/12¹¹² ≈ %s × 10⁻¹²², the '
        'leading term PRIME_ORDER :67 gives (relay `data/b615_arith.txt`).' % ('{:,}'.format(int(round(A['t12']))), A['her'] * 1e8,
                                                                              A['lam0'].split('e')[0][:5]), '',
        '**The correction.** At FANO_DERIVATION_OF_LAMBDA :193 and UNIFICATION_OF_FORCES :644 the exponent of record is 112, as PRIME_ORDER :65 '
        'carries it: with 11/2 the leading term is about 9.3 × 10⁻⁸, so the exponent carries the paper’s number.', '',
        '**Scope.** No line is edited: FANO_DERIVATION_OF_LAMBDA takes the correction at its next edition as a fact item (OPEN_TRAILS :%d), and '
        'UNIFICATION_OF_FORCES, which REGISTRY files DEFUNCT in heritage/, carries it beside any later reading. No banked number, verdict or grade '
        'moves.' % fa, '',
        '**Status.** FILED.', '']
    return [(ERR_IDS[0], e3), (ERR_IDS[1], e4)]


def errata(*a):
    """### PLACE-papers ERRATA.md: the two entries of (R225)(3), appended through tools/errata_append.py, each refused if its id is used.
    ### Needs the record lines (the entries point at the fact items' line)."""
    import errata_append as EA
    blocks = _errata_blocks('dry' in a)
    text = NL.join(NL.join(b) for _i, b in blocks)
    nd, _n = nd_hits(text)
    import banned_terms as BT
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    print('  ceiling hits in the entries: %s ; banned stems: %s ; no-disclosure hits: %s' % ([m.group(0) for m in CEILING.finditer(text)] or 'NONE',
                                                                                             live or 'NONE', nd))
    if 'dry' in a:
        print(text)
        return
    if any(nd.values()) or live:
        sys.exit('### AN ENTRY WOULD CARRY TECHNE TEXT OR A STEM -- NOTHING WRITTEN')
    path = os.path.join(PP, 'ERRATA.md')
    out = []
    for i, b in blocks:
        code, lines = EA.append(path, i, b)
        for l in lines:
            print(l)
        if code != 0:
            sys.exit('### THE APPENDER REFUSED %s -- STOPPED' % i)
        R = io.open(path, encoding='utf-8').read().replace(chr(13), '').split(NL)
        out.append(dict(id=i, line=next(k + 1 for k, l in enumerate(R) if l.startswith('## %s ' % i))))
    put_json('b615_errata.json', dict(at=utc(), entries=out))
    for o in out:
        print('  ERRATA.md %s :%d' % (o['id'], o['line']))


# ================================================================================ COMPONENT 2: THE RE-READ OF THE FOUR TIER LINES
THESIS = {
    '1.2': 'the mechanism exclusion as the four papers present it -- the specification n² → θ → ξ, the seven classes, the I.D.S. Mechanism Theorem '
           'and the three paths: the conditional the papers state from the conservation clause h2 to RH and the pieces it is built from',
    '1.5E': 'the {2, 3} substrate and the Trivium -- the Frobenius pair, the seven quadratic fields, the Trivium vector, the class-number diagonal and '
            'the prime mosaic',
    '2B': 'the Silence Principle and interface darkness -- natural language and validity, the conservation of cognition, the pedagogy and IMO '
          'correlations and the identity subspace',
    '2D': 'the baryon fraction, the dark sector and the constants -- the lithium plateaux, the Størmer wall, the Fano split, Hodge conservation and '
          'the Yang-Mills exclusion form, as physics',
}
LOADS = {
    '1.2': {
        'EA-01': (True, 'ConservationBridge.riemann_hypothesis: the conditional from h2 to RH, the exclusion’s compiled output'),
        'EA-20': (True, 'rh_from_structural_exhaustiveness: the conditional StructuralExhaustiveness → RH the papers name as the kernel’s output'),
        'EA-21': (False, 'that the named terminals resolve and compile, with the formation sum 2 + 3 + 2 + 0 = 7 by decide: names and arithmetic '
                         'over numerals'),
        'ME-01': (True, 'ConservationBridge.riemann_hypothesis: the conditional from h2 to RH'),
        'ME-04': (False, '2 + 3 + 2 + 0 = 7 by decide: arithmetic over numerals, not that the classes number seven'),
        'ME-09': (True, 'spectral_cannon: the derivative of the completed zeta purely imaginary on the line, an analytic statement about ξ'),
        'IR-08': (True, 'rh_from_structural_exhaustiveness: the conditional StructuralExhaustiveness → RH'),
        'IP-03': (True, 'balance_theorem: p^(−s) = p^(−(1−s)) ↔ s = 1/2 for a prime p, the balance class’s content'),
    },
    '1.5E': {
        'FR-01': (True, 'g_two_three and g_two_three_minimal: g(2, 3) = 1 and g ≥ 2 for every other pair, a theorem over all pairs, the Frobenius '
                        'pair the head names'),
        'FR-03': (True, 'the indicial factorisation over ℚ with the double root −1/2, the substrate’s appearance at σ = 1/2'),
        'FR-05': (True, 'S² = −1 and (ST)³ = −1 in SL₂(ℤ), matrix identities over ℤ, the substrate’s modular appearance'),
        'TS-04': (True, 'g(2, 3) = 1 and the modular relations at SIDE-frobenius v0.1.0, as FR-01 and FR-05'),
        'CN-02': (False, 'partition_cardinalities: a count over a list the kernel defines; the identification with ℚ(√−6) is the paper’s'),
        'CN-07': (False, 'sideIDS: the schema applied to an instance defined with the formation ⟨2, 3, 2, 0⟩, a definition'),
        'CN-10': (False, 'the abstract schema: bijectivity from the structure’s own fields'),
        'CN-11': (False, 'trivium_theorem: an equivalence between two types the kernel defines, each of card 7'),
        'CN-12': (False, 'by decide over an encoded class-number table whose grounding is open (LV-L-4)'),
        'CN-13': (False, 'diagonal_unpaired: a combinatorial fact over the kernel’s own enumeration'),
    },
    '2B': {},
    '2D': {
        'MA-18': (False, 'Ω of a tuple defined as ⟨2, 3, 2, 0⟩ is 4/81: arithmetic over a tuple its own file defines'),
        'MA-19': (False, 'the counts 81 and 4 for a tuple defined as numerals'),
        'ST-16': (False, 'the sum of four numerals is 7'),
        'ST-17': (False, 'the card of a kernel-defined type equals the card of a seven-integer set: a derived count over definitions'),
        'ST-18': (False, 'the same 4/81 arithmetic, as MA-18'),
        'FA-08': (False, 'three copies of (14, 3) sum to 14 by decide: arithmetic over a pair its own file defines'),
        'YM-20': (False, 'a placeholder form, each sector’s predicate defined True, bearing no claim about the physics'),
        'YM-21': (False, 'the count (3, 3, 2, 0) = 8 over entries defined as numerals'),
    },
}
SUMMARY_C = {
    '2D': 'they certify arithmetic over tuples their own files define (4/81, the count 7, the sum 14), a placeholder form and the count of eight, '
          'and certify nothing about the physics',
}
KV_ROW = re.compile(r'^\| ([A-Z]{2}-\d\d) \| [^|]+ \| [^|]+ \| kernel-verified \| ')


def _syn(key):
    t = g(PP, 'show', 'HEAD:' + SYN[key])
    return K.lines_of(t)


def reread(*a):
    """### data/b615_reread.txt and its json: each synthesis's kernel-verified rows read against its head's thesis, load-bearing or not,
    ### and the tier line left or re-read, (R225)(2)."""
    out, L = {}, ['b615 -- COMPONENT 2: THE RE-READ OF THE FOUR TIER LINES UNDER THE LOAD-BEARING CLAUSE, (R225)(2), banked %s' % utc(),
                  '### THE CLAUSE (OPEN_TRAILS :%d): a tier line reads KC when at least one kernel-verified row is load-bearing for the cluster`s thesis '
                  'as the document`s head states it; C when the rows certify definitions, arithmetic over the papers` own tuples, or placeholders that '
                  'bear no claim the thesis makes -- the rows stay kernel-verified, the tier does not follow them.' % _rl()['clause'],
                  '### THE SEAT`S READING OF "LOAD-BEARING", strikeable: the statement read at the row`s pin is a claim the head makes about the head`s '
                  'objects -- not a definition, not arithmetic over numerals or tuples the kernel`s own file defines, not a placeholder (a predicate '
                  'defined True), and not a record that names resolve.', '']
    for key, path in SYN.items():
        ls = _syn(key)
        tier_line = ls[2] if len(ls) > 2 else ''
        now = 'KC' if 'TIER KC**' in tier_line else 'C' if 'TIER C**' in tier_line else '?'
        rows = [(m.group(1), l) for l in ls for m in [KV_ROW.match(l)] if m]
        ids = [r[0] for r in rows]
        if sorted(ids) != sorted(LOADS[key]):
            sys.exit('### %s: THE KERNEL-VERIFIED ROWS %s ARE NOT THE READING`S %s -- NOTHING WRITTEN' % (key, ids, sorted(LOADS[key])))
        lb = [i for i in ids if LOADS[key][i][0]]
        read = 'KC' if lb else 'C'
        act = 'left: the tier line stands' if read == now else 're-read: %s -> %s, a one-line edition beside v0.1' % (now, read)
        if key == '2B':
            act = 'unaffected: no row reads kernel-verified, the tier C stands'
        L += ['### %s -- `%s` at PLACE-papers %s' % (key, path, g(PP, 'rev-parse', '--short=7', 'HEAD').strip()),
              '    the title: %s' % ls[0][2:], '    the head line: %s' % ls[4], '    the thesis read from the head: %s' % THESIS[key],
              '    the tier line now: TIER %s ; kernel-verified rows: %d' % (now, len(ids))]
        for i in ids:
            L.append('      %-6s %-17s -- %s' % (i, 'LOAD-BEARING' if LOADS[key][i][0] else 'not load-bearing', LOADS[key][i][1]))
        L += ['    ### THE TIER UNDER THE CLAUSE: %s (%s) -- %s' % (read, ('load-bearing: ' + ', '.join(lb)) if lb else 'no row load-bearing', act), '']
        out[key] = dict(path=path, tier_now=now, tier_read=read, kv=ids, load_bearing=lb, action=act)
    L += ['### ### **THE RE-READ: %s.**' % ' ; '.join('%s %s -> %s' % (k, v['tier_now'], v['tier_read']) for k, v in out.items())]
    put_txt('b615_reread.txt', L)
    put_json('b615_reread.json', dict(at=utc(), syntheses=out))
    print(L[-1])


def _tier_c_line(key, ncert, clause):
    return ('**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER C** — *declared 2026-10-04 (b615), under '
            '`(R225)`(2): the tier line re-read under the load-bearing clause (OPEN_TRAILS :%d) -- the %d rows read kernel-verified stay '
            'kernel-verified at their pins, each pin resolving in its clone and at its remote, and none is load-bearing for the thesis the head '
            'states: %s; each row is cited at its stated grade, the Correspondence in the back matter (`(R221)`(3)); v0.1 beside it read KC (relay '
            'data/b615_reread.txt).*' % (clause, ncert, SUMMARY_C[key]))


def edition(key, *a):
    """### PLACE-papers <synthesis>_v0_2.md, beside v0.1 (unedited), where the re-read moves the tier: the tier line, the Correspondence's
    ### placement and the version line, nothing else. Built from v0.1's blob at HEAD by line transforms; data/b615_edition_<key>.json."""
    R = jl('b615_reread.json')['syntheses'][key]
    if R['tier_read'] == R['tier_now']:
        sys.exit('### %s: THE TIER DOES NOT MOVE -- NO EDITION' % key)
    if R['tier_read'] != 'C':
        sys.exit('### %s: ONLY A KC -> C EDITION IS BUILT HERE -- NOTHING WRITTEN' % key)
    v1 = _syn(key)
    blob = g(PP, 'rev-parse', 'HEAD:' + SYN[key]).strip()
    ci = v1.index('## Correspondence')
    bi = next(i for i, l in enumerate(v1) if l.startswith('## 1. '))
    ri = v1.index('### The routes through the five tests')
    if not (ci < bi < ri) or v1[bi - 1] != '' or v1[ri - 1] != '':
        sys.exit('### %s: THE LAYOUT IS NOT THE FORM`S -- NOTHING WRITTEN' % key)
    block = v1[ci:bi]
    clause = _rl()['clause']
    tier_new = _tier_c_line(key, len(R['kv']), clause)
    ver_old = next(l for l in v1[:12] if l.startswith('*v0.1, '))
    ver_new = ('*v0.2, 2026-10-04 -- written at b615 under `(R225)`(2), beside v0.1: the tier line re-read under the load-bearing clause and the '
               'Correspondence moved to the back matter, nothing else changed; the synthesis for 2D that THE_KEYSTONE_CENSUS v0.3 names (its row R14).*')
    v2 = v1[:ci] + v1[bi:ri] + block + v1[ri:]
    v2[2] = tier_new
    v2[v2.index(ver_old)] = ver_new
    b = (NL.join(v2) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b615_edition_%s_dry.md' % key) if DRY else os.path.join(PP, *EDITION[key].split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE EDITION EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    diff = [x for x in difflib.unified_diff(v1, v2, 'v0.1', 'v0.2', lineterm='', n=0) if not x.startswith(('---', '+++', '@@'))]
    put_json('b615_edition_%s.json' % key, dict(at=utc(), path=EDITION[key], v1=SYN[key], v1_blob=blob, sha256=sha(b), bytes=len(b), lines=len(v2),
                                               moved=[ci + 1, bi], block_len=len(block), corr_at=v2.index('## Correspondence') + 1,
                                               body_at=next(i for i, l in enumerate(v2) if l.startswith('## 1. ')) + 1, tier_line=tier_new,
                                               version_line=ver_new, sorted_equal_except_two=sorted(v1) != sorted(v2)))
    print('  %s : %d lines, %d bytes, sha256 %s ; the block v0.1 :%d-:%d (%d lines) now at :%d ; diff lines %d' % (
        ('DRY ' + dest) if DRY else EDITION[key], len(v2), len(b), sha(b)[:16], ci + 1, bi, len(block), v2.index('## Correspondence') + 1, len(diff)))


# ================================================================================ COMPONENT 3: THE CLAIM BANK
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


def claims(*a):
    """### data/b615_claims_2F.txt and data/b615_claims.json: each paper's path, version and head; every claim with its line, grade and reason;
    ### the routes through the five tests; the pins and the kernel reads, the load-bearing reading; the TECHNE citation with its pointer; the
    ### cluster's arithmetic; H49a's trace table -- banked before any writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    kr = K.resolve_kernel()
    nt = K.resolve_nt()
    sieve = K.sieve_rows()
    CC = K.claims()
    if not all(ok for ok, _l in rc.values()) or not all(ok for _k, ok, _l in kr) or not all(ok for _k, ok, _l in nt):
        sys.exit('### A NEEDLE FAILS -- NOTHING WRITTEN')
    bad = [c[0] for c in K.C if not K.grade_ok(c)]
    if bad:
        sys.exit('### GRADES OUT OF RULE %s -- NOTHING WRITTEN' % bad)
    L = ['b615 -- COMPONENT 3: THE CLAIM BANK OF CLUSTER 2F, (R225)(5), banked %s before any writing' % utc(),
         '### the papers at PLACE-papers %s; the sieve v0.4 at %s' % (PRE_PP, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'A ROUTE is' in x or 'RESOLVES' in x or 'LOAD-BEARING CLAUSE' in x] + ['']
    L += ['### PART A -- THE PAPERS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        reg = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        ver = next((l.strip() for l in ls[:20] if re.search(r'v\d+\.\d|April 2026|May 2026|Working Document', l)), '')
        L.append('  %s = `%s` -- REGISTRY %s (:%d), its version %s, its status %s -- %d lines -- head :1 “%s” -- the paper`s own version/date line “%s” '
                 '-- last commit %s' % (k, path, rid, rline, reg[3], reg[5].replace('*', '')[:40], len(ls), ls[0][:120], ver[:120],
                                       g(PP, 'log', '-1', '--format=%h %ad', '--date=short', PRE_PP, '--', path).strip()))
    L += ['  lines in all: %d' % sum(len(v) for v in P.values())]
    L += ['', '### PART B -- THE CLAIMS, EACH WITH ITS LINE, NEEDLE, GRADE AND REASON (%d):' % len(CC)]
    for c in CC:
        cid, pk, n, needle, text, grade, support, reason, route = c
        nd_ = needle if 'TECHNE' not in needle else needle[:2] + '… (the TECHNE citation`s first words)'
        L.append('  %-6s %s :%-4d %-25s support %-11s -- %s' % (cid, pk, n, grade, support, text))
        L.append('         needle “%s” on the line: %s ; reason: %s%s' % (nd_[:90], rc[cid][0], reason,
                                                                     (' ; route %s %s%s' % (route[0], route[1], '' if route[2] is None else ' test %d' % route[2])) if route else ''))
    L += ['', '### PART C -- THE ROUTES, EACH THROUGH THE FIVE TESTS IN ORDER, WITH ITS VERDICT AND INSTRUMENT:']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        passed = ('tests 1-%d passed; ' % (t - 1)) if t and t > 1 else ''
        L.append('  %s -- claims %s -- %s%s -- %s, %s -- %s -- the sieve`s row %s' % (
            r, ', '.join(x[0] for x in cs), passed, 'fails test %d' % t if t else 'not asked (not a route)', v, inst, why,
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', ''))))) if row else 'none'))
    L += ['', '### PART D -- THE PINS THE PAPERS NAME, THE STATEMENTS READ THERE, THE LOAD-BEARING READING, AND THE NAMES CITED WITHOUT A PIN:']
    for k in K.PINS:
        st = K.pin_state(k)
        L.append('  %-9s %s %s -> commit %s ; at the remote: %s ; named at %s' % (k, st[1], st[2], st[3] or 'DOES NOT RESOLVE', st[4] or 'NONE', K.PINS[k][3]))
    for k, ok, l in kr:
        v = K.KREADS[k]
        L.append('  read %-8s %s :%d at %s -- needle on the line: %s -- %s' % (k, v[1], v[2], K.PINS[v[0]][1], ok, v[4]))
    for c in CC:
        if c[5] == 'kernel-verified':
            lb, kind, why = K.LOAD[c[0]]
            L.append('  load-bearing %-6s %s (%s): %s' % (c[0], 'YES' if lb else 'NO', kind, why))
    for k in K.PINS_NT:
        st = K.pin_state(k)
        L.append('  no terminal: %-6s %s %s -> commit %s ; at the remote: %s ; named at %s' % (k, st[1], st[2], st[3] or 'DOES NOT RESOLVE', st[4] or 'NONE',
                                                                                           K.PINS_NT[k][3]))
    for k, ok, l in nt:
        v = K.NTREADS[k]
        L.append('  read for the record %-9s %s :%d at %s -- needle on the line: %s -- %s' % (k, v[1], v[2], K.PINS_NT[v[0]][1], ok, v[4]))
    L.append('  the head commits` subjects: %s' % [K.commit_subject(k) for k in ('bft', 'bm')])
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('  %-44s named without a pin (%s); stands at %s %s = %s, %s :%d -- no row certifies from it' % (k, st[7], st[1], st[2], st[6], st[3], st[4]))
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '[]')
    TT = T.get('rows') if isinstance(T, dict) else T
    for nm in ('sha_bounded', 'bsd_full', 'exists_norm_completedLFunction_le_exp', 'C7_finite_type_false', 'e_difficulty', 'sieve_ceiling_semantic',
               'transversal_generic_empty', 'six_sha_frameworks', 'formation_total_seven'):
        r = [x for x in TT if str(x.get('name', '')).split('.')[-1] == nm]
        L.append('  the terminal table on %s: %s' % (nm, ['%s %s %s %s' % (x.get('repo'), x.get('name'), x.get('pin'), x.get('grade')) for x in r] or 'no row'))
    zl = K.lines_of(io.open(os.path.join(D, NODES['zeta']), encoding='utf-8').read())
    xl = K.lines_of(io.open(os.path.join(D, NODES['chi']), encoding='utf-8').read())
    names = [v[3].split()[1] for v in K.KREADS.values() if v[3].startswith('theorem ')] + list(K.UNPINNED)[:2]
    hit = [n for n in names if any(n in l for l in zl + xl)]
    L += ['  the pages: ζ list %d lines, χ list %d lines; nodes of either the three papers cite: %s' % (len(zl), len(xl), hit or 'none')]
    L += ['', '### PART E -- THE TECHNE CITATION: BT :198, carried by pointer alone -- TECHNE-Core, its tracked-file manifest sha256 %s ; no sentence '
          'of its body carried' % K.techne_pointer()]
    L += ['', '### PART F -- THE CLUSTER`S ARITHMETIC, RECOMPUTED (mpmath %s):' % __import__('mpmath').__version__]
    AR = K.arith2f()
    for lab, val, paper, ok in AR:
        L.append('  %s -- computed %s ; the paper %s ; %s' % (lab, val, paper, 'AGREES' if ok else '### DIFFERS'))
    trace = sorted(set((c[1], c[2]) for c in CC))
    L += ['', '### PART G -- H49a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    reached, matched, listed = route_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in CC)
    kvpins = sorted(set(K.PINS[c[7]][0] + ' ' + K.PINS[c[7]][1] for c in K.C if c[5] == 'kernel-verified'))
    lbrows = [c[0] for c in K.C if c[5] == 'kernel-verified' and K.LOAD[c[0]][0]]
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### THE CERTIFYING PINS: %d (%s), in %d kernels ; LOAD-BEARING ROWS: %s' % (len(kvpins), ', '.join(kvpins), len(set(x.split()[0] for x in kvpins)),
                                                                                     lbrows or 'none'),
          '### THE ROUTES: %d (%s); against the sieve: %s; with no row, listed for its next version: %s' % (
              len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                  for r, row, m, t, ok in matched) or 'none', listed or 'none')]
    put_txt(BANK, L)
    put_json('b615_claims.json', dict(at=utc(), n=len(CC), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, matched=matched, listed=listed,
                                      kvpins=kvpins, load_bearing=lbrows, pointer=K.techne_pointer(),
                                      arith=[dict(label=x[0], value=x[1], paper=x[2], agrees=x[3]) for x in AR],
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in CC]))
    print(L[-3])
    print(L[-2])
    print(L[-1])


# ================================================================================ COMPONENT 4: THE DOCUMENT
TITLE = ('# Zero Simplicity and the Formation Transfer to Elliptic Curves: the Codimension Argument, the GUE Reading, the Seven Classes at '
         'Re(s) = 1, the Shafarevich-Tate Exclusion Form and the Factorization of the BSD Formula')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional|[Uu]nique|[Ee]xact)\b')
HEADLINE = '*This document synthesises the three papers it names and certifies nothing they do not.*'
VERSION = '*v0.1, 2026-10-04 -- written at b615 under `(R225)`(5), the synthesis for 2F that THE_KEYSTONE_CENSUS v0.3 names (its row R16).*'
BM_TAG = '<!-- b615 (R225) THE v0.1 BACK MATTER, 2026-10-04 -->'
BODY1 = '## 1. The papers and their status'

BODY = [
    (BODY1, [
        'ZS states a codimension argument for simple zeros of ξ and classes zero simplicity TYPE I, while saying that neither of its two mechanisms alone settles simplicity (ZS :12, ZS :119).',
        'BT asks whether the transfer that takes RH to GRH works for L(E, s) with Hasse’s bound in place of |χ(p)|² = 1 (BT :12, BT :14), and BV is its expansion, re-graded twice so that the formation transfer is what is machine-verified while Ш-finiteness and full BSD remain open (BV :11, BV :13).']),
    ('## 2. The codimension argument', [
        'ZS splits ξ′ by mechanism class into five additive contributions and two constraints (ZS :20), defining ξ(s) as π^(−s/2) Γ(s/2) ζ(s) (ZS :18).',
        'A double zero then needs the five contributions to sum to zero, a curve in ℂ⁵ meeting a hyperplane, which ZS reads as a codimension-5 condition on one parameter (ZS :12, ZS :52).',
        'ZS cites Thom’s transversality for the curve generically missing the hyperplane (ZS :54), states that generic position is actual position in a determined system with no tunable parameters (ZS :58), and concludes from the Mechanism Theorem’s Independence that every zero is simple (ZS :60).',
        'ZS gives the codimension as 5 at its margin (ZS :64) and as 5 − 1 = 4 in its formation-framework section (ZS :106).',
        'ZS names SIDESimplicity.transversal_generic_empty, without a pin, as the compiled terminal its transversality argument stands beside (ZS :54).']),
    ('## 3. The digamma term and the numerics', [
        'ZS gives |f₃(γ₁)| ≈ 0.90 for the digamma contribution at the first zero (ZS :28), which the claim bank recomputes as 0.8996.',
        'ZS states that the digamma function has no zeros in the right half-plane (ZS :28), where ψ vanishes near 1.4616 on the positive real axis; the claim bank finds |f₃(γ)| above 0.82 on (0, 100] all the same.',
        'ZS states that at σ = 1/2 each p^(−s) lies on the unit circle and that the prime sum is absolutely convergent (ZS :26), where |p^(−s)| = p^(−1/2) there and the claim bank’s partial sums grow without bound.',
        'ZS states that ξ′(ρ) ≠ 0 is confirmed computationally for the first 10¹³ and more zeros, citing Platt (2017) (ZS :80), and reads its numerical table as consistent with the codimension argument (ZS :82).']),
    ('## 4. The GUE reading', [
        'ZS states that the Trivium’s quarter-twist T has T² = −I (ZS :88) and tabulates Dyson’s three ensembles with T² = −I assigned to GUE (ZS :93), where in Dyson’s classification β = 2 belongs to systems without an antiunitary time reversal.',
        'ZS reports var/mean² = 0.189 for a perturbed Trivium matrix against GUE’s 0.178 (ZS :96), and states that level repulsion at β = 2 gives a double zero probability zero (ZS :98).',
        'ZS cites Montgomery’s pair-correlation conjecture and Odlyzko’s computations for the match with GUE (ZS :100), and lists the GUE argument as its second mechanism (ZS :117).']),
    ('## 5. The transfer to L(E, s)', [
        'BT states the functional equation Λ(E, s) = w_E Λ(E, 2 − s) with critical line Re(s) = 1 (BT :37) and cites Hasse’s theorem |a_p| ≤ 2√p (BT :41).',
        'BT computes the balance for L(E, s), |α_p p^(−s)| = p^(1/2 − σ) meeting its reflection at σ = 1 (BT :105), and places Hasse’s bound at C₄ (BT :107), coupled to C₅ through modularity (BT :127).',
        'BT states that all seven classes transfer (BT :171), and BV that they transfer four unconditionally and three through the Hasse bound, the formation (2, 3, 2, 0) = 7 kept (BV :19).',
        'Root number −1 forces a zero at s = 1, the parity phenomenon BT reads as a bonus of the reality class (BT :71).',
        'BV’s four-stage table counts three Ostrowski places, ∞, p-adic and global (BV :127), where Ostrowski’s theorem gives the archimedean place and one p-adic place for each prime.',
        'BV cites a growth terminal for the completed Dirichlet L-function at SIDE-lv-conservation v0.5.0 and a compiled negative for the finite-type form of C₇ at v0.5.1 (BV :145).']),
    ('## 6. The Shafarevich-Tate exclusion form', [
        'BV’s Chapter 1 heads Ш-finiteness and the rank equality as theorems (BV :33, BV :37), and its own markers scope both as open, the squares closing argument-forms under the premise h2 (BV :207, BV :263).',
        'BV argues Ш finite by SIDE Exclusion over six frameworks, each bounding and none producing growth (BV :198), and the compiled form, BSD.sha_bounded at SIDE-effects c66f3c5, certifies each framework through a := True placeholder (BV :213, BV :64).',
        'BV names six_sha_frameworks of SIDE-bsd-multiplicity as a count of the six frameworks that bounds nothing (BV :213).']),
    ('## 7. The rank equality', [
        'BV states that four candidate mismatches exhaust the sites where rank and analytic order could decouple (BV :250), and bsd_full at c66f3c5 certifies each through a placeholder BV names excluded (BV :267), which the file names mismatch_absent.',
        'BV gives rank two and above as a formation-transfer and placement result under h2, full rank equality open (BV :279), the SIDE analysis being rank-independent (BV :273).',
        'BV’s Chapter 7 prints the namespace with names the file at c66f3c5 does not carry (BV :329), and gives its toolchain as v4.29.0-rc8 (BV :374).']),
    ('## 8. The factorization of the BSD formula', [
        'BT traces the period to C₁, the regulator to C₂, |Ш| to C₄ and the Tamagawa product to C₅ (BT :203), and calls the formula a product of seven contributions, an observation it calls new (BT :210).',
        'BV reads the formula’s right side as factoring by mechanism class (BV :291), adds the torsion at C₃ or C₆ (BV :303), and states that verifying BSD for a curve admits a factor-by-factor decomposition (BV :313).']),
    ('## 9. The compiled pieces the papers name', [
        'BV states that the SIDE Exclusion form is machine-checked with := True placeholders, settling neither Ш-finiteness nor rank equality (BV :57), the theorems retired from the tree head and cited at their pin (BV :64).',
        'BV states that at SIDE-kernel v1.4 e_difficulty reads its system and extracts the Ostrowski, a statement over an abstract system naming no L-function, and reads the location and multiplicity classification as kernel-certified at the structural level (BV :169).',
        'BV’s era annotation records both paired kernels relabelled as placement scaffolding at their head commits 3491766 and d77ce30 (BV :472), and BV states that their machine-verified content is the formation transfer (BV :19).']),
    ('## 10. The routes the papers offer', [
        'ZS offers the codimension argument (ZS :60) and the GUE argument (ZS :98) toward simplicity, and the computed range of zeros as consistency (ZS :80).',
        'BT and BV offer the transfer of the seven classes’ argument for ξ to Λ(E, s), every nontrivial zero on Re(s) = 1 (BT :173, BT :179), BV under the open premise h2 (BV :159).']),
    ('## 11. What the papers leave open', [
        'BT states that the transfer addresses location and not the multiplicity at s = 1 (BT :183), the remaining content of BSD (BT :190).',
        'BV states that the consequence for Λ(E, s) rests on h2 and is not an independent unconditional result (BV :161), and that neither Clay problem is settled in it (BV :476).',
        'BT names a tool of a private library for the multiplicity question, carried here by pointer alone (BT :198).']),
]
TRACE_RE = re.compile(r'\b(ZS|BT|BV) :(\d+)')


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    lb = [c for c in cert if K.LOAD[c[0]][0]]
    return ('KC' if lb else 'C'), len(cert), [c[0] for c in lb]


def _tier_line(tier, cert_rows):
    kvp = jl('b615_claims.json')['kvpins']
    cl = _rl()['clause']
    by = {}
    for c in K.C:
        if c[5] == 'kernel-verified':
            by.setdefault(c[7], []).append(c[0])
    return ('**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-04 (b615), under '
            '`(R225)`(5): the tier the rows earn, read under the load-bearing clause (OPEN_TRAILS :%d) after the rows were graded -- %d rows read '
            'kernel-verified at %d pins in %d kernels, each pin resolving in its clone and at its remote, and none is load-bearing for the thesis '
            'the head states: %d certify the Shafarevich-Tate and rank exclusion forms over := True placeholders at SIDE-effects c66f3c5, %d state '
            'growth bounds for the completed Dirichlet L-function and the completed ζ at SIDE-lv-conservation v0.5.0 and v0.5.1, not for Λ(E, s), '
            'and %d, at SIDE-kernel v1.4, states an equivalence over an abstract system naming no L-function; the rows stay kernel-verified and the '
            'tier does not follow them; each row is cited at its stated grade, the Correspondence in the back matter (`(R221)`(3)).*' % (
                tier, cl, cert_rows, len(kvp), len(set(x.split()[0] for x in kvp)), len(by.get('effects', [])),
                len(by.get('lv050', [])) + len(by.get('lv051', [])), len(by.get('k14', []))))


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | paper | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(P[k][0].lstrip('# ').strip()), _cell(st[5]).replace('*', '')[:40]))
    return [TITLE, '', _tier_line(tier, cert_rows), '', HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for cluster 2F (THE_KEYSTONE_CENSUS v0.3, its row R16 and §2): the three papers REGISTRY '
            'files as p2-6, p2-11 and p2-29, each claim listed with the grade its own text supports; for a reader who meets those papers and needs what '
            'each states and what backs it.*', '',
            '**The papers, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** BSD_TRANSFER (BT) is the predecessor of BSD_VIA_FORMATION_TRANSFER (BV), both retained by REGISTRY’s '
            'multiple-keystones ruling; BT names TECHNE once, and this document carries that citation by pointer alone and no sentence of it. The '
            'grades are `(R19)`’s vocabulary as `(R220)`(5) lists it; a row reads kernel-verified only where its paper names the terminal at a pin, '
            'and the statement there is quoted in the row; cite the synthesis for orientation and each row at its stated grade.', '']


def _corr(CC):
    S = ['## Correspondence', '',
         '*Every claim of the three papers this document carries, with the grade the paper’s own text supports. A route is read through the sieve’s '
         'five tests in order; the routes and their instruments are below.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in CC:
        cid, pk, n, _needle, text, grade, _support, reason, route = c
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(reason), rcell))
    return S + ['']


def _back(CC, tier):
    sieve = K.sieve_rows()
    cl = _rl()['clause']
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-04 by b615 under the author’s ruling `(R225)`(5), by the synthesis form of `(R220)`(5), '
         '`(R221)`(3) and `(R225)`(2)', '',
         '### The grading rule, confirmed by `(R222)`(1)', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A pin resolves when its commit is in the clone and at the remote (`(R223)`(1)).',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.',
         '- The tier reads KC when at least one kernel-verified row is load-bearing for the thesis the head states, and C otherwise, the rows staying '
         'kernel-verified (OPEN_TRAILS :%d).' % cl, '']
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
    B += ['', '### The certifying rows under the load-bearing clause', '', '| row | load-bearing | why |', '|:--|:--|:--|']
    for c in K.C:
        if c[5] == 'kernel-verified':
            lb, _kind, why = K.LOAD[c[0]]
            B.append('| %s | %s | %s |' % (c[0], 'yes' if lb else 'no', _cell(why)))
    B += ['', '### The pins named without a terminal', '', '| as cited | its resolution | where the paper names it | what stands there |', '|:--|:--|:--|:--|']
    nts = {v[0]: v for v in K.NTREADS.values()}
    for k in K.PINS_NT:
        st = K.pin_state(k)
        what = ('`%s` :%d, %s; the commit’s subject: %s' % (nts[k][1], nts[k][2], nts[k][4], K.commit_subject(k))) if k in nts else 'a reference, no terminal named'
        B.append('| %s %s | commit `%s`, %s | %s | %s |' % (st[1], st[2], st[3], st[4] or 'NOT AT THE REMOTE', K.PINS_NT[k][3], _cell(what)))
    B += ['', '### Names cited without a pin', '', '| name | where the paper names it | where it stands |', '|:--|:--|:--|']
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        B.append('| %s | %s | %s %s = %s, `%s` :%d |' % (k, st[7], st[1], st[2], st[6], st[3], st[4]))
    B += ['', '### The TECHNE citation', '',
          '- BT :198 names a tool of a private library; this document carries it by pointer alone: TECHNE-Core, the sha256 of its tracked-file manifest, '
          '`%s`. No sentence of its body is carried.' % K.techne_pointer(), '']
    B += ['### The arithmetic the rows cite, recomputed in the claim bank', '', '| what | computed | the paper | agrees |', '|:--|:--|:--|:--|']
    for x in jl('b615_claims.json')['arith']:
        B.append('| %s | %s | %s | %s |' % (_cell(x['label']), _cell(x['value'][:400]), _cell(x['paper']), 'yes' if x['agrees'] else 'no'))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b615 |' % DOC]
    for k, (path, rid, _rl_) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R16 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/%s` | banked before this document |' % BANK, '',
          '### Version history', '',
          '- **v0.1, 2026-10-04 (b615, `(R225)`(5))**: the synthesis of p2-6, p2-11 and p2-29, %d claims graded, the routes read through the five '
          'tests, the tier read under the load-bearing clause.' % len(CC), '']
    return B


def doc(*a):
    """### PLACE-papers phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md (created) and data/b615_doc.json; `dry`:
    ### the scratchpad. Needs the claim bank and the record lines first."""
    if not os.path.exists(_p('b615_claims.json')):
        sys.exit('### THE CLAIM BANK IS NOT BANKED -- NOTHING WRITTEN')
    CC = K.claims()
    tier, ncert, lb = _tier()
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
    dest = os.path.join(SP, 'b615_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b615_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert, load_bearing=lb,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(CC)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows, load-bearing %s) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, lb or 'none', corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b615_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b615_doc_termscan.txt', t.rstrip(NL).split(NL))


def h49a(ls, J):
    trace = set((p, n) for p, n in jl('b615_claims.json')['trace'])
    body = [l for l in ls[J['body_at'] - 1:J['body_end']] if l.strip() and not l.startswith('#')]
    sents = [s for l in body for s in _segs(l)]
    bad = []
    for s in sents:
        tr = [(m.group(1), int(m.group(2))) for m in TRACE_RE.finditer(s)]
        if not tr or any(x not in trace for x in tr):
            bad.append(s[:120])
    return not bad, len(sents), bad


def corr_rows(ls):
    """### the Correspondence's claim rows alone: from its heading to the next heading (the load-bearing table carries row ids too)"""
    if '## Correspondence' not in ls:
        return []
    i = ls.index('## Correspondence') + 1
    j = next((k for k in range(i, len(ls)) if ls[k].startswith('#')), len(ls))
    return [l for l in ls[i:j] if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]


def h49c_check(tier_line):
    """### C or KC; KC with a load-bearing certifying row named, C with none load-bearing and the clause cited; every certifying pin resolving
    ### with its statements standing"""
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    lb = [c[0] for c in kv if K.LOAD[c[0]][0]]
    pins_ok = all(K.grade_ok(c) for c in kv)
    if lb:
        return 'TIER KC**' in tier_line and any(x in tier_line for x in lb) and pins_ok
    return 'TIER C**' in tier_line and 'none is load-bearing' in tier_line and 'load-bearing clause (OPEN_TRAILS :' in tier_line and pins_ok


def doc_bank(*a):
    """### data/b615_doc_bank.txt and data/b615_h49.json: the title's property words, H49a-H49d, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b615_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b615_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h49a(ls, J)
    rows = corr_rows(ls)
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h49b = 'HOLDS' if len(rows) >= 12 and not over and len(rows) == len(K.C) else 'REFUTED'
    hits, sizes = nd_hits(NL.join(ls))
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    h49c = 'HOLDS' if h49c_check(tier_line) else 'REFUTED'
    h49d = 'HOLDS' if not any(hits.values()) and all(v > 0 for v in sizes.values()) else 'REFUTED'
    pointer_ok = K.techne_pointer() in NL.join(ls)
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    CJ = jl('b615_claims.json')
    L = ['b615 -- COMPONENT 4: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified, load-bearing %s; the line: %s' % (J['tier'], J['cert_rows'], J['load_bearing'] or 'none', tier_line[:900]),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'in the back matter, after the body (C)' if placed and J['tier'] == 'C'
                                                                                          else 'after the front matter (KC)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s ; THE VERSION LINE: %s ; THE TECHNE POINTER: %s' % (HEADLINE in ls[:12], VERSION in ls[:12], pointer_ok),
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM over this document, the needles read locally and never printed: the method document %d needles, %d hits ; the '
         'tree %d, %d ; every module document %d, %d' % (sizes['method'], hits['method'], sizes['tree'], hits['tree'], sizes['modules'], hits['modules']),
         '### H49a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H49a %s** -- every body sentence traces by path and line to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H49b %s** -- the Correspondence carries %d rows (at least twelve), none graded above its paper`s named backing (%s)' % (h49b, len(rows), over or 'none'),
         '### ### **H49c %s** -- the tier line reads %s, %s, every certifying pin resolving with its statements standing' % (
             h49c, J['tier'], ('load-bearing rows named: ' + ', '.join(J['load_bearing'])) if J['load_bearing'] else 'no certifying row load-bearing and the clause cited'),
         '### ### **H49d %s** -- the no-disclosure arm reads %d hits over %d + %d + %d needles' % (h49d, sum(hits.values()), sizes['method'], sizes['tree'], sizes['modules']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and h49c == 'HOLDS' and placed and pointer_ok and h49d == 'HOLDS'
         else '### ### **HELD.**']
    put_txt('b615_doc_bank.txt', L)
    put_json('b615_h49.json', dict(H49a='HOLDS' if a_ok else 'REFUTED', H49b=h49b, H49c=h49c, H49d=h49d, sentences=n_sent, untraced=a_bad, rows=len(rows),
                                   over=over, clean=clean, ceiling=len(ceiling), title_props=title_props, nd_hits=hits, nd_sizes=sizes, placed=placed,
                                   tier=J['tier'], pointer=pointer_ok, routes=CJ['routes']))
    for l in L[-6:]:
        print(l)


# ================================================================================ COMPONENT 6: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b615_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b615_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b615_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b615 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b615_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b615_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 7: THE SCORES AND THE RECORD
HKEYS = ('H49a', 'H49b', 'H49c', 'H49d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + tuple(PAPERS_2D.values()) + tuple(SYN.values()) + (
    CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md', 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', K.SIEVE)
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the seat's expectation, registered on the face


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _n4():
    p = _p('b615_lsr_after_edit.json')
    if not os.path.exists(p):
        return ('NOT SCORABLE', 'the suite has not run after the edit')
    X = jl('b615_lsr_after_edit.json')
    lsr = X.get('lsr') or {}
    att = []
    for n in ('b615_lsr_after_edit_attempt1.json', 'b615_lsr_after_edit_attempt2.json'):
        if os.path.exists(_p(n)):
            att.append('%s %s' % (n, jl(n).get('lsr')))
    return ('HELD' if lsr and all(v <= 1 for v in lsr.values()) else 'REFUTED',
            'the run after the edit (relay data/b615_checks_after_edit.txt) made ls-remote calls per repository %s, at most %d; the runs kept '
            'beside it: %s -- the second a transient network failure, each failed read retried once alone as the standing line orders, the claim '
            'tested directly and the suite re-run alone' % (lsr, max(lsr.values()) if lsr else 0, '; '.join(att) or 'none'))


def _ed_ok(key):
    p = _p('b615_edition_%s.json' % key)
    if not os.path.exists(p):
        return False, 'not written'
    E = jl('b615_edition_%s.json' % key)
    v1 = K.lines_of(g(PP, 'show', '%s:%s' % (PRE_PP, SYN[key])))
    disk = os.path.join(PP, *E['path'].split('/'))
    v2 = K.lines_of(io.open(disk, encoding='utf-8').read().replace(chr(13), '')) if os.path.exists(disk) else []
    rest1 = [l for i, l in enumerate(v1) if i != 2 and not l.startswith('*v0.1, ')]
    rest2 = [l for i, l in enumerate(v2) if i != 2 and not l.startswith('*v0.2, ')]
    same_multiset = sorted(rest1) == sorted(rest2)
    ci, ri = v2.index('## Correspondence') if '## Correspondence' in v2 else -1, v2.index('### The routes through the five tests') if '### The routes through the five tests' in v2 else -1
    bm = next((i for i, l in enumerate(v2) if l.startswith('## Back matter')), 10 ** 9)
    ok = same_multiset and bm < ci < ri and 'TIER C**' in v2[2] and v2[6].startswith('*v0.2, ') and sha((NL.join(v2) + NL).encode('utf-8')) == E['sha256']
    return ok, 'every v0.1 line but the tier and version lines carried: %s ; the Correspondence at :%d, after the back matter`s head :%d and before the routes :%d' % (
        same_multiset, ci + 1, bm + 1, ri + 1)


def scores(*a):
    H, CJ, J = jl('b615_h49.json'), jl('b615_claims.json'), jl('b615_doc.json')
    RR = jl('b615_reread.json')['syntheses']
    Z, X = jl('b615_page_zeta.json'), jl('b615_page_chi.json')
    face = jl('b615_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    eds = [EDITION[k] for k, v in RR.items() if v['tier_read'] != v['tier_now'] and k != '2B']
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', DOC] + eds + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b615_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b614_closing_push_out.txt'))
    rc = K.resolve_claims()
    kr = K.resolve_kernel()
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    pins = {k: K.pin_state(k) for k in K.PINS}
    arms2 = rd('b615_page_arms_c2.txt')
    reached = [r for r in CJ['routes']]
    true_routes = [r for r in reached if r in [m[0] for m in CJ['matched'] if not m[2].startswith('NOT A ROUTE')]]
    ed_ok, ed_why = _ed_ok('2D')
    S = {
        'H49a': (H['H49a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H49b': (H['H49b'], 'Correspondence rows %d (the floor 12), graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H49c': (H['H49c'], 'the tier line reads %s, %d certifying rows, load-bearing %s; every certifying pin resolves in its clone and at its remote: %s' % (
            H['tier'], J['cert_rows'], J['load_bearing'] or 'none', all(bool(pins[c[7]][3]) and bool(pins[c[7]][4]) for c in kv))),
        'H49d': (H['H49d'], 'the no-disclosure arm over the document: %s hits over %s needles' % (H['nd_hits'], H['nd_sizes'])),
        'N1': ('HELD' if RR['2D']['tier_read'] == 'C' and RR['1.2']['tier_read'] == 'KC' and RR['1.5E']['tier_read'] == 'KC' else 'REFUTED',
               'under the clause 2D reads %s (was %s), 1.2 %s, 1.5E %s, 2B %s (relay data/b615_reread.txt)' % (
                   RR['2D']['tier_read'], RR['2D']['tier_now'], RR['1.2']['tier_read'], RR['1.5E']['tier_read'], RR['2B']['tier_read'])),
        'N2': ('HELD' if CJ['n'] >= 30 and len(true_routes) >= 1 else 'REFUTED', '%d claims (the floor 30) ; route rows %d (%s), of which routes read '
                                                                                 'through the tests %d (%s)' % (CJ['n'], len(reached), ', '.join(reached), len(true_routes),
                                                                                                                ', '.join(true_routes))),
        'N3': ('HELD' if H['H49d'] == 'HOLDS' else 'REFUTED', 'the no-disclosure arm: %s hits' % sum(H['nd_hits'].values())),
        'N4': _n4(),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the papers of 2F and 2D, the four syntheses` current versions, the census, REGISTRY, '
               'SPIRAL_MAP, the taxonomy and the sieve unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools and the table %s' % (
                   kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if all(p[3] and p[4] for p in pins.values()) and all(ok for _k, ok, _l in kr) and len(kv) == 7 and not J['load_bearing'] else 'REFUTED',
               'the certifying pins resolving %d of %d ; the kernel reads standing %d of %d ; rows kernel-verified %d ; load-bearing %s' % (
                   sum(1 for p in pins.values() if p[3] and p[4]), len(pins), sum(ok for _k, ok, _l in kr), len(kr), len(kv), J['load_bearing'] or 'none')),
        'S3': ('HELD' if ed_ok else 'REFUTED', '2D`s v0.2: %s' % ed_why),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b615_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:240]))


def _title():
    J, CJ = jl('b615_doc.json'), jl('b615_claims.json')
    return ('## The 2F synthesis: zero simplicity and the formation transfer to elliptic curves at v0.1 from p2-6, p2-11 and p2-29, %d claims '
            'graded, %d routes read, tier %s; the KC tier’s load-bearing clause and the re-read of four tier lines; the 2D papers’ findings and two '
            'errata' % (J['rows'], len(CJ['routes']), J['tier']))


TRAIL_HEAD = ('### b615 — lane three, act forty-two under (R225): the synthesis for 2F; the KC tier’s load-bearing clause and the re-read of the '
              'earlier tier lines; the 2D papers’ findings and two errata; the suite’s remote reads one per run')
FOR_AUTHOR = (
    '(1) the 2F papers’ findings, for their next editions: ZERO_SIMPLICITY :18 defines ξ(s) as π^(−s/2) Γ(s/2) ζ(s), without the factor s(s − 1)/2 '
    'that makes ξ entire, while :30 uses the Hadamard product of the entire ξ; :26 puts each p^(−s) on the unit circle at σ = 1/2, where its '
    'modulus is p^(−1/2), and calls the prime sum absolutely convergent there, where its partial sums grow without bound; :28 says the digamma '
    'function has no zeros in the right half-plane, where ψ vanishes near 1.4616 (its conclusion, |f₃| bounded away from zero, stands on other '
    'grounds in the claim bank); :93 assigns T² = −I to GUE, where in Dyson’s classification β = 2 is the class with no antiunitary time '
    'reversal and T² = −1 gives β = 4; :64 gives codimension 5 and :106 gives 5 − 1 = 4 for the same condition; :80 attributes 10¹³ and more zeros '
    'to Platt (2017), the literature to be read at its edition; BSD_TRANSFER :210 calls the formula a product of seven contributions where its own '
    ':203-:206 lists four; BSD_VIA_FORMATION_TRANSFER :64 and :267 name the placeholder excluded where SIDE-effects c66f3c5 names it '
    'mismatch_absent, its Chapter 7 listing (:325-:370) does not match that file, and :374 gives the toolchain v4.29.0-rc8 where the kernel at '
    'c66f3c5 names v4.30.0-rc2; :127 counts three Ostrowski places, as MATTER_AS_ARITHMETIC :99 did; (2) b614’s own trail record prints its '
    'For-the-author percentages as 40%%, 41.6%% and 100%% with a doubled percent sign (OPEN_TRAILS, its record), a formatting slip of b614’s record '
    'tool, its sense unchanged; (3) the load-bearing reading is the seat’s, strikeable: a row is load-bearing when the statement read at its pin '
    'is a claim the head makes about the head’s objects, not a definition, not arithmetic over the kernel’s own tuples, not a placeholder, not a '
    'record that names resolve')


def _finding_text():
    S, J, CJ = jl('b615_scores.json'), jl('b615_doc.json'), jl('b615_claims.json')
    rl, ej = _rl(), jl('b615_errata.json')
    RR = jl('b615_reread.json')['syntheses']
    dc = _pp_commit('b615 (R225)(5): ' + DOC)
    ec = _pp_commit('b615 (R225)(2): ' + EDITION['2D'])
    erc = _pp_commit('b615 (R225)(3): ERRATA')
    t = _title()
    gr = CJ['grades']
    e = ['', t, '',
         '*Filed at b615 on the author’s ruling `(R225)`. Banks: relay `data/b615_reads.txt`, `data/%s`, `data/b615_arith.txt`, `data/b615_reread.txt`, '
         '`data/b615_doc_bank.txt`, `data/b615_checks_after_edit.txt`, `data/b615_page_arms_c2.txt`. Nothing deposits.*' % BANK, '',
         '**The document** (`(R225)`(5)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the three papers REGISTRY files as p2-6, '
         'p2-11 and p2-29 read whole at %s, %d claims each restated in one sentence and graded by its paper’s own text -- kernel-verified %d, '
         'theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d. Tier %s under the '
         'load-bearing clause: the kernel-verified rows sit at %d pins in %d kernels, each resolving in its clone and at its remote -- the '
         'Shafarevich-Tate and rank exclusion forms over := True placeholders at SIDE-effects c66f3c5, growth bounds for the completed Dirichlet '
         'L-function and the completed ζ at SIDE-lv-conservation v0.5.0 and v0.5.1, and an equivalence over an abstract system at SIDE-kernel v1.4 '
         '-- and none is load-bearing for the thesis the head states; the Correspondence in the back matter (`(R221)`(3)). BSD_TRANSFER’s one TECHNE '
         'citation is carried by pointer alone, the no-disclosure arm at 0 hits.' % (
             DOC, dc, PRE_PP, CJ['n'], gr.get('kernel-verified', 0), gr.get('theorem-supported', 0), gr.get('argument-supported', 0),
             gr.get('computationally-verified', 0), gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), J['tier'], len(CJ['kvpins']),
             len(set(x.split()[0] for x in CJ['kvpins']))), '',
         '**The routes** (the five tests). %d route rows: ZERO_SIMPLICITY’s codimension argument toward simplicity, DARK by test 2 (RH-60, the '
         'mechanism enumeration at multiplicity); its GUE argument, DARK by test 1 (RH-59); the transfer of the seven classes’ argument to Λ(E, s) in '
         'BSD_TRANSFER and BSD_VIA_FORMATION_TRANSFER, DARK by test 2 (RH-60); and the computed range of zeros, NOT A ROUTE (RH-58) -- each verdict '
         'matching the sieve’s row.' % len(CJ['routes']), '',
         '**The load-bearing clause and the re-read** (`(R225)`(2)). The clause entered beneath the form’s clauses at OPEN_TRAILS :%d; the four '
         'earlier tier lines re-read under it (relay data/b615_reread.txt): 1.2 %s, 1.5E %s, 2B %s, 2D %s -> %s, its v0.2 written beside v0.1 at '
         'PLACE-papers `%s` (commit %s), the tier line, the Correspondence’s placement and the version line changed and nothing else.' % (
             rl['clause'], RR['1.2']['tier_read'], RR['1.5E']['tier_read'], RR['2B']['tier_read'], RR['2D']['tier_now'], RR['2D']['tier_read'],
             EDITION['2D'], ec), '',
         '**The record lines.** b614’s weight at FINDINGS :%d; the mirror’s figures at OPEN_TRAILS :%d; the 2D papers’ findings at :%d, two of them '
         'ERRATA %s (:%d) and %s (:%d), committed alone at %s, the computations at relay data/b615_arith.txt; the remote-reads standing line at '
         ':%d.' % (rl['weight'], rl['mirror'], rl['fact'], ej['entries'][0]['id'], ej['entries'][0]['line'], ej['entries'][1]['id'],
                   ej['entries'][1]['line'], erc, rl['standing']), '',
         '**The suite’s remote reads** (`(R225)`(4)). The suite edited after its seal through the Edit tool and committed alone in relay, beside '
         'a commit of the suite as it stood: every remote pin resolved from one ls-remote read per repository per run, a failed read retried once '
         'alone. The run after the edit made %s ls-remote call per repository at most (relay data/b615_checks_after_edit.txt and its ls-remote '
         'bank, against 50 to one repository at the prerun); two runs are kept beside it -- the first found two positive controls of the sealed '
         'suite passing, defect (a), repaired through the Edit tool; the second met a transient network failure, each failed read retried once '
         'alone, the claim tested directly and the suite re-run alone.' % ('one' if S['N4'][0] == 'HELD' else 'more than one'), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R16 (FINDINGS :7212, b610’s §2) and follows the form '
         'of b611’s, b612’s, b613’s and b614’s syntheses (:7240, :7260, :7280, :7300); its routes meet b609’s sieve rows RH-58, RH-59 and RH-60 '
         '(:7186), as the earlier syntheses’ did; the load-bearing clause re-reads b614’s tier line and leaves b611’s and b612’s standing; its '
         'placeholder rows read the same SIDE-effects pin as b614’s Yang-Mills rows. It strengthens the programme’s offering of the formation '
         'transfer: three papers now have one place where each claim stands at its own grade, the kernel anchors are read at their pins and named '
         'for what they certify, and a tier line no longer follows a row that bears no claim of its thesis.', '',
         '**Next.** Per `(R225)`(6): b616, the synthesis for 2G, the sequence’s last. The author rules on the closing.', '',
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
    put_json('b615_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl, ej = jl('b615_scores.json'), jl('b615_findings.json'), _rl(), jl('b615_errata.json')
    rows_ = ['', TRAIL_HEAD, '',
             '**(R225) ratified.** (1) b614 at its weight, the mirror’s figures entered. (2) The KC tier’s load-bearing clause; 2D’s tier line re-read '
             'at v0.2, 1.2’s and 1.5E’s re-read and left, 2B unaffected. (3) The 2D papers’ findings, two as errata. (4) The suite’s remote reads one '
             'per run, standing. (5) The synthesis for 2F; H49a-H49d. (6) The act after: b616.', '',
             '**Entered:** FINDINGS.md:%d (b614’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the mirror’s figures, '
             'addressed to b614’s record :12675), :%d (the load-bearing clause, addressed to the form’s clauses :12601), :%d (the 2D fact items, '
             'addressed to b614’s record :12675), :%d (the remote-reads standing line, addressed to :12188); ERRATA %s (:%d), %s (:%d); this record; '
             'PLACE-papers `%s` and `%s`; relay data/%s, data/b615_arith.txt, data/b615_reread.txt.' % (
                 rl['weight'], fj['entry_line'], rl['mirror'], rl['clause'], rl['fact'], rl['standing'], ej['entries'][0]['id'], ej['entries'][0]['line'],
                 ej['entries'][1]['id'], ej['entries'][1]['line'], DOC, EDITION['2D'], BANK), '',
             '**Resolved by the seat, for the author’s strike:** the load-bearing reading of each certifying row (relay data/b615_reread.txt and the '
             'claim bank’s Part D); 2D’s v0.2 by the ruling’s letter, its back matter’s Placement and Version history carried from v0.1 unedited; the '
             'transfer to Λ(E, s) read as a route and matched to RH-60, the mechanism enumeration transferred; the computed range read NOT A ROUTE '
             'at RH-58; the 137-to-337 stretch of PRIME_ORDER :17 entered in its erratum beside the ruling’s named stretch, the seat’s computation; '
             'the suite edit committed alone in relay after a commit of the suite as it stood, so the edit’s diff stands in the record. No prompt was '
             'put (relay data/b615_author_answers.txt).', '',
             '**For the author:** %s.' % FOR_AUTHOR, '',
             '**b616 priced** (the sequence’s form: each act prices the next): the census row R17, 2G, nine REGISTRY rows -- seven papers in '
             'phase2/physics-speculative, 1,611 lines (SYMMETRY_FILTER, LOCAL_COSMIC, T7_CMB, QUATERNIONIC, DARK_DELTA_MU, FORMATION_DISTANCE, '
             'THEORY_SPACE), and two simulators, qec_kappa_infrastructure.py and qec_kappa_v2.py, 449 lines -- read whole at address; one act, no '
             'Lean call; the tier read from the rows under the load-bearing clause; QUATERNIONIC names TECHNE once, carried by pointer; the '
             'sequence’s last, the author ruling on the closing.', '',
             '**Defects** (relay data/b615_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**A transient network failure, kept:** the second run after the suite edit read three repositories’ remotes as empty, each read '
             'retried once alone as the standing line orders; tested directly, all three answer by ls-remote, and the suite was re-run alone '
             '(relay data/b615_checks_after_edit_attempt2.txt beside data/b615_checks_after_edit.txt).', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R225)`(6), b616, the synthesis for 2G, the sequence’s last; the author rules on the closing.', '',
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
    put_json('b615_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b615_trail.json')['line'])


def desk(*a):
    S = jl('b615_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b615 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H49a-H49d, (R225)(5).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H49 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b615_defects.txt').rstrip(NL).split(NL)
    put_txt('b615_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, ej = jl('b615_scores.json'), jl('b615_findings.json'), jl('b615_trail.json'), _rl(), jl('b615_errata.json')
    Z, X = jl('b615_page_zeta.json'), jl('b615_page_chi.json')
    RR = jl('b615_reread.json')['syntheses']
    L = ['b615 -- THE COMPONENTS, BANKED UNDER (R225).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b614`s closing push-out relay %s ; push-b614* branches deleted by name '
         '(data/b615_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b615_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b614`s weight FINDINGS :%d ; the mirror`s figures OPEN_TRAILS :%d ; the load-bearing clause :%d ; the 2D fact items :%d ; '
         'the standing line :%d ; ERRATA %s :%d, %s :%d ; the arithmetic data/b615_arith.txt' % (rl['weight'], rl['mirror'], rl['clause'], rl['fact'],
                                                                                             rl['standing'], ej['entries'][0]['id'], ej['entries'][0]['line'],
                                                                                             ej['entries'][1]['id'], ej['entries'][1]['line']),
         '### COMPONENT 2 : the re-read data/b615_reread.txt -- %s ; 2D`s v0.2 %s' % (' ; '.join('%s %s -> %s' % (k, v['tier_now'], v['tier_read'])
                                                                                            for k, v in RR.items()), EDITION['2D']),
         '### COMPONENT 3 : the claim bank data/%s ; routes %s' % (BANK, ', '.join(jl('b615_claims.json')['routes'])),
         '### COMPONENT 4 : the document %s ; data/b615_doc_bank.txt ; H49a %s, H49b %s, H49c %s, H49d %s' % (DOC, S['H49a'][0], S['H49b'][0], S['H49c'][0], S['H49d'][0]),
         '### COMPONENT 5 : the suite edit, committed alone in relay ; data/b615_checks_after_edit.txt ; N4 %s' % S['N4'][0],
         '### COMPONENT 6 : the ζ page changed %s, the χ page changed %s ; page arms data/b615_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 7 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b616 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b615_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b615_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
