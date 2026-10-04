# -*- coding: utf-8 -*-
"""b617_record.py -- THE ACT'S RECORD TOOL, UNDER (R227). ### ONE SUBCOMMAND PER BANK.

### ### b617: LANE THREE, ACT FORTY-FOUR -- THE SIEVE AT v0.5: THE TEN CONCLUSIONS GATHERED FROM THE SIX SYNTHESES AS ROWS; THE 2G
### PAPERS' FINDINGS AND THREE ERRATA; THE LIVING DOCUMENTS' CURRENCY ENTERED FOR b618.
### Subcommands write only `data/b617_*` unless the docstring names another file; `dry` on the command line routes every b617 bank and
### the edition to the seat's scratchpad (for `findings`, `trail`, `record_lines` and `errata`, `dry` prints and appends nothing). Banks
### are written by encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`; ERRATA through
### tools/errata_append.py, which refuses a used id before it writes. The act's data is tools/b617_worklist.py's. No platform call. No
### Lean call: both pages are re-emitted from their banked probes. The templates are tools/b616_record.py (the record, the pages, the
### ledgers) and tools/b609_record.py (the sieve's edition, its bank and its re-pin step).
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
import b617_worklist as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EFK = 'D:/SIDE-explicit-formula'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_RELAY = '365bc07e'
STEPZERO = '9d80f449'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/4430dadd-ebc7-4bca-a2e4-2aa8752aee4f/scratchpad'
SESSION_ID = '4430dadd-ebc7-4bca-a2e4-2aa8752aee4f'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
SV4, SV5 = K.SV4, K.SV5
B605_TAG = '<!-- b605 (R215) THE v0.3 EDITION`S BACK MATTER, 2026-10-03 -->'
B609_TAG = '<!-- b609 (R219) THE v0.4 EDITION`S BACK MATTER, 2026-10-03 -->'
BM_TAG5 = '<!-- b617 (R227) THE v0.5 EDITION`S BACK MATTER, 2026-10-04 -->'
ERR_IDS = ('E-2026-10-04-5', 'E-2026-10-04-6', 'E-2026-10-04-7')
PS = 'phase2/physics-speculative/'
LIVING = [
    ('VERIFICATION_LOOM', 'VERIFICATION_LOOM.md', '**PURPOSE:**'),
    ('INSTRUMENTS', 'phase1.5/method/INSTRUMENTS.md', '**PURPOSE:**'),
    ('THE_METHOD_CANON', 'phase1.5/method/THE_METHOD_CANON.md', '**PURPOSE:**'),
    ('THE_METHOD_AS_IT_STANDS', 'phase1.5/method/THE_METHOD_AS_IT_STANDS.md', '> ### **WHAT THIS DOCUMENT IS.**'),
    ('FACES_LEDGER', 'FACES_LEDGER.md', '**PURPOSE:**'),
    ('THE_LOAD_BEARING_MAP', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', '**PURPOSE:**'),
    ('GAUGE_AND_INVARIANT', 'phase1.5/method/GAUGE_AND_INVARIANT.md', '**PURPOSE:**'),
    ('REGISTRY', 'REGISTRY.md', '**PURPOSE:**'),
]

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
_show = R4._show
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines', 'errata')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b617_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b617_') else '', name, len(b)))
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


def _count(ls):
    return sum(len(_segs(l)) for l in ls)


def _poss(s):
    """### a backtick possessive (word`s) becomes ’s for a PLACE-papers file; a code span keeps its backticks."""
    return re.sub(r'(?<=\w)`(?=s\b)', '’', s)


def _cell(s):
    return R4._cell(_poss(s))


DEFECTS = [
    '(a) THE SEAT`S, AT COMPONENT 1, AFTER THE SEAL: the -5 entry`s Scope named the -7 entry by its id, and tools/errata_append.py reads '
    'an id as taken wherever it occurs in the file; with -5 and -6 written, the appender refused -7 before writing it (nothing of -7 '
    'written). The dry run printed the entries without calling the appender, so it could not see it. ERRATA.md, uncommitted, was cut back to '
    'its HEAD blob after the HEAD bytes were read as a prefix of the file on disk and the bytes beyond them as -5 and -6 alone (153850 of '
    '157670 bytes); the -5 Scope reworded through the Edit tool to name no later id; the three entries appended again whole.',
]
DEFECT_SHORT = ['(a) the seat’s: the -5 errata entry named the -7 entry by its id, so the appender, which reads any occurrence of an id as '
                'taken, refused -7 after -5 and -6 landed; ERRATA, uncommitted, cut back to its HEAD blob on a verified prefix, the -5 Scope '
                'reworded through the Edit tool, the three entries appended again']


def defects(*a):
    L = ['b617 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b617_defects.txt', L)


# ================================================================================ b616 AT ITS WEIGHT, FROM ITS BANKS
def _b616():
    """### b616's figures from its banks at relay 365bc07e and its commits in PLACE-papers 3dd4f29..52962da"""
    j = lambda p: json.loads(R4._show(RELAY, PRE_RELAY, 'data/' + p))   # noqa: E731
    CJ, DJ, H, S, RL, FJ, TJ, RS, Z, X = (j('b616_claims.json'), j('b616_doc.json'), j('b616_h50.json'), j('b616_scores.json'),
                                          j('b616_record_lines.json'), j('b616_findings.json'), j('b616_trail.json'),
                                          j('b616_routes_for_sieve.json'), j('b616_page_zeta.json'), j('b616_page_chi.json'))
    chk = {}
    for n in ('b616_checks.txt', 'b616_checks_postpush.txt', 'b616_checks_attempt1.txt'):
        t = R4._show(RELAY, PRE_RELAY, 'data/' + n) or ''
        m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', t)
        chk[n] = (int(m.group(1)), int(m.group(2))) if m else None
    log = [l.split(' ', 1) for l in g(PP, 'log', '--format=%h %s', '3dd4f29..' + PRE_PP).split(NL) if l.strip()]
    com = lambda pre: next((h for h, s in log if s.startswith(pre)), '?')   # noqa: E731
    rlog = [l.split(' ', 1) for l in g(RELAY, 'log', '--format=%h %s', '8c1f87dd..' + PRE_RELAY).split(NL) if l.strip()]
    rcom = lambda pre: next((h for h, s in rlog if s.startswith(pre)), '?')   # noqa: E731
    walk = json.loads(R4._show(RELAY, PRE_RELAY, 'data/b616_sim_walk.json'))
    return dict(CJ=CJ, DJ=DJ, H=H, S={k: v[0] for k, v in S.items()}, RL=RL, FJ=FJ, TJ=TJ, RS=RS, Z=Z, X=X, chk=chk, walk=walk,
                doc=com('b616 (R226)(3): '), rec=com('b616 (R226): '), stepzero=rcom('b616 step zero'), act=rcom('b616 -- LANE THREE'),
                closing=rcom('b616 closing'))


def weight616_lines():
    W = _b616()
    CJ = W['CJ']
    return ['### b616 AT ITS WEIGHT, printed from its banks at relay %s and its commits in PLACE-papers 3dd4f29..%s:' % (PRE_RELAY, PRE_PP),
            '    the document `%s` v0.1 at PLACE-papers %s, tier %s, %d claims: %s ; cert rows %d ; load-bearing %s' % (
                W['DJ']['path'], W['doc'], W['DJ']['tier'], CJ['n'], CJ['grades'], W['DJ']['cert_rows'], CJ['load_bearing'] or 'none'),
            '    the route %s matched %s ; H50c %s ; the T7 bank %s' % (CJ['routes'], CJ['matched'], CJ['h50c'], str(CJ['t7_bank'])[:200]),
            '    H50 bank: sentences %d, untraced %s, scanner clean %s, no-disclosure %s ; pages changed zeta %s chi %s' % (
                W['H']['sentences'], W['H']['untraced'] or 'none', W['H']['clean'], W['H']['nd_hits'], W['Z']['changed'], W['X']['changed']),
            '    the sequence: %d listed rows, %d conclusions ; the record lines %s ; FINDINGS entry :%d ; trail record :%d' % (
                W['RS']['listed'], len(W['RS']['conclusions']), [(x['file'], x['line']) for x in W['RL']['lines']], W['FJ']['entry_line'], W['TJ']['line']),
            '    the scores %s' % W['S'],
            '    the suite (arms run, live passing): pre-push %s, post-push %s, the kept run %s ; the walk %d files, %d outputs' % (
                W['chk']['b616_checks.txt'], W['chk']['b616_checks_postpush.txt'], W['chk']['b616_checks_attempt1.txt'],
                W['walk']['n_hits'], W['walk']['candidates']),
            '    PLACE-papers: the document %s, the record %s ; relay: step zero %s, the act %s, the closing %s' % (
                W['doc'], W['rec'], W['stepzero'], W['act'], W['closing'])]


# ================================================================================ READING (1): THE READS
SYN_ALL = {'1.2': K.SYN['1.2'], '1.5E': K.SYN['1.5E'], '2B': K.SYN['2B'],
           '2D': 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md',
           '2F': 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md',
           '2G': 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md'}
READS = [
    ('relay data/b616_routes_for_sieve.txt whole', RELAY, PRE_RELAY, 'data/b616_routes_for_sieve.txt', 'ALL', 900),
    ('the sieve v0.4 whole: the head`s counts, the groups, RH-60`s instrument line', PP, PRE_PP, SV4, 'ALL', 240),
] + [('the %s synthesis: its route rows' % k, PP, PRE_PP, p, ('GREP', r'^\| R\d+ \| |^### The routes through the five tests'), 600)
     for k, p in SYN_ALL.items()] + [
    ('the detector at v0.16', EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Detector.lean', [99, 100, 101], 300),
    ('epstein_not_h2_sign_cfg at v0.16', EFK, 'v0.16', 'SIDEExplicitFormula/Schema/Epstein.lean', [57, 58], 300),
    ('INVARIANCE_BARRIERS v1.4: Theorem 3.1 and Theorem 3.7 (tests 1 and 2)', PP, '1d0109f', K.IB, [148, 259], 400),
    ('INSTRUMENTS I-7 (test 1)', PP, '847e433', 'phase1.5/method/INSTRUMENTS.md', [93], 200),
    ('the forall_upto pair at v0.3 and li_nonneg_iff_rh at v0.9 (test 4)', EFK, 'v0.3', 'SIDEExplicitFormula/DetectionRegion.lean', [47, 52], 200),
    ('li_nonneg_iff_rh at v0.9', EFK, 'v0.9', 'SIDEExplicitFormula/LiCriterionBridge.lean', [179], 200),
    ('ERRATA.md`s form: the head and the last two entries', PP, PRE_PP, 'ERRATA.md', list(range(1, 21)) + list(range(865, 900)), 500),
] + [('%s: its function line' % n, PP, PRE_PP, p, ('GREP', re.escape(nd)), 500) for n, p, nd in LIVING] + [
    ('OPEN_TRAILS: the form, the precedence order, the sequence`s form, b616`s lines and record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 12228, 12566] + list(range(12727, 12752)), 2600),
    ('FINDINGS: b616`s weight line for b615 and b616`s entry', PP, PRE_PP, 'FINDINGS.md', list(range(7344, 7365)), 900),
    ('relay data/b616_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b616_closing_push_out.txt', 'ALL', 260),
]
FACT_LINES = [('SYMMETRY_FILTER.md', [62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 76, 82]),
              ('THEORY_SPACE.md', [18, 46, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 99, 108, 109, 110, 111, 112, 113, 114,
                                   115, 116, 117, 118, 298]),
              ('DARK_DELTA_MU.md', [37, 107]), ('FORMATION_DISTANCE.md', [100, 139]), ('T7_CMB.md', [106, 199]),
              ('QUATERNIONIC.md', [12, 125]), ('qec_kappa_v2.py', [17, 78])]
READS += [('the 2G line %s' % f, PP, PRE_PP, PS + f, ns, 500) for f, ns in FACT_LINES]


def reads(*a):
    L = ['b617 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
    L += [''] + weight616_lines()
    L += ['', '### THE LIVING DOCUMENTS` LAST COMMITS (git log -1 at PLACE-papers %s):' % PRE_PP]
    for n, p, _nd in LIVING:
        L.append('    %-24s %s' % (n, g(PP, 'log', '-1', '--format=%h %ad %s', '--date=short', PRE_PP, '--', p).strip()[:200]))
    L += ['### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(),
                                                                    g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b617_reads.txt', L)


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
    L = ['### b617 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-04), banked verbatim with the options and the '
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
    put_txt('b617_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b617_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b617_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


# ================================================================================ COMPONENT 1: THE ARITHMETIC
def arith(*a):
    """### data/b617_arith.txt and its json: (R227)(2)'s 2G computations, each computed here from the papers' own tables."""
    import itertools
    import math
    import numpy as np
    import b616_claims as C6   # ### its tables and helpers, read only; arith2g is not called (it reads a remote)
    n_c, n_p = sum(b[1] for b in C6.SF_BINS), sum(b[2] for b in C6.SF_BINS)
    d = [b[0] for b in C6.SF_BINS]
    rate = [b[2] / b[1] for b in C6.SF_BINS]
    r, slope, icpt = C6._pearson(d, rate)
    rs = C6._pearson(C6._rank(d), C6._rank(rate))[0]
    nT = sum(C6.TH_DOMAINS)
    ni = sum(c for c, _v in C6.TH_IDS)
    wm = sum(c * v for c, v in C6.TH_IDS) / ni
    um = sum(v for _c, v in C6.TH_IDS) / len(C6.TH_IDS)
    lines = [(0, 1, 3), (1, 2, 4), (2, 3, 5), (3, 4, 6), (4, 5, 0), (5, 6, 1), (6, 0, 2)]
    N = np.zeros((7, 7))
    for j, ln in enumerate(lines):
        for i in ln:
            N[i, j] = 1
    evN = sorted(np.linalg.eigvals(N), key=lambda z: -abs(z))
    modN = [round(float(abs(z)), 4) for z in evN]
    nnt = [round(float(x), 4) for x in sorted(np.linalg.eigvalsh(N @ N.T))]
    k7 = [round(float(x), 4) for x in sorted(np.linalg.eigvalsh(np.ones((7, 7)) - np.eye(7)))]
    order, orb, stab, orbs, perms = C6._gl32()
    H = np.array([[0, 0, 0, 1, 1, 1, 1], [0, 1, 1, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0, 1]])
    cw = [b for b in itertools.product((0, 1), repeat=7) if not ((H @ np.array(b)) % 2).any()]
    idx = lambda b: int(''.join(map(str, b)), 2)   # noqa: E731
    z = np.zeros(128, complex)
    o = np.zeros(128, complex)
    for b in cw:
        (z if sum(b) % 2 == 0 else o)[idx(b)] = 1 / np.sqrt(8)
    t7 = np.array([np.exp(1j * np.pi / 4 * bin(i).count('1')) for i in range(128)])
    tz = t7 * z
    ov0, ov1 = np.vdot(z, tz), np.vdot(o, tz)
    norm = math.hypot(abs(ov0), abs(ov1))
    A = dict(sf=dict(constants=n_c, psmooth=n_p, not_psmooth=n_c - n_p, pearson=round(r, 4), slope=round(slope, 4), icpt=round(icpt, 4),
                     spearman=round(rs, 4)),
             th=dict(theories=nT, ids=ni, weighted=round(wm, 4), unweighted=round(um, 4)),
             fano=dict(mod_N=modN, NNt=nnt, K7=k7),
             gl32=dict(order=order, orbit=orb, stabilizer=stab, orbits=orbs + [1], perms=perms),
             steane=dict(codewords=len(cw), ov0=[round(float(ov0.real), 4), round(float(ov0.imag), 4)], ov1=round(float(abs(ov1)), 4),
                         norm=round(norm, 4)))
    L = ['b617 -- COMPONENT 1: THE ARITHMETIC OF (R227)(2), the 2G papers` findings, computed %s (Python %s, numpy %s), from the papers` own '
         'tables as b616`s claims module carries them (tools/b616_claims.py, read only)' % (utc(), sys.version.split()[0], np.__version__), '',
         '### (i) SYMMETRY_FILTER :64-:74, the bins table, summed against :62 and :82 (439 constants, five violations):',
         '    constants %d ; P-smooth %d ; not P-smooth %d.' % (n_c, n_p, n_c - n_p),
         '    THE FACT OF RECORD: the table sums to %d constants with %d not P-smooth; the paper states 439 and 5 -- ERRATA %s.' % (n_c, n_c - n_p, ERR_IDS[0]), '',
         '### (ii) THEORY_SPACE :50-:64, the domain counts, against :46, :65 and :298 (375); :108-:118, the per-domain values, against :18 and :99 (0.918):',
         '    the domain counts sum to %d ; the I∩D∩S counts to %d ; the count-weighted mean %.4f ; the unweighted mean over the eleven domains %.4f.' % (nT, ni, wm, um),
         '    THE FACT OF RECORD: %d theories, not 375; the count-weighted mean %.3f, not 0.918 -- ERRATA %s.' % (nT, wm, ERR_IDS[1]), '',
         '### (iii) SYMMETRY_FILTER :76 (the linear fit, r = −0.66) and the −0.66 called Spearman ρ at DARK_DELTA_MU :37 and FORMATION_DISTANCE :139:',
         '    over the nine bins, rate against distance: least squares rate = %.3f − %.4f × distance ; Pearson r = %.3f ; Spearman ρ = %.3f.' % (icpt, -slope, r, rs),
         '    THE FACT OF RECORD: −0.66 is the Pearson r of SYMMETRY_FILTER`s fit; the Spearman ρ over the bins is %.3f -- ERRATA %s at the two citing papers.' % (rs, ERR_IDS[2]), '',
         '### (iv) T7_CMB :106 and :199, “the Fano incidence matrix” with eigenvalues 3 once and −1 six times:',
         '    the incidence matrix N (lines {0, 1, 3} + k mod 7): the moduli of its eigenvalues %s ; N Nᵀ = 2I + J, its eigenvalues %s ; the '
         'collinearity graph K₇ (J − I), its eigenvalues %s.' % (modN, nnt, k7),
         '    THE FACT OF RECORD: N has 3 once and six eigenvalues of modulus √2; K₇ has 6 once and −1 six times; the pair 3 and −1 six times '
         'is the spectrum of neither -- its 3 is N`s and its −1 six times K₇`s. (b616`s reading, that the pair belongs to K₇, is corrected here: '
         'its own bank prints λ(K₇) with 6 once.)', '',
         '### (v) QUATERNIONIC :12 and :125, DARK_DELTA_MU :107, FORMATION_DISTANCE :100: the diagonal`s stabilizer S₃ (or a parabolic) with orbits (3, 3, 1):',
         '    GL(3, 𝔽₂) enumerated: order %d ; the orbit of a non-zero vector %d ; the stabilizer of (1, 1, 1) of order %d ; its orbits on the seven '
         'non-zero vectors %s ; the coordinate permutations inside it %d.' % (order, orb, stab, orbs + [1], perms),
         '    THE FACT OF RECORD: the stabilizer has order 24, not 6, contains S₃ as its coordinate permutations, and its orbits are (6, 1).', '',
         '### (vi) qec_kappa_v2.py :17 and :78, transversal T read as a logical T on the Steane code:',
         '    the [7, 4, 3] code`s %d codewords ; T on all seven qubits applied to |0_L⟩: ⟨0_L|T⊗7|0_L⟩ = %.3f%+.3fi ; ⟨1_L|T⊗7|0_L⟩ = %.3f ; '
         'the norm kept in the code space %.3f.' % (len(cw), ov0.real, ov0.imag, abs(ov1), norm),
         '    THE FACT OF RECORD: T⊗7 keeps %.3f of the norm of |0_L⟩ in the code space, so it is not a logical gate on the Steane code.' % norm]
    put_txt('b617_arith.txt', L)
    put_json('b617_arith.json', dict(at=utc(), **A))
    for l in L:
        print(l[:220])


# ================================================================================ COMPONENT 1: THE ERRATA, THE FACT ITEMS, THE CURRENCY
B616_ENTRY = '## The 2G synthesis: the local–cosmic interface and the dark sector at v0.1 from p2-d1 to p2-d9'
B616_TRAIL = '### b616 — lane three, act forty-three under (R226): the synthesis for 2G, the sequence’s last'
CONSOL = ('*Appended 2026-10-04 by b616 to the synthesis sequence’s form (:12566), under `(R226)`(4) -- THE CONSOLIDATION, THE ACTS AFTER THE '
          'SEQUENCE, IN ORDER, EACH ON THE AUTHOR’S WORD AT ITS CLOSING:*')
F_HEAD = ('*Appended 2026-10-04 by b617 to b616’s record (:%d), under `(R227)`(2) -- THE 2G PAPERS’ FINDINGS, FACT ITEMS FOR THEIR NEXT EDITIONS, '
          'THREE OF THEM ERRATA, THE SYNTHESIS’S ROWS STANDING AS GRADED:*')
C_HEAD = ('*Appended 2026-10-04 by b617 to the consolidation (:%d), under `(R227)`(3) and (5) -- THE LIVING DOCUMENTS’ CURRENCY, ENTERED AS b618, '
          'BEFORE THE CENSUS’S v0.4, PRICED BY COUNT:*')
W_HEAD = '*Appended 2026-10-04 by b617 to b616’s entry (:%d), under `(R227)`(1) -- b616 AT ITS WEIGHT:*'


def _arithj(dry=False):
    A = json.load(io.open(os.path.join(SP if dry else D, 'b617_arith.json'), encoding='utf-8'))
    for k in ('spearman', 'pearson'):   # ### the house minus sign in the ledgers' figures
        A['sf'][k + '_s'] = ('%.3f' % A['sf'][k]).replace('-', '−')
    return A


def _deposited(needles):
    """### every needle searched under PLACE-papers outputs/ (the deposited mirror), tracked files"""
    out = {}
    for nd in needles:
        r = subprocess.run(['git', '-C', PP, 'grep', '-n', '-F', nd, PRE_PP, '--', 'outputs'], capture_output=True)
        out[nd] = [x for x in r.stdout.decode('utf-8', 'replace').split(NL) if x.strip()]
    return out


DEP_NEEDLES = ('439 constants', 'exactly 5 are violations', '375 physical theories', '**375**', 'Mean α_T | 0.918', 'Spearman ρ = −0.66')


def _errata_blocks(fact_line, dry=False):
    A = _arithj(dry)
    sf, th = A['sf'], A['th']
    dep = 'searched at PLACE-papers %s for “439 constants”, “exactly 5 are violations”, “375 physical theories”, “**375**”, “Mean α_T | 0.918” and ' \
          '“Spearman ρ = −0.66”' % PRE_PP
    e5 = ['## %s — SYMMETRY_FILTER :62 and :82 count 439 constants and five violations of P-smooth structure, where its own bins table (:64-:74) '
          'sums to %d constants with %d not P-smooth (CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)' % (ERR_IDS[0], sf['constants'], sf['not_psmooth']), '',
          '**Filed 2026-10-04 by b617, on the author’s ruling `(R227)`(2); found at b616 (relay `data/b616_claims_2G.txt`, SF-10), computed at b617 '
          '(relay `data/b617_arith.txt`). Record affected: `%sSYMMETRY_FILTER.md` :62, :82. ### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY: no '
          'file under `outputs/` carries these sentences (%s).**' % (PS, dep), '',
          '**What the lines say.** :62: *“We organize 439 constants into 9 bins by their \"distance\" from local physics (0 = electroweak core, 8 = '
          'dark sector).”*; :82: *“Of 439 constants tested for P-smooth structure, exactly 5 are violations (1.1%).”*', '',
          '**What is true.** The table at :64-:74 lists nine bins whose constants sum to %d and whose P-smooth counts sum to %d, so %d of its '
          'constants are not P-smooth (relay `data/b617_arith.txt`).' % (sf['constants'], sf['psmooth'], sf['not_psmooth']), '',
          '**The correction.** The counts the paper’s own table carries are %d constants and %d not P-smooth. Where 439 and five are counted over a '
          'population the table does not show, the paper’s next edition names that population; this entry corrects the counting sentences against '
          'the table and does not choose the population.' % (sf['constants'], sf['not_psmooth']), '',
          '**Scope.** No line is edited: SYMMETRY_FILTER takes the correction at its next edition as a fact item (OPEN_TRAILS :%d), and the citing '
          'lines that repeat 439 (DARK_DELTA_MU :37, FORMATION_DISTANCE :139) take it beside the entry filed after this one for their Spearman ρ. '
          'No banked number, verdict or grade moves. Nothing here is a statement about RH or any zero.' % fact_line, '',
          '**Status.** FILED.', '']
    e6 = ['## %s — THEORY_SPACE :46, :65 and :298 total 375 theories, where its domain rows (:50-:64) sum to %d, and :18 and :99 give the mean α_T '
          'as 0.918, where its per-domain table (:108-:118) gives a count-weighted mean of %.3f (CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)' % (
              ERR_IDS[1], th['theories'], th['weighted']), '',
          '**Filed 2026-10-04 by b617, on the author’s ruling `(R227)`(2); found at b616 (relay `data/b616_claims_2G.txt`, TH-01, TH-04), computed at '
          'b617 (relay `data/b617_arith.txt`). Record affected: `%sTHEORY_SPACE.md` :18, :46, :65, :99, :298. ### NO DEPOSITED ARTIFACT IS AFFECTED BY '
          'THIS ENTRY: no file under `outputs/` carries these sentences (%s).**' % (PS, dep), '',
          '**What the lines say.** :46: *“375 physical theories selected from 15 domains:”*; :65: *“| **Total** | **375** | |”*; :18: *“α_T = 0.918 ± '
          '0.018 (CV = 2.0%)”*; :99: *“| Mean α_T | 0.918 |”*.', '',
          '**What is true.** The fifteen domain rows at :50-:64 sum to %d. The per-domain table at :108-:118 gives the I∩D∩S counts summing to %d, as '
          ':94 says, and their count-weighted mean α_T is %.4f; the unweighted mean over its eleven domains is %.4f (relay `data/b617_arith.txt`).' % (
              th['theories'], th['ids'], th['weighted'], th['unweighted']), '',
          '**The correction.** At :46, :65 and :298 the total of record is %d theories, the sum of the paper’s own rows. At :18 and :99 the mean the '
          'per-domain table reproduces is %.3f; the stated 0.918 is not reproduced from the table at three decimals, and the paper’s next edition '
          'prints the fourteen values its mean is taken over.' % (th['theories'], th['weighted']), '',
          '**Scope.** No line is edited: THEORY_SPACE takes the correction at its next edition as a fact item (OPEN_TRAILS :%d). No banked number, '
          'verdict or grade moves. Nothing here is a statement about RH or any zero.' % fact_line, '',
          '**Status.** FILED.', '']
    e7 = ['## %s — DARK_DELTA_MU :37 and FORMATION_DISTANCE :139 call the −0.66 of the P-smooth degradation a Spearman ρ, where it is '
          'SYMMETRY_FILTER’s Pearson r (:76) and the Spearman ρ over the same nine bins is %s (CORPUS-FACING; NO DEPOSITED ARTIFACT IS AFFECTED)' % (
              ERR_IDS[2], sf['spearman_s']), '',
          '**Filed 2026-10-04 by b617, on the author’s ruling `(R227)`(2); found at b616 (relay `data/b616_claims_2G.txt`, DM-02), computed at b617 '
          '(relay `data/b617_arith.txt`). Records affected: `%sDARK_DELTA_MU.md` :37 and `%sFORMATION_DISTANCE.md` :139. ### NO DEPOSITED ARTIFACT IS '
          'AFFECTED BY THIS ENTRY: no file under `outputs/` carries these sentences (%s).**' % (PS, PS, dep), '',
          '**What the lines say.** DARK_DELTA_MU :37: *“### 2. P-smooth Degradation (439 constants, Spearman ρ = −0.66)”*; FORMATION_DISTANCE :139: '
          '*“| P-smooth degradation (439 constants) | 100% local to 50% dark | Spearman ρ = −0.66 |”*; the source, SYMMETRY_FILTER :76: *“The linear '
          'fit gives kappa = 1.047 minus 0.039 times distance, with correlation r = minus 0.66.”*', '',
          '**What is true.** Over the nine bins of SYMMETRY_FILTER :64-:74, the least-squares line of the P-smooth rate against distance is rate = '
          '%.3f − %.4f × distance with Pearson r = %s, and the Spearman rank correlation is ρ = %s (relay `data/b617_arith.txt`).' % (
              sf['icpt'], -sf['slope'], sf['pearson_s'], sf['spearman_s']), '',
          '**The correction.** At DARK_DELTA_MU :37 and FORMATION_DISTANCE :139 the statistic of record is the Pearson r = −0.66 of SYMMETRY_FILTER’s '
          'fit; read as a Spearman ρ it is %s. The count 439 in both lines takes %s beside this entry.' % (sf['spearman_s'], ERR_IDS[0]), '',
          '**Scope.** No line is edited: the two papers take the correction at their next editions as a fact item (OPEN_TRAILS :%d). No banked '
          'number, verdict or grade moves. Nothing here is a statement about RH or any zero.' % fact_line, '',
          '**Status.** FILED.', '']
    return [(ERR_IDS[0], e5), (ERR_IDS[1], e6), (ERR_IDS[2], e7)]


# ### the b618 pricing: each item the ruling names, located by needle at PLACE-papers or relay; counted, never inferred
CUR_INSTR = [   # ### (the ruling's item, where, the line, the needle the line holds)
    ('the edition form', 'OPEN_TRAILS', 11864, 'THE FORM OF AN EDITION, STANDING FOR CP-7'),
    ('the edition form: H28b restated', 'OPEN_TRAILS', 11902, 'H28b, RESTATED FOR EVERY EDITION ACT'),
    ('the edition form: the stem clause', 'OPEN_TRAILS', 11904, 'THE STEM CLAUSE, STANDING'),
    ('the edition form: the ceiling clause', 'OPEN_TRAILS', 11906, 'THE CEILING CLAUSE'),
    ('the edition form: the history clause', 'OPEN_TRAILS', 11908, 'THE HISTORY CLAUSE'),
    ('the edition form: H28b final form', 'OPEN_TRAILS', 11930, 'H28b, FINAL FORM FOR EVERY EDITION ACT'),
    ('the edition form: the re-pin step', 'OPEN_TRAILS', 11932, 'THE RE-PIN STEP, THE FORM’S LAST'),
    ('the edition form: the name-and-title exception', 'OPEN_TRAILS', 11934, 'THE NAME-AND-TITLE EXCEPTION'),
    ('the edition form: the fact clause', 'OPEN_TRAILS', 11954, 'THE FACT CLAUSE, STANDING'),
    ('the edition form: the placement clause', 'OPEN_TRAILS', 11956, 'THE PLACEMENT CLAUSE'),
    ('the edition form: inside a dated entry', 'OPEN_TRAILS', 12044, 'INSIDE A DATED ENTRY THE HISTORY CLAUSE GOVERNS'),
    ('the edition form: an item name', 'OPEN_TRAILS', 12082, 'AN ITEM NAME OF A CITED PROGRAMME DOCUMENT'),
    ('the edition form: the page clause', 'OPEN_TRAILS', 12190, 'THE PAGE CLAUSE'),
    ('the edition form: the restatement clause', 'OPEN_TRAILS', 12192, 'THE RESTATEMENT CLAUSE'),
    ('the edition form: an era annotation', 'OPEN_TRAILS', 12194, 'AN ERA ANNOTATION IS A DATED ENTRY'),
    ('the edition form: H28b for a reorganising edition', 'OPEN_TRAILS', 12456, 'H28b FOR A REORGANISING EDITION'),
    ('the edition form: multi-act editions', 'OPEN_TRAILS', 12496, 'A CLAUSE OF THE FORM FOR MULTI-ACT EDITIONS'),
    ('the precedence order', 'OPEN_TRAILS', 12228, 'THE PRECEDENCE ORDER'),
    ('the frozen control', 'OPEN_TRAILS', 12300, '(2) Defect (f) repaired, the control frozen.'),
    ('the five tests', 'relay', 'data/b604_author_answers.txt', 'five tests'),
    ('the pin-resolution rule', 'FINDINGS', 7278, 'THE PIN-RESOLUTION RULE'),
    ('the load-bearing rule', 'OPEN_TRAILS', 12699, 'THE FORM’S FOURTH CLAUSE, THE KC TIER’S LOAD-BEARING CLAUSE'),
    ('the one-read rule', 'OPEN_TRAILS', 12703, 'THE SUITE’S REMOTE READS, STANDING'),
]
CUR_INSTR_UNLOCATED = ['the generator’s channels']
CUR_FORM = [x for x in CUR_INSTR if x[0].startswith('the edition form')]
CUR_FACES = [('simplicity', 'simplicity_iff', 'v0.17'), ('product', 'productLemma_holds', 'v0.18'), ('doubling', 'doubling_holds', 'v0.19'),
             ('Keiper', 'keiperTaylorIdentity_of', 'v0.19'), ('the window', 'plateauRampWindow_of', 'v0.20'), ('family', 'family_theorem', 'v0.21')]
CUR_REG = [('the row addition given the word: THE_RIEMANN_PATHS_CLUSTER_SPINE.md', 'OPEN_TRAILS', 12645, 'THE_RIEMANN_PATHS_CLUSTER_SPINE.md'),
           ('the disagreement REGISTRY :787 against :333', 'OPEN_TRAILS', 12599, ':787'),
           ('the disagreement SPIRAL_MAP :104 against REGISTRY :731', 'OPEN_TRAILS', 12599, ':731')]
CANON_FORMS = [('the located-clause method’s form (its document at TECHNE-Core by pointer; the public entry)', 'FINDINGS', 6760,
                '## The located-clause method:'),
               ('the edition form', 'OPEN_TRAILS', 11864, 'THE FORM OF AN EDITION, STANDING FOR CP-7')]


def _ledger(name):
    p = {'OPEN_TRAILS': 'OPEN_TRAILS.md', 'FINDINGS': 'FINDINGS.md'}[name]
    return K.lines_of(R4._show(PP, PRE_PP, p))


def _loc(where, line, needle):
    if where == 'relay':
        t = R4._show(RELAY, PRE_RELAY, line) or ''
        return needle in t
    ls = _ledger(where)
    return 0 < line <= len(ls) and needle in ls[line - 1]


def currency(*a):
    """### data/b617_currency.txt and its json: the eight living documents, each with its function line and last commit, and the items
    ### (R227)(3) names under its function since that commit, located and counted -- the price of b618."""
    out, L = {}, ['b617 -- COMPONENT 1: THE LIVING DOCUMENTS` CURRENCY, PRICED FOR b618 UNDER (R227)(3), at PLACE-papers %s and relay %s (%s)' % (
        PRE_PP, PRE_RELAY, utc()), '']
    tx = {n: K.lines_of(R4._show(PP, PRE_PP, p)) for n, p, _nd in LIVING}
    for n, p, nd in LIVING:
        fl = next(((i + 1, l) for i, l in enumerate(tx[n]) if l.startswith(nd)), (0, '### NO FUNCTION LINE'))
        lc = g(PP, 'log', '-1', '--format=%h|%ad|%s', '--date=short', PRE_PP, '--', p).strip().split('|', 2)
        out[n] = dict(path=p, function_line=fl[0], function=fl[1][:400], last=lc[0], last_date=lc[1], last_subject=lc[2][:120])
    # ### the loom: every suite verdict bank since b537 in relay, against the loom's own text
    banks = sorted(x for x in g(RELAY, 'ls-tree', '-r', '--name-only', PRE_RELAY, 'data/').split(NL)
                   if re.match(r'^data/b(\d{3})_(checks|arms_prerun)', x) and 537 <= int(re.match(r'^data/b(\d{3})', x).group(1)) <= 616)
    acts = sorted(set(re.match(r'^data/(b\d{3})', x).group(1) for x in banks))
    kept = [x for x in banks if 'attempt' in x]
    loom_mentions = sum(1 for l in tx['VERIFICATION_LOOM'] for a_ in acts if a_ in l)
    out['VERIFICATION_LOOM'].update(items=dict(acts=len(acts), banks=len(banks), kept_failed=len(kept), loom_mentions=loom_mentions,
                                               first=acts[0] if acts else None, last=acts[-1] if acts else None))
    # ### INSTRUMENTS: the ruling's list, each located by its needle
    inst = [dict(item=i, where=w, line=ln, ok=_loc(w, ln, nd)) for i, w, ln, nd in CUR_INSTR]
    inst_in = sum(1 for l in tx['INSTRUMENTS'] for nd in ('PRECEDENCE ORDER', 'LOAD-BEARING', 'one-read', 'FORM OF AN EDITION') if nd in l)
    out['INSTRUMENTS'].update(items=dict(located=inst, unlocated=CUR_INSTR_UNLOCATED, kinds=8, form_clauses=len(CUR_FORM) - 1,
                                         in_document=inst_in))
    # ### the canon and the method-as-it-stands: the two forms
    forms = [dict(item=i, where=w, line=ln, ok=_loc(w, ln, nd)) for i, w, ln, nd in CANON_FORMS]
    for n in ('THE_METHOD_CANON', 'THE_METHOD_AS_IT_STANDS'):
        out[n].update(items=dict(forms=forms, form_clauses=len(CUR_FORM) - 1,
                                 in_document=sum(1 for l in tx[n] if 'FORM OF AN EDITION' in l or 'located-clause' in l.lower())))
    # ### FACES_LEDGER: the faces added at v0.17-v0.21, each looked up by its declaration's name
    fl_t = NL.join(tx['FACES_LEDGER'])
    out['FACES_LEDGER'].update(items=dict(faces=[dict(face=f, decl=d, pin=v, in_ledger=d in fl_t) for f, d, v in CUR_FACES]))
    # ### the load-bearing map: the page nodes at v0.21, each looked up by its short name
    mp = NL.join(tx['THE_LOAD_BEARING_MAP'])
    import chain_page as CP
    nodes = []
    for k in ('zeta', 'chi'):
        nodes += [x['name'] for x in CP.read_nodes(os.path.join(D, NODES[k]))[0] if x['source'] == 'kernel']   # ### the generator's own reader
    short = sorted(set(x.split('.')[-1] for x in nodes))
    absent = [s for s in short if s not in mp]
    out['THE_LOAD_BEARING_MAP'].update(items=dict(nodes=len(short), absent=len(absent), absent_names=absent))
    # ### GAUGE_AND_INVARIANT: the ruling names no item; the trails since its last commit searched for its own words
    gl = [i + 1 for i, l in enumerate(_ledger('OPEN_TRAILS')) if i + 1 > 9000 and l.startswith('*Appended 2026-')
          and re.search(r'GAUGE|REPRESENTATION-DEPENDEN|representation-dependen', l[:400])]
    out['GAUGE_AND_INVARIANT'].update(items=dict(named=0, trail_heads=gl))
    # ### REGISTRY: the ruling's three items, and the documents added since its last commit that it does not name
    reg = [dict(item=i, where=w, line=ln, ok=_loc(w, ln, nd)) for i, w, ln, nd in CUR_REG]
    rt = NL.join(tx['REGISTRY'])
    added = [x for x in g(PP, 'diff', '--name-only', '--diff-filter=A', out['REGISTRY']['last'], PRE_PP).split(NL)
             if x.endswith('.md') and (x.startswith('phase') or x.startswith('day1/') or '/' not in x)]
    unnamed = [x for x in added if os.path.basename(x) not in rt]
    ctl = [x for x in g(PP, 'ls-tree', '-r', '--name-only', out['REGISTRY']['last']).split(NL)   # ### the control: the same test on the
           if x.endswith('.md') and (x.startswith('phase') or x.startswith('day1/'))]          # ### documents present at its last commit
    out['REGISTRY'].update(items=dict(ruled=reg, added_since=len(added), unnamed=unnamed, control=(sum(1 for x in ctl if os.path.basename(x) in rt), len(ctl))))
    for n, _p, _nd in LIVING:
        o = out[n]
        L += ['### %s -- `%s`' % (n, o['path']),
              '    function line :%d %s' % (o['function_line'], o['function'][:300]),
              '    last commit %s %s -- %s' % (o['last'], o['last_date'], o['last_subject'])]
        it = o['items']
        if n == 'VERIFICATION_LOOM':
            L.append('    since b537 (%s to %s): %d acts with a suite verdict bank in relay, %d bank files, %d of them kept failed runs (`attempt`); the '
                     'loom names %d of those acts' % (it['first'], it['last'], it['acts'], it['banks'], it['kept_failed'], it['loom_mentions']))
            o['price'] = it['acts']
        elif n == 'INSTRUMENTS':
            L += ['    %-52s %s :%s %s' % (x['item'], x['where'], x['line'], 'LOCATED' if x['ok'] else '### NOT LOCATED') for x in it['located']]
            L.append('    not located on the ledgers: %s ; the document names %d of the located items' % (it['unlocated'], it['in_document']))
            o['price'] = len(it['located']) + len(it['unlocated'])
        elif n in ('THE_METHOD_CANON', 'THE_METHOD_AS_IT_STANDS'):
            L += ['    %-52s %s :%s %s' % (x['item'][:52], x['where'], x['line'], 'LOCATED' if x['ok'] else '### NOT LOCATED') for x in it['forms']]
            L.append('    the edition form`s clauses on the trails: %d ; the document names either form on %d lines' % (it['form_clauses'], it['in_document']))
            o['price'] = len(it['forms'])
        elif n == 'FACES_LEDGER':
            L += ['    %-12s `%s` (%s) in the ledger: %s' % (x['face'], x['decl'], x['pin'], x['in_ledger']) for x in it['faces']]
            o['price'] = sum(1 for x in it['faces'] if not x['in_ledger'])
        elif n == 'THE_LOAD_BEARING_MAP':
            L.append('    the two pages` kernel nodes (b602`s ζ list, b603`s χ list, read by chain_page.read_nodes, by short name): %d ; absent from the map %d -- %s' % (
                it['nodes'], it['absent'], ', '.join(it['absent_names'])[:1500]))
            o['price'] = it['absent']
        elif n == 'GAUGE_AND_INVARIANT':
            L.append('    the ruling names no item; trail heads since :9000 naming gauge or representation-dependence: %s' % (it['trail_heads'] or 'NONE'))
            o['price'] = len(it['trail_heads'])
        elif n == 'REGISTRY':
            L += ['    %-60s %s :%s %s' % (x['item'][:60], x['where'], x['line'], 'LOCATED' if x['ok'] else '### NOT LOCATED') for x in it['ruled']]
            L.append('    documents added since %s: %d ; not named in REGISTRY %d -- %s' % (o['last'], it['added_since'], len(it['unnamed']),
                                                                                       ', '.join(it['unnamed'])[:1500]))
            L.append('    the control, the same basename test on the phase and day1 documents present at %s: named %d of %d' % (
                o['last'], it['control'][0], it['control'][1]))
            o['price'] = len(it['ruled']) + len(it['unnamed'])
        L += ['    ### THE PRICE: %d' % o['price'], '']
    L += ['### FACT, the navigator`s: THE_METHOD_CANON`s last commit is %s %s (%s), not 2026-09-08; its version line still reads v1.3.' % (
        out['THE_METHOD_CANON']['last'], out['THE_METHOD_CANON']['last_date'], out['THE_METHOD_CANON']['last_subject'][:60]),
          '### ### **THE PRICES: %s.**' % ', '.join('%s %d' % (n, out[n]['price']) for n, _p, _nd in LIVING)]
    put_txt('b617_currency.txt', L)
    put_json('b617_currency.json', dict(at=utc(), docs=out))
    print(L[-1])


def _texts(trail, consol, dry=False):
    A = _arithj(dry)
    CU = json.load(io.open(os.path.join(SP if dry else D, 'b617_currency.json'), encoding='utf-8'))['docs']
    fa, gl, st = A['fano'], A['gl32'], A['steane']
    tf = ('\n%s (i) phase2/physics-speculative/SYMMETRY_FILTER.md :62 and :82 count 439 constants and five violations, where its bins table '
          '(:64-:74) sums to %d constants with %d not P-smooth -- ERRATA %s. (ii) THEORY_SPACE :46, :65 and :298 total 375 theories, where its domain '
          'rows sum to %d, and :18 and :99 give the mean α_T 0.918, where the per-domain table’s count-weighted mean is %.3f -- ERRATA %s. (iii) '
          'DARK_DELTA_MU :37 and FORMATION_DISTANCE :139 call the −0.66 a Spearman ρ, where it is SYMMETRY_FILTER’s Pearson r (:76) and the Spearman '
          'ρ over the bins is %s -- ERRATA %s at the two citing papers. (iv) T7_CMB :106 and :199 give the Fano incidence eigenvalues as 3 once '
          'and −1 six times, where the incidence matrix has 3 once and six of modulus √2 and the collinearity graph K₇ has 6 once and −1 six times, '
          'the pair matching neither -- its 3 the incidence matrix’s and its −1 six times K₇’s; a fact item, b616’s reading that the pair is K₇’s '
          'corrected by the seat (b616’s own bank prints K₇’s top eigenvalue as 6). (v) QUATERNIONIC :12 and :125, DARK_DELTA_MU :107 and '
          'FORMATION_DISTANCE :100 name the diagonal’s stabilizer S₃ or a parabolic with orbits (3, 3, 1), where in GL(3, 𝔽₂), of order %d, the '
          'stabilizer of (1, 1, 1) has order %d, holds the %d coordinate permutations, and has orbits (6, 1); a fact item joining '
          'MATTER_AS_ARITHMETIC :111’s (:12701) at the 2D and 2G editions. (vi) phase2/physics-speculative/qec_kappa_v2.py :17 and :78 read T on all '
          'seven qubits as a logical T, where T⊗7 keeps %.3f of the norm of the logical zero in the code space, so it is not a logical gate on the '
          'Steane code; a fact item on the simulator. The computations are banked at relay data/b617_arith.txt. The synthesis’s rows for these '
          'claims (SF-01, SF-02, SF-10, TH-01, TH-04, DM-02, TC-09, TC-15, QD-04, QD-13, DM-08, QV-01, QV-03) stand at the grades b616 gave them.\n' % (
              F_HEAD % trail, A['sf']['constants'], A['sf']['not_psmooth'], ERR_IDS[0], A['th']['theories'], A['th']['weighted'], ERR_IDS[1],
              A['sf']['spearman_s'], ERR_IDS[2], gl['order'], gl['stabilizer'], gl['perms'], st['norm']))
    pr = lambda n: CU[n]['price']   # noqa: E731
    lc = lambda n: '%s %s' % (CU[n]['last'], CU[n]['last_date'])   # noqa: E731
    it = lambda n: CU[n]['items']   # noqa: E731
    tc = ('\n%s b618, the act after the sieve’s v0.5 and before the census’s v0.4: each living document read for its own function line and every '
          'item since its last commit that falls under that function listed by act and line, then the author’s word per document, at b618’s '
          'prompt with the seat’s recommendation printed, between a dated append in the document’s own form carrying what it missed and a dated '
          'line stating that its function has moved and naming where; no document retired, none created. The prices, by count (relay '
          'data/b617_currency.txt): VERIFICATION_LOOM (the verification log, :%d; last %s) -- %d acts since b537 with suite verdict banks in relay, '
          '%d bank files, %d of them kept failed runs, the loom naming %d of those acts; INSTRUMENTS (:%d; last %s) -- %d items located on the '
          'ledgers (the edition form and %d of its clauses, the precedence order, the frozen control, the five tests, the pin-resolution, '
          'load-bearing and one-read rules) and %d the seat did not locate (the generator’s channels); THE_METHOD_CANON (:%d; last %s, b588’s '
          'census / totality append, not 2026-09-08 -- the navigator’s, its version line still v1.3) and THE_METHOD_AS_IT_STANDS (:%d; last %s) -- '
          'the two forms each, the located-clause method’s by its public entry (FINDINGS :6760) and the edition form with its %d clauses; '
          'FACES_LEDGER (:%d; last %s) -- %d of the six faces of v0.17-v0.21 absent by their declarations’ names; THE_LOAD_BEARING_MAP (:%d; last '
          '%s) -- %d of the two pages’ %d kernel nodes absent by name; GAUGE_AND_INVARIANT (:%d; last %s) -- the ruling names no item and the trails’ '
          'heads since its last commit name none, a price of %d; REGISTRY (:%d; last %s) -- the row addition given the word (:12645) and the two '
          'disagreements (:12599), with %d documents added since its last commit that it does not name. One act; no Lean call.\n' % (
              C_HEAD % consol,
              CU['VERIFICATION_LOOM']['function_line'], lc('VERIFICATION_LOOM'), it('VERIFICATION_LOOM')['acts'], it('VERIFICATION_LOOM')['banks'],
              it('VERIFICATION_LOOM')['kept_failed'], it('VERIFICATION_LOOM')['loom_mentions'],
              CU['INSTRUMENTS']['function_line'], lc('INSTRUMENTS'), sum(1 for x in it('INSTRUMENTS')['located'] if x['ok']),
              it('INSTRUMENTS')['form_clauses'], len(it('INSTRUMENTS')['unlocated']),
              CU['THE_METHOD_CANON']['function_line'], lc('THE_METHOD_CANON'), CU['THE_METHOD_AS_IT_STANDS']['function_line'],
              lc('THE_METHOD_AS_IT_STANDS'), it('THE_METHOD_CANON')['form_clauses'],
              CU['FACES_LEDGER']['function_line'], lc('FACES_LEDGER'), pr('FACES_LEDGER'),
              CU['THE_LOAD_BEARING_MAP']['function_line'], lc('THE_LOAD_BEARING_MAP'), pr('THE_LOAD_BEARING_MAP'), it('THE_LOAD_BEARING_MAP')['nodes'],
              CU['GAUGE_AND_INVARIANT']['function_line'], lc('GAUGE_AND_INVARIANT'), pr('GAUGE_AND_INVARIANT'),
              CU['REGISTRY']['function_line'], lc('REGISTRY'), len(it('REGISTRY')['unnamed'])))
    return [(F_HEAD % trail, tf), (C_HEAD % consol, tc)]


def _weight(entry, fline, cline):
    W = _b616()
    CJ, gr, S = W['CJ'], W['CJ']['grades'], W['S']
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    pre, post, kept = W['chk']['b616_checks.txt'], W['chk']['b616_checks_postpush.txt'], W['chk']['b616_checks_attempt1.txt']
    G6 = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
    return ('\n%s THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md v0.1 (PLACE-papers %s) in its cluster’s folder: %d claims -- %s; tier %s, no '
            'paper naming a declaration at a pin, the three kernels named reading as pins with no terminal; the registered T-seven search '
            'computationally-verified on its bank at SIDE-t7-topology-cmb 575a802; the simulators’ claims at statement grade, no bank holding a '
            'run (H50c holding, its other side VACUOUS); one route, DARK by test 2, matching RH-60; %d body sentences traced, the scanner clean, '
            'the no-disclosure arm at 0 hits; both pages unchanged. The sequence closed: relay data/b616_routes_for_sieve.txt, %d listed route rows '
            'gathered into %d conclusions. The verdicts, as relay data/b616_scores.json prints them: H50a-H50d %s; N1-N5 %s; S1-S5 %s; the suite %d '
            'of %d pre-push and %d of %d post-push, a kept run at %d of %d (relay data/b616_checks_attempt1.txt). Defect (a), the seat’s, the '
            'simulator walk banked through the record tool (relay data/b616_sim_walk.txt, %d files, none an output). Confirmed by the author: the '
            'three kernels read as pins with no terminal; the routes listed for the sieve read as the rows whose sieve column names no row; the ten '
            'conclusion groupings. The 2G papers’ findings at OPEN_TRAILS :%d, three of them ERRATA; the living documents’ currency, b618, at :%d. '
            'Nothing deposited; no kernel touched; TECHNE-Core untouched.\n' % (
                W_HEAD % entry, W['doc'], CJ['n'], ', '.join('%d %s' % (gr.get(k, 0), k) for k in G6), W['DJ']['tier'], W['H']['sentences'],
                W['RS']['listed'], len(W['RS']['conclusions']), allh(('H50a', 'H50b', 'H50c', 'H50d'), 'HOLDS'),
                allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), pre[1], pre[0], post[1], post[0],
                kept[1], kept[0], W['walk']['n_hits'], fline, cline))


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
    return Q, Q.line_of(Q.FIND, B616_ENTRY), Q.line_of(Q.OT, B616_TRAIL), Q.line_of(Q.OT, CONSOL)


def _nd(text):
    import b616_record as R6
    return R6.nd_hits(text)


def record_lines(*a):
    """### OPEN_TRAILS: the 2G fact items (addressed to b616's record), the living documents' currency (addressed to the consolidation); then
    ### FINDINGS: b616's weight, addressed to b616's entry -- each appended at the end. Needs the arithmetic and the currency."""
    Q, entry, trail, consol = _addr()
    if (entry, trail, consol) != (7346, 12733, 12731):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s) -- NOTHING WRITTEN' % (entry, trail, consol))
    dry = 'dry' in a
    for f in ('b617_arith.json', 'b617_currency.json'):
        if not os.path.exists(os.path.join(SP if dry else D, f)):
            sys.exit('### %s IS NOT BANKED -- NOTHING WRITTEN' % f)
    parts = _texts(trail, consol, dry)
    wt = _weight(entry, 0, 0)
    bad = ledger_check(*([t for _h, t in parts] + [wt]))
    nd, _n = _nd(NL.join([t for _h, t in parts] + [wt]))
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
    wt = _weight(entry, out[0]['line'], out[1]['line'])
    r = Q.append_to(Q.FIND, wt)
    out.append(dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r))
    put_json('b617_record_lines.json', dict(entry=entry, trail=trail, consol=consol, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


def _rl():
    """### the record lines by role: fact, currency, weight"""
    ls = jl('b617_record_lines.json')['lines']
    return dict(zip(('fact', 'currency', 'weight'), [x['line'] for x in ls]))


def errata(*a):
    """### PLACE-papers ERRATA.md: the three entries of (R227)(2), appended through tools/errata_append.py, each refused if its id is used.
    ### Needs the record lines (the entries point at the fact items' line)."""
    import errata_append as EA
    import banned_terms as BT
    dry = 'dry' in a
    blocks = _errata_blocks(0 if dry else _rl()['fact'], dry)
    text = NL.join(NL.join(b) for _i, b in blocks)
    nd, _n = _nd(text)
    live = [m.group(0) for l in text.split(NL) for m in BT.PAT.finditer(l)]
    dep = _deposited(DEP_NEEDLES)
    print('  ceiling hits in the entries: %s ; banned stems: %s ; no-disclosure hits: %s ; deposited hits: %s' % (
        [m.group(0) for m in CEILING.finditer(text)] or 'NONE', live or 'NONE', nd, {k: len(v) for k, v in dep.items()}))
    if dry:
        print(text)
        return
    if any(nd.values()) or live or any(dep.values()) or CEILING.search(text):
        sys.exit('### AN ENTRY WOULD CARRY TECHNE TEXT, A STEM OR THE CEILING, OR A DEPOSITED FILE CARRIES A SENTENCE -- NOTHING WRITTEN')
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
    put_json('b617_errata.json', dict(at=utc(), entries=out, deposited={k: v for k, v in dep.items()}))
    for o in out:
        print('  ERRATA.md %s :%d' % (o['id'], o['line']))


# ================================================================================ COMPONENT 2: THE ROWS
def _rows4():
    S4 = K.lines_of(_show(PP, PRE_PP, SV4))
    body = S4[:S4.index(R4.BM_TAG)]
    return S4, K.rows_of(body), {m.group(1): i + 1 for i, l in enumerate(body) for m in [re.match(r'^\| ([A-Z]{2}-\d\d) \| ', l)] if m}


def _h51(rows4, ins, src):
    ids4 = set(x[0] for x in rows4)
    concl4 = set(x[1] for x in rows4)
    nb = {r['id']: K.neighbours([(a_, b_) for a_, b_, _c, _d in rows4], r) for r in K.NEW_ROWS}
    dup = []
    for r in K.NEW_ROWS:
        near = K.DUP.get(r['id'])
        ok = (r['id'] not in ids4 and r['conclusion'] not in concl4 and bool(near) and near[0] in ids4 and nb[r['id']][0][0] < 0.5
              and all(x['ok'] for x in src if x['row'] == r['id']) and len([x for x in src if x['row'] == r['id']]) == len(r['sources'])
              and K.row_line(r).count(' | ') == 7)
        dup.append(dict(row=r['id'], nearest=near[0] if near else None, top=nb[r['id']][0], ok=ok))
    h51a = 'HOLDS' if len(K.NEW_ROWS) == 10 and all(x['ok'] for x in dup) else 'REFUTED'
    routes = [r for r in K.NEW_ROWS if r['verdict'] != 'NOT A ROUTE']
    tests_ok = {t: all(x['ok'] for x in ins if x['test'] == t.split(' ')[0]) for t in K.INST}
    dark = [r for r in routes if r['verdict'] == 'DARK' and r['test'] in K.INST and tests_ok[r['test']] and re.match(r'^[1-5] \(', r['test'])]
    t2 = [r for r in dark if r['test'] == K.RH60_TEST]
    h51b = 'HOLDS' if len(routes) == 9 and len(dark) == 9 and len(t2) >= 7 else 'REFUTED'
    return h51a, h51b, dup, dict(routes=len(routes), dark=len(dark), t2=len(t2), by_test={t.split(' ')[0]: sum(1 for r in dark if r['test'] == t)
                                                                                        for t in K.INST})


def rows(*a):
    """### data/b617_rows.txt and data/b617_rows.json: the ten rows, each printed with its proposed row and checked against the existing rows by
    ### conclusion, the instruments and the source route rows resolved by git at their pins -- banked before the edition; H51a-H51b scored."""
    S4, rows4, pos4 = _rows4()
    ins = K.resolve_instruments()
    src = K.resolve_sources()
    _S4, bad = K.resolve_sieve()
    W = json.loads(R4._show(RELAY, PRE_RELAY, 'data/b616_routes_for_sieve.json'))
    wl = {o['key']: o for o in W['conclusions']}
    L = ['b617 -- COMPONENT 2: THE TEN ROWS, (R227)(4), EACH PRINTED WITH ITS PROPOSED ROW AND CHECKED AGAINST THE EXISTING ROWS BY CONCLUSION -- '
         'BANKED BEFORE THE EDITION, %s' % utc(), '',
         '### THE WORK-LIST: relay data/b616_routes_for_sieve.txt at %s -- %d conclusions from %d listed rows; the sieve v0.4 at PLACE-papers %s, '
         '%d rows in its body (%s)' % (PRE_RELAY, len(W['conclusions']), W['listed'], PRE_PP, len(rows4),
                                       ', '.join('%s %d' % (v, sum(1 for x in rows4 if x[2] == v)) for v in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE'))),
         '### THE INSTRUMENTS, EACH RESOLVED BY git AT ITS PIN:']
    L += ['    test %s : %s %s @ %s :%d -- %s' % (x['test'], 'RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', x['path'], x['rev'], x['line'], x['text'][:150])
          for x in ins]
    L += ['', '### PART A -- THE TEN ROWS (shape (H), register, verdict, test, instrument at pin, sources):']
    for r in K.NEW_ROWS:
        w = wl.get(r['key'], {})
        L += ['  %s <- %s (the work-list`s “%s”, verdicts %s)' % (r['id'], r['key'], w.get('conclusion', '### NOT IN THE WORK-LIST'), w.get('verdicts')),
              '      shape %s ; register %s ; verdict %s ; test %s' % (r['shape'], r['register'], r['verdict'], r['test']),
              '      the row: %s' % K.row_line(r)]
        for x in src:
            if x['row'] == r['id']:
                L.append('      source %s %s %s `%s` :%d -- %s' % ('RESOLVES' if x['ok'] else '### DOES NOT RESOLVE', x['cluster'], x['route'], x['path'],
                                                                 x['line'], x['text'][:170]))
    h51a, h51b, dup, tb = _h51(rows4, ins, src)
    L += ['', '### PART B -- EACH ROW AGAINST THE EXISTING ROWS BY CONCLUSION (the nearest by hand, and the three nearest by shared content words, '
          'printed as an aid):']
    c4 = {x[0]: x[1] for x in rows4}
    for x, r in zip(dup, K.NEW_ROWS):
        near, why = K.DUP[r['id']]
        L += ['  %s -- the nearest existing row %s (v0.4 :%d): “%s”' % (r['id'], near, pos4.get(near, 0), c4.get(near, '### NONE')[:220]),
              '      why the conclusions differ: %s' % why,
              '      by shared words: %s ; %s' % (', '.join('%s %.2f' % (b_, a_) for a_, b_ in K.neighbours([(a_, b_) for a_, b_, _c, _d in rows4], r)),
                                                   'DISTINCT' if x['ok'] else '### HELD')]
    L += ['', '### PART C -- THE VERDICTS: %d routes, %d DARK with the test and instrument printed; by test %s; at RH-60`s instrument (%s) %d' % (
        tb['routes'], tb['dark'], tb['by_test'], K.RH60_TEST, tb['t2']),
          '### the data`s own checks (resolve_sieve): %s' % (bad or 'NONE'), '',
          '### ### **H51a %s -- all ten print as rows with every cell filled, and none duplicates an existing row by conclusion.**' % h51a,
          '### ### **H51b %s -- the nine routes read DARK with the test and instrument printed, %d of them by test 2 at RH-60`s instrument (the '
          'floor seven).**' % (h51b, tb['t2'])]
    if bad or not all(x['ok'] for x in ins) or not all(x['ok'] for x in src):
        sys.exit('### A SOURCE OR AN INSTRUMENT DOES NOT RESOLVE -- NOTHING WRITTEN')
    put_txt('b617_rows.txt', L)
    put_json('b617_rows.json', dict(at=utc(), instruments=ins, sources=src, rows=[dict(r, line=K.row_line(r)) for r in K.NEW_ROWS], dup=dup,
                                    tests=tb, H51a=h51a, H51b=h51b))
    print(L[-2])
    print(L[-1])


# ================================================================================ COMPONENT 3: THE SIEVE AT v0.5
def _sv4():
    return K.lines_of(_show(PP, PRE_PP, SV4))


def _sv_map(S4):
    """### v0.4 line -> v0.5 line: the version line and its blank above :3, the ten rows after RH-60."""
    i60 = next(i + 1 for i, l in enumerate(S4) if l.startswith('| RH-60 | '))
    return {n: n + (2 if n >= 3 else 0) + (10 if n > i60 else 0) for n in range(1, len(S4) + 1)}, i60


def _sv_repin(l, w, sec):
    """### a carried back-matter line of v0.2`s, v0.3`s or v0.4`s, its own-line cells mapped to this file; returns (line, [(old, new)])."""
    subs = []

    def f(m):
        o = int(m.group(2))
        subs.append((o, w[o]))
        return m.group(1) + str(w[o]) + m.group(3)
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \(:)(\d+)(\) \|)', f, l)
    l2 = re.sub(r'^(\| [A-Z]{2}-\d\d \| :)(\d+)( \|)', f, l2)
    if sec in ('v0.3', 'v0.4'):
        l2 = re.sub(r'^(\| :)(\d+)( \| )', f, l2)
    if sec == 'v0.3':
        l2 = re.sub(r'(the clause’s one verdict \(:)(\d+)(\))', f, l2)
    if sec == 'v0.4':
        l2 = re.sub(r'(\(:)(\d+)(\))', f, l2)
    return l2, subs


def _sec(n, S4):
    if n >= S4.index(B609_TAG) + 1:
        return 'v0.4'
    if n >= S4.index(B605_TAG) + 1:
        return 'v0.3'
    return 'v0.2'


def sieve_edition(*a):
    """### PLACE-papers phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_5.md beside v0.4 (unedited), from v0.4`s blob at 52962da by line
    ### transforms (carry / rewrite / insert / re-pin); the re-pin step last (`sieve_repin`). Writes the edition and
    ### data/b617_sieve_edition.json; `dry` writes both to the scratchpad instead."""
    dry = 'dry' in a
    S4, bad = K.resolve_sieve()
    if bad:
        sys.exit('### THE SIEVE`S DATA DOES NOT RESOLVE %s -- NOTHING WRITTEN' % bad)
    if g(PP, 'rev-parse', 'HEAD:' + SV4).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, SV4)).strip():
        sys.exit('### v0.4 MOVED SINCE %s -- NOTHING WRITTEN' % PRE_PP)
    if not dry and not os.path.exists(os.path.join(D, 'b617_rows.txt')):
        sys.exit('### THE ROWS ARE NOT BANKED -- NOTHING WRITTEN')
    dest = os.path.join(SP, 'b617_sieve_dry.md') if dry else os.path.join(PP, *SV5.split('/'))
    if not dry and os.path.exists(dest):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    w, i60 = _sv_map(S4)
    i604 = S4.index(R4.BM_TAG) + 1
    rew = {n: (old, new, what) for n, old, new, what in K.SV_REWRITES}
    E, rewd, ins, rep = [], [], [], []
    for n in range(1, len(S4) + 1):
        l = S4[n - 1]
        if n == 3:
            E.append(K.VERSION5)
            ins.append(dict(v5=len(E), text=K.VERSION5, what='the version line, above v0.4`s'))
            E.append('')
        if n in rew:
            old, new, what = rew[n]
            s = l.replace(old, new)
            E.append(s)
            rewd.append(dict(v4=n, v5=len(E), old=l, new=s, frag_old=old, frag_new=new, what=what))
        elif n >= i604:
            sec = _sec(n, S4)
            s, subs = _sv_repin(l, w, sec)
            E.append(s)
            if subs:
                rep.append(dict(v4=n, v5=len(E), subs=subs, sec=sec))
        else:
            E.append(l)
        if w[n] != len(E):
            sys.exit('### THE MAP DRIFTED AT :%d' % n)
        if n == i60:
            for r in K.NEW_ROWS:
                E.append(K.row_line(r))
                ins.append(dict(v5=len(E), text=K.row_line(r), what='row %s, (R227)(4)' % r['id']))
    pos = dict(rows={}, version=ins[0]['v5'])
    for i, l in enumerate(E, 1):
        m = re.match(r'^\| ([A-Z]{2}-\d\d) \| ', l)
        if m and i < w[i604]:
            pos['rows'][m.group(1)] = i
        if l.startswith('- **The super-repulsion fit.**'):
            pos['bench_sr'] = i
        if l.startswith('**The clause’s verdict, stated once:'):
            pos['clause'] = i
        if l.startswith('## Simplicity / RH cascade'):
            pos['cluster'] = i
        if l.startswith('**The verdicts at this edition:**'):
            pos['verdicts'] = i
    E += _sv_bm(S4, w, rewd, ins, rep, pos)
    text = NL.join(E) + NL
    b = text.encode('utf-8')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    ed = text.split(NL)[:-1]
    body5, bm5 = R4._body_and_bm(ed)
    body4, bm4 = R4._body_and_bm(S4)
    b5i = set(i for i, _l in body5)
    J = dict(at=utc(), dry=dry, path=SV5, sha256=sha(b), bytes=len(b), lines=len(ed), v4_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, SV4)).strip(),
             n_v4_body=_count([l for _i, l in body4]), n_body=_count([l for _i, l in body5]), n_backmatter=_count([l for _i, l in bm5]),
             n_v4_backmatter=_count([l for _i, l in bm4]), n_full=_count(ed),
             version_lines=len(_segs(K.VERSION5)), ruled_insertions=sum(len(_segs(x['text'])) for x in ins if x['what'].startswith('row ')),
             credit=0, removals=0, rewrite_deltas=[dict(v4=x['v4'], v5=x['v5'], d=len(_segs(x['new'])) - len(_segs(x['old']))) for x in rewd],
             where={str(k): v for k, v in w.items()}, rew=rewd, ins=ins, rep=rep, pos=pos, bm5=ed.index(BM_TAG5) + 1,
             ceiling_in_body=[(i, m.group(0)) for i, l in body5 for m in CEILING.finditer(l)],
             inserted_in_body=all(x['v5'] in b5i for x in ins))
    put_json('b617_sieve_edition.json', J)   # ### `dry` routes it to the scratchpad
    print('  %s : %d lines, sha256 %s ; body v0.4 %d ; v0.5 %d (%+d) ; version %d ; ruled insertions %d ; rewrite deltas %s ; back matter %d '
          '(v0.4 %d) ; re-pinned lines %d (cells %d) ; ceiling in body %s ; rows %s' % (
              dest, len(ed), J['sha256'][:16], J['n_v4_body'], J['n_body'], J['n_body'] - J['n_v4_body'], J['version_lines'],
              J['ruled_insertions'], [(x['v4'], x['d']) for x in J['rewrite_deltas'] if x['d']], J['n_backmatter'], J['n_v4_backmatter'],
              len(rep), sum(len(x['subs']) for x in rep), J['ceiling_in_body'] or 'none',
              {k: pos['rows'].get(k) for k in ('RH-58', 'RH-60', 'RH-61', 'RH-70', 'FD-01', 'MC-01')}))


def _sv_bm(S4, w, rewd, ins, rep, pos):
    q = _cell
    RJ = dict(instruments=K.resolve_instruments(), sources=K.resolve_sources())
    _S4, rows4, pos4 = _rows4()
    c4 = {x[0]: x[1] for x in rows4}
    L = ['', '---', '', BM_TAG5, '',
         '## Back matter of the v0.5 edition — written 2026-10-04 by b617 under the author’s ruling `(R227)`(4), by the form of `(R187)`(5), its '
         'clauses and the precedence order', '',
         '*This file is v0.5 of THE_FINDINGS_AS_THEY_STAND, written beside v0.4 (`%s`, unedited) from that version’s blob at PLACE-papers %s and the '
         'rows bank (relay `data/b617_rows.txt`) banked before the edition was written; v0.3, v0.2 and the current version (read as v0.1) stand '
         'unedited too. The back matter of v0.2, of v0.3 and of v0.4 is carried above whole, its own-line cells re-pinned to this file’s lines '
         '(counted below). Every line cited in this section is this file’s own unless it is marked otherwise.*' % (SV4, PRE_PP), '',
         '### The readings, each the seat’s and strikeable', '',
         '- **R-1** the ten rows are the ten conclusions of relay `data/b616_routes_for_sieve.txt`, K1 to K10 in its order, entered in the '
         'Simplicity / RH cascade’s other rows after RH-60 and numbered RH-61 to RH-70: each concludes about ξ’s zeros or their multiplicity, the '
         'cluster’s object, whichever synthesis lists it.',
         '- **R-2** each row’s conclusion is the work-list’s sentence restated under the ceiling as offered toward its target, the step the papers '
         'leave open named; each verdict and test is the source route rows’ own, as the syntheses read them through the five tests at the '
         'instruments’ pins, and where two syntheses list one conclusion their verdicts agree.',
         '- **R-3** the registers: RH-63 and RH-70 read multiplicity (a zero’s multiplicity, and the derivative at a zero whose nonvanishing is '
         'its simplicity); RH-68 reads the mechanism catalogue; RH-69 reads the codes and the substrate; the other six read the symmetry and its '
         'level curves, entered in the registers’ list as one more.',
         '- **R-4** the shapes, hand-read (H) from each sentence: FINITE for the paths’ withdrawal and the finite localization, DENSITY for the '
         'statistic over thirty ordinates, UNIVERSAL for the rest.',
         '- **R-5** the compiled-face column: none of the ten has a declaration at a pin; its cell names the source route rows by synthesis and '
         'line, each synthesis’s path in the table of rows added below.',
         '- **R-6** the FACE group, the rows already standing, the bench (:%d), the mutual-light lines, the dated blocks and every other line are '
         'carried unchanged; the head’s counts and the cluster’s headings are re-stated.' % pos['bench_sr'], '',
         '### Removals', '', 'None.', '',
         '### The ten rows added', '',
         '| row | this edition’s line | the verdict | test, instrument at pin | the instrument lines and the source route rows, each resolved by git at its pin | Status |',
         '|:--|:--|:--|:--|:--|:--|']
    for r in K.NEW_ROWS:
        il = '; '.join('%s @ %s %s :%d' % (x['repo'], x['rev'], x['path'], x['line']) for x in RJ['instruments'] if r['test'] != '—'
                       and x['test'] == r['test'].split(' ')[0])
        sl = '; '.join('%s %s: PLACE-papers @ %s %s :%d' % (x['cluster'], x['route'], PRE_PP, x['path'], x['line']) for x in RJ['sources'] if x['row'] == r['id'])
        L.append('| %s | :%d | %s | %s | %s | added, (R227)(4) |' % (r['id'], pos['rows'][r['id']], r['verdict'], r['test'], q('; '.join(x for x in (il, sl) if x))))
    L += ['', '### Each row against the existing rows, by conclusion', '',
          '| row | the nearest existing row | its line | why the conclusions differ | Status |', '|:--|:--|:--|:--|:--|']
    for r in K.NEW_ROWS:
        near, why = K.DUP[r['id']]
        L.append('| %s | %s | :%d | %s | distinct, (R227)(4) H51a |' % (r['id'], near, pos['rows'][near], q(why)))
    nt2 = sum(1 for r in K.NEW_ROWS if r['test'] == K.RH60_TEST)
    L += ['', '### The verdicts of the rows added, by test', '',
          '- DARK by test 2 at RH-60’s instrument (%s, RH-60 at :%d): %d rows -- %s.' % (K.RH60_TEST, pos['rows']['RH-60'], nt2,
                                                                                      ', '.join(r['id'] for r in K.NEW_ROWS if r['test'] == K.RH60_TEST)),
          '- DARK by test 4 (%s): %s.' % (K.T4, ', '.join(r['id'] for r in K.NEW_ROWS if r['test'] == K.T4)),
          '- DARK by test 1 (%s): %s.' % (K.T1, ', '.join(r['id'] for r in K.NEW_ROWS if r['test'] == K.T1)),
          '- NOT A ROUTE: %s.' % ', '.join(r['id'] for r in K.NEW_ROWS if r['verdict'] == 'NOT A ROUTE'), '',
          '### Rewrites -- the registers, the head’s counts and the cluster’s headings', '',
          '| this edition’s line | v0.4’s line | v0.4’s wording | this edition’s wording | Status |', '|:--|:--|:--|:--|:--|']
    for x in rewd:
        L.append('| :%d | :%d | %s | %s | %s |' % (x['v5'], x['v4'], q(x['frag_old']), q(x['frag_new']), q(x['what'])))
    L += ['', '### Insertions ordered by the ruling', '', '| this edition’s line | the text | Status |', '|:--|:--|:--|']
    for x in ins:
        L.append('| :%d | %s | %s |' % (x['v5'], q(x['text'])[:300], q(x['what'])))
    L += ['', '### Re-pins of v0.4’s back matter', '',
          '%d own-line cells on %d lines of the carried back matter re-pinned to this file’s lines (v0.2’s: %d lines; v0.3’s: %d lines; v0.4’s: %d '
          'lines); every other line carried verbatim.' % (sum(len(x['subs']) for x in rep), len(rep), sum(1 for x in rep if x['sec'] == 'v0.2'),
                                                          sum(1 for x in rep if x['sec'] == 'v0.3'), sum(1 for x in rep if x['sec'] == 'v0.4')), '',
          '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this edition, v0.5 | `%s` | written at b617 |' % SV5,
          '| v0.4 | `%s` | unedited |' % SV4,
          '| v0.3 | `%s` | unedited |' % K.SV3,
          '| v0.2 | `%s` | unedited |' % K.SV2,
          '| the current version, unnumbered (read as v0.1) | `%s` | unedited |' % K.SV1,
          '| the work-list | relay `data/b616_routes_for_sieve.txt` | banked at b616 |',
          '| the rows bank | relay `data/b617_rows.txt` | banked at b617 before the edition |',
          '| the sentence-by-sentence diff | relay `data/b617_edition_FINDINGS_STAND.txt` | banked at b617 |', '',
          '### Correspondence', '',
          '| row | this edition’s line | v0.4’s line | the verdict at v0.4 | the verdict at v0.5 | Status |', '|:--|:--|:--|:--|:--|:--|']
    for r in K.NEW_ROWS:
        L.append('| %s | :%d | none | none | %s%s | added |' % (r['id'], pos['rows'][r['id']], r['verdict'],
                                                              ', test %s' % r['test'].split(' ')[0] if r['test'] != '—' else ''))
    L.append('| RH-60 | :%d | :%d | DARK, test 2 | DARK, test 2 | carried; the instrument seven of the rows added share |' % (
        pos['rows']['RH-60'], pos4['RH-60']))
    L += ['', '### Version history', '',
          '- **v0.5, 2026-10-04 (b617, `(R227)`(4))**: ten rows added from the routes the six syntheses list for the sieve -- RH-61 the paths’ '
          'withdrawal, NOT A ROUTE; RH-62 and RH-64 to RH-69, DARK by test 2; RH-63 the localization, DARK by test 4; RH-70 the derivative '
          'statistic, DARK by test 1 -- and one register; the head’s counts re-stated, 97 rows: 2 BRIGHT, 16 DARK, 68 NOT A ROUTE, 11 FACE. v0.4 '
          'stands beside it, unedited.',
          '- **v0.4, 2026-10-03 (b609, `(R219)`(3)(a))**: its own version history is carried above.', '']
    return L


def _ed(path):
    t = io.open(os.path.join(PP, *path.split('/')), encoding='utf-8').read().replace(chr(13), '')
    return K.lines_of(t)


def _scan(path):
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    return r.stdout or ''


def sieve_termscan(*a):
    """### the scanner (banned_terms.py --new) on v0.5, banked as data/b617_sieve_termscan.txt."""
    out = _scan(os.path.join(SP, 'b617_sieve_dry.md') if DRY else os.path.join(PP, *SV5.split('/')))
    put_txt('b617_sieve_termscan.txt', out.rstrip(NL).split(NL))
    print([l for l in out.split(NL) if 'live uses' in l or 'VERDICT' in l])


def sieve_carried(E, ed, S4):
    """### every non-blank v0.4 line: carried verbatim at its mapped line, rewritten with both fragments in this file`s rewrites table, or
    ### re-pinned (its own-line cells only)."""
    rw = {x['v4']: x for x in E['rew']}
    rp = {x['v4']: x for x in E['rep']}
    bm = NL.join(ed[E['bm5'] - 1:])
    w = {int(k): v for k, v in E['where'].items()}
    ok, bad = 0, []
    for n in range(1, len(S4) + 1):
        if not S4[n - 1].strip():
            continue
        x5 = w[n]
        if n in rw:
            x = rw[n]
            good = ed[x5 - 1] == S4[n - 1].replace(x['frag_old'], x['frag_new']) and \
                ('| :%d | :%d | %s | %s |' % (x5, n, _cell(x['frag_old']), _cell(x['frag_new']))) in bm
        elif n in rp:
            good = ed[x5 - 1] == _sv_repin(S4[n - 1], w, _sec(n, S4))[0] and ed[x5 - 1] != S4[n - 1]
        else:
            good = ed[x5 - 1] == S4[n - 1]
        ok += good
        if not good:
            bad.append(n)
    return ok, bad


def sieve_bank(*a):
    """### data/b617_edition_FINDINGS_STAND.txt and data/b617_h51.json: the diff with its offset line, the rows, the counts, the ceiling, the
    ### scanner, H28a-H28c (H51c) and the head's counts against v0.4's."""
    E = jl('b617_sieve_edition.json')
    ed = K.lines_of(io.open(os.path.join(SP, 'b617_sieve_dry.md'), encoding='utf-8').read()) if DRY else _ed(SV5)
    S4 = _sv4()
    if sha((NL.join(ed) + NL).encode('utf-8')) != E['sha256']:
        sys.exit('### THE EDITION ON DISK IS NOT THE BANKED ONE -- NOTHING WRITTEN')
    RJ = jl('b617_rows.json') if not DRY else dict(instruments=K.resolve_instruments(), sources=K.resolve_sources())
    scan = rd('b617_sieve_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    ok, bad = sieve_carried(E, ed, S4)
    body, bm = R4._body_and_bm(ed)
    bi = set(i for i, _l in body)
    hits = [dict(line=i, hit=m.group(0), kind='body' if i in bi else 'record') for i, l in enumerate(ed, 1) for m in CEILING.finditer(l)]
    beyond = [h for h in hits if h['kind'] == 'body']
    bmt = NL.join(ed[E['bm5'] - 1:])
    P = E['pos']
    h28a_rows = [dict(id='v0.4 :%d' % x['v4'], line=x['v5'], recorded=('| :%d | :%d | ' % (x['v5'], x['v4'])) in bmt) for x in E['rew']]
    ins_ok = bool(RJ.get('instruments')) and all(x['ok'] for x in RJ['instruments']) and all(x['ok'] for x in RJ['sources'])
    rows_cite = all(ed[P['rows'][r['id']] - 1] == K.row_line(r) and ('| %s | :%d |' % (r['id'], P['rows'][r['id']])) in bmt for r in K.NEW_ROWS)
    h28a = 'HOLDS' if all(x['recorded'] for x in h28a_rows) and ins_ok and rows_cite else 'REFUTED'
    body_dn = E['n_body'] - E['n_v4_body']
    allowed = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines'] + sum(abs(x['d']) for x in E['rewrite_deltas'])
    strict = E['credit'] + E['removals'] + E['ruled_insertions'] + E['version_lines']
    h28b = 'HOLDS' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HOLDS' if clean and not beyond else 'REFUTED'
    h51c = 'HOLDS' if (h28a, h28b, h28c) == ('HOLDS', 'HOLDS', 'HOLDS') else 'REFUTED'
    body4 = S4[:S4.index(R4.BM_TAG)]
    body5 = ed[:ed.index(R4.BM_TAG)]
    VW = ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')
    c4 = {v: sum(1 for x in K.rows_of(body4) if x[2] == v) for v in VW}
    c5 = {v: sum(1 for x in K.rows_of(body5) if x[2] == v) for v in VW}
    head = ed[P['verdicts'] - 1]
    head_ok = ('%d rows -- %d BRIGHT, %d DARK, %d NOT A ROUTE, and %d FACE rows' % (sum(c5.values()), c5['BRIGHT'], c5['DARK'], c5['NOT A ROUTE'],
                                                                                 c5['FACE'])) in head
    offs, last = [], None
    for n in range(1, len(S4) + 1):
        o = E['where'][str(n)] - n
        if o != last:
            offs.append((n, o))
            last = o
    L = ['### OFFSET FROM v0.4 (R190)(3): %s -- the offset changes at each v0.4 line printed (v0.4 line, offset); every v0.4 line`s v0.5 '
         'line is printed below (the map), and every edition line cited here is the final file`s own.' % ', '.join('%+d from :%d' % (o, n) for n, o in offs), '',
         'b617 -- COMPONENT 3: THE SIEVE AT v0.5, (R227)(4), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER', '',
         '### v0.4 : PLACE-papers %s @ %s (blob %s), %d lines' % (SV4, PRE_PP, E['v4_blob'][:8], len(S4)),
         '### v0.5 : PLACE-papers %s, %d lines, sha256 %s' % (SV5, E['lines'], E['sha256']), '',
         '### THE VERSION LINE, PRINTED: :%d %s' % (P['version'], ed[P['version'] - 1]), '',
         '### THE TEN ROWS, PRINTED AT THEIR LINES:']
    for r in K.NEW_ROWS:
        L += ['  %s :%d -- %s ; test %s' % (r['id'], P['rows'][r['id']], r['verdict'], r['test']), '      %s' % ed[P['rows'][r['id']] - 1]]
    L += ['', '### THE HEAD`S COUNTS: v0.4 %s (%d rows) ; v0.5 %s (%d rows) ; the head line at :%d re-stated to them: %s' % (
        c4, sum(c4.values()), c5, sum(c5.values()), P['verdicts'], head_ok),
          '### THE CLUSTER`S HEADING at :%d: %s' % (P['cluster'], ed[P['cluster'] - 1]), '',
          '### EVERY REWRITE (v0.5 line <- v0.4 line, its fragments, the segment change):']
    for x in E['rew']:
        L += ['  :%d <- :%d  %s (%+d)' % (x['v5'], x['v4'], x['what'], len(_segs(x['new'])) - len(_segs(x['old']))),
              '      was : %s' % x['frag_old'], '      now : %s' % x['frag_new']]
    L += ['', '### EVERY INSERTION (v0.5 line, its segments, what orders it):']
    L += ['  :%d (%d) %s' % (x['v5'], len(_segs(x['text'])), x['what']) for x in E['ins']]
    L += ['', '### THE RE-PINS OF THE CARRIED BACK MATTER (%d lines, %d cells: v0.4 line -> v0.5 line, its cells old -> new):' % (
        len(E['rep']), sum(len(x['subs']) for x in E['rep']))]
    L += ['  :%d -> :%d  %s %s' % (x['v4'], x['v5'], x['sec'], ', '.join(':%d -> :%d' % tuple(s) for s in x['subs'])) for x in E['rep']]
    L += ['', '### EVERY NON-BLANK v0.4 LINE -> ITS v0.5 LINE (%d carried verbatim, rewritten with its fragments recorded, or re-pinned ; '
          'failing %s):' % (ok, bad or 'none')]
    L += ['  :%s -> :%d' % (n, x) for n, x in sorted((int(k), v) for k, v in E['where'].items())]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): v0.4`s BODY %d ; v0.5`s BODY %d (%+d) ; the BACK MATTER %d '
          '(v0.2`s, v0.3`s and v0.4`s carried, this act`s own, the history blocks included), printed separately ; the edition whole %d' % (
              E['n_v4_body'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled insertions %d (the ten rows) + rewrites` '
          'segment changes %d + one version line %d = %d ; the strict count %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_insertions'], sum(abs(x['d']) for x in E['rewrite_deltas']), E['version_lines'],
              allowed, strict), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s' % (h['line'], h['hit'], h['kind']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling in the body: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on v0.5: live uses %s ; verdict %s' % (live.group(1) if live else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED-IN-MEANING sentence (%d rewrites) recorded with both wordings; the ten rows each citing its '
          'instruments and sources, every one resolving.**' % (h28a, len(h28a_rows)),
          '### ### **H28b %s -- the body differs by %+d sentences against at most %d (strict %d); the back matter %d, excluded and printed.**' % (
              h28b, body_dn, allowed, strict, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling in the body %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **H51c %s -- H28a-H28c hold.**' % h51c,
          '### ### **THE SIEVE LANDS: NO SENTENCE HELD.**' if h28a == 'HOLDS' and not bad else '### ### **HELD AT A SENTENCE: see above.**']
    put_txt('b617_edition_FINDINGS_STAND.txt', L)
    put_json('b617_h51.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, H51c=h51c, h28a_rows=h28a_rows, body_dn=body_dn, allowed=allowed, strict=strict,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, clean=clean, beyond=len(beyond), hits=hits,
                                   carried_ok=ok, carried_bad=bad, c4=c4, c5=c5, head_ok=head_ok))
    print('H28a %s H28b %s H28c %s H51c %s ; carried %d bad %s ; body_dn %d allowed %d strict %d ; beyond %d ; live %s ; counts %s -> %s head %s' % (
        h28a, h28b, h28c, h51c, ok, bad, body_dn, allowed, strict, len(beyond), live.group(1) if live else None, c4, c5, head_ok))


def sieve_repin(*a):
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932), for v0.5. Writes data/b617_repin_sieve.txt."""
    E = jl('b617_sieve_edition.json')
    ed = K.lines_of(io.open(os.path.join(SP, 'b617_sieve_dry.md'), encoding='utf-8').read()) if DRY else _ed(SV5)
    S4 = _sv4()
    P = E['pos']
    w = {int(k): v for k, v in E['where'].items()}
    checks = []
    for x in E['rep']:
        for o, n in x['subs']:
            checks.append(('carried cell :%d -> :%d (at :%d)' % (o, n, x['v5']), w[o] == n and (ed[n - 1] == S4[o - 1] or any(
                y['v4'] == o and ed[n - 1] == y['new'] for y in E['rew']))))
    for r in K.NEW_ROWS:
        checks.append(('row %s on :%d' % (r['id'], P['rows'][r['id']]), ed[P['rows'][r['id']] - 1] == K.row_line(r)))
    for f in ('RH-60', 'FD-01', 'FD-02', 'MC-01'):
        checks.append(('%s on :%d' % (f, P['rows'][f]), ed[P['rows'][f] - 1].startswith('| %s | ' % f)))
    bm = NL.join(ed[E['bm5'] - 1:])
    for m in re.finditer(r'^\| (RH-\d\d|FD-0\d|CT-\d\d) \| :(\d+) \|', bm, re.M):
        checks.append(('v0.5`s back matter names %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    for m in re.finditer(r'^\| :(\d+) \| :(\d+) \| ', bm, re.M):
        a_, b_ = int(m.group(1)), int(m.group(2))
        checks.append(('the rewrites table`s :%d <- :%d' % (a_, b_), w.get(b_) == a_ and any(y['v5'] == a_ for y in E['rew'])))
    for m in re.finditer(r'^\| :(\d+) \| ', bm, re.M):
        a_ = int(m.group(1))
        checks.append(('a cited line :%d holds text' % a_, bool(ed[a_ - 1].strip())))
    for k in ('version', 'bench_sr', 'clause', 'cluster', 'verdicts'):
        checks.append(('%s on :%d' % (k, P[k]), bool(ed[P[k] - 1].strip())))
    checks.append(('the bench line cited at :%d' % P['bench_sr'], ('(:%d)' % P['bench_sr']) in bm))
    checks.append(('the version line above v0.4`s', ed[P['version'] - 1] == K.VERSION5 and ed[P['version'] + 1] == S4[2]))
    bank = rd('b617_edition_FINDINGS_STAND.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM v0.4') and bank.count('### OFFSET FROM') == 1))
    fsha = hashlib.sha256((NL.join(ed) + NL).encode('utf-8')).hexdigest()
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and fsha == E['sha256']))
    for m in re.finditer(r'^  (RH-\d\d) :(\d+) -- ', bank, re.M):
        checks.append(('the diff bank`s %s at :%s' % (m.group(1), m.group(2)), P['rows'].get(m.group(1)) == int(m.group(2))))
    L = ['### b617 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % SV5, '']
    L += ['    %-100s %s' % (x[:100], 'OK' if ok else '### FAILS') for x, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _x, ok in checks), len(checks))]
    put_txt('b617_repin_sieve.txt', L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b617_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b617_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b617_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b617 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b617_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b617_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 5: THE SCORES AND THE RECORD
HKEYS = ('H51a', 'H51b', 'H51c')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
CURRENTS = (SV4, K.SV3, K.SV2, K.SV1) + tuple(SYN_ALL.values()) + tuple(PS + f for f, _n in FACT_LINES) + tuple(p for _n, p, _nd in LIVING) + (
    'README.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md', 'SPIRAL_MAP_v0_7.md')
S4_EXPECT = {'zeta': True, 'chi': True}   # ### the seat's expectation, registered on the face: each page's Placement gains v0.5


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def _placement_only(z):
    """### a changed page's diff: every changed line a Placement row naming v0.5 (or none, when unchanged)"""
    dl = [x for x in z.get('diff') or [] if x[:1] in '+-' and not x.startswith(('+++', '---'))]
    return all(x.startswith('+') and SV5 in x for x in dl) and (len(dl) == 1 if z.get('changed') else not dl)


def scores(*a):
    RJ, H, E = jl('b617_rows.json'), jl('b617_h51.json'), jl('b617_sieve_edition.json')
    Z, X = jl('b617_page_zeta.json'), jl('b617_page_chi.json')
    face = jl('b617_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', SV5] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b617_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b616_closing_push_out.txt'))
    ins, src = K.resolve_instruments(), K.resolve_sources()
    arms2 = rd('b617_page_arms_c2.txt')
    repin = rd('b617_repin_sieve.txt')
    m = re.search(r'RE-PIN : (\d+) of (\d+)', repin)
    tb = RJ['tests']
    c4, c5 = H['c4'], H['c5']
    strict_ok = H['body_dn'] == H['strict'] and all(x['d'] == 0 for x in E['rewrite_deltas'])
    S = {
        'H51a': (RJ['H51a'], 'ten rows printed with every cell filled ; each against the existing rows by conclusion: %s' % (
            ', '.join('%s~%s %s' % (x['row'], x['nearest'], 'distinct' if x['ok'] else 'HELD') for x in RJ['dup']))),
        'H51b': (RJ['H51b'], '%d routes, %d DARK with test and instrument printed, by test %s ; at RH-60`s instrument %d (the floor 7)' % (
            tb['routes'], tb['dark'], tb['by_test'], tb['t2'])),
        'H51c': (H['H51c'], 'H28a %s, H28b %s (body %+d against at most %d, strict %d), H28c %s (scanner %s, beyond the ceiling %d)' % (
            H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['strict'], H['H28c'], 'CLEAN' if H['clean'] else 'NOT CLEAN', H['beyond'])),
        'N1': ('HELD' if RJ['H51a'] == 'HOLDS' else 'REFUTED', 'none of the ten duplicates an existing row by conclusion: %s' % RJ['H51a']),
        'N2': ('HELD' if tb['t2'] >= 7 else 'REFUTED', '%d of the nine routes DARK by test 2 at RH-60`s instrument (the floor 7)' % tb['t2']),
        'N3': ('HELD' if c5['DARK'] - c4['DARK'] == 9 and c5['NOT A ROUTE'] - c4['NOT A ROUTE'] == 1 and H['head_ok'] else 'REFUTED',
               'DARK %d -> %d (%+d) ; NOT A ROUTE %d -> %d (%+d) ; the head re-stated %s' % (c4['DARK'], c5['DARK'], c5['DARK'] - c4['DARK'],
                                                                                         c4['NOT A ROUTE'], c5['NOT A ROUTE'],
                                                                                         c5['NOT A ROUTE'] - c4['NOT A ROUTE'], H['head_ok'])),
        'N4': ('HELD' if H['H51c'] == 'HOLDS' and not H['carried_bad'] else 'REFUTED',
               'H28a-H28c %s ; sentences held %s' % (H['H51c'], H['carried_bad'] or 'none')),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the sieve`s earlier versions, the six syntheses, the 2G papers, the living '
               'documents, README, the census and SPIRAL_MAP unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools and the '
               'table %s' % (kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(x['ok'] for x in ins) and all(x['ok'] for x in src) else 'REFUTED',
               'the instrument lines resolving %d of %d ; the source route rows %d of %d' % (sum(x['ok'] for x in ins), len(ins), sum(x['ok'] for x in src), len(src))),
        'S2': ('HELD' if strict_ok else 'REFUTED', 'the body differs by %+d, the strict count %d (the ten rows and the version line), every rewrite`s '
                                                   'segment change %s' % (H['body_dn'], H['strict'], [x['d'] for x in E['rewrite_deltas']])),
        'S3': ('HELD' if m and m.group(1) == m.group(2) else 'REFUTED', 'the re-pin step: %s' % (m.group(0) if m else 'no bank')),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] and _placement_only(Z) and _placement_only(X)
               else 'REFUTED', 'the ζ page changed %s (expected %s), the χ page changed %s (expected %s), each by one Placement row naming v0.5: %s, %s' % (
                   Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'], _placement_only(Z), _placement_only(X))),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b617_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:260]))


def _title():
    H = jl('b617_h51.json')
    return ('## The sieve at v0.5: ten conclusions from the six syntheses as rows, %d DARK and %d NOT A ROUTE, the head at %d rows; the 2G papers’ '
            'findings and three errata' % (H['c5']['DARK'] - H['c4']['DARK'], H['c5']['NOT A ROUTE'] - H['c4']['NOT A ROUTE'], sum(H['c5'].values())))


TRAIL_HEAD = ('### b617 — lane three, act forty-four under (R227): the sieve at v0.5 -- the ten conclusions gathered from the six syntheses as '
              'rows; the 2G papers’ findings and three errata; the living documents’ currency entered for b618')


def _finding_text():
    S, J, RJ, H = jl('b617_scores.json'), jl('b617_sieve_edition.json'), jl('b617_rows.json'), jl('b617_h51.json')
    EJ = jl('b617_errata.json')
    rl = _rl()
    dc = _pp_commit('b617 (R227)(4): ' + SV5)
    ec = _pp_commit('b617 (R227)(2): ERRATA')
    t = _title()
    tb = RJ['tests']
    e = ['', t, '',
         '*Filed at b617 on the author’s ruling `(R227)`. Banks: relay `data/b617_reads.txt`, `data/b617_arith.txt`, `data/b617_currency.txt`, '
         '`data/b617_rows.txt`, `data/b617_edition_FINDINGS_STAND.txt`, `data/b617_repin_sieve.txt`, `data/b617_page_arms_c2.txt`. Nothing deposits.*', '',
         '**The edition** (`(R227)`(4)). PLACE-papers `%s` (commit %s), beside v0.4, unedited: the ten conclusions of relay '
         'data/b616_routes_for_sieve.txt entered as RH-61 to RH-70 in the Simplicity / RH cascade’s other rows after RH-60, each with its shape '
         '(H), register, verdict, test and instrument at pin, and the source route rows named by synthesis and line. Nine routes read DARK -- %d '
         'by test 2 at RH-60’s instrument (the detector and epstein_not_h2_sign_cfg at SIDE-explicit-formula v0.16, INVARIANCE_BARRIERS Theorem '
         '3.7), one by test 4 (the finite localization), one by test 1 (the derivative statistic) -- and the paths’ withdrawal reads NOT A ROUTE; '
         'one register entered, the symmetry and its level curves. The head re-stated: %d rows, %d BRIGHT, %d DARK, %d NOT A ROUTE, %d FACE. '
         'Each row checked against the existing rows by conclusion, none a duplicate (relay data/b617_rows.txt). The body differs from v0.4’s by '
         '%+d sentences, the strict count; the carried back matter re-pinned, %s.' % (
             SV5, dc, tb['t2'], sum(H['c5'].values()), H['c5']['BRIGHT'], H['c5']['DARK'], H['c5']['NOT A ROUTE'], H['c5']['FACE'], H['body_dn'],
             S['S3'][1].replace('the re-pin step: ', '')), '',
         '**The record lines.** b616’s weight at FINDINGS :%d; the 2G papers’ findings at OPEN_TRAILS :%d, the computations at relay '
         'data/b617_arith.txt; ERRATA %s (:%d), %s (:%d) and %s (:%d) at PLACE-papers %s, alone; the living documents’ currency, b618, priced at '
         ':%d (relay data/b617_currency.txt).' % (rl['weight'], rl['fact'], EJ['entries'][0]['id'], EJ['entries'][0]['line'], EJ['entries'][1]['id'],
                                                 EJ['entries'][1]['line'], EJ['entries'][2]['id'], EJ['entries'][2]['line'], ec, rl['currency']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the edition takes the work-list b616 gathered (FINDINGS :7346) from the six syntheses’ '
         'route tables (:7240, :7260, :7280, :7300, :7322, :7346) and reads seven of its routes through the instrument b609’s RH-60 was read by '
         '(:7186), the mechanism enumeration, so RH-60 now stands with seven neighbours that fail at the Epstein configuration for the same reason '
         '-- a functional equation with no prime side; the earlier editions (:7060, :7084, :7186) stand beside it. It strengthens the programme’s '
         'offering of the sieve: every route the six syntheses carry is now one row of one table, read at a pinned instrument, and the head’s '
         'count of routes the record has read and darkened rises from 7 to 16.', '',
         '**Next.** Per `(R227)`(5): b618, the living documents’ currency, then the census’s v0.4. The author rules on the closing.', '',
         '*Nothing deposits; no paper, synthesis or earlier version of the sieve edited; README, REGISTRY and the census unwritten; nothing here is '
         'a statement about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    return t, NL.join(e)


def findings(*a):
    Q = R2._Q()
    t, e = _finding_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s' % (bad or 'NONE', nd))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    Q.guard_absent(Q.FIND, t[:90])
    r = Q.append_to(Q.FIND, e)
    put_json('b617_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


FOR_AUTHOR = (
    '(1) the ten rows’ readings, strikeable: the cluster (all ten in the Simplicity / RH cascade, each concluding about ξ’s zeros or their '
    'multiplicity); the registers (one entered, the symmetry and its level curves, for six rows; multiplicity for the localization and the '
    'derivative statistic; the mechanism catalogue for the inventory; the codes and the substrate for the Frobenius row); the shapes (H); the '
    'compiled-face cell naming the source route rows; (2) the inventory row RH-68 read as distinct from RH-60: TS’s inventory (TS :605-:611) is '
    'of the known zero-producing mechanisms by kind, uncompiled, and not the seven classes; (3) the fact item on T7_CMB’s eigenvalues corrects '
    'b616’s reading that (R227)(2) quotes: 3 once and −1 six times is the spectrum of neither the incidence matrix (3 once, six of modulus √2) '
    'nor K₇ (6 once, −1 six times); (4) THE_METHOD_CANON’s last commit is b588’s census / totality append of 2026-10-01, the ruling’s 2026-09-08 '
    'being v1.3’s own date; (5) the generator’s channels, named among INSTRUMENTS’ missed items, not located on the ledgers by the seat -- b618 '
    'asks where they stand')


def _trail_text():
    S, fj, rl = jl('b617_scores.json'), jl('b617_findings.json'), _rl()
    EJ, CU = jl('b617_errata.json'), jl('b617_currency.json')['docs']
    rows_ = ['', TRAIL_HEAD, '',
             '**(R227) ratified.** (1) b616 at its weight, the three readings confirmed. (2) The 2G papers’ findings, three to ERRATA. (3) The living '
             'documents’ currency, entered as b618. (4) The sieve at v0.5; H51a-H51c. (5) The act after: b618, then the census’s v0.4.', '',
             '**Entered:** FINDINGS.md:%d (b616’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the 2G fact items, addressed '
             'to b616’s record :12733), :%d (the living documents’ currency, b618, addressed to the consolidation :12731); this record; ERRATA %s; '
             'PLACE-papers `%s`; relay data/b617_rows.txt, data/b617_edition_FINDINGS_STAND.txt, data/b617_arith.txt, data/b617_currency.txt.' % (
                 rl['weight'], fj['entry_line'], rl['fact'], rl['currency'], ', '.join('%s (:%d)' % (x['id'], x['line']) for x in EJ['entries']), SV5), '',
             '**Resolved by the seat, for the author’s strike:** the ten conclusions entered in the Simplicity / RH cascade after RH-60 as RH-61 to '
             'RH-70; each verdict and test the source route rows’ own; one register entered; the head and the cluster’s headings re-stated; the '
             'carried back matter of v0.2, v0.3 and v0.4 re-pinned by its own-line cells; b618 addressed to the consolidation as the act before the '
             'census’s v0.4, per (R227)(5); the errata in their form, each addressed to the fact items’ line. No prompt was put (relay '
             'data/b617_author_answers.txt).', '',
             '**For the author:** %s.' % FOR_AUTHOR, '',
             '**b618 priced** (`(R227)`(3)): the eight living documents read for their function lines; the prices by count, relay '
             'data/b617_currency.txt -- %s; one act, no Lean call, the author’s word per document at its prompt.' % (
                 ', '.join('%s %d' % (n, CU[n]['price']) for n, _p, _nd in LIVING)), '',
             '**Defects** (relay data/b617_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R227)`(5), b618, the living documents’ currency; then the census’s v0.4; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left '
             'it; the four lists stay OPEN.', '']
    return NL.join(rows_)


def trail(*a):
    Q = R2._Q()
    e = _trail_text()
    bad = ledger_check(e)
    nd, _n = _nd(e)
    print('  grade-word lines naming a backticked name: %s ; no-disclosure hits: %s' % (bad or 'NONE', nd))
    if 'dry' in a:
        print(e)
        return
    if bad or any(nd.values()):
        sys.exit('### A LINE WOULD GRADE A TABLE NAME OR CARRY TECHNE TEXT -- NOTHING WRITTEN')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    r = Q.append_to(Q.OT, e)
    put_json('b617_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b617_trail.json')['line'])


def desk(*a):
    S = jl('b617_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b617 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H51a-H51c, (R227)(4).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H51 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b617_defects.txt').rstrip(NL).split(NL)
    put_txt('b617_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b617_scores.json'), jl('b617_findings.json'), jl('b617_trail.json'), _rl()
    Z, X, EJ, H = jl('b617_page_zeta.json'), jl('b617_page_chi.json'), jl('b617_errata.json'), jl('b617_h51.json')
    L = ['b617 -- THE COMPONENTS, BANKED UNDER (R227).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b616`s closing push-out relay %s ; push-b616* branches deleted by name '
         '(data/b617_branches.txt) ; the kept branches untouched ; the suite run at HEAD before the face (data/b617_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b616`s weight FINDINGS :%d ; the 2G fact items OPEN_TRAILS :%d ; ERRATA %s ; the currency, b618, :%d ; the arithmetic '
         'data/b617_arith.txt ; data/b617_currency.txt' % (rl['weight'], rl['fact'], [(x['id'], x['line']) for x in EJ['entries']], rl['currency']),
         '### COMPONENT 2 : the rows data/b617_rows.txt ; H51a %s, H51b %s' % (S['H51a'][0], S['H51b'][0]),
         '### COMPONENT 3 : the edition %s ; data/b617_edition_FINDINGS_STAND.txt ; H28a %s, H28b %s, H28c %s ; H51c %s ; %s' % (
             SV5, H['H28a'], H['H28b'], H['H28c'], S['H51c'][0], S['S3'][1]),
         '### COMPONENT 4 : the ζ page changed %s, the χ page changed %s ; page arms data/b617_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b618 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b617_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b617_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
