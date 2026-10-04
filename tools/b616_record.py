# -*- coding: utf-8 -*-
"""b616_record.py -- THE ACT'S RECORD TOOL, UNDER (R226). ### ONE SUBCOMMAND PER BANK.

### ### b616: LANE THREE, ACT FORTY-THREE -- THE SYNTHESIS FOR CLUSTER 2G, THE SEQUENCE'S LAST; THE SEQUENCE CLOSED AND THE
### CONSOLIDATION ENTERED.
### Subcommands write only `data/b616_*` unless the docstring names another file; `dry` on the command line routes every b616 bank and
### the document to the seat's scratchpad (for `findings`, `trail` and `record_lines`, `dry` prints and appends nothing). Banks are
### written by encode, temp file, `os.replace`; ledger appends through b566's guarded `append_to`. TECHNE-Core's module documents are read
### locally for the no-disclosure needles and never printed; the act's public text carries TECHNE by pointer alone. No platform call. No
### Lean call. The template is tools/b615_record.py.
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
import b616_claims as K  # noqa: E402

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
RELAY = ROOT.replace('\\', '/')
PRE_PP = K.PRE_PP
PRE_PP615 = 'f22a13a'
PRE_RELAY = '8c1f87dd'
STEPZERO = 'd145e6fd'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/27215af0-0981-48f7-b5c6-4a4ad5f20ef9/scratchpad'
SESSION_ID = '27215af0-0981-48f7-b5c6-4a4ad5f20ef9'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % SESSION_ID
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b602_nodes_zeta.txt', 'chi': 'b603_nodes_chi.txt'}
PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
DOC = 'phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md'
DOC2F = 'phase2/empirical/ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md'
CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
METHOD_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
TREE_REL = 'modules/2026-10/DELIBERATION_TREE.md'
BANK = 'b616_claims_2G.txt'
QEC = 'phase2/quantum/QEC_KAPPA_MAGIC_FINDINGS_v0_1.md'
SYN = {
    '1.2': 'phase1.5/proofs/THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md',
    '1.5E': 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md',
    '2B': 'phase2/philosophy/THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md',
    '2D': 'phase2/physics/THE_BARYON_FRACTION_THE_DARK_SECTOR_AND_THE_CONSTANTS_v0_2.md',
    '2F': DOC2F,
    '2G': DOC,
}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

g, sha, utc = R2.g, R2.sha, R2.utc
CEILING = R4.CEILING
DRY = 'dry' in sys.argv[2:] and sys.argv[1] not in ('findings', 'trail', 'record_lines')
DOUT = SP if DRY else D


def _p(name):
    return os.path.join(DOUT if name.startswith('b616_') else D, name)


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = _p(name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s%s (%d bytes)' % ('DRY ' if DRY and name.startswith('b616_') else '', name, len(b)))
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
    '(a) THE SEAT`S, FOUND AFTER THE SEAL, AT THE CLAIM BANK: Part H`s header (data/b616_claims_2G.txt) lists among the simulators` bank '
    'search a walk of the download folders by file name, which b616_claims.sim_banks() does not run -- it runs the two git greps alone; the '
    'walk was the seat`s own call before the seal, unbanked. The claims module, which the sealed suite reads, is not edited; the walk is '
    're-run through the record tool and banked (data/b616_sim_walk.txt), its candidate output files counted, and H50c`s reading rests on '
    'both.',
]
DEFECT_SHORT = ['(a) the seat’s: the claim bank’s Part H names a file-name walk the claims module’s search does not run; the walk re-run '
                'through the record tool and banked (relay data/b616_sim_walk.txt), the sealed suite’s claims module not edited']


def defects(*a):
    L = ['b616 -- THE DEFECT LIST (the act`s own).', '']
    L += ['    ' + d for d in DEFECTS] or ['    ### NO DEFECT RECORDED.']
    put_txt('b616_defects.txt', L)


# ================================================================================ b615 AT ITS WEIGHT, FROM ITS BANKS
def _b615():
    """### b615's figures from its banks at relay 8c1f87dd and its commits in PLACE-papers f22a13a..3dd4f29"""
    j = lambda p: json.loads(R4._show(RELAY, PRE_RELAY, 'data/' + p))   # noqa: E731
    CJ, DJ, S, RL, FJ, TJ, EJ, RR, EDJ = (j('b615_claims.json'), j('b615_doc.json'), j('b615_scores.json'), j('b615_record_lines.json'),
                                          j('b615_findings.json'), j('b615_trail.json'), j('b615_errata.json'), j('b615_reread.json'),
                                          j('b615_edition_2D.json'))
    chk = {}
    for n in ('b615_checks.txt', 'b615_checks_postpush.txt', 'b615_checks_after_edit.txt'):
        t = R4._show(RELAY, PRE_RELAY, 'data/' + n) or ''
        m = re.search(r'ARMS RUN : (\d+)\. ### LIVE PASSING : (\d+)\.', t)
        chk[n] = (int(m.group(1)), int(m.group(2))) if m else None
    log = [l.split(' ', 1) for l in g(PP, 'log', '--format=%h %s', PRE_PP615 + '..' + PRE_PP).split(NL) if l.strip()]
    com = lambda pre: next((h for h, s in log if s.startswith(pre)), '?')   # noqa: E731
    rlog = [l.split(' ', 1) for l in g(RELAY, 'log', '--format=%h %s', 'b89d88e8..' + PRE_RELAY).split(NL) if l.strip()]
    edit = next((h for h, s in rlog if s.startswith('b615 (R225)(4): the suite edit')), '?')
    return dict(CJ=CJ, DJ=DJ, S={k: v[0] for k, v in S.items()}, RL=RL, FJ=FJ, TJ=TJ, EJ=EJ, RR=RR['syntheses'], EDJ=EDJ, chk=chk,
                doc=com('b615 (R225)(5): '), ed=com('b615 (R225)(2): '), err=com('b615 (R225)(3): ERRATA'), rec=com('b615 (R225): '), edit=edit)


def weight615_lines():
    W = _b615()
    gr, CJ = W['CJ']['grades'], W['CJ']
    L = ['### b615 AT ITS WEIGHT, printed from its banks at relay %s and its commits in PLACE-papers %s..%s:' % (PRE_RELAY, PRE_PP615, PRE_PP),
         '    the document `%s` v0.1 at PLACE-papers %s, tier %s, %d claims: %s' % (W['DJ']['path'], W['doc'], W['DJ']['tier'], CJ['n'],
                                                                                    ', '.join('%s %d' % (k, gr.get(k, 0)) for k in K.GRADES)),
         '    the certifying pins %s ; load-bearing %s ; the route rows %s, matched %s' % (CJ['kvpins'], CJ['load_bearing'] or 'none', CJ['routes'],
                                                                                         [(m[0], m[1], m[2]) for m in CJ['matched']]),
         '    the re-read %s ; 2D`s v0.2 `%s` at %s, sha256 %s' % ({k: '%s -> %s' % (v['tier_now'], v['tier_read']) for k, v in W['RR'].items()},
                                                                  W['EDJ']['path'], W['ed'], W['EDJ']['sha256'][:16]),
         '    ERRATA %s at %s ; the suite edit relay %s' % ([(e['id'], e['line']) for e in W['EJ']['entries']], W['err'], W['edit']),
         '    the record lines %s ; FINDINGS entry :%d ; trail record :%d ; the record commit %s' % ([(x['file'], x['line']) for x in W['RL']['lines']],
                                                                                                   W['FJ']['entry_line'], W['TJ']['line'], W['rec']),
         '    the scores %s' % W['S'],
         '    the suite (arms run, live passing): pre-push %s, post-push %s; the run after the edit, made mid-act before the record banks '
         'existed, %s, its ls-remote calls %s' % (W['chk']['b615_checks.txt'], W['chk']['b615_checks_postpush.txt'], W['chk']['b615_checks_after_edit.txt'],
                                                  json.loads(R4._show(RELAY, PRE_RELAY, 'data/b615_lsr_after_edit.json')).get('lsr'))]
    return L


# ================================================================================ READING (1): THE READS
_SYN_SEL = ('GREP', r'^# |^\*\*DOCUMENT CLASS|^\*This document synthesises|^\*v0\.[12], |^## Correspondence|^## 1\. |^## Back matter|'
                    r'^### The routes through the five tests|^\| R\d+ \| ')
READS = [
    ('THE_KEYSTONE_CENSUS v0.3: the 2G rows', PP, PRE_PP, CEN3, ('GREP', r'^\| R17 \||^- \*\*R17 '), 1200),
    ('REGISTRY.md: the 2G heading and rows p2-d1 to p2-d9', PP, PRE_PP, 'REGISTRY.md', [297, 301, 302, 303, 304, 305, 306, 307, 308, 309], 420),
] + [('%s whole (%s)' % (v[0].split('/')[-1], v[1]), PP, PRE_PP, v[0], 'ALL', 300) for k, v in K.PAPERS.items()] + [
    ('the five syntheses: title, tier line, head line, version line, the Correspondence and body heads, the route rows (%s)' % k, PP, PRE_PP, p,
     _SYN_SEL, 700) for k, p in SYN.items() if k != '2G'] + [
    ('THE_DOCUMENT_CLASS_TAXONOMY.md: the tier definitions and (R19)`s KC', PP, PRE_PP, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md',
     [14, 16, 18, 20, 57, 59, 61, 63], 700),
    ('the sieve v0.4: the five tests, RH-58, RH-59, RH-60 and the cosmology row MC-01', PP, PRE_PP, K.SIEVE,
     [24, 26, 28, 29, 30, 31, 32, 120, 121, 122, 578, 582], 700),
    ('OPEN_TRAILS: the form, the arm-unrun standing line, the precedence order, the sequence`s form, the form`s clauses and the load-bearing '
     'clause, the standing line, b614`s For-the-author line, b615`s record', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11864, 12188, 12228, 12566, 12601, 12683, 12699, 12703, 12705, 12707, 12709, 12711, 12713, 12715, 12717], 1500),
    ('FINDINGS: b615`s weight line for b614 and b615`s entry', PP, PRE_PP, 'FINDINGS.md', [7320, 7322], 600),
    ('the companion findings paper of the simulators (a report, not a bank)', PP, PRE_PP, QEC, [13, 15, 19, 20, 21, 22, 23, 24, 25, 26, 38, 106, 107],
     260),
    ('relay data/b615_closing_push_out.txt (committed at step zero)', RELAY, STEPZERO, 'data/b615_closing_push_out.txt', 'ALL', 260),
    ('relay data/b615_scores.json (whole)', RELAY, STEPZERO, 'data/b615_scores.json', 'ALL', 300),
    ('SIDE-t7-topology-cmb main: the run`s provenance', 'D:/SIDE-t7-topology-cmb', 'main', 'RUN_PROVENANCE.md', list(range(108, 126)), 260),
] + [('%s at %s: %s' % (K.PINS_NT[v[0]][0], K.PINS_NT[v[0]][1], k), 'D:/' + K.PINS_NT[v[0]][0], K.PINS_NT[v[0]][1], v[1], [v[2]], 260)
     for k, v in K.NTREADS.items()]


def reads(*a):
    L = ['b616 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
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
            if 'TECHNE' in line and path.endswith('QUATERNIONIC.md'):
                line = ' '.join(line.split()[:6]) + ' ### [TECHNE CONTENT: by pointer alone, TECHNE-Core manifest sha256 %s]' % K.techne_pointer()
            L.append('    :%-6d %s' % (n, line[:width]))
    L += [''] + weight615_lines()
    L += ['', '### THE PINS THE PAPERS NAME, EACH AS CITED, RESOLVED IN ITS CLONE AND AT ITS REMOTE (no paper names a terminal at a pin):']
    for k in K.PINS_NT:
        st = K.pin_state(k)
        L.append('    %-6s %s %s -> %s ; at the remote: %s -- named at %s ; the commit`s subject: %s' % (
            k, st[1], st[2], st[3] or '### DOES NOT RESOLVE AS CITED', st[4] or '### NONE', K.PINS_NT[k][3], K.commit_subject(k) if st[3] else '—'))
    L += ['    the registered run`s bank: %s' % K.t7_bank(),
          '    the simulators` bank search (%s; needles %s): %s' % ('; '.join('%s by %s' % x for x in K.SIM_SEARCH), list(K.SIM_NEEDLES),
                                                                   K.sim_banks() or 'NONE')]
    nd = nd_sets()
    L += ['### THE NO-DISCLOSURE NEEDLE SETS, read locally at TECHNE-Core %s and never printed: the method document %s, %d sentences of 40 '
          'characters or more (b591`s form); the tree %s, %d (b595`s form); every module document, %d sentences of 60 characters or more '
          '(b611`s form)' % (g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), METHOD_REL, len(nd['method']), TREE_REL, len(nd['tree']), len(nd['modules'])),
          '### TECHNE mentions in the cluster`s files: %s ; the pointer each takes: TECHNE-Core, its tracked-file manifest sha256 %s' % (
              {k: sum(l.count('TECHNE') for l in K.lines_of(K.show(v[0]))) for k, v in K.PAPERS.items()}, K.techne_pointer()),
          '### PLACE-papers HEAD at the reads: %s ; relay HEAD: %s' % (g(PP, 'rev-parse', '--short=8', 'HEAD').strip(), g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip())]
    put_txt('b616_reads.txt', L)


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
    L = ['### b616 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-04), banked verbatim with the options and the '
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
    put_txt('b616_author_answers.txt', L)


KERNS = ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-global-section', 'SIDE-effects', 'SIDE-t7-topology-cmb',
         'SIDE-local-cosmic-interface', 'SIDE-quaternionic-dark-sector', 'SIDE-omega-b', 'SIDE-cosmo', 'SIDE-constants')
KERN_PIN = {'SIDE-explicit-formula': '1d5d4dd', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-global-section': '3528bcf',
            'SIDE-t7-topology-cmb': '936cd65', 'SIDE-local-cosmic-interface': '7a62ced', 'SIDE-quaternionic-dark-sector': 'e860142'}


def kern_state():
    out = {}
    for k in KERNS:
        p = 'D:/' + k
        out[k] = (g(p, 'rev-parse', '--short=7', 'main').strip(), sorted(x for x in g(p, 'tag', '-l').split(NL) if x.strip()),
                  sorted(x for x in g(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()))
    return out


def kernels(*a):
    """### data/b616_kernels_face.json: every kernel this act reads, its main, its tags and its branches, banked before the seal"""
    put_json('b616_kernels_face.json', dict(at=utc(), kernels={k: list(v) for k, v in kern_state().items()}))


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


# ================================================================================ COMPONENT 1: THE ARITHMETIC AND THE RECORD LINES
def arith(*a):
    """### data/b616_arith.txt and its json: (R226)(2)'s three ZERO_SIMPLICITY computations, each computed here."""
    import mpmath
    import numpy as np
    mpmath.mp.dps = 30
    x0 = mpmath.findroot(mpmath.digamma, 1.46)
    sg = [mpmath.digamma(mpmath.mpf(x)) for x in ('1.4', '1.5')]
    g1 = mpmath.im(mpmath.zetazero(1))
    mods = [(p, abs(mpmath.power(p, -(mpmath.mpf(1) / 2 + 1j * g1)))) for p in (2, 3, 5, 7)]
    rng = np.random.default_rng(616)
    n = 4

    def herm(m):
        A = rng.normal(size=(m, m)) + 1j * rng.normal(size=(m, m))
        return (A + A.conj().T) / 2
    A, B = herm(n), rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    B = (B - B.T) / 2
    Hs = np.block([[A, B], [-B.conj(), A.conj()]])   # ### commutes with T = (iσ_y ⊗ I) K, T² = −I: the symplectic class
    J = np.block([[np.zeros((n, n)), np.eye(n)], [-np.eye(n), np.zeros((n, n))]])
    tinv = np.allclose(J @ Hs.conj() @ J.T, Hs)
    es = np.linalg.eigvalsh(Hs)
    pair = max(abs(es[2 * k] - es[2 * k + 1]) for k in range(n))
    sep = min(es[2 * k + 2] - es[2 * k + 1] for k in range(n - 1))
    eg = np.linalg.eigvalsh(herm(2 * n))
    gmin = min(np.diff(eg))
    L = ['b616 -- COMPONENT 1: THE ARITHMETIC OF (R226)(2), the 2F papers` fact items, computed %s (Python %s, mpmath %s, numpy %s)' % (
        utc(), sys.version.split()[0], mpmath.__version__, np.__version__), '',
         '### (i) ZERO_SIMPLICITY :28 (phase2/empirical/ZERO_SIMPLICITY.md): “The digamma function has no zeros in the right half-plane”.',
         '    ψ(1.4) = %s, ψ(1.5) = %s: a sign change; the root ψ(x₀) = 0 at x₀ = %s, on the positive real axis.' % (
             mpmath.nstr(sg[0], 8), mpmath.nstr(sg[1], 8), mpmath.nstr(x0, 12)),
         '    THE FACT OF RECORD: ψ vanishes at x₀ ≈ 1.4616 in the right half-plane, so the sentence is false of ψ as stated (b615`s claim bank found '
         'the paper`s conclusion, |f₃(γ)| bounded away from zero, standing on other grounds).', '',
         '### (ii) ZERO_SIMPLICITY :26: “At σ = 1/2, the balance identity forces each term p⁻ˢ to lie on the unit circle”.',
         '    |p^(−s)| at s = 1/2 + iγ₁ (γ₁ = %s): %s' % (mpmath.nstr(g1, 10), ' ; '.join('p = %d: %s (p^(−1/2) = %s)' % (
             p, mpmath.nstr(v, 8), mpmath.nstr(mpmath.power(p, -0.5), 8)) for p, v in mods)),
         '    THE FACT OF RECORD: |p^(−s)| = p^(−1/2) on the line, not 1; the terms do not lie on the unit circle.', '',
         '### (iii) ZERO_SIMPLICITY :93: “| GUE | T² = −I (complex) | 2 | Fermionic |”.',
         '    a Hermitian matrix of size %d built to commute with the antiunitary T = (iσ_y ⊗ I)K, T² = −I: T-invariant %s; its levels pair, the largest '
         'difference within a pair %.2e, the smallest distance between pairs %.4f; a GUE matrix of the same size (no antiunitary symmetry): '
         'smallest level spacing %.4f' % (2 * n, tinv, pair, sep, gmin),
         '    THE FACT OF RECORD: an antiunitary symmetry with T² = −I forces Kramers pairs, the symplectic class of Dyson`s classification, β = 4; '
         'GUE`s β = 2 is the class with no antiunitary symmetry.', '',
         '### (iv) BSD_VIA_FORMATION_TRANSFER`s Chapter 7 listing (:325-:370) and the placeholder name excluded (:64, :267) against '
         'SIDE-effects c66f3c5 (mismatch_absent): no computation; b615`s claim bank (relay data/b615_claims_2F.txt, BV-30, BV-36) read the file, '
         'and the listing is diffed against it at the paper`s edition.']
    put_txt('b616_arith.txt', L)
    put_json('b616_arith.json', dict(at=utc(), psi_root=mpmath.nstr(x0, 12), psi_14=float(sg[0]), psi_15=float(sg[1]), gamma1=mpmath.nstr(g1, 12),
                                     mods={str(p): float(v) for p, v in mods}, kramers=dict(size=2 * n, t_invariant=bool(tinv), pair_max=float(pair),
                                                                                           pair_sep=float(sep), gue_min=float(gmin))))
    for l in L:
        print(l[:220])


B615_ENTRY = '## The 2F synthesis: zero simplicity and the formation transfer to elliptic curves at v0.1'
B615_TRAIL = '### b615 — lane three, act forty-two under (R225): the synthesis for 2F'
B614_AUTHOR = '**For the author:** (1) the 2D papers’ findings, for their next editions: COSMOLOGICAL_SIEVE_CEILING :72'
SEQ_FORM = '*Appended 2026-10-03 by b610, under `(R220)`(5), the author’s explicit ask -- THE SYNTHESIS SEQUENCE, ENTERED WITH ITS FORM:*'
CR_HEAD = ('*Appended 2026-10-04 by b616 to b614’s trail record, its For-the-author line (:%d), under `(R226)`(1) -- A DATED CORRECTION LINE, THE '
           'LINE ABOVE NOT EDITED:*')
F_HEAD = ('*Appended 2026-10-04 by b616 to b615’s record (:%d), under `(R226)`(2) -- THE 2F PAPERS’ FINDINGS, FACT ITEMS FOR THEIR NEXT EDITIONS, '
          'THE SYNTHESIS’S ROWS STANDING AS GRADED:*')
CN_HEAD = ('*Appended 2026-10-04 by b616 to the synthesis sequence’s form (:%d), under `(R226)`(4) -- THE CONSOLIDATION, THE ACTS AFTER THE '
           'SEQUENCE, IN ORDER, EACH ON THE AUTHOR’S WORD AT ITS CLOSING:*')
W_HEAD = '*Appended 2026-10-04 by b616 to b615’s entry (:%d), under `(R226)`(1) -- b615 AT ITS WEIGHT:*'


def _texts(entry, trail, author, form, dry=False):
    A = json.load(io.open(os.path.join(SP if dry else D, 'b616_arith.json'), encoding='utf-8'))
    tcr = ('\n%s the line prints the proportions it reports for Selberg, for Conrey and for the record each with a doubled percent sign; they read '
           '40 percent, 41.6 percent and 100 percent. The doubling is a formatting slip of b614’s record tool, the sense unchanged, as b615’s record '
           'notes at :%d.\n' % (CR_HEAD % author, trail + 8))
    tf = ('\n%s (i) phase2/empirical/ZERO_SIMPLICITY.md :28 says the digamma function has no zeros in the right half-plane, where ψ vanishes on the '
          'positive real axis at x₀ ≈ %s -- the sentence is false of ψ as stated, its conclusion that |f₃| stays bounded away from zero standing on '
          'other grounds (relay data/b615_claims_2F.txt); a fact item. (ii) ZERO_SIMPLICITY :26 puts each p^(−s) on the unit circle at σ = 1/2, where '
          '|p^(−s)| = p^(−1/2), %.4f at p = 2 and %.4f at p = 3, not 1; a fact item. (iii) ZERO_SIMPLICITY :93 assigns T² = −I to GUE, where an '
          'antiunitary symmetry with T² = −I is the symplectic class, Dyson β = 4, its levels in Kramers pairs, and GUE’s β = 2 carries no '
          'antiunitary symmetry; a fact item. The three computations are banked at relay data/b616_arith.txt. (iv) '
          'phase2/empirical/BSD_VIA_FORMATION_TRANSFER.md prints in its Chapter 7 (:325-:370) a kernel listing and gives the placeholder the name '
          'excluded (:64, :267), where SIDE-effects c66f3c5 defines mismatch_absent; a fact item, the listing diffed against that file at the '
          'paper’s edition. The synthesis’s rows for these claims (ZS-05, ZS-07, ZS-19, BV-30, BV-36) stand at the grades b615 gave them.\n' % (
              F_HEAD % trail, A['psi_root'][:6], A['mods']['2'], A['mods']['3']))
    tc = ('\n%s (i) the sieve’s v0.5, taking every route the six syntheses listed for it -- the work-list at relay data/b616_routes_for_sieve.txt, '
          'gathered at b616 and deduplicated by conclusion -- with its head’s counts re-stated; (ii) THE_KEYSTONE_CENSUS’s v0.4, its six '
          'no-keystone rows (P12, 15E, 2B, 2D, 2F and 2G) updated to name their keystones and tiers; (iii) W-ORD-SECOND-READER’s batch, now the '
          'three monograph acts, the sieve’s editions and the six syntheses, run by its form; (iv) W-ORD-QUANTIFIER-COLUMN’s generator with '
          'DENSITY, the pages re-emitted and the sieve’s hand-read H marks replaced; (v) W-ORD-TAG-REMOTES; (vi) the mirror refreshed after (iv). '
          'Each act begins on the author’s word at the closing of the act before it, the first on the word at b616’s closing. The deposit of the '
          'edition wave is a separate (R110)-route item for the author’s word and is not entered here.\n' % (CN_HEAD % form))
    return [(CR_HEAD % author, tcr), (F_HEAD % trail, tf), (CN_HEAD % form, tc)]


def _weight(entry, cline, fline, nline):
    W = _b615()
    gr, CJ, S = W['CJ']['grades'], W['CJ'], W['S']
    allh = lambda ks, w: w if all(S[k] == w for k in ks) else [S[k] for k in ks]   # noqa: E731
    rr = W['RR']
    pre, post = W['chk']['b615_checks.txt'], W['chk']['b615_checks_postpush.txt']
    return ('\n%s ZERO_SIMPLICITY_AND_THE_FORMATION_TRANSFER_TO_ELLIPTIC_CURVES.md v0.1 (PLACE-papers %s) in its cluster’s folder: three papers '
            'read whole at f22a13a and unedited; %d claims -- %s; tier %s under the load-bearing clause, the %d kernel-verified rows at %d pins in '
            '%d kernels, each resolving in its clone and at its remote, and none load-bearing; %d route rows -- the codimension argument DARK by '
            'test 2 (RH-60), the GUE argument DARK by test 1 (RH-59), the transfer to L(E, s) DARK by test 2 (RH-60), the computed range NOT A '
            'ROUTE (RH-58). The re-read of four tier lines: 1.2 %s, 1.5E %s, 2B %s, 2D %s -> %s, 2D’s v0.2 at %s carrying its Placement and '
            'Version history unedited under “nothing else”, which the author accepts. ERRATA %s (:%d) and %s (:%d) at %s; the suite edit committed '
            'alone at relay %s, the run after it at one ls-remote call per repository. The verdicts, as relay data/b615_scores.json prints them: '
            'H49a-H49d %s; N1-N5 %s; S1-S5 %s; the suite %d of %d pre-push and %d of %d post-push. Confirmed by the author: the transfer to L(E, s) '
            'read as the RH argument transferred and matched to RH-60; the PRIME_ORDER stretch from 137 to 337 entered beside the named one as the '
            'seat’s own computation; the full findings list at OPEN_TRAILS :%d, inside b615’s record at :%d; the doubled percent signs of b614’s '
            'record take the dated correction line at :%d. The 2F papers’ findings at :%d; the consolidation at :%d. Nothing deposited; no kernel '
            'touched; TECHNE-Core untouched.\n' % (
                W_HEAD % entry, W['doc'], CJ['n'], ', '.join('%d %s' % (gr.get(k, 0), k) for k in K.GRADES), W['DJ']['tier'], W['DJ']['cert_rows'],
                len(CJ['kvpins']), len(set(x.split()[0] for x in CJ['kvpins'])), len(CJ['routes']), rr['1.2']['tier_read'], rr['1.5E']['tier_read'],
                rr['2B']['tier_read'], rr['2D']['tier_now'], rr['2D']['tier_read'], W['ed'], W['EJ']['entries'][0]['id'], W['EJ']['entries'][0]['line'],
                W['EJ']['entries'][1]['id'], W['EJ']['entries'][1]['line'], W['err'], W['edit'], allh(('H49a', 'H49b', 'H49c', 'H49d'), 'HOLDS'),
                allh(('N1', 'N2', 'N3', 'N4', 'N5'), 'HELD'), allh(('S1', 'S2', 'S3', 'S4', 'S5'), 'HELD'), pre[1], pre[0], post[1], post[0],
                W['TJ']['line'] + 8, W['TJ']['line'], cline, fline, nline))


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
    return Q, Q.line_of(Q.FIND, B615_ENTRY), Q.line_of(Q.OT, B615_TRAIL), Q.line_of(Q.OT, B614_AUTHOR), Q.line_of(Q.OT, SEQ_FORM)


def record_lines(*a):
    """### OPEN_TRAILS: the dated correction line (addressed to b614's For-the-author line), the 2F fact items (addressed to b615's record),
    ### the consolidation (addressed to the sequence's form); then FINDINGS: b615's weight, addressed to b615's entry -- each appended at the
    ### end. Needs the arithmetic."""
    Q, entry, trail, author, form = _addr()
    if (entry, trail, author, form) != (7322, 12705, 12683, 12566):
        sys.exit('### AN ADDRESSED LINE MOVED (%s, %s, %s, %s) -- NOTHING WRITTEN' % (entry, trail, author, form))
    dry = 'dry' in a
    if not os.path.exists(os.path.join(SP if dry else D, 'b616_arith.json')):
        sys.exit('### b616_arith.json IS NOT BANKED -- NOTHING WRITTEN')
    parts = _texts(entry, trail, author, form, dry)
    wt = _weight(entry, 0, 0, 0)
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
    wt = _weight(entry, out[0]['line'], out[1]['line'], out[2]['line'])
    r = Q.append_to(Q.FIND, wt)
    out.append(dict(file='FINDINGS.md', head=W_HEAD % entry, line=Q.line_of(Q.FIND, W_HEAD % entry), append=r))
    put_json('b616_record_lines.json', dict(entry=entry, trail=trail, author=author, form=form, lines=out))
    for o in out:
        print('  %s :%s' % (o['file'], o['line']))


def _rl():
    """### the record lines by role: correction, fact, consolidation, weight"""
    ls = jl('b616_record_lines.json')['lines']
    return dict(zip(('correction', 'fact', 'consolidation', 'weight'), [x['line'] for x in ls]))


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


def h50c_lines(CC):
    sims = [c for c in CC if c[1] in K.SIMULATORS]
    banks = K.sim_banks()
    cv = [c[0] for c in sims if c[5] == 'computationally-verified']
    ok = (not banks and not cv) or (bool(banks) and all(c[5] == 'computationally-verified' for c in sims))
    L = ['  %-6s %s :%-4d %-17s -- a bank holds the run: %s' % (c[0], c[1], c[2], c[5], 'yes' if banks else 'no') for c in sims]
    verdict = 'HOLDS' if ok else 'REFUTED'
    return L, verdict, ('%d simulator claims, %d graded computationally-verified, %d below it; the bank search found %s -- every claim graded below '
                        'computationally-verified for want of a banked run; the arm`s other side, computationally-verified where a bank holds the run, '
                        'is VACUOUS: no bank holds a run of either simulator' % (len(sims), len(cv), len(sims) - len(cv), banks or 'none')
                        if not banks else '%d simulator claims, %d computationally-verified, banks %s' % (len(sims), len(cv), banks))


SIM_ROOTS = ('D:/MY-DOwnloads', 'D:/HERITAGE', 'D:/PLACE-phase2', 'D:/PLACE-phase1.5')
OUT_SUFFIX = ('.txt', '.json', '.csv', '.log', '.out', '.npy', '.npz', '.pkl', '.dat')


def sim_walk(*a):
    """### data/b616_sim_walk.txt and its json: the download folders walked by file name (git directories, build trees and the PLACE-papers
    ### clone skipped), every file whose name carries qec or kappa listed, and those with an output's suffix counted as candidate banks."""
    hits = []
    for root in SIM_ROOTS:
        for dp, dn, fn in os.walk(root):
            dn[:] = [d for d in dn if d not in ('.git', '.lake', 'node_modules', 'PLACE-papers')]
            for f in fn:
                if 'qec' in f.lower() or 'kappa' in f.lower():
                    hits.append(os.path.join(dp, f).replace('\\', '/'))
    cand = [h for h in hits if h.lower().endswith(OUT_SUFFIX)]
    pat = [h for h in hits if '/patent-package' in h]
    shown = [h for h in hits if h not in pat]
    kinds = sorted(set(os.path.splitext(h)[1] for h in pat))
    L = ['b616 -- THE SIMULATORS` BANK SEARCH BY FILE NAME, %s: roots %s, the git directories, build trees and the PLACE-papers clone skipped' % (
        utc(), list(SIM_ROOTS)), '### files whose name carries qec or kappa (%d): %d listed; %d in the patent repository, their names withheld '
        '(local-only, the standing rule of b590), of kinds %s' % (len(hits), len(shown), len(pat), kinds)] + ['    ' + h for h in sorted(shown)] + [
        '### ### **CANDIDATE OUTPUT FILES (suffix %s): %d**' % ('/'.join(OUT_SUFFIX), len(cand))]
    put_txt('b616_sim_walk.txt', L)
    put_json('b616_sim_walk.json', dict(at=utc(), roots=list(SIM_ROOTS), n_hits=len(hits), listed=sorted(shown), patent_withheld=len(pat),
                                        patent_kinds=kinds, candidates=len(cand)))
    print(L[-1])


def claims(*a):
    """### data/b616_claims_2G.txt and data/b616_claims.json: each paper's and simulator's path, version and head; every claim with its line,
    ### grade and reason; the routes through the five tests; the pins named without a terminal, the registered run's bank, the simulators'
    ### bank search; the TECHNE citation with its pointer; the cluster's arithmetic; H50a's trace table and H50c -- banked before any writing."""
    P = K.paper_lines()
    rc = dict((i, (ok, l)) for i, ok, l in K.resolve_claims())
    nt = K.resolve_nt()
    sieve = K.sieve_rows()
    CC = K.claims()
    if not all(ok for ok, _l in rc.values()) or not all(ok for _k, ok, _l in nt):
        sys.exit('### A NEEDLE FAILS -- NOTHING WRITTEN')
    bad = [c[0] for c in K.C if not K.grade_ok(c)]
    if bad:
        sys.exit('### GRADES OUT OF RULE %s -- NOTHING WRITTEN' % bad)
    L = ['b616 -- COMPONENT 2: THE CLAIM BANK OF CLUSTER 2G, (R226)(3), banked %s before any writing' % utc(),
         '### the papers and simulators at PLACE-papers %s; the sieve v0.4 at %s' % (PRE_PP, PRE_PP)]
    L += ['### ' + x.strip('# ').strip() for x in K.__doc__.split(NL) if 'GRADING RULE' in x or 'kernel-verified only' in x or 'computationally-verified only' in x
          or 'synthesis-suggested where' in x or 'paper\'s own support' in x or 'THE SIMULATORS' in x or 'A ROUTE is' in x or 'RESOLVES' in x
          or 'LOAD-BEARING CLAUSE' in x] + ['']
    L += ['### PART A -- THE PAPERS AND THE SIMULATORS, EACH WITH ITS PATH, REGISTRY ROW, VERSION AND HEAD:']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        ls = P[k]
        reg = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        ver = next((l.strip() for l in ls[:12] if re.search(r'v\d+\.\d|Version|April 2026|May 2026|June 2026|July 2026', l)), '')
        L.append('  %s = `%s` -- REGISTRY %s (:%d), its version %s, its status %s -- %d lines -- head :1 “%s” -- its own version/date line “%s” '
                 '-- last commit %s' % (k, path, rid, rline, reg[3], reg[5].replace('*', '')[:40], len(ls), ls[0][:120], ver[:120],
                                       g(PP, 'log', '-1', '--format=%h %ad', '--date=short', PRE_PP, '--', path).strip()))
    L += ['  lines in all: %d (the papers %d, the simulators %d)' % (sum(len(v) for v in P.values()), sum(len(v) for k, v in P.items() if k not in K.SIMULATORS),
                                                                    sum(len(v) for k, v in P.items() if k in K.SIMULATORS))]
    L += ['', '### PART B -- THE CLAIMS, EACH WITH ITS LINE, NEEDLE, GRADE AND REASON (%d):' % len(CC)]
    for c in CC:
        cid, pk, n, needle, text, grade, support, reason, route = c
        L.append('  %-6s %s :%-4d %-25s support %-11s -- %s' % (cid, pk, n, grade, support, text))
        L.append('         needle “%s” on the line: %s ; reason: %s%s' % (needle[:90] if 'TECHNE' not in needle else needle[:30], rc[cid][0], reason,
                                                                     (' ; route %s %s%s' % (route[0], route[1], '' if route[2] is None else ' test %d' % route[2])) if route else ''))
    L += ['', '### PART C -- THE ROUTES, EACH THROUGH THE FIVE TESTS IN ORDER, WITH ITS VERDICT AND INSTRUMENT:']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        passed = ('tests 1-%d passed; ' % (t - 1)) if t and t > 1 else ''
        L.append('  %s -- claims %s -- %s%s -- %s, %s -- %s -- the sieve`s row %s' % (
            r, ', '.join(x[0] for x in cs), passed, 'fails test %d' % t if t else 'not asked (not a route)', v, inst, why,
            ('%s = %s' % (row, ' '.join(sieve.get(row, ('?', ''))))) if row else 'none'))
    L += ['  the cosmology claims (κ, the census, the topology, the embedding, α_T) are offered toward no target the sieve reads, as its row MC-01 = %s '
          'reads the constants and the empirical layer' % ' '.join(sieve.get('MC-01', ('?', '')))]
    L += ['', '### PART D -- THE PINS THE PAPERS NAME (none with a terminal), THE READS THERE, AND THE REGISTERED RUN`S BANK:']
    for k in K.PINS_NT:
        st = K.pin_state(k)
        L.append('  no terminal: %-6s %s %s -> commit %s ; at the remote: %s ; named at %s' % (k, st[1], st[2], st[3] or 'DOES NOT RESOLVE AS CITED',
                                                                                           st[4] or 'NONE', K.PINS_NT[k][3]))
    for k, ok, l in nt:
        v = K.NTREADS[k]
        L.append('  read for the record %-7s %s :%d at %s -- needle on the line: %s -- %s' % (k, v[1], v[2], K.PINS_NT[v[0]][1], ok, v[4]))
    L.append('  the commits` subjects: %s' % [K.commit_subject(k) for k in K.PINS_NT if K.pin_state(k)[3]])
    tb = K.t7_bank()
    L.append('  the registered run`s bank: %s:%s at %s -- %s' % (K.T7BANK[0], K.T7BANK[2], K.T7BANK[1], tb))
    L.append('  load-bearing reading: no row reads kernel-verified; LOAD %s' % (K.LOAD or 'empty'))
    T = json.loads(R4._show(RELAY, STEPZERO, 'data/terminal_table.json') or '[]')
    TT = T.get('rows') if isinstance(T, dict) else T
    for nm in ('kappa_x100', 'em_98', 'dm_total_eq_16_over_3', 'decomp_A_factorization', 'twenty_one_incidences', 'T7_torsion_eight', 'riemannZeta'):
        r = [x for x in TT if str(x.get('name', '')).split('.')[-1] == nm]
        L.append('  the terminal table on %s: %s' % (nm, ['%s %s %s %s' % (x.get('repo'), x.get('name'), x.get('pin'), x.get('grade')) for x in r] or 'no row'))
    zl = K.lines_of(io.open(os.path.join(D, NODES['zeta']), encoding='utf-8').read())
    xl = K.lines_of(io.open(os.path.join(D, NODES['chi']), encoding='utf-8').read())
    names = ['kappa_x100', 'dm_total_eq_16_over_3', 'T7_torsion_eight', 'H1_free_rank']
    hit = [n for n in names if any(n in l for l in zl + xl)]
    L += ['  the pages: ζ list %d lines, χ list %d lines; nodes of either the cluster names: %s' % (len(zl), len(xl), hit or 'none')]
    L += ['', '### PART E -- THE TECHNE CITATION: QD :228, carried by pointer alone -- TECHNE-Core, its tracked-file manifest sha256 %s ; no sentence '
          'of its body carried and no tool of it named' % K.techne_pointer()]
    L += ['', '### PART F -- THE CLUSTER`S ARITHMETIC, RECOMPUTED (mpmath %s):' % __import__('mpmath').__version__]
    AR = K.arith2g()
    for lab, val, paper, ok in AR:
        L.append('  %s -- computed %s ; the paper %s ; %s' % (lab, val, paper, 'AGREES' if ok else '### DIFFERS'))
    trace = sorted(set((c[1], c[2]) for c in CC))
    L += ['', '### PART G -- H50a`S TRACE TABLE: the (paper, line) pairs a body sentence may cite, each a claim line above (%d):' % len(trace),
          '  ' + ', '.join('%s :%d' % x for x in trace)]
    hl, hv, hwhy = h50c_lines(CC)
    L += ['', '### PART H -- THE SIMULATORS AND H50c: the bank search (%s; needles %s): %s' % ('; '.join('%s by %s' % x for x in K.SIM_SEARCH),
                                                                                          list(K.SIM_NEEDLES), K.sim_banks() or 'NONE')] + hl
    L += ['### ### **H50c %s** -- %s' % (hv, hwhy)]
    reached, matched, listed = route_score(sieve)
    from collections import Counter
    gc = Counter(c[5] for c in CC)
    L += ['', '### THE GRADES: %s' % ', '.join('%s %d' % (gname, gc.get(gname, 0)) for gname in K.GRADES),
          '### THE CERTIFYING PINS: none ; LOAD-BEARING ROWS: none',
          '### THE ROUTES: %d (%s); against the sieve: %s; with no row, listed for its next version: %s' % (
              len(reached), ', '.join(sorted(reached)), '; '.join('%s against %s: %s / %s -- %s' % (r, row, m, t, 'MATCH' if ok else 'DIFFER')
                                                                  for r, row, m, t, ok in matched) or 'none', listed or 'none')]
    put_txt(BANK, L)
    put_json('b616_claims.json', dict(at=utc(), n=len(CC), routes=sorted(_route_rows()), grades=dict(gc), trace=trace, matched=matched, listed=listed,
                                      kvpins=[], load_bearing=[], pointer=K.techne_pointer(), h50c=hv, h50c_why=hwhy, sim_banks=K.sim_banks(), t7_bank=tb,
                                      arith=[dict(label=x[0], value=x[1], paper=x[2], agrees=x[3]) for x in AR],
                                      claims=[dict(id=c[0], paper=c[1], line=c[2], grade=c[5], support=c[6], route=c[8][0] if c[8] else None) for c in CC]))
    print(L[-3])
    print(L[-2])
    print(L[-1])
    print('### ### **H50c %s**' % hv)


# ================================================================================ COMPONENT 3: THE DOCUMENT
TITLE = ('# The Local–Cosmic Interface and the Dark Sector: the κ Channels, the P-smooth Census, the T-seven Matched-Arc Search, the (ℤ/2)³ '
         'Embedding and the 77/4 Ratio, the Alignment Constant α_T and the Steane κ Simulators')
PROPERTY_WORDS = re.compile(r'\b(?:[Pp]roofs?|[Pp]rov(?:e|ed|en|es|ing)|[Cc]omplete|[Vv]erified|[Rr]esolved|[Ee]stablished|[Ff]orced|[Ss]ettled|'
                            r'[Cc]losed|[Dd]ecisive|[Dd]efinitive|[Uu]nconditional|[Uu]nique|[Ee]xact)\b')
HEADLINE = '*This document synthesises the seven papers and two simulators it names and certifies nothing they do not.*'
VERSION = ('*v0.1, 2026-10-04 -- written at b616 under `(R226)`(3), the synthesis for 2G that THE_KEYSTONE_CENSUS v0.3 names (its row R17), the '
           'sequence’s last.*')
BM_TAG = '<!-- b616 (R226) THE v0.1 BACK MATTER, 2026-10-04 -->'
BODY1 = '## 1. The papers and their status'

BODY = [
    (BODY1, [
        'The cluster’s seven papers read the boundary between local physics and cosmology as an interface with a conservation strength κ, and the dark sector as its formation distance (SF :12, DM :12, FD :14).',
        'T7_CMB reports a pre-registered search run once (TC :172), THEORY_SPACE an analysis of physical theories by structural class (TH :18), and the two simulators measure κ on the Steane code, no bank holding a run of either (QI :187, QV :66).']),
    ('## 2. The κ channels and the symmetry filter', [
        'SF defines κ(Q, I) as the share of a quantity’s structure that survives an interface and the formation distance as Δμ = n − μ (SF :26, SF :28).',
        'It assigns κ from 0.98 for electromagnetism down to 0 for the dark sector over eight channels, values given without a measurement procedure (SF :38, SF :20), and LC assesses κ per channel as the share of local information that predicts the cosmic observable (LC :28).',
        'LC’s means, 0.70 over eight channels and 0.80 without the dark sector, recompute as 0.704 and 0.804 (LC :55).',
        'Both papers read the channels near 1 as gauge-invariant and those near 0 as symmetry-breaking, and call the interface a symmetry filter (SF :54, LC :59).',
        'LC states that BBN abundances and the dark matter density differ in κ by 0.96 (LC :98), and FD repeats the figure (FD :46), where 0.96 is SF’s bin-5 P-smooth rate and not a channel κ.',
        'LC’s twelve-test comparison totals 21, 10, 14 and 20 of 24 for ΛCDM, CCC+TL, MOND and the programme (LC :79), and its abstract’s four observations excluding CCC+TL are not the four zero scores of its table, which put σ₈ where the abstract puts the α-variation constraint (LC :12, LC :90).',
        'LC states that no cosmological model meets all four SIDE conditions (LC :117).',
        'SF reads the Hubble tension as one formation unit (SF :131) and predicts a separation of 6–8 km/s/Mpc (SF :141), where the values it quotes differ by 5.68.']),
    ('## 3. The P-smooth census and the violations', [
        'SF calls a constant P-smooth when a rational approximation of it factors through a fifteen-prime set (SF :30), and LC takes the rates from the 439-constant census of Constance v13.0 (LC :32).',
        'SF reports exactly five violations among 439 constants (SF :82), clustered at the boundary with p ≈ 5.8 × 10⁻⁵ (SF :12, SF :91), while its own bins table sums to 279 constants with 14 not P-smooth.',
        'The table’s rates fit the line 1.047 − 0.0385 × distance with r = −0.660, as SF gives (SF :76), and DM reports the same −0.66 as a Spearman ρ (DM :37), which over the nine bins is −0.644.',
        'A Poisson count at mean 350 × 5/439 gives zero with probability 0.0186, SF’s 1.9 percent (SF :91).',
        'SF lists θ₁₃ mixing among the five violations (SF :96) while its neutrino table marks sin²θ₁₃ P-smooth, and argues from that table that symmetry content discriminates within one sector (SF :121).',
        'DM reports a contingency hierarchy at Spearman ρ = 1.00 without its data (DM :69).']),
    ('## 4. The T-seven topology and the registered search', [
        'TC proposes a seven-fold non-orientable topology with seven matched arc pairs (TC :12) and argues that the reflected polarization at each arc is a signature no orientable topology produces (TC :72).',
        'Its abstract counts three matched circles for a 3-torus and twelve for a dodecahedral space (TC :12), where its own table counts three pairs and six pairs.',
        'The observed quadrupole is 0.17 of its ΛCDM prediction and the combined deficit at l = 2 to 5 is 24 percent, both recomputed from TC’s table (TC :22, TC :27).',
        'TC states H₁ = ℤ ⊕ (ℤ/2)³ for its Klein surface without a construction (TC :49), and gives the Fano incidence eigenvalues as 3 once and −1 six times (TC :106, TC :199), which are the eigenvalues of the collinearity graph K₇, the incidence matrix’s other eigenvalues having modulus √2.',
        'The registered search ran once on Planck 2018 SMICA (TC :172), and its bank, t7_results.json at SIDE-t7-topology-cmb 575a802, carries the best θ_min 54.0° and a look-elsewhere p of 46/1001 ≈ 0.046, the Marginal band (TC :178).',
        'TC records the seven-distinct-scale discriminator as untested and underdetermined (TC :174), every construction it screens yielding at most three classes or one scale (TC :215), and reads the outcome as leaving the methodology unfalsified (TC :180).',
        'Its link to the dark sector, 77/4 as seven Fano elements times 11/4, is a hypothesis by its own word (TC :225).']),
    ('## 5. The (ℤ/2)³ embedding and the 77/4 ratio', [
        'QD gives the dark-to-baryon ratio as 19.28 from Planck 2018 and fits it by 77/4 at 0.17 percent and by 58/3 at 0.26 percent (QD :12), the recomputed distances 0.176 and 0.256 percent.',
        'Dark matter over baryons, 5.381, sits 0.89 percent from 16/3 and dark energy over baryons, 13.903, 0.70 percent from 14 (QD :30), and three weights of 16/9 and three of 14/3 give those fractions (QD :83).',
        'QD reads the 1/12 between the decompositions as the weight of the diagonal element (QD :35) and the flatness deviation as Ω_b/12 ≈ 0.0041 (QD :149), as FD writes 1/243 (FD :108).',
        'It places the (3, 3, 1) partition under the parabolic stabilizer of the diagonal (QD :12) and names that stabilizer S₃ (QD :125), where in GL(3, 𝔽₂) the stabilizer of (1, 1, 1) has order 24 and one orbit of six on the other non-zero vectors, and DM carries the same placement (DM :107).',
        'QD identifies the seven non-identity elements with the square classes generated by −1, 2 and 3 (QD :43), and states that the weights 16/9 and 14/3 are not free parameters (QD :177).',
        'QD keeps the equation-of-state assignment open (QD :139) and names its falsifiers, the ratio leaving 19.25 by more than 1σ among them (QD :197).']),
    ('## 6. Formation distance across the cluster', [
        'DM states that the dark sector is the formation distance of the interface (DM :12), and DM and FD read 81 = 3⁴ from the tuple (2, 3, 2, 0) as four visible parts and 77 dark (DM :91, FD :16).',
        'FD gives Ω_b = 4/81 at 0.13σ from Planck (FD :22) and places 16/3 at 0.45σ and 14 at 0.41σ (FD :145), each recomputed, while the five combined datasets behind its 0.03σ are not named (FD :22).',
        'FD reads Planck’s Ω_K as consistent with both decompositions (FD :112), Decomposition B lying 1.8σ from it.',
        'FD writes Δμ = 77/4 for the cosmos (FD :128), a ratio where its own definition is a difference of counts, and reads 11 as the first prime not reached from 2 and 3 (FD :77), where 5 and 7 come first.',
        'FD’s threshold clause, appended under (R38), reads the condition w = −1 by stated sigmas (FD :161).']),
    ('## 7. The alignment constant α_T', [
        'TH reports α_T = 0.918 ± 0.018 over fourteen I∩D∩S theories (TH :18, TH :20), and its per-domain table gives a count-weighted mean of 0.922.',
        'It totals 375 theories (TH :65) where its domain counts sum to 348, and states α_T the same across fifteen domains (TH :20) while four of them carry no I∩D∩S theory.',
        'TH reports χ² = 2.1 on 10 degrees of freedom with p = 0.995 (TH :128) and a bootstrap interval [0.906, 0.930] (TH :130), and notes α_T within 0.0013 of 11/12 (TH :216).',
        'It reads 12 as the Standard Model fermions per generation (TH :218), where a generation carries two quark flavours in three colours and two leptons.',
        'TH states its findings reproducible (TH :300) while its table of theories is available on request, and its retrocheck finds three falsified theories each failing independence (TH :208).']),
    ('## 8. The Steane κ simulators', [
        'QI builds the Steane code from the [7, 4, 3] Hamming code, asserting sixteen codewords (QI :59) and taking the even-weight ones as the support of |0_L⟩ (QI :61), both of which the claim bank recounts.',
        'It defines κ at the syndrome interface as one minus the within-class variance over the total (QI :187), and measures logical Z as the parity of all seven qubits (QI :167).',
        'QI states that T gates anticommute with the X-type stabilizers (QI :280), where T X T† = (X + Y)/√2, and lists a Toffoli it does not define (QI :7).',
        'QV states that T on all seven qubits is a logical T preserving the code space (QV :17, QV :78), where applied to |0_L⟩ it leaves norm 0.750 in the code space, and prints its run’s value at n_T = 7 beside the word Confirmed whatever the value is (QV :81).',
        'QI expects κ near 0 at T-count 0 and rising monotonically with T-count (QI :358, QI :366), and no bank holds a run of either simulator, so each claim stands at statement grade (QV :66).']),
    ('## 9. The kernel legs the papers name', [
        'TC names the pipeline SIDE-t7-topology-cmb v0.3 = 8eb0d5a (TC :172), whose kernel file enters the homology’s ranks as numerals (TC :49).',
        'LC and QD name SIDE-local-cosmic-interface 7a62ced and SIDE-quaternionic-dark-sector e860142 as kernel legs (LC :163, QD :236), each defining the paper’s values and deciding their arithmetic, and no paper names a declaration at a pin.']),
    ('## 10. The routes the papers offer', [
        'DM and FD state that the SIDE Exclusion Principle settles RH, no mechanism class producing off-line zeros once the system is sealed (DM :147, FD :179), and FD restates the zeros as confined to the critical line (FD :187).',
        'TH states that the Lean kernel for RH compiles the architecture of the argument, the instantiation left to Lean’s riemannZeta (TH :176).',
        'SF and LC read Conservation of Spectra as extending to cosmology, the product formula s-dark at the scale of ζ (SF :153, LC :123).']),
    ('## 11. What the papers leave open', [
        'SF states that it does not claim to know what dark matter is (SF :161), and QD keeps the identification of its 1/12 with ζ(−1) open (QD :153).',
        'TH asks for at least thirty I∩D∩S theories to decide the 11/12 question (TH :232).',
        'QD’s version note records an editorial pass through a tool of a private library, carried here by pointer alone (QD :228).']),
]
TRACE_RE = re.compile(r'\b(SF|LC|TC|QD|DM|FD|TH|QI|QV) :(\d+)')


def _tier():
    cert = [c for c in K.C if c[5] == 'kernel-verified']
    lb = [c for c in cert if K.LOAD.get(c[0], (False,))[0]]
    return ('KC' if lb else 'C'), len(cert), [c[0] for c in lb]


def _tier_line(tier, cert_rows):
    return ('**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): TIER %s** — *declared 2026-10-04 (b616), under '
            '`(R226)`(3): the tier the rows earn, read under the load-bearing clause (OPEN_TRAILS :12699) after the rows were graded -- %d rows '
            'read kernel-verified, so none is load-bearing for the thesis the head states: no paper names a declaration at a pin, and the three '
            'kernels the papers name without one -- SIDE-t7-topology-cmb v0.3 = 8eb0d5a, SIDE-local-cosmic-interface 7a62ced and '
            'SIDE-quaternionic-dark-sector e860142, each resolving in its clone and at its remote -- enter the papers’ values as definitions and '
            'decide arithmetic over them, so read as terminals they would certify definitions and arithmetic over the papers’ own tuples; each row '
            'is cited at its stated grade, the Correspondence in the back matter (`(R221)`(3)).*' % (tier, cert_rows))


def _front(tier, cert_rows):
    P = K.paper_lines()
    keys = ['| key | file | REGISTRY row | its head | its status in REGISTRY |', '|:--|:--|:--|:--|:--|']
    R = K.lines_of(K.show('REGISTRY.md'))
    for k, (path, rid, rline) in K.PAPERS.items():
        st = [x.strip() for x in R[rline - 1].strip().strip('|').split('|')]
        head = P[k][0].lstrip('# ').strip() if k not in K.SIMULATORS else P[k][1].strip()
        keys.append('| %s | `%s` | %s (REGISTRY :%d) | “%s” | %s |' % (k, path, rid, rline, _cell(head), _cell(st[5]).replace('*', '')[:40]))
    return [TITLE, '', _tier_line(tier, cert_rows), '', HEADLINE, '', VERSION, '',
            '**PURPOSE:** *the keystone the census found wanting for cluster 2G (THE_KEYSTONE_CENSUS v0.3, its row R17 and §2): the seven papers and '
            'two simulators REGISTRY files as p2-d1 to p2-d9, each claim listed with the grade its own text supports; for a reader who meets those '
            'files and needs what each states and what backs it.*', '',
            '**The papers and simulators, by the key the body cites:**', ''] + keys + ['',
            '**Two notes on reading.** QUATERNIONIC (QD) names TECHNE once; this document carries that citation by pointer alone and no sentence of '
            'it. The grades are `(R19)`’s vocabulary as `(R220)`(5) lists it; a row reads kernel-verified only where its paper names the terminal at '
            'a pin, and a simulator’s row reads computationally-verified only where a bank holds its run; cite the synthesis for orientation and '
            'each row at its stated grade.', '']


def _corr(CC):
    S = ['## Correspondence', '',
         '*Every claim of the seven papers and two simulators this document carries, with the grade the paper’s own text supports. A route is '
         'read through the sieve’s five tests in order; the routes and their instruments are below.*', '',
         '| claim | paper :line | the claim | grade | what backs it | route |', '|:--|:--|:--|:--|:--|:--|']
    for c in CC:
        cid, pk, n, _needle, text, grade, _support, reason, route = c
        rcell = ('%s: %s%s' % (route[0], route[1], '' if route[2] is None else ', test %d' % route[2])) if route else '—'
        S.append('| %s | %s :%d | %s | %s | %s | %s |' % (cid, pk, n, _cell(text), grade, _cell(reason), rcell))
    return S + ['']


def _back(CC, tier):
    sieve = K.sieve_rows()
    B = [BM_TAG, '', '## Back matter of v0.1 — written 2026-10-04 by b616 under the author’s ruling `(R226)`(3), by the synthesis form of `(R220)`(5), '
         '`(R221)`(3) and `(R225)`(2)', '',
         '### The grading rule, confirmed by `(R222)`(1)', '',
         '- **kernel-verified** only where the paper names a terminal or its file at a pin and the statement read at that pin carries the claim; '
         '**theorem-supported** only where the paper names a theorem of the literature for it; **computationally-verified** only where the paper reports '
         'a computation; **argument-supported** where the paper’s text argues the claim; **synthesis-suggested** where it reads a pattern across results; '
         '**statement-grade** where it states without argument. No row is graded above what its paper’s own text names as its backing.',
         '- A simulator’s row reads computationally-verified only where a bank holds its run (`(R226)`(3)); where none does, its row is graded by what '
         'its text states.',
         '- A pin resolves when its commit is in the clone and at the remote (`(R223)`(1)).',
         '- A route is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the sieve’s five tests in order, '
         'DARK at the first it fails, with that test’s instrument at its pin.',
         '- The tier reads KC when at least one kernel-verified row is load-bearing for the thesis the head states, and C otherwise (OPEN_TRAILS '
         ':12699).', '']
    if tier != 'KC':
        B += _corr(CC)
    B += ['### The routes through the five tests', '',
          '| route | claims | verdict | test, instrument at pin | reason | the sieve’s row |', '|:--|:--|:--|:--|:--|:--|']
    for r, cs in sorted(_route_rows().items()):
        _rid, v, t, inst, why, row = cs[0][8]
        B.append('| %s | %s | %s | %s | %s | %s |' % (r, ', '.join(x[0] for x in cs), v, ('%d (%s)' % (t, inst)) if t else '—', _cell(why),
                                                   ('%s, %s' % (row, ' '.join(sieve.get(row, ('?', ''))).replace(' —', ''))) if row else 'none'))
    B += ['', '- The cluster’s cosmology claims are offered toward no target the sieve reads: its row MC-01 reads the constants and the empirical '
          'layer, NOT A ROUTE.', '']
    B += ['### The pins the papers name, none with a terminal', '', '| as cited | its resolution | where the paper names it | what stands there |',
          '|:--|:--|:--|:--|']
    nts = {}
    for k, v in K.NTREADS.items():
        nts.setdefault(v[0], v)
    for k in K.PINS_NT:
        st = K.pin_state(k)
        what = ('`%s` :%d, %s' % (nts[k][1], nts[k][2], nts[k][4])) if k in nts else (
            'the tag does not exist as cited; the clone carries v0.1.0, v0.2, v0.2.1 and v0.3' if not st[3] else 'a reference, no terminal named')
        B.append('| %s %s | %s | %s | %s |' % (st[1], st[2], ('commit `%s`, %s' % (st[3], st[4] or 'NOT AT THE REMOTE')) if st[3] else 'does not resolve as cited',
                                             K.PINS_NT[k][3], _cell(what)))
    tb = jl('b616_claims.json')['t7_bank']
    B += ['', '### The registered run’s bank', '',
          '- `t7_results.json` at SIDE-t7-topology-cmb %s, on the remote main %s: the best θ_min %s°, the look-elsewhere p %.5f (46 of 1001), the seed %s, '
          '%s rotations, a scan of %s points, the decision %s; its working copy’s md5 `%s`, the paper’s `%s…`, the committed blob’s md5 differing by '
          'line endings alone (core.autocrlf).' % (tb['rev'], tb['remote_main'], tb['theta'], tb['p'], tb['seed'], tb['n_mc'], tb['scan'], tb['decision'],
                                                    tb['md5_wc'], tb['md5_paper'][:8]), '',
          '### The simulators’ runs', '',
          '- No bank holds a run of `qec_kappa_infrastructure.py` or `qec_kappa_v2.py`: the search reads PLACE-papers’ tracked and untracked text and '
          'relay’s tracked text for the runs’ printed headers, and the download folders by file name, finding copies of the two scripts and no '
          'output. The companion paper `%s` reports a table of κ against T-count (:15-:26), a report and not a bank.' % QEC, '']
    B += ['### The TECHNE citation', '',
          '- QD :228 names a tool of a private library; this document carries it by pointer alone: TECHNE-Core, the sha256 of its tracked-file manifest, '
          '`%s`. No sentence of its body is carried.' % K.techne_pointer(), '']
    B += ['### The arithmetic the rows cite, recomputed in the claim bank', '', '| what | computed | the paper | agrees |', '|:--|:--|:--|:--|']
    for x in jl('b616_claims.json')['arith']:
        B.append('| %s | %s | %s | %s |' % (_cell(x['label']), _cell(x['value'][:420]), _cell(x['paper']), 'yes' if x['agrees'] else 'no'))
    B += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
          '| this document, v0.1 | `%s` | written at b616 |' % DOC]
    for k, (path, rid, _rl_) in K.PAPERS.items():
        B.append('| %s, %s | `%s` | read, unedited |' % (k, rid, path))
    B += ['| the census row naming this cluster | `%s`, row R17 | unedited; updated at its next version |' % CEN3,
          '| the claim bank | relay `data/%s` | banked before this document |' % BANK, '',
          '### Version history', '',
          '- **v0.1, 2026-10-04 (b616, `(R226)`(3))**: the synthesis of p2-d1 to p2-d9, %d claims graded, the routes read through the five tests, '
          'the tier read under the load-bearing clause; the sequence’s last.' % len(CC), '']
    return B


def doc(*a):
    """### PLACE-papers phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md (created) and data/b616_doc.json; `dry`:
    ### the scratchpad. Needs the claim bank first."""
    if not os.path.exists(_p('b616_claims.json')):
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
    dest = os.path.join(SP, 'b616_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))
    if not DRY and os.path.exists(dest):
        sys.exit('### THE DOCUMENT EXISTS -- NOTHING WRITTEN')
    open(dest + '.tmp', 'wb').write(b)
    os.replace(dest + '.tmp', dest)
    corr_at = lines.index('## Correspondence') + 1
    put_json('b616_doc.json', dict(at=utc(), path=DOC, sha256=sha(b), bytes=len(b), lines=len(lines), tier=tier, cert_rows=ncert, load_bearing=lb,
                                   corr_at=corr_at, body_at=body_at, body_end=body_end, bm=lines.index(BM_TAG) + 1, title=TITLE, rows=len(CC)))
    print('  %s : %d lines, %d bytes, sha256 %s ; tier %s (%d kernel-verified rows, load-bearing %s) ; Correspondence at :%d ; body :%d-:%d' % (
        ('DRY ' + dest) if DRY else DOC, len(lines), len(b), sha(b)[:16], tier, ncert, lb or 'none', corr_at, body_at, body_end))


def _docpath():
    return os.path.join(SP, 'b616_doc_dry.md') if DRY else os.path.join(PP, *DOC.split('/'))


def doc_lines():
    return K.lines_of(io.open(_docpath(), encoding='utf-8').read().replace(chr(13), ''))


def doc_scan(*a):
    t = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', _docpath()], capture_output=True, text=True,
                       encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout
    put_txt('b616_doc_termscan.txt', t.rstrip(NL).split(NL))


def h50a(ls, J):
    trace = set((p, n) for p, n in jl('b616_claims.json')['trace'])
    body = [l for l in ls[J['body_at'] - 1:J['body_end']] if l.strip() and not l.startswith('#')]
    sents = [s for l in body for s in _segs(l)]
    bad = []
    for s in sents:
        tr = [(m.group(1), int(m.group(2))) for m in TRACE_RE.finditer(s)]
        if not tr or any(x not in trace for x in tr):
            bad.append(s[:120])
    return not bad, len(sents), bad


def corr_rows(ls):
    """### the Correspondence's claim rows alone: from its heading to the next heading"""
    if '## Correspondence' not in ls:
        return []
    i = ls.index('## Correspondence') + 1
    j = next((k for k in range(i, len(ls)) if ls[k].startswith('#')), len(ls))
    return [l for l in ls[i:j] if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)]


def tier_check(tier_line):
    """### C with no certifying row, none load-bearing and the clause cited; KC never (no row reads kernel-verified)"""
    kv = [c for c in K.C if c[5] == 'kernel-verified']
    return not kv and 'TIER C**' in tier_line and 'none is load-bearing' in tier_line and 'load-bearing clause (OPEN_TRAILS :12699)' in tier_line \
        and '0 rows read kernel-verified' in tier_line


def doc_bank(*a):
    """### data/b616_doc_bank.txt and data/b616_h50.json: the title's property words, H50a-H50d, the scanner, the ceiling, the no-disclosure arm."""
    J = jl('b616_doc.json')
    ls = doc_lines()
    if sha((NL.join(ls) + NL).encode('utf-8')) != J['sha256']:
        sys.exit('### THE DOCUMENT ON DISK IS NOT THE BANKED BYTES -- NOTHING WRITTEN')
    scan = rd('b616_doc_termscan.txt')
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None
    title_props = PROPERTY_WORDS.findall(TITLE)
    a_ok, n_sent, a_bad = h50a(ls, J)
    rows = corr_rows(ls)
    over = [c[0] for c in K.C if not K.grade_ok(c)]
    h50b = 'HOLDS' if len(rows) >= 20 and not over and len(rows) == len(K.C) else 'REFUTED'
    hits, sizes = nd_hits(NL.join(ls))
    tier_line = next((l for l in ls[:6] if l.startswith('**DOCUMENT CLASS')), '')
    tier_ok = tier_check(tier_line)
    h50d = 'HOLDS' if not any(hits.values()) and all(v > 0 for v in sizes.values()) else 'REFUTED'
    pointer_ok = K.techne_pointer() in NL.join(ls)
    placed = (J['corr_at'] < J['body_at']) if J['tier'] == 'KC' else (J['corr_at'] > J['body_end'])
    ceiling = [(i + 1, m.group(0)) for i, l in enumerate(ls[:J['bm'] - 1]) for m in CEILING.finditer(l)]
    CJ = jl('b616_claims.json')
    L = ['b616 -- COMPONENT 3: THE DOCUMENT`S BANK -- `%s`, sha256 %s, %d lines, %d bytes' % (DOC, J['sha256'], J['lines'], J['bytes']),
         '### THE TITLE: %s' % TITLE[2:], '### the title`s property words: %s' % (title_props or 'NONE'),
         '### THE TIER: %s -- %d rows read kernel-verified, load-bearing %s; the line holds the clause: %s; the line: %s' % (
             J['tier'], J['cert_rows'], J['load_bearing'] or 'none', tier_ok, tier_line[:900]),
         '### THE PLACEMENT, (R221)(3): the Correspondence at :%d, the body at :%d-:%d -- %s' % (J['corr_at'], J['body_at'], J['body_end'],
                                                                                          'in the back matter, after the body (C)' if placed and J['tier'] == 'C'
                                                                                          else 'after the front matter (KC)' if placed else '### MISPLACED'),
         '### THE HEAD LINE: %s ; THE VERSION LINE: %s ; THE TECHNE POINTER: %s' % (HEADLINE in ls[:12], VERSION in ls[:12], pointer_ok),
         '### THE SCANNER: %s, live %s ; the ceiling pattern above the back matter: %s' % ('CLEAN' if clean else 'NOT CLEAN',
                                                                                         (re.search(r'live uses\s*: (\d+)', scan) or [None, '?'])[1], ceiling or 'none'),
         '### THE NO-DISCLOSURE ARM over this document, the needles read locally and never printed: the method document %d needles, %d hits ; the '
         'tree %d, %d ; every module document %d, %d' % (sizes['method'], hits['method'], sizes['tree'], hits['tree'], sizes['modules'], hits['modules']),
         '### H50a`s trace check: %d body sentences; without a trace, or with a trace the bank does not carry: %s' % (n_sent, a_bad or 'NONE'),
         '', '### ### **H50a %s** -- every body sentence traces by path and line to a paper`s line the bank carries' % ('HOLDS' if a_ok else 'REFUTED'),
         '### ### **H50b %s** -- the Correspondence carries %d rows (at least twenty), none graded above its paper`s named backing (%s)' % (h50b, len(rows), over or 'none'),
         '### ### **H50c %s** -- %s (relay data/%s, Part H; the walk by file name, relay data/b616_sim_walk.txt: %d candidate output files)' % (
             CJ['h50c'], CJ['h50c_why'], BANK, jl('b616_sim_walk.json')['candidates']),
         '### ### **H50d %s** -- the no-disclosure arm reads %d hits over %d + %d + %d needles' % (h50d, sum(hits.values()), sizes['method'], sizes['tree'], sizes['modules']),
         '### ### **THE DOCUMENT LANDS.**' if a_ok and clean and not ceiling and not title_props and tier_ok and placed and pointer_ok and h50d == 'HOLDS'
         else '### ### **HELD.**']
    put_txt('b616_doc_bank.txt', L)
    put_json('b616_h50.json', dict(H50a='HOLDS' if a_ok else 'REFUTED', H50b=h50b, H50c=CJ['h50c'], H50d=h50d, sentences=n_sent, untraced=a_bad, rows=len(rows),
                                   over=over, clean=clean, ceiling=len(ceiling), title_props=title_props, nd_hits=hits, nd_sizes=sizes, placed=placed,
                                   tier=J['tier'], tier_ok=tier_ok, pointer=pointer_ok, routes=CJ['routes']))
    for l in L[-7:]:
        print(l)


# ================================================================================ COMPONENT 4: THE SEQUENCE'S CLOSE
# ### each listed route's conclusion, read by the seat from the claims it cites (strikeable): two rows share a conclusion when they argue the
# ### same step toward the same target
CONCL = {
    ('1.2', 'R3'): ('K1', 'the paths to σ = 1/2 identify the line through one shared involution and carry no placement'),
    ('1.5E', 'R2'): ('K1', None), ('2B', 'R2'): ('K1', None),
    ('1.2', 'R2'): ('K2', 'an off-line zero is a location-type property that neither the symmetry nor the multiplicative structure produces'),
    ('1.2', 'R4'): ('K3', 'localizing the explicit formula at a zero equates its multiplicity with a prime-side value, computed 1 at finitely many zeros'),
    ('1.2', 'R5'): ('K4', 'along the curve Re ξ = 0 from a simple zero |Im ξ| increases, so no off-line zero lies on it'),
    ('1.2', 'R6'): ('K5', 'an off-line zero is a coincidence of two real conditions in one real parameter, which a determined system generically misses'),
    ('1.5E', 'R5'): ('K5', None),
    ('1.2', 'R7'): ('K6', 'the involution s ↦ 1 − s fixes σ = 1/2, and its monodromy concentrated there places the zeros'),
    ('1.5E', 'R4'): ('K6', None),
    ('1.5E', 'R6'): ('K7', 'analytic, topological and structural lines of evidence converge on every zero on the line'),
    ('1.5E', 'R7'): ('K8', 'an inventory of the known mechanisms finds none producing an off-line zero'),
    ('1.5E', 'R8'): ('K9', 'the Frobenius property of {2, 3} that fixes the constants also places the zeros'),
    ('1.5E', 'R9'): ('K10', 'a statistic over thirty ordinates, |ζ′(ρ)|/√γ, read as a barrier growing like √γ'),
}
ROUTE_HEAD = '### The routes through the five tests'


def _syn_read(key):
    ls = K.lines_of(g(PP, 'show', 'HEAD:' + SYN[key]))
    title = ls[0][2:] if ls else ''
    ver = next((l for l in ls[:12] if re.match(r'^\*v0\.\d', l)), '')
    tier = 'KC' if len(ls) > 2 and 'TIER KC**' in ls[2] else 'C' if len(ls) > 2 and 'TIER C**' in ls[2] else '?'
    rows = corr_rows(ls)
    ri = ls.index(ROUTE_HEAD) if ROUTE_HEAD in ls else -1
    routes = []
    if ri >= 0:
        for l in ls[ri + 1:]:
            if l.startswith('#'):
                break
            m = re.match(r'^\| (R\d+) \| ', l)
            if m:
                c = [x.strip() for x in l.strip().strip('|').split(' | ')]
                routes.append(dict(route=c[0], claims=c[1], verdict=c[2], test=c[3], reason=c[4], sieve=c[5], line=ls.index(l) + 1))
    return dict(path=SYN[key], title=title, version=ver[1:5] if ver else '?', tier=tier, claims=len(rows), routes=routes)


def routes_sieve(*a):
    """### data/b616_routes_for_sieve.txt and its json: the six syntheses in one table; every route they list for the sieve (a route row whose
    ### sieve column names no row), gathered and deduplicated by conclusion with each source synthesis named -- the work-list for b617."""
    S = {k: _syn_read(k) for k in SYN}
    L = ['b616 -- COMPONENT 4: THE SEQUENCE`S CLOSE, (R226)(3)-(4), banked %s at PLACE-papers %s' % (utc(), g(PP, 'rev-parse', '--short=7', 'HEAD').strip()), '',
         '### THE SIX SYNTHESES:', '| cluster | path | version | tier | claims | route rows | listed for the sieve | matched to a row |', '|:--|:--|:--|:--|:--|:--|:--|:--|']
    listed, matched = [], []
    for k, s in S.items():
        li = [r for r in s['routes'] if r['sieve'].startswith('none')]
        ma = [r for r in s['routes'] if not r['sieve'].startswith('none')]
        listed += [(k, r) for r in li]
        matched += [(k, r) for r in ma]
        L.append('| %s | `%s` | %s | %s | %d | %d | %s | %s |' % (k, s['path'], s['version'], s['tier'], s['claims'], len(s['routes']),
                                                                ', '.join(r['route'] for r in li) or '—', ', '.join('%s = %s' % (r['route'], r['sieve'].split(',')[0]) for r in ma) or '—'))
    miss = [(k, r['route']) for k, r in listed if (k, r['route']) not in CONCL]
    extra = [x for x in CONCL if x not in [(k, r['route']) for k, r in listed]]
    if miss or extra:
        sys.exit('### THE CONCLUSION READING DOES NOT COVER THE LISTED ROUTES (missing %s, extra %s) -- NOTHING WRITTEN' % (miss, extra))
    groups = {}
    for k, r in listed:
        groups.setdefault(CONCL[(k, r['route'])][0], []).append((k, r))
    gtext = {v[0]: v[1] for v in CONCL.values() if v[1]}
    order = sorted(groups, key=lambda x: int(x[1:]))
    L += ['', '### THE ROUTES LISTED FOR THE SIEVE: %d rows in %d syntheses, gathered into %d conclusions (%d routes, %d NOT A ROUTE):' % (
        len(listed), len(set(k for k, _r in listed)), len(order), sum(1 for x in order if groups[x][0][1]['verdict'] != 'NOT A ROUTE'),
        sum(1 for x in order if groups[x][0][1]['verdict'] == 'NOT A ROUTE'))]
    out = []
    for x in order:
        rows = groups[x]
        verdicts = sorted(set(('%s %s' % (r['verdict'], r['test'].split(' ')[0] if r['test'] != '—' else '')).strip() for _k, r in rows))
        L.append('  %s -- %s' % (x, gtext[x]))
        L.append('       verdicts %s ; from %s' % (verdicts, '; '.join('%s %s (claims %s; `%s` :%d)' % (k, r['route'], r['claims'], SYN[k], r['line']) for k, r in rows)))
        out.append(dict(key=x, conclusion=gtext[x], verdicts=verdicts, sources=[dict(cluster=k, route=r['route'], claims=r['claims'], line=r['line'],
                                                                                     verdict=r['verdict'], test=r['test']) for k, r in rows]))
    L += ['', '### THE ROUTES ALREADY MATCHED TO A SIEVE ROW (carried by the sieve, not the work-list): %s' % '; '.join(
        '%s %s -> %s' % (k, r['route'], r['sieve'].split(',')[0]) for k, r in matched)]
    L += ['', '### ### **THE WORK-LIST FOR b617: %d conclusions, %d of them routes, gathered from %d listed rows.**' % (
        len(order), sum(1 for o in out if not o['verdicts'][0].startswith('NOT A ROUTE')), len(listed))]
    put_txt('b616_routes_for_sieve.txt', L)
    put_json('b616_routes_for_sieve.json', dict(at=utc(), syntheses={k: dict((kk, vv) for kk, vv in s.items() if kk != 'routes') for k, s in S.items()},
                                                route_rows={k: len(s['routes']) for k, s in S.items()}, listed=len(listed), conclusions=out,
                                                matched=[dict(cluster=k, route=r['route'], sieve=r['sieve'].split(',')[0]) for k, r in matched]))
    for l in L[3:11] + L[-1:]:
        print(l[:260])


# ================================================================================ COMPONENT 5: THE PAGES
def page(k, *a):
    """### ONE page per call in the foreground, re-emitted from its banked probe; writes the page only when it changed."""
    import chain_page as CP
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    pdir = os.path.join(SP, '_b616_%s' % k)
    fm = R2.free_mb()
    print('  free memory before the call: %d MB (hold %d)' % (fm, CP.HOLD_MB))
    if 0 <= fm < CP.HOLD_MB:
        sys.exit('### BELOW THE HOLD -- NOT STARTED')
    t0 = time.time()
    rc, pg, meta, log = CP.build(os.path.join(D, NODES[k]), pdir, os.path.join(D, PROBE[k]))
    secs = int(time.time() - t0)
    if rc:
        put_json('b616_page_%s.json' % k, dict(rc=rc, log=log, at=utc(), free_mb_before=fm, seconds=secs))
        sys.exit('### %s RE-EMIT FAILED, exit %d' % (k, rc))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = R2.cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(R2.cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    put_json('b616_page_%s.json' % k, dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl,
                                           at=utc(), free_mb_before=fm, seconds=secs, pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip()))
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; %d s' % (k, rc, len(b), changed, secs))
    for x in dl[:40]:
        print('    ' + x[:240])


def page_arms(tag, *a):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    L = ['b616 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b616_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = TC.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d' % (TC.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc']))
    L.append('### ### **%s PASSING : %d of 2.**' % (TC.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b616_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ COMPONENT 6: THE SCORES AND THE RECORD
HKEYS = ('H50a', 'H50b', 'H50c', 'H50d')
SCORE_KEYS = HKEYS + ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
CURRENTS = tuple(v[0] for v in K.PAPERS.values()) + tuple(v for k, v in SYN.items() if k != '2G') + (
    CEN3, 'REGISTRY.md', 'SPIRAL_MAP_v0_7.md', 'SPIRAL_MAP.md', 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', K.SIEVE, QEC, 'ERRATA.md')
S4_EXPECT = {'zeta': False, 'chi': False}   # ### the seat's expectation, registered on the face


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def scores(*a):
    H, CJ, J = jl('b616_h50.json'), jl('b616_claims.json'), jl('b616_doc.json')
    RS = jl('b616_routes_for_sieve.json')
    Z, X = jl('b616_page_zeta.json'), jl('b616_page_chi.json')
    face = jl('b616_kernels_face.json')['kernels']
    now = {k: list(v) for k, v in kern_state().items()}
    kern_same = now == face and all(now[k][0] == v for k, v in KERN_PIN.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip())
                   | set(x[3:] for x in g(PP, 'status', '--porcelain', '--untracked-files=all', '--', 'phase2', 'phase1.5', 'day1', 'heritage').split(NL)
                         if x.startswith('?? ')))
    want_pp = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', DOC] + [p['page'] for p in (Z, X) if p.get('changed')])
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + p).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, p)).strip()
                   and not g(PP, 'status', '--porcelain', '--', p).strip() for p in CURRENTS)
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b616_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b615_closing_push_out.txt'))
    rc = K.resolve_claims()
    nt = K.resolve_nt()
    pins = {k: K.pin_state(k) for k in K.PINS_NT}
    tb = K.t7_bank()
    arms2 = rd('b616_page_arms_c2.txt')
    sims = [c for c in K.C if c[1] in K.SIMULATORS]
    below = [c[0] for c in sims if c[5] != 'computationally-verified']
    nconc = len(RS['conclusions'])
    nroutes = sum(1 for o in RS['conclusions'] if not o['verdicts'][0].startswith('NOT A ROUTE'))
    S = {
        'H50a': (H['H50a'], 'body sentences %d, untraced %s' % (H['sentences'], H['untraced'] or 'none')),
        'H50b': (H['H50b'], 'Correspondence rows %d (the floor 20), graded above the paper`s backing %s' % (H['rows'], H['over'] or 'none')),
        'H50c': (H['H50c'], CJ['h50c_why']),
        'H50d': (H['H50d'], 'the no-disclosure arm over the document: %s hits over %s needles' % (H['nd_hits'], H['nd_sizes'])),
        'N1': ('HELD' if CJ['n'] >= 80 else 'REFUTED', '%d claims from the seven papers and two simulators (the floor 80)' % CJ['n']),
        'N2': ('HELD' if 2 * len(below) >= len(sims) and not CJ['sim_banks'] else 'REFUTED',
               '%d of %d simulator claims graded below computationally-verified, the bank search finding %s' % (len(below), len(sims), CJ['sim_banks'] or 'no bank')),
        'N3': ('HELD' if nconc >= 8 else 'REFUTED', '%d conclusions after deduplication (%d routes and %d NOT A ROUTE) from %d listed rows (relay '
                                                     'data/b616_routes_for_sieve.txt)' % (nconc, nroutes, nconc - nroutes, RS['listed'])),
        'N4': ('HELD' if H['H50a'] == 'HOLDS' and H['clean'] and H['H50d'] == 'HOLDS' else 'REFUTED',
               'body sentences traced %s, the scanner %s, the no-disclosure arm %s hits' % (H['H50a'] == 'HOLDS', 'CLEAN' if H['clean'] else 'NOT CLEAN',
                                                                                         sum(H['nd_hits'].values()))),
        'N5': ('HELD' if kern_same and cur_same and pp_ch == want_pp and relay_beyond == [] else 'REFUTED',
               'nothing deposits; kernels unmoved since the face %s; the papers, simulators, five syntheses, census, REGISTRY, SPIRAL_MAP, taxonomy, '
               'sieve, companion paper and ERRATA unedited %s; PLACE-papers %s (wanted %s); relay beyond the act`s banks, tools and the table %s' % (
                   kern_same, cur_same, pp_ch, want_pp, relay_beyond)),
        'S1': ('HELD' if all(ok for _i, ok, _l in rc) else 'REFUTED', 'claim needles on their lines at %s: %d of %d' % (PRE_PP, sum(ok for _i, ok, _l in rc), len(rc))),
        'S2': ('HELD' if sum(1 for p in pins.values() if p[3] and p[4]) == 3 and not pins['t7v01'][3] and all(ok for _k, ok, _l in nt)
               and tb.get('wc_matches') and tb.get('on_remote') else 'REFUTED',
               'the pins named resolving %d of %d (v0.1 does not resolve as cited) ; the reads there standing %d of %d ; the run`s bank: working-copy '
               'md5 as the paper %s, its commit on the remote main %s' % (sum(1 for p in pins.values() if p[3] and p[4]), len(pins), sum(ok for _k, ok, _l in nt),
                                                                         len(nt), tb.get('wc_matches'), tb.get('on_remote'))),
        'S3': ('HELD' if nconc == 10 and nroutes == 9 and RS['listed'] == 14 else 'REFUTED',
               'the six syntheses` listed rows %d gathered into %d conclusions, %d of them routes' % (RS['listed'], nconc, nroutes)),
        'S4': ('HELD' if Z.get('changed') is S4_EXPECT['zeta'] and X.get('changed') is S4_EXPECT['chi'] else 'REFUTED',
               'the ζ page changed %s (expected %s) ; the χ page changed %s (expected %s)' % (Z.get('changed'), S4_EXPECT['zeta'], X.get('changed'), S4_EXPECT['chi'])),
        'S5': ('HELD' if 'PAGE ARMS PASSING : 2 of 2' in arms2 and 'PASSING : 2 of 2.**' in arms2.split('PAGE ARMS PASSING')[-1] else 'REFUTED',
               'after the pages: %s' % [l.strip() for l in arms2.split(NL) if 'PASSING' in l]),
    }
    put_json('b616_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k, S[k][0], str(S[k][1])[:260]))


def _title():
    J, CJ, RS = jl('b616_doc.json'), jl('b616_claims.json'), jl('b616_routes_for_sieve.json')
    nr = len(CJ['routes'])
    return ('## The 2G synthesis: the local–cosmic interface and the dark sector at v0.1 from p2-d1 to p2-d9, seven papers and two simulators, %d '
            'claims graded, %s read, tier %s; the synthesis sequence closed at six documents, %d conclusions gathered for the sieve' % (
                J['rows'], 'one route' if nr == 1 else '%d routes' % nr, J['tier'], len(RS['conclusions'])))


TRAIL_HEAD = ('### b616 — lane three, act forty-three under (R226): the synthesis for 2G, the sequence’s last; the sequence closed and the '
              'consolidation entered')
FOR_AUTHOR = (
    '(1) the 2G papers’ findings, for their next editions: SYMMETRY_FILTER :62 and :82 count 439 constants and five violations where its bins '
    'table (:64-:74) sums to 279 constants with 14 not P-smooth, and :96 lists θ₁₃ among the violations where :112 marks sin²θ₁₃ P-smooth; :141 '
    'predicts a separation of 6–8 km/s/Mpc where the values it quotes at :127 differ by 5.68; DARK_DELTA_MU :37 and FORMATION_DISTANCE :139 call '
    'the −0.66 a Spearman ρ where it is SYMMETRY_FILTER’s Pearson r (Spearman over the bins −0.644); LOCAL_COSMIC :12 and :90 name α variation '
    'among the four observations excluding CCC+TL where its table’s fourth zero is σ₈, and :98 and FORMATION_DISTANCE :46 read 0.96 as a κ where '
    'it is a P-smooth rate; T7_CMB :106 and :199 give the Fano incidence eigenvalues as 3 and −1 six times, the eigenvalues of K₇, where the '
    'incidence matrix’s others have modulus √2, and :12 counts circles for one topology and pairs for the other; QUATERNIONIC :125, :12 and '
    'DARK_DELTA_MU :107 and FORMATION_DISTANCE :100 name the diagonal’s stabilizer S₃ or a parabolic with orbits (3, 3, 1), where in GL(3, 𝔽₂) it '
    'has order 24 and orbits (6, 1); FORMATION_DISTANCE :77 calls 11 the first prime not reached from 2 and 3, where 5 and 7 come first; '
    'THEORY_SPACE :65 totals 375 theories where its domain rows sum to 348, its count-weighted mean is 0.922 against the stated 0.918, :20 says '
    'all fifteen domains where :120 leaves four without a theory, and :218 gives twelve fermions per generation; qec_kappa_infrastructure.py :280 '
    'says T anticommutes with the X stabilizers, where T X T† = (X + Y)/√2, and lists a Toffoli it does not define (:7); qec_kappa_v2.py :17 and '
    ':78 read T on all seven qubits as a logical T, where it leaves the Steane code space (norm 0.750 kept); no bank holds a run of either '
    'simulator; (2) the seat’s readings, strikeable: the three kernels named without a declaration (SIDE-t7-topology-cmb v0.3, '
    'SIDE-local-cosmic-interface 7a62ced, SIDE-quaternionic-dark-sector e860142) read as pins with no terminal, certifying no row; the routes '
    'for the sieve read as the rows whose sieve column names no row, deduplicated by the step each argues (relay data/b616_routes_for_sieve.txt)')


def _finding_text():
    S, J, CJ, RS = jl('b616_scores.json'), jl('b616_doc.json'), jl('b616_claims.json'), jl('b616_routes_for_sieve.json')
    rl = _rl()
    dc = _pp_commit('b616 (R226)(3): ' + DOC)
    t = _title()
    gr = CJ['grades']
    syn = RS['syntheses']
    tab = '; '.join('%s %s %s, %d claims, %d route row%s' % (k, v['version'], v['tier'], v['claims'], RS['route_rows'][k],
                                                              '' if RS['route_rows'][k] == 1 else 's') for k, v in syn.items())
    e = ['', t, '',
         '*Filed at b616 on the author’s ruling `(R226)`. Banks: relay `data/b616_reads.txt`, `data/%s`, `data/b616_arith.txt`, `data/b616_doc_bank.txt`, '
         '`data/b616_routes_for_sieve.txt`, `data/b616_page_arms_c2.txt`. Nothing deposits.*' % BANK, '',
         '**The document** (`(R226)`(3)). PLACE-papers `%s` (commit %s), v0.1, in the cluster’s folder: the seven papers and two simulators REGISTRY '
         'files as p2-d1 to p2-d9 read whole at %s, %d claims each restated in one sentence and graded by its file’s own text -- kernel-verified %d, '
         'theorem-supported %d, argument-supported %d, computationally-verified %d, synthesis-suggested %d, statement-grade %d. Tier %s under the '
         'load-bearing clause: no paper names a declaration at a pin, so no row reads kernel-verified; the three kernels the papers name without one '
         'resolve and define the papers’ values. The registered T-seven run is computationally-verified on its bank at SIDE-t7-topology-cmb '
         '575a802; the simulators’ twelve claims stand at statement grade, no bank holding a run of either (H50c, its other side VACUOUS). '
         'QUATERNIONIC’s one TECHNE citation is carried by pointer alone, the no-disclosure arm at 0 hits.' % (
             DOC, dc, PRE_PP, CJ['n'], gr.get('kernel-verified', 0), gr.get('theorem-supported', 0), gr.get('argument-supported', 0),
             gr.get('computationally-verified', 0), gr.get('synthesis-suggested', 0), gr.get('statement-grade', 0), J['tier']), '',
         '**The routes** (the five tests). DARK_DELTA_MU’s and FORMATION_DISTANCE’s statement that the SIDE Exclusion Principle settles RH, and '
         'THEORY_SPACE’s kernel architecture, read as one route, DARK by test 2, matching the sieve’s RH-60; the cosmology claims are offered toward '
         'no target the sieve reads, its row MC-01.', '',
         '**The sequence closed** (`(R226)`(4)(i)). The six syntheses: %s. Every route they list for the sieve, %d rows, gathered at relay '
         'data/b616_routes_for_sieve.txt into %d conclusions -- the work-list for b617.' % (tab, RS['listed'], len(RS['conclusions'])), '',
         '**The record lines.** b615’s weight at FINDINGS :%d; the dated correction line beneath b614’s For-the-author line at OPEN_TRAILS :%d; the '
         '2F papers’ findings at :%d, the computations at relay data/b616_arith.txt; the consolidation, six acts in order, at :%d.' % (
             rl['weight'], rl['correction'], rl['fact'], rl['consolidation']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the document answers the census’s R17 (FINDINGS :7212, b610’s §2) and closes the sequence '
         'b610 entered (OPEN_TRAILS :12566), following b611’s to b615’s syntheses (:7240, :7260, :7280, :7300, :7322); its one route meets b609’s '
         'RH-60 (:7186), as the 2B, 2D and 2F syntheses’ did, and its cosmology claims meet the sieve’s MC-01; its kernel legs are the cosmology '
         'cluster’s definitional species b614 read for 2D. It strengthens the programme’s offering of the cosmology cluster: seven papers and two '
         'simulators now have one place where each claim stands at its own grade, the registered search is read on its bank, and the sieve’s '
         'next version has its work-list from all six syntheses in one bank.', '',
         '**Next.** Per `(R226)`(5): b617, the sieve’s v0.5, as the consolidation’s first act. The author rules on the closing.', '',
         '*Nothing deposits; no paper or simulator of the cluster edited; README, REGISTRY and the census unwritten; nothing here is a statement '
         'about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
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
    put_json('b616_findings.json', dict(entry_line=Q.line_of(Q.FIND, t[:90]), title=t, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, t[:90]))


def _trail_text():
    S, fj, rl = jl('b616_scores.json'), jl('b616_findings.json'), _rl()
    RS = jl('b616_routes_for_sieve.json')
    rows_ = ['', TRAIL_HEAD, '',
             '**(R226) ratified.** (1) b615 at its weight, the readings confirmed, the doubled percent signs taking a dated line. (2) The 2F papers’ '
             'findings, fact items. (3) The synthesis for 2G, the sequence’s last; H50a-H50d. (4) The consolidation, six acts in order. (5) The act '
             'after: b617.', '',
             '**Entered:** FINDINGS.md:%d (b615’s weight), :%d (the entry, with its mutual-light line); OPEN_TRAILS :%d (the dated correction line, '
             'addressed to b614’s For-the-author line :12683), :%d (the 2F fact items, addressed to b615’s record :12705), :%d (the consolidation, '
             'addressed to the sequence’s form :12566); this record; PLACE-papers `%s`; relay data/%s, data/b616_arith.txt, '
             'data/b616_routes_for_sieve.txt.' % (rl['weight'], fj['entry_line'], rl['correction'], rl['fact'], rl['consolidation'], DOC, BANK), '',
             '**Resolved by the seat, for the author’s strike:** the kernel legs read as pins with no terminal; the registered T-seven run read '
             'computationally-verified on its bank (t7_results.json at SIDE-t7-topology-cmb 575a802, its working copy’s md5 the paper’s); the '
             'simulators’ claims graded by their text, no bank found; the routes listed for the sieve read as the route rows whose sieve column names '
             'no row, %d of them in three syntheses, deduplicated by the step each argues into %d conclusions; the consolidation addressed to the '
             'sequence’s form; the correction line appended at the ledger’s end and addressed to the line it corrects, the ledgers append-only. No '
             'prompt was put (relay data/b616_author_answers.txt).' % (RS['listed'], len(RS['conclusions'])), '',
             '**For the author:** %s.' % FOR_AUTHOR, '',
             '**b617 priced** (the consolidation’s first act, `(R226)`(4)(i)): the sieve’s v0.5 beside v0.4, taking the %d conclusions of relay '
             'data/b616_routes_for_sieve.txt as rows read through the five tests, each with its source syntheses, its head’s counts re-stated; one '
             'act, no Lean call.' % len(RS['conclusions']), '',
             '**Defects** (relay data/b616_defects.txt): %s.' % ('; '.join(DEFECT_SHORT) if DEFECT_SHORT else 'none recorded'), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R226)`(5), b617, the sieve’s v0.5; the author rules on the closing.', '',
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
    put_json('b616_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b616_trail.json')['line'])


def desk(*a):
    S = jl('b616_scores.json')
    NK, SK = ('N1', 'N2', 'N3', 'N4', 'N5'), ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b616 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H50a-H50d, (R226)(3).', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HKEYS]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **H50 : HOLDS %d ; REFUTED %d.** ### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d ; '
          'REFUTED %d.**' % (sum(S[k][0] == 'HOLDS' for k in HKEYS), sum(S[k][0] == 'REFUTED' for k in HKEYS), sum(S[k][0] == 'HELD' for k in NK),
                             sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK), sum(S[k][0] == 'HELD' for k in SK),
                             sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b616_defects.txt').rstrip(NL).split(NL)
    put_txt('b616_desk_notes.txt', L)


def components(*a):
    S, fj, tj, rl = jl('b616_scores.json'), jl('b616_findings.json'), jl('b616_trail.json'), _rl()
    Z, X = jl('b616_page_zeta.json'), jl('b616_page_chi.json')
    RS = jl('b616_routes_for_sieve.json')
    L = ['b616 -- THE COMPONENTS, BANKED UNDER (R226).', '',
         '### COMPONENT 0 : the process listing (no orphan at step zero) ; b615`s closing push-out relay %s ; push-b615* branches deleted by name '
         '(data/b616_branches.txt) ; the kept branches untouched ; b615`s figures printed from its banks (data/b616_reads.txt) ; the suite run at '
         'HEAD before the face (data/b616_arms_prerun.txt)' % STEPZERO,
         '### COMPONENT 1 : b615`s weight FINDINGS :%d ; the dated correction line OPEN_TRAILS :%d ; the 2F fact items :%d ; the consolidation :%d ; '
         'the arithmetic data/b616_arith.txt' % (rl['weight'], rl['correction'], rl['fact'], rl['consolidation']),
         '### COMPONENT 2 : the claim bank data/%s ; routes %s ; H50c %s' % (BANK, ', '.join(jl('b616_claims.json')['routes']), S['H50c'][0]),
         '### COMPONENT 3 : the document %s ; data/b616_doc_bank.txt ; H50a %s, H50b %s, H50d %s' % (DOC, S['H50a'][0], S['H50b'][0], S['H50d'][0]),
         '### COMPONENT 4 : the six syntheses and the routes for the sieve data/b616_routes_for_sieve.txt -- %d listed rows, %d conclusions' % (
             RS['listed'], len(RS['conclusions'])),
         '### COMPONENT 5 : the ζ page changed %s, the χ page changed %s ; page arms data/b616_page_arms_c2.txt' % (Z.get('changed'), X.get('changed')),
         '### COMPONENT 6 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b617 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b616_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b616_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
