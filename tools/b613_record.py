# -*- coding: utf-8 -*-
"""b613_record.py -- THE ACT'S RECORD TOOL, UNDER (R223). ### ONE SUBCOMMAND PER BANK.

### ### b613: LANE THREE, ACT FORTY -- THE SYNTHESIS FOR CLUSTER 2B: ONE DOCUMENT FROM THE CLUSTER'S SIX PAPERS READ AT ADDRESS, EVERY
### CLAIM GRADED, THE ROUTES READ, THE NO-DISCLOSURE ARM BEARING; THE 1.5E PAPERS' FINDINGS ENTERED, TWO OF THEM AS ERRATA.
### Subcommands write only `data/b613_*` unless the docstring names another file; `dry` on the command line routes every b613 bank and the
### document to the seat's scratchpad (for `findings`, `trail`, `record_lines` and `errata`, `dry` prints and appends nothing). Banks are
### written by encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`; ERRATA appends through
### tools/errata_append.py, which refuses a used id before it writes. TECHNE-Core's module documents are read locally for the
### no-disclosure needles and never printed; the act's public text carries TECHNE by pointer alone. No platform call. No Lean call. The
### template is tools/b612_record.py.
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
import b613_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = '3b92db0d'
STEPZERO = '3f4e8c85'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/8f2ff82c-2889-4443-a8e7-85de4d1b215f/scratchpad'
SESSION_ID = '8f2ff82c-2889-4443-a8e7-85de4d1b215f'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md'
B612_DOC = 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
MONO = 'outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md'
METHOD_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
BANK = 'b613_claims_2B.txt'
ERR_IDS = ('E-2026-10-04-1', 'E-2026-10-04-2')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines', 'errata')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b613_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b613_') else '', name, len(b)))
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
    '(a) THE SEAT`S, IN THE SUITE, FOUND AT THE PRE-PUSH RUN: G-DOC-TRACES` positive control deleted the trace (SE :29) from a body '
    'sentence that also carries (SE :25), so the mutated sentence still traced and the positive control passed; the harness marked the arm '
    'DEFECTIVE and G-ARMS-NO-LIVE-LIMB failed with it. The control re-pointed through the Edit tool at the body sentence whose one trace is '
    '(IS :355), that text occurring once in the document. The trail record, appended but not yet committed with the line none recorded, was '
    'cut back to its banked byte length before the append and re-appended; the FINDINGS entry carries no defect line and stands. The suite '
    're-run whole.',
]
DEFECT_SHORT = ['(a) the seat’s: G-DOC-TRACES’ positive control deleted one of a sentence’s two traces, so it passed -- re-pointed at a '
                'sentence with one trace; the uncommitted trail record cut back and re-appended; the suite re-run whole']


def defects(*a):
    L = ['b613 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b613_defects.txt', L)


# ================================================================================ READING (1): THE READS
READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the 2B row and the no-keystone section', PP, PRE_PP, CEN3, ('GREP', r'^\| R12 \||^## §2|^- \*\*R12 '), 900),
    ('REGISTRY.md: the 2B heading and rows p2-2, p2-24, p2-14, p2-21, p2-22, p2-28', PP, PRE_PP, 'REGISTRY.md', [244, 248, 249, 250, 251, 252, 253], 900),
    ('SILENCE_EMERGENCE.md whole (p2-2)', PP, PRE_PP, K.PAPERS['SE'][0], 'ALL', 300),
    ('DARK_INTERFACE.md whole (p2-24), its TECHNE line :125 printed by its first words alone', PP, PRE_PP, K.PAPERS['DI'][0], 'ALL', 300),
    ('COGNITION.md whole (p2-14)', PP, PRE_PP, K.PAPERS['CG'][0], 'ALL', 300),
    ('UNIFIED_COGNITIVE.md whole (p2-21)', PP, PRE_PP, K.PAPERS['UC'][0], 'ALL', 300),
    ('IDENTITY_SUBSPACE.md whole (p2-22)', PP, PRE_PP, K.PAPERS['IS'][0], 'ALL', 300),
    ('INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md whole (p2-28)', PP, PRE_PP, K.PAPERS['ID'][0], 'ALL', 300),
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the five tests, RH-60, and the Philosophy / cognition / interfaces cluster (no rows)', PP, PRE_PP, K.SIEVE,
     [27, 28, 29, 30, 31, 44, 122], 700),
    ('OPEN_TRAILS: the form, the precedence order, the sequence`s form, the form`s clauses, b612`s record lines and record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 12228, 12566, 12601, 12621, 12623, 12625], 1500),
    ('THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md v0.1, the form`s latest instance: tier line, head line, version, Correspondence, body, back matter',
     PP, PRE_PP, B612_DOC, [1, 3, 5, 7, 24, 120, 168], 500),
    ('ERRATA.md: the head, the entry form and the latest entries, the pointer rule', PP, PRE_PP, 'ERRATA.md',
     [1, 13, 14, 15, 16, 17, 18, 19, 20, 819, 821, 823, 825, 827, 829, 831, 833, 835], 700),
    ('the 1.5E fact items` lines: TRIVIUM_FINDINGS :171, :255, :257', PP, PRE_PP, 'phase1.5/deep-structure/TRIVIUM_FINDINGS.md', [171, 255, 257], 400),
    ('the 1.5E fact items` lines: CONSTANCE :1007, :1315, :1530, :2210, :2216, :2469, :2667', PP, PRE_PP, 'phase1.5/deep-structure/CONSTANCE.md',
     [1007, 1315, 1530, 2210, 2216, 2469, 2667], 400),
    ('the 1.5E fact items` lines: FROBENIUS :75, :93', PP, PRE_PP, 'phase1.5/deep-structure/FROBENIUS.md', [75, 93], 400),
    ('the 1.5E fact items` lines: TRIVIUM_IDENTITY_SUBSPACE :174, :287', PP, PRE_PP, 'phase1.5/deep-structure/TRIVIUM_IDENTITY_SUBSPACE.md', [174, 287], 400),
    ('the 1.5E fact items` lines: CLASS_NUMBER_ANOMALY :53, :130, :134', PP, PRE_PP, 'phase1.5/deep-structure/CLASS_NUMBER_ANOMALY.md', [53, 130, 134], 400),
    ('the deposited monograph v1.1.2 mirror: Appendix F', PP, PRE_PP, MONO, [2063, 2065, 2067, 2069, 2070, 2071, 2072, 2074], 400),
    ('SIDE-silence-principle v0.1.0 (the paper cites v0.1, which does not resolve): the record and the principle', 'D:/SIDE-silence-principle', 'v0.1.0',
     'SIDESilencePrinciple/Basic.lean', [60, 64, 104, 105, 136, 137, 138, 139, 140, 141, 146, 147], 220),
    ('SIDE-kernel main: silence_universal (named without a pin)', 'D:/SIDE-kernel', 'main', 'Kernel/SilenceTheorem.lean', [74, 75, 76], 220),
    ('relay data/b612_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b612_closing_push_out.txt', 'ALL', 260),
    ('relay data/b612_scores.json (whole)', RELAY, STEPZERO, 'data/b612_scores.json', 'ALL', 300),
]
TECHNE_LINES = {(K.PAPERS['DI'][0], 125)}   # ### lines whose body cites TECHNE content: printed by their first words alone


def reads(*a):
    L = ['b613 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
            if (path, n) in TECHNE_LINES:
                line = ' '.join(line.split()[:6]) + ' ### [TECHNE CONTENT: by pointer alone, TECHNE-Core manifest sha256 %s]' % K.techne_pointer()
            L.append('    :%-6d %s' % (n, line[:width]))
    L += ['', '### THE PINS THE PAPERS NAME, EACH AS CITED, RESOLVED IN ITS CLONE AND AT ITS REMOTE:']
    for k in K.CITED_PINS:
        key, repo, pin, loc, rem, tags = K.cited_pin_state(k)
        L.append('    %-8s %s %s -> %s ; at the remote: %s ; the clone`s tags %s -- %s' % (key, repo, pin, loc or '### DOES NOT RESOLVE', rem or '### NONE',
                                                                                   tags, K.CITED_PINS[k][2]))
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('    %-8s named without a pin; read for the record at %s %s %s :%d: %s' % (k, st[1], st[2], st[3], st[4], 'stands' if st[5] else '### ABSENT'))
    nd = nd_sets()
    L += ['### THE NO-DISCLOSURE NEEDLE SETS, read locally at TECHNE-Core %s and never printed: the method document %s, %d sentences of 40 '
          'characters or more (b591`s form); the tree %s, %d (b595`s form); every module document, %d sentences of 60 characters or more '
          '(b611`s form)' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), METHOD_REL, len(nd['method']), TREE_REL, len(nd['tree']), len(nd['modules'])),
          '### TECHNE mentions in the six papers: %s ; the pointer each takes: TECHNE-Core, its tracked-file manifest sha256 %s' % (
              {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()}, K.techne_pointer()),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b613_reads.txt', L)


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
                if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion' and i > ANSWERS_FROM_LINE:
                    calls.append((i, c['id'], c['input']))
                if isinstance(c, dict) and c.get('type') == 'tool_result':
                    t = c.get('content')
                    results[c.get('tool_use_id')] = (i, ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t)
    n = sum(len(c[2].get('questions', [])) for c in calls)
    L = ['### b613 -- THE AUTHOR`S ANSWERS, %d prompt(s) put by the seat (2026-10-04), banked verbatim with the options and the recommended '
         'mark, as the standing line at OPEN_TRAILS :12246 orders.' % n, '']
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session %s, transcript line %d)' % (cid, SESSION_ID, i))
        for q in inp.get('questions', []):
            L.append('### PROMPT (%s): %s' % (q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d: %s :: %s' % (j, op.get('label'), op.get('description')))
        L += ['RESULT: %s' % (results.get(cid, (None, '### NO RESULT'))[1]), '']
    if not calls:
        L.append('### NONE: no prompt was put to the author in this act; the precedence order and the ruling`s letter reached every '
                 'reading, each declared on the face and strikeable.')
    put_txt('b613_author_answers.txt', L)


ANSWERS_FROM_LINE = 0   # ### the session carries b610-b612 too; none put a prompt, so every call found is b613's

KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-silence-principle', 'SIDE-meta',
         'SIDE-dark-interface', 'SIDE-interfaces')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b613_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b613_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ THE NO-DISCLOSURE NEEDLE SETS
SECTION_RE = re.compile(r'^## \((i|ii|iii|iv|v|vi|vii|viii)\) ', re.M)   # ### b591's and b595's, carried


def _sections(text):
    ms = list(SECTION_RE.finditer(text))
    out = []
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        out.append((m.group(1), text[m.start():end]))
    return out


def _prose40(text):
    """### b591's form, carried: prose sentences of sections (i)-(vii), tables and headings dropped, markdown stripped, 40 characters or more"""
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
    """### the three needle sets, built at run time and never printed"""
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
def arith(*a):
    """### data/b613_arith.txt: the valence-7 congruence over a stated range, the factorisations, the placement of π^(1/4), and COGNITION`s
    ### table re-read -- each computed here, its range printed (R223)(2)."""
    from sympy import primerange, legendre_symbol as Lg, factorint
    import math
    import statistics as st
    N = 100000
    ps = list(primerange(5, N))
    ds = (-1, 2, 3, -2, -3, 6, -6)
    val = {p: sum(Lg(d % p, p) == 1 for d in ds) for p in ps}
    v7 = [p for p in ps if val[p] == 7]
    m23 = [p for p in ps if p % 24 == 23]
    q = math.pi ** 0.25
    rows = [(2, .39), (2.5, .47), (4, .61), (4.5, .49), (4, .65), (4, .55), (4, .48), (5, .73), (1.5, .15), (4.5, .58), (4, .36)]
    r = st.correlation([x for x, _ in rows], [y for _, y in rows])
    n2 = (29, 104, 62, 12, 8, 1, 1)
    L = ['b613 -- COMPONENT 1: THE ARITHMETIC OF (R223)(2), computed %s (sympy %s, Python %s)' % (utc(), __import__('sympy').__version__, sys.version.split()[0]), '',
         '### (i) THE VALENCE-7 CONGRUENCE. Range: the primes 5 <= p < %d, %d of them; d over %s; valence = #{d : (d/p) = +1}.' % (N, len(ps), list(ds)),
         '    valences found: %s' % sorted(set(val.values())),
         '    valence-7 primes: %d ; their residues mod 24: %s' % (len(v7), sorted(set(p % 24 for p in v7))),
         '    primes = 23 mod 24: %d ; of them valence 7: %d ; the first, 23: valence %d, (−1/23) = %d' % (len(m23), sum(1 for p in m23 if val[p] == 7), val[23], Lg(22, 23)),
         '    THE CONDITION OF RECORD: valence 7 exactly when p = 1 mod 24 (the papers` own argument: all of (−1/p), (2/p), (3/p) = +1).',
         '', '### (iv) THE FACTORISATIONS. factorint(79981) = %s ; 11 × 661 = %d ; 11² × 661 = %d ; factorint(79949) = %s' % (
             factorint(79981), 11 * 661, 121 * 661, factorint(79949)),
         '    THE FACTORISATION OF RECORD: 79981 = 11² × 661 (the ruling`s reading confirmed by this computation).',
         '', '### (vi) π^(1/4) = %.6f ; √2 = %.6f ; √3 = %.6f ; 1 < π^(1/4) < √2: %s ; between √2 and √3: %s' % (q, 2 ** .5, 3 ** .5, 1 < q < 2 ** .5, 2 ** .5 < q < 3 ** .5),
         '    THE PLACEMENT OF RECORD: π^(1/4) ≈ 1.3313 lies between 1 and √2.',
         '', '### THE SEAT`S READING OF COGNITION`S TABLE (phase2/philosophy/COGNITION.md :155-:168, :172, :178-:180), for the author:',
         '    rows after excluding the Feeling-of-Learning row: %d (:172 says n = 12) ; r over them with each Bloom range at its midpoint: %.3f (:172 says 0.762; '
         'the coding the paper used is not stated)' % (len(rows), r),
         '    concept inventories over exams 0.61/0.39 = %.3f (:184 says 56%%) ; Ruiz-Primo conceptual over factual 0.58/0.15 = %.3f (:186 says 3.9)' % (.61 / .39, .58 / .15),
         '    the n₂ rows` study counts %s sum to %d (:179 says 261) ; the n₁ rows` 158 + 225 + 1 = %d (:178 says 384)' % (list(n2), sum(n2), 158 + 225 + 1)]
    put_txt('b613_arith.txt', L)
    put_json('b613_arith.json', dict(at=utc(), N=N, primes=len(ps), valences=sorted(set(val.values())), v7=len(v7), v7_res=sorted(set(p % 24 for p in v7)),
                                     m23=len(m23), m23_v7=sum(1 for p in m23 if val[p] == 7), f79981={str(k): v for k, v in factorint(79981).items()},
                                     pi4=q, cg_rows=len(rows), cg_r=r, cg_n2=sum(n2)))
    for l in L:
        print(l[:220])


B612_ENTRY = '## The 1.5E synthesis: the {2, 3} substrate and the Trivium at v0.1'
B612_TRAIL = '### b612 — lane three, act thirty-nine under (R222): the synthesis for 1.5E'
B612_REGROW = '*Appended 2026-10-03 by b612, under `(R222)`(2)(iv) -- A REGISTRY ROW-ADDITION ITEM, FOR THE AUTHOR’S WORD:*'
W_HEAD = ('*Appended 2026-10-04 by b613 to b612’s entry (:%d), under `(R223)`(1) -- b612 AT ITS WEIGHT; THE PIN-RESOLUTION RULE, THE MOD-24 ROW, '
          'THE VERDICTS AND THE TIER CONFIRMED:*')
G_HEAD = '*Appended 2026-10-04 by b613 to b612’s REGISTRY row-addition item (:%d), under `(R223)`(1) -- THE AUTHOR’S WORD, RECORDED:*'
F_HEAD = ('*Appended 2026-10-04 by b613 to b612’s record (:%d), under `(R223)`(2) -- SIX FACT ITEMS FOR THE 1.5E PAPERS’ NEXT EDITIONS, THE '
          'SYNTHESIS’S ROWS STANDING AS GRADED:*')
M_HEAD = '*Appended 2026-10-04 by b613, under `(R223)`(2)(iii) -- THE MOD-24 LEMMA, A KERNEL ITEM PRICED FOR THE AUTHOR’S WORD:*'


def _b612():
    S = json.loads(R4._show(RELAY, STEPZERO, 'data/b612_scores.json'))
    return {k: v[0] for k, v in S.items()}


def _texts(entry, regrow, trail, dry=False):
    s = _b612()
    allh = lambda ks, w: w if all(s[k] == w for k in ks) else [s[k] for k in ks]   # noqa: E731
    A = json.load(io.open(os.path.join(SP if dry else D, 'b613_arith.json'), encoding='utf-8'))
    t1 = ('\n%s THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md v0.1 (PLACE-papers d00957a), in the 1.5E papers’ folder: 1.5e-1 to 1.5e-6 read whole at '
          'a79215a and unedited, CONSTANCE included by the census row with its reclassification noted in the front matter; 89 claims -- 10 '
          'kernel-verified, 11 theorem-supported, 23 argument-supported, 10 computationally-verified, 13 synthesis-suggested, 22 statement-grade; tier KC '
          'on the 10 rows whose terminals sit at six pins in five kernels, every pin resolving in its clone and at its remote; 9 routes -- the '
          'seven-class exclusion DARK by test 2 (RH-60), the finite computations NOT A ROUTE (RH-58), the five identification paths NOT A ROUTE by the '
          'papers’ own correction, five DARK by test 2 and one by test 1 with no sieve row, listed for its next version; neither page changed. The '
          'verdicts, as relay data/b612_scores.json prints them: H46a-H46d %s; N1-N5 %s; S1-S5 %s; no defect; two drafting errors caught in dry mode. '
          'The author confirms the pin-resolution rule (a commit in the clone and at the remote), the mod-24 row at argument-supported, the nine '
          'verdicts with the six-row list, and the KC tier. FINDINGS :7258, :7260; OPEN_TRAILS :12621, :12623, :12625; PLACE-papers a4f16fe; relay '
          '59f524f8, 3b92db0d. The suite 81 of 81. Nothing deposited; no kernel touched; TECHNE-Core untouched.\n' % (
              W_HEAD % entry, allh(('H46a', 'H46b', 'H46c', 'H46d'), 'HOLDS'), allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'),
              allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD')))
    t2 = ('\n%s the row for phase1.5/proofs/THE_RIEMANN_PATHS_CLUSTER_SPINE.md is added in REGISTRY’s own dated row-addition form at the next act that '
          'touches REGISTRY, its cluster, version and tier read from the document; this act does not touch REGISTRY.\n' % (G_HEAD % regrow))
    t3 = ('\n%s (i) phase1.5/deep-structure/TRIVIUM_FINDINGS.md :171 and CONSTANCE.md :2216 give the valence-7 primes as p ≡ ±1 mod 24; the '
          'papers’ own argument (TRIVIUM_IDENTITY_SUBSPACE.md :287, CONSTANCE.md :2210) and the computation over the %d primes 5 to %d give p ≡ 1 mod '
          '24 alone, %d valence-7 primes and none of the %d primes ≡ 23 mod 24 (relay data/b613_arith.txt) -- a fact correction at each; the '
          'deposited monograph v1.1.2 carries the same line at its Appendix F (%s :2071), so the error is entered at ERRATA as %s. (ii) '
          'FROBENIUS.md :75 and :93 and TRIVIUM_IDENTITY_SUBSPACE.md :174 report (ST)³ = I as machine-checked where SIDE-frobenius v0.1.0 compiles '
          '(ST)³ = −1 in SL₂(ℤ), equal to I in PSL₂(ℤ) alone -- a fact correction naming the group at each. (iii) CLASS_NUMBER_ANOMALY.md :53, :130 '
          'and :134 say SIDE-dirichlet-mod-24 verifies (ℤ/24)* ≅ (ℤ/2)³ where 597b0869 compiles the order, each unit squaring to 1 and a count '
          'equality, the isomorphism standing in comments -- the ceiling clause at each, the kernel lemma priced beneath. (iv) CONSTANCE.md :1315 '
          'gives 79981 = 11 × 661, which is 7271; the computation gives 79981 = 11² × 661, the square dropped, and Appendix D :2469 gives 79949 = '
          '31 × 2579 for the same ratio -- a fact item for CONSTANCE, entered at ERRATA as %s. (v) CONSTANCE.md drops superscripts at :685-:693, '
          ':796-:798, :1007 and :1530, and :2667 names SL₃(ℤ) for the modular group -- fact items. (vi) TRIVIUM_FINDINGS.md :255 places π^(1/4) '
          'between √2 and √3; π^(1/4) ≈ %.4f lies between 1 and √2, as its :257 says -- a fact item.\n' % (
              F_HEAD % trail, A['primes'], A['N'], A['v7'], A['m23'], MONO, ERR_IDS[0], ERR_IDS[1], A['pi4']))
    t4 = ('\n%s one lemma at SIDE-dirichlet-mod-24’s next tag: the isomorphism (ℤ/24)* ≅ (ℤ/2)³ stated as a Prop over Mathlib’s units of ZMod 24 '
          'and closed by decide, beside the compiled order, squares and count equality at 597b0869. Price: one act, one module built, one tag pushed '
          'through tools/push_gated.sh after its read-back. Trigger: the author’s word. Not started.\n' % M_HEAD)
    return [(W_HEAD % entry, t1), (G_HEAD % regrow, t2), (F_HEAD % trail, t3), (M_HEAD, t4)]


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
    return Q, Q.line_of(Q.FIND, B612_ENTRY), Q.line_of(Q.OT, B612_REGROW), Q.line_of(Q.OT, B612_TRAIL)


def record_lines(*a):
    """### FINDINGS: b612's weight, addressed to b612's entry; OPEN_TRAILS: the author's word on the REGISTRY row (addressed to :12623), the
    ### six 1.5E fact items (addressed to b612's record) and the mod-24 lemma priced -- each appended at the end. Needs the arithmetic bank."""
    Q, entry, regrow, trail = _addr()
    if (entry, regrow, trail) != (7260, 12623, 12625):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, regrow, trail))
    dry = 'dry' in a
    if not os.path.exists(os.path.join(SP if dry else D, 'b613_arith.json')):
        sys.exit('### THE ARITHMETIC IS NOT BANKED -- NOTHING WRITTEN')
    parts = _texts(entry, regrow, trail, dry)
    bad = ledger_check(*[t for _h, t in parts])
    nd, _n = nd_hits(NL.join(t for _h, t in parts))
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits in the lines: %s' % (bad or 'NONE', nd))
    if 'dry' in a:
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
    put_json('b613_record_lines.json', dict(entry=entry, regrow=regrow, trail=trail, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


def _errata_blocks(dry=False):
    A = json.load(io.open(os.path.join(SP if dry else D, 'b613_arith.json'), encoding='utf-8'))
    fa = 0 if dry else jl('b613_record_lines.json')['lines'][2]['line']   # ### dry: the fact items' line is not yet appended
    e1 = [
        '## %s — TRIVIUM_FINDINGS :171, CONSTANCE :2216 and the deposited monograph’s Appendix F give the valence-7 primes as p ≡ ±1 mod 24; the '
        'valence-7 primes are p ≡ 1 mod 24 alone (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2)' % ERR_IDS[0], '',
        '**Filed 2026-10-04 by b613, on the author’s ruling `(R223)`(2)(i) and its closing sentence; found at b612 (relay `data/b612_reads.txt`), '
        'computed at b613 (relay `data/b613_arith.txt`). Records affected: `phase1.5/deep-structure/TRIVIUM_FINDINGS.md` :171, '
        '`phase1.5/deep-structure/CONSTANCE.md` :2216, and the deposited monograph *A Place to Stand*, Zenodo v1.1.2 '
        '([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)), Appendix F, mirrored at `%s` :2071 (the same line in the earlier '
        'deposit snapshot `outputs/DEPOSITED/A_Place_to_Stand.v5.4.EARLIER-DEPOSIT-SNAPSHOT.md` :1983). ### THE DEPOSITED FILES ARE IMMUTABLE AT '
        'THEIR VERSIONS; NO ZENODO RECORD IS WRITTEN BY THIS ENTRY.**' % MONO, '',
        '**What the lines say.** TRIVIUM_FINDINGS :171: *“these are the primes ≡ ±1 mod 24”*; CONSTANCE :2216: *“The primes ≡ ±1 (mod 24) are '
        'valence-7.”*; Appendix F: *“| p ≡ ±1 mod 24 | 7 | Splits in every field |”*.', '',
        '**What is true.** A prime p > 3 has valence 7 exactly when (−1/p), (2/p) and (3/p) are all +1 -- the papers’ own argument '
        '(TRIVIUM_IDENTITY_SUBSPACE :287, CONSTANCE :2210) -- and that holds exactly when p ≡ 1 mod 24: (−1/p) = 1 needs p ≡ 1 mod 4, (2/p) = 1 '
        'needs p ≡ ±1 mod 8, (3/p) = 1 needs p ≡ ±1 mod 12, and the three meet at 1 mod 24 alone. A prime p ≡ 23 mod 24 has (−1/p) = −1 and '
        'valence 3. Computed over the %d primes 5 to %d: valences {3, 7} only; %d valence-7 primes, every one ≡ 1 mod 24; none of the %d primes '
        '≡ 23 mod 24 has valence 7 (relay `data/b613_arith.txt`).' % (A['primes'], A['N'], A['v7'], A['m23']), '',
        '**The correction.** Where the three lines read “≡ ±1 mod 24”, the condition of record is “≡ 1 mod 24”. The dichotomy itself -- every prime '
        'p > 3 has valence 3 or 7 -- stands.', '',
        '**Scope.** No line is edited: the papers take the correction at their next editions as fact items (OPEN_TRAILS :%d), and the monograph at '
        'its next version. No banked number, verdict or grade moves. Nothing here is a statement about RH or any zero.' % fa, '',
        '**Status.** FILED. Retained at monograph v1.1.2.', '']
    e2 = [
        '## %s — CONSTANCE :1315 factors 79981 as 11 × 661, which is 7271; 79981 = 11² × 661, and Appendix D :2469 gives a different value for '
        'the same ratio (CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)' % ERR_IDS[1], '',
        '**Filed 2026-10-04 by b613, on the author’s ruling `(R223)`(2)(iv) and its closing sentence; found at b612 (relay `data/b612_reads.txt`), '
        'computed at b613 (relay `data/b613_arith.txt`). Record affected: `phase1.5/deep-structure/CONSTANCE.md` :1315, with :2469. ### NO DEPOSITED '
        'ARTIFACT IS AFFECTED BY THIS ENTRY: no file under `outputs/` carries the factorisation (searched at PLACE-papers a4f16fe); the ruling’s '
        '“deposited text” is read as the corpus text, the deposit search recorded here.**', '',
        '**What the lines say.** CONSTANCE :1315: *“| u → t | 79981 = 11 × 661 | Beyond (661) |”*; Appendix D :2469: *“| t/u | 79949 | 31 × '
        '2579 | No (2579) |”*.', '',
        '**What is true.** 11 × 661 = 7271; 79981 = 11² × 661 = 121 × 661; 79949 = 31 × 2579 (relay `data/b613_arith.txt`). The two lines give '
        'different integers for one ratio; this entry does not choose between them.', '',
        '**The correction.** At :1315 the factorisation of record is 79981 = 11² × 661, the square dropped in the text. The line’s classification, '
        'a prime outside the set, is unchanged by the square.', '',
        '**Scope.** No line is edited: CONSTANCE takes the correction at its next edition as a fact item (OPEN_TRAILS :%d). No banked number, '
        'verdict or grade moves.' % fa, '',
        '**Status.** FILED.', '']
    return [(ERR_IDS[0], e1), (ERR_IDS[1], e2)]


def errata(*a):
    """### PLACE-papers ERRATA.md: the two entries of (R223)(2), appended through tools/errata_append.py, each refused if its id is used.
    ### Needs the record lines (the entries point at the fact items' line)."""
    import errata_append as EA
    blocks = _errata_blocks('dry' in a)
    text = NL.join(NL.join(b) for _i, b in blocks)
    nd, _n = nd_hits(text)
    print('  ceiling hits in the entries: %s ; no-disclosure hits: %s' % ([m.group(0) for m in CEILING.finditer(text)] or 'NONE', nd))
    if 'dry' in a:
        print(text)
        return
    if any(nd.values()):
        sys.exit('### AN ENTRY WOULD CARRY TECHNE TEXT -- NOTHING WRITTEN')
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
    put_json('b613_errata.json', dict(at=utc(), entries=out))
    for o in out:
        print('  ERRATA.md %s :%d' % (o['id'], o['line']))


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


def claims(*a):
    """### data/b613_claims_2B.txt and data/b613_claims.json: each paper's path, version and head; every claim with its line, grade and reason;
    ### the routes through the five tests; the pins as cited and their resolution; the TECHNE citations with their pointer; H47a's trace table
    ### -- banked before any writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    sieve = K.sieve_rows()
    CC = K.claims()
    if not all(ok for ok, _l in rc.values()):
        sys.exit('### A NEEDLE FAILS -- NOTHING WRITTEN')
    L = ['b613 -- COMPONENT 2: THE CLAIM BANK OF CLUSTER 2B, (R223)(3), banked %s before any writing' % utc(),
         '### the papers at PLACE-papers %s; the sieve v0.4 at %s' % (PRE_PP, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'A ROUTE is' in x or 'RESOLVES' in x or 'pointer alone' in x] + ['']
    L += ['### PART A -- THE PAPERS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        reg = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        ver = next((l.strip() for l in ls[:20] if re.search(r'v\d+\.\d|April 2026|May 2026', l)), '')
        L.append('  %s = `%s` -- REGISTRY %s (:%d), its version %s, its status %s -- %d lines -- head :1 “%s” -- the paper`s own version/date line “%s”' % (
            k, path, rid, rline, reg[3], reg[5].replace('*', '')[:40], len(ls), ls[0][:120], ver[:120]))
    L += ['', '### PART B -- THE CLAIMS, EACH WITH ITS LINE, NEEDLE, GRADE AND REASON (%d):' % len(CC)]
    for c in CC:
        cid, pk, n, needle, text, grade, support, reason, route = c
        L.append('  %-6s %s :%-4d %-25s support %-11s -- %s' % (cid, pk, n, grade, support, text))
        nd_show = ' '.join(needle.split()[:6]) if (K.PAPERS[pk][0], n) in TECHNE_LINES else needle[:80]
        L.append('         needle “%s” on the line: %s ; reason: %s%s' % (nd_show, rc[cid][0], reason,
                                                                     (' ; route %s %s%s' % (route[0], route[1], '' if route[2] is None else ' test %d' % route[2])) if route else ''))
    L += ['', '### PART C -- THE ROUTES, EACH THROUGH THE FIVE TESTS IN ORDER, WITH ITS VERDICT AND INSTRUMENT:']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        passed = ('tests 1-%d passed; ' % (t - 1)) if t and t > 1 else ''
        L.append('  %s -- claims %s -- %s%s -- %s, %s -- %s -- the sieve`s row %s' % (
            r, ', '.join(x[0] for x in cs), passed, 'fails test %d' % t if t else 'not asked (not a route)', v, inst, why,
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', ''))))) if row else 'none'))
    L += ['', '### PART D -- THE PINS THE PAPERS NAME, AS CITED, AND THE TABLE`S ROWS:']
    for k in K.CITED_PINS:
        key, repo, pin, loc, rem, tags = K.cited_pin_state(k)
        L.append('  %-8s %s %s -> %s ; at the remote: %s ; the clone`s tags %s -- %s ; no row certifies from it' % (
            key, repo, pin, loc or 'DOES NOT RESOLVE', rem or 'NONE', tags, K.CITED_PINS[k][2]))
    for k in K.UNPINNED:
        st = K.unpinned_state(k)
        L.append('  %-8s named without a pin (ID :250); stands at %s %s %s :%d -- no row certifies from it' % (k, st[1], st[2], st[3], st[4]))
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '[]')
    TT = T.get('rows') if isinstance(T, dict) else T
    for nm in ('silence_principle', 'silence_universal'):
        r = [x for x in TT if str(x.get('name', '')).split('.')[-1] == nm]
        L.append('  the terminal table on %s: %s' % (nm, ['%s %s %s' % (x.get('repo'), x.get('name'), x.get('pin')) for x in r] or 'no row'))
    L += ['  the pages: no node of either page`s list is a name the six papers cite (both lists read in the dry run)']
    L += ['', '### PART E -- THE TECHNE CITATIONS AND THE POINTER EACH TAKES:']
    for c in CC:
        if (K.PAPERS[c[1]][0], c[2]) in TECHNE_LINES:
            L.append('  %s %s :%d -- TECHNE-Core, its tracked-file manifest sha256 %s ; no sentence of its body carried' % (c[0], c[1], c[2], K.techne_pointer()))
    trace = sorted(set((c[1], c[2]) for c in CC))
    L += ['', '### PART F -- H47a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    reached, matched, listed = route_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in CC)
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### THE ROUTES: %d (%s); against the sieve: %s; with no row, listed for its next version: %s' % (
              len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                  for r, row, m, t, ok in matched) or 'none', listed or 'none')]
    put_txt(BANK, L)
    put_json('b613_claims.json', dict(at=utc(), n=len(CC), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, matched=matched, listed=listed,
                                      pointer=K.techne_pointer(),
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in CC]))
    print(L[-1])


# ================================================================================ COMPONENT 3: THE DOCUMENT
TITLE = ('# The Silence Principle and Interface Darkness: Natural Language and Validity, the Conservation of Cognition, the Pedagogy and IMO '
         'Correlations and the Identity Subspace')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional|[Uu]nique|[Ee]xact)\b')
HEADLINE = '*This document synthesises the six papers it names and certifies nothing they do not.*'
VERSION = '*v0.1, 2026-10-04 -- written at b613 under `(R223)`(3), the synthesis for 2B that THE_KEYSTONE_CENSUS v0.3 names (its row R12).*'
BM_TAG = '<!-- b613 (R223) THE v0.1 BACK MATTER, 2026-10-04 -->'
BODY1 = '## 1. The papers and their status'

BODY = [
    (BODY1, [
        'ID states that the cluster’s epistemic status is empirical regularity (ID :17) and that its content is empirically anchored and not kernel-verified (ID :245).',
        'ID states that the Silence Principle is checked in a kernel it cites as SIDE-silence-principle v0.1 (ID :25), and names silence_universal with nine instances compiled (ID :250).',
        'IS states that whether its structures assemble into a resolution of RH is open (IS :365).']),
    ('## 2. The Silence Principle', [
        'SE states a four-step theorem and names it the Silence Principle (SE :13): for an essential universal interface, κ(P, I) = 0 for every behavioral parameter that varies across configurations (SE :79).',
        'SE calls the load-bearing step, that what works for all works the same for all, close to tautological (SE :92), and limits the principle to coupled systems joined by an essential universal interface (SE :96).',
        'SE states that the product formula builds ξ without encoding where its zeros sit (SE :25), and gives κ = 0.94 for amino-acid identity and κ = 0.08 for codon frequency (SE :29).',
        'SE reads the failure of reductionism at scale transitions as due to the universality of fundamental laws (SE :112), and Fodor’s autonomy of the special sciences as the principle applied (SE :120).',
        'SE reads codon-usage bias as emergence in the zone the genetic code leaves silent (SE :233).']),
    ('## 3. Consciousness', [
        'SE reads the hard problem of consciousness as a consequence of the principle, given an essential and universal neural-experiential interface (SE :147), and distinguishes this from eliminativism, mysterianism, panpsychism and strong emergence (SE :163).',
        'SE states that neural correlates do not refute the principle, correlation not being derivation (SE :195), and names as its falsifier a future derivation of specific qualia from neural patterns (SE :215).',
        'SE states that whether neural structure and experience are coupled or identical is empirical (SE :183), that the principle does not solve the hard problem (SE :269), and that its consciousness instance is argued by structural analogy (SE :275).',
        'ID argues that the neural-experiential interface must be universal and so dark for qualia (ID :93).']),
    ('## 4. Natural language and validity', [
        'DI states that natural language carries no information about the validity of a mathematical argument (DI :28), citing three historical cases (DI :30).',
        'DI applies the principle to state that every essential, universal medium for mathematical communication is dark for validity (DI :52), and reads natural language and the product formula as one phenomenon (DI :60).',
        'DI states that the Lean type system transmits validity exactly (DI :104), being bright because it is not universal (DI :110).',
        'DI reads the darkness of natural language as protection (DI :143), and states that a model working in natural language stays at κ ≈ 0 for validity whatever its capability (DI :153).',
        'DI states its claim falsifiable by a feature of natural language that reliably separates valid from invalid arguments (DI :175).',
        'DI reports a worked example from a private library, cited here by pointer alone (DI :125), and reads peer review as the mathematical analogue of the genetic code’s error correction (DI :135).']),
    ('## 5. Density and placement', [
        'DI states that sieve methods give density results, such as at least 40% of the zeros on the critical line, and not the placement of every zero (DI :74), and reads peer review and the sieve as limited for one reason (DI :86).',
        'ID reads peer review and sieve methods as sharing one density-without-placement barrier (ID :73), and reads three historical cases as confirming it (ID :29).']),
    ('## 6. The conservation of cognition', [
        'CG states that the interface between external stimulation and internal construction runs at κ ≈ 0 in healthy cognition as a metabolic conservation law (CG :22), with κ(Task-Positive) + κ(Default Mode) ≈ 1 (CG :98).',
        'CG states a four-stage formation whose interface stage has n₄ = 0 (CG :68) and maps three brain networks onto its stages (CG :104), a mapping it calls an interpretive choice and a law it calls approximate (CG :327).',
        'CG maps McLuhan’s hot and cool media onto κ (CG :114) and reads the ICAP hierarchy as a κ gradient (CG :199).',
        'CG proposes Clause G, that dark interfaces are the necessary condition for structural self-organisation (CG :226), and ID gives its status as empirical regularity (ID :141).',
        'CG reads creative insight as a transient breach of the law (CG :246) and depression as its breakdown (CG :262), and predicts that anti-correlation strength predicts mindfulness response (CG :274).',
        'ID states κ_TPN + κ_DMN ≈ 1 as an empirical structural finding (ID :109), and reads sustained co-activation as pathological (ID :131).']),
    ('## 7. The pedagogy and IMO correlations', [
        'CG reports r = 0.762 between the Bloom level of assessment and the active-learning advantage (CG :24), concept inventories with a 56% larger effect than exams (CG :184), a conceptual-to-factual ratio of 3.9 (CG :186), and stage means 0.34, 0.53 and 0.73 (CG :178).',
        'CG cites Deslauriers and colleagues (2019): test of learning d = +0.36, feeling of learning d = −0.30 (CG :210).',
        'UC reports r = 0.762 for learning and r = 0.656 for the difficulty of 156 IMO problems (UC :13), combinatorics the hardest domain at mean MOHS 29.6 (UC :23), and 12/12 accuracy on AI performance at IMO 2024–2025 (UC :65).',
        'UC reads the two datasets’ agreement as the signature of one domain-general variable (UC :80) and maps bright and dark interfaces onto network engagement (UC :88).',
        'UC predicts that AI systems will fail at dark-interface problems until they build internal models (UC :100), and that κ will predict outcomes in other domains (UC :102).',
        'ID states interface darkness as a domain-general cognitive variable (ID :15), reports the 12/12 accuracy (ID :187), states a forward prediction for IMO 2026 (ID :193), and states that its coefficients depend on the re-analysis method (ID :289).']),
    ('## 8. The identity subspace', [
        'IS states that n^(−σ) = n^(−(1−σ)) for every n ≥ 2 holds exactly at σ = 1/2 (IS :35), and that the pointwise intersection of the identity loci is empty, taking the centered coordinate instead (IS :85).',
        'IS states five convergent constructions of σ = 1/2 and, corrected, that three share the involution σ ↦ 1 − σ (IS :53), while its sentence of disjoint machinery stands beneath the correction (IS :65).',
        'IS states that g(2, 3) = 1 (IS :129), that {−1, 2, 3} generate seven quadratic fields (IS :141), Størmer’s four pairs for {2, 3} (IS :155), and the dimension 7 from the smooth integers up to 3 (IS :171).',
        'IS states the norm squared 12 (IS :203), T² = −I (IS :219), the spectrum {0⁶, 12} (IS :239), the valence dichotomy (IS :305) and the order 8 of (ℤ/24)* (IS :331).',
        'IS asks whether the fiber bundle over the critical line is orientable (IS :355).']),
    ('## 9. The routes the papers offer', [
        'DI states that the content for resolving RH by exhaustive enumeration existed before it was assembled (DI :92), and that a kernel certifies the conditional from structural exhaustiveness to RH while the manuscripts supply its antecedent (DI :119).']),
]
TRACE_RE = re.compile(r'\b(SE|DI|CG|UC|IS|ID) :(\d+)')


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | paper | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(P[k][0].lstrip('# ').strip()), _cell(st[5]).replace('*', '')[:40]))
    return [TITLE, '',
            '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-04 (b613), under `(R223)`(3): '
            'the tier the rows earn, decided after they were graded -- %d rows read kernel-verified: the one kernel pin the papers name with a claim, '
            'SIDE-silence-principle v0.1, resolves neither in the clone nor at the remote, and the terminal they name, silence_universal, is named '
            'without a pin; each row is cited at its stated grade, the Correspondence in the back matter (`(R221)`(3)).*' % (tier, cert_rows), '',
            HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for cluster 2B (THE_KEYSTONE_CENSUS v0.3, its row R12 and §2): the six papers REGISTRY '
            'files as p2-2, p2-24, p2-14, p2-21, p2-22 and p2-28, each claim listed with the grade its own text supports; for a reader who meets those '
            'papers and needs what each states and what backs it.*', '',
            '**The papers, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** INTERFACE_DARKNESS (ID) is itself a cluster keystone in its own words, synthesised here as one of the six papers '
            'the census row lists. Where a paper cites TECHNE content, this document carries a pointer by name and sha256 alone and no sentence of it. '
            'The grades are `(R19)`’s vocabulary as `(R220)`(5) lists it; cite the synthesis for orientation and each row at its stated grade.', '']


def _corr(CC):
    S = ['## Correspondence', '',
         '*Every claim of the six papers this document carries, with the grade the paper’s own text supports. A route is read through the sieve’s '
         'five tests in order; the routes and their instruments are below.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in CC:
        cid, pk, n, _needle, text, grade, _support, reason, route = c
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(reason), rcell))
    return S + ['']


def _back(CC):
    sieve = K.sieve_rows()
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-04 by b613 under the author’s ruling `(R223)`(3), by the synthesis form of `(R220)`(5) and `(R221)`(3)', '',
         '### The grading rule, confirmed by `(R222)`(1)', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A pin resolves when its commit is in the clone and at the remote (`(R223)`(1)).',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.', '']
    B += _corr(CC)
    B += ['### The routes through the five tests', '',
          '| route | claims | verdict | test, instrument at pin | reason | the sieve’s row |', '|:--|:--|:--|:--|:--|:--|']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        B.append('| %s | %s | %s | %s | %s | %s |' % (r, ', '.join(x[0] for x in cs), v, ('%d (%s)' % (t, inst)) if t else '—', _cell(why),
                                                   ('%s, %s' % (row, ' '.join(sieve.get(row, ('?', ''))).replace(' —', ''))) if row else 'none'))
    B += ['', '### The pins the papers name', '', '| as cited | its resolution | what the paper names there |', '|:--|:--|:--|']
    for k in K.CITED_PINS:
        key, repo, pin, loc, rem, tags = K.cited_pin_state(k)
        B.append('| %s %s | %s | %s |' % (repo, pin, ('commit `%s`, %s' % (loc, rem)) if loc and rem else ('does not resolve; the clone’s tags %s' % ', '.join(tags)),
                                          _cell(K.CITED_PINS[k][2])))
    st = K.unpinned_state('silence_universal')
    B.append('| silence_universal, no pin | named at %s %s, `%s` :%d | the universal form, nine instances (ID :250) |' % (st[1], st[2], st[3], st[4]))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b613 |' % DOC]
    for k, (path, rid, _rl) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R12 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/%s` | banked before this document |' % BANK, '',
          '### Version history', '',
          '- **v0.1, 2026-10-04 (b613, `(R223)`(3))**: the synthesis of p2-2, p2-24, p2-14, p2-21, p2-22 and p2-28, %d claims graded, the routes read '
          'through the five tests.' % len(CC), '']
    return B


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    return ('KC' if cert else 'C'), len(cert)


def doc(*a):
    """### PLACE-papers phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md (created) and data/b613_doc.json; `dry`: the scratchpad.
    ### Needs the claim bank first."""
    if not os.path.exists(_p('b613_claims.json')):
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
    lines = lines + _back(CC)
    b = (NL.join(lines) + NL).encode('utf-8')
    dest = os.path.join(SP, 'b613_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b613_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(CC)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b613_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b613_doc_termscan.txt', t.rstrip(NL).split(NL))


def h47a(ls, J):
    trace = set((p, n) for p, n in jl('b613_claims.json')['trace'])
    body = [l for l in ls[J['body_at'] - 1:J['body_end']] if l.strip() and not l.startswith('#')]
    sents = [s for l in body for s in _segs(l)]
    bad = []
    for s in sents:
        tr = [(m.group(1), int(m.group(2))) for m in TRACE_RE.finditer(s)]
        if not tr or any(x not in trace for x in tr):
            bad.append(s[:120])
    return not bad, len(sents), bad


def h47d_check(tier_line):
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    return (not kv and 'TIER C**' in tier_line) or (bool(kv) and 'TIER KC**' in tier_line)


def doc_bank(*a):
    """### data/b613_doc_bank.txt and data/b613_h47.json: the title's property words, H47a-H47d, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b613_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b613_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h47a(ls, J)
    rows = [l for l in ls if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h47b = 'HOLDS' if len(rows) >= 15 and not over and len(rows) == len(K.C) else 'REFUTED'
    hits, sizes = nd_hits(NL.join(ls))
    h47c = 'HOLDS' if not any(hits.values()) and all(sizes.values()) else 'REFUTED'
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    h47d = 'HOLDS' if h47d_check(tier_line) else 'REFUTED'
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    pointer_ok = K.techne_pointer() in NL.join(ls)
    L = ['b613 -- COMPONENT 3: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified; the line: %s' % (J['tier'], J['cert_rows'], tier_line[:600]),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'in the back matter, after the body (C)' if placed and J['tier'] == 'C'
                                                                                          else 'after the front matter (KC)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s' % (HEADLINE in ls[:12]),
         '### THE TECHNE POINTER in the document: %s' % pointer_ok,
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM over this document, the needles read locally and never printed: the method document %d needles, %d hits ; the '
         'tree %d, %d ; every module document %d, %d' % (sizes['method'], hits['method'], sizes['tree'], hits['tree'], sizes['modules'], hits['modules']),
         '### H47a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H47a %s** -- every body sentence traces by path and line to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H47b %s** -- the Correspondence carries %d rows (at least fifteen), none graded above its paper`s named backing (%s)' % (h47b, len(rows), over or 'none'),
         '### ### **H47c %s** -- the no-disclosure arm finds %d hits on the new document' % (h47c, sum(hits.values())),
         '### ### **H47d %s** -- the tier line reads %s, %d rows certifying' % (h47d, J['tier'], J['cert_rows']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and h47c == 'HOLDS' and placed and pointer_ok else '### ### **HELD.**']
    put_txt('b613_doc_bank.txt', L)
    put_json('b613_h47.json', dict(H47a='HOLDS' if a_ok else 'REFUTED', H47b=h47b, H47c=h47c, H47d=h47d, sentences=n_sent, untraced=a_bad, rows=len(rows),
                                   over=over, clean=clean, ceiling=len(ceiling), title_props=title_props, nd_hits=hits, nd_sizes=sizes, placed=placed,
                                   tier=J['tier'], pointer=pointer_ok))
    for l in L[-6:]:
        print(l)


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b613_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b613_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b613_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b613 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b613_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b613_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H47a', 'H47b', 'H47c', 'H47d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + (CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md', B612_DOC,
                                                     'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', K.SIEVE, MONO,
                                                     'phase1.5/deep-structure/TRIVIUM_FINDINGS.md', 'phase1.5/deep-structure/CONSTANCE.md')
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the seat's expectation, registered on the face


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores(*a):
    H, CJ, J = jl('b613_h47.json'), jl('b613_claims.json'), jl('b613_doc.json')
    Z, X = jl('b613_page_zeta.json'), jl('b613_page_chi.json')
    face = jl('b613_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1').split(NL) if x.startswith('?? ')))
    want_pp = sorted(['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b613_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b612_closing_push_out.txt'))
    rc = K.resolve_claims()
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    pins = {k: K.cited_pin_state(k) for k in K.CITED_PINS}
    arms2 = rd('b613_page_arms_c2.txt')
    nroutes = len(CJ['routes'])
    nd = H['nd_hits']
    S = {
        'H47a': (H['H47a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H47b': (H['H47b'], 'Correspondence rows %d (the floor 15), graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H47c': (H['H47c'], 'no-disclosure hits on the new document: method %d of %d needles, tree %d of %d, modules %d of %d' % (
            nd['method'], H['nd_sizes']['method'], nd['tree'], H['nd_sizes']['tree'], nd['modules'], H['nd_sizes']['modules'])),
        'H47d': (H['H47d'], 'the tier line reads %s with %d certifying rows; no pin the papers name resolves to a row' % (H['tier'], J['cert_rows'])),
        'N1': ('HELD' if CJ['n'] >= 60 and nroutes >= 5 else 'REFUTED', '%d claims (the floor 60), %d routes (the floor 5): the papers offer two '
                                                                         'route claims of their own, R1 and R2' % (CJ['n'], nroutes)),
        'N2': ('HELD' if not any(nd.values()) else 'REFUTED', 'the no-disclosure arm on the new document: %d hits' % sum(nd.values())),
        'N3': ('HELD' if len(kv) <= 4 else 'REFUTED',
               '%d rows kernel-verified (at most 4); every one resolves -- VACUOUS on its second clause, there being none' % len(kv)),
        'N4': ('HELD' if H['H47a'] == 'HOLDS' and H['clean'] and H['ceiling'] == 0 else 'REFUTED',
               'every body sentence traced %s ; the scanner %s ; the ceiling pattern %d' % (H['H47a'], 'CLEAN' if H['clean'] else 'NOT CLEAN', H['ceiling'])),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the papers, the census, REGISTRY, SPIRAL_MAP, b612`s document, the taxonomy, the '
               'sieve, the deposited mirror and the 1.5E papers unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools and the '
               'table %s' % (kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if not pins['silence'][3] and pins['meta'][3] and pins['meta'][4] and K.unpinned_state('silence_universal')[5] and not kv else 'REFUTED',
               'SIDE-silence-principle v0.1 resolves %s ; SIDE-meta v0.3 resolves %s ; silence_universal stands at SIDE-kernel main %s ; rows '
               'kernel-verified %d' % (bool(pins['silence'][3]), bool(pins['meta'][3] and pins['meta'][4]), K.unpinned_state('silence_universal')[5], len(kv))),
        'S3': ('HELD' if H['placed'] else 'REFUTED', 'the Correspondence placed by (R221)(3) for tier %s: %s' % (H['tier'], H['placed'])),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b613_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:220]))


def _title():
    J, CJ = jl('b613_doc.json'), jl('b613_claims.json')
    return ('## The 2B synthesis: the Silence Principle and interface darkness at v0.1 from p2-2, p2-24, p2-14, p2-21, p2-22 and p2-28, %d claims '
            'graded, %d routes read, tier %s; the 1.5E papers’ six fact items and two errata' % (J['rows'], len(CJ['routes']), J['tier']))


TRAIL_HEAD = ('### b613 — lane three, act forty under (R223): the synthesis for 2B -- one document from the cluster’s six papers read at address, every '
              'claim graded, the routes read, the no-disclosure arm bearing; the 1.5E papers’ findings entered, two as errata')
FOR_AUTHOR = (
    '(1) ERRATA %s’s finding sits in deposited text: the monograph v1.1.2’s Appendix F carries “p ≡ ±1 mod 24 | 7” (%s :2071), and the v5.4 '
    'deposit snapshot the same line; %s’s factorisation sits in no deposited file, so that entry reads corpus-facing; (2) '
    'INTERFACE_DARKNESS_DOMAIN_GENERAL_COGNITIVE_VARIABLE.md :25, :245, :249 and :327 cite SIDE-silence-principle v0.1, which resolves neither in '
    'the clone nor at the remote (tags v0.1.0, v0.2.0); at v0.1.0 silence_principle is an implication over Boolean fields that each instance sets in '
    'its own definition, the product formula’s silence among them; (3) COGNITION.md :172 gives n = 12 after excluding one of its table’s twelve '
    'rows, and its r = 0.762 is not recovered from the table at midpoint coding (0.782), the coding unstated; its n₂ study count at :179, 261, is '
    'not the sum of the rows listed, 217 (relay data/b613_arith.txt); (4) IDENTITY_SUBSPACE.md :129 bounds every other coprime pair by g ≥ 1, '
    'which does not separate {2, 3}; :171 lists 0 among the {2,3}-smooth integers; :65 keeps the sentence of disjoint machinery beneath its own '
    ':53 correction; (5) the papers offer two route claims, so (N1)’s floor of five routes is refuted on the papers’ own letter')


def _finding_text():
    S, J, CJ = jl('b613_scores.json'), jl('b613_doc.json'), jl('b613_claims.json')
    rl, ej = jl('b613_record_lines.json'), jl('b613_errata.json')
    w, gw, fa, mo = [x['line'] for x in rl['lines']]
    e1, e2 = [x['line'] for x in ej['entries']]
    dc = _pp_commit('b613 (R223)(3): ' + DOC)
    t = _title()
    gr = CJ['grades']
    e = ['', t, '',
         '*Filed at b613 on the author’s ruling `(R223)`. Banks: relay `data/b613_reads.txt`, `data/%s`, `data/b613_arith.txt`, `data/b613_doc_bank.txt`, '
         '`data/b613_page_arms_c2.txt`. Nothing deposits.*' % BANK, '',
         '**The document** (`(R223)`(3)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the six papers REGISTRY files as p2-2, p2-24, '
         'p2-14, p2-21, p2-22 and p2-28 read whole at %s, %d claims each restated in one sentence and graded by its paper’s own text -- '
         'theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d, kernel-verified %d. '
         'Tier %s: the one kernel pin the papers name with a claim, SIDE-silence-principle v0.1, resolves neither in the clone nor at the remote, and '
         'silence_universal is named without a pin, so no row certifies and the Correspondence sits in the back matter (`(R221)`(3)). The one TECHNE '
         'citation, DARK_INTERFACE :125, is carried by pointer alone; the no-disclosure arm, with the method document’s, the tree’s and every module '
         'document’s needles, finds 0 hits.' % (
             DOC, dc, PRE_PP, CJ['n'], gr.get('theorem-supported', 0), gr.get('argument-supported', 0), gr.get('computationally-verified', 0),
             gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), gr.get('kernel-verified', 0), J['tier']), '',
         '**The routes** (the five tests). %d routes: the exhaustive-enumeration claims of DARK_INTERFACE DARK by test 2, matching the sieve’s RH-60; '
         'the five identification paths of IDENTITY_SUBSPACE NOT A ROUTE by its own correction. The cluster’s other claims are about cognition, '
         'media, pedagogy and the identity subspace, and offer no argument toward RH.' % len(CJ['routes']), '',
         '**The record lines.** b612’s weight, with the four confirmations, at FINDINGS :%d; the author’s word on the REGISTRY row recorded at '
         'OPEN_TRAILS :%d; the six 1.5E fact items at :%d; the mod-24 lemma priced at :%d. ERRATA %s (the valence-7 congruence, deposit-facing) at '
         ':%d and %s (the 79981 factorisation, corpus-facing) at :%d, committed alone, the computations at relay data/b613_arith.txt.' % (
             w, gw, fa, mo, ERR_IDS[0], e1, ERR_IDS[1], e2), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R12 (FINDINGS :7212, b610’s §2) and follows the form of '
         'b611’s and b612’s syntheses (:7240, :7260); its one route meets b609’s sieve row RH-60 (:7186) again; its identity-subspace rows read '
         'the shorter paper on the object whose sections TRIVIUM_IDENTITY_SUBSPACE, synthesised by b612 (:7260), carries; the errata answer b612’s '
         'findings. It strengthens '
         'the programme’s offering of the Silence Principle’s cognitive applications: six papers, one of them calling itself a keystone, now have '
         'one place where each claim stands at its own grade and the principle’s kernel citation is read at its pin.', '',
         '**Next.** Per `(R223)`(4): b614, the synthesis act for 2D. The author rules on the closing.', '',
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
    put_json('b613_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl, ej = jl('b613_scores.json'), jl('b613_findings.json'), jl('b613_record_lines.json'), jl('b613_errata.json')
    w, gw, fa, mo = [x['line'] for x in rl['lines']]
    e1, e2 = [x['line'] for x in ej['entries']]
    rows_ = ['', TRAIL_HEAD, '',
             '**(R223) ratified.** (1) b612 at its weight, the pin-resolution rule, the mod-24 row, the verdicts and the tier confirmed; the author’s '
             'word on the REGISTRY row. (2) The six 1.5E findings entered as fact items, two as errata. (3) The synthesis for 2B; H47a-H47d. (4) The '
             'act after: b614.', '',
             '**Entered:** FINDINGS.md:%d (b612’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the author’s word, addressed '
             'to :12623), :%d (six fact items, addressed to b612’s record :12625), :%d (the mod-24 lemma priced); ERRATA.md :%d (%s), :%d (%s); this '
             'record; PLACE-papers `%s`; relay data/%s, data/b613_arith.txt.' % (w, fj['entry_line'], gw, fa, mo, e1, ERR_IDS[0], e2, ERR_IDS[1], DOC, BANK), '',
             '**Resolved by the seat, for the author’s strike:** the cited pin SIDE-silence-principle v0.1 read as written, unresolved, so no row '
             'certifies and the tier reads C; the TECHNE pointer as the sha256 of TECHNE-Core’s tracked-file manifest; the 79981 entry corpus-facing, '
             'the ruling’s “deposited text” read against a search of outputs/; the two routes and their verdicts. No prompt was put (relay '
             'data/b613_author_answers.txt).', '',
             '**For the author:** %s.' % (FOR_AUTHOR % (ERR_IDS[0], MONO, ERR_IDS[1])), '',
             '**b614 priced** (the sequence’s form: each act prices the next): the census row R14, 2D, eight papers, 2,615 lines -- '
             'phase2/physics/COSMOLOGICAL_SIEVE_CEILING.md, MATTER_AS_ARITHMETIC.md, STORMER.md, HODGE_CONSERVATION.md, PRIME_ORDER.md, '
             'FANO_DERIVATION_OF_LAMBDA.md, YANG_MILLS_MONOGRAPH.md and heritage/UNIFICATION_OF_FORCES.md -- read whole at address; one act, no Lean '
             'call; the tier read from the rows; the cluster’s kernels read at the pins its papers name; no paper names TECHNE.', '',
             '**Defects** (relay data/b613_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R223)`(4), b614, the synthesis act for 2D; the author rules on the closing.', '',
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
    put_json('b613_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b613_trail.json')['line'])


def desk(*a):
    S = jl('b613_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b613 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H47a-H47d, (R223)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H47 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
        sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b613_defects.txt').rstrip(NL).split(NL)
    put_txt('b613_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl, ej = jl('b613_scores.json'), jl('b613_findings.json'), jl('b613_trail.json'), jl('b613_record_lines.json'), jl('b613_errata.json')
    Z, X = jl('b613_page_zeta.json'), jl('b613_page_chi.json')
    L = ['b613 -- THE COMPONENTS, BANKED UNDER (R223).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b612`s closing push-out relay %s ; push-b612* branches deleted by name '
         '(data/b613_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b613_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b612`s weight FINDINGS :%d ; the author`s word OPEN_TRAILS :%d ; six fact items :%d ; the mod-24 lemma priced :%d ; '
         'the arithmetic data/b613_arith.txt ; ERRATA %s' % (tuple(x['line'] for x in rl['lines']) + (', '.join('%s :%d' % (x['id'], x['line']) for x in ej['entries']),)),
         '### COMPONENT 2 : the claim bank data/%s ; routes %s' % (BANK, ', '.join(jl('b613_claims.json')['routes'])),
         '### COMPONENT 3 : the document %s ; data/b613_doc_bank.txt ; H47a %s, H47b %s, H47c %s, H47d %s' % (DOC, S['H47a'][0], S['H47b'][0], S['H47c'][0], S['H47d'][0]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b613_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b614 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b613_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b613_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
